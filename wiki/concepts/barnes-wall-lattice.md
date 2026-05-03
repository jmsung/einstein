---
type: concept
author: agent
drafted: 2026-05-02
related_problems: [P23, P22]
related_techniques: [first-order-link-tangent-test.md]
related_findings: [structural-cap-at-score-2-meta.md, p22-d12-construction-survey.md, hinge-overlap-rank3-squeeze.md]
related_personas: [conway.md, viazovska.md, cohn.md, ramanujan.md]
cites:
  - sphere-packing.md
  - kissing-number.md
  - cohn-elkies-bound.md
  - coxeter-todd-k12.md
  - modular-forms-magic-function.md
  - ../source/papers/1959-barnes-wall-lattice.md
  - ../source/papers/2024-cohn-li-kissing.md
---

# Barnes–Wall lattice family BW_n

## TL;DR

The **Barnes–Wall lattices** `BW_n` (Barnes & Wall 1959) are an infinite family of integer lattices in dimensions `n = 2^k` with extremal-density properties. **`BW_{16}` is the foundation of P23's κ(16) = 4320 construction** (Levenshtein 1979; proven optimal). The family has tight modular-form connections (theta series), close ties to the Reed–Muller error-correcting codes, and is the second-most-special infinite lattice family after the Eisenstein-rooted lattices culminating in Leech.

## What it is

`BW_n` for `n = 2^k` is built recursively from the binary Reed-Muller `RM(1, k)` code via Construction A (or D for higher orders). Equivalent characterizations:

1. **Reed-Muller Construction A**: lift codewords of `RM(1, k)` to `ℤ^n` via `c ↦ c + 2ℤ^n`, then scale.
2. **Real-Clifford-algebra construction**: as a 1-dimensional module over the real Clifford algebra `Cl_k`.
3. **Recursive "doubling"**: `BW_{2n}` constructed from two copies of `BW_n` glued via specific cosets.

Standard properties for `BW_{16}`:

| Property | Value |
|---|---|
| Dimension | 16 |
| Discriminant | 2^8 = 256 |
| Minimum norm | 4 |
| Kissing number κ(BW₁₆) | **4320** |
| Theta series | weight 8 modular form |
| Automorphism group | order 2^21 · 3^5 · 5^2 · 7 |

## When it applies

- **P23 d=16 kissing** — the primary application. `BW_{16}` provides 4320 unit vectors at angular distance ≥ 60°. Combined with Levenshtein 1979 LP bound, this **proves κ(16) = 4320 exactly** (one of the few small dimensions with a proven kissing number). The arena's n=4321 problem is at the score-2 structural floor (per [`structural-cap-at-score-2-meta.md`](../findings/structural-cap-at-score-2-meta.md)).
- **P22 d=12 kissing** — `BW_{16}` is RELATED but doesn't directly apply (P22 uses Coxeter-Todd K₁₂, see [`coxeter-todd-k12.md`](coxeter-todd-k12.md)). The Reed-Muller construction can be specialized to d=12 with different parameters.
- **General d=2^k sphere packing** — `BW_n` is the densest known lattice in dimensions 4, 8, 16. (At d=8, `BW_8 = E_8`, *proven* densest by Viazovska 2016; at d=16, `BW_{16}` is densest known but not proven.)
- **Decoder design** — `BW_n` lattices have efficient decoders via the Reed-Muller code structure; relevant for any arena problem invoking lattice quantization.

## Why it works (the structural argument)

The recursive construction is what makes `BW_n` special:

1. **Reed-Muller `RM(1, k)`**: a `[2^k, k+1, 2^{k-1}]` binary code with min distance growing as `2^{k-1}`. This is exactly the right asymptotic scaling for sphere packing in `2^k` dimensions.
2. **Construction A lift**: codewords become lattice cosets at norm 2 (one copy) or 4 (two copies); the minimum-norm vectors form the kissing configuration.
3. **Real-Clifford module structure**: ensures the lattice has a *huge* automorphism group (much larger than typical d=16 lattices), giving high symmetry and structural rigidity.
4. **Theta series modularity**: `BW_n`'s theta series is a modular form of weight `n/2` on the principal congruence subgroup `Γ_0(2)`; this connects to [`modular-forms-magic-function.md`](modular-forms-magic-function.md) and Viazovska-style optimality proofs.

## Classic examples

