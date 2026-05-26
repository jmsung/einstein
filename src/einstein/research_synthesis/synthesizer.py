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
    queries: list[str] | None = None,
    drafted_at: str | None = None,
    runner: Runner | None = None,
    model: str = "claude-opus-4-7[1m]",
    timeout_seconds: int = 300,
    max_budget_usd: float | None = None,
) -> LiteratureSynthesis | None:
    """Call claude headless to produce a LiteratureSynthesis.

    Returns ``None`` on any failure path (auth, timeout, schema mismatch).
    Caller decides whether to fall back to a stub or skip the synthesis step.

    Division of labor (G10 take 7 fix): the SCRIPT owns the mechanical fields
    it already has — ``queries``, ``top_sources``, ``top_wiki`` — and they are
    injected into the result directly from the args here. Claude owns ONLY the
    analytical fields (``cross_source_patterns``, ``proposed_approaches``,
    ``gaps_identified``). This removes the entire class of "claude didn't echo
    the hits back" failures (the same root cause as the earlier problem_id
    omission) and shrinks claude's output so it's faster + less timeout-prone.
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
    # Parse claude's JSON for the ANALYTICAL fields only. The mechanical
    # fields (identity + queries + hits) are overwritten from our own args —
    # claude doesn't need to (and reliably won't) echo them back.
    try:
        import json as _json

        # Best-effort extract first JSON object from claude's response.
        text = res.stdout.strip()
        if text.startswith("```"):
            # strip ```json ... ``` fence if present
            text = text.strip("`")
            text = text.removeprefix("json").strip()
            if text.endswith("```"):
                text = text[:-3].strip()
        data = _json.loads(text) if text else {}
        if not isinstance(data, dict):
            raise ValueError(f"top-level JSON is {type(data).__name__}, expected object")
        # Orchestrator-owned identity fields.
        data["problem_id"] = problem_id
        data["problem_slug"] = problem_slug
        data["drafted_at"] = drafted
        # Script-owned mechanical fields — overwrite whatever claude emitted
        # (or didn't) with the real gather() results we already have.
        data["queries"] = list(queries or [])
        data["top_sources"] = [
            {"path": h.path, "score": h.score, "snippet": h.snippet, "collection": h.collection}
            for h in source_hits
        ]
        data["top_wiki"] = [
            {"path": h.path, "score": h.score, "snippet": h.snippet, "collection": h.collection}
            for h in wiki_hits
        ]
        return LiteratureSynthesis.from_dict(data)
    except (ValueError, Exception) as e:  # noqa: BLE001
        log.warning("synthesizer: malformed JSON from claude: %s", e)
        return None
