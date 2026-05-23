---
type: source
kind: paper
title: The Tammes Problem for N = 14
authors: O. Musin, A. Tarasov
year: 2014
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1410.2536
source_local: ../raw/2014-musin-tammes-problem.pdf
topic: general-knowledge
cites:
---

# The Tammes Problem for N = 14

**Authors:** O. Musin, A. Tarasov  ·  **Year:** 2014  ·  **Source:** https://arxiv.org/abs/1410.2536

## One-line
A computer-assisted proof that the optimal arrangement of 14 points on $S^2$ maximizing minimum pairwise angular distance is the conjectured configuration $P_{14}$ with $d_{14} \approx 55.67057°$.

## Key claim
$d_{14} = \psi(P_{14}) \approx 55.67057°$, and the maximal arrangement is unique up to isometry (Theorem 1), resolving a >60-year-old open case of the Tammes problem.

## Method
Irreducible contact graph enumeration plus LP feasibility filtering. Step 1: `plantri` generates ~1.5 billion candidate planar graphs satisfying combinatorial constraints (vertex degrees $\in\{0,3,4,5\}$, face sizes $\in\{3,4,5,6\}$). Step 2: iterated linear-programming domain shrinkage (using angle-sum equations, equilateral-triangle/rhombus relations from Prop. 3.2) eliminates non-embeddable graphs; survivors are checked by nonlinear solvers (ipopt). Step 3: uniqueness uses (a) a geometric symmetry/monotonicity argument for $\Gamma_{14}^{(1,2)}$ and (b) Connelly-style equilibrium stress matrix LP infeasibility for $\Gamma_{14}^{(3,4)}$.

## Result
Lemma 1 reduces $G_{14}$ to one of five candidate graphs $\Gamma_{14}^{(0..4)}$; Lemma 2 rules out the four non-extremal ones, leaving $\Gamma_{14}^{(0)} = \Gamma_{14}$. The bound improves on Bachoc–Vallentin SDP ($d_{14}<56.58°$) and Böröczky–Szabó ($d_{14}<58°$), and matches the lower-bound configuration from Fejes Tóth / Sloane's `pack.3.14.txt`.

## Why it matters here
Directly relevant to any arena problem framed as "max-min angular distance of $N$ points on $S^2$" (kissing / spherical-code variants). Demonstrates the **irreducible-contact-graph + plantri-enumerate + LP-filter + stress-matrix-rigidity** pipeline as a reproducible recipe for small-$N$ optimal sphere configurations — directly transferable to discrete-geometry and packing problems in the arena inventory.

## Open questions / connections
- Extends Musin–Tarasov 2012 (N=13, strong thirteen spheres) using nearly identical machinery; suggests N=15,16,17 are next (cf. Böröczky–Szabó upper bounds already exist).
- Connelly equilibrium-stress matrix LP infeasibility as a uniqueness-proof technique — when does it suffice vs. when does one need explicit symmetry/monotonicity (as for $\Gamma_{14}^{(1,2)}$)?
- Computational scaling: 1.5B graphs at N=14 implies plantri enumeration becomes a bottleneck well before N=20; what filtering at generation time would prune earlier?

## Key terms
Tammes problem, spherical code, kissing number, irreducible contact graph, Danzer flip, plantri, planar graph enumeration, equilibrium stress matrix, Connelly rigidity, Karush-Kuhn-Tucker, Fejes Tóth bound, Bachoc-Vallentin SDP, Schütte–van der Waerden, max-min angular distance, $S^2$ packing
