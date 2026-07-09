---
type: source
kind: paper
title: Upper tails and independence polynomials in random graphs
authors: B. Bhattacharya, S. Ganguly, E. Lubetzky, Yufei Zhao
year: 2015
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1507.04074
source_local: ../raw/2015-bhattacharya-upper-tails-independence-polynomials.pdf
topic: general-knowledge
cites:
---

# Upper tails and independence polynomials in random graphs

**Authors:** B. Bhattacharya, S. Ganguly, E. Lubetzky, Yufei Zhao  ·  **Year:** 2015  ·  **Source:** https://arxiv.org/abs/1507.04074

## One-line
Determines the precise leading-order constant of the upper-tail large-deviation rate function for $H$-subgraph counts in sparse Erdős–Rényi $G_{n,p}$, showing it is governed by the independence polynomial of $H$.

## Key claim
For any fixed connected graph $H$ with max degree $\Delta\ge 2$ and $n^{-\alpha_H}\le p=o(1)$, $-\log\mathbb{P}(X_H \ge (1+\delta)\mathbb{E}X_H) \sim c_H(\delta)\, n^2 p^\Delta \log(1/p)$, where $c_H(\delta)=\min(\theta,\tfrac{1}{2}\delta^{2/|V(H)|})$ if $H$ regular and $c_H(\delta)=\theta$ if irregular, with $\theta$ the unique positive root of $P_{H^*}(\theta)=1+\delta$ ($P_{H^*}$ the independence polynomial of the subgraph induced on max-degree vertices).

## Method
Reduces (via Chatterjee–Dembo's nonlinear large deviations) to a graphon variational problem $\inf \tfrac{1}{2}\mathbb{E}[I_p(W)]$ subject to $t(H,W)\ge(1+\delta)p^{|E(H)|}$. Solves it by an adaptively chosen degree threshold $b(p)$ splitting $[0,1]$ into high/low-degree sets $B_b,\bar B_b$, then applying the generalized Hölder (Brascamp–Lieb) inequality with non-uniform weights tied to fractional matching numbers; König's edge-coloring + 2-matching constructions reduce general $H$ to paths/cycles.

## Result
Two extremal constructions (planted clique of size $\sim\delta^{1/|V(H)|}p^{\Delta/2}n$, planted anti-clique/star of size $\sim\theta p^\Delta n$) are shown to be asymptotically optimal; a phase transition in $\delta$ at $\delta_0(H)$ separates the two regimes (e.g., $\delta_0(K_3)=27/8$, $\delta_0(C_{2k})=2k$). Worked formulas given for $C_k$ (via Chebyshev-like recursion $P_{C_k}=P_{C_{k-1}}+xP_{C_{k-2}}$), complete binary trees, and complete bipartite $K_{k,\ell}$ (e.g., $\phi(K_{k,\ell})/n^2 p^k\log(1/p)\to (1+\delta)^{1/\ell}-1$ for $k>\ell$). Disconnected $H$ yields a 2-variable mixture optimum.

## Why it matters here
General background; no direct arena tie. Independence-polynomial-as-rate-function and the "fractional matching / generalized Hölder" toolkit could inform extremal-graph / autocorrelation problems where subgraph-density tail bounds appear, but not directly used in current Einstein problems.

## Open questions / connections
- Sharp $\alpha_H$ — what is the true lower threshold of $p$ for the variational reduction (later improved by Eldan 2016 to $p\ge n^{-1/(6|E(H)|)}\log n$)?
- Formalizing "localization": characterizing the conditional measure as "close to" a planted clique/anti-clique in a sparse-graph metric (no analog of cut-metric known here).
- Extension to hypergraphs and to non-homomorphism-density functionals.

## Key terms
upper tail large deviations, Erdős–Rényi random graph, independence polynomial, graphon variational problem, generalized Hölder inequality, Brascamp–Lieb, fractional matching number, König's edge-coloring, planted clique, planted anti-clique, subgraph counts, Chatterjee–Dembo nonlinear large deviations
