"""CVXPY-based optimization for Erdős Minimum Overlap.

Uses convex relaxation / iterative reweighted approaches.
Key insight from White (2022): in the Fourier domain, the optimal overlap
function has all even cosine coefficients A_{2m} <= 0.

This script tries:
1. LP relaxation at reduced dimension (aggregate bins)
2. Iterative reweighted LP (cutting plane method)
3. White's SOCP formulation for Fourier coefficients
"""

import json
import sys
import time
from pathlib import Path

import numpy as np
from scipy.signal import fftconvolve

sys.path.insert(0, "src")
from einstein.erdos.fast import fast_evaluate
from einstein.erdos.evaluator import evaluate as exact_evaluate

RESULTS_DIR = Path("results/problem-1-erdos-overlap")
ARENA_SOTA = 0.3808703105862199
TARGET = ARENA_SOTA - 1e-6


def approach_cutting_plane(n: int = 600, max_iters: int = 100):
    """Cutting plane method for minimax correlation.

    Start with a small set of active lags, solve LP, add violated constraints.
    """
    import cvxpy as cp

    print("\n" + "=" * 60)
    print("CVXPY APPROACH 1: Cutting plane LP")
    print("=" * 60)

    # Variables
    h = cp.Variable(n, nonneg=True)
    t = cp.Variable()  # Minimax bound

    # Fixed constraints
    constraints = [
        h >= 0,
        h <= 1,
        cp.sum(h) == n / 2.0,
    ]

    # Start with a few lag constraints
    # For lag s: C(s) = sum_i h[i]*(1-h[i+s]) * 2/n
    # This is quadratic in h, so we linearize around current point

    # Initialize from SOTA
    sota_path = RESULTS_DIR / "sota_rank1_Together-AI_0.380870310586.json"
    with open(sota_path) as f:
        sol = json.load(f)
    h_curr = np.array(sol["data"]["values"], dtype=np.float64)

    best_score = fast_evaluate(h_curr)
    best_h = h_curr.copy()
    print(f"  Start: C={best_score:.13f}")

    for iteration in range(max_iters):
        # Compute correlations at current point
        corr = fftconvolve(h_curr, (1.0 - h_curr)[::-1], mode="full")
        C_vals = corr * 2.0 / n
        C_max = np.max(C_vals)

        # Find violated/active lags (top 20)
        active = np.argsort(C_vals)[-20:]

        # Linearize each C(s) around h_curr:
        # C(s) ≈ C(s)|h_curr + grad_s . (h - h_curr)
        # grad_s[i] = ((1 - h_curr[i+s]) - h_curr[i-s]) * 2/n
        lag_constraints = []
        for lag_idx in active:
            s = lag_idx - (n - 1)
            # Linear approximation
            grad = np.zeros(n)
            for i in range(n):
                g = 0.0
                ip = i + s
                im = i - s
                if 0 <= ip < n:
                    g += (1.0 - h_curr[ip])
                if 0 <= im < n:
                    g -= h_curr[im]
                grad[i] = g * 2.0 / n

            C_at_curr = C_vals[lag_idx]
            # Linearized constraint: C_at_curr + grad . (h - h_curr) <= t
            lag_constraints.append(C_at_curr + grad @ (h - h_curr) <= t)

        # Solve LP
        prob = cp.Problem(cp.Minimize(t), constraints + lag_constraints)
        try:
            prob.solve(solver=cp.CLARABEL, verbose=False)
        except Exception as e:
            print(f"  Solver error at iter {iteration}: {e}")
            break

        if prob.status not in ["optimal", "optimal_inaccurate"]:
            print(f"  LP infeasible/unbounded at iter {iteration}: {prob.status}")
            break

        h_new = np.array(h.value).flatten()
        h_new = np.clip(h_new, 0, 1)
        target = n / 2.0
        h_new *= target / np.sum(h_new)
        h_new = np.clip(h_new, 0, 1)

        new_score = fast_evaluate(h_new)

        if new_score < best_score:
            improvement = best_score - new_score
            best_score = new_score
            best_h = h_new.copy()
            h_curr = h_new
            if improvement > 1e-10:
                print(f"    iter {iteration}: C={best_score:.13f} (imp={improvement:.2e})")
        else:
            # Mix: step towards LP solution
            alpha = 0.3
            h_mixed = alpha * h_new + (1 - alpha) * h_curr
            mixed_score = fast_evaluate(h_mixed)
            if mixed_score < best_score:
                best_score = mixed_score
                best_h = h_mixed.copy()
                h_curr = h_mixed
            else:
                # No progress
                if iteration > 10:
                    print(f"  No progress at iter {iteration}, stopping")
                    break
                h_curr = h_new  # Still update linearization point

    print(f"  Final: C={best_score:.13f}")
    return best_h, best_score


