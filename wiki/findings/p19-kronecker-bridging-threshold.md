---
type: finding
author: agent
drafted: 2026-05-02
question_origin: P19
status: answered
related_concepts: [kronecker-decomposition.md, basin-rigidity.md, parameterization-selection.md]
related_techniques: [kronecker-search-decomposition.md]
related_findings: [dead-end-p19-different-k-local-search.md, dead-end-p19-extended-span-1-swap.md, dead-end-p19-from-scratch-extended-span.md]
cites:
  - ../source/papers/2010-vinuesa-sidon-thesis.md
  - ../personas/_synthesis.md
refined_by: dead-end-p19-from-scratch-extended-span.md
---

> **CORRECTION (2026-05-02, cycle 6)**: The "Next step" prediction below — that Wichmann gives `c(A) ≈ 1500` for k=90 in the extended-span regime, leading to `v ≈ 49566` and `score ≈ 2.6147` — is **structurally incorrect**. Wichmann perfect rulers exist only at k = 4r+3 (87, 91, 95, ...), NOT at k=90. Empirically, both Pegg- and Wikipedia-style Wichmann gap formulations at k=90 yield `c ≤ 65`. Cycle 3 (1-swap from SOTA atom, [`dead-end-p19-extended-span-1-swap.md`](dead-end-p19-extended-span-1-swap.md)) and cycle 6 (direct BnB from scratch in [0, 8010], 3.715B nodes) both returned 0 hits. The structural insight — that bridging is a 2-axis constraint `(c(A), max(A))` — is preserved. The predicted improvement target is invalidated. See [`dead-end-p19-from-scratch-extended-span.md`](dead-end-p19-from-scratch-extended-span.md) for the full refutation.

# P19 Kronecker structure has a JOINT bridging threshold; SOTA saturates it

## TL;DR

The formula `v = L·λ + c(A)` for Kronecker-decomposed difference bases is not just a lever on `c(A)` — it's a **conditional identity** with a bridging threshold `c(A) ≥ λ − max(A) − 1`. SOTA sits **exactly at the threshold** (1043 = 8011 − 6967 − 1 + 1 = 1044... actually 8011 − 6967 = 1044, so threshold is c(A) ≥ 1043). This refines the prior "atom is the bottleneck" framing: the lever is the *joint* parameter `(c(A), λ, max(A))`, not `c(A)` alone.

## Setup

SOTA: `B = A ⊕ 8011·{0,1,4,6}` with `|A|=90`, `max(A)=6967`, `c(A)=1043`, `λ=8011`, `R={0,1,4,6}` (perfect Sidon ruler), `L=max((R-R)⁺)=6`. Score = 360²/49109 = 2.6390274695.

Formula from prior strategy: `v = L·λ + c(A) = 6·8011 + 1043 = 49109`. Tight on SOTA.

## What the analysis showed

**1. Per-shell coverage is uniform.** Each cross-block shell `k ∈ {1,2,3,4,5,6}` covers exactly `|A−A| = 8011` distinct positive integers in a window of width `2·max(A)+1 = 13935`. Density 0.575. Identical across all 6 shells (each is a translation of the same `A−A` multiset by `k·λ`).

**2. Bridging requires two conditions:**
- **Same-block → shell 1**: `c(A) ≥ λ − max(A) − 1 = 8011 − 6967 − 1 = 1043`. SOTA: c(A) = 1043. ⇐ **saturated**.
- **Shell k → shell k+1**: `2·max(A) ≥ λ − 1`, i.e., `max(A) ≥ (λ−1)/2`. SOTA: max(A)=6967 vs (8011−1)/2=4005. ⇐ comfortably satisfied (overlap by 2962).

So the structural bottleneck is the **first** bridging condition. SOTA's `c(A) = 1043` is precisely tuned to the minimum value that lets [1, c(A)] connect to the lowest value in shell 1 (= `λ − max(A) = 1044`).

**3. Perturbation test confirms the threshold.** 15 random 1-swaps of the SOTA atom were tested. Every perturbation dropped `c(A)` (from 1043 to values ∈ {3, 4, 6, 7, 10, 13, 14, 28, 31, 33, 43, 49, 51, 51, 59}). For each, the actual v fell to **exactly c(A)** (not `L·λ + c(A)`), because the bridging gap `[c(A)+1, 1043]` broke contiguity. The formula's prediction stayed near 48k while actual v collapsed to small values.

