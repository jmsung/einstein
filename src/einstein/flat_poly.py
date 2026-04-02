"""Evaluator for the Flat Polynomials problem (Problem 12).

Exact replica of the arena verifier. Given 70 coefficients in {+1, -1}
(descending degree order per np.poly1d convention), evaluates
max|p(z)| / sqrt(71) on 1M unit circle points.

Lower score is better.
"""

import numpy as np

N_POINTS = 1_000_000
NORM = np.sqrt(71)


def compute_score(coefficients: list[int]) -> float:
    """Compute flat polynomial score.

    Args:
        coefficients: 70 values in {-1, +1}, descending degree order
            (coefficients[0] * z^69 + ... + coefficients[69]).

    Returns:
        max|p(z)| / sqrt(71) over 1M unit circle points.
    """
    coeffs = np.asarray(coefficients, dtype=np.float64)
    if len(coeffs) != 70:
        raise AssertionError(f"Expected 70 coefficients, got {len(coeffs)}.")
    if np.isnan(coeffs).any():
        raise AssertionError("Coefficients contain NaN values.")
    if not np.all((coeffs == 1) | (coeffs == -1)):
        raise AssertionError("All coefficients must be +1 or -1.")

    p = np.poly1d(coeffs)
    z = np.exp(2j * np.pi * np.arange(N_POINTS) / N_POINTS)
    return float(np.max(np.abs(p(z))) / NORM)


def evaluate(data: dict) -> float:
    """Score a solution for Problem 12. Matches arena verifier exactly."""
    return compute_score(data["coefficients"])


# ---------------------------------------------------------------------------
# Known constructions (return ascending order: a_0, a_1, ..., a_{n-1})
# Reverse with [::-1] before passing to compute_score.
# ---------------------------------------------------------------------------


def rudin_shapiro(n: int = 70) -> list[int]:
    """Generate first n terms of the Rudin-Shapiro sequence.

    r(k) = (-1)^(number of occurrences of '11' in binary of k).
    At power-of-2 lengths, max|p(z)| <= sqrt(2) * sqrt(n).
    """
    seq = []
    for k in range(n):
        # Count overlapping "11" pairs in binary representation
        b = bin(k)[2:]  # strip "0b"
        count = sum(1 for i in range(len(b) - 1) if b[i] == "1" and b[i + 1] == "1")
        seq.append((-1) ** count)
    return seq


