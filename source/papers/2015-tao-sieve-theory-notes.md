---
type: source
provenance: papers
author: agent
drafted: 2026-05-02
level: 4
source_type: web_resource
source_url: https://terrytao.wordpress.com/2015/01/21/254a-notes-4-some-sieve-theory/
cites:
  - problem-7-prime-number-theorem/strategy.md
  - findings/prime-number-theorem-lp.md
  - findings/lp-solver-scaling.md
---

[[../home]] | [[../index]]

# Tao — 254A Notes 4: Some Sieve Theory

**Author:** Terence Tao
**Year:** 2015
**Source:** UCLA Math 254A lecture notes (blog post)

## Summary

Tao's sieve theory notes provide the canonical exposition of sieve theory as a linear programming problem. The key contribution for the einstein project is the LP duality framework: the sifted sum (counting elements surviving the sieve) equals the infimum of a linear functional over upper bound sieve coefficients, subject to divisibility constraints.

This directly connects to Problem 7's formulation: the arena's LP is a finite, numerical instance of the general sieve LP that Tao describes in the asymptotic setting.

## Key Concepts

- **Sieve as LP (Problem 3)**: Estimate sum of a_n over sifted elements given partial information about sums X_d = sum(a_n for n in E_d) for divisors d in a restricted set D
- **LP duality (Theorem 5)**: The sifted sum's supremum equals the infimum of sum(lambda_d * X_d) where the sieve coefficients lambda satisfy pointwise bounds. Upper bound sieve coefficients must satisfy: lambda_1 >= 1 and sum(lambda_d for d|n) >= 0 for all n|P
- **Idealized sieve (Problem 10)**: Drop remainder terms, leaving pure optimization: minimize sum(lambda_d * g(d)) subject to coefficient constraints, where g is multiplicative with 0 <= g(p) <= 1
- **Sieve dimension**: The rate kappa such that g(p) ~ kappa/p governs sieve effectiveness. Twin primes have dimension 2
- **Parity problem**: Lower bound sieves cannot achieve nontrivial bounds at large sifting levels — a fundamental barrier

## Relevance to Einstein Project

### Problem 7 (Prime Number Theorem) — Direct Theoretical Framework

The arena's P7 formulation is the *primal* of a Selberg-type sieve LP:
- **Variables**: f(k) (sieve weights on squarefree integers)
- **Objective**: maximize -sum(f(k) * log(k)/k)
- **Constraints**: sum(f(k) * floor(x/k)) <= 1 for all x

Tao's LP duality framework shows this is one side of a dual pair. The *dual* would give a certificate bounding how good any sieve weight scheme can be — potentially useful for understanding the theoretical maximum score.

### LP Solver Strategy

The idealized sieve problem (Problem 10) suggests that structured sieve weights (exploiting multiplicativity of g) could outperform generic LP solvers at large N — a potential path beyond brute-force HiGHS IPM.

## Limitations

- Blog post format — not peer-reviewed, though Tao's exposition is canonical
- Asymptotic framework — does not give finite-N numerical bounds
- Does not address the specific floor(x/k) constraint structure of the arena problem

*Last updated: 2026-04-21*
