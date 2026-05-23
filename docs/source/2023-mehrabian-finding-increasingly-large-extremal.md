---
type: source
kind: paper
title: Finding Increasingly Large Extremal Graphs with AlphaZero and Tabu Search
authors: Abbas Mehrabian, Ankit Anand, Hyunjik Kim, Nicolas Sonnerat, Matej Balog, Gheorghe Comanici, Tudor Berariu, Andy Lee, Anian Ruoss, Anna Bulanova, Daniel Toyama, Sam Blackwell, B. R. Paredes, Petar Velivckovi'c, Laurent Orseau, Joonkyung Lee, Anurag Murty Naredla, D. Precup, Adam Zsolt Wagner
year: 2023
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2311.03583
source_local: ../raw/2023-mehrabian-finding-increasingly-large-extremal.pdf
topic: general-knowledge
cites:
---

# Finding Increasingly Large Extremal Graphs with AlphaZero and Tabu Search

**Authors:** Abbas Mehrabian, Ankit Anand, Hyunjik Kim, Nicolas Sonnerat, Matej Balog, Gheorghe Comanici, Tudor Berariu, Andy Lee, Anian Ruoss, Anna Bulanova, Daniel Toyama, Sam Blackwell, B. R. Paredes, Petar Velivckovi'c, Laurent Orseau, Joonkyung Lee, Anurag Murty Naredla, D. Precup, Adam Zsolt Wagner  ·  **Year:** 2023  ·  **Source:** https://arxiv.org/abs/2311.03583

## One-line
Combines AlphaZero (neural-guided MCTS) and tabu search with a size-incremental curriculum to push the lower bounds on $f(n) := \mathrm{ex}(n, \{C_3, C_4\})$ — max edges in an $n$-node graph of girth $\geq 5$ — for $n$ between 64 and 190.

## Key claim
Incremental curriculum is the decisive ingredient: starting search at size $n$ from a high-scoring graph at size $n-k$ (rather than the empty graph) improves state-of-the-art lower bounds for $f(n)$ across $n \in \{64,\ldots,134\} \cup \{138,\ldots,160\} \cup \{176,\ldots,186\} \cup \{188,\ldots,190\}$. AlphaZero with curriculum *matches* but does not beat incremental tabu search — learning alone did not outperform a strong local-search baseline.

## Method
Formulate graph generation as an "edge-flipping" MDP: state = simple undirected $n$-node graph, action = flip any one of the $\binom{n}{2}$ possible edges (add if absent, remove if present), telescopic reward $R(G,e) = s(G\oplus e) - s(G)$ where $s(G) = e(G) - \triangle(G) - \square(G)$. Lemma 1 shows maximizing $s$ over all graphs is equivalent to lower-bounding $f(n)$. Two solvers compared: (i) AlphaZero with a novel **Pairformer** torso (a stripped-down Evoformer/AlphaFold block doing triangle row/column self-attention over an $(n,n,c)$ pair-representation that carries features for *non-edges* too), plus a ResNet policy head; (ii) tabu search that bans recently-flipped *actions* (not states) with history size $h=5$. Both are wrapped in a curriculum: sample initial graph from `BestGraphs[n-k]` for random $k \in \{1,\ldots,K=4\}$, pad with isolated nodes.

## Result
Concrete new lower bounds tabulated for $n = 51\ldots 200$ (e.g. $f(64) \geq 230$, $f(100) \geq 434$, $f(134) \geq 649$, $f(190) \geq 1050$); graphs released at `gdm_girth5_graphs/girth5_graphs.zip` in sparse6 format. Pairformer beats ResNet on cycle-detection proxy task and on AlphaZero policy cross-entropy / episode return at sizes 80–100 (Pairformer leads by one edge at $n=80,86,93$). Wagner's cross-entropy method [arXiv:2104.14516] is significantly outperformed by both incremental methods as $n$ grows. Without curriculum, both methods degrade fast past $n \approx 30$–40.

## Why it matters here
General background for the Einstein Arena agent — not a direct hit on any of the 23 problems, but methodologically rich: the **incremental/curriculum-from-smaller-$n$ pattern** applies directly to size-parameterized arena problems (sphere packing $n=2..\infty$, kissing-number variants, Sidon sets, Hardin–Sloane configs on $S^2$) where good $n-k$ solutions often near-embed in $n$ optima. The **edge-flipping reversible MDP + telescopic reward + tabu-on-actions** is a transferable template for discrete-combinatorial arena problems where Wagner-style "build once from empty" RL has been the only ML baseline. Confirms the project's prior intuition that strong local-search baselines are hard to beat with pure RL.

## Open questions / connections
- For arena problems with a substructure property, does warm-starting parallel tempering / basin-hopping from $n-k$ solutions yield similar wins as it does here for tabu? (Test on P1 sphere packing, kissing-number problems.)
- What is the right RL objective when the goal is best-case (not expected) return in a deterministic environment? Authors flag this as open — relevant to any optimizer-as-policy framing.
- Pairformer's $O(n^3)$ cost vs ResNet's $O(n^2)$: when is pair-of-nodes message passing worth it for arena graph problems (extremal graph, contact graphs in packing)?
- Backelin (2015) substructure theorem for girth-5 extremals — is there an analog for sphere-packing / Sidon-set lattices?
- Why does AlphaZero only *match* not beat tabu here? Connects to broader question of when neural-guided search adds value over strong heuristics (compare AlphaTensor success vs this null result).

## Key terms
extremal graph theory, girth 5, ex(n;C3,C4), Erdős conjecture, Mantel's theorem, Turán, AlphaZero, MCTS, tabu search, curriculum learning, incremental search, edge-flipping MDP, Pairformer, Evoformer, triangle self-attention, graph neural networks, telescopic reward, substructure property, Wagner cross-entropy, counterexample construction
