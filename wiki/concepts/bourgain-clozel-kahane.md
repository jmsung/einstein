---
type: concept
author: agent
drafted: 2026-05-02
related_problems: [P9, P18, P22, P23]
related_techniques: [k-climbing.md, gap-space-parameterization.md]
related_findings: [k-climbing.md, verification-patterns.md]
related_personas: [cohn.md, viazovska.md, hilbert.md, hardy.md]
cites:
  - uncertainty-principle.md
  - cohn-elkies-bound.md
  - modular-forms-magic-function.md
  - lp-duality.md
  - ../source/papers/2017-goncalves-hermite-uncertainty.md
  - ../source/papers/2019-cohn-uncertainty-d12.md
---

# Bourgain–Clozel–Kahane sign-uncertainty principle

## TL;DR

The **Bourgain–Clozel–Kahane (BCK 2010) sign-uncertainty principle** says: any sufficiently nice even function `f : ℝᵈ → ℝ` whose Fourier transform `f̂` is also "negative at the origin and eventually positive" cannot have its first sign-change `r₁` and `f̂`'s first sign-change `r₂` both arbitrarily small — there is a positive universal lower bound on `r₁ · r₂`. This is the analytic backbone of P9 (and would-be P18) in the arena. Sharp constants are known **only** in `d = 1` (BCK 2010) and `d = 12` (Cohn–Gonçalves 2019, via Eisenstein series `E₆`). Every other dimension is open. **Any P9 score below `0.2025` is an evaluator artifact, not a real improvement** — the BCK lower bound rules it out.

## What it is

Fix `d ≥ 1`. Let `𝒜₊(d)` be the class of integrable, even functions `f : ℝᵈ → ℝ` whose Fourier transform `f̂` is also integrable, with:

- `f(0) ≤ 0` and `f̂(0) ≤ 0`,
- `f(x) ≥ 0` for `|x| ≥ r₁`,
- `f̂(ξ) ≥ 0` for `|ξ| ≥ r₂`.

(Functions in `𝒜₊` are "double-negative-at-origin, eventually positive on both sides of Fourier.") Define

```
A₊(d)  =  inf  { r₁ · r₂  :  f ∈ 𝒜₊(d), f ≢ 0 }.
```

The companion class `𝒜₋(d)` flips the signs at the origin: `f(0) ≥ 0`, `f̂(0) ≥ 0`, eventually negative outside `r₁` / `r₂`. Define `A₋(d)` analogously.

**BCK's theorem** (Bourgain–Clozel–Kahane 2010, *Annales de l'Institut Fourier* 60(4): 1215–1232):

```
A₊(d)  >  0   and   A₋(d)  >  0,    for every d ≥ 1.
```

That is, the sign-uncertainty problem has a **strictly positive lower bound**. The proof is non-constructive in general, but BCK gave the first explicit estimate in `d = 1`: `A₊(1) ≥ 0.45`. (Subsequently sharpened by Gonçalves–Oliveira–Silva–Steinerberger 2017 to `0.45 ≤ A₊(1) ≤ 0.594`; sharp constant in `d = 1` still open as of 2026.)

## Sharp constants known

| Dimension | Sharp value of `A₊(d)` | Achieved by | How proven |
|---|---|---|---|
| `d = 1` | conjecturally `≈ 0.572`; proven `[0.45, 0.594]` | open | BCK 2010 + Gonçalves–Oliveira–Silva–Steinerberger 2017 |
| `d = 12` | `A₊(12) = √2` (so `r₁·r₂ ≥ 2`) | weight-6 Eisenstein-series Poincaré construction | Cohn–Gonçalves 2019, *Inventiones* 217 |
| all other `d` | open | open | only existence (BCK 2010) |

The `d = 12` sharp result is the *only* fully-resolved case in any dimension. It uses the same modular-form machinery (weight-6 Eisenstein `E₆`, Poincaré series on `SL₂(ℤ)`) that powers Viazovska's `d = 8` sphere-packing magic function. The deeper reason `d = 12` is special: `E₆` produces a self-Fourier eigenfunction with the right sign structure; no analogous identity is known in adjacent dimensions.

## Why it matters

