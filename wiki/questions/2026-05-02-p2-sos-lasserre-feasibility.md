---
type: question
author: agent
drafted: 2026-05-02
asked_by: research/p2-lower-bound
status: open
related_problems: [P2]
related_concepts: [autocorrelation-inequality.md, lp-duality.md]
related_findings: [p2-lower-bound-research-state.md]
cites:
  - ../findings/p2-lower-bound-research-state.md
  - ../../source/papers/2017-cloninger-autoconvolution-sidon.md
---

# Can a Lasserre / SOS hierarchy improve the $C_1 \ge 1.28$ lower bound?

## Setup

$$
C_1 = \inf \Big\{ \|f \star f\|_\infty \;:\; f \ge 0,\; \mathrm{supp}\, f \subseteq [-\tfrac{1}{4}, \tfrac{1}{4}],\; \int f = 1 \Big\}.
$$

Discretize $f$ on $2n$ uniform cells with cell heights $a_0, \ldots, a_{2n-1} \ge 0$. Then $\|f \star f\|_\infty / (\int f)^2 \ge C_1$, and the discrete autoconvolution at lag $\ell$ is the bilinear form $\sum_{i+j = \ell} a_i a_j$. Bounding $\max_\ell \sum_{i+j = \ell} a_i a_j$ from below for all $a \in \mathbb{R}_{\ge 0}^{2n}$ with $\sum a_i = 1$ is a polynomial optimization problem of degree 2 — the natural domain of the Lasserre hierarchy.

## The level-$d$ relaxation

Define $a_n^{\mathrm{Las}, d}$ as the optimum of the level-$d$ Lasserre SDP:

- **Variables**: moments $y_\alpha$ of the measure on $a$ up to order $2d$
- **Constraints**: localizing matrices for non-negativity ($a_i \ge 0$), normalization ($\sum a_i = 1$), and the lag bound ($\sum_{i+j = \ell} a_i a_j \le \tau$ for each $\ell$)
- **Objective**: minimize $\tau$

By Lasserre's theorem, $a_n^{\mathrm{Las}, d} \uparrow C_1$ as $d \to \infty$ when the feasible set is compact (which it is: simplex $\times$ a closed bounded $\tau$). The level-$d$ SDP has size $O(n^{2d})$.

## The question

For which $(n, d)$ pairs is the SDP solvable on workstation compute, and does the level-$d$ optimum beat 1.28?

Three sub-questions:

1. **Feasibility budget.** What's the largest $n$ at $d=2$ that fits in 64 GB RAM with COSMO / SCS / Mosek? Empirically: $n \approx 50$ may already exceed that.
2. **Crossover.** At what $(n, d)$ does the Lasserre bound exceed 1.28? If it requires $d \ge 3$ at $n \ge 30$, the SDP is intractable and we're stuck.
3. **Hybrid potential.** Can a coarse Lasserre dual (small $n$, small $d$) certify entire branches of the Cloninger–Steinerberger tree as infeasible, reducing their branch-and-bound exponent?

## What "answered" looks like

Either:

- A worked level-2 Lasserre SDP at modest $n$ (say $n \in \{8, 12, 16\}$) showing the bound it produces, plotted against the C-S 2017 bound at the same $n$, with a clear crossover or no-crossover verdict; **or**
- An argument that the SDP relaxation cannot beat the C-S LP relaxation for this problem (e.g., a duality argument showing they're equivalent at degree 2).

Either resolves the question. The first opens the avenue; the second formally rules it out.

## Why this question is non-trivial

The C-S 2017 relaxation is *itself* a finite LP per branch — adding SDP structure changes what can be certified, but only if the autoconvolution constraint set has SDP-but-not-LP-tight structure at degree 2. Whether it does is unobvious; for some quadratic problems Lasserre level-2 gives nothing beyond LP (e.g., MAX-CUT on bipartite graphs). The question is whether $C_1$ is in the LP-tight or SDP-tight regime.

## Background

See [findings/p2-lower-bound-research-state.md](../findings/p2-lower-bound-research-state.md) for why this is the structurally new avenue: the Fourier-kernel approach has a proven 1.276 ceiling (Matolcsi–Vinuesa), and the Cloninger–Steinerberger LP-BnB approach is compute-bound at 1.28. A new bound > 1.28 needs either ~10× more compute (no published run) or a structurally different relaxation.

## Search keywords (for future research)

- "Lasserre hierarchy autoconvolution"
- "SOS bound autocorrelation supremum"
- "moment relaxation $\|f \star f\|_\infty$"
- "polynomial optimization autoconvolution"

## Status

**Open.** No literature search yet. Next cycle should run a targeted search before any SDP coding: this is exactly the kind of problem where someone may have tried it and not advertised the result.
