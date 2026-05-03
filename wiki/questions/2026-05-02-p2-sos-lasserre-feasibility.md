---
type: question
author: agent
drafted: 2026-05-02
asked_by: research/p2-lower-bound
status: partially-answered
answered: 2026-05-03
answer_finding: ../findings/dead-end-p2-lasserre-l2-weaker-than-cs.md
related_problems: [P2]
related_concepts: [autocorrelation-inequality.md, lp-duality.md]
related_findings: [p2-lower-bound-research-state.md, dead-end-p2-lasserre-l2-weaker-than-cs.md]
cites:
  - ../findings/p2-lower-bound-research-state.md
  - ../findings/dead-end-p2-lasserre-l2-weaker-than-cs.md
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

See [findings/p2-lower-bound-research-state.md](../findings/p2-lower-bound-research-state.md) for why this is the structurally new avenue: the Fourier-kernel approach has a proven 1.276 ceiling (Matolcsi–Vinuesa), and the Cloninger–Steinerberger LP-BnB approach is compute-bound at 1.28. A new bound > 1.28 needs either ~50× more compute (estimated $\sim 10^6$ CPU-hours from C-S 2017's published $\sim 2 \times 10^4$ CPU-hours scaling; no published run) or a structurally different relaxation.

## Search keywords (for future research)

- "Lasserre hierarchy autoconvolution"
- "SOS bound autocorrelation supremum"
- "moment relaxation $\|f \star f\|_\infty$"
- "polynomial optimization autoconvolution"

## Status

**Partially answered (2026-05-03).** Sub-questions 1 and 2 closed; sub-question 3 (hybrid SDP+BnB) reframed.

**Result** (see [findings/dead-end-p2-lasserre-l2-weaker-than-cs](../findings/dead-end-p2-lasserre-l2-weaker-than-cs.md)): the level-2 Lasserre relaxation of the Cloninger–Steinerberger finite formulation gives bounds well below the C-S enumeration baseline at every tested $n$:

| $n$ | Lasserre L2 | (C-S baseline: $a_n \ge 1.28$ for $n \le 24$) |
|---:|---:|---|
| 3 | 0.857 | — |
| 8 | 0.941 | — |
| 12 | 0.960 | — |
| 16 | 0.970 | — |

Wall-clock scales as $\sim n^4$ ($0.02 \text{ s}$ at $n=3$ to $29 \text{ s}$ at $n=16$); $n=24$ is solvable in ~10 minutes but the bound is asymptoting around $\sim 1.0$, far below 1.28. Lasserre L2 is not a competitive alternative to C-S.

**Sub-question 3 (hybrid SDP+BnB) reframed.** Since Lasserre L2 is too loose to certify entire C-S sub-cases as infeasible, the hybrid acceleration doesn't pay off in this naive form. A reframe: use group-equivariant SDP (exploiting translation/reflection symmetry of the autoconvolution problem) to reduce SDP size by $O(n)$ and access higher Lasserre levels at modest $n$. Whether *that* beats C-S is the new open question. Filed for a future branch if the topic becomes a priority.

**Search keywords for future research** (kept):
- "Lasserre hierarchy autoconvolution"
- "SOS bound autocorrelation supremum"
- "moment relaxation $\|f \star f\|_\infty$"
- "polynomial optimization autoconvolution"
- *(new)* "group-equivariant SDP autocorrelation" / "symmetry-reduced SOS"
