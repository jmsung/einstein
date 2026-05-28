"""thompson.py — Thompson sampler over (category, technique) skill arms.

Pure, seeded posterior-sampling bandit. Each `(category, technique)` row in
`docs/agent/skill-library.md` is one Bernoulli arm: `top3` successes in
`tried` pulls of "did this technique reach top-3 on this category?". The
conjugate posterior is `Beta(top3+1, tried-top3+1)` (uniform `Beta(1,1)` for
an unpulled arm). `pick()` draws one θ per masked arm and returns the argmax
— exploration is automatic and proportional to posterior variance, which is
exactly right for the library's sparse, warm-started counts.

Why Beta-Bernoulli (not UCB / ε-greedy): see
`docs/wiki/findings/beta-bernoulli-skill-bandit-posterior.md`.

Design contract (from the branch file):
  - `ThompsonSampler.pick(category, *, rng) -> PickResult | None`
  - per-category arm masking (don't sample autocorrelation arms for kissing)
  - uniform `Beta(1,1)` prior for unseen / empty-history arms
  - pure function of (skill-library state, category, seeded rng)

The sampler reuses `docs/tools/strategy_picker.py` for skill-library parsing
and category matching — no duplicate parser. The math (`sample_arms`) is
separated from the I/O (`ThompsonSampler.pick`) so it is trivially testable
without a file.
"""

from __future__ import annotations

import random
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Protocol, Sequence

# src/einstein/bandit/thompson.py → parents[3] == repo root.
_REPO = Path(__file__).resolve().parents[3]
DEFAULT_LIBRARY = _REPO / "docs" / "agent" / "skill-library.md"


class _Row(Protocol):
    """Duck type for a parsed skill-library row (strategy_picker.SkillRow)."""

    technique: str
    category: str
    tried: int
    top3: int


def _strategy_picker():
    """Lazily import docs/tools/strategy_picker (script-style layout)."""
    tools = _REPO / "docs" / "tools"
    if str(tools) not in sys.path:
        sys.path.insert(0, str(tools))
    import strategy_picker  # type: ignore[import-not-found]

    return strategy_picker


# ---------------- arms ----------------


@dataclass(frozen=True)
class Arm:
    """One Beta-Bernoulli arm: technique with posterior Beta(alpha, beta)."""

    technique: str
    alpha: float
    beta: float

    @property
    def mean(self) -> float:
        """Posterior mean = Laplace-smoothed hit-rate (top3+1)/(tried+2)."""
        return self.alpha / (self.alpha + self.beta)


def arm_from_row(row: _Row) -> Arm:
    """Build a Beta-Bernoulli arm from a skill-library row.

    `Beta(top3+1, tried-top3+1)`. Guards against malformed rows where
    `top3 > tried` (would give beta < 1) by flooring beta's count at 0, so
    the worst case is the uniform `Beta(1,1)` prior, never an improper Beta.
    """
    top3 = max(0, int(row.top3))
    tried = max(top3, int(row.tried))
    return Arm(technique=row.technique, alpha=top3 + 1.0, beta=(tried - top3) + 1.0)


# ---------------- pick result ----------------


def _fmt_count(x: float) -> str:
    """Render an alpha/beta as an int when integral (Beta(4,2) not Beta(4.0,2.0))."""
    return str(int(x)) if float(x).is_integer() else f"{x:g}"


@dataclass(frozen=True)
class PickResult:
    """The winning arm plus the audit fields the cycle-log note needs (G4)."""

    technique: str
    alpha: float
    beta: float
    theta: float  # the posterior draw that won this pick
    n_arms: int  # how many arms were in contention (after masking)

    @property
    def prior_str(self) -> str:
        return f"Beta({_fmt_count(self.alpha)},{_fmt_count(self.beta)})"

    def note(self) -> str:
        """`technique=foo prior=Beta(4,2) sampled_θ=0.71` for the cycle-log."""
        return f"technique={self.technique} prior={self.prior_str} " f"sampled_θ={self.theta:.2f}"


# ---------------- the sampler ----------------


def sample_arms(arms: Sequence[Arm], *, rng: random.Random) -> PickResult | None:
    """Draw one θ ~ Beta(α,β) per arm; return the argmax as a PickResult.

    Pure: depends only on `arms` and the state of `rng`. Returns None for an
    empty arm set (no technique tagged for the category → caller falls back to
    council dispatch, mirroring strategy_picker's empty-pick behavior).

    Ties (equal θ, vanishingly unlikely with continuous Beta draws) resolve to
    the first arm by iteration order for determinism.
    """
    if not arms:
        return None
    best: tuple[float, Arm] | None = None
    for arm in arms:
        theta = rng.betavariate(arm.alpha, arm.beta)
        if best is None or theta > best[0]:
            best = (theta, arm)
    assert best is not None  # arms non-empty
    theta, arm = best
    return PickResult(
        technique=arm.technique,
        alpha=arm.alpha,
        beta=arm.beta,
        theta=theta,
        n_arms=len(arms),
    )


class ThompsonSampler:
    """Thompson sampler reading `docs/agent/skill-library.md`.

    `rows` may be injected (tests, or a caller that already parsed the
    library) to skip file I/O — keeps the sampler a pure function of state.
    """

    def __init__(
        self,
        library_path: Path = DEFAULT_LIBRARY,
        *,
        rows: Sequence[_Row] | None = None,
    ) -> None:
        self.library_path = library_path
        self._rows = rows

    def _load_rows(self) -> list[_Row]:
        if self._rows is not None:
            return list(self._rows)
        sp = _strategy_picker()
        return sp.load_skill_library(self.library_path)

    def arms_for(self, category: str, *, avoid: set[str] | None = None) -> list[Arm]:
        """Per-category masked arm set. `avoid` drops already-tried techniques
        (used by multi-attempt visits so the bandit doesn't repeat itself)."""
        sp = _strategy_picker()
        avoid = avoid or set()
        return [
            arm_from_row(r)
            for r in self._load_rows()
            if sp.category_matches(r.category, category) and r.technique not in avoid
        ]

    def pick(
        self,
        category: str,
        *,
        rng: random.Random,
        avoid: set[str] | None = None,
    ) -> PickResult | None:
        """Sample one technique for `category`. None if no arm matches."""
        return sample_arms(self.arms_for(category, avoid=avoid), rng=rng)


__all__ = [
    "Arm",
    "PickResult",
    "ThompsonSampler",
    "arm_from_row",
    "sample_arms",
]
