---
type: source
kind: paper
title: "Some old and new problems in combinatorial geometry I: around Borsuk's problem"
authors: G. Kalai
year: 2015
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1505.04952
source_local: ../raw/2015-kalai-some-old-new-problems.pdf
topic: general-knowledge
cites:
---

# Some old and new problems in combinatorial geometry I: around Borsuk's problem

**Authors:** G. Kalai  ·  **Year:** 2015  ·  **Source:** https://arxiv.org/abs/1505.04952

## One-line
A survey of open problems orbiting Borsuk's partition conjecture — covering lower/upper bounds for $f(d)$, spherical and normed-space variants, diameter/unit-distance/tangent graphs, and conjectured extensions of Frankl–Wilson/Frankl–Rödl.

## Key claim
The Borsuk number $f(d)$ — the minimum number of smaller-diameter pieces needed to cover any diameter-1 set in $\mathbb{R}^d$ — satisfies $1.2^{\sqrt{d}} \le f(d) \le (\sqrt{3/2}+o(1))^d$, and almost every "natural" attack on closing this gap reduces to a forbidden-intersection or LP/SDP question on highly symmetric combinatorial configurations (cuts, cocycles, equiangular lines, two-distance sets).

## Method
Survey/problem-list synthesis: catalogues counterexample constructions (Kahn–Kalai $\pm 1$ vectors via the $x \mapsto x \otimes x$ embedding into rank-1 PSD; Bondarenko/Jenrich two-distance sets from strongly regular graphs; Hinrichs from Leech lattice) and upper-bound techniques (Schramm/Bourgain–Lindenstrauss covering by homothets, Lassak). Identifies the linear-algebra/polynomial method behind Frankl–Wilson and isoperimetric bootstrapping behind Frankl–Rödl as the structural engine, and proposes Delsarte LP and cocycle-cone generalizations as the way forward.

## Result
Concrete bounds collected: $f(d) \ge 1.2^{\sqrt{d}}$ (Kahn–Kalai); $f(d) \le 2^{d-1}+1$ (Lassak) and $f(d) \le (\sqrt{3/2}+o(1))^d$ (Schramm; Bourgain–Lindenstrauss); smallest known counterexample dimension $d=64$ (Jenrich, 416-point two-distance set from a strongly regular graph). Spherical-cap-without-orthogonal-pair conjecture: $\mu(A) \le 2 \cdot \mathrm{vol}(\text{cap of radius } \pi/4)$ would yield Borsuk counterexamples for $d>70$; Frankl–Wilson currently gives $\mu(A) \le 1.203^{-n}$, Raigorodskii improved to $1.225^{-n}$, DeCorte–Pikhurko improved the 2D bound from $1/3$ to $0.31$.

## Why it matters here
Directly informs the **kissing-number / sphere-packing / equiangular-lines** problem cluster: the $x \otimes x$ embedding, the cut polytope $C_1$, and the rank-1 PSD cone $C_3$ are the same objects underlying LP/SDP bounds the agent uses on Cohn–Elkies-style problems, and de Caen's $\Omega(n^2)$ equiangular lines result is a hard ceiling for any "economic" Euclidean embedding of the elliptic metric. Frankl–Wilson / Frankl–Rödl are the linear-algebra-method workhorses the agent reaches for whenever a forbidden-intersection structure appears in a discrete-geometry problem.

## Open questions / connections
- Is $f(d)$ exponential in $d$? Best route proposed: AG-codes with exponentially many max-weight codewords + Frankl–Wilson-style covering lower bound.
- Conjecture 2.8: every $A \subset S^n$ avoiding orthogonal pairs has $\mu(A) \le 2 \cdot \mathrm{vol}(\text{cap}(\pi/4))$ — would replace Frankl–Wilson and give a Borsuk counterexample at $d \approx 70$.
- Kusner / Swanepoel equilateral-set conjectures in $\ell_p^n$ and general normed spaces; current best lower bound $\exp(c\sqrt{\log n})$ (Swanepoel–Villa).
- Frankl–Rödl for cocycles (Conj. 7.7) and the $T(n,2k,2k+1) = f(n,k)$ Turán-cocycle conjecture — would push lower bounds via the $U_{k,n}$ cone analogue of rank-1 PSD.
- Is there a Delsarte-LP proof of Frankl–Rödl? Could unlock sharper constants for several problems.

## Key terms
Borsuk conjecture, Frankl–Wilson theorem, Frankl–Rödl theorem, Kahn–Kalai counterexample, two-distance sets, equiangular lines, de Caen, cut polytope, rank-one PSD cone, cocycles, Larman conjecture, Delsarte linear programming, strongly regular graphs, Schramm upper bound, diameter graph, polynomial method, Hadwiger covering, Witsenhausen orthogonal-pair, tensor embedding, Szemerédi–Trotter
