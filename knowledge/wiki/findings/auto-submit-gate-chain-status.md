---
type: finding
author: agent
drafted: 2026-06-03
question_origin: phase-5-triple-verify-wiring
status: answered
related_concepts: [minimprovement-gate, arena-tolerance-drift, float64-ceiling]
cites:
  - src/einstein/auto_submit.py
  - src/einstein/triple_verify/core.py
  - scripts/autonomous_loop.py
  - .claude/rules/axioms.md
  - knowledge/wiki/techniques/triple-verify.md
  - knowledge/wiki/findings/triple-verify-wiring-design.md
---

# Auto-submit gate chain status — gate 2 is now real (Phase 5)

## The blocker (before this branch)

The 6-gate auto-submit chain (`auto_submit.try_submit`, axiom A2's revised
gate-chain policy) was a no-op at **gate 2**: `autonomous_loop.py` hardcoded
`triple_verify={"passed": False, "note": "triple-verify not yet wired"}`. Gate 2
hard-rejects any candidate whose `triple_verify["passed"]` is not truthy, so
**every** auto-submission was rejected regardless of `EINSTEIN_AUTO_SUBMIT`.
Flipping the kill switch live was a no-op. Phase 4's dry-run
(`mb/logs/record-campaign-gate.md`) confirmed the safety/scoping pipeline worked
but could not exercise an accept-at-gate-2 path.

## Status now (after `js/feat/triple-verify-wiring`)

Gate 2 reads a **real per-problem verdict** from
`triple_verify.run_payload(problem_id, payload)` (see
[triple-verify technique](../techniques/triple-verify.md)). The 6 gates:

| # | gate | status |
|---|---|---|
| 1 | kill switch (`EINSTEIN_AUTO_SUBMIT=0`) | unchanged |
| 2 | **triple-verify** | **REAL** — 9 problems wired + P22 honest-unavailable; `not_registered` → reject |
| 3 | daily cap | unchanged |
| 4 | per-problem throttle | unchanged |
| 5 | arena #1 SOTA strict-improvement | unchanged |
| 6 | POST + audit | unchanged |

The campaign blocker is removed: flipping `EINSTEIN_AUTO_SUBMIT=1` is now a real
action, still bounded by gate 5 (must beat arena #1 by ≥ minImprovement), gate 4
(1h throttle), and gate 3 (daily cap).

## Verified end-to-end (P14)

Real rank-2 P14 seed → triple-verify passes (3-way Σr agreement) → gate 2 lets
it through → gate 5 rejects (`2.6359830849 < arena #1 2.6359830953`) → no POST
(`tests/circle_packing_square/test_p14_e2e_gate_chain.py`). Corroborated by
genuine `no-improvement` rows in `mb/logs/auto-submit.md` — reachable only after
gate 2 passes.

## What this unblocks

- The autocorrelation family ([autocorrelation-family-displaced-2026-06](autocorrelation-family-displaced-2026-06.md)):
  P2's tight 1.84e-7 gap is now the most-likely first auto-submission candidate
  once a polish run produces a strict improvement.
- **Next blocker: Phase 6** (`headroom-target-set`) — more manifest wiring +
  seeds. A problem must be both manifest-wired (dispatchable) and triple-verify
  registered (verifiable); the coverage gate keeps the two in lock-step.

See also: [triple-verify technique](../techniques/triple-verify.md),
[triple-verify-wiring-design](triple-verify-wiring-design.md),
Phase 4 gate log `mb/logs/record-campaign-gate.md`.
