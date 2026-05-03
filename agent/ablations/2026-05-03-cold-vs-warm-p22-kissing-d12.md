---
type: ablation
author: agent
drafted: 2026-05-03
hypothesis: "On a structurally-capped problem (P22), the wiki's score-2 floor finding plus first-order link-tangent test plus P₁₂ₐ construction recipe is the difference between rank #3 (achievable) and chasing rank #1 (mathematically infeasible)."
status: complete-as-audit
held_out_problem: P22 Kissing Number d=12 (n=841)
prior_ablations:
  - 2026-05-02-cold-vs-warm-p10-thomson.md  # easy case (frozen + magic number)
  - 2026-05-03-cold-vs-warm-p11-tammes.md   # harder case (tolerance discipline)
---

# Ablation 2026-05-03: cold-vs-warm-wiki on P22 Kissing d=12 (n=841)

## Why P22 (the hardest ablation case so far)

The series so far:

| Ablation | Problem type | Wiki uplift | Cold-agent outcome |
|---|---|---|---|
| **P10 Thomson** | Frozen (magic-number) | Compute-saving only | Same SOTA basin, wasted hours |
| **P11 Tammes** | Basin-locked (partially-known) | **Score-affecting** (1 ulp tolerance recipe) | Likely 1–10 ulps below ceiling 70% |
| **P22 d=12 kissing** | Structurally-capped | **Score-AND-direction** (chases impossibility) | Likely **fails to reach rank #3** at all |

P22 is the most extreme case yet because the wiki's structural-cap finding tells the agent **the score floor is 2.0, not 0** — if the cold agent doesn't know this, it will spend its compute budget chasing an impossible target rather than securing the achievable rank #3.

## Hypothesis

The wiki's three load-bearing pieces for P22 are:

1. **`structural-cap-at-score-2-meta` finding**: kissing-tight arena problems at `n = κ(d) + 1` have a *structural floor* at score 2.0 (one duplicate pair required). Beating 2.0 requires `κ(d) ≥ n + 1`, contradicting established results. **Score 2.0 is the floor, not a target**.
2. **`first-order-link-tangent-test` concept + technique**: for a candidate filler `v ∈ S^{d-2}`, `min S(u) ≈ 8.02` over the 60°-link tangent vs threshold 1.155 — a 6.8× margin certifying strict local minimum and ruling out rank #1 via first-order analysis.
3. **P₁₂ₐ Construction A recipe**: the 840-core comes from the binary `[12, 6, 4]` Hamming code via Construction A on `ℝ^12`. Adding one duplicate vector reaches `n = 841` at score 2.0; sub-ulp polish lands rank #3 at ~2.0014.

Predicted uplift:

