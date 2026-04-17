"""Campaign 3: Optimize the ORIGINAL ClaudeExplorer 1.6M solution.

Previous campaigns optimized the UPSAMPLED 1.6M (424k nnz, C=0.96270).
The original 1.6M has 1.6M nnz (dense!) and scores C=0.96272.
These are completely different basins (correlation = -0.10).

This script tries to improve the original 1.6M beyond 0.96274 (target).

Approaches:
1. L-BFGS Dinkelbach on original 1.6M (never done before on THIS solution)
2. Coordinated block perturbation (not single ULP)
3. Gradient-informed multi-coordinate update
4. If improvement found at 1.6M, check if submittable
"""

import sys
sys.path.insert(0, "src")

import time
import numpy as np
from scipy.optimize import minimize
from scipy.signal import fftconvolve
from einstein.autocorrelation.fast import fast_evaluate, score_from_conv

TOTAL_TIME = 3600  # 1 hour budget
t_start = time.time()


def elapsed():
    return time.time() - t_start


def remaining():
    return TOTAL_TIME - elapsed()


def log(msg):
    print(f"[{elapsed():6.1f}s] {msg}", flush=True)


# Load original 1.6M
f_orig = np.load("/tmp/original_1600k.npy", allow_pickle=True).astype(np.float64)
n = len(f_orig)
score_orig = fast_evaluate(f_orig)
log(f"Original 1.6M: n={n}, score={score_orig:.16f}")
log(f"Target: 0.96274 (gap = {0.9627433 - score_orig:.7f})")
log(f"nnz={np.count_nonzero(f_orig)}, max={np.max(f_orig):.4f}")

best_f = f_orig.copy()
best_score = score_orig


def update_best(f_new, score_new, tag):
    global best_f, best_score
    if score_new > best_score + 1e-15:
        improvement = score_new - best_score
        best_f = f_new.copy()
        best_score = score_new
        log(f"  *** NEW BEST: {score_new:.16f} (+{improvement:.2e}) [{tag}]")
        return True
    return False


# ============================================================
# Approach 1: L-BFGS Dinkelbach refinement
# ============================================================
log("=" * 60)
log("Approach 1: L-BFGS Dinkelbach on original 1.6M")
log("=" * 60)

w = np.sqrt(np.maximum(f_orig, 0.0))

# Compute initial lambda
conv = fftconvolve(f_orig, f_orig, mode="full")
lam = score_from_conv(conv)
log(f"Initial lambda (C proxy): {lam:.16f}")

beta_schedule = [1e6, 5e6, 1e7, 5e7, 1e8, 5e8, 1e9, 5e9, 1e10]

for beta in beta_schedule:
    if remaining() < 60:
        log("Time limit approaching, skipping remaining betas")
        break

    t_beta = time.time()

    def obj_grad(ww):
        f = ww * ww
        c = fftconvolve(f, f, mode="full")
        if not np.all(np.isfinite(c)) or np.sum(c) <= 0:
            return 1e30, np.zeros_like(ww)

        nc = len(c)
        sum_c2 = np.sum(c * c)
        sum_cc = np.sum(c[:-1] * c[1:])
        numer = 2.0 * sum_c2 + sum_cc
        c_sum = np.sum(c)
        c_max = np.max(c)

        z = np.clip(beta * (c / c_max - 1.0), -700, 0)
        exp_z = np.exp(z)
        mean_exp = np.sum(exp_z) / nc
        proxy = c_max * mean_exp ** (1.0 / beta)
        d_proxy_dc = mean_exp ** (1.0 / beta - 1.0) * exp_z / nc

        denom_val = 3.0 * c_sum * proxy
        phi = numer - lam * denom_val

        dn_dc = 4.0 * c.copy()
        dn_dc[1:] += c[:-1]
        dn_dc[:-1] += c[1:]
        dd_dc = 3.0 * (proxy + c_sum * d_proxy_dc)
        dphi_dc = dn_dc - lam * dd_dc

        dphi_df = 2.0 * fftconvolve(dphi_dc, f[::-1], mode="full")
        dphi_df = dphi_df[n - 1: 2 * n - 1]

        dobj_dw = -dphi_df * 2.0 * ww
        scale = max(abs(numer), 1e-30)
        dobj_dw /= scale
        dobj_dw = np.clip(dobj_dw, -1e6, 1e6)
        dobj_dw = np.nan_to_num(dobj_dw, nan=0.0)

        return float(-phi / scale), dobj_dw

    for outer in range(5):
        if remaining() < 30:
            break

        res = minimize(
            obj_grad, w, method="L-BFGS-B", jac=True,
            options={"maxiter": 200, "ftol": 1e-15, "gtol": 1e-14, "maxfun": 500}
        )
        w = res.x
        f_new = w * w
        conv = fftconvolve(f_new, f_new, mode="full")
        if np.all(np.isfinite(conv)) and np.sum(conv) > 0:
            score = score_from_conv(conv)
            true_score = fast_evaluate(f_new)
            lam = score
            update_best(f_new, true_score, f"lbfgs_beta{beta:.0e}_outer{outer}")

        if res.nit <= 2:
            break

    dt = time.time() - t_beta
    log(f"  beta={beta:.0e}: best={best_score:.16f} ({dt:.1f}s, {res.nit} iters)")

