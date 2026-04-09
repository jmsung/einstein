"""LP iteration variant via ``scipy.optimize.linprog`` (HIGHS backend).

Same iteration as ``km_lp.py`` but calls scipy directly instead of going
through cvxpy, which avoids the cvxpy compilation cost on large sparse
problems.

At moderate ``n`` the full sparse Toeplitz LP with all ``2n-1`` constraints
fits in memory. ``scipy.optimize.linprog`` with ``'highs-ipm'``
(HiGHS interior-point crossover) is the default here.

Usage:
    uv run python scripts/first_autocorrelation/km_lp_scipy.py \\
        --warmstart PATH --n N --max-iters K --out OUT
"""

from __future__ import annotations

import argparse
import json
import time
from pathlib import Path

import numpy as np
import scipy.sparse as sp
from scipy.optimize import linprog

from einstein.first_autocorrelation.evaluator import verify_and_compute


# ----------------------------------------------------------------------------
# Warmstart loaders (shared with km_lp.py)
# ----------------------------------------------------------------------------

def load_warmstart(path: Path) -> np.ndarray:
    with open(path) as fh:
        d = json.load(fh)
    return np.array(d["values"], dtype=np.float64)


def block_sum(f: np.ndarray, n_target: int) -> np.ndarray:
    """Downsample by summing consecutive blocks. Preserves total L¹ mass."""
    n_src = len(f)
    assert n_src % n_target == 0
    block = n_src // n_target
    return f.reshape(n_target, block).sum(axis=1)


def block_average(f: np.ndarray, n_target: int) -> np.ndarray:
    n_src = len(f)
    assert n_src % n_target == 0
    block = n_src // n_target
    return f.reshape(n_target, block).mean(axis=1)


