---
type: source
kind: paper
title: Constrained Pseudo-Market Equilibrium
authors: F. Echenique, Antonio Miralles, Jun Zhang
year: 2019
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1909.05986
source_local: ../raw/2019-echenique-constrained-pseudo-market-equilibrium.pdf
topic: general-knowledge
cites:
---

# Constrained Pseudo-Market Equilibrium

**Authors:** F. Echenique, Antonio Miralles, Jun Zhang  ·  **Year:** 2019  ·  **Source:** https://arxiv.org/abs/1909.05986

## One-line
Extends Hylland–Zeckhauser pseudo-market equilibrium to arbitrary polyhedral constraint sets by pricing each binding constraint, not just supply, so agents internalize all pecuniary externalities via personalized prices.

## Key claim
For any constrained allocation problem $(\Gamma, C)$ with $C$ a polytope and agents having continuous, quasi-concave, strictly increasing utilities, a pseudo-market equilibrium $(x^*, p^*)$ exists; it is weakly $C$-constrained Pareto efficient (efficient under semi-strict quasi-concavity), and equal-type envy-free. With endowments, an $\alpha$-slack variant mixing exogenous income with endowment value attains approximate individual rationality.

## Method
Treat the feasible set $C$ as primitive (the convex hull of feasible deterministic assignments). Use Rockafellar's polyhedral-cone theorem to write $\mathrm{lcs}(C)$ as a finite intersection of half-spaces $\{a\cdot x \le b\}$ with non-negative coefficients (Lemma 1), then price each non-individual constraint $c=(a,b)\in\Omega^*$ with $p_c\ge 0$; personalized prices $p_{i,l}=\sum_{c} a^c_{i,l} p_c$. Existence follows from Kakutani's fixed-point theorem applied to a truncated excess-demand correspondence on a bounded price box $[0,\bar p]^{\Omega^*}$.

## Result
Theorems 1–2 prove existence + constrained efficiency + equal-type envy-freeness; Theorem 3 establishes approximate individual rationality as $\alpha \to 0$ (Hausdorff continuity of budget sets, Lemma 8). Applications: doctor-hospital with regional floor/ceiling quotas (Kamada-Kojima), controlled school choice (Ehlers et al.), the roommate problem via symmetry constraints (an efficient market-clearing assignment exists even when stable matchings don't), combinatorial assignment, and time-exchange markets.

## Why it matters here
General background; no direct arena tie. The polytope-as-primitive + linear-inequality pricing framework is a clean instance of using LP-duality-flavored reasoning *without* convex programming duality (the authors note Vazirani-Yannakakis 2020 show HZ is computationally hard, ruling out CP duality) — relevant as a methodology touchpoint for problems where constraint geometry matters, but no direct application to the 23 arena problems.

## Open questions / connections
- Computational complexity: Garg-Tröbst-Vazirani (2020) extend hardness results to the endowment version — algorithmic tractability remains open.
- Connection to Budish-Che-Kojima-Milgrom (2013) implementability via bihierarchical constraints — this paper sidesteps implementation by taking the convex hull as primitive.
- Relation to Miralles-Pycia (2020) second-welfare-theorem-without-transfers and McLennan (2018) equilibrium-with-slack — distinct notions of slack for satiation vs endowments.

## Key terms
pseudo-market equilibrium, Hylland-Zeckhauser, constrained allocation, polytope, lower contour set, personalized prices, pecuniary externality, Kakutani fixed point, envy-freeness, roommate problem, distributional constraints, school choice
