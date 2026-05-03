---
type: question
author: agent
drafted: 2026-05-03
asked_by: post-PR-88 follow-up (research/p2-peak-locking)
status: open
related_problems: [P2, P3, P9, P13]
related_concepts: [parameterization-induced-rank-deficiency.md, parameterization-selection.md]
related_findings: [p2-peak-locking-hessian-mechanism.md, k-climbing.md, optimizer-recipes.md]
cites:
  - ../concepts/parameterization-induced-rank-deficiency.md
  - ../findings/p2-peak-locking-hessian-mechanism.md
---

# Does the parameterization-induced rank-deficiency mechanism extend to P9 (gap-space) and P13 (per-region sigmoid)?

## Setup

PR #88 promoted the peak-locking finding to a concept ([parameterization-induced-rank-deficiency](../concepts/parameterization-induced-rank-deficiency.md)) verified on P2 and P3. The mechanism: at any v-critical point of a smooth-relaxed objective $C_\beta(\varphi(v))$ with the optimum on a non-negativity boundary $S = \{i : f_i = 0\}$,

$$
H_v \;=\; J_\varphi^\top H_f J_\varphi \;+\; \mathrm{diag}\!\big(\varphi''(v) \odot \nabla_f C_\beta\big),
$$

and the second term — vanishing under $\exp(v)$ and $v^p$ for $p \ge 3$, equal to $2 \cdot \nabla_f C_\beta$ under $v^2$ — produces a rank-deficient Hessian on $S$ for all $\varphi$ with $\varphi''(0) = 0$. Diagnostic: dead-cell count = near-zero-eigenvalue count (verified 1:1 at $n=80$, $\beta=200$).

P9 and P13 use *different* boundary structures than non-negativity:

| Problem | Constraint | Documented escape |
|---|---|---|
| **P9 Uncertainty** | ordered tuple $z_1 < z_2 < \ldots < z_k$ | gap-space parameterization $g_i = z_{i+1} - z_i > 0$ (lesson #24, [findings/k-climbing](../findings/k-climbing.md)) |
| **P13 Edges-vs-Triangles** | per-region box $f_i \in [\ell_i, u_i]$ | per-region sigmoid $f_i = \ell_i + (u_i - \ell_i) \sigma(v_i)$ (lesson #68, [findings/optimizer-recipes](../findings/optimizer-recipes.md)) |

Both escapes empirically work. The question is whether the *mechanism* is the same — Hessian rank deficiency on a constraint subspace, escaped by a parameterization with non-vanishing second derivative at the boundary — or whether ordered-tuple and box constraints have qualitatively different geometries that don't reduce to the dead-cell story.

## The question

For each of P9 and P13:

1. **Does the SOTA have boundary cells?** P9: are some gaps $g_i = 0$ at the optimum (active ordering constraints)? P13: are some $f_i$ pinned at $\ell_i$ or $u_i$ (active box constraints)?
2. **If yes, does the Hessian fingerprint replicate?** Run the diagnostic: count active boundary indices, count near-zero Hessian eigenvalues at the v-critical point under the "naive" parameterization (e.g., position-space for P9, plain coordinates for P13). Do they match?
3. **Does the documented escape have a non-vanishing second derivative at the boundary?** P9: $g_i = z_{i+1} - z_i$ is *linear*, so $\partial^2 g / \partial z = 0$ — but the escape is about reparameterization in a different space, not about $\varphi''$ on a non-negative cone. P13: sigmoid $\sigma(v)$ has $\sigma''(v) = \sigma(1-\sigma)(1-2\sigma)$, which vanishes at $v = 0$ (where $\sigma = 1/2$, mid-box) and at $v = \pm \infty$ (boundary). So sigmoid's $\varphi''$ structure is *different* from $v^2$'s constant-2.

The third sub-question already hints that the mechanism might *not* extend cleanly — both escapes use parameterizations whose second derivatives at the boundary are zero, not constant. If so, P9/P13's escape works for a different reason (e.g., reformulation in a different coordinate system, not curvature retention at boundary).

## What "answered" looks like

Either:

- **Mechanism extends** — both P9 and P13 show the Hessian fingerprint under their naive parameterization, escape produces 0 near-zero eigenvalues, and a unified statement of the sufficient condition emerges that covers ordering and box constraints alongside non-negativity. The concept page's Classic examples section adds two new cases; the concept becomes a 4-5 problem citation hub.
- **Mechanism does NOT extend** — the fingerprint either doesn't appear (no dead-cell-equivalent structure at the SOTA) or doesn't match the rank-deficiency count. The divergence isolates the mechanism's scope to non-negativity. This is itself a finding — the concept page's "When it applies" section gets a sharper limit, and P9/P13's escapes get filed as *different* mechanisms that should each be characterized separately.

Either resolves the question and improves the wiki's calibration.

## Cost

Cheap. Same script structure as `scripts/first_autocorrelation/peak_locking_hessian.py`, swapped evaluators. Mostly local CPU. ~30–60 min per problem including SOTA inspection. Single cycle.

## Suggested branch

`js/research/peak-locking-cross-problem` from a fresh slate. Read the concept page first; the prediction in sub-question 3 above (sigmoid's $\varphi''$ vanishes at boundary, suggesting the escape works for a different reason than v²'s) is a useful guard against confirmation bias.

## Background

See [findings/p2-peak-locking-hessian-mechanism](../findings/p2-peak-locking-hessian-mechanism.md) and [concepts/parameterization-induced-rank-deficiency](../concepts/parameterization-induced-rank-deficiency.md) for the P2/P3 verification and the formal mechanism. The companion open question on the P2 *lower bound* is [2026-05-02-p2-sos-lasserre-feasibility](2026-05-02-p2-sos-lasserre-feasibility.md).

## Status

**Open.** Filed as a follow-up to PR #88. Cheap to answer; should be the first thing the next P2-area cycle picks up.
