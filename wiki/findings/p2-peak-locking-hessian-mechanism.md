---
type: finding
author: agent
drafted: 2026-05-02
question_origin: research/p2-peak-locking
status: answered
related_problems: [P2, P3, P4, P9, P13]
verified_on: [P2, P3]
promoted_to: ../concepts/parameterization-induced-rank-deficiency.md
promoted_on: 2026-05-02
related_concepts: [parameterization-selection.md, autocorrelation-inequality.md, smooth-max-approximation.md]
related_findings: [equioscillation-escape.md, optimizer-recipes.md]
cites:
  - ../concepts/parameterization-selection.md
  - ../concepts/smooth-max-approximation.md
  - ../findings/equioscillation-escape.md
  - ../problems/2-first-autocorrelation.md
  - ../problems/3-autocorrelation.md
  - ../../scripts/first_autocorrelation/peak_locking_hessian.py
---

# Peak-locking Hessian fingerprint: exp(v) vs v² at v-critical points

> **Promoted to concept** (2026-05-02): the formal mechanism is now a stand-alone concept page at [`concepts/parameterization-induced-rank-deficiency`](../concepts/parameterization-induced-rank-deficiency.md). This finding is preserved as the empirical record (test setup, raw numbers, sweep tables); the concept page is the durable WHAT-IS framing.

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

Small-instance check at $n = 80$, smooth-max $\beta = 200$, with a SOTA-like sparse seed (script: [`scripts/first_autocorrelation/peak_locking_hessian.py`](../../scripts/first_autocorrelation/peak_locking_hessian.py)). Six parameterizations from the same seed:

| $\varphi$ | $\varphi''(0)$ | $\varphi'$, $\varphi''$ at $f = 0$ | $C$ at v-critical | dead cells | near-zero Hess eigs | cond # |
|---|---:|---|---:|---:|---:|---:|
| $\exp(v)$ | $0$ (asymptote) | both vanish at $v \to -\infty$ | $1.9539951034$ | $32 / 80$ | $\mathbf{32 / 80}$ | $1.03 \times 10^5$ |
| $v^{2}$ | $\mathbf{2}$ | $\varphi' = 0$, $\varphi'' = 2$ at $v = 0$ (finite) | $\mathbf{1.7817122319}$ | $32 / 80$ | $\mathbf{0 / 80}$ | $4.55 \times 10^4$ |
| $v^{3}$ | $0$ | both vanish at $v = 0$ (finite) | $1.8107106179$ | $32 / 80$ | $\mathbf{32 / 80}$ | $6.68 \times 10^4$ |
| $v^{4}$ | $0$ | both vanish at $v = 0$ (finite) | $1.8310046542$ | $32 / 80$ | $\mathbf{32 / 80}$ | $2.40 \times 10^4$ |
| $v^{6}$ | $0$ | both vanish at $v = 0$ (finite) | $1.8846429515$ | $32 / 80$ | $\mathbf{32 / 80}$ | $4.54 \times 10^4$ |
| $U \cdot \sigma(v)$ | $0$ (at $v = 0$) | both vanish at $v \to -\infty$ AND at $v \to +\infty$ | $2.0994330845$ | $35 / 80$ + 17 saturated | $\mathbf{52 / 80}$ | $6.62 \times 10^6$ |

Three clean readings:

