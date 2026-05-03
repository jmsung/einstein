---
type: question
author: agent
drafted: 2026-05-03
status: open
asked_by: agent
parent_question: 2026-05-02-p19-structural-cap-conjecture.md
related_problems: [P19]
related_concepts: [p19-fully-resolved.md, lp-duality.md, kolountzakis-matolcsi-bound.md, cohn-elkies-bound.md, provable-floor-and-frozen-problems.md, sidon-sets.md]
related_personas: [cohn.md, viazovska.md, hilbert.md, riemann.md]
cites:
  - ../concepts/p19-fully-resolved.md
  - ../findings/p19-kronecker-bridging-threshold.md
  - 2026-05-02-p19-structural-cap-conjecture.md
  - ../../source/papers/2019-bernshteyn-tait-difference-bases.md
---

# Can the Bernshteyn–Tait 2019 lower bound `d* ≥ 2.4344 + ε` be tightened to `2.639` (the SOTA)?

> **2026-05-03 update — paper ingested.** The actual contribution of Bernshteyn–Tait 2019 is *strictly tightening* Leech's 1956 bound `d* ≥ 2.4344…` to `d* ≥ 2.4344… + ε` for some `ε > 0`, with numerical estimate `ε ≈ 10⁻³` (not optimized). See [`source/papers/2019-bernshteyn-tait-difference-bases.md`](../../source/papers/2019-bernshteyn-tait-difference-bases.md). Earlier versions of this question conflated the two attributions; corrected throughout below.

This is the **concrete attack-route scoping** for the open H2 question on P19. The parent question [`2026-05-02-p19-structural-cap-conjecture.md`](2026-05-02-p19-structural-cap-conjecture.md) asks whether *any* LP/SDP certificate exists; this question scopes the most promising path: tightening the Bernshteyn–Tait 2019 PSD-truncation bound directly.

## Setting

P19 (restricted difference bases / sparse rulers) score: `c²(B) = |B|² / v(B)`, minimized. Note: arena P19 uses `|B|² / v` while B-T uses `D(n)² / n` — different normalizations of the same underlying constant `d* = lim D(n)²/n`. Asymptotically aligned.

