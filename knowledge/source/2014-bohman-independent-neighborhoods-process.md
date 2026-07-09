---
type: source
kind: paper
title: The independent neighborhoods process
authors: T. Bohman, D. Mubayi, Michael E. Picollelli
year: 2014
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1407.7192
source_local: ../raw/2014-bohman-independent-neighborhoods-process.pdf
topic: general-knowledge
cites:
---

# The independent neighborhoods process

**Authors:** T. Bohman, D. Mubayi, Michael E. Picollelli  ·  **Year:** 2014  ·  **Source:** https://arxiv.org/abs/1407.7192

## One-line
Analyzes a random greedy hypergraph process that builds a maximal $T(r)$-free $r$-uniform hypergraph and bounds its independence number, pinning down the Ramsey number $r(T(r), K_s^{(r)})$ up to constants.

## Key claim
For fixed $r \geq 3$, the $T(r)$-free process on $n$ points produces an $r$-graph with independence number $O((n \log n)^{1/r})$ w.h.p., which combined with the matching upper bound of Kostochka–Mubayi–Verstraëte gives $r(T(r), K_s^{(r)}) = \Theta(s^r / \log s)$.

## Method
Random greedy hypergraph independent-set process applied to the auxiliary $(r+1)$-uniform hypergraph $H_{T(r)}$ whose edges are copies of $T(r)$, analyzed via the differential equations method (Wormald). Tracks two key trajectories $q(t) = \exp(-t^r)$ (open-set density) and $c(t) = rt^{r-1}q(t)$ (closure rate), using supermartingale concentration with error function $f(t) = \exp(W(t^r + t))$. The independence-number bound uses a two-step argument: dynamic concentration of open $r$-sets *with respect to* disjoint $\ell$-set pairs $(A,B)$, plus a deterministic combinatorial argument that every $k$-set contains a "good" pair avoiding high-degree $(r-1)$-set neighborhoods.

## Result
Theorem 1: independence number of $G^{(M)}$ from the $T(r)$-free process is $O((n \log n)^{1/r})$ w.h.p., where $k = \kappa(n \log n)^{1/r}$ with constants $\kappa \gg 1/\zeta \gg W \gg 1/\varepsilon \gg 1/\gamma \gg r$. Corollary 2: $c_1 \cdot s^r/\log s < r(T(r), K_s^{(r)}) < c_2 \cdot s^r/\log s$ for fixed $r \geq 3$. Process is tracked up to $i_{\max} = \zeta \cdot N D^{-1/r} (\log N)^{1/r}$ steps where $N = \binom{n}{r}$, $D = (r+1)\binom{n-r}{r-1}$.

## Why it matters here
General background; no direct arena tie. The DE-method / supermartingale-with-error-function machinery is the same toolkit used in extremal combinatorics for random greedy processes, and the "two-step argument" (pseudorandom concentration + structural surgery on bad sets) is a general template — potentially relevant if any arena problem reduces to a random greedy construction or hypergraph independence bound, but no current problem in the wiki uses this directly.

## Open questions / connections
- Extends Ajtai–Komlós–Szemerédi (1980) and Kim (1995) on $r(K_3, K_s) = \Theta(s^2/\log s)$ to all uniformities $r \geq 3$.
- The "loose triangle" Ramsey problem $r(C_3^{(3)}, K_s^{(3)})$ remains open between $\Omega(s^{3/2}/(\log s)^{3/4})$ and $O(s^{3/2})$ (Kostochka–Mubayi–Verstraëte conjecture: $o(s^{3/2})$).
- Tight-path Ramsey $r(P_3^{(3)}, K_s^{(3)})$ growth rate still open (Cooper–Mubayi resolved $t \geq 4$).
- Builds directly on Bennett–Bohman (arXiv:1308.3732) random greedy independent set framework.

## Key terms
random greedy process, triangle-free process, hypergraph Ramsey number, independence number, differential equations method, dynamic concentration, supermartingale, Ajtai-Komlós-Szemerédi, Kim, Bohman, T(r)-free hypergraph, semi-random nibble method
