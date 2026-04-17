"""Auto P3 Optimizer: Multi-approach campaign to beat SOTA 0.96264.

Target: C ≥ 0.96274 (SOTA + minImprovement 0.0001)

Approaches:
  A) Polish orig 1.6M with extended Dinkelbach
  B) Optimize at n=800k from transplanted starting points
  C) Optimize at n=600k and n=400k with different starting points
  D) Multi-start from scratch at various n
  E) Perturbation escape at 1.6M (large noise + re-optimize)
"""

import json
import os
import sys
import time

import numpy as np
from scipy.optimize import minimize
from scipy.signal import fftconvolve

sys.path.insert(0, "src")
from einstein.autocorrelation.fast import fast_evaluate, score_from_conv

RESULTS_DIR = "results/problem-3-autocorrelation"
os.makedirs(RESULTS_DIR, exist_ok=True)

# Load solutions
SOTA_400K = np.load("/tmp/sota_400k.npy")
ORIG_1600K = np.load(
    os.path.expanduser(
        "~/projects/einstein/cb/results/problem-3-autocorrelation/best_1600k.npy"
    )
)

ARENA_SOTA = 0.9626433187626762
MIN_IMPROVEMENT = 0.0001
TARGET = ARENA_SOTA + MIN_IMPROVEMENT

GLOBAL_BEST_SCORE = 0.0
GLOBAL_BEST_F = None
GLOBAL_BEST_TAG = ""
T_START = time.time()


def elapsed():
    return time.time() - T_START


def log(msg):
    print(f"[{elapsed():7.1f}s] {msg}", flush=True)


def save_solution(f, score, tag):
    global GLOBAL_BEST_SCORE, GLOBAL_BEST_F, GLOBAL_BEST_TAG
    if score > GLOBAL_BEST_SCORE:
        GLOBAL_BEST_SCORE = score
        GLOBAL_BEST_F = f.copy()
        GLOBAL_BEST_TAG = tag
        fname = f"{RESULTS_DIR}/auto_p3_{tag}_n{len(f)}_{score:.10f}.json"
        data = {"values": f.tolist(), "score": score, "n": len(f), "tag": tag}
        with open(fname, "w") as fh:
            json.dump(data, fh)
        gap = score - TARGET
        status = "SUBMITTABLE!" if gap >= 0 else f"short by {-gap:.10f}"
        log(f"*** NEW BEST: {score:.16f} ({tag}, n={len(f)}) — {status}")
        return True
    return False


# ── Gradient computation ──────────────────────────────────────────────
def score_grad_lse(w, beta):
    """Compute C and dC/dw using LogSumExp smooth max. w² parametrization."""
    n = len(w)
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


def dinkelbach_obj_grad(w, lam, beta):
    """Dinkelbach: minimize -(numer - lam*denom)."""
    n = len(w)
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


# ── Optimizers ────────────────────────────────────────────────────────
def adam_optimize(w_init, schedule, time_limit, tag="adam"):
    """Adam with progressive beta cascade."""
    w = w_init.copy()
    best_score = fast_evaluate(w * w)
    best_w = w.copy()
    t0 = time.time()

    b1, b2, eps = 0.9, 0.999, 1e-8
    m = np.zeros_like(w)
    v = np.zeros_like(w)
    step_count = 0

    for beta, n_iters, lr in schedule:
        if time.time() - t0 > time_limit:
            break
        m[:] = 0
        v[:] = 0
        for it in range(n_iters):
            if time.time() - t0 > time_limit:
                break
            _, grad = score_grad_lse(w, beta)
            grad = np.clip(grad, -1e6, 1e6)
            grad = np.nan_to_num(grad, nan=0.0)
            m = b1 * m + (1 - b1) * grad
            v = b2 * v + (1 - b2) * grad * grad
            mh = m / (1 - b1 ** (it + 1))
            vh = v / (1 - b2 ** (it + 1))
            w = w + lr * mh / (np.sqrt(vh) + eps)
            w = np.maximum(w, 0)
            step_count += 1

            if step_count % 500 == 0:
                f_cur = w * w
                score = fast_evaluate(f_cur)
                if score > best_score:
                    best_score = score
                    best_w = w.copy()
                    save_solution(f_cur, score, tag)

    f_final = w * w
    score = fast_evaluate(f_final)
    if score > best_score:
        best_score = score
        best_w = w.copy()
        save_solution(f_final, score, tag)

    return best_w, best_score