log(f"After L-BFGS: {best_score:.16f} (improvement: {best_score - score_orig:.2e})")


# ============================================================
# Approach 2: Coordinated block perturbation
# ============================================================
if remaining() > 120:
    log("=" * 60)
    log("Approach 2: Coordinated block perturbation")
    log("=" * 60)

    # Identify block structure in original
    active = f_orig > np.max(f_orig) * 1e-6
    active_idx = np.where(active)[0]
    n_active = len(active_idx)
    log(f"Active positions: {n_active} (threshold: {np.max(f_orig) * 1e-6:.4f})")

    # Divide active region into K blocks
    for K in [50, 100, 200, 500]:
        if remaining() < 30:
            break

        block_size = n_active // K
        improvements = 0
        f_trial = best_f.copy()
        trial_score = best_score

        for bi in range(K):
            if remaining() < 10:
                break

            start = active_idx[bi * block_size]
            end = active_idx[min((bi + 1) * block_size, n_active) - 1] + 1

            # Try scaling this block
            for scale in [0.999, 0.9999, 1.0001, 1.001]:
                f_test = f_trial.copy()
                f_test[start:end] *= scale
                s = fast_evaluate(f_test)
                if s > trial_score + 1e-15:
                    trial_score = s
                    f_trial = f_test
                    improvements += 1

        if update_best(f_trial, trial_score, f"block_K{K}"):
            log(f"  K={K}: {improvements} improvements")
        else:
            log(f"  K={K}: no net improvement (tried {K} blocks)")


# ============================================================
# Approach 3: Gradient-informed multi-coordinate update
# ============================================================
if remaining() > 120:
    log("=" * 60)
    log("Approach 3: Gradient-informed coordinate search")
    log("=" * 60)

    f_work = best_f.copy()
    w_work = np.sqrt(np.maximum(f_work, 0.0))

    # Compute gradient of C w.r.t. f
    conv = fftconvolve(f_work, f_work, mode="full")
    nc = len(conv)
    c_sum = np.sum(conv)
    c_max = np.max(conv)

    sum_c2 = np.sum(conv * conv)
    sum_cc = np.sum(conv[:-1] * conv[1:])
    numer = 2.0 * sum_c2 + sum_cc
    denom = 3.0 * c_sum * c_max
    C_val = numer / denom

    dn_dc = 4.0 * conv.copy()
    dn_dc[1:] += conv[:-1]
    dn_dc[:-1] += conv[1:]

    max_idx = np.argmax(conv)
    dd_dc = 3.0 * np.full(nc, c_max)
    dd_dc[max_idx] += 3.0 * c_sum

    dC_dc = (dn_dc * denom - numer * dd_dc) / (denom * denom)

    # dC/df via correlation with reversed f
    dC_df = 2.0 * fftconvolve(dC_dc, f_work[::-1], mode="full")
    dC_df = dC_df[n - 1: 2 * n - 1]

    # Find coordinates with largest positive gradient
    top_pos = np.argsort(dC_df)[-1000:]  # top 1000 positive gradient positions
    top_neg = np.argsort(dC_df)[:1000]   # top 1000 negative gradient positions

    log(f"Max gradient: {np.max(dC_df):.6e}, Min: {np.min(dC_df):.6e}")
    log(f"Top positive grad positions: {len(top_pos)}")

    # Try small perturbations along gradient direction
    for step_size in [1e-6, 1e-5, 1e-4, 1e-3, 1e-2, 1e-1]:
        if remaining() < 30:
            break

        f_test = f_work.copy()
        f_test += step_size * dC_df
        f_test = np.maximum(f_test, 0.0)
        s = fast_evaluate(f_test)
        update_best(f_test, s, f"grad_step_{step_size:.0e}")

    # Try targeted perturbation of top gradient positions only
    for n_coords in [10, 50, 100, 500]:
        if remaining() < 20:
            break

        for step_size in [1e-4, 1e-3, 1e-2]:
            f_test = f_work.copy()
            for idx in top_pos[-n_coords:]:
                f_test[idx] += step_size * abs(dC_df[idx]) / np.max(np.abs(dC_df))
            f_test = np.maximum(f_test, 0.0)
            s = fast_evaluate(f_test)
            if update_best(f_test, s, f"grad_top{n_coords}_step{step_size:.0e}"):
                break


