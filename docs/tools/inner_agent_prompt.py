#!/usr/bin/env python3
"""inner_agent_prompt.py — render the prompt body for one autonomous cycle.

Goal 7.1 of `mb/active/feat-autonomous-loop.md`. Pure string building: this
module owns the contract between the orchestrator (autonomous_loop.py) and
the inner agent (a `claude -p` invocation, wired in 7.2 via
`docs/tools/claude_headless.py`).

A "cycle" is one `claude -p` invocation = one cycle-log row. A "visit" is up
to 3 cycles on the same problem with convergence-detect between them; the
visit concept lives in autonomous_loop, not here.

The rendered prompt encodes the math-solving-protocol as the agent's task:

    1. WIKI-FIRST  — qmd query before any other tool call
    2. COUNCIL     — only when fresh problem (no prior cycles)
    3. GAP DETECT  — wiki_graph for council questions
    4. RESEARCH    — gap_search for arxiv candidates
    5. STRATEGY    — autoresearch 1+1 rule
    6. EXECUTE     — optimizer_dispatch if manifest entry exists
    7. LOG         — emit the JSON response

Inputs are read defensively: missing files render as "(none)" rather than
raising. The prompt itself does not enforce any policy — that's done by
the orchestrator (resource gates) and the headless wrapper (tool
allow-list, output schema validation).

Usage as a CLI (for dogfooding / debugging):

    uv run python docs/tools/inner_agent_prompt.py \
        --problem-id 14 --attempt 1 --cycle-id 99 > /tmp/prompt.md
"""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Sequence

_REPO = Path(__file__).resolve().parents[2]
DEFAULT_PROBLEMS_DIR = _REPO / "docs" / "wiki" / "problems"
DEFAULT_CYCLE_LOG = _REPO / "docs" / "agent" / "cycle-log.md"
DEFAULT_SKILL_LIBRARY = _REPO / "docs" / "agent" / "skill-library.md"
DEFAULT_EXPERIMENT_DIR = _REPO.parent / "mb" / "problems"

# Single source of truth for the schema string — parser + prompt share it.
sys.path.insert(0, str(Path(__file__).resolve().parent))
from inner_agent_output import OUTPUT_SCHEMA  # noqa: E402

_FM_RE = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)


# ---------------- helpers ----------------


@dataclass(frozen=True)
class CycleRow:
    """One parsed row of `cycle-log.md` — 11 cells per the schema header."""

    cycle_id: int
    problem: str
    score_pair: str
    hours: str
    compute: str
    outcome: str
    notes: str

    @classmethod
    def parse(cls, line: str) -> "CycleRow | None":
        if not line.lstrip().startswith("|"):
            return None
        parts = [p.strip() for p in line.split("|")]
        # `| a | b | c |` → ['', 'a', 'b', 'c', '']
        cells = parts[1:-1] if parts[0] == "" and parts[-1] == "" else parts
        if len(cells) < 11:
            return None
        try:
            cid = int(cells[0])
        except ValueError:
            return None
        return cls(
            cycle_id=cid,
            problem=cells[1],
            score_pair=cells[2],
            hours=cells[3],
            compute=cells[4],
            outcome=cells[9],
            notes=cells[10],
        )


def _read_safe(p: Path, default: str = "(none)") -> str:
    try:
        return p.read_text()
    except OSError:
        return default


def _strip_frontmatter(text: str) -> str:
    m = _FM_RE.match(text)
    return text[m.end() :] if m else text


def _tail(s: str, max_lines: int) -> str:
    lines = s.splitlines()
    if len(lines) <= max_lines:
        return s
    return (
        "\n".join(lines[-max_lines:]) + f"\n\n(truncated to last {max_lines} of {len(lines)} lines)"
    )


def _cycle_rows_for(cycle_log: Path, problem_prefix: str, n: int = 10) -> list[CycleRow]:
    text = _read_safe(cycle_log, default="")
    rows: list[CycleRow] = []
    for line in text.splitlines():
        if problem_prefix not in line:
            continue
        row = CycleRow.parse(line)
        if row is not None and row.problem.startswith(problem_prefix):
            rows.append(row)
    return rows[-n:]


# ---------------- prompt sections ----------------


