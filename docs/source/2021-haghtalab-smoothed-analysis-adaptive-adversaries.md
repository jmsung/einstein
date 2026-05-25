---
type: source
kind: paper
title: Smoothed Analysis with Adaptive Adversaries
authors: Nika Haghtalab, Tim Roughgarden, Abhishek Shetty
year: 2021
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2102.08446
source_local: ../raw/2021-haghtalab-smoothed-analysis-adaptive-adversaries.pdf
topic: general-knowledge
cites:
---

# Smoothed Analysis with Adaptive Adversaries

**Authors:** Nika Haghtalab, Tim Roughgarden, Abhishek Shetty  ·  **Year:** 2021  ·  **Source:** https://arxiv.org/abs/2102.08446

## One-line
A coupling-based reduction that lifts smoothed-analysis guarantees from oblivious to adaptive adversaries in online learning, online discrepancy minimization, and online optimization.

## Key claim
For $\sigma$-smooth adaptive adversaries, the regret of online learning over a VC-class of dimension $d$ is $\tilde O(\sqrt{Td\ln(1/\sigma)} + d\ln(T/\sigma))$ — so under smoothing, online learnability is characterized by VC dimension, not the (often infinite) Littlestone dimension. Online Komlós discrepancy is bounded by $\tilde O(\log^2(nT/\sigma))$ under adaptive smooth isotropic inputs, and piecewise-Lipschitz function sequences are $(\sigma/\sqrt{T\ell},\tilde O(\sqrt{T\ell}))$-dispersed.

## Method
Central tool is a **coupling**: for any adaptive sequence of $\sigma$-smooth distributions producing $(X_1,\dots,X_T)$, construct a joint distribution with $kT$ i.i.d. uniform variables $Z_i^{(t)}$, $k=\Theta(\sigma^{-1}\log T)$, such that with high probability $\{X_1,\dots,X_T\}\subseteq\{Z_i^{(j)}\}$ (monotone containment). $\sigma$-smooth distributions are written as convex combinations of uniforms on sets of measure $\sigma$ (Choquet representation), enabling a per-round rejection-style coupling. This reduces anti-concentration arguments against adaptive adversaries to standard concentration on i.i.d. uniform variables, so oblivious-adversary proofs lift mechanically once the key anti-concentration step is isolated.

## Result
- Online learning: $\tilde O(\sqrt{Td\ln(1/\sigma)} + d\ln(T/\sigma))$ regret with near-matching $\Omega(\sqrt{Td\log(1/\sigma d)})$ lower bound; resolves an open question of Rakhlin–Sridharan–Tewari [RST11].
- Online Komlós discrepancy ($\ell_2$-ball, isotropic): $\ell_\infty$ discrepancy $\tilde O(\log^2(nT/\sigma))$ with high probability; also a matching lower bound $\Omega(\sqrt{T/n})$ showing isotropy is required (smoothness alone is insufficient).
- Dispersion: piecewise-Lipschitz functions with $\ell$ discontinuities per step from a smooth adaptive adversary give $(\sigma(T\ell)^{\alpha-1},\tilde O((T\ell)^\alpha))$-dispersion for any $\alpha\in[0.5,1]$, matching [BDV18] oblivious bounds up to logs.

## Why it matters here
General background; no direct arena tie. The coupling technique is a methodology for converting average-case/oblivious analyses into adaptive-adversary analyses — potentially relevant if any Arena problem reframes as online combinatorial decision-making with adversarial sequence structure, but none of the 23 problems are online learning / discrepancy / dispersion problems in the form analyzed here.

## Open questions / connections
- Can the coupling extend to multi-pass / batch optimization settings where decisions revise past choices?
- Is the $\log^2$ factor in online discrepancy tight, or does the worst-case $\log(nT)$ [ALS20] extend to adaptive smooth?
- Connection to discrepancy theory (Spencer, Komlós, Banaszczyk) — adaptive lower bound $\Omega(\sqrt{T/n})$ for non-isotropic smooth distributions sharpens the role of isotropy assumptions.
- Extends [BDV18] dispersion, [Hag18] / [HRS20] smoothed online learning, and the Spielman–Teng smoothed-analysis program [ST04] beyond running-time analysis to online performance metrics.

## Key terms
smoothed analysis, adaptive adversary, oblivious adversary, coupling argument, VC dimension, Littlestone dimension, online learning, online discrepancy, Komlós problem, dispersion, piecewise Lipschitz, anti-concentration, Spielman-Teng, Rakhlin-Sridharan-Tewari, Choquet representation
