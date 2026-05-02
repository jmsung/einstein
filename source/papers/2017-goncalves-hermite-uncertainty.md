---
type: source
provenance: papers
author: agent
drafted: 2026-05-02
level: 4
source_type: published_paper
source_url: https://arxiv.org/abs/1602.03366
source_local: sources/2017-goncalves-hermite-uncertainty.pdf
cites:
  - ../papers/2019-cohn-uncertainty-d12.md
  - problem-18-uncertainty-principle/literature.md
---

[[../home]] | [[../index]]

# Gonçalves, Oliveira e Silva & Steinerberger — Hermite Polynomials, Linear Flows on the Torus, and an Uncertainty Principle for Roots

**Authors:** Felipe Gonçalves, Diogo Oliveira e Silva, Stefan Steinerberger
**Year:** 2017 (J. Math. Anal. Appl. 451(2):678–711)
**arXiv:** 1602.03366

## Summary

Studies the Bourgain-Clozel-Kahane sign uncertainty principle in the "root" formulation: for a sufficiently nice function f: ℝ → ℝ that coincides with its Fourier transform and vanishes at the origin, what is the smallest c such that f must have a root in (c, ∞)? Prior bounds were 0.41 ≤ c ≤ 0.64. This paper improves the one-dimensional bound to **0.45 ≤ c ≤ 0.594** and tightens the higher-dimensional lower bound, while also proving:

- Extremizers exist and have *infinitely many double roots*
- A new structure result connecting Hermite polynomial pointwise evaluations to linear flows on the torus
- The structure result extends to other families of orthogonal polynomials (Laguerre, Jacobi, …)

The technical core is a torus-flow representation of Hermite values: H_n(x) for fixed x and varying n traces a quasi-periodic orbit on a torus, and equidistribution arguments give effective bounds. This is the prototype of the "modular form duality" later sharpened in Cohn-Gonçalves 2019 for d=12.

## Key Techniques

- **Hermite-flow correspondence** — H_n(x) ↔ point on torus T^k, n → ∞ becomes equidistributed
- **Self-Fourier ansatz** — restrict to functions f = f̂ to halve the constraint set
- **Eigenfunction expansion** — decompose into Fourier-Hermite (Plancherel-Rotach) basis
- **Double-root forcing** — extremizer optimization produces tangent (not transverse) zeros
- **Orthogonal-polynomial generality** — same machinery extends beyond Hermite

## Relevance to Einstein Arena

### Problem 18 — Uncertainty Principle

The Bourgain-Clozel-Kahane sign uncertainty principle is the analytic backbone of P18. This paper sharpens the 1D constant and is one of three landmark improvements (BCK 2010 → this paper 2017 → Cohn-Gonçalves 2019 sharp d=12). For arena work, the *technique* — Hermite-eigenfunction expansion + torus-flow equidistribution — is the natural tool when the arena evaluator requires explicit f satisfying the BCK conditions.

The "infinitely many double roots" structural result is also useful: any arena attempt that produces an extremizer with only finitely many roots is necessarily suboptimal in 1D.

### Cross-cutting — orthogonal polynomial methods

Hermite expansions are reusable infrastructure for the autoconvolution problems (P2, by way of Gaussian-modulated bases) and the Heilbronn / packing problems (P14–P17, by way of Fourier-eigenfunction LP bounds).

## Limitations

- Bound 0.45 ≤ c ≤ 0.594 still has a gap; sharp 1D constant remains open
- Higher-dimension improvements are *not* sharp (only d=1 BCK and d=12 Cohn-Gonçalves are known sharp)
- Extremizer existence is shown but no closed form
- 33 pages of dense analysis; not self-contained

## See Also

- [[2019-cohn-uncertainty-d12]] — Cohn-Gonçalves's sharp d=12 follow-up
- [[../problem-18-uncertainty-principle/literature]]
