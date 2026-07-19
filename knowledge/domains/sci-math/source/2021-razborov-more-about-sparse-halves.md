---
type: source
kind: paper
title: More about sparse halves in triangle-free graphs
authors: Alexander Razborov
year: 2021
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/2104.09406v2
source_local: ../raw/2021-razborov-more-about-sparse-halves.pdf
topic: general-knowledge
cites: 
---

# More about sparse halves in triangle-free graphs

**Authors:** Alexander Razborov  ·  **Year:** 2021  ·  **Source:** http://arxiv.org/abs/2104.09406v2

## One-line
Partial progress on Erdős's half-graph conjecture — every triangle-free graph on $n$ vertices should contain $n/2$ vertices inducing at most $n^2/50$ edges — via flag-algebra bounds on $C_4$ density and case analysis on independence/girth/regularity.

## Key claim
For any triangle-free graph $G$, $\beta(G) \le 27/1024$ (improving Krivelevich's $1/36$); and the half-graph conjecture $\beta(G) \le 1/50$ is fully proved for (i) graphs without induced $2$-matchings, (ii) girth $\ge 5$, (iii) independence number $\alpha(G) \ge 2/5$, and (iv) triangle-free strongly regular graphs.

## Method
Flag-algebra Cauchy–Schwarz SDPs (medium-size, on $8$- and $6$-vertex triangle-free graphs) establish the quadrilateral lower bound $C_4(G) \ge \tfrac{3}{2}\rho^2 - \tfrac{81}{256}\rho$ (tight at Clebsch, $\rho = 5/16$) and a sharper $\tfrac{3}{2}\rho^2 - \tfrac{6}{25}\rho$ for induced-$M_2$-free graphs (tight at $C_5$, $\rho=2/5$). These feed Krivelevich's edge-splitting construction (Prop. 1.1: $\beta(G) \le C_4/(12\rho) + \rho/8 - \rho(G)$). Remaining cases use ad-hoc half constructions, greedy expansion from an independent set, Ramsey numbers $R(3,u)$, and Maple-verified recursive case analysis.

## Result
- General bound: $\beta(G) \le 27/1024 \approx 0.0264$ (vs conjectured $1/50 = 0.02$).
- Conjecture fully proved for: girth $\ge 5$; $\alpha(G) \ge 2/5$ (more generally $\beta(G) \le \alpha(\tfrac12-\alpha)(\tfrac12-\alpha)$ when $\alpha \ge 3/8$); no induced $M_2$; $\rho(G) \le (33-\sqrt{161})/116 \approx 0.1751$; all triangle-free strongly regular graphs (Petersen, Clebsch, Hoffman–Singleton, Gewirtz, $M_{22}$, Higman–Sims, plus ruling out the hypothetical $57$-regular Krein graph).
- New extremal problem: minimum $C_4$ density given $\rho$ in triangle-free graphs — Clebsch is extremal at $\rho=5/16$.

## Why it matters here
Direct relevance to the **extremal-graph / Razborov flag-algebra** problem family in the arena; demonstrates how flag-algebra SDPs (Razborov's own machinery — see `concepts/razborov-flag-algebras`-style content) yield bounds tight at small extremal configurations ($C_5$, Petersen, Clebsch). The "edge-splitting + weighted-half" construction (Prop. 1.1, Lemma 4.1) is a reusable optimization template for any "find a sparse/dense induced subgraph" problem.

## Open questions / connections
- Quadrilateral density problem: determine $\min C_4(G)$ as a function of $\rho(G)$ for triangle-free $G$ — only $\rho = 5/16$ (Clebsch) and $\rho=2/5$ ($C_5$) solved exactly; "measure of non-randomness" in triangle-free graphs.
- Extend $\alpha \ge 2/5$ result to an open neighbourhood $\alpha \ge 2/5 - \epsilon$ (already known for min/avg degree per Norin–Yepremyan).
- Erdős's companion conjecture: any triangle-free graph on $n$ vertices is bipartite after removing $\le n^2/25$ edges — still wide open.
- Is the Higman–Sims bound $\beta(G) \le 1/50 - 10^{-4}$ actually tight? (Optimization suggests yes; not rigorously verified.)

## Key terms
half-graph conjecture, Erdős, triangle-free, sparse halves, flag algebras, Razborov, quadrilateral density, $C_4$ density, Clebsch graph, Petersen graph, strongly regular graphs, induced matching, girth, independence number, Krein graphs, Cauchy-Schwarz SDP
