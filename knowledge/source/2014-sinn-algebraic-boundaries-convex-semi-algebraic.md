---
type: source
kind: paper
title: Algebraic boundaries of convex semi-algebraic sets
authors: Rainer Sinn
year: 2014
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1405.7822
source_local: ../raw/2014-sinn-algebraic-boundaries-convex-semi-algebraic.pdf
topic: general-knowledge
cites:
---

# Algebraic boundaries of convex semi-algebraic sets

**Authors:** Rainer Sinn  ·  **Year:** 2014  ·  **Source:** https://arxiv.org/abs/1405.7822

## One-line
Generalizes the polytope facet/vertex duality to arbitrary convex semi-algebraic sets, characterizing which irreducible components of the algebraic boundary arise as projective duals of extreme-point loci of the dual body.

## Key claim
For a compact convex semi-algebraic $C \subset \mathbb{R}^n$ with $0 \in \operatorname{int}(C)$, every irreducible component $Z$ of $\overline{\operatorname{Ex}(C^o)}^{Zar}$ dualizes to an irreducible component of $\partial_a C$ (Cor. 3.4). The converse direction is characterized exactly: $Z^*$ is a component of $\partial_a C^o$ iff $\dim(Z) + \dim(N_C(\{x\})) = n$ at a general extreme point (Thm. 3.7 / Cor. 3.9).

## Method
Convex duality (polar bodies, normal cones, Straszewicz's theorem on exposed extreme points) combined with projective algebraic duality (conormal varieties, biduality, dual hypersurfaces). The proof of the dimension-criterion threads an incidence correspondence $\Sigma \subset \partial C \times \partial C^o$ through the conormal variety $\operatorname{CN}(\mathbb{P}Z)$ and balances two dimension counts. An algorithmic device — iterated singular loci $(\partial_a C^o)_{k,sing}$ — yields candidate components when $\partial_a C^o$ is smooth along $\partial C^o$ (Thm. 3.16).

## Result
The duality is one-sided in general: $(\mathbb{P}\partial_a C)^* = \mathbb{P}\operatorname{Ex}_a^r(C^\vee)$ always, but the reverse can fail when normal cones have the "wrong" dimension (Rem. 3.6, circle-cut-by-halfspace example). Exceptional extreme-point strata (those whose duals are boundary components but which are *not* themselves boundary components of the dual) live inside iterated singular loci of $\partial_a C^o$ under the smoothness hypothesis; Whitney $a$-regular refinement is needed without it (Ex. 3.20, perturbed teardrop). Worked examples: spectrahedral "pillow" (quartic + two quadric pieces dual to four corners), intersection of two cylinders (degree-8 dual surface).

## Why it matters here
General background; no direct arena tie. Possibly informs SDP/spectrahedral approaches to LP-bound problems (P1 sphere packing, kissing numbers) where understanding the algebraic boundary of feasible regions matters, and intersects faintly with the `findings/sdp-relaxation-uselessness` line of reasoning about why SDP lifts can lose rank-1 structure.

## Open questions / connections
- Extends Ranestad–Sturmfels convex-hull-of-a-variety theory by removing their finite-tangency technical assumption.
- Asserted Sturmfels–Uhler Prop. 2.4 (Gaussian graphical model algebraic boundaries) — now proved.
- Whitney $a$-regular stratification refinement needed for non-smooth $\partial_a C^o$ — left as a structural open direction.
- Connects to Nie–Ranestad–Sturmfels "algebraic degree of SDP" and to hyperbolicity-cone boundary analysis (Renegar, Plaumann–Vinzant).

## Key terms
algebraic boundary, convex semi-algebraic set, projective dual variety, normal cone, extreme point, extreme ray, hyperbolicity cone, spectrahedron, conormal variety, biduality, iterated singular locus, Whitney a-regular, Straszewicz, Ranestad-Sturmfels, Sinn
