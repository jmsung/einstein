"""skill_update.py — close the bandit learning loop (Goal 3).

At cycle end the chosen technique's `(category, technique)` arm in
`docs/agent/skill-library.md` is updated: `tried += 1` always, `top3 += 1`
when the cycle reached top-3 (`finding += 1` optionally), then `hit_rate` and
`last_used` are refreshed. The bandit's next pick reads these counts, so this
is the feedback edge that makes the bandit *learn*.

Idempotent per `(cycle_id, technique)` via a ledger file (private, under
`mb/logs/`): re-running a cycle's update — a crash-restart, a re-run, a
double-invocation from the discipline step — never double-counts.

The row pattern is reused from `docs/tools/strategy_picker.ROW_RE`, so there
is one parser of the skill-library table, not two.
"""

from __future__ import annotations

import datetime as dt
import sys
from dataclasses import dataclass
from pathlib import Path

# src/einstein/bandit/skill_update.py → parents[3] == repo root.
_REPO = Path(__file__).resolve().parents[3]
DEFAULT_LIBRARY = _REPO / "docs" / "agent" / "skill-library.md"
# mb is the umbrella sibling of cb; under a worktree it's one level up
# (matches autonomous_loop.DEFAULT_MB_DIR).
DEFAULT_LEDGER = _REPO.parent / "mb" / "logs" / "skill-bandit-updates.tsv"


def _row_re():
    """Borrow strategy_picker's compiled row regex (script-style layout)."""
    tools = _REPO / "docs" / "tools"
    if str(tools) not in sys.path:
        sys.path.insert(0, str(tools))
    import strategy_picker  # type: ignore[import-not-found]

    return strategy_picker.ROW_RE


@dataclass
class UpdateResult:
    """Outcome of one update_counts call. Counts populated only on applied=True."""

    applied: bool
    technique: str
    reason: str
    tried: int | None = None
    top3: int | None = None
    finding: int | None = None
    hit_rate: float | None = None


def _ledger_key(cycle_id: int, technique: str, pull_index: int | None = None) -> str:
    """Build the ledger key.

    `pull_index=None` (single-attempt path) → `cycle\ttechnique` (legacy
    format, preserved for backward compat).
    `pull_index=int` (fanout K-pull path) → `cycle\tP{pull_index}\ttechnique`,
    a distinct namespace so the same arm pulled K times in one cycle counts
    as K trials, not deduped to 1.
    """
    if pull_index is None:
        return f"{cycle_id}\t{technique}"
    return f"{cycle_id}\tP{pull_index}\t{technique}"


def _ledger_has(
    ledger_path: Path, cycle_id: int, technique: str, pull_index: int | None = None
) -> bool:
    if not ledger_path.exists():
        return False
    key = _ledger_key(cycle_id, technique, pull_index)
    return any(line.rstrip("\n") == key for line in ledger_path.read_text().splitlines())


def _ledger_append(
    ledger_path: Path, cycle_id: int, technique: str, pull_index: int | None = None
) -> None:
    ledger_path.parent.mkdir(parents=True, exist_ok=True)
    with ledger_path.open("a", encoding="utf-8") as f:
        f.write(_ledger_key(cycle_id, technique, pull_index) + "\n")


def update_counts(
    library_path: Path,
    technique: str,
    *,
    reached_top3: bool,
    cycle_id: int,
    ledger_path: Path = DEFAULT_LEDGER,
    produced_finding: bool = False,
    today: str | None = None,
    pull_index: int | None = None,
) -> UpdateResult:
    """Bump `technique`'s row in `library_path`. Idempotent per ledger key.

    `pull_index=None` (single-attempt path) — ledger key is `(cycle, technique)`,
    matching the pre-Goal-3 format. Two calls with the same (cycle, technique)
    dedupe.

    `pull_index=int` (fanout K-pull, Goal 3 of js/feat/parallel-attempts) —
    ledger key is `(cycle, P{pull}, technique)`. K pulls of the SAME arm in
    one cycle apply K times because the keys differ. This is the bandit
    semantics requested by branch line 81: "tried increments for every arm
    pulled (not just winner)". Under K-pull Thompson, posterior collisions
    are informative; the posterior should advance by K trials.

    Returns `UpdateResult(applied=False, ...)` without mutating anything when
    the ledger already has this key, or when the technique has no row in the
    library.
    """
    if _ledger_has(ledger_path, cycle_id, technique, pull_index):
        return UpdateResult(False, technique, "already applied (idempotent)")

    row_re = _row_re()
    today = today or dt.date.today().isoformat()
    lines = library_path.read_text().splitlines(keepends=True)

    out: list[str] = []
    counts: tuple[int, int, int, float] | None = None
    for line in lines:
        m = row_re.match(line.strip())
        if m and m.group(1).strip() == technique and counts is None:
            category = m.group(2).strip()
            tried = int(m.group(3)) + 1
            top3 = int(m.group(4)) + (1 if reached_top3 else 0)
            finding = int(m.group(5)) + (1 if produced_finding else 0)
            hit = top3 / tried if tried else 0.0
            out.append(
                f"| `{technique}` | {category} | {tried} | {top3} | {finding} "
                f"| {today} | {hit:.2f} |\n"
            )
            counts = (tried, top3, finding, hit)
        else:
            out.append(line)

    if counts is None:
        return UpdateResult(False, technique, "technique not in library")

    library_path.write_text("".join(out))
    _ledger_append(ledger_path, cycle_id, technique, pull_index)
    tried, top3, finding, hit = counts
    return UpdateResult(True, technique, "updated", tried, top3, finding, hit)


__all__ = ["UpdateResult", "update_counts", "DEFAULT_LIBRARY", "DEFAULT_LEDGER"]
