---
type: source
kind: paper
title: Stability in the Erdős-Gallai Theorem on cycles and paths, II
authors: Z. Füredi, A. Kostochka, Ruth Luo, Jacques Verstraëte
year: 2017
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1704.02866
source_local: ../raw/2017-fredi-stability-erd-s-gallai-theorem.pdf
topic: general-knowledge
cites:
---

# Stability in the Erdős-Gallai Theorem on cycles and paths, II

**Authors:** Z. Füredi, A. Kostochka, Ruth Luo, Jacques Verstraëte  ·  **Year:** 2017  ·  **Source:** https://arxiv.org/abs/1704.02866

## One-line
Completes a stability theorem for 2-connected $n$-vertex graphs with no cycle of length $\geq k$, characterizing all near-extremal graphs by giving a second-order edge bound and an explicit list of exceptional families.

## Key claim
For $t \geq 4$, $k \in \{2t+1, 2t+2\}$, and any 2-connected $n$-vertex graph $G$ with $c(G) < k$: either $e(G) \leq \max\{h(n,k,t-1), h(n,k,3)\}$ where $h(n,k,a) = \binom{k-a}{2} + a(n-k+a)$, or $G$ is a subgraph of one of the explicit extremal/near-extremal graphs $H_{n,k,t}$, $H_{n,k,2}$, or a member of structured exceptional classes $\mathcal{G}_2, \mathcal{G}_3, \mathcal{G}_4$ (the last only for $k=10$).

## Method
Edge-contraction induction combined with Kopylov's disintegration ($\alpha$-core: iteratively remove vertices of degree $\leq \alpha$). Authors use a Modified Basic Procedure (MBP) that contracts edges minimizing triangle count $T_G(uv)$ while preserving 2-connectedness, reducing $G$ to a small graph $G_m$ amenable to analysis via Chvátal's hamiltonian condition and Kopylov's path-length theorem. A family $\mathcal{F}(k)$ of "dense witness subgraphs" (near-complete bipartite $K_{t,t+1}$ or $K_{t,t+2}$ with $\leq t-3$ edges removed) is preserved under contraction (Lemma 3.1) and forces the global structure.

## Result
The bound $\max\{h(n,k,t-1), h(n,k,3)\}$ is tight, and the exceptional families are completely classified: $\mathcal{G}_1 = \{H_{n,k,t}, H_{n,k,2}\}$ always; $\mathcal{G}_2, \mathcal{G}_3$ when $k$ is even; $\mathcal{G}_4$ only at $k=10$. Combined with the authors' 2016 paper (which handled $n \geq 3k/2$), this gives a full description for all $k \geq 9$ and $n \geq k$. A clean 3-connected corollary: only $H_{n,k,t}$ and a $k=10$ exception remain.

## Why it matters here
General background; no direct arena tie. Closest relevance is extremal/Turán-type combinatorics — could inform discrete combinatorics or extremal graph problems if any arena problem reduces to bounding edges under cycle-length constraints, but no current Einstein Arena problem in the wiki inventory uses Erdős-Gallai-style cycle extremality directly.

## Open questions / connections
- Extends Füredi-Kostochka-Verstraëte 2016 (JCTB 121, 197–228) which covered $n \geq 3k/2$; this paper closes the small-$n$ gap.
- Builds directly on Kopylov 1977 (extremal graphs) and Erdős-Gallai 1959 (original bound).
- The $k=10$ anomaly (class $\mathcal{G}_4$) is structurally isolated — suggests other low-$k$ sporadic exceptions may exist but are now ruled out for $k \geq 9, k \neq 10$.

## Key terms
Erdős-Gallai theorem, Kopylov, extremal graph theory, Turán-type problem, cycle length, 2-connected graphs, stability theorem, edge contraction, disintegration method, $\alpha$-core, Chvátal hamiltonian condition, path Ramsey
