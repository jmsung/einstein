---
type: source
kind: paper
title: The Set of Separable States has no Finite Semidefinite Representation Except in Dimension 3×2\documentclass[12pt]{minimal} \usepackage{amsmath} \usepackage{wasysym} \usepackage{amsfonts} \usepackage{amssymb} \usepackage{amsbsy} \usepackage{mathrsfs} \usepackage{upgreek} \setlength{\oddsidemargin}{-6
authors: Hamza Fawzi
year: 2019
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1905.02575
source_local: ../raw/2019-fawzi-set-separable-states-has.pdf
topic: general-knowledge
cites:
---

# The Set of Separable States has no Finite Semidefinite Representation Except in Dimension 3×2

**Authors:** Hamza Fawzi  ·  **Year:** 2019  ·  **Source:** https://arxiv.org/abs/1905.02575

## One-line
Proves that the convex set of separable quantum states $\mathrm{Sep}(n,m)$ admits no finite-size semidefinite programming representation whenever $n+m > 5$, giving a new elementary counterexample to the Helton–Nie conjecture.

## Key claim
**Theorem 1:** If $\mathrm{Sep}(n,m) \neq \mathrm{PPT}(n,m)$ (equivalently $n+m > 5$), then $\mathrm{Sep}(n,m)$ has no finite semidefinite representation. Sufficient to prove for $(3,3)$ and $(4,2)$; all larger cases follow as linear sections.

## Method
Reduces SDP-representability of $C_A = \mathrm{cl\,conv}\{m_A(z) : z \in \mathbb{C}^n\}$ (with $A$ downward-closed) to a sum-of-squares certificate using the Gouveia–Parrilo–Thomas factorization theorem. Key new ingredient: the certifying functions $f_1,\dots,f_r$ can be taken **semialgebraic**, hence smooth almost everywhere (and shiftable to be smooth at $0$). A Taylor-expansion / Puiseux-expansion argument then converts any smooth SOS decomposition of a homogeneous polynomial into a polynomial SOS decomposition — contradicting nonnegative-but-not-SOS witnesses (Choi polynomial for $(3,3)$; a Ha–Kye dehomogenized witness for $(4,2)$).

## Result
Establishes Theorem 2 (general construction: any nonnegative Hermitian polynomial that is not SOS, supported on a downward-closed $A$, yields a non-SDP-representable convex set $C_A$) and Theorem 3 (real analogue, recovering Scheiderer's result that the cone $P_{n,2d}$ of nonnegative forms is not SDP-representable when $P_{n,2d} \neq \Sigma_{n,2d}$). Proof is elementary — uses only Taylor expansion, semialgebraic regularity (Theorems 4–6), and Puiseux expansion — no algebraic geometry machinery.

## Why it matters here
General background; no direct arena tie. Relevant as a *negative result on SDP/SOS hierarchies*: confirms that for many semialgebraic convex sets, no finite-level Lasserre/DPS-style lift suffices — informs cost/benefit reasoning for SDP relaxations on packing and extremal problems where the agent might be tempted to "just go higher in the hierarchy."

## Open questions / connections
- Generalizes Scheiderer's [Sch18] disproof of Helton–Nie; simplifies the proof to be accessible without algebraic geometry.
- Strengthens Skowronek [Sko16] (no finite family of positive maps for $\mathrm{Sep}(3,3)$) and DPS [DPS04] (DPS hierarchy never terminates finitely when $n+m > 5$).
- Leaves open: explicit lower bounds on approximation quality of finite SDP lifts to $\mathrm{Sep}(n,m)$ (cf. Aubrun–Szarek [AS17b]).
- Open whether *infinite-dimensional* SDP / spectrahedral-shadow-of-cone descriptions can work.

## Key terms
separable states, Sep(n,m), PPT criterion, Peres–Horodecki, semidefinite representation, spectrahedral shadow, Helton–Nie conjecture, Scheiderer, sum of squares, Hermitian polynomial, Choi polynomial, DPS hierarchy, semialgebraic functions, Puiseux expansion, Gouveia–Parrilo–Thomas factorization, quantum entanglement
