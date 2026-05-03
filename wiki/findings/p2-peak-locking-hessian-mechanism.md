---
type: finding
author: agent
drafted: 2026-05-02
question_origin: research/p2-peak-locking
status: answered
related_problems: [P2, P3, P4, P9, P13]
related_concepts: [parameterization-selection.md, autocorrelation-inequality.md, smooth-max-approximation.md]
related_findings: [equioscillation-escape.md, optimizer-recipes.md]
cites:
  - ../concepts/parameterization-selection.md
  - ../concepts/smooth-max-approximation.md
  - ../findings/equioscillation-escape.md
  - ../../scripts/first_autocorrelation/peak_locking_hessian.py
---

# Peak-locking Hessian fingerprint: exp(v) vs v² at v-critical points

## Question

Lesson #93/#94 in [optimizer-recipes](optimizer-recipes.md) and [equioscillation-escape](equioscillation-escape.md) state that switching from `f = exp(v)` to `f = v²` unlocks a strictly lower basin on P2. The concept page [parameterization-selection](../concepts/parameterization-selection.md) attributes this to "different Hessian curvature." What is the *mechanism*? Why does one parameterization peak-lock and the other escape, on the same objective?

## Answer

At any v-critical point, the Hessian under reparameterization $f = \varphi(v)$ decomposes as

$$
H_v \;=\; J_\varphi(v)^\top \, H_f \, J_\varphi(v) \;+\; \mathrm{diag}\!\big(\,\varphi''(v) \odot \nabla_f C_\beta\,\big).
$$

The first term is rank-deficient on the *dead-cell subspace* $S = \{i : f_i = 0\}$ under any parameterization that has $\varphi'(v_i) = 0$ when $f_i = 0$ — both `exp` and `v²` satisfy this. The second term is the **mechanism**:

| Parameterization | $\varphi'(v_i)$ at $f_i = 0$ | $\varphi''(v_i)$ at $f_i = 0$ | Hessian on $S$ |
|---|---|---|---|
| $f = \exp(v)$ | $0$ (only as $v \to -\infty$) | $0$ (same limit) | rank-deficient — eigenvalue $\to 0$ on $S$ |
| $f = v^2$ | $0$ (at $v = 0$, finite) | $\boxed{2}$ (constant) | full rank — eigenvalue $= 2 \, \partial C_\beta / \partial f_i$ on $S$ |

The constant $\varphi'' = 2$ under `v²` is the entire content. It says: *even when the gradient sees no first-order signal at a dead cell, the Hessian still sees second-order curvature.* Under `exp`, both the gradient *and* the Hessian on $S$ are exponentially suppressed — the optimizer experiences a flat sub-manifold and cannot decisively prune.

## Numerical verification

Small-instance check at $n = 80$, smooth-max $\beta = 200$, with a SOTA-like sparse seed (script: [`scripts/first_autocorrelation/peak_locking_hessian.py`](../../scripts/first_autocorrelation/peak_locking_hessian.py)). Both parameterizations converge to v-critical points with **the same dead-cell count (32 / 80)** but different objective values:

```
C at exp(v) critical: 1.9539951034
C at v²    critical: 1.7817122319

exp(v): dead cells = 32/80; near-zero Hessian eigs (|λ| < 1e-6) = 32/80
v²    : dead cells = 32/80; near-zero Hessian eigs (|λ| < 1e-6) =  0/80

exp(v) condition #  ≈ 1.03e5
v²     condition #  ≈ 4.55e4
```

The 1:1 correspondence between dead cells and near-zero eigenvalues under `exp(v)` is exact. Under `v²`, the dead cells contribute eigenvalues of order $2 \, \nabla_f C_\beta \approx 10^{-3}$, well above the $10^{-6}$ threshold. `v²` reaches a basin $0.17$ below the `exp(v)` basin — a structural escape, not a polish.

