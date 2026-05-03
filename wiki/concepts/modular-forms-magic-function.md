---
type: concept
author: agent
drafted: 2026-05-02
related_problems: [P6, P9, P11, P22]
related_techniques: []
related_findings: []
cites:
  - ../source/papers/2017-goncalves-hermite-uncertainty.md
  - ../source/papers/2019-cohn-uncertainty-d12.md
  - ../source/papers/2024-cohn-li-kissing.md
  - ../source/papers/1995-wiles-fermat.md
  - ../source/papers/1990-ribet-level-lowering.md
  - ../source/papers/1987-serre-mod-representations.md
  - ../source/papers/2005-diamond-modular-forms.md
  - ../source/papers/2026-angdinata-ramanujan-tau-primes.md
  - ../personas/atiyah.md
  - ../personas/cohn.md
  - ../personas/conway.md
  - ../personas/ramanujan.md
  - ../personas/riemann.md
  - ../personas/viazovska.md
  - ../personas/wiles.md
related_personas: [atiyah.md, cohn.md, conway.md, ramanujan.md, riemann.md, viazovska.md, wiles.md]
---

# Modular Forms & Magic Functions

## TL;DR

A "magic function" is an explicit Schwartz function whose existence closes the Cohn–Elkies LP duality gap, proving sphere-packing or uncertainty bounds tight in specific dimensions. Viazovska (2016) and Cohn–Kumar–Miller–Radchenko–Viazovska (2017) constructed magic functions in `d = 8, 24` via Laplace transforms of quasimodular forms. Modular forms are the algebraic-analytic structure that makes such constructions exist precisely in the dimensions where the bound is tight.

## What it is

**Modular form** of weight `k` for `SL₂(ℤ)`: a holomorphic `f: ℍ → ℂ` (upper half-plane) with `f((aτ + b)/(cτ + d)) = (cτ + d)^k f(τ)` for all `[[a,b],[c,d]] ∈ SL₂(ℤ)`, plus growth conditions. Examples: Eisenstein series `E_k`, the discriminant `Δ`, theta series of even unimodular lattices.

**Quasimodular form**: weakens the transformation to allow polynomial corrections in `c/(cτ + d)`; includes derivatives of modular forms.

**Magic function** (sphere packing in `d`): a radial Schwartz function `f: ℝᵈ → ℝ` satisfying

- `f(x) ≤ 0` for `‖x‖ ≥ r₀` (where `r₀` is the lattice's minimum-distance threshold),
- `f̂(ξ) ≥ 0` for all `ξ`,
- `f(0) = f̂(0)` (so the Cohn–Elkies LP attains the lattice density).

For `d = 8` and `d = 24`, Viazovska / CKMRV constructed `f` as `(1 − ‖x‖²/r₀²)·g(‖x‖²)` with `g` realized as the Laplace transform of an explicit quasimodular form. The verification that `f̂ ≥ 0` reduces to positivity of a finite sum of Eisenstein series — a calculation that *succeeds* because of the modular-form algebra in those dimensions.

**Fourier interpolation**: the Cohn–Kumar–Miller–Radchenko–Viazovska 2022 follow-up shows that radial Schwartz functions are uniquely determined by `(f(√(2n)), f̂(√(2n)))` for `n ≥ 1` — a +1-style interpolation theorem that powers the magic-function construction.

## When it applies

- Sphere packing in `d ∈ {8, 24}` — Viazovska / CKMRV proven optimal.
- Uncertainty principles where the optimal bound matches a Hermite/Laguerre eigensystem (Cohn–Gonçalves 2019 for `d = 12`, see `source/papers/2019-cohn-uncertainty-d12.md`).
- Whenever you need to *prove tight* an LP bound on `ℝᵈ` whose dual variable is a positivity-constrained Schwartz function — modular-form algebra is the only known way to construct provably-positive Fourier-self-dual functions in special dimensions.

The arena does not require proving new magic functions. It requires:

- **Recognizing** when a problem reduces to evaluating known magic functions or LP duals (P6, P11, P22, P23 sphere/kissing).
- **Citing** the modular-form construction when explaining why a bound is tight in `d = 8, 24` (Leech lattice, E₈ root system).
- **Avoiding** wasted compute in dimensions where the bound is *not* known tight — modular forms are not a numerical optimizer.

## Why it works (sketch)

Cohn–Elkies primal/dual:

```
density(d) ≤ vol(B_{r₀ / 2}) · f(0) / f̂(0)
```

for any feasible Schwartz `f`. Equality requires both `f` and `f̂` vanish on the lattice's support set, and this is a strong analytic condition. Viazovska's insight: the Eisenstein series `E_4, E_6` and the cusp form `Δ` generate the modular ring; in `d = 8`, the requisite `f` is (essentially) the Laplace transform of `−E_4 / Δ + ...`, and the positivity follows from `E_4` and `E_6` being non-negative on the imaginary axis.

In dimensions `d ∉ {8, 24}` (and `d ∉ {1, 2, 3}`), no such magic function is known; the LP gap is genuine. For `d = 12`, the de Laat clustered SDP gives `κ(12) ≤ 1355` — a *bound*, not a tight constant. Modular forms are necessary but not sufficient: they exist for every dimension, but the *positivity* required by Cohn–Elkies happens only in the magic dimensions.

The general theory of modular forms (Wiles 1995 modularity for `Q`-elliptic curves, see `source/papers/1995-wiles-fermat.md`; Ribet 1990 level-lowering, `source/papers/1990-ribet-level-lowering.md`; Serre's conjecture on mod-`p` representations, `source/papers/1987-serre-mod-representations.md`) is the algebraic background. Diamond's text `source/papers/2005-diamond-modular-forms.md` is the canonical introduction.

## Classic examples

1. **Viazovska 2016** — sphere packing in `d = 8` is `π⁴ / 384` (E₈ density), proven via magic function. Extended to `d = 24` (Leech) by CKMRV 2017.
2. **Cohn–Gonçalves 2019, `d = 12` uncertainty** — `source/papers/2019-cohn-uncertainty-d12.md`. Explicit Hermite/Laguerre construction matches the LP bound. Relevant to P9 Uncertainty Principle which tests Hermite/Laguerre eigensystems.
3. **Gonçalves 2017, Hermite uncertainty** — `source/papers/2017-goncalves-hermite-uncertainty.md`. Eigenfunctions of the Fourier transform with prescribed sign changes; foundational for the d=12 result.

## Related

- Concepts: [lp-duality](lp-duality.md), [sphere-packing](sphere-packing.md), [kissing-number](kissing-number.md), [uncertainty-principle](uncertainty-principle.md).
- Techniques: (none directly — modular forms are concept-side, no production technique uses them).
- Findings: P6 strategy, P22 d=12 construction survey ([p22-d12-construction-survey](../findings/p22-d12-construction-survey.md)).
- Sources: `source/papers/2019-cohn-uncertainty-d12.md`, `source/papers/2024-cohn-li-kissing.md`, `source/papers/2017-goncalves-hermite-uncertainty.md`, `source/papers/2005-diamond-modular-forms.md`, `source/papers/1995-wiles-fermat.md`, `source/papers/1990-ribet-level-lowering.md`, `source/papers/1987-serre-mod-representations.md`, `source/papers/2026-angdinata-ramanujan-tau-primes.md`.
