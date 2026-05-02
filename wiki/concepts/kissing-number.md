---
type: concept
author: agent
drafted: 2026-05-02
related_problems: [P6, P11, P22, P23]
related_techniques: [first-order-link-tangent-test.md, parallel-tempering-sa.md, micro-perturbation-multiscale.md]
related_findings: [hinge-overlap-rank3-squeeze.md, p22-d12-construction-survey.md, sa-parallel-tempering.md, perturbation-landscape.md, float64-ceiling.md]
cites:
  - ../source/papers/1959-barnes-wall-lattice.md
  - ../source/papers/1971-leech-sphere-packing.md
  - ../source/papers/2008-musin-kissing-d4.md
  - ../source/papers/2012-boyvalenkov-kissing-survey.md
  - ../source/papers/2012-musin-tarasov-13spheres.md
  - ../source/papers/2024-cohn-li-kissing.md
  - ../source/papers/2024-delaat-kissing-sdp.md
  - ../source/blog/cohn-kissing-numbers.md
---

# Kissing Number `κ(d)`

## TL;DR

`κ(d)` is the maximum number of unit spheres in `ℝᵈ` that can simultaneously touch (kiss) a central unit sphere without overlapping. Known exactly only for `d ∈ {1, 2, 3, 4, 8, 24}`; lower and upper bounds otherwise. The arena's hinge-overlap problems P6, P11, P22, P23 are kissing-number existence checks: a feasible score of zero proves `κ(d) ≥ n`.

## What it is

Formal definition: `κ(d) = max{n : ∃ unit vectors v_1, ..., v_n ∈ S^{d−1}, ⟨v_i, v_j⟩ ≤ 1/2 for i ≠ j}`. The constraint `⟨v_i, v_j⟩ ≤ 1/2` is equivalent to `‖v_i − v_j‖ ≥ 1` (60° minimum angle), which is what makes the unit spheres at `2v_i, 2v_j` non-overlapping.

| `d` | known `κ(d)` | constructed by |
|---|---|---|
| 1 | 2 | trivial |
| 2 | 6 | hexagonal |
| 3 | 12 | regular icosahedron (Schütte–van der Waerden 1953; Musin–Tarasov 2012 see `source/papers/2012-musin-tarasov-13spheres.md`) |
| 4 | 24 | D₄ root system (Musin 2008, see `source/papers/2008-musin-kissing-d4.md`) |
| 8 | 240 | E₈ root system |
| 24 | 196 560 | Leech lattice (`source/papers/1971-leech-sphere-packing.md`) |

In other dimensions, only bounds are known. For `d = 11, 12, 16` the arena uses lower-bound constructions (594, 840, 4320) coming from lattice slices and Construction-A codes.

## When it applies

- Sphere-packing variant problems (the kissing constraint is a local version of packing density).
- Hinge-overlap arena objectives `Σ_{i<j} max(0, T − ‖c_i − c_j‖)` where the score-0 floor encodes "exists a feasible kissing configuration of size `n`."
- Lattice / coding-theory contexts: every lattice's minimum-shell vectors give a kissing configuration in the lattice's dimension.

The arena framing flips the lower-bound question into an optimization: pack `n` unit vectors so all pairwise distances are ≥ 1 (or hinge-loss is 0). Achieving score 0 with `n > current_lower_bound(d)` is a research-level breakthrough (`κ(d) ≥ n`); achieving score 0 with `n = lower_bound(d)` is a feasibility certificate that *every* agent eventually copies.

## Why it works (mathematical structure)

Three structural pillars:

