"""Subgradient/bundle method for Erdős Minimum Overlap.

Key insight: the objective max_k C(k) is non-smooth at equioscillation points.
Standard gradient methods fail. Instead use:
1. Subgradient method with diminishing step sizes
2. Bundle method (keep track of active constraints)
3. Projected subgradient on the intersection of active half-spaces

The solution space is: h in [0,1]^n, sum(h) = n/2.
"""

import json
import time
import numpy as np
from scipy.signal import fftconvolve

import sys
sys.path.insert(0, "src")
from einstein.erdos.evaluator import evaluate
from einstein.erdos.fast import fast_evaluate


def compute_correlations(h: np.ndarray) -> np.ndarray:
    """Compute all correlation values C(k) = correlate(h, 1-h, 'full') * 2/n."""
    n = len(h)
    one_minus_h = 1.0 - h
    corr = fftconvolve(h, one_minus_h[::-1], mode="full")
    return corr * 2.0 / n


def compute_subgradient(h: np.ndarray, active_lags: list[int],
                         weights: np.ndarray | None = None) -> np.ndarray:
    """Compute subgradient of max_k C(k) with respect to h.

    For a single active lag s:
    dC(s)/dh[j] = [(1 - h[j+s]) - h[j-s]] * 2/n

    For multiple active lags, use a weighted combination.
    """
    n = len(h)
    dx = 2.0 / n

    if weights is None:
        weights = np.ones(len(active_lags)) / len(active_lags)

    grad = np.zeros(n)
    for w, s in zip(weights, active_lags):
        for j in range(n):
            g = 0.0
            # Derivative of C(s) with respect to h[j]:
            # C(s) = sum_m h[m]*(1-h[m+s]) * dx (where m+s wraps... but actually no wrapping)
            # partial C(s) / partial h[j]:
            #   from h[j]*(1-h[j+s]) term: (1-h[j+s]) * dx  (if j+s in range)
            #   from h[j-s]*(1-h[j]) term: -h[j-s] * dx     (if j-s in range)

            # The correlation is: correlate(h, 1-h, 'full') uses np.correlate convention
            # corr[k] = sum_m h[m] * (1-h)[m - (k - (n-1))]
            # Let's use shift index directly. For the full correlation:
            # corr_full[k] = sum_m h[m] * (1-h[m - shift]) where shift = k - (n-1)
            # So if lag s is the index into the full array: shift = s - (n-1)
            shift = s - (n - 1)
            # dC/dh[j] where C uses shift 'shift':
            # = (1-h[j+shift]) if 0 <= j+shift < n, else 0
            # - h[j-shift] if 0 <= j-shift < n, else 0
            # all * dx
            jps = j + shift
            jms = j - shift
            if 0 <= jps < n:
                g += (1.0 - h[jps])
            if 0 <= jms < n:
                g -= h[jms]
            grad[j] += w * g * dx

    return grad


def project_to_feasible(h: np.ndarray) -> np.ndarray:
    """Project h onto {h in [0,1]^n : sum(h) = n/2}."""
    n = len(h)
    target = n / 2.0

    # Clip to [0, 1]
    h = np.clip(h, 0, 1)

    # Project onto sum = n/2 via bisection on the dual variable
    # h_proj[i] = clip(h[i] - mu, 0, 1) where mu is chosen so sum = n/2
    lo, hi = -1.0, 1.0
    for _ in range(100):
        mu = (lo + hi) / 2
        h_proj = np.clip(h - mu, 0, 1)
        s = np.sum(h_proj)
        if s > target:
            lo = mu
        else:
            hi = mu
    return np.clip(h - (lo + hi) / 2, 0, 1)


def get_active_lags(corr: np.ndarray, tol: float = 1e-8) -> list[int]:
    """Find all lags where C(k) is within tol of the maximum."""
    max_c = np.max(corr)
    active = np.where(corr >= max_c - tol)[0].tolist()
    return active


