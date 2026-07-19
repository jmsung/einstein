---
type: source
kind: paper
title: Deriving Finite Sphere Packings
authors: N. Arkus, V. Manoharan, M. Brenner
year: 2010
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1011.5412
source_local: ../raw/2010-arkus-deriving-finite-sphere-packings.pdf
topic: general-knowledge
cites:
---

# Deriving Finite Sphere Packings

**Authors:** N. Arkus, V. Manoharan, M. Brenner  ·  **Year:** 2010  ·  **Source:** https://arxiv.org/abs/1011.5412

## One-line
An analytical graph-theoretic + geometric method that enumerates all minimally-rigid finite packings of $n$ identical hard spheres in $\mathbb{R}^3$ (complete for $n \le 10$, partial for $n \le 20$).

## Key claim
A complete enumeration of minimally-rigid sphere packings (≥3 contacts/sphere, ≥$3n-6$ total contacts) is computed for $n \le 10$, with these structural facts: (i) all minimally-rigid packings for $n \le 9$ have exactly $3n-6$ contacts; (ii) first non-rigid minimally-rigid packings appear at $n=9$; (iii) first packings with $>3n-6$ contacts appear at $n=10$; (iv) for $10 \le n \le 13$, the maximum-contact packings are all commensurate with the HCP lattice, but for $14 \le n \le 20$ they are not; (v) the count of ground states oscillates with $n$.

## Method
Each candidate packing is encoded as an $n \times n$ adjacency matrix $A$ ($A_{ij}=1 \Leftrightarrow r_{ij}=2r$); nonisomorphic $A$'s are enumerated via nauty, and minimal rigidity ($\ge 3n-6$ contacts, $\ge 3$ per sphere) filters the list. For each surviving $A$, the matching Euclidean distance matrix $D$ is solved by geometric "intersection-circle" rules — chiefly the **triangular bipyramid rule**, which expresses an unknown $r_{ij}$ via dihedral-angle relations $A_1 = A_2 \pm A_3$ around a shared edge — plus elimination rules (e.g. "no more than 2 spheres can simultaneously touch a connected trimer"). Iterative adjacency matrices (those whose all $m<n$ minimally-rigid subgraphs are already realized packings) are solved uniformly by this single rule; non-iterative cases need per-pattern derivations.

## Result
For $n=1,\dots,10$ the numbers of nonisomorphic minimally-rigid $A$'s are $1,1,1,1,1,4,29,438,13828,750352$; the method scales further than algebraic-geometry/Gröbner-basis baselines (SINGULAR caps out at $n=7$). At $n=10$ the first "excess" packings appear with 25 contacts (one more than $3n-6=24$), each realized as an iterative 25-contact $D$ even when the underlying 24-contact $A$ is non-iterative. The recovered set contains all known minimal-second-moment clusters and matches experimentally observed colloidal clusters and Janus-particle structures.

## Why it matters here
Direct relevance to discrete-geometry / sphere-contact arena problems: this is the canonical reference for "what are the rigid finite contact graphs of equal spheres in $\mathbb{R}^3$" and for the structural conjecture that maximum-contact packings must contain octahedra. It also frames the link to Erdős repeated-distance and Euclidean distance matrix completion, which can inform autocorrelation / distance-set problems.

## Open questions / connections
- Maximum-contact conjecture: must every maximum-contact $n$-packing in $\mathbb{R}^3$ contain an octahedral subcluster? Only checked $n \le 20$.
- Scalability past $n=10$ — the triangular-bipyramid algorithm hits combinatorial limits; need a scalable replacement for the non-iterative geometric rules.
- Why does the count of ground states oscillate with $n$, and when does HCP-commensurability break (here, at $n=14$)?
- Extends/connects to: Erdős repeated-distance problem, Euclidean distance matrix completion, PSD matrix completion, 3D generic graph rigidity (Laman-type conditions in $\mathbb{R}^3$).

## Key terms
finite sphere packing, minimal rigidity, adjacency matrix, Euclidean distance matrix completion, triangular bipyramid rule, intersection circle, hexagonal close packing, HCP, ground state enumeration, polytetrahedral cluster, octahedron, colloidal self-assembly, Erdős repeated distance, graph rigidity, Arkus Manoharan Brenner
