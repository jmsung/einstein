"""Sequential Linear Programming (SLP) for Erdős Minimum Overlap.

The SOTA was found by Together Computer using sequential LP.
This implements a proper SLP with trust region, warm-starting from
diverse initial points (not just from SOTA).

Key insight: SLP from SOTA finds no improvement (verified in prior work).
So we warm-start from DIFFERENT initial solutions to find new basins,
then SLP-polish those basins to see if any beat SOTA.
"""

import json
import sys
import time
from pathlib import Path

import numpy as np
from scipy.optimize import linprog
from scipy.signal import fftconvolve

sys.path.insert(0, "src")
from einstein.erdos.evaluator import evaluate as exact_evaluate
from einstein.erdos.fast import fast_evaluate

RESULTS_DIR = Path("results/problem-1-erdos-overlap")
ARENA_SOTA = 0.3808703105862199
TARGET = ARENA_SOTA - 1e-6


def compute_correlation(h: np.ndarray) -> np.ndarray:
    """Compute all correlations C(k) = correlate(h, 1-h, 'full') * 2/n."""
    n = len(h)
    corr = fftconvolve(h, (1.0 - h)[::-1], mode="full")
    return corr * 2.0 / n


def slp_step(h: np.ndarray, trust_radius: float = 0.01, n_active: int = 50) -> np.ndarray:
    """One step of Sequential Linear Programming.

    Linearize the minimax objective around h, solve LP to find improving direction.

    min t s.t.
        C_k + grad_k . delta <= t for all active k
        -trust_radius <= delta_i <= trust_radius
        sum(delta) = 0 (preserve sum)
        0 <= h_i + delta_i <= 1

    Returns new h.
    """
    n = len(h)
    C = compute_correlation(h)
    C_max = np.max(C)
    n_lags = len(C)

    # Find active lags (near the max)
    active_threshold = C_max - 0.001  # Include lags within 0.001 of max
    active_idx = np.where(C >= active_threshold)[0]

    # If too many, keep top n_active
    if len(active_idx) > n_active:
        top_idx = np.argsort(C[active_idx])[-n_active:]
        active_idx = active_idx[top_idx]

    n_active_actual = len(active_idx)

    # Compute gradient of C_k w.r.t. h for each active lag
    # C_k = sum_i h[i] * (1 - h[i-k]) * 2/n
    # dC_k/dh[i] = ((1 - h[i+k]) - h[i-k]) * 2/n  (for appropriate shift k)
    grads = np.zeros((n_active_actual, n))
    for idx, lag_idx in enumerate(active_idx):
        s = lag_idx - (n - 1)  # Actual shift
        for i in range(n):
            g = 0.0
            ip = i + s
            im = i - s
            if 0 <= ip < n:
                g += (1.0 - h[ip])
            if 0 <= im < n:
                g -= h[im]
            grads[idx, i] = g * 2.0 / n

    # LP: min t s.t. C_k + grad_k . delta <= t, constraints on delta
    # Variables: [delta_0, ..., delta_{n-1}, t]
    # Objective: minimize t -> c = [0, 0, ..., 0, 1]
    c = np.zeros(n + 1)
    c[n] = 1.0  # Minimize t

    # Inequality constraints: C_k + grad_k . delta - t <= 0
    # -> grad_k . delta - t <= -C_k
    A_ub = np.zeros((n_active_actual, n + 1))
    b_ub = np.zeros(n_active_actual)
    for idx in range(n_active_actual):
        A_ub[idx, :n] = grads[idx]
        A_ub[idx, n] = -1.0  # -t
        b_ub[idx] = -C[active_idx[idx]]

    # Equality constraint: sum(delta) = 0
    A_eq = np.zeros((1, n + 1))
    A_eq[0, :n] = 1.0
    b_eq = np.array([0.0])

    # Bounds on delta: max of trust radius and box constraint
    bounds = []
    for i in range(n):
        lo = max(-trust_radius, -h[i])  # h[i] + delta[i] >= 0
        hi = min(trust_radius, 1.0 - h[i])  # h[i] + delta[i] <= 1
        bounds.append((lo, hi))
    bounds.append((None, None))  # t is unbounded

    try:
        result = linprog(c, A_ub=A_ub, b_ub=b_ub, A_eq=A_eq, b_eq=b_eq,
                        bounds=bounds, method='highs')

        if result.success:
            delta = result.x[:n]
            t_opt = result.x[n]

            # Check if improvement is found
            if t_opt < C_max - 1e-14:
                h_new = h + delta
                h_new = np.clip(h_new, 0, 1)
                target = len(h) / 2.0
                h_new *= target / np.sum(h_new)
                h_new = np.clip(h_new, 0, 1)
                return h_new
    except Exception:
        pass

    return h  # No improvement


