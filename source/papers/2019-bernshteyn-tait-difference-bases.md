---
type: source
provenance: papers
author: agent
drafted: 2026-05-03
level: 4
source_type: published_paper
source_url: https://arxiv.org/abs/1901.09411
source_local: raw/papers/2019-bernshteyn-tait-difference-bases.pdf
cites:
  - ../papers/2010-vinuesa-sidon-thesis.md
  - ../papers/2007-gyarmati-sums-differences.md
  - problem-19-difference-bases/strategy.md
---

[[../home]] | [[../index]]

# Bernshteyn & Tait — Improved Lower Bound for Difference Bases

**Authors:** Anton Bernshteyn, Michael Tait
**Year:** 2019 (J. Number Theory 205: 50–58)
**arXiv:** 1901.09411
**DOI/Journal:** Journal of Number Theory, vol 205, 2019

## Summary

A **difference basis with respect to `n`** is a subset `A ⊆ ℤ` such that `A − A ⊇ {1, …, n}`. Let `D(n)` denote the smallest size of such a basis, and define

```
d*  :=  lim_{n → ∞}  D(n)² / n.
```

Rédei–Rényi (1949) showed `d*` exists and `2.4244 ≤ d* ≤ 2.6666`. Leech (1956) improved the lower bound to `d* ≥ 2 − 2 inf_θ [sin(θ)/θ] = 2.4344…`. Golay (1972) improved the upper bound to `d* ≤ 2.6458`.

**This paper's contribution (Theorem 1.3):** there exists `ε > 0` such that

```
d*  ≥  ε + 2 − 2 inf_θ [sin(θ)/θ]    =    ε + 2.4344…
```

— i.e., **Leech's bound is not sharp**. Numerical computations suggest `ε ≈ 10⁻³`, though the paper does not optimize the constant. Six pages, dense.

## Key technique — Fourier-analytic on probability measures

The proof rephrases the difference-basis question as a Fourier-coefficient problem on probability measures on the unit circle `𝕋 = {z ∈ ℂ : |z| = 1}`:

1. **Setup**. Suppose for contradiction that `D(n)² / n ≤ 2 − 2 sin(θ)/θ + o(1)` for `θ` minimizing `sin(θ)/θ` (so `θ ≈ 4.4934`, `sin(θ)/θ ≈ −0.2172`). Take an infinite "bad" sequence `B ⊆ ℕ⁺` and corresponding bases `A_n` saturating this bound up to `o(1)`.

2. **Construct two probability measures**. Define `φ_n(k) := exp(θik/n)` and push forward `uni(A_n)` to get `μ_n ∈ Prob(𝕋)`; similarly construct `ν_n ∈ Prob(𝕋)` from `uni([−n] ∪ [n])`. Pass to the limit (using compactness of `Prob(𝕋)` under weak-* topology) to get `μ, ν ∈ Prob(𝕋)`. The difference-basis condition `A_n − A_n ⊇ [−n] ∪ [n]` becomes the convolution identity

```
μ * μ̄  =  (2 / (2 + α)) · ν  +  (α / (2 + α)) · ζ        (eq. 3.3)
```

where `α := lim_{n} α_n = lim |A_n|²/n − 2 ∈ [0, 0.4344…]` and `ζ ∈ Prob(𝕋)` is the limit of the "extra mass" measures.

3. **Bochner–Herglotz** (Theorem 2.2 in the paper, after Rudin 1990 §1.4.3): a function `f : ℤ → ℂ` with `f(0) = 1`, `f(−k) = conj(f(k))`, and the `n×n` Hermitian matrix `A(i, j) := f(j − i)` positive semidefinite for every `n` is the Fourier transform of a unique probability measure on `𝕋`. **The PSD constraints on Hermitian matrices of Fourier coefficients translate the measure-theoretic problem into a chain of inequalities on a few real numbers.**

4. **Decomposition.** Set `β := √(α / (2 + α)) ≈ 0.4224`. Show `μ = (1 − β)η + βδ₁` for some `η ∈ Prob(𝕋)` (Lemma 3.8: `μ` has exactly one atom at `1` of mass `β`). The Fourier coefficients `η̂(0) = 1`, `η̂(1) = −β/(1 − β) ≈ −0.7314…` are determined.