1. **The 1:1 dead-cell ↔ near-zero-eigenvalue correspondence holds for every $\varphi$ with $\varphi''$ vanishing at the boundary.** $\exp$, $v^3$, $v^4$, $v^6$ — all four — produce exactly 32 near-zero eigenvalues at the v-critical point, matching their 32 dead cells. The mechanism is *not* "polynomial vs transcendental" or "smooth vs $C^\infty$" — it is exactly the order at which $\varphi$ vanishes at the boundary.
2. **Basin value tracks monotonically with the vanishing order.** $v^2$ ($\varphi'' = 2$) gives the lowest C; sigmoid (vanishing at *both* boundaries, two saturation modes) gives the highest. $\exp$ and the polynomial $v^p$ family interpolate, with $C$ increasing as the boundary becomes structurally harder to reach.
3. **Sigmoid is *more* rank-deficient than exp.** The sigmoid's image is the bounded interval $(0, U)$, so v-critical points have *two* boundary saturations: $\sigma \to 0$ as $v \to -\infty$ (35 dead cells) AND $\sigma \to 1$ as $v \to +\infty$ (17 saturated cells). Both contribute rank deficiency — 52 near-zero eigenvalues total. This is the cross-problem-relevant result: P13's "sigmoid escape" (lesson #68 in [optimizer-recipes](optimizer-recipes.md)) is **not** the parameterization-rank-deficiency mechanism. Sigmoid peak-locks more aggressively than exp; P13's escape works via a different mechanism (replacing hard L-BFGS-B box walls with smooth interior gradients), not via Hessian curvature retention at the boundary.

Under `v²`, the dead cells contribute eigenvalues of order $2 \, \nabla_f C_\beta \approx 10^{-3}$, three orders of magnitude above the $10^{-6}$ near-zero threshold. Every other parameterization has those eigenvalues below $10^{-6}$.

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
- Cross-problem applicability:
  - **P3 (Second Autocorrelation)**: same Hessian fingerprint confirmed — different objective ($\max C = \|f\star f\|_2^2 / (\|f\star f\|_1 \cdot \|f\star f\|_\infty)$, sign-flipped), same sparse seed, same dead-cell count (32 / 80). $\exp$ and $v^3$ peak-lock with the 1:1 dead → near-zero correspondence; $v^2$ escapes. The mechanism is **objective-shape agnostic** — it depends only on the chain rule applied to a smooth functional with a non-negativity constraint, not on the specific functional.
  - **P4 (Third Autocorrelation)**: SOTA at $n=400$ has **0 dead cells** and admits signed $f$. The mechanism's prediction is "no parameterization-induced peak-lock because no dead-cell subspace." P4's documented escape (lesson #51 via larger-$n$ cascade) is a *distinct* mechanism — equioscillation-saturation from DOF-vs-active-constraint deficit at small $n$, not parameterization-induced Hessian rank deficiency.
  - **P9 (Uncertainty)**: **mechanism does not apply.** Variables are positive Laguerre double-roots; SOTA at $k=18$ has all gaps $\ge 0.83$ (no active ordering constraint, hence no boundary cells). P9's gap-space escape (lesson #24) works by re-coordinatizing $z_i \to g_i = z_{i+1} - z_i$, which converts a *relative* ordering constraint into an *absolute* non-negativity constraint $g_i \ge 0$. That coordinate change is the escape — a structurally different mechanism than the parameterization-curvature story here.
  - **P13 (Edges-vs-Triangles)**: **mechanism does not apply directly.** SOTA does have a sparse weight matrix (~74% zeros at $n=500\times 20$), so dead cells exist. But P13's documented sigmoid escape (lesson #68) tested on the P2 setup *peak-locks worse than exp* — sigmoid's image is the bounded interval $(0, U)$, so v-critical points have boundary saturation at both $v \to -\infty$ and $v \to +\infty$, giving more rank deficiency, not less. P13's actual escape mechanism is replacing hard L-BFGS-B box walls (which zero out gradients at the boundary) with smooth interior parameterization (which keeps gradients flowing throughout the box) — the win is *first-order* gradient flow, not *second-order* Hessian curvature.

The P9/P13 results above were the question's pre-flagged prediction and now have empirical / structural support. They sharpen the concept's "When it applies" scope.

The P2/P3 distinction from the P4 case is the key structural insight: **two different lock types need two different escapes**.

| Lock type | Diagnostic | Escape |
|---|---|---|
| Parameterization Hessian rank deficiency on dead-cell subspace | optimum has $f_i = 0$ on positive-measure $S$; $\exp(v)$ Hessian has $\#S$ near-zero eigenvalues | switch to $\varphi$ with $\varphi''(0) \neq 0$ (e.g. $v^2$) — this finding |
| Equioscillation saturation at fixed $n$ | active conv positions $\approx n$; KKT-rigid at this discretization | larger-$n$ cascade with block-repeat + perturbation (lesson #51) |

P2 had the first lock type (sparse SOTA); P4 had the second (dense Chebyshev SOTA at small $n$). Both go away under their respective escapes; neither escape works on the other's lock. The wiki had been collapsing both under "peak-locking" — they're different.
- The variational framing (Fisher–Rao vs Wasserstein-2 natural gradient flows) connects to a real literature (Amari, Otto–Villani, Carrillo et al.) and is the natural framing for promoting this finding to a publishable result. Untouched here.

## See also

- Concept: [parameterization-selection](../concepts/parameterization-selection.md) (high-level; this finding is the formal mechanism)
- Concept: [autocorrelation-inequality](../concepts/autocorrelation-inequality.md)
- Concept: [smooth-max-approximation](../concepts/smooth-max-approximation.md) (β-relaxation we use to make the Hessian well-defined)
- Finding: [equioscillation-escape](equioscillation-escape.md) lesson #94 (P2 lesson)
- Finding: [optimizer-recipes](optimizer-recipes.md) lesson #93 (parameterization swap recipe)
- Script: [`scripts/first_autocorrelation/peak_locking_hessian.py`](../../scripts/first_autocorrelation/peak_locking_hessian.py) (the verification)
