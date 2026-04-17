"""Optimize C2 at n=400k and n=800k via transplant + Dinkelbach refinement.

Strategy:
  1. Transplant 1.6M → target_n via average pooling
  2. Try multiple thresholds for active region detection
  3. Dinkelbach + L-BFGS refinement (CPU, float64)
  4. Also try warm-starting from ClaudeExplorer's 400k SOTA

Target: C > 0.96274 (to beat SOTA + minImprovement)
"""

import sys
sys.path.insert(0, "src")

import json
import time
from pathlib import Path

import numpy as np
from scipy.optimize import minimize
from scipy.signal import fftconvolve

from einstein.autocorrelation.fast import fast_evaluate, score_from_conv

RESULTS_DIR = Path("results/problem-3-autocorrelation")
RESULTS_DIR.mkdir(parents=True, exist_ok=True)

TARGET_SCORE = 0.96274  # SOTA + minImprovement


def transplant(f_source, target_n, active_threshold=0.0):
    """Average-pool source solution to target_n."""
    if active_threshold > 0:
        nz = np.nonzero(f_source > active_threshold)[0]
        f_active = f_source[nz[0]:nz[-1]+1]
    else:
        f_active = f_source

    source_n = len(f_active)
    f_target = np.zeros(target_n)
    for i in range(target_n):
        start = int(i * source_n / target_n)
        end = int((i + 1) * source_n / target_n)
        f_target[i] = np.mean(f_active[start:end])
    return f_target


def dinkelbach_obj_grad(w, lam, beta, n):
    """Dinkelbach objective and gradient for L-BFGS."""
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
    if c_sum <= 0 or c_max <= 0:
        return 0.0, np.zeros_like(w)

    nc = len(conv)
    z = np.clip(beta * (conv / c_max - 1.0), -700, 0)
    exp_z = np.exp(z)
    mean_exp = np.sum(exp_z) / nc
    proxy = c_max * mean_exp ** (1.0 / beta)
    d_proxy_dc = mean_exp ** (1.0 / beta - 1.0) * exp_z / nc

    denom_val = 3.0 * c_sum * proxy
    phi = numer - lam * denom_val

    dn_dc = 4.0 * conv.copy()
    dn_dc[1:] += conv[:-1]
    dn_dc[:-1] += conv[1:]
    dd_dc = 3.0 * (proxy + c_sum * d_proxy_dc)
    dphi_dc = dn_dc - lam * dd_dc

    dphi_df = 2.0 * fftconvolve(dphi_dc, f[::-1], mode="full")
    dphi_df = dphi_df[n - 1: 2 * n - 1]

    dobj_dw = -dphi_df * 2.0 * w
    scale = max(abs(numer), 1e-30)
    dobj_dw /= scale
    dobj_dw = np.clip(dobj_dw, -1e6, 1e6)
    dobj_dw = np.nan_to_num(dobj_dw, nan=0.0)

    return float(-phi / scale), dobj_dw


def lbfgs_refine(w_init, n, beta_schedule, outer_per_beta=5, maxiter=2000, time_limit=600):
    """Refine solution using Dinkelbach + L-BFGS."""
    w = w_init.copy()
    f = w * w
    best_score = fast_evaluate(f)
    best_w = w.copy()
    t0 = time.time()

    conv = fftconvolve(f, f, mode="full")
    lam = score_from_conv(conv)

    for bi, beta in enumerate(beta_schedule):
        if time.time() - t0 > time_limit:
            break
        for outer in range(outer_per_beta):
            if time.time() - t0 > time_limit:
                break

            res = minimize(
                lambda ww: dinkelbach_obj_grad(ww, lam, beta, n),
                w,
                method="L-BFGS-B",
                jac=True,
                options={"maxiter": maxiter, "ftol": 1e-15, "gtol": 1e-14},
            )
            w = res.x
            f = w * w
            conv = fftconvolve(f, f, mode="full")
            if np.all(np.isfinite(conv)) and np.sum(conv) > 0:
                score = score_from_conv(conv)
                lam = score
                true_score = fast_evaluate(f)
                if true_score > best_score:
                    best_score = true_score
                    best_w = w.copy()
                    print(f"    beta={beta:.0e} outer={outer}: C={true_score:.16f} (nit={res.nit})")
            if res.nit <= 2:
                break

        elapsed = time.time() - t0
        print(f"  beta={beta:.0e} done ({elapsed:.0f}s) best={best_score:.16f}")

    return best_w, best_score


def save_solution(f, score, tag):
    """Save solution to disk."""
    fname = RESULTS_DIR / f"opt_{tag}_{score:.10f}.json"
    result = {
        "problem": "second-autocorrelation-inequality",
        "n_points": len(f),
        "score": score,
        "values": [round(float(v), 12) for v in f],
        "tag": tag,
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%S"),
    }
    with open(fname, "w") as fh:
        json.dump(result, fh)
    print(f"  Saved to {fname}")
    return fname


