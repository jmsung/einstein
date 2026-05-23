---
type: source
kind: paper
title: A Survey of mass partitions
authors: E. Rold'an-Pensado, P. Sober'on
year: 2020
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2010.00478
source_local: ../raw/2020-roldanpensado-survey-mass-partitions.pdf
topic: general-knowledge
cites:
---

# A Survey of mass partitions

**Authors:** E. Rold'an-Pensado, P. Sober'on  ·  **Year:** 2020  ·  **Source:** https://arxiv.org/abs/2010.00478

## One-line
A broad survey of mass partition theorems — how partitions of $\mathbb{R}^d$ split families of measures or point sets — covering hyperplane arrangements, convex partitions, fans/cones, and extremal variants, with connections to topology, discrete geometry, and computer science.

## Key claim
The ham sandwich theorem and its many generalizations form a rich landscape parametrized by the family $\mathcal{P}$ of admissible partitions; the central open problem is the Grünbaum–Hadwiger–Ramos conjecture: $k$ hyperplanes equipartition $m$ measures in $\mathbb{R}^d$ iff $d \geq \lceil (2^k-1)/k \rceil \cdot m$. The best known upper bound (Mani-Levitska–Vrećica–Živaljević) is $d \geq m + (2^{k-1}-1)2^a$ where $2^a \leq m < 2^{a+1}$.

## Method
Survey synthesizing the test-map/configuration-space (TM/CS) topological scheme: parametrize partitions as a $G$-space $X$, map equivariantly to a target $Y$ encoding the splitting, and apply Borsuk–Ulam or Dold's theorem (Theorem 1.3.2) to force a zero. Algorithmic counterparts are reviewed (ham sandwich in $\mathbb{R}^d$ runs in $O(n^{d-1})$ time with $\Omega(n^{d-2})$ lower bound; PPA-complete when $d$ is part of input).

## Result
Catalogs results on: ham sandwich (Stone–Tukey 1942), Grünbaum–Hadwiger–Ramos hyperplane equipartitions (settled for $d \neq 4$ when $k=d$, $m=1$), Nandakumar–Ramana-Rao convex equipartitions (resolved when number of parts is a prime power, via equivariant obstruction theory), necklace splitting (Alon 1987: $k$ thieves, $m$ colors need $m(k-1)$ cuts), Yao–Yao partitions, $k$-fan equipartitions, Holmsen–Kynčl–Valculescu conjecture, and extremal halving-hyperplane bounds. Highlights Conjecture 2.3.1 (Langerman): $nd$ measures bisectable by chessboard coloring from $n$ hyperplanes.

## Why it matters here
General background — provides the topological-combinatorial toolkit (Borsuk–Ulam, equivariant obstruction theory, TM/CS scheme) underlying many extremal-geometry arguments that may surface in Einstein Arena problems involving discrete geometry, packing, or combinatorial splitting; no direct arena tie to a specific problem.

## Open questions / connections
- Problem 2.1.4: does every absolutely continuous measure in $\mathbb{R}^4$ admit 4 hyperplanes splitting it into 16 equal parts? (only open dimension for Grünbaum's $k=d$, $m=1$ case)
- Langerman's chessboard-bisection conjecture (2.3.1): verified only for $n$ a power of two (Hubard–Karasev); odd $n$ open.
- Nandakumar–Ramana-Rao: convex equipartition into $n$ parts with equal measure AND equal perimeter — open when $n$ is not a prime power.
- Connections to incidence geometry (Guth–Katz distinct distances) via polynomial partitioning, geometric range searching, and gerrymandering applications.

## Key terms
ham sandwich theorem, Borsuk-Ulam, mass partition, Grünbaum-Hadwiger-Ramos, hyperplane arrangement, equipartition, configuration space test map, equivariant obstruction theory, Nandakumar-Ramana-Rao, necklace splitting, Yao-Yao partition, convex k-fan, polynomial partitioning, PPA-complete, halving hyperplanes, Dold theorem
