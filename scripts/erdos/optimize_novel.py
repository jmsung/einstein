"""Novel optimization approaches for Erdős Minimum Overlap (Problem 1).

Tries genuinely unexplored angles beyond the 37 prior experiments.
CPU-only (M4 Mac). Target: beat 0.3808703105862199 by > 1e-6.

Approaches:
1. Spectral flattening via ADMM (alternating direction method of multipliers)
2. Multi-n global search (diverse n values, not just n=600)
3. Cosine-basis parameterization with differential evolution
4. Subgradient projection with momentum (Polyak step)
5. Random restarts from analytical constructions (Haugland-style)
"""

import json
import sys
import time
from pathlib import Path

import numpy as np
from scipy.optimize import differential_evolution, minimize
from scipy.signal import fftconvolve

sys.path.insert(0, "src")
from einstein.erdos.evaluator import evaluate as exact_evaluate
from einstein.erdos.fast import fast_evaluate

RESULTS_DIR = Path("results/problem-1-erdos-overlap")
RESULTS_DIR.mkdir(parents=True, exist_ok=True)

ARENA_SOTA = 0.3808703105862199
TARGET = ARENA_SOTA - 1e-6  # Must beat by minImprovement


def score_fft(h: np.ndarray) -> float:
    """Fast FFT-based scoring."""
    n = len(h)
    s = np.sum(h)
    target = n / 2.0
    if s == 0:
        return float("inf")
    if s != target:
        h = h * (target / s)
    if np.any(h > 1.0) or np.any(h < 0.0):
        return float("inf")
    corr = fftconvolve(h, (1.0 - h)[::-1], mode="full")
    return float(np.max(corr)) / n * 2


def score_logsumexp(h: np.ndarray, beta: float = 1e6) -> float:
    """Smooth approximation of max via LogSumExp for gradient-based optimization."""
    n = len(h)
    s = np.sum(h)
    target = n / 2.0
    if s == 0:
        return float("inf")
    if s != target:
        h = h * (target / s)
    if np.any(h > 1.0) or np.any(h < 0.0):
        return float("inf")
    corr = fftconvolve(h, (1.0 - h)[::-1], mode="full")
    corr_scaled = corr / n * 2
    # LogSumExp smooth max
    c_max = np.max(corr_scaled)
    return c_max + np.log(np.sum(np.exp(beta * (corr_scaled - c_max)))) / beta


# ============================================================
# Approach 1: Multi-n exploration with aggressive warm-start
# ============================================================
def approach_multi_n(sota_values: np.ndarray, n_list: list[int], iters_per_n: int = 500_000):
    """Try different discretization sizes with interpolation from SOTA."""
    print("\n" + "=" * 60)
    print("APPROACH 1: Multi-n exploration")
    print("=" * 60)

    best_overall = ARENA_SOTA
    best_h = None

    for n_new in n_list:
        n_old = len(sota_values)
        # Interpolate SOTA to new grid
        x_old = np.linspace(0, 1, n_old, endpoint=False)
        x_new = np.linspace(0, 1, n_new, endpoint=False)
        h = np.interp(x_new, x_old, sota_values)
        # Ensure constraints
        h = np.clip(h, 0, 1)
        target = n_new / 2.0
        h *= target / np.sum(h)
        h = np.clip(h, 0, 1)
        h *= target / np.sum(h)  # Re-normalize after clip

        start_score = score_fft(h)
        print(f"\n  n={n_new}: interpolated score = {start_score:.13f}")

        if start_score >= ARENA_SOTA + 0.001:
            print(f"  Skipping n={n_new} (too far from SOTA)")
            continue

        # Polish with multi-point mass transport
        rng = np.random.default_rng(42 + n_new)
        improved = 0
        best_n = start_score

        for trial in range(iters_per_n):
            k = rng.choice([2, 3, 4, 5, 6])
            idx = rng.choice(n_new, size=k, replace=False)
            delta = rng.standard_normal(k) * 1e-7
            delta -= delta.mean()

            old = h[idx].copy()
            new_vals = old + delta
            if np.any(new_vals < 0) or np.any(new_vals > 1):
                continue

            h[idx] = new_vals
            s = score_fft(h)
            if s < best_n:
                best_n = s
                improved += 1
            else:
                h[idx] = old

            if (trial + 1) % 200_000 == 0:
                print(f"    iter {trial+1}: C={best_n:.13f}, improved={improved}")

        print(f"  n={n_new} final: {best_n:.13f} (improved {improved} times)")
        if best_n < best_overall:
            best_overall = best_n
            best_h = h.copy()

    return best_h, best_overall


