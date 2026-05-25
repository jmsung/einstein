---
type: source
kind: paper
title: 2-Complexes with Large 2-Girth
authors: Dominic Dotterrer, L. Guth, M. Kahle
year: 2015
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1509.03871
source_local: ../raw/2015-dotterrer-2-complexes-large-2-girth.pdf
topic: general-knowledge
cites:
---

# 2-Complexes with Large 2-Girth

**Authors:** Dominic Dotterrer, L. Guth, M. Kahle  ·  **Year:** 2015  ·  **Source:** https://arxiv.org/abs/1509.03871

## One-line
Establishes nearly-matching upper and lower bounds on the maximum 2-girth (minimum non-zero $\mathbb{Z}/2$ 2-cycle size) of a 2-dimensional simplicial complex with $n$ vertices and $m$ 2-faces, revealing a phase transition at $m = n^{5/2}$.

## Key claim
Let $g_2(n,m)$ be the max 2-girth with $n$ vertices, $m$ 2-faces. For $m = n^{2+\alpha}$: if $\alpha < 1/2$, then $c_{\alpha,\epsilon} n^{2-2\alpha-\epsilon} \le g_2(n,m) \le 4 n^{2-2\alpha}$; if $\alpha > 1/2$, then $g_2(n,m) \le C_\alpha$ (constant). Phase transition at $\alpha = 1/2$.

## Method
Upper bound (Thm 3.1): random induced subcomplex on $k = 2n^{1-\alpha}$ vertices forces $f_2 \ge \binom{k}{2}$, triggering $H_2 \ne 0$ by Euler counting, hence a small inclusion-minimal cycle. Upper bound for $\alpha > 1/2$ (Sós–Erdős–Brown): edge-degree pigeonhole produces a dense link-intersection graph $\mathrm{lk}(a) \cap \mathrm{lk}(b)$ which contains a short cycle via Moore-bound arguments, giving a short suspension 2-cycle. Lower bound (Thm 4.1): Linial–Meshulam $Y(n,p)$ with $p = n^{\alpha-1}$, plus a novel counting bound $|T(f,w)| \le C_\delta^f f^{f/2} w^{-(1-\delta)w}$ on combinatorial types of triangulated surfaces obtained via a gluing-story argument that tracks internal vertices through edge gluings.

## Result
- $g_2(n, n^{2+\alpha}) \le 4 n^{2-2\alpha}$ for $0 \le \alpha \le 1/2$ (Thm 3.1).
- $g_2(n, n^{2+\alpha}) \le C_\alpha$ for $\alpha > 1/2$ (Thm 3.2, Sós–Erdős–Brown).
- $g_2(n, n^{2+\alpha}) \ge n^{2-2\alpha-\epsilon}$ exists w.h.p. (Thm 4.1).
- Surface-counting bound $|T(f,w)| \le C_\delta^f f^{f/2} w^{-(1-\delta)w}$ (Thm 5.1) — the technical core.
- Filling area of a triangle cycle in $Y(n,p)$ is $n^{2-2\alpha\pm\epsilon}$ w.h.p. (Thm 6.1).
- Filling distortion $\ge c n^{2-2\alpha-\epsilon}$ for any affine map $Y \to$ Hilbert space (Thm 6.4).

## Why it matters here
General background; no direct arena tie. Combinatorial 2-girth and triangulated-surface counting are extremal-topology results — relevant if the agent ever attacks problems involving 2-dimensional simplicial complexes, random topology, or filling area / isoperimetry. Could inform any future combinatorial-extremal problem about minimal non-trivial substructures in random hypergraph-like objects.

## Open questions / connections
- Tighter bounds on $|T(f,w)|$: gap between current upper bound and any known lower bound.
- Counting connected pseudomanifolds (not just triangulated surfaces) with $f$ faces, $w$ vertices.
- Higher-dimensional generalizations: $d$-girth of $d$-complexes, counting $d$-dimensional simplicial pseudomanifolds.
- Sharpens Aronshtam–Linial–Łuczak–Meshulam [2] from $n^{2-16\alpha}$ to $n^{2-2\alpha-\epsilon}$ in the lower-bound regime $\alpha > 0$.
- Connects to volume distortion of random complexes (Dotterrer [5]).

## Key terms
2-girth, simplicial complex, triangulated surface, Linial-Meshulam random complex, Y(n,p), inclusion-minimal cycle, pseudomanifold, gluing story, Z/2 homology, filling area, isoperimetry, Moore bound, Sós-Erdős-Brown, extremal hypergraph, Brooks-Makover
