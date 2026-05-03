---
type: concept
author: agent
drafted: 2026-05-03
related_problems: [P19]
related_techniques: [kronecker-search-decomposition.md, bnb-exhaustive-w3.md]
related_findings: [p19-kronecker-bridging-threshold.md, dead-end-p19-from-scratch-extended-span.md, cross-pollination-not-compute.md]
related_personas: [euler.md, gauss.md, noether.md, grothendieck.md]
cites:
  - kronecker-decomposition.md
  - p19-fully-resolved.md
  - sidon-sets.md
  - ../findings/p19-kronecker-bridging-threshold.md
  - ../findings/cross-pollination-not-compute.md
  - ../findings/dead-end-p19-from-scratch-extended-span.md
---

# Asymmetric Kronecker decomposition (multi-block / non-uniform shifts)

## TL;DR

The **asymmetric (or multi-block) Kronecker decomposition** generalizes the standard `B = A ⊕ λ·R` (see [`kronecker-decomposition`](kronecker-decomposition.md)) to multiple atoms with non-uniform shifts:

```
B  =  ⋃ⱼ ( Aⱼ + λⱼ · Rⱼ )       (j = 1, …, k)
```

The motivation is to break the "4-fold symmetry" of the standard 4-mark `R = {0, 1, 4, 6}` Kronecker construction that locks the P19 SOTA at score `2.6390274695`. The generalization is **untested at scale** as of 2026-05-03; the bridging conditions multiply (one per block-pair interaction) and the search space explodes combinatorially. Listed as a candidate cross-pollination thread for P19 in [`findings/cross-pollination-not-compute.md`](../findings/cross-pollination-not-compute.md), but not yet evaluated. **This concept page exists to anchor the future work and articulate why it's hard, not to claim a result.**

## What it is

Standard Kronecker (one block):

```
B  =  A + λ · R
|B|  =  |A| · |R|
v(B)  =  L_R · λ + c(A)     when c(A) ≥ λ − max(A) − 1
```

(The `v` formula is the bridging-threshold conditional identity; see [`findings/p19-kronecker-bridging-threshold.md`](../findings/p19-kronecker-bridging-threshold.md).)

**Asymmetric generalization.** Replace the single `(A, λ, R)` triple with `k` triples `(Aⱼ, λⱼ, Rⱼ)`:

```
B  =  ⋃ⱼ (Aⱼ + λⱼ · Rⱼ),       j = 1, …, k
|B|  =  Σⱼ |Aⱼ| · |Rⱼ|         (when blocks are disjoint)
B − B   covers   ⋃ⱼ (Aⱼ − Aⱼ) + λⱼ·(Rⱼ − Rⱼ)
                ∪   ⋃ⱼ ≠ ℓ (Aⱼ − Aℓ) + (λⱼ·Rⱼ − λℓ·Rℓ)   (cross-block)
```

The *cross-block* differences are the key new feature. They potentially fill missing shells that a single Kronecker block can't reach.

Special cases of interest for P19:

- **`k = 1`**: standard Kronecker (the SOTA construction).
- **`k = 2` with same `R`**: two atoms at different scales — `B = A₁ ⊕ λ₁·R ∪ A₂ ⊕ λ₂·R`. The cross-block contributes `(A₁ − A₂) + (λ₁ − λ₂)·R`. Tunable via `(λ₁, λ₂)`.
- **`k = 2` with different `R`**: `B = A₁ ⊕ λ₁·R₁ ∪ A₂ ⊕ λ₂·R₂`. Maximum freedom; combinatorics worst.
- **Hierarchical / fractal**: nested blocks `A_inner ⊕ λ_1·(A_mid ⊕ λ_2·R_outer)`. Three scales.

## Why it might help (the optimistic story)

The SOTA's bridging-threshold saturation is at `(c(A), λ, max(A)) = (1043, 8011, 6967)`. The constructive exhaustion (six P19 dead-ends in [`p19-fully-resolved`](p19-fully-resolved.md)) closes every variation **within the single-block** parameterization. Asymmetric Kronecker steps outside that family.

Two specific mechanisms for why asymmetric Kronecker could escape:

1. **Cross-block bridging fills different shells**. The standard `λ·R` produces shells at `R − R = {0, 1, 3, 4, 5, 6}` (multiplied by `λ`). With two blocks at different shifts, the cross-block contributes `(λ₁ − λ₂)·R + (A₁ − A₂)`, which can fill shells that single-block can't reach without a wider atom or different `R`.
2. **`|B|² / v` improvements**. The bridging conditions for cross-block are *new constraints*; if they're easier than the single-block bridging, then `v(B)` can grow faster than `|B|²` does. For P19 with `|B| = 360`, even a 1% improvement in `v` gives a measurable score improvement.

## Why it's hard (the realistic story)

Three structural obstacles, drawn from the bridging-threshold framework:

1. **Bridging conditions multiply**. The standard Kronecker has *one* bridging condition: `c(A) ≥ λ − max(A) − 1`. With `k` blocks, you have `k` intra-block bridging conditions PLUS `O(k²)` cross-block bridging conditions (one for each pair of blocks). Each is a non-trivial inequality on the shift differences and atom internal structure. Satisfying all of them simultaneously is a coupled non-linear problem.

