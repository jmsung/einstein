---
type: source
kind: paper
title: Enumerating rigid sphere packings
authors: Miranda C. Holmes-Cerfon
year: 2014
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/1407.3285v2
source_local: ../raw/2014-holmescerfon-enumerating-rigid-sphere-packings.pdf
ingested_for_concept: basin-rigidity.md
cites: 
---

# Enumerating rigid sphere packings

**Authors:** Miranda C. Holmes-Cerfon  ·  **Year:** 2014  ·  **Source:** http://arxiv.org/abs/1407.3285v2

## One-line
Computational enumeration of all rigid clusters of $n \le 14$ identical hard spheres (and maximum-contact clusters for $n \le 19$), revealing surprising geometric phenomena including hypostatic packings that violate Maxwell's $3n-6$ criterion.

## Key claim
A nearly complete catalogue of pre-stress-stable rigid clusters exists for $n \le 14$, growing as $N(n) \approx 2.5(n-5)!$ (faster than exponential, slower than the smooth-potential rate), with $\sim 2.5\%$ of clusters being singular (linearly floppy but nonlinearly rigid) and a nontrivial fraction being hypostatic (fewer than $3n-6$ contacts).

## Method
Bottom-up dynamical enumeration: start from a known rigid cluster, break each contact to obtain a 1-dimensional constraint manifold, numerically follow the path until a new contact forms, and recurse on all distinct clusters found. Rigidity is certified via pre-stress stability — first-order rigidity from the rigidity matrix Jacobian $R(x)$, then second-order via Fredholm-alternative test $w^T R(v) v$ sign-definite (solvable by SDP). Dimension of the singular solution set is estimated numerically by stepping in candidate tangent directions and re-projecting via Newton's method.

## Result
Total cluster counts: $N(5..14) = 1, 2, 5, 13, 52, 263, 1659, 11980, 98529, 895478$. Maximum-contact numbers $M(n)$ saturate the Bezdek lower bound $\lceil 6n - 7.862 n^{2/3} \rceil$ plus 1 for $6 \le n \le 19$ (except $n=12$). Smallest hypostatic cluster at $n=10$ (missing 1 contact); rigid clusters can be constructed with contact count growing only as $\sim n$ (Kusner's fcc-shell-with-columns family). Multiple geometric realizations of a single adjacency matrix appear from $n=11$ (one pair) up to 666+ pairs at $n=14$. Ground states beyond $n \ge 15$ are almost entirely close-packing fragments — much earlier than for Lennard-Jones.

## Why it matters here
Directly informs discrete-geometry / packing problems on the arena: gives a concrete enumeration framework, a rigorous nonlinear notion of rigidity (pre-stress stability via SDP), and hard data on how often Maxwell's counting heuristic fails. The path-following + Newton-projection algorithm and the singular-cluster handling (deflation, $\sqrt{\text{Tol}}$ accuracy floor) are reusable templates for any problem where local minima of a packing energy must be enumerated rather than just bounded.

## Open questions / connections
- How to compute vibrational entropy / partition function of singular clusters where the harmonic approximation diverges (asymptotic volumes of intersecting manifolds, [Chamber-Loir–Tschinkel]).
- Do "circular" 1D transition paths exist that never re-form a contact, giving rise to indefinitely deforming metastable states?
- Tighten the Combinatorial Kepler bounds $6n - 7.862 n^{2/3} \le M(n) \le 6n - 0.926 n^{2/3}$ — data suggests the lower bound is closer.
- Extends Arkus–Manoharan–Brenner ($n \le 11$, SIAM J. Disc. Math. 2011) and Hoy–Harwayne-Gidansky–O'Hern; relates to coNP-hardness of linkage rigidity (Demaine–O'Rourke, Abbott).

## Key terms
sphere packing, rigid cluster enumeration, pre-stress stability, Maxwell counting rule $3n-6$, hypostatic packing, singular cluster, second-order rigidity, Fredholm alternative, semidefinite programming rigidity test, close-packing fragment, kissing number $n=13$, combinatorial Kepler problem, Bezdek bound, hard-sphere energy landscape, Holmes-Cerfon
