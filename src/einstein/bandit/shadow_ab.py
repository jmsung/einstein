"""shadow_ab.py — bandit vs manifest dispatcher A/B (Goal 5).

The meta-loop's shadow harness (`meta_loop.shadow`) applies a proposal *diff*
to a worktree arm. The bandit-vs-manifest difference is not a diff — it is the
`EINSTEIN_BANDIT` env flag — so this is a small dedicated comparison that
*reuses* the meta-loop's metric machinery (`compute_arm_metrics`) and cycle-log
parser (`diagnose.parse_cycle_log`) rather than its worktree plumbing.

  Arm A = `EINSTEIN_BANDIT=1`  (Thompson bandit picks the technique)
  Arm B = unset                (manifest `strategy_picker` picks)

Promotion gate (the G5 metric):
  promote the bandit to default ONLY when
    (1) findings/cycle is **non-worse** than the manifest arm, AND
    (2) the bandit arm shows **>= 1 cross-problem skill rediscovery**
        (a technique the bandit picked on >= 2 distinct problems).
Promotion itself is **human-gated** — this harness records the verdict to
`mb/logs/meta-shadow-runs.md`; it never flips the default.

The cycle-running step is injectable (`arm_runner`) so the harness can be
validated mechanically without a live multi-hour LLM campaign.
"""

from __future__ import annotations

import datetime as dt
import logging
import os
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Callable

from einstein.meta_loop import diagnose
from einstein.meta_loop.shadow import compute_arm_metrics

log = logging.getLogger("bandit.shadow_ab")

_REPO = Path(__file__).resolve().parents[3]
DEFAULT_SHADOW_LOG = _REPO.parent / "mb" / "logs" / "meta-shadow-runs.md"

# The G4 audit note embeds `technique=<name> ...`; cross-problem rediscovery is
# measured from the bandit arm's notes only (the manifest arm uses prior=/novel=).
_TECH_RE = re.compile(r"technique=(\S+)")


def count_cross_problem_rediscoveries(rows: list[diagnose.CycleRow]) -> int:
    """How many techniques the bandit picked on >= 2 distinct problems.

    This is the "the bandit found a cross-problem skill" signal: a technique
    rediscovered on multiple problem families is evidence the bandit is
    transporting wisdom, not just local-fitting one problem.
    """
    seen: dict[str, set[str]] = {}
    for r in rows:
        for m in _TECH_RE.finditer(r.notes):
            seen.setdefault(m.group(1), set()).add(r.problem)
    return sum(1 for problems in seen.values() if len(problems) >= 2)


@dataclass(frozen=True)
class Verdict:
    """A/B outcome + the promotion decision (advisory — promotion is human-gated)."""

    promote: bool
    reason: str
    a_findings_per_cycle: float
    b_findings_per_cycle: float
    cross_problem_rediscoveries: int
    a_cycles: int
    b_cycles: int


def decide(
    arm_a_rows: list[diagnose.CycleRow],
    arm_b_rows: list[diagnose.CycleRow],
    *,
    min_rediscoveries: int = 1,
) -> Verdict:
    """Apply the G5 gate to two arms' cycle-log rows. Arm A is the bandit."""
    a = compute_arm_metrics(arm_a_rows)
    b = compute_arm_metrics(arm_b_rows)
    a_fpc = a.per_cycle("findings_added")
    b_fpc = b.per_cycle("findings_added")
    rediscoveries = count_cross_problem_rediscoveries(arm_a_rows)

    findings_non_worse = a_fpc >= b_fpc
    has_rediscovery = rediscoveries >= min_rediscoveries
    promote = findings_non_worse and has_rediscovery
    reason = (
        f"findings/cyc A={a_fpc:.3f} {'>=' if findings_non_worse else '<'} B={b_fpc:.3f}; "
        f"cross-problem rediscoveries={rediscoveries} (need >={min_rediscoveries})"
    )
    return Verdict(
        promote=promote,
        reason=reason,
        a_findings_per_cycle=a_fpc,
        b_findings_per_cycle=b_fpc,
        cross_problem_rediscoveries=rediscoveries,
        a_cycles=a.cycles,
        b_cycles=b.cycles,
    )


# ---------------- verdict log ----------------


_SHADOW_LOG_HEADER = (
    "# meta-shadow runs — skill-bandit (A) vs manifest dispatcher (B)\n\n"
    "Promotion of the bandit to default (`EINSTEIN_BANDIT` on by default) is "
    "human-gated. This log is the evidence; a `promote: yes` row is a *candidate*, "
    "not an applied change.\n\n"
    "| timestamp_utc | mode | n_cycles | problems | A_findings/cyc | B_findings/cyc "
    "| cross_problem_rediscovery | promote | reason |\n"
    "|---|---|---|---|---|---|---|---|---|\n"
)


