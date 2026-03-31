"""Dinkelbach + LogSumExp + L-BFGS optimizer for Problem 3 (PATH B).

Maximize C = (2*sum(c^2) + sum(c_i*c_{i+1})) / (3 * sum(c) * max(c))
where c = convolve(f, f, mode='full') and f >= 0.

Approach:
  - Cluster initialization (nc=15-40, cw=1-4 at n=2000)
  - Full-space Dinkelbach + L-BFGS with progressive beta annealing
  - Random perturbation restarts to escape local optima
  - Ultra-high beta refinement at the end
  - Iterative refinement with progressive beta annealing
"""

import sys

sys.path.insert(0, "src")

import json
import time
from pathlib import Path

import numpy as np
from scipy.optimize import minimize
from scipy.signal import fftconvolve

from einstein.autocorrelation import evaluate
from einstein.autocorrelation_fast import diagnose, fast_evaluate, score_from_conv

RESULTS_DIR = Path("results")
RESULTS_DIR.mkdir(exist_ok=True)


def save_result(f, score, tag=""):
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


def logsumexp_max_and_grad(c, beta):
    c_max_val = np.max(c)
    if c_max_val <= 0:
        return 0.0, np.zeros_like(c)
    z = np.clip(beta * (c / c_max_val - 1.0), -700, 0)
    exp_z = np.exp(z)
    nc = len(c)
    mean_exp_z = np.sum(exp_z) / nc
    if mean_exp_z <= 0:
        return c_max_val, np.zeros_like(c)
    proxy = c_max_val * mean_exp_z ** (1.0 / beta)
    grad = mean_exp_z ** (1.0 / beta - 1.0) * exp_z / nc
    return proxy, grad


def dinkelbach_obj_and_grad(w, lam, beta, n):
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
    proxy_max, d_proxy_dc = logsumexp_max_and_grad(conv, beta)
    denom_proxy = 3.0 * c_sum * proxy_max

    if not np.isfinite(numer) or not np.isfinite(denom_proxy):
        return 1e30, np.zeros_like(w)

    phi = numer - lam * denom_proxy

    dnumer_dc = 4.0 * conv.copy()
    dnumer_dc[1:] += conv[:-1]
    dnumer_dc[:-1] += conv[1:]
    ddenom_dc = 3.0 * (proxy_max + c_sum * d_proxy_dc)
    dphi_dc = dnumer_dc - lam * ddenom_dc

    dphi_df = 2.0 * fftconvolve(dphi_dc, f[::-1], mode="full")
    dphi_df = dphi_df[n - 1: 2 * n - 1]
    dobj_dw = -(-dphi_df * 2.0 * w)  # minimize -phi
    # Actually: obj = -phi, so dobj/dw = -dphi_df * 2w
    dobj_dw = dphi_df * (-2.0 * w)
    dobj_dw = np.clip(dobj_dw, -1e15, 1e15)
    dobj_dw = np.nan_to_num(dobj_dw, nan=0.0)
    return -phi, dobj_dw


def optimize_lbfgs(n, f_init, beta_schedule, outer_iters, maxiter_lbfgs, time_limit):
    f = np.maximum(f_init, 0.0).copy()
    s = np.sum(f)
    if s > 0:
        f *= n / s
    w = np.sqrt(f)
    best_f = f.copy()
    best_score = fast_evaluate(f)
    t0 = time.time()

    conv = fftconvolve(f, f, mode="full")
    lam = score_from_conv(conv)

    for beta in beta_schedule:
        if time.time() - t0 > time_limit:
            break
        for outer in range(outer_iters):
            if time.time() - t0 > time_limit:
                break

            result = minimize(
                lambda ww: dinkelbach_obj_and_grad(ww, lam, beta, n),
                w, method="L-BFGS-B", jac=True,
                options={"maxiter": maxiter_lbfgs, "maxfun": maxiter_lbfgs * 3,
                         "ftol": 1e-15, "gtol": 1e-10, "maxls": 40},
            )
            w = result.x
            f_current = w * w
            s = np.sum(f_current)
            if s > 0:
                f_current *= n / s
                w = np.sqrt(f_current)

            conv = fftconvolve(f_current, f_current, mode="full")
            score = score_from_conv(conv)
            lam = score

            if score > best_score:
                best_score = score
                best_f = f_current.copy()
            if result.nit <= 1:
                break
    return best_f, best_score


def cluster_init(n, nc, cw, rng):
    f = np.zeros(n)
    spacing = n // nc
    for c in range(nc):
        center = c * spacing + spacing // 2
        for offset in range(-cw, cw + 1):
            idx = center + offset
            if 0 <= idx < n:
                f[idx] = abs(1.0 + 0.3 * rng.standard_normal())
    return f


