"""Smoke test for the sieve-LP solver (Problem 7) at small N.

Validates the crossover-off HiGHS solve mechanics quickly: it returns a feasible
(worst_G <= 1) solution whose score matches the objective, without the degeneracy
stall that breaks scipy.linprog at large N.
"""

import math

import pytest

from einstein.prime.evaluator import compute_score_only

highspy = pytest.importorskip("highspy")
from einstein.prime.lp_solver import solve_sieve_lp  # noqa: E402


def _squarefree(n: int) -> list[int]:
    sf = [True] * (n + 1)
    for p in range(2, int(math.isqrt(n)) + 1):
        for m in range(p * p, n + 1, p * p):
            sf[m] = False
    return [k for k in range(2, n + 1) if sf[k]]


def test_solver_returns_feasible_optimum_small_n():
    keys = _squarefree(60)
    # Trivial Möbius-ish seed just to warm-start the constraint set.
    from sympy import mobius

    seed = {k: float(mobius(k)) for k in keys}
    f, base, worst_g, rounds = solve_sieve_lp(
        keys, seed, xcap_mult=10, time_limit=60, max_rounds=6, log=lambda *_: None
    )
    assert f is not None, "solver returned no feasible solution"
    # Feasible on the full integer grid (worst constraint <= 1 + tiny).
    assert worst_g <= 1.0 + 1e-7, f"infeasible: worst_G={worst_g}"
    # Reported base score matches the objective recomputed from f.
    pf = {k: float(v) for k, v in zip(keys, f) if abs(v) > 1e-15}
    assert compute_score_only(pf) == pytest.approx(base, abs=1e-9)
    # A nontrivial certificate scores well below the theoretical max of 1.0 at small N.
    assert 0.0 < base < 1.0
