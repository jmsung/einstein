---
type: source
kind: paper
title: The Power of Two Choices in Graphical Allocation
authors: Nikhil Bansal, Ohad Feldheim
year: 2021
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/2106.06051v2
source_local: ../raw/2021-bansal-power-two-choices-graphical.pdf
topic: general-knowledge
cites: 
---

# The Power of Two Choices in Graphical Allocation

**Authors:** Nikhil Bansal, Ohad Feldheim  ·  **Year:** 2021  ·  **Source:** http://arxiv.org/abs/2106.06051v2

## One-line
A non-greedy allocation strategy for the graphical balls-into-bins process that achieves polylogarithmic load gap on any well-connected graph, matching the lower bound up to polylog factors.

## Key claim
For any $k$-edge-connected, $d$-regular graph $G$ on $n$ vertices, there is an allocation strategy guaranteeing $\mathrm{gap}_G(t) = O((d/k)\log^4 n \log\log n)$ w.h.p. at every time $t$; this is tight up to polylog factors since every strategy has gap $\Omega(d/k + \log n)$.

## Method
Hierarchical Räcke cut-based decomposition tree of $G$, converted to a binary tree $T$. For each internal node $i$ with children $\ell(i), r(i)$, define an *orthogonal* balancing drift (Haar-basis on $T$) of magnitude $\beta k$ between the sibling sets, realized as a multicommodity flow via Räcke flow templates with congestion ratio $\alpha_G = O(\log^2 n \log\log n)$. Edge biases $p_e(i), \sigma_e(i)$ are precomputed; online allocation samples one node $i$ per requested edge and compares average loads on $S_{\ell(i)}$ vs $S_{r(i)}$. Concentration via a 2-point potential argument with $\Phi(t) = \cosh(\alpha \delta(t))$.

## Result
- **Upper bound (Thm 1.1):** $\mathrm{gap}_G(t) = O((d/k) \alpha_G \log^2 n) = O((d/k)\log^4 n \log\log n)$ w.h.p., for any $t$.
- **Lower bound (Thm 1.2):** $\mathrm{gap}_G(t) = \Omega(d/k + \log n)$ with constant probability, for any strategy.
- Implies $\mathrm{polylog}(n)$ gap for cycles, tori, and bounded-degree connected graphs — vs. conjectured $\Theta(\sqrt{n})$ for greedy on cycles.
- Implementation: $O(\log n)$ time per allocation (amortized $O(1)$), $O(m\log n)$ space, $O(1)$ amortized messages in distributed setting.

## Why it matters here
General background; no direct arena tie. The orthogonal-Haar-decomposition + Räcke-flow technique is a clean instance of using hierarchical multicommodity flow to control deviations on *sets* rather than singletons — a structural template that could inform load-balancing intuition in discrete-geometry packings or large-scale parallel optimizer scheduling, but does not bear on any of the 23 Einstein Arena problems directly.

## Open questions / connections
- Closing the polylog gap between $O((d/k)\log^4 n \log\log n)$ upper and $\Omega(d/k + \log n)$ lower bound.
- Does greedy on cycles converge (scaled) to Brownian motion, and on grids to a Gaussian free field (Peres conjecture)?
- Extending beyond regular graphs / 2-choice to $(1+\beta)$ choice or asymmetric (Vöcking) choice on graphs.

## Key terms
balls-into-bins, two-choice load balancing, graphical allocation, Räcke decomposition tree, oblivious routing, multicommodity flow, edge expansion, edge connectivity, Haar basis orthogonal drift, potential function method, congestion ratio, Peres-Talwar-Wieder
