---
type: concept
author: agent
drafted: 2026-05-02
related_problems: [P6]
related_techniques: [micro-perturbation-multiscale.md, parallel-tempering-sa.md]
related_findings: [perturbation-landscape.md, sa-parallel-tempering.md, float64-polish.md]
cites:
  - ../findings/perturbation-landscape.md
  - ../findings/sa-parallel-tempering.md
  - ../personas/poincare.md
related_personas: [poincare.md]
---

# Fractal Perturbation Landscape

## TL;DR

Hinge-overlap landscapes (and other piecewise-linear / kinked landscapes) are **fractal at atomic scales**: finer perturbations can have *higher* improvement rates than coarser ones (P6: 1e-13 ulp gives 0.07%/step improvement vs 1e-10 at 0.02%/step). The landscape exposes structure invisible at smooth scales. Always cascade through scales `1e-10 → 1e-12 → 1e-14` before declaring stagnation; gradient descent finds zero where stochastic perturbation finds thousands.

## What it is

For a non-smooth objective (typically piecewise-linear with kinks at active constraints), the landscape near the optimum is **not** locally quadratic. Instead, the level sets of `L` near the minimum exhibit self-similar structure across multiple scales:

- At scale `δ`, the perturbation finds improvements with rate `r(δ)` per step.
- For smooth Morse-Bott landscapes, `r(δ)` is monotone decreasing in `δ` (smaller perturbations explore less of the basin per step).
- For **fractal landscapes**, `r(δ)` is non-monotone — the rate can *increase* as `δ` shrinks, because finer scales access different geometric features.

P6 measurement: scale `1e-10` gave 0.02%, `1e-12` gave 0.10%, `1e-13` gave 0.07%. The 5× rate jump from `1e-10` → `1e-12` is counterintuitive but reproducible.

The effective "dimension" of the level set at scale `δ` increases as `δ` shrinks — there are more orthogonal descent directions at fine scale than at coarse. This is the defining feature of fractal landscapes.

## When it applies

- **Hinge-overlap and piecewise-linear losses** (P6, P22, P23). Active constraints create kinks; gradient is zero on the inactive side.
- **Sphere-packing problems near the float64 ceiling**. The basin's true math optimum is structurally rich at sub-ulp scales.
- **Constraint-rich landscapes** where small motions in the active set change the local geometry abruptly.

Recognition: gradient descent reports zero gradient and stalls. Random perturbation at coarse scale (`1e-6`–`1e-8`) finds zero improvement. Random perturbation at fine scale (`1e-10`–`1e-14`) finds many improvements.

## Why it works

The objective is a finite sum of piecewise-linear hinges. Near the optimum:

- **Coarse perturbation** (`δ ~ 1e-6`) typically activates a *new* hinge — moving into a region where the objective is locally larger. Net rejection in greedy descent.
- **Fine perturbation** (`δ ~ 1e-12`) rarely activates a new hinge but moves *along* the active constraint surface. Some directions on the surface decrease the objective via second-order or boundary effects.
- **Atomic-scale perturbation** (`δ ~ 1e-14`) explores the float64 ulp neighborhood. Some configurations have float64 representations that round to *lower* objective values via rounding-mode randomness; this is why "atomic-scale improvements" are reproducible (P6).

The combination of (a) finite-difference gradient is non-zero where analytical gradient is zero (P6 lesson #20) and (b) the level set has features at multiple scales gives the **multi-scale perturbation cascade**: try `1e-10 → 1e-12 → 1e-14` in sequence; coarser scales handle "easy" basin moves, finer scales access fractal structure.

The key companion concept is **contribution-weighted sampling** ([findings/perturbation-landscape.md](../findings/perturbation-landscape.md) lesson #18): focus perturbations on high-contribution vectors (those near the active constraint), recompute weights every ~50K iterations. Without weighting, most perturbations are wasted on already-saturated vectors.

## Classic examples

1. **P6 Kissing d=11** — atomic-scale perturbation cascade `1e-10 → 1e-12 → 1e-14`. SA parallel tempering at `1e-6` with 64 replicas + GPU fused-batch reaches 131K perturbations/sec on A100. Drove score from `1e-7` → `0.0` over a sustained polish race. See [findings/sa-parallel-tempering.md](../findings/sa-parallel-tempering.md), [findings/perturbation-landscape.md](../findings/perturbation-landscape.md).
2. **P22 Kissing d=12** — same fractal pattern, but the basin has a structural cap at 840 (see [first-order-link-tangent-test](first-order-link-tangent-test.md)). Multi-scale perturbation finds rank-2/3 squeeze improvements but cannot break the cap.
3. **Diminishing returns within basin** (P6 lesson #27): each round of SA parallel tempering finds ~50–60% less improvement than the previous (exponential decay). This indicates **basin exhaustion**, not a plateau across basins. To escape: change starting basin (different topology) or parameterization, *not* perturbation scale further.

## Related

- Concepts: [hinge-overlap](hinge-overlap.md), [kissing-number](kissing-number.md), [sphere-packing](sphere-packing.md), [smooth-max-approximation](smooth-max-approximation.md) (counter-example: smooth surrogate fails on hinge-overlap).
- Techniques: [micro-perturbation-multiscale](../techniques/micro-perturbation-multiscale.md), [parallel-tempering-sa](../techniques/parallel-tempering-sa.md).
- Findings: [perturbation-landscape](../findings/perturbation-landscape.md), [sa-parallel-tempering](../findings/sa-parallel-tempering.md), [float64-polish](../findings/float64-polish.md), [polish-race-dynamics](../findings/polish-race-dynamics.md).