# ============================================================
# Approach 2: Cosine-basis parameterization + differential evolution
# ============================================================
def cosine_construction(params: np.ndarray, n: int = 600) -> np.ndarray:
    """Construct h from cosine-basis coefficients.

    h(x) = 0.5 + sum_k a_k * cos(2*pi*k*x) + b_k * sin(2*pi*k*x)
    Clipped to [0, 1] and normalized.
    """
    K = len(params) // 2
    x = np.linspace(0, 1, n, endpoint=False)
    h = np.full(n, 0.5)
    for k in range(K):
        h += params[2*k] * np.cos(2 * np.pi * (k+1) * x)
        h += params[2*k+1] * np.sin(2 * np.pi * (k+1) * x)
    h = np.clip(h, 0, 1)
    target = n / 2.0
    s = np.sum(h)
    if s > 0:
        h *= target / s
    h = np.clip(h, 0, 1)
    s = np.sum(h)
    if s > 0:
        h *= target / s
    return h


def approach_cosine_de(K_values: list[int] = [10, 20, 30, 50], n: int = 600,
                       maxiter: int = 200, popsize: int = 15):
    """Differential evolution in cosine-basis parameter space."""
    print("\n" + "=" * 60)
    print("APPROACH 2: Cosine-basis + Differential Evolution")
    print("=" * 60)

    best_overall = ARENA_SOTA
    best_h = None

    for K in K_values:
        print(f"\n  K={K} ({2*K} params)...")

        def objective(params):
            h = cosine_construction(params, n)
            return score_fft(h)

        bounds = [(-0.5, 0.5)] * (2 * K)
        t0 = time.time()

        result = differential_evolution(
            objective, bounds, maxiter=maxiter, popsize=popsize,
            tol=1e-12, seed=42, disp=False, workers=1
        )

        elapsed = time.time() - t0
        print(f"  K={K}: score={result.fun:.13f}, time={elapsed:.0f}s")

        if result.fun < best_overall:
            best_overall = result.fun
            best_h = cosine_construction(result.x, n)

    return best_h, best_overall


# ============================================================
# Approach 3: Subgradient projection with Polyak step
# ============================================================
def approach_subgradient(h_init: np.ndarray, n_iters: int = 50000):
    """Projected subgradient descent with Polyak step size."""
    print("\n" + "=" * 60)
    print("APPROACH 3: Subgradient projection (Polyak step)")
    print("=" * 60)

    h = h_init.copy()
    n = len(h)
    best_score = score_fft(h)
    best_h = h.copy()
    print(f"  Start: C={best_score:.13f}")

    for iteration in range(n_iters):
        # Compute all correlations
        corr = fftconvolve(h, (1.0 - h)[::-1], mode="full")
        C_vals = corr / n * 2
        max_idx = np.argmax(C_vals)
        C_max = C_vals[max_idx]

        # Find all lags within epsilon of max (active set)
        eps = 1e-9
        active = np.where(C_vals >= C_max - eps)[0]

        # Compute subgradient: average over active lags
        # For lag s: d/dh[i] of corr_s = (1 - h[i+s]) - h[i-s]
        # where indexing wraps or is zero-padded
        grad = np.zeros(n)
        for lag_idx in active:
            s = lag_idx - (n - 1)  # Convert to actual shift
            for i in range(n):
                i_plus_s = i + s
                i_minus_s = i - s
                g = 0.0
                if 0 <= i_plus_s < n:
                    g += (1.0 - h[i_plus_s])
                if 0 <= i_minus_s < n:
                    g -= h[i_minus_s]
                grad[i] += g
        grad /= len(active)
        # Scale by 2/n to match the C scaling
        grad *= 2.0 / n

        # Project gradient to sum-preserving subspace
        grad -= np.mean(grad)

        grad_norm_sq = np.dot(grad, grad)
        if grad_norm_sq < 1e-30:
            print(f"  Converged at iteration {iteration} (zero gradient)")
            break

        # Polyak step: step_size = (C_max - target) / ||grad||^2
        # Use a conservative target slightly below current best
        target_val = best_score - 1e-8
        step = max(0, (C_max - target_val)) / grad_norm_sq
        step = min(step, 1e-4)  # Cap step size

        h_new = h - step * grad
        # Project to [0, 1]
        h_new = np.clip(h_new, 0, 1)
        # Re-normalize sum
        target_sum = n / 2.0
        h_new *= target_sum / np.sum(h_new)
        h_new = np.clip(h_new, 0, 1)
        h_new *= target_sum / np.sum(h_new)

        s = score_fft(h_new)
        if s < best_score:
            best_score = s
            best_h = h_new.copy()
            h = h_new

        if (iteration + 1) % 5000 == 0:
            print(f"    iter {iteration+1}: C={best_score:.13f}, C_max={C_max:.13f}, "
                  f"active={len(active)}, step={step:.2e}")

    print(f"  Final: C={best_score:.13f}")
    return best_h, best_score


