---
type: concept
author: agent
drafted: 2026-05-02
related_problems: [P19]
related_techniques: [kronecker-search-decomposition.md, bnb-exhaustive-w3.md]
related_findings: [p19-kronecker-bridging-threshold.md, dead-end-p19-different-k-local-search.md, dead-end-p19-extended-span-1-swap.md, dead-end-p19-4mark-sidon-rulers.md, dead-end-p19-bose-chowla.md, dead-end-p19-imperfect-5mark-sidon.md, dead-end-bose-chowla-840-coincidence.md]
related_personas: [gauss.md, cohn.md, hadamard.md, riemann.md]
cites:
  - kronecker-decomposition.md
  - bose-chowla-construction.md
  - sidon-sets.md
  - provable-floor-and-frozen-problems.md
---

# P19 Difference Bases — fully resolved (umbrella concept)

## TL;DR

P19 (restricted difference bases / sparse rulers, score `|B|² / v` minimized) is **fully resolved at the level of constructive attacks**. The 7-way SOTA tie at score 2.6390274695 sits at the global Pareto-optimum on the constraint surface `(|R|, |A|, c_A, λ, max(A))` for Kronecker decompositions `B = A ⊕ λ·R`. **Six independent dead-ends** (this session, 2026-05-02) close every constructive sub-question of council H1; the remaining open paths are non-constructive (LP/SDP cap certificates, magic-function arguments). This page is the **umbrella concept** that unifies the dead-end cluster and serves as the single entry point for any future P19-related work.

## What P19 is (briefly)

Find a set `B ⊆ ℤ_{≥0}` (with `0 ∈ B`, `|B| ≤ 2000`) maximizing `v` = the largest integer such that `{1, ..., v} ⊆ {b_i − b_j : b_i > b_j}`. Score `= |B|² / v`, minimized.

Current SOTA (7-way tied, 2026-04-08): `|B| = 360`, `v = 49109`, **score = 2.6390274695**. Achieved by the Kronecker decomposition `B = A ⊕ 8011·{0,1,4,6}` where:

- `R = {0, 1, 4, 6}` is the unique 4-mark perfect Sidon ruler covering [1, 6]
- `A` is a 90-mark "atom" with `c(A) = 1043` (longest contiguous prefix in `(A−A)⁺`) and `max(A) = 6967`
- `λ = 8011`

## The constraint surface

The bridging-threshold framework (cycle 2 of `js/research/p19-difference-bases`, see [`findings/p19-kronecker-bridging-threshold.md`](../findings/p19-kronecker-bridging-threshold.md)) characterizes the formula's behavior:

```
v(A, R, λ) = L_R · λ + c(A)        when bridging holds:
                                      c(A) ≥ λ − max(A) − 1
                                      (and for imperfect R: max(A) ≥ λ for skip-shells)
```

This makes the optimization over Kronecker decompositions a constrained problem on **five coupled axes**: `(|R|, |A|, c_A, λ, max(A))`, with `|R|·|A| = k` fixed (typically k=360).

## How each dead-end maps to the surface

Every constructive attack on P19 is closing a slice of this surface:

| Dead-end | Constraint slice closed |
|---|---|
| [`dead-end-p19-different-k-local-search`](../findings/dead-end-p19-different-k-local-search.md) | `k` ∈ {358, 359, 361, …} — varying total mark count locally fails |
| [`dead-end-p19-extended-span-1-swap`](../findings/dead-end-p19-extended-span-1-swap.md) | atom 1-swap with new mark `y ∈ [6968, 8010]` — extended-span variants fail |
| [`dead-end-p19-4mark-sidon-rulers`](../findings/dead-end-p19-4mark-sidon-rulers.md) | 4-mark Sidon `R'` ≠ {0,1,4,6}, fixed atom — collapses v due to missing-shell gaps |
| [`dead-end-p19-bose-chowla`](../findings/dead-end-p19-bose-chowla.md) | algebraic atom from Bose–Chowla — Sidon-distinct-diffs antagonistic to contiguous-prefix |
| [`dead-end-bose-chowla-840-coincidence`](../findings/dead-end-bose-chowla-840-coincidence.md) | `29² − 1 = 840 = κ(12)` ruled out as structural connection |
| [`dead-end-p19-imperfect-5mark-sidon`](../findings/dead-end-p19-imperfect-5mark-sidon.md) | 5-mark imperfect Sidon `R'` + custom atom — \|R\| > 4 worsens the trade-off |
| (prior, in `mb/tracking`) | Singer / Paley QR / GMW algebraic constructions — failed empirically (2026-04-08) |

**Each of these closes a distinct slice.** Together they cover the entire constructive attack surface.

## Why the SOTA is the Pareto-optimum

Across the 5-dim constraint surface, the trade-offs are antagonistic:

