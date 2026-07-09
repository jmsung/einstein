"""auto_submit.py — 6-gate decision chain for autonomous arena submissions.

Replaces the human-approval-each-time policy of old axiom A2 (per the
revised .claude/rules/axioms.md, 2026-05-24). The autonomous loop may
auto-submit a candidate IFF every gate below passes; otherwise the
candidate is logged for human review.

Gate order (fail-fast — cheapest checks first):

  1. Kill switch         — env EINSTEIN_AUTO_SUBMIT=0 disables all auto-submit
  2. Triple-verify       — caller must pass triple_verify['passed'] = True
  3. Daily cap           — default 5 auto-submits/day across all problems
  4. Per-problem throttle — default 1h between auto-submits per problem_id
  5. Arena #1 SOTA gate  — fetch live leaderboard; our score must beat #1
                            by ≥ min_improvement. Not just beating our own
                            prior best — must be a real new arena record.
  6. POST + audit log    — call arena_submit.submit_solution; record outcome
                            in mb/logs/auto-submit.md regardless of HTTP result.

Every decision (submit / reject) appends one row to the audit log so the
human can review weekly. No silent rejections.
"""

from __future__ import annotations

import datetime as dt
import fcntl
import json
import logging
import os
import urllib.error
import urllib.request
from dataclasses import dataclass, field
from pathlib import Path
from typing import Callable

# Sibling import — arena_submit is the POST layer (A1)
from . import arena_submit

log = logging.getLogger("auto_submit")

_REPO = Path(__file__).resolve().parents[2]
# mb is the private workspace sibling of cb; audit log lives there
DEFAULT_AUDIT_LOG = _REPO.parent / "mb" / "logs" / "auto-submit.md"
DEFAULT_MIN_IMPROVEMENT = 1e-8
DEFAULT_THROTTLE_MINUTES = 60
DEFAULT_DAILY_CAP = 5
ARENA_API_BASE = "https://einsteinarena.com/api"

KILL_SWITCH_ENV = "EINSTEIN_AUTO_SUBMIT"  # set to "0" to disable

# Per-problem optimisation direction. True = minimise (a LOWER arena score
# wins), False = maximise (a HIGHER arena score wins). Source: each problem's
# evaluator docstring (arena-verifier convention). This is the single source of
# truth gate 5 needs — `try_submit(minimize=...)` is meaningless without it.
#
# Why this exists: on 2026-06-04 the autonomous loop submitted a *worse* P2
# score (1.5028628585992 > arena #1 1.5028609073611, and P2 is minimise) as a
# "new record" twice, because the caller never passed `minimize`, so gate 5
# defaulted to maximise. Callers MUST look the direction up here and fail closed
# when a problem is absent (never guess). See
# knowledge/wiki/findings/dead-end-auto-submit-direction-sign.md.
PROBLEM_MINIMIZE: dict[int, bool] = {
    1: True,  # erdos-overlap          — "Lower C is better"
    2: True,  # first-autocorrelation  — "Minimize C(f) = max(f★f)/(∫f)²"
    3: False,  # second-autocorrelation — "Higher C is better"
    4: True,  # third-autocorrelation  — max(f★f)/(∫f)², minimise (P2 family)
    5: True,  # min-distance-ratio     — "Minimizing Max/Min Distance Ratio"
    7: False,  # prime-number-theorem   — "Higher S is better"
    9: True,  # uncertainty-principle  — "Minimize a ... uncertainty bound"
    10: True,  # thomson-n282           — "Lower score is better"
    11: False,  # tammes-n50             — "maximize min distance"
    12: True,  # flat-polynomials       — "Lower score is better"
    13: False,  # edges-triangles        — "higher (less negative) is better"
    14: False,  # circle-packing-square  — "Maximize Σ r_i"
    15: False,  # heilbronn-triangles    — "maximize the ... min triangle area"
    16: False,  # heilbronn-convex       — "maximize the area of the smallest triangle"
    18: False,  # circles-rectangle      — "maximizing the sum of radii"
    19: True,  # difference-bases       — "minimizing |B|²/v"
    22: True,  # kissing-d12            — "Lower score is better"
    24: True,  # kissing-d11-605        — "Lower score is better" (fixed-n family)
    25: True,  # kissing-d12-842        — "Lower score is better" (fixed-n family)
}

AUDIT_LOG_HEADER = (
    "| timestamp_utc | problem_id | score | decision | reason | "
    "http_status | arena_id |\n"
    "|---|---|---|---|---|---|---|\n"
)


@dataclass
class AutoSubmitResult:
    """Outcome of one try_submit call."""

    submitted: bool
    problem_id: int
    score: float | None = None
    rejected_at_gate: str | None = None
    reason: str | None = None
    submission: arena_submit.SubmissionResult | None = None
    arena_top1_score: float | None = None
    extra: dict = field(default_factory=dict)


# ---------------- audit log ----------------


_AUDIT_PREAMBLE = "# auto-submit audit log\n\n" + AUDIT_LOG_HEADER


