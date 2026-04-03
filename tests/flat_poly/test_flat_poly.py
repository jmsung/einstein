"""Tests for the Flat Polynomials evaluator (Problem 12).

Verifies that our local evaluator exactly matches the arena's scoring function.
Comprehensive coverage: constraints, scoring correctness, mathematical properties,
arena cross-validation, and performance.
"""

import time

import numpy as np
import pytest
from einstein.flat_poly import (
    compute_score,
    crt_tensor,
    evaluate,
    fast_score,
    fekete,
    genetic_algorithm,
    kloosterman_sign,
    legendre_sidelnikov,
    memetic_tabu_search,
    rudin_shapiro,
    simulated_annealing,
    tabu_search,
    turyn,
)


# ---------------------------------------------------------------------------
# Reference: independent FFT-based scoring for cross-validation
# ---------------------------------------------------------------------------
def _arena_verify(coefficients):
    """Independent implementation via FFT — cross-check against np.poly1d.

    Reverses coefficients to ascending order, then uses FFT to evaluate
    the polynomial at 1M unit circle points. Different algorithm than
    the evaluator's Horner method, so a genuine cross-check.
    """
    coeffs = np.array(coefficients, dtype=np.float64)
    assert len(coeffs) == 70
    assert all(c in (-1, 1) for c in coeffs)
    # Reverse to ascending order [a_0, a_1, ..., a_69] for FFT
    ascending = coeffs[::-1]
    # FFT evaluates p(z) at z = exp(-2πi k/N), same set of points as exp(+2πi k/N)
    fft_vals = np.fft.fft(ascending, n=1_000_000)
    return float(np.max(np.abs(fft_vals)) / np.sqrt(71))


# ---------------------------------------------------------------------------
# Input validation
# ---------------------------------------------------------------------------
class TestConstraints:
    """Input validation — reject bad inputs fast."""

    def test_wrong_length_short(self):
        with pytest.raises(AssertionError, match="70"):
            evaluate({"coefficients": [1] * 69})

    def test_wrong_length_long(self):
        with pytest.raises(AssertionError, match="70"):
            evaluate({"coefficients": [1] * 71})

    def test_non_pm1_rejected(self):
        coeffs = [1] * 70
        coeffs[5] = 2
        with pytest.raises(AssertionError, match="must be"):
            evaluate({"coefficients": coeffs})

    def test_zero_rejected(self):
        coeffs = [1] * 70
        coeffs[0] = 0
        with pytest.raises(AssertionError, match="must be"):
            evaluate({"coefficients": coeffs})

    def test_nan_rejected(self):
        coeffs = [1.0] * 70
        coeffs[3] = float("nan")
        with pytest.raises(AssertionError, match="NaN"):
            evaluate({"coefficients": coeffs})

    def test_missing_key_rejected(self):
        with pytest.raises(KeyError):
            evaluate({"values": [1] * 70})

    def test_float_pm1_accepted(self):
        """±1.0 floats should work (they equal ±1 exactly)."""
        coeffs = [1.0] * 35 + [-1.0] * 35
        score = evaluate({"coefficients": coeffs})
        assert score > 0


# ---------------------------------------------------------------------------
# Scoring correctness — known shapes
# ---------------------------------------------------------------------------
class TestScoring:
    """Scoring correctness for known polynomial shapes."""

    def test_all_ones(self):
        """p(z) = z^69 + z^68 + ... + 1. At z=1: p(1) = 70.
        Score = 70 / sqrt(71) ≈ 8.307."""
        score = evaluate({"coefficients": [1] * 70})
        expected = 70.0 / np.sqrt(71)
        assert score == pytest.approx(expected, rel=1e-6)

    def test_all_neg_ones(self):
        """p(z) = -(z^69 + ... + 1). At z=1: |p(1)| = 70.
        Same score as all-ones."""
        score_pos = evaluate({"coefficients": [1] * 70})
        score_neg = evaluate({"coefficients": [-1] * 70})
        assert score_pos == pytest.approx(score_neg, rel=1e-12)

    def test_alternating_at_minus_one(self):
        """Alternating [1, -1, 1, -1, ...].
        At z=-1: p(-1) = sum_{k=0}^{69} (-1)^k * (-1)^(69-k) = -70.
        Score = 70 / sqrt(71)."""
        coeffs = [(-1) ** k for k in range(70)]
        score = evaluate({"coefficients": coeffs})
        expected = 70.0 / np.sqrt(71)
        assert score == pytest.approx(expected, rel=1e-6)

    def test_score_positive(self):
        """Score is always positive for valid inputs."""
        for seed in range(5):
            rng = np.random.default_rng(seed)
            coeffs = rng.choice([-1, 1], size=70).tolist()
            assert evaluate({"coefficients": coeffs}) > 0