def slp_optimize(h: np.ndarray, max_iters: int = 200, trust_radius: float = 0.01) -> tuple[np.ndarray, float]:
    """Run SLP optimization loop."""
    best_score = fast_evaluate(h)
    best_h = h.copy()

    for it in range(max_iters):
        h_new = slp_step(h, trust_radius=trust_radius)

        new_score = fast_evaluate(h_new)
        if new_score < best_score - 1e-14:
            improvement = best_score - new_score
            best_score = new_score
            best_h = h_new.copy()
            h = h_new

            if (it + 1) % 10 == 0 or improvement > 1e-8:
                print(f"    SLP iter {it+1}: C={best_score:.13f} (imp={improvement:.2e})")
        else:
            # Reduce trust radius
            trust_radius *= 0.8
            if trust_radius < 1e-12:
                print(f"    SLP converged at iter {it+1} (trust radius exhausted)")
                break

    return best_h, best_score


def generate_diverse_starts(n: int = 600, n_starts: int = 30) -> list[tuple[str, np.ndarray]]:
    """Generate diverse starting points for SLP."""
    starts = []
    x = np.linspace(0, 1, n, endpoint=False)

    for seed in range(n_starts):
        rng = np.random.default_rng(seed * 17 + 3)

        if seed < 5:
            # Power-tent variants
            alpha = 0.5 + seed * 0.5
            center = 0.5
            h = np.maximum(0, 1 - np.abs((x - center) / 0.4) ** alpha)
            name = f"power-tent-a{alpha:.1f}"

        elif seed < 10:
            # Fourier constructions with different frequency profiles
            h = np.full(n, 0.5)
            K = 5 + seed * 3
            for k in range(1, K + 1):
                # Decay pattern: different for each seed
                amp = 0.4 / (k ** (0.5 + seed * 0.1))
                phase = rng.uniform(0, 2 * np.pi)
                h += amp * np.cos(2 * np.pi * k * x + phase)
            name = f"fourier-K{K}"

        elif seed < 15:
            # Block constructions (Haugland-inspired)
            K = 10 + seed * 5
            h = np.zeros(n)
            block_size = n // K
            for b in range(K):
                start = b * block_size
                end = min(start + block_size, n)
                if b % 2 == 0:
                    h[start:end] = rng.uniform(0.6, 1.0)
                else:
                    h[start:end] = rng.uniform(0.0, 0.4)
            name = f"block-K{K}"

        elif seed < 20:
            # Cosine-chirp (frequency sweep)
            f0 = 1 + seed
            f1 = 10 + seed * 3
            phase = np.cumsum(np.linspace(f0, f1, n)) * 2 * np.pi / n
            h = 0.5 + 0.4 * np.cos(phase)
            name = f"chirp-f{f0}-{f1}"

        elif seed < 25:
            # Mixtures of Gaussians
            n_bumps = 3 + seed - 20
            h = np.zeros(n)
            for _ in range(n_bumps):
                center = rng.uniform(0.1, 0.9)
                width = rng.uniform(0.02, 0.15)
                amp = rng.uniform(0.5, 1.5)
                h += amp * np.exp(-0.5 * ((x - center) / width) ** 2)
            name = f"gmm-{n_bumps}"

        else:
            # Bernstein polynomial
            from scipy.special import comb
            degree = 5 + seed - 25
            coeffs = rng.uniform(0, 1, degree + 1)
            h = np.zeros(n)
            for k in range(degree + 1):
                h += coeffs[k] * comb(degree, k) * (x ** k) * ((1 - x) ** (degree - k))
            name = f"bernstein-d{degree}"

        # Normalize
        h = np.clip(h, 0, 1)
        target = n / 2.0
        s = np.sum(h)
        if s > 0:
            h *= target / s
        h = np.clip(h, 0, 1)
        s = np.sum(h)
        if s > 0:
            h *= target / s
        starts.append((name, h))

    return starts


