"""shadow_ab.py — parallel-K (K=4) vs single-attempt (K=1) A/B (Goal 5).

Mirrors `einstein.bandit.shadow_ab` — the K-vs-K difference is an env flag
(`EINSTEIN_PARALLEL_K`), not a code diff, so this reuses the meta-loop's
metric machinery (`compute_arm_metrics`) and cycle-log parser
(`diagnose.parse_cycle_log`) rather than its worktree+diff plumbing.

  Arm A = `EINSTEIN_PARALLEL_K=4` (fanout active; K-attempt diverse pulls)
  Arm B = `EINSTEIN_PARALLEL_K=1` (single attempt; pre-fanout baseline)

Promotion gate (branch line 100-101 of mb/active/js-feat-parallel-attempts.md):

    arm-A improvements/cycle strictly higher
      OR
    arm-A findings/cycle strictly higher AND improvements/cycle non-worse

Promotion is **human-gated** — this harness records the verdict to
`mb/logs/meta-shadow-runs.md`; it never flips the default. The default for
`EINSTEIN_PARALLEL_K` stays at 1 until a human-approved promotion lands.

The cycle-running step is injectable (`arm_runner`) so the harness can be
validated mechanically without a live multi-hour LLM campaign.
"""

from __future__ import annotations

import datetime as dt
import logging
import os
from dataclasses import dataclass
from pathlib import Path
from typing import Callable

from einstein.meta_loop import diagnose
from einstein.meta_loop.shadow import compute_arm_metrics

log = logging.getLogger("parallel.shadow_ab")

_REPO = Path(__file__).resolve().parents[3]
DEFAULT_SHADOW_LOG = _REPO.parent / "mb" / "logs" / "meta-shadow-runs.md"


@dataclass(frozen=True)
class Verdict:
    """A/B outcome + the promotion decision (advisory — promotion is human-gated)."""

    promote: bool
    reason: str
    a_improvements_per_cycle: float
    b_improvements_per_cycle: float
    a_findings_per_cycle: float
    b_findings_per_cycle: float
    a_cycles: int
    b_cycles: int


def decide(
    arm_a_rows: list[diagnose.CycleRow],
    arm_b_rows: list[diagnose.CycleRow],
) -> Verdict:
    """Apply the Goal 5 gate to two arms' cycle-log rows.

    `score_changed_cycles` (≈ improvements/cycle) and `findings_added/cycle`
    are the two signals. Promote iff arm A is strictly better on either
    improvements OR findings (with improvements non-worse on the findings
    path) — symmetric to the bandit's gate but with two signals."""
    a = compute_arm_metrics(arm_a_rows)
    b = compute_arm_metrics(arm_b_rows)
    a_ipc = a.per_cycle("score_changed_cycles")
    b_ipc = b.per_cycle("score_changed_cycles")
    a_fpc = a.per_cycle("findings_added")
    b_fpc = b.per_cycle("findings_added")

    improvements_strictly_better = a_ipc > b_ipc
    findings_strictly_better_with_non_worse_improvements = a_fpc > b_fpc and a_ipc >= b_ipc
    promote = improvements_strictly_better or findings_strictly_better_with_non_worse_improvements

    reason = (
        f"improvements/cyc A={a_ipc:.3f} {'>' if improvements_strictly_better else '<='} "
        f"B={b_ipc:.3f}; findings/cyc A={a_fpc:.3f} "
        f"{'>' if a_fpc > b_fpc else '<='} B={b_fpc:.3f}"
    )
    return Verdict(
        promote=promote,
        reason=reason,
        a_improvements_per_cycle=a_ipc,
        b_improvements_per_cycle=b_ipc,
        a_findings_per_cycle=a_fpc,
        b_findings_per_cycle=b_fpc,
        a_cycles=a.cycles,
        b_cycles=b.cycles,
    )


# ---------------- verdict log ----------------


