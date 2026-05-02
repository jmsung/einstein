---
type: concept
author: agent
drafted: 2026-05-02
related_problems: [P1, P6, P7, P11, P22, P23]
related_techniques: [lp-cutting-plane-warmstart.md, sdp-flag-algebra.md]
related_findings: [prime-number-theorem-lp.md, lp-solver-scaling.md]
cites:
  - ../source/papers/2015-tao-sieve-theory-notes.md
  - ../source/papers/2024-cohn-li-kissing.md
  - ../source/papers/2024-delaat-kissing-sdp.md
  - ../findings/prime-number-theorem-lp.md
---

# LP Duality (Certificate Machinery)

## TL;DR

Strong duality of linear programs converts a primal optimization (find the best feasible primal value) into a dual optimization (find the tightest *certified* bound). For sphere-packing and kissing-number problems, the **Cohn–Elkies LP** and its descendants produce upper bounds via Fourier positivity duality; for sieve-theoretic problems (Tao's PNT), the dual variables are the multiplier functions whose existence proves the primal is at most some value. LP duality is the certificate-issuing machinery behind every "we *proved* the bound" result in this codebase.

## What it is

A standard-form linear program

```
(P)   maximize cᵀx   subject to   Ax ≤ b,  x ≥ 0
```

has dual

```
(D)   minimize bᵀy   subject to   Aᵀy ≥ c,  y ≥ 0.
```

**Strong duality**: when both are feasible, `max (P) = min (D)`. The dual optimum `y*` is a **certificate** — its existence proves the primal cannot exceed `bᵀy*`. Three load-bearing structures arise repeatedly:

1. **Cohn–Elkies LP** (sphere-packing upper bounds in `ℝᵈ`): minimize `f(0) / f̂(0)` over Schwartz functions with `f(x) ≤ 0` for `‖x‖ ≥ 1` and `f̂(ξ) ≥ 0`. The dual is the packing density. Strong duality gives an upper bound on packing density from any *feasible* `f`. Viazovska (2016) constructed magic functions in `d = 8, 24` that achieve the optimum; Cohn–Kumar–Miller–Radchenko–Viazovska (2017) extended to Leech.
2. **Levenshtein / three-point LP** (kissing-number upper bounds): a discrete analog where positivity is enforced on Gegenbauer/spherical-harmonic coefficients. de Laat–Leijenhorst (2024) push to clustered low-rank SDPs for stronger bounds (`κ(12) ≤ 1355`, `κ(16) ≤ 7355`, etc.).
3. **Tao's sieve LP** (PNT and prime-counting bounds): a sieve weight `f(k)` is a primal LP variable; the constraint `Σ f(k) ⌊x/k⌋ ≤ 1` is a polytope; the dual exhibits the sieve identity that *proves* the bound on `Σ f(k) log(k)/k`. Solving the primal LP **is** the sieve theorist's calculation.

## When it applies

- Discrete or continuous problems whose objective is linear (or made linear by an LP relaxation) and whose constraints are convex hyperplanes/halfspaces.
- Sphere-packing / kissing-number / coding-theory bounds — any problem where a positivity-of-test-function dual is available.
- Sieve-theoretic prime-counting where the sieve weight is the primal variable.
- Extremal combinatorics where the count of induced sub-structures linearly weights the unknown density.

The LP is the right tool when:

- Cold-start cutting-plane converges slowly: warm-start from a known dual function (CHRONOS for P7).
- The constraint matrix is dense (>50%): switch from simplex to interior-point method (HiGHS IPM, lesson #47).
- The variable count is large but the binding-constraint count is small: dual sparsity makes IPM scale.

## Why it works

LP duality is a consequence of separating-hyperplane: a feasible primal point either has objective ≤ `bᵀy*` or witnesses an unbounded direction; finite primal optimum implies a separating hyperplane that becomes the dual certificate. Constructively, complementary slackness pins the active primal variables to the binding dual constraints, so `O(min(m, n))` constraints/variables are active at the optimum — sparsity that IPM exploits.

The certificate role is what distinguishes "we computed a number" from "we *proved* a number." For P6/P11/P22/P23 (sphere/kissing), the LP/SDP gives an upper bound; even if not tight, the bound is *provable* because the dual function exists and has been verified positive. This is why Viazovska's magic-function for `d = 8` rests on Cohn–Elkies duality — the magic function is the *dual variable* whose construction closes the gap to the lattice lower bound.

## Classic examples

1. **P7 Prime Number Theorem** — the problem looks like analytic number theory but is actually an LP (lesson #14, see [findings/prime-number-theorem-lp.md](../findings/prime-number-theorem-lp.md)). Variables: `f(k)` for squarefree `k ∈ [2, N]`. Constraint: `Σ f(k) ⌊x/k⌋ ≤ 1` for all integer `x`. Objective: maximize `−Σ f(k) log(k) / k`. HiGHS IPM on `N = 3350` reclaimed rank #1 at score 0.994847. Source: `source/papers/2015-tao-sieve-theory-notes.md`.
2. **P6 Kissing d=11** — the score-0 configuration (KawaiiCorgi 2026-04-10) is a *primal-feasible point* matching the Cohn–Elkies LP/SDP upper bound for κ(11) ≥ 594. The fact that this is achievable, not merely conjectured, is itself an LP certificate: a feasible 594-packing exists. Source: `source/papers/2024-cohn-li-kissing.md`.
3. **P22 / P23 Kissing d=12, d=16** — de Laat–Leijenhorst's clustered low-rank SDP gives `κ(12) ≤ 1355`, `κ(16) ≤ 7355`. P22 sits at 840 (lower bound from `P₁₂ₐ` construction); the gap to the SDP upper bound is the formal feasibility window. The first-order link-tangent test (see [first-order-link-tangent-test](first-order-link-tangent-test.md)) establishes the structural cap at 840 within this window. Source: `source/papers/2024-delaat-kissing-sdp.md`.

## Related

- Concepts: [sphere-packing](sphere-packing.md), [kissing-number](kissing-number.md), [sieve-theory-as-lp](sieve-theory-as-lp.md), [modular-forms-magic-function](modular-forms-magic-function.md), [flag-algebra](flag-algebra.md).
- Techniques: [lp-cutting-plane-warmstart](../techniques/lp-cutting-plane-warmstart.md), [sdp-flag-algebra](../techniques/sdp-flag-algebra.md).
- Findings: [prime-number-theorem-lp](../findings/prime-number-theorem-lp.md), [lp-solver-scaling](../findings/lp-solver-scaling.md).
