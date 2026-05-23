---
type: source
kind: paper
title: Proof of László Fejes Tóth’s zone conjecture
authors: Zilin Jiang, A. Polyanskii
year: 2017
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1703.10550
source_local: ../raw/2017-jiang-proof-szl-fejes-zone.pdf
topic: general-knowledge
cites:
---

# Proof of László Fejes Tóth's zone conjecture

**Authors:** Zilin Jiang, A. Polyanskii  ·  **Year:** 2017  ·  **Source:** https://arxiv.org/abs/1703.10550

## One-line
Resolves Fejes Tóth's 1973 zone conjecture: any collection of spherical zones covering the unit sphere has total width $\geq \pi$, generalized to all dimensions $S^d$.

## Key claim
**Theorem 1:** For any zones $P_1,\dots,P_n$ covering $S^d$ with widths $2\alpha_1,\dots,2\alpha_n$, $\sum_i 2\alpha_i \geq \pi$. Equality holds iff the normal lines $\ell_i$ to the central hyperplanes are coplanar in clockwise order with $\angle(\ell_i,\ell_{i+1}) = \alpha_i + \alpha_{i+1}$ (cyclic).

## Method
Combines Bang's plank-problem technique with the Goodman–Goodman circle-covering argument. Define $w_i := \sin(\alpha_i)\,u_i$ where $u_i$ is the unit normal to zone $P_i$, and consider the discrete set $L = \{\sum \varepsilon_i w_i : \varepsilon_i \in \{\pm 1\}\}$. Using Bognár's trick, pick the $w \in L$ of maximum norm: either $|w| < 1$ (giving an uncovered point $w/|w|$) or projective duality + two technical lemmas (Lemma 4 covers caps by a smaller cap; Lemma 5 forces coplanarity in equality cases) let one replace a subfamily of zones with a single zone of no larger total width, then induct.

## Result
Total width $\sum 2\alpha_i \geq \pi$ on $S^d$ for all $d \geq 1$. Equality characterized exactly (planar equiangular configurations). Corollaries: (3) caps whose every great sphere intersects one have $\sum r_i \geq \pi/2$ (dual form); (6) antipodal caps with $\sum r_i \geq (n-1)\pi/2$ share a common point; (7) $n$ great spheres always leave an open cap of radius $\pi/(2n)$ uncovered; (8) centrally symmetric convex spherical domains satisfy Fejes Tóth's zone problem — width-$w$ cover implies single zone of width $w$ suffices; cap of radius $r$ needs zones of total width $\geq 2r$.

## Why it matters here
Sharp covering bound on $S^d$ with full equality characterization — useful background for any sphere-packing / kissing / spherical-covering problem where dual cap/zone framings or Bang-style discrete-set max-norm arguments could apply. Demonstrates the "discrete set $\{\pm 1\}^n$ + max-norm vector" trick (Bognár/Bang) as a recurring tool for plank-type lower bounds.

## Open questions / connections
- Conjecture 1/2 (paper): same $\pi$ bound for spherical *segments* covering the ball/sphere — open.
- Conjecture 3: non-separable caps on a hemisphere coverable by a single cap of radius $\sum r_i$ (spherical Goodman–Goodman) — open.
- Bezdek annulus conjecture and Bezdek–Schneider inradius conjecture remain open; this paper's techniques may extend.
- Connects to Ball's complex plank theorem, Kadets's Euclidean covering, fractional plank problem (Aharoni–Holzman–Krivelevich–Meshulam).

## Key terms
Fejes Tóth zone conjecture, Tarski plank problem, Bang theorem, spherical zone, great sphere, cap covering, projective duality, Bognár max-norm trick, Goodman–Goodman circle covering, Bezdek–Schneider, spherical inradius, plank width
