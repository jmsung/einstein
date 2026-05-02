---
type: concept
author: agent
drafted: 2026-05-02
related_problems: [P2, P3, P19]
related_techniques: [bnb-exhaustive-w3.md, kronecker-search-decomposition.md]
related_findings: []
cites:
  - ../source/papers/2010-vinuesa-sidon-thesis.md
  - ../source/papers/2017-cloninger-autoconvolution-sidon.md
  - ../source/papers/2007-gyarmati-sums-differences.md
  - ../source/papers/2010-matolcsi-autoconvolution.md
---

# Sidon Sets and `B_h[g]` Generalizations

## TL;DR

A Sidon set (`B_2` set) is a set `A ⊂ ℤ` whose pairwise sums (or differences) are all distinct. The generalization `B_h[g]`: every integer has at most `g` representations as a sum of `h` elements. The autocorrelation function `f ⋆ f` is the continuous analog: pointwise bounds on `(1_A ⋆ 1_A)(t)` translate directly to multiplicities in `A + A`. This duality makes Sidon-set machinery the right toolkit for autocorrelation problems P2, P3, and the sparse-ruler / difference-base problem P19.

## What it is

For `h, g ≥ 1` and a finite set `A ⊆ ℤ`:

- `A` is a **`B_h` (Sidon) set** if every integer `n` has at most one representation `n = a_1 + ... + a_h` with `a_i ∈ A` (up to permutation).
- `A` is a **`B_h[g]` set** if every integer has at most `g` such representations.
- `A` is a **`B_h⁻[g]` set** for differences: every integer has at most `g` representations as a difference of `h` elements.

The autocorrelation `(1_A ⋆ 1_A)(t)` counts representations `t = a_i + a_j` (for `B_2`); `‖1_A ⋆ 1_A‖_∞` is the maximum representation count, and `Sidon ⇔ ‖1_A ⋆ 1_A‖_∞ ≤ 2`. So:

```
extremal Sidon-set theory   ⟷   pointwise bounds on f ⋆ f for f = 1_A.
```

The continuous analog (Cloninger–Steinerberger 2017, Matolcsi 2010, Boyer 2025) replaces `1_A` with a non-negative function on `[−1/4, 1/4]` and asks for the same minimax / ratio bounds. P2/P3/P4 are exactly this continuous question.

For **`B_h[g]` and difference-base / sparse-ruler problems**: arena P19 asks for `B ⊆ ℤ` with `0 ∈ B`, `|B| ≤ 2000`, maximizing `v = max(∪(B − B))` and minimizing `|B|² / v`. This is a difference-base problem closely linked to `B_2⁻[g]` machinery; the Kronecker decomposition `B = A ⊕ λ R` (see [kronecker-decomposition](kronecker-decomposition.md)) is a `B_h`-flavored algebraic structure.

## When it applies

- Continuous autocorrelation/autoconvolution problems (P2, P3, P4) where `f` plays the role of `1_A`.
- Difference-base / sparse-ruler problems (P19) — extremal `B_h⁻[g]` constructions.
- Any problem where a pointwise/integral bound on a self-convolution is the load-bearing constraint.

Recognition pattern: if the objective involves `f ⋆ f` or `1_A ± 1_A`, the literature on Sidon sets, `B_h[g]`, and generalized rulers is the right starting point — even when the problem is named differently.

## Why it works

Three structural connections:

1. **Sidon = max-bound = `1_A ⋆ 1_A` characterization.** Vinuesa's 2010 thesis (`source/papers/2010-vinuesa-sidon-thesis.md`) is the canonical reference connecting discrete Sidon-set extremal theory with the continuous autoconvolution problem. Every continuous extremal `f` corresponds to a sequence of discrete `1_{A_n} / |A_n|^{1/2}` whose Sidon-like properties converge.
2. **Cloninger–Steinerberger autoconvolution Sidon bounds.** `source/papers/2017-cloninger-autoconvolution-sidon.md` proves explicit lower bounds on `inf_f ‖f ⋆ f‖_∞ / (∫f)²` via the Sidon-set interpretation. These bounds inform what's *achievable* for P2, P3.
3. **Gyarmati on sums and differences.** `source/papers/2007-gyarmati-sums-differences.md` covers the dual `B_2⁻[g]` family — directly relevant to P19's difference-base question.

The practical implication: when the optimizer stalls on an autocorrelation problem, the Sidon-set bound (a discrete construction) often improves on the smooth-optimizer continuous solution. Discrete extremal constructions are the "hidden" structure that pure-numerical optimization misses.

## Classic examples

1. **P2 First Autocorrelation** — Cloninger–Steinerberger 2017 gives an explicit lower bound construction for `‖f ⋆ f‖_∞ / (∫f)²`. JSAgent's rank-#1 score `1.502861628` is consistent with the continuous Sidon-bound asymptotics. Source: `source/papers/2017-cloninger-autoconvolution-sidon.md`.
2. **P19 Difference Bases** — `B_h⁻[g]` machinery + Kronecker decomposition `A ⊕ 8011 · {0,1,4,6}`. The Singer/Bose/Paley constructions (cited in P19 strategy.md) are classical Sidon-flavored constructions in finite fields.
3. **Vinuesa thesis 2010** — the unifying reference. `source/papers/2010-vinuesa-sidon-thesis.md` covers Sidon sets, generalized Sidon, autoconvolution, and the bridge to discrete Fourier analysis.

## Related

- Concepts: [autocorrelation-inequality](autocorrelation-inequality.md), [kronecker-decomposition](kronecker-decomposition.md), [equioscillation](equioscillation.md), [discretization-as-structure](discretization-as-structure.md).
- Techniques: [bnb-exhaustive-w3](../techniques/bnb-exhaustive-w3.md), [kronecker-search-decomposition](../techniques/kronecker-search-decomposition.md).
- Findings: P19 strategy.md (council finding on Kronecker decomposition).
- Sources: `source/papers/2010-vinuesa-sidon-thesis.md`, `source/papers/2017-cloninger-autoconvolution-sidon.md`, `source/papers/2007-gyarmati-sums-differences.md`, `source/papers/2010-matolcsi-autoconvolution.md`.
