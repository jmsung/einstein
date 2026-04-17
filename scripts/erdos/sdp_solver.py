"""SDP relaxation for Erdős Minimum Overlap.

For small n, solve the following SDP:

maximize alpha
s.t.  for all k=1,...,n-1:  sum_i h[i]*(1-h[i+k]) <= (n/2) * t
      h ∈ [0,1]^n, sum(h) = n/2

This is not directly an SDP because of the quadratic terms h[i]*h[i+k].
We use a lifting: X[i,j] = h[i]*h[j], X is PSD, diag(X) relates to h.

Actually, a cleaner formulation:
Let r(k) = sum_i h[i]*h[i+k] (autocorrelation of h at lag k).
Then C(k) = (sum(h) - r(k)) * 2/n = (n/2 - r(k)) * 2/n = 1 - 2*r(k)/n.

Minimize max_k C(k) = minimize (1 - 2/n * min_k r(k))
= 1 - 2/n * maximize(min_k r(k))

We need r(k) to come from a valid h ∈ [0,1]^n with sum=n/2.

Relaxation: r is a valid autocorrelation (positive definite) with r(0) <= n/2.

This gives us a LOWER BOUND on the achievable C.
"""

import sys
sys.path.insert(0, "src")

import json
import time
import numpy as np
from pathlib import Path
from scipy.signal import fftconvolve
from scipy.optimize import linprog

RESULTS_DIR = Path("results/problem-1-erdos-overlap")


def fast_eval(h):
    h = np.asarray(h, dtype=np.float64)
    n = len(h)
    if n == 0:
        return float("inf")
    h = np.clip(h, 0, 1)
    s = np.sum(h)
    if s == 0:
        return float("inf")
    h = h * (n / 2.0 / s)
    if np.any(h > 1.0):
        return float("inf")
    corr = fftconvolve(h, (1.0 - h)[::-1], mode="full")
    return float(np.max(corr)) / n * 2


def normalize(h):
    h = np.clip(h, 0, 1)
    n = len(h)
    s = np.sum(h)
    if s > 0:
        h = h * (n / 2.0 / s)
    h = np.clip(h, 0, 1)
    return h


def sdp_lower_bound(n):
    """Compute SDP lower bound on C for given n.

    Uses the Toeplitz autocorrelation relaxation.
    """
    import cvxpy as cp

    # Variables: autocorrelation values r(0), r(1), ..., r(n-1)
    r = cp.Variable(n)
    alpha = cp.Variable()

    constraints = []

    # r(k) >= alpha for all k=0,...,n-1 (we want to maximize min r(k))
    for k in range(n):
        constraints.append(r[k] >= alpha)

    # Toeplitz matrix from r must be PSD
    # Build Toeplitz matrix: T[i,j] = r[|i-j|]
    T = cp.Variable((n, n), symmetric=True)
    for i in range(n):
        for j in range(i, n):
            constraints.append(T[i, j] == r[j - i])
    constraints.append(T >> 0)  # PSD constraint

    # r(0) <= n/2 (from sum(h^2) <= sum(h) = n/2)
    constraints.append(r[0] <= n / 2.0)

    # r(0) >= n/4 (from h ∈ [0,1] with sum=n/2: h^2 >= 2h-1 when h >= 0.5)
    # Actually: min sum(h^2) subject to h ∈ [0,1], sum(h)=n/2 is achieved at h=0.5, giving n/4
    constraints.append(r[0] >= n / 4.0)

    # sum of r(k) for all k is related to (sum h)^2 = n^2/4
    # Actually: sum_{k=0}^{n-1} r(k) = sum_{i,j: j=i+k for some k>=0} h[i]h[j]
    # This is the upper-triangular part of sum h[i]h[j] = (sum h)^2 / 2 + sum(h^2)/2
    # Hmm, this is getting complex. Let's just use the PSD + bound constraints.

    # Also: 0 <= r(k) <= n/2 for all k (since h[i]*h[i+k] >= 0 and <= max(h)^2 * count)
    for k in range(n):
        constraints.append(r[k] >= 0)
        constraints.append(r[k] <= n / 2.0)

    # Objective: maximize alpha (= min autocorrelation)
    prob = cp.Problem(cp.Maximize(alpha), constraints)

    try:
        prob.solve(solver=cp.SCS, max_iters=10000, verbose=False)
        if prob.status in ['optimal', 'optimal_inaccurate']:
            min_autocorr = alpha.value
            C_lower = 1.0 - 2.0 * min_autocorr / n
            return C_lower, r.value
        else:
            print(f"  SDP status: {prob.status}")
            return None, None
    except Exception as e:
        print(f"  SDP error: {e}")
        return None, None


