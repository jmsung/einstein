---
type: source
kind: paper
title: On Regularity and Mass Concentration Phenomena for the Sign Uncertainty Principle
authors: Felipe Gonçalves, Diogo Oliveira e Silva, João P. G. Ramos
year: 2020
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2003.10765
source_local: ../raw/2020-gonalves-regularity-mass-concentration-phenomena.pdf
topic: general-knowledge
cites:
---

# On Regularity and Mass Concentration Phenomena for the Sign Uncertainty Principle

**Authors:** Felipe Gonçalves, Diogo Oliveira e Silva, João P. G. Ramos  ·  **Year:** 2020  ·  **Source:** https://arxiv.org/abs/2003.10765

## One-line
Establishes equivalence of three formulations of the Bourgain–Clozel–Kahane $+1$ sign uncertainty principle in $d=1$ (general $L^1$, bandlimited, Schwartz) and proves mass-concentration for near-minimizers of the complementary $-1$ problem in all dimensions.

## Key claim
**Theorem 1:** $A_+(1) = A_+^B(1) = A_+^S(1)$ — the sharp constant is the same whether one minimizes over $L^1$, bandlimited functions, or Schwartz functions. **Theorem 2:** For every $d \geq 1$, there exist $\varepsilon_d, \sigma_d > 0$ such that any radial $g \in \mathcal{A}_-(d)$ with $\widehat g = -g$, $g(0)=0$, and $|r(g) - A_-(d)| \leq \varepsilon_d$ satisfies $\int_{B_{r(g)}^d} g_+ \geq \sigma_d \|g\|_{L^1}$. Higher-dim improvement: $A_+^S(d) \leq (2 - \delta_d) A_+(d)$ with $\sqrt{d}(2\pi e)^{d/2}\delta_d \to 1$.

## Method
Combines (a) a Logan-style moment inequality $\int |y|^2 f(y)\,dy \leq 0$ derived from a vanishing-sequence hypothesis with (b) rearrangement / bathtub-principle estimates (Lemma 5) on superlevel sets of minimizers to force contradictions. The key technical step is showing any 1D minimizer is *strictly negative* on a punctured neighborhood of the origin, enabling convolution with a positive-definite measure $\delta_{x_0} + \delta_{-x_0} + 2\delta_0$ that strictly lowers $\widehat f(0)$ while bounding $r(\cdot)$, followed by mollification to land in $\mathcal{S}(\mathbb{R})$. Theorem 2 uses Banach–Alaoglu + Mazur's lemma on a minimizing sequence, then Jaming's higher-dim Nazarov uncertainty principle for the $L^1$ lower bound.

## Result
$A_+(1) = A_+^B(1) = A_+^S(1)$; Conjecture 1 ($A_s(d) = A_s^B(d) = A_s^S(d)$) raised in full generality. Mass-concentration $\sigma_d$ for $-1$ near-minimizers established but not quantified explicitly. Proposition 1 characterizes the unique bandlimited $+1$ minimizer with $\operatorname{supp}\widehat f \subseteq [-\tfrac12, \tfrac12]$, $r(f)=1$ as $f(x) = \alpha\,\sin^2(\pi\tfrac{x-1}{2})/(x^2-1)$. Recalls known values: $A_-(1)=1$, $A_+(12)=A_-(8)=\sqrt 2$, $A_-(24)=2$.

## Why it matters here
Directly informs **P15/P16** (Cohn–Elkies / sign-uncertainty optimization problems in the wiki, the $+1$ and $-1$ FELPP families) by certifying that searching within the Schwartz class loses nothing in $d=1$ — i.e., bandlimited/smooth ansatzes are optimal-attaining there. The bathtub-principle moment estimate (Lemma 5) and the $\delta_{x_0}+\delta_{-x_0}+2\delta_0$ convolution trick are reusable techniques for any Fourier-eigenfunction LP where the agent wants to certify regularity of near-minimizers.

## Open questions / connections
- Conjecture 1 open for $(s,d) \notin \{(+,1), (+,12), (-,1), (-,8), (-,24)\}$ — Schwartz/bandlimited equivalence unresolved in nearly all dimensions.
- Is every $+1$ minimizer nonpositive on the full ball $B_{A_+(d)}^d$? True for $d \in \{1, 12\}$; conjectured for all $d$.
- Connects to Cohn–Gonçalves [4] (modular-form construction at $d=12$) and to the sphere-packing solutions of Viazovska / Cohn–Kumar–Miller–Radchenko–Viazovska at $d \in \{8, 24\}$.
- Companion paper [6] (arXiv:2003.10771) generalizes to operator/metric-measure settings and yields discrete torus version $P_s(\mathbb{T}^d) \leq A_s^B(d)$.

## Key terms
sign uncertainty principle, Bourgain-Clozel-Kahane, Fourier eigenfunction, $+1$ eigenfunction, $-1$ eigenfunction, FELPP, Cohn-Gonçalves, Viazovska, sphere packing, bandlimited function, Schwartz class, bathtub principle, Logan extremal problem, Nazarov uncertainty, Poisson summation, mass concentration, modular forms
