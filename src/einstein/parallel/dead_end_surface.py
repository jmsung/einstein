"""dead_end_surface.py — Goal 6 of js/feat/parallel-attempts.

After a K-attempt cycle, scan non-winning attempts and decide if any cross
the threshold for "would a peer have tried this and learned something" (per
`.claude/rules/failure-is-a-finding.md`). When one does, auto-draft a stub
finding file the agent or a later /wiki-learn pass can flesh out.

Mechanical heuristic — NOT a substitute for the rule's actual test:

  - exit == "ok" (genuine attempt, not noise from timeout/dispatch-fail)
  - relative score-gap from winner ≥ 10% (different basin, not same-basin
    shuffle); winner.score == 0 treats any gap as infinite-relative
  - technique under-explored: arms_tried[tech] ≤ 10 (already-well-mapped
    techniques probably have a finding; new ones are where the learning is)

At most ONE candidate per cycle (the largest-gap high-signal loser).
Branch line 109: "Don't force one per loser — over-filing dilutes the signal."

The stub explicitly carries `status: stub` + a `TODO: needs distillation`
marker so a future /wiki-learn pass (or a human) knows the WHY field still
needs the actual obstruction articulation. Mechanical surfacing produces a
SEED, not a finished finding — the wiki-attribution rule's quality bar
("Grounded, Cited, Verifiable, No filler") is met by the upgrade pass, not
by this auto-stub.
"""

from __future__ import annotations

import re
from dataclasses import dataclass

from einstein.parallel.fanout import AttemptResult

# Tuning constants — explicit so a future PR (e.g. after Goal 5 A/B verdict)
# can re-calibrate without spelunking. See branch file Goal 6 risk-notes.
SCORE_GAP_REL_THRESHOLD = 0.10  # 10% relative gap from winner
ARM_NOVELTY_TRIED_CAP = 10  # tried ≤ 10 → still under-explored


def _safe_relative_gap(loser_score: float, winner_score: float) -> float:
    """Relative gap |loser - winner| / max(|winner|, eps)."""
    eps = 1e-12
    return abs(loser_score - winner_score) / max(abs(winner_score), eps)


def is_high_signal_loser(
    attempt: AttemptResult,
    winner: AttemptResult,
    *,
    arms_tried: dict[str, int],
) -> bool:
    """True iff `attempt` looks like a real dead-end worth surfacing.

    Returns False on any noise condition (exit != ok, scores missing) and on
    any well-mapped-arm condition (tried > cap). Pure predicate."""
    if attempt.exit != "ok" or winner.exit != "ok":
        return False
    if attempt.score is None or winner.score is None:
        return False
    if attempt.technique is None:
        return False
    if _safe_relative_gap(attempt.score, winner.score) < SCORE_GAP_REL_THRESHOLD:
        return False
    tried = arms_tried.get(attempt.technique, 0)
    if tried > ARM_NOVELTY_TRIED_CAP:
        return False
    return True


def select_top_candidate(
    *,
    losers: list[AttemptResult],
    winner: AttemptResult | None,
    arms_tried: dict[str, int],
) -> AttemptResult | None:
    """Return the highest-score-gap high-signal loser, or None.

    One per cycle — the rule is "don't force one per loser." When two losers
    tie on gap, the lower attempt_index wins for determinism.
    """
    if winner is None:
        return None
    candidates = [a for a in losers if is_high_signal_loser(a, winner, arms_tried=arms_tried)]
    if not candidates:
        return None
    candidates.sort(
        key=lambda a: (-_safe_relative_gap(a.score or 0.0, winner.score or 0.0), a.index),
    )
    return candidates[0]


_SLUG_RE = re.compile(r"[^a-z0-9]+")


def _slug(text: str) -> str:
    """Lowercase, strip `.md`, replace non-alnum runs with `-`, trim hyphens."""
    s = text.lower()
    if s.endswith(".md"):
        s = s[:-3]
    s = _SLUG_RE.sub("-", s)
    return s.strip("-")


@dataclass(frozen=True)
class _ProblemLike:
    problem_id: int
    display: str
    slug: str


def draft_stub(
    *,
    problem,
    candidate: AttemptResult,
    winner: AttemptResult,
    today: str,
) -> tuple[str, str]:
    """Build the (relative_path, file_content) for a stub finding.

    Path: `knowledge/wiki/findings/dead-end-<tech-slug>-p<id>-<YYYY-MM-DD>.md`.
    Content: full frontmatter (status: stub) + structured "What we tried"
    + an explicit "Why it failed" TODO placeholder pointing at /wiki-learn.

    Frontmatter complies with the wiki-attribution rule
    (`type/author/drafted/status` mandatory). Cites the problem page.
    """
    tech_slug = _slug(candidate.technique or "unknown")
    fname = f"dead-end-{tech_slug}-p{problem.problem_id}-{today}.md"
    rel_path = f"knowledge/wiki/findings/{fname}"

    frontmatter = (
        "---\n"
        "type: finding\n"
        "author: agent\n"
        f"drafted: {today}\n"
        f"question_origin: problem-{problem.problem_id}\n"
        "status: stub\n"
        "related_concepts: []\n"
        f"cites:\n"
        f"  - knowledge/wiki/problems/{problem.problem_id}-{problem.slug}.md\n"
        "---\n\n"
    )
    body = (
        f"# Dead end: `{candidate.technique}` on P{problem.problem_id}\n\n"
        "## What we tried\n\n"
        f"Fanout cycle (Goal 5+ pilot, js/feat/parallel-attempts) "
        f"attempted `{candidate.technique}` against P{problem.problem_id} "
        f"({problem.display}) and reached score `{candidate.score}`.\n\n"
        f"The cycle's winner — `{winner.technique}` — reached "
        f"`{winner.score}`. Relative basin gap = "
        f"`{_safe_relative_gap(candidate.score or 0.0, winner.score or 0.0):.3f}`.\n\n"
        f"Per-attempt audit: `{candidate.pick_note}` → exit=`{candidate.exit}`.\n\n"
        "## Why it failed\n\n"
        "TODO: needs distillation. This is an auto-stub from "
        "`einstein.parallel.dead_end_surface` — the structural data above is "
        "filled, but the OBSTRUCTION (per `.claude/rules/failure-is-a-finding.md`) "
        "still needs articulation. Run `/wiki-learn` on this branch, or "
        "expand by hand, then flip `status: stub` → `status: answered`.\n\n"
        "## What this rules out\n\n"
        "TODO (post-distillation).\n\n"
        "## What might still work\n\n"
        "TODO (post-distillation).\n"
    )
    return rel_path, frontmatter + body


__all__ = [
    "ARM_NOVELTY_TRIED_CAP",
    "SCORE_GAP_REL_THRESHOLD",
    "draft_stub",
    "is_high_signal_loser",
    "select_top_candidate",
]
