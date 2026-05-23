---
type: source
kind: paper
title: Topologically Distinct Sets of Non-intersecting Circles in the Plane
authors: Richard J. Mathar
year: 2016
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1603.00077
source_local: ../raw/2016-mathar-topologically-distinct-sets-non-intersecting.pdf
topic: general-knowledge
cites:
---

# Topologically Distinct Sets of Non-intersecting Circles in the Plane

**Authors:** Richard J. Mathar  ·  **Year:** 2016  ·  **Source:** https://arxiv.org/abs/1603.00077

## One-line
Enumerates the topologically distinct configurations of $N$ circles in the plane under nested, non-intersecting, pair-intersecting, and triple-intersecting regimes, by mapping each configuration to nested-parenthesis expressions / rooted forests and deriving generating-function recurrences.

## Key claim
The number $|C_N|$ of topologically distinct sets of $N$ non-intersecting circles in the plane equals the unlabeled rooted-tree count $1,1,2,4,9,20,48,115,286,719,1842,4766,12486,\dots$ (OEIS A000081), with generating function $C(z)=\exp\!\big(\sum_{j\ge1} z^j C(z^j)/j\big)$; analogous closed-form recurrences extend the count to $k$ distinguishable shapes, one marked circle ($M_N$), one intersecting pair ($X_N$, A261070), touching pairs ($X_N^{(t)}$, A269800), arbitrarily many pair-intersections ($^2X_N$), and up to triple-intersections ($^3X_N$).

## Method
Bijection between nested parenthesis strings $P_N$ (Catalan, A000108) and circle topologies on a line; quotienting by factor reordering yields the commutative-algebra count $C_N$ realized as multisets / unlabeled rooted forests. Generating functions are built by the Pólya / Otter exp-log identity (cycle-index substitution $t_j\mapsto C(z^j)$), with half-convolutions $\tfrac12[C(z)^2+C(z^2)]$ encoding $C_2$ symmetry between the two outer regions of an intersecting pair. Triple intersections are handled by enumerating six fundamental Venn topologies and substituting each one's cycle index (e.g. $(t_1^3+3t_1t_2+2t_3)/6$ for the symmetric RGB diagram).

## Result
Tabulates exact counts to $N\!\approx\!11$–$12$ across all six regimes: $|C_N|$ A000081; sphere-embedded variant A000055; $k=2,3$ shape variants A000151, A006964; marked-circle $|M_N|$ A000243; one-intersecting-pair $|X_N|=0,1,3,15,50,162,506,1558,4727,14227,42521$; touching-pair $|X_N^{(t)}|$ A269800; at-most-binary intersections $|^2X_N|=1,3,8,27,90,330,1225,4729,18554,74234,300828$; up-to-triple $|^3X_N|=1,3,14,61,252,1019,4127,17242,74007,325615,1458604$. Explicit GFs given, e.g. $X(z)=1+z^2 D(z)C(z)/(1-zC(z))$.

## Why it matters here
General background; no direct arena tie — none of the 23 Einstein Arena problems concerns planar circle topology enumeration. Tangentially relevant to the agent's toolkit as a clean worked example of (i) Pólya cycle-index counting under symmetry quotients and (ii) the exp-log / Otter generating-function identity for unlabeled rooted forests, both of which can recur in extremal combinatorics and packing-graph counting tasks.

## Open questions / connections
- Counting circle sets with arbitrary intersection multiplicity ($N\ge4$); only $N\le3$ resolved here (A250001 sequence still open).
- Generalization to other planar curves (ellipses, polygons) or higher-genus surfaces — sphere case is sketched (A000055) but torus / Klein bottle untouched.
- Extends the Knopfmacher–Mays "envelope" sequence $1,1,3,7,19,47,127,330,889,2378,\dots$ as the limiting column of $|C_N^{(N-i)}|$ for fixed $i$; connects to the Euler transform of $|C_N|$.
- Companion to Pólya 1937 and Leroux–Miloudi's Otter-formula generalizations; cycle-index arithmetic with $tj \mapsto F(z^j)$ is the central reusable tool.

## Key terms
nested parentheses, Catalan numbers, Dyck paths, unlabeled rooted trees, rooted forests, generating functions, Pólya enumeration, cycle index, Otter formula, Euler transform, OEIS A000081, circle topology, Venn diagram, planar combinatorics, intersecting circles, Mathar