def perturb(f, sigma, rng):
    f_new = f.copy()
    n = len(f)
    mask = f_new > 1e-10
    nz_idx = np.where(mask)[0]
    n_nz = len(nz_idx)
    if n_nz == 0:
        return f_new
    f_new[mask] *= np.exp(sigma * rng.standard_normal(n_nz))
    f_new = np.maximum(f_new, 0.0)
    n_remove = max(1, int(0.05 * n_nz * (1 + sigma)))
    remove_idx = rng.choice(nz_idx, min(n_remove, n_nz), replace=False)
    f_new[remove_idx] = 0.0
    n_add = max(1, int(0.03 * n_nz * max(sigma, 0.1)))
    add_base = rng.choice(nz_idx, min(n_add, n_nz), replace=True)
    mean_val = np.mean(f_new[f_new > 1e-10]) if np.any(f_new > 1e-10) else 1.0
    for base in add_base:
        offset = rng.integers(-5, 6)
        idx = base + offset
        if 0 <= idx < n and f_new[idx] < 1e-10:
            f_new[idx] = rng.exponential(mean_val)
    return f_new


def main():
    print("=" * 60)
    print("Dinkelbach + LogSumExp + L-BFGS Optimizer (PATH B)")
    print("Target: C > 0.90 at n=2000")
    print("=" * 60)

    t_start = time.time()
    n = 2000
    rng = np.random.default_rng(42)

    # Phase 1: Multi-start with progressive beta
    print(f"\n--- Phase 1: Multi-start at n={n} ---")
    best_f = None
    best_score = 0.0

    # Start with gentle beta, then increase
    beta_warmup = (200, 1000, 5000, 50000, 500000)

    configs = [(nc, cw) for nc in [15, 20, 25, 30, 40, 50] for cw in [1, 2, 3, 4]]
    for nc, cw in configs:
        if time.time() - t_start > 50:
            break
        seed = rng.integers(100000)
        f_init = cluster_init(n, nc, cw, np.random.default_rng(seed))
        f, score = optimize_lbfgs(n, f_init, beta_warmup, 4, 300, time_limit=3)
        if score > best_score:
            best_score = score
            best_f = f.copy()
            nnz = np.count_nonzero(f > 1e-10)
            print(f"  cl_{nc}_w{cw}: C={score:.8f} nnz={nnz} *** BEST")

    print(f"  Phase 1 best: C={best_score:.8f}")

    # Phase 2: Deep optimization
    print(f"\n--- Phase 2: Deep optimization ---")
    beta_deep = (5000, 20000, 100000, 500000, 2000000)
    stale = 0

    for rnd in range(200):
        elapsed = time.time() - t_start
        if elapsed > 240:
            break

        if rnd == 0:
            f_start = best_f.copy()
        elif stale > 5:
            f_start = perturb(best_f, 0.5 + 0.5 * rng.random(), rng)
            stale = 0
        else:
            f_start = perturb(best_f, 0.05 + 0.3 * rng.random(), rng)

        f, score = optimize_lbfgs(n, f_start, beta_deep, 5, 500, time_limit=5)

        if score > best_score + 1e-6:
            best_score = score
            best_f = f.copy()
            stale = 0
            nnz = np.count_nonzero(f > 1e-10)
            print(f"  R{rnd+1}: C={score:.8f} nnz={nnz} *** NEW BEST")
        else:
            stale += 1
            if rnd % 10 == 0:
                print(f"  R{rnd+1}: C={score:.8f} (best={best_score:.8f})")

    print(f"\n  Phase 2 best: C={best_score:.8f}")
    save_result(best_f, best_score, "dinkelbach_n2000")

    # Phase 3: Ultra-high beta refinement
    print(f"\n--- Phase 3: Ultra-high beta ---")
    beta_ultra = (500000, 5000000, 50000000)
    for rnd in range(20):
        if time.time() - t_start > 275:
            break
        f_start = best_f.copy()
        if rnd > 0:
            mask = f_start > 1e-10
            if np.any(mask):
                f_start[mask] *= np.exp(0.03 * rng.standard_normal(np.sum(mask)))
                f_start = np.maximum(f_start, 0.0)
        f, score = optimize_lbfgs(n, f_start, beta_ultra, 8, 600, time_limit=3)
        if score > best_score + 1e-7:
            best_score = score
            best_f = f.copy()
            print(f"  R{rnd+1}: C={score:.8f} *** NEW BEST")

    # Final verification
    print(f"\n{'='*60}")
    print("Final Verification")
    print(f"{'='*60}")

    arena_score = evaluate({"values": best_f.tolist()})
    print(f"  Fast:  C={fast_evaluate(best_f):.10f}")
    print(f"  Arena: C={arena_score:.10f}")
    print(f"  n={len(best_f)}, nonzero={np.count_nonzero(best_f > 1e-10)}")

    d = diagnose(best_f)
    print(f"  Blocks: {d['n_blocks']}, mean width: {d['mean_block_width']:.1f}")
    print(f"  Conv std/mean: {d['conv_std_over_mean']:.4f}")

    save_result(best_f, arena_score, "dinkelbach_final")

    total_time = time.time() - t_start
    print(f"\n  Total time: {total_time:.1f}s")
    print(f"  {'TARGET MET (>0.90)!' if arena_score > 0.90 else 'Below target (0.90)'}")


if __name__ == "__main__":
    main()
