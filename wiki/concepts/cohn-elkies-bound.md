---
type: concept
author: agent
drafted: 2026-05-02
related_problems: [P6, P11, P22, P23]
related_techniques: [lp-cutting-plane-warmstart.md, first-order-link-tangent-test.md]
related_findings: [hinge-overlap-rank3-squeeze.md, p22-d12-construction-survey.md]
related_personas: [cohn.md, viazovska.md, conway.md, hadamard.md, atiyah.md]
cites:
  - lp-duality.md
  - sphere-packing.md
  - kissing-number.md
  - modular-forms-magic-function.md
  - ../source/papers/2024-delaat-kissing-sdp.md
  - ../source/papers/2024-cohn-li-kissing.md
---

# Cohn–Elkies LP bound (and the magic-function dual certificate)

## TL;DR

The **Cohn–Elkies bound** (Cohn–Elkies 2003) is an LP/SDP upper bound on sphere-packing densities and kissing numbers, derived from a Fourier-positivity dual that asks: *find a function `f` on `ℝ^d` whose Fourier transform `f̂` is non-negative everywhere, with `f(0) = f̂(0)`, and `f(x) ≤ 0` for `|x| ≥ 1`*. Such an `f` certifies that no sphere packing has density above a specific value. For `d = 8` and `d = 24`, Viazovska et al. (2016, 2017) constructed *exact* magic functions via modular forms, proving E₈ and Leech are the densest packings. For all other `d`, the bound is loose but tractable, and **JSAgent should compute it for any kissing-tight or sphere-packing arena problem before optimizing**.

## What it is

For sphere packing in `ℝ^d` (densest disjoint unit spheres):

> If there exists `f : ℝ^d → ℝ` such that:
> 1. `f(x) ≤ 0` for all `|x| ≥ 1`
> 2. `f̂(ξ) ≥ 0` for all `ξ ∈ ℝ^d`
> 3. `f(0) > 0` and `f̂(0) > 0`
>
> Then the sphere-packing density in dimension `d` is bounded above by:
>
> ```
> Δ(ℝ^d)  ≤  (vol(B_{1/2})) · f(0) / f̂(0)
> ```

For kissing numbers (related extremal problem): the analogous LP has `f(x) ≤ 0` for `|x| ≥ 1` AND additional positivity conditions. The bound becomes:

> ```
> κ(d)  ≤  f(0) / f̂(0)  −  1
> ```

The function `f` is the **magic function**. Cohn–Elkies showed (2003) that for `d = 8, 24` the bound is *tight* if you can find the right `f`. Viazovska 2016 found it for `d = 8` (Eisenstein-series construction), and Cohn–Kumar–Miller–Radchenko–Viazovska 2017 extended to `d = 24` (Leech).

## When it applies

- **P6 Kissing Number d=11** — JSAgent achieves κ(11) ≥ 594 (score 0.0, theoretical minimum). The Cohn–Elkies LP gives a *companion upper bound*; the gap (currently ~22% loose) tells us how much the lower bound could potentially be tightened.
- **P11 Tammes (n=50)** — adjacent problem; the LP bound on minimum angular distance complements the Hardin-Sloane lower bounds.
- **P22 Kissing d=12** — the LP bound is one of the inputs to the "8-way structural cap" analysis; combined with Levenshtein 1979 it gives the empirical κ(12) = 840 ceiling that locks our score 2.0 at the structural floor.
- **P23 Kissing d=16** — Levenshtein gives the proven κ(16) = 4320; Cohn–Elkies extension is what made that proof possible.

In general: any "place points/spheres at minimum-distance / no-overlap" arena problem has a Cohn–Elkies LP companion. **Compute it before optimizing.**

## Why it works

The Cohn–Elkies dual is a beautiful instance of LP duality applied to an *infinite-dimensional* primal (the set of all packings). The primal asks: maximize density subject to non-overlap. The dual asks: find a Fourier-positive function `f` that certifies the maximum can't exceed `f(0)/f̂(0)`. By weak LP duality, *any* feasible `f` gives a valid upper bound; tightness requires hitting the dual optimum.

The magic-function viewpoint ([modular-forms-magic-function.md](modular-forms-magic-function.md)) reveals that for special dimensions (`d = 1, 8, 24`), the dual optimum is attained by a function constructed from modular forms — explaining why the LP bound is sharp at exactly those dimensions and not others.

For non-special dimensions:
- The LP can be **discretized** (truncate to radial polynomials of degree N, solve via SDP). Modern formulations (de Laat–Leijenhorst 2024) push N to ~100, getting bounds within a few % of conjectured optima.
- The bound is **provably loose** at most `d` because no Eisenstein-style construction exists.

