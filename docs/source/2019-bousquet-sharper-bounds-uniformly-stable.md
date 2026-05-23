---
type: source
kind: paper
title: Sharper bounds for uniformly stable algorithms
authors: O. Bousquet, Yegor Klochkov, Nikita Zhivotovskiy
year: 2019
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1910.07833
source_local: ../raw/2019-bousquet-sharper-bounds-uniformly-stable.pdf
topic: general-knowledge
cites:
---

# Sharper bounds for uniformly stable algorithms

**Authors:** O. Bousquet, Yegor Klochkov, Nikita Zhivotovskiy  ·  **Year:** 2019  ·  **Source:** https://arxiv.org/abs/1910.07833

## One-line
Proves a sharper high-probability generalization bound for uniformly stable learning algorithms via a new moment inequality for weakly correlated sums, plus matching lower bounds.

## Key claim
For a $\gamma$-uniformly stable algorithm with loss bounded by $L$, with probability $\geq 1-\delta$: $n|R(A_S)-R_{\text{emp}}(A_S)| \lesssim n\gamma \log n \log(1/\delta) + L\sqrt{n\log(1/\delta)}$, removing the spurious $n\gamma(\log n)^2$ term from Feldman–Vondrák (2019), and lower bounds show the moment inequality is tight up to a single $\log n$ factor.

## Method
Central tool is a moment inequality (Theorem 4): for functions $g_i(Z)$ with $\mathbb{E}[g_i|Z_{[n]\setminus i}]=0$, $|\mathbb{E}[g_i|Z_i]|\leq M$, and bounded differences $\beta$ in the other coordinates, $\|\sum_i g_i\|_p \lesssim \sqrt{pn}\,\beta \lceil\log_2 n\rceil + M\sqrt{pn}$. Proof uses a dyadic nested-partition / telescoping conditional-expectation decomposition combined with Marcinkiewicz–Zygmund and McDiarmid (bounded-differences) moment inequalities — replacing Feldman–Vondrák's truncation+union-bound by triangle inequality on $L^p$ norms. Lower bound uses explicit Rademacher chaos $g_i = M Z_i + (\beta/2) Z_i \sum_{j\neq i} Z_j$ with Hitczenko's Montgomery-Smith moment bound and Paley–Zygmund.

## Result
Generalization bound (5): $n|R-R_{\text{emp}}| \lesssim n\gamma\log n \log(1/\delta) + L\sqrt{n\log(1/\delta)}$, beating both Feldman–Vondrák (2018)'s sub-Gaussian $(n\sqrt{\gamma L}+L\sqrt n)\sqrt{\log(1/\delta)}$ and FV (2019)'s mixed bound. Lemma 1 establishes the equivalence: $\|Y\|_p\leq \sqrt p\, a + p b\ \forall p$ iff $|Y|\leq a\sqrt{\log(e/\delta)}+b\log(e/\delta)$ w.p. $1-\delta$. Lower bound (Proposition 9): $\|\sum g_i\|_p \gtrsim pn\beta + M\sqrt{pn}$ for $\kappa\leq p\leq n$, matching the upper bound modulo $\log n$.

## Why it matters here
General background; no direct arena tie. The moment-via-tail equivalence (Lemma 1) and the dyadic nested-partition trick for telescoping conditional expectations are reusable concentration technology if the agent ever needs sharp probabilistic bounds on sums of weakly correlated quantities (e.g., parallel-tempering swap statistics, multistart aggregate scores).

## Open questions / connections
- Can the $\log n$ factor in Theorem 4 and bound (5) be removed entirely for $p>2$? Variance bound (16) achieves this at $p=2$, suggesting it may be an artifact.
- Find a uniformly-stable learning algorithm whose $g_i$ are bounded $|g_i|\leq L$ (with $L\sim M$) achieving the high-prob lower bound (14) — current Rademacher-chaos example has $L=\beta(n-1)\gg M$.
- Extend to unbounded losses using Kontorovich's (2014) unbounded-metric bounded-differences extensions.

## Key terms
uniform stability, generalization bound, moment inequality, bounded differences, McDiarmid inequality, Marcinkiewicz-Zygmund inequality, Rademacher sums, Montgomery-Smith bound, Paley-Zygmund, sub-Gaussian sub-exponential, Feldman-Vondrak, weakly correlated random variables, telescoping conditional expectation, dyadic partition
