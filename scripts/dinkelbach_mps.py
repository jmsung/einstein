"""Dinkelbach optimizer on Apple MPS (M4 GPU) for n=100,000.

Maximizes C = ||f*f||_2^2 / (||f*f||_1 * ||f*f||_inf) over non-negative f.

Strategy:
1. GPU-accelerated L-BFGS at LOW beta (1e2-1e3) where float32 gradients are
   still informative — moves the solution in "coarse" directions.
2. CPU float64 L-BFGS refinement at high beta for precision.
3. Perturbation search: random perturbations scored with GPU FFT.

Key MPS adaptations:
- float32 on GPU (MPS does not support float64)
- Final verification on CPU with float64
- Lower beta values for float32 numerical stability
"""

import json
import sys
import time
from pathlib import Path

import numpy as np
import torch
from scipy.optimize import minimize
from scipy.signal import fftconvolve

sys.path.insert(0, "src")
from einstein.autocorrelation import evaluate
from einstein.autocorrelation_fast import diagnose, fast_evaluate, score_from_conv

RESULTS_DIR = Path("results")
RESULTS_DIR.mkdir(exist_ok=True)

DEVICE = "mps"
GPU_DTYPE = torch.float32


# ---------------------------------------------------------------------------
# Scoring helpers
# ---------------------------------------------------------------------------
def save_result(f, score, tag=""):
    """Save result to JSON."""
    result = {
        "problem": "second-autocorrelation-inequality",
        "n_points": len(f),
        "score": score,
        "values": f.tolist() if isinstance(f, np.ndarray) else f,
        "tag": tag,
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%S"),
    }
    fname = RESULTS_DIR / f"c2_n{len(f)}_{score:.8f}_{tag}.json"
    with open(fname, "w") as fh:
        json.dump(result, fh)
    print(f"  Saved to {fname}")
    return fname


def cpu_score_f64(f_np):
    """Exact C(f) on CPU in float64 — matches arena verifier."""
    return evaluate({"values": f_np.tolist()})


# ---------------------------------------------------------------------------
# GPU-accelerated Dinkelbach inner solver (float32)
# ---------------------------------------------------------------------------
def dinkelbach_inner_mps(f_np, lam, beta=1e3, n_inner=1000):
    """One Dinkelbach inner problem via L-BFGS on MPS GPU (float32).

    Best for low beta (1e2-1e3) where float32 gradients are informative.
    """
    w = np.sqrt(np.maximum(f_np, 0.0)).astype(np.float32)
    n = len(w)
    nc = 2 * n - 1
    nfft = 1
    while nfft < nc:
        nfft <<= 1

    w_t = torch.tensor(w, dtype=GPU_DTYPE, device=DEVICE).requires_grad_(True)
    best_w = w_t.data.clone()
    best_C = 0.0
    eval_count = 0

    optimizer = torch.optim.LBFGS(
        [w_t],
        lr=1.0,
        max_iter=n_inner,
        line_search_fn="strong_wolfe",
        tolerance_grad=1e-7,
        tolerance_change=1e-8,
    )

    zero = torch.zeros(1, device=DEVICE, dtype=GPU_DTYPE)

    def closure():
        nonlocal best_w, best_C, eval_count
        optimizer.zero_grad()
        f = w_t ** 2

        F = torch.fft.rfft(f, n=nfft)
        conv = torch.fft.irfft(F * F, n=nfft)[:nc]
        conv = torch.maximum(conv, zero)

        # Simpson-rule L2^2
        h = 1.0 / (nc + 1)
        z = torch.zeros(1, device=DEVICE, dtype=GPU_DTYPE)
        y = torch.cat([z, conv, z])
        y0, y1 = y[:-1], y[1:]
        l2sq = (h / 3.0) * torch.sum(y0 ** 2 + y0 * y1 + y1 ** 2)

        l1 = torch.sum(conv) / (nc + 1)

        # Smooth Linf via LogSumExp
        g_max = torch.max(conv)
        lse_arg = beta * (conv / (g_max + 1e-12) - 1.0)
        linf_proxy = g_max * torch.exp(
            torch.logsumexp(lse_arg, dim=0) / beta
        )

        obj = l2sq - lam * l1 * linf_proxy

        C_exact = l2sq.item() / (l1.item() * g_max.item()) if (l1.item() > 0 and g_max.item() > 0) else 0.0
        eval_count += 1
        if C_exact > best_C and C_exact < 1.5:
            best_C = C_exact
            best_w = w_t.data.clone()

        loss = -obj
        loss.backward()
        return loss

    try:
        optimizer.step(closure)
    except Exception as e:
        print(f"    L-BFGS MPS exception: {e}")

    f_new = (best_w ** 2).cpu().numpy().astype(np.float64)
    C_new = fast_evaluate(f_new)
    return f_new, C_new, eval_count


