---
type: source
kind: paper
title: Fully Adaptive Composition in Differential Privacy
authors: J. Whitehouse, Aaditya Ramdas, Ryan M. Rogers, Zhiwei Steven Wu
year: 2022
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2203.05481
source_local: ../raw/2022-whitehouse-fully-adaptive-composition-differential.pdf
topic: general-knowledge
cites:
---

# Fully Adaptive Composition in Differential Privacy

**Authors:** J. Whitehouse, Aaditya Ramdas, Ryan M. Rogers, Zhiwei Steven Wu  ·  **Year:** 2022  ·  **Source:** https://arxiv.org/abs/2203.05481

## One-line
Constructs privacy filters and odometers that match advanced-composition rates (including constants) when both algorithms AND their privacy parameters are chosen adaptively based on prior outputs.

## Key claim
For an adaptively chosen sequence of $(\epsilon_n,\delta_n)$-DP algorithms, the stopping rule "halt before $\sqrt{2\log(1/\delta')\sum \epsilon_m^2} + \tfrac{1}{2}\sum \epsilon_m^2 > \epsilon$" yields an overall $(\epsilon,\delta)$-DP interaction — matching Dwork-Rothblum-Vadhan advanced composition exactly, with no extra constants, despite full adaptivity. Also gives a privacy filter for approximate zCDP/RDP, and three families of odometers tight at chosen or all points in "intrinsic time" $V_n = \sum \epsilon_m^2$.

## Method
Reframe adaptive privacy loss as a martingale with predictable variance proxy $V_n = \sum_m \epsilon_m^2$ ("intrinsic time"), then apply Ville's inequality and recent time-uniform martingale concentration (Howard et al. 2020/2021): line-crossing bound for filters (single-point tightness), method-of-mixtures and boundary-stitching for odometers (all-time tightness up to doubly-log factor). The approximate-zCDP filter is proven via an optional-stopping argument on a non-negative supermartingale built from Rényi-divergence likelihood ratios on the "good" part of a mixture decomposition; an alternative proof reduces conditional DP to conditional randomized response.

## Result
Filter (Thm 2): improves Rogers et al. 2016 constants to match advanced composition. Approximate-zCDP filter (Thm 1) strictly generalizes Feldman-Zrnic Rényi filters and avoids the lossy DP→pDP conversion (Lemma 2: $(\epsilon,\delta)$-DP $\Rightarrow (2\epsilon, e^{2\epsilon}\delta/\epsilon)$-pDP). Odometer families (Thm 3, requiring conditional pDP) give high-prob simultaneous bounds tight at a preselected intrinsic time or, via stitching, at all times up to $\sqrt{\log\log V_n}$. Counterexample in App. F shows $(\epsilon,\delta)$-DP $\not\Rightarrow$ $(\epsilon,\delta)$-pDP, motivating the pDP odometer assumption.

## Why it matters here
General background; no direct arena tie. Possibly informs general methodology for time-uniform / stopping-time arguments via martingale concentration and "intrinsic time" reparametrizations, which could be borrowed in autocorrelation or sieve-theory budget-allocation contexts — but the paper itself is about DP composition, not extremal/discrete-geometry optimization.

## Open questions / connections
- Can odometers be made valid under $(\epsilon,\delta)$-DP (not pDP)? Authors conjecture no but leave a formal lower bound open.
- Extends Feldman-Zrnic 2021 Rényi filters and Rogers et al. 2016 originals; complements Koskela 2022 / Smith-Thakurta 2022 Gaussian-DP filters by handling catastrophic-failure tails.
- Could optimal-composition-style randomized-response reductions (Kairouz-Oh-Viswanath 2015, Murtagh-Vadhan 2016) yield even tighter adaptive filters?

## Key terms
differential privacy, advanced composition, privacy filter, privacy odometer, fully adaptive composition, zero-concentrated differential privacy, zCDP, Rényi differential privacy, martingale concentration, Ville's inequality, optional stopping theorem, time-uniform concentration, method of mixtures, boundary stitching, intrinsic time, randomized response, Whitehouse, Ramdas, Rogers, Howard
