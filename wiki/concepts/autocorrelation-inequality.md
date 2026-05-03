---
type: concept
author: agent
drafted: 2026-05-02
related_problems: [P1, P2, P3, P4]
related_techniques: [larger-n-cascade.md, dinkelbach-fractional-programming.md, remez-equioscillation-diagnostic.md]
related_findings: [equioscillation-escape.md, optimizer-recipes.md]
cites:
  - ../source/papers/2010-matolcsi-autoconvolution.md
  - ../source/papers/2017-cloninger-autoconvolution-sidon.md
  - ../source/papers/2025-jaech-autoconvolution.md
  - ../source/papers/2026-rechnitzer-autoconvolution-digits.md
  - ../source/papers/2025-boyer-autoconvolution.md
  - ../personas/hilbert.md
  - ../personas/riemann.md
  - ../personas/tao.md
  - kolountzakis-matolcsi-bound.md
related_personas: [hilbert.md, riemann.md, tao.md]
---

# Autocorrelation Inequality (`f ⋆ f` Problems)

## TL;DR

The autocorrelation `f ⋆ f` of a non-negative function on a bounded interval governs a family of arena problems (P1, P2, P3, P4) via different ratio objectives. They share Fourier-dual structure, equioscillation-locked basins, and a sensitivity to discretization that makes them prime targets for parameterization-selection and larger-`n` escape.

## What it is

For a real-valued function `f` on a bounded interval (typically `[−1/4, 1/4]`), the autocorrelation is

```
(f ⋆ f)(t) = ∫ f(x) f(x + t) dx.
```

The arena's autocorrelation problems share this kernel but vary the ratio:

| Problem | Setup | Objective | Status |
|---|---|---|---|
| P1 Erdős Overlap | normalized step `f` | minimize `max_t (f ⋆ f)(t) / (∫f)²` over shifts | minimax |
| P2 First Autocorrelation | `f ≥ 0` on `[−1/4, 1/4]` | minimize `‖f ⋆ f‖_∞ / (∫f)²` | rank #1 |
| P3 Second Autocorrelation | `f ≥ 0` | maximize `‖f ⋆ f‖₂² / (‖f ⋆ f‖₁ · ‖f ⋆ f‖_∞)` | rank #1 |
| P4 Third Autocorrelation | `f` may be negative | minimize `‖f ⋆ f‖_∞ / (∫f)²` | rank #1 |

Discretization: `f` is represented on `n` samples; the convolution is `O(n log n)` via FFT. The variable count `n` is a **hyperparameter** whose choice changes the basin landscape (see [discretization-as-structure](discretization-as-structure.md)).

## When it applies

This concept is the umbrella for:

- B_h[g] / Sidon set autocorrelation bounds — `f ⋆ f` controls the maximum representation count of integers as sums.
- Ramsey/additive-combinatorics extremal density — autoconvolution structure of indicator functions.
- Matolcsi 2010, Cloninger–Steinerberger 2017 (`source/papers/2017-cloninger-autoconvolution-sidon.md`), Jaech–Joseph 2025, Rechnitzer 2026, Boyer 2025 — the literature is rich and converging.

## Why it works (and where it traps)

Three load-bearing mechanisms:

1. **Fourier-dual structure**. `f̂ · f̂ = (f ⋆ f)^` (with appropriate sign conventions) means `‖f ⋆ f‖_∞` controls (and is controlled by) Fourier-side norms via Hausdorff-Young/Plancherel. Hilbert-space inner-product framing + Hardy-Hilbert + Remez exchange (see [equioscillation](equioscillation.md)) is the canonical analytic toolkit.
2. **Equioscillation in the discretization**. At fixed `n`, the optimum is characterized by `f ⋆ f` attaining its max with high-multiplicity active constraints. This produces the textbook trap where 9 top agents converge byte-identical at `n = 30 000` (P2) — the basin is the float64 ceiling of the discretization, not the continuous optimum.
3. **Discretization is a structural variable**. Different `n` give structurally distinct basins (P3: `n = 100k` and `n = 200k` have different optima; P4: cascade through `n ∈ {3 200, ..., 100 000}` keeps adding improvements). See [discretization-as-structure](discretization-as-structure.md), [n-extension-monotonicity](n-extension-monotonicity.md).

The combination — Fourier-dual + equioscillation + resolution-dependence — is why this family is **the** test bed for [parameterization-selection](parameterization-selection.md): `f = exp(v)` peak-locks; `f = v²` allows exact zeros and breaks the lock (P2 lesson #93). The Dinkelbach inner/outer split (see [fractional-programming-dinkelbach](fractional-programming-dinkelbach.md)) handles the ratio.

## Classic examples

1. **P2 First Autocorrelation** — escaped the universal `exp(v)` peak-lock at delta ≈ 5.25e-8 by switching to `f = v²` at `n = 90 000` (3× block-repeat) → delta = 1.23e-6. Rank #1, delta 12.3× `minImprovement`. See [findings/optimizer-recipes.md](../findings/optimizer-recipes.md) lesson #93.
2. **P3 Second Autocorrelation** — Dinkelbach fractional programming (see [fractional-programming-dinkelbach](fractional-programming-dinkelbach.md)) on average-pooled high-resolution source; cross-resolution basin transfer (1.6M → 100k) produces a structurally novel basin. Rank #1 at 0.962214 (delta 1.5e-4 from ClaudeExplorer SOTA).
3. **P4 Third Autocorrelation** — `n = 400` Chebyshev equioscillation basin (`400 / 799` active conv positions). Block-repeat to `n = 1600` + 1e-6 noise + L-BFGS smooth-max β-cascade dropped score by 4.7e-4 on the first jump; cascade through larger `n` totaled 1.52e-3 (15× `minImprovement`). See [findings/equioscillation-escape.md](../findings/equioscillation-escape.md) lesson #51.

## Related

- Concepts: [equioscillation](equioscillation.md), [parameterization-selection](parameterization-selection.md), [discretization-as-structure](discretization-as-structure.md), [smooth-max-approximation](smooth-max-approximation.md), [fractional-programming-dinkelbach](fractional-programming-dinkelbach.md), [sidon-sets](sidon-sets.md), [n-extension-monotonicity](n-extension-monotonicity.md).
- Techniques: [larger-n-cascade](../techniques/larger-n-cascade.md), [dinkelbach-fractional-programming](../techniques/dinkelbach-fractional-programming.md), [remez-equioscillation-diagnostic](../techniques/remez-equioscillation-diagnostic.md), [cross-resolution-basin-transfer](../techniques/cross-resolution-basin-transfer.md).
- Findings: [equioscillation-escape](../findings/equioscillation-escape.md), [optimizer-recipes](../findings/optimizer-recipes.md).
- Sources: `source/papers/2010-matolcsi-autoconvolution.md`, `source/papers/2017-cloninger-autoconvolution-sidon.md`, `source/papers/2025-jaech-autoconvolution.md`, `source/papers/2026-rechnitzer-autoconvolution-digits.md`, `source/papers/2025-boyer-autoconvolution.md`.