def block_repeat(f: np.ndarray, n_target: int) -> np.ndarray:
    n_src = len(f)
    assert n_target % n_src == 0
    return np.repeat(f, n_target // n_src)


# ----------------------------------------------------------------------------
# Sparse Toeplitz (full, all 2n-1 constraints)
# ----------------------------------------------------------------------------

def build_full_toeplitz_coo(f: np.ndarray, drop_tol: float = 0.0) -> sp.csr_matrix:
    """Build the full 2n-1 × n sparse Toeplitz T with T[k, j] = f[k-j].

    Uses COO construction with column-major iteration (fast for sparse f).
    Drops entries with |f| ≤ drop_tol.
    """
    n = len(f)
    m = 2 * n - 1

    # Identify significant indices in f
    if drop_tol > 0:
        idx_nz = np.where(np.abs(f) > drop_tol)[0]
    else:
        idx_nz = np.arange(n, dtype=np.int64)
    vals_nz = f[idx_nz]
    n_nz = len(idx_nz)

    # For each column j in [0, n), the nonzero rows are k = j + d for d in idx_nz
    # So row k = j + d, col j, val f[d]
    cols = np.repeat(np.arange(n, dtype=np.int64), n_nz)
    rows = np.tile(idx_nz, n) + cols
    vals = np.tile(vals_nz, n)

    return sp.csr_matrix((vals, (rows, cols)), shape=(m, n))


# ----------------------------------------------------------------------------
# KM LP step via scipy.linprog
# ----------------------------------------------------------------------------

def km_lp_step_scipy(
    f: np.ndarray,
    method: str,
    drop_tol: float,
    verbose: bool,
):
    n = len(f)
    auto = np.convolve(f, f, mode="full")
    M = float(auto.max())
    s0 = float(f.sum())

    t0 = time.time()
    T = build_full_toeplitz_coo(f, drop_tol=drop_tol)
    t_build = time.time() - t0
    if verbose:
        print(
            f"  Toeplitz: shape={T.shape}, nnz={T.nnz}, build={t_build:.2f}s",
            flush=True,
        )

    # LP: max 1ᵀb ⟺ min -1ᵀb
    c = -np.ones(n, dtype=np.float64)
    b_ub = np.full(2 * n - 1, M, dtype=np.float64)

    t0 = time.time()
    res = linprog(
        c,
        A_ub=T,
        b_ub=b_ub,
        bounds=(0, None),
        method=method,
        options={"disp": verbose, "presolve": True},
    )
    t_solve = time.time() - t0

    b_val = res.x if res.x is not None else None
    s_star = float(b_val.sum()) if b_val is not None else float("nan")

    return b_val, {
        "M": M,
        "s0": s0,
        "s_star": s_star,
        "ratio": s_star / s0 if s0 > 0 else float("nan"),
        "nnz": int(T.nnz),
        "build_time": t_build,
        "solve_time": t_solve,
        "status": res.status,
        "message": res.message,
        "success": res.success,
    }


# ----------------------------------------------------------------------------
# Line search
# ----------------------------------------------------------------------------

def line_search(f: np.ndarray, b: np.ndarray):
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

    return best_eps, best_f, best_C


# ----------------------------------------------------------------------------
# Iteration loop
# ----------------------------------------------------------------------------

def km_iterate(
    f0: np.ndarray,
    max_iters: int,
    method: str,
    drop_tol: float,
    verbose: bool,
):
    f = f0 / f0.sum()
    base_C = float(verify_and_compute(f.tolist()))
    best_C = base_C
    best_f = f.copy()
    print(f"[iter 0] C = {base_C:.16f}  sum(f) = {f.sum():.6f}", flush=True)

    for it in range(1, max_iters + 1):
        b_star, info = km_lp_step_scipy(f, method=method, drop_tol=drop_tol, verbose=verbose)
        print(
            f"[iter {it}] LP: nnz={info['nnz']} build={info['build_time']:.1f}s "
            f"solve={info['solve_time']:.1f}s success={info['success']} "
            f"s0={info['s0']:.6f} s*={info['s_star']:.6f} ratio={info['ratio']:.6f}",
            flush=True,
        )
        if b_star is None or not info["success"]:
            print(f"  solver failed: {info['message']}", flush=True)
            break
        eps, f_new, C_new = line_search(f, b_star)
        print(
            f"  line-search: best_eps={eps:.3e} C_new={C_new:.16f} "
            f"delta={best_C - C_new:+.3e}",
            flush=True,
        )
        if C_new < best_C - 1e-15:
            best_C = C_new
            best_f = f_new.copy()
            f = f_new.copy()
        else:
            print("  no improvement — LP fixed point reached", flush=True)
            break

    return best_f, best_C


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--warmstart", type=Path, required=True)
    p.add_argument("--n", type=int, default=None,
                   help="Target n (downsample warmstart via block-sum)")
    p.add_argument("--downsample", choices=["sum", "avg"], default="sum",
                   help="Downsample method: sum (preserves L¹) or avg")
    p.add_argument("--max-iters", type=int, default=20)
    p.add_argument("--method", default="highs-ipm",
                   choices=["highs", "highs-ds", "highs-ipm"])
    p.add_argument("--drop-tol", type=float, default=0.0,
                   help="Drop |f| < drop-tol when building Toeplitz (sparsify)")
    p.add_argument("--verbose", action="store_true")
    p.add_argument("--out", type=Path, default=None)
    args = p.parse_args()

    print(f"Warmstart: {args.warmstart}", flush=True)
    f_in = load_warmstart(args.warmstart)
    print(f"Input n={len(f_in)}, sum={f_in.sum():.6f}", flush=True)

    if args.n is not None and args.n != len(f_in):
        if len(f_in) % args.n == 0:
            if args.downsample == "sum":
                f0 = block_sum(f_in, args.n)
                print(f"Downsampled {len(f_in)}->{args.n} via block-sum", flush=True)
            else:
                f0 = block_average(f_in, args.n)
                print(f"Downsampled {len(f_in)}->{args.n} via block-avg", flush=True)
        elif args.n % len(f_in) == 0:
            f0 = block_repeat(f_in, args.n)
            print(f"Upsampled {len(f_in)}->{args.n} via block-repeat", flush=True)
        else:
            raise SystemExit(f"n={args.n} incompatible with input n={len(f_in)}")
    else:
        f0 = f_in.copy()

    base_C = float(verify_and_compute((f0 / f0.sum()).tolist()))
    print(f"Starting C at n={len(f0)}: {base_C:.16f}", flush=True)

    best_f, best_C = km_iterate(
        f0, max_iters=args.max_iters, method=args.method,
        drop_tol=args.drop_tol, verbose=args.verbose,
    )

    print(f"\n=== FINAL ===")
    print(f"Best C = {best_C:.16f}")

    if args.out:
        args.out.parent.mkdir(parents=True, exist_ok=True)
        with open(args.out, "w") as fh:
            json.dump({
                "values": best_f.tolist(),
                "score": best_C,
                "n": len(best_f),
                "warmstart": str(args.warmstart),
            }, fh)
        print(f"Saved: {args.out}")


if __name__ == "__main__":
    main()
