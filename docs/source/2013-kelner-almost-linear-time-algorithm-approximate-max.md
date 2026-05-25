---
type: source
kind: paper
title: An Almost-Linear-Time Algorithm for Approximate Max Flow in Undirected Graphs, and its Multicommodity Generalizations
authors: Jonathan A. Kelner, L. Orecchia, Y. Lee, Aaron Sidford
year: 2013
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1304.2338
source_local: ../raw/2013-kelner-almost-linear-time-algorithm-approximate-max.pdf
topic: general-knowledge
cites:
---

# An Almost-Linear-Time Algorithm for Approximate Max Flow in Undirected Graphs, and its Multicommodity Generalizations

**Authors:** Jonathan A. Kelner, L. Orecchia, Y. Lee, Aaron Sidford  ·  **Year:** 2013  ·  **Source:** https://arxiv.org/abs/1304.2338

## One-line
An almost-linear-time $O(m^{1+o(1)}\varepsilon^{-2})$ algorithm for $\varepsilon$-approximate maximum $s$-$t$ flow in undirected graphs, with a multicommodity generalization at $O(m^{1+o(1)}\varepsilon^{-2}k^2)$.

## Key claim
For undirected capacitated graphs with $n$ vertices and $m$ edges, $\varepsilon$-approximate max $s$-$t$ flow is computable in $O(m^{1+o(1)}\varepsilon^{-2})$ time (vs prior $O(mn^{1/3}\mathrm{poly}(1/\varepsilon))$), and $k$-commodity concurrent max flow in $O(m^{1+o(1)}\varepsilon^{-2}k^2)$ (vs prior $O(m^{4/3}\mathrm{poly}(k,\varepsilon^{-1}))$).

## Method
Non-Euclidean gradient descent in the $\ell_\infty$ norm (with a smoothed soft-max objective) reduces congestion minimization to repeated application of a linear circulation-projection matrix; the matrix is supplied by an oblivious routing scheme. The scheme is built recursively via two reductions: vertex elimination (embedding $G$ into partial-tree graphs reducible to almost-$j$-trees with $O(|E|/t)$ vertices via greedy degree-1/2 elimination) and flow sparsification (a new sparsifier $\tilde G$ that admits a low-congestion embedding back into $G$ via electrical flows, closing the flow/cut sparsifier gap). Total competitive ratio $2^{O(\sqrt{\log n \log\log n})}$.

## Result
Theorem: $\varepsilon$-approximate max flow in $O(m \cdot 2^{O(\sqrt{\log n \log\log n})}/\varepsilon^2)$ time; concurrent multicommodity flow in $O(|E| \cdot 2^{O(\sqrt{\log n \log\log n})} k^2/\varepsilon^2)$. Also gives the first almost-linear-time construction of an $O(m^{o(1)})$-competitive oblivious routing scheme (prior best $\Omega(mn)$), and a general gradient-descent convergence bound $f(x_k)-f^* \le 2LR^2/(k+4)$ for arbitrary norms with Lipschitz-gradient constant $L$.

## Why it matters here
General background; no direct arena tie. The non-Euclidean gradient descent framework (optimizing local linearization over the unit ball of an arbitrary norm rather than $\ell_2$) and the $\ell_2$-vs-$\ell_\infty$ $\sqrt{m}$-iteration barrier are conceptually relevant to any optimizer whose constraint geometry is non-spherical — potentially useful framing for problems where $\ell_\infty$-style worst-case constraints dominate (e.g. equioscillation, kissing-graph contact constraints).

## Open questions / connections
- Can the multicommodity $k^2$ dependence be improved to $k^{3/2}$ via Nesterov acceleration over the $\ell_1$ geometry? Authors conjecture yes; blocked by absence of a good regularizer for $\|\cdot\|_{1;\infty}$.
- No known accelerated method (Nesterov-style) for gradient descent in general norms beyond $\ell_p$, $p\le 2$ — open whether one exists.
- Sherman (independent, simultaneous, [27]) gives a dual approach via congestion-bound objects from Madry [19]; comparing the two frameworks is open.
- Extends Spielman–Teng sparsification recursion [30,32] from cuts to flows via embeddable sparsifiers.

## Key terms
maximum flow, multicommodity flow, oblivious routing, flow sparsifier, non-Euclidean gradient descent, electrical flow, Laplacian solver, almost-j-tree, soft-max smoothing, competitive ratio, circulation projection, Kelner, Orecchia, Sherman, Madry, Spielman-Teng