_SHADOW_LOG_HEADER_PARALLEL = (
    "\n## parallel-K (K=4) vs single-attempt (K=1) — Goal 5 of js/feat/parallel-attempts\n\n"
    "Default for `EINSTEIN_PARALLEL_K` stays at 1 until a human-approved "
    "promotion lands here. `mode=wiring-validation` rows exercise the metric → "
    "verdict → log path mechanically; `mode=live` is a real campaign.\n\n"
    "| timestamp_utc | mode | K_A | K_B | n_cycles_each | problems "
    "| A_improvements/cyc | B_improvements/cyc | A_findings/cyc | B_findings/cyc "
    "| promote | reason |\n"
    "|---|---|---|---|---|---|---|---|---|---|---|---|\n"
)


def append_run(
    path: Path,
    *,
    timestamp: dt.datetime,
    mode: str,
    n_cycles: int,
    problems: list[int],
    verdict: Verdict,
    k_a: int = 4,
    k_b: int = 1,
) -> None:
    """Append one parallel-K A/B verdict row.

    Uses a NEW section header if the file already exists (the bandit's section
    is at the top of the file from PR #107); otherwise creates the file with
    just the parallel section header.
    """
    if not path.is_file():
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text("# meta-shadow runs\n" + _SHADOW_LOG_HEADER_PARALLEL.lstrip())
    else:
        text = path.read_text()
        if "## parallel-K (K=4) vs single-attempt" not in text:
            # First parallel-K row — append the section header
            if not text.endswith("\n"):
                text += "\n"
            path.write_text(text + _SHADOW_LOG_HEADER_PARALLEL)

    problems_str = ",".join(f"P{p}" for p in problems) if problems else "—"
    row = (
        f"| {timestamp.strftime('%Y-%m-%dT%H:%M:%SZ')} | {mode} | {k_a} | {k_b} "
        f"| {n_cycles} | {problems_str} "
        f"| {verdict.a_improvements_per_cycle:.3f} | {verdict.b_improvements_per_cycle:.3f} "
        f"| {verdict.a_findings_per_cycle:.3f} | {verdict.b_findings_per_cycle:.3f} "
        f"| {'yes' if verdict.promote else 'no'} | {verdict.reason} |\n"
    )
    with path.open("a") as fh:
        fh.write(row)


# ---------------- orchestration ----------------


# (arm_label, k_value, problem_ids, n_cycles, cycle_log_path) -> None
ArmRunner = Callable[[str, int, list[int], int, Path], None]


def _default_arm_runner(
    arm: str, k: int, problems: list[int], n_cycles: int, cycle_log: Path
) -> None:
    """Live arm runner — drives `scripts/autonomous_loop` in-process with the
    `EINSTEIN_PARALLEL_K` flag set for this arm.

    Heavy — only invoked on a deliberate live A/B (`mode=live`); the
    wiring-validation path injects a stub. Reuses the autonomous_loop's
    `run_queue` walk; exact problem-subset targeting needs the loop's
    own subset support (TODO follow-on).
    """
    import sys

    sys.path.insert(0, str(_REPO / "scripts"))
    import autonomous_loop as al  # type: ignore[import-not-found]

    prev = os.environ.get("EINSTEIN_PARALLEL_K")
    os.environ["EINSTEIN_PARALLEL_K"] = str(k)
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
            os.environ.pop("EINSTEIN_PARALLEL_K", None)
        else:
            os.environ["EINSTEIN_PARALLEL_K"] = prev


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
    k_a: int = 4,
    k_b: int = 1,
    now: dt.datetime | None = None,
) -> ShadowABResult:
    """Run both arms, parse each arm's cycle-log, decide, and append a verdict.

    Inject a stub `arm_runner` to validate the harness without a live campaign.
    """
    now = now or dt.datetime.now(dt.timezone.utc)
    arm_runner("A", k_a, problems, n_cycles, arm_a_log)
    arm_runner("B", k_b, problems, n_cycles, arm_b_log)
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
        k_a=k_a,
        k_b=k_b,
    )
    log.info("parallel-K shadow A/B verdict: promote=%s — %s", verdict.promote, verdict.reason)
    return ShadowABResult(verdict=verdict, arm_a_rows=arm_a_rows, arm_b_rows=arm_b_rows)


__all__ = [
    "DEFAULT_SHADOW_LOG",
    "ShadowABResult",
    "Verdict",
    "append_run",
    "decide",
    "run_shadow_ab",
]
