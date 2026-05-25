---
type: source
kind: paper
title: Convergence of graphs with intermediate density
authors: P. Frenkel
year: 2016
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1602.05937
source_local: ../raw/2016-frenkel-convergence-graphs-intermediate-density.pdf
topic: general-knowledge
cites:
---

# Convergence of graphs with intermediate density

**Authors:** P. Frenkel  ·  **Year:** 2016  ·  **Source:** https://arxiv.org/abs/1602.05937

## One-line
Proposes a unified graph-convergence notion interpolating between Benjamini–Schramm (bounded-degree) and Lovász dense graph limits, with new "graphoning" limit objects covering intermediate density.

## Key claim
For an admissible pair $(G,d)$, define $t(F,G,d) = \hom(F,G) / (v(G)\, d^{v(F)-1})$ for connected $F$ (extended multiplicatively). Convergence in this single density profile recovers both Benjamini–Schramm convergence (when $d_n=d$ fixed) and dense graph convergence (when $d_n=v(G_n)$). Every convergent sequence of large essential girth admits a limit object: a unique involution-invariant probability measure on the sub-Markov space $\mathbb{M}$ of consistent measure sequences (Theorem 5.10), and — for $\alpha$-regular large-essential-girth sequences with concave $1/v(G_n) \mapsto 1/d_n$ — an explicit $\{0,1\}$-valued Euclidean graphoning limit (Theorem 4.36).

## Method
Build homomorphism-density normalization that unifies sparse and dense regimes; characterize regularity ($\alpha$-regular iff $t(F,\cdot)\to\alpha^{e(F)}$ on forests) and large essential girth ($t_{\rm inj}(C_k,\cdot)\to 0$). For limits, construct **graphonings** $(X,\mathcal{B},\lambda,\mu,W)$ combining a probability measure $\lambda$ (for unrooted statistics) with a (possibly $\sigma$-finite) measure $\mu$ via a kernel $W$, plus Hausdorff/Euclidean variants using geometric measure theory on Cantor-like sets in $[0,1]$ with tailored gauge functions $h$ (e.g. $h_{\rm cube}(x) = 1/\log_2(1/x)$, $h_{\rm proj}(x) = \sqrt{2x}$). The inverse-limit space $\mathbb{M}$ of sub-probability-measure towers furnishes a terminal object in the category of sub-Markov spaces.

## Result
- Spectra rescaled by $d$ concentrate at 0 (Prop 2.1) but second-moment-weighted spectral measures converge along convergent sequences (Lemma 2.2).
- Asymptotics of proper-coloring counts and matching counts are computed for large-essential-girth and approximately-regular sequences.
- Explicit Euclidean graphoning limits constructed for: hypercubes $Q_n$ (with $h_{\rm cube}$, Cantor set with $a_1{=}a_2,\,a_3{=}a_4,\,a_5{=}\cdots{=}a_8,\ldots$); incidence graphs of finite projective planes of order $q\to\infty$ (with $h_{\rm proj}$, Cantor set with triple-then-pair block structure); Cartesian powers; large $n\times\cdots\times n$ grids; random nearly-$d$-regular graphs with $d_n = O(n^{1-\epsilon})$.
- A weak Aldous–Lyons analogue (Problem 5.11) is posed.

## Why it matters here
General background for extremal/discrete combinatorics — relevant if Einstein Arena problems involve sequences of graphs at intermediate density (Cayley graphs of growing groups, incidence structures, hypercube-indexed problems) where neither dense nor bounded-degree limit theory applies. No direct arena tie identified.

## Open questions / connections
- Does every convergent admissible sequence have a pseudo-graphoning limit? (§6 — would need an intermediate-density Szemerédi regularity lemma.)
- Aldous–Lyons converse for $\mathbb{M}$: is every involution-invariant measure on $\mathbb{M}$ realized by some large-essential-girth sequence?
- Extends Bollobás–Riordan and Borgs–Chayes–Cohn–Zhao sparse-limit programs ($L^p$ graphons) by unifying with Benjamini–Schramm rather than only generalizing dense.
- Hausdorff/Euclidean construction depends on a special arithmetic property of gauge functions $h$ — does it extend beyond hypercubes/projective planes?

## Key terms
graph limits, Benjamini–Schramm convergence, dense graph convergence, graphon, graphoning, homomorphism density, large essential girth, regular graph sequence, hypercube, projective plane incidence graph, Hausdorff measure, sub-Markov kernel, involution invariance, Aldous–Lyons conjecture, Lovász, Frenkel