def append_run(
    path: Path,
    *,
    timestamp: dt.datetime,
    mode: str,
    n_cycles: int,
    problems: list[int],
    verdict: Verdict,
) -> None:
    """Append one verdict row to `mb/logs/meta-shadow-runs.md`.

    `mode` is `live` (a real A/B campaign) or `wiring-validation` (the harness
    was exercised on synthetic cycles to prove the metric→verdict→log path).
    """
    if not path.is_file():
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(_SHADOW_LOG_HEADER)
    problems_str = ",".join(f"P{p}" for p in problems)
    row = (
        f"| {timestamp.strftime('%Y-%m-%dT%H:%M:%SZ')} | {mode} | {n_cycles} "
        f"| {problems_str} | {verdict.a_findings_per_cycle:.3f} "
        f"| {verdict.b_findings_per_cycle:.3f} | {verdict.cross_problem_rediscoveries} "
        f"| {'yes' if verdict.promote else 'no'} | {verdict.reason} |\n"
    )
    with path.open("a") as fh:
        fh.write(row)


# ---------------- orchestration ----------------


# (arm_label, bandit_on, problem_ids, n_cycles, cycle_log_path) -> None
ArmRunner = Callable[[str, bool, list[int], int, Path], None]


def _default_arm_runner(
    arm: str, bandit: bool, problems: list[int], n_cycles: int, cycle_log: Path
) -> None:
    """Live arm runner — drives scripts/autonomous_loop in-process with the
    `EINSTEIN_BANDIT` flag set for this arm, writing to `cycle_log`.

    Heavy (real cycles) and only invoked on a deliberate live A/B; the test /
    validation path injects a stub. Walks the id-ordered queue for
    `len(problems)` visits — exact problem-subset targeting is a refinement
    (the autonomous loop has no problem-subset flag yet).
    """
    import sys

    sys.path.insert(0, str(_REPO / "scripts"))
    import autonomous_loop as al  # type: ignore[import-not-found]

    prev = os.environ.get("EINSTEIN_BANDIT")
    os.environ["EINSTEIN_BANDIT"] = "1" if bandit else "0"
    try:
        per_visit = max(1, n_cycles // max(1, len(problems)))
        al.run_queue(
            cycle_log=cycle_log,
            max_problems=len(problems),
            max_attempts_per_visit=per_visit,
            skip_gates=True,
        )
    finally:
        if prev is None:
            os.environ.pop("EINSTEIN_BANDIT", None)
        else:
            os.environ["EINSTEIN_BANDIT"] = prev


@dataclass
class ShadowABResult:
    verdict: Verdict
    arm_a_rows: list[diagnose.CycleRow]
    arm_b_rows: list[diagnose.CycleRow]


def run_shadow_ab(
    problems: list[int],
    n_cycles: int,
    *,
    arm_a_log: Path,
    arm_b_log: Path,
    arm_runner: ArmRunner = _default_arm_runner,
    shadow_log: Path = DEFAULT_SHADOW_LOG,
    mode: str = "live",
    now: dt.datetime | None = None,
) -> ShadowABResult:
    """Run both arms, parse each arm's cycle-log, decide, and append a verdict.

    `arm_runner` writes each arm's cycles to the given log; inject a stub to
    validate the harness without a live campaign.
    """
    now = now or dt.datetime.now(dt.timezone.utc)
    arm_runner("A", True, problems, n_cycles, arm_a_log)
    arm_runner("B", False, problems, n_cycles, arm_b_log)
    arm_a_rows = diagnose.parse_cycle_log(arm_a_log)
    arm_b_rows = diagnose.parse_cycle_log(arm_b_log)
    verdict = decide(arm_a_rows, arm_b_rows)
    append_run(
        shadow_log,
        timestamp=now,
        mode=mode,
        n_cycles=n_cycles,
        problems=problems,
        verdict=verdict,
    )
    log.info("shadow A/B verdict: promote=%s — %s", verdict.promote, verdict.reason)
    return ShadowABResult(verdict=verdict, arm_a_rows=arm_a_rows, arm_b_rows=arm_b_rows)


__all__ = [
    "Verdict",
    "ShadowABResult",
    "count_cross_problem_rediscoveries",
    "decide",
    "append_run",
    "run_shadow_ab",
    "DEFAULT_SHADOW_LOG",
]
