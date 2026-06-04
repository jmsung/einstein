---
type: finding
author: agent
drafted: 2026-06-04
question_origin: problem-3
status: answered
related_concepts: [autocorrelation-inequality, cross-resolution-basin-transfer, triple-verify]
related_problems: [3]
cites:
  - ../findings/autocorrelation-family-displaced-2026-06.md
  - src/einstein/autocorrelation/evaluator.py
  - src/einstein/triple_verify/problems/p03_autocorrelation.py
  - mb/logs/leaderboard-audit-2026-06.md
---

# Dead end: promoting the 1.6M-resolution P3 solution as a seed (resolution inflation)

## What we tried
While backfilling P3's seed (Phase 6, Goal 4) we found two classes of local
solution in `mb/problems/3-autocorrelation/solutions/`:
- a 1.6M-point raw array scoring **C2 = 0.9627189978** locally, *above* arena #1
  (ClaudeExplorer 0.9626433);
- a 100k reclaim basin scoring **0.962273842954706**, consistent with our arena
  board score (0.9622135, rank #3).

The tempting move: promote the 1.6M solution (it "beats #1" locally).

## Why it failed (the obstruction)
**The P3 score C2 = ‖f★f‖₂²/(‖f★f‖₁·‖f★f‖∞) is resolution-dependent**, and the
1.6M number does not transfer to the arena. Evidence:
- Our arena board score is 0.9622, not 0.9627 — i.e., when we actually submitted
  our best attempts, the arena scored them ~4e-4 *below* the high-res local
  value. The leaders (ClaudeExplorer 0.9626) sit between, holding rank #1.
- The wiki's own P3 wisdom hook (`autocorrelation-family-displaced-2026-06.md`)
  is literally "cross-resolution downsampling creates distinct basins" — the
  high-res raw and the submitted/arena-resolution function are *different points*
  with different scores.
- Naive decimation is not a valid downsample (it destroys the fine function), so
  the high-res 0.9627 is not even a stable quantity under resolution change.

So the 1.6M 0.9627 is a **resolution artifact**, not a submittable record.

## What this rules out
- **Promoting a higher-resolution solution to "beat" a ratio-style autocorrelation
  SOTA.** For any score that is a discretised functional ratio (P2/P3/P4), the
  number is only meaningful *at the arena's evaluation resolution*. A local score
  computed at a different resolution is not comparable to the leaderboard.
- **Trusting a single-resolution triple-verify to gate a submission on this
  family.** Three checks that all run at 1.6M would *agree* on 0.9627 and still
  be wrong about the arena. The danger is acute now that auto-submit is armed: a
  1.6M seed would make `verify_seed` report a false record and could trip a false
  auto-submission (the 2026-04-09 false-breakthrough class).

## What we did instead
Promoted the **100k board-consistent** reclaim seed (0.962273842954706, honestly
below arena #1). Triple-verify (fast / fftconvolve / mpmath) agrees to ~2e-14 at
that resolution. P3 stays a non-submittable headroom target.

## What might still work (Phase 7)
- Treat P3 as a **new-basin** problem, not polish (the +4.30e-4 gap is ~3× our
  prior tie-break improvement). Re-attempt cross-resolution transplant with a
  *valid* downsampling kernel (band-limited / anti-aliased), 4M → 100k, and
  re-score at the arena resolution.
- Before any P3 submission: add a cross-resolution agreement check to gate 2 —
  the score must be stable when re-discretised at the arena's resolution, not
  just self-consistent at the local one.
