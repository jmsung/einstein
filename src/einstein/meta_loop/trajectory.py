"""Trajectory metric + classifier — Goal 1 of js/feat/evolve-and-measure.

Turns the append-only cycle-log into the closed-loop signal it was always
meant to be: a per-problem *best-verified-score-vs-cycle* curve, plus a
classifier that distinguishes the three plateaus the loop kept conflating:

- **improving** — the running-best moved in the right direction recently.
- **solved-at-floor** — a *certificate* proves we are at the floor (a dual
  bound matching the value, a BnB negative lemma, a PD Hessian certificate).
  A flat score with a certificate is *solved*, not *stuck*.
- **stuck** — open headroom vs arena #1, no certificate, no recent gain. This
  is the only plateau that warrants more compute (or the evolve engine).
- **unknown** — not enough signal to decide honestly (no headroom data, no
  certificate, flat curve). We say "unknown" rather than mislabel.

Why a certificate and not status strings: the whole point of this branch is
to stop conflating "frozen by policy" with "proven at floor". The certificate
is an explicit per-problem frontmatter field (`certificate:`); see
`certificate_of`.

Pure and dependency-light by design (Goal 1 says "pure, tested"): `classify`
takes headroom + certificate as explicit arguments. The dashboard (Goal 2)
and engine gate (Goal 4) resolve those from frontmatter / the headroom cache
and feed them in.
"""

from __future__ import annotations

import enum
import re
from dataclasses import dataclass

from einstein.meta_loop.diagnose import CycleRow

# ---------------- score parsing ----------------

# Matches the first two numbers around an arrow, e.g. "2.6 → 2.7".
_ARROW_RE = re.compile(r"([-+]?[\d.]+(?:[eE][-+]?\d+)?)\s*→\s*([-+]?[\d.]+(?:[eE][-+]?\d+)?)")
# Matches a single leading number, e.g. "0.38087 (no Δ)".
_SINGLE_RE = re.compile(r"^\s*([-+]?[\d.]+(?:[eE][-+]?\d+)?)")
_PID_RE = re.compile(r"P(\d+)")


def _to_float(s: str) -> float | None:
    try:
        return float(s)
    except (TypeError, ValueError):
        return None


def parse_score(score_field: str) -> tuple[float | None, float | None]:
    """Parse a cycle-log `score_field` into ``(start, end)`` numeric scores.

    Handles every shape the log uses in the wild::

        "2.6 → 2.7"                  -> (2.6, 2.7)
        "2.639... → 2.639..."        -> (2.639..., 2.639...)
        "0.38087 (no Δ)"             -> (0.38087, 0.38087)   # single value
        "none (no Δ)" / "(n/a)"      -> (None, None)
        "(HIDDEN)" / "(HIDDEN) → ..."-> (None, None)

    Non-numeric placeholders collapse to ``None`` so callers can skip them.
    """
    m = _ARROW_RE.search(score_field)
    if m:
        return _to_float(m.group(1)), _to_float(m.group(2))
    m = _SINGLE_RE.match(score_field)
    if m:
        val = _to_float(m.group(1))
        return val, val
    return None, None


def problem_id_of(label: str) -> int | None:
    """Extract the numeric problem id from a cycle-log problem label.

    ``"P19 difference-bases"`` / ``"P19-difference-bases"`` -> ``19``.
    Returns ``None`` for non-problem rows (``"refactor"``, tooling rows).
    """
    m = _PID_RE.search(label)
    return int(m.group(1)) if m else None


# ---------------- per-problem trajectory ----------------


@dataclass(frozen=True)
class TrajectoryPoint:
    """One point on a problem's best-verified-score-vs-cycle curve."""

    cycle_id: int
    best_score: float


def problem_trajectory(
    rows: list[CycleRow], *, problem_id: int, minimize: bool
) -> list[TrajectoryPoint]:
    """Build the running-best score curve for one problem across cycles.

    For each cycle that names this problem and carries a numeric *end* score,
    emit a point whose ``best_score`` is the best end-score seen so far
    (lowest if ``minimize`` else highest). Cycles with unparseable scores
    (``(n/a)``, ``(HIDDEN)``) are skipped — they carry no verified score.
    """
    points: list[TrajectoryPoint] = []
    best: float | None = None
    better = min if minimize else max
    for row in sorted(rows, key=lambda r: r.cycle_id):
        if problem_id_of(row.problem) != problem_id:
            continue
        _, end = parse_score(row.score_field)
        if end is None:
            continue
        best = end if best is None else better(best, end)
        points.append(TrajectoryPoint(cycle_id=row.cycle_id, best_score=best))
    return points


# ---------------- classification ----------------


class Classification(enum.Enum):
    IMPROVING = "improving"
    SOLVED_AT_FLOOR = "solved-at-floor"
    STUCK = "stuck"
    UNKNOWN = "unknown"

    @property
    def badge(self) -> str:
        return {
            Classification.IMPROVING: "📈 improving",
            Classification.SOLVED_AT_FLOOR: "✅ solved-at-floor",
            Classification.STUCK: "🧱 stuck",
            Classification.UNKNOWN: "❔ unknown",
        }[self]


