"""Phase 1: Polish the 1.6M original solution.

Even though MB says it's at a local max, let's verify with fresh optimization.
Try different beta schedules and approaches.
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

RESULTS = "results/problem-3-autocorrelation"
os.makedirs(RESULTS, exist_ok=True)

f_orig = np.load(
    os.path.expanduser(
        "~/projects/einstein/cb/results/problem-3-autocorrelation/best_1600k.npy"
    )
)
SCORE_ORIG = fast_evaluate(f_orig)
TARGET = 0.9627433187626762

print(f"Original 1.6M score: {SCORE_ORIG:.16f}")
print(f"Target:              {TARGET:.16f}")
print(f"Gap:                 {TARGET - SCORE_ORIG:.10f}")


def dinkelbach_obj_grad(w, lam, beta):
    n = len(w)
    f = w * w
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


def score_grad_lse(w, beta):
    n = len(w)
    f = w * w
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


t0 = time.time()
best_score = SCORE_ORIG
best_f = f_orig.copy()

# ── Method 1: L-BFGS-B Dinkelbach with ultra-high beta ──
print("\n=== Method 1: L-BFGS Dinkelbach (ultra beta) ===")
w = np.sqrt(f_orig + 1e-30)
lam = SCORE_ORIG

for beta in [1e6, 1e7, 1e8, 1e9, 1e10, 1e11, 1e12]:
    if time.time() - t0 > 1800:
        break
    for outer in range(5):
        res = minimize(
            lambda ww: dinkelbach_obj_grad(ww, lam, beta),
            w,
            method="L-BFGS-B",
            jac=True,
            options={"maxiter": 100, "ftol": 1e-15, "gtol": 1e-15},
        )
        w = res.x
        f = w * w
        conv = fftconvolve(f, f, mode="full")
        if np.all(np.isfinite(conv)) and np.sum(conv) > 0:
            score = score_from_conv(conv)
            lam = score
            if score > best_score + 1e-16:
                best_score = score
                best_f = f.copy()
                print(
                    f"  beta={beta:.0e} outer={outer}: {score:.16f} "
                    f"(+{score-SCORE_ORIG:.2e}) [{time.time()-t0:.1f}s]"
                )
        if res.nit <= 2:
            break
    print(f"  beta={beta:.0e}: {lam:.16f} nit={res.nit} [{time.time()-t0:.1f}s]")

# ── Method 2: Adam with progressive beta cascade ──
print("\n=== Method 2: Adam (extended cascade) ===")
w = np.sqrt(best_f + 1e-30)
b1, b2, eps = 0.9, 0.999, 1e-8

for beta, n_iters, lr in [
    (1e5, 500, 0.001),
    (1e6, 500, 0.0005),
    (1e7, 500, 0.0003),
    (1e8, 500, 0.0001),
    (1e9, 500, 0.00005),
    (1e10, 500, 0.00003),
    (1e11, 500, 0.00001),
    (1e12, 500, 0.000005),
]:
    if time.time() - t0 > 3600:
        break
    m = np.zeros_like(w)
    v = np.zeros_like(w)
    for it in range(n_iters):
        if time.time() - t0 > 3600:
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

    f = w * w
    score = fast_evaluate(f)
    if score > best_score:
        best_score = score
        best_f = f.copy()
    print(f"  beta={beta:.0e} lr={lr}: {score:.16f} [{time.time()-t0:.1f}s]")

# ── Method 3: Perturbation escape ──
print("\n=== Method 3: Perturbation escape ===")
rng = np.random.default_rng(12345)

for trial in range(20):
    if time.time() - t0 > 5400:
        break
    # Random multiplicative perturbation
    noise_scale = rng.choice([0.001, 0.003, 0.01, 0.03, 0.1])
    f_perturbed = f_orig * (1 + rng.normal(0, noise_scale, len(f_orig)))
    f_perturbed = np.maximum(f_perturbed, 0)
    s_init = fast_evaluate(f_perturbed)

    # Quick L-BFGS refinement
    w = np.sqrt(f_perturbed + 1e-30)
    lam = s_init
    for beta in [1e6, 1e8, 1e10]:
        for _ in range(3):
            res = minimize(
                lambda ww: dinkelbach_obj_grad(ww, lam, beta),
                w,
                method="L-BFGS-B",
                jac=True,
                options={"maxiter": 50, "ftol": 1e-15, "gtol": 1e-14},
            )
            w = res.x
            f = w * w
            conv = fftconvolve(f, f, mode="full")
            if np.all(np.isfinite(conv)) and np.sum(conv) > 0:
                lam = score_from_conv(conv)

    score = fast_evaluate(w * w)
    if score > best_score:
        best_score = score
        best_f = (w * w).copy()
        print(f"  trial {trial} (noise={noise_scale:.3f}): {score:.16f} ***NEW BEST***")
    elif trial % 5 == 0:
        print(f"  trial {trial} (noise={noise_scale:.3f}): {score:.16f} [{time.time()-t0:.1f}s]")

# ── Summary ──
total = time.time() - t0
print(f"\n{'='*60}")
print(f"PHASE 1 COMPLETE")
print(f"Original: {SCORE_ORIG:.16f}")
print(f"Best:     {best_score:.16f}")
print(f"Improvement: {best_score - SCORE_ORIG:+.2e}")
print(f"Gap to target: {TARGET - best_score:.10f}")
print(f"Time: {total:.1f}s")

if best_score > SCORE_ORIG + 1e-15:
    np.save(f"{RESULTS}/phase1_best_1600k.npy", best_f)
    data = {"values": best_f.tolist(), "score": best_score, "n": len(best_f)}
    with open(f"{RESULTS}/phase1_best_1600k.json", "w") as fh:
        json.dump(data, fh)
    print(f"Saved improved solution to {RESULTS}/phase1_best_1600k.npy")
else:
    print("No improvement found — confirmed local maximum")
