"""Priority picker for the autonomous loop — Phase 3 Goal 1.

priority = headroom × hit-rate × staleness

Replaces problem_id-ascending order for `--one-problem --by-priority` so the
unattended scheduler targets problems with real headroom instead of grinding
P1. Pure logic lives here (testable, fetcher-injectable); the live
leaderboard fetch + cache path wiring live in `scripts/autonomous_loop.py`.

Factors:
- **headroom** — relative gap to arena #1, 0.0 when tied/leading, None when
  unknown (fetch failed, no cache, no local score, or unknown optimisation
  direction — fail-closed per `dead-end-auto-submit-direction-sign`).
- **hit-rate** — tried-weighted top3 rate of the problem's category in
  `docs/agent/skill-library.md` (via `strategy_picker.load_skill_library`).
  None when the category has no rows; floored so a 0-hit-rate category
  cannot annihilate real headroom.
- **staleness** — cycles since the problem's last cycle-log row, normalized
  by the log's id span. Never-visited → 1.0 (max). Floored so a
  just-visited problem with big headroom stays rankable.

Queue contract (tests in tests/tools/test_problem_priority.py):
- rank by priority desc; tie-break problem_id asc
- problems with headroom=None rank AFTER all scored problems, in id order
- if NO problem has headroom data → plain id order (= build_queue fallback)
"""

from __future__ import annotations

import json
import logging
import re
import sys
from pathlib import Path
from typing import TYPE_CHECKING, Callable, Sequence

log = logging.getLogger("problem_priority")

_TOOLS = Path(__file__).resolve().parent
sys.path.insert(0, str(_TOOLS))

from strategy_picker import load_skill_library  # noqa: E402

if TYPE_CHECKING:  # Problem is autonomous_loop's dataclass; avoid runtime cycle
    from autonomous_loop import Problem

# Floors keep the product a *total* ranking signal: a single zero factor
# (fresh visit, 0-hit-rate category) must dampen, not erase, real headroom.
HIT_RATE_FLOOR = 0.1
STALENESS_FLOOR = 0.1
NEUTRAL_HIT_RATE = 0.5

_ROW_RE = re.compile(r"^\|\s*(\d+)\s*\|\s*(P\d+-[a-z0-9-]+)\s*\|", re.IGNORECASE)


# ---------------- headroom ----------------


def relative_headroom(
    our_score: float | None, arena1_score: float | None, minimize: bool | None
) -> float | None:
    """Relative gap to arena #1; 0.0 when tied or leading; None on missing data."""
    if our_score is None or arena1_score is None or minimize is None:
        return None
    gap = (our_score - arena1_score) if minimize else (arena1_score - our_score)
    if gap <= 0:
        return 0.0
    return gap / max(abs(arena1_score), 1e-12)


def load_cached_arena_best(cache_path: Path, problem_id: int) -> float | None:
    """Read the cached arena-#1 score for a problem; None on any failure."""
    try:
        data = json.loads(cache_path.read_text())
        return float(data[str(problem_id)]["arena1"])
    except (OSError, ValueError, KeyError, TypeError):
        return None


def save_cached_arena_best(
    cache_path: Path, problem_id: int, arena1_score: float, *, ts: str
) -> None:
    """Upsert one problem's arena-#1 score; tolerates a missing/corrupt file."""
    try:
        data = json.loads(cache_path.read_text())
        if not isinstance(data, dict):
            data = {}
    except (OSError, ValueError):
        data = {}
    data[str(problem_id)] = {"arena1": arena1_score, "ts": ts}
    try:
        cache_path.parent.mkdir(parents=True, exist_ok=True)
        cache_path.write_text(json.dumps(data, indent=2) + "\n")
    except OSError as e:
        log.warning("headroom cache write failed: %s", e)


def headroom_for(
    problem_id: int,
    *,
    our_score: float | None,
    minimize: bool | None,
    fetcher: Callable[[int], float] | None,
    cache_path: Path,
    ts: str = "",
) -> float | None:
    """Resolve headroom via the live-fetch → cache → None ladder."""
    arena1: float | None = None
    if fetcher is not None:
        try:
            arena1 = fetcher(problem_id)
            if arena1 is not None and ts:
                save_cached_arena_best(cache_path, problem_id, arena1, ts=ts)
        except Exception as e:  # noqa: BLE001 — any fetch failure → cache fallback
            log.warning("P%d leaderboard fetch failed (%s) — trying cache", problem_id, e)
    if arena1 is None:
        arena1 = load_cached_arena_best(cache_path, problem_id)
    return relative_headroom(our_score, arena1, minimize)


# ---------------- hit-rate ----------------


def category_hit_rate(category: str, skill_library: Path) -> float | None:
    """Tried-weighted top3 rate over skill-library rows matching `category`.

    Substring match mirrors the table's compound cells ("packing / kissing").
    None when no rows match, the category is unknown ('?'), or the file is
    missing — callers substitute the neutral prior.
    """
    if not category or category == "?":
        return None
    try:
        rows = load_skill_library(skill_library)
    except OSError:
        return None
    tried = top3 = 0
    for r in rows:
        if category in r.category:
            tried += r.tried
            top3 += r.top3
    if tried == 0:
        return None if top3 == 0 and not any(category in r.category for r in rows) else 0.0
    return top3 / tried


# ---------------- staleness ----------------


def staleness(problem_label: str, cycle_log: Path) -> float:
    """Cycles since this problem's last row, normalized to [0, 1].

    1.0 = never visited (or no log). 0.0 = touched by the most recent cycle.
    """
    try:
        text = cycle_log.read_text()
    except OSError:
        return 1.0
    max_id = -1
    last_id: int | None = None
    for line in text.splitlines():
        m = _ROW_RE.match(line.strip())
        if not m:
            continue
        cid = int(m.group(1))
        max_id = max(max_id, cid)
        if m.group(2).lower() == problem_label.lower():
            last_id = cid if last_id is None else max(last_id, cid)
    if max_id < 0 or last_id is None:
        return 1.0
    return (max_id - last_id) / max(max_id, 1)


# ---------------- priority ----------------


def problem_priority(headroom: float, hit_rate: float | None, staleness: float) -> float:
    """priority = headroom × max(hit_rate, floor) × max(staleness, floor).

    headroom is the dominant, un-floored term: 0 headroom (tied/leading) → 0
    priority regardless of the other factors.
    """
    hr = NEUTRAL_HIT_RATE if hit_rate is None else hit_rate
    return headroom * max(hr, HIT_RATE_FLOOR) * max(staleness, STALENESS_FLOOR)


def build_priority_queue(
    problems: Sequence["Problem"],
    headrooms: dict[int, float | None],
    *,
    skill_library: Path,
    cycle_log: Path,
) -> list["Problem"]:
    """Rank problems by priority desc; see module docstring for the contract."""
    try:
        from strategy_picker import category_for
    except ImportError:
        category_for = lambda _pid: "?"  # noqa: E731 — degraded but functional

    scored: list[tuple[float, int, "Problem"]] = []
    unscored: list["Problem"] = []
    for p in problems:
        h = headrooms.get(p.problem_id)
        if h is None:
            unscored.append(p)
            continue
        hr = category_hit_rate(category_for(p.problem_id), skill_library)
        st = staleness(f"P{p.problem_id}-{p.slug}", cycle_log)
        scored.append((problem_priority(h, hr, st), p.problem_id, p))

    if not scored:
        return sorted(unscored, key=lambda p: p.problem_id)

    scored.sort(key=lambda t: (-t[0], t[1]))
    unscored.sort(key=lambda p: p.problem_id)
    return [p for _, _, p in scored] + unscored
