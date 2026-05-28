"""meta_loop.propose — agentic proposer (Goal 2).

Reads the diagnostic report + raw filesystem (cycle-log, findings, dead-ends),
invokes an LLM proposer with filesystem-tool access, parses typed proposals
back, writes them to `mb/proposals/pending/`.

Per `docs/wiki/findings/meta-loop-design-from-literature.md`:
- Filesystem-as-feedback (Meta-Harness): raw rows + raw markdown beat
  summaries. The proposer reads the diagnostic AS WELL AS the raw files;
  the report is a launchpad, not a substitute.
- Change-manifest pattern (AHE): every proposal carries evidence_cycles,
  expected_metric_delta, predicted_regressions.

The LLM call (`_default_proposer`) shells out via `docs/tools/claude_headless`.
For tests, callers can inject any `Callable[[ProposerInput], list[dict]]` —
useful when we don't want to spend tokens validating control flow.

Excluded proposal types (deliberate — see Goal 2 in the branch file):

  - `code_edit`        deferred to Goal 5 (needs shadow A/B before promote)
  - `meta_self_edit`   deferred to `js/feat/recursive-meta` (recursive case)
"""

from __future__ import annotations

import datetime as dt
import functools
import json
import logging
import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Callable

from . import diagnose, proposals
from .proposals import (
    Confidence,
    Proposal,
    ProposalStore,
    ProposalType,
    ProposalValidationError,
    make_proposal_id,
)

log = logging.getLogger("meta_loop.propose")

# Provenance tag for proposals emitted by the default LLM proposer below.
# Free-text by convention (`<approach>-<variant>`) — a non-LLM proposer
# (e.g. a Thompson bandit) sets its own. See the swap-surface finding.
DEFAULT_PROPOSER_ID = "metaharness-llm-v1"

# The proposer's system prompt lives in a file, not in code, so it can be
# A/B-tested and shadow-compared without a code edit. `run(prompt_path=...)`
# overrides it; the default is the v1 metaharness prompt. cb root = parents[3].
_REPO = Path(__file__).resolve().parents[3]
DEFAULT_PROMPT_PATH = _REPO / "docs" / "agent" / "proposer_prompts" / "metaharness-v1.md"


# ---------------- proposer-input contract ----------------


@dataclass
class ProposerInput:
    """All the context handed to the proposer LLM call."""

    report_text: str
    cycle_log_path: Path
    skill_library_path: Path
    findings_dir: Path
    questions_dir: Path
    mb_logs_dir: Path
    allowed_types: list[str] = field(default_factory=lambda: sorted(proposals.VALID_PROPOSAL_TYPES))
    prompt_path: Path = DEFAULT_PROMPT_PATH  # system-prompt file the proposer renders


@dataclass
class ProposerOutput:
    """Result of one propose() invocation."""

    written: list[Path] = field(default_factory=list)
    rejected_raw: list[dict] = field(default_factory=list)  # malformed candidates
    proposer_error: str | None = None  # populated if the LLM call failed outright


# ---------------- the default LLM-backed proposer ----------------


@functools.lru_cache(maxsize=8)
def _load_system_prompt(prompt_path: Path) -> str:
    """Read the proposer system prompt from a file (cached per path).

    Externalized from code so prompts can be A/B-tested + shadow-compared
    without a code edit. The dynamic suffix (filesystem roots) stays in
    `_render_prompt`; this is only the static system-prompt body.
    """
    return Path(prompt_path).read_text()