def classify(
    trajectory: list[TrajectoryPoint],
    *,
    headroom: float | None,
    certificate: str | None,
    minimize: bool = True,
    window: int = 3,
) -> Classification:
    """Classify one problem from its trajectory + headroom + certificate.

    Precedence (strongest signal first):

    1. **certificate present** → ``SOLVED_AT_FLOOR``. A proof of the floor
       overrides everything; a flat score with a certificate is solved.
    2. **recent strict gain** (running-best moved within the last ``window``
       points) → ``IMPROVING``.
    3. **open headroom, no gain** (``headroom`` known and > 0) → ``STUCK``.
    4. otherwise → ``UNKNOWN`` (not enough signal to decide honestly).
    """
    if certificate:
        return Classification.SOLVED_AT_FLOOR
    if not trajectory:
        return Classification.UNKNOWN

    recent = trajectory[-window:]
    first, last = recent[0].best_score, recent[-1].best_score
    improved = (last < first) if minimize else (last > first)
    if improved:
        return Classification.IMPROVING

    if headroom is not None and headroom > 0:
        return Classification.STUCK
    return Classification.UNKNOWN


# ---------------- certificate resolution ----------------

_CERT_FALSY = {
    "", "none", "false", "no", "0", "off", "n/a", "na",
    # placeholders — a frozen-but-unproven problem must NOT read as solved-at-floor
    # (red-team 2026-06-27: `tbd`/`???` slipped through → false SOLVED_AT_FLOOR):
    "tbd", "tba", "todo", "pending", "wip", "draft", "unknown", "placeholder",
    "?", "??", "???", "xxx", "-", "--", "...",
}


def certificate_of(frontmatter: dict) -> str | None:
    """Resolve the `certificate:` frontmatter field to a cert name or None.

    Treats absent / falsy / placeholder values as *no certificate*, so a
    problem is only ``solved-at-floor`` when a real proof is named. Placeholder
    strings (``tbd``, ``???`` …) are rejected too — otherwise a typo'd/aspirational
    certificate would falsely mark an unsolved problem as proven-at-floor and drop
    it from the work queue.
    """
    raw = str(frontmatter.get("certificate", "")).strip()
    if raw.lower() in _CERT_FALSY:
        return None
    return raw


# ---------------- per-problem bundle + aggregates ----------------


@dataclass(frozen=True)
class ProblemClassification:
    problem_id: int
    label: str
    classification: Classification
    trajectory: list[TrajectoryPoint]
    headroom: float | None
    certificate: str | None


_IMPROVEMENT_OUTCOMES = {"improved", "conquered"}


@dataclass(frozen=True)
class AggregateMetrics:
    """Branch-level scoreboard derived from the per-problem classifications."""

    num_rank_1: int
    num_solved_at_floor: int
    num_stuck: int
    num_improving: int
    num_unknown: int
    total_cycles: int
    records_per_100_cycles: float
    headroom_closed_rate: float


@dataclass(frozen=True)
class ProblemSpec:
    """Minimal per-problem input for the orchestrator: id, display label, and
    raw frontmatter (for the `certificate:` field). ``minimize`` defaults to
    the canonical map but can be overridden per-spec for tests."""

    problem_id: int
    label: str
    frontmatter: dict
    minimize: bool | None = None


def build_classifications(
    rows: list[CycleRow],
    specs: list[ProblemSpec],
    headrooms: dict[int, float | None],
    *,
    window: int = 3,
) -> list[ProblemClassification]:
    """Orchestrate trajectory + classify for each problem spec.

    Pure: ``headrooms`` (problem_id → relative headroom, or None) is injected
    by the caller (dashboard / engine), so this stays offline and testable.
    ``minimize`` falls back to ``PROBLEM_MINIMIZE`` when the spec doesn't set
    it; problems with no known direction are skipped (we can't build a
    running-best without one).
    """
    from einstein.auto_submit import PROBLEM_MINIMIZE

    out: list[ProblemClassification] = []
    for spec in specs:
        minimize = spec.minimize
        if minimize is None:
            minimize = PROBLEM_MINIMIZE.get(spec.problem_id)
        if minimize is None:
            continue
        traj = problem_trajectory(rows, problem_id=spec.problem_id, minimize=minimize)
        cert = certificate_of(spec.frontmatter)
        headroom = headrooms.get(spec.problem_id)
        cls = classify(traj, headroom=headroom, certificate=cert, minimize=minimize, window=window)
        out.append(
            ProblemClassification(
                problem_id=spec.problem_id,
                label=spec.label,
                classification=cls,
                trajectory=traj,
                headroom=headroom,
                certificate=cert,
            )
        )
    return out


def aggregate(
    classifications: list[ProblemClassification],
    rows: list[CycleRow],
    *,
    rank1_ids: set[int],
) -> AggregateMetrics:
    """Roll per-problem classifications + raw cycle rows into headline metrics.

    - ``records_per_100_cycles`` — improvement-outcome cycles per 100 cycles.
    - ``headroom_closed_rate`` — solved-at-floor / (solved-at-floor + stuck):
      of the problems where the floor question is *decided*, the fraction
      closed. Excludes improving/unknown (the question is still open there).
    """
    by_class: dict[Classification, int] = {c: 0 for c in Classification}
    for pc in classifications:
        by_class[pc.classification] += 1

    total = len(rows)
    records = sum(1 for r in rows if r.outcome.strip() in _IMPROVEMENT_OUTCOMES)
    records_per_100 = (100.0 * records / total) if total else 0.0

    solved = by_class[Classification.SOLVED_AT_FLOOR]
    stuck = by_class[Classification.STUCK]
    decided = solved + stuck
    closed_rate = (solved / decided) if decided else 0.0

    return AggregateMetrics(
        num_rank_1=len(rank1_ids),
        num_solved_at_floor=solved,
        num_stuck=stuck,
        num_improving=by_class[Classification.IMPROVING],
        num_unknown=by_class[Classification.UNKNOWN],
        total_cycles=total,
        records_per_100_cycles=records_per_100,
        headroom_closed_rate=closed_rate,
    )
