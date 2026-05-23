---
type: source
provenance: papers
author: agent
drafted: 2026-05-02
level: 4
source_type: published_paper
source_url: https://arxiv.org/abs/1403.7988
source_local: sources/2017-cloninger-autoconvolution-sidon.pdf
cites:
  - ../papers/2010-matolcsi-autoconvolution.md
  - ../papers/2010-vinuesa-sidon-thesis.md
  - ../papers/2025-jaech-autoconvolution.md
  - ../papers/2025-boyer-autoconvolution.md
  - problem-2-first-autocorrelation/strategy.md
  - problem-19-difference-bases/literature.md
---

[[../home]] | [[../index]]

# Cloninger & Steinerberger — On Suprema of Autoconvolutions with an Application to Sidon Sets

**Authors:** Alexander Cloninger, Stefan Steinerberger
**Year:** 2017 (Proc. Amer. Math. Soc. 145(8):3191–3200)
**arXiv:** 1403.7988

## Summary

Tightens the Matolcsi-Vinuesa 2010 lower bound on the autoconvolution supremum: for f ≥ 0 supported on (-1/4, 1/4),
```
sup_x ∫ f(t) f(x − t) dt ≥ 1.28 · (∫ f)²,
```
where 1.28 improves on a series of earlier results (the previous best was around 1.262 from Matolcsi-Vinuesa). Proof reduces the LP relaxation to a finite case analysis: the authors derive a *relaxation* of the underlying optimization that splits into finitely many sub-cases, each solved exactly. They observe that their approach can in principle achieve constants arbitrarily close to the sharp bound — the only obstruction is **runtime**: the case enumeration grows fast.

This places the constant at 1.28 and identifies the sharp problem as a "compute-bound LP" — directly motivating the modern arena P2 attacks (Boyer-Li 2025: SA + 575 intervals at 0.901564 = 1.293 reciprocal-style, Jaech-Joseph 2025: Adam + upsampling, Rechnitzer 2026: 128-digit rigorous).

## Key Techniques

- **Finite-case LP relaxation** — replace the infinite-dimensional optimization with a sequence of finite LPs
- **Step-function refinement** — increase resolution of the discretization to tighten bounds
- **Sidon-set equivalence** — the autoconvolution constant equals the asymptotic max density of B_2[g] sets
- **Provable convergence to sharp** — the method has no fundamental ceiling; only compute limits stop it

## Relevance to Einstein Arena

### Problem 2 — First Autocorrelation

This is the conceptual link between *classical* autoconvolution analysis (Matolcsi-Vinuesa 2010, Vinuesa thesis 2010) and *modern* compute-heavy arena attacks (Boyer-Li, Jaech-Joseph, Rechnitzer). Cloninger-Steinerberger explicitly state the bottleneck — *runtime* — that the modern computational approaches are designed to overcome. Reading their finite-case-LP construction is the cleanest entry point into why discretization-then-optimization works for P2.

### Problem 19 — Difference Bases

The B_2[g] / Sidon-set equivalence (autoconvolution constant ↔ Sidon density) directly connects to P19's difference-basis framework. Same combinatorial object, different framing.

## Limitations

- Bound 1.28 has been improved (current is ~1.293 via Boyer-Li / arena agents)
- The method is provably approachable but not provably tight — no closed form for the sharp constant
- The case enumeration scales poorly without algorithmic improvements
- Pure analysis paper; no code or numerical artifacts

## See Also

- [[2010-matolcsi-autoconvolution]] — predecessor with the disproof of Schinzel-Schmidt
- [[2010-vinuesa-sidon-thesis]] — full B_2[g] / Sidon framework
- [[2025-jaech-autoconvolution]] — modern Adam + upsampling
- [[2025-boyer-autoconvolution]] — modern SA + 575 intervals
- [[../problem-2-first-autocorrelation/strategy]]
- [[../problem-19-difference-bases/literature]]
