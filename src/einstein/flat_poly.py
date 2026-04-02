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