# ---------------------------------------------------------------------------
# CPU float64 Dinkelbach inner solver (scipy L-BFGS-B)
# ---------------------------------------------------------------------------
def dinkelbach_obj_and_grad_cpu(w, lam, beta, n):
    """Compute Dinkelbach objective and gradient on CPU float64."""
    f = w * w
    if np.sum(f) < 1e-30:
        return 0.0, np.zeros_like(w)

    conv = fftconvolve(f, f, mode="full")
    if not np.all(np.isfinite(conv)):
        return 1e30, np.zeros_like(w)

    sum_c2 = np.sum(conv * conv)
    sum_cc = np.sum(conv[:-1] * conv[1:])
    numer = 2.0 * sum_c2 + sum_cc

    c_sum = np.sum(conv)
    c_max = np.max(conv)

    # LogSumExp smooth max
    if c_max <= 0:
        return 0.0, np.zeros_like(w)
    z = np.clip(beta * (conv / c_max - 1.0), -700, 0)
    exp_z = np.exp(z)
    nc = len(conv)
    mean_exp_z = np.sum(exp_z) / nc
    if mean_exp_z <= 0:
        return 0.0, np.zeros_like(w)
    proxy_max = c_max * mean_exp_z ** (1.0 / beta)
    d_proxy_dc = mean_exp_z ** (1.0 / beta - 1.0) * exp_z / nc

    denom_proxy = 3.0 * c_sum * proxy_max
    if not np.isfinite(numer) or not np.isfinite(denom_proxy):
        return 1e30, np.zeros_like(w)

    phi = numer - lam * denom_proxy
    obj = -phi

    dnumer_dc = 4.0 * conv.copy()
    dnumer_dc[1:] += conv[:-1]
    dnumer_dc[:-1] += conv[1:]

    ddenom_dc = 3.0 * (proxy_max + c_sum * d_proxy_dc)
    dphi_dc = dnumer_dc - lam * ddenom_dc

    dphi_df = 2.0 * fftconvolve(dphi_dc, f[::-1], mode="full")
    dphi_df = dphi_df[n - 1: 2 * n - 1]

    dobj_dw = -dphi_df * 2.0 * w
    dobj_dw = np.clip(dobj_dw, -1e15, 1e15)
    dobj_dw = np.nan_to_num(dobj_dw, nan=0.0)

    return obj, dobj_dw


def optimize_cpu_lbfgs(f_init, betas, n_outer=3, maxiter=500, time_limit=60, verbose=True):
    """CPU float64 Dinkelbach + L-BFGS-B (high precision)."""
    n = len(f_init)
    f = np.maximum(f_init, 0.0).copy()
    w = np.sqrt(f)
    best_f = f.copy()
    best_score = fast_evaluate(f)
    t0 = time.time()

    conv = fftconvolve(f, f, mode="full")
    lam = score_from_conv(conv)

    for beta in betas:
        if time.time() - t0 > time_limit:
            break
        for outer in range(n_outer):
            if time.time() - t0 > time_limit:
                break

            def obj_grad(w_flat, _lam=lam, _beta=beta):
                return dinkelbach_obj_and_grad_cpu(w_flat, _lam, _beta, n)

            result = minimize(
                obj_grad, w, method="L-BFGS-B", jac=True,
                options={"maxiter": maxiter, "maxfun": maxiter * 3,
                         "ftol": 1e-15, "gtol": 1e-12, "maxls": 40},
            )
            w = result.x
            f_current = w * w

            conv = fftconvolve(f_current, f_current, mode="full")
            score = score_from_conv(conv)
            lam = score

            if score > best_score:
                best_score = score
                best_f = f_current.copy()
                if verbose:
                    print(f"    CPU beta={beta:.0e} outer={outer+1}: "
                          f"C={score:.13f} *** NEW BEST")
            elif verbose:
                print(f"    CPU beta={beta:.0e} outer={outer+1}: "
                      f"C={score:.13f}")

            if result.nit <= 1:
                break

    return best_f, best_score