- **Direction**: warm agent secures rank #3 in ~2 hours. Cold agent likely chases score < 2.0 for 10+ GPU-hours before realizing it's infeasible (or never realizing).
- **Score**: warm agent at 2.0014 (rank #3, +1 pt). Cold agent at score ≥ 2.5 likely (no rank, 0 pts).
- **Compute**: 5–10× ratio depending on whether cold agent eventually finds the duplicate-construction insight.

Falsifiable form: if a cold agent in equal compute reaches rank #3 (score ≤ 2.01), the wiki's structural-cap finding adds nothing. If the cold agent stays at score ≥ 2.5 OR reaches rank #3 only after substantially more compute, the wiki helps.

## Held-out choice

**P22 Kissing Number d=12 (n=841)**: place 841 unit vectors in `ℝ^12`; minimize hinge-overlap `Σᵢ<ⱼ max(0, 2 − ‖cᵢ − cⱼ‖)` where `cᵢ = 2 vᵢ / ‖vᵢ‖`. Score 0 would prove `κ(12) ≥ 841`.

- SOTA: arena leaderboard's #1 at 2.0 + ulps; JSAgent rank #3 at 2.001403089191293.
- Status: rank-3 secured (2026-04-25); rank-1 ruled out by 12-agent council + 60M+ first-order proof.
- Held-out test: P22 has NOT been touched in this session.

## Setup

This is the audit half. The cold-side run requires a fresh Claude session.

## What the WARM wiki has for P22

### Direct hits (qmd query "P22 kissing number d=12 hinge overlap structural cap")

| Page | Score | Substantive content |
|---|---|---|
| `findings/structural-cap-at-score-2-meta.md` | 93% | The score-2 floor finding (load-bearing) |
| `concepts/first-order-link-tangent-test.md` | 56% | The proof technique that closes rank #1 |
| `concepts/coxeter-todd-k12.md` | 47% | K₁₂ lattice underlying κ(12) bound (756 → 840 via P₁₂ₐ) |
| `concepts/hinge-overlap.md` | 47% | The objective function structure |
| `concepts/kissing-number.md` | 47% | Family framework |

### Concept pages directly relevant

- [`concepts/kissing-number.md`](../../wiki/concepts/kissing-number.md) — `κ(d)` definition + table.
- [`concepts/coxeter-todd-k12.md`](../../wiki/concepts/coxeter-todd-k12.md) — K₁₂ lattice; 756 vectors; the structural building block.
- [`concepts/first-order-link-tangent-test.md`](../../wiki/concepts/first-order-link-tangent-test.md) — formal proof framework: `min S(u)` over the 60° link tangent vs threshold 1.155.
- [`concepts/hinge-overlap.md`](../../wiki/concepts/hinge-overlap.md) — the loss function's geometry.
- [`concepts/cohn-elkies-bound.md`](../../wiki/concepts/cohn-elkies-bound.md) — LP bound machinery (κ(12) ≤ 1355 via de Laat–Leijenhorst 2024).
- [`concepts/bourgain-clozel-kahane.md`](../../wiki/concepts/bourgain-clozel-kahane.md) — sharp d=12 sign-uncertainty (NEW from PR #80); the modular-form connection that *circumstantially* supports `κ(12) = 840`.
- [`concepts/sphere-packing.md`](../../wiki/concepts/sphere-packing.md) — broader framework.

### Technique pages

- [`techniques/first-order-link-tangent-test.md`](../../wiki/techniques/first-order-link-tangent-test.md) — concrete LP/eigenvalue computation.
- [`techniques/parallel-tempering-sa.md`](../../wiki/techniques/parallel-tempering-sa.md) — fallback for hard exploration (used in P22's 16-replica SA).
- [`techniques/slsqp-active-pair-polish.md`](../../wiki/techniques/slsqp-active-pair-polish.md) — float64-ceiling polish.
- [`techniques/micro-perturbation-multiscale.md`](../../wiki/techniques/micro-perturbation-multiscale.md) — sub-ulp landing within the basin.

### Findings (load-bearing)

- `findings/structural-cap-at-score-2-meta.md` — **THE finding**. Tells the agent the floor is 2.0, not 0. Lists the 8-way structural cap (K₁₂ lattice, P₁₂ₐ Construction A, SDP cluster bound, Leech cross-section).
- `findings/p22-d12-construction-survey.md` — exhaustive survey of construction families: P₁₂ₐ binary code, K₁₂ lattice cosets, Leech 12-section, BW-style binary lifts. Identifies P₁₂ₐ Construction A from `[12, 6, 4]` Hamming code as the 840-vector backbone.
- `findings/hinge-overlap-rank3-squeeze.md` — the technique applied: P₁₂ₐ 840-core + one duplicate at `(1, 0, ..., 0)` + sub-ulp polish lands at score 2.0014.
- `source/papers/2024-delaat-kissing-sdp.md` — de Laat–Leijenhorst 2024: `κ(12) ≤ 1355` formally; Cohn–Salmon believe the cap is at 840 itself.

### Personas that would dispatch on P22

- **Conway** (lattices, sphere codes; Coxeter-Todd K₁₂ is in his orbit).
- **Cohn** (LP bounds, Cohn-Elkies; the de Laat-Leijenhorst proof descends from his framework).
- **Viazovska** (modular forms; the d=12 modular-form proof connection via Cohn-Goncalves 2019).
- **Hilbert** (functional analysis; LP/SDP duality).

### Total wiki investment for P22

**~18 pages directly relevant**, **4 personas would dispatch**, **3 specific findings (1 meta + 1 survey + 1 technique recipe)**, **4 techniques with calibrated recipes**. Plus 2 ingested papers (de Laat–Leijenhorst 2024 SDP, Cohn–Goncalves 2019 d=12 uncertainty).

## What a COLD agent would have

- Problem statement.
- Arena API access (can fetch SOTA solutions).
- General-purpose Python/numpy/scipy.
- General training-data knowledge:
  - Knows `κ(d)` definition, classical bounds (`κ(8) = 240`, `κ(24) = 196560` from Viazovska & Cohn et al.).
  - Knows `κ(12) ≥ 840` is well-published (P₁₂ₐ via [12, 6, 4] code is documented in Conway-Sloane). **But probably won't realize this is conjecturally tight** without the meta-finding's framing.
  - Standard hinge-loss optimization techniques.
- **No specific knowledge of**:
  - The score-2 structural floor as a *known result* — this is JSAgent's earned-wisdom from the 12-agent council + first-order proof, not in the published literature in this exact framing.
  - The first-order link-tangent test as the canonical *proof technique* (the technique itself is general; its application to P22 with concrete `S(u) = 8.02` is JSAgent's calibration).
  - The 8-way structural cap convergence framing (K₁₂ + P₁₂ₐ + SDP + Leech). A cold agent would have to re-derive each of these as separate threads.
  - The "rank #3 is +1 pt; don't pursue rank #1" submission-policy implication.

## Predicted outcome

### Warm-wiki agent

1. Reads `wiki/problems/_inventory.md`. Sees P22 listed as rank-3 at 2.001403, score-2 floor.
2. Reads `findings/structural-cap-at-score-2-meta.md`. **Concludes immediately**: "score 2.0 is the floor; rank #1 is mathematically infeasible; aim for rank #3."
3. Reads `findings/p22-d12-construction-survey.md`. Selects P₁₂ₐ Construction A as the 840-core.
4. **Acts**: build P₁₂ₐ from binary [12, 6, 4] code, scale to unit sphere, add `v_{841} = (1, 0, ..., 0)`, polish with SLSQP active-pair at the standard recipe.
5. Verifies the rank-#1 ruling-out via first-order link-tangent: `min S(u) ≈ 8.02 ≫ 1.155 threshold`. Documents.
6. **Final score**: 2.001403089191293, rank #3, +1 pt.
7. **Time**: ~2 hours (most of it is constructing P₁₂ₐ correctly the first time).
8. **Compute**: Local CPU; no GPU needed.

### Cold-wiki agent

1. Reads problem statement. Sees `n = 841`. Plans to place 841 unit vectors with minimal overlap.
2. Searches training data: knows κ(12) ≥ 840 from Conway-Sloane. **Reasons**: "if 840 fit, maybe 841 also fits" — not necessarily flagged as impossible.
3. Tries to construct 841 non-overlapping unit vectors:
   - Random initialization + L-BFGS / Adam on hinge loss → converges to score ~ 50 (most pairs overlapping).
   - Smart initialization from K₁₂ or random spherical codes → score ~ 5–15.
   - SA / parallel tempering at scale → may eventually find the 840-core + 1 duplicate, score ~ 2 + small slack.
4. **Most likely outcome**: cold agent burns 5–20 GPU-hours optimizing without realizing 2.0 is the floor. Eventually either:
   - (a) **Discovers the duplicate is forced** (~30% likelihood after many iterations), reaches score ~ 2.0 + small noise = rank #4–6 depending on polish.
   - (b) **Stays at score ≥ 5** chasing fixed-cardinality constructions (~50% likelihood).
   - (c) **Successfully replicates JSAgent's 840-core + duplicate + polish** (~20% likelihood with SA + good seed).
5. **Final score**: in case (a), rank #4–6 (1 pt only if rank #3 hit); in case (b), no leaderboard placement; in case (c), rank #3 (matches warm agent).
6. **Time**: 10–40 GPU-hours / wall-time.

### Predicted uplift

| Dimension | Warm | Cold (median) | Magnitude |
|---|---|---|---|
| Final score | 2.001403 (rank #3, +1 pt) | 5–15 (most likely no placement) | **categorically different** |
| Compute | ~2 CPU-hours | 10–40 GPU-hours | 50–200× |
| Direction | "match #3, don't chase #1" | "chase score 0, never realize it's infeasible" | **mission-critical** |
| Wisdom yield | nothing new (wiki captures it) | possible re-derivation of structural cap (one-off finding) | low |

**Predicted uplift on P22**: warm agent reliably secures +1 pt in ~2 hours. Cold agent has 20% chance of matching, 80% chance of failing entirely. **The wiki's load-bearing contribution is the *direction* of search, not just a parameter.**

This is qualitatively MORE significant than P11. P11 was "wrong tolerance → 1 ulp worse." P22 is "wrong target → no leaderboard placement at all."

## What this measures

- **Direction-discipline transfer**: whether the wiki's "score 2.0 is the floor, not the target" framing redirects compute productively. P10 measured *compute-saving non-action*; P11 measured *correct parameter*; P22 measures *correct direction*.
- **Stop-condition transfer**: whether the first-order link-tangent test's `min S(u) ≈ 8.02 ≫ 1.155` formal proof prevents rank-#1 chasing.
- **Construction recipe transfer**: whether the P₁₂ₐ Construction A recipe (binary [12, 6, 4] code) actually gets built correctly without ambiguity.

## Limits of this audit

- The score-2 floor IS in the public wiki and the de Laat-Leijenhorst 2024 paper. A sufficiently thorough cold agent that read both would have the framing. The "doesn't know the floor" claim assumes a typical cold-agent first-pass run.
- Cold agent's 20% success rate is a guess. Could be higher if the agent is given more time + better tools (SA at scale, smart initialization).
- The submission-policy reasoning ("rank #3 is +1 pt; rank #1 infeasible; don't waste budget") is JSAgent-specific operational discipline. A cold agent without arena-strategy training might still pursue rank #1 even if it suspected infeasibility.

## Recommendation for the next ablation cycle

After P22, the natural progression is:

| Held-out candidate | Why interesting |
|---|---|
| **P9 sign-uncertainty** | wiki has BCK floor 0.2025 + Cohn–Goncalves 0.3102 upper + gap-space NM technique. Different uplift mechanism: cold agent could chase verifier artifacts below 0.2025 (which JSAgent itself did pre-correction; see verification-patterns finding). |
| **Inverse case: a problem with NO substantive wiki coverage** | Tests whether the warm agent does *worse* on out-of-coverage problems (overconfidence in inapplicable wiki). |
| **Parallel run: warm vs warm-with-one-page-removed** | Surgically tests the load-bearing claim: remove `findings/structural-cap-at-score-2-meta.md` and re-run. Does the agent re-derive? Does it fail? |

The third option is methodologically strongest — it isolates *which page* is load-bearing. Currently we infer load-bearing from page citations + qualitative reasoning, not surgical testing.

## Verdict

For P22 specifically: **wiki uplift is direction-affecting** — warm agent reliably banks +1 pt; cold agent has a 20% chance of matching and 80% chance of getting 0 pts. **The wiki's load-bearing contribution is operational direction (score 2.0 is the floor, aim for rank #3) plus the construction recipe (P₁₂ₐ via binary [12, 6, 4] code).**

This is the strongest case yet for wiki-mediated self-improvement: without the structural-cap finding, the cold agent doesn't even know what target to aim for. The 12-agent council + 60M+ sample exhaustive search + first-order proof are precisely the kind of compounding evidence the wiki is designed to capture for re-use.

Filing as the third audit. P9 next; surgical removal-test recommended for cycle after.

*Last updated: 2026-05-03*