TOOL_ALLOWLIST = """- Read, Grep
- Write                                                — create new wiki/mb files (SCOPED, see below)
- Bash(qmd:*)                                          — wiki search (use FIRST)
- Bash(gap_search.py:*)                                — arxiv candidate search
- Bash(uv run python -m einstein.optimizer_dispatch:*) — run a per-problem optimizer
- Task                                                 — dispatch council subagents (e.g. Tao, Cohn, Razborov)

**Write scope** — restrict to these two trees per `wiki-attribution.md`:
  - `docs/wiki/findings/` — new finding pages (including `dead-end-<slug>.md`)
  - `docs/wiki/questions/` — new gap questions
  - `docs/wiki/concepts/` — only if a concept is genuinely missing (rare)
  - `mb/problems/<id>-<slug>/experiment-log.md` — append per-attempt notes

Every wiki page MUST include the `author: agent` frontmatter field. The
orchestrator's git-status delta (Goal 7.6) captures every file you write
for human review. Whatever you Write, ALSO list in the JSON `wiki_writes`
field so the cycle-log notes column reflects it."""


# ---------------- main render ----------------


def render_prompt(
    *,
    problem_id: int,
    problem_slug: str,
    file_slug: str,
    score_current: float | str | None,
    status: str,
    tier: str,
    category: str,
    cycle_id: int,
    attempt_index: int,
    prior_visit_summaries: Sequence[str] = (),
    cycle_log: Path = DEFAULT_CYCLE_LOG,
    skill_library: Path = DEFAULT_SKILL_LIBRARY,
    problems_dir: Path = DEFAULT_PROBLEMS_DIR,
    experiment_log_dir: Path = DEFAULT_EXPERIMENT_DIR,
    cycle_log_tail_n: int = 10,
    experiment_log_tail_lines: int = 200,
    skill_library_tail_lines: int = 80,
    out_token_cap: int = 50_000,
    wall_clock_min: int = 30,
    pre_cycle_synthesis: str | None = None,
    bandit_recommendation: str | None = None,
) -> str:
    """Render the prompt body for one inner cycle.

    Args:
        problem_id: e.g. 14
        problem_slug: e.g. 'circle-packing-square'
        file_slug: e.g. '14-circle-packing-square' (matches docs/wiki/problems/<file_slug>.md)
        score_current, status, tier: problem state from frontmatter
        category: strategy-picker category (e.g. 'sphere-packing')
        cycle_id: the cycle-log row id this cycle will write
        attempt_index: 1, 2, or 3 — which attempt of the visit this is
        prior_visit_summaries: one short string per prior cycle in *this visit*
            (not the historical cycle-log). Empty on attempt 1.
        cycle_log: path to docs/agent/cycle-log.md
        skill_library: path to docs/agent/skill-library.md
        problems_dir: path to docs/wiki/problems/
        experiment_log_dir: path to mb/problems/ (each problem has its own subdir)
        cycle_log_tail_n: keep this many most-recent rows for this problem
        experiment_log_tail_lines: tail lines from experiment-log.md
        skill_library_tail_lines: tail lines from skill-library.md
        out_token_cap, wall_clock_min: budgets surfaced in the prompt itself

    Returns:
        The prompt body, ready to hand to claude_headless.run(prompt=...).
    """
    problem_label = f"P{problem_id}-{problem_slug}"

    problem_md = problems_dir / f"{file_slug}.md"
    problem_body = _strip_frontmatter(
        _read_safe(problem_md, default="(problem statement not found)")
    ).strip()
    if not problem_body:
        problem_body = "(problem statement not found)"

    prior_rows = _cycle_rows_for(cycle_log, problem_label, n=cycle_log_tail_n)
    if prior_rows:
        prior_table_lines = [
            f"  cycle {r.cycle_id}: {r.score_pair} | {r.outcome} | {r.notes}" for r in prior_rows
        ]
        prior_table = "\n".join(prior_table_lines)
    else:
        prior_table = "  (no prior cycles on this problem)"

    if prior_visit_summaries:
        visit_summary = "\n".join(
            f"  attempt {i + 1}: {s}" for i, s in enumerate(prior_visit_summaries)
        )
    else:
        visit_summary = "  (this is attempt 1 of the visit)"

    skill_lib = _tail(
        _read_safe(skill_library, default="(skill-library missing)"),
        skill_library_tail_lines,
    )

    exp_log_path = experiment_log_dir / file_slug / "experiment-log.md"
    exp_log = _tail(
        _read_safe(exp_log_path, default="(no experiment log yet)"),
        experiment_log_tail_lines,
    )

    score_str = (
        f"{score_current:.14g}"
        if isinstance(score_current, (int, float))
        else (str(score_current) if score_current is not None else "none")
    )

    # Goal 8 of js/feat/research-synthesis: when the orchestrator has produced
    # a pre-cycle literature synthesis (by inspecting cycle-discipline.md for
    # the rule_edit marker), inject it as a leading section so the inner
    # agent reads source-grounded patterns BEFORE deciding strategy.
    if pre_cycle_synthesis and pre_cycle_synthesis.strip():
        synthesis_section = (
            "## Pre-cycle synthesis (auto-generated)\n\n"
            "The orchestrator ran `cb/scripts/research_synthesis.py` before this cycle "
            "because `.claude/rules/cycle-discipline.md` enables the research-synthesis "
            "step. The block below summarizes top-k qmd hits against the wiki + source "
            "collections plus claude's cross-source pattern extraction. **Use the "
            "`cited_sources` array in your JSON output to declare which of these source "
            "paths actually informed your attempt.**\n\n"
            f"{pre_cycle_synthesis.strip()}\n"
        )
    else:
        synthesis_section = ""

    # G2 extension (js/feat/skill-bandit): when EINSTEIN_BANDIT=1, the
    # orchestrator samples the Thompson skill-bandit and threads its
    # recommendation in as a *strong prior* for step 5 (STRATEGY). Treat it
    # like a council vote with quantified evidence — override only with
    # explicit reason. Without this section, the LLM has no signal that the
    # bandit prefers any particular technique for this category.
    if bandit_recommendation and bandit_recommendation.strip():
        bandit_section = (
            "## Bandit recommendation (consider strongly for STRATEGY step)\n\n"
            "The Thompson skill-bandit (`EINSTEIN_BANDIT=1`) sampled its "
            "Beta-Bernoulli posterior over `docs/agent/skill-library.md` and "
            "recommends:\n\n"
            f"  {bandit_recommendation.strip()}\n\n"
            "Treat this as a strong prior for the 1+1 rule's *prior* slot. "
            "Override only if you can name a concrete reason (e.g. the "
            "recommended technique has a known dead-end finding for this "
            "problem). When you override, say why in `notes`.\n"
        )
    else:
        bandit_section = ""

    return f"""# Autonomous cycle — problem {problem_label}

Attempt {attempt_index}/3 in this visit. cycle_id={cycle_id}. category={category}.

{synthesis_section}{bandit_section}## Your task

Run the math-solving-protocol (`.claude/rules/math-solving-protocol.md`) and
emit a single JSON object matching the schema at the end. Concretely:

1. **WIKI-FIRST** — your FIRST tool call must be `qmd query "<concept>" -c einstein-wiki -n 5`
   for at least one in-scope concept. Per `.claude/rules/cycle-discipline.md`
   step 0, refusing this step breaks the self-improvement loop.
2. **COUNCIL** — if no prior cycles exist on this problem, dispatch 3–5
   personas via Task. Each writes a *question*, not a solution. Pick from
   `docs/wiki/personas/`.
3. **GAP DETECT** — for each council question, check coverage; escalate
   real gaps to step 4.
4. **RESEARCH** — `gap_search.py` for arxiv candidates only if a gap is real.
5. **STRATEGY** — pick at most 1 prior approach + at most 1 novel
   (autoresearch 1+1 rule). On attempts 2/3 of this visit, avoid repeating
   the prior cycle's chosen strategy.
6. **EXECUTE** — call `uv run python -m einstein.optimizer_dispatch \\
   --problem-id {problem_id} --strategy <strategy>` if the problem has a
   manifest entry. If no entry, return `"score": null` and explain in `notes`.
7. **LOG** — emit the JSON response. Stop calling tools after emitting it.
   If the attempt failed (dead end), set `dead_end_finding` to the intended
   path under `docs/wiki/findings/dead-end-*.md`; the orchestrator writes
   the file in Goal 7.6.
8. **CITED SOURCES** — populate `cited_sources` with every
   `docs/source/<file>.md` path that materially informed this attempt
   (read in step 1's wiki-first lookup, surfaced by gap_search, or
   referenced in a council question). Empty list is OK if no source/
   page was load-bearing. This field feeds `mb/logs/cited-sources.jsonl`
   and the promotion-candidate detector per Goal 4 of
   `js/feat/research-synthesis`.

## Problem statement

{problem_body}

## Current state

- score_current: {score_str}
- status: {status}
- tier: {tier}

## Prior cycles on this problem (last {cycle_log_tail_n})

{prior_table}

## Prior attempts in this visit

{visit_summary}

## Skill library snapshot (last {skill_library_tail_lines} lines of skill-library.md)

```
{skill_lib}
```

## Experiment log ({exp_log_path.name} — last {experiment_log_tail_lines} lines)

```
{exp_log}
```

## Tools you may use

{TOOL_ALLOWLIST}

## Resource budget

- Output tokens cap: {out_token_cap}
- Wall-clock cap: {wall_clock_min} min (orchestrator enforces via subprocess timeout)
- Network is OK (arxiv + arena pre-checked by the orchestrator).
- Kill switch `EINSTEIN_INNER_AGENT=0` reverts to mechanical path; if you
  see that env var unset assume the autonomous path is active.

## Required output

Emit exactly one JSON object matching this schema, and nothing else after it:

```json
{OUTPUT_SCHEMA}
```
"""


