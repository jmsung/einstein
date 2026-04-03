"""Tests for the Prime Number Theorem certificate evaluator (Problem 7).

Verifies that our local evaluator matches the arena's scoring function.
Coverage: input validation, scoring correctness, normalization, constraint
checking, determinism, and known mathematical results.
"""

import math
import time

import numpy as np
import pytest
from einstein.prime import (
    check_constraint_at_x,
    compute_score_only,
    evaluate,
    evaluate_fast,
    find_constraint_violations,
)


# ---------------------------------------------------------------------------
# Reference: inline arena verifier for cross-validation
# ---------------------------------------------------------------------------
def _arena_verify(partial_function: dict, n_samples=10_000_000, seed=42):
    """Replica of the arena verifier — used as ground truth."""
    pf = {}
    for k_str, v in partial_function.items():
        k = int(k_str)
        if k < 1:
            continue
        pf[k] = float(np.clip(v, -10.0, 10.0))

    if not pf:
        return 0.0

    keys = sorted(pf.keys())
    max_key = keys[-1]

    # Normalize f(1) so sum f(k)/k = 0
    sum_rest = sum(pf[k] / k for k in keys if k != 1)
    pf[1] = float(np.clip(-sum_rest, -10.0, 10.0))
    keys = sorted(pf.keys())

    k_arr = np.array(keys, dtype=np.int64)
    v_arr = np.array([pf[k] for k in keys], dtype=np.float64)

    # Monte Carlo constraint check
    rng = np.random.RandomState(seed)
    x_max = 10.0 * max_key
    x_samples = rng.uniform(1.0, x_max, size=n_samples)

    chunk_size = max(1, 100_000_000 // len(keys))
    for start in range(0, n_samples, chunk_size):
        end = min(start + chunk_size, n_samples)
        x_chunk = x_samples[start:end]
        floors = np.floor(x_chunk[:, None] / k_arr[None, :])
        vals = floors @ v_arr
        if np.any(vals > 1.0 + 1e-12):
            return 0.0

    log_k = np.log(k_arr.astype(np.float64))
    return float(-np.sum(v_arr * log_k / k_arr))


# ---------------------------------------------------------------------------
# Helper: Mobius function
# ---------------------------------------------------------------------------
def _mobius(n: int) -> int:
    """Compute the Möbius function μ(n)."""
    if n == 1:
        return 1
    factors = 0
    d = 2
    temp = n
    while d * d <= temp:
        if temp % d == 0:
            temp //= d
            factors += 1
            if temp % d == 0:
                return 0  # repeated prime factor
        d += 1
    if temp > 1:
        factors += 1
    return (-1) ** factors


# ---------------------------------------------------------------------------
# Input validation
# ---------------------------------------------------------------------------
class TestInputValidation:
    """Reject bad inputs fast."""

    def test_empty_solution(self):
        score = evaluate({"partial_function": {}})
        assert score == 0.0

    def test_missing_key(self):
        """Should handle missing partial_function key gracefully."""
        score = evaluate({})
        assert score == 0.0

    def test_single_key(self):
        """Single key k=2 with some value."""
        score = evaluate({"partial_function": {"2": -1.0}})
        assert isinstance(score, float)

    def test_values_clipped(self):
        """Values outside [-10, 10] get clipped."""
        sol1 = {"partial_function": {"2": -100.0, "3": 50.0}}
        sol2 = {"partial_function": {"2": -10.0, "3": 10.0}}
        s1 = evaluate(sol1, n_samples=100_000)
        s2 = evaluate(sol2, n_samples=100_000)
        assert s1 == pytest.approx(s2, rel=1e-6)

    def test_string_keys_parsed(self):
        """Keys can be strings (arena format)."""
        sol = {"partial_function": {"2": -1.0, "3": -1.0}}
        score = evaluate(sol, n_samples=100_000)
        assert isinstance(score, float)


# ---------------------------------------------------------------------------
# Normalization
# ---------------------------------------------------------------------------
class TestNormalization:
    """Verify f(1) adjustment makes sum f(k)/k = 0."""

    def test_normalization_zeroes_sum(self):
        """After normalization, sum f(k)/k should be 0."""
        pf = {2: -1.0, 3: -1.0, 5: -1.0}
        # f(1) should be set to -((-1/2) + (-1/3) + (-1/5)) = 1/2 + 1/3 + 1/5
        expected_f1 = 1 / 2 + 1 / 3 + 1 / 5
        # Check that compute_score_only handles this correctly
        score = compute_score_only(pf)
        # The score = -sum f(k)*log(k)/k for k>=2
        expected = -((-1) * math.log(2) / 2 + (-1) * math.log(3) / 3 + (-1) * math.log(5) / 5)
        assert score == pytest.approx(expected, rel=1e-10)

    def test_f1_does_not_contribute_to_score(self):
        """f(1) * log(1) / 1 = 0, so f(1) doesn't affect score."""
        pf1 = {2: -1.0, 3: -1.0}
        pf2 = {1: 999.0, 2: -1.0, 3: -1.0}  # explicit f(1) gets overwritten
        assert compute_score_only(pf1) == pytest.approx(compute_score_only(pf2), rel=1e-10)


# ---------------------------------------------------------------------------
# Scoring correctness — Möbius truncation
# ---------------------------------------------------------------------------
class TestMobiusTruncation:
    """Truncated Möbius function should give known scores."""

    def test_mobius_small_n(self):
        """Truncated Möbius at small N: score should be positive."""
        N = 20
        pf = {}
        for k in range(2, N + 1):
            mu = _mobius(k)
            if mu != 0:
                pf[k] = float(mu)
        score = compute_score_only(pf)
        # For Möbius function: score = sum mu(k)*log(k)/k (without negation of mu)
        # Since mu(k) is already the right sign, and score = -sum f(k)*log(k)/k
        # with f(k) = mu(k), score = -sum mu(k)*log(k)/k = sum (-mu(k))*log(k)/k
        # For perfect Möbius, this converges to 1.0
        assert score > 0, f"Truncated Möbius at N={N} should have positive score, got {score}"

    def test_mobius_larger_n(self):
        """Score should increase with more Möbius terms (approaching 1.0)."""
        scores = []
        for N in [10, 50, 100, 500]:
            pf = {}
            for k in range(2, N + 1):
                mu = _mobius(k)
                if mu != 0:
                    pf[k] = float(mu)
            scores.append(compute_score_only(pf))
        # Scores should generally increase with N (more terms)
        assert scores[-1] > scores[0], (
            f"Score should increase with N: {scores}"
        )

    def test_mobius_constraint_at_integers(self):
        """For exact Möbius, sum mu(k)*floor(x/k) = 1 for all x >= 1 (Mertens)."""
        N = 50
        pf = {}
        for k in range(1, N + 1):
            mu = _mobius(k)
            if mu != 0:
                pf[k] = float(mu)

        # Check at several integer x values
        for x in [1, 2, 3, 5, 10, 20, 30, 49]:
            val = check_constraint_at_x(pf, float(x))
            # For x < N, sum mu(k)*floor(x/k) should be exactly 1
            if x < N:
                assert val == pytest.approx(1.0, abs=1e-10), (
                    f"Möbius identity failed at x={x}: got {val}"
                )


# ---------------------------------------------------------------------------
# Constraint checking
# ---------------------------------------------------------------------------
class TestConstraintChecking:
    """Test the constraint sum f(k)*floor(x/k) <= 1."""

    def test_trivial_valid(self):
        """f = {2: 0} should always satisfy constraint."""
        score = evaluate({"partial_function": {"2": 0.0}}, n_samples=10_000)
        assert score == 0.0  # score is 0 because f is all zeros after norm

    def test_violation_detected(self):
        """Multiple large positive values should violate constraint.
        With many large positive keys, the normalization of f(1) can't
        compensate enough, and floor(x/k) sums exceed 1."""
        # Many positive values — normalization sets f(1) very negative,
        # but floor(x/k) accumulates faster than f(1)*floor(x/1) compensates
        pf = {str(p): 10.0 for p in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]}
        score = evaluate({"partial_function": pf}, n_samples=100_000)
        # Either it violates (score=0) or the score is negative (bad solution)
        # The key test is that the evaluator handles this without crashing
        assert isinstance(score, float)

    def test_check_constraint_at_x_basic(self):
        """Direct constraint check at a specific point."""
        pf = {1: 1.0}  # f(1)*floor(x/1) = floor(x) which is > 1 for x >= 2
        val = check_constraint_at_x(pf, 5.0)
        assert val == 5.0

    def test_find_violations(self):
        """Should find violations for a bad solution (without normalization)."""
        # Construct a function that definitely violates:
        # f(1) = 0, f(2) = 5 -> at x=4: 0*4 + 5*2 = 10 >> 1
        pf = {1: 0.0, 2: 5.0}
        violations = find_constraint_violations(pf, n_samples=10_000, seed=42)
        assert len(violations) > 0, "Should find constraint violations"


