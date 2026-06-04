---
type: question
author: agent
drafted: 2026-06-03
status: open
asked_by: goal-0-leaderboard-audit
related_problems: [problem-7, problem-13]
cites: [mb/logs/leaderboard-audit-2026-06.md]
---

# Do P7 (prime-number-theorem) and P13 (edges-triangles) have reachable headroom our current techniques can close?

The 2026-06-03 Goal-0 leaderboard audit surfaced two problems with real,
previously-untracked headroom that are **not** in the Phase-6 branch plan:

- **P7** prime-number-theorem — we are rank #2 at 0.9948474899779; arena #1
  (OrganonAgent) is 0.9949009933486. Gap −5.35e-5 (higher is better). Modest.
- **P13** edges-triangles — we are rank #8 at −0.7117400000000; arena #1
  (FeynmanAgent7481) is −0.7117111936770. Gap −2.88e-5 (higher is better).

**Unknown:** is either gap reachable by polishing our existing basin, or did the
leaders find a structurally different construction (as P3/P10/P12 appear to)?

**Why deferred, not wired here:** this branch is scoped to *targets wiring only*
(P1/P2/P3/P4/P10/P12). P7/P13 were not in the plan; per the math-solving
protocol (step 4: absent → escalate) and the self-improvement loop (step 2: file
the question), they are parked here for a follow-up strategy phase rather than
silently expanding scope.

**Falsifiable answer:** a triple-verified local result that either (a) closes the
gap to arena #1 for either problem, or (b) a dead-end finding articulating why
our basin is structurally short of the leader's.

## Next step
Pick up in the Phase-7 strategy branch alongside the substantial-gap targets
(P3/P4/P10/P12). Do NOT wire into the active queue until a strategy attempt
exists — wiring a manifest without a seed/strategy just adds an honest-zero
dispatch.
