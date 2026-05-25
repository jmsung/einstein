---
type: source
kind: paper
title: Algorithms to Approximate Column-sparse Packing Problems
authors: Brian Brubach, Karthik Abinav Sankararaman, A. Srinivasan, Pan Xu
year: 2017
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1711.02724
source_local: ../raw/2017-brubach-algorithms-approximate-column-sparse-packing.pdf
topic: general-knowledge
cites:
---

# Algorithms to Approximate Column-sparse Packing Problems

**Authors:** Brian Brubach, Karthik Abinav Sankararaman, A. Srinivasan, Pan Xu  ·  **Year:** 2017  ·  **Source:** https://arxiv.org/abs/1711.02724

## One-line
Improved randomized-rounding approximation algorithms for $k$-column-sparse packing problems, attaining LP integrality gaps up to lower-order terms via two unifying ideas: non-uniform attenuation and multiple-chance rounding.

## Key claim
For $k$-column-sparse packing IPs ($k$-CS-PIP) the approximation ratio is improved from $ek + o(k)$ to $2k + o(k)$ (matching the strengthened-LP integrality gap of [Bansal et al. 2012]); for stochastic $k$-set packing (SKSP) from $2k$ to $k + o(k)$ (matching the natural-LP gap); and for hypergraph matching the bound is tightened from $k_e + 1$ to $k_e + O(k_e \exp(-k_e))$, "half the remaining distance" to the Füredi–Kahn–Seymour conjecture $k_e - 1 + 1/k_e$.

## Method
LP relaxation + randomized rounding with alterations, framed inside the contention-resolution-scheme (CR scheme) machinery of Chekuri–Vondrák–Zenklusen. Two new ingredients: (i) **non-uniform attenuation** — items are dropped with probability depending on $x_j$ rather than a single global factor $\alpha$, with the attenuation curve chosen by solving a small optimization; (ii) **multiple chances** — because one rounding pass uses only an $O(1/k)$ fraction of each budget in expectation, the algorithm reruns ALG on unselected items, "nibble"-style à la Ajtai–Komlós–Szemerédi / Rödl. Simulation-based attenuation (Monte Carlo estimation of conditional safety probabilities, then re-weighting) is used to equalize per-item inclusion probabilities. Chernoff–Hoeffding bounds under cylindrical negative correlation (Panconesi–Srinivasan) close the analysis.

## Result
Theorem 1: $2k + \Theta(k^{0.8}\,\mathrm{polylog}\,k)$ approximation for $k$-CS-PIP, asymptotically optimal vs. the strengthened LP ($2k-1$ integrality gap lower bound). Theorem 2: $k + o(k)$ for SKSP, asymptotically optimal vs. the natural LP. Theorem 3: a samplable matching distribution where each edge $e$ appears with probability $\geq x_e / (k_e + O(k_e e^{-k_e}))$. Theorem 4: improves the CR scheme for unit-demand UFP-TREES from $1/27$- to $1/8.15$-balanced, giving an $8.15/\eta_f$-approximation for non-negative submodular objectives.

## Why it matters here
General background; no direct arena tie. The non-uniform attenuation idea (optimize the attenuation curve rather than a scalar) and the multiple-chances/nibble template are reusable patterns for any combinatorial-optimization step the agent might encounter in discrete-geometry or extremal-graph problems, but no Einstein Arena problem in the current inventory is a column-sparse packing IP.

## Open questions / connections
- Fully resolve the Füredi–Kahn–Seymour conjecture (the remaining gap is $O(k_e e^{-k_e})$); authors suggest combining non-uniform attenuation + multiple-chances with the primal-dual machinery of [Füredi–Kahn–Seymour 1993].
- Find stronger LP relaxations for $k$-CS-PIP / SKSP that close the $2k$ vs. $k$ integrality-gap separation.
- Extend the same techniques to column-restricted packing programs (Kolliopoulos–Stein) and to general PIPs.
- Connects to the "nibble method" lineage (Ajtai–Komlós–Szemerédi, Rödl) and to negative-dependence rounding (Chekuri–Vondrák–Zenklusen, Peres–Singh–Vishnoi).

## Key terms
column-sparse packing, k-CS-PIP, stochastic k-set packing, hypergraph matching, Füredi-Kahn-Seymour conjecture, non-uniform attenuation, multiple-chance rounding, contention resolution scheme, randomized rounding with alterations, nibble method, integrality gap, submodular maximization, UFP-TREES, cylindrical negative correlation, Chernoff-Hoeffding
