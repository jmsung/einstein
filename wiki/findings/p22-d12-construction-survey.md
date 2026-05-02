---
type: finding
author: agent
drafted: 2026-05-02
level: 1
source_type: agent_analysis
cites:
  - problem-22-kissing-d12/strategy.md
  - problem-22-kissing-d12/literature.md
  - problem-22-kissing-d12/implementation-recipes.md
  - ../source/papers/1971-leech-sphere-packing.md
  - ../source/papers/2024-delaat-kissing-sdp.md
  - ../source/papers/2022-ganzhinov-symmetric-lines.md
  - ../source/blog/cohn-kissing-numbers.md
---

[[../home]] | [[../index]]

# Kissing Number d=12 — Construction Landscape Survey

Synthesis of what is known about K(12)=840 constructions, current upper bound, and the structural cap that makes the arena's score-0 target (κ(12) ≥ 841) almost certainly unreachable. Filed by `/wiki-research` 2026-04-24 as Tier-A synthesis on branch `js/feat/p22-kissing-d12`.

## Established lower bound: K(12) = 840

Classical lower bound, established by the **P₁₂ₐ construction** of Leech & Sloane (Canad. J. Math. 23:718, 1971) (see [../source/papers/1971-leech-sphere-packing.md](../../source/papers/1971-leech-sphere-packing.md)). Method: error-correcting code → Construction A on lattice K₁₂.

CHRONOS reconstructed the explicit recipe (arena thread 195, see [problem-22-kissing-d12/literature.md](../problem-22-kissing-d12/literature.md)):

1. Build Steiner system S(5,6,12) via PSL(2,11) orbit of base block `{1,3,4,5,9,∞}`.
2. Augment to a nonlinear (12, 144, 4) binary code.
3. Pick a weight-6 codeword `c` with `A_4(c) = 51`.
4. Construction A: centers at `x ∈ ℤ¹²` with `x mod 2 ∈ code`, radius 1.
5. At center `c`, the 840 neighbors decompose as 24 axis shifts `±e_i` + 816 = 16·51 half-integer patterns.
6. All pairwise inner products lie in `{0, ±¼, ±½, ±1}`; max is exactly ½ (60° touching).

Rescaling integer coords by ½ yields unit vectors with entries in `{0, ±½, ±1}` — exactly what the arena's CHRONOS submission uses (see [problem-22-kissing-d12/strategy.md](../problem-22-kissing-d12/strategy.md)).

## Three independent construction pathways, all capped at 840

CHRONOS arena thread 198 (see [problem-22-kissing-d12/literature.md](../problem-22-kissing-d12/literature.md)) summarizes the "8-way structural cap":

- **Lattice-based**: K₁₂ (Coxeter-Todd) min-shell = 756, forms a saturated (756, 3)-design.
- **Construction A from binary codes**: `A(12,4) = 144` proven optimal (Östergård-Baicheva-Kolev 1999, IEEE TIT 45).
- **Leech-lattice cross-section**: every 12-d sublattice of Λ₂₄ caps at 756.

Decomposition candidate (thread 193): `P₁₂ₐ = Λ₁₂ ∪ (h + Λ₁₂)` where `h` is a deep hole of Λ₁₂ → 648 + 192 = 840.

## Upper bound: K(12) ≤ 1355

de Laat & Leijenhorst (Math. Programming Computation 16:503, 2024) — clustered low-rank SDP three-point bound (see [../source/papers/2024-delaat-kissing-sdp.md](../../source/papers/2024-delaat-kissing-sdp.md)). The 840–1355 gap of 515 is the formal feasibility window; in practice CHRONOS believes the structural cap sits at 840 itself.

## What recent literature does NOT do for D12

Ganzhinov's symmetric-lines framework improves D10/D11/D14 lower bounds via group-theoretic constructions (PSU(4,2), Mathieu groups) but explicitly leaves D12 unchanged at 840 (see [../source/papers/2022-ganzhinov-symmetric-lines.md](../../source/papers/2022-ganzhinov-symmetric-lines.md)).

The canonical [Cohn MIT bounds table](../../source/blog/cohn-kissing-numbers.md) records the 840 / 1355 pair and has not been updated with a stronger D12 construction.

## Arena framing (n=841, hinge overlap)

The arena problem places **n = 841** unit vectors (one above K(12)=840) and minimizes hinge overlap `Σ_{i<j} max(0, 2 − ‖cᵢ − cⱼ‖)`. CHRONOS's leader at score = 2.000000000000000 is precisely the 840-vector P₁₂ₐ core plus a duplicate of `(1,0,...,0)` — the single duplicate contributes exactly 2.0 to the score.

Beating 2.0 requires showing there exists a position `v ∈ S¹¹` such that
`Σᵢ max(0, 2 − ‖2v − 2vᵢ‖) < 2`,
which is equivalent to showing K(12) ≥ 841 — a 55-year breakthrough (see [problem-22-kissing-d12/strategy.md](../problem-22-kissing-d12/strategy.md) §"Key insight"). The 8-way structural cap suggests this is impossible.

## Open work items (gaps surfaced during research)

These are not paper-ingestable and are queued as analysis/data tasks:

- [ ] **Extract explicit P₁₂ₐ coordinates** — currently only implicit in CHRONOS's arena payload. Build a script under `src/einstein/p22_kissing_d12/` that reconstructs the 840-vector configuration from the PSL(2,11) recipe (or parses CHRONOS's payload), checks pairwise inner products lie in `{0, ±¼, ±½, ±1}`, and writes a deterministic data file.
- [ ] **Compute link structure of v₀ at γ=½** — strategy.md attack-ladder step 2. Compute the link `link(v₀) = { vᵢ : ⟨v₀, vᵢ⟩ = ½ }` and look for `u ⊥ v₀` minimizing `Σ_{i ∈ link(v₀)} [⟨u, wᵢ⟩]_+` where `wᵢ` are the link projections. If the minimum is `< 1`, the duplicate position is not a local minimum and a strict score < 2 exists.
- [ ] **Verify P₁₂ₐ ↔ Λ₁₂ ∪ (h + Λ₁₂) decomposition** numerically — CHRONOS's thread-193 candidate.

*Last updated: 2026-04-24*
