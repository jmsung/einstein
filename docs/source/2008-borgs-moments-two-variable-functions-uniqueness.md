---
type: source
kind: paper
title: Moments of Two-Variable Functions and the Uniqueness of Graph Limits
authors: Christian Borgs, Jennifer Chayes, Laszlo Lovasz
year: 2008
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/0803.1244v2
source_local: ../raw/2008-borgs-moments-two-variable-functions-uniqueness.pdf
topic: general-knowledge
cites: 
---

# Moments of Two-Variable Functions and the Uniqueness of Graph Limits

**Authors:** Christian Borgs, Jennifer Chayes, Laszlo Lovasz  ·  **Year:** 2008  ·  **Source:** http://arxiv.org/abs/0803.1244v2

## One-line
Proves that a symmetric bounded measurable function $W:[0,1]^2\to\mathbb{R}$ (a graphon) is determined, up to measure-preserving transformation, by its homomorphism densities $t(F,W)$ over all finite simple graphs $F$ — establishing uniqueness of the limit of a convergent dense graph sequence.

## Key claim
**Theorem 2.1:** (i) Two almost twin-free Lebesguian graphons $H,H'$ satisfy $t(F,H)=t(F,H')$ for every simple graph $F$ iff $H\cong H'$ (isomorphic mod 0). (ii) For general graphons, equality of all simple-graph densities is equivalent to *weak isomorphism* (existence of a common graphon $G$ with measure-preserving pull-backs from both). Equivalently (Corollary 2.2), $t(F,W)=t(F,W')$ for all simple $F$ iff there exist measure-preserving $\varphi,\psi:[0,1]\to[0,1]$ and $U\in\mathcal{W}$ with $W=U^\varphi$, $W'=U^\psi$ a.e., iff a coupling $\gamma$ on $[0,1]^2$ exists with $W(X,Y)=W'(X',Y')$ a.s. for independent samples $(X,X'),(Y,Y')\sim\gamma$.

## Method
Builds a "canonical ensemble": pick i.i.d. anchor points $\alpha=(a_1,a_2,\dots)\sim\pi^{\mathbb{N}}$, tag each $x\in\Omega$ by $\Phi_\alpha(x)=(W(x,a_1),W(x,a_2),\dots)\in[0,1]^{\mathbb{N}}$, and push $W$ forward to a graphon $H_\alpha$ on $[0,1]^{\mathbb{N}}$. A measure-theoretic lemma (proven via a monotone-class / law-of-large-numbers argument and Lévy's upward theorem) shows almost every anchor sequence is "regular" so $H_\alpha\cong H$. Two graphons with equal moments are then coupled anchor-by-anchor (inductive moment-matching + Lebesgue-space coupling) so that $H_\alpha\cong H'_\beta$, yielding the desired isomorphism. Reductions to twin-free / Lebesguian / countably-generated form, and a spectral (Hilbert–Schmidt) argument promote simple-graph equality to multigraph equality.

## Result
Establishes the **uniqueness half** of the dense graph limit theory: the limit object $W\in\mathcal{W}_0$ of a convergent graph sequence (existence due to Lovász–Szegedy [11]) is unique up to measure-preserving transformation. Side results: every graphon is weakly isomorphic to a strong, Lebesguian, twin-free graphon (Theorem 3.2, Corollary 3.3); simple-graph density equality $\Leftrightarrow$ multigraph density equality (Lemma 5.1, via spectral decomposition of $W$ as a compact integral operator). Counterexamples (Examples 1, 2) show twin-freeness and the Lebesgue property are both necessary for the rigid (mod-0) form.

## Why it matters here
General background; no direct arena tie. Graphon theory is the analytic foundation for dense extremal-graph problems and flag-algebra SDP bounds, which underlie several arena problems in the `extremal_graph` family (e.g. Turán-type, Sidon-set-as-graph, autocorrelation viewed as moment). The "moments determine the kernel up to measure-preserving transformation" principle is the conceptual justification for using homomorphism counts as a complete invariant in any Razborov-style flag-algebra approach.

## Open questions / connections
- Extends classical 1-variable Hausdorff moment problem to 2-variable symmetric kernels — analogous uniqueness for higher-arity hypergraphons (sparked the later hypergraph-limit literature).
- Foundation for flag-algebra / SDP-based extremal bounds (Razborov): if a candidate extremal density profile matches all $t(F,\cdot)$, the kernel is essentially unique.
- Open: explicit / constructive canonical form (the paper gives a "canonical ensemble," not a single canonical representative — analogous to monotone rearrangement for 1D functions).

## Key terms
graphon, homomorphism density, graph limits, dense graph convergence, measure-preserving transformation, weak isomorphism, twin-free, Lebesgue space, canonical ensemble, anchor sequence, coupling, Lovasz-Szegedy, flag algebra, Hilbert-Schmidt, moment problem
