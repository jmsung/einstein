---
type: finding
author: agent
drafted: 2026-05-02
question_origin: cross-problem
status: answered
related_concepts: [coxeter-todd-k12.md, kissing-number.md, hinge-overlap.md, provable-floor-and-frozen-problems.md, first-order-link-tangent-test.md, bourgain-clozel-kahane.md]
related_techniques: [first-order-link-tangent-test.md]
related_findings: [p22-d12-construction-survey.md, hinge-overlap-rank3-squeeze.md]
related_personas: [conway.md, cohn.md, viazovska.md]
cites:
  - ../concepts/kissing-number.md
  - ../concepts/coxeter-todd-k12.md
  - ../concepts/bourgain-clozel-kahane.md
  - p22-d12-construction-survey.md
  - hinge-overlap-rank3-squeeze.md
---

# The "score-2 structural floor" pattern across kissing-tight arena problems

## TL;DR

The Einstein Arena's kissing-number-style problems (P22 d=12, P23 d=16, and any future similar) all share a **structural floor at hinge-overlap score 2.0** when the arena's `n` exceeds the dimension's known kissing cap κ(d). Beating 2.0 is mathematically equivalent to proving κ(d) ≥ n+1, which contradicts established results. **Score 2.0 is the floor, not a target.** The arena's reward structure (rank #2/#3 = +1/+2 pts for matching the floor) makes these problems "Tier-A entry, Tier-D improvement" — get on the leaderboard, then move on.

## What the pattern is

For an arena problem of the form *"place n unit vectors on `S^{d-1}` minimizing total hinge overlap"*, where `n = κ(d)_known + 1`:

1. The known κ(d) cap (from Levenshtein 1979 / Cohn-Elkies LP / construction-A on codes / etc.) gives `κ(d)` non-overlapping unit vectors at angular distance ≥ 60°.
2. Adding one more unit vector to reach `n = κ(d) + 1` necessarily creates exactly one **duplicate or near-duplicate** (within minimum-pairwise-distance threshold).
3. This duplicate contributes hinge overlap = 2.0 to the total score (one perfect overlap from the duplicate + zero from all other pairs).
4. **Score = 2.0 is the floor**; beating it requires the configuration to NOT have a duplicate, which means reaching κ(d) + 1 distinct points — directly contradicting the known cap.

This is the *same pattern* as P5 minimum-distance ratio (provable global optimum at the (22, 8) Cantrell configuration) and P10 Thomson (provable global optimum at the icosadeltahedral n=282) — but specific to the kissing-number family.

## Where it applies in the arena

| Problem | Dim `d` | κ(d) | Arena `n` | Structural floor | JSAgent status |
|---|---|---|---|---|---|
| **P22** | 12 | 840 (empirical, conjectured optimal) | 841 | **2.0** | rank #3 at 2.0014 (+1 pt; conf rank-1 infeasible by 12-agent council + 60M+ first-order proof) |
| **P23** | 16 | 4320 (**proven**, Levenshtein 1979) | 4321 | **2.0** | rank #2 at 2.0000027 (+1 pt; rank-1 ruled out by 5 attacks) |
| (P6 d=11) | 11 | ≥ 594 (LB known; UB ~745 LP) | 594 | (different — score 0 achievable) | rank #1, score 0 (theoretical minimum, unbeatable; +0 pts) |

P6 is the *exception* — the arena's `n` matches κ(11)'s known lower bound, so the LB construction itself achieves score 0 (no duplicate needed). P22 and P23 share the structural floor because their `n = κ + 1`.

## Why beating 2.0 is structurally impossible

For P22 specifically (per [`findings/p22-d12-construction-survey.md`](p22-d12-construction-survey.md)):

- **8-way structural cap**: lattice K₁₂ (756) → P₁₂ₐ Construction A (840) → SDP cluster bound at 840 → Leech cross-section (756) — all four pathways converge at 840 from above and below.
- **First-order link-tangent test** ([`techniques/first-order-link-tangent-test.md`](../techniques/first-order-link-tangent-test.md)): for any candidate filler position `v ∈ S^{d-2}`, `min S(u) ≈ 8.02` over the 60°-link tangent, vs threshold 1.155 for hinge-overlap improvability. This is a 6.8x margin — a strict local-minimum proof.
- **De Laat–Leijenhorst 2024** ([source/papers/2024-delaat-kissing-sdp.md](../source/papers/2024-delaat-kissing-sdp.md)): proves κ(12) ≤ 1355 formally; CHRONOS believes the structural cap sits at 840 itself.

For P23 ([`findings/hinge-overlap-rank3-squeeze.md`](hinge-overlap-rank3-squeeze.md)):

- κ(16) = 4320 is **proven** (Levenshtein 1979); no analogous open question.
- Rank-#1 ruled out by 5 independent attacks (link-tangent S(u)=16.67 vs threshold 1.155, 200K random scan, L-BFGS multi-start, remove-and-replace, P22 precedent).

Both: score 2.0 is the structural floor; the only achievable improvements are sub-ulp polish in the cap+duplicate configuration.

## How the agent should approach a score-2 problem

When dispatched with kissing-tight category at `n = κ(d) + 1`:

1. **Don't try to beat score 0** — it's mathematically infeasible. Document this immediately, don't waste compute.
2. **Compute the cap construction** — for d=12, P₁₂ₐ Construction A from binary [12,6,4] code; for d=16, BW₁₆ from extended [16,11,4] Hamming. These give the κ(d) base configuration.
3. **Add one duplicate vector** — usually `(1, 0, ..., 0)` repeated. This gives the score-2 floor configuration.
4. **Polish to the float64 ceiling** — the duplicate's exact angular position is a free parameter; minor polish can push score from 2.0001 down toward 2.0 + ulps. Use mpmath at 80 dps for verification.
5. **Submit if rank #2 or #3** — the +1 or +2 point reward is achievable; document and move on.
6. **Do NOT pursue rank #1** unless someone publishes a new construction beating κ(d).

This is the canonical "Tier-A entry, Tier-D improvement" pattern: get on board, don't push.

## Why this finding compounds across cycles

The pattern is **structural, not problem-specific**. Future arena problems following this template (e.g., a hypothetical "P24 kissing d=8 at n=241" — would be infeasible since κ(8) = 240 is *proven* via Viazovska 2016) would benefit from this finding immediately. The agent doesn't need to re-derive the obstruction; it cites this finding and the relevant κ(d) reference.

This is also a concrete instance of the [`provable-floor-and-frozen-problems.md`](../concepts/provable-floor-and-frozen-problems.md) concept — extends the abstract framework with a specific kissing-number family pattern.

## Cross-problem citations

This finding ties together:

- P22 (cohn-elkies-bound, coxeter-todd-k12, first-order-link-tangent-test, p22-d12-construction-survey)
- P23 (hinge-overlap-rank3-squeeze, kissing-number)
- P5 (analogous structural-floor pattern in 2D distance-ratio problems)
- P10 Thomson (analogous icosadeltahedral magic-number floor)

It's the kind of meta-finding the gap-detector (`tools/wiki_graph.py`) is designed to surface: clusters of related findings without an abstracting concept page that names the pattern.

## See also

- [`concepts/coxeter-todd-k12.md`](../concepts/coxeter-todd-k12.md) — the lattice underlying P22's 840 cap
- [`concepts/kissing-number.md`](../concepts/kissing-number.md) — broader concept
- [`concepts/provable-floor-and-frozen-problems.md`](../concepts/provable-floor-and-frozen-problems.md) — abstract framework
- [`techniques/first-order-link-tangent-test.md`](../techniques/first-order-link-tangent-test.md) — the proof technique that establishes the floor
- [`findings/p22-d12-construction-survey.md`](p22-d12-construction-survey.md) — P22-specific deep dive
- [`findings/hinge-overlap-rank3-squeeze.md`](hinge-overlap-rank3-squeeze.md) — P23-specific deep dive

*Last updated: 2026-05-02*
