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


def period3_base(n: int = 70) -> list[int]:
    """Period-3 base sequence [-1,-1,1] repeated.

    The SOTA's first 18 coefficients are exactly [-1,-1,1]×6.
    This base provides a starting point for structured perturbation search.
    Returns ascending order.
    """
    pattern = [-1, -1, 1]
    return [pattern[k % 3] for k in range(n)]


def phi35_score(
    coeffs_ascending: list[int] | np.ndarray,
) -> float:
    """Fast score using only the 24 primitive 35th roots of unity.

    The Phi_35 cyclotomic component is the spectral bottleneck.
    ~4000x cheaper than N=100K evaluation.
    """
    coeffs = np.asarray(coeffs_ascending, dtype=np.float64)
    # Primitive 35th roots: omega_35^k for gcd(k, 35) = 1
    prim_indices = [k for k in range(35) if np.gcd(k, 35) == 1]
    z = np.exp(2j * np.pi * np.array(prim_indices) / 35)
    # Evaluate polynomial at these points
    vals = np.array([np.polyval(coeffs[::-1], zi) for zi in z])
    return float(np.max(np.abs(vals)) / NORM)


def spectral_equalization_score(
    coeffs_ascending: list[int] | np.ndarray,
    n_points: int = 4096,
    log_weight: float = 0.1,
) -> float:
    """Spectral score with log-barrier for equalization.

    Combines L-infinity (peak suppression) with negative log-spectral
    (valley lifting). Encourages equioscillation.

    score = max|p(z)|/sqrt(71) - log_weight * mean(log(|p(z)|^2))
    """
    fft_vals = np.fft.fft(coeffs_ascending, n=n_points)
    power = np.abs(fft_vals) ** 2
    peak = float(np.max(np.abs(fft_vals)) / NORM)
    # Log-barrier: penalize low valleys (add small eps to avoid log(0))
    log_term = float(np.mean(np.log(power + 1e-10)))
    return peak - log_weight * log_term


def crt_tensor(
    b2: list[int], b5: list[int], b7: list[int],
) -> list[int]:
    """CRT tensor product construction using 70 = 2 × 5 × 7.

    Maps a 2×5×7 tensor of ±1 values to a length-70 sequence via CRT bijection.
    a[CRT(i,j,k)] = b2[i] * b5[j] * b7[k] for i<2, j<5, k<7.

    Returns ascending order [a_0, ..., a_69].
    """
    seq = [0] * 70
    for i in range(2):
        for j in range(5):
            for k in range(7):
                # CRT: find x such that x≡i mod 2, x≡j mod 5, x≡k mod 7
                # 35*i mod 2=i, 21*j mod 5=j, 15*k mod 7=k
                x = (35 * i + 21 * j + 15 * k) % 70
                seq[x] = b2[i] * b5[j] * b7[k]
    return seq


def kloosterman_sign(p: int = 71, n: int = 70) -> list[int]:
    """Kloosterman sum sign sequence.

    a_k = sign(Re(K(1, k+1; p))) where K(a,b;p) = Σ exp(2πi(ax + bx⁻¹)/p).
    Novel construction — unexplored for flat polynomials.

    Returns ascending order.
    """
    coeffs = []
    zeta = np.exp(2j * np.pi / p)
    for k in range(n):
        b = k + 1  # avoid b=0
        # Kloosterman sum K(1, b; p)
        ksum = sum(zeta ** ((x + b * pow(x, p - 2, p)) % p) for x in range(1, p))
        coeffs.append(1 if ksum.real >= 0 else -1)
    return coeffs


def legendre_sidelnikov(p: int = 7, q: int = 11) -> list[int]:
    """Legendre-Sidelnikov two-prime construction, period p*(q-1).

    a_k = L_p(k mod p) * S_q(k mod (q-1)), where L_p is the Legendre
    sequence and S_q is the Sidelnikov sequence (QR of primitive root powers).

    For p=7, q=11: period 7*10 = 70.
    Returns ascending order.
    """
    period = p * (q - 1)
    # Legendre sequence of period p
    leg = [_legendre(k, p) if k % p != 0 else 1 for k in range(p)]
    # Sidelnikov sequence: find primitive root of q, then QR of powers
    g = _primitive_root(q)
    sid = [_legendre(pow(g, k, q), q) for k in range(q - 1)]
    # Combine
    return [leg[k % p] * sid[k % (q - 1)] for k in range(period)]


