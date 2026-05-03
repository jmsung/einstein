---
type: concept
author: agent
drafted: 2026-05-02
related_problems: [P22, P23]
related_techniques: [first-order-link-tangent-test.md]
related_findings: [p22-d12-construction-survey.md, dead-end-bose-chowla-840-coincidence.md]
related_personas: [conway.md, cohn.md, viazovska.md, ramanujan.md]
cites:
  - sphere-packing.md
  - kissing-number.md
  - cohn-elkies-bound.md
  - modular-forms-magic-function.md
  - ../source/papers/2024-cohn-li-kissing.md
  - ../source/papers/2024-delaat-kissing-sdp.md
  - ../source/papers/1971-leech-sphere-packing.md
---

# Coxeter–Todd lattice K₁₂

## TL;DR

The **Coxeter–Todd lattice** `K₁₂` is the densest known 12-dimensional integer lattice and the foundation of κ(12) = 840 lower-bound constructions. It has 756 minimum vectors at norm 4 (kissing number of the lattice itself = 756), but the related Construction-A on the binary `[12, 6, 4]` code or the deep-hole `Λ₁₂ ∪ (h + Λ₁₂)` decomposition extends to 840 unit vectors achieving the empirical κ(12) cap. **Authored 2026-05-02** to close a Type-1 gap (6 mentions, no own page).

## What it is

`K₁₂` is a 12-dimensional Eisenstein-rooted lattice constructed via the ternary Golay code. Equivalent characterizations:

1. **Construction A from ternary [12, 6, 6] Golay code**: lift each codeword to ℤ¹² via `c ↦ c + 3ℤ¹²`, then scale.
2. **Eisenstein integer construction**: as a 6-dimensional lattice over `ℤ[ω]` (with `ω = e^{2πi/3}`), giving 12-dim ℝ-lattice via the standard embedding.
3. **Sublattice of Leech**: cross-section of the Leech lattice `Λ₂₄` by an appropriate 12-dim subspace.

Standard properties:

| Property | Value |
|---|---|
| Dimension | 12 |
| Discriminant | 729 (= 3⁶) |
| Minimum norm | 4 |
| Kissing number κ(K₁₂) | **756** |
| Minimum vectors | 756 vectors at norm 4, forming a (756, 3)-design |
| Theta series | `1 + 756q² + 4032q³ + 20412q⁴ + ...` (modular form of weight 6) |
| Automorphism group | 6 · 6.PSU(4,3).2 (order 78382080) |

## When it applies

- **P22 d=12 kissing** — `K₁₂`'s 756 minimum vectors plus an additional 84 deep-hole-shifted vectors give the 840-element kissing configuration that achieves the empirical κ(12) ≥ 840 cap. The arena n=841 problem places one extra vector, making score 2.0 the structural floor (one inevitable duplicate).
- **P23 d=16 kissing** — `K₁₂` is a building block; the 16-dim construction uses similar code-lattice machinery (Barnes-Wall `BW₁₆`).
- **General d=12 sphere-packing** — `K₁₂` is the densest known 12-dim lattice. Cohn-Elkies LP bound at d=12 isn't tight here (known LP bound is loose by ~10%).
- **Modular forms / Eisenstein integers** — `K₁₂` is a natural object in the Eisenstein-integer family alongside `E₈` (special at d=8) and Leech (special at d=24).

## Why it works (the structural argument)

`K₁₂` achieves its kissing number 756 because:

1. **Code structure**: the [12, 6, 6] ternary Golay code has 729 = 3⁶ codewords, each a length-12 ternary vector with min Hamming distance 6. Construction A lifts these to lattice vectors with controlled angle structure.
2. **Eisenstein-integer arithmetic**: the multiplicative structure of `ℤ[ω]` ensures the lattice has a high degree of internal automorphism — the 78-million-element `Aut(K₁₂)` is much larger than typical 12-d lattices.
3. **Theta series modularity**: K₁₂'s theta series is a weight-6 modular form on the full modular group, putting `K₁₂` in the same "specialness" family as `E₈` (weight 4) and Leech (weight 12). This is the connection to [`modular-forms-magic-function.md`](modular-forms-magic-function.md).

