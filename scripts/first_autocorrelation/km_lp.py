"""Linear programming iteration for the non-negative autoconvolution problem.

Given a current ``f ≥ 0`` with ``M = max(f*f)``, solve

    max 1ᵀb  s.t.  (f*b)_k ≤ M ∀k,  b ≥ 0

and update ``f`` in the direction of the LP optimum. Iterate until the LP
returns a ratio ``1ᵀb* / 1ᵀf ≈ 1`` (fixed point of the linearized iteration).

Includes two modes:
- ``dense``: full sparse Toeplitz LP with all ``2n-1`` constraints.
- ``cutting-plane``: lazy constraint generation starting from the
  currently-active rows, adding violated ones after each LP solve.

Usage:
    uv run python scripts/first_autocorrelation/km_lp.py \\
        --warmstart PATH --n N --max-iters K --out OUTPUT
"""

from __future__ import annotations

import argparse
import json
import time
from pathlib import Path

import cvxpy as cp
import numpy as np
import scipy.sparse as sp

from einstein.first_autocorrelation.evaluator import verify_and_compute


# ----------------------------------------------------------------------------
# Warmstart helpers
# ----------------------------------------------------------------------------

def load_warmstart(path: Path) -> np.ndarray:
    with open(path) as fh:
        d = json.load(fh)
    return np.array(d["values"], dtype=np.float64)


def block_average(f: np.ndarray, n_target: int) -> np.ndarray:
    """Downsample f from len n_src to n_target by block-averaging.

    Requires n_src % n_target == 0. Preserves sum(f)/n (the density).
    """
    n_src = len(f)
    assert n_src % n_target == 0, f"{n_src} not divisible by {n_target}"
    block = n_src // n_target
    return f.reshape(n_target, block).mean(axis=1)


def block_sum(f: np.ndarray, n_target: int) -> np.ndarray:
    """Downsample f by summing consecutive blocks. Preserves total L¹ mass
    and (approximately) the spike structure better than block-averaging when
    downsampling a spiky function.
    """
    n_src = len(f)
    assert n_src % n_target == 0, f"{n_src} not divisible by {n_target}"
    block = n_src // n_target
    return f.reshape(n_target, block).sum(axis=1)


