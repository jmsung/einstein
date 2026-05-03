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
---

# Can the Bernshteyn–Tait 2019 lower bound `c² ≥ 2.434` be tightened to `2.639` (the SOTA)?

This is the **concrete attack-route scoping** for the open H2 question on P19. The parent question [`2026-05-02-p19-structural-cap-conjecture.md`](2026-05-02-p19-structural-cap-conjecture.md) asks whether *any* LP/SDP certificate exists; this question scopes the most promising path: tightening the Bernshteyn–Tait 2019 LP bound directly.

## Setting

P19 (restricted difference bases / sparse rulers) score: `c²(B) = |B|² / v(B)`, minimized.

- **SOTA**: 7-way tie at `c² = 2.6390274695`. Achieved by Kronecker decomposition `B = A ⊕ 8011 · {0,1,4,6}` with a 90-mark Wichmann-style atom `A` (`c(A) = 1043`, `max(A) = 6967`). See [`p19-fully-resolved`](../concepts/p19-fully-resolved.md).
- **Best published lower bound**: Bernshteyn–Tait 2019 gives `c² ≥ 2.434` for any restricted difference base.
- **Gap**: `2.6390 − 2.4343 ≈ 0.205` (about 8% of the SOTA value).

## Question

Can the Bernshteyn–Tait LP relaxation be tightened — by adding constraints, by SDP lifting, by exploiting Kronecker-decomposition structure, or by a magic-function dual — to close (or substantially narrow) the gap to `c² = 2.639`?

A tight certificate (i.e., showing `c² ≥ 2.639`) would prove `2.639` is the global infimum of the P19 score — a publishable formal result analogous to Cohn–Elkies for sphere packing.

## Why it matters

Constructive attacks on P19 are exhausted (six dead-end findings closing every Kronecker variant; see [`p19-fully-resolved`](../concepts/p19-fully-resolved.md)). H2 (this question) and H3 (magic-function argument) are the only remaining moves. Closing H2 either:

- (a) **Proves** `2.639` is the global floor, converting the empirical 7-way tie into a formal theorem.
- (b) **Falsifies** it (the LP gap is genuinely loose), in which case the constructive attack space must be reopened — there exists a base `B` with `c² ∈ [2.434, 2.639)` that no Kronecker decomposition has found.

Either outcome is wisdom. The (a) outcome is publication-grade; the (b) outcome reopens P19 as a live arena target.

## What is known about Bernshteyn–Tait 2019

(All claims here need ingestion of the actual paper — see "First step" below.)

The Bernshteyn–Tait 2019 result on `B_2[1]`-type structures (restricted difference bases / additive bases) bounds `c²(B)` from below using a Fourier-analytic argument on the indicator function `1_B`:

- **Variable**: indicator `1_B : ℤ → {0, 1}` (or its `ℝ`-relaxation in the LP).
- **Constraint**: every integer in `[1, v]` is in the difference set `B − B`. Equivalently, `1_B \star 1_{-B}(k) ≥ 1` for `k ∈ [1, v]`.
- **Dual variable**: a non-negative function `μ` on `ℤ` (or `ℝ_{≥0}` in the LP relaxation).
- **Bound mechanism**: Plancherel + Fourier-positivity of `\hat{μ}` gives a lower bound on `|B|² / v`.

The 2.434 constant arises from a specific feasibility argument in the dual; exact derivation pending paper ingest.

## Hypotheses

### H2.1 — Sharper Plancherel / Hardy–Hilbert step

The BT 2019 bound uses a Plancherel argument that sums `|\hat{1_B}(ξ)|²` against a kernel. The current bound's slack may come from a sub-optimal Hardy–Hilbert / autoconvolution step. The Kolountzakis–Matolcsi cutting-plane LP framework (see [`kolountzakis-matolcsi-bound`](../concepts/kolountzakis-matolcsi-bound.md)) is the natural numerical tool for tightening this: at finite `n`, the LP can be solved exactly and the dual gives a certificate.

**Concrete experiment**: implement the BT LP at `n = 1000`, `n = 5000`, `n = 30 000`, with the SOTA configuration as a feasibility witness. Read off the LP's *primal* optimum (lower bound on `c²`). If primal at `n = 30 000` is ≥ `2.55`, the LP is tightening; if it stays ≤ `2.45`, the LP is fundamentally loose and H2 fails via this route.

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

**Before any of the above**: ingest the actual Bernshteyn–Tait 2019 paper into `source/papers/`. The wiki references it 5 times but no distillation exists. Until ingested, all "what BT actually proves" claims here are reconstructions from secondary references.

The arXiv link (to verify): search "Bernshteyn Tait" + "Sidon" + "B_2[1]" — the relevant paper is likely *Bernshteyn, A. & Tait, M., "Improved lower bounds on the size of B_2[g] sets,"* (2019) on arXiv. **User approval required for ingest** per the wiki-ingest discipline.

After ingest, the next concrete steps in priority order:

1. Verify the `2.434` constant against the ingested paper (current claim is a citation-of-citation).
2. Set up H2.1 numerical LP at `n = 1000` as a sanity check (a few hours; local CPU).
3. Based on H2.1 result, decide whether H2.2 (SDP lift) is worth the cost (a day + MOSEK license question).
4. H2.3 (Kronecker-restricted) is a smaller side branch — implementable in a day on local CPU.
5. H2.4 (magic function) is a research-week-or-more investment; only worth pursuing if H2.1–3 give a clean negative.

## Estimated effort

| Hypothesis | Effort | Compute | Wisdom yield |
|---|---|---|---|
| BT paper ingest + verify constants | 1 hour | local | required for any other step |
| H2.1 (LP at n=1k–30k) | 3–6 hours | local CPU | tightness curve regardless of outcome |
| H2.2 (SDP lift) | 1 day | local CPU + solver license | first-of-kind data on SDP slack for difference bases |
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
