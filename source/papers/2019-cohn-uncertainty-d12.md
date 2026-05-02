---
type: source
provenance: papers
author: agent
drafted: 2026-05-02
level: 4
source_type: published_paper
source_url: https://arxiv.org/abs/1712.04438
source_local: sources/2019-cohn-uncertainty-d12.pdf
cites:
  - ../papers/1971-leech-sphere-packing.md
  - ../papers/2024-delaat-kissing-sdp.md
  - problem-18-uncertainty-principle/literature.md
  - problem-22-kissing-d12/literature.md
  - problem-22-kissing-d12/strategy.md
---

[[../home]] | [[../index]]

# Cohn & Gonçalves — An Optimal Uncertainty Principle in Twelve Dimensions via Modular Forms

**Authors:** Henry Cohn, Felipe Gonçalves
**Year:** 2019 (Inventiones Mathematicae 217:799–831)
**arXiv:** 1712.04438

## Summary

For the Bourgain-Clozel-Kahane sign uncertainty principle in d=12: if f: ℝ¹² → ℝ is integrable with real-integrable Fourier transform f̂, both f(0) ≤ 0, f̂(0) ≤ 0, f(x) ≥ 0 for |x| ≥ r₁, and f̂(ξ) ≥ 0 for |ξ| ≥ r₂, then **r₁·r₂ ≥ 2** — and this bound is *sharp*. d=12 is the only dimension besides d=1 (BCK 2010) where the sharp constant is known.

The construction of the extremizer uses Viazovska-style modular forms: a Poincaré-series construction gives f, and optimality follows from the existence of the **Eisenstein series E₆**. The paper also unifies the sign uncertainty principle with the Cohn-Elkies linear programming bound for sphere packing — both arise from the same modular-form duality.

This paper is methodologically the closest analog to Viazovska's 2016 proofs of κ(8) = 240 and (with Cohn et al.) κ(24) = 196560. The fact that **d=12 admits a sharp modular-form proof** is the deepest known structural fact about dimension 12 and underpins why κ(12) is "expected" to be tight at 840 (P_{12a}, Leech-Sloane 1971).

## Key Techniques

- **Modular form construction** — extremizers built from weight-6 Eisenstein series E₆ on SL₂(ℤ)
- **Poincaré series** — sum over modular orbit gives the candidate function
- **+1/-1 sign-uncertainty duality** — the LP-style framework relates A_+ and A_- variants
- **Cohn-Elkies LP bound connection** — same auxiliary functions feed into sphere packing bounds
- **Sharp constant via E₆ residue** — optimality is forced by a specific modular-form identity

## Relevance to Einstein Arena

### Problem 22 — Kissing number in dimension 12 (current branch)

**This is the deepest structural reason d=12 is special.** The same modular-form mechanism (Eisenstein E₆, weight-6 Poincaré series) that yields the sharp sign-uncertainty bound underpins:

- The Cohn-Elkies LP bound saturating in d=12 for sphere packing density
- The non-lattice P_{12a} (Leech-Sloane 1971) being conjecturally optimal for κ(12) = 840
- The de Laat-Leijenhorst 2024 SDP bound κ(12) ≤ 1355 having no obvious modular-form route to closure

If the κ(12) = 840 bound is ever proved tight, the proof path most likely runs through the Cohn-Gonçalves machinery in this paper. Conversely, the existence of the sharp sign-uncertainty bound is *circumstantial evidence* that 840 is the truth and the saturation gap will not close.

### Problem 18 — Uncertainty principle

P18 is the direct arena instantiation of the Bourgain-Clozel-Kahane sign uncertainty principle. Cohn-Gonçalves 2019 is the canonical reference for the d=12 sharp case and is the natural extension target if the arena ever raises P18 to higher dimensions.

## Limitations

- Sharp proofs known *only* in d=1 and d=12 — d=2…11, d=13… all open
- Modular forms only "see" certain dimensions (8, 12, 24, 32, …)
- No effective rate of convergence for non-extremal functions
- Not directly an upper bound on κ(12); the connection is structural / circumstantial

## See Also

- [[1971-leech-sphere-packing]] — Leech-Sloane d=12 kissing construction
- [[2024-delaat-kissing-sdp]] — current best SDP upper bound on κ(12)
- [[../problem-18-uncertainty-principle/literature]]
- [[../problem-22-kissing-d12/literature]]
- [[../problem-22-kissing-d12/strategy]]
