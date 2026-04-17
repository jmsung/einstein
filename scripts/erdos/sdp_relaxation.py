"""SDP relaxation for Erdős Minimum Overlap.

At small n, we can solve the exact problem via Shor's SDP relaxation:
- Introduces X ≈ h*h^T (PSD matrix)
- Linearizes the bilinear autocorrelation terms
- Gives a LOWER BOUND on C* and a candidate solution via rank-1 rounding

Strategy: solve SDP at small n (30-100), extract h, upsample to n=600, polish.
"""

import json
import time
import numpy as np
import cvxpy as cp
from scipy.interpolate import interp1d

import sys
sys.path.insert(0, "/Users/jmsung/projects/einstein/cb-feat-auto-p1")
from einstein.erdos.evaluator import evaluate
from einstein.erdos.fast import fast_evaluate


def solve_sdp(n: int, verbose: bool = True) -> tuple[float, np.ndarray]:
    """Solve the SDP relaxation at resolution n.

    Returns (lower_bound, h_rounded) where h_rounded is the rank-1 extraction.
    """
    if verbose:
        print(f"\n=== SDP at n={n} ===")
        t0 = time.time()

    h = cp.Variable(n)
    X = cp.Variable((n, n), symmetric=True)
    t = cp.Variable()

    constraints = [
        # h in [0, 1]
        h >= 0,
        h <= 1,
        # sum = n/2
        cp.sum(h) == n / 2,
        # Shor relaxation: [[X, h], [h^T, 1]] PSD
        cp.bmat([[X, cp.reshape(h, (n, 1))],
                 [cp.reshape(h, (1, n)), np.ones((1, 1))]]) >> 0,
        # X[i,i] <= h[i] (since h[i] in [0,1] implies h[i]^2 <= h[i])
        cp.diag(X) <= h,
        # X >= 0 elementwise (since h >= 0)
        X >= 0,
    ]

    # Correlation constraints: C(k) <= t for all valid lags
    # C(k) = (sum(h) - sum_j X[j, j+k]) * 2/n
    # = (n/2 - trace(S_k @ X)) * 2/n
    # = 1 - 2*trace(S_k @ X)/n
    dx = 2.0 / n
    for k in range(-(n - 1), n):
        # Autocorrelation at lag k: R(k) = sum_{j} X[j, j+k]
        # C(k) = (n/2 - R(k)) * dx
        indices = []
        for j in range(n):
            jk = j + k
            if 0 <= jk < n:
                indices.append((j, jk))
        if not indices:
            continue
        # R(k) = sum of X[j, j+k]
        R_k = sum(X[j, jk] for j, jk in indices)
        C_k = (n / 2.0 - R_k) * dx
        constraints.append(C_k <= t)

    prob = cp.Problem(cp.Minimize(t), constraints)

    if verbose:
        print(f"  Variables: h({n}), X({n}x{n}), t")
        print(f"  Constraints: {len(constraints)}")
        print(f"  Solving...")

    try:
        prob.solve(solver=cp.SCS, verbose=False, max_iters=50000,
                   eps=1e-8, warm_start=True)
    except cp.SolverError:
        try:
            prob.solve(solver=cp.CLARABEL, verbose=False)
        except cp.SolverError:
            print(f"  FAILED: no solver could handle n={n}")
            return float('inf'), np.ones(n) * 0.5

    if verbose:
        print(f"  Status: {prob.status}")
        print(f"  SDP lower bound: {prob.value:.10f}")
        print(f"  Time: {time.time() - t0:.1f}s")

    # Extract h from SDP
    h_val = h.value
    if h_val is None:
        return float('inf'), np.ones(n) * 0.5

    # Also try rank-1 rounding of X
    X_val = X.value
    if X_val is not None:
        # Eigendecomposition
        eigvals, eigvecs = np.linalg.eigh(X_val)
        # Best rank-1 approximation
        h_eig = eigvecs[:, -1] * np.sqrt(max(0, eigvals[-1]))
        # Fix sign (h should be mostly positive)
        if np.sum(h_eig) < 0:
            h_eig = -h_eig
    else:
        h_eig = h_val.copy()

    # Try both h_val and h_eig, return the better one
    candidates = []
    for name, hc in [("direct", h_val), ("rank1", h_eig)]:
        hc = np.clip(hc, 0, 1)
        s = np.sum(hc)
        if s > 0:
            hc = hc * (n / 2.0 / s)
            hc = np.clip(hc, 0, 1)
            s = np.sum(hc)
            if s > 0:
                hc = hc * (n / 2.0 / s)
        score = fast_evaluate(hc)
        candidates.append((score, hc, name))
        if verbose:
            print(f"  {name}: score={score:.10f}")

    best = min(candidates, key=lambda x: x[0])
    return prob.value, best[1]