def approach_fourier_socp(K: int = 50, n: int = 600):
    """White's SOCP formulation in the Fourier domain.

    Key identity: C(k) = 1/2 - (1/n^2) * sum_{f} |H(f)|^2 * cos(2*pi*f*k/n)

    Minimize max_k C(k) by optimizing |H(f)|^2 subject to:
    - h(x) in [0, 1] (spectral constraints)
    - H(0) = n/2 (sum constraint)
    """
    import cvxpy as cp

    print("\n" + "=" * 60)
    print(f"CVXPY APPROACH 2: Fourier SOCP (K={K})")
    print("=" * 60)

    # We optimize the power spectrum P(f) = |H(f)|^2 / n
    # Only need f = 0, 1, ..., n//2 by symmetry
    n_freq = n // 2 + 1

    # Reduce to K frequencies
    K_actual = min(K, n_freq)
    print(f"  Using {K_actual} frequency components")

    # Variables: power spectrum values P(f) for f = 1, ..., K
    # P(0) = (n/2)^2 / n = n/4 (fixed by sum constraint)
    P = cp.Variable(K_actual - 1, nonneg=True)
    t = cp.Variable()  # Minimax bound

    # The correlation at lag k:
    # C(k) = 1/2 - (2/n) * sum_{f=1}^{n/2} P(f) * cos(2*pi*f*k/n)
    #       + (1/n) * P(0) * ... (DC term is fixed)
    # Simplified: C(k) ≈ const - (2/n) * sum_{f} P(f) * cos(2*pi*f*k/n)

    # Actually, let's compute C(k) directly in terms of power spectrum.
    # autocorr(k) = IFFT(|H|^2)[k] = sum_f |H(f)|^2 * exp(2*pi*i*f*k/n) / n
    # For real h: autocorr(k) = P(0)/n + 2/n * sum_{f=1}^{n/2-1} P(f) * cos(2*pi*f*k/n) + P(n/2)/n * cos(pi*k)
    # And C(k) = n/2 * 2/n - autocorr(k) * 2/n = 1 - 2*autocorr(k)/n

    # Wait, let's be more careful.
    # correlate(h, 1-h, 'full') at lag k = sum_i h[i] * (1 - h[i-k])
    #   = sum(h) - autocorr(k) = n/2 - autocorr(k)
    # C = max_k (n/2 - autocorr(k)) * 2/n = 1 - min_k autocorr(k) * 2/n

    # So minimizing C = maximizing min_k autocorr(k)
    # autocorr(k) = sum_f |H(f)|^2 * cos(2*pi*f*k/n) (for real h)
    #             = P(0) + 2 * sum_{f=1}^{n/2-1} P(f) * cos(2*pi*f*k/n) + P(n/2) * cos(pi*k)

    # where P(f) = |H(f)|^2 for our purposes (not normalized by n)

    # We want to maximize min_k autocorr(k), equivalently minimize -min_k autocorr(k)
    # = minimize max_k (-autocorr(k))

    P0 = (n / 2.0) ** 2  # Fixed: |H(0)|^2 = (sum(h))^2 = (n/2)^2

    constraints = [P >= 0]

    # For a subset of lags, add: -autocorr(k) <= t
    # i.e., P0 + 2*sum P(f)*cos(...) + ... >= -t
    # i.e., t >= -autocorr(k) for all k

    n_lags = 2 * n - 1
    # Sample lags uniformly
    lag_indices = list(range(n_lags))

    for lag_idx in lag_indices:
        k = lag_idx - (n - 1)  # Actual shift, range [-(n-1), n-1]
        # autocorr(k) for full (non-circular) correlation is more complex
        # Let's just use a representative set

        # For the linear correlation (not circular), the relationship is:
        # correlate(h, 1-h, 'full')[k] = sum_{i} h[i] * (1 - h[i - (k - n + 1)])
        # This is harder to express in Fourier domain cleanly.
        pass

    # The Fourier approach works cleanly for CIRCULAR correlation.
    # For the arena's LINEAR correlation, the connection is less direct.
    # Let me use the circular approximation (which is tight for n >> 1).

    # For circular correlation:
    # autocorr_circ(k) = P(0) + 2*sum_{f=1}^{n/2-1} P(f)*cos(2*pi*f*k/n) + P(n/2)*(-1)^k
    # where P(f) = |H(f)|^2 (unnormalized)

    # We fix P(0) = (n/2)^2 and have P(1),...,P(n/2) as variables

    # Parseval: sum(h^2) = sum P(f) / n
    # For h in [0,1]: sum(h^2) <= sum(h) = n/2, so sum P(f) <= n^2/2

    constraints.append(cp.sum(P) <= n**2 / 2 - P0)

    # Maximize min_k autocorr(k) = minimize t where -autocorr(k) <= t for all k
    for k in range(n):
        cos_vals = np.array([np.cos(2 * np.pi * f * k / n) for f in range(1, K_actual)])
        autocorr_k = P0 + 2 * cos_vals @ P
        if K_actual <= n // 2:
            pass  # Ignore higher frequencies
        constraints.append(-autocorr_k <= t)

    # Minimize t (maximize minimum autocorrelation)
    prob = cp.Problem(cp.Minimize(t), constraints)

    try:
        prob.solve(solver=cp.CLARABEL, verbose=False, max_iter=10000)
    except Exception as e:
        print(f"  Solver error: {e}")
        return None, ARENA_SOTA

    if prob.status not in ["optimal", "optimal_inaccurate"]:
        print(f"  Problem status: {prob.status}")
        return None, ARENA_SOTA

    P_opt = np.array(P.value).flatten()
    t_opt = float(t.value)
    print(f"  Optimal t (neg min autocorr): {t_opt:.10f}")

    # Reconstruct h from power spectrum
    # We know |H(f)|^2 but not the phases. Try multiple random phases.
    best_score = ARENA_SOTA
    best_h = None

    H_mags = np.zeros(n_freq)
    H_mags[0] = n / 2.0  # DC
    H_mags[1:K_actual] = np.sqrt(np.maximum(0, P_opt))

    for phase_trial in range(100):
        rng = np.random.default_rng(phase_trial)
        H_complex = np.zeros(n_freq, dtype=complex)
        H_complex[0] = H_mags[0]
        phases = rng.uniform(0, 2 * np.pi, K_actual - 1)
        H_complex[1:K_actual] = H_mags[1:K_actual] * np.exp(1j * phases)

        h_reconstructed = np.fft.irfft(H_complex, n=n)
        h_reconstructed = np.clip(h_reconstructed, 0, 1)
        target = n / 2.0
        s = np.sum(h_reconstructed)
        if s > 0:
            h_reconstructed *= target / s
        h_reconstructed = np.clip(h_reconstructed, 0, 1)
        s = np.sum(h_reconstructed)
        if s > 0:
            h_reconstructed *= target / s

        score = fast_evaluate(h_reconstructed)
        if score < best_score:
            best_score = score
            best_h = h_reconstructed.copy()

    print(f"  Best reconstruction: C={best_score:.13f}")
    return best_h, best_score