def lbfgs_dinkelbach(w_init, beta_schedule, outer_per_beta, maxiter, time_limit, tag="lbfgs"):
    """Dinkelbach + L-BFGS-B refinement."""
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
                lambda ww: dinkelbach_obj_grad(ww, lam, beta),
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
                    save_solution(f, score, tag)
            if res.nit <= 2:
                break

    return best_w, best_score


def perturbation_search(f_init, n_trials, noise_scale, time_limit, tag="perturb"):
    """Large perturbation + local refinement."""
    best_f = f_init.copy()
    best_score = fast_evaluate(best_f)
    t0 = time.time()
    rng = np.random.default_rng(42)

    for trial in range(n_trials):
        if time.time() - t0 > time_limit:
            break

        # Perturb
        f_trial = f_init.copy()
        noise = rng.normal(0, noise_scale, len(f_init))
        f_trial += noise * f_init  # multiplicative noise
        f_trial = np.maximum(f_trial, 0)

        # Quick Adam polish
        w = np.sqrt(f_trial + 1e-30)
        quick_schedule = [
            (1e4, 200, 0.001),
            (1e5, 200, 0.0005),
            (1e6, 200, 0.0002),
        ]
        w_opt, score = adam_optimize(
            w, quick_schedule, min(30, time_limit * 0.3 / max(n_trials, 1)),
            tag=f"{tag}_t{trial}"
        )

        if score > best_score:
            best_score = score
            best_f = (w_opt * w_opt).copy()
            log(f"  Perturbation trial {trial}: C={score:.16f} (noise={noise_scale:.3f})")
            save_solution(best_f, score, tag)

    return best_f, best_score


def upsample(f, target_n):
    """Upsample f to target_n using linear interpolation."""
    n = len(f)
    x_old = np.linspace(0, 1, n)
    x_new = np.linspace(0, 1, target_n)
    return np.maximum(np.interp(x_new, x_old, f), 0)


def avg_pool_transplant(f, target_n, threshold=0):
    """Average-pool active region of f to target_n."""
    if threshold > 0:
        active = f > threshold
        idx = np.where(active)[0]
        if len(idx) == 0:
            return np.zeros(target_n)
        start, end = idx[0], idx[-1] + 1
    else:
        start, end = 0, len(f)

    f_active = f[start:end]
    active_n = len(f_active)
    result = np.zeros(target_n)
    for i in range(target_n):
        s = int(i * active_n / target_n)
        e = int((i + 1) * active_n / target_n)
        if e > s:
            result[i] = np.mean(f_active[s:e])
    return result


# ── Beta schedules ────────────────────────────────────────────────────
ADAM_SCHEDULE_DEEP = [
    (1e3, 1000, 0.003),
    (1e4, 1000, 0.001),
    (3e4, 1000, 0.0005),
    (1e5, 1000, 0.0003),
    (3e5, 1000, 0.0002),
    (1e6, 1000, 0.0001),
    (3e6, 1000, 0.00005),
    (1e7, 1000, 0.00003),
    (3e7, 1000, 0.00001),
    (1e8, 1000, 0.000005),
]

ADAM_SCHEDULE_EXTENDED = [
    (1e3, 2000, 0.003),
    (3e3, 2000, 0.002),
    (1e4, 2000, 0.001),
    (3e4, 2000, 0.0007),
    (1e5, 2000, 0.0005),
    (3e5, 2000, 0.0003),
    (1e6, 2000, 0.0002),
    (3e6, 2000, 0.0001),
    (1e7, 2000, 0.00005),
    (3e7, 2000, 0.00003),
    (1e8, 2000, 0.00001),
    (3e8, 2000, 0.000005),
    (1e9, 2000, 0.000003),
    (1e10, 2000, 0.000001),
]

LBFGS_BETAS_DEEP = [
    1e4, 3e4, 1e5, 3e5, 1e6, 3e6, 1e7, 3e7, 1e8, 3e8, 1e9, 3e9, 1e10
]

LBFGS_BETAS_ULTRA = [
    1e4, 3e4, 1e5, 3e5, 1e6, 3e6, 1e7, 3e7, 1e8, 3e8, 1e9, 3e9,
    1e10, 3e10, 1e11, 3e11, 1e12
]


