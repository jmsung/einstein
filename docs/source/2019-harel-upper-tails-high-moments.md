---
type: source
kind: paper
title: Upper tails via high moments and entropic stability
authors: Matan Harel, Frank Mousset, Wojciech Samotij
year: 2019
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/1904.08212v2
source_local: ../raw/2019-harel-upper-tails-high-moments.pdf
topic: general-knowledge
cites: 
---

# Upper tails via high moments and entropic stability

**Authors:** Matan Harel, Frank Mousset, Wojciech Samotij  ·  **Year:** 2019  ·  **Source:** http://arxiv.org/abs/1904.08212v2

## One-line
Solves the long-standing upper-tail large-deviation problem for $k$-AP counts in random subsets of $[N]$ and for clique counts in $G_{n,p}$ by reducing the log-probability to a combinatorial "core" optimisation problem under an entropic-stability condition.

## Key claim
For bounded-degree polynomials $X(Y)$ with nonnegative coefficients on the $p$-biased hypercube, $-\log P(X \geq (1+\delta)\mathbb{E}[X]) = (1+o(1))\,\Phi_X(\delta)$ whenever the associated extremal problem $\Phi_X(\delta) = \min\{|I|\log(1/p) : \mathbb{E}[X \mid Y_I=1] \geq (1+\delta)\mathbb{E}[X]\}$ is *entropically stable* — i.e., the number of near-minimising "cores" of size $m$ is $(1/p)^{o(m)}$.

## Method
Adapts the Janson–Oleszkiewicz–Ruciński high-moment argument: bound $\mathbb{E}[X^t]$ for $t \asymp \Phi_X(\delta)/\log(1/p)$ via cluster expansions, then show the dominant contribution comes from "cores" (rigid feasible sets $I$ with $|I|=O(\Phi_X(\delta))$ where every element contributes appreciably). A union bound over cores closes the loop when entropic stability holds. For Poisson regimes a separate factorial-moment computation is used.

## Result
For $k$-AP counts $X^{k\text{-AP}}_{N,p}$ with $k\geq 3$: $\lim -\log P(X \geq (1+\delta)\mathbb{E}[X])/(Np^{k/2}\log(1/p)) = \sqrt{\delta}$ for $N^{-1}\log N \ll p^{k/2} \ll 1$ (Thm 1.3); Poisson-rate $(1+\delta)\log(1+\delta)-\delta$ for $N^{-1} \ll p^{k/2} \ll N^{-1}\log N$ (Thm 1.4). For $r$-clique counts in $G_{n,p}$, $r\geq 3$: explicit formula in terms of $\min(\delta^{2/r}/2, \delta/r)$ — clique-planting vs. hub construction — covering $n^{-1}(\log n)^{1/(r-2)} \ll p^{(r-1)/2} \ll 1$ (Thm 1.7). Plus structural description of $G_{n,p}\mid\{X\geq (1+\delta)\mathbb{E}[X]\}$ as either a planted near-clique or a hub (Thm 1.8). General $\Delta$-regular nonbipartite $H$: matching bound with $\theta$ from independence polynomial $P_H(\theta)=1+\delta$ (Thm 1.5).

## Why it matters here
General background — extremal/combinatorial-probability methodology. The "entropic stability ⇒ tail = $\Phi_X(\delta)$" framework is a template for any extremal problem where rare structures dominate a counting tail; relevant analogue for $B_h$/Sidon-set counting and arithmetic-additive problems on the arena. The Lubetzky–Zhao independence-polynomial variational principle it invokes also appears in extremal graph theory adjacent to arena combinatorial problems. No direct arena tie.

## Open questions / connections
- Nonregular and bipartite $H$ — Theorem 1.5 leaves the bipartite case open below $p^{\Delta/2}=n^{-1/2-o(1)}$; entropic stability fails there.
- Phase transition between Poisson and localised regimes when $p \asymp p^*$ — conjectured mixed behaviour (eq. 68).
- Structural characterisation of near-maximisers of $k$-AP counts in subsets of given size (extending Green–Sisask $k=3$).
- Moderate-deviation regime $\delta \to 0$ — pursued in follow-up [40].
- Decomposing the upper-tail measure into a mixture of product measures (Eldan–Gross, Austin).

## Key terms
upper tail large deviations, entropic stability, nonlinear large deviations, arithmetic progressions, clique counts, $G_{n,p}$, independence polynomial, Janson–Oleszkiewicz–Ruciński, Chatterjee–Dembo, Lubetzky–Zhao, hub construction, planted clique, high-moment method
