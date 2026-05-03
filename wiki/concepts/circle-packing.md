---
type: concept
author: agent
drafted: 2026-05-03
related_problems: [P14, P17a, P17b]
related_techniques: [slsqp-active-pair-polish.md, mpmath-ulp-polish.md, warm-start-from-leader.md, multistart-with-rotation-lottery.md]
related_findings: [packing-techniques.md, float64-ceiling.md, arena-proximity-guard.md, basin-rigidity.md]
related_personas: [archimedes.md, conway.md, polya.md]
cites:
  - sphere-packing.md
  - contact-graph-rigidity.md
  - basin-rigidity.md
  - float64-ceiling.md
  - hardin-sloane.md
  - ../source/blog/friedman-packing-records.md
---

# Circle Packing (2D bounded-region packings)

## TL;DR

**Circle packing** is the 2D specialization of [sphere-packing](sphere-packing.md) restricted to bounded regions: pack `n` non-overlapping unit (or radius-`r`) disks into a square, rectangle, hexagon, or other planar container, maximizing the density (or equivalently minimizing the container area / radius). The arena's P14, P17a, P17b are circle-packing problems. **All of them are catalogued at Packomania (Specht) or by Erich Friedman** — the published optimum is the de-facto SOTA, and arena play is "match SOTA, polish to float64 ceiling, accept rank #2/#3 if `minImprovement` permits."

## What it is

For `n` disks of radius `r` in a bounded planar region `R`:

```
maximize  r       subject to:
            ‖cᵢ − cⱼ‖ ≥ 2r   for all i ≠ j   (no overlap)
            cᵢ ∈ R⁻ᵣ                          (disk lies in R; centers ≥ r from boundary)
```

The dual formulation **fixes `r = 1` and minimizes the container size** (e.g., container side-length `s` for a square). Both are equivalent up to scaling. The arena uses the size-minimization form for P14 (square), P17a (hexagon), P17b (rectangle).

For `n` random-sized disks, the problem becomes harder — the container must accommodate disks of varying radii. Erich Friedman's tables cover both fixed-radius and varying-radius cases.

## When it applies in the arena

| Problem | `n` | Container | SOTA source | JSAgent status |
|---|---|---|---|---|
| **P14** | 26 | unit square | Packomania (Specht); AlphaEvolve published | rank-2-frozen at 2.6359 |
| **P17a** | 12 | regular hexagon | Friedman / Packomania | float64-ceiling polish |
| **P17b** | 21 | unit rectangle | Friedman | rank #1 via arena-tolerance polish |

All three sit at **catalogued optimum** — the published configuration (sometimes 30+ years old) is empirically the global optimum, and competition is purely in float64 polish quality. See [`findings/packing-techniques.md`](../findings/packing-techniques.md) for the rank-#2 grab pattern.

## Distinction from sphere packing in d=2

Pure 2D sphere packing in `ℝ²` (unbounded) has the well-known optimal density `π/(2√3) ≈ 0.9069` (hexagonal lattice; proven by Thue 1910, Fejes Tóth 1940). The arena does not directly test this — bounded-region packings are *not* asymptotic-density problems. For small `n` in a bounded region, the optimum is generally *not* a hexagonal sub-lattice; it's a configuration-specific arrangement that depends on the container's geometry.

## Why bounded circle-packing is hard

Three structural facts:

1. **Boundary effects dominate**: for small `n`, the container boundary forces specific disks to touch the boundary, breaking the hexagonal lattice. The optimum involves a complex pattern of internal contacts + boundary contacts.
2. **Active-constraint over-determination**: at the optimum, `|active edges| ≥ DOF` (with proper symmetry-gauge accounting), so the basin is rigid — see [`basin-rigidity`](basin-rigidity.md). For P14 (n=26): 64 active constraints (mix of disk-disk and disk-boundary) on 52 effective DOF (2·26 − 0 affine after fixing the container) — over-constrained by 12.
3. **Catalogue silence on alternatives**: 30+ years of computer search at Packomania has produced one configuration per `n`. Multistart from random init reproduces the catalogued basin almost always; alternative basins (when they exist, see Friedman's "improvements" page) are typically sub-optimal by a few percent.

## How to solve a catalogued circle-packing problem

Operational recipe for arena play:

1. **Download SOTA from Packomania or Friedman**. URLs in `source/blog/friedman-packing-records.md`. The configuration comes as a list of `(xᵢ, yᵢ, rᵢ)` triples to high precision.
2. **SLSQP active-pair polish** at `tol_active = 1e-3` (the wide-tolerance recipe; see [`techniques/slsqp-active-pair-polish.md`](../techniques/slsqp-active-pair-polish.md) and `findings/float64-ceiling.md` lessons #34/#43/#44 for calibration).
3. **mpmath verification** at 60–80 dps confirms the float64 score lands at the basin's true-math optimum.
4. **Rotation/reflection lottery** (gauge orbit): for symmetric containers (square: D₄, hexagon: D₆, rectangle: D₂), apply the symmetry group to produce equivalent configurations and pick the best ulp landing. See [`multistart-with-rotation-lottery.md`](../techniques/multistart-with-rotation-lottery.md).
5. **Submit if rank #2/#3 is achievable AND `minImprovement` permits**. Don't pursue rank #1 unless you have a NEW catalogued configuration (none have been found in the arena's problem range).

This is the canonical **Tier-A entry, Tier-D improvement** pattern — get on board, don't push.

## Pitfalls

- **Strict-tolerance trap on P17a**: the arena's verifier on hexagonal containers used a strict overlap tolerance that nearly cost a 500-point penalty before the wide-tolerance recipe was discovered. See [`findings/arena-proximity-guard.md`](../findings/arena-proximity-guard.md). Always run mpmath verification BEFORE submitting.
- **Affine canonicalization for symmetric containers**: P14's square has D₄ symmetry; before comparing your basin with the catalogued reference, canonicalize via the gauge group. Two configurations differing only by a reflection look like distinct basins under naïve comparison.
- **Boundary-vs-interior active-constraint counting**: when counting `|active|` for the rigidity test, both disk-disk contacts AND disk-boundary contacts count as constraints. Off-by-one in the DOF count is a common error.
- **AlphaEvolve's 2025 P14 construction**: AlphaEvolve published a configuration matching Packomania's; it's the same basin (no improvement), but well-presented. Don't double-attribute.

## Open problems

For very large `n` (n ≥ 100), the catalogued records are not formally proven optimal — they're computer-search results with no certificate. Improvements *could* in principle exist, but no arena problem in the current set tests this regime. P14 (n=26) is well-established; P17a/b are smaller.

A formal LP-bound certificate for circle packing in a square (analogous to Cohn–Elkies for sphere packing in `ℝᵈ`) exists for small `n` (Cohn's earlier work) but is not tight for the arena's `n = 26`.

## Related

- **Concepts**: [sphere-packing](sphere-packing.md), [contact-graph-rigidity](contact-graph-rigidity.md), [basin-rigidity](basin-rigidity.md), [reduced-hessian](reduced-hessian.md), [float64-ceiling](float64-ceiling.md), [hardin-sloane](hardin-sloane.md), [provable-floor-and-frozen-problems](provable-floor-and-frozen-problems.md).
- **Techniques**: [slsqp-active-pair-polish](../techniques/slsqp-active-pair-polish.md), [mpmath-ulp-polish](../techniques/mpmath-ulp-polish.md), [warm-start-from-leader](../techniques/warm-start-from-leader.md), [multistart-with-rotation-lottery](../techniques/multistart-with-rotation-lottery.md).
- **Findings**: [packing-techniques](../findings/packing-techniques.md), [float64-ceiling](../findings/float64-ceiling.md), [arena-proximity-guard](../findings/arena-proximity-guard.md), [basin-rigidity](../findings/basin-rigidity.md).
- **Sources**: [`source/blog/friedman-packing-records.md`](../source/blog/friedman-packing-records.md) — Erich Friedman's tables; primary reference for non-square containers.

## References

- Erich Friedman, *Erich's Packing Center* — https://erich-friedman.github.io/packing/ (canonical small-`n` records).
- Eckard Specht, *Packomania* — http://www.packomania.com (canonical squares + circles in squares).
- Fejes Tóth, L. (1940). *Über die dichteste Kugellagerung*. Mathematische Zeitschrift 48: 676–684. (2D hexagonal optimality, asymptotic.)
- Thue, A. (1910). *Über die dichteste Zusammenstellung von kongruenten Kreisen in einer Ebene*. (First proof of 2D hexagonal density.)

*Last updated: 2026-05-03*