def subgradient_descent(h0: np.ndarray, max_iters: int = 100000,
                         step_schedule: str = "diminishing",
                         step0: float = 1e-4, verbose: bool = True) -> tuple[float, np.ndarray]:
    """Run subgradient descent on max_k C(k)."""
    h = h0.copy()
    n = len(h)
    best_score = fast_evaluate(h)
    best_h = h.copy()

    if verbose:
        print(f"  Start: {best_score:.12f}")

    improved = 0
    for it in range(max_iters):
        # Compute correlations
        corr = compute_correlations(h)
        current_score = float(np.max(corr))

        # Find active lags
        active = get_active_lags(corr, tol=1e-9)

        # Compute subgradient (average over active lags)
        grad = compute_subgradient(h, active)

        # Step size
        if step_schedule == "diminishing":
            step = step0 / (1 + it * 0.001)
        elif step_schedule == "polyak":
            # Polyak step: (f(x) - f*) / ||g||^2, use f* = 0.379 (lower bound)
            f_star = 0.379
            gnorm = np.dot(grad, grad)
            if gnorm > 0:
                step = (current_score - f_star) / gnorm * 0.01
            else:
                step = step0
        else:
            step = step0

        # Take step
        h_new = h - step * grad

        # Project
        h_new = project_to_feasible(h_new)

        # Evaluate
        new_score = fast_evaluate(h_new)
        if new_score < best_score:
            best_score = new_score
            best_h = h_new.copy()
            improved += 1

        # Always update h for exploration (even if score is worse)
        h = h_new

        if verbose and (it + 1) % 10000 == 0:
            print(f"    iter {it+1}: current={current_score:.12f} best={best_score:.12f} "
                  f"active={len(active)} improved={improved} step={step:.2e}")

    if verbose:
        print(f"  Final: {best_score:.12f} ({improved} improvements)")
    return best_score, best_h


def bundle_method(h0: np.ndarray, max_iters: int = 50000,
                   verbose: bool = True) -> tuple[float, np.ndarray]:
    """Bundle method: maintain a set of cutting planes and solve a QP at each step."""
    h = h0.copy()
    n = len(h)
    best_score = fast_evaluate(h)
    best_h = h.copy()

    if verbose:
        print(f"  Bundle start: {best_score:.12f}")

    improved = 0
    # Keep a bundle of (subgradient, value) pairs
    bundle_grads = []
    bundle_vals = []
    bundle_size = 20

    for it in range(max_iters):
        corr = compute_correlations(h)
        current_score = float(np.max(corr))
        active = get_active_lags(corr, tol=1e-9)
        grad = compute_subgradient(h, active)

        # Add to bundle
        bundle_grads.append(grad.copy())
        bundle_vals.append(current_score)
        if len(bundle_grads) > bundle_size:
            bundle_grads.pop(0)
            bundle_vals.pop(0)

        # Direction: average of recent subgradients (simple version)
        direction = np.mean(bundle_grads, axis=0)

        # Line search
        step = 1e-4
        for _ in range(10):
            h_trial = project_to_feasible(h - step * direction)
            trial_score = fast_evaluate(h_trial)
            if trial_score < current_score:
                break
            step *= 0.5

        h = project_to_feasible(h - step * direction)
        new_score = fast_evaluate(h)

        if new_score < best_score:
            best_score = new_score
            best_h = h.copy()
            improved += 1

        if verbose and (it + 1) % 10000 == 0:
            print(f"    iter {it+1}: current={new_score:.12f} best={best_score:.12f} "
                  f"improved={improved}")

    if verbose:
        print(f"  Bundle final: {best_score:.12f} ({improved} improvements)")
    return best_score, best_h


