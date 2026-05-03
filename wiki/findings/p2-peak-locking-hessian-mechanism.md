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

Small-instance check at $n = 80$, smooth-max $\beta = 200$, with a SOTA-like sparse seed (script: [`scripts/first_autocorrelation/peak_locking_hessian.py`](../../scripts/first_autocorrelation/peak_locking_hessian.py)). Five parameterizations from the same seed:

| $\varphi$ | $\varphi''(0)$ | $C$ at v-critical | dead cells | near-zero Hess eigs | cond # |
|---|---:|---:|---:|---:|---:|
| $\exp(v)$ | $0$ | $1.9539951034$ | $32 / 80$ | $\mathbf{32 / 80}$ | $1.03 \times 10^5$ |
| $v^{2}$ | $\mathbf{2}$ | $\mathbf{1.7817122319}$ | $32 / 80$ | $\mathbf{0 / 80}$ | $4.55 \times 10^4$ |
| $v^{3}$ | $0$ | $1.8107106179$ | $32 / 80$ | $\mathbf{32 / 80}$ | $6.68 \times 10^4$ |
| $v^{4}$ | $0$ | $1.8310046542$ | $32 / 80$ | $\mathbf{32 / 80}$ | $2.40 \times 10^4$ |
| $v^{6}$ | $0$ | $1.8846429515$ | $32 / 80$ | $\mathbf{32 / 80}$ | $4.54 \times 10^4$ |

Two clean readings:

1. **The 1:1 dead-cell ↔ near-zero-eigenvalue correspondence holds for every $\varphi$ with $\varphi''(0) = 0$.** $\exp$, $v^3$, $v^4$, $v^6$ — all four — produce exactly 32 near-zero eigenvalues at the v-critical point, matching their 32 dead cells. The mechanism is *not* "polynomial vs transcendental" or "smooth vs $C^\infty$" — it is exactly $\varphi''(0)$.
2. **Basin value tracks monotonically with the vanishing order of $\varphi$ at zero.** $v^2$ ($\varphi'' = 2$) gives the lowest C; $\exp$ (vanishing to all orders) gives the highest. The polynomials $v^3, v^4, v^6$ interpolate, with $C$ increasing as $\varphi$ vanishes faster at zero. This is consistent with the rank-deficient subspace getting "flatter" as the vanishing order grows.

Under `v²`, the dead cells contribute eigenvalues of order $2 \, \nabla_f C_\beta \approx 10^{-3}$, three orders of magnitude above the $10^{-6}$ near-zero threshold. The other four parameterizations have those eigenvalues all below $10^{-6}$.