# ══════════════════════════════════════════════════════════════════════
#  MAIN CAMPAIGN
# ══════════════════════════════════════════════════════════════════════
def main():
    log(f"Starting Auto P3 Optimization Campaign")
    log(f"SOTA: {ARENA_SOTA:.16f}, Target: {TARGET:.16f}")

    # Verify starting scores
    score_400k = fast_evaluate(SOTA_400K)
    score_1600k = fast_evaluate(ORIG_1600K)
    log(f"SOTA 400k: {score_400k:.16f}")
    log(f"Orig 1.6M: {score_1600k:.16f}")

    save_solution(ORIG_1600K, score_1600k, "orig_1600k")
    save_solution(SOTA_400K, score_400k, "sota_400k")

    # ── Approach A: Polish 1.6M with extended optimization ────────────
    log("=" * 60)
    log("APPROACH A: Polish 1.6M solution")
    log("=" * 60)

    w_1600k = np.sqrt(ORIG_1600K + 1e-30)

    # A1: Extended L-BFGS Dinkelbach at ultra-high beta
    log("  A1: L-BFGS Dinkelbach at 1.6M (ultra-high beta)")
    w_a1, score_a1 = lbfgs_dinkelbach(
        w_1600k, LBFGS_BETAS_ULTRA, outer_per_beta=5, maxiter=200,
        time_limit=900, tag="A1_lbfgs_1600k"
    )
    log(f"  A1 result: {score_a1:.16f}")

    # A2: Adam at 1.6M
    log("  A2: Adam at 1.6M")
    w_a2, score_a2 = adam_optimize(
        w_1600k, ADAM_SCHEDULE_EXTENDED, time_limit=600, tag="A2_adam_1600k"
    )
    log(f"  A2 result: {score_a2:.16f}")

    # ── Approach B: Optimize at n=800k ────────────────────────────────
    log("=" * 60)
    log("APPROACH B: Optimize at n=800k")
    log("=" * 60)

    # B1: Upsample SOTA 400k to 800k
    f_800k_up = upsample(SOTA_400K, 800000)
    log(f"  B1 init (upsample 400k): C={fast_evaluate(f_800k_up):.16f}")
    w_b1 = np.sqrt(f_800k_up + 1e-30)
    w_b1_opt, score_b1 = adam_optimize(
        w_b1, ADAM_SCHEDULE_DEEP, time_limit=600, tag="B1_800k_from400k"
    )
    w_b1_ref, score_b1_ref = lbfgs_dinkelbach(
        w_b1_opt, LBFGS_BETAS_DEEP, 5, 200, 300, tag="B1_800k_lbfgs"
    )
    log(f"  B1 result: {max(score_b1, score_b1_ref):.16f}")

    # B2: Avg-pool transplant 1.6M → 800k
    f_800k_tp = avg_pool_transplant(ORIG_1600K, 800000)
    log(f"  B2 init (transplant 1.6M): C={fast_evaluate(f_800k_tp):.16f}")
    w_b2 = np.sqrt(f_800k_tp + 1e-30)
    w_b2_opt, score_b2 = adam_optimize(
        w_b2, ADAM_SCHEDULE_DEEP, time_limit=600, tag="B2_800k_transplant"
    )
    w_b2_ref, score_b2_ref = lbfgs_dinkelbach(
        w_b2_opt, LBFGS_BETAS_DEEP, 5, 200, 300, tag="B2_800k_tp_lbfgs"
    )
    log(f"  B2 result: {max(score_b2, score_b2_ref):.16f}")

    # B3: Downsample 1.6M → 800k (different from avg-pool)
    f_800k_ds = ORIG_1600K[::2]  # every other point
    log(f"  B3 init (downsample 1.6M): C={fast_evaluate(f_800k_ds):.16f}")
    w_b3 = np.sqrt(f_800k_ds + 1e-30)
    w_b3_opt, score_b3 = adam_optimize(
        w_b3, ADAM_SCHEDULE_DEEP, time_limit=600, tag="B3_800k_downsample"
    )
    w_b3_ref, score_b3_ref = lbfgs_dinkelbach(
        w_b3_opt, LBFGS_BETAS_DEEP, 5, 200, 300, tag="B3_800k_ds_lbfgs"
    )
    log(f"  B3 result: {max(score_b3, score_b3_ref):.16f}")

    # ── Approach C: Optimize at n=600k ────────────────────────────────
    log("=" * 60)
    log("APPROACH C: Optimize at n=600k")
    log("=" * 60)

    # C1: Upsample 400k → 600k
    f_600k = upsample(SOTA_400K, 600000)
    log(f"  C1 init (upsample 400k): C={fast_evaluate(f_600k):.16f}")
    w_c1 = np.sqrt(f_600k + 1e-30)
    w_c1_opt, score_c1 = adam_optimize(
        w_c1, ADAM_SCHEDULE_DEEP, time_limit=600, tag="C1_600k"
    )
    w_c1_ref, score_c1_ref = lbfgs_dinkelbach(
        w_c1_opt, LBFGS_BETAS_DEEP, 5, 200, 300, tag="C1_600k_lbfgs"
    )
    log(f"  C1 result: {max(score_c1, score_c1_ref):.16f}")

    # C2: Transplant 1.6M → 600k
    f_600k_tp = avg_pool_transplant(ORIG_1600K, 600000)
    log(f"  C2 init (transplant 1.6M): C={fast_evaluate(f_600k_tp):.16f}")
    w_c2 = np.sqrt(f_600k_tp + 1e-30)
    w_c2_opt, score_c2 = adam_optimize(
        w_c2, ADAM_SCHEDULE_DEEP, time_limit=600, tag="C2_600k_transplant"
    )
    w_c2_ref, score_c2_ref = lbfgs_dinkelbach(
        w_c2_opt, LBFGS_BETAS_DEEP, 5, 200, 300, tag="C2_600k_tp_lbfgs"
    )
    log(f"  C2 result: {max(score_c2, score_c2_ref):.16f}")

    # ── Approach D: Polish SOTA 400k from different directions ────────
    log("=" * 60)
    log("APPROACH D: Polish SOTA 400k variants")
    log("=" * 60)

    # D1: Direct L-BFGS on SOTA
    w_400k = np.sqrt(SOTA_400K + 1e-30)
    w_d1, score_d1 = lbfgs_dinkelbach(
        w_400k, LBFGS_BETAS_ULTRA, 5, 200, 600, tag="D1_400k_lbfgs"
    )
    log(f"  D1 result: {score_d1:.16f}")

    # D2: Transplant 1.6M → 400k with different thresholds
    for thresh in [0, 1e-5, 1e-4, 1e-3, 1e-2, 1e-1]:
        f_tp = avg_pool_transplant(ORIG_1600K, 400000, threshold=thresh)
        s0 = fast_evaluate(f_tp)
        w_tp = np.sqrt(f_tp + 1e-30)
        w_tp_opt, s_opt = adam_optimize(
            w_tp, ADAM_SCHEDULE_DEEP[:6], time_limit=120,
            tag=f"D2_tp_t{thresh:.0e}"
        )
        w_tp_ref, s_ref = lbfgs_dinkelbach(
            w_tp_opt, LBFGS_BETAS_DEEP[:8], 3, 100, 60,
            tag=f"D2_tp_t{thresh:.0e}_lbfgs"
        )
        best_s = max(s_opt, s_ref)
        log(f"  D2 threshold={thresh:.0e}: init={s0:.8f} → final={best_s:.16f}")

    # ── Approach E: Perturbation escape at 1.6M ──────────────────────
    log("=" * 60)
    log("APPROACH E: Perturbation escape at 1.6M")
    log("=" * 60)

    for noise_level in [0.001, 0.005, 0.01, 0.05, 0.1]:
        remaining = max(3600 * 3.5 - elapsed(), 300)
        if remaining < 300:
            break
        log(f"  E: noise={noise_level}")
        f_e, score_e = perturbation_search(
            ORIG_1600K, n_trials=5, noise_scale=noise_level,
            time_limit=min(300, remaining / 5), tag=f"E_perturb_{noise_level}"
        )
        log(f"  E noise={noise_level}: {score_e:.16f}")

    # ── Final summary ─────────────────────────────────────────────────
    log("=" * 60)
    log("CAMPAIGN COMPLETE")
    log(f"Best score: {GLOBAL_BEST_SCORE:.16f} ({GLOBAL_BEST_TAG})")
    log(f"Target:     {TARGET:.16f}")
    gap = GLOBAL_BEST_SCORE - TARGET
    if gap >= 0:
        log(f"STATUS: SUBMITTABLE! (margin: {gap:.10f})")
    else:
        log(f"STATUS: Short by {-gap:.10f}")
    log(f"Total time: {elapsed():.1f}s")


if __name__ == "__main__":
    main()
