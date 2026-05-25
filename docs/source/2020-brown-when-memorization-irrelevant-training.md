---
type: source
kind: paper
title: When is memorization of irrelevant training data necessary for high-accuracy learning?
authors: Gavin Brown, Mark Bun, V. Feldman, Adam M. Smith, Kunal Talwar
year: 2020
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2012.06421
source_local: ../raw/2020-brown-when-memorization-irrelevant-training.pdf
topic: general-knowledge
cites:
---

# When is memorization of irrelevant training data necessary for high-accuracy learning?

**Authors:** Gavin Brown, Mark Bun, V. Feldman, Adam M. Smith, Kunal Talwar  ·  **Year:** 2020  ·  **Source:** https://arxiv.org/abs/2012.06421

## One-line
Proves that for natural learning tasks, any near-optimal algorithm must encode $\Omega(nd)$ bits of information about its training sample — including information irrelevant to the prediction task — regardless of architecture.

## Key claim
For natural next-symbol prediction and hypercube cluster labeling tasks $q$ over $\{0,1\}^d$, any $\varepsilon$-suboptimal learner $A$ satisfies $I(X; M \mid P) = \Omega(nd)$, where $M = A(X)$ and $P \sim q$. For some tasks, a subset $X_S \subseteq X$ of expected size $\Omega(n)$ has $I(X_S; M \mid P) = (1-o(1)) H(X_S \mid P) = \Omega(nd)$ — i.e., near-complete memorization of singletons.

## Method
Reduction from learning to a one-way communication game called Singletons$(k, q_c)$, where Alice holds $k$ labeled examples from independent subpopulations and must send a single message letting Bob predict the label of a fresh example from a uniformly random one. Information-complexity lower bounds for this game (extending Bassily–Moran–Nachum–Shafer–Yehudayoff direct-sum techniques) transfer to learning via the structure of "singleton" examples — subpopulations represented exactly once in the sample. A new $(1-o(1)) \cdot d$ one-way information complexity lower bound for Gap-Hamming, via a general product-distribution technique, anchors the cluster-labeling result.

## Result
For next-symbol prediction and hypercube cluster labeling, $\varepsilon$-suboptimal learners must leak $\Omega(nd)$ bits, quantitatively stronger than prior $\Omega(n \log d)$ [Nachum–Shafer–Yehudayoff] or $\Omega(n \log \log d)$ [Livni–Moran] bounds, and applies to *any* sufficiently accurate learner, not just proper/consistent ones. Implies $(\alpha, \beta)$-differentially private algorithms with $\alpha = O(\log n)$, $\beta = o(1)$ cannot achieve near-optimal accuracy on these tasks. Empirical neural-network and logistic-regression attacks recover $>97\%$ of singleton-example bits.

## Why it matters here
General background; no direct arena tie. The information-complexity / direct-sum / Gap-Hamming machinery is mathematically adjacent to LP-bound and communication-complexity arguments occasionally invoked in extremal combinatorics, but the paper is about ML privacy and does not bear on sphere-packing, autocorrelation, or kissing-number problems.

## Open questions / connections
- Conjecture 4.1: does the "whole-sample memorization" bound $I(X_S; M \mid P) = (1-o(1)) H(X_S \mid P)$ hold for cluster labeling (would follow from a conjectured one-way info-complexity bound for multi-sample Gap-Hamming)?
- Can the independence-of-subpopulations assumption be relaxed to model real text/images while preserving the lower bound?
- Computationally efficient training-data recovery from black-box model access — when does information-theoretic memorization imply extractability?
- Extends/strengthens Bassily et al. [7], Nachum–Shafer–Yehudayoff [34], Livni–Moran [29] threshold-learning leakage bounds.

## Key terms
information complexity, mutual information lower bound, one-way communication complexity, Gap-Hamming, direct sum, singleton examples, subpopulation mixture, differential privacy, PAC learning, memorization, next-symbol prediction, hypercube cluster labeling, Berry-Esséen, threshold functions, long-tail distribution
