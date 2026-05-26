"""claude_headless orchestration for the literature synthesis step.

`synthesize()` builds a prompt from the gathered hits, asks Claude to produce
JSON matching `LiteratureSynthesis`'s schema, and returns the parsed result.
On any failure (auth, timeout, malformed JSON) it returns ``None`` so the
caller can fall back.
"""

from __future__ import annotations

import datetime as _dt
import logging
from collections.abc import Callable
from dataclasses import dataclass

from einstein.research_synthesis.schema import JSON_SCHEMA, Hit, LiteratureSynthesis

log = logging.getLogger("research_synthesis.synthesizer")


@dataclass
class _RunnerResult:
    """Subset of claude_headless.HeadlessResult used here."""

    ok: bool
    stdout: str = ""
    stderr: str = ""
    error_kind: str = ""
    error_message: str = ""


Runner = Callable[..., _RunnerResult]


def _default_runner(**kwargs) -> _RunnerResult:
    # Imported lazily so tests don't need claude_headless on the path.
    import sys
    from pathlib import Path

    tools = Path(__file__).resolve().parents[3] / "docs" / "tools"
    if str(tools) not in sys.path:
        sys.path.insert(0, str(tools))
    from claude_headless import run as _run  # type: ignore[import-not-found]

    res = _run(**kwargs)
    return _RunnerResult(
        ok=res.ok,
        stdout=res.stdout,
        stderr=res.stderr,
        error_kind=res.error_kind,
        error_message=res.error_message,
    )


def _build_prompt(
    *,
    problem_id: int,
    problem_slug: str,
    problem_context: str,
    source_hits: list[Hit],
    wiki_hits: list[Hit],
    drafted_at: str,
) -> str:
    """Construct the user prompt fed to `claude -p`."""

    def render_hits(hits: list[Hit], header: str) -> str:
        if not hits:
            return f"{header}: (none)\n"
        lines = [header + ":"]
        for h in hits:
            pct = int(round(h.score * 100))
            lines.append(f"- [{pct}%] {h.path} — {h.snippet}")
        return "\n".join(lines) + "\n"

    return f"""Pre-cycle literature synthesis for Einstein Arena problem P{problem_id} ({problem_slug}).

Today: {drafted_at}.

You are reading top retrieval hits from the einstein wiki + source distillations.
Produce a JSON object matching the LiteratureSynthesis schema. Anchor every
proposed approach in 1+ cited_sources from the lists below. Cross-source
patterns must be backed by 2+ supporting_sources. The cross_source_patterns
should NOT re-derive what `docs/wiki/findings/research-synthesis-design.md`
already covers (patterns A/B/C/D); name *new* patterns specific to this
problem's literature.

Problem context (from mb/problems/{problem_id}-{problem_slug}/strategy.md):
\"\"\"
{problem_context.strip()}
\"\"\"

{render_hits(source_hits, "Top source distillations")}
{render_hits(wiki_hits, "Top wiki synthesis pages")}

Required JSON shape — populate every list with concrete items grounded in the
hits above. Do not invent paths that aren't in the lists.
"""


def synthesize(
    *,
    problem_id: int,
    problem_slug: str,
    problem_context: str,
    source_hits: list[Hit],
    wiki_hits: list[Hit],
    drafted_at: str | None = None,
    runner: Runner | None = None,
    model: str = "claude-opus-4-7[1m]",
    timeout_seconds: int = 300,
    max_budget_usd: float | None = None,
) -> LiteratureSynthesis | None:
    """Call claude headless to produce a LiteratureSynthesis.

    Returns ``None`` on any failure path (auth, timeout, schema mismatch).
    Caller decides whether to fall back to a stub or skip the synthesis step.
    """
    drafted = drafted_at or _dt.date.today().isoformat()
    prompt = _build_prompt(
        problem_id=problem_id,
        problem_slug=problem_slug,
        problem_context=problem_context,
        source_hits=source_hits,
        wiki_hits=wiki_hits,
        drafted_at=drafted,
    )
    runner_fn: Runner = runner or _default_runner
    kwargs: dict = {
        "prompt": prompt,
        "model": model,
        "timeout_seconds": timeout_seconds,
        "output_format": "json",
        "json_schema": JSON_SCHEMA,
    }
    if max_budget_usd is not None:
        kwargs["max_budget_usd"] = max_budget_usd
    res = runner_fn(**kwargs)
    if not res.ok:
        log.warning(
            "synthesizer: claude call failed kind=%s msg=%s",
            res.error_kind,
            res.error_message,
        )
        return None
    try:
        return LiteratureSynthesis.from_json(res.stdout)
    except ValueError as e:
        log.warning("synthesizer: malformed JSON from claude: %s", e)
        return None
