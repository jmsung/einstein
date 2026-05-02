---
type: concept
author: agent
drafted: 2026-05-02
related_problems: [P2, P11, P14, P17a, P17b]
related_techniques: [mpmath-ulp-polish.md, slsqp-active-pair-polish.md, multistart-with-rotation-lottery.md]
related_findings: [float64-ceiling.md, packing-techniques.md, basin-rigidity.md]
cites:
  - ../findings/float64-ceiling.md
  - ../findings/basin-rigidity.md
---

# Float64 Ceiling

## TL;DR

A **float64 ceiling** is the basin's true-math optimum rounded to IEEE-754 double precision. When all top agents converge to the same configuration up to ulps, the basin is mathematically rigid (see [basin-rigidity](basin-rigidity.md)) and the *score* is at its float64 representation. mpmath at 50–120 dps confirms this empirically; further "improvements" in float64 are noise. Triple-verify before claiming any sub-ulp win — float64 zero is not mpmath zero.

## What it is

For a constrained optimization with optimum `s* ∈ ℝ`, the **float64 ceiling** is `s_64 = round_64(s*)`, the nearest IEEE-754 double. When the basin is rigid (active constraints saturate the DOF) and the underlying math has a unique optimum, every polisher with sufficient precision reaches `s_64` modulo ulps.

Operational signs:

- **All top agents within 1–2 ulps**. Score differences in the 7th+ decimal digit only.
- **mpmath at 80 dps** finds the basin's true-math optimum and confirms it rounds to `s_64`.
- **Probability of beating `s_64` by `k` ulps** (random rotation lottery): `~(1/4)^{Mk}` where `M` is the number of active pair constraints. For Tammes n=50 with `M = 1225`, `k = 2` has probability `~10^{-61}`.

When the arena's verifier is *also* float64, the basin's float64 score is genuinely unbeatable. When the verifier is upgraded to mpmath (P6 lesson #73 — silent verifier shift overnight), candidates whose "score = 0.0" in float64 re-score as `7.7e-13` in mpmath: the float64 zero was a mirage, the polish "improvements" were degrading the true objective.

## When it applies

- **Geometric packings** with active-pair contact graph (P11, P14, P17a, P17b).
- **Sphere codes** with rigid contact graph (P11 Tammes).
- **Discretized-function problems** at the byte-identical SOTA (P2 — 8 frontier-model agents submit byte-identical solutions hash `19fdb2925f5f9024`, the float64 floor of a published step-function construction).

Recognition: hash the top-K solutions' raw bytes (after rounding to a canonical form). Byte-identical = same float64 floor. Different bytes but same score to 7+ digits = same basin, different polish quality.

## Why it works

Three facts:

1. **The basin's true-math optimum exists and is unique** when the configuration is rigid (proven via mpmath KKT solve at sufficient precision).
2. **Float64 representation has discrete granularity** ~2.22e-16 relative. Around the basin floor, the function is approximately quadratic; small perturbations move the value in ulp-sized chunks.
3. **Different polishers find different float64 *values* for the same true-math configuration**. Iterations differ in the order of floating-point operations, accumulating in ulp-direction fluctuations. The set of achievable float64 values is finite; the lowest is the "true" float64 ceiling.

This is why the **rotation lottery** technique works on Tammes/Kissing: the basin's true-math optimum is invariant under `SO(d)`, but rotating the polished configuration and re-evaluating in float64 picks a different point in the ulp-cloud. A small fraction (~4% for Tammes n=50) lands exactly at the basin's float64 ceiling.

The proving-impossibility protocol (from [findings/float64-ceiling.md](../findings/float64-ceiling.md)):

1. Check for an external reference database (Hardin-Sloane, Packomania) — confirm same basin.
2. mpmath at 80 dps to find the basin's true math optimum.
3. Probability calculation `(1/4)^{Mk}` for beating the leader by `k` ulps.
4. Massive ulp lottery (1M+ rotations × permutations × reflections) with the arena evaluator.

If all four confirm the ceiling, declare rank #1 mathematically impossible.

## Classic examples

1. **P11 Tammes (n=50)** — JSAgent rank #2 at `0.513472084680564`, 2 ulps below KawaiiCorgi #1. Hardin-Sloane reference confirms same basin. mpmath 80-digit polish confirms the basin floor matches KawaiiCorgi to all printed digits. See [findings/float64-ceiling.md](../findings/float64-ceiling.md).
2. **P14 Circle Packing in Square (n=26)** — 30-year Packomania-known-optimal. Top agents differ by 1 ulp; AlphaEvolve #1 sits at the basin float64 ceiling.
3. **P2 First Autocorrelation byte-identical SOTA** — 8 different frontier-model agents submitted *byte-identical* `data.values` (sha256 `19fdb2925f5f9024`). When N independent agents converge to byte-identical solutions, the collective optimum is the basin's float64 ceiling of a known published construction. Same lesson: from-scratch optimization at the same `n` cannot beat it without (a) structurally different algorithm, (b) higher resolution, or (c) different mathematical formulation.

## Related

- Concepts: [basin-rigidity](basin-rigidity.md), [contact-graph-rigidity](contact-graph-rigidity.md), [arena-tolerance-drift](arena-tolerance-drift.md), [provable-floor-and-frozen-problems](provable-floor-and-frozen-problems.md), [warm-start-dynamics](warm-start-dynamics.md).
- Techniques: [mpmath-ulp-polish](../techniques/mpmath-ulp-polish.md), [slsqp-active-pair-polish](../techniques/slsqp-active-pair-polish.md), [multistart-with-rotation-lottery](../techniques/multistart-with-rotation-lottery.md).
- Findings: [float64-ceiling](../findings/float64-ceiling.md), [packing-techniques](../findings/packing-techniques.md), [basin-rigidity](../findings/basin-rigidity.md).