This is decisive: **when `c(A) < 1043`, the formula's `v = L·λ + c(A)` is wrong (too high). The correct v is `c(A)` — losing the entire cross-block contribution.**

## The conditional identity

```
                ┌  L·λ + c(A)        if  c(A) ≥ λ − max(A) − 1     (bridging holds)
   v(A,R,λ)  =  ┤  c(A)              if  c(A) < λ − max(A) − 1     (bridging fails)
                └  (other regimes if shell-to-shell bridging also fails)
```

The first branch is what prior strategy.md captured. The second branch explains why every local perturbation of SOTA is catastrophic: any 1-swap moves c(A) below the threshold, dropping v to that c(A) directly.

## Why this is a refinement, not a refutation

Prior framing: "atom A is the bottleneck; c(A) is the lever."

Refined framing: "**SOTA saturates a joint structural threshold `c(A) = λ − max(A) − 1`. The lever is the joint parameter `(c(A), λ, max(A))`, not c(A) alone.**"

Both framings agree at SOTA. They diverge on what to optimize for improvement.

## What this opens up

The conditional identity makes a precise design space visible:

| Tune | Constraint | Effect |
|---|---|---|
| Increase λ | Forces larger max(A) for bridging (max(A) ≥ λ − c(A) − 1) | Increases L·λ term but constrains atom |
| Decrease λ | Easier bridging | Reduces L·λ term — usually loses v |
| Increase max(A) | Easier bridging condition | Allows smaller c(A); keeps L·λ |
| Increase L (use 5-mark non-perfect R') | Adds shells beyond k=6 | But |R|=5 with k=360 forces |A|=72; smaller atom → smaller c(A) — likely worse |
| Asymmetric Kronecker (multi-block) | Different shell pattern | Bridging conditions multiply; harder to satisfy |

The hidden Pareto frontier has three axes: `(c(A), λ, max(A))`. SOTA is at one extremal point. Other extremal points might give v(B) ≥ 49109 with different score.

**Concrete example** (untested): if max(A) is increased to ~7500 (allowed since arena permits span > v), bridging threshold becomes c(A) ≥ λ − 7500 − 1 = 510. A 90-mark atom in [0, 7500] with c(A) ≥ 510 is much easier to construct (Wichmann gives c(A) ≈ 1500 for k=90 in this range). Then v could reach 6·8011 + 1500 = 49566 — beating SOTA by 457, score 2.6147. Within the bridging design space, this is a new optimization target.

## Connection to the cross-pollination principle

This is exactly the kind of insight the [cross-pollination filter](cross-pollination-not-compute.md) was designed to surface: it didn't come from "more compute on the SOTA basin" — it came from asking *why* the formula holds and noticing the conditional structure. The cycle 1 negative result (different-k local search) made the saturation point visible because every perturbation revealed the threshold.

Same general principle as `parameterization-selection.md`: a structural reframe of the optimization target can outperform brute-force search by orders of magnitude.

## Next step (for cycle 3)

Test the `max(A) ↑, c(A) ↓ jointly` design space:

1. Generate a 90-mark atom `A'` in `[0, 7500]` (extended span) with `c(A') ≥ 510` (the relaxed threshold).
2. Compute `v(A' ⊕ 8011·{0,1,4,6})`.
3. If `v > 49109`, we have a new SOTA candidate (triple-verify, surface for user approval).
4. If formula gives v ≈ 49566 but actual v is lower, identify what's broken (likely shell-to-shell bridging at higher max(A)).

This is genuinely new ground — prior work fixed `max(A)` at 6967 throughout.

## Reproduction

```bash
cd cb/
uv run python scripts/difference_bases/cross_block_analysis.py
```

Output reproduces the per-shell density (0.575 across all 6 shells) and the formula tightness on SOTA. Perturbation test reproduces the c(A) collapse.

## See also

- [`findings/dead-end-p19-different-k-local-search.md`](dead-end-p19-different-k-local-search.md) — the cycle 1 negative that surfaced the saturation
- [`findings/cross-pollination-not-compute.md`](cross-pollination-not-compute.md) — the meta-principle that filtered to this analysis
- [`concepts/kronecker-decomposition.md`](../concepts/kronecker-decomposition.md) — the structural framework

*Last updated: 2026-05-02*
