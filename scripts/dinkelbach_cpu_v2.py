"""Dinkelbach CPU v2: Adam + L-BFGS optimizer for Problem 3.

Maximize C = (2*sum(c^2) + sum(c_i*c_{i+1})) / (3 * sum(c) * max(c))
where c = fftconvolve(f, f, mode='full') and f >= 0.

Strategy:
  1. Adam with progressive beta cascade (LogSumExp smooth max)
     - Low beta explores; high beta refines
     - Overcomes non-smooth max gradient
  2. Multi-start: many random block inits at width 25-35
  3. Deep refinement of top candidates with extended Adam + L-BFGS
  4. Greedy support expansion to escape local optima

Target: C > 0.90 at n=2000-3000. Runtime < 5 minutes.
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
    """Save a result to disk."""
    result = {
        "problem": "second-autocorrelation-inequality",
        "n_points": len(f),
        "score": score,
        "values": f.tolist() if isinstance(f, np.ndarray) else f,
        "tag": tag,
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%S"),
    }
    fname = RESULTS_DIR / f"dinkelbach_cpu_v2_n{len(f)}_{score:.8f}_{tag}.json"
    with open(fname, "w") as fh:
        json.dump(result, fh)
    print(f"  Saved to {fname}")
    return fname


# ---------------------------------------------------------------------------
# Gradient computation: direct C gradient via LogSumExp
# ---------------------------------------------------------------------------
def score_grad_lse(w, n, beta):
    """Compute C and dC/dw using LogSumExp smooth max."""
    f = w * w
    s = np.sum(f)
    if s < 1e-30:
        return 0.0, np.zeros_like(w)
    conv = fftconvolve(f, f, mode="full")
    if not np.all(np.isfinite(conv)):
        return 0.0, np.zeros_like(w)

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

    denom = 3.0 * c_sum * proxy
    C_val = numer / denom

    dn_dc = 4.0 * conv.copy()
    dn_dc[1:] += conv[:-1]
    dn_dc[:-1] += conv[1:]
    dd_dc = 3.0 * (proxy + c_sum * d_proxy_dc)
    dC_dc = (dn_dc * denom - numer * dd_dc) / (denom * denom)

    dC_df = 2.0 * fftconvolve(dC_dc, f[::-1], mode="full")
    dC_df = dC_df[n - 1 : 2 * n - 1]
    dC_dw = dC_df * 2.0 * w

    return float(C_val), dC_dw


# ---------------------------------------------------------------------------
# Dinkelbach objective for L-BFGS refinement
# ---------------------------------------------------------------------------
def dinkelbach_obj_grad(w, lam, beta, n):
    """Dinkelbach objective: minimize -(numer - lam*denom)."""
    f = w * w
    s = np.sum(f)
    if s < 1e-30:
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
    dphi_df = dphi_df[n - 1 : 2 * n - 1]

    dobj_dw = -dphi_df * 2.0 * w
    scale = max(abs(numer), 1e-30)
    dobj_dw /= scale
    dobj_dw = np.clip(dobj_dw, -1e6, 1e6)
    dobj_dw = np.nan_to_num(dobj_dw, nan=0.0)

    return float(-phi / scale), dobj_dw


# ---------------------------------------------------------------------------
# Adam optimizer
# ---------------------------------------------------------------------------
def adam_optimize(w_init, n, schedule, time_limit):
    """Maximize C using Adam with progressive beta cascade."""
    w = w_init.copy()
    best_score = fast_evaluate(w * w)
    best_w = w.copy()
    t0 = time.time()

    b1, b2, eps = 0.9, 0.999, 1e-8
    m = np.zeros_like(w)
    v = np.zeros_like(w)

    for beta, n_iters, lr in schedule:
        if time.time() - t0 > time_limit:
            break
        m[:] = 0
        v[:] = 0
        for it in range(n_iters):
            if time.time() - t0 > time_limit:
                break
            _, grad = score_grad_lse(w, n, beta)
            grad = np.clip(grad, -1e6, 1e6)
            grad = np.nan_to_num(grad, nan=0.0)
            m = b1 * m + (1 - b1) * grad
            v = b2 * v + (1 - b2) * grad * grad
            mh = m / (1 - b1 ** (it + 1))
            vh = v / (1 - b2 ** (it + 1))
            w = w + lr * mh / (np.sqrt(vh) + eps)
            w = np.maximum(w, 0)
        f_cur = w * w
        score = fast_evaluate(f_cur)
        if score > best_score:
            best_score = score
            best_w = w.copy()

    return best_w, best_score


# ---------------------------------------------------------------------------
# L-BFGS Dinkelbach refinement
# ---------------------------------------------------------------------------
def lbfgs_refine(w_init, n, beta_schedule, outer_per_beta, maxiter, time_limit):
    """Refine solution using Dinkelbach + L-BFGS."""
    w = w_init.copy()
    f = w * w
    best_score = fast_evaluate(f)
    best_w = w.copy()
    t0 = time.time()

    conv = fftconvolve(f, f, mode="full")
    lam = score_from_conv(conv)

    for beta in beta_schedule:
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
                if score > best_score:
                    best_score = score
                    best_w = w.copy()
            if res.nit <= 2:
                break

    return best_w, best_score


# ---------------------------------------------------------------------------
# Greedy support expansion
# ---------------------------------------------------------------------------
def greedy_expand(f_in, n, time_limit):
    """Try adding support points near the existing support to improve C."""
    best_f = f_in.copy()
    best_score = fast_evaluate(best_f)
    t0 = time.time()

    for iteration in range(30):
        if time.time() - t0 > time_limit:
            break
        improved = False
        nz = np.where(best_f > 1e-10)[0]
        if len(nz) == 0:
            break
        search_lo = max(0, nz.min() - 10)
        search_hi = min(n, nz.max() + 11)
        mean_val = best_f[nz].mean()

        local_best_gain = 0
        local_best_pos = -1
        local_best_val = 0

        for pos in range(search_lo, search_hi):
            if best_f[pos] > 1e-10:
                continue
            for frac in [0.05, 0.1, 0.2, 0.5, 1.0, 2.0, 5.0]:
                f_trial = best_f.copy()
                f_trial[pos] = frac * mean_val
                score = fast_evaluate(f_trial)
                gain = score - best_score
                if gain > local_best_gain:
                    local_best_gain = gain
                    local_best_pos = pos
                    local_best_val = frac * mean_val

        if local_best_pos >= 0 and local_best_gain > 1e-10:
            best_f[local_best_pos] = local_best_val
            # Refine the new value
            for _ in range(10):
                for factor in [0.7, 0.85, 0.95, 1.05, 1.15, 1.3, 1.5]:
                    f_trial = best_f.copy()
                    f_trial[local_best_pos] *= factor
                    score = fast_evaluate(f_trial)
                    if score > best_score + 1e-12:
                        best_score = score
                        best_f = f_trial.copy()
            # Refine all values
            for idx in np.where(best_f > 1e-10)[0]:
                for factor in [0.95, 1.05]:
                    f_trial = best_f.copy()
                    f_trial[idx] *= factor
                    score = fast_evaluate(f_trial)
                    if score > best_score + 1e-12:
                        best_score = score
                        best_f = f_trial.copy()
            improved = True

        if not improved:
            break

    return best_f, best_score


# ---------------------------------------------------------------------------
# Schedules
# ---------------------------------------------------------------------------
SCHEDULE_QUICK = [
    (10, 2000, 0.005),
    (30, 2000, 0.003),
    (100, 2000, 0.001),
    (300, 2000, 0.0005),
    (1000, 2000, 0.0003),
    (3000, 2000, 0.0001),
]

SCHEDULE_DEEP = [
    (10, 5000, 0.005),
    (30, 5000, 0.003),
    (50, 5000, 0.002),
    (100, 5000, 0.001),
    (200, 5000, 0.0008),
    (500, 5000, 0.0005),
    (1000, 5000, 0.0003),
    (2000, 5000, 0.0002),
    (5000, 5000, 0.0001),
    (10000, 5000, 0.00005),
    (30000, 5000, 0.00003),
    (100000, 5000, 0.00001),
]


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main():
    print("=" * 60)
    print("Dinkelbach CPU v2: Adam + L-BFGS Optimizer")
    print("Target: C > 0.90 at n=2000-3000")
    print("=" * 60)

    t_global = time.time()
    TIME_LIMIT = 280

    overall_best = {}

    for n in [2000, 2500, 3000]:
        print(f"\n{'='*60}")
        print(f"Optimizing n={n}")
        print(f"{'='*60}")

        n_start = time.time()
        n_time = min(TIME_LIMIT - (time.time() - t_global), 90)
        if n_time < 10:
            print(f"  Skipping n={n} (insufficient time)")
            continue

        best_f = None
        best_score = 0.0

        # ----- Phase 1: Quick multi-start screening (30% of time) -----
        screen_time = n_time * 0.30
        print(f"\n  Phase 1: Quick screening ({screen_time:.0f}s budget)")

        candidates = []
        seed_counter = 0
        for width in [25, 28, 30, 32, 35, 40]:
            for seed_base in range(15):
                elapsed = time.time() - n_start
                if elapsed > screen_time:
                    break
                seed = seed_counter
                seed_counter += 1

                rng = np.random.default_rng(seed * 97 + width * 31 + n)
                f_init = np.zeros(n)
                start = rng.integers(0, max(n - width, 1))
                f_init[start : start + width] = rng.exponential(1.0, width)
                w_init = np.sqrt(f_init)

                w_opt, score = adam_optimize(w_init, n, SCHEDULE_QUICK, 3)
                candidates.append((score, w_opt * w_opt, f"w{width}_s{seed}"))

                if score > best_score:
                    best_score = score
                    best_f = (w_opt * w_opt).copy()
                    if score > 0.87:
                        nnz = np.count_nonzero(best_f > 1e-10)
                        print(f"    w={width} s={seed_base}: C={score:.8f} nnz={nnz}")
            if time.time() - n_start > screen_time:
                break

        # ----- Phase 2: Deep optimization of top candidates (50% of time) -----
        candidates.sort(key=lambda x: -x[0])
        n_top = min(5, len(candidates))
        deep_time = n_time * 0.50
        per_deep = max(deep_time / n_top, 5) if n_top > 0 else 0

        print(f"\n  Phase 2: Deep optimization of top {n_top} ({deep_time:.0f}s budget)")

        for i, (cand_score, cand_f, cand_name) in enumerate(candidates[:n_top]):
            elapsed = time.time() - n_start
            if elapsed > screen_time + deep_time:
                break
            remaining = screen_time + deep_time - elapsed
            t_limit = min(per_deep, remaining - 2)
            if t_limit < 3:
                break

            w_cand = np.sqrt(cand_f + 1e-30)

            # Deep Adam
            w_deep, score_deep = adam_optimize(
                w_cand, n, SCHEDULE_DEEP, t_limit * 0.75
            )

            # L-BFGS refinement
            w_ref, score_ref = lbfgs_refine(
                w_deep, n, [10000, 100000, 1000000], 30, 500,
                max(t_limit * 0.25, 1)
            )

            deep_score = max(score_deep, score_ref)
            deep_f = (w_ref * w_ref) if score_ref >= score_deep else (w_deep * w_deep)

            if deep_score > best_score:
                best_score = deep_score
                best_f = deep_f.copy()
                nnz = np.count_nonzero(best_f > 1e-10)
                print(
                    f"    Deep #{i} ({cand_name}): C={deep_score:.8f} nnz={nnz} "
                    f"*** BEST ({time.time()-n_start:.1f}s)"
                )

        # ----- Phase 3: Greedy expansion + final refinement (20% of time) -----
        refine_time = n_time - (time.time() - n_start)
        if best_f is not None and refine_time > 5:
            print(f"\n  Phase 3: Greedy expansion + refinement ({refine_time:.0f}s)")

            # Greedy support expansion
            f_exp, score_exp = greedy_expand(best_f, n, refine_time * 0.4)
            if score_exp > best_score:
                best_score = score_exp
                best_f = f_exp.copy()
                print(f"    Greedy: C={score_exp:.8f}")

            # Final deep Adam from best
            remaining = n_time - (time.time() - n_start)
            if remaining > 5:
                w_final = np.sqrt(best_f + 1e-30)
                w_opt, score_opt = adam_optimize(
                    w_final, n, SCHEDULE_DEEP, remaining * 0.7
                )
                if score_opt > best_score:
                    best_score = score_opt
                    best_f = (w_opt * w_opt).copy()

                # L-BFGS polish
                remaining2 = n_time - (time.time() - n_start)
                if remaining2 > 2:
                    w_pol, score_pol = lbfgs_refine(
                        w_opt, n, [100000, 1000000, 10000000], 20, 500,
                        max(remaining2, 1)
                    )
                    if score_pol > best_score:
                        best_score = score_pol
                        best_f = (w_pol * w_pol).copy()
                    print(f"    Final refine: C={max(score_opt, score_pol):.8f}")

        if best_f is None:
            print(f"  No valid solution found for n={n}")
            continue

        # ----- Verify and save -----
        arena_score = evaluate({"values": best_f.tolist()})
        fast_score = fast_evaluate(best_f)
        nnz = np.count_nonzero(best_f > 1e-10)

        print(f"\n  n={n} Result:")
        print(f"    Fast score:  C={fast_score:.10f}")
        print(f"    Arena score: C={arena_score:.10f}")
        print(f"    Nonzero:     {nnz}")

        d = diagnose(best_f)
        print(f"    Blocks: {d['n_blocks']}, mean width: {d['mean_block_width']:.1f}")

        save_result(best_f, arena_score, f"cpu_v2_n{n}")
        overall_best[n] = (best_f, arena_score)

        target_met = arena_score > 0.90
        print(f"    {'TARGET MET (>0.90)!' if target_met else 'Below target (0.90)'}")

    # Summary
    total_time = time.time() - t_global
    print(f"\n{'='*60}")
    print("Summary")
    print(f"{'='*60}")
    for n_val, (f, score) in overall_best.items():
        nnz = np.count_nonzero(f > 1e-10)
        print(f"  n={n_val}: C={score:.10f} nnz={nnz}")
    print(f"  Total time: {total_time:.1f}s")


if __name__ == "__main__":
    main()