def main():
    t_start = time.time()

    print("=" * 60)
    print("Erdős Minimum Overlap — Sequential Linear Programming")
    print(f"SOTA: {ARENA_SOTA:.16f}")
    print(f"TARGET: {TARGET:.16f}")
    print("=" * 60)

    # Phase 1: Adam polish from diverse starts, then SLP finish
    starts = generate_diverse_starts(n=600, n_starts=30)

    best_overall = ARENA_SOTA
    best_h = None
    results = []

    print(f"\nPhase 1: Quick Adam pre-polish ({len(starts)} starts)...")

    # Quick Adam pre-polish using scipy minimize
    for name, h in starts:
        init_score = fast_evaluate(h)

        # Quick L-BFGS-B polish (proxy for Adam, works in scipy)
        from scipy.optimize import minimize as sp_minimize

        def obj(x):
            x_clip = np.clip(x, 0, 1)
            target = len(x_clip) / 2.0
            s = np.sum(x_clip)
            if s > 0:
                x_clip = x_clip * (target / s)
            x_clip = np.clip(x_clip, 0, 1)
            return fast_evaluate(x_clip)

        bounds = [(0, 1)] * 600
        result = sp_minimize(obj, h, method='L-BFGS-B', bounds=bounds,
                           options={'maxiter': 500, 'ftol': 1e-15})
        polished_score = result.fun
        h_polished = np.clip(result.x, 0, 1)
        target = 300.0
        h_polished *= target / np.sum(h_polished)
        h_polished = np.clip(h_polished, 0, 1)

        actual_score = fast_evaluate(h_polished)
        results.append((name, init_score, actual_score, h_polished))
        print(f"  {name}: {init_score:.8f} -> {actual_score:.8f}")

    # Sort by score, take top 5 for SLP
    results.sort(key=lambda x: x[2])
    print(f"\nTop 5 after pre-polish:")
    for name, init, polished, _ in results[:5]:
        print(f"  {name}: {polished:.10f}")

    print(f"\nPhase 2: SLP refinement of top 5...")
    for name, _, polished_score, h_polished in results[:5]:
        print(f"\n  SLP on {name} (start={polished_score:.10f}):")
        h_slp, slp_score = slp_optimize(h_polished, max_iters=100, trust_radius=0.01)
        actual = fast_evaluate(h_slp)
        print(f"  -> SLP result: {actual:.13f}")

        if actual < best_overall:
            best_overall = actual
            best_h = h_slp.copy()

    # Summary
    elapsed = time.time() - t_start
    print("\n" + "=" * 60)
    print(f"SLP Best: {best_overall:.16f}")
    print(f"SOTA:     {ARENA_SOTA:.16f}")
    print(f"Diff:     {best_overall - ARENA_SOTA:+.2e}")
    print(f"Beats SOTA by 1e-6? {'YES' if best_overall < TARGET else 'NO'}")
    print(f"Total time: {elapsed:.0f}s")
    print("=" * 60)

    if best_h is not None:
        out = {
            "problem": "erdos-minimum-overlap",
            "n_points": len(best_h),
            "score": float(best_overall),
            "values": best_h.tolist(),
            "approach": "SLP",
            "timestamp": time.strftime("%Y-%m-%dT%H:%M:%S"),
        }
        fname = RESULTS_DIR / f"slp_best_{best_overall:.10f}.json"
        with open(fname, "w") as f:
            json.dump(out, f)
        print(f"Saved: {fname}")


if __name__ == "__main__":
    main()