# ============================================================
# Approach 4: Analytical constructions from scratch
# ============================================================
def haugland_step_function(K: int, n: int = 600) -> np.ndarray:
    """K-piece step function construction following Haugland's approach.

    Start with a symmetric K-piece function and optimize breakpoints + heights.
    """
    # Initialize with K symmetric segments
    x = np.linspace(0, 1, n, endpoint=False)
    h = np.zeros(n)
    # Create K intervals with alternating high/low values
    breakpoints = np.linspace(0, 1, K + 1)
    for i in range(K):
        mask = (x >= breakpoints[i]) & (x < breakpoints[i + 1])
        # Alternate between high and low, with gradual transitions
        if i % 2 == 0:
            h[mask] = 0.8 - 0.3 * np.sin(np.pi * (x[mask] - breakpoints[i]) / (breakpoints[i+1] - breakpoints[i]))
        else:
            h[mask] = 0.2 + 0.3 * np.sin(np.pi * (x[mask] - breakpoints[i]) / (breakpoints[i+1] - breakpoints[i]))

    h = np.clip(h, 0, 1)
    target = n / 2.0
    h *= target / np.sum(h)
    return h


def power_tent(alpha: float, n: int = 600) -> np.ndarray:
    """Power-tent construction: h(x) = max(0, 1 - |2x - 1|^alpha)."""
    x = np.linspace(0, 1, n, endpoint=False)
    h = np.maximum(0, 1 - np.abs(2 * x - 1) ** alpha)
    target = n / 2.0
    s = np.sum(h)
    if s > 0:
        h *= target / s
    h = np.clip(h, 0, 1)
    h *= target / np.sum(h)
    return h