1. **Lower bound on P9 / P18 scores.** Arena P9 (and the now-merged P18) discretizes the sign-uncertainty problem. The BCK + Cohn–Gonçalves bounds give the *floor* below which no real score can land. Specifically, with the arena's normalization the lower bound is `0.2025` and the upper bound (Cohn–de Laat–Gonçalves, unpublished) is `0.3102`. **Any reported score below `0.2025` is a verifier artifact** — see [`findings/verification-patterns.md`](../findings/verification-patterns.md) for the P9 incident where a score of `1.07e-13` was celebrated before discovering it violated the BCK bound.
2. **Same machinery as Cohn–Elkies.** The BCK auxiliary function (an `f` with prescribed sign behavior on `f` and `f̂`) is structurally identical to the Cohn–Elkies sphere-packing certificate. The Cohn–Gonçalves 2019 paper makes this explicit: the same modular-form duality that produces the sharp `d = 12` sign-uncertainty bound also feeds the Cohn–Elkies LP bound for sphere packing. See [`cohn-elkies-bound`](cohn-elkies-bound.md) and [`modular-forms-magic-function`](modular-forms-magic-function.md).
3. **Circumstantial evidence for `κ(12) = 840`.** The existence of a sharp modular-form proof in `d = 12` — and in *no other dimension* between 1 and 23 — is the deepest known structural fact about dimension 12. It underpins the conjecture that `κ(12) = 840` is tight (achieved by `P₁₂ₐ`) rather than the LP/SDP upper bound `1355` (de Laat–Leijenhorst 2024). See [`findings/structural-cap-at-score-2-meta.md`](../findings/structural-cap-at-score-2-meta.md) and [`findings/p22-d12-construction-survey.md`](../findings/p22-d12-construction-survey.md).
4. **Extremizer structure: infinitely many double roots.** Gonçalves–Oliveira–Silva–Steinerberger 2017 proved that any `d = 1` extremizer has infinitely many *tangent* (double) zeros. This is a structural constraint any arena-feasible candidate must asymptotically respect — finite-root candidates are necessarily suboptimal in the limit.

## Why it works

Three ingredients underlie the BCK theorem:

1. **Self-Fourier ansatz**. Restricting to `f = f̂` (eigenfunctions of `F` with eigenvalue `+1`) halves the constraint set. Hermite functions `H_n(x) e^{−x²/2}` for `n ≡ 0 (mod 4)` are the basis. This is what makes the LP/SDP relaxations tractable.
2. **Hermite-eigenfunction expansion**. Even Schwartz functions on `ℝ` expand uniquely in `{H_{2k}(x) e^{−x²/2}}_{k ≥ 0}`. The Fourier transform multiplies the `k`-th coefficient by `(−1)^k` (since `F H_{2k} = (−1)^k H_{2k}` after Hermite normalization). Thus "sign of `f` at infinity" + "sign of `f̂` at infinity" become two linear constraints on the coefficient vector.
3. **Equidistribution / torus-flow structure** (Gonçalves–Oliveira–Silva–Steinerberger 2017). For fixed `x`, `H_n(x)` traces a quasi-periodic orbit on a torus as `n → ∞`. Equidistribution arguments give effective bounds. This is the technical heart of the 1D constant-sharpening from `0.41` to `0.45`.

For `d = 12` specifically (Cohn–Gonçalves 2019): replace Hermite with **Laguerre eigenfunctions** for radial Fourier in `ℝᵈ`, then construct the extremizer as a weight-6 Poincaré series over `SL₂(ℤ)`. Optimality follows from the Eisenstein-series identity `E₆² − E₄³ = ...` (the same one Viazovska uses for `d = 8`).

## Relation to Cohn–Elkies LP

The BCK auxiliary function `f` with prescribed sign behavior is essentially the **dual variable** of an LP relaxation. The LP is:

```
minimize    r₁ · r₂
subject to  f(0) ≤ 0,        f̂(0) ≤ 0,
            f(x) ≥ 0 for |x| ≥ r₁,
            f̂(ξ) ≥ 0 for |ξ| ≥ r₂,
            f even, f ∈ L¹(ℝᵈ), f̂ ∈ L¹(ℝᵈ).
```

The dual would-be Cohn–Elkies-style: maximize a packing density subject to a "magic function" constraint. The **same modular-form construction saturates both** in `d = 8, 12, 24` — that's why Viazovska's 2016 `d = 8` packing proof and Cohn–Gonçalves 2019 `d = 12` uncertainty proof share so much machinery. See [`modular-forms-magic-function`](modular-forms-magic-function.md).

## When it applies in the arena