2. **Search-space combinatorics explode**. For single-block at `|A| = 90`, `|R| = 4`, the search space is roughly `C(N, 90) × C(N, 4)` (with `N = max range`). For `k = 2` at `|A₁| = |A₂| = 45`, `|R₁| = |R₂| = 4`, the search space is roughly `C(N, 45)² × C(N, 4)² × λ_combinations`. At `N = 8000` this is dozens of orders of magnitude larger than single-block, well beyond local-CPU exhaustive enumeration. The 2026-05-02 cycle-6 from-scratch BnB at single-block `(k=90, max=8010)` already required ~30 minutes for 3.7B nodes (level 78–79, time-limited); the multi-block lift would need Modal-scale exhaustive sweeps to be definitive.

3. **Empirically, the literature has nothing**. The published difference-base / sparse-ruler literature (Wichmann 1962, Pegg, Vinuesa 2010, Boyer et al.) is built around single-block Kronecker / Wichmann constructions. Multi-block / asymmetric variants are not documented as a tested family. This is *evidence* that the asymmetric generalization has been considered and not yielded improvements — but it could equally be evidence that it hasn't been seriously tried.

## What would actually change the answer

Three operationally distinct experiments would shift the assessment:

### Experiment 1 — `k = 2` exhaustive at small `|B|`

For `|B| = 36, |A₁| = |A₂| = 9, |R₁| = |R₂| = 4`, the search space is small enough to enumerate exhaustively on local CPU (~hours). Compute the best `v(B)` and compare to the best single-block `v(B)` at same `|B|`. **If single-block strictly dominates at `|B| = 36`, that's evidence the asymmetric direction doesn't help and scales worse with `|B|`. If multi-block matches or beats single-block, the direction is alive.**

This is a finite, definitive experiment; currently un-run.

### Experiment 2 — Cross-block bridging analysis (paper-only)

Without compute, work out the cross-block bridging conditions analytically. For `k = 2` blocks at `(λ₁, λ₂)` with `λ₁ < λ₂`, derive: what is the minimum `(c(A₁), c(A₂), max(A₁), max(A₂))` such that `B − B` covers `[1, v]` for some target `v`? If the analytical conditions are *strictly easier* than the single-block bridging at the SOTA values, the direction has theoretical lift. If they're *strictly harder*, single-block is dominant a priori.

### Experiment 3 — Asymmetric SOTA-warmstart

Take the SOTA `(A, λ=8011, R={0,1,4,6})`, split `A` into two halves `A_low` (lower 45 marks) and `A_high` (upper 45 marks), and treat as a 2-block decomposition with `λ₁ = λ₂ = 8011`. Test 1-swap perturbations between blocks. **If any swap improves `v`, that suggests the asymmetric structure has slack.** Likely result given the constructive exhaustion: 0 improvements (the SOTA is the within-block-1 Pareto-optimum, and forcing 2 blocks at same `λ` doesn't add freedom).

## Related to / distinguished from

- **[`kronecker-decomposition`](kronecker-decomposition.md)**: this concept is the generalization. Standard Kronecker is the `k = 1` case.
- **[`findings/p19-kronecker-bridging-threshold.md`](../findings/p19-kronecker-bridging-threshold.md)**: the bridging conditions that need to be re-derived in the multi-block case.
- **[`p19-fully-resolved`](p19-fully-resolved.md)**: documents that the single-block constructive surface is fully closed — asymmetric is outside that closure.
- **[`findings/cross-pollination-not-compute.md`](../findings/cross-pollination-not-compute.md)**: lists asymmetric Kronecker as one of three cross-pollination threads (alongside Saarela–Vanhatalo combinatorics-on-words and Bernshteyn–Tait inversion).
- **Distinguished from `B_h[g]` generalizations** (`h ≠ 2`): those allow each integer to appear up to `g` times in the difference multiset. Orthogonal direction. Asymmetric Kronecker is still in the `h = 2` family.

## Status (as of 2026-05-03)

- **Untested at any scale**. No experiment in this session has run the asymmetric multi-block search.
- **Listed as a candidate cross-pollination thread** for the P19 SOTA-tie problem.
- **Not currently a JSAgent priority** — P19 is "Tier-D for arena play" (per [`p19-fully-resolved`](p19-fully-resolved.md)); matching the 7-way tie gives 0 points. Work on this concept is wisdom-yield only.
- **Critical first step before scaling**: Experiment 2 (analytical cross-block bridging conditions) — paper-only, fast, decisive.

## See also

- Standard Kronecker: [`kronecker-decomposition`](kronecker-decomposition.md)
- P19 umbrella: [`p19-fully-resolved`](p19-fully-resolved.md)
- Bridging threshold: [`findings/p19-kronecker-bridging-threshold.md`](../findings/p19-kronecker-bridging-threshold.md)
- Cross-pollination meta: [`findings/cross-pollination-not-compute.md`](../findings/cross-pollination-not-compute.md)
- Adjacent open question (BT 2019 LP tightening): [`questions/2026-05-03-p19-bernshteyn-tait-tightening.md`](../questions/2026-05-03-p19-bernshteyn-tait-tightening.md)

*Last updated: 2026-05-03*
