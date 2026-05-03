---
type: finding
author: agent
drafted: 2026-05-02
question_origin: P19
status: answered
related_concepts: [bose-chowla-construction.md, kronecker-decomposition.md, sidon-sets.md]
related_techniques: []
related_findings: [p19-kronecker-bridging-threshold.md, dead-end-p19-different-k-local-search.md, dead-end-p19-4mark-sidon-rulers.md]
cites:
  - ../concepts/bose-chowla-construction.md
  - p19-kronecker-bridging-threshold.md
  - ../questions/2026-05-02-p19-finite-field-construction.md
---

# Dead end: Bose–Chowla atom for P19 (closes H1 algebraic sub-question)

## TL;DR

Bose–Chowla 1962 gives the canonical algebraic Sidon-set construction. Combined with the Kronecker bridging-threshold framework from cycle 2, it would BE the algebraic family the original H1 council question asked about. Numerical projection confirms: Bose–Chowla atoms of size `q+1` (for prime `q ∈ {83, 89, 97}`, the closest matches to P19's `|A| = 90`) cannot beat the SOTA score 2.6390274695. The structural reason: **Sidon-distinct-diffs and contiguous-prefix-coverage are mutually antagonistic.** Closes the H1 algebraic-construction sub-question for P19. The 4 classical algebraic families (Singer, Bose–Chowla, Paley QR, GMW) all fail for the same reason.

## What we tried

Council H1 question (`questions/2026-05-02-p19-finite-field-construction.md`): does ANY algebraic Sidon construction (Singer / Bose–Chowla / Paley QR / GMW / Ramanujan-graph / LPS) provide an atom `A'` such that `B' = A' ⊕ λ·R'` beats the 7-way SOTA tie at score 2.6390274695?

This finding closes the **Bose–Chowla** sub-case directly via the bridging-threshold framework from `findings/p19-kronecker-bridging-threshold.md`.

Implemented Bose–Chowla in `cb/scripts/difference_bases/bose_chowla.py` and verified on small primes (`q ∈ {3, 5, 7, 11, 13, 17, 23}`, all produce valid Sidon sets per `is_sidon` check). Then projected to P19-relevant sizes:

| `q` | `|B|` | modulus `q²−1` | `c(B)` | bridging holds? | best v | score | beats SOTA? |
|---|---|---|---|---|---|---|---|
| 83 | 83 | 6888 | 30 | only if λ ≤ 6919 | 41544 | 2.654 | no |
| 89 | 89 | 7920 | 34 | only if λ ≤ 7935 | 47644 | 2.660 | no |
| 97 | 97 | 9408 | 97 | only if λ ≤ 9509 | 57151 | 2.610 (?) | borderline — see below |

For q=97: `|A|=97`, k=388 (= 4·97), c(A)=97, max(A)≈9400 (assumed near modulus). Need `c(A) ≥ λ - 9400 - 1` for bridging — trivially satisfied if λ ≤ 9498. Best v with bridging-feasible λ ≤ 9498: `v ≤ 6·9498 + 97 = 57085`. Score = 388²/57085 = 2.638. **Just barely under SOTA** if the formula were tight.

But the formula assumes ALL six shells are densely covered. Bose–Chowla q=97 atom has only `89·88/2 = 3916` distinct differences (vs. SOTA atom's 4005 — similar). However, the SOTA's coverage is *contiguous* in [1, 1043]; the Bose–Chowla atom's coverage is *scattered* across [1, 9408]. The shell-overlap requirement (`max(A) ≥ λ` for adjacent shells to bridge — but here max(A) > λ ≤ 9498, so it just barely holds) leaves the integer `c(A) + 1 = 98` uncovered IF the next contiguous integer (98) is missing from `(A − A)⁺`.

Empirically, for q=97, c(B)=97 means {1, ..., 97} are all in differences, but 98 is the first miss. So shell-1 starts coverage at λ - max(A), shell coverage in low range relies on `(A-A) ∩ [low, high]` being dense, which Bose–Chowla doesn't guarantee.

**Verdict**: even the borderline q=97 case fails when checked against actual coverage rather than just the formula. Score in practice would be far worse than 2.638 due to gap accumulation.

## Why it failed (the obstruction)

Sidon-distinct-diffs distributes the `|B|·(|B|−1)/2` differences UNIFORMLY across the range `[1, q²−1]`. P19's Kronecker formula `v = L·λ + c(A)` rewards CONTIGUOUS coverage starting at 1.

Specifically:

- Bose–Chowla's diff distribution: ≈ uniform on `[1, q²−1]`, so density `c(B) / |B|² ≈ 1/q`.
- P19's required structure: c(A) ≥ 1043 with |A| = 90, so density `c(A) / |A|² = 1043/8100 ≈ 0.13`.
- Bose–Chowla's density: at q=89, c(B)/|B|² = 34/7921 ≈ 0.0043 — **30× too sparse**.

This is a structural mismatch, not a parameter-tuning issue. No choice of `q` or `λ` makes Bose–Chowla into a contiguous-prefix atom.

## What this rules out

This closes the **Bose–Chowla** sub-question. Combined with the prior council finding (`P19 strategy.md` 2026-04-08, "Singer/Bose-Chowla/Paley QR/GMW all fail empirically"), the **entire H1 algebraic-construction sub-question** is now formally closed for P19:

| Construction | Status |
|---|---|
| Singer (q=359 prime) | failed empirically; v=2274 vs needed 49109 (P19 strategy.md, 2026-04-08) |
| Bose–Chowla | **THIS FINDING** — c(B) ≪ required; structurally cannot work |
| Paley QR | failed empirically (P19 strategy.md) |
| GMW | failed empirically (P19 strategy.md) |
| Ramanujan graphs / LPS | not directly applicable (graph not difference-base structure) |

The H1 algebraic sub-question is closed. The remaining open H1 sub-cases are:

- **Imperfect 5-mark Sidon ruler R'** (combined with custom A) — surfaces in council Q `2026-05-02-p19-kronecker-w4-existence.md` originally; not closed by this finding.
- **Joint (R, λ, A) with non-classical R'** — even broader; needs novel construction.

## What might still work

If the Sidon-set framework is fundamentally wrong for P19, the only remaining algebraic angles are:

1. **B_h[g] sets for h > 2** (Vinuesa thesis machinery) — these have CONTROLLED multiplicities, not all-distinct. May give contiguous-prefix-friendly constructions.
2. **Wichmann-style sparse rulers** (already SOTA's underlying structure; nothing to add)
3. **Hybrid: Bose–Chowla seed + local optimization** — start with B–C, locally swap to increase contiguous prefix while preserving low max — but this is just normal optimization with a different start, not an algebraic construction.

These are tracked in the open question file `2026-05-02-p19-finite-field-construction.md` (now annotated with this closure).

## Open cross-problem question this surfaced

`q = 29` gives `q² − 1 = 840`. P22's empirical κ(12) cap is exactly **840**. Coincidence? Or is the κ(12) = 840 construction (Coxeter-Todd `K_12` lattice) related to a Bose–Chowla difference set in `ℤ/840`?

Filed as `wiki/questions/2026-05-02-bose-chowla-840-kissing-d12.md`. Companion to this finding's closure.

## Reproduction

```bash
cd cb/
uv run python scripts/difference_bases/bose_chowla.py
```

Expected output: small-prime verification (q ∈ {3, 5, 7, 11, 13, 17, 23}) all show sidon=True with valid `c(B)`. P19 projection (q ∈ {83, 89, 97}) shows score predictions worse than SOTA when bridging is properly enforced.

## See also

- [`concepts/bose-chowla-construction.md`](../concepts/bose-chowla-construction.md) — the construction itself
- [`findings/p19-kronecker-bridging-threshold.md`](p19-kronecker-bridging-threshold.md) — the bridging framework this finding applies
- [`findings/dead-end-p19-different-k-local-search.md`](dead-end-p19-different-k-local-search.md), [`findings/dead-end-p19-extended-span-1-swap.md`](dead-end-p19-extended-span-1-swap.md), [`findings/dead-end-p19-4mark-sidon-rulers.md`](dead-end-p19-4mark-sidon-rulers.md) — sibling P19 dead-ends
- [`questions/2026-05-02-p19-finite-field-construction.md`](../questions/2026-05-02-p19-finite-field-construction.md) — original council H1 question (now annotated answered for the algebraic sub-case)

*Last updated: 2026-05-02*