# ---------------------------------------------------------------------------
# GPU-accelerated perturbation search
# ---------------------------------------------------------------------------
def perturb_search(f_init, n_trials=5000, time_limit=60, seed=42,
                   sigma=0.01, verbose=True):
    """Random perturbation search with fast CPU scoring.

    Perturbs support values and positions, scores with fast_evaluate.
    Uses adaptive perturbation sizes.
    """
    n = len(f_init)
    f_best = f_init.copy()
    C_best = fast_evaluate(f_best)
    t0 = time.time()
    rng = np.random.default_rng(seed)
    improved = 0
    stagnant = 0

    nz_idx = np.where(f_best > 1e-10)[0]
    n_nz = len(nz_idx)
    vals_nz = f_best[nz_idx]

    for trial in range(n_trials):
        if time.time() - t0 > time_limit:
            break

        # Adapt sigma: shrink when stagnant (exploit), grow occasionally (explore)
        if stagnant > 200:
            sigma *= 0.9
            stagnant = 0
        if trial % 500 == 0 and trial > 0:
            sigma = max(sigma, 0.001)

        f_trial = f_best.copy()
        move = rng.integers(8)

        if move == 0 and n_nz > 0:
            # Perturb a single support point value
            idx = rng.choice(nz_idx)
            f_trial[idx] *= np.exp(sigma * rng.standard_normal())

        elif move == 1 and n_nz > 0:
            # Perturb values of multiple support points
            k = min(rng.integers(2, max(3, n_nz // 20)), n_nz)
            idx = rng.choice(nz_idx, k, replace=False)
            factors = np.exp(sigma * rng.standard_normal(k))
            f_trial[idx] *= factors

        elif move == 2 and n_nz > 1:
            # Shift a support point
            idx = rng.choice(nz_idx)
            offset = rng.integers(-3, 4)
            new_idx = idx + offset
            if 0 <= new_idx < n and f_trial[new_idx] < 1e-10:
                f_trial[new_idx] = f_trial[idx]
                f_trial[idx] = 0.0

        elif move == 3:
            # Add a new support point near existing
            if n_nz > 0:
                base = rng.choice(nz_idx)
                offset = rng.integers(-5, 6)
                new_idx = base + offset
                if 0 <= new_idx < n and f_trial[new_idx] < 1e-10:
                    mean_val = np.mean(vals_nz)
                    f_trial[new_idx] = rng.exponential(mean_val * 0.05)

        elif move == 4 and n_nz > 5:
            # Remove a small support point
            probs = 1.0 / (vals_nz + 1e-10)
            probs /= probs.sum()
            idx = rng.choice(nz_idx, p=probs)
            f_trial[idx] = 0.0

        elif move == 5 and n_nz > 0:
            # Perturb a contiguous block of support
            base = rng.choice(nz_idx)
            width = rng.integers(1, 6)
            for offset in range(-width, width + 1):
                j = base + offset
                if 0 <= j < n and f_trial[j] > 1e-10:
                    f_trial[j] *= np.exp(sigma * 0.5 * rng.standard_normal())

        elif move == 6 and n_nz > 0:
            # Swap two support values
            if n_nz >= 2:
                i1, i2 = rng.choice(nz_idx, 2, replace=False)
                f_trial[i1], f_trial[i2] = f_trial[i2], f_trial[i1]

        elif move == 7 and n_nz > 0:
            # Tiny uniform perturbation of ALL nonzero values
            f_trial[nz_idx] *= np.exp(sigma * 0.1 * rng.standard_normal(n_nz))

        f_trial = np.maximum(f_trial, 0.0)
        C_trial = fast_evaluate(f_trial)

        if C_trial > C_best:
            C_best = C_trial
            f_best = f_trial
            nz_idx = np.where(f_best > 1e-10)[0]
            n_nz = len(nz_idx)
            vals_nz = f_best[nz_idx]
            improved += 1
            stagnant = 0
            if verbose and improved % 10 == 0:
                elapsed = time.time() - t0
                print(f"    trial={trial}: C={C_best:.13f} "
                      f"({improved} impr, sigma={sigma:.4f}, {elapsed:.1f}s)")
        else:
            stagnant += 1

    if verbose:
        elapsed = time.time() - t0
        print(f"    Done: C={C_best:.13f} "
              f"({improved} improvements in {trial+1} trials, {elapsed:.1f}s)")

    return f_best, C_best


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main():
    print("=" * 70)
    print("Dinkelbach MPS Optimizer — n=100,000 on Apple M4 GPU")
    print("=" * 70)
    t_start = time.time()

    # Load public best
    f_public = np.load("results/public_best_100k.npy").astype(np.float64)
    f_public = np.maximum(f_public, 0.0)
    C_public = fast_evaluate(f_public)
    nnz = np.count_nonzero(f_public > 1e-10)
    print(f"\n  Public best: C={C_public:.13f}, nnz={nnz}")

    f_best = f_public.copy()
    C_best = C_public

    # -----------------------------------------------------------------------
    # Phase 1: GPU L-BFGS at low beta (coarse moves in float32)
    # -----------------------------------------------------------------------
    print("\n--- Phase 1: MPS GPU L-BFGS (low beta, float32) ---")

    for beta in [100, 300, 1000]:
        if time.time() - t_start > 90:
            break
        lam = C_best
        f_new, C_new, n_evals = dinkelbach_inner_mps(
            f_best, lam, beta=beta, n_inner=500
        )
        if C_new > C_best and C_new < 1.0 and np.all(np.isfinite(f_new)):
            C_best = C_new
            f_best = f_new
            print(f"  beta={beta}: C={C_best:.13f} *** IMPROVED (evals={n_evals})")
        else:
            print(f"  beta={beta}: C={C_new:.13f} (evals={n_evals})")

    dt1 = time.time() - t_start
    print(f"\n  Phase 1: C={C_best:.13f} ({dt1:.1f}s)")

    # -----------------------------------------------------------------------
    # Phase 2: Perturbation search (main workhorse)
    # Multiple rounds with different seeds and sigma values
    # -----------------------------------------------------------------------
    print("\n--- Phase 2: Perturbation search ---")

    for rnd, (sigma, seed) in enumerate([
        (0.01, 42), (0.005, 123), (0.02, 456),
        (0.001, 789), (0.05, 1000), (0.003, 2000),
        (0.008, 3000), (0.015, 4000),
    ]):
        time_left = 480 - (time.time() - t_start)
        if time_left < 20:
            break
        rnd_time = min(60, time_left / max(1, 8 - rnd))
        print(f"\n  Round {rnd+1} (sigma={sigma}, seed={seed}, {rnd_time:.0f}s):")
        f_p, C_p = perturb_search(
            f_best, n_trials=20000, time_limit=rnd_time,
            seed=seed, sigma=sigma, verbose=True,
        )
        if C_p > C_best:
            C_best = C_p
            f_best = f_p
            print(f"  Round {rnd+1} improved: C={C_best:.13f}")

    dt2 = time.time() - t_start
    print(f"\n  Phase 2: C={C_best:.13f} ({dt2:.1f}s)")

    # -----------------------------------------------------------------------
    # Phase 3: CPU float64 L-BFGS refinement (if time permits)
    # -----------------------------------------------------------------------
    time_left = 520 - (time.time() - t_start)
    if time_left > 30:
        print(f"\n--- Phase 3: CPU float64 L-BFGS ({time_left:.0f}s) ---")
        betas_cpu = [1e5, 5e5, 1e6, 5e6]
        f_cpu, C_cpu = optimize_cpu_lbfgs(
            f_best, betas=betas_cpu, n_outer=3, maxiter=300,
            time_limit=time_left - 10, verbose=True,
        )
        if C_cpu > C_best:
            C_best = C_cpu
            f_best = f_cpu
            print(f"\n  Phase 3 improved: C={C_best:.13f}")
        else:
            print(f"\n  Phase 3: no improvement (C_cpu={C_cpu:.13f})")

    # -----------------------------------------------------------------------
    # Final verification
    # -----------------------------------------------------------------------
    print(f"\n{'='*70}")
    print("Final Verification")
    print(f"{'='*70}")

    arena_score = cpu_score_f64(f_best)
    fast_score = fast_evaluate(f_best)
    nnz = np.count_nonzero(f_best > 1e-10)

    print(f"  Fast evaluator:  C = {fast_score:.13f}")
    print(f"  Arena evaluator: C = {arena_score:.13f}")
    print(f"  n = {len(f_best)}, nonzero = {nnz}")

    d = diagnose(f_best)
    print(f"  Blocks: {d['n_blocks']}, mean width: {d['mean_block_width']:.1f}")
    print(f"  Conv std/mean: {d['conv_std_over_mean']:.4f}")

    # Save
    save_result(f_best, arena_score, "dinkelbach_mps")

    # Also save as npy for future warm-starting
    npy_path = RESULTS_DIR / f"dinkelbach_mps_n{len(f_best)}.npy"
    np.save(npy_path, f_best)

    total_time = time.time() - t_start
    print(f"\n  Total time: {total_time:.1f}s")

    improved = arena_score > C_public
    print(f"  Public best:  C = {C_public:.13f}")
    print(f"  Our result:   C = {arena_score:.13f}")
    print(f"  {'IMPROVED!' if improved else 'Matched or below public best.'}")
    print(f"  Delta: {arena_score - C_public:+.13f}")


if __name__ == "__main__":
    main()
