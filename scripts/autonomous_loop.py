#!/usr/bin/env python3
"""autonomous_loop.py — outer loop over the 23 Einstein Arena problems.

Architecture (this file = OUTER loop only; the inner attempt is filled
by Goal 4):

    1. Load problem queue (docs/wiki/problems/*.md frontmatter)
    2. Filter by status (skip blocked / hidden / shelved / frozen / conquered)
    3. Sort by tier (S>A>B>C) then problem_id ascending
    4. For each problem in the queue:
       a. inner_attempt(problem)  — placeholder for Goal 4
       b. record_cycle_row(...)   — append to docs/agent/cycle-log.md
       c. cycle_runner.sh(cycle_id, problem)  — discipline (refresh_qmd,
          wiki_graph, gap_search, promotion check)

Usage:
    uv run python scripts/autonomous_loop.py --one-problem
    uv run python scripts/autonomous_loop.py --one-problem --dry-run
    uv run python scripts/autonomous_loop.py --max-problems 3
    uv run python scripts/autonomous_loop.py --queue-only      # just print

Per .claude/rules/cycle-discipline.md: every cycle gets exactly one row in
docs/agent/cycle-log.md. This module is the row-writer for autonomous
cycles; human-driven cycles still hand-author their rows.
"""

from __future__ import annotations

import argparse
import datetime as dt
import logging
import os
import re
import subprocess
import sys
import time
from dataclasses import dataclass, field
from pathlib import Path
from typing import Callable

_REPO = Path(__file__).resolve().parents[1]
DEFAULT_PROBLEMS_DIR = _REPO / "docs" / "wiki" / "problems"
DEFAULT_CYCLE_LOG = _REPO / "docs" / "agent" / "cycle-log.md"
DEFAULT_CYCLE_RUNNER = _REPO / "docs" / "tools" / "cycle_runner.sh"
DEFAULT_SKILL_LIBRARY = _REPO / "docs" / "agent" / "skill-library.md"
DEFAULT_LOCKFILE = _REPO / ".autonomous-loop.lock"
# mb is the umbrella's sibling of cb; under the worktree the umbrella mb
# lives one level up. See `mb/active/feat-autonomous-loop.md` operational
# decisions for the layout contract.
DEFAULT_MB_DIR = _REPO.parent / "mb"
DEFAULT_BUDGET_PATH = DEFAULT_MB_DIR / "logs" / "inner-agent-budget.md"
DEFAULT_SENTINEL_PATH = DEFAULT_MB_DIR / ".inner-agent-disabled"

# Local imports — strategy_picker + inner_agent_gates live in docs/tools/
sys.path.insert(0, str(_REPO / "docs" / "tools"))
try:
    import strategy_picker  # type: ignore[import-not-found]
except ImportError:
    strategy_picker = None  # type: ignore[assignment]
try:
    import inner_agent_gates  # type: ignore[import-not-found]
except ImportError:
    inner_agent_gates = None  # type: ignore[assignment]

log = logging.getLogger("autonomous_loop")

FM_RE = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)
ROW_ID_RE = re.compile(r"^\|\s*(\d+)\s*\|")

# Statuses considered permanently inactive — only `retired` (the 5 dead pages
# archived 2026-05-23). Everything else — frozen, hidden, blocked, conquered,
# rank-N-frozen, shelved, rank-N-frozen-by-proximity-guard — is still a live
# arena problem. A more powerful agent should attempt every live problem in
# id order; let inner-loop convergence-detect / strategy-picker decide if
# real work is feasible. Local status often drifts from arena state anyway.
SKIP_STATUSES = {"retired"}


# ---------------- data model ----------------


@dataclass
class Problem:
    problem_id: int
    slug: str
    tier: str
    status: str
    score_current: float | None
    path: Path
    extra: dict = field(default_factory=dict)

    @property
    def display(self) -> str:
        return f"P{self.problem_id}-{self.slug}"

    @property
    def file_slug(self) -> str:
        return f"{self.problem_id}-{self.slug}"


@dataclass
class CycleResult:
    cycle_id: int
    problem: Problem
    outcome: str
    notes: str


# ---------------- frontmatter parsing ----------------


def _parse_frontmatter(text: str) -> dict | None:
    m = FM_RE.match(text)
    if not m:
        return None
    fm: dict = {}
    for line in m.group(1).splitlines():
        kv = re.match(r"^([a-zA-Z_]+):\s*(.*)$", line)
        if not kv:
            continue
        key, val = kv.group(1), kv.group(2).strip()
        fm[key] = val.strip().strip("\"'")
    return fm


def load_problems(problems_dir: Path) -> list[Problem]:
    """Parse every problem page in `problems_dir`. Skips _*.md and README.md."""
    problems: list[Problem] = []
    for path in sorted(problems_dir.glob("*.md")):
        name = path.name
        if name.startswith("_") or name == "README.md":
            continue
        fm = _parse_frontmatter(path.read_text())
        if not fm or "problem_id" not in fm:
            log.warning("skipping %s — no/invalid frontmatter", path.name)
            continue
        try:
            pid = int(fm["problem_id"])
        except ValueError:
            continue

        # Slug derived from filename: '1-erdos-overlap.md' → 'erdos-overlap'
        stem = path.stem  # '1-erdos-overlap'
        slug_match = re.match(r"^(\d+[a-z]?)-(.+)$", stem)
        slug = slug_match.group(2) if slug_match else stem

        score: float | None = None
        if fm.get("score_current"):
            try:
                score = float(fm["score_current"])
            except ValueError:
                pass

        problems.append(
            Problem(
                problem_id=pid,
                slug=slug,
                tier=fm.get("tier", "?"),
                status=fm.get("status", "unknown"),
                score_current=score,
                path=path,
                extra=fm,
            )
        )
    return problems


# ---------------- queue ----------------


def is_active(problem: Problem) -> bool:
    """True unless the problem is permanently inactive (retired)."""
    return problem.status not in SKIP_STATUSES