def _append_audit_row(
    audit_log: Path,
    *,
    timestamp: dt.datetime,
    problem_id: int,
    score: float | None,
    decision: str,
    reason: str,
    http_status: int | None = None,
    arena_id: str | None = None,
) -> None:
    """Append one row to mb/logs/auto-submit.md."""
    score_s = f"{score:.14g}" if isinstance(score, (int, float)) else "—"
    status_s = str(http_status) if http_status is not None else "—"
    arena_s = str(arena_id) if arena_id is not None else "—"
    # Pipe-escape pipes in the reason text to keep the markdown table valid
    reason_safe = (reason or "").replace("|", "\\|")
    row = (
        f"| {timestamp.strftime('%Y-%m-%dT%H:%M:%SZ')} | {problem_id} | "
        f"{score_s} | {decision} | {reason_safe} | {status_s} | {arena_s} |\n"
    )
    # The kissing family runs one push-loop per problem, all sharing this single
    # audit log. An exclusive flock serializes concurrent appends so rows never
    # interleave or clobber each other (harness mb-safety, PR #18). The header is
    # written on first use UNDER the same lock — doing it in a pre-lock
    # check-then-write would let two concurrent first-writers each see the file
    # missing and the second's header truncate the first's row (defeating the
    # gate: a lost `submitted` row bypasses the daily-cap / throttle counters).
    audit_log.parent.mkdir(parents=True, exist_ok=True)
    with audit_log.open("a") as fh:
        try:
            fcntl.flock(fh.fileno(), fcntl.LOCK_EX)
            if os.fstat(fh.fileno()).st_size == 0:
                fh.write(_AUDIT_PREAMBLE)
            fh.write(row)
        finally:
            fcntl.flock(fh.fileno(), fcntl.LOCK_UN)


def _parse_audit_log(audit_log: Path) -> list[dict]:
    """Return list of past auto-submit decisions, oldest first.

    Each row: {timestamp: datetime, problem_id: int, decision: str}.
    Rejected rows count toward the daily cap iff decision == "submitted"
    (per axiom — only actual submissions count). Throttle uses submitted-only too.
    """
    if not audit_log.is_file():
        return []
    rows: list[dict] = []
    for line in audit_log.read_text().splitlines():
        if not line.startswith("| 20"):  # match ISO timestamps
            continue
        parts = [p.strip() for p in line.strip("|").split("|")]
        if len(parts) < 4:
            continue
        try:
            ts = dt.datetime.strptime(parts[0], "%Y-%m-%dT%H:%M:%SZ")
            ts = ts.replace(tzinfo=dt.timezone.utc)
        except ValueError:
            continue
        try:
            pid = int(parts[1])
        except ValueError:
            continue
        rows.append({"timestamp": ts, "problem_id": pid, "decision": parts[3]})
    return rows


# ---------------- arena #1 SOTA fetcher ----------------


def _fetch_arena_top1_score(problem_id: int, *, timeout: int = 15) -> float | None:
    """Query /api/solutions/best?problem_id=N&limit=1 and return the top score.

    Returns None on network failure / unexpected shape — caller treats that
    as "leaderboard unavailable" and rejects.
    """
    url = f"{ARENA_API_BASE}/solutions/best?problem_id={problem_id}&limit=1"
    try:
        with urllib.request.urlopen(url, timeout=timeout) as resp:
            data = json.loads(resp.read())
    except (urllib.error.URLError, json.JSONDecodeError, OSError) as e:
        log.warning("arena leaderboard fetch failed for P%d: %s", problem_id, e)
        return None
    if not isinstance(data, list) or not data:
        return None
    top = data[0]
    if not isinstance(top, dict):
        return None
    score = top.get("score")
    try:
        return float(score) if score is not None else None
    except (TypeError, ValueError):
        return None


# ---------------- main entry point ----------------