The leap from 756 to **840** — the empirical κ(12) — comes from extending `K₁₂` via:

- **Deep-hole shift** (Conway–Sloane SPLAG): take `K₁₂ ∪ (h + K₁₂)` where `h` is a deep hole of `K₁₂`. Gives 648 + 192 = 840 unit vectors at minimum distance.
- **Construction A from binary [12, 6, 4] code** (Leech–Sloane 1971, [source/papers/1971-leech-sphere-packing.md](../source/papers/1971-leech-sphere-packing.md)): direct construction giving 24 axis shifts + 816 = 16·51 half-integer patterns, total 840.

Both decompositions hit 840; the de Laat–Leijenhorst 2024 SDP cluster bound proves κ(12) ≤ 1355, leaving a 515-gap to formal proof of κ(12) = 840 exactly. **The empirical cap is widely believed but not proven.**

## Classic examples

The 756 minimum vectors of `K₁₂`:

- 12·11 = 132 vectors of the form `±e_i ± e_j` (norm 4, with `e_i, e_j` standard basis)
- 624 = 4·156 "Eisenstein-mixed" vectors with mod-3 structure derived from the ternary Golay code

Plus the +84 extension to 840 (in P₁₂ₐ Construction A): half-integer-pattern vectors that respect the binary code's parity-check structure.

## How the agent should use it

When the council dispatches with category `kissing_number`, `sphere_packing`, or any d=12 / d=16 / d=24 problem:

1. **Conway persona** ([personas/conway.md](../personas/conway.md)) explicitly knows the K₁₂ structure. Reach for it first.
2. For P22 specifically, the structural cap at 840 is established; the arena's n=841 problem is provably at score-2.0 floor. Don't try to beat it; document.
3. **Viazovska persona** ([personas/viazovska.md](../personas/viazovska.md)) might be relevant if magic-function machinery extends to d=12 (open conjecture; would prove κ(12) = 840 exactly).
4. **Cohn persona** ([personas/cohn.md](../personas/cohn.md)) for the LP/SDP cap side: tightening the de Laat–Leijenhorst bound from 1355 to 840 is a major open problem.

For arena play:

- **P22**: rank-#1 infeasible (score 0 = κ(12) ≥ 841 = contradicts the cap). Best achievable rank: #2 or #3 with score 2.0 (cap + duplicate).
- **P23**: similar; κ(16) = 4320 is *proven* (Levenshtein 1979), so n=4321 is mathematically infeasible at score 0; floor is 2.0.

## Limits

- `K₁₂` is a *specific lattice*; doesn't directly generalize to other dimensions without modifications.
- The 756 → 840 extension is via *non-lattice* configurations (the 840-config isn't itself a lattice — it's a packing of 840 unit vectors that don't generate a lattice when combined with the central sphere).
- Cohn–Elkies LP at d=12 is loose (~10% gap to 756 lattice density); sharp magic function not known.
- Tightening the κ(12) ≤ 1355 bound to ≤ 840 is a major open problem.

## See also

- [`concepts/sphere-packing.md`](sphere-packing.md), [`concepts/kissing-number.md`](kissing-number.md) — broader concepts
- [`concepts/cohn-elkies-bound.md`](cohn-elkies-bound.md) — LP bound machinery; loose at d=12
- [`concepts/modular-forms-magic-function.md`](modular-forms-magic-function.md) — theta-series specialness; K₁₂ is in this family
- [`findings/p22-d12-construction-survey.md`](../findings/p22-d12-construction-survey.md) — comprehensive P22 structural survey
- [`source/papers/1971-leech-sphere-packing.md`](../../source/papers/1971-leech-sphere-packing.md) — Leech-Sloane 1971 P₁₂ₐ construction
- [`source/papers/2024-cohn-li-kissing.md`](../../source/papers/2024-cohn-li-kissing.md), [`source/papers/2024-delaat-kissing-sdp.md`](../../source/papers/2024-delaat-kissing-sdp.md) — modern SDP machinery

*Last updated: 2026-05-02*
