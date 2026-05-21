---
type: concept
author: agent
drafted: 2026-05-02
related_problems: [P2, P3, P4, P9, P13]
related_techniques: [bounded-lbfgs-per-region-sigmoid.md, gap-space-parameterization.md, larger-n-cascade.md]
related_findings: [p2-peak-locking-hessian-mechanism.md, equioscillation-escape.md, optimizer-recipes.md]
cites:
  - ../findings/p2-peak-locking-hessian-mechanism.md
  - ../findings/equioscillation-escape.md
  - ../concepts/parameterization-selection.md
  - ../concepts/smooth-max-approximation.md
  - ../personas/polya.md
  - ../personas/tao.md
related_personas: [polya.md, tao.md]
promoted_from: ../findings/p2-peak-locking-hessian-mechanism.md
promoted_on: 2026-05-02
---

# Parameterization-induced rank deficiency

## TL;DR

When the optimum of a constrained problem lies on the boundary of the feasible region (e.g. some cells of $f$ at zero in a non-negativity-constrained problem), the *parameterization* of the unconstrained reformulation determines whether the Hessian at a v-critical point retains finite curvature on the boundary subspace. Parameterizations $f = \varphi(v)$ with $\varphi'(0) = 0$ but $\varphi''(0) \neq 0$ — paradigmatically $f = v^2$ — escape this trap. Parameterizations with $\varphi'(0) = \varphi''(0) = 0$ — including $f = \exp(v)$ and $f = v^p$ for $p \geq 3$ — produce a rank-deficient Hessian on the boundary subspace, and the optimizer experiences a flat sub-manifold it cannot decisively traverse. This is the formal mechanism behind the "peak-locking" phenomenon documented across the autocorrelation problem family.

## What it is

For a smooth objective $C(f)$ over a feasible region $\mathcal{F}$ with a non-negativity-style constraint, an unconstrained reformulation $C \circ \varphi$ over $v \in \mathbb{R}^d$ has Hessian at a v-critical point

$$
H_v \;=\; J_\varphi(v)^\top \, H_f \, J_\varphi(v) \;+\; \mathrm{diag}\!\big(\varphi''(v) \odot \nabla_f C\big).
$$

Let $S = \{i : f_i = 0\}$ be the *dead-cell subspace* (boundary indices of the optimum). The first term is rank-deficient on $S$ for any $\varphi$ with $\varphi'(0) = 0$ — the Jacobian kills those rows. The second term is the **load-bearing factor**: it is zero on $S$ when $\varphi''(0) = 0$, and is $\varphi''(0) \cdot \nabla_f C$ on $S$ otherwise.

| Boundary location for $f = 0$ | $\varphi'$, $\varphi''$ at the boundary | Hessian on $S$ | Optimizer behavior |
|---|---|---|---|
| Finite $v_0$ with $\varphi'(v_0) \neq 0$ | $\varphi' \neq 0$ | full rank (boundary not at a critical point of $v$-problem) | constraint is hard-bounded, often hits L-BFGS-B walls |
| Finite $v_0$ with $\varphi' = \varphi'' = 0$ at $v_0$ | both vanish | rank-deficient on $S$ | **peak-locking** |
| **$v_0$ at infinity** ($\varphi$ vanishes asymptotically) | both vanish in the limit | rank-deficient on $S$ | **peak-locking** ($\exp$, sigmoid) |
| Finite $v_0$ with $\varphi'(v_0) = 0$, $\varphi''(v_0) \neq 0$ | $\varphi'' \neq 0$ | full rank — eigenvalue $\varphi''(v_0) \cdot \nabla_f C$ on $S$ | **escape** — KKT-style activity test exposed at boundary |

Only the last row escapes. **Finite $v$-coordinate for the boundary AND non-vanishing second derivative there** are *both* required. $v^2$ is the canonical example (boundary at $v_0 = 0$, $\varphi''(0) = 2$); sigmoid is *not* an escape (boundary at $v_0 = \pm \infty$, where $\sigma'' \to 0$); $\exp$ is not an escape (boundary at $v_0 = -\infty$).

## When it applies

The mechanism applies whenever:

- The objective $C$ is smooth (or made smooth via a relaxation like $\mathrm{LSE}_\beta$ for $\max$); and
- The optimum has $f_i = 0$ on a non-empty index set $S$ (sparse SOTA — typical for variational problems with positivity constraints); and
- The unconstrained reformulation $f = \varphi(v)$ has $\varphi(0) = 0$ at a *finite* $v$-coordinate (so $v_i = 0$ corresponds to $f_i = 0$ at finite $v$, not at an asymptote).

