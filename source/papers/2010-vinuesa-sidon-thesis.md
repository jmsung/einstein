---
type: source
provenance: papers
author: agent
drafted: 2026-05-02
level: 4
source_type: phd_thesis
source_url: https://www.icmat.es/Thesis/CVinuesa.pdf
source_local: sources/2010-vinuesa-sidon-thesis.pdf
cites:
  - ../papers/2010-matolcsi-autoconvolution.md
  - ../papers/2017-cloninger-autoconvolution-sidon.md
  - problem-2-first-autocorrelation/strategy.md
  - problem-19-difference-bases/literature.md
---

[[../home]] | [[../index]]

# Vinuesa del Río — Generalized Sidon Sets (PhD thesis, UAM 2010)

**Author:** Carlos Vinuesa del Río
**Advisor:** Javier Cilleruelo
**Year:** 2010 (Universidad Autónoma de Madrid; ICMAT)

## Summary

Comprehensive 113-page treatment of generalized Sidon sets B_h[g] — sets in which every integer can be represented as a sum of h elements in at most g ways. The thesis is the canonical reference for the additive-combinatorics machinery underpinning autoconvolution-supremum problems and Sidon-set extremal problems. Chapters cover:

1. **Generalized Sidon sets in groups** — F_p, finite cyclic groups, Singer-Bose-Chowla constructions
2. **B_h[g] sets in [1, N]** — counting bounds, density estimates, asymptotic regimes
3. **Autoconvolutions** — continuous analog, Schinzel-Schmidt conjecture (with Matolcsi disproof)
4. **Generalized Sidon sequences** — infinite versions, density results

The thesis articulates the equivalence between the discrete extremal problem (max density of B_2[g] in [1, N]) and the continuous autoconvolution-supremum problem, which is the conceptual core of arena P2 (autocorrelation) and P19 (difference bases).

## Key Techniques

- **B_h[g] formalism** — the unified framework for Sidon-like extremal sets
- **Continuous-discrete duality** — autoconvolution f*f vs. representation function r(n)
- **Singer / Bose-Chowla constructions** — perfect / near-perfect Sidon sets via finite-field projective planes
- **LP duality for B_2[g]** — the same LP that powers Matolcsi-Vinuesa 2010
- **Plünnecke-Ruzsa machinery** — sumset/difference-set inequalities for derivative bounds

## Relevance to Einstein Arena

### Problem 2 — First Autocorrelation
The thesis is the textbook for the autoconvolution-supremum problem (chapter 3 in particular). All modern arena work (Boyer-Li, Jaech-Joseph, Rechnitzer) builds on this framework. If you only read one source for P2, this is it.

### Problem 19 — Difference Bases
Chapters 1–2 cover B_2[1] (= classical Sidon) and B_2[g] sets, which are the additive-combinatorics underpinning of the difference-basis problem. The Singer-Bose-Chowla constructions in particular give the asymptotic lower bound k²/L → 1 for perfect difference sets.

### Cross-cutting — additive combinatorics framework
Plünnecke-Ruzsa and B_h[g] machinery are reusable across multiple arena problems involving sums/differences of finite sets (P2, P19, latently P1). Worth keeping the chapter-1 prerequisites at hand.

## Limitations

- Pre-2010 — does not include Cloninger-Steinerberger 2017 or any modern computational improvements
- Heavy on classical theory, light on numerical methods
- 113 pages — slow read; most arena work uses chapters 1, 3 only
- Spanish-affiliated thesis but written in English

## See Also

- [[2010-matolcsi-autoconvolution]] — co-authored short paper with the headline disproof
- [[2017-cloninger-autoconvolution-sidon]] — direct continuation
- [[2007-gyarmati-sums-differences]] — Plünnecke-Ruzsa background
- [[../problem-2-first-autocorrelation/strategy]]
- [[../problem-19-difference-bases/literature]]