| Problem | Relation to BCK | Status |
|---|---|---|
| **P9 Uncertainty Principle** | direct discretization (Hermite/Laguerre eigensystem with `k` far-cluster roots) | rank #1 locally `0.318169` (gap-space NM at `k=14`); HIDDEN (verifier bug) |
| **P18 Uncertainty** (merged with P9) | same arena slot, divergent tracking history | HIDDEN; same theoretical floor `0.2025` |
| **P22 Kissing d=12** | structural / circumstantial — `d=12` modular-form machinery | rank #3 at `2.0014`, the 840 cap is *conjecturally* tight via this connection |
| **P23 Kissing d=16** | adjacent (no sharp BCK in `d=16`) | rank #2 at `2.0000027`; the structural floor is `2.0` |

**Operational rule for P9 / P18**: any score below `0.2025` triggers a verifier audit *before* any celebration. The BCK lower bound is the closed-form sanity check. (See lesson #69 in `findings/verification-patterns.md`.)

## Pitfalls

- **Confusing `A₊` with `A₋`**. The two classes (sign at origin) give *different* constants. P9 uses the `+1` flavor (`f(0), f̂(0) < 0` then eventually positive). Mixing them produces misleading bounds.
- **Confusing dimension index**. The "`d = 1` BCK constant" is an unrelated number from the "`d = 12` Cohn–Gonçalves constant." When a paper says "the BCK bound", check which dimension is meant. The arena P9 is `d = 12` (since the score is normalized accordingly).
- **Non-constructive existence**. BCK 2010 *proves* `A₊(d) > 0` but the proof is non-constructive in general dimensions. The 1D and 12D sharp values are the only constructive ones. Treating BCK as a "sharp bound generator" for arbitrary `d` is a category error.
- **Verifier–theory mismatch**. The arena P9 verifier (as of 2026-04-19) does *not* enforce `f(0) < 0` and `f̂(0) < 0` constraints. This makes scores below the BCK floor numerically reachable but mathematically meaningless. The verifier-fix is tracked at GitHub issue #51; until resolved, P9 is hidden. See [`findings/verification-patterns.md`](../findings/verification-patterns.md).

## Open problems

- Sharp constant `A₊(1)` (current `[0.45, 0.594]`).
- Sharp constants in `d ∈ {2, …, 11, 13, …, 23}` — none known.
- Tight upper bound `A₊(12) ≤ √2 + ε` (current `√2`, conjecturally tight).
- Effective rate of convergence for non-extremal functions (no known result).

## Related

- **Concepts**: [uncertainty-principle](uncertainty-principle.md), [cohn-elkies-bound](cohn-elkies-bound.md), [modular-forms-magic-function](modular-forms-magic-function.md), [lp-duality](lp-duality.md).
- **Techniques**: [k-climbing](../techniques/k-climbing.md), [gap-space-parameterization](../techniques/gap-space-parameterization.md).
- **Findings**: [k-climbing](../findings/k-climbing.md), [verification-patterns](../findings/verification-patterns.md), [structural-cap-at-score-2-meta](../findings/structural-cap-at-score-2-meta.md), [p22-d12-construction-survey](../findings/p22-d12-construction-survey.md).
- **Sources**: [`source/papers/2017-goncalves-hermite-uncertainty.md`](../../source/papers/2017-goncalves-hermite-uncertainty.md), [`source/papers/2019-cohn-uncertainty-d12.md`](../../source/papers/2019-cohn-uncertainty-d12.md).

## References

- Bourgain, J., Clozel, L. & Kahane, J.-P. (2010). *Principe d'Heisenberg et fonctions positives.* Annales de l'Institut Fourier 60(4): 1215–1232. (Original existence theorem; explicit `d = 1` lower bound `0.41`.)
- Gonçalves, F., Oliveira e Silva, D. & Steinerberger, S. (2017). *Hermite Polynomials, Linear Flows on the Torus, and an Uncertainty Principle for Roots.* J. Math. Anal. Appl. 451(2): 678–711. arXiv:1602.03366. (`d = 1` sharpened to `[0.45, 0.594]`; double-root extremizer structure.)
- Cohn, H. & Gonçalves, F. (2019). *An optimal uncertainty principle in twelve dimensions via modular forms.* Inventiones Mathematicae 217: 799–831. arXiv:1712.04438. (Sharp `d = 12` constant via Eisenstein-series `E₆`.)
- Viazovska, M. (2017). *The sphere packing problem in dimension 8.* Annals of Mathematics 185(3): 991–1015. (Companion `d = 8` sphere-packing proof using related modular-form construction.)

*Last updated: 2026-05-02*
