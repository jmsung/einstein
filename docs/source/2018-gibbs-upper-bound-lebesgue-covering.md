---
type: source
kind: paper
title: An Upper Bound for Lebesgue’s Covering Problem
authors: P. Gibbs
year: 2018
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1810.10089
source_local: ../raw/2018-gibbs-upper-bound-lebesgue-covering.pdf
topic: general-knowledge
cites:
---

# An Upper Bound for Lebesgue's Covering Problem

**Authors:** P. Gibbs  ·  **Year:** 2018  ·  **Source:** https://arxiv.org/abs/1810.10089

## One-line
Improves the upper bound on Lebesgue's universal covering problem — the smallest convex shape containing a congruent copy of every planar set of unit diameter — to area $0.8440935944$.

## Method
Starts from the "slanted Pál covering" $\mathcal{P}(\sigma)$: a regular hexagon (unit width between opposite sides) with two corners cut by a copy rotated $30° + \sigma$. Removes Sprague-like regions ($C_S, E_S, A_S$) using the fact that any orbiform of unit diameter touching certain edges cannot reach points at distance $>1$. Then removes larger regions $A_H$ near corner $A$ and $E_H$ near corner $E$ via reflection/rotation arguments (Hansen-style): if an orbiform enters the removed region, its reflection or $120°$ rotation also fits in the cover but avoids the region. Minimizes the area of the resulting cover $\mathcal{H}(\sigma)$ numerically over $\sigma < 10°$.

## Result
Theorem 1: $\mathcal{H}(\sigma)$ is a convex covering for all unit-diameter planar sets when $\sigma < 10°$. The minimum area is $< 0.8440935944$, achieved at $\sigma \approx 1.5494°$. Improves the prior Baez–Bagdasaryan–Gibbs (2015) bound of $0.8441153$. Current lower bound (Brass–Sharifi 2005) is $0.832$, leaving a gap of $\approx 0.012$.

## Why it matters here
General background; no direct arena tie. Methodologically interesting as an example of squeezing improved bounds out of a covering problem via reflection-symmetry arguments + slanted-parameter optimization — relevant pattern for any covering/packing problem where the optimal configuration has a small free parameter (cf. P11 packing problems, slanted-angle parameterizations). The reflection-symmetry "if it enters region $X$, its image avoids $X$" argument is a transferable technique.

## Open questions / connections
- Is the optimal Lebesgue cover a subset of $\mathcal{P}(\sigma)$ for some $\sigma$? Computational evidence yes; no proof.
- Author hints further reductions still possible near both $E_H$ and $A_H$ — bound not yet saturated.
- Lower-bound progress (Elekes, Brass–Sharifi) lags far behind upper bounds; conditional lower bounds via unique-fit orbiforms suggested but not pursued.
- Extends Pál (1920), Sprague (1936), Hansen (1992), Baez–Bagdasaryan–Gibbs (2015).

## Key terms
Lebesgue covering problem, universal cover, orbiform, curve of constant width, Pál hexagon, slanted Pál covering, Sprague reduction, Hansen reflection argument, Reuleaux triangle, Jung's theorem, convex covering, unit diameter, Baez-Bagdasaryan-Gibbs, reflection symmetry argument