# ---------------------------------------------------------------------------
# Mathematical properties
# ---------------------------------------------------------------------------
class TestMathProperties:
    """Properties that the score must satisfy."""

    def test_parseval_lower_bound(self):
        """By Parseval: ||p||_2 = sqrt(70). Since ||p||_inf >= ||p||_2,
        score >= sqrt(70)/sqrt(71) ≈ 0.993."""
        lower = np.sqrt(70) / np.sqrt(71)
        for seed in range(10):
            rng = np.random.default_rng(seed)
            coeffs = rng.choice([-1, 1], size=70).tolist()
            score = evaluate({"coefficients": coeffs})
            assert score >= lower - 1e-6, f"seed={seed}: {score} < {lower}"

    def test_deterministic(self):
        """Same coefficients always give same score."""
        coeffs = [1, -1] * 35
        s1 = evaluate({"coefficients": coeffs})
        s2 = evaluate({"coefficients": coeffs})
        assert s1 == s2

    def test_negation_same_score(self):
        """Negating all coefficients: |-p(z)| = |p(z)|. Same score."""
        rng = np.random.default_rng(7)
        coeffs = rng.choice([-1, 1], size=70).tolist()
        neg_coeffs = [-c for c in coeffs]
        s1 = evaluate({"coefficients": coeffs})
        s2 = evaluate({"coefficients": neg_coeffs})
        assert s1 == pytest.approx(s2, rel=1e-12)

    def test_reversal_same_score(self):
        """Reversing coefficients: p_rev(z) = z^69 * p(1/z).
        On the unit circle |z|=1, |p_rev(z)| = |p(1/z)| = |p(z̄)|.
        Max over unit circle is same."""
        rng = np.random.default_rng(13)
        coeffs = rng.choice([-1, 1], size=70).tolist()
        rev_coeffs = coeffs[::-1]
        s1 = evaluate({"coefficients": coeffs})
        s2 = evaluate({"coefficients": rev_coeffs})
        assert s1 == pytest.approx(s2, rel=1e-6)


# ---------------------------------------------------------------------------
# Arena cross-validation (the critical test)
# ---------------------------------------------------------------------------
class TestArenaMatch:
    """Cross-validate against independent FFT implementation."""

    @pytest.mark.parametrize("seed", range(10))
    def test_random_coefficients_match(self, seed):
        """Random ±1 polynomials: poly1d and FFT must agree."""
        rng = np.random.default_rng(seed)
        coeffs = rng.choice([-1, 1], size=70).tolist()
        ours = evaluate({"coefficients": coeffs})
        arena = _arena_verify(coeffs)
        assert ours == pytest.approx(arena, rel=1e-6), (
            f"seed={seed}: ours={ours}, arena={arena}"
        )

    def test_all_ones_match(self):
        coeffs = [1] * 70
        assert evaluate({"coefficients": coeffs}) == pytest.approx(
            _arena_verify(coeffs), rel=1e-6
        )

    def test_asymmetric_match(self):
        """Asymmetric polynomial — verifies coefficient ordering."""
        coeffs = [1] * 35 + [-1] * 35
        assert evaluate({"coefficients": coeffs}) == pytest.approx(
            _arena_verify(coeffs), rel=1e-6
        )

    def test_compute_score_matches_evaluate(self):
        """Direct call to compute_score matches evaluate wrapper."""
        rng = np.random.default_rng(99)
        coeffs = rng.choice([-1, 1], size=70).tolist()
        assert compute_score(coeffs) == evaluate({"coefficients": coeffs})


# ---------------------------------------------------------------------------
# Performance
# ---------------------------------------------------------------------------
class TestPerformance:
    """Ensure evaluation is fast enough for optimization."""

    def test_single_eval_under_200ms(self):
        """Single evaluation should complete in < 200ms."""
        coeffs = [1] * 70
        t0 = time.perf_counter()
        for _ in range(3):
            evaluate({"coefficients": coeffs})
        elapsed = (time.perf_counter() - t0) / 3
        assert elapsed < 0.2, f"Single eval took {elapsed:.4f}s (target < 200ms)"


