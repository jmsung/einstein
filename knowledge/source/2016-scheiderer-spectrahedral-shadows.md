---
type: source
kind: paper
title: Spectrahedral Shadows
authors: Claus Scheiderer
year: 2016
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1612.07048
source_local: ../raw/2016-scheiderer-spectrahedral-shadows.pdf
topic: general-knowledge
cites:
---

# Spectrahedral Shadows

**Authors:** Claus Scheiderer  ·  **Year:** 2016  ·  **Source:** https://arxiv.org/abs/1612.07048

## One-line
Disproves the Helton–Nie conjecture by exhibiting convex semi-algebraic sets that admit no semidefinite (SDP) representation, i.e. are not spectrahedral shadows.

## Key claim
The Helton–Nie conjecture is **false**: not every convex semi-algebraic set in $\mathbb{R}^n$ is a spectrahedral shadow. Concretely, for any semi-algebraic $S \subseteq \mathbb{R}^m$ with $\dim(S) \ge 2$, there is a polynomial map $\varphi : S \to \mathbb{R}^k$ whose closed convex hull $\overline{\mathrm{conv}}(\varphi(S))$ has no SDP representation (Thm 4.23). In particular, the PSD cone $P_{n,2d}$ is a spectrahedral shadow **iff** $P_{n,2d} = \Sigma_{n,2d}$, i.e. only for $2d=2$, $n \le 2$, or $(n,2d)=(3,4)$ (Cor 4.25).

## Method
Establishes a **necessary condition** for SDP-representability via semidefinite duality (Thm 3.4): $\overline{\mathrm{conv}(S)}$ is a spectrahedral shadow iff there exists a morphism $\varphi : X \to \mathbb{A}^n$ of affine $\mathbb{R}$-varieties and a finite-dim subspace $U \subseteq \mathbb{R}[X]$ such that every linear $f \ge 0$ on $S$ pulls back to a sum of squares of elements of $U$ — *uniformly*, stable under real-closed-field extension. Counter-examples are built using smooth morphisms + a Puiseux/non-Archimedean infinitesimal trick: a PSD-but-not-SOS form $f(x_0, x_1, \dots, x_n)$ (e.g. Motzkin, Choi–Lam, Hilbert ternary sextics) evaluated at $f(\epsilon, x-\xi)$ for infinitesimal $\epsilon$ blocks any uniform SOS certificate (Prop 4.18).

## Result
Explicit counter-examples include: closed convex hulls of degree-$\le 6$ Veronese images of any 2D semi-algebraic set with non-empty interior in $\mathbb{R}^2$ (embedding to $\mathbb{R}^{27}$, or $\mathbb{R}^{14}$ with the Motzkin form, Ex 4.20–4.21); closed convex hulls of degree-$\le 6$ Veronese of 3D sets to $\mathbb{R}^{83}$ (Ex 4.9); the PSD cone $P_{n,2d}$ for all $(n,2d)$ where strict containment $\Sigma_{n,2d} \subsetneq P_{n,2d}$ holds. Optimization corollary: minimizing a generic polynomial of degree $d \ge 4$ in $n \ge 3$ variables (or $d \ge 6$, $n=2$) over the unit ball **cannot be modeled exactly as an SDP**.

## Why it matters here
Directly informs Cohn–Elkies / sphere-packing LP-bound work, sum-of-squares / Lasserre relaxations, and any arena problem where one is tempted to assume an SDP exact formulation exists — Scheiderer's theorem says exactness can fail structurally, not just numerically. Relevant to P1 (sphere packing) `findings/sdp-relaxation-uselessness`, to autocorrelation/extremal problems whose feasibility cones may be non-spectrahedral, and as a hardness companion to the moment-relaxation toolbox.

## Open questions / connections
- Smallest dimension of a convex semi-algebraic set without SDP representation? Author realizes 14 (11 with refinement); conjectured $\ge 3$; HN proved true for $\mathbb{R}^2$ subsets.
- Is the copositive cone $C_n$ ($n \ge 5$) a spectrahedral shadow? Criterion 3.3 hard to apply directly — alternative characterizations wanted.
- Do counter-examples exist with **smooth boundary**? All constructions here have boundary singularities; Helton–Nie sufficient conditions cover smooth strictly-curved cases.
- Generalized Lax conjecture: are all hyperbolicity cones for $n \ge 4$ spectrahedral shadows? (Known for smooth, via Netzer–Sanyal.)

## Key terms
spectrahedral shadow, semidefinite representation, Helton-Nie conjecture, Lasserre moment relaxation, Parrilo sum-of-squares, PSD cone, Motzkin form, Choi-Lam form, Hilbert 1888, copositive cone, hyperbolicity cone, generalized Lax conjecture, Veronese embedding, real closed field, Puiseux series, semidefinite duality, convex algebraic geometry, Scheiderer