def build_queue(problems: list[Problem]) -> list[Problem]:
    """Return live problems ordered by problem_id ascending.

    Goes through every live arena problem regardless of local status (frozen,
    conquered, blocked, hidden, etc.) — only `retired` is filtered. Tier-based
    prioritization removed: a powerful agent should attempt every problem in
    id order and let inner-loop logic decide viability.
    """
    return sorted(
        (p for p in problems if is_active(p)),
        key=lambda p: p.problem_id,
    )


# ---------------- cycle-log row ----------------


def _author_mix(d: dict[str, int]) -> str:
    return f"a:{d.get('agent', 0)}/h:{d.get('human', 0)}/hyb:{d.get('hybrid', 0)}"


def format_cycle_log_row(
    *,
    cycle_id: int,
    problem: str,
    start_score: float | str,
    end_score: float | str,
    hours: float,
    compute: str,
    wiki_citations: int,
    findings_added: int,
    concepts_added: int,
    author_mix: dict[str, int],
    outcome: str,
    notes: str,
) -> str:
    """Produce one markdown table row matching docs/agent/cycle-log.md schema."""

    def _fmt_score(s: float | str) -> str:
        if isinstance(s, (int, float)):
            # 14 sig figs preserves problem scores like 2.6390274695 and
            # 1.5028616283497658 without truncation.
            return f"{s:.14g}"
        return str(s)

    s_start = _fmt_score(start_score)
    s_end = _fmt_score(end_score)
    score_pair = f"{s_start} → {s_end}" if s_start != s_end else f"{s_start} (no Δ)"
    return (
        f"| {cycle_id} | {problem} | {score_pair} | {hours:g} | {compute} | "
        f"{wiki_citations} | {findings_added} | {concepts_added} | "
        f"{_author_mix(author_mix)} | {outcome} | {notes} |"
    )


def append_cycle_log_row(cycle_log: Path, row: str) -> None:
    """Append `row` (no newline) to the end of `cycle_log`."""
    text = cycle_log.read_text() if cycle_log.exists() else ""
    if text and not text.endswith("\n"):
        text += "\n"
    text += row + "\n"
    cycle_log.write_text(text)


def next_cycle_id(cycle_log: Path) -> int:
    """Read existing cycle ids from the log; return max + 1, or 0 if empty."""
    if not cycle_log.exists():
        return 0
    max_id = -1
    for line in cycle_log.read_text().splitlines():
        m = ROW_ID_RE.match(line)
        if m:
            try:
                max_id = max(max_id, int(m.group(1)))
            except ValueError:
                continue
    return max_id + 1


# ---------------- inner attempt placeholder ----------------


def _call_auto_submit(
    *,
    problem: Problem,
    score: float,
    payload: dict,
    auto_submitter: Callable[..., object] | None,
    notes_parts: list[str],
    notifier: Callable[..., bool] | None = None,
) -> str | None:
    """Run the A2 auto-submit gate chain. Returns an outcome override
    ("improved-and-submitted") if the gate chain accepted, else None.

    Triple-verify is hardcoded `passed=False` — per-problem verifiers land
    separately. The audit row in `mb/logs/auto-submit.md` records every
    decision regardless of acceptance.

    On `submitted=True`, fires a macOS notification (Goal 7.8c). The
    notifier is a test seam — defaults to `notify_milestone.notify_arena_record`.
    Notification failures are silent (best-effort UX, never load-bearing).

    Mutates `notes_parts` in place with the auto-submit decision tag.
    """
    if auto_submitter is None:
        try:
            from einstein.auto_submit import try_submit as _real_submit

            auto_submitter = _real_submit
        except ImportError:
            return None
    sub_result = auto_submitter(
        problem.problem_id,
        payload,
        score,
        triple_verify={"passed": False, "note": "triple-verify not yet wired"},
    )
    if getattr(sub_result, "submitted", False):
        notes_parts.append("auto-submit: SUBMITTED")
        # Milestone notification — best effort, never blocks the cycle.
        if notifier is None:
            try:
                from notify_milestone import notify_arena_record as _real_notif

                notifier = _real_notif
            except ImportError:
                notifier = None
        if notifier is not None:
            try:
                notifier(problem_id=problem.problem_id, score=score)
            except Exception as e:  # pragma: no cover — defensive
                log.warning("milestone notification failed: %s", e)
        return "improved-and-submitted"
    gate = getattr(sub_result, "rejected_at_gate", "?")
    notes_parts.append(f"auto-submit-rejected@{gate}")
    return None