# ---------------------------------------------------------------------------
# Constructions — known polynomial families
# ---------------------------------------------------------------------------
class TestRudinShapiro:
    """Rudin-Shapiro sequence construction."""

    def test_length(self):
        assert len(rudin_shapiro()) == 70

    def test_all_pm1(self):
        rs = rudin_shapiro()
        assert all(c in (-1, 1) for c in rs)

    def test_known_prefix(self):
        """First 8 RS values: r(n) = (-1)^(count of '11' in binary of n).
        n=0: 0b0 -> 0 -> 1
        n=1: 0b1 -> 0 -> 1
        n=2: 0b10 -> 0 -> 1
        n=3: 0b11 -> 1 -> -1
        n=4: 0b100 -> 0 -> 1
        n=5: 0b101 -> 0 -> 1
        n=6: 0b110 -> 1 -> -1
        n=7: 0b111 -> 2 -> 1"""
        rs = rudin_shapiro()
        assert rs[:8] == [1, 1, 1, -1, 1, 1, -1, 1]

    def test_valid_score(self):
        """RS construction produces a valid, finite score."""
        rs = rudin_shapiro()
        # Reverse to descending order for compute_score
        score = compute_score(rs[::-1])
        assert 0.99 < score < 10

    def test_custom_length(self):
        assert len(rudin_shapiro(n=128)) == 128


class TestFekete:
    """Fekete polynomial (Legendre symbol) construction."""

    def test_length(self):
        assert len(fekete()) == 70

    def test_all_pm1(self):
        """All coefficients must be ±1 (no zeros)."""
        fk = fekete()
        assert all(c in (-1, 1) for c in fk)

    def test_valid_score(self):
        fk = fekete()
        score = compute_score(fk[::-1])
        assert 0.99 < score < 10

    def test_prime_67(self):
        """Fekete for p=67 should return 66 coefficients."""
        fk = fekete(p=67, n=66)
        assert len(fk) == 66
        assert all(c in (-1, 1) for c in fk)


class TestTuryn:
    """Turyn (shifted Fekete) polynomial construction."""

    def test_length(self):
        assert len(turyn()) == 70

    def test_all_pm1(self):
        ty = turyn()
        assert all(c in (-1, 1) for c in ty)

    def test_valid_score(self):
        ty = turyn()
        score = compute_score(ty[::-1])
        assert 0.99 < score < 10

    def test_different_shifts_differ(self):
        """Different shift values should produce different polynomials."""
        t1 = turyn(shift=10)
        t2 = turyn(shift=18)
        assert t1 != t2


class TestBaselineScores:
    """Evaluate all constructions and verify scores are reasonable."""

    def test_all_constructions_beat_all_ones(self):
        """All constructions should beat the trivial all-ones (score ≈ 8.3)."""
        all_ones_score = 70.0 / np.sqrt(71)
        for name, coeffs in [
            ("rudin_shapiro", rudin_shapiro()),
            ("fekete", fekete()),
            ("turyn", turyn()),
        ]:
            score = compute_score(coeffs[::-1])
            assert score < all_ones_score, f"{name}: {score} >= {all_ones_score}"

    def test_structured_beats_random_avg(self):
        """Best structured construction should beat average random score."""
        random_scores = []
        for seed in range(50):
            rng = np.random.default_rng(seed)
            coeffs = rng.choice([-1, 1], size=70).tolist()
            random_scores.append(compute_score(coeffs))
        avg_random = np.mean(random_scores)

        structured_scores = [
            compute_score(rudin_shapiro()[::-1]),
            compute_score(fekete()[::-1]),
            compute_score(turyn()[::-1]),
        ]
        best_structured = min(structured_scores)
        assert best_structured < avg_random, (
            f"Best structured {best_structured:.4f} >= avg random {avg_random:.4f}"
        )