def approach_constructions(n: int = 600, polish_iters: int = 500_000):
    """Try diverse analytical constructions, then polish the best."""
    print("\n" + "=" * 60)
    print("APPROACH 4: Analytical constructions + polish")
    print("=" * 60)

    constructions = {}

    # Power-tent family
    for alpha in [0.5, 0.8, 1.0, 1.2, 1.5, 2.0, 3.0]:
        h = power_tent(alpha, n)
        s = score_fft(h)
        constructions[f"power-tent-{alpha}"] = (h, s)

    # Haugland-style step functions
    for K in [10, 20, 30, 51, 95, 150]:
        h = haugland_step_function(K, n)
        s = score_fft(h)
        constructions[f"haugland-K{K}"] = (h, s)

    # Gaussian bump
    x = np.linspace(0, 1, n, endpoint=False)
    for sigma in [0.15, 0.2, 0.25, 0.3]:
        h = np.exp(-0.5 * ((x - 0.5) / sigma) ** 2)
        target = n / 2.0
        h *= target / np.sum(h)
        h = np.clip(h, 0, 1)
        h *= target / np.sum(h)
        s = score_fft(h)
        constructions[f"gaussian-{sigma}"] = (h, s)

    # Raised cosine family
    for k_freq in [1, 2, 3, 5, 10]:
        h = 0.5 + 0.49 * np.cos(2 * np.pi * k_freq * x)
        h = np.clip(h, 0, 1)
        target = n / 2.0
        h *= target / np.sum(h)
        h = np.clip(h, 0, 1)
        h *= target / np.sum(h)
        s = score_fft(h)
        constructions[f"cosine-{k_freq}"] = (h, s)

    # Mixed cosine construction (first few harmonics)
    rng = np.random.default_rng(123)
    for trial in range(20):
        h = np.full(n, 0.5)
        for k in range(1, 11):
            amp = rng.uniform(-0.3, 0.3)
            phase = rng.uniform(0, 2 * np.pi)
            h += amp * np.cos(2 * np.pi * k * x + phase)
        h = np.clip(h, 0, 1)
        target = n / 2.0
        s = np.sum(h)
        if s > 0:
            h *= target / s
        h = np.clip(h, 0, 1)
        h *= target / np.sum(h)
        s = score_fft(h)
        constructions[f"mixed-cosine-{trial}"] = (h, s)

    # Sort and report
    sorted_constructions = sorted(constructions.items(), key=lambda x: x[1][1])
    print("\n  Top 10 constructions:")
    for name, (h, s) in sorted_constructions[:10]:
        print(f"    {name}: {s:.10f}")

    # Polish the best 3
    best_overall = ARENA_SOTA
    best_h = None

    for name, (h, s) in sorted_constructions[:3]:
        print(f"\n  Polishing {name} (start={s:.10f})...")
        rng = np.random.default_rng(42)
        best_s = s
        improved = 0

        for trial in range(polish_iters):
            k = rng.choice([2, 3, 4])
            idx = rng.choice(n, size=k, replace=False)
            delta = rng.standard_normal(k) * 1e-6
            delta -= delta.mean()

            old = h[idx].copy()
            new_vals = old + delta
            if np.any(new_vals < 0) or np.any(new_vals > 1):
                continue

            h[idx] = new_vals
            score = score_fft(h)
            if score < best_s:
                best_s = score
                improved += 1
            else:
                h[idx] = old

            if (trial + 1) % 200_000 == 0:
                print(f"    iter {trial+1}: C={best_s:.10f}, improved={improved}")

        print(f"  {name} polished: {best_s:.10f}")
        if best_s < best_overall:
            best_overall = best_s
            best_h = h.copy()

    return best_h, best_overall


# ============================================================
# Approach 5: ADMM for spectral flattening
# ============================================================
def approach_admm(h_init: np.ndarray, n_iters: int = 1000, rho: float = 1.0):
    """ADMM: split into spectral objective + [0,1] box + sum constraint."""
    print("\n" + "=" * 60)
    print("APPROACH 5: ADMM spectral flattening")
    print("=" * 60)

    n = len(h_init)
    h = h_init.copy()
    z = h.copy()  # Auxiliary variable (in box)
    u = np.zeros(n)  # Dual variable
    target = n / 2.0

    best_score = score_fft(h)
    best_h = h.copy()
    print(f"  Start: C={best_score:.13f}")

    for iteration in range(n_iters):
        # h-update: minimize spectral objective + (rho/2)||h - z + u||^2
        # Approximate: take gradient of overlap and do proximal step
        corr = fftconvolve(h, (1.0 - h)[::-1], mode="full")
        C_vals = corr / n * 2
        max_idx = np.argmax(C_vals)
        C_max = C_vals[max_idx]

        # Subgradient of max correlation wrt h
        s = max_idx - (n - 1)
        grad = np.zeros(n)
        for i in range(n):
            g = 0.0
            i_plus_s = i + s
            i_minus_s = i - s
            if 0 <= i_plus_s < n:
                g += (1.0 - h[i_plus_s])
            if 0 <= i_minus_s < n:
                g -= h[i_minus_s]
            grad[i] = g * 2.0 / n

        # Proximal gradient step
        step = 1.0 / (rho + 1.0)
        h = step * (z - u) + (1.0 - step) * h - step * grad / rho

        # z-update: project to [0, 1] ∩ {sum = target}
        z = np.clip(h + u, 0, 1)
        # Project to sum = target via water-filling
        excess = np.sum(z) - target
        z -= excess / n
        z = np.clip(z, 0, 1)
        excess = np.sum(z) - target
        z -= excess / n  # Iterate projection
        z = np.clip(z, 0, 1)
        if np.sum(z) > 0:
            z *= target / np.sum(z)
        z = np.clip(z, 0, 1)

        # u-update: dual ascent
        u = u + h - z

        s_score = score_fft(z)
        if s_score < best_score:
            best_score = s_score
            best_h = z.copy()

        if (iteration + 1) % 200 == 0:
            print(f"    iter {iteration+1}: C_max={C_max:.10f}, best={best_score:.10f}, "
                  f"primal_res={np.linalg.norm(h-z):.2e}")

    print(f"  Final: C={best_score:.13f}")
    return best_h, best_score


