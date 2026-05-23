---
type: source
kind: paper
title: A note on five dimensional kissing arrangements
authors: Ferenc SzollHosi
year: 2023
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2301.08272
source_local: ../raw/2023-szollhosi-note-five-dimensional-kissing.pdf
topic: general-knowledge
cites:
---

# A note on five dimensional kissing arrangements

**Authors:** Ferenc SzollHosi  ·  **Year:** 2023  ·  **Source:** https://arxiv.org/abs/2301.08272

## One-line
Reports the discovery of a third, previously unknown 40-vector kissing arrangement $Q_5$ in $\mathbb{R}^5$ via clique search on a "multiangular cloud."

## Key claim
In dimension 5 there exist at least three pairwise non-isometric kissing arrangements of 40 unit vectors: the classical $D_5$, Leech's $L_5$ (1967), and a new arrangement $Q_5$ — refuting the Cohn–Jiao–Kumar–Torquato belief that only $D_5$ and $L_5$ exist. This saturates the best known lower bound $\tau(5) \geq 40$.

## Method
Three computer-aided "multiangular cloud" methods: (1) fix a basis $B$ of $d$ pairwise compatible unit vectors and a finite angle set $A \subset [-1, 1/2]$, then enumerate $C_{A,B} = \{tG^{-1}B : t \in A^d,\, tG^{-1}t^T = 1\}$ where $G = BB^T$; (2) extend a $d$-dim basis into $\mathbb{R}^{d+1}$ via the orthogonal complement, allowing $tG^{-1}t^T \leq 1$; (3) precomputed unit-vector sets. In each case a maximum clique search (using `cliquer`) in the compatibility graph $\Gamma$ (edges between vectors with inner product $\leq 1/2$) yields the kissing arrangement, giving $\tau(d) \geq d + \omega(\Gamma)$ (or just $\omega(\Gamma'')$ in Method 3).

## Result
With $d=4$, $A = \{-1, -1/2, 0, 1/2\}$, $B$ the rows of $\tfrac{1}{\sqrt{50}}\begin{pmatrix}2&1&1&1\\1&2&1&1\\1&1&2&1\\1&1&1&2\end{pmatrix}$, and $B_5 = \tfrac{1}{\sqrt{5}}[-1,1,1,1,1]$, the cloud $C'_{A,B} \subset \mathbb{R}^5$ has 78 vectors and $\Gamma'$ has exactly four maximum cliques of size $\omega(\Gamma') = 36$. Two yield $D_5$'s profile; two yield $Q_5$ with profile $\{[-1]^{20},[-4/5]^{60},[-1/2]^{360},[-3/10]^{120},[0]^{500},[1/5]^{20},[1/2]^{480},[1]^{40}\}$, distinct from $D_5$ and $L_5$. $Q_5$ has only 20 antipodal pairs and does not contain $D_4$ as a subset.

## Why it matters here
Directly informs **kissing-number problems** in the arena: gives a constructive, reproducible recipe (multiangular cloud + clique search) for discovering kissing arrangements without LP/SDP, exploiting the gap between the LP upper bound $\tau(5) \leq 44$ and the lower bound $\geq 40$. The "cloud + clique" framework generalizes to other dimensions and could plausibly produce new arrangements in $d=6,7$ where the LP gap is also open.

## Open questions / connections
- Is $Q_5$ rigid in the sense of Cohn–Jiao–Kumar–Torquato (2011)? Does it admit a continuous deformation?
- Do higher-dimensional ($d \geq 6$) kissing arrangements contain an isometric copy of $Q_5$ as a subset, analogous to how $E_8$ contains $D_4$-like structure?
- Are there further non-isometric arrangements at the 40-vector level, or is the moduli space of $\tau(5)=40$ configurations finite?

## Key terms
kissing number, $\tau(5)$, sphere packing, multiangular cloud, clique search, cliquer, Gram matrix, antipodal arrangement, $D_5$ lattice, Leech 1967, rigidity, Cohn–Jiao–Kumar–Torquato, inner product profile, dimension 5
