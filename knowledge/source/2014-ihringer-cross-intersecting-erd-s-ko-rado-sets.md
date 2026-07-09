---
type: source
kind: paper
title: Cross-Intersecting Erdős-Ko-Rado Sets in Finite Classical Polar Spaces
authors: F. Ihringer
year: 2014
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1409.3606
source_local: ../raw/2014-ihringer-cross-intersecting-erd-s-ko-rado-sets.pdf
topic: general-knowledge
cites:
---

# Cross-Intersecting Erdős-Ko-Rado Sets in Finite Classical Polar Spaces

**Authors:** F. Ihringer  ·  **Year:** 2014  ·  **Source:** https://arxiv.org/abs/1409.3606

## One-line
Tight upper bounds (and equality classifications) for $|Y|\cdot|Z|$ over pairs $(Y,Z)$ of generator-sets in finite classical polar spaces where every $y\in Y$ meets every $z\in Z$ in at least a point.

## Key claim
For all finite classical polar spaces except Hermitian $H(2d-1,q^2)$, the maximum product $|Y|\cdot|Z|$ equals (i) $n/2$ for $Q^+(2d-1,q)$, or (ii) the number of generators on a fixed point for $Q(2d,q),W(2d-1,q),H(2d,q),Q^-(2d+1,q)$; the extremal pairs are classified (latins/greeks split for hyperbolic-even, or $Y=Z$ as an EKR set, modulo a $Q^+(2d-1,q)$ sub-geometry exception in even rank).

## Method
Algebraic / association-scheme approach: the disjointness relation $A_d$ on generators sits in a cometric association scheme whose eigenvalues are $(-1)^r q^{\binom{d-r}{2}+\binom{r}{2}+e(d-r)}$. Apply the Haemers/Hoffman-style **extended weight adjacency** ratio bound (Lemma 4.1: $|Y|\cdot|Z|\le n\,\lambda_b/(k+\lambda_b)$) to the disjointness graph, with Tokushige's equality analysis (Lemma 4.3) pinning $\chi_Y,\chi_Z$ into specific eigenspaces $W_0\perp W_1\perp W_d$. For Hermitian $H(2d-1,q^2)$, a weighted Hoffman matrix $A=A_d-\alpha E_1+\frac{1-c}{n}\alpha f_1 J+\alpha f_1 \frac{c}{n}I$ recovers the LP bound of Ihringer–Metsch and yields $|Y|\cdot|Z|\lesssim q^{d^2-2d+2}$.

## Result
- $Q^+(2d-1,q)$: $|Y|\cdot|Z|\le n/2$; in even $d$ extremal pairs are exactly the latin/greek split.
- $Q(2d,q), W(2d-1,q)$: bound equals number of generators on a point, $\prod_{i=1}^{d-1}(q^i+1)$; in even $d$ a sub-$Q^+(2d-1,q)$ construction can match it.
- $H(2d,q), Q^-(2d+1,q)$: bound equals generators on a point; extremals are EKR sets.
- $H(2d-1,q^2)$: $|Y|\cdot|Z|\lesssim q^{d^2-2d+2}$ (much sharper than the trivial $q^{d^2-d}$); not tight for $d>2$ — known examples reach only $q^{(d-1)^2}$ (point-pencil) or $q^{19/2}$ for $H(7,q^2)$ via a $(2{-}space,3{-}space)$ flag construction.

## Why it matters here
General background for extremal combinatorics on polar-space geometries — informs the **eigenvalue/Hoffman ratio bound** as a generic upper-bound technique applicable to intersecting-family problems on association schemes. No direct Einstein Arena problem ties, but the *weighted Hoffman = LP bound* equivalence (Luz 2007) is a transferable lever for any arena problem framable as a coclique-product on a distance-regular graph.

## Open questions / connections
- Tight bound for cross-intersecting EKR in $H(2d-1,q^2)$, $d\ge 3$, remains open; even $H(7,q^2)$ (where Example 6.5 gives $\approx q^{19/2}$ vs upper bound $\approx q^{10}$) is unresolved.
- Solving cross-intersecting in $H(7,q^2)$ is offered as a stepping stone to the open EKR-max problem in $H(9,q^2)$ via the quotient-geometry reduction sketched in §1.
- Extends Pepe–Storme–Vanhove (2011) EKR-in-polar-spaces classification to the cross-intersecting product regime; parallels Tokushige's eigenvalue technique for cross-$t$-intersecting families.

## Key terms
Erdős-Ko-Rado, cross-intersecting families, finite classical polar spaces, generators, Hermitian polar space H(2d-1,q^2), hyperbolic quadric Q+, association scheme, Hoffman bound, weighted Hoffman / ratio bound, eigenvalue method, Delsarte LP bound, latins and greeks, Ihringer, Tokushige
