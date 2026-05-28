#!/usr/bin/env python3
"""strategy_picker.py — pick (prior, novel) approaches per the autoresearch 1+1 rule.

Reads `docs/agent/skill-library.md` (which tracks technique hit rates per
category) and picks two approaches for the next attempt on a given
problem:

  - **prior**: highest hit-rate technique already attempted on this
    problem's category. The safe move that has worked before.
  - **novel**: technique with the strongest "finding" rate that is
    structurally different from the prior. The exploration arm.

Plus `convergence_detect()` — the helper that decides whether to keep
attempting or stop based on score-progress and gap-surfacing history.

Categories are inferred from problem_id via a static mapping derived
from `docs/wiki/problems/_inventory.md`. The library file may use
slash-separated multi-categories like "packing / kissing"; matching is
substring-based to handle this.

Usage:
    uv run python docs/tools/strategy_picker.py --problem-id 22
    uv run python docs/tools/strategy_picker.py --category sphere-packing
"""

from __future__ import annotations

import argparse
import logging
import re
from dataclasses import dataclass
from pathlib import Path

_REPO = Path(__file__).resolve().parents[2]
DEFAULT_LIBRARY = _REPO / "docs" / "agent" / "skill-library.md"

log = logging.getLogger("strategy_picker")


# ---------------- problem → category ----------------
# Derived from docs/wiki/problems/_inventory.md "Problem-family clustering".

_PROBLEM_CATEGORY: dict[int, str] = {
    # Autocorrelation family
    2: "autocorrelation",
    3: "autocorrelation",
    4: "autocorrelation",
    # Sphere packing / kissing family
    6: "sphere-packing",
    10: "sphere-packing",
    11: "sphere-packing",
    22: "sphere-packing",
    23: "sphere-packing",
    # Geometric packing (bounded region, 2D)
    5: "packing",
    14: "packing",
    17: "packing",  # 17a + 17b both
    18: "packing",
    # Discrete combinatorics
    12: "discrete-combinatorics",
    19: "discrete-combinatorics",
    21: "discrete-combinatorics",  # lean sum formula
    # Functional inequalities
    1: "functional-inequality",
    9: "functional-inequality",
    # Density / extremal
    7: "sieve",
    13: "extremal-graph",
    15: "extremal-graph",
    16: "extremal-graph",
}


def category_for(problem_id: int) -> str:
    """Return the canonical category for a problem id, or '?' if unknown."""
    return _PROBLEM_CATEGORY.get(problem_id, "?")


# ---------------- skill-library parsing ----------------


@dataclass
class SkillRow:
    technique: str
    category: str
    tried: int
    top3: int
    finding: int
    last_used: str
    hit_rate: float

    @property
    def finding_rate(self) -> float:
        return self.finding / self.tried if self.tried > 0 else 0.0


_ROW_RE = re.compile(
    r"^\|\s*`([^`]+)`\s*\|\s*([^|]+?)\s*\|\s*(\d+)\s*\|\s*(\d+)\s*\|"
    r"\s*(\d+)\s*\|\s*([0-9-]+|\S*)\s*\|\s*([0-9.]+)\s*\|\s*$"
)

# Public alias — the skill bandit's counter updater (src/einstein/bandit/
# skill_update.py) reuses this row pattern to rewrite a technique's counts.
# Groups: 1=technique 2=category 3=tried 4=top3 5=finding 6=last_used 7=hit_rate.
ROW_RE = _ROW_RE


def load_skill_library(path: Path) -> list[SkillRow]:
    """Parse the markdown table rows from skill-library.md.

    Rows with invalid columns (non-int tried/top3/finding, missing backtick
    technique cell, etc.) are silently skipped.
    """
    rows: list[SkillRow] = []
    for line in path.read_text().splitlines():
        m = _ROW_RE.match(line.strip())
        if not m:
            continue
        try:
            rows.append(
                SkillRow(
                    technique=m.group(1).strip(),
                    category=m.group(2).strip(),
                    tried=int(m.group(3)),
                    top3=int(m.group(4)),
                    finding=int(m.group(5)),
                    last_used=m.group(6).strip(),
                    hit_rate=float(m.group(7)),
                )
            )
        except ValueError:
            continue
    return rows


# ---------------- 1+1 pick ----------------


@dataclass
class StrategyPick:
    category: str
    prior: SkillRow | None
    novel: SkillRow | None
    rationale: str


def _category_matches(row_category: str, target: str) -> bool:
    """Slash-separated multi-category fields like 'packing / kissing' match
    if any segment substring-matches the target (or vice versa)."""
    target_lower = target.lower()
    for segment in re.split(r"[/,]", row_category.lower()):
        s = segment.strip()
        if not s:
            continue
        if s == target_lower or s in target_lower or target_lower in s:
            return True
    return False


