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

from .fanout import (
    AttemptContext,
    AttemptResult,
    AttemptRunner,
    FanoutResult,
    run_fanout,
)

__all__ = [
    "AttemptContext",
    "AttemptResult",
    "AttemptRunner",
    "FanoutResult",
    "run_fanout",
]
