---
type: source
kind: paper
title: A tight bound for the number of edges of matchstick graphs
authors: Jérémy Lavollée, Konrad Swanepoel
year: 2022
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/2209.09800v2
source_local: ../raw/2022-lavolle-tight-bound-number-edges.pdf
topic: general-knowledge
cites: 
---

# A tight bound for the number of edges of matchstick graphs

**Authors:** Jérémy Lavollée, Konrad Swanepoel  ·  **Year:** 2022  ·  **Source:** http://arxiv.org/abs/2209.09800v2

## One-line
Proves Harborth's 1981 conjecture that a matchstick graph on $n$ vertices has at most $\lfloor 3n - \sqrt{12n-3} \rfloor$ edges.

## Key claim
For every matchstick graph $G$ (plane graph drawn with non-crossing unit-length straight edges) on $n \geq 1$ vertices with $e$ edges: $e \leq 3n - \sqrt{12n-3}$, matching the triangular-lattice construction exactly.

## Method
Induction on $n$ combined with two isoperimetric inequalities: the classical $4\pi A < b^2$ (Lemma 1) handles small $n$ and gives a first bound $F < c\sqrt{12n-3}$ on the weighted count of non-triangular faces; a new hexagonal isoperimetric inequality (Lemma 2, a variant of L'Huilier's), allowing a bounded portion $b^*$ of perimeter to be unconstrained in direction, yields $\sqrt{3}A \leq \tfrac{1}{8}(b + (\tfrac{2}{\sqrt{3}}-1)b^*)^2$. Euler's formula plus edge–face double counting, lower bounds on triangular faces, and analysis of "lattice components" (maximal 2-connected subgraphs on a triangular lattice) combine these into a 12-claim induction step, contradicting any putative counterexample.

## Result
The bound $e \leq 3n - \sqrt{12n-3}$ is tight: triangular-lattice subgraphs achieve $\lfloor 3n - \sqrt{12n-3} \rfloor$ for all $n \geq 1$. The classical isoperimetric inequality alone disposes of $n < 147$; the new hexagonal inequality + lattice-component analysis closes the remaining cases. Improves the authors' previous $3n - c\sqrt{12n-3}$ with $c = 0.976...$ to the optimal $c = 1$.

## Why it matters here
Discrete-geometry extremal bound with a triangular-lattice extremizer — same family as kissing/sphere-packing in the plane and several Einstein Arena packing-style problems. The L'Huilier-variant isoperimetric inequality (bounded "free-direction" perimeter) is a transferable technique: it gives a sharper area bound when most of a boundary lies on a fixed lattice, useful whenever an extremal configuration is nearly-lattice with bounded boundary deviation.

## Open questions / connections
- Extends Harborth's 1974 penny-graph theorem (Theorem 1) from same-lattice configurations to arbitrary matchstick graphs.
- The constants in the proof are deliberately loose (e.g. $c = 1/11$ usable down to $1/20$); a cleaner proof tightening these is open.
- Generalizes to: edge bounds for unit-distance graphs in higher dimensions, or with relaxed crossing constraints (penny → matchstick → general unit-distance).
- Lemma 2 (hexagonal isoperimetric with free-direction allowance) is a standalone tool; finding other extremal-geometry applications is open.

## Key terms
matchstick graph, penny graph, unit-distance graph, Harborth conjecture, isoperimetric inequality, L'Huilier inequality, triangular lattice, Euler formula, lattice components, extremal planar graphs, hexagonal isoperimetric, plane graph edge bound, Lavollée, Swanepoel
