---
type: source
kind: paper
title: Some remarks on hypergraph matching and the Füredi-Kahn-Seymour conjecture
authors: Nikhil Bansal, David G. Harris
year: 2020
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/2011.07097v3
source_local: ../raw/2020-bansal-some-remarks-hypergraph-matching.pdf
topic: author-sweep
cites: 
---

# Some remarks on hypergraph matching and the Füredi-Kahn-Seymour conjecture

**Authors:** Nikhil Bansal, David G. Harris  ·  **Year:** 2020  ·  **Source:** http://arxiv.org/abs/2011.07097v3

## One-line
Improved bounds on the integrality gap between integer and fractional hypergraph matchings, proving the Füredi–Kahn–Seymour conjecture for rank-3 hypergraphs via an iterated rounding algorithm.

## Key claim
For rank-3 hypergraphs, $\sum_{e\in M}(|e|-1+1/|e|)w(e) \geq w^*$ holds (FKS conjecture). In general rank, the iterated rounding algorithm achieves $\sum_{e\in M}(|e|-\delta(e))w(e) \geq w^*$ with $\delta(e) = |e|/(|e|^2+|e|-1)$, strictly improving the baseline $\sum_{e\in M}|e|w(e) \geq w^*$.

## Method
Extends Chan–Lau iterative ("local-ratio") rounding to allow per-edge discount factors $g(e)$. Defines $g$ as "good for $H$" if no subgraph has a basic fractional matching that is "stuck" (i.e., satisfies $\sum_{f\in N(e)} g(f)x(f) > 1 - g(e)x(e)$ for every $e$). Reaches contradictions by combining stuck-inequalities with basic-LP-solution bounds $|L|\leq |B(L)|$ on tight vertices, refined by bi-uniform self-interaction tracking.

## Result
Theorem 2.5: FKS holds for rank 3 (via $p=h^*(2)=2/3$, $q=h^*(3)=3/7$, integer-$n$ case check up to $T=4.2$). Theorem 2.6: any $h:\mathbb{N}\to\mathbb{R}$ with (A1) monotone, (A2) $\leq 1/(k-1+1/k)$, (A3) $h(k+1)\leq 1-(k-1)h(k)$ yields a good discount. Corollary 2.7 gives explicit choices $h_r(k)$, $h_\infty(k) = (-1)^k(D_{k-2} - (k-2)!/e)$, and $\tilde h_\infty(k) = 1/(k - k/(k^2+k-1))$, all of form $k^{-1}+k^{-3}-O(k^{-4})$ vs. the FKS target $k^{-1}+k^{-2}-O(k^{-4})$.

## Why it matters here
Hypergraph matching LP rounding is the standard framework for extremal/packing problems and approximation algorithms (Sidon sets, set packing, kissing/packing bounds via combinatorial relaxations). The technique — derive contradictions from "stuck" basic-LP solutions using $|L|\leq|B(L)|$ — is a reusable LP-extreme-point trick relevant to LP-relaxation-based attacks on discrete geometry problems.

## Open questions / connections
- FKS conjecture remains open for rank $\geq 4$; the closed-form $h^*(k) = 1/(k-1+1/k)$ target still has $k^{-2}$ gap to current $h_\infty$.
- Extends Chan–Lau [6] (uniform case) and Anegg–Angelidakis–Zenklusen [1] (general non-uniform $|e|$ bound).
- Bi-uniform analysis suggests deeper integer-arithmetic structure ($n=n_k(f)$ integrality was critical for rank-3) — generalizing to multi-uniform may need finer counting.

## Key terms
hypergraph matching, Füredi-Kahn-Seymour conjecture, integrality gap, fractional matching polytope, iterated rounding, local ratio, basic LP solution, Caro-Wei theorem, line graph independent set, rank-3 hypergraph, bi-uniform hypergraph, discount factor, projective plane tightness, Bansal, Harris
