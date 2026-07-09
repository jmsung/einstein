---
type: source
kind: paper
title: Percolation on random graphs with a fixed degree sequence
authors: Nikolaos Fountoulakis, Felix Joos, Guillem Perarnau
year: 2016
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/1611.08496v2
source_local: ../raw/2016-fountoulakis-percolation-random-graphs-fixed.pdf
topic: general-knowledge
cites: 
---

# Percolation on random graphs with a fixed degree sequence

**Authors:** Nikolaos Fountoulakis, Felix Joos, Guillem Perarnau  ·  **Year:** 2016  ·  **Source:** http://arxiv.org/abs/1611.08496v2

## One-line
Characterises which sparse degree sequences $D$ admit a strictly positive bond-percolation threshold $p_{\text{crit}}$ for a giant component in the uniform simple-graph model $G_D$, with no second-moment or maximum-degree restrictions.

## Key claim
A dichotomy holds: if $D$ is strongly uniformly integrable and $d(D) := \sup_{c \ge 1} \lim_n \max(\sum_{i \notin W_n(c)} d_i(d_i-1) / \sum_{i \notin W_n(c)} d_i,\, 1) < \infty$, then $p_{\text{crit}} = 1/d(D)$ is a sharp threshold for a linear-order component; if $d(D)=\infty$ or strong uniform integrability robustly fails, then for every $p \in (0,1)$ a giant component exists with probability $\ge 1-\delta$.

## Method
Switching method applied directly to the uniform simple-graph model $G_D$, avoiding the configuration model and its usual second-moment/max-degree assumptions. Components are revealed by a sequential exploration process in which high-degree vertices and their neighbourhoods are placed in the initial explored set, and conditions $A_1(x,c)$ (tail-degree-sum bound $\sum_{i \in W(c)} d_i \le xn/c$) and $A_2(x,c_1,c_2)$ (bounded $\sum d_i^2$ on a moderate-degree window) control sub-/super-criticality. Concentration via Chernoff and McDiarmid; double-counting of valid switches yields $\mathbb{P}[\mathcal{F}] = (d(\mathcal{F}' \to \mathcal{F})/d(\mathcal{F} \to \mathcal{F}'))\, \mathbb{P}[\mathcal{F}']$.

## Result
Theorem 1: for sparse $D_n$ with average degree $\le \bar d$ and $d(D)$ existing, $p_{\text{crit}} = 1/d(D)$ when $D$ is strongly uniformly integrable and $d(D)<\infty$; otherwise the giant component appears for any $p>0$. Theorems 2 and 3 give the stronger non-asymptotic versions in terms of $A_1$, $A_2$. For power-law sequences with $n_k/n \asymp k^{-\gamma}$: $\gamma > 3 \Rightarrow p_{\text{crit}} > 0$; $2 < \gamma < 3 \Rightarrow p_{\text{crit}} = 0$; $\gamma = 3$ uninformative. Theorem 2 also detects "secondary jumps" in $L_1(G_D^p)$ above an existing giant (Example 3: $D_n=(\xi n,3,\dots,3)$ has $p_{\text{crit}}=0$ but a Theorem-2 boost at $p=1/2$).

## Why it matters here
General background; no direct arena tie — this is extremal random-graph / percolation theory rather than sphere packing, kissing, autocorrelation, or SDP-bound work. Closest in-scope contact is the extremal-graph cluster (giant-component thresholds, Molloy–Reed criterion) and the switching method as a combinatorial tool that could conceivably surface in graph-flag / regularity-style arguments.

## Open questions / connections
- The "secondary jump" at $p > 0$ for non-uniformly-integrable sequences (Example 3) is not characterised — what is the limiting size of $L_1$ around this second critical point?
- Behaviour at the boundary exponent $\gamma = 3$ for power-law sequences is left open.
- Extends Molloy–Reed (1995), Fountoulakis (2007), Janson (2009), Bollobás–Riordan (2015), Joos–Perarnau–Rautenbach–Reed (2018) by removing configuration-model technical assumptions.
- Counterexample (Section 12, remark 1) shows Theorem 3's $1-\delta$ probability cannot be upgraded to $1-o(1)$.

## Key terms
bond percolation, configuration model, switching method, giant component, degree sequence, Molloy–Reed criterion, uniform integrability, power-law degree distribution, sparse random graphs, Galton-Watson survival probability, critical threshold, extremal graph theory