def _try_llm_path(
    *,
    problem: Problem,
    attempt_index: int,
    avoid_techniques: set[str] | None,
    auto_submitter: Callable[..., object] | None,
    headless_runner: Callable[..., object] | None = None,
    prompt_renderer: Callable[..., str] | None = None,
    response_parser: Callable[[str], object] | None = None,
    budget_recorder: Callable[..., object] | None = None,
    budget_path: Path = DEFAULT_BUDGET_PATH,
    timeout_seconds: int = 1800,
) -> dict | None:
    """Best-effort LLM cycle (Goal 7.7).

    Pipeline:
      1. Render the prompt (inner_agent_prompt.render_prompt)
      2. Invoke claude_headless.run with the autonomous-loop tool allow-list
      3. Parse the agent's JSON reply (inner_agent_output.parse_response)
      4. Record estimated token usage in the daily budget ledger
      5. If the agent ran the optimizer (score + payload), hand to auto_submit
      6. Build the cycle-log result dict shaped like the mechanical path

    Returns None on any failure — caller falls back to mechanical. Failure
    paths logged at WARNING; we never raise from this function.
    """
    try:
        if prompt_renderer is None:
            from inner_agent_prompt import render_prompt as _real_render

            prompt_renderer = _real_render
        if headless_runner is None:
            from claude_headless import run as _real_run

            headless_runner = _real_run
        if response_parser is None:
            from inner_agent_output import parse_response as _real_parse

            response_parser = _real_parse
        if budget_recorder is None:
            try:
                from inner_agent_gates import record_token_usage as _real_rec

                budget_recorder = _real_rec
            except ImportError:
                budget_recorder = None
    except ImportError as e:
        log.warning("LLM path components unavailable (%s) — falling back", e)
        return None

    category = (
        strategy_picker.category_for(problem.problem_id) if strategy_picker is not None else "?"
    )
    try:
        prompt = prompt_renderer(
            problem_id=problem.problem_id,
            problem_slug=problem.slug,
            file_slug=problem.file_slug,
            score_current=problem.score_current,
            status=problem.status,
            tier=problem.tier,
            category=category,
            # cycle_id isn't threaded yet — informational only in the prompt
            cycle_id=0,
            attempt_index=attempt_index,
        )
    except Exception as e:
        log.warning("render_prompt failed: %s — falling back", e)
        return None

    # Tool allow-list reflects what the agent actually needs to run the
    # math-solving-protocol per `.claude/rules/`. Write is allowed so the
    # agent can create findings / questions / dead-end pages under
    # docs/wiki/ + mb/ per wiki-attribution (author: agent). Scope is
    # enforced by --add-dir (cwd is cb worktree; we add the sibling mb so
    # those writes land too). The prompt instructs the agent to restrict
    # writes to docs/wiki/* and mb/* paths; the 7.6 git-status audit
    # captures every actual write for human review.
    allowed_tools = [
        "Read",
        "Grep",
        "Write",
        "Bash(qmd:*)",
        "Bash(gap_search.py:*)",
        "Bash(uv run python -m einstein.optimizer_dispatch:*)",
        "Task",
    ]

    try:
        run_result = headless_runner(
            prompt,
            allowed_tools=allowed_tools,
            timeout_seconds=timeout_seconds,
            add_dirs=[DEFAULT_MB_DIR],
        )
    except Exception as e:
        log.warning("claude_headless raised unexpectedly: %s — falling back", e)
        return None

    if not getattr(run_result, "ok", False):
        log.warning(
            "claude_headless not ok: kind=%s msg=%s — falling back",
            getattr(run_result, "error_kind", "?"),
            getattr(run_result, "error_message", "?"),
        )
        return None

    try:
        response = response_parser(run_result.stdout)
    except Exception as e:
        log.warning("inner_agent_output.parse_response failed: %s — falling back", e)
        return None

    # Estimate token usage from char counts (rough 4 chars / token). The
    # exact count would require `claude -p --output-format json` and
    # envelope parsing, which is a heavier path. Estimate is good enough
    # for the daily-budget gate.
    input_estimate = len(prompt) // 4
    output_estimate = len(run_result.stdout) // 4
    if budget_recorder is not None:
        try:
            budget_recorder(
                budget_path,
                input_tokens=input_estimate,
                output_tokens=output_estimate,
            )
        except Exception as e:
            log.warning("budget recorder failed: %s (continuing)", e)

    # Build the cycle-log result dict
    notes_parts: list[str] = []
    if attempt_index > 1:
        notes_parts.append(f"attempt={attempt_index}")
    notes_parts.append(f"category={category}")
    notes_parts.append(f"llm-strategy={response.strategy}")
    notes_parts.append(f"tokens=in:{input_estimate}/out:{output_estimate}")

    start_score = problem.score_current
    end_score: float | str = (
        response.score
        if response.score is not None
        else (problem.score_current if problem.score_current is not None else "none")
    )

    # Outcome priority: converged > dead-end > improvement vs start > no-change
    if response.converged:
        outcome = "converged"
    elif response.dead_end_finding:
        outcome = "dead-end"
        notes_parts.append(f"dead_end={response.dead_end_finding}")
    elif response.score is not None and start_score is not None and response.score < start_score:
        outcome = "improved-local"
    elif response.score is not None:
        outcome = "no-change"
    else:
        outcome = "llm-no-execution"

    # If we have score + payload, hand to auto_submit (Goal A3 wiring).
    if response.score is not None and response.payload is not None:
        override = _call_auto_submit(
            problem=problem,
            score=response.score,
            payload=response.payload,
            auto_submitter=auto_submitter,
            notes_parts=notes_parts,
        )
        if override is not None:
            outcome = override

    # Surface the agent's notes verbatim (≤ 200 chars per schema)
    if response.notes:
        notes_parts.append(f"agent={response.notes}")

    notes = "autonomous_loop LLM cycle — " + "; ".join(notes_parts)

    return {
        "start_score": start_score if start_score is not None else "none",
        "end_score": end_score,
        # claude_headless doesn't expose wall-clock directly; rough estimate
        # via wall-clock measurement is a follow-up. 0.0 is honest about
        # "unknown" until the headless wrapper surfaces timing.
        "hours": 0.0,
        "compute": "local-cpu+llm",
        "wiki_citations": 0,
        "findings_added": 1 if response.dead_end_finding else 0,
        "concepts_added": 0,
        "author_mix": {"agent": 1, "human": 0, "hybrid": 0},
        "outcome": outcome,
        "notes": notes,
        "chosen_techniques": [response.strategy] if response.strategy else [],
    }


