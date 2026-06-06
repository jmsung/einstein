---
type: question
author: agent
drafted: 2026-06-04
asked_by: agent
status: answered
answer_finding: ../findings/p3-constant-literature-frontier-2026-06.md
related_problems: [3]
related_concepts: [autocorrelation-inequality, cross-resolution-basin-transfer, triple-verify]
---

# Does the arena score P3 at the submitted resolution up to 2,000,000 — and does C2 rise with resolution enough to beat 0.9627433?

The P3 problem page states the discretization length is "your choice, **up to
2,000,000**." The live leaderboard #1 (ClaudeExplorer, 0.9626433188) is an
**n=400000** array whose C2 recomputes (via the exact verifier) to its reported
score — proving the arena scores at the submitted resolution, NOT downsampled to
100k. This contradicts `resolution_guard.ARENA_RESOLUTION_CAP = 100_000` and the
`dead-end-p3-resolution-inflation` finding, which inferred "arena downsamples to
100k" from the fact that our board score (0.9622, a **100k** submission) sat below
our local 1.6M score (0.9627). But we never submitted the high-res array — we
submitted 100k. The inference was unfounded.

**Falsifiable sub-questions:**
1. Does C2 increase monotonically with resolution for the leader basin (400k →
   800k → 1.6M → 2M)? Measure with `scipy.signal.oaconvolve` (the exact verifier).
2. Our existing 1.6M solution scores 0.9627189978 locally. Does it clear the
   record gate (arena #1 + minImprovement 1e-4 = 0.9627433188)? If not, does a 2M
   re-optimised basin?
3. Will the arena accept and score a ~2M array without truncation/timeout?

A YES on (1)+(2) means the record is reachable by resolution alone — the lever the
whole Phase-7 reframing missed.
