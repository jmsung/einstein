---
type: source
kind: paper
title: "Balanced Allocations: A Simple Proof for the Heavily Loaded Case"
authors: Kunal Talwar, Udi Wieder
year: 2013
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1310.5367
source_local: ../raw/2013-talwar-balanced-allocations-simple-proof.pdf
topic: general-knowledge
cites:
---

# Balanced Allocations: A Simple Proof for the Heavily Loaded Case

**Authors:** Kunal Talwar, Udi Wieder  ·  **Year:** 2013  ·  **Source:** https://arxiv.org/abs/1310.5367

## One-line
A self-contained, computer-free proof that the two-choice balls-into-bins process keeps max-load minus average load at $(1+o(1))\log\log n$ for arbitrarily many balls.

## Key claim
For the Greedy[$d$] process with $d>1$ and any number $m$ of balls thrown into $n$ bins, the expected gap $E[G_t] \le \log_d \log n + \alpha \log\log\log n + \gamma$, with tail $\Pr[G_t \ge \log_d\log n + \alpha\log\log\log n + \gamma] \le 2/(\log\log n)^4$ — independent of $m$.

## Method
Markov-chain analysis of the normalized load vector $X^t$ combined with an exponential potential function $\Gamma = \sum_i (e^{\alpha X_i} + e^{-\alpha X_i})$ shown to be a supermartingale ($E[\Gamma(t+1)\mid x(t)] \le (1-\alpha\epsilon/4n)\Gamma + c$). This yields a "base case" bound $E[\sum_i \exp(a|X_i^t|)] \le bn$, from which a layered induction à la Azar–Broder–Karlin–Upfal propagates: if the fraction of bins at height $i$ is $\beta_i$, then $\beta_{i+1} \le 2L\beta_i^d$ holds w.h.p. via Chernoff, with the potential bound seeding the layers.

## Result
Replaces the heavy Markov-chain mixing-time + computer-aided 4-invariant induction of Berenbrink–Czumaj–Steger–Vöcking (2006) with a short potential + induction argument. Trade-off: tail bound weakens from $1-n^{-c}$ (BCSV) to $1-(\log\log n)^{-c}$, and additive constant becomes $\gamma'(c)\log\log\log n$ instead of $\gamma(c)$. The technique extends cleanly to weighted balls (bounded weight $W$: gap $\le 2\log_d\log n + O(1)$ when $W\in\{1,2\}$) and to Vöcking's Left[$d$] scheme (gap $\log\log n / d\ln\phi_d$).

## Why it matters here
General background; no direct arena tie — load-balancing / balls-into-bins is not among the 23 Einstein Arena problem families (sphere packing, autocorrelation, kissing, discrete geometry, extremal graph, sieve, uncertainty). The layered-induction + exponential-potential pattern is a generic technique worth knowing for any extremal-combinatorics argument where one needs to chain Chernoff bounds across "height" levels.

## Open questions / connections
- Can one recover the BCSV $n^{-c}$ tail without computer assistance? The bottleneck is concentration of $\sum_i e^{\alpha X_i}$; a different potential is likely needed.
- The weighted-case proof has a "hole" for $m \in [n, n\log n)$ since majorization fails — open whether the $O(\log\log n)$ bound holds there.
- Stationary-distribution interpretation: $X^t$ has a stationary law and all bounds hold for it; an alternative to mixing-time arguments for similar Markov chains.

## Key terms
balls-into-bins, two-choice process, Greedy[d], power of two choices, balanced allocations, layered induction, exponential potential function, Schur-convex, Markov chain stationary distribution, majorization, Vöcking Left[d], Azar–Broder–Karlin–Upfal, Berenbrink–Czumaj–Steger–Vöcking, Chernoff bound, heavily loaded case