5. **Contradiction via 3×3 and 4×4 PSD matrices.**
   - From the 3×3 PSD matrix on `Re(η̂(j − i))` for `i, j ∈ {0, 1, 2}`: derive `0 < Re(η̂(2)) < 0.1` (Lemma 3.12).
   - From the 4×4 PSD matrix on `Re(η̂(j − i))` for `i, j ∈ {0, 1, 2, 3}`: derive `Re(η̂(3)) > 0.4` (last step of §3).
   - Combined with the convolution identity from (3.10) and Lemma 3.4 (which gives `ν̂(k) = sin(kθ)/(kθ)` for `k ≠ 0`), this forces `Re(η̂(3)) < 0.1`, contradicting `> 0.4`.

   Therefore the assumption `d* ≤ 2 − 2 sin(θ)/θ + o(1)` was false; `d* ≥ 2 − 2 sin(θ)/θ + ε` for some `ε > 0`.

## Key constants and inequalities

| Quantity | Value | Origin |
|---|---|---|
| `θ_*` | `4.4934…` | minimum of `sin(θ)/θ` for `θ > 0` |
| `inf sin(θ)/θ` | `−0.2172…` | at `θ_*` |
| `2 − 2 inf sin(θ)/θ` | `2.4344…` | Leech 1956 lower bound on `d*` |
| `α` | `≤ 0.4344…` | gap variable in eq. (3.1) |
| `β = √(α / (2 + α))` | `≈ 0.4224…` | atom mass in `μ`'s decomposition |
| `γ = −β / (1 − β)` | `≈ −0.7314…` | `Re(η̂(1))` |
| ε in Theorem 1.3 | `≈ 10⁻³` (numerical) | the strict improvement; not optimized |

## Open question (paper's §3.13)

Let `a` denote the infimum of `α > 0` such that there exist `μ, ζ ∈ Prob(𝕋)` satisfying eq. (3.3). Bernshteyn–Tait know `d* ≥ 2 + a`. **Is it true that `d* = 2 + a`?** This would convert the strict-improvement existence theorem into an explicit value (or at least a tractable variational problem on probability measures).

## Relevance to Einstein Arena P19

P19 (restricted difference bases / sparse rulers, score `|B|² / v` minimized): the SOTA at score `2.6390274695` (7-way tie) sits above the Leech `2.4344` and B-T `2.4344 + ε` lower bounds. The gap is about **8.4%** of the SOTA value. Closing the gap to prove `d* = 2.6390` (the H2 hypothesis in `wiki/concepts/p19-fully-resolved.md`) would require either:

1. **Tighten B-T's `ε`**. Their numerical estimate `ε ≈ 10⁻³` is far below the gap `0.205` to the SOTA. Optimizing the proof's constants might give `ε` of order `10⁻²` but probably not `10⁻¹`.
2. **Larger PSD matrices.** Their proof uses 4×4 PSD matrices on `Re(η̂(0..3))`. Generalizing to `n × n` for larger `n` and computing the resulting LP / SDP feasibility would be the natural systematic improvement. This is exactly the [`wiki/questions/2026-05-03-p19-bernshteyn-tait-tightening.md`](../../../wiki/questions/2026-05-03-p19-bernshteyn-tait-tightening.md) H2.1 / H2.2 program.
3. **Magic-function dual.** A Viazovska-style modular-form construction that saturates B-T's LP at the value `2.6390`. Highly speculative; H2.4 in the same question file.

## Cross-cutting: same Fourier-PSD machinery as P22

The Bochner–Herglotz step is structurally the same as the [Cohn–Goncalves 2019 d=12 sign-uncertainty proof](2019-cohn-uncertainty-d12.md): in both cases, the problem is reduced to PSD constraints on Fourier coefficients of a probability measure, then bounded by a finite truncation of the constraint matrix. P19 (this paper) uses 4×4 truncation; Cohn–Goncalves saturates with infinite-dimensional Eisenstein-series machinery.

## Limitations

- `ε` not explicitly bounded — paper says ~10⁻³ numerically, but no proven lower bound.
- 4×4 truncation is the smallest case that gives a contradiction; larger truncations would presumably tighten further but require more bookkeeping.
- The variational problem in Question 3.13 (the limit `a`) is open — closed-form expression unknown; Golay (1972) felt "the correct value will, undoubtedly, never be expressed in closed form."
- No upper-bound improvement; only `d* ≥ 2.4344 + ε`. Golay's `2.6458` upper bound from 1972 has not been beaten in this paper or, to the authors' knowledge, since.

## See Also

- [[2010-vinuesa-sidon-thesis]] — `B_2[g]` framework; B-T's `d*` is the analogous limit for `B_2[1]` restricted bases.
- [[2010-matolcsi-autoconvolution]] — autoconvolution-supremum bounds via similar step-function / LP machinery.
- [[2019-cohn-uncertainty-d12]] — same Bochner–Herglotz / PSD-Fourier machinery for sign-uncertainty in d=12.
- [[../problem-19-difference-bases/strategy]]
