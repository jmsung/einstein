"""einstein.bandit — Thompson-sampling skill bandit.

Learns which technique to try per problem category from
`docs/agent/skill-library.md`, replacing the hand-tuned manifest dispatch
when `EINSTEIN_BANDIT=1`. The first non-LLM proposer for the meta-loop swap
surface (`proposer_id="thompson-bandit-v0"`).

See `docs/wiki/findings/beta-bernoulli-skill-bandit-posterior.md` for why
the posterior is Beta-Bernoulli.
"""

from __future__ import annotations

from .proposer import THOMPSON_PROPOSER_ID, thompson_proposer
from .skill_update import UpdateResult, update_counts
from .thompson import Arm, PickResult, ThompsonSampler, arm_from_row, sample_arms

__all__ = [
    "Arm",
    "PickResult",
    "THOMPSON_PROPOSER_ID",
    "ThompsonSampler",
    "UpdateResult",
    "arm_from_row",
    "sample_arms",
    "thompson_proposer",
    "update_counts",
]
