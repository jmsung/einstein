---
type: source
kind: paper
title: A Unified Approach to Structural Limits and
 Limits of Graphs with Bounded Tree-Depth
authors: J. Nesetril, P. D. Mendez
year: 2013
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1303.6471
source_local: ../raw/2013-nesetril-unified-approach-structural-limits.pdf
topic: general-knowledge
cites:
---

# A Unified Approach to Structural Limits and
 Limits of Graphs with Bounded Tree-Depth

**Authors:** J. Nesetril, P. D. Mendez  ·  **Year:** 2013  ·  **Source:** https://arxiv.org/abs/1303.6471

## One-line
A unified model-theoretic + measure-theoretic framework for graph limits, casting FO-convergence as weak-* convergence of probability measures on Stone spaces, with explicit modeling limits constructed for graphs of bounded tree-depth.

## Key claim
Every FO-convergent sequence of finite $\lambda$-structures corresponds to a regular probability measure on the Stone space $S_\lambda$ of the Boolean algebra of FO-formulas (Theorem 1.12/1.13), and every FO-convergent sequence of graphs with bounded tree-depth $\leq h$ admits an explicit "modeling" FO-limit — a standard Borel probability space where every FO-definable set is measurable (Theorem 4.36). Conversely, any monotone class admitting modeling FO-limits for all FO-convergent sequences must be nowhere dense (Theorem 1.8/3.39).

## Method
Define the **Stone pairing** $\langle\phi,A\rangle = |\Omega_\phi(A)|/|A|^p$ (probability $\phi$ holds on a uniformly-random tuple). FO-convergence = pointwise convergence of $\langle\phi,\cdot\rangle$ for all $\phi \in \mathrm{FO}(\lambda)$. Via Stone duality, formulas $\to$ clopen sets and finite structures $\to$ regular probability measures on $S_\lambda$; FO-convergence becomes weak-* convergence. For bounded tree-depth, reduce to colored rooted trees of bounded height via a basic interpretation scheme $I_t$, then build modeling limits inductively on tree height using a "comb"/forest decomposition and a **Finitary Mass Transport Principle** (FMTP) as the inverse-side characterization.

## Result
- Representation: FO-limits ↔ $S_\omega$-invariant Radon measures on $S_\lambda$ (Thm 1.12, 1.13).
- Bounded degree: FO-convergence $\iff$ Benjamini-Schramm + elementary convergence; graphing represents the limit (Thm 1.9(1), via Elek).
- Bounded tree-depth: explicit modeling FO-limit exists, and a colored rooted tree modeling of height $\leq h$ is an FO-limit of finite trees iff it satisfies FMTP (Thm 1.11, 4.35, 4.36).
- Obstruction: modeling FO-limits cannot exist universally outside nowhere-dense classes (Thm 1.8); Erdős–Rényi $G(n,p)$ limits cannot be represented as random-free graphons or modelings.

## Why it matters here
General background; no direct arena tie. Possibly relevant as conceptual scaffolding if any arena problem touches extremal graph theory / graph-limit techniques (graphons, flag algebras), but the paper is about *foundations of graph limits*, not extremal bounds — flag-algebra/SDP-style attacks on Turán-type problems would cite the Lovász-Szegedy graphon line, not this generalization.

## Open questions / connections
- Conjecture 5.1 (Problem 5.1): every FO-convergent sequence in a nowhere dense class has a modeling FO-limit (addendum notes [81] proved existence; FMTP version still open).
- Aldous–Lyons conjecture (1.2): every graphing is a Benjamini–Schramm limit of finite bounded-degree graphs — would imply all groups are sofic.
- Problem 5.4: tree-depth modeling $L$ always factors as $I_h(Y)$ for some bounded-height tree modeling $Y$?
- Extends Lovász–Szegedy graphons (dense case) and Benjamini–Schramm/Elek graphings (bounded-degree case) into one framework; generalizes to bounded SC-depth and bounded expansion via low-tree-depth decompositions.

## Key terms
FO-convergence, Stone pairing, Stone duality, modeling, graphon, graphing, Benjamini-Schramm convergence, nowhere dense, bounded tree-depth, bounded expansion, Finitary Mass Transport Principle, Aldous-Lyons conjecture, Lovász-Szegedy, Nešetřil, Ossona de Mendez, Rado graph, low tree-depth decomposition, first-order logic limits