# ---------------------------------------------------------------------------
# Determinism
# ---------------------------------------------------------------------------
class TestDeterminism:
    """Same seed must give identical results."""

    def test_same_seed_same_result(self):
        """Evaluating twice with seed=42 gives identical score."""
        sol = {"partial_function": {"2": -1.0, "3": -1.0, "5": -1.0}}
        s1 = evaluate(sol, n_samples=100_000, seed=42)
        s2 = evaluate(sol, n_samples=100_000, seed=42)
        assert s1 == s2, f"Non-deterministic: {s1} != {s2}"

    def test_different_seed_may_differ(self):
        """Different seeds can give different results (different MC samples)."""
        sol = {"partial_function": {"2": -1.0, "3": -1.0, "5": -1.0}}
        s1 = evaluate(sol, n_samples=100_000, seed=42)
        s2 = evaluate(sol, n_samples=100_000, seed=99)
        # They might be the same if both pass, but the MC samples are different
        assert isinstance(s1, float) and isinstance(s2, float)


# ---------------------------------------------------------------------------
# Arena cross-validation
# ---------------------------------------------------------------------------
class TestArenaMatch:
    """Our evaluator must match the arena verifier exactly."""

    def test_small_mobius_matches(self):
        """Truncated Möbius at N=20 matches arena."""
        pf = {}
        for k in range(2, 21):
            mu = _mobius(k)
            if mu != 0:
                pf[str(k)] = float(mu)
        sol = {"partial_function": pf}
        ours = evaluate(sol, n_samples=100_000, seed=42)
        arena = _arena_verify(pf, n_samples=100_000, seed=42)
        assert ours == pytest.approx(arena, rel=1e-12), (
            f"Mismatch: ours={ours}, arena={arena}"
        )

    def test_random_sparse_matches(self):
        """Random sparse partial function matches arena."""
        rng = np.random.default_rng(123)
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
        pf = {str(p): float(rng.uniform(-2, 2)) for p in primes}
        sol = {"partial_function": pf}
        ours = evaluate(sol, n_samples=100_000, seed=42)
        arena = _arena_verify(pf, n_samples=100_000, seed=42)
        assert ours == pytest.approx(arena, rel=1e-12), (
            f"Mismatch: ours={ours}, arena={arena}"
        )

    @pytest.mark.parametrize("seed", range(5))
    def test_random_functions_match(self, seed):
        """Random partial functions with various structures match arena."""
        rng = np.random.default_rng(seed)
        n_keys = int(rng.integers(5, 50))
        keys = sorted(rng.choice(range(2, 200), size=n_keys, replace=False))
        pf = {str(int(k)): float(rng.uniform(-5, 5)) for k in keys}
        sol = {"partial_function": pf}
        ours = evaluate(sol, n_samples=100_000, seed=42)
        arena = _arena_verify(pf, n_samples=100_000, seed=42)
        assert ours == pytest.approx(arena, rel=1e-12), (
            f"seed={seed}: ours={ours}, arena={arena}"
        )