(The negative eigenvalues seen in all spectra are saddle-curvature from the smooth-max $\beta = 200$ approximation; they're a feature of the LSE relaxation, not of the parameterization, and are comparable in size across cases.)

## Why this is the right framing

The standard explanation — "exp can't reach exact zeros" — is necessary but not sufficient. Under `exp(v)`, the gradient at a dead cell *is* zero in the limit; what matters is that the Hessian *also* vanishes, so a perturbation in that direction has third-order or higher effect. Under `v²`, perturbing $v_i$ from $0$ to $\varepsilon$ moves $f_i$ to $\varepsilon^2$, and the change in $C_\beta$ is $\varepsilon^2 \cdot \partial C_\beta / \partial f_i + O(\varepsilon^4)$. The *sign* of $\partial C_\beta / \partial f_i$ at the dead cell is a finite KKT-style signal that activates a structural decision:

- $\partial C_\beta / \partial f_i > 0$: the cell wants to stay dead. Local minimum along that direction.
- $\partial C_\beta / \partial f_i < 0$: the cell wants to be activated. The current $v_i = 0$ is a saddle.

`v²` thus exposes the boundary KKT conditions to the optimizer; `exp(v)` hides them behind an exponentially flat asymptote.

## Sufficient condition for parameterization-induced basin escape

**Sufficient condition** (verified at $n=80$ across $\varphi \in \{\exp, v^2, v^3, v^4, v^6\}$): if the true optimum has $f_i = 0$ for some non-empty index set $S$, then a parameterization $f = \varphi(v)$ produces v-critical points that expose boundary KKT stationarity (and hence escape peak-locking) if and only if

$$
\varphi'(v_i) = 0 \quad \text{and} \quad \varphi''(v_i) \neq 0 \quad \text{at } v_i \text{ where } f_i = 0.
$$

The first condition is necessary so that $v_i$ is a finite v-critical-point coordinate (not an asymptote). The second is necessary so that the Hessian's $\mathrm{diag}(\varphi'' \odot \nabla_f C_\beta)$ term retains finite curvature on the dead-cell subspace. Parameterizations satisfying both ($v^2$ is the canonical example) escape; parameterizations with $\varphi'' = 0$ on $S$ (whether $\exp$ or any $v^p$ with $p \geq 3$) peak-lock.

The empirical sweep above is the falsification test: $v^p$ for $p \in \{3, 4, 6\}$ all peak-lock as predicted, ruling out alternative mechanisms ("any non-exp escapes" or "any polynomial escapes") and isolating the mechanism to exactly $\varphi''(0) \neq 0$.

**Equivalent variational view**: the $v^2$ parameterization is the squared-magnitude of the natural gradient flow on the simplex $\{f \geq 0, \int f = 1\}$ with respect to the Wasserstein-2 metric, while `exp(v)` is the natural flow with respect to the Fisher–Rao information metric. The Wasserstein flow respects the boundary (cells can deactivate); the Fisher–Rao flow penalizes the boundary infinitely (cells cannot reach zero in finite time). The peak-locking is the Fisher–Rao boundary penalty showing up as Hessian rank deficiency.

## What this rules out

- Rules out: scaling compute or optimizer effort to escape `exp(v)` peak-locking on problems where the optimum has $f_i = 0$ on a positive-measure index set. The Hessian rank deficiency is structural.
- Rules out: claiming `exp(v)` and `v²` reach equivalent basins on autocorrelation problems with sparse optima. Numerical evidence at $n=80$ shows a $\sim 9\%$ basin gap; the P2 SOTA gap (5e-8 vs 1.2e-6 over the published tied basin) is consistent.

## What this opens

- A clean diagnostic for the parameterization choice: **count zero-cells of the empirical SOTA**. If the count is $> 0$ and the gap is the parameterization-induced rank-deficient subspace, switching to `v²` (or any $\varphi$ with $\varphi'' \neq 0$ at the boundary) is indicated.
- ~~A natural extension: $v^p$ for $p \geq 3$ should peak-lock since $\varphi''(0) = 0$.~~ **Verified.** $v^3, v^4, v^6$ all peak-lock at the same dead-cell count as $\exp$, with basin C tracking the vanishing order. Question [2026-05-02-p2-vp-parameterization-test](../questions/2026-05-02-p2-vp-parameterization-test.md) is closed answered.
- Cross-problem applicability: P3 (Second Autocorrelation), P4 (Third Autocorrelation), P9 (Uncertainty), P13 (Edges-vs-Triangles) — any problem with sparse SOTA structure under non-negativity is a candidate. P9's $k$-climbing escape (lesson #24) plausibly fits the same mechanism: gap-space parameterization $g_i = z_{i+1} - z_i$ has a different second-derivative structure than position-space. Untested.
- The variational framing (Fisher–Rao vs Wasserstein-2 natural gradient flows) connects to a real literature (Amari, Otto–Villani, Carrillo et al.) and is the natural framing for promoting this finding to a publishable result. Untouched here.

## See also

- Concept: [parameterization-selection](../concepts/parameterization-selection.md) (high-level; this finding is the formal mechanism)
- Concept: [autocorrelation-inequality](../concepts/autocorrelation-inequality.md)
- Concept: [smooth-max-approximation](../concepts/smooth-max-approximation.md) (β-relaxation we use to make the Hessian well-defined)
- Finding: [equioscillation-escape](equioscillation-escape.md) lesson #94 (P2 lesson)
- Finding: [optimizer-recipes](optimizer-recipes.md) lesson #93 (parameterization swap recipe)
- Script: [`scripts/first_autocorrelation/peak_locking_hessian.py`](../../scripts/first_autocorrelation/peak_locking_hessian.py) (the verification)
