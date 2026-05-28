"""einstein.parallel — K-attempt fan-out per cycle (AlphaEvolve-shaped).

Replaces the single-attempt inner-loop with K diverse parallel attempts
(different seeds × techniques sampled from the Thompson skill bandit); the
arena verifier picks the winner. Pure orchestration; the real per-attempt
execution lives behind an injectable `runner` callable so unit tests don't
need to spin up the optimizer dispatch.

See `mb/active/js-feat-parallel-attempts.md` for the rationale + Goal 0
research note pinning down the K-pull Thompson semantics.
"""

from __future__ import annotations

from .dead_end_surface import (
    ARM_NOVELTY_TRIED_CAP,
    SCORE_GAP_REL_THRESHOLD,
    draft_stub,
    is_high_signal_loser,
    select_top_candidate,
)
from .fanout import (
    AttemptContext,
    AttemptResult,
    AttemptRunner,
    FanoutResult,
    run_fanout,
)

__all__ = [
    "ARM_NOVELTY_TRIED_CAP",
    "AttemptContext",
    "AttemptResult",
    "AttemptRunner",
    "FanoutResult",
    "SCORE_GAP_REL_THRESHOLD",
    "draft_stub",
    "is_high_signal_loser",
    "run_fanout",
    "select_top_candidate",
]