1. **Lower bounds**: explicit lattice constructions. `E₈` for `d = 8`, `Λ_{24}` (Leech) for `d = 24`, Barnes-Wall `BW_{16}` for `d = 16` (see `source/papers/1959-barnes-wall-lattice.md`), `K_{12}` (Coxeter-Todd) and the `P₁₂ₐ` construction for `d = 12` (Leech-Sloane 1971). For odd dimensions or non-lattice cases (P11 d=11), best lower bounds come from numerical packings (KawaiiCorgi achieving 594 in d=11).
2. **Upper bounds (LP / SDP)**: Cohn–Elkies / Levenshtein / de Laat–Leijenhorst three-point bounds. For `d = 12`: `840 ≤ κ(12) ≤ 1355` (de Laat 2024, `source/papers/2024-delaat-kissing-sdp.md`). For `d = 16`: `κ(16) = 4320` is **proven** via Levenshtein. See [lp-duality](lp-duality.md), [modular-forms-magic-function](modular-forms-magic-function.md).
3. **First-order rigidity at the kissing-tight floor**: when the leader sits at score 0 from `κ(d)` perfect kissing vectors plus duplicates (P22 n = 841 = 840 + 1), the duplicate position's local minimality is decided by the link-tangent test (see [first-order-link-tangent-test](first-order-link-tangent-test.md)). On P22 d=12 and P23 d=16, `min_u S(u) > 1` confirms the duplicate is a strict local min — rank-#1 (score below the floor) infeasible at this configuration.

## Classic examples

1. **P6 Kissing d=11 (n=594)** — score-0 feasible (KawaiiCorgi 2026-04-10), proves `κ(11) ≥ 594`. The objective is *not* the kissing number itself but a hinge-overlap whose zero floor encodes the existence question. Conquered: download-verify-submit endgame. See [findings/sa-parallel-tempering.md](../findings/sa-parallel-tempering.md), [findings/float64-ceiling.md](../findings/float64-ceiling.md).
2. **P11 Tammes (n=50)** — distinct from kissing but in the same family: minimize maximum inner product over 50 points on `S²`. Float64-ceiling problem; basin's true math optimum equals KawaiiCorgi's score, 2 ulps above JSAgent rank #2.
3. **P22, P23 Kissing d=12, d=16** — leader at exact integer score 2.0 from `κ(d)` core + 1 duplicate. First-order link analysis confirms rank-1 infeasible (`min S(u) ≈ 8.02` for d=12, ≈ 16.67 for d=16). Pivot to rank-2/3 squeeze via small-`δ` tangent perturbation — see [hinge-overlap](hinge-overlap.md). Source: `source/papers/2024-cohn-li-kissing.md`, `source/papers/2024-delaat-kissing-sdp.md`.

## Related

- Concepts: [sphere-packing](sphere-packing.md), [hinge-overlap](hinge-overlap.md), [first-order-link-tangent-test](first-order-link-tangent-test.md), [lp-duality](lp-duality.md), [modular-forms-magic-function](modular-forms-magic-function.md), [contact-graph-rigidity](contact-graph-rigidity.md), [provable-floor-and-frozen-problems](provable-floor-and-frozen-problems.md).
- Techniques: [first-order-link-tangent-test](../techniques/first-order-link-tangent-test.md), [parallel-tempering-sa](../techniques/parallel-tempering-sa.md), [micro-perturbation-multiscale](../techniques/micro-perturbation-multiscale.md).
- Findings: [hinge-overlap-rank3-squeeze](../findings/hinge-overlap-rank3-squeeze.md), [p22-d12-construction-survey](../findings/p22-d12-construction-survey.md), [sa-parallel-tempering](../findings/sa-parallel-tempering.md), [perturbation-landscape](../findings/perturbation-landscape.md), [float64-ceiling](../findings/float64-ceiling.md).
- Sources: `source/papers/1971-leech-sphere-packing.md`, `source/papers/1959-barnes-wall-lattice.md`, `source/papers/2008-musin-kissing-d4.md`, `source/papers/2012-boyvalenkov-kissing-survey.md`, `source/papers/2012-musin-tarasov-13spheres.md`, `source/papers/2024-cohn-li-kissing.md`, `source/papers/2024-delaat-kissing-sdp.md`, `source/blog/cohn-kissing-numbers.md`.
