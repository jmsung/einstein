---
type: source
kind: paper
title: Approximating CSPs with global cardinality constraints using SDP hierarchies
authors: P. Raghavendra, Ning Tan
year: 2011
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1110.1064
source_local: ../raw/2011-raghavendra-approximating-csps-global-cardinality.pdf
topic: general-knowledge
cites:
---

# Approximating CSPs with global cardinality constraints using SDP hierarchies

**Authors:** P. Raghavendra, Ning Tan  ·  **Year:** 2011  ·  **Source:** https://arxiv.org/abs/1110.1064

## One-line
A general SDP-hierarchy framework for approximating CSPs with a global cardinality constraint (Max Bisection, Min Bisection, Balanced Separator) by conditioning Lasserre solutions until variables become globally "uncorrelated."

## Key claim
Using $O(\mathrm{poly}(1/\delta))$ rounds of the Lasserre hierarchy, Max Bisection admits an $(0.85-\delta)$-approximation and, on instances with a $(1-\varepsilon)$-bisection, a $1 - O(\sqrt{\varepsilon}) - \delta$ bisection — near-optimal under UGC (matching Max Cut's $\sqrt{\varepsilon}$ lower bound up to constants). Same algorithm gives $0.92$ for balanced Max 2-SAT and $O(\sqrt{\varepsilon}) + \delta$ for Min Bisection / $\alpha$-Balanced Separator on $\varepsilon$-cut instances.

## Method
Lasserre SDP solutions admit consistent local marginal distributions $\mu_S$ on subsets $|S| \le k$ and allow conditioning on partial assignments. They define $\alpha$**-independence**: $\mathbb{E}_{i,j \sim W}[I_{\mu_{\{i,j\}}}(X_i;X_j)] \le \alpha$ (average pairwise mutual information). Starting from a $(k+\ell)$-round solution, repeatedly sample a random vertex and condition on its value — each conditioning drops $\sum_j H(X_j)$ by $\ge \alpha$ in expectation, so within $1/\alpha$ steps the residual $\ell$-round solution is $\alpha$-independent. Then a halfspace-style rounding gives a cut whose balance variance is $\mathrm{poly}(\alpha)$ (via Pinsker: $\mathrm{Cov}(X,Y) \le O(\sqrt{I(X;Y)})$), so the cut is concentrated near bisection.

## Result
Theorem 1.1: $O(n^{\mathrm{poly}(1/\delta)})$-time algorithm achieves $0.85 - \delta$ approximation for Max Bisection (previous best $0.7027$ [FL06]; UG hardness $0.878$). Theorem 1.2: same machinery handles Min Bisection / $\alpha$-Balanced Separator with $O(\sqrt{\varepsilon}) + \delta$ from $\varepsilon$-bisection. Theorem 1.3: generic conversion of Lasserre integrality gap instances into dictatorship tests with completeness $c - O(\varepsilon+\delta)$ and soundness $s + O(\varepsilon+\delta)$, extending the [Rag08] framework to globally constrained CSPs.

## Why it matters here
General background; no direct arena tie. The **global-correlation conditioning trick** (decorrelate Lasserre by conditioning on $\sim 1/\alpha$ random variables) is a transferable optimization-theoretic technique potentially relevant to LP/SDP hierarchies appearing in sphere-packing (Cohn-Elkies-style) and Sidon-set / extremal-graph problems where SOS/Lasserre tightenings are considered.

## Open questions / connections
- Concurrent / closely related work: Barak-Raghavendra-Steurer [BRS11] (covariance-based version, low-threshold-rank 2-CSPs) and Guruswami-Sinop [GS11] (quadratic IPs with PSD + linear constraints).
- The dictatorship test does **not** yet yield UG-based hardness for Max Bisection / Balanced Separator — needs the stronger Small Set Expansion hypothesis [RS10].
- Can the $\alpha$-independence machinery improve approximations for other globally constrained problems (Densest-$k$-Subgraph, kissing-style packing relaxations)?

## Key terms
Lasserre hierarchy, SDP hierarchies, Max Bisection, Min Bisection, Balanced Separator, global cardinality constraint, CSP approximation, dictatorship test, Unique Games Conjecture, mutual information conditioning, global correlation rounding, Goemans-Williamson, Raghavendra, integrality gap
