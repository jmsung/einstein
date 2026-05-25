---
type: source
kind: paper
title: Improved Lower Bounds for Kissing Numbers in Dimensions 25 through 31
authors: K. Kallal, Tomoka Kan, Eric Wang
year: 2016
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1608.07270
source_local: ../raw/2016-kallal-improved-lower-bounds-kissing.pdf
topic: general-knowledge
cites:
---

# Improved Lower Bounds for Kissing Numbers in Dimensions 25 through 31

**Authors:** K. Kallal, Tomoka Kan, Eric Wang  ·  **Year:** 2016  ·  **Source:** https://arxiv.org/abs/1608.07270

## One-line
Uses simulated annealing on Leech-lattice minimal vectors plus an improved probabilistic argument over $\mathrm{Co}_0$ to raise the best-known kissing-number lower bounds in dimensions 25–31.

## Key claim
A subset $S \subset C$ of the $196560$ Leech-lattice minimal vectors with pairwise inner product $\le 1$ can be enlarged from $|S|=480$ (Cohn–Jiao–Kumar–Torquato 2011) to $|S|=488$, and 24 mutually disjoint such sets of size 488 can be constructed, yielding new records: $K(25)\ge 197048$, $K(26)\ge 198512$, $K(27)\ge 199976$, $K(28)\ge 204368$, $K(29)\ge 208272$, $K(30)\ge 219984$, $K(31)\ge 232874$.

## Method
Three pieces: (1) **Simulated annealing** with $\mathrm{energy}(S)=-|S|$, linear cooling, antipodal-pair moves, to enlarge $|S|$ beyond what greedy gives (~238 random, 480 [CJKT11], 488 here). (2) **Explicit disjoint-copy construction**: sample random $g\in\mathrm{Co}_0$ via [CLGM+95], apply to $S$, greedily delete overlaps with previously built $S_i$; yields 51 disjoint subsets, 24 of size 488. (3) **Improved probabilistic argument**: model $\mathrm{Co}_0$ as a regular graph $H$ where $g_i\sim g_j$ iff $g_iS\cap g_jS=\emptyset$; using antipodality (even intersection sizes) plus a regular-graph parity lemma, sharpen the [CJKT11] recursion $|S_i|\ge |S|(1-\sum_{j<i}|S_j|/|C|)$ by exploiting the gap between $E_k$ and $\lfloor E_k\rfloor_2$ (Algorithms 4.14/4.15).

## Result
With $|S|=488$ and explicit $S_i$'s, lower bounds improve over [CJKT11] by 8–2002 spheres across dimensions 25–31 (Table 2). The improved probabilistic argument alone (Algorithm 4.15) beats [CJKT11]'s probabilistic bound for dims 28–31 at $|S|=488$ and beats their final dim-30, 31 bounds even at $|S|=480$, but is still surpassed by the explicit construction. Construction is suboptimal: 24 disjoint copies at full size hints at deeper Leech structure.

## Why it matters here
Direct precedent for the **simulated-annealing-on-lattice-minimal-vectors** pattern used in Einstein Arena packing/kissing problems (P2/P11/P19 family) — energy = $-|S|$, antipodal-pair moves, linear cooling. Also a template for **probabilistic constructions via automorphism groups + regular-graph arguments**, relevant to any problem where a large symmetry group acts on the configuration space.

## Open questions / connections
- Is there a 25th (or 51st) disjoint copy of size 488? — the existence of 24 hints at unexploited $\mathrm{Co}_0$ structure.
- Optimal $|S|$ unknown — should be antipodal with deeper symmetries; backtracking or longer SA may push past 488.
- Recasting as max-independent-set / max-clique on a symmetric Cayley-like graph and using SDP / Lovász $\vartheta$ bounds.
- Bounds $K(n)$ for $n\le 24$ in Table 1 are the [CS99] / [CJKT11] benchmark for Arena-style comparisons.

## Key terms
kissing number, Leech lattice $\Lambda_{24}$, minimal vectors, Conway group $\mathrm{Co}_0$, simulated annealing, antipodal sets, greedy construction, probabilistic method, regular graph, automorphism group, Cohn–Jiao–Kumar–Torquato, spherical codes, dimensions 25–31, disjoint-subsets construction
