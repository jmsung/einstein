---
type: source
kind: paper
title: Relative Entropy Relaxations for Signomial Optimization
authors: 
year: 2014
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1409.7640
source_local: ../raw/2014-anon-relative-entropy-relaxations-signomial.pdf
topic: general-knowledge
cites:
---

# Relative Entropy Relaxations for Signomial Optimization

**Authors:** Venkat Chandrasekaran, Parikshit Shah  ·  **Year:** 2014  ·  **Source:** https://arxiv.org/abs/1409.7640

## One-line
Introduces SAGE (Sum-of-AM/GM-Exponentials) decompositions and a relative-entropy convex-optimization hierarchy that produces convergent lower bounds for non-convex signomial programs.

## Key claim
For signomial programs $f^\star = \inf_x \sum_j c_j \exp(\alpha^{(j)\prime} x)$, a hierarchy of tractable relative-entropy programs $f_{\text{SAGE}}^{(p)}$ yields a non-decreasing sequence of lower bounds that converges to $f^\star$ for broad classes of constrained and unconstrained SPs (Theorems 15, 16), with GPs solved exactly at level 0.

## Method
A signomial with at most one negative coefficient ("AM/GM-exponential") is globally nonnegative iff a dual certificate $\nu \in \mathbb{R}^\ell_+$ exists satisfying $D(\nu, e\cdot c) \le \beta$ and $Q\nu = (\mathbf{1}'\nu)\alpha$, where $D(\nu,\lambda) = \sum \nu_j \log(\nu_j/\lambda_j)$ is the relative entropy. A general signomial is "SAGE" if it decomposes into a sum of AM/GM-exponentials; this is a convex feasibility problem (joint convexity of $D$). Tightening uses powers $E_p(\{\alpha^{(j)}\})$ of the exponent set, analogous to Lasserre/Parrilo SOS hierarchies but with relative-entropy cones instead of PSD cones.

## Result
The SAGE cone $C_{\text{SAGE}}(\alpha^{(1)},\ldots,\alpha^{(\ell)})$ has an explicit representation via linear + relative-entropy inequalities (Prop. 6); it is invariant under non-singular linear transformations of exponents (Cor. 7) and robust to small perturbations of exponents (Prop. 17). Theorems 15/16 prove completeness via Krivine's Positivstellensatz applied after rational-exponent implicitization. The Motzkin polynomial — not a sum of squares — admits a short AM/GM certificate, showing SAGE can beat SOS on sparse "fewnomial" instances.

## Why it matters here
Provides an alternative to SOS/SDP for certifying nonnegativity of sparse polynomials and signomials — directly relevant to packing/autocorrelation Cohn-Elkies-style LP/SDP duals where exponent sparsity is high, and to any arena problem where the objective is naturally a posynomial/signomial (P1, P15/P16 equioscillation duals). Complements the wiki's existing SDP-flag-algebra and LP-duality findings.

## Open questions / connections
- Hybrid SAGE+SOS hierarchies for polynomial optimization — bounds at least as tight as SOS at extra cost.
- Transcendental (relative-entropy) representations of semialgebraic sets that have no compact-size SDP — proof-system separation between AM/GM and SOS certificates.
- Effective bounds on relaxation level $p$ required for a target approximation quality (currently absent from Theorems 15/16).
- Extends Ghasemi-Marshall (GP lower bounds for polynomials, ref [10]) and Reznick uniform-denominator results.

## Key terms
SAGE decomposition, AM/GM inequality, relative entropy, signomial programming, geometric programming, posynomial, Lasserre hierarchy, sum of squares, Positivstellensatz, Krivine, Motzkin polynomial, fewnomials, convex relaxation, Cohn–Elkies dual, joint convexity