def upsample_and_polish(h_small: np.ndarray, target_n: int = 600,
                         polish_iters: int = 200000) -> tuple[float, np.ndarray]:
    """Upsample a small-n solution to target_n and polish with mass transport."""
    n_small = len(h_small)
    print(f"\n  Upsampling n={n_small} -> n={target_n}")

    # Interpolate
    x_small = np.linspace(0, 2, n_small, endpoint=False)
    x_target = np.linspace(0, 2, target_n, endpoint=False)
    f = interp1d(x_small, h_small, kind='cubic', fill_value='extrapolate')
    h = f(x_target)

    # Project to feasibility
    h = np.clip(h, 0, 1)
    h *= target_n / 2.0 / np.sum(h)
    h = np.clip(h, 0, 1)
    h *= target_n / 2.0 / np.sum(h)

    score0 = fast_evaluate(h)
    print(f"  After interpolation: {score0:.10f}")

    # Polish with mass transport
    best_score = score0
    best_h = h.copy()
    rng = np.random.default_rng(42)

    improved = 0
    for it in range(polish_iters):
        # Pick 2-4 random indices for zero-sum perturbation
        k = rng.integers(2, 5)
        indices = rng.choice(target_n, k, replace=False)
        deltas = rng.standard_normal(k) * 1e-5
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

        if (it + 1) % 50000 == 0:
            print(f"    iter {it+1}/{polish_iters}: score={best_score:.12f} ({improved} improvements)")

    print(f"  Final: {best_score:.12f} ({improved} improvements)")
    return best_score, best_h


def main():
    print("=" * 60)
    print("Erdős Minimum Overlap — SDP Relaxation + Upsample")
    print("=" * 60)
    print(f"Target: beat 0.3808703105862199 by >= 1e-6")
    print(f"Need:   <= 0.3808693105862199")

    overall_best_score = float('inf')
    overall_best_h = None

    # Phase 1: SDP at increasing n
    for n in [30, 40, 50, 60, 80]:
        try:
            lb, h_small = solve_sdp(n, verbose=True)
            small_score = fast_evaluate(h_small)
            if small_score < float('inf'):
                score, h_up = upsample_and_polish(h_small, target_n=600,
                                                   polish_iters=100000)
                if score < overall_best_score:
                    overall_best_score = score
                    overall_best_h = h_up
                    print(f"  *** New best: {score:.12f}")
        except Exception as e:
            print(f"  Error at n={n}: {e}")
            continue

    # Phase 2: Try convex combinations of SDP solutions with SOTA
    print("\n\n=== Phase 2: Convex combinations with SOTA ===")
    with open('/tmp/p1_sota.json') as f:
        sota_data = json.load(f)
    h_sota = np.array(sota_data['values'])
    sota_score = fast_evaluate(h_sota)
    print(f"SOTA score: {sota_score:.12f}")

    if overall_best_h is not None:
        for alpha in [0.01, 0.02, 0.05, 0.1, 0.2, 0.5]:
            h_mix = (1 - alpha) * h_sota + alpha * overall_best_h
            h_mix = np.clip(h_mix, 0, 1)
            h_mix *= 300.0 / np.sum(h_mix)
            h_mix = np.clip(h_mix, 0, 1)
            h_mix *= 300.0 / np.sum(h_mix)
            mix_score = fast_evaluate(h_mix)
            print(f"  alpha={alpha:.2f}: {mix_score:.12f}")

            if mix_score < overall_best_score:
                overall_best_score = mix_score
                overall_best_h = h_mix

    # Phase 3: Polish the overall best
    if overall_best_h is not None and overall_best_score < 0.39:
        print(f"\n=== Phase 3: Extended polish of best ({overall_best_score:.12f}) ===")
        score, h_polished = upsample_and_polish(
            overall_best_h, target_n=600, polish_iters=500000
        )
        if score < overall_best_score:
            overall_best_score = score
            overall_best_h = h_polished

    # Verify with exact evaluator
    if overall_best_h is not None:
        exact = evaluate({"values": overall_best_h.tolist()})
        print(f"\n=== FINAL RESULT ===")
        print(f"Best score (fast):  {overall_best_score:.16f}")
        print(f"Best score (exact): {exact:.16f}")
        print(f"SOTA:               0.3808703105862199")
        print(f"Improvement:        {0.3808703105862199 - exact:.2e}")
        print(f"Need:               1.00e-06")

        # Save
        with open('/tmp/p1_sdp_best.json', 'w') as f:
            json.dump({"values": overall_best_h.tolist()}, f)
        print("Saved to /tmp/p1_sdp_best.json")


if __name__ == "__main__":
    main()