- **SOTA**: 7-way tie at `c² = 2.6390274695`. Achieved by Kronecker decomposition `B = A ⊕ 8011 · {0,1,4,6}` with a 90-mark Wichmann-style atom `A` (`c(A) = 1043`, `max(A) = 6967`). See [`p19-fully-resolved`](../concepts/p19-fully-resolved.md).
- **Leech 1956 lower bound**: `d* ≥ 2 − 2 inf_θ [sin(θ)/θ] = 2.4344…` (with `θ_* ≈ 4.4934`, `sin(θ_*)/θ_* ≈ −0.2172`).
- **Bernshteyn–Tait 2019 strict improvement**: `d* ≥ 2.4344 + ε` for some `ε > 0`, numerical estimate `ε ≈ 10⁻³`. Proof uses Bochner–Herglotz + 4×4 PSD constraints on Fourier coefficients of a probability measure on `𝕋`.
- **Best published upper bound**: Golay 1972, `d* ≤ 2.6458`. (No improvement post-1972 to the authors' knowledge.)
- **Gap to SOTA**: `2.6390 − 2.4344 ≈ 0.2046` (about 8.4% of the SOTA value). The B-T improvement closes only `~10⁻³` of this gap.

## Question

Can the Bernshteyn–Tait LP relaxation be tightened — by adding constraints, by SDP lifting, by exploiting Kronecker-decomposition structure, or by a magic-function dual — to close (or substantially narrow) the gap to `c² = 2.639`?

A tight certificate (i.e., showing `c² ≥ 2.639`) would prove `2.639` is the global infimum of the P19 score — a publishable formal result analogous to Cohn–Elkies for sphere packing.

## Why it matters

Constructive attacks on P19 are exhausted (six dead-end findings closing every Kronecker variant; see [`p19-fully-resolved`](../concepts/p19-fully-resolved.md)). H2 (this question) and H3 (magic-function argument) are the only remaining moves. Closing H2 either:

- (a) **Proves** `2.639` is the global floor, converting the empirical 7-way tie into a formal theorem.
- (b) **Falsifies** it (the LP gap is genuinely loose), in which case the constructive attack space must be reopened — there exists a base `B` with `c² ∈ [2.434, 2.639)` that no Kronecker decomposition has found.

Either outcome is wisdom. The (a) outcome is publication-grade; the (b) outcome reopens P19 as a live arena target.

## What is known about Bernshteyn–Tait 2019

(Paper ingested 2026-05-03; full distillation at [`source/papers/2019-bernshteyn-tait-difference-bases.md`](../../source/papers/2019-bernshteyn-tait-difference-bases.md). Summary below.)

The Bernshteyn–Tait 2019 result reformulates the difference-basis question as a Fourier-coefficient problem on probability measures on the unit circle `𝕋`:

- **Setup**: Suppose `D(n)² / n ≤ 2 − 2 sin(θ)/θ + o(1)` (i.e., violates Leech's bound by `ε`). Construct probability measures `μ, ν ∈ Prob(𝕋)` from the difference basis via push-forward by `k ↦ exp(θik/n)`.
- **Convolution identity** (eq. 3.3 in B-T): `μ * μ̄ = (2 / (2 + α)) ν + (α / (2 + α)) ζ` where `α := lim |A_n|²/n − 2 ∈ [0, 0.4344]` and `ζ ∈ Prob(𝕋)`.
- **Bochner–Herglotz** (Theorem 2.2): `n × n` Hermitian matrix `A(i, j) := μ̂(j − i)` is positive semidefinite for every `n`.
- **Decomposition**: `μ = (1−β)η + βδ₁` where `β = √(α/(2+α)) ≈ 0.4224`. The atom at `1 ∈ 𝕋` is forced.
- **Contradiction via 3×3 + 4×4 PSD matrices** on `Re(η̂(0..3))`. The 3×3 PSD constraint forces `0 < Re(η̂(2)) < 0.1`; the 4×4 constraint forces `Re(η̂(3)) > 0.4`; combined with the convolution identity, `Re(η̂(3)) < 0.1` — contradiction.

**Leech's `2.4344` bound** comes from the optimal `θ_*` minimizing `sin(θ)/θ`. **B-T's `+ε` improvement** comes from the 4×4 PSD truncation; larger truncations should give larger `ε` (this is the natural sharpening direction).

**Open question** in the paper (§3.13): let `a` be the infimum of `α > 0` such that `(μ, ζ)` exist satisfying the convolution identity. Is `d* = 2 + a`? This would convert the strict-improvement existence theorem into a tractable variational problem.

## Hypotheses

### H2.1 — Larger PSD truncations (the natural sharpening direction)

B-T's contradiction comes from PSD constraints on the 4×4 Hermitian matrix `M(i, j) := Re(η̂(j − i))` for `i, j ∈ {0, 1, 2, 3}`. The systematic improvement is to use `n × n` matrices for `n ≥ 5`. Each additional row/column adds new PSD constraints that may force the contradiction at larger `α` (smaller `ε`-violation), giving a strictly tighter `d*` lower bound.

**Concrete experiment**: solve the SDP feasibility problem "does there exist `(η̂(0), η̂(1), …, η̂(n−1))` with `η̂(0) = 1`, `η̂(1) = γ ≈ −0.7314`, satisfying B-T's convolution identity at the chosen `α` AND the `n × n` Hermitian PSD constraint?" Find the largest `α` for which feasibility holds; that is the new lower bound `d* ≥ 2 + α`. Implement at `n = 5, 6, 7, 8, …` until SDP solver runtime becomes prohibitive (likely `n ≈ 12` on local CPU).

### H2.2 — SDP lift

Lift the LP to an SDP using a moment-matrix construction on `1_B \star 1_{-B}`. SDP lifts are sometimes tight where LP relaxations are loose (cf. flag-algebra lifts in extremal graph theory). The 2.6390 SOTA might saturate the level-2 SDP.

**Concrete experiment**: write down the level-2 moment matrix for `1_B \star 1_{-B}` over the support `[0, v]`. Solve via MOSEK / SCS / CLARABEL. Read off the SDP optimum.

### H2.3 — Kronecker structure injection

Every known competitive P19 construction is a Kronecker decomposition `B = A ⊕ λ R`. Adding the *constraint* "the LP feasible region restricts to Kronecker products" might tighten the bound for the construction class we already know is competitive — even if it doesn't close the gap for arbitrary `B`. This would prove `2.639` is the floor *within Kronecker constructions*, which is what the constructive exhaustion already empirically suggests.

**Concrete experiment**: parameterize the LP by `(|R|, |A|, λ, max(A), c(A))` and write the bridging-threshold conditional identity (see [`p19-kronecker-bridging-threshold`](../findings/p19-kronecker-bridging-threshold.md)) as a hard constraint. Solve. Read off the SDP/LP optimum on the Kronecker manifold.

### H2.4 — Magic function (= H3 in the umbrella, listed here for completeness)

A Viazovska-style magic function `f : ℝ → ℝ` whose Fourier transform satisfies specific positivity conditions would saturate the BT LP exactly, analogous to how Viazovska's `f` saturates Cohn–Elkies for `d = 8`. Highly speculative; depends on whether the right modular-form identity exists for `ℤ`-valued bases.

**Concrete experiment**: search for an Eisenstein-series Poincaré sum on `SL₂(ℤ)` that produces a function with the right positivity at the BT LP optimum. Effort: substantial — this is research-level mathematics.

## First step (concrete)

**Done 2026-05-03**: BT 2019 paper ingested at [`source/papers/2019-bernshteyn-tait-difference-bases.md`](../../source/papers/2019-bernshteyn-tait-difference-bases.md). Constants and proof structure verified. Earlier "Bernshteyn–Tait 2019 gives `c² ≥ 2.434`" claims across 4 wiki pages were corrected to attribute `2.434` to Leech 1956 and `2.434 + ε` (numerical `ε ≈ 10⁻³`) to B-T 2019.

After ingest, the next concrete steps in priority order:

1. **H2.1 SDP feasibility at `n = 5, 6, 7, 8`**. The smallest experiment that should give measurable improvement over B-T's 4×4 result. ~1 day local CPU with CLARABEL or SCS. **First non-trivial experiment.**
2. H2.3 (Kronecker-restricted LP) is a smaller side branch — implementable in a day on local CPU. Independent of H2.1 outcome.
3. H2.2 (full LP-relaxation lift) is harder — requires writing the convolution-identity LP from scratch with the full asymptotic limit machinery.
4. H2.4 (magic function) is a research-week-or-more investment; only worth pursuing if H2.1 saturates near SOTA.

## Estimated effort

| Hypothesis | Effort | Compute | Wisdom yield |
|---|---|---|---|
| ~~BT paper ingest + verify constants~~ | ~~1 hour~~ | ~~local~~ | **DONE 2026-05-03** |
| H2.1 (PSD truncation `n = 5..8`) | 1 day | local CPU + CLARABEL/SCS | tightness curve regardless of outcome; new bound `d* ≥ 2 + α_n` |
| H2.2 (full convolution-identity LP lift) | 2–3 days | local CPU | systematic generalization of B-T's argument |
| H2.3 (Kronecker-restricted LP) | 1 day | local CPU | proves SOTA tight within construction class — even if not globally |
| H2.4 (magic function search) | weeks | varies | research-grade math; publishable on success |

**Total to a clean negative or positive**: ~1 week of focused work for H2.1–3. H2.4 is open-ended.

## Submission policy

**P19 SOTA is a 7-way tie at score 2.6390. Matching = rank #8 = 0 pts.** This work has *no* arena-rank consequence; it's purely wisdom-yield. The submission floor in `axioms.md` doesn't apply (no submission expected). The work product is:

- The wiki finding answering this question (positive or negative)
- A possible companion paper / arXiv preprint if H2 closes positively
- Reusable infrastructure (LP/SDP code in `scripts/p19/`) for H2-style attacks on adjacent problems (P2/P3/P4 autocorrelation, P11 Tammes Delsarte LP, P22 d=12 SDP)

## References

- [`wiki/concepts/p19-fully-resolved.md`](../concepts/p19-fully-resolved.md) — umbrella; H2 is the canonical open path
- [`wiki/findings/p19-kronecker-bridging-threshold.md`](../findings/p19-kronecker-bridging-threshold.md) — the conditional identity that defines the Kronecker manifold (input to H2.3)
- [`wiki/concepts/kolountzakis-matolcsi-bound.md`](../concepts/kolountzakis-matolcsi-bound.md) — cutting-plane LP framework for autoconvolution; structurally adjacent to H2.1
- [`wiki/concepts/cohn-elkies-bound.md`](../concepts/cohn-elkies-bound.md) — magic-function precedent for H2.4 (different domain but same machinery)
- `source/papers/2010-matolcsi-autoconvolution.md` — adjacent autoconvolution-LP work
- `source/papers/2010-vinuesa-sidon-thesis.md` — `B_h[g]` framework
- (pending ingest) Bernshteyn & Tait 2019 — the load-bearing paper
- Parent question: [`2026-05-02-p19-structural-cap-conjecture.md`](2026-05-02-p19-structural-cap-conjecture.md)