def approach_reduced_lp(n_bins: int = 60, n_full: int = 600):
    """Solve at reduced resolution (aggregate bins), then upsample and polish."""
    import cvxpy as cp

    print("\n" + "=" * 60)
    print(f"CVXPY APPROACH 3: Reduced LP (n_bins={n_bins}) + upsample")
    print("=" * 60)

    # At reduced resolution, each bin represents n_full/n_bins original bins
    ratio = n_full // n_bins

    # Variables
    h = cp.Variable(n_bins, nonneg=True)
    t = cp.Variable()

    constraints = [
        h >= 0,
        h <= 1,
        cp.sum(h) == n_bins / 2.0,
    ]

    # For each lag k, linearize correlation constraint
    # correlate(h, 1-h) at lag k (at reduced resolution)
    n_lags = 2 * n_bins - 1

    for lag_idx in range(n_lags):
        k = lag_idx - (n_bins - 1)
        # correlate(h, 1-h, 'full') at position lag_idx
        # = sum_i h[i] * (1 - h[i - k]) where valid
        # This is quadratic — need to linearize or use different formulation

        # For LP: use the identity that for fixed g = 1-h:
        # sum h[i] * g[i-k] where g is not a variable
        # But g = 1-h so it IS a variable.

        # Use McCormick relaxation: h[i]*(1-h[j]) <= h[i], <= 1-h[j], >= 0
        # That gives a valid upper bound on each correlation.
        pass

    # Actually, the minimax of bilinear form is NP-hard in general.
    # But we can use iterative linearization (which is what SLP does).
    # Let me just solve at reduced n directly with SLP.

    # Initialize with downsampled SOTA
    sota_path = RESULTS_DIR / "sota_rank1_Together-AI_0.380870310586.json"
    with open(sota_path) as f:
        sol = json.load(f)
    h_full = np.array(sol["data"]["values"], dtype=np.float64)
    h_reduced = h_full.reshape(n_bins, ratio).mean(axis=1)
    h_reduced = np.clip(h_reduced, 0, 1)
    target = n_bins / 2.0
    h_reduced *= target / np.sum(h_reduced)
    h_reduced = np.clip(h_reduced, 0, 1)

    score_reduced = fast_evaluate(h_reduced)
    print(f"  Downsampled SOTA at n={n_bins}: {score_reduced:.10f}")

    # Try cold-start SLP at reduced dimension
    rng = np.random.default_rng(42)
    best_score = score_reduced
    best_h_reduced = h_reduced.copy()

    # Try several random starts at reduced dimension
    for trial in range(20):
        if trial == 0:
            h_init = h_reduced.copy()
        else:
            h_init = rng.random(n_bins)
            h_init = np.clip(h_init, 0, 1)
            h_init *= target / np.sum(h_init)

        # Quick local search at reduced dimension
        h_opt = h_init.copy()
        best_local = fast_evaluate(h_opt)

        for _ in range(200_000):
            k = rng.choice([2, 3])
            idx = rng.choice(n_bins, size=k, replace=False)
            delta = rng.standard_normal(k) * 1e-5
            delta -= delta.mean()
            old = h_opt[idx].copy()
            new_vals = old + delta
            if np.any(new_vals < 0) or np.any(new_vals > 1):
                continue
            h_opt[idx] = new_vals
            s = fast_evaluate(h_opt)
            if s < best_local:
                best_local = s
            else:
                h_opt[idx] = old

        print(f"  Trial {trial} at n={n_bins}: {best_local:.10f}")
        if best_local < best_score:
            best_score = best_local
            best_h_reduced = h_opt.copy()

    # Upsample best reduced solution to full resolution
    h_upsampled = np.repeat(best_h_reduced, ratio)
    h_upsampled = np.clip(h_upsampled, 0, 1)
    target_full = n_full / 2.0
    h_upsampled *= target_full / np.sum(h_upsampled)

    # Polish at full resolution
    score_up = fast_evaluate(h_upsampled)
    print(f"\n  Upsampled to n={n_full}: {score_up:.10f}")

    # Polish
    best_full = score_up
    h_full_opt = h_upsampled.copy()
    for _ in range(500_000):
        k = rng.choice([2, 3, 4])
        idx = rng.choice(n_full, size=k, replace=False)
        delta = rng.standard_normal(k) * 1e-7
        delta -= delta.mean()
        old = h_full_opt[idx].copy()
        new_vals = old + delta
        if np.any(new_vals < 0) or np.any(new_vals > 1):
            continue
        h_full_opt[idx] = new_vals
        s = fast_evaluate(h_full_opt)
        if s < best_full:
            best_full = s
        else:
            h_full_opt[idx] = old

    print(f"  Polished: {best_full:.13f}")
    return h_full_opt, best_full