def main():
    t_start = time.time()

    # Load SOTA solution
    sota_path = RESULTS_DIR / "sota_rank1_Together-AI_0.380870310586.json"
    with open(sota_path) as f:
        sol = json.load(f)
    sota_values = np.array(sol["data"]["values"], dtype=np.float64)

    print("=" * 60)
    print("Erdős Minimum Overlap — Novel Optimization Approaches")
    print(f"SOTA: {ARENA_SOTA:.16f}")
    print(f"TARGET (beat by 1e-6): {TARGET:.16f}")
    print("=" * 60)

    results = {}

    # Approach 1: Multi-n exploration
    t0 = time.time()
    h1, s1 = approach_multi_n(sota_values,
                               n_list=[480, 540, 599, 601, 660, 720],
                               iters_per_n=300_000)
    results["multi_n"] = (s1, time.time() - t0)

    # Approach 2: Cosine-basis DE
    t0 = time.time()
    h2, s2 = approach_cosine_de(K_values=[10, 20, 30], n=600, maxiter=150, popsize=10)
    results["cosine_de"] = (s2, time.time() - t0)

    # Approach 3: Subgradient projection from SOTA
    t0 = time.time()
    h3, s3 = approach_subgradient(sota_values.copy(), n_iters=20000)
    results["subgradient"] = (s3, time.time() - t0)

    # Approach 4: Analytical constructions
    t0 = time.time()
    h4, s4 = approach_constructions(n=600, polish_iters=300_000)
    results["constructions"] = (s4, time.time() - t0)

    # Approach 5: ADMM from SOTA
    t0 = time.time()
    h5, s5 = approach_admm(sota_values.copy(), n_iters=500, rho=0.5)
    results["admm"] = (s5, time.time() - t0)

    # Summary
    elapsed = time.time() - t_start
    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)
    print(f"{'Approach':<20} {'Score':<20} {'vs SOTA':<15} {'Time':<10}")
    print("-" * 65)
    for name, (score, t) in sorted(results.items(), key=lambda x: x[1][0]):
        diff = score - ARENA_SOTA
        status = "BEATS!" if score < TARGET else "no"
        print(f"{name:<20} {score:.13f}  {diff:+.2e}  {t:.0f}s  {status}")

    best_name = min(results, key=lambda k: results[k][0])
    best_score = results[best_name][0]

    print(f"\nBest: {best_name} = {best_score:.16f}")
    print(f"SOTA: {ARENA_SOTA:.16f}")
    print(f"Diff: {best_score - ARENA_SOTA:+.2e}")
    print(f"Beats SOTA by 1e-6? {'YES' if best_score < TARGET else 'NO'}")
    print(f"Total time: {elapsed:.0f}s")

    # Save best result
    all_results = [(h1, s1), (h2, s2), (h3, s3), (h4, s4), (h5, s5)]
    best_idx = min(range(5), key=lambda i: all_results[i][1] if all_results[i][0] is not None else float("inf"))
    best_h, best_s = all_results[best_idx]

    if best_h is not None:
        out = {
            "problem": "erdos-minimum-overlap",
            "n_points": len(best_h),
            "score": float(best_s),
            "values": best_h.tolist(),
            "approach": best_name,
            "timestamp": time.strftime("%Y-%m-%dT%H:%M:%S"),
        }
        fname = RESULTS_DIR / f"novel_best_{best_s:.13f}.json"
        with open(fname, "w") as f:
            json.dump(out, f)
        print(f"\nSaved: {fname}")

    return best_score < TARGET


if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
