"""Evaluator for the Prime Number Theorem certificate problem (Problem 7).

Exact replica of the arena verifier. Given a partial function f: integers -> floats,
computes score S(f) = -sum f(k)*log(k)/k subject to the constraint that
sum f(k)*floor(x/k) <= 1 for all x >= 1.

The constraint is validated via Monte Carlo sampling (10M samples, seed=42).

Higher S is better. Theoretical maximum S = 1.0 (achieved by Möbius function).
"""

import math

import numpy as np


def evaluate(
    data: dict,
    *,
    n_samples: int = 10_000_000,
    seed: int = 42,
) -> float:
    """Score a solution for Problem 7. Matches arena verifier exactly.

    Args:
        data: {"partial_function": {"k": v, ...}} with string or int keys.
        n_samples: Number of Monte Carlo samples for constraint validation.
        seed: RNG seed for deterministic Monte Carlo.

    Returns:
        Score S(f) = -sum f(k)*log(k)/k, or 0.0 if constraint violated.
    """
    pf_raw = data.get("partial_function", data)
    if not pf_raw:
        return 0.0

    # Parse keys to integers, values to floats, clip to [-10, 10]
    pf = {}
    for k_str, v in pf_raw.items():
        k = int(k_str)
        if k < 1:
            continue
        pf[k] = float(np.clip(v, -10.0, 10.0))

    if not pf:
        return 0.0

    keys = sorted(pf.keys())
    max_key = keys[-1]

    # Normalize: adjust f(1) so that sum f(k)/k = 0
    sum_fk_over_k = sum(pf[k] / k for k in keys if k != 1)
    # f(1)/1 + sum_rest = 0 => f(1) = -sum_rest
    pf[1] = -sum_fk_over_k
    pf[1] = float(np.clip(pf[1], -10.0, 10.0))

    # Rebuild keys after normalization may have added key 1
    keys = sorted(pf.keys())

    # Pre-compute arrays for vectorized evaluation
    k_arr = np.array(keys, dtype=np.int64)
    v_arr = np.array([pf[k] for k in keys], dtype=np.float64)

    # Monte Carlo constraint validation
    rng = np.random.RandomState(seed)
    x_max = 10.0 * max_key
    x_samples = rng.uniform(1.0, x_max, size=n_samples)

    # Vectorized: for each x, compute sum f(k) * floor(x/k)
    # Shape: (n_samples, n_keys)
    # This can be memory-intensive for large n_keys, so process in chunks
    n_keys = len(keys)
    chunk_size = max(1, 100_000_000 // n_keys)  # ~100M elements per chunk

    for start in range(0, n_samples, chunk_size):
        end = min(start + chunk_size, n_samples)
        x_chunk = x_samples[start:end]
        # floor(x/k) for each x and k
        floors = np.floor(x_chunk[:, None] / k_arr[None, :])  # (chunk, n_keys)
        constraint_vals = floors @ v_arr  # (chunk,)
        if np.any(constraint_vals > 1.0 + 1e-12):
            return 0.0

    # Compute score: S(f) = -sum f(k) * log(k) / k
    log_k = np.log(k_arr.astype(np.float64))
    score = -np.sum(v_arr * log_k / k_arr)

    return float(score)


def evaluate_fast(
    pf: dict[int, float],
    *,
    n_samples: int = 100_000,
    seed: int = 42,
) -> float:
    """Fast evaluator for optimization loop — fewer MC samples.

    Args:
        pf: {k: v, ...} with integer keys (already parsed).
        n_samples: Fewer samples for speed.
        seed: RNG seed.

    Returns:
        Score or 0.0 if constraint violated.
    """
    return evaluate(
        {"partial_function": {str(k): v for k, v in pf.items()}},
        n_samples=n_samples,
        seed=seed,
    )


def compute_score_only(pf: dict[int, float]) -> float:
    """Compute score without constraint checking. For analysis only.

    Args:
        pf: {k: v, ...} with integer keys.

    Returns:
        S(f) = -sum f(k) * log(k) / k after normalization.
    """
    if not pf:
        return 0.0

    pf = dict(pf)  # copy
    keys = sorted(pf.keys())

    # Normalize f(1)
    sum_fk_over_k = sum(pf.get(k, 0) / k for k in keys if k != 1)
    pf[1] = -sum_fk_over_k

    keys = sorted(pf.keys())
    score = 0.0
    for k in keys:
        if k >= 2:
            score -= pf[k] * math.log(k) / k
    # f(1) * log(1) / 1 = 0 (log(1) = 0), so key 1 doesn't contribute to score
    return score


def check_constraint_at_x(pf: dict[int, float], x: float) -> float:
    """Compute sum f(k) * floor(x/k) at a specific x value.

    Returns the constraint value (must be <= 1).
    """
    total = 0.0
    for k, v in pf.items():
        total += v * math.floor(x / k)
    return total


def find_constraint_violations(
    pf: dict[int, float],
    *,
    n_samples: int = 10_000_000,
    seed: int = 42,
) -> list[tuple[float, float]]:
    """Find x values where the constraint is violated.

    Returns list of (x, constraint_value) where constraint_value > 1.
    """
    keys = sorted(pf.keys())
    max_key = max(keys)

    k_arr = np.array(keys, dtype=np.int64)
    v_arr = np.array([pf[k] for k in keys], dtype=np.float64)

    rng = np.random.RandomState(seed)
    x_max = 10.0 * max_key
    x_samples = rng.uniform(1.0, x_max, size=n_samples)

    floors = np.floor(x_samples[:, None] / k_arr[None, :])
    constraint_vals = floors @ v_arr

    violations = []
    mask = constraint_vals > 1.0 + 1e-12
    for idx in np.where(mask)[0]:
        violations.append((float(x_samples[idx]), float(constraint_vals[idx])))

    return violations