def coordinated_multi_lag_transport(h0: np.ndarray, max_iters: int = 500000,
                                     verbose: bool = True) -> tuple[float, np.ndarray]:
    """Mass transport that targets ALL active lags simultaneously.

    Key idea: instead of random perturbations, choose perturbations that
    decrease C(k) for ALL active lags at once. This requires solving a
    small LP at each step.
    """
    h = h0.copy()
    n = len(h)
    best_score = fast_evaluate(h)
    best_h = h.copy()

    if verbose:
        print(f"  Multi-lag transport start: {best_score:.12f}")

    rng = np.random.default_rng(12345)
    improved = 0

    for it in range(max_iters):
        # Every 10000 iterations, recompute active lags
        if it % 10000 == 0:
            corr = compute_correlations(h)
            active = get_active_lags(corr, tol=1e-10)
            # Compute gradients for each active lag
            active_grads = []
            for s in active[:20]:  # Limit to top 20 active lags
                g = compute_subgradient(h, [s])
                active_grads.append(g)
            active_grads = np.array(active_grads)

        # Pick 2-4 indices to perturb
        k = rng.integers(2, 5)
        indices = rng.choice(n, k, replace=False)

        # Try to find a perturbation that improves all active lags
        # Use a random zero-sum perturbation
        delta_scale = rng.choice([1e-8, 1e-7, 1e-6, 1e-5])
        deltas = rng.standard_normal(k) * delta_scale
        deltas -= np.mean(deltas)  # zero-sum

        h_new = h.copy()
        h_new[indices] += deltas

        # Check feasibility
        if np.any(h_new < 0) or np.any(h_new > 1):
            continue

        new_score = fast_evaluate(h_new)
        if new_score < best_score:
            best_score = new_score
            h = h_new
            best_h = h.copy()
            improved += 1

        if verbose and (it + 1) % 100000 == 0:
            print(f"    iter {it+1}: best={best_score:.14f} improved={improved}")

    if verbose:
        print(f"  Multi-lag final: {best_score:.14f} ({improved} improvements)")
    return best_score, best_h


def main():
    print("=" * 60)
    print("Erdős Minimum Overlap — Subgradient/Bundle Methods")
    print("=" * 60)

    with open('/tmp/p1_sota.json') as f:
        sota_data = json.load(f)
    h_sota = np.array(sota_data['values'])
    sota_score = fast_evaluate(h_sota)
    print(f"SOTA score: {sota_score:.16f}")
    print(f"Target:     <= 0.3808693105862199 (need 1e-6 improvement)")

    overall_best = sota_score
    overall_best_h = h_sota.copy()

    # Method 1: Subgradient descent from SOTA
    print("\n=== Method 1: Subgradient descent (diminishing step) ===")
    score1, h1 = subgradient_descent(h_sota, max_iters=50000,
                                      step_schedule="diminishing", step0=1e-5)
    if score1 < overall_best:
        overall_best = score1
        overall_best_h = h1

    # Method 2: Subgradient with Polyak step
    print("\n=== Method 2: Subgradient (Polyak step) ===")
    score2, h2 = subgradient_descent(h_sota, max_iters=50000,
                                      step_schedule="polyak", step0=1e-4)
    if score2 < overall_best:
        overall_best = score2
        overall_best_h = h2

    # Method 3: Bundle method
    print("\n=== Method 3: Bundle method ===")
    score3, h3 = bundle_method(h_sota, max_iters=20000)
    if score3 < overall_best:
        overall_best = score3
        overall_best_h = h3

    # Method 4: Coordinated multi-lag transport (extended run)
    print("\n=== Method 4: Coordinated multi-lag transport ===")
    score4, h4 = coordinated_multi_lag_transport(h_sota, max_iters=1000000)
    if score4 < overall_best:
        overall_best = score4
        overall_best_h = h4

    # Method 5: Subgradient from perturbed starting points
    print("\n=== Method 5: Subgradient from perturbed starts ===")
    rng = np.random.default_rng(999)
    for trial in range(5):
        noise = rng.standard_normal(len(h_sota)) * 0.01
        h_start = project_to_feasible(h_sota + noise)
        score, h = subgradient_descent(h_start, max_iters=20000,
                                        step_schedule="diminishing", step0=1e-4,
                                        verbose=False)
        print(f"  Trial {trial}: {score:.12f}")
        if score < overall_best:
            overall_best = score
            overall_best_h = h

    # Verify
    exact = evaluate({"values": overall_best_h.tolist()})
    print(f"\n=== FINAL RESULT ===")
    print(f"Best (fast):  {overall_best:.16f}")
    print(f"Best (exact): {exact:.16f}")
    print(f"SOTA:         0.3808703105862199")
    print(f"Improvement:  {0.3808703105862199 - exact:.2e}")

    with open('/tmp/p1_subgrad_best.json', 'w') as f:
        json.dump({"values": overall_best_h.tolist()}, f)
    print("Saved to /tmp/p1_subgrad_best.json")


if __name__ == "__main__":
    main()