def inner_attempt(
    problem: Problem,
    dry_run: bool = False,
    skill_library: Path = DEFAULT_SKILL_LIBRARY,
    dispatcher: Callable[..., object] | None = None,
    auto_submitter: Callable[..., object] | None = None,
    attempt_index: int = 1,
    avoid_techniques: set[str] | None = None,
    llm_enabled: bool = False,
    headless_runner: Callable[..., object] | None = None,
    prompt_renderer: Callable[..., str] | None = None,
    response_parser: Callable[[str], object] | None = None,
    budget_recorder: Callable[..., object] | None = None,
    budget_path: Path = DEFAULT_BUDGET_PATH,
) -> dict:
    """Reflection chain for one cycle attempt.

    Two paths:

      - **LLM** (Goal 7.7) — when `llm_enabled=True` and `claude_headless` +
        `inner_agent_prompt` + `inner_agent_output` are importable. The
        agent runs the math-solving-protocol via `claude -p`; this function
        parses the structured reply and threads score/payload to auto_submit.
      - **Mechanical** — default. strategy_picker reads skill-library +
        optimizer_dispatch invokes the per-problem optimizer.

    LLM path falls back to mechanical on ANY error (import, render, claude
    unavailable, parse, etc.) so the loop is resilient. Default is
    mechanical (`llm_enabled=False`) to keep direct test callers honest;
    `run_one_visit` flips it to True when the gate decision says so.

    `dispatcher` / `auto_submitter` / `headless_runner` / `prompt_renderer`
    / `response_parser` / `budget_recorder` are test seams.

    Returns a dict shaped for `format_cycle_log_row` plus an extra
    `chosen_techniques` key (list[str], not part of the cycle-log schema) so
    `run_one_visit` can build the avoid set for the next attempt.
    """
    if llm_enabled and not dry_run:
        llm_result = _try_llm_path(
            problem=problem,
            attempt_index=attempt_index,
            avoid_techniques=avoid_techniques,
            auto_submitter=auto_submitter,
            headless_runner=headless_runner,
            prompt_renderer=prompt_renderer,
            response_parser=response_parser,
            budget_recorder=budget_recorder,
            budget_path=budget_path,
        )
        if llm_result is not None:
            return llm_result
        log.info("LLM path unavailable — using mechanical fallback")

    log.info(
        "inner_attempt — problem=%s tier=%s status=%s attempt=%d",
        problem.display,
        problem.tier,
        problem.status,
        attempt_index,
    )

    notes_parts: list[str] = []
    chosen_strategy: str | None = None
    chosen_techniques: list[str] = []
    if attempt_index > 1:
        notes_parts.append(f"attempt={attempt_index}")
    if strategy_picker is None:
        log.warning("strategy_picker not importable — skipping strategy pick")
        notes_parts.append("strategy_picker unavailable")
    else:
        category = strategy_picker.category_for(problem.problem_id)
        log.info("  category=%s", category)
        pick = strategy_picker.pick_strategy(
            skill_library,
            category=category,
            avoid_techniques=avoid_techniques,
        )
        log.info("  %s", pick.rationale)
        notes_parts.append(f"category={category}")
        if pick.prior is not None:
            notes_parts.append(f"prior={pick.prior.technique}({pick.prior.hit_rate:.2f})")
            chosen_strategy = pick.prior.technique
            chosen_techniques.append(pick.prior.technique)
        if pick.novel is not None:
            notes_parts.append(
                f"novel={pick.novel.technique}(finding_rate={pick.novel.finding_rate:.2f})"
            )
            # Novel takes precedence as the strategy name passed to dispatch
            chosen_strategy = pick.novel.technique
            chosen_techniques.append(pick.novel.technique)
        if pick.prior is None and pick.novel is None:
            notes_parts.append("(no library matches — council needed)")

    # EXECUTE step — optimizer_dispatch
    start_score = problem.score_current
    end_score = problem.score_current
    outcome = "scaffold-no-attempt"
    runtime_hours = 0.0
    compute_tag = "none-strategy-only"

    if dispatcher is None:
        # Lazy import — dispatch lives in src/einstein, not docs/tools
        sys.path.insert(0, str(_REPO / "src"))
        try:
            from einstein.optimizer_dispatch import dispatch as _real_dispatch

            dispatcher = _real_dispatch
        except ImportError:
            log.warning("optimizer_dispatch unavailable — skipping execute")
            dispatcher = None

    if dispatcher is not None and not dry_run:
        result = dispatcher(problem_id=problem.problem_id, strategy=chosen_strategy)
        if getattr(result, "error", None) and "no manifest entry" in result.error:
            log.info("  no manifest entry for P%d — execute deferred", problem.problem_id)
            notes_parts.append("dispatch: no-manifest-entry")
            outcome = "strategy-picked-no-execution"
        elif result.ok:
            log.info(
                "  dispatch ok: optimizer=%s score=%s runtime=%.1fs",
                result.optimizer,
                result.score,
                result.runtime_seconds,
            )
            notes_parts.append(f"dispatch={result.optimizer} score={result.score}")
            end_score = result.score
            runtime_hours = result.runtime_seconds / 3600.0
            compute_tag = "local-cpu"  # TODO: thread compute_router decision through
            if start_score is not None and result.score is not None and result.score < start_score:  # type: ignore[operator]
                outcome = "improved-local"
            else:
                outcome = "no-change"

            # A3: hand the candidate to auto_submit's gate chain (shared with
            # the LLM path via `_call_auto_submit`). Triple-verify is NOT yet
            # implemented per-problem; passed=False rejects every candidate
            # at the verify gate but still writes the audit row.
            if (
                result.score is not None
                and getattr(result, "payload", None) is not None
                and not dry_run
            ):
                override = _call_auto_submit(
                    problem=problem,
                    score=result.score,
                    payload=result.payload,
                    auto_submitter=auto_submitter,
                    notes_parts=notes_parts,
                )
                if override is not None:
                    outcome = override
        else:
            log.warning("  dispatch failed: %s", result.error)
            notes_parts.append(f"dispatch-failed: {result.error}")
            outcome = "dispatch-failed"
    elif dry_run:
        notes_parts.append("dry-run (dispatch skipped)")

    notes = "autonomous_loop inner_attempt — " + "; ".join(notes_parts)

    return {
        "start_score": start_score if start_score is not None else "none",
        "end_score": end_score if end_score is not None else "none",
        "hours": runtime_hours,
        "compute": compute_tag,
        "wiki_citations": 0,
        "findings_added": 0,
        "concepts_added": 0,
        "author_mix": {"agent": 1, "human": 0, "hybrid": 0},
        "outcome": outcome,
        "notes": notes,
        # Extra field — NOT part of the cycle-log schema. Consumed by
        # run_one_visit to build the avoid set for the next attempt.
        "chosen_techniques": chosen_techniques,
    }


