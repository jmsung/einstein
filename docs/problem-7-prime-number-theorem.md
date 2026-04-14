# Problem 7: The Prime Number Theorem

**Status**: JSAgent **#1**

## Problem

Construct a partial function f: integers → reals that maximizes the score S(f) = −Σ f(k) log(k) / k, subject to the constraint that Σ f(k) floor(x/k) ≤ 1 for all x ≥ 1, and Σ f(k)/k = 0 (enforced by normalizing f(1)).

The theoretical maximum S = 1.0 is achieved by the Mobius function μ(n), since Σ μ(k) floor(x/k) = 1 for all x ≥ 1 (the Mobius inversion identity).

## Background

This problem is connected to elementary proofs of the Prime Number Theorem. The Selberg-Erdős approach shows that if one can construct an arithmetic function satisfying the constraint with a score close to 1, it yields quantitative bounds on the distribution of primes.

## Arena Details

- **API ID**: 7
- **Direction**: maximize (higher S is better)
- **Solution format**: `{"partial_function": {"k": v, ...}}`
- **Constraint validation**: Monte Carlo sampling (10M samples, seed=42)
- **Normalization**: f(1) is set so that Σ f(k)/k = 0

## Approach

### Strategy Overview

The critical insight was recognizing a **domain mismatch**: this problem *looks* like analytic number theory but is actually a **linear program**. Checking arena discussions before coding revealed this, saving weeks of misguided number-theoretic approaches.

### Linear Programming Formulation

The problem is naturally a linear program: maximize a linear objective (score) subject to linear constraints (Σ f(k) floor(x/k) ≤ 1 for sampled x values). The key decisions are:

1. **Variable selection**: Restrict to squarefree integers as keys. Squarefree k values dominate the contribution because the Mobius function vanishes on non-squarefree integers. Final count: 2,000 squarefree keys (from integers up to N = 3,287).
2. **Cutting-plane iteration**: Start with a small subset of constraints, solve the LP, find violated constraints via Monte Carlo sampling, add them, repeat until no violations remain.
3. **Interior Point Method (IPM)**: With ~33,000 constraints × 2,000 variables, simplex methods time out. IPM solves in ~2,000 seconds — dramatically faster for this constraint-to-variable ratio.

### Mobius Function as Warm-Start

The truncated Mobius function μ(n) for n ≤ N provides a natural baseline that satisfies all constraints exactly (by the Mobius inversion identity). This serves as both a feasibility check and a warm-start for the LP solver.

### What Worked

- **LP formulation** — the right framework once the domain mismatch was recognized
- **IPM over simplex** — essential for the high constraint-to-variable ratio (33k × 2k)
- **Squarefree key restriction** — reduces variable count while preserving solution quality
- **Cutting-plane iteration** — efficiently handles the exponentially many constraints

### What Didn't Work

- **Number-theoretic approaches** — the problem looks like analytic number theory but isn't; formulating number-theoretic optimizations was a dead end
- **Simplex method** — times out on the full constraint matrix; IPM is required
- **Small key counts** — insufficient variables to approach the theoretical maximum

## Key Insights

- **Domain mismatch is expensive**: This problem looks like number theory but is LP. Always check arena discussions and formalize the optimization structure before choosing an approach.
- **IPM beats simplex for many-constraint problems**: When constraints >> variables, Interior Point Methods dramatically outperform simplex. This is a general principle for LP formulations of mathematical optimization problems.
- **Squarefree integers are the natural basis**: The Mobius function's structure (vanishing on non-squarefree) tells you exactly which variables to include in the LP.

## References

- Selberg (1949) — An elementary proof of the prime-number theorem
- Erdős (1949) — On a new method in elementary number theory
- Diamond (1982) — Elementary methods in the study of the distribution of prime numbers

## Infrastructure

- `src/einstein/prime/evaluator.py` — arena-matching evaluator with MC constraint validation
- `scripts/prime/optimize_prime.py` — cutting-plane LP optimizer
- `tests/prime/test_prime.py` — evaluator tests and arena cross-validation

*Last updated: 2026-04-13*
