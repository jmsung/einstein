"""Level-2 Lasserre / SOS relaxation for the C-S finite formulation of the P2 lower bound.

The Cloninger-Steinerberger (2017) finite formulation:

    a_n := min over a in (R+)^{2n} with sum(a) = 4n of
              max over (ell, k) of  (1/(4n*ell)) * sum_{k <= i+j <= k+ell-2} a_i a_j

with C_1 >= a_n for every n. C-S enumerated rational a's (m=50 denominator) at
n <= 24 with branch-and-bound to certify a_n >= 1.28.

This script computes the level-2 Lasserre relaxation of the *continuous* min:

    min over moment matrix M >= 0 (size (2n+1)^2) of tau
    s.t.  M[0,0] = 1,  M[0,i+1] >= 0,  sum(M[0,1:]) = 4n
          (1/(4n*ell)) * sum_{k <= i+j <= k+ell-2} M[i+1, j+1] <= tau
            for every (ell, k) constraint

Lasserre L2 produces a *lower* bound on a_n (and hence on C_1), so it is a valid
relaxation. The question is whether the Lasserre bound is competitive with C-S
at matched n (or beats C-S at small n where C-S is tractable).

Empirical result at n in {1, 3, 4, 6, 8, 10, 12, 16}:

    n     Lasserre L2 bound
    1     0.667     (analytical a_1 = 1.0; relaxation gap 0.33)
    3     0.857
    4     0.889
    6     0.923
    8     0.941
    10    0.952
    12    0.960
    16    0.970

Bounds increase slowly with n; extrapolating, the level-2 limit looks like ~1.0,
well below the C-S baseline of 1.28. **Lasserre level-2 in this formulation is
structurally weaker than C-S's enumeration.** Higher levels (L3 = O(n^6), L4 =
O(n^8)) might tighten the bound but rapidly become intractable.

Verdict: Lasserre L2 is not a competitive alternative to C-S at any tested n.
Either higher levels are needed (with prohibitive compute), or the SOS hierarchy
is fundamentally a poor fit for this problem class. Closes Goal 2 of
wiki/questions/2026-05-02-p2-sos-lasserre-feasibility.md (negative answer).
"""

from __future__ import annotations

import time

import cvxpy as cp


def lasserre_l2_bound(n: int, *, max_iters: int = 30000, verbose: bool = False) -> tuple[float | None, str, float]:
    """Compute the level-2 Lasserre relaxation lower bound at discretization n.

    Returns (bound_value, solver_status, solve_time_seconds).
    """
    N = 2 * n
    M = cp.Variable((N + 1, N + 1), symmetric=True)
    constraints: list = [
        M >> 0,
        M[0, 0] == 1,
        cp.sum([M[0, i + 1] for i in range(N)]) == 4 * n,
    ]
    for i in range(N):
        constraints.append(M[0, i + 1] >= 0)

    tau = cp.Variable()
    for ell in range(2, N + 1):
        for t0 in range(0, 2 * N - ell + 1):
            terms = []
            for t in range(t0, t0 + ell - 1):
                for i in range(max(0, t - (N - 1)), min(N - 1, t) + 1):
                    j = t - i
                    if 0 <= j <= N - 1:
                        terms.append(M[i + 1, j + 1])
            if terms:
                constraints.append(cp.sum(terms) / (4 * n * ell) <= tau)

    prob = cp.Problem(cp.Minimize(tau), constraints)
    t0 = time.time()
    try:
        prob.solve(solver="SCS", max_iters=max_iters, verbose=verbose)
        return prob.value, prob.status, time.time() - t0
    except Exception as e:
        return None, f"error: {e}", time.time() - t0


def main() -> None:
    print(f"{'n':>4} {'L2 bound':>10} {'status':>10} {'time (s)':>10}")
    print("-" * 40)
    for n in [1, 3, 4, 6, 8, 10, 12, 16]:
        v, status, t = lasserre_l2_bound(n)
        print(f"{n:>4} {v if v is None else f'{v:.4f}':>10} {status:>10} {t:>10.2f}")


if __name__ == "__main__":
    main()
