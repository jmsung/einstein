---
type: source
kind: paper
title: Spectral Gaps of Random Graphs and Applications
authors: C. Hoffman, M. Kahle, Elliot Paquette
year: 2012
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1201.0425
source_local: ../raw/2012-hoffman-spectral-gaps-random-graphs.pdf
topic: general-knowledge
cites:
---

# Spectral Gaps of Random Graphs and Applications

**Authors:** C. Hoffman, M. Kahle, Elliot Paquette  ·  **Year:** 2012  ·  **Source:** https://arxiv.org/abs/1201.0425

## One-line
Sharp spectral-gap bounds for the normalized Laplacian of Erdős–Rényi $G(n,p)$ near the connectivity threshold, with applications to random simplicial complexes and random groups.

## Key claim
For any fixed $\delta>0$, if $p \ge (\tfrac{1}{2}+\delta)\log n / n$ and $d=p(n-1)$, then the giant component $\tilde G$ of $G(n,p)$ satisfies $\lambda(\tilde G) = \max_{i\ne 1}|1-\lambda_i| < C/\sqrt{d}$ with failure probability $\le Cn\exp(-(2-\varepsilon)d) + C\exp(-d^{1/4}\log n)$. The constant $1/2$ is optimal: for $p \le \tfrac{1}{2}\log n/n$ (and $p=\omega(\sqrt{\log n}/n)$), $\lambda(\tilde G) \ge 1/2$ w.h.p.

## Method
Sharpened Kahn–Szemerédi machinery applied to the adjacency matrix $A$, then transferred to the normalized Laplacian $L = \pi_+ - T^{-1/2}AT^{-1/2}$ via a structural analysis of low-degree vertices. The key new structure theorem: near the connectivity threshold low-degree vertices share no edges or common neighbors, so they are linked only through a high-degree core, letting $T^{-1/2}$ nearly preserve the orthogonal-to-$\mathbf 1$ subspace. Light/heavy coupling decomposition + Bernstein inequality + discrepancy lemma on dyadic level sets controls $|x^t A y|$.

## Result
Proves $\lambda(\tilde G) = O(1/\sqrt{np})$ down to $p \ge (1/2+\delta)\log n/n$, extending Coja-Oghlan's $C\log n/n$ threshold to the optimal constant $1/2$. Establishes the sharp phase transition at $p = \tfrac{1}{2}\log n/n$ (where degree-2 path quadruplets in the giant component force eigenvalues near $1/2$ and $3/2$). Yields: at connection time $\tau_c$ of the $G(n,m)$ process, $\lambda(G(n,\tau_c)) \le C/\sqrt{\log n}$; a new short proof of Linial–Meshulam–Wallach cohomology-vanishing threshold $p=d\log n/n$ over $\mathbb Q$; and a structure theorem for $\pi_1(Y_2(n,p))$ as free product of a Kazhdan-(T) group and a free group on the isolated edges, for $p\ge (1+\delta)\log n/n$.

## Why it matters here
General background; no direct arena tie. Concept-adjacent to extremal graph theory and spectral methods (Kahn–Szemerédi, Cheeger, expander mixing) that might inform extremal-graph problems on the arena; the sharp-threshold-constant style of analysis is a template worth knowing.

## Open questions / connections
- Conjectured family of phase transitions at $p = \tfrac{1}{k}\log n/n$ where the giant-component gap matches that of a path on $k$ vertices.
- Does $\lambda_2(L) = 1 - (2-o(1))/\sqrt{np}$ exactly at $p\sim \log n/n$, mirroring the Wigner semicircle prediction (Knowles–Erdős–Yau–Yin)?
- Garland's method + this gap bound should sharpen Gundert–Wagner and Parzanchevski–Rosenthal–Tessler "geometric overlap" thresholds for random $d$-complexes; not yet written down.

## Key terms
Erdős–Rényi random graph, normalized Laplacian, spectral gap, connectivity threshold, Kahn–Szemerédi, Coja-Oghlan, Feige–Ofek, Garland's method, Linial–Meshulam–Wallach, Kazhdan property (T), random simplicial complex, expander, Cheeger constant, discrepancy inequality, Wigner semicircle
