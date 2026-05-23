---
type: source
kind: paper
title: Four-dimensional polytopes of minimum positive semidefinite rank
authors: J. Gouveia, Kanstantsin Pashkovich, Richard Z. Robinson, Rekha R. Thomas
year: 2015
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1506.00187
source_local: ../raw/2015-gouveia-four-dimensional-polytopes-minimum-positive.pdf
topic: general-knowledge
cites:
---

# Four-dimensional polytopes of minimum positive semidefinite rank

**Authors:** J. Gouveia, Kanstantsin Pashkovich, Richard Z. Robinson, Rekha R. Thomas  ·  **Year:** 2015  ·  **Source:** https://arxiv.org/abs/1506.00187

## One-line
Complete classification of 4-dimensional polytopes whose positive semidefinite (psd) rank attains the dimension lower bound $d+1=5$.

## Key claim
There are exactly **31 combinatorial classes** of psd-minimal 4-polytopes; 11 of them (the projectively unique 4-polytopes) are psd-minimal for every realization, while the other 20 require explicit (sometimes non-linear algebraic) conditions on the slack matrix.

## Method
Two new tools: (i) **trinomial obstructions** — if the symbolic slack matrix $S_P(x)$ has a $(d+2)$-minor that is a trinomial, no polytope in the combinatorial class is psd-minimal (since $D(u_i^2) = D(u_i) = 0$ is impossible for three monomials). (ii) The **slack ideal** $I_P$ — the saturation of the ideal of $(d+2)$-minors of $S_P(x)$, whose positive real zeros parametrize projective-equivalence classes; binomial slack ideals imply combinatorial psd-minimality. Combined with computer algebra (Macaulay2 / Sage), they enumerate classes and produce parametrized minimality conditions.

## Result
The 31 classes are tabulated with $f$-vectors, facet types, and explicit psd-minimal realizations. For classes 1–11 the slack ideal is binomial → every member is psd-minimal. For classes 12–15 (including a dual pair containing non-trivial behavior), psd-minimality is cut out by a **quartic** equation (class 12/13: $x_1^4 + 2x_1^3 x_2 + \cdots + x_2^2 = 0$) and a **degree-8** equation (class 14/15). These classes give the first psd-minimal polytopes whose positive Hadamard square root $\sqrt{S_P}$ has rank $>d+1$, refuting [BKLT13, Problem 2] and the weaker conjecture that the support matrix of a psd-minimal $d$-polytope has rank $d+1$. The 3-cube is psd-minimal iff projectively equivalent to a segment $\times$ trapezoid; the 4-cube iff projectively equivalent to a product of two trapezoids or a cubical prismoid.

## Why it matters here
General background; no direct arena tie. Provides algebraic-geometric machinery (slack ideals, trinomial obstructions, Hadamard square-root rank) that could inform any arena problem requiring exact rank conditions on structured nonnegative matrices, and connects to LP/SDP lift complexity — a recurring theme for combinatorial optimization problems (extremal graphs, stable sets).

## Open questions / connections
- Maximum number of facets of a psd-minimal $d$-polytope — conjecturally $2d$ (tight for 2-level polytopes).
- Precise psd-minimality conditions for general $d$-cube and $d$-cross-polytope.
- Behavior of psd-minimality under free sum / product / join.
- Is every binomial slack ideal toric? Is the slack ideal of a combinatorially psd-minimal polytope always binomial?

## Key terms
positive semidefinite rank, psd-minimal polytope, slack matrix, slack ideal, trinomial obstruction, Hadamard square root rank, projectively unique polytope, 2-level polytope, semidefinite lift, 4-polytope classification, binomial ideal, stable set polytope, Lovász theta, combinatorial optimization, Gouveia, Pashkovich, Thomas
