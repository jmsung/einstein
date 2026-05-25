---
type: source
kind: paper
title: A lower bound on the positive semidefinite rank of convex bodies
authors: Hamza Fawzi, M. S. E. Din
year: 2017
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1705.06996
source_local: ../raw/2017-fawzi-lower-bound-positive-semidefinite.pdf
topic: general-knowledge
cites: 
---

# A lower bound on the positive semidefinite rank of convex bodies

**Authors:** Hamza Fawzi, M. S. E. Din  ·  **Year:** 2017  ·  **Source:** https://arxiv.org/abs/1705.06996

## One-line
Proves an explicit lower bound on the smallest size of a semidefinite-programming lift of a convex body in terms of the algebraic degree of its polar's boundary.

## Key claim
For any convex body $C$ with polar $C^o$, if $d$ is the smallest degree of a polynomial vanishing on $\partial C^o$, then $\mathrm{rank}_{\mathrm{psd}}(C) \geq \sqrt{\log d}$ (Theorem 1), and this bound is tight up to a constant factor: there exist bodies where $\mathrm{rank}_{\mathrm{psd}}(C) \leq \sqrt{20 \log d}$ (Theorem 2).

## Method
Write the KKT optimality system for $\max c^T x$ over the spectrahedron $S$, dropping inequality constraints to get an algebraic variety in $(x,X,Z)$. Bézout's theorem bounds the number of complex solutions of this system by $2^{m^2}$ (Lemma 1), and eliminating auxiliary variables yields a degree-$2^{m^2}$ polynomial vanishing on $\partial S^o$ (Lemma 2). For tightness, use Nie–Ranestad–Sturmfels and von Bothmer–Ranestad formulas $\delta(n,m,r)$ for the algebraic degree of SDP applied to random spectrahedra of dimension $n \approx t_{m/2}$.

## Result
Main bound: $\mathrm{rank}_{\mathrm{psd}}(C) \geq \sqrt{\log d}$, improving the prior bound from quantifier elimination [GPT13] which had unknown constants. Corollary (Theorem 4): a convex body with an SDP lift of size $m$ has at most $2^{m^2}$ vertices — the first such bound on vertices of spectrahedral shadows. For polytopes, $d$ is simply the number of vertices, so this is the SDP analogue of Goemans's $\log d$ bound for LP extension complexity.

## Why it matters here
General background; no direct arena tie. Relevant if the agent ever explores SDP-based lower bounds for combinatorial-geometry problems (P1 sphere-packing, P15/P16 equioscillation, kissing-number LP bounds) — it sharpens the algebraic-geometry framing of "what SDP can and cannot express," complementing the existing `findings/sdp-relaxation-uselessness` dead-end finding from P1.

## Open questions / connections
- Can the $\sqrt{\log d}$ bound be improved to $\log d$ when $C$ is a polytope (matching the LP case)?
- Is the $2^{m^2}$ vertex bound on spectrahedral shadows tight — does some random spectrahedron in dimension $n \approx t_{m/2}$ realize $2^{\Omega(m^2)}$ vertices?
- Conjecture: $\delta(n,m,r) = 2^{\Omega(m^2)}$ for all $r$ in the Pataki range when $n \approx t_{m/2}$ — would simplify the proof of Theorem 2 and improve constants.
- Connects to Rostalski–Sturmfels on algebraic boundaries of polars of spectrahedra and Sinn–Sturmfels on generic spectrahedral shadows.

## Key terms
positive semidefinite rank, SDP lift, spectrahedron, spectrahedral shadow, polar body, algebraic boundary, KKT conditions, Bézout bound, algebraic degree of semidefinite programming, Pataki range, extension complexity, Goemans, Nie-Ranestad-Sturmfels