class TestNovelConstructions:
    """Novel constructions from mathematician council research."""

    def test_crt_tensor_length(self):
        assert len(crt_tensor([1, -1], [1, 1, -1, -1, 1], [1, 1, -1, 1, -1, -1, 1])) == 70

    def test_crt_tensor_all_pm1(self):
        seq = crt_tensor([1, -1], [1, 1, -1, -1, 1], [1, 1, -1, 1, -1, -1, 1])
        assert all(c in (-1, 1) for c in seq)

    def test_crt_tensor_valid_score(self):
        seq = crt_tensor([1, -1], [1, 1, -1, -1, 1], [1, 1, -1, 1, -1, -1, 1])
        score = compute_score(seq[::-1])
        assert 0.99 < score < 10

    def test_kloosterman_sign_length(self):
        assert len(kloosterman_sign()) == 70

    def test_kloosterman_sign_all_pm1(self):
        seq = kloosterman_sign()
        assert all(c in (-1, 1) for c in seq)

    def test_kloosterman_sign_valid_score(self):
        score = compute_score(kloosterman_sign()[::-1])
        assert 0.99 < score < 10

    def test_legendre_sidelnikov_length(self):
        assert len(legendre_sidelnikov()) == 70

    def test_legendre_sidelnikov_all_pm1(self):
        seq = legendre_sidelnikov()
        assert all(c in (-1, 1) for c in seq)

    def test_legendre_sidelnikov_valid_score(self):
        score = compute_score(legendre_sidelnikov()[::-1])
        assert 0.99 < score < 10


# ---------------------------------------------------------------------------
# Fast scorer (FFT-based, for optimization loops)
# ---------------------------------------------------------------------------
class TestFastScore:
    """FFT-based fast scorer for optimization."""

    def test_matches_compute_score(self):
        """fast_score should agree with compute_score within tolerance."""
        rng = np.random.default_rng(42)
        for _ in range(5):
            ascending = rng.choice([-1, 1], size=70).tolist()
            descending = ascending[::-1]
            exact = compute_score(descending)
            fast = fast_score(ascending, n_points=1_000_000)
            assert fast == pytest.approx(exact, rel=1e-4), (
                f"fast={fast}, exact={exact}"
            )

    def test_various_n_points(self):
        """Should work at different evaluation resolutions."""
        ascending = [1] * 70
        for n in [10_000, 100_000, 1_000_000]:
            score = fast_score(ascending, n_points=n)
            expected = 70.0 / np.sqrt(71)
            assert score == pytest.approx(expected, rel=1e-3)

    def test_faster_than_poly1d(self):
        """FFT at 100K should be faster than poly1d at 1M."""
        ascending = list(np.random.default_rng(0).choice([-1, 1], size=70))
        descending = ascending[::-1]

        t0 = time.perf_counter()
        for _ in range(5):
            fast_score(ascending, n_points=100_000)
        fast_time = (time.perf_counter() - t0) / 5

        t0 = time.perf_counter()
        for _ in range(5):
            compute_score(descending)
        slow_time = (time.perf_counter() - t0) / 5

        assert fast_time < slow_time, f"fast={fast_time:.4f}s >= slow={slow_time:.4f}s"


# ---------------------------------------------------------------------------
# Simulated annealing
# ---------------------------------------------------------------------------
class TestSimulatedAnnealing:
    """Simulated annealing optimizer."""

    def test_improves_from_random(self):
        """SA should improve a random starting point."""
        rng = np.random.default_rng(42)
        init = rng.choice([-1, 1], size=70).tolist()
        init_score = fast_score(init)
        best_coeffs, best_score = simulated_annealing(
            init, n_iters=10_000, seed=42,
        )
        assert best_score < init_score

    def test_improves_from_turyn(self):
        """SA should improve the Turyn baseline."""
        init = turyn(shift=22)
        init_score = fast_score(init)
        best_coeffs, best_score = simulated_annealing(
            init, n_iters=200_000, seed=7,
        )
        assert best_score < init_score

    def test_output_valid(self):
        """Output must be 70 ±1 values."""
        init = turyn(shift=22)
        best_coeffs, _ = simulated_annealing(init, n_iters=1_000, seed=0)
        assert len(best_coeffs) == 70
        assert all(c in (-1, 1) for c in best_coeffs)

    def test_deterministic(self):
        """Same seed gives same result."""
        init = [1] * 70
        _, s1 = simulated_annealing(init, n_iters=5_000, seed=123)
        _, s2 = simulated_annealing(init, n_iters=5_000, seed=123)
        assert s1 == s2