# ---------------- cycle-log row formatting helper ----------------


_CYCLE_LOG_ROW_KEYS = (
    "start_score",
    "end_score",
    "hours",
    "compute",
    "wiki_citations",
    "findings_added",
    "concepts_added",
    "author_mix",
    "outcome",
    "notes",
)


def _row_from_attempt(attempt_result: dict) -> dict:
    """Strip the non-schema `chosen_techniques` key before passing to
    `format_cycle_log_row` — that helper takes **kwargs and would error on
    unknown args."""
    return {k: attempt_result[k] for k in _CYCLE_LOG_ROW_KEYS}


# ---------------- wiki/mb write audit (Goal 7.6) ----------------


# Cap on the wiki_writes paths appended to the cycle-log notes column.
# notes is meant to be a one-line gloss (~200 chars in practice); listing
# 100 paths would blow that out. Beyond this cap we tag the count instead.
_MAX_WIKI_WRITE_PATHS_IN_NOTES = 5


def _snapshot_wiki_mb_paths(repo_root: Path) -> set[str]:
    """Return uncommitted paths under `docs/wiki/` + `mb/` per `git status`.

    Per Goal 7.6 the wiki-write audit is "single source of truth = git" —
    no separate audit file. Snapshot at cycle start and end; the delta is
    what this cycle wrote.

    Captures both new (untracked) and modified files. Renames are recorded
    under their new path. Returns the empty set if git isn't available or
    the call fails — the audit is best-effort and must never break the
    cycle.
    """
    try:
        # `--untracked-files=all` is required: the default `normal` mode
        # collapses untracked files under a previously-empty directory into a
        # single entry "docs/wiki/" instead of listing each file. The audit
        # needs the individual paths.
        proc = subprocess.run(
            ["git", "status", "--porcelain", "--untracked-files=all", "--", "docs/wiki/", "mb/"],
            capture_output=True,
            text=True,
            cwd=repo_root,
            timeout=10,
            check=False,
        )
    except (FileNotFoundError, subprocess.TimeoutExpired):
        return set()
    if proc.returncode != 0:
        log.debug("git status (audit snapshot) failed rc=%d", proc.returncode)
        return set()

    paths: set[str] = set()
    for line in proc.stdout.splitlines():
        # Porcelain v1: "XY path" or "XY old -> new"; first two cols are status.
        if len(line) < 4:
            continue
        body = line[3:].strip()
        if " -> " in body:
            body = body.split(" -> ", 1)[1].strip()
        # Quoted path when it contains spaces — strip the wrap.
        if len(body) >= 2 and body.startswith('"') and body.endswith('"'):
            body = body[1:-1]
        paths.add(body)
    return paths


def _format_wiki_writes_note(paths: list[str]) -> str:
    """Render the wiki_writes suffix for the notes column.

    Sorted, capped at _MAX_WIKI_WRITE_PATHS_IN_NOTES; tail collapsed to
    "+N more" when over the cap. Empty input → empty string (caller skips).
    """
    if not paths:
        return ""
    head = paths[:_MAX_WIKI_WRITE_PATHS_IN_NOTES]
    suffix = "wiki_writes=" + ",".join(head)
    remainder = len(paths) - len(head)
    if remainder > 0:
        suffix += f",+{remainder}-more"
    return suffix


# ---------------- single-cycle drive ----------------


CycleRunner = Callable[[int, str], int]


def _shell_cycle_runner(cycle_id: int, problem_slug: str) -> int:
    """Invoke docs/tools/cycle_runner.sh; return its exit code."""
    script = DEFAULT_CYCLE_RUNNER
    if not script.is_file():
        log.warning("cycle_runner.sh not at %s — skipping discipline step", script)
        return 0
    return subprocess.run(
        ["bash", str(script), str(cycle_id), problem_slug],
        cwd=_REPO,
        check=False,
    ).returncode


def _run_one_cycle(
    problem: Problem,
    *,
    cycle_log: Path,
    dry_run: bool,
    cycle_runner: "CycleRunner | None",
    attempt_index: int = 1,
    avoid_techniques: set[str] | None = None,
    repo_root: Path = _REPO,
    llm_enabled: bool = False,
) -> tuple[CycleResult, dict]:
    """Run exactly one inner_attempt + log row + cycle_runner for `problem`.

    Internal helper shared by `run_one_problem` (1-cycle path, kept for
    back-compat) and `run_one_visit` (1..3 cycle path, Goal 7.4).

    Order of operations (Goal 7.6 reorders cycle_runner before row append
    so wiki_graph's auto-filed questions land in the wiki-writes delta):

      1. Snapshot uncommitted wiki/mb paths (audit baseline)
      2. inner_attempt — the strategy pick + dispatch + auto_submit
      3. cycle_runner.sh — discipline (refresh_qmd → wiki_graph → gap_search → lint)
      4. Snapshot again; delta = this cycle's wiki/mb writes
      5. Augment notes with wiki_writes=… suffix; append cycle-log row

    Returns (CycleResult, attempt_result_dict). The full attempt dict is
    returned so `run_one_visit` can read `chosen_techniques` + `end_score`
    for the next attempt's avoid set + convergence-detect.
    """
    cycle_id = next_cycle_id(cycle_log)
    log.info(
        "cycle %d → %s (tier %s, status %s) attempt=%d",
        cycle_id,
        problem.display,
        problem.tier,
        problem.status,
        attempt_index,
    )

    snapshot_before = _snapshot_wiki_mb_paths(repo_root) if not dry_run else set()
    log.info(
        "audit snapshot_before: %d paths %s", len(snapshot_before), sorted(snapshot_before)[:5]
    )

    result = inner_attempt(
        problem,
        dry_run=dry_run,
        attempt_index=attempt_index,
        avoid_techniques=avoid_techniques,
        llm_enabled=llm_enabled,
    )
    cycle_result = CycleResult(
        cycle_id=cycle_id,
        problem=problem,
        outcome=result["outcome"],
        notes=result["notes"],
    )

    if dry_run:
        log.info(
            "[dry-run] would append cycle %d row to %s and call cycle_runner",
            cycle_id,
            cycle_log.name,
        )
        return cycle_result, result

    # Run cycle_runner BEFORE writing the row so the wiki-writes delta
    # includes whatever wiki_graph + gap_search auto-file this cycle.
    runner = cycle_runner or _shell_cycle_runner
    rc = runner(cycle_id, problem.file_slug)
    if rc != 0:
        log.warning("cycle_runner exited %d for cycle %d", rc, cycle_id)

    # Compute the wiki/mb delta and augment notes (Goal 7.6).
    snapshot_after = _snapshot_wiki_mb_paths(repo_root)
    wiki_writes = sorted(snapshot_after - snapshot_before)
    log.info(
        "audit snapshot_after: %d paths; delta=%d %s",
        len(snapshot_after),
        len(wiki_writes),
        wiki_writes[:5],
    )
    if wiki_writes:
        suffix = _format_wiki_writes_note(wiki_writes)
        # Avoid double-suffix if the result was already augmented (shouldn't
        # happen, but defensive — keeps idempotency).
        if "wiki_writes=" not in result["notes"]:
            result = {**result, "notes": result["notes"] + "; " + suffix}
            # Update CycleResult.notes too so callers see the augmented text.
            cycle_result = CycleResult(
                cycle_id=cycle_id,
                problem=problem,
                outcome=result["outcome"],
                notes=result["notes"],
            )

    row = format_cycle_log_row(
        cycle_id=cycle_id,
        problem=problem.display,
        **_row_from_attempt(result),
    )
    append_cycle_log_row(cycle_log, row)

    return cycle_result, result


