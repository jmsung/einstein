---
type: source
kind: paper
title: Max Cuts in Triangle-Free Graphs
authors: J. Balogh, F. Clemen, Bernard Lidick'y
year: 2021
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2103.14179
source_local: ../raw/2021-balogh-max-cuts-triangle-free-graphs.pdf
topic: general-knowledge
cites:
---

# Max Cuts in Triangle-Free Graphs

**Authors:** J. Balogh, F. Clemen, Bernard Lidick'y  ·  **Year:** 2021  ·  **Source:** https://arxiv.org/abs/2103.14179

## One-line
Uses flag algebras to improve bounds on how many edges must be deleted to make a triangle-free graph bipartite, advancing Erdős' $n^2/25$ conjecture.

## Key claim
Every triangle-free graph $G$ on $n$ vertices satisfies $D_2(G) \le n^2/23.5$ (improving the prior $n^2/18$ bound), and Erdős' conjecture $D_2(G) \le n^2/25$ holds when edge density is $\le 0.2486\,n^2$ or $\ge 0.3197\,n^2$ (previously only $\le 0.172\,n^2$ or $\ge 0.4\,n^2$).

## Method
Flag algebras (Razborov) encode local cuts as SDP constraints: for each rooted subgraph $H$ on $k$ vertices, vertex classes $X_i$ are split into bipartition parts $A,B$ with probabilities $p_i \in \{0, 0.5, 1\}$, yielding inequalities like $D_2(G) \ge 2/25$ that an SDP solver combines. They enumerate cuts rooted on $|V(H)|\le 4$ (953+ cuts) plus $C_5$ (125 cuts) and add hand-designed cuts targeting the Clebsch graph (a known adversary) and $K_2\cup K_2\cup K_2$. The high-density range near $2/5$ is handled separately via a minimum-degree-removal algorithm plus Häggkvist's $C_5$-blow-up subgraph result and Erdős-Győri-Simonovits's blow-up reduction.

## Result
Theorem 2: for large $n$, $D_2(G) \le n^2/23.5$ unconditionally; $D_2(G) \le n^2/25$ when $|E(G)| \ge 0.3197\,n^2$ or $|E(G)| \le 0.2486\,n^2$. Theorem 4 specifically resolves the conjecture for $|E(G)| \ge (0.2 - 10^{-8})n^2$, closing in on the conjectured extremal example (balanced $C_5$-blow-up at density $2/5$).

## Why it matters here
Demonstrates flag-algebra SDP machinery for extremal graph theory in a way directly relevant to discrete combinatorics arena problems — encoding many local cuts and letting an SDP combine them is a transferable template. The Clebsch-graph adversarial-instance trick (add cuts specifically tuned against the known hard example) is a generalizable optimization heuristic for any flag-algebra attack.

## Open questions / connections
- Can adding more cuts (rooted on $\ge 6$ vertices) close the remaining density gap $[0.2486, 0.3197]$ and resolve Conjecture 1 fully? Computational cost grows quickly.
- Local version (Conjecture 2): every triangle-free graph contains $\lfloor n/2 \rfloor$ vertices spanning at most $n^2/50$ edges (Erdős, $250). For regular graphs this implies Conjecture 1 (Krivelevich).
- Extends Erdős-Faudree-Pach-Spencer (1988); parallel to Sudakov ($K_4$-free) and Hu-Lidický-Martins-Norin-Volec ($K_6$-free) flag-algebra results.

## Key terms
flag algebras, triangle-free graphs, max cut, bipartite, Erdős conjecture, semidefinite programming, Razborov, $C_5$-blow-up, Clebsch graph, extremal combinatorics, local cuts, Erdős-Győri-Simonovits
