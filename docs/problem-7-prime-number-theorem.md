# Problem 7: The Prime Number Theorem

## Problem

Construct a partial function f: integers -> reals that maximizes the score
S(f) = -sum f(k) log(k) / k, subject to the constraint that
sum f(k) floor(x/k) <= 1 for all x >= 1, and sum f(k)/k = 0 (enforced by normalizing f(1)).

The theoretical maximum S = 1.0 is achieved by the Mobius function mu(n), since
sum mu(k) floor(x/k) = 1 for all x >= 1 (the Mobius inversion identity).

## Background

This problem is connected to elementary proofs of the Prime Number Theorem.
The Selberg-Erdos approach shows that if one can construct an arithmetic function
satisfying the constraint with a score close to 1, it yields quantitative bounds on
the distribution of primes.

## Arena Details

- **API ID**: 7
- **Direction**: maximize (higher S is better)
- **Solution format**: `{"partial_function": {"k": v, ...}}`
- **Constraint validation**: Monte Carlo sampling (10M samples, seed=42)
- **Normalization**: f(1) is set so that sum f(k)/k = 0

## Approach

1. **Mobius baseline**: Truncated Mobius function provides a natural starting point
2. **Linear programming**: Cutting-plane LP formulation over squarefree integers
3. **Cloud compute**: Large-scale LP on Modal for extended variable counts

## Infrastructure

- `src/einstein/prime/evaluator.py` -- arena-matching evaluator with MC constraint validation
- `scripts/prime/optimize_prime.py` -- cutting-plane LP optimizer
- `scripts/prime/modal_prime_lp.py` -- cloud LP solver on Modal
- `tests/prime/test_prime.py` -- evaluator tests and arena cross-validation

## References

- Selberg (1949) -- An elementary proof of the prime-number theorem
- Erdos (1949) -- On a new method in elementary number theory
- Diamond (1982) -- Elementary methods in the study of the distribution of prime numbers

*Last updated: 2026-04-03*