# ---------------------------------------------------------------------------
# Genetic algorithm
# ---------------------------------------------------------------------------
class TestGeneticAlgorithm:
    """Genetic algorithm optimizer."""

    def test_improves_from_random(self):
        """GA should improve over random population."""
        rng = np.random.default_rng(42)
        # Average random score
        random_scores = [
            fast_score(rng.choice([-1, 1], size=70).tolist())
            for _ in range(20)
        ]
        avg_random = np.mean(random_scores)

        best_coeffs, best_score = genetic_algorithm(
            pop_size=50, n_gens=30, seed=42,
        )
        assert best_score < avg_random

    def test_warm_start(self):
        """GA with warm start from constructions should work."""
        warm = [turyn(shift=22), rudin_shapiro()]
        best_coeffs, best_score = genetic_algorithm(
            pop_size=50, n_gens=20, warm_start=warm, seed=42,
        )
        assert best_score > 0
        assert len(best_coeffs) == 70

    def test_output_valid(self):
        """Output must be 70 ±1 values."""
        best_coeffs, _ = genetic_algorithm(
            pop_size=20, n_gens=10, seed=0,
        )
        assert len(best_coeffs) == 70
        assert all(c in (-1, 1) for c in best_coeffs)


# ---------------------------------------------------------------------------
# Tabu search
# ---------------------------------------------------------------------------
class TestTabuSearch:
    """Tabu search optimizer (steepest descent with tabu list)."""

    def test_improves_from_random(self):
        """Tabu search should improve a random start."""
        rng = np.random.default_rng(42)
        init = rng.choice([-1, 1], size=70).tolist()
        init_score = fast_score(init, n_points=4096)
        best_coeffs, best_score = tabu_search(
            init, max_iter=500, n_eval_points=4096, seed=42,
        )
        assert best_score < init_score

    def test_output_valid(self):
        """Output must be 70 ±1 values."""
        rng = np.random.default_rng(0)
        init = rng.choice([-1, 1], size=70).tolist()
        best_coeffs, _ = tabu_search(init, max_iter=100, seed=0)
        assert len(best_coeffs) == 70
        assert all(c in (-1, 1) for c in best_coeffs)

    def test_deterministic(self):
        """Same seed gives same result."""
        init = [1] * 70
        _, s1 = tabu_search(init, max_iter=200, seed=77)
        _, s2 = tabu_search(init, max_iter=200, seed=77)
        assert s1 == s2

    def test_beats_sa_same_evals(self):
        """Tabu should beat SA given similar evaluation budget.
        Tabu: 200 iters x 70 neighbors = 14K evals.
        SA: 14K iters x 1 neighbor = 14K evals."""
        rng = np.random.default_rng(42)
        init = rng.choice([-1, 1], size=70).tolist()
        _, tabu_score = tabu_search(
            init, max_iter=200, n_eval_points=4096, seed=42,
        )
        _, sa_score = simulated_annealing(
            init, n_iters=14_000, n_eval_points=4096, seed=42,
        )
        assert tabu_score <= sa_score


# ---------------------------------------------------------------------------
# Memetic tabu search
# ---------------------------------------------------------------------------
class TestMemeticTabuSearch:
    """Memetic Tabu Search with population crossover."""

    def test_improves_from_random(self):
        """MTS should improve over random population."""
        rng = np.random.default_rng(42)
        random_scores = [
            fast_score(rng.choice([-1, 1], size=70).tolist(), n_points=4096)
            for _ in range(20)
        ]
        avg_random = np.mean(random_scores)
        best_coeffs, best_score = memetic_tabu_search(
            pop_size=20, n_rounds=10, max_iter_per_round=200,
            n_eval_points=4096, seed=42,
        )
        assert best_score < avg_random

    def test_warm_start(self):
        """MTS with warm start should work."""
        warm = [turyn(shift=22)]
        best_coeffs, best_score = memetic_tabu_search(
            pop_size=20, n_rounds=5, max_iter_per_round=100,
            warm_start=warm, seed=42,
        )
        assert best_score > 0
        assert len(best_coeffs) == 70

    def test_output_valid(self):
        """Output must be 70 ±1 values."""
        best_coeffs, _ = memetic_tabu_search(
            pop_size=10, n_rounds=3, max_iter_per_round=50, seed=0,
        )
        assert len(best_coeffs) == 70
        assert all(c in (-1, 1) for c in best_coeffs)