def _primitive_root(p: int) -> int:
    """Find the smallest primitive root modulo prime p."""
    for g in range(2, p):
        if all(pow(g, (p - 1) // f, p) != 1 for f in _prime_factors(p - 1)):
            return g
    return 2


def _prime_factors(n: int) -> list[int]:
    """Return distinct prime factors of n."""
    factors = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            factors.append(d)
            while n % d == 0:
                n //= d
        d += 1
    if n > 1:
        factors.append(n)
    return factors


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


def tabu_search(
    init_coeffs: list[int],
    max_iter: int = 1000,
    n_eval_points: int = 4096,
    seed: int = 42,
) -> tuple[list[int], float]:
    """Tabu search with vectorized all-neighbor evaluation.

    Each iteration evaluates ALL n single-flip neighbors simultaneously,
    picks the best non-tabu one (even if it worsens the score).

    Args:
        init_coeffs: Initial ±1 coefficients in ascending order.
        max_iter: Number of tabu iterations.
        n_eval_points: FFT evaluation points (4096 for speed).
        seed: RNG seed.

    Returns:
        (best_coefficients, best_score) — ascending order.
    """
    rng = np.random.default_rng(seed)
    n = len(init_coeffs)
    coeffs = np.array(init_coeffs, dtype=np.float64)
    N = n_eval_points

    # Precompute twiddle factors: (n, N)
    k_idx = np.arange(N)
    twiddle = np.exp(-2j * np.pi * np.arange(n)[:, None] * k_idx[None, :] / N)

    # Initial FFT
    fft_vals = coeffs @ twiddle
    score = float(np.max(np.abs(fft_vals)) / NORM)
    best_score = score
    best_coeffs = coeffs.copy()

    # Tabu list: tabu_until[j] = iteration when position j becomes available
    tabu_until = np.zeros(n, dtype=np.int64)
    tenure_lo = max(1, max_iter // 10)
    tenure_hi = max(2, max_iter * 12 // 100)

    for it in range(max_iter):
        # Vectorized: evaluate all n neighbors at once
        deltas = -2.0 * coeffs  # (n,)
        all_new_fft = fft_vals[None, :] + deltas[:, None] * twiddle  # (n, N)
        all_scores = np.max(np.abs(all_new_fft), axis=1) / NORM  # (n,)

        # Mask tabu positions, except aspiration (beats global best)
        mask = tabu_until > it
        aspiration = all_scores < best_score
        blocked = mask & ~aspiration
        all_scores[blocked] = np.inf

        # Pick best neighbor
        j = int(np.argmin(all_scores))
        if all_scores[j] == np.inf:
            break

        # Accept move
        coeffs[j] *= -1
        fft_vals = all_new_fft[j]
        score = float(all_scores[j])
        tabu_until[j] = it + rng.integers(tenure_lo, tenure_hi + 1)

        if score < best_score:
            best_score = score
            best_coeffs = coeffs.copy()

    return best_coeffs.astype(int).tolist(), best_score


def memetic_tabu_search(
    pop_size: int = 50,
    n_rounds: int = 100,
    max_iter_per_round: int = 1000,
    n_eval_points: int = 4096,
    n_coeffs: int = 70,
    warm_start: list[list[int]] | None = None,
    seed: int = 42,
) -> tuple[list[int], float]:
    """Memetic Tabu Search with population crossover.

    Maintains a population of solutions. Each round: select two parents,
    crossover + mutate, refine the child with tabu search, replace a
    random population member.

    Args:
        pop_size: Population size.
        n_rounds: Number of memetic rounds.
        max_iter_per_round: Tabu search iterations per child.
        n_eval_points: FFT evaluation points.
        n_coeffs: Number of polynomial coefficients.
        warm_start: Optional initial solutions (ascending order).
        seed: RNG seed.

    Returns:
        (best_coefficients, best_score) — ascending order.
    """
    rng = np.random.default_rng(seed)

    # Initialize population
    pop = [
        rng.choice([-1, 1], size=n_coeffs).tolist() for _ in range(pop_size)
    ]
    if warm_start:
        for i, ws in enumerate(warm_start[:pop_size]):
            pop[i] = list(ws)

    # Evaluate initial population
    scores = [fast_score(p, n_points=n_eval_points) for p in pop]
    best_idx = int(np.argmin(scores))
    best_score = scores[best_idx]
    best_coeffs = list(pop[best_idx])

    for r in range(n_rounds):
        # Tournament selection (k=3)
        c1 = rng.integers(pop_size, size=3)
        p1 = pop[c1[np.argmin([scores[c] for c in c1])]]
        c2 = rng.integers(pop_size, size=3)
        p2 = pop[c2[np.argmin([scores[c] for c in c2])]]

        # Uniform crossover
        child = [
            p1[i] if rng.random() < 0.5 else p2[i] for i in range(n_coeffs)
        ]

        # Mutation (flip each bit with prob 1/n)
        for i in range(n_coeffs):
            if rng.random() < 1.0 / n_coeffs:
                child[i] *= -1

        # Refine with tabu search
        child, child_score = tabu_search(
            child,
            max_iter=max_iter_per_round,
            n_eval_points=n_eval_points,
            seed=seed + r * 137,
        )

        # Replace random population member
        replace_idx = rng.integers(pop_size)
        pop[replace_idx] = child
        scores[replace_idx] = child_score

        if child_score < best_score:
            best_score = child_score
            best_coeffs = list(child)

    return best_coeffs, best_score