def _default_proposer(inp: ProposerInput) -> list[dict]:
    """Shell out via `claude_headless` and parse the JSON array out.

    Import is lazy so unit tests that inject a stub proposer don't pay the
    import cost (and don't need claude_headless on path).
    """
    import importlib.util as _ilu
    import sys as _sys

    # docs/tools/claude_headless.py is the canonical wrapper. Add its dir
    # to sys.path on first use (the script-style layout means it's not on
    # the Python package path).
    tools_dir = Path(inp.cycle_log_path).resolve().parents[1] / "tools"
    if str(tools_dir) not in _sys.path:
        _sys.path.insert(0, str(tools_dir))

    spec = _ilu.find_spec("claude_headless")
    if spec is None:
        raise RuntimeError(
            f"claude_headless not importable from {tools_dir} — "
            "scripts/meta_loop.py propose requires docs/tools/claude_headless.py"
        )
    claude_headless = _ilu.module_from_spec(spec)
    spec.loader.exec_module(claude_headless)

    prompt = _render_prompt(inp)
    result = claude_headless.run(
        prompt=prompt,
        allowed_tools=["Read", "Grep", "Glob"],
        output_format="text",
        timeout_seconds=600,
        add_dirs=[
            inp.cycle_log_path.parent.parent,  # docs/
            inp.mb_logs_dir.parent,  # mb/
        ],
    )
    if not result.ok:
        raise RuntimeError(
            f"proposer LLM call failed: kind={result.error_kind} message={result.error_message!r}"
        )
    return _extract_json_array(result.stdout)


def _render_prompt(inp: ProposerInput) -> str:
    return (
        _load_system_prompt(inp.prompt_path).rstrip()
        + "\n\n--- DIAGNOSTIC REPORT ---\n"
        + inp.report_text
        + "\n\n--- FILESYSTEM ROOTS YOU MAY READ ---\n"
        + f"cycle_log: {inp.cycle_log_path}\n"
        + f"skill_library: {inp.skill_library_path}\n"
        + f"findings_dir: {inp.findings_dir}\n"
        + f"questions_dir: {inp.questions_dir}\n"
        + f"mb_logs_dir: {inp.mb_logs_dir}\n"
        + "\nUse Read/Grep/Glob to inspect raw rows + raw findings before "
        + "emitting proposals.\n"
    )


# Matches a ```json … ``` fence with optional surrounding whitespace.
_JSON_FENCE_RE = re.compile(r"```json\s*\n(.*?)\n```", re.DOTALL)


def _extract_json_array(text: str) -> list[dict]:
    """Pull the first JSON array out of a fenced code block.

    Robust to the LLM emitting prose around the JSON. Returns [] if no fence
    found OR if the parsed value isn't a list of dicts.
    """
    if not text:
        return []
    m = _JSON_FENCE_RE.search(text)
    raw = m.group(1) if m else text
    # Try the fenced block first, then fall back to the entire stdout (some
    # models drop the fence when asked to be terse).
    for candidate in [raw, text]:
        try:
            data = json.loads(candidate)
        except json.JSONDecodeError:
            continue
        if isinstance(data, list) and all(isinstance(d, dict) for d in data):
            return data
    return []


# ---------------- harness — wire diagnose → proposer → store ----------------


_DEFAULT_REGRESSIONS_PER_TYPE: dict[str, list[str]] = {
    # When the proposer forgets `predicted_regressions`, the harness backfills
    # a minimal placeholder so the proposal validates. The audit log shows
    # `predicted_regressions: ["(none stated)"]` so the reader sees it was
    # asserted (with no specifics) — not silently absent.
    ProposalType.RULE_EDIT.value: ["(none stated)"],
    ProposalType.MANIFEST_TWEAK.value: ["(none stated)"],
    ProposalType.QUEUE_REORDER.value: ["(none stated)"],
    ProposalType.NEW_QUESTION.value: ["(none stated — read-only artifact)"],
}


def _requires_shadow_default(proposal_type: str) -> bool:
    """Default per-type shadow-required flag. Proposer can override."""
    # `new_question` is purely additive markdown — cannot regress the loop.
    # `rule_edit` / `manifest_tweak` / `queue_reorder` can shift behavior;
    # default to TRUE and let the proposer downgrade with justification.
    return proposal_type != ProposalType.NEW_QUESTION.value


