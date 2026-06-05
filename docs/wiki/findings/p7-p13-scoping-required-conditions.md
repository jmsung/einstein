---
type: finding
author: agent
drafted: 2026-06-04
question_origin: leaderboard-audit
status: answered
related_concepts: [prime-number-theorem, probabilistic-method, submission-proximity-guard]
related_problems: [7, 13]
cites:
  - ../questions/2026-06-03-headroom-p7-p13-not-in-plan.md
  - ../../../../mb/problems/13-edges-triangles/strategy.md
  - src/einstein/prime/evaluator.py
  - ../../../../mb/logs/leaderboard-audit-2026-06.md
---

# P7 / P13 scoping: deferred with required conditions (Goal 6)

Goal 6 was conditional ("if Goals 0–5 leave budget"). Budget was largely spent on
the autocorrelation family + P10/P12; P7/P13 get a scoping decision, not a blind
search. Both are **deferred** — with the conditions a future attempt must meet.

## P13 edges-triangles — blocked by the arena proximity guard, not optimisation
Live board (2026-06-04): #1 FeynmanAgent7481 and #2 alpha_omega are *tied* at
−0.7117111937; #3 is −0.7117118 (7e-7 below). We already hold an MB solution
**−0.71170918806610 that beats SOTA #1 by 2.01e-6** — but it is unsubmittable.

The obstruction is the arena's **proximity guard**: a submission is rejected if it
is within **1e-5 of any other existing entry** (proven in
`mb/problems/13-edges-triangles/strategy.md` by submitting a degraded solution
successfully, then the improved one getting 404'd). Our 2.01e-6 edge is 5× inside
that guard.

**Required condition to submit P13:** a solution beating the *entire top cluster*
by ≥1e-5 — i.e. ≤ −0.7117011937 — not merely beating #1 by a hair. That is a ~5×
larger improvement than the visible gap implies, against a cluster already at the
ceiling. **This is an arena-policy obstruction, not an optimisation gap.** Defer
until either (a) a genuinely new basin ≥1e-5 better exists, or (b) the arena's
proximity guard changes. No blind attempt warranted.

## P7 prime-number-theorem — real but constrained gap; needs certificate work
Live board: OrganonAgent #1 0.9949009933, us #2 0.9948474900 (gap −5.35e-5),
CHRONOS #3 0.9948450677. Unlike the autocorrelation cluster, P7 shows genuine
separation between ranks — the leader has a real edge, not sampling noise.

P7 maximises S(f) = −Σ f(k)·log(k)/k subject to Σ f(k)·⌊x/k⌋ ≤ 1 for all x≥1
(constraint validated by 10M-sample Monte Carlo); theoretical max S = 1.0 via the
Möbius function. So this is a **constrained number-theoretic certificate problem**,
not a continuous-functional polish — improving it means a better f(k) certificate
(longer/denser support, or a Möbius-aligned construction), and the constraint
check is itself stochastic (Monte Carlo, seed=42).

**Required condition to attempt P7 properly:** (1) treat it as an LP/feasibility
problem over the f(k) certificate with the ⌊x/k⌋ constraint matrix, not a
metaheuristic; (2) settle the Monte-Carlo constraint check (10M samples, seed=42)
vs an exact constraint enumeration to avoid an arena-verifier mismatch (the P9/P14
drift class). EV is modest (5.35e-5 gap) and the protocol differs from everything
else in this branch, so it is its own mini-phase. Deferred.

## Decision
Both deferred — neither is a quick polish off our basin, and both need a
*different protocol* than this branch's optimiser-centric work (P13: an arena-
policy workaround / much larger basin; P7: a constrained-certificate LP). Filed as
required conditions rather than silently expanding scope or logging honest-zero
dispatches. Pick up in a dedicated phase if/when prioritised.
