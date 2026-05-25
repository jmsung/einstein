---
type: source
kind: paper
title: Critical percolation on random regular graphs
authors: Felix Joos, G. Perarnau
year: 2017
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1703.03639
source_local: ../raw/2017-joos-critical-percolation-random-regular.pdf
topic: general-knowledge
cites:
---

# Critical percolation on random regular graphs

**Authors:** Felix Joos, G. Perarnau  ·  **Year:** 2017  ·  **Source:** https://arxiv.org/abs/1703.03639

## One-line
Proves that for every degree $d \in \{3,\dots,n-1\}$, the largest component of a random $d$-regular graph at the percolation threshold $p = 1/(d-1)$ has order $\Theta(n^{2/3})$ with high probability.

## Key claim
For $p = (1+\lambda n^{-1/3})/(d-1)$ with $\lambda \in \mathbb{R}$ and sufficiently large $A=A(\lambda)$: $\mathbb{P}[L_1(G_{n,d,p}) \notin [A^{-1} n^{2/3}, A n^{2/3}]] \le 20 A^{-1/2}$. This confirms mean-field behaviour across the full critical window of width $\Theta(n^{-1/3})$ for all $d$, settling Benjamini's question and Nachmias–Peres's prediction.

## Method
Switching method (McKay) applied to an exploration process on inputs $(G,S)$ where $S$ is a uniform collection of $n$ permutations of length $d$ encoding semi-edge labels. Two switching lemmas bound conditional adjacency probabilities and conditional degree expectations $\mathbb{E}[d_{G,S}(v)] \le 6d|S|/n$. Track $X_t$ = unexposed edges between explored set $S_t$ and its complement; sharp first and second moment estimates of $\eta_{t+1} = X_{t+1}-X_t$ feed Optional Stopping (sub/super-martingale) arguments in two phases.

## Result
Lower bound on $L_1$: with probability $\ge 1 - 19 A^{-1/2}$, there is a component of size $\ge A^{-1} n^{2/3}$. Two-phase analysis: phase 1 shows $X_t$ exceeds $h = A^{-1/4} d n^{1/3}$ within $T_1 = 5dn^{2/3}/6$ steps; phase 2 shows $X_t$ stays positive for $T_2 = 2A^{-1} d n^{2/3}$ further steps. Corollary: largest component has $\mathrm{diam}(C) = \Theta(n^{1/3})$ and lazy random walk mixing time $T_{\mathrm{mix}}(C) = \Theta(n)$ w.h.p.

## Why it matters here
General background; no direct arena tie. Critical-window mean-field universality and the switching method are tools for extremal combinatorics on random regular graphs, potentially relevant if a future arena problem touches extremal graph theory on regular hosts, but not aligned with the current 23-problem inventory (sphere packing / autocorrelation / kissing / Sidon).

## Open questions / connections
- Extends Nachmias–Peres (2010) and Pittel (2008) from fixed $d$ to all $d \in \{3,\dots,n-1\}$; complements Erdős–Rényi $G_{n,p}$ critical-window results.
- Authors conjecture analogous sharp estimates hold in barely subcritical / supercritical regimes for all $d$, extending Nachmias–Peres.
- Switching-method exploration framework may generalise to other random-graph models with given degree sequence (cf. Fountoulakis–Joos–Perarnau 2016, Joos–Perarnau–Rautenbach–Reed 2017).

## Key terms
critical percolation, random regular graph, configuration model, switching method, McKay, exploration process, mean-field critical window, giant component, Erdős–Rényi, Nachmias–Peres, Benjamini, martingale optional stopping, mixing time, diameter, $n^{2/3}$ scaling