def run_one_problem(
    *,
    problems_dir: Path = DEFAULT_PROBLEMS_DIR,
    cycle_log: Path = DEFAULT_CYCLE_LOG,
    dry_run: bool = False,
    cycle_runner: CycleRunner | None = None,
    skip_problem_ids: set[int] | None = None,
) -> CycleResult | None:
    """Pick the top-priority active problem and run ONE cycle on it.

    Kept as the single-cycle entry point. For up-to-3-cycle visits with
    convergence-detect, use `run_one_visit`.

    Returns None if the queue is empty (no active problems).
    """
    problems = load_problems(problems_dir)
    queue = build_queue(problems)
    if skip_problem_ids:
        queue = [p for p in queue if p.problem_id not in skip_problem_ids]
    if not queue:
        log.info("queue empty — no active problems")
        return None

    cycle_result, _ = _run_one_cycle(
        queue[0],
        cycle_log=cycle_log,
        dry_run=dry_run,
        cycle_runner=cycle_runner,
    )
    return cycle_result


# ---------------- visit (Goal 7.4) ----------------


DEFAULT_MAX_ATTEMPTS_PER_VISIT = 3


def _write_gate_skip_row(
    *,
    problem: Problem,
    cycle_log: Path,
    reason: str,
) -> CycleResult:
    """Honor cycle-discipline: gate skips still get a cycle-log row.

    Writes one `outcome: gate-skipped` row + a CycleResult. No cycle_runner
    call — we never started a real cycle.
    """
    cycle_id = next_cycle_id(cycle_log)
    notes = f"autonomous_loop gate-skip — {reason}"
    row = format_cycle_log_row(
        cycle_id=cycle_id,
        problem=problem.display,
        start_score=problem.score_current if problem.score_current is not None else "none",
        end_score=problem.score_current if problem.score_current is not None else "none",
        hours=0.0,
        compute="none-gate-skipped",
        wiki_citations=0,
        findings_added=0,
        concepts_added=0,
        author_mix={"agent": 0, "human": 0, "hybrid": 0},
        outcome="gate-skipped",
        notes=notes,
    )
    append_cycle_log_row(cycle_log, row)
    return CycleResult(
        cycle_id=cycle_id,
        problem=problem,
        outcome="gate-skipped",
        notes=notes,
    )