# ---------------- CLI ----------------


def _cli(argv: list[str] | None = None) -> int:
    """Render a prompt to stdout. Reads problem frontmatter to derive defaults.

    Used for dogfooding / debugging the prompt before 7.2 wires it into
    a real `claude -p` call.
    """
    parser = argparse.ArgumentParser(description=__doc__.split("\n", 1)[0])
    parser.add_argument("--problem-id", type=int, required=True)
    parser.add_argument("--cycle-id", type=int, required=True)
    parser.add_argument("--attempt", type=int, default=1, choices=[1, 2, 3])
    parser.add_argument(
        "--category",
        default="?",
        help="Problem category (e.g. sphere-packing). "
        "Default '?' triggers a generic strategy pick.",
    )
    parser.add_argument("--problems-dir", type=Path, default=DEFAULT_PROBLEMS_DIR)
    parser.add_argument("--cycle-log", type=Path, default=DEFAULT_CYCLE_LOG)
    parser.add_argument("--skill-library", type=Path, default=DEFAULT_SKILL_LIBRARY)
    parser.add_argument("--experiment-log-dir", type=Path, default=DEFAULT_EXPERIMENT_DIR)
    args = parser.parse_args(argv)

    # Locate the problem page by problem_id.
    candidate = None
    for path in sorted(args.problems_dir.glob("*.md")):
        if path.name.startswith("_") or path.name == "README.md":
            continue
        fm_match = _FM_RE.match(path.read_text())
        if not fm_match:
            continue
        fm: dict[str, str] = {}
        for line in fm_match.group(1).splitlines():
            kv = re.match(r"^([a-zA-Z_]+):\s*(.*)$", line)
            if kv:
                fm[kv.group(1)] = kv.group(2).strip().strip("\"'")
        if fm.get("problem_id") == str(args.problem_id):
            candidate = (path, fm)
            break

    if candidate is None:
        print(f"error: no problem page found for problem_id={args.problem_id}", file=sys.stderr)
        return 2
    path, fm = candidate
    stem = path.stem  # e.g. '14-circle-packing-square'
    m = re.match(r"^(\d+[a-z]?)-(.+)$", stem)
    slug = m.group(2) if m else stem

    score_raw = fm.get("score_current")
    score: float | str | None = None
    if score_raw:
        try:
            score = float(score_raw)
        except ValueError:
            score = score_raw

    prompt = render_prompt(
        problem_id=args.problem_id,
        problem_slug=slug,
        file_slug=stem,
        score_current=score,
        status=fm.get("status", "unknown"),
        tier=fm.get("tier", "?"),
        category=args.category,
        cycle_id=args.cycle_id,
        attempt_index=args.attempt,
        cycle_log=args.cycle_log,
        skill_library=args.skill_library,
        problems_dir=args.problems_dir,
        experiment_log_dir=args.experiment_log_dir,
    )
    sys.stdout.write(prompt)
    return 0


if __name__ == "__main__":
    raise SystemExit(_cli())
