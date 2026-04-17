"""Phase 2: Optimize at untested mid-resolution n values.

The push campaign tested: 100k, 400k, 800k, 1.6M
This tests: 500k, 600k, 700k — potentially hitting a lucky basin.

Also tries different transplant methods for each n.
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

f_orig_1600k = np.load(
    os.path.expanduser(
        "~/projects/einstein/cb/results/problem-3-autocorrelation/best_1600k.npy"
    )
)
f_sota_400k = np.load("/tmp/sota_400k.npy")

TARGET = 0.9627433187626762
best_overall = 0.0
best_overall_f = None
best_overall_tag = ""
t_start = time.time()


def log(msg):
    print(f"[{time.time()-t_start:7.1f}s] {msg}", flush=True)


def save_if_best(f, score, tag):
    global best_overall, best_overall_f, best_overall_tag
    if score > best_overall:
        best_overall = score
        best_overall_f = f.copy()
        best_overall_tag = tag
        np.save(f"{RESULTS}/phase2_{tag}_n{len(f)}.npy", f)
        gap = score - TARGET
        status = "SUBMITTABLE!" if gap >= 0 else f"short by {-gap:.10f}"
        log(f"*** NEW BEST: {score:.16f} ({tag}, n={len(f)}) — {status}")


def upsample_linear(f, target_n):
    x_old = np.linspace(0, 1, len(f))
    x_new = np.linspace(0, 1, target_n)
    return np.maximum(np.interp(x_new, x_old, f), 0)


def avg_pool_transplant(f, target_n, threshold=0):
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


def block_avg_downsample(f, target_n):
    """Downsample by averaging blocks of source values."""
    n = len(f)
    result = np.zeros(target_n)
    for i in range(target_n):
        s = int(i * n / target_n)
        e = int((i + 1) * n / target_n)
        result[i] = np.mean(f[s:e])
    return result


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


def optimize_at_n(f_init, n_target, tag, time_budget):
    """Full Adam + L-BFGS optimization at given n."""
    t0 = time.time()
    w = np.sqrt(f_init + 1e-30)
    best_score = fast_evaluate(f_init)
    best_w = w.copy()

    log(f"  {tag}: init score={best_score:.16f}")
    save_if_best(f_init, best_score, f"{tag}_init")

    # Phase A: Adam cascade (60% of time)
    adam_time = time_budget * 0.6
    b1, b2, eps = 0.9, 0.999, 1e-8

    for beta, n_iters, lr in [
        (1e3, 300, 0.003),
        (1e4, 300, 0.001),
        (3e4, 300, 0.0007),
        (1e5, 300, 0.0005),
        (3e5, 300, 0.0003),
        (1e6, 300, 0.0002),
        (3e6, 300, 0.0001),
        (1e7, 300, 0.00005),
        (3e7, 300, 0.00003),
        (1e8, 300, 0.00001),
        (3e8, 300, 0.000005),
        (1e9, 200, 0.000003),
        (1e10, 200, 0.000001),
    ]:
        if time.time() - t0 > adam_time:
            break
        m = np.zeros_like(w)
        v = np.zeros_like(w)
        for it in range(n_iters):
            if time.time() - t0 > adam_time:
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
            best_w = w.copy()
            save_if_best(f, score, f"{tag}_adam_b{beta:.0e}")

    # Phase B: L-BFGS Dinkelbach (40% of time)
    w = best_w.copy()
    lam = best_score
    lbfgs_time = time_budget - (time.time() - t0)

    for beta in [1e6, 1e7, 1e8, 1e9, 1e10, 1e11, 1e12]:
        if time.time() - t0 > time_budget:
            break
        for outer in range(5):
            if time.time() - t0 > time_budget:
                break
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
                if score > best_score:
                    best_score = score
                    best_w = w.copy()
                    save_if_best(f, score, f"{tag}_lbfgs_b{beta:.0e}")
            if res.nit <= 2:
                break

    log(f"  {tag}: FINAL score={best_score:.16f} ({time.time()-t0:.1f}s)")
    return best_w * best_w, best_score


# ══════════════════════════════════════════════════════════════════════
log("Starting Phase 2: Mid-Resolution Sweep")
log(f"Target: {TARGET:.16f}")

# Time budget: 3 hours = 10800s
TOTAL_TIME = 10800
PER_N_TIME = 1200  # 20 min per n value

for n_target in [500000, 600000, 700000, 800000]:
    if time.time() - t_start > TOTAL_TIME - 600:
        log(f"Time limit approaching, skipping n={n_target}")
        break

    log(f"\n{'='*60}")
    log(f"n = {n_target}")
    log(f"{'='*60}")

    # Method 1: Upsample from SOTA 400k
    f_up = upsample_linear(f_sota_400k, n_target)
    optimize_at_n(f_up, n_target, f"up400k_n{n_target//1000}k", PER_N_TIME)

    # Method 2: Avg-pool transplant from 1.6M
    f_tp = avg_pool_transplant(f_orig_1600k, n_target)
    optimize_at_n(f_tp, n_target, f"tp16m_n{n_target//1000}k", PER_N_TIME)

    # Method 3: Block-average downsample from 1.6M
    f_ds = block_avg_downsample(f_orig_1600k, n_target)
    optimize_at_n(f_ds, n_target, f"ds16m_n{n_target//1000}k", PER_N_TIME)

    # Method 4: Transplant with threshold
    f_tp2 = avg_pool_transplant(f_orig_1600k, n_target, threshold=1e-3)
    optimize_at_n(f_tp2, n_target, f"tpt1e3_n{n_target//1000}k", PER_N_TIME)

# Final summary
log(f"\n{'='*60}")
log(f"PHASE 2 COMPLETE")
log(f"Best overall: {best_overall:.16f} ({best_overall_tag})")
log(f"Gap to target: {TARGET - best_overall:.10f}")
log(f"Total time: {time.time()-t_start:.1f}s")

if best_overall_f is not None:
    n = len(best_overall_f)
    data = {"values": best_overall_f.tolist(), "score": best_overall, "n": n, "tag": best_overall_tag}
    with open(f"{RESULTS}/phase2_best.json", "w") as fh:
        json.dump(data, fh)
    log(f"Saved best to {RESULTS}/phase2_best.json")

    # Estimate JSON size
    nnz = np.count_nonzero(best_overall_f)
    est_size = nnz * 18 + (n - nnz) * 2
    log(f"Estimated JSON payload: {est_size/1e6:.1f}MB (n={n}, nnz={nnz})")