- **`BW_4 = D_4`** (root lattice). Kissing number 24. Densest in d=4.
- **`BW_8 = E_8`** (root lattice). Kissing number 240. **Proven densest at d=8** (Viazovska 2016).
- **`BW_{16}`**. Kissing number 4320. **Proven kissing-optimal at d=16** (Levenshtein 1979).
- **`BW_{32}`**. Kissing number 261120 (4320 ≤ but with caveat). Densest known at d=32 but not proven.

The d=8 → d=16 jump is crucial: `BW_{16}` is the *only* dimension above 8 where the kissing number is known exactly via lattice bounds. d=24 (Leech, also extremal) uses *different* construction machinery (theta series of weight 12 + Eisenstein-style modular forms), not Barnes–Wall.

## Construction details (P23-relevant)

For P23 specifically:

- `BW_{16}` is built from the extended Hamming code `[16, 11, 4]` (binary, distance 4) — actually a 1st-order Reed-Muller `RM(1, 4)`.
- Construction A: codewords `c ∈ {0,1}^{16}` lift to lattice points `(c + 2ℤ^{16}) / 2`.
- The 4320 minimum-norm vectors at norm 4 split as:
  - 480 vectors of type `(±1, ±1, 0, ..., 0)` permuted (32-element basis × 15 = 480 = 2^4 · 30)
  - 3840 vectors derived from the Hamming-code structure
- All pairwise inner products lie in `{0, ±1/4, ±1/2, ±1}` (60° touching condition).

The arena's n=4321 problem can never beat κ(16) = 4320 + 1 = 4321 because Levenshtein's proof is tight. JSAgent's rank #2 at score 2.0000026872 is the BW₁₆ 4320-core + one duplicate vector — the structural floor.

## How the agent should use it

When the council dispatches with category `kissing_number`, `sphere_packing`, or any d ∈ {4, 8, 16, 32} problem:

1. **Conway persona** ([`personas/conway.md`](../personas/conway.md)) and **Cohn persona** ([`personas/cohn.md`](../personas/cohn.md)) both recognize `BW_n`. Reach for it first when dimension is a power of 2.
2. For **P23**: use the BW₁₆ construction directly. The 4320-core is fully determined; the arena's n=4321 has score-2 structural floor.
3. For **P22 (d=12)**: BW₁₆ doesn't apply directly, but Reed-Muller / code-based constructions might. Look for [12, *, 4] codes with similar structure.
4. **Viazovska persona** for the modular-form / magic-function angle if extending optimality proofs.

## Limits

- **Dimension restriction**: only defined for `n = 2^k`. Other dimensions use different lattice families (Leech at d=24, Coxeter-Todd at d=12, root lattices at d ≤ 8).
- **Kissing-density vs sphere-density distinction**: `BW_n` is kissing-optimal at d=8, 16; sphere-packing-density is similarly optimal at d=8 but only conjectured at d=16, 32.
- **Decoder complexity**: while Reed-Muller decoding is efficient, the full lattice decoder for `BW_n` at large `n` requires extensive structural analysis.

## Open questions

- Is `BW_{32}`'s kissing number 261120 *proven* (it's the best known), or could a stronger Levenshtein-style LP improve the bound? (Mostly resolved via de Laat–Leijenhorst SDP techniques, but with caveats.)
- Are there `BW_n`-relatives in dimensions 12, 20 that improve current best lattices? (P22 / hypothetical d=20 problems would benefit.)

## See also

- [`concepts/sphere-packing.md`](sphere-packing.md), [`concepts/kissing-number.md`](kissing-number.md) — broader concepts
- [`concepts/coxeter-todd-k12.md`](coxeter-todd-k12.md) — the d=12 analog (different family)
- [`concepts/cohn-elkies-bound.md`](cohn-elkies-bound.md) — LP bound machinery; tight at d=8, 16, 24
- [`concepts/modular-forms-magic-function.md`](modular-forms-magic-function.md) — theta-series specialness
- [`findings/structural-cap-at-score-2-meta.md`](../findings/structural-cap-at-score-2-meta.md) — meta-pattern for κ(d) + 1 arena problems
- [`findings/hinge-overlap-rank3-squeeze.md`](../findings/hinge-overlap-rank3-squeeze.md) — rank-#2 grab pattern at P22/P23
- [`source/papers/1959-barnes-wall-lattice.md`](../../source/papers/1959-barnes-wall-lattice.md) — original Barnes-Wall paper
- [`source/papers/2024-cohn-li-kissing.md`](../../source/papers/2024-cohn-li-kissing.md) — modern improvements at d=17-21 via sign-flip techniques

*Last updated: 2026-05-02*