# ============================================================
# Approach 4: Try different resolutions from original
# ============================================================
if remaining() > 120:
    log("=" * 60)
    log("Approach 4: Resolution experiments from original")
    log("=" * 60)

    for target_n in [400000, 800000]:
        if remaining() < 30:
            break

        # Avg-pool original to target_n
        f_pool = np.zeros(target_n)
        for i in range(target_n):
            start = int(i * n / target_n)
            end = int((i + 1) * n / target_n)
            f_pool[i] = np.mean(f_orig[start:end])

        s_pool = fast_evaluate(f_pool)
        log(f"  Avg-pool to {target_n}: C={s_pool:.16f}")

        # Quick L-BFGS refinement
        w_pool = np.sqrt(np.maximum(f_pool, 0.0))
        conv_pool = fftconvolve(f_pool, f_pool, mode="full")
        lam_pool = score_from_conv(conv_pool)

        for beta in [1e6, 1e7, 1e8, 1e9, 1e10]:
            if remaining() < 10:
                break

            def obj_grad_pool(ww, _beta=beta, _lam=lam_pool, _n=target_n):
                f = ww * ww
                c = fftconvolve(f, f, mode="full")
                if not np.all(np.isfinite(c)) or np.sum(c) <= 0:
                    return 1e30, np.zeros_like(ww)
                nc = len(c)
                sum_c2 = np.sum(c * c)
                sum_cc = np.sum(c[:-1] * c[1:])
                numer_v = 2.0 * sum_c2 + sum_cc
                c_sum = np.sum(c)
                c_max = np.max(c)
                z = np.clip(_beta * (c / c_max - 1.0), -700, 0)
                exp_z = np.exp(z)
                mean_exp = np.sum(exp_z) / nc
                proxy = c_max * mean_exp ** (1.0 / _beta)
                d_proxy_dc = mean_exp ** (1.0 / _beta - 1.0) * exp_z / nc
                denom_val = 3.0 * c_sum * proxy
                phi = numer_v - _lam * denom_val
                dn_dc = 4.0 * c.copy()
                dn_dc[1:] += c[:-1]
                dn_dc[:-1] += c[1:]
                dd_dc = 3.0 * (proxy + c_sum * d_proxy_dc)
                dphi_dc = dn_dc - _lam * dd_dc
                dphi_df = 2.0 * fftconvolve(dphi_dc, f[::-1], mode="full")
                dphi_df = dphi_df[_n - 1: 2 * _n - 1]
                dobj_dw = -dphi_df * 2.0 * ww
                scale = max(abs(numer_v), 1e-30)
                dobj_dw /= scale
                dobj_dw = np.clip(dobj_dw, -1e6, 1e6)
                dobj_dw = np.nan_to_num(dobj_dw, nan=0.0)
                return float(-phi / scale), dobj_dw

            res = minimize(
                obj_grad_pool, w_pool, method="L-BFGS-B", jac=True,
                options={"maxiter": 300, "ftol": 1e-15, "gtol": 1e-14}
            )
            w_pool = res.x
            f_pool = w_pool * w_pool
            conv_pool = fftconvolve(f_pool, f_pool, mode="full")
            if np.all(np.isfinite(conv_pool)) and np.sum(conv_pool) > 0:
                lam_pool = score_from_conv(conv_pool)

        s_refined = fast_evaluate(f_pool)
        log(f"  After L-BFGS at {target_n}: C={s_refined:.16f}")

        # Save if competitive
        if s_refined > 0.96274:
            np.save(f"/tmp/solution_{target_n}_c3.npy", f_pool)
            log(f"  *** SUBMITTABLE! Saved to /tmp/solution_{target_n}_c3.npy")


