---
type: source
kind: paper
title: SPECTRAHEDRAL LIFTS OF CONVEX SETS
authors: Rekha R. Thomas
year: 2018
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1803.08079
source_local: ../raw/2018-thomas-spectrahedral-lifts-convex-sets.pdf
topic: general-knowledge
cites:
---

# SPECTRAHEDRAL LIFTS OF CONVEX SETS

**Authors:** Rekha R. Thomas  ·  **Year:** 2018  ·  **Source:** https://arxiv.org/abs/1803.08079

## One-line
A survey of how convex sets can be represented as projections of affine slices of the psd cone (spectrahedral lifts), governed by cone factorizations of the slack operator.

## Key claim
The existence of a $K$-lift of a convex body $C$ is equivalent (up to a properness condition) to the existence of a $K$-factorization of its slack operator $S_C(x,y)=1-\langle x,y\rangle$ on $\text{ext}(C)\times\text{ext}(C^\circ)$ — generalizing Yannakakis's polyhedral theorem to arbitrary closed convex cones, and in particular to psd cones $S^k_+$.

## Method
Convex cone programming + duality: for a proper $K$-lift, Slater's condition gives strong duality and produces the factorization maps $A:\text{ext}(C)\to K$, $B:\text{ext}(C^\circ)\to K^*$; conversely, the affine space $L=\{(x,z):1-\langle x,y\rangle=\langle z,B(y)\rangle\,\forall y\}$ reconstructs the lift. For polytopes the operator collapses to the slack matrix; psd rank is then the smallest $k$ with an $S^k_+$-factorization, lower-bounded via Hadamard square root rank $\text{rank}_{\sqrt{}}$.

## Result
- Factorization theorem (Thm 2.3 / 3.3): $K$-lift $\iff$ $K$-factorization of slack operator/matrix.
- psd rank lower bounds: $\text{rank}_{\text{psd}}(P)\geq n+1$ for $n$-polytopes (Thm 4.4); $\text{rank}_{\text{psd}}(C)=\Omega(\sqrt{n})$ for $n$-dim bodies (Prop 4.8); $\text{rank}_{\text{psd}}(C)\geq\sqrt{\log d}$ where $d$ is algebraic degree of $\partial C^\circ$ (Fawzi–Safey El Din).
- Super-polynomial lower bounds $2^{n^\delta}$ for cut, TSP, stable-set polytopes (Lee–Raghavendra–Steurer).
- psd-minimal polytopes classified in dim ≤ 4 (triangles/quads in 2D; simplices, quad pyramids, bisimplices, biplanar octahedra and polars in 3D; 31 classes in 4D).
- Scheiderer (2018): not every convex semialgebraic set has a spectrahedral lift — disproves the Helton–Nie conjecture; smallest counterexamples sit in $\mathbb{R}^{11}$.

## Why it matters here
Background for SDP-relaxation techniques on arena problems where convex hulls of algebraic/discrete sets appear (stable-set/TSP-style polytopes, LP/SDP bounds for sphere packing and kissing). Reinforces the wiki's existing `findings/sdp-relaxation-uselessness` line of reasoning: SDP/spectrahedral lifts have hard lower bounds (psd rank ≥ $n+1$, super-poly for combinatorial polytopes, infinite for some semialgebraic sets), so an SDP approach must clear a known structural floor before being competitive.

## Open questions / connections
- Is psd rank of $n$-gons monotone in $n$? (open in the paper).
- Joint dependence of $\text{rank}_{\text{psd}}(C)$ on algebraic degree of $C^\circ$ and on $n$.
- Does a Helton–Nie counterexample exist in $\mathbb{R}^3$? (current smallest is $\mathbb{R}^{11}$.)
- Connection to theta bodies $\text{TH}_k(I)$ and Lasserre hierarchy — when is the sos-based lift tight, and what's the size cost?
- Symmetric/equivariant lifts (Fawzi–Saunderson–Parrilo) — relevant when arena problems have permutation symmetry (autocorrelation, Sidon, kissing).

## Key terms
spectrahedral lift, psd rank, slack matrix, cone factorization, Yannakakis theorem, theta body, sum of squares, Lasserre hierarchy, stable set polytope, Helton-Nie conjecture, Scheiderer, extended formulation, semidefinite programming, Lovász, perfect graph, psd-minimal polytope