The escape — switching to a $\varphi$ with $\varphi''(0) \neq 0$ — applies under the same conditions.

**This applies to** the autocorrelation family with sparse optima: P2 verified, P3 verified.

**This does *not* apply to**:

- **P4 (Third Autocorrelation)** — SOTA has zero dead cells; no boundary subspace exists. The "lock" there is equioscillation saturation at small $n$, a different mechanism, escaped by larger-$n$ cascade.
- **P9 (Uncertainty)** — variables are positive Laguerre double-roots; SOTA at $k=18$ has all gaps $\ge 0.83$ (no active ordering constraint, no boundary cells). P9's documented gap-space escape (lesson #24) is a *coordinate change* that converts an *ordering* constraint into a non-negativity constraint on gaps — that re-coordinatization is the escape, not parameterization curvature.
- **P13 (Edges-vs-Triangles)** — SOTA has dead cells (~74% sparse weight matrix), but P13's documented sigmoid escape (lesson #68) is **not** the curvature-retention escape. Sigmoid has its boundary at $v = \pm \infty$ where $\sigma''$ vanishes — peak-locks worse than exp on a P2 controlled test (52 near-zero eigs vs 32 under exp; basin C 2.10 vs 1.95). P13's actual escape mechanism is replacing hard L-BFGS-B box walls with smooth interior gradients — a *first-order* gradient-flow win, not a *second-order* Hessian-curvature win.

The P9/P13 tests sharpen the scope: parameterization-induced rank deficiency is a non-negativity-cone phenomenon with the boundary at a finite $v$-coordinate. Other constraint geometries (ordering, box) admit their own escapes that are not this mechanism.

## Diagnostic

Two-line test for any problem suspected of parameterization-induced peak-locking:

1. **Count zero-cells of the empirical SOTA.** If $|S| = 0$, the mechanism does not apply — look for equioscillation-saturation locks instead.
2. **At a v-critical point under $\exp(v)$, count Hessian eigenvalues with $|\lambda| < 10^{-6}$.** If the count equals $|S|$ to within rounding, the rank deficiency is exact and the cell heights $\{f_i \approx 0\}$ project 1:1 onto the near-null subspace. Switching to $f = v^2$ should produce zero such eigenvalues at the new v-critical point and a strictly lower (resp. higher, for max problems) basin value.

Numerically verified at $n=80$, $\beta=200$ on P2 and P3: 32 dead cells under $\exp(v)$ produce 32 near-zero eigenvalues; 0 under $v^2$. The full sweep $\{\exp, v^2, v^3, v^4, v^6, U \cdot \sigma\}$ confirms the sufficient condition exactly. See [findings/p2-peak-locking-hessian-mechanism](../findings/p2-peak-locking-hessian-mechanism.md) for the table.

## Why it works

The mechanism is purely the chain rule plus one observation about second derivatives at zero. The chain rule for $H_v$ is standard:

$$
\frac{\partial^2 (C \circ \varphi)}{\partial v_i \partial v_j} = \sum_{k,l} \frac{\partial f_k}{\partial v_i} \frac{\partial f_l}{\partial v_j} \frac{\partial^2 C}{\partial f_k \partial f_l} + \sum_k \frac{\partial^2 f_k}{\partial v_i \partial v_j} \frac{\partial C}{\partial f_k}.
$$

For component-wise $\varphi$ (i.e. $f_i = \varphi(v_i)$), $\partial f_k / \partial v_i = \varphi'(v_i) \delta_{ki}$ and $\partial^2 f_k / \partial v_i \partial v_j = \varphi''(v_i) \delta_{ki} \delta_{ij}$. Substituting gives the announced decomposition.

The observation about $\varphi''(0)$ is the load-bearing fact: among the parameterizations with $\varphi(0) = \varphi'(0) = 0$ (the parameterizations that map $v_i = 0$ to $f_i = 0$ as a finite v-critical point coordinate), only those with non-vanishing second derivative at zero retain a finite Hessian eigenvalue on the boundary subspace. $f = v^2$ is the unique low-degree polynomial with this property; everything higher-order ($v^3, v^4, \ldots$) and $\exp$ all have $\varphi'' \to 0$ at zero.