# ============================================================
# Approach 5: From-scratch long training at small n
# ============================================================
if remaining() > 300:
    log("=" * 60)
    log("Approach 5: Long from-scratch at n=768 (seeking new basin)")
    log("=" * 60)

    from scripts.autocorrelation.dinkelbach_cpu_v2 import score_grad_lse

    n_small = 768
    n_seeds = 20
    best_small_score = 0
    best_small_f = None

    time_per_seed = min(remaining() / (n_seeds + 1), 30)

    for seed in range(n_seeds):
        if remaining() < 60:
            break

        rng = np.random.default_rng(seed * 137 + 42)

        # Different initialization strategies
        if seed < 5:
            # Random block
            w_init = np.zeros(n_small)
            width = rng.integers(20, 50)
            start = rng.integers(0, n_small - width)
            w_init[start:start+width] = rng.exponential(1.0, width)
        elif seed < 10:
            # Multiple blocks
            w_init = np.zeros(n_small)
            n_blocks = rng.integers(3, 10)
            for _ in range(n_blocks):
                width = rng.integers(5, 30)
                start = rng.integers(0, max(1, n_small - width))
                w_init[start:start+width] = rng.exponential(0.5, width)
        elif seed < 15:
            # Uniform + noise
            w_init = rng.uniform(0.5, 1.5, n_small)
        else:
            # Sparse random
            w_init = np.zeros(n_small)
            n_pts = rng.integers(50, 200)
            positions = rng.choice(n_small, n_pts, replace=False)
            w_init[positions] = rng.exponential(1.0, n_pts)

        # Extended Adam schedule (much longer than default)
        schedule = [
            (10, 5000, 0.01),
            (30, 5000, 0.005),
            (100, 5000, 0.003),
            (300, 5000, 0.001),
            (1000, 5000, 0.0005),
            (3000, 3000, 0.0003),
            (10000, 3000, 0.0001),
            (30000, 2000, 0.00005),
            (100000, 2000, 0.00003),
        ]

        # Run Adam
        w = w_init.copy()
        b1, b2, eps = 0.9, 0.999, 1e-8
        m = np.zeros_like(w)
        v = np.zeros_like(w)
        seed_best = 0
        seed_best_w = w.copy()
        t_seed = time.time()

        for beta, n_iters, lr in schedule:
            if time.time() - t_seed > time_per_seed:
                break
            m[:] = 0
            v[:] = 0
            for it in range(n_iters):
                if time.time() - t_seed > time_per_seed:
                    break
                _, grad = score_grad_lse(w, n_small, beta)
                grad = np.clip(grad, -1e6, 1e6)
                grad = np.nan_to_num(grad, nan=0.0)
                m = b1 * m + (1 - b1) * grad
                v = b2 * v + (1 - b2) * grad * grad
                mh = m / (1 - b1 ** (it + 1))
                vh = v / (1 - b2 ** (it + 1))
                w = w + lr * mh / (np.sqrt(vh) + eps)
                w = np.maximum(w, 0)

            s = fast_evaluate(w * w)
            if s > seed_best:
                seed_best = s
                seed_best_w = w.copy()

        if seed_best > best_small_score:
            best_small_score = seed_best
            best_small_f = (seed_best_w * seed_best_w).copy()
            log(f"  Seed {seed}: C={seed_best:.8f} *** NEW BEST")

        if seed_best > 0.90:
            log(f"  Seed {seed}: C={seed_best:.8f}")

    if best_small_f is not None:
        log(f"Best from-scratch at n={n_small}: {best_small_score:.8f}")


# ============================================================
# Summary
# ============================================================
log("=" * 60)
log("CAMPAIGN 3 SUMMARY")
log("=" * 60)
log(f"Original 1.6M score: {score_orig:.16f}")
log(f"Best achieved:       {best_score:.16f}")
log(f"Improvement:         {best_score - score_orig:.2e}")
log(f"Target:              0.9627433187626762")
log(f"Gap to target:       {0.9627433187626762 - best_score:.2e}")
log(f"Can submit #1?       {'YES' if best_score > 0.9627433 else 'NO'}")
log(f"Total time:          {elapsed():.1f}s")

# Save best solution
np.save("/tmp/campaign3_best.npy", best_f)
log(f"Best solution saved to /tmp/campaign3_best.npy")
