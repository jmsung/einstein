---
type: finding
author: agent
drafted: 2026-06-04
question_origin: problem-3
status: answered
related_concepts: [autocorrelation-inequality, discretization-as-structure, triple-verify]
related_problems: [2, 3, 4]
cites:
  - ./dead-end-p3-resolution-inflation.md
  - ./dead-end-p3-antialias-transplant-fails.md
  - src/einstein/triple_verify/resolution_guard.py
  - ../questions/2026-06-04-p3-headroom-hilbert-agreement-test.md
---

# Dead end: a *numerical* cross-resolution agreement predicate for the autocorrelation family

## What we tried
Phase 8 set out to wire Hilbert's cross-resolution agreement predicate into the
P3/P4 triple-verify as a gate-2 prerequisite: re-discretise the candidate f to a
finer grid and require the score to be stable (so a resolution-inflated score —
high at fine resolution, low at the arena's — is rejected).

## Why it failed (the obstruction)
**The functional is resolution-dependent for *every* f, not just inflated ones**,
so a stability threshold cannot separate good from inflated. Measured: a clean
100k-native P3 seed (0.9622738) re-scored after a 2× linear-interp upsample gives
0.9616704 — a shift of **−6.0e-4**, far larger than any submission tolerance. The
decimated 1.6M solution shifts +8.1e-2. Both are "unstable" by any tolerance that
would also pass legitimate solutions; the predicate has no discriminating
threshold.

The root cause: re-discretising f (by interpolation) produces a *different
function*, and the C2 = ‖f★f‖₂²/(‖f★f‖₁·‖f★f‖∞) ratio of that different function
is legitimately different. There is no resolution-invariant "the same f at higher
resolution" for a point-sampled array — the in-between values are an arbitrary
modelling choice the arena never sees.

## What this rules out
- **A numerical resolution-stability gate for P2/P3/P4 submissions.** No
  re-discretisation-agreement threshold both passes clean solutions and rejects
  inflated ones.

## What works instead (the procedural guard)
The only safe rule is procedural, and it is simple: **score the exact array you
submit, at a length within the arena cap (100k).** A score computed at any other
resolution is not comparable to the leaderboard. Implemented as
`einstein.triple_verify.resolution_guard.assert_arena_resolution` (rejects empty
or over-cap arrays) and already enforced for the *value* by running the per-array
triple-verify on the exact submission payload. The P3 resolution-inflation false
record came from violating the procedure (scoring at 1.6M, claiming vs a 100k
board), not from a missing numerical check.

So Hilbert's question resolves to: there is no numerical predicate; the guard is
"don't change resolution between scoring and submitting," enforced procedurally.