def run_one_visit(
    problem: Problem,
    *,
    cycle_log: Path = DEFAULT_CYCLE_LOG,
    dry_run: bool = False,
    cycle_runner: CycleRunner | None = None,
    max_attempts: int = DEFAULT_MAX_ATTEMPTS_PER_VISIT,
    budget_path: Path = DEFAULT_BUDGET_PATH,
    sentinel_path: Path = DEFAULT_SENTINEL_PATH,
    skip_gates: bool = False,
    llm_enabled: bool | None = None,
) -> list[CycleResult]:
    """Run up to `max_attempts` cycles on `problem` with convergence-detect.

    The visit is the natural unit of work for the autonomous loop: one
    problem, up to 3 attempts, each with its own cycle-log row. Between
    attempts:

      - The avoid-set grows with the prior attempt's chosen techniques so
        the strategy picker doesn't repeat itself.
      - convergence_detect() decides whether to keep going. Stops early when
        score didn't improve AND no new gap was surfaced (the LLM is wired
        in 7.7; until then `new_gap_counts` are all zero and the rule
        effectively stops after the second no-progress attempt).

    Goal 7.5 — gates: `inner_agent_gates.precheck()` runs once at visit
    start. Sentinel / budget / network / thermal failures → write one
    `gate-skipped` cycle-log row + return immediately. Kill switch is
    not a skip — it flips `llm_enabled=False` and the visit proceeds
    with the mechanical path. `skip_gates=True` bypasses the precheck
    entirely (used by tests and by callers that have already gated
    upstream).

    Returns the list of CycleResult, one per cycle actually run
    (or one `gate-skipped` row on skip).
    """
    # Gate precheck. Tests can opt out; the real loop always opts in.
    # `llm_enabled=None` (default) means "infer from precheck or default
    # False if no precheck". An explicit True/False overrides.
    if not skip_gates and inner_agent_gates is not None and not dry_run:
        decision = inner_agent_gates.precheck(
            budget_path=budget_path,
            sentinel_path=sentinel_path,
        )
        log.info(
            "gate precheck: %s — %s (llm_enabled=%s)",
            decision.action,
            decision.reason,
            decision.llm_enabled,
        )
        if decision.action == "skip":
            return [
                _write_gate_skip_row(
                    problem=problem,
                    cycle_log=cycle_log,
                    reason=decision.reason,
                )
            ]
        if llm_enabled is None:
            llm_enabled = decision.llm_enabled
    if llm_enabled is None:
        # No precheck ran (skip_gates / dry_run) and caller didn't say —
        # default to mechanical so tests stay quiet (no real claude -p).
        llm_enabled = False

    # strategy_picker may be None (importable-failure path); fall back to a
    # 1-attempt run since convergence-detect needs it.
    if strategy_picker is None:
        log.warning("strategy_picker unavailable — visit collapses to 1 cycle")
        cr, _ = _run_one_cycle(
            problem,
            cycle_log=cycle_log,
            dry_run=dry_run,
            cycle_runner=cycle_runner,
            attempt_index=1,
            llm_enabled=llm_enabled,
        )
        return [cr]

    results: list[CycleResult] = []
    score_history: list[float] = []
    new_gap_counts: list[int] = []
    avoid_techniques: set[str] = set()

    for i in range(1, max_attempts + 1):
        cr, attempt = _run_one_cycle(
            problem,
            cycle_log=cycle_log,
            dry_run=dry_run,
            cycle_runner=cycle_runner,
            attempt_index=i,
            avoid_techniques=avoid_techniques if avoid_techniques else None,
            llm_enabled=llm_enabled,
        )
        results.append(cr)

        # Update avoid set so attempt i+1 doesn't repeat this attempt's picks
        for t in attempt.get("chosen_techniques", []):
            avoid_techniques.add(t)

        # Build score_history for convergence-detect. If end_score isn't
        # numeric (no manifest entry → "none"), reuse the prior score so
        # convergence reads as "no progress" and stops on the second such
        # cycle. This is the right behavior for the mechanical path; the
        # LLM-wired path (7.5+) will populate actual scores.
        end = attempt["end_score"]
        if isinstance(end, (int, float)):
            score_history.append(float(end))
        elif score_history:
            score_history.append(score_history[-1])
        else:
            score_history.append(0.0)

        # new_gap_counts: 0 until the LLM is wired (7.5). Placeholder so the
        # convergence-detect signature stays stable.
        new_gap_counts.append(0)

        decision = strategy_picker.convergence_detect(
            score_history=score_history,
            new_gap_counts=new_gap_counts,
            max_attempts=max_attempts,
        )
        log.info("visit convergence: %s — %s", decision.action, decision.reason)
        if decision.action == "stop":
            break

    return results


# ---------------- concurrency lock ----------------


class _LockHeld(RuntimeError):
    """Raised when the lockfile already exists (another loop is running)."""


def _acquire_lock(lockfile: Path) -> int:
    """Acquire an exclusive lock by creating `lockfile` with O_CREAT|O_EXCL.

    Returns the file descriptor (caller is responsible for releasing). On
    contention, raises _LockHeld with the holding pid + age.
    """
    try:
        fd = os.open(lockfile, os.O_CREAT | os.O_EXCL | os.O_WRONLY, 0o644)
    except FileExistsError:
        try:
            stale = lockfile.read_text().strip()
        except OSError:
            stale = "(unknown)"
        try:
            age = time.time() - lockfile.stat().st_mtime
            age_str = f"{age:.0f}s old"
        except OSError:
            age_str = "(age unknown)"
        raise _LockHeld(
            f"another autonomous_loop is running (lockfile {lockfile} "
            f"held by {stale}, {age_str}). Remove the lockfile if stale."
        )
    os.write(fd, f"pid={os.getpid()} started={dt.datetime.now().isoformat()}\n".encode())
    return fd


def _release_lock(fd: int, lockfile: Path) -> None:
    try:
        os.close(fd)
    except OSError:
        pass
    try:
        lockfile.unlink()
    except FileNotFoundError:
        pass


# ---------------- recency skip ----------------


def _has_recent_cycle(cycle_log: Path, *, minutes: int) -> bool:
    """Return True iff the cycle-log was modified within the last `minutes`.

    Used for cron/loop safety: skip running if a cycle landed very recently.
    """
    if not cycle_log.is_file():
        return False
    age_sec = time.time() - cycle_log.stat().st_mtime
    return age_sec < minutes * 60


def run_queue(
    *,
    problems_dir: Path = DEFAULT_PROBLEMS_DIR,
    cycle_log: Path = DEFAULT_CYCLE_LOG,
    max_problems: int = 1,
    max_attempts_per_visit: int = DEFAULT_MAX_ATTEMPTS_PER_VISIT,
    dry_run: bool = False,
    cycle_runner: CycleRunner | None = None,
    budget_path: Path = DEFAULT_BUDGET_PATH,
    sentinel_path: Path = DEFAULT_SENTINEL_PATH,
    skip_gates: bool = False,
    llm_enabled: bool | None = None,
) -> list[CycleResult]:
    """Walk the queue: one visit (up to N cycles) per distinct problem.

    `max_problems` caps the number of problems visited this invocation.
    `max_attempts_per_visit` caps the cycles per visit (Goal 7.4). Set to
    1 to recover the pre-7.4 one-cycle-per-problem behavior.

    Tracks already-visited problem ids so each iteration picks the next
    un-visited problem.

    Returns the flat list of CycleResult across all visits (so callers can
    inspect every cycle, not just the final one of each visit).
    """
    results: list[CycleResult] = []
    done_ids: set[int] = set()
    for i in range(max_problems):
        problems = load_problems(problems_dir)
        queue = [p for p in build_queue(problems) if p.problem_id not in done_ids]
        if not queue:
            log.info("queue exhausted after %d visits", i)
            break
        problem = queue[0]
        log.info("visit %d/%d → %s", i + 1, max_problems, problem.display)
        visit_results = run_one_visit(
            problem,
            cycle_log=cycle_log,
            dry_run=dry_run,
            cycle_runner=cycle_runner,
            max_attempts=max_attempts_per_visit,
            budget_path=budget_path,
            sentinel_path=sentinel_path,
            skip_gates=skip_gates,
            llm_enabled=llm_enabled,
        )
        results.extend(visit_results)
        done_ids.add(problem.problem_id)
    return results