def optimize_transplant(f_source, target_n, tag, threshold=0.0, time_budget=1800):
    """Full pipeline: transplant → Dinkelbach refinement."""
    print(f"\n{'='*70}")
    print(f"Optimizing: {tag} (n={target_n}, threshold={threshold})")
    print(f"{'='*70}")

    f_init = transplant(f_source, target_n, active_threshold=threshold)
    init_score = fast_evaluate(f_init)
    print(f"  Transplant score: C={init_score:.16f}")

    w = np.sqrt(np.maximum(f_init, 0) + 1e-30)
    n = len(w)

    # Beta cascade — aggressive schedule for GPU-like refinement on CPU
    beta_schedule = [1e4, 5e4, 1e5, 5e5, 1e6, 5e6, 1e7, 5e7, 1e8]

    w_opt, best_score = lbfgs_refine(
        w, n, beta_schedule,
        outer_per_beta=5,
        maxiter=1000,
        time_limit=time_budget,
    )

    f_opt = w_opt * w_opt
    final_score = fast_evaluate(f_opt)
    print(f"  Final score: C={final_score:.16f}")
    print(f"  Improvement: {final_score - init_score:.2e}")

    save_solution(f_opt, final_score, tag)
    return f_opt, final_score


def optimize_warmstart(f_start, tag, time_budget=1800):
    """Refine an existing solution with Dinkelbach."""
    print(f"\n{'='*70}")
    print(f"Warm-start refinement: {tag} (n={len(f_start)})")
    print(f"{'='*70}")

    init_score = fast_evaluate(f_start)
    print(f"  Starting score: C={init_score:.16f}")

    w = np.sqrt(np.maximum(f_start, 0) + 1e-30)
    n = len(w)

    # High beta schedule for polishing near-optimal solutions
    beta_schedule = [1e6, 5e6, 1e7, 5e7, 1e8, 5e8, 1e9, 5e9, 1e10]

    w_opt, best_score = lbfgs_refine(
        w, n, beta_schedule,
        outer_per_beta=5,
        maxiter=1000,
        time_limit=time_budget,
    )

    f_opt = w_opt * w_opt
    final_score = fast_evaluate(f_opt)
    print(f"  Final score: C={final_score:.16f}")
    print(f"  Improvement: {final_score - init_score:.2e}")

    save_solution(f_opt, final_score, tag)
    return f_opt, final_score


def main():
    t_global = time.time()
    TIME_LIMIT = 3 * 3600  # 3 hours total

    # Load source solutions
    f_1600k = np.load("/Users/jmsung/projects/einstein/cb/results/problem-3-autocorrelation/best_1600k.npy")
    print(f"1.6M source: C={fast_evaluate(f_1600k):.16f}")

    sota_400k_path = RESULTS_DIR / "sota_400k.npy"
    f_sota_400k = np.load(sota_400k_path) if sota_400k_path.exists() else None
    if f_sota_400k is not None:
        print(f"SOTA 400k:   C={fast_evaluate(f_sota_400k):.16f}")

    results = {}

    # Strategy 1: Transplant 1.6M → 400k with different thresholds
    for threshold in [0.0, 1e-3, 1e-2]:
        tag = f"400k_t{threshold:.0e}" if threshold > 0 else "400k_full"
        remaining = TIME_LIMIT - (time.time() - t_global)
        if remaining < 300:
            print(f"Skipping {tag} (insufficient time)")
            break
        f_opt, score = optimize_transplant(
            f_1600k, 400000, tag, threshold=threshold,
            time_budget=min(1800, remaining * 0.25),
        )
        results[tag] = (f_opt, score)

    # Strategy 2: Transplant 1.6M → 800k (less resolution tax)
    remaining = TIME_LIMIT - (time.time() - t_global)
    if remaining > 600:
        f_opt, score = optimize_transplant(
            f_1600k, 800000, "800k_full", threshold=0.0,
            time_budget=min(2400, remaining * 0.3),
        )
        results["800k_full"] = (f_opt, score)

    # Strategy 3: Warm-start from ClaudeExplorer's 400k SOTA
    remaining = TIME_LIMIT - (time.time() - t_global)
    if f_sota_400k is not None and remaining > 300:
        f_opt, score = optimize_warmstart(
            f_sota_400k, "400k_warmstart",
            time_budget=min(1800, remaining * 0.3),
        )
        results["400k_warmstart"] = (f_opt, score)

    # Strategy 4: Upsample ClaudeExplorer 400k → 800k and refine
    remaining = TIME_LIMIT - (time.time() - t_global)
    if f_sota_400k is not None and remaining > 600:
        # Linear interpolation upsample
        x_400k = np.linspace(0, 1, 400000)
        x_800k = np.linspace(0, 1, 800000)
        f_800k_up = np.interp(x_800k, x_400k, f_sota_400k)
        f_opt, score = optimize_warmstart(
            f_800k_up, "800k_upsample_sota",
            time_budget=min(2400, remaining * 0.4),
        )
        results["800k_upsample_sota"] = (f_opt, score)

    # Summary
    print(f"\n{'='*70}")
    print("SUMMARY")
    print(f"{'='*70}")
    best_tag = None
    best_score = 0.0
    for tag, (f, score) in sorted(results.items(), key=lambda x: -x[1][1]):
        marker = " *** BEATS SOTA" if score > TARGET_SCORE else ""
        print(f"  {tag:30s}: C={score:.16f}{marker}")
        if score > best_score:
            best_score = score
            best_tag = tag

    total_time = time.time() - t_global
    print(f"\nBest: {best_tag} = {best_score:.16f}")
    print(f"Target: {TARGET_SCORE:.16f}")
    print(f"Gap: {TARGET_SCORE - best_score:.2e}")
    print(f"Total time: {total_time:.0f}s")

    # Save the overall best
    if best_tag:
        f_best = results[best_tag][0]
        np.save(RESULTS_DIR / "opt_best.npy", f_best)
        save_solution(f_best, best_score, "overall_best")


if __name__ == "__main__":
    main()