def block_repeat(f: np.ndarray, n_target: int) -> np.ndarray:
    """Upsample f from len n_src to n_target by block-repeating.

    Requires n_target % n_src == 0. Preserves C exactly.
    """
    n_src = len(f)
    assert n_target % n_src == 0, f"{n_target} not divisible by {n_src}"
    return np.repeat(f, n_target // n_src)


# ----------------------------------------------------------------------------
# Toeplitz assembly
# ----------------------------------------------------------------------------

def build_toeplitz_sparse(f: np.ndarray, threshold: float = 0.0) -> sp.csr_matrix:
    """Build sparse T with T[k, j] = f[k-j] for k in [0, 2n-2], j in [0, n-1].

    Entries with |f[d]| ≤ threshold are dropped (d = k-j).
    """
    n = len(f)
    m = 2 * n - 1
    idx_nz = np.where(np.abs(f) > threshold)[0]
    if len(idx_nz) == 0:
        return sp.csr_matrix((m, n))
    vals_nz = f[idx_nz]

    rows_list = []
    cols_list = []
    vals_list = []
    j_range = np.arange(n)
    for d, v in zip(idx_nz, vals_nz):
        k = j_range + int(d)
        rows_list.append(k)
        cols_list.append(j_range)
        vals_list.append(np.full(n, v, dtype=np.float64))
    rows = np.concatenate(rows_list)
    cols = np.concatenate(cols_list)
    vals = np.concatenate(vals_list)
    return sp.csr_matrix((vals, (rows, cols)), shape=(m, n))


# ----------------------------------------------------------------------------
# KM LP step — dense (sparse Toeplitz with all 2n-1 constraints)
# ----------------------------------------------------------------------------

def km_lp_step(f: np.ndarray, solver: str, threshold: float, verbose: bool):
    """Solve one KM LP. Returns (b_star, info_dict)."""
    n = len(f)
    auto = np.convolve(f, f, mode="full")
    M = float(auto.max())
    s0 = float(f.sum())

    t_build = time.time()
    T = build_toeplitz_sparse(f, threshold=threshold)
    t_build = time.time() - t_build

    # cvxpy LP
    b = cp.Variable(n, nonneg=True)
    constraints = [T @ b <= M]
    prob = cp.Problem(cp.Maximize(cp.sum(b)), constraints)

    t_solve = time.time()
    prob.solve(solver=solver, verbose=verbose)
    t_solve = time.time() - t_solve

    b_val = np.asarray(b.value, dtype=np.float64) if b.value is not None else None
    s_star = float(b_val.sum()) if b_val is not None else float("nan")

    return b_val, {
        "M": M,
        "s0": s0,
        "s_star": s_star,
        "ratio": s_star / s0 if s0 > 0 else float("nan"),
        "T_shape": T.shape,
        "T_nnz": int(T.nnz),
        "build_time": t_build,
        "solve_time": t_solve,
        "status": prob.status,
    }


# ----------------------------------------------------------------------------
# KM LP step — cutting plane (active set only)
# ----------------------------------------------------------------------------

def fft_conv(f: np.ndarray, b: np.ndarray) -> np.ndarray:
    """Compute f★b (full convolution) via rfft. Returns length 2n-1 array."""
    n = len(f)
    m = 2 * n - 1
    m_pad = 1 << (m - 1).bit_length()
    F = np.fft.rfft(f, n=m_pad)
    B = np.fft.rfft(b, n=m_pad)
    return np.fft.irfft(F * B, n=m_pad)[:m]


def build_active_toeplitz_csr(f: np.ndarray, active_k: list[int]) -> sp.csr_matrix:
    """Directly build sparse CSR Toeplitz restricted to `active_k` rows.

    Avoids the O(|S|·n) dense intermediate. For each row i with row-index
    k = active_k[i], the nonzero columns j are in [max(0, k-n+1), min(n-1, k)]
    with values f[k-j]. But we still want to drop j where f[k-j] == 0 for
    sparsity. Here we keep all j (f may be nonzero throughout).
    """
    n = len(f)
    S = len(active_k)

    # Precompute per-row bounds and total nnz
    rows_list = []
    cols_list = []
    vals_list = []
    for i, k in enumerate(active_k):
        j_lo = max(0, k - (n - 1))
        j_hi = min(n - 1, k)
        width = j_hi - j_lo + 1
        j = np.arange(j_lo, j_hi + 1)
        v = f[k - j]
        # Drop zeros for sparsity in case f has exact-zero cells
        nz = v != 0.0
        if not nz.all():
            j = j[nz]
            v = v[nz]
        rows_list.append(np.full(len(j), i, dtype=np.int32))
        cols_list.append(j.astype(np.int32))
        vals_list.append(v)

    rows = np.concatenate(rows_list)
    cols = np.concatenate(cols_list)
    vals = np.concatenate(vals_list)
    return sp.csr_matrix((vals, (rows, cols)), shape=(S, n))


def km_lp_step_cutting_plane(
    f: np.ndarray,
    solver: str,
    verbose: bool = False,
    init_rel_tol: float = 1e-10,
    init_top_k: int = 100,
    max_rounds: int = 50,
    max_new_cuts: int = 2000,
    bound_scale: float = 10.0,
):
    """KM LP via cutting plane / lazy constraint generation.

    Start with a generous active set (all k within init_rel_tol of M, or top
    init_top_k by (f*f)_k, whichever is larger). Solve the small LP, compute
    (f*b*) at all k via FFT, add any violated rows, re-solve. Repeat until no
    new violations.

    Bounding: adds 1ᵀb ≤ bound_scale · s0 to keep the LP bounded even if the
    initial constraint set is too loose.
    """
    n = len(f)
    auto_ff = np.convolve(f, f, mode="full")
    M = float(auto_ff.max())
    s0 = float(f.sum())

    # Initial active set: all k within init_rel_tol of M, OR top init_top_k
    mask_near = auto_ff >= (1.0 - init_rel_tol) * M
    k_near = list(np.where(mask_near)[0])
    k_topk = list(np.argsort(-auto_ff)[:init_top_k])
    active_k = sorted(set(k_near) | set(k_topk))
    print(
        f"  initial active set: |S|={len(active_k)}  "
        f"(|near-M|={len(k_near)}  top_k={init_top_k})",
        flush=True,
    )

    t_build_total = 0.0
    t_solve_total = 0.0
    rounds = 0
    cuts_added = 0
    b_val = None
    status = None

    for rnd in range(max_rounds):
        rounds += 1
        t0 = time.time()
        A = build_active_toeplitz_csr(f, active_k)
        t_build_total += time.time() - t0
        if verbose:
            print(
                f"  round {rnd+1} build: A {A.shape}, nnz={A.nnz}, "
                f"built in {time.time()-t0:.2f}s",
                flush=True,
            )

        b = cp.Variable(n, nonneg=True)
        constraints = [A @ b <= M, cp.sum(b) <= bound_scale * s0]
        prob = cp.Problem(cp.Maximize(cp.sum(b)), constraints)
        t0 = time.time()
        prob.solve(solver=solver, verbose=verbose)
        t_solve_total += time.time() - t0
        status = prob.status
        if b.value is None:
            break
        b_val = np.asarray(b.value, dtype=np.float64)

        # Check all constraints for violations via FFT
        fb = fft_conv(f, b_val)
        viol = fb - M
        # Find indices where viol > tolerance and not already in active set
        active_set = set(active_k)
        cand = np.where(viol > 1e-12 * M)[0]
        new_k = [int(k) for k in cand if int(k) not in active_set]
        print(
            f"  round {rnd+1}: |S|={len(active_k)}  s*={b_val.sum():.6f}  "
            f"status={status}  n_violated={len(new_k)}"
            + (f"  max_viol={viol[new_k].max():.3e}" if len(new_k) > 0 else "  — DONE"),
            flush=True,
        )
        # Sort by violation, take top-K
        if len(new_k) == 0:
            break
        viol_new = viol[new_k]
        order = np.argsort(-viol_new)[:max_new_cuts]
        new_k_sorted = [new_k[i] for i in order]
        active_k.extend(new_k_sorted)
        cuts_added += len(new_k_sorted)

    s_star = float(b_val.sum()) if b_val is not None else float("nan")
    return b_val, {
        "M": M,
        "s0": s0,
        "s_star": s_star,
        "ratio": s_star / s0 if s0 > 0 else float("nan"),
        "|S|": len(active_k),
        "rounds": rounds,
        "cuts_added": cuts_added,
        "build_time": t_build_total,
        "solve_time": t_solve_total,
        "status": status,
    }


# ----------------------------------------------------------------------------
# Line search along f + ε·b
# ----------------------------------------------------------------------------

def line_search(f: np.ndarray, b: np.ndarray, verbose: bool = False):
    """Grid-search ε ∈ geometric for the minimum C(f + ε·b).

    Returns (best_eps, best_f, best_C).
    """
    base_C = float(verify_and_compute((f / f.sum()).tolist()))
    best_eps = 0.0
    best_f = f / f.sum()
    best_C = base_C

    eps_grid = np.concatenate([
        [0.0],
        np.geomspace(1e-8, 1e-1, 32),
        np.geomspace(1e-1, 1e2, 16),
    ])

    for eps in eps_grid:
        f_new = f + eps * b
        s = f_new.sum()
        if s <= 0 or np.any(f_new < 0):
            continue
        try:
            c = float(verify_and_compute((f_new / s).tolist()))
        except Exception:
            continue
        if c < best_C - 1e-16:
            best_C = c
            best_eps = float(eps)
            best_f = f_new / s
        if verbose and eps in (0.0, 1e-6, 1e-3, 1.0, 100.0):
            print(f"    eps={eps:.2e}  C={c:.16f}")

    return best_eps, best_f, best_C


# ----------------------------------------------------------------------------
# Main iteration loop
# ----------------------------------------------------------------------------

def km_iterate(
    f0: np.ndarray,
    max_iters: int,
    solver: str,
    threshold: float,
    verbose_lp: bool,
    mode: str = "dense",
    cp_max_rounds: int = 50,
    cp_max_new_cuts: int = 500,
):
    """Run KM iteration until no improvement. mode ∈ {"dense", "cutting-plane"}."""
    f = f0 / f0.sum()  # start normalized
    base_C = float(verify_and_compute(f.tolist()))
    best_C = base_C
    best_f = f.copy()
    history = [{"iter": 0, "C": base_C, "s": float(f.sum()), "eps": 0.0, "s_star": None}]
    print(f"[iter 0] C = {base_C:.16f}  sum(f) = {f.sum():.6f}  mode={mode}", flush=True)

    for it in range(1, max_iters + 1):
        if mode == "dense":
            b_star, info = km_lp_step(f, solver=solver, threshold=threshold, verbose=verbose_lp)
        elif mode == "cutting-plane":
            b_star, info = km_lp_step_cutting_plane(
                f, solver=solver, verbose=verbose_lp,
                max_rounds=cp_max_rounds, max_new_cuts=cp_max_new_cuts,
            )
        else:
            raise ValueError(f"unknown mode: {mode}")
        size_str = (
            f"nnz={info['T_nnz']}" if "T_nnz" in info
            else f"|S|={info.get('|S|', '?')} rounds={info.get('rounds', '?')} cuts={info.get('cuts_added', '?')}"
        )
        print(
            f"[iter {it}] LP: M={info['M']:.6e}  s0={info['s0']:.6f}  "
            f"s*={info['s_star']:.6f}  ratio={info['ratio']:.6f}  "
            f"{size_str}  build={info['build_time']:.2f}s  "
            f"solve={info['solve_time']:.2f}s  status={info['status']}",
            flush=True,
        )
        if b_star is None or info["status"] not in ("optimal", "optimal_inaccurate"):
            print(f"  solver failed: {info['status']}", flush=True)
            break
        # line-search along f + eps*b
        eps, f_new, C_new = line_search(f, b_star, verbose=False)
        print(f"  line-search: best_eps={eps:.3e}  C_new={C_new:.16f}  delta={best_C - C_new:+.3e}", flush=True)
        history.append({
            "iter": it, "C": C_new, "s": float(f_new.sum()),
            "eps": eps, "s_star": info["s_star"],
        })
        if C_new < best_C - 1e-15:
            best_C = C_new
            best_f = f_new.copy()
            f = f_new.copy()
        else:
            print("  no improvement — LP fixed point reached")
            break

    return best_f, best_C, history


# ----------------------------------------------------------------------------
# Triple-verify
# ----------------------------------------------------------------------------

def triple_verify(f: np.ndarray) -> dict:
    """Cross-check C on the SAME f via three independent methods at 1 ulp.

    1. np.convolve (arena method, exact)
    2. FFT-based autoconvolution (different numerical path)
    3. scipy.signal.fftconvolve (different FFT backend + padding strategy)
    """
    from scipy.signal import fftconvolve

    n = len(f)
    dx = 0.5 / n
    denom = (f.sum() * dx) ** 2

    # Method 1: np.convolve (arena verifier)
    c1 = float(verify_and_compute(f.tolist()))

    # Method 2: FFT-based via np.fft.rfft
    m = 2 * n - 1
    m_pad = 1 << (m - 1).bit_length()
    F = np.fft.rfft(f.astype(np.float64), n=m_pad)
    auto_fft = np.fft.irfft(F * F, n=m_pad)[:m]
    c2 = float(auto_fft.max() * dx / denom)

    # Method 3: scipy.signal.fftconvolve (different FFT backend)
    auto_scipy = fftconvolve(f, f, mode="full")
    c3 = float(auto_scipy.max() * dx / denom)

    eps = 2.220446049250313e-16
    max_c = max(c1, c2, c3)
    return {
        "np_convolve": c1,
        "np_rfft": c2,
        "scipy_fftconvolve": c3,
        "ulp_diff_12": abs(c1 - c2) / (eps * max_c),
        "ulp_diff_13": abs(c1 - c3) / (eps * max_c),
        "ulp_diff_23": abs(c2 - c3) / (eps * max_c),
    }


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--warmstart", type=Path, required=True)
    p.add_argument("--n", type=int, default=None,
                   help="Target n (downsample/upsample warmstart if needed)")
    p.add_argument("--downsample", choices=["avg", "sum"], default="sum",
                   help="Block downsample method (sum preserves L¹, better for spikes)")
    p.add_argument("--max-iters", type=int, default=20)
    p.add_argument("--solver", default="CLARABEL",
                   choices=["CLARABEL", "HIGHS", "SCS", "OSQP", "SCIPY"])
    p.add_argument("--mode", default="dense",
                   choices=["dense", "cutting-plane"],
                   help="dense: full sparse Toeplitz LP. cutting-plane: lazy constraint generation.")
    p.add_argument("--threshold", type=float, default=0.0,
                   help="Drop |f[d]| ≤ threshold from Toeplitz (dense mode)")
    p.add_argument("--cp-max-rounds", type=int, default=50)
    p.add_argument("--cp-max-new-cuts", type=int, default=500)
    p.add_argument("--verbose-lp", action="store_true")
    p.add_argument("--out", type=Path, default=None)
    args = p.parse_args()

    print(f"Warmstart: {args.warmstart}")
    f_in = load_warmstart(args.warmstart)
    print(f"Input n = {len(f_in)}  sum = {f_in.sum():.6f}")

    if args.n is not None and args.n != len(f_in):
        if len(f_in) % args.n == 0:
            if args.downsample == "sum":
                f0 = block_sum(f_in, args.n)
                print(f"Downsampled {len(f_in)} -> {args.n} via block-sum")
            else:
                f0 = block_average(f_in, args.n)
                print(f"Downsampled {len(f_in)} -> {args.n} via block-avg")
        elif args.n % len(f_in) == 0:
            f0 = block_repeat(f_in, args.n)
            print(f"Upsampled {len(f_in)} -> {args.n} via block repeat")
        else:
            raise SystemExit(f"n={args.n} not compatible with input n={len(f_in)}")
    else:
        f0 = f_in.copy()

    base_C = float(verify_and_compute((f0 / f0.sum()).tolist()))
    print(f"Starting C at n={len(f0)}: {base_C:.16f}")

    best_f, best_C, history = km_iterate(
        f0, max_iters=args.max_iters, solver=args.solver,
        threshold=args.threshold, verbose_lp=args.verbose_lp,
        mode=args.mode,
        cp_max_rounds=args.cp_max_rounds,
        cp_max_new_cuts=args.cp_max_new_cuts,
    )

    print(f"\n=== FINAL ===")
    print(f"Best C = {best_C:.16f}")

    # Triple-verify final
    print("\n=== TRIPLE VERIFY ===")
    tv = triple_verify(best_f)
    for k, v in tv.items():
        print(f"  {k}: {v}")

    if args.out:
        args.out.parent.mkdir(parents=True, exist_ok=True)
        with open(args.out, "w") as fh:
            json.dump({
                "values": best_f.tolist(),
                "score": best_C,
                "n": len(best_f),
                "warmstart": str(args.warmstart),
                "history": history,
                "triple_verify": tv,
            }, fh)
        print(f"\nSaved: {args.out}")


if __name__ == "__main__":
    main()
