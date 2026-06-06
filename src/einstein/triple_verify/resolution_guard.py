"""Procedural resolution guard for discretised-functional problems (P2/P3/P4/P12).

Phase-8 promotion of the resolution-comparability lesson from the autocorrelation
campaign. These problems score a *discretised* functional ratio that is only
meaningful at the resolution the array is scored on — comparing a score computed
at one resolution to a leaderboard scored at another caused the P3 resolution-
inflation false-record class (docs/wiki/findings/dead-end-p3-resolution-inflation.md).

WHY THIS IS PROCEDURAL, NOT NUMERICAL: we tried a *numerical* agreement predicate
(re-discretise f to a finer grid, require the score to be stable). It does not
discriminate — linear-interp upsampling shifts even a clean 100k-native P3 seed by
~6e-4, because the functional is genuinely resolution-dependent for ALL f, not
just inflated ones (docs/wiki/findings/dead-end-resolution-agreement-predicate.md).
The only safe rule is procedural: **score on the exact array you submit, at a
length within the arena cap.** A score computed at any other resolution is not
comparable to the leaderboard and must never back a submission claim.
"""

from __future__ import annotations

import numpy as np

# Arena payload cap for the autocorrelation family.
# CORRECTED 2026-06-04: the P3 problem page states the discretization length is
# "your choice, up to 2,000,000". The earlier 100_000 value was wrong — it came
# from the resolution-inflation episode, which mis-inferred a 100k downsample
# from the fact that our *board* score (a 100k submission) sat below our local
# high-res score. The live #1 (ClaudeExplorer, 0.9626433) is an n=400000 array
# whose C2 recomputes to its exact board score, proving the arena scores at the
# submitted length up to the 2M cap. See
# docs/wiki/findings/p3-resolution-is-the-lever-2026-06.md.
ARENA_RESOLUTION_CAP = 2_000_000


def assert_arena_resolution(values, *, cap: int = ARENA_RESOLUTION_CAP) -> int:
    """Return len(values) after asserting it is a valid arena submission length.

    Raises if the array is empty or exceeds the arena resolution cap — the two
    ways a discretised-functional score becomes non-comparable to the board
    (a longer array is silently truncated/rejected; the score you computed is
    then not the score the arena assigns).
    """
    n = len(np.asarray(values))
    if n == 0:
        raise ValueError("empty submission array")
    if n > cap:
        raise ValueError(
            f"submission length {n} exceeds arena cap {cap}; the arena will not "
            f"score this array at {n}, so the local score is not comparable. "
            f"Re-optimise/score at the cap before any submission claim."
        )
    return n
