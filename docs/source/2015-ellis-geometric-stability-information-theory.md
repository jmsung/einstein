---
type: source
kind: paper
title: Geometric stability via information theory
authors: David Ellis, E. Friedgut, Guy Kindler, A. Yehudayoff
year: 2015
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1510.00258
source_local: ../raw/2015-ellis-geometric-stability-information-theory.pdf
topic: general-knowledge
cites:
---

# Geometric stability via information theory

**Authors:** David Ellis, E. Friedgut, Guy Kindler, A. Yehudayoff  ·  **Year:** 2015  ·  **Source:** https://arxiv.org/abs/1510.00258

## One-line
Proves sharp stability versions of the Loomis–Whitney / Uniform Cover projection inequalities and the lattice edge-isoperimetric inequality, via an information-theoretic argument that forces near-extremal sets to be close in symmetric difference to a box (or cube).

## Key claim
If $S \subset \mathbb{Z}^d$ satisfies $|S| \ge (1-\varepsilon)\bigl(\prod_{g\in G}|\pi_g(S)|\bigr)^{1/m(G)}$ for a cover $G$ with $m(G),\sigma(G)>0$, then there is a box $B\subset\mathbb{Z}^d$ with $|S\triangle B|\le b(d)\rho(G)\varepsilon\,|S|$, where $b(d)=4d^2+64d$ and $\rho(G)=m(G)/\sigma(G)$ — linear-in-$\varepsilon$ dependence, which is best possible. As a corollary, near-isoperimetric $S\subset\mathbb{Z}^d$ (i.e. $|\partial S|\le(1+\varepsilon)2d|S|^{(d-1)/d}$) satisfies $|S\triangle C|\le 72 d^{5/2}\sqrt{\varepsilon}\,|S|$ for some axis-aligned cube $C$.

## Method
Reverses the Llewellyn–Radhakrishnan entropy proof of Shearer's lemma: near-tightness in the Uniform Cover inequality forces the mutual information $I(p_{\{i\}};p_{[d]\setminus\{i\}})\le 2\rho(G)\varepsilon$ between any single-coordinate marginal and its complement. To convert "near-product distribution" back into "near-box set," the authors avoid the lossy Pinsker step ($\sqrt{\varepsilon}$) by introducing a new functional — the **hole-weight** $\mathrm{Hole}(S)=\sum_{x\notin S}\prod_j p_{g_j}(x)$ — and run an iterative trimming procedure on fibres of a 2D slice, applied $d$ times (once per coordinate) to assemble the approximating box. The isoperimetric corollary then combines the projection stability with a stability version of AM–GM.

## Result
Theorem 1 (Uniform Cover stability): $|S\triangle B|\le(4d^2+64d)\rho(G)\varepsilon|S|$, sharp in $\varepsilon$ (witness: $[a]^d\setminus[a']^d$). Corollary 3 (Loomis–Whitney stability): $|S\triangle B|\le 36 d^3\varepsilon|S|$. Theorem 8 (edge-isoperimetric stability in $\mathbb{L}^d$): $|S\triangle C|\le 72 d^{5/2}\sqrt{\varepsilon}|S|$ for a cube $C$, sharp in $\varepsilon$ (witness: cuboid $[a]^{d-1}\times[b]$). Open conjectures: the $d$-dependence may be removable (Conj. 20) or improvable to $\Theta(\sqrt d)$ (Conj. 21). A weighted Brascamp–Lieb-type variant (Theorem 4) carries the same bound.

## Why it matters here
General background; no direct arena tie — but two threads connect: (1) Shearer/entropy + Loomis–Whitney are the canonical tool for projection/volume bounds in discrete-geometry and sphere-packing-adjacent counting arguments, so the stability statement could feed any problem where a near-product configuration arises; (2) the hole-weight trick (a sharper-than-Pinsker functional for $L^1$-style closeness) is a transferable technique for stability arguments in arena problems where $\sqrt{\varepsilon}$ vs $\varepsilon$ matters (e.g. equioscillation tolerance, basin rigidity).

## Open questions / connections
- Conjecture 20: can the constant $b(d)=4d^2+64d$ in Theorem 1 be made dimension-free (absolute constant)?
- Conjecture 21: improve the edge-isoperimetric stability constant from $72d^{5/2}$ to $\Theta(\sqrt d)$.
- Extends/sharpens Bollobás–Thomason Box Theorem and the Chung–Frankl–Graham–Shearer Uniform Cover inequality; complements Fusco–Maggi–Pratelli continuous isoperimetric stability (Theorem 7) with a lattice analogue.
- Hole-weight as a divergence-substitute: where else (parallel repetition, additive combinatorics) does it beat Pinsker?

## Key terms
Loomis-Whitney inequality, Uniform Cover inequality, Shearer's entropy lemma, Brascamp-Lieb inequality, Kullback-Leibler divergence, mutual information, hole-weight, edge-isoperimetric inequality, Bollobás-Thomason box theorem, Fusco-Maggi-Pratelli stability, Pinsker inequality, projection inequality