# ---------------- CLI ----------------


def main(argv: list[str] | None = None) -> int:
    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")
    parser = argparse.ArgumentParser(description=__doc__.split("\n", 1)[0])
    parser.add_argument("--problems-dir", type=Path, default=DEFAULT_PROBLEMS_DIR)
    parser.add_argument("--cycle-log", type=Path, default=DEFAULT_CYCLE_LOG)
    parser.add_argument(
        "--one-problem",
        action="store_true",
        help="Run a single cycle on the top-priority active problem.",
    )
    parser.add_argument(
        "--max-problems",
        type=int,
        default=1,
        help="Maximum problem-visits to run in one invocation "
        "(default 1). Each visit is up to "
        "--max-attempts-per-visit cycles.",
    )
    parser.add_argument(
        "--max-attempts-per-visit",
        type=int,
        default=DEFAULT_MAX_ATTEMPTS_PER_VISIT,
        help=f"Cap on cycles per visit (default "
        f"{DEFAULT_MAX_ATTEMPTS_PER_VISIT}). Set to 1 "
        f"to recover pre-7.4 one-cycle-per-problem "
        f"behavior. Convergence-detect may stop the "
        f"visit earlier when score progress and gap "
        f"surfacing both flatten.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print plan only; do not append cycle-log or call cycle_runner.",
    )
    parser.add_argument(
        "--queue-only", action="store_true", help="Print the current active queue and exit."
    )
    parser.add_argument(
        "--skip-if-recent",
        type=int,
        default=0,
        metavar="MINUTES",
        help="Skip the run (exit 0) if cycle-log was modified within "
        "MINUTES. Useful under cron / loop to avoid clobbering "
        "an in-flight cycle.",
    )
    parser.add_argument(
        "--discipline-once",
        action="store_true",
        help="For multi-cycle sweeps: skip per-cycle "
        "cycle_runner.sh (refresh_qmd, wiki_graph, "
        "gap_search, wiki_lint) and run it once at the "
        "end with the last cycle's info. Saves ~5min/"
        "cycle on full-queue sweeps where the wiki "
        "doesn't change between cycles.",
    )
    parser.add_argument(
        "--no-lock",
        action="store_true",
        help="Skip the concurrency lockfile (use for explicit " "manual concurrent runs).",
    )
    parser.add_argument(
        "--lockfile", type=Path, default=DEFAULT_LOCKFILE, help="Path to the concurrency lockfile."
    )
    parser.add_argument(
        "--budget-path",
        type=Path,
        default=DEFAULT_BUDGET_PATH,
        help="Path to mb/logs/inner-agent-budget.md — daily token "
        "ledger consumed by the gate precheck (Goal 7.5).",
    )
    parser.add_argument(
        "--sentinel-path",
        type=Path,
        default=DEFAULT_SENTINEL_PATH,
        help="Path to mb/.inner-agent-disabled — regression-"
        "detect sentinel (Goal 7.8). Presence skips the "
        "visit entirely until a human removes the file.",
    )
    parser.add_argument(
        "--skip-gates",
        action="store_true",
        help="Bypass the gate precheck (sentinel / budget / "
        "reach / thermal). Equivalent to running with "
        "EINSTEIN_INNER_AGENT=0 + no sentinel + no "
        "network — used for tests and forced runs.",
    )
    args = parser.parse_args(argv)

    if args.queue_only:
        problems = load_problems(args.problems_dir)
        queue = build_queue(problems)
        log.info("active queue (%d problems):", len(queue))
        for p in queue:
            score = f"{p.score_current:.6g}" if p.score_current is not None else "—"
            print(
                f"  tier={p.tier}  id={p.problem_id:>2}  "
                f"score={score:>14}  status={p.status:<30}  {p.slug}"
            )
        return 0

    # cron/loop safety: skip if a cycle just landed
    if args.skip_if_recent > 0 and _has_recent_cycle(args.cycle_log, minutes=args.skip_if_recent):
        log.info(
            "cycle-log mtime within %d min — skipping run (cron/loop safety)", args.skip_if_recent
        )
        return 0

    # concurrency lock
    fd: int | None = None
    if not args.no_lock and not args.dry_run:
        try:
            fd = _acquire_lock(args.lockfile)
        except _LockHeld as e:
            log.error("%s", e)
            return 75  # EX_TEMPFAIL — cron will retry next interval

    try:
        max_problems = 1 if args.one_problem else args.max_problems
        inner_runner: CycleRunner | None = None
        if args.discipline_once and max_problems > 1:

            def inner_runner(_cid: int, _slug: str) -> int:  # no-op for per-cycle
                return 0

        results = run_queue(
            problems_dir=args.problems_dir,
            cycle_log=args.cycle_log,
            max_problems=max_problems,
            max_attempts_per_visit=args.max_attempts_per_visit,
            dry_run=args.dry_run,
            cycle_runner=inner_runner,
            budget_path=args.budget_path,
            sentinel_path=args.sentinel_path,
            skip_gates=args.skip_gates,
        )
        log.info("completed %d cycles", len(results))
        if args.discipline_once and results and not args.dry_run:
            last = results[-1]
            log.info(
                "--discipline-once: running cycle_runner once at end " "(cycle %d, %s)",
                last.cycle_id,
                last.problem.file_slug,
            )
            rc = _shell_cycle_runner(last.cycle_id, last.problem.file_slug)
            if rc != 0:
                log.warning("end-of-sweep cycle_runner exited %d", rc)
        return 0
    finally:
        if fd is not None:
            _release_lock(fd, args.lockfile)


if __name__ == "__main__":
    raise SystemExit(main())