The Hessian eigenvalue under $v^2$ on $S$ is exactly $2 \cdot \partial C / \partial f_i$, which encodes the **KKT activity** of the boundary constraint. Its sign determines whether the cell *should* stay dead (eigenvalue positive — local minimum on $S$) or be activated (eigenvalue negative — saddle on $S$). Under $\exp(v)$ this sign information is buried in an exponentially decaying tail and the optimizer cannot extract it.

## Equivalent variational view

The choice $f = v^2$ corresponds to the natural gradient flow on the simplex $\{f \geq 0, \int f = 1\}$ under the **Wasserstein-2 metric**. The choice $f = \exp(v)$ corresponds to the natural flow under the **Fisher–Rao information metric**. The Wasserstein flow respects the boundary (cells can deactivate); the Fisher–Rao flow penalizes the boundary infinitely (cells cannot reach zero in finite time). The peak-locking is the Fisher–Rao boundary penalty showing up as Hessian rank deficiency in the parameterized formulation.

This connects to a real literature on natural gradient flows and Otto calculus — see Amari (Information Geometry), Otto–Villani 2000, Carrillo–McCann–Villani on geodesic-convexity. The connection is provisional in this wiki and not yet built out.

## Classic examples

1. **P2 First Autocorrelation** ([2-first-autocorrelation](../problems/2-first-autocorrelation.md)). SOTA at $n=30000$ has ~16% dead cells. Universal $\exp(v)$ peak-locking at $\delta \approx 5.25 \times 10^{-8}$ across all tested $n \in [30k, 300k]$. Switch to $f = v^2$ at $n=90000$ → $\delta = 1.23 \times 10^{-6}$, rank #1. Hessian fingerprint at $n=80$ confirms: 32 dead cells under $\exp(v)$ produce 32 near-zero eigenvalues; 0 under $v^2$.

2. **P3 Second Autocorrelation** ([3-autocorrelation](../problems/3-autocorrelation.md)). Different objective shape (maximize $\|f \star f\|_2^2 / (\|f \star f\|_1 \cdot \|f \star f\|_\infty)$) — same Hessian fingerprint at $n=80$ from a sparse seed. Cross-problem confirmation that the mechanism is **objective-shape agnostic**: it is a property of the parameterization at the boundary, not of the specific functional.

3. **P4 Third Autocorrelation** ([4-third-autocorrelation](../problems/4-third-autocorrelation.md)) — *not* an example. SOTA at $n=400$ has 0 dead cells (function spans $[-22.86, +32.04]$, 81/400 cells negative). The mechanism does not apply; P4's documented escape via larger-$n$ cascade (lesson #51) is a distinct lock type. Useful as a counterexample: not all "peak-locking" is parameterization-induced.

## Distinct lock types — calibration

The wiki had been collapsing two distinct phenomena under "peak-locking." This concept page is one half of the pair:

| Lock type | Diagnostic | Escape | Concept |
|---|---|---|---|
| **Parameterization-induced rank deficiency** (this page) | optimum has $f_i = 0$ on $S$; Hessian under $\exp(v)$ has $\|S\|$ near-zero eigenvalues | switch to $\varphi$ with $\varphi''(0) \neq 0$ | this concept |
| **Equioscillation saturation at fixed $n$** | active constraints $\approx n$; KKT-rigid at this discretization | larger-$n$ cascade with block-repeat + perturbation | [equioscillation](equioscillation.md), [discretization-as-structure](discretization-as-structure.md) |

The two escapes are independent. P2 had only the first lock type (escapes by parameterization). P4 had only the second (escapes by larger $n$). P3 had both at different points of its solution trajectory.

## Related

- Concepts: [parameterization-selection](parameterization-selection.md) (the broader concept; this page is its formal mechanism), [smooth-max-approximation](smooth-max-approximation.md), [equioscillation](equioscillation.md), [discretization-as-structure](discretization-as-structure.md), [autocorrelation-inequality](autocorrelation-inequality.md).
- Findings: [p2-peak-locking-hessian-mechanism](../findings/p2-peak-locking-hessian-mechanism.md) (the empirical verification this page is promoted from), [equioscillation-escape](../findings/equioscillation-escape.md), [optimizer-recipes](../findings/optimizer-recipes.md).
- Personas: [polya](../personas/polya.md) (heuristic of "ask the question first"), [tao](../personas/tao.md) (harmonic analysis perspective on autocorrelation).
- Script: [`scripts/first_autocorrelation/peak_locking_hessian.py`](../../scripts/first_autocorrelation/peak_locking_hessian.py) (reproducibility for the diagnostic).
