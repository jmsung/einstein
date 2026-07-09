---
type: finding
author: agent
drafted: 2026-05-25
question_origin: knowledge/wiki/questions/2026-05-24-p14-strict-tol-manifest-wiring.md
status: answered
related_concepts: [float64-ceiling, arena-tolerance-drift, basin-rigidity]
cites:
  - src/einstein/optimizer_manifest.yaml
  - scripts/circle_packing_square/slsqp_polish.py
  - knowledge/wiki/findings/dead-end-newton-max-strict-tol-lockout-p14.md
  - knowledge/wiki/questions/2026-05-24-p14-strict-tol-manifest-wiring.md
  - results/circle_packing_square/slsqp_polish_result.json
---

# P14 manifest wire-fix verified — slsqp_polish is the strict-tol-safe default

## What we verified

Autonomous-loop cycle 52 (2026-05-25) ran
`uv run python -m einstein.optimizer_dispatch --problem-id 14 --strategy slsqp_polish`
end-to-end against the post-fix manifest. The dispatch:

- exited 0,
- wrote `results/circle_packing_square/slsqp_polish_result.json` in the
  `json_score_payload` shape (`{"score": float, "payload": {"circles": [...]}}`),
- produced score **2.6359830849175245** — exactly the held rank-#2 strict-disjoint
  basin from the original 2026-04-08 / 04-09 campaign (matches `mb/problems/14-…/experiment-log.md` final number to all 16 digits).

This closes the open question
[`2026-05-24-p14-strict-tol-manifest-wiring`](../questions/2026-05-24-p14-strict-tol-manifest-wiring.md)
and lifts the structural blocker recorded in
[`dead-end-newton-max-strict-tol-lockout-p14`](dead-end-newton-max-strict-tol-lockout-p14.md).

## Manifest state (verified)

```yaml
14:
  slug: circle-packing-square
  default: slsqp_polish               # strict tol=0 by construction
  optimizers:
    slsqp_polish:
      script: scripts/circle_packing_square/slsqp_polish.py
      cli_args: []
      timeout_seconds: 300
      result_file: results/circle_packing_square/slsqp_polish_result.json
      result_parser: json_score_payload
    newton_max:
      script: scripts/circle_packing_square/newton_max.py
      cli_args: ["--pair-gap", "0"]   # forces strict-disjoint (axiom A1)
      timeout_seconds: 1800
      result_file: results/circle_packing_square/newton_max_result.json
      result_parser: json_score_payload
```

The `newton_max` block stays available but its tolerance-band exploit is now
disarmed at the manifest level — even an explicit `--strategy newton_max` pick
runs strict-disjoint. Prior cycles (47–49) failed precisely because empty
`cli_args` let the script's `--pair-gap=-9e-10` default through.

## What this rules out

- The "P14 dispatch is structurally lockout" narrative from cycles 47–51. The
  autonomous loop can now produce a strict-tol-safe candidate for P14 on every
  cycle. Cycle hygiene restored.
- The "every P14 cycle costs an attempt to `dispatch-failed`" failure mode.
  `dispatch-failed` was an upstream wiring bug, not a property of the problem.

## What this does NOT change

- **P14 score remains float64-ceiling-locked at 2.6359830849175245.** The
  wire-fix is purely about cycle hygiene; it does **not** unlock new headroom.
  Arena #1 (AlphaEvolve, 2.6359830849176) sits 8e-14 above this in float64-ulp
  terms — unreachable without mpmath ulp polish AND a verifier with mpmath-grade
  tolerance handling on the arena side.
- The submission policy is unchanged: 2.6359830849175245 is rank #2, not a
  strict improvement over arena #1, so auto-submit gates (axioms A1 + arena
  leaderboard) correctly reject. Held score on the leaderboard remains rank #2.

## What might still work for actual P14 rank improvement

This is intentionally a short list; cycle 49's dead-end and the experiment log
exhausted the basin survey of 2026-04-08 / 04-09. The remaining doors are:

- **mpmath-ulp-polish** (existing technique, hit-rate 5/8 = 0.62 on
  float64-ceiling family). Would need a new manifest entry pointing at a
  strict-disjoint mpmath polish wrapper. Skill library shows the technique is
  proven on other float64-ceiling problems.
- **Different basin discovery via Voronoi or higher-symmetry init**
  (Hardin-Sloane, n=26 sub-grids). The 10-approach 2026-04-08 survey ruled out
  the obvious ones; remaining ones are exotic and low-EV.
- Both are gated on someone having tooling-bandwidth to wire a new optimizer
  block; neither is auto-runnable today.

## See also

- [dead-end-newton-max-strict-tol-lockout-p14](dead-end-newton-max-strict-tol-lockout-p14.md)
- [float64-ceiling](float64-ceiling.md)
- [arena-proximity-guard](arena-proximity-guard.md)
- [packing-techniques](packing-techniques.md)
