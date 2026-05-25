---
type: source
kind: paper
title: A Model Theory Approach to Structural Limits
authors: J. Nesetril, P. D. Mendez
year: 2013
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1303.2865
source_local: ../raw/2013-nesetril-model-theory-approach-structural.pdf
topic: general-knowledge
cites:
---

# A Model Theory Approach to Structural Limits

**Authors:** J. Nesetril, P. D. Mendez  ·  **Year:** 2013  ·  **Source:** https://arxiv.org/abs/1303.2865

## One-line
Unifies four notions of graph convergence (dense, bounded-degree Benjamini–Schramm, elementary, left) into a single framework where limits of finite structures are probability measures on Stone spaces of first-order fragments.

## Key claim
For any Boolean sub-algebra $X \subseteq \mathrm{FO}(L)$, a sequence $(G_n)$ of finite $L$-structures is $X$-convergent iff the associated measures $\mu_{G_n}$ on the Stone space $T(X)$ converge weakly; in the bounded-degree case, every FO-limit decomposes as a union $G \cup \hat{G}$ of a (cleaned) graphing BS-limit and a countable elementary limit (Theorem 5).

## Method
Combines Stone duality with functional analysis: the density $\langle \phi, G\rangle = |\{\bar v : G \models \phi(\bar v)\}|/|G|^p$ defines a bounded additive function on the Lindenbaum–Tarski algebra; via Riesz representation, $\mathrm{ba}(B) \cong \mathrm{rca}(S(B))$, turning convergence of densities into weak-$*$ convergence of measures on the Stone space of complete theories. A non-standard ultraproduct + Loeb-measure construction (after Elek–Szegedy) provides an alternative limit object. Gaifman locality decomposes FO-convergence into FO$_{\mathrm{local}}$ + elementary parts.

## Result
Theorem 1: bijection between $X$-convergent sequences and probability measures on $T(X)$. Proposition 2 / Corollary 1: FO-convergence = FO$_{\mathrm{local}}$-convergence + elementary convergence. Proposition 5: for bounded-degree graphs, BS-convergence ≡ FO$_{\mathrm{local}_1}$-convergence ≡ FO$_{\mathrm{local}}$-convergence. Theorem 5 + Cleaning Lemma: bounded-degree FO-limits are realized by a topological graphing union a countable graph.

## Why it matters here
General background; no direct arena tie. Closest relevance is the meta-template "encode combinatorial densities as measures on a compact dual space and use weak-$*$ limits" — same shape as flag-algebra / SDP limits used in extremal graph theory, which can show up tangentially for extremal-graph or Sidon-style arena problems.

## Open questions / connections
- When does a "nice" Borel limit structure $(V, E, \Sigma, \mu)$ exist for FO-convergent sequences beyond bounded-degree? (forthcoming paper [22] handles bounded tree-depth)
- Measurability of FO-definable sets in $V^p$ depends on projective determinacy / large-cardinal assumptions — pinpointing minimal hypotheses is open.
- Extends Benjamini–Schramm [3], Lovász–Szegedy [15], Elek–Szegedy [7]; bridges sparse/dense dichotomy via the fragment-of-FO lens.

## Key terms
graph limits, structural limits, Stone duality, Lindenbaum-Tarski algebra, Boolean algebra, first-order convergence, Benjamini-Schramm convergence, elementary convergence, Gaifman locality, graphing, ultraproduct, Loeb measure, bounded degree graphs, flag algebra, Nesetril, Ossona de Mendez
