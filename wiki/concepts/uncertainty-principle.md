---
type: concept
author: agent
drafted: 2026-05-02
related_problems: [P9]
related_techniques: [gap-space-parameterization.md, k-climbing.md]
related_findings: [k-climbing.md]
cites:
  - ../source/papers/2017-goncalves-hermite-uncertainty.md
  - ../source/papers/2019-cohn-uncertainty-d12.md
  - ../personas/hilbert.md
  - bourgain-clozel-kahane.md
related_personas: [hilbert.md]
---

# Uncertainty Principle (Heisenberg / Cohn–Gonçalves)

## TL;DR

The classical Heisenberg uncertainty principle states that a function and its Fourier transform cannot both be sharply localized. Modern variants (Bourgain–Clozel–Kahane, Cohn–Gonçalves) sharpen this with sign-change and eigensystem constraints: minimize the smallest sign-change radius `r₁` of an even function `f` with `f(0), f̂(0) < 0` and `f, f̂ ≥ 0` outside `[r₁, ∞)`. Cohn–Gonçalves (2019) computed the optimum in `d = 12`. P9 is the discretized version: a Hermite/Laguerre eigensystem parameterization with `k` roots in the far cluster.

## What it is

Setup (Bourgain–Clozel–Kahane / Cohn–Gonçalves):

- **Function class**: even Schwartz `f: ℝ → ℝ` (or `ℝᵈ` radial), with `f(0) < 0`, `f̂(0) < 0`, and `f(x) ≥ 0` for `‖x‖ ≥ r₁`, `f̂(ξ) ≥ 0` for `‖ξ‖ ≥ r₂`.
- **Quantity to minimize**: the product `r₁ · r₂` (or, in normalized units, just `r₁` since one can rescale).
- **Result**: there is a positive lower bound on `r₁ · r₂`. In `d = 12`, Cohn–Gonçalves 2019 (`source/papers/2019-cohn-uncertainty-d12.md`) computed the *tight* lower bound via an explicit Hermite/Laguerre eigensystem construction.

The arena's **P9 Uncertainty Principle**: a polynomial-based discretization of this question. The function `f` is parameterized by `k` roots in a "far cluster" plus a polynomial structure; minimize a functional `S(f) ≈ r₁ · r₂` subject to the sign and Fourier-positivity constraints. The verifier checks `f`-even, `f(0) < 0`, `f̂(0) < 0`, sign distribution.

P9 is currently **HIDDEN** from the arena (verifier bug — cannot enforce constraints).

## When it applies

- Sharpened uncertainty bounds on Schwartz functions with sign restrictions.
- Sphere-packing in `d = 8, 24` (the magic-function construction is intimately tied to uncertainty: Viazovska's `f` is a "minimizer" of an uncertainty principle on the lattice support).
- Hermite/Laguerre eigensystem-based extremal problems where the function's expansion in eigenfunctions is the optimization variable.

## Why it works

Three structural facts:

1. **Hermite functions are Fourier eigenfunctions.** `H_n(x) e^{−x²/2}` is an eigenfunction of `F` with eigenvalue `(−i)^n`. So a function expanded in Hermite basis has a Fourier transform with the same expansion modulo phase. This makes "sign of `f` and `f̂` simultaneously" a tractable condition: it is the sign of `(−i)^n a_n` Hermite coefficients.
2. **Laguerre eigenfunctions for radial Fourier in `ℝᵈ`.** In `d`-dimensional radial Fourier, Laguerre polynomials play the analogous role. Cohn–Gonçalves 2019 leverages this for `d = 12`.
3. **`+1` Fourier interpolation** (Cohn–Kumar–Miller–Radchenko–Viazovska 2022): radial Schwartz functions are uniquely determined by `(f(√(2n)), f̂(√(2n)))` for `n ≥ 1`. This is the *uncertainty-principle counterpart* to the magic-function construction in d=8/24. See [modular-forms-magic-function](modular-forms-magic-function.md).

For P9, the discrete version: the polynomial expansion has `k` "free" roots in the far cluster. Increasing `k` adds DOF (see [k-climbing-and-dof-augmentation](k-climbing-and-dof-augmentation.md)) — escapes the fixed-`k` plateau by accessing previously-invisible directions. Gap-space parameterization (`g_i = z_{i+1} − z_i`, see [parameterization-selection](parameterization-selection.md)) handles the ordering constraint cleanly.

## Classic examples

1. **P9 Uncertainty Principle** — JSAgent rank #1 locally at `0.318169` via gap-space NM at `k = 14` (jumped from `k = 13` plateau at `S ≈ 0.31835`). k-climbing to `k = 15, 19, 50` showed rapidly diminishing returns. Currently HIDDEN by arena (verifier cannot enforce f-even / f̂(0) < 0). See [findings/k-climbing.md](../findings/k-climbing.md).
2. **Cohn–Gonçalves 2019 (d=12 uncertainty)** — `source/papers/2019-cohn-uncertainty-d12.md`. Tight lower bound via explicit Laguerre-eigensystem construction. Same algebraic machinery that gives Viazovska's d=8 magic function.
3. **Gonçalves 2017, Hermite uncertainty** — `source/papers/2017-goncalves-hermite-uncertainty.md`. Foundational paper on Hermite-eigenfunction extremals; the d=12 result is a direct refinement.

## Related

- Concepts: [modular-forms-magic-function](modular-forms-magic-function.md), [k-climbing-and-dof-augmentation](k-climbing-and-dof-augmentation.md), [parameterization-selection](parameterization-selection.md), [lp-duality](lp-duality.md).
- Techniques: [gap-space-parameterization](../techniques/gap-space-parameterization.md), [k-climbing](../techniques/k-climbing.md).
- Findings: [k-climbing](../findings/k-climbing.md).
- Sources: `source/papers/2017-goncalves-hermite-uncertainty.md`, `source/papers/2019-cohn-uncertainty-d12.md`.