## Classic examples

| `d` | LP bound | Best lower bound | Status |
|---|---|---|---|
| 1 | exact (1) | trivial | tight |
| 2 | exact (π/√12) | hexagonal | tight (Thue 1910) |
| 3 | open | Kepler / FCC | LP loose, problem solved by Hales 2014 |
| 8 | **exact** | E₈ lattice | **proven optimal** (Viazovska 2016) |
| 11 | ~745 | 594 (= our P6 score) | LP bound 22% loose; gap is research subject |
| 12 | ~870 | 840 (de Laat-Leijenhorst SDP cluster) | bound + cluster combine to lock κ(12)=840 |
| 16 | 4320 | 4320 (Levenshtein 1979) | tight via LP+Cohn–Li sign-flip |
| 17–24 | various | various | tight at 24 (Leech), partial elsewhere |
| 24 | **exact** | Leech | **proven optimal** (Cohn-Kumar-Miller-Radchenko-Viazovska 2017) |

## How the agent should use it

When the council dispatches with category `kissing_number` or `sphere_packing`:

1. **Cohn persona** ([personas/cohn.md](../personas/cohn.md)) explicitly asks: *"compute the LP bound. What's the gap?"* — first action.
2. Use existing implementations: de Laat–Leijenhorst's clustered SDP (2024, [source/papers/2024-delaat-kissing-sdp.md](../../source/papers/2024-delaat-kissing-sdp.md)) is the SOTA computational machinery. For `d ≤ 24`, results are tractable on M5 Max via SDPA-GMP.
3. Compare LP bound to current arena SOTA. The gap tells you how hard the problem really is:
   - **Tight gap** → SOTA is provably optimal; pivot to a different problem.
   - **Wide gap** → room exists; LP bound is loose but the magic-function approach might exist.
4. **Viazovska persona** ([personas/viazovska.md](../personas/viazovska.md)) takes over for the magic-function search: are there special structures at this `d` that suggest a modular-form construction?
5. **Hadamard persona** ([personas/hadamard.md](../personas/hadamard.md)) — *invert the obstruction*: what would a saturating `f` have to look like? Sometimes the inversion produces a candidate construction.

For arena play specifically:

- **P6 (κ(11) ≥ 594)**: the LP says we're 22% from the optimum. *Either* there's a denser configuration we don't know (extremely unlikely after the literature search) *or* the LP bound is loose — both directions live with the gap, neither beats us at SOTA = score 0.
- **P11 (Tammes n=50)**: LP bound is essentially saturated at the Hardin-Sloane configuration. Float64-ceiling problem. ([float64-ceiling.md](float64-ceiling.md))

## Limits

- **LP relaxation is *upper* bound** — beating it on the lower-bound side requires explicit construction. Cohn–Elkies gives no construction directly; only certificates.
- **SDP discretization scales as N⁵** for naive implementations. The de Laat–Leijenhorst clustering reduces this to N³ via symmetry. Beyond N ~ 100, you need cluster-aware code or the bound stops improving.
- **The "magic function" doesn't exist generically** — only `d = 1, 8, 24` (and conjecturally `d = 4`) have exact constructions. For other `d`, you're stuck with discretized LP/SDP forever.

## Related to / distinguished from

- [`concepts/lp-duality.md`](lp-duality.md) — the general framework. Cohn–Elkies is the sphere-packing instance.
- [`concepts/modular-forms-magic-function.md`](modular-forms-magic-function.md) — the constructive companion at `d = 1, 8, 24`.
- [`concepts/sphere-packing.md`](sphere-packing.md), [`concepts/kissing-number.md`](kissing-number.md) — the *target* problems.
- [`concepts/hardy-hilbert-inequality.md`](hardy-hilbert-inequality.md) — analogous functional-analytic dual for the autocorrelation family.
- [`techniques/lp-cutting-plane-warmstart.md`](../techniques/lp-cutting-plane-warmstart.md) — the optimizer that solves the discretized LP.

## See also

- [`personas/cohn.md`](../personas/cohn.md), [`personas/viazovska.md`](../personas/viazovska.md), [`personas/conway.md`](../personas/conway.md) — the personas embodying this concept
- [`source/papers/2024-delaat-kissing-sdp.md`](../../source/papers/2024-delaat-kissing-sdp.md) — modern SDP machinery
- [`source/papers/2024-cohn-li-kissing.md`](../../source/papers/2024-cohn-li-kissing.md) — sign-flip improvements for `d ∈ [17, 21]`
- [`findings/p22-d12-construction-survey.md`](../findings/p22-d12-construction-survey.md) — concrete P22 deployment of the LP bound