def main():
    t_start = time.time()

    print("=" * 60)
    print("Erdős Minimum Overlap — CVXPY Optimization Approaches")
    print(f"SOTA: {ARENA_SOTA:.16f}")
    print(f"TARGET: {TARGET:.16f}")
    print("=" * 60)

    results = {}

    # Approach 1: Cutting plane
    t0 = time.time()
    h1, s1 = approach_cutting_plane(n=600, max_iters=50)
    results["cutting_plane"] = (s1, time.time() - t0)

    # Approach 2: Fourier SOCP
    t0 = time.time()
    h2, s2 = approach_fourier_socp(K=50, n=600)
    results["fourier_socp"] = (s2, time.time() - t0)

    # Approach 3: Reduced LP
    t0 = time.time()
    h3, s3 = approach_reduced_lp(n_bins=60, n_full=600)
    results["reduced_lp"] = (s3, time.time() - t0)

    # Summary
    elapsed = time.time() - t_start
    print("\n" + "=" * 60)
    print("CVXPY SUMMARY")
    print("=" * 60)
    for name, (score, t) in sorted(results.items(), key=lambda x: x[1][0]):
        diff = score - ARENA_SOTA
        status = "BEATS!" if score < TARGET else "no"
        print(f"  {name:<20} {score:.13f}  {diff:+.2e}  {t:.0f}s  {status}")

    best_name = min(results, key=lambda k: results[k][0])
    best_score = results[best_name][0]
    print(f"\nBest: {best_name} = {best_score:.16f}")
    print(f"Beats SOTA by 1e-6? {'YES' if best_score < TARGET else 'NO'}")
    print(f"Total time: {elapsed:.0f}s")


if __name__ == "__main__":
    main()