def sdp_with_lifting(n):
    """Direct SDP with matrix lifting X = h h^T.

    Variables:
      X (n x n, PSD): X[i,j] = h[i] * h[j]
      h (n): h[i] = diag(X)[i] (with additional constraints)

    The autocorrelation at lag k is: r(k) = sum_i X[i, i+k]

    Constraints:
      X >> 0
      X[i,j] >= 0 for all i,j (since h >= 0)
      X[i,j] <= X[i,i] and X[i,j] <= X[j,j] (since h <= 1)
      sum diag(X) = ... wait, X = hh^T means diag(X) = h^2
      sum h = n/2 → sum sqrt(diag(X)) = n/2 (non-convex!)

    This doesn't work directly because of the nonlinear constraint.
    Let's use a weaker relaxation:
      X[i,i] <= h[i] (since h^2 <= h for h in [0,1])
      h[i] <= 1
      sum(h) = n/2
      X - h h^T PSD (Schur complement)

    Actually, the standard lifting is:
      Y = [[1, h^T], [h, X]], Y >> 0
      diag(X) = ... (this is the Shor relaxation)
    """
    import cvxpy as cp

    h = cp.Variable(n, nonneg=True)
    X = cp.Variable((n, n), symmetric=True)
    t = cp.Variable()  # max overlap

    constraints = []

    # X must be PSD
    constraints.append(X >> 0)

    # Schur complement: X >= h h^T
    # [[X, h], [h^T, 1]] >> 0
    Y = cp.bmat([[X, cp.reshape(h, (n, 1))],
                  [cp.reshape(h, (1, n)), np.ones((1, 1))]])
    constraints.append(Y >> 0)

    # h in [0, 1], sum = n/2
    constraints.append(h <= 1)
    constraints.append(cp.sum(h) == n / 2.0)

    # X[i,j] >= 0
    constraints.append(X >= 0)

    # X[i,i] <= h[i] (since h_i^2 <= h_i for h_i in [0,1])
    for i in range(n):
        constraints.append(X[i, i] <= h[i])

    # Overlap constraints: for each lag k
    # C(k) = sum_i h[i] - sum_i X[i, (i+k) % n if using circular, else i+k if valid]
    # For linear correlation at lag k (0 <= k < n):
    # overlap(k) = sum_{i=0}^{n-1-k} (h[i] - X[i, i+k]) * 2/n
    # We minimize the maximum of these

    for k in range(n):
        # Linear correlation at lag k
        # sum_{i=0}^{n-1-k} h[i](1 - h[i+k]) = sum h[i] - sum X[i,i+k]
        h_sum_k = cp.sum(h[:n - k])  # sum of h[i] for i=0..n-1-k
        x_sum_k = cp.sum([X[i, i + k] for i in range(n - k)])
        overlap_k = (h_sum_k - x_sum_k) * 2.0 / n
        constraints.append(overlap_k <= t)

    # Also for negative lags (by symmetry of correlation)
    for k in range(1, n):
        h_sum_k = cp.sum(h[k:])
        x_sum_k = cp.sum([X[i + k, i] for i in range(n - k)])
        overlap_k = (h_sum_k - x_sum_k) * 2.0 / n
        constraints.append(overlap_k <= t)

    prob = cp.Problem(cp.Minimize(t), constraints)

    try:
        prob.solve(solver=cp.SCS, max_iters=20000, verbose=True)
        if prob.status in ['optimal', 'optimal_inaccurate']:
            return t.value, h.value, X.value
        else:
            print(f"  SDP status: {prob.status}")
            return None, None, None
    except Exception as e:
        print(f"  SDP error: {e}")
        return None, None, None


def main():
    print("=" * 70)
    print("SDP SOLVER: Erdős Minimum Overlap (Problem 1)")
    print("=" * 70)

    # 1. Simple SDP lower bounds at various n
    print("\n--- SDP Lower Bounds (autocorrelation relaxation) ---")
    for n in [10, 20, 30, 50, 75, 100]:
        t0 = time.time()
        lb, r = sdp_lower_bound(n)
        elapsed = time.time() - t0
        if lb is not None:
            print(f"  n={n:4d}: C_lower >= {lb:.10f} ({elapsed:.1f}s)")
        else:
            print(f"  n={n:4d}: FAILED ({elapsed:.1f}s)")

    # 2. Full SDP with lifting at small n
    print("\n--- Full SDP with Lifting ---")
    for n in [10, 20, 30, 50]:
        print(f"\n  n={n}:")
        t0 = time.time()
        t_val, h_val, X_val = sdp_with_lifting(n)
        elapsed = time.time() - t0

        if t_val is not None:
            print(f"    SDP bound: {t_val:.10f} ({elapsed:.1f}s)")

            # Round to feasible solution
            h_rounded = normalize(np.clip(h_val, 0, 1))
            actual_score = fast_eval(h_rounded)
            print(f"    Rounded score: {actual_score:.10f}")

            # Try optimization from SDP solution
            # Upsample to 600 and evaluate
            h_600 = np.interp(np.linspace(0, 1, 600),
                              np.linspace(0, 1, n), h_rounded)
            h_600 = normalize(h_600)
            score_600 = fast_eval(h_600)
            print(f"    Upsampled to n=600: {score_600:.10f}")
        else:
            print(f"    FAILED ({elapsed:.1f}s)")

    # 3. Known lower bound comparison
    print("\n--- Lower bound comparison ---")
    print(f"  White (2022): 0.379005")
    print(f"  SOTA (upper): 0.380870")
    print(f"  Gap:          0.001865")


if __name__ == "__main__":
    main()
