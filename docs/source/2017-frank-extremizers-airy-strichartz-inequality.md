---
type: source
kind: paper
title: Extremizers for the Airy–Strichartz inequality
authors: R. Frank, Julien Sabin
year: 2017
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1712.04156
source_local: ../raw/2017-frank-extremizers-airy-strichartz-inequality.pdf
topic: general-knowledge
cites:
---

# Extremizers for the Airy–Strichartz inequality

**Authors:** R. Frank, Julien Sabin  ·  **Year:** 2017  ·  **Source:** https://arxiv.org/abs/1712.04156

## One-line
Identifies the sharp compactness threshold for maximizing sequences of the Airy–Strichartz inequality in 1D, reducing existence of extremizers to a strict inequality against an explicit multiple of the Schrödinger–Strichartz constant.

## Key claim
For $4 < p < \infty$ with $2/p + 1/q = 1/2$, every maximizing sequence for the Airy–Strichartz constant $A_p$ is precompact modulo the symmetry group $G = \{g_{t,x,\lambda}\}$ **iff** $A_p > a_p S_p$, where $S_p$ is the sharp 1D Schrödinger–Strichartz constant and $a_p = \big(\tfrac{1}{2\pi}\int_0^{2\pi}(1+\cos\theta)^{q/2}\,d\theta\big)^{p/q} > 1$ (e.g. $a_6 = 5/2$). This corrects [Shao 2009], whose threshold lacked the $a_p$ factor.

## Method
Method of the Missing Mass (Lieb) combined with a refined Airy–Strichartz inequality proved via Hausdorff–Young in 1D. A two-bubble concentration analysis at *opposite* frequencies $\pm 1/\varepsilon$ shows that frequency-antipodal concentration is energetically more favorable than single-point concentration (due to attractive Fourier interaction between bubbles), which is the mechanism producing the constant $a_p$. A Brézis–Lieb lemma for mixed Lebesgue spaces (Appendix A) and a complex-interpolation result (Appendix C) plug the gaps.

## Result
The "highest energy of non-precompact sequences" is exactly $A^*_p = a_p S_p$, and this supremum is attained by an explicit two-bubble sequence (Lemma 2.4). Consequence: if $A_p > a_p S_p$ then a maximizer exists; the real-valued constant $A_{p,\mathbb{R}}$ equals $A_p$ and has a maximizer iff $A_p$ does. In the subcritical case $\gamma < 1/p$ (Theorem 4, Appendix E), maximizers always exist unconditionally.

## Why it matters here
General background; no direct arena tie. The paper's structural ideas — Lions concentration-compactness, missing-mass via Brézis–Lieb, strict-subadditivity thresholds, "two antipodal concentration points beat one" — are functional-analysis tools relevant to autocorrelation / uncertainty / Fourier-restriction style problems on the arena where extremizer existence reduces to checking a strict-inequality energy gap.

## Open questions / connections
- Is $S_p$ attained by Gaussians for all $p > 4$? (Known only for $p = 6, 8$.) Affirmative would make the threshold $a_p S_p$ explicitly testable.
- No conjectured form for $A_p$ maximizers; even checking $A_p > a_p S_p$ requires nontrivial trial functions.
- Extends [Frank–Lieb–Sabin 2016] (Stein–Tomas on sphere) — there scaling was approximate, modulation exact; here the roles flip (modulation approximate, scaling exact).
- The negative next-order $\varepsilon$-expansion (unlike the sphere case) leaves the strict inequality (1.7) unverified even at $p=6$.

## Key terms
Airy–Strichartz inequality, Strichartz inequality, Fourier extension, Stein–Tomas, concentration-compactness, missing mass method, Brézis–Lieb lemma, two-bubble concentration, antipodal frequencies, sharp constants, extremizers, Gaussian maximizers, profile decomposition, Frank, Sabin, Shao, Foschi, Lieb
