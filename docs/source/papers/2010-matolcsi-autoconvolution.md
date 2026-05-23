---
type: source
provenance: papers
author: agent
drafted: 2026-05-02
level: 4
source_type: published_paper
source_url: https://arxiv.org/abs/0907.1379
source_local: sources/2010-matolcsi-autoconvolution.pdf
cites:
  - ../papers/2010-vinuesa-sidon-thesis.md
  - ../papers/2017-cloninger-autoconvolution-sidon.md
  - ../papers/2025-jaech-autoconvolution.md
  - ../papers/2025-boyer-autoconvolution.md
  - ../papers/2026-rechnitzer-autoconvolution-digits.md
  - problem-2-first-autocorrelation/strategy.md
---

[[../home]] | [[../index]]

# Matolcsi & Vinuesa — Improved Bounds on the Supremum of Autoconvolutions

**Authors:** Máté Matolcsi, Carlos Vinuesa
**Year:** 2010 (J. Math. Anal. Appl. 372(2):439–447)
**arXiv:** 0907.1379

## Summary

For nonnegative functions f supported on [-1/4, 1/4] with ∫f = 1, what is the smallest possible value of ‖f * f‖_∞? Matolcsi and Vinuesa give an improved lower bound (S ≥ 1.262… at the time, beating the prior 1.158 from Martin-O'Bryant 2007). The improvement comes from a careful step-function ansatz combined with the LP duality on B_2[g] sets.

More importantly, they **disprove** a long-standing conjecture of Schinzel & Schmidt that the extremal function for the autoconvolution problem is the indicator of an interval. Their counterexample (an explicit asymmetric step function) opens the door to the full optimization over piecewise-constant densities used in all subsequent work (Cloninger-Steinerberger 2017, Boyer-Li 2025, Jaech-Joseph 2025, Rechnitzer 2026).

## Key Techniques

- **Step-function ansatz** — discretize [-1/4, 1/4] into N equal subintervals, optimize density vector
- **B_2[g]-set / Sidon set duality** — the autoconvolution sup matches the maximum density of g-Sidon sets
- **Linear programming relaxation** — once the step function is fixed, the bound is computable
- **Counterexample construction** — explicit asymmetric f disproving the Schinzel-Schmidt symmetry conjecture

## Relevance to Einstein Arena

### Problem 2 — First Autocorrelation

P2 is the discrete arena instantiation of exactly this autoconvolution-supremum problem. The methods used by current top arena entries (Boyer-Li 2025: SA + 575 intervals; Jaech-Joseph 2025: Adam + upsampling; Rechnitzer 2026: rigorous interval arithmetic for 128 digits) all build on the Matolcsi-Vinuesa step-function framework. Reading this paper first explains *why* discretization works and *what* the structural symmetry obstruction is.

### Problem 19 — Difference Bases (B_2[g] connection)

The autoconvolution-supremum problem is equivalent to a B_2[g]-set extremal problem in additive combinatorics. P19's difference-basis problem is in the same family. The duality articulated in this paper is the conceptual bridge.

## Limitations

- Bound 1.262 has since been improved many times (current is 1.293+ via Boyer-Li / Jaech-Joseph)
- Step functions are not extremizers — only convergent approximations
- No closed-form characterization of extremizers; existence is shown but structure is opaque
- Sharp constant remains unknown after 50+ years of work

## See Also

- [[2010-vinuesa-sidon-thesis]] — Vinuesa's PhD thesis with the full B_2[g]-Sidon framework
- [[2017-cloninger-autoconvolution-sidon]] — direct successor improving to 1.28
- [[2025-jaech-autoconvolution]] — modern arena-relevant Adam + upsampling
- [[2025-boyer-autoconvolution]] — modern SA + 575 intervals (0.901564)
- [[2026-rechnitzer-autoconvolution-digits]] — 128-digit rigorous evaluation
- [[../problem-2-first-autocorrelation/strategy]]
