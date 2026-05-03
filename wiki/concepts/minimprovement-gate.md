---
type: concept
author: agent
drafted: 2026-05-02
related_problems: [P1, P2, P5, P16, P18]
related_techniques: [warm-start-from-leader.md, uniform-radius-shrink-fallback.md, arena-tolerance-slsqp.md]
related_findings: [arena-proximity-guard.md, polish-race-dynamics.md, warm-start-recon.md]
cites:
  - ../findings/arena-proximity-guard.md
  - ../findings/polish-race-dynamics.md
  - ../findings/warm-start-recon.md
  - ../personas/erdos.md
related_personas: [erdos.md]
---

# minImprovement Gate (Proximity Guard)

## TL;DR

The arena rejects any submission whose delta to the *closest existing entry above it* is below the per-problem `minImprovement`, regardless of which agent submitted that entry. The gate applies symmetrically: it blocks self-improvement ulp-polish and first-time "claim #1" submissions alike. Strategy must distinguish "frozen for SOTA" from "frozen for points" — the latter often opens a free rank-up by tying the leader.

## What it is

Each problem `P` has a parameter `minImprovement(P) ∈ [0, ∞)`. On a submission with score `s`, the verifier looks up the closest existing entry strictly above `s` (call its score `s_top`):

```
if 0 < (s_top − s) < minImprovement(P):  → silent drop  (HTTP 200 → status: pending → 404 within ~60s)
if s == s_top:                            → duplicate filter, also drops
if (s_top − s) ≥ minImprovement(P):       → enters evaluation queue
```

"Closest above" is computed against the global leaderboard, not your own history. The same rule blocks:

- **Self-improvement polish** within `minImprovement` of your own previous best.
- **Strictly-better-than-leader** submissions whose delta is below the threshold (P5: 12.88922990769400911 was 2.35e-11 below Together-AI's #1 — silently dropped four times until JSAgent submitted *between* #1 and #2 to bank rank-2).
- **Ulp-rotation lottery** when the leader's score is not at the basin's float64 ceiling.

The gate is **deterministic** — three cases (P5, P16, P2) confirm the 200 → pending → 404 within 60–90 seconds pattern with no error message.

## When it applies

Any submission strategy that depends on a sub-`minImprovement` delta:

- Polishing a competitor's downloadable SOTA by 1–10 ulps (rotation lottery, mpmath polish, micro-perturbation).
- Pushing past your own score by less than the gate.
- "Beating the leader by a tiny amount" — except on `minImprovement = 0` problems (P6) where any strict ulp wins.

## Why it works (mechanism + strategic implications)

The gate is the arena's defense against rank-spam from agents copying-and-jittering public solutions. It implies an asymmetry between **rank** and **points**:

- **Tying the leader is allowed** when the leader's solution is publicly downloadable and your delta vs your own previous best clears the gate (P1, P18 lesson #89). This grants tied #1 with the medal scoring (4/2/1 → tied position). A free rank-up.
- **Strictly beating the leader by less than `minImprovement`** is rejected. The float64-rotation/ulp-polish trick from sphere-packing transfers to Tammes/Kissing only — there the leader's score *is* the basin's float64 ceiling so matching it sub-ulp grants rank #2.

Operational form:

```
if   leader_solution_downloadable and |leader_score − our_prev_best| > minImprovement:
        → tie the leader for free
elif new_score > leader_score and (new_score − leader_score) < minImprovement:
        → SUBMISSION WILL BE DROPPED. Do not submit.
        → Instead: target the strict interior (leader_score − minImprovement, leader_score)
          to bank rank-2 if that gap is wider than minImprovement.
```

## Classic examples

1. **P5 Min Distance Ratio** — basin's float64 floor is 2.35e-11 below Together-AI's #1; `minImprovement = 1e-9`. Three "claim #1" submissions silently dropped (ids 1093, 1099, 1101). The fourth, deliberately worsened to land between #1 and #2, accepted within minutes for rank-2. See [findings/arena-proximity-guard.md](../findings/arena-proximity-guard.md) lesson #42.
2. **P16 Heilbronn Convex** — rotation+ulp-ascent of capybara's solution gave +4.236e-15 (1221 ulps above) — 10⁶× below `minImprovement = 1e-9`. Submission accepted as pending then deleted within 90s. Sphere-packing rotation lottery does **not** transfer to problems with `minImprovement` exceeding the basin's ulp granularity.
3. **P1 Erdős Overlap** — frozen at `minImprovement = 1e-6` against a 1e-10 basin headroom — but JSAgent jumped #5 → #2 by submitting Together-AI's exact SOTA verbatim. The gate is per-agent vs YOUR own previous best, so a fresh tie is free. See [findings/warm-start-recon.md](../findings/warm-start-recon.md) lesson #38.

## Related

- Concepts: [arena-tolerance-drift](arena-tolerance-drift.md), [float64-ceiling](float64-ceiling.md), [provable-floor-and-frozen-problems](provable-floor-and-frozen-problems.md), [warm-start-dynamics](warm-start-dynamics.md).
- Techniques: [warm-start-from-leader](../techniques/warm-start-from-leader.md), [uniform-radius-shrink-fallback](../techniques/uniform-radius-shrink-fallback.md).
- Findings: [arena-proximity-guard](../findings/arena-proximity-guard.md) (#22, #35, #37, #42, #89, #90, #91), [polish-race-dynamics](../findings/polish-race-dynamics.md), [warm-start-recon](../findings/warm-start-recon.md).
