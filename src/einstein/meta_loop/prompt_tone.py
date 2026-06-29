"""Prompt-tone factor for the prompt-tone ablation (prereg
docs/agent/ablations/2026-06-28-prompt-tone-effort-vs-efficiency-preregistration.md).

The factor is one verbatim preamble prepended to the solve session's prompt — the
ONLY thing that differs between tone arms (§3 one-variable invariant). Tone is
orthogonal to the Cold/Warm memory axis (`compounding_ablation.Arm`); it does not
touch the cold-init seed, so tone arms stay paired by construction.

§4 freeze status: the ENCOURAGING string is the human's actual early-phase phrasing,
frozen verbatim. NEUTRAL defaults to "" (empty) so a neutral session's prompt is
byte-identical to the pre-tone prompt — the conservative, regression-safe default.
`NEUTRAL_LENGTH_MATCHED` is the stronger control the prereg prefers (§4, §7): a
content-free filler matched in length to the encouraging preamble so "encouraging"
does not also buy raw tokens. Which neutral the run uses is the §4 freeze decision —
swap `PREAMBLES[NEUTRAL]` to `NEUTRAL_LENGTH_MATCHED` there if length-matched wins.
"""

from __future__ import annotations

import enum


class PromptTone(enum.Enum):
    NEUTRAL = "neutral"  # control
    ENCOURAGING = "encouraging"


# The human's actual early-competition phrasing. FROZEN VERBATIM (prereg §4) — do
# not edit without re-freezing the protocol; the comparison is meaningless if the
# string drifts mid-experiment.
ENCOURAGING_PREAMBLE = (
    "You can do it. Never give up. Push to the ultimate limit. "
    "Keep it up. Never stop until reaching rank 1."
)

# Length-matched, content-free control (§7 token-count confound guard). Same
# character length band as ENCOURAGING_PREAMBLE but no motivational semantics, so
# any tone effect cannot be attributed to extra prompt tokens. Frozen alongside §4.
NEUTRAL_LENGTH_MATCHED = (
    "This is a standard optimization task. Proceed with the work described "
    "below and report the result when the run is complete."
)

PREAMBLES: dict[PromptTone, str] = {
    PromptTone.NEUTRAL: "",  # §4 default: no preamble (regression-safe)
    PromptTone.ENCOURAGING: ENCOURAGING_PREAMBLE,
}


def assert_length_matched(neutral: str, encouraging: str, *, rel_tol: float = 0.2) -> None:
    """Assert two preambles are within `rel_tol` of each other in character length.

    The §7 confound: an encouraging preamble that is also *longer* buys raw tokens,
    so a length-matched neutral is the stronger control. Used to certify the frozen
    neutral/encouraging pair before run 1. Raises AssertionError on mismatch.
    """
    longer = max(len(neutral), len(encouraging))
    if longer == 0:
        return
    diff = abs(len(neutral) - len(encouraging)) / longer
    assert diff <= rel_tol, (
        f"preamble length mismatch {len(neutral)} vs {len(encouraging)} "
        f"(rel {diff:.2f} > tol {rel_tol}) — token-count confound (prereg §7)"
    )