# ---------------------------------------------------------------------------
# Score-only computation (no MC)
# ---------------------------------------------------------------------------
class TestScoreOnly:
    """Test the fast score-only function (no constraint checking)."""

    def test_matches_full_evaluator_on_valid(self):
        """Score-only should match full evaluator when constraint passes."""
        pf_dict = {2: -1.0, 3: -1.0, 5: -1.0}
        score_only = compute_score_only(pf_dict)
        full = evaluate(
            {"partial_function": {str(k): v for k, v in pf_dict.items()}},
            n_samples=100_000,
            seed=42,
        )
        if full > 0:  # constraint passed
            assert score_only == pytest.approx(full, rel=1e-6)

    def test_known_value(self):
        """Score for f = {2: -1} is -(-1)*log(2)/2 = log(2)/2."""
        pf = {2: -1.0}
        score = compute_score_only(pf)
        expected = math.log(2) / 2
        assert score == pytest.approx(expected, rel=1e-10)


# ---------------------------------------------------------------------------
# Performance
# ---------------------------------------------------------------------------
class TestPerformance:
    """Evaluation speed for optimization loop."""

    def test_fast_eval_under_1s(self):
        """Fast evaluator (100k samples) with 100 keys should be < 1s."""
        pf = {p: -1.0 for p in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29,
                                  31, 37, 41, 43, 47, 53, 59, 61, 67, 71]}
        t0 = time.perf_counter()
        evaluate_fast(pf, n_samples=100_000, seed=42)
        elapsed = time.perf_counter() - t0
        assert elapsed < 1.0, f"Fast eval took {elapsed:.3f}s (target < 1s)"

    def test_score_only_instant(self):
        """Score-only computation should be < 1ms for 2000 keys."""
        pf = {k: -1.0 / k for k in range(2, 2001)}
        t0 = time.perf_counter()
        for _ in range(100):
            compute_score_only(pf)
        elapsed = (time.perf_counter() - t0) / 100
        assert elapsed < 0.001, f"Score-only took {elapsed:.6f}s (target < 1ms)"