# Public alias — the skill bandit (src/einstein/bandit/) reuses this matcher
# for per-category arm masking rather than re-implementing it.
category_matches = _category_matches


def pick_strategy(
    library_path: Path, *, category: str, avoid_techniques: set[str] | None = None
) -> StrategyPick:
    """Apply the autoresearch 1+1 rule: max 1 prior + max 1 novel per attempt.

    `avoid_techniques`: technique names to exclude from selection. Used by
    `run_one_visit` (Goal 7.4) to make attempts 2/3 within a visit avoid
    repeating the strategies that earlier attempts already picked. None or
    empty set = no exclusions.
    """
    rows = load_skill_library(library_path)
    candidates = [r for r in rows if _category_matches(r.category, category)]
    avoid = avoid_techniques or set()
    if avoid:
        candidates = [r for r in candidates if r.technique not in avoid]
    if not candidates:
        avoid_note = f" (avoid={sorted(avoid)})" if avoid else ""
        return StrategyPick(
            category=category,
            prior=None,
            novel=None,
            rationale=(
                f"no techniques in skill-library matching category "
                f"'{category}'{avoid_note} — council dispatch + "
                f"gap_search may be needed to seed."
            ),
        )

    # Prior: highest hit_rate, with finding count as tiebreak (more findings = more proven)
    prior = max(candidates, key=lambda r: (r.hit_rate, r.finding, -r.tried))

    # Novel: highest finding_rate among remaining, with low hit_rate breaking ties
    # toward genuinely exploratory techniques. Exclude the prior pick.
    remaining = [r for r in candidates if r.technique != prior.technique]
    novel = (
        max(remaining, key=lambda r: (r.finding_rate, r.finding, -r.hit_rate))
        if remaining
        else None
    )

    rationale = (
        f"prior = {prior.technique} (hit_rate={prior.hit_rate}, "
        f"tried={prior.tried}, top3={prior.top3})"
    )
    if novel is not None:
        rationale += (
            f"; novel = {novel.technique} (finding_rate={novel.finding_rate:.2f}, "
            f"tried={novel.tried}, finding={novel.finding})"
        )
    else:
        rationale += "; novel = none (only one technique in category)"
    if avoid:
        rationale += f"; avoided={sorted(avoid)}"

    return StrategyPick(category=category, prior=prior, novel=novel, rationale=rationale)


# ---------------- convergence detect ----------------


@dataclass
class ConvergenceDecision:
    action: str  # "continue" | "stop"
    reason: str


def convergence_detect(
    *,
    score_history: list[float],
    new_gap_counts: list[int],
    max_attempts: int = 3,
    score_tolerance: float = 0.0,
) -> ConvergenceDecision:
    """Decide whether to keep attempting or stop the inner loop.

    Stops when EITHER:
      - Score didn't improve AND no new gap was surfaced in the last attempt
      - Attempt budget is exhausted

    Otherwise continues. First attempt always continues.
    """
    if len(score_history) == 0:
        return ConvergenceDecision(action="continue", reason="no attempts yet")

    if len(score_history) >= max_attempts:
        return ConvergenceDecision(
            action="stop",
            reason=f"reached max attempts ({max_attempts})",
        )

    if len(score_history) == 1:
        return ConvergenceDecision(action="continue", reason="first attempt — keep going")

    last_score = score_history[-1]
    prev_score = score_history[-2]
    last_gap = new_gap_counts[-1] if new_gap_counts else 0

    # Lower scores are better in this project's scoring convention; treat any
    # decrease as progress.
    no_progress = abs(last_score - prev_score) <= score_tolerance
    no_new_gap = last_gap == 0

    if no_progress and no_new_gap:
        return ConvergenceDecision(
            action="stop",
            reason=(
                f"no progress (Δ={last_score - prev_score:+.6g} within "
                f"tol {score_tolerance}) and no new gap surfaced — "
                f"inner loop converged"
            ),
        )

    return ConvergenceDecision(
        action="continue",
        reason=("score improved" if not no_progress else "new gap to explore"),
    )


# ---------------- CLI ----------------


def main(argv: list[str] | None = None) -> int:
    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")
    parser = argparse.ArgumentParser(description=__doc__.split("\n", 1)[0])
    g = parser.add_mutually_exclusive_group(required=True)
    g.add_argument("--problem-id", type=int, help="Problem id (1-23).")
    g.add_argument("--category", type=str, help="Category name (overrides id-based lookup).")
    parser.add_argument("--library", type=Path, default=DEFAULT_LIBRARY)
    args = parser.parse_args(argv)

    category = args.category if args.category else category_for(args.problem_id)
    print(f"category: {category}")
    if category == "?":
        print(
            f"  (problem-id {args.problem_id} not mapped — using '?' "
            f"won't match any library row)"
        )

    pick = pick_strategy(args.library, category=category)
    print(f"\n{pick.rationale}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