def _legendre(a: int, p: int) -> int:
    """Legendre symbol (a/p) via Euler's criterion."""
    a = a % p
    if a == 0:
        return 0
    ls = pow(a, (p - 1) // 2, p)
    return -1 if ls == p - 1 else ls


def fekete(p: int = 71, n: int = 70) -> list[int]:
    """Fekete polynomial coefficients using Legendre symbol.

    a_k = (k+1 / p) for k = 0, ..., n-1.
    Uses indices 1..n to avoid the zero at (0/p).
    """
    return [_legendre(k + 1, p) for k in range(n)]


def turyn(p: int = 71, n: int = 70, shift: int | None = None) -> list[int]:
    """Turyn (shifted Fekete) polynomial coefficients.

    a_k = ((k + shift) mod p / p) for k = 0, ..., n-1.
    Zero entries (when (k+shift) ≡ 0 mod p) are set to +1.
    Default shift ≈ p/4 (optimal for asymptotic Mahler measure).
    """
    if shift is None:
        shift = p // 4
    coeffs = []
    for k in range(n):
        val = _legendre((k + shift) % p, p)
        coeffs.append(val if val != 0 else 1)
    return coeffs


# ---------------------------------------------------------------------------
# Fast scorer + optimizers (ascending order: a_0, a_1, ..., a_{n-1})
# ---------------------------------------------------------------------------


def fast_score(
    coeffs_ascending: list[int] | np.ndarray,
    n_points: int = 100_000,
) -> float:
    """FFT-based scoring for optimization loops.

    Args:
        coeffs_ascending: Coefficients in ascending order [a_0, ..., a_{n-1}].
        n_points: Number of unit circle evaluation points.

    Returns:
        max|p(z)| / sqrt(71).
    """
    fft_vals = np.fft.fft(coeffs_ascending, n=n_points)
    return float(np.max(np.abs(fft_vals)) / NORM)


def simulated_annealing(
    init_coeffs: list[int],
    n_iters: int = 1_000_000,
    t_start: float = 0.5,
    t_end: float = 1e-4,
    n_eval_points: int = 100_000,
    seed: int = 42,
) -> tuple[list[int], float]:
    """Simulated annealing with single-bit-flip and FFT delta updates.

    Args:
        init_coeffs: Initial ±1 coefficients in ascending order.
        n_iters: Number of SA iterations.
        t_start: Starting temperature.
        t_end: Final temperature.
        n_eval_points: FFT evaluation points (100K default).
        seed: RNG seed for reproducibility.

    Returns:
        (best_coefficients, best_score) — ascending order.
    """
    rng = np.random.default_rng(seed)
    n = len(init_coeffs)
    coeffs = np.array(init_coeffs, dtype=np.float64)
    N = n_eval_points

    # Precompute twiddle factors: twiddle[j, k] = exp(-2πi j k / N)
    k_idx = np.arange(N)
    twiddle = np.exp(-2j * np.pi * np.arange(n)[:, None] * k_idx[None, :] / N)

    # Initial FFT values via matrix multiply
    fft_vals = coeffs @ twiddle
    score = float(np.max(np.abs(fft_vals)) / NORM)
    best_score = score
    best_coeffs = coeffs.copy()

    # Log-linear temperature schedule
    log_t_start = np.log(t_start)
    log_t_end = np.log(t_end)

    for i in range(n_iters):
        j = rng.integers(n)
        delta = -2.0 * coeffs[j]

        # O(N) delta update
        new_fft_vals = fft_vals + delta * twiddle[j]
        new_score = float(np.max(np.abs(new_fft_vals)) / NORM)

        # Metropolis acceptance
        t = np.exp(log_t_start + (log_t_end - log_t_start) * i / n_iters)
        delta_score = new_score - score
        if delta_score < 0 or rng.random() < np.exp(-delta_score / t):
            coeffs[j] *= -1
            fft_vals = new_fft_vals
            score = new_score
            if score < best_score:
                best_score = score
                best_coeffs = coeffs.copy()

    return best_coeffs.astype(int).tolist(), best_score


def genetic_algorithm(
    pop_size: int = 200,
    n_gens: int = 500,
    mutation_rate: float = 0.03,
    n_eval_points: int = 100_000,
    n_coeffs: int = 70,
    warm_start: list[list[int]] | None = None,
    seed: int = 42,
) -> tuple[list[int], float]:
    """Genetic algorithm with tournament selection and uniform crossover.

    Args:
        pop_size: Population size.
        n_gens: Number of generations.
        mutation_rate: Per-bit mutation probability.
        n_eval_points: FFT evaluation points.
        n_coeffs: Number of polynomial coefficients.
        warm_start: Optional list of initial solutions (ascending order).
        seed: RNG seed.

    Returns:
        (best_coefficients, best_score) — ascending order.
    """
    rng = np.random.default_rng(seed)

    # Initialize population
    pop = rng.choice([-1, 1], size=(pop_size, n_coeffs)).astype(np.float64)
    if warm_start:
        for i, ws in enumerate(warm_start[:pop_size]):
            pop[i] = np.array(ws, dtype=np.float64)

    def _eval_pop(population: np.ndarray) -> np.ndarray:
        """Evaluate entire population via FFT."""
        scores = np.empty(len(population))
        for idx in range(len(population)):
            fft_vals = np.fft.fft(population[idx], n=n_eval_points)
            scores[idx] = np.max(np.abs(fft_vals)) / NORM
        return scores

    scores = _eval_pop(pop)
    best_idx = np.argmin(scores)
    best_score = float(scores[best_idx])
    best_coeffs = pop[best_idx].copy()

    for _ in range(n_gens):
        # Tournament selection (k=3)
        new_pop = np.empty_like(pop)
        for i in range(pop_size):
            candidates = rng.integers(pop_size, size=3)
            winner = candidates[np.argmin(scores[candidates])]
            new_pop[i] = pop[winner]

        # Uniform crossover
        for i in range(0, pop_size - 1, 2):
            mask = rng.random(n_coeffs) < 0.5
            child1 = np.where(mask, new_pop[i], new_pop[i + 1])
            child2 = np.where(mask, new_pop[i + 1], new_pop[i])
            new_pop[i] = child1
            new_pop[i + 1] = child2

        # Bit-flip mutation
        flip_mask = rng.random((pop_size, n_coeffs)) < mutation_rate
        new_pop[flip_mask] *= -1

        # Elitism: keep best from previous generation
        new_pop[0] = best_coeffs

        pop = new_pop
        scores = _eval_pop(pop)

        gen_best_idx = np.argmin(scores)
        if scores[gen_best_idx] < best_score:
            best_score = float(scores[gen_best_idx])
            best_coeffs = pop[gen_best_idx].copy()

    return best_coeffs.astype(int).tolist(), best_score