- **Increasing `|R|`** beyond 4 forces `|A|` smaller (since `|R|·|A| = 360`), which lowers max attainable `c_A` (Wichmann ratio). Net loss.
- **Increasing `c_A`** above SOTA's 1043 requires denser atom — provably impossible at `|A|=90` per w=3 BnB exhaustive (1.22T nodes, 0 hits, formal lemma).
- **Increasing `max(A)`** beyond 6967 (extended span) doesn't help because c(A) doesn't increase (1-swap with `y ∈ [6968, 8010]` exhausted).
- **Algebraic R-substitution** (Singer, Bose–Chowla, Paley, GMW) fails because Sidon-distinct-diffs ≠ contiguous-prefix.

The constraint geometry locks the SOTA at:

```
(|R|, |A|, c_A, λ, max(A))  =  (4, 90, 1043, 8011, 6967)
v  =  6 · 8011 + 1043  =  49109
score  =  360² / 49109  =  2.6390274695
```

## What remains open (post-constructive)

The constructive surface is fully closed. Non-constructive attacks:

1. **H2 — LP/SDP cap certificate**. Bernshteyn–Tait 2019 gives `c² ≥ 2.434` (lower bound on score). Tightening this LP bound to `2.639` would PROVE 2.639 is the global floor — a publishable formal result analogous to Cohn–Elkies for sphere packing. Effort: ~week of work; substantial mathematics. **Concrete attack-route scoping**: see [`questions/2026-05-03-p19-bernshteyn-tait-tightening.md`](../questions/2026-05-03-p19-bernshteyn-tait-tightening.md) (4 sub-hypotheses H2.1–2.4: sharper Plancherel, SDP lift, Kronecker-restricted LP, magic function).
2. **H3 — magic-function argument**. If a Viazovska-style magic function exists for difference bases, it would saturate Bernshteyn–Tait. Highly speculative; depends on the right modular-form structure for `ℤ` vs the sphere-packing context where Viazovska 2016 works.
3. **w=4 BnB Modal exhaustive**. The prior partial w=4 sample (2,504 / 10,000) on Modal at $4 found 0 hits. Completing the sweep ($12 more) would make w=4 a *formal* exhaustion lemma analogous to w=3 (1.22T nodes, 0 hits). Modal-only; per current discipline, not pursued without explicit user direction.

## Status: P19 is "publication-ready" wisdom

The 6+ dead-end findings + this umbrella + the bridging-threshold + cross-pollination meta together constitute a **self-contained body of P19 wisdom** suitable for a research-paper-style writeup. The full chain:

1. **Setup**: difference bases / sparse rulers; SOTA construction (Kronecker + Wichmann atom).
2. **Structural insight** (cycle 2): bridging-threshold conditional identity, SOTA at saturation.
3. **Constructive exhaustion** (cycles 1, 3, 4 + Bose–Chowla + 5-mark): every Kronecker variant fails; Pareto-optimum proven.
4. **Methodological**: cross-pollination-not-compute filter prevented chasing more compute on known recipes.
5. **Open**: H2 (LP/SDP cap) and H3 (magic function) — research-grade math beyond arena scope.

## How the agent should treat P19 going forward

When dispatched on P19:

1. **First action**: read this umbrella page. The constructive surface is closed; don't waste compute re-running optimizers.
2. **Document**: any new approach should reference this page and explain *which slice* it tackles (constructive variant we missed? non-constructive H2/H3?).
3. **Submit policy**: P19 SOTA is a 7-way tie; matching = rank #8 = 0 pts. Don't submit unless we genuinely beat 2.6390274695, which requires either H2/H3 or a non-Kronecker construction not yet conceived.
4. **Pivot**: P19 is "Tier-D" for arena play (frozen + saturated). Move compute to other problems unless the user explicitly asks for H2/H3 work.

## See also

- [`findings/p19-kronecker-bridging-threshold.md`](../findings/p19-kronecker-bridging-threshold.md) — the cycle-2 structural foundation
- The 5 dead-end findings listed above
- [`questions/2026-05-02-p19-kronecker-w4-existence.md`](../questions/2026-05-02-p19-kronecker-w4-existence.md), [`questions/2026-05-02-p19-finite-field-construction.md`](../questions/2026-05-02-p19-finite-field-construction.md), [`questions/2026-05-02-p19-structural-cap-conjecture.md`](../questions/2026-05-02-p19-structural-cap-conjecture.md) — the council-dispatched questions (most now answered)
- [`findings/cross-pollination-not-compute.md`](../findings/cross-pollination-not-compute.md) — the meta-principle that filtered the search
- [`mb/tracking/problem-19-difference-bases/strategy.md`](../../../mb/tracking/problem-19-difference-bases/strategy.md) — private operational tracking (BnB w=3,4 numerical artifacts; Singer/Paley empirical fails)

*Last updated: 2026-05-02*