def try_submit(
    problem_id: int,
    payload: dict,
    score: float,
    *,
    triple_verify: dict | None = None,
    min_improvement: float = DEFAULT_MIN_IMPROVEMENT,
    minimize: bool = False,
    arena_top1_score: float | None = None,
    audit_log: Path | None = None,
    throttle_minutes: int = DEFAULT_THROTTLE_MINUTES,
    daily_cap: int = DEFAULT_DAILY_CAP,
    leaderboard_fetcher: Callable[[int], float | None] | None = None,
    submitter: Callable[..., arena_submit.SubmissionResult] | None = None,
    clock: Callable[[], dt.datetime] | None = None,
    dry_run: bool = False,
) -> AutoSubmitResult:
    """Decide whether to auto-submit `(score, payload)` for `problem_id`.

    Runs the 6 gates in order; submits only if all pass. Every decision is
    appended to the audit log regardless of outcome.

    Required:
      - `triple_verify`: dict with key `"passed"` (bool). Optional keys
        `"fast"`, `"exact"`, `"cross"` for the audit reason text.

    Optional knobs:
      - `min_improvement` — score margin required over arena #1 (default 1e-8)
      - `minimize` — if True, "improvement" = lower; default is maximize
      - `arena_top1_score` — caller-supplied to skip the live leaderboard fetch
      - `throttle_minutes`, `daily_cap` — gate knobs
      - `leaderboard_fetcher`, `submitter`, `clock` — test seams

    Returns AutoSubmitResult. `submitted=True` iff POST succeeded with 2xx.
    """
    log_path = audit_log if audit_log is not None else DEFAULT_AUDIT_LOG
    now = (clock or (lambda: dt.datetime.now(dt.timezone.utc)))()
    if now.tzinfo is None:
        now = now.replace(tzinfo=dt.timezone.utc)

    def _record(
        *,
        submitted: bool,
        gate: str | None,
        reason: str,
        submission: arena_submit.SubmissionResult | None = None,
        arena_top1: float | None = None,
    ) -> AutoSubmitResult:
        http_status = submission.http_status if submission else None
        arena_id = None
        if submission and submission.arena_response:
            arena_id = submission.arena_response.get("id")
        decision = "submitted" if submitted else "rejected"
        _append_audit_row(
            log_path,
            timestamp=now,
            problem_id=problem_id,
            score=score,
            decision=decision,
            reason=f"{gate or 'ok'}: {reason}" if gate else reason,
            http_status=http_status,
            arena_id=arena_id,
        )
        return AutoSubmitResult(
            submitted=submitted,
            problem_id=problem_id,
            score=score,
            rejected_at_gate=gate,
            reason=reason,
            submission=submission,
            arena_top1_score=arena_top1,
        )

    # --- Gate 1: kill switch -----------------------------------------------
    if os.environ.get(KILL_SWITCH_ENV) == "0":
        return _record(
            submitted=False,
            gate="kill-switch",
            reason=f"{KILL_SWITCH_ENV}=0 — auto-submit disabled",
        )

    # --- Gate 2: triple-verify ---------------------------------------------
    if not triple_verify or not triple_verify.get("passed"):
        reason = "triple_verify['passed'] not True"
        if triple_verify:
            tv = {k: v for k, v in triple_verify.items() if k != "passed"}
            if tv:
                reason += f" (numbers: {tv})"
        return _record(submitted=False, gate="triple-verify-failed", reason=reason)

    past = _parse_audit_log(log_path)
    submitted_rows = [r for r in past if r["decision"] == "submitted"]

    # --- Gate 3: daily cap -------------------------------------------------
    today_utc = now.date()
    today_count = sum(1 for r in submitted_rows if r["timestamp"].date() == today_utc)
    if today_count >= daily_cap:
        return _record(
            submitted=False,
            gate="daily-cap",
            reason=f"{today_count} submits already today (cap={daily_cap})",
        )

    # --- Gate 4: per-problem throttle --------------------------------------
    throttle_delta = dt.timedelta(minutes=throttle_minutes)
    recent_for_problem = [
        r
        for r in submitted_rows
        if r["problem_id"] == problem_id and (now - r["timestamp"]) < throttle_delta
    ]
    if recent_for_problem:
        last_ts = max(r["timestamp"] for r in recent_for_problem)
        mins_since = int((now - last_ts).total_seconds() / 60)
        return _record(
            submitted=False,
            gate="throttle",
            reason=f"P{problem_id} last submitted {mins_since}min ago "
            f"(throttle={throttle_minutes}min)",
        )

    # --- Gate 5: arena #1 SOTA improvement ---------------------------------
    if arena_top1_score is None:
        fetcher = leaderboard_fetcher or _fetch_arena_top1_score
        arena_top1_score = fetcher(problem_id)
    if arena_top1_score is None:
        return _record(
            submitted=False,
            gate="leaderboard-unavailable",
            reason="could not fetch arena #1 score — refusing to submit blind",
        )
    if minimize:
        beats = arena_top1_score - score >= min_improvement
        delta = arena_top1_score - score
    else:
        beats = score - arena_top1_score >= min_improvement
        delta = score - arena_top1_score
    if not beats:
        return _record(
            submitted=False,
            gate="no-improvement",
            reason=f"score={score:.14g} vs arena #1={arena_top1_score:.14g} "
            f"(delta={delta:.3g}, need ≥{min_improvement:g})",
            arena_top1=arena_top1_score,
        )

    # --- Gate 6: POST + audit ----------------------------------------------
    if dry_run:
        return _record(
            submitted=False,
            gate="dry-run",
            reason=f"all gates passed, would POST (delta={delta:.3g})",
            arena_top1=arena_top1_score,
        )

    submit_fn = submitter or arena_submit.submit_solution
    sub = submit_fn(problem_id, payload, expected_score=score)

    if not sub.ok:
        return _record(
            submitted=False,
            gate="post-failed",
            reason=f"submit_solution failed: {sub.error}",
            submission=sub,
            arena_top1=arena_top1_score,
        )

    return _record(
        submitted=True,
        gate=None,
        reason=f"new arena record: {score:.14g} beats #1={arena_top1_score:.14g} by {delta:.3g}",
        submission=sub,
        arena_top1=arena_top1_score,
    )
