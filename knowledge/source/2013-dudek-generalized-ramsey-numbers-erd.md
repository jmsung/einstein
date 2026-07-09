---
type: source
kind: paper
title: On generalized Ramsey numbers of Erdős and Rogers
authors: A. Dudek, Troy Retter, V. Rödl
year: 2013
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1309.4521
source_local: ../raw/2013-dudek-generalized-ramsey-numbers-erd.pdf
topic: general-knowledge
cites:
---

# On generalized Ramsey numbers of Erdős and Rogers

**Authors:** A. Dudek, Troy Retter, V. Rödl  ·  **Year:** 2013  ·  **Source:** https://arxiv.org/abs/1309.4521

## One-line
Establishes near-tight upper bounds for the Erdős–Rogers function $f_{s,t}(n)$ — the minimum, over $K_t$-free graphs of order $n$, of the largest $K_s$-free vertex subset.

## Key claim
For every $s \geq 3$, $f_{s,s+1}(n) \leq c_1(s)(\log n)^{4s^2}\sqrt{n}$ (tight up to polylog), and for every $s \geq 4$, $f_{s,s+2}(n) \leq c_3(s)\sqrt{n}$ (no log factor). Together with prior lower bounds, this confirms $\lim_{n\to\infty} f_{s+1,s+2}(n)/f_{s,s+2}(n) = \infty$ for $s \geq 4$, partially resolving an old question of Erdős.

## Method
Construction is a random graph $G$ built in two layers: (i) a random $q$-uniform sub-hypergraph $H$ of the affine plane of order $q$ (each line kept with probability $\alpha/q$, $\alpha = (\log q)^2$), then (ii) for each surviving line, replace it with a random complete $s$-partite graph via uniform $[s]$-coloring of its points. Theorem 1.2 ($t = s+2$) follows by deleting $\leq 2\alpha^8 q$ vertices to kill "dangerous" 5/6-vertex line configurations that force $K_{s+2}$. Theorem 1.1 ($t = s+1$) takes a further random edge-subgraph at rate $1/\gamma$, $\gamma = (\log q)^8$, and applies the Lovász Local Lemma to simultaneously avoid all $K_{s+1}$ while keeping a $K_s$ in every large vertex set.

## Result
$f_{s,s+1}(n) = n^{1/2 + o(1)}$ for all $s \geq 3$, matching the lower bound $\Omega(\sqrt{n \log n / \log\log n})$ up to a polylog gap and confirming a conjecture of Dudek–Rödl. $f_{s,s+2}(n) = O(\sqrt{n})$ for $s \geq 4$, strictly improving on the $f_{s,s+2}(n) \leq f_{s,s+1}(n)$ bound and giving the best known bound on $f_{s,t}(n)$ for all $6 \leq s+2 \leq t < 2s$. For $t \geq 2s$, Krivelevich's $c(\log n)^{1/(s-1)} n^{s/(t+1)}$ remains best.

## Why it matters here
General background; no direct arena tie. Erdős–Rogers / extremal graph theory is in the agent's scope tag list but no current arena problem is framed as bounding $f_{s,t}(n)$. The affine-plane + random-coloring construction (finite geometry as a sparse incidence backbone, then probabilistic refinement) is a transferable design pattern for any extremal-combinatorics problem where "structure + small noise" beats pure random.

## Open questions / connections
- Question 5.2: Is $f_{s,s+2}(n) = o(\sqrt{n})$ for $s \geq 3$? (i.e., can the $\sqrt{n}$ bound be strictly beaten?)
- Question 5.5: Is $\lim_{n\to\infty} f_{s+1,t+1}(n)/f_{s,t}(n) = \infty$ for all $t > s \geq 3$? (Stronger form of Erdős's original question (3).)
- Extends Wolfovitz (2013, $s=3$ case) and the Dudek–Rödl (2011) line; lower-bound side rests on Krivelevich (1994) + Shearer (1995); $t = s+2$ improvement uses Sudakov (2005) lower bound to get the separation ratio.

## Key terms
Erdős–Rogers function, generalized Ramsey numbers, $K_t$-free graphs, $s$-independence number, affine plane construction, Lovász local lemma, random hypergraph, complete $s$-partite replacement, Chernoff bound, Krivelevich bound, Sudakov lower bound, extremal graph theory