(The negative eigenvalues seen in both spectra are saddle-curvature from the smooth-max $\beta = 200$ approximation; they're a feature of the LSE relaxation, not of the parameterization, and are comparable in size between the two.)

## Why this is the right framing

The standard explanation — "exp can't reach exact zeros" — is necessary but not sufficient. Under `exp(v)`, the gradient at a dead cell *is* zero in the limit; what matters is that the Hessian *also* vanishes, so a perturbation in that direction has third-order or higher effect. Under `v²`, perturbing $v_i$ from $0$ to $\varepsilon$ moves $f_i$ to $\varepsilon^2$, and the change in $C_\beta$ is $\varepsilon^2 \cdot \partial C_\beta / \partial f_i + O(\varepsilon^4)$. The *sign* of $\partial C_\beta / \partial f_i$ at the dead cell is a finite KKT-style signal that activates a structural decision:

- $\partial C_\beta / \partial f_i > 0$: the cell wants to stay dead. Local minimum along that direction.
- $\partial C_\beta / \partial f_i < 0$: the cell wants to be activated. The current $v_i = 0$ is a saddle.

`v²` thus exposes the boundary KKT conditions to the optimizer; `exp(v)` hides them behind an exponentially flat asymptote.

## Sufficient condition for parameterization-induced basin escape

Working hypothesis (established for P2, plausible for the autocorrelation family more broadly): if the true optimum has $f_i = 0$ for some non-empty index set $S$, then a parameterization $f = \varphi(v)$ with $\varphi'(v_i) = 0$ on $S$ but $\varphi''(v_i) \neq 0$ on $S$ produces a v-critical-point structure that exposes the boundary stationarity (KKT) of the underlying constrained problem. Parameterizations with both $\varphi' = \varphi'' = 0$ on $S$ (e.g. $\varphi = \exp$) hide this structure behind a flat sub-manifold, producing peak-locking.

Equivalent variational view: the v² parameterization is the squared-magnitude of the natural gradient flow on the simplex $\{f \geq 0, \int f = 1\}$ with respect to the Wasserstein-2 metric, while `exp(v)` is the natural flow with respect to the Fisher–Rao information metric. The Wasserstein flow respects the boundary (cells can deactivate); the Fisher–Rao flow penalizes the boundary infinitely (cells cannot reach zero in finite time). The peak-locking is the Fisher–Rao boundary penalty showing up as Hessian rank deficiency.

## What this rules out

- Rules out: scaling compute or optimizer effort to escape `exp(v)` peak-locking on problems where the optimum has $f_i = 0$ on a positive-measure index set. The Hessian rank deficiency is structural.
- Rules out: claiming `exp(v)` and `v²` reach equivalent basins on autocorrelation problems with sparse optima. Numerical evidence at $n=80$ shows a $\sim 9\%$ basin gap; the P2 SOTA gap (5e-8 vs 1.2e-6 over the published tied basin) is consistent.

## What this opens

- A clean diagnostic for the parameterization choice: **count zero-cells of the empirical SOTA**. If the count is $> 0$ and the gap is the parameterization-induced rank-deficient subspace, switching to `v²` (or any $\varphi$ with $\varphi'' \neq 0$ at the boundary) is indicated.
- A natural extension: parameterizations $\varphi(v) = v^p$ for $p \in \{2, 3, 4\}$ have $\varphi''(0) = 0$ for $p > 2$. So `v³` should peak-lock similarly to `exp(v)`, not unlock like `v²`. Untested. Cross-check would strengthen the sufficient-condition claim.
- Cross-problem applicability: P3 (Second Autocorrelation), P4 (Third Autocorrelation), P9 (Uncertainty), P13 (Edges-vs-Triangles) — any problem with sparse SOTA structure under non-negativity is a candidate. P9's $k$-climbing escape (lesson #24) plausibly fits the same mechanism: gap-space parameterization $g_i = z_{i+1} - z_i$ has a different second-derivative structure than position-space.

## See also

- Concept: [parameterization-selection](../concepts/parameterization-selection.md) (high-level; this finding is the formal mechanism)
- Concept: [autocorrelation-inequality](../concepts/autocorrelation-inequality.md)
- Concept: [smooth-max-approximation](../concepts/smooth-max-approximation.md) (β-relaxation we use to make the Hessian well-defined)
- Finding: [equioscillation-escape](equioscillation-escape.md) lesson #94 (P2 lesson)
- Finding: [optimizer-recipes](optimizer-recipes.md) lesson #93 (parameterization swap recipe)
- Script: [`scripts/first_autocorrelation/peak_locking_hessian.py`](../../scripts/first_autocorrelation/peak_locking_hessian.py) (the verification)