def _coerce_raw(raw: dict, *, now: dt.datetime) -> Proposal:
    """Build a Proposal from raw LLM-emitted dict. Raises on schema violation."""
    ptype = raw.get("type", "")
    target = raw.get("target_path", "")
    proposed_diff = raw.get("proposed_diff", "")
    evidence = list(raw.get("evidence_cycles", []) or [])
    delta = {str(k): float(v) for k, v in (raw.get("expected_metric_delta") or {}).items()}
    regressions = list(raw.get("predicted_regressions") or [])
    if not regressions:
        regressions = list(_DEFAULT_REGRESSIONS_PER_TYPE.get(ptype, ["(none stated)"]))
    confidence = raw.get("confidence", Confidence.LOW.value)
    requires_shadow = raw.get(
        "requires_shadow",
        _requires_shadow_default(ptype),
    )
    rationale = raw.get("rationale", "")
    # Provenance: this path is the default LLM proposer. A raw dict may carry
    # an explicit proposer_id (e.g. a future non-LLM proposer reusing _coerce_raw);
    # otherwise tag it as the metaharness LLM proposer. See the swap-surface finding.
    proposer_id = raw.get("proposer_id") or DEFAULT_PROPOSER_ID

    pid = make_proposal_id(proposal_type=ptype, target_path=target, now=now)
    return Proposal(
        id=pid,
        type=ptype,
        target_path=target,
        proposed_diff=proposed_diff,
        evidence_cycles=evidence,
        expected_metric_delta=delta,
        predicted_regressions=regressions,
        confidence=confidence,
        requires_shadow=bool(requires_shadow),
        rationale=rationale,
        proposer_id=proposer_id,
        created_at=now,
    )


def run(
    *,
    cycle_log: Path,
    skill_library: Path,
    findings_dir: Path,
    questions_dir: Path,
    mb_logs_dir: Path,
    proposals_root: Path,
    output: Path,
    proposer: Callable[[ProposerInput], list[dict]] | None = None,
    prompt_path: Path | None = None,
    now: dt.datetime | None = None,
) -> ProposerOutput:
    """Generate a fresh diagnostic, invoke the proposer, write valid proposals.

    Args:
        proposer: injectable for tests; defaults to `_default_proposer` which
            shells out to `claude -p`. The injected callable receives a
            `ProposerInput` and returns a list of raw dict candidates.
        prompt_path: system-prompt file the default proposer renders;
            defaults to DEFAULT_PROMPT_PATH (the v1 metaharness prompt).
            Override to A/B a prompt variant without a code edit.

    Returns:
        ProposerOutput — written paths + rejected-raw candidates + error.
    """
    now = now or dt.datetime.now(dt.timezone.utc)
    proposer = proposer or _default_proposer
    prompt_path = prompt_path or DEFAULT_PROMPT_PATH

    report = diagnose.run(
        cycle_log=cycle_log,
        skill_library=skill_library,
        findings_dir=findings_dir,
        questions_dir=questions_dir,
        output=output,
        now=now,
    )
    inp = ProposerInput(
        report_text=report.render(),
        cycle_log_path=cycle_log,
        skill_library_path=skill_library,
        findings_dir=findings_dir,
        questions_dir=questions_dir,
        mb_logs_dir=mb_logs_dir,
        prompt_path=prompt_path,
    )
    try:
        raw_proposals = proposer(inp)
    except Exception as e:  # broad — we want the harness to be honest about failure
        log.warning("proposer failed: %s", e)
        return ProposerOutput(proposer_error=str(e))

    store = ProposalStore(proposals_root)
    out = ProposerOutput()
    for raw in raw_proposals:
        try:
            proposal = _coerce_raw(raw, now=now)
        except (ProposalValidationError, KeyError, ValueError, TypeError) as e:
            log.info("rejected raw proposal: %s; raw=%r", e, raw)
            out.rejected_raw.append({"raw": raw, "error": str(e)})
            continue
        try:
            path = store.write_pending(proposal)
        except FileExistsError as e:
            log.warning("id collision on %s — skipping (cause: %s)", proposal.id, e)
            out.rejected_raw.append({"raw": raw, "error": str(e)})
            continue
        out.written.append(path)

    return out


__all__ = [
    "ProposerInput",
    "ProposerOutput",
    "run",
]
