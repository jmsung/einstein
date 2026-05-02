---
type: source
provenance: papers
author: agent
drafted: 2026-05-02
level: 4
source_type: published_paper
source_url: https://arxiv.org/abs/1907.09464
source_local: sources/2020-balister-flat-littlewood.pdf
cites:
  - problem-12-flat-polynomials/literature.md
  - problem-12-flat-polynomials/strategy.md
  - ../blog/bloom-erdos-problems.md
---

[[../home]] | [[../index]]

# Balister, Bollobás, Morris, Sahasrabudhe & Tiba — Flat Littlewood Polynomials Exist

**Authors:** Paul Balister, Béla Bollobás, Robert Morris, Julian Sahasrabudhe, Marius Tiba
**Year:** 2020 (Annals of Mathematics 192(3):977–1004; arXiv:1907.09464 from 2019)

## Summary

A **Littlewood polynomial** of degree n is P(z) = Σ_{k=0}^n ε_k z^k with ε_k ∈ {-1, +1}. A polynomial is *flat* if there exist absolute constants 0 < δ < Δ such that

  δ √n ≤ |P(z)| ≤ Δ √n  for all z ∈ ℂ with |z| = 1.

Balister, Bollobás, Morris, Sahasrabudhe and Tiba prove that **flat Littlewood polynomials exist for all n ≥ 2**. This resolves Erdős's 1957 Problem #26 and confirms a 1966 conjecture of Littlewood.

The upper bound P(z) ≤ Δ √n was already known (Rudin-Shapiro 1950s explicit constructions; Spencer 1985 non-constructive via discrepancy). The hard direction is the **lower bound** P(z) ≥ δ √n: Littlewood polynomials must not "dip" near zero anywhere on the unit circle. Spencer's discrepancy-theoretic upper-bound technique is part of the toolkit, but the lower bound requires new ideas.

The construction is non-trivial and uses:
- **Rudin-Shapiro recursion** — base block giving the upper bound
- **Discrepancy-theoretic random sign perturbations** — to fill in the lower bound
- **Geometric averaging arguments** — controlling worst-case z over the unit circle
- **Explicit constants** — δ and Δ are determined explicitly though large

The proof is non-constructive in the sense that it shows existence rather than giving a polynomial-time algorithm; explicit flat Littlewood polynomials for specific small n (e.g., n = 69, the arena's P12 size) are *not* directly produced by this paper.

## Key Techniques

- **Rudin-Shapiro construction** — base flat polynomials with controlled max
- **Random sign perturbation** — discrepancy theory bounds to control deviations
- **Spencer-style derandomization** — converting probabilistic bounds into existence
- **Mean-value / averaging on |z|=1** — handling worst-case z by integrating
- **Recursive doubling** — degree-n polynomial built from degree-(n/2) blocks

## Relevance to Einstein Arena

### Problem 12 — Flat Polynomials (current arena n=69)
**This is the canonical reference paper for P12.** P12 asks for the Littlewood polynomial of degree 69 minimizing max|p(z)|/√(n+1) over the unit circle. The Balister et al. proof confirms that *some* polynomial exists with this max ≤ Δ for an absolute constant Δ. Specifically:

- P12 score = max|p(z)|/√(n+1). Lower is better.
- Trivial Parseval: max|p(z)| ≥ √(n+1), so the score ≥ 1.
- Conjectured infimum (Littlewood): score → 1 as n → ∞. *Confirmed for some sequence by Balister et al.*
- Best known explicit construction: Turyn (quadratic-residue) polynomials give score ≈ 1.50 at n = 70.
- Balister et al. say there exist polynomials with score ≤ Δ, but the explicit construction is not given. Our arena work has to find them numerically.

### What this paper does and does not give us
- **Yes**: existence of a flat polynomial at n=69 (so the optimization problem is *non-vacuous* — there is something to find).
- **No**: explicit coefficients for small n. For arena work at n=69, the Balister et al. construction does not directly produce a candidate — it works asymptotically and Δ is not numerically tight.
- **Implication**: the gap between best known explicit (Turyn ~1.50) and the asymptotic existence (Δ unspecified but constant) is the room for arena search.

### Strategic takeaway for P12
- Existence of flat polynomials means **brute-force / SA / RL searches will eventually find them** for small n
- The question is *how close to the asymptotic constant Δ* one can get at n=69
- Reading this paper helps avoid the trap of "maybe no flat polynomial exists at n=69" — it does
- The proof's discrepancy-theoretic / Rudin-Shapiro structure suggests **layered random ensembles** are a productive search space for arena work

## Limitations

- Non-constructive — explicit polynomials at finite n require separate work
- Constants Δ, δ are not computed numerically; the paper proves existence with unspecified absolute constants
- The construction is asymptotic; for n = 69 (arena P12), it's unclear if the construction even applies cleanly
- Rudin-Shapiro family gives sub-optimal δ; tighter constructions remain open

## See Also

- [[../problem-12-flat-polynomials/literature]] — arena P12 literature
- [[../problem-12-flat-polynomials/strategy]] — arena P12 strategy
- [[resource-erdos-problems]] — Erdős Problem #26 is this question
