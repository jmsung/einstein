#!/usr/bin/env python3
"""inner_agent_output.py — schema + validator for the inner-agent JSON reply.

Goal 7.3 of `mb/active/feat-autonomous-loop.md`. The agent (running inside
`claude -p` per cycle) emits one JSON object matching `OUTPUT_SCHEMA`.
This module is the contract: prompt embeds the schema string, parser
enforces it before the orchestrator threads the result into cycle-log /
auto_submit.

Schema:

    {
      "strategy": "<one-line name>",
      "score": <float | null>,
      "payload": <object | null>,
      "dead_end_finding": <"knowledge/wiki/findings/dead-end-..." | null>,
      "new_questions": [<paths under knowledge/wiki/questions/>],
      "wiki_writes": [<paths under knowledge/wiki/ or mb/>],
      "converged": <bool>,
      "notes": "<<= 200 chars, single line>"
    }

Validation rules (each field surfaces a precise error on failure):

  - `strategy`         non-empty string
  - `score`            real number (int → coerced to float) or null;
                       bool is rejected (Python's isinstance(True, int) trap)
  - `payload`          dict or null
  - `dead_end_finding` null OR path starting with `knowledge/wiki/findings/dead-end-`
  - `new_questions`    list of strings, each starting with `knowledge/wiki/questions/`
  - `wiki_writes`      list of strings, each starting with `knowledge/wiki/` or `mb/`
  - `converged`        strict bool (not 0/1)
  - `notes`            single-line string, ≤ 200 chars

Tolerance: leading/trailing whitespace, ```json fences, and trailing text
after the JSON object are all stripped silently. The prompt instructs the
agent to emit JSON only, but real responses occasionally include a
trailing comment.
"""

from __future__ import annotations

import json
import logging
import re
from dataclasses import dataclass, field
from typing import Any

log = logging.getLogger("inner_agent_output")

# ---------------- constants ----------------

MAX_NOTES_CHARS = 200
DEAD_END_PREFIX = "knowledge/wiki/findings/dead-end-"
QUESTIONS_PREFIX = "knowledge/wiki/questions/"
WIKI_OR_MB_PREFIXES = ("knowledge/wiki/", "mb/")
SOURCE_PREFIX = "knowledge/source/"

OUTPUT_SCHEMA = """{
  "strategy": "<one-line name of the approach tried this cycle>",
  "score": <float | null>,
  "payload": <object | null — solution payload for auto_submit, per-problem shape>,
  "dead_end_finding": <"knowledge/wiki/findings/dead-end-..." | null>,
  "new_questions": [<paths under knowledge/wiki/questions/ written this cycle>],
  "wiki_writes": [<all paths written under knowledge/wiki/ or mb/ this cycle>],
  "cited_sources": [<paths under knowledge/source/ that informed this attempt; empty list is OK>],
  "converged": <bool — true if no plausible next step remains>,
  "notes": "<<= 200 chars, single line, for cycle-log notes column>"
}"""


# ---------------- types ----------------


class InnerAgentOutputError(ValueError):
    """Raised when the agent's response can't be parsed or fails validation."""


@dataclass
class InnerAgentResponse:
    strategy: str
    score: float | None
    payload: dict | None
    dead_end_finding: str | None
    new_questions: list[str]
    wiki_writes: list[str]
    converged: bool
    notes: str
    # Goal 4 of js/feat/research-synthesis. Optional in the agent reply
    # (default empty for backwards-compat with pre-G4 responses); each
    # entry must start with knowledge/source/.
    cited_sources: list[str] = field(default_factory=list)


# ---------------- fence stripping + JSON extraction ----------------


_FENCE_RE = re.compile(r"^```(?:json|JSON)?\s*\n(.*?)\n```\s*$", re.DOTALL)


def _strip_fences(text: str) -> str:
    """If wrapped in ```json\n...\n```, return the inside; else return as-is."""
    text = text.strip()
    m = _FENCE_RE.match(text)
    return m.group(1).strip() if m else text


def _extract_first_json_value(text: str) -> Any:
    """Find + parse the first JSON value (object or array) in `text`.

    Tolerates trailing text after the value (raw_decode returns the end
    offset; we discard it). Raises InnerAgentOutputError if there's no
    JSON in the response or the value is malformed. We accept arrays here
    too so `validate()` can produce a meaningful "expected object, got list"
    error if the agent wraps its response in an array.
    """
    candidates = [i for i in (text.find("{"), text.find("[")) if i != -1]
    if not candidates:
        raise InnerAgentOutputError("no JSON object found in response")
    idx = min(candidates)
    decoder = json.JSONDecoder()
    try:
        obj, _end = decoder.raw_decode(text, idx=idx)
    except json.JSONDecodeError as e:
        raise InnerAgentOutputError(f"JSON parse error at offset {e.pos}: {e.msg}") from e
    return obj


# ---------------- per-field validators ----------------


def _require_key(d: dict, k: str) -> Any:
    if k not in d:
        raise InnerAgentOutputError(f"missing required field: {k!r}")
    return d[k]


def _check_strategy(v: Any) -> str:
    if not isinstance(v, str):
        raise InnerAgentOutputError(f"field 'strategy': expected string, got {type(v).__name__}")
    if not v.strip():
        raise InnerAgentOutputError("field 'strategy': must be non-empty")
    return v


def _check_score(v: Any) -> float | None:
    # Reject bool first — Python's isinstance(True, int) → True is a footgun
    # for "looks like a number" checks.
    if isinstance(v, bool):
        raise InnerAgentOutputError(
            "field 'score': bool is not a valid number (expected float | null)"
        )
    if v is None:
        return None
    if not isinstance(v, (int, float)):
        raise InnerAgentOutputError(
            f"field 'score': expected number | null, got {type(v).__name__}"
        )
    return float(v)


def _check_payload(v: Any) -> dict | None:
    if v is None:
        return None
    if not isinstance(v, dict):
        raise InnerAgentOutputError(
            f"field 'payload': expected object | null, got {type(v).__name__}"
        )
    return v


def _check_dead_end_finding(v: Any) -> str | None:
    if v is None:
        return None
    if not isinstance(v, str):
        raise InnerAgentOutputError(
            f"field 'dead_end_finding': expected string | null, got {type(v).__name__}"
        )
    if not v.startswith(DEAD_END_PREFIX):
        raise InnerAgentOutputError(
            f"field 'dead_end_finding': must start with {DEAD_END_PREFIX!r}, got {v!r}"
        )
    return v


def _check_path_list(v: Any, field_name: str, prefixes: tuple[str, ...]) -> list[str]:
    if not isinstance(v, list):
        raise InnerAgentOutputError(f"field {field_name!r}: expected list, got {type(v).__name__}")
    out: list[str] = []
    for i, item in enumerate(v):
        if not isinstance(item, str):
            raise InnerAgentOutputError(
                f"{field_name}[{i}]: expected string, got {type(item).__name__}"
            )
        if not item.startswith(prefixes):
            joined = " | ".join(repr(p) for p in prefixes)
            raise InnerAgentOutputError(
                f"{field_name}[{i}]: must start with {joined}, got {item!r}"
            )
        out.append(item)
    return out


def _filter_path_list(v: Any, field_name: str, prefixes: tuple[str, ...]) -> list[str]:
    """Lenient variant of `_check_path_list` for OPTIONAL informational fields.

    A non-list is still a hard error (the field is structurally malformed),
    but individual entries that aren't strings or don't match `prefixes` are
    *dropped with a warning* rather than rejected. Used for `cited_sources`:
    the agent frequently cites a findings/concepts page it actually read, but
    that field feeds the knowledge/source/-only promotion detector, so the right
    behavior is to keep the valid source/ paths and discard the rest — NOT to
    fail the whole (otherwise valid) cycle and force a mechanical fallback.

    Phase 2 Goal 1 reliability fix: pilot cycles fell back precisely because a
    single `knowledge/wiki/findings/...` entry in `cited_sources` raised here. See
    `knowledge/wiki/findings/inner-agent-cited-sources-parse-fallback.md`.
    """
    if not isinstance(v, list):
        raise InnerAgentOutputError(f"field {field_name!r}: expected list, got {type(v).__name__}")
    out: list[str] = []
    for item in v:
        if isinstance(item, str) and item.startswith(prefixes):
            out.append(item)
        else:
            log.warning(
                "field %r: dropping non-conforming entry %r (must start with %s)",
                field_name,
                item,
                " | ".join(prefixes),
            )
    return out


def _check_converged(v: Any) -> bool:
    # Strict bool — reject 0/1/etc to avoid silently treating int as truthy.
    if type(v) is not bool:
        raise InnerAgentOutputError(f"field 'converged': expected bool, got {type(v).__name__}")
    return v


def _check_notes(v: Any) -> str:
    if not isinstance(v, str):
        raise InnerAgentOutputError(f"field 'notes': expected string, got {type(v).__name__}")
    # Lenient on shape, strict on type — same policy as cited_sources
    # (Phase 2: strict-parse on a cosmetic constraint caused a 40% fallback
    # rate; Goal-5 runs 6-7 reproduced it via 283/294-char notes → mechanical
    # fallback). Newlines flatten to "; ", overlength truncates with a marker.
    # Failing the WHOLE response over a long note costs an LLM cycle for zero
    # informational gain.
    if "\n" in v:
        log.warning("field 'notes': flattening %d newline(s)", v.count("\n"))
        v = "; ".join(part.strip() for part in v.splitlines() if part.strip())
    if len(v) > MAX_NOTES_CHARS:
        log.warning("field 'notes': %d chars > %d max — truncating", len(v), MAX_NOTES_CHARS)
        v = v[: MAX_NOTES_CHARS - 1] + "…"
    return v


# ---------------- top-level API ----------------


def validate(raw: dict) -> InnerAgentResponse:
    """Validate an already-parsed dict against the schema.

    Lets callers reuse the validator independently of the JSON-extraction
    code path (e.g. when claude is invoked with --output-format=json and
    the orchestrator gets a dict instead of a stringified blob).
    """
    if not isinstance(raw, dict):
        raise InnerAgentOutputError(f"top-level value is not an object (got {type(raw).__name__})")
    return InnerAgentResponse(
        strategy=_check_strategy(_require_key(raw, "strategy")),
        score=_check_score(_require_key(raw, "score")),
        payload=_check_payload(_require_key(raw, "payload")),
        # dead_end_finding is the one optional field — absent is OK (→ None).
        dead_end_finding=_check_dead_end_finding(raw.get("dead_end_finding")),
        new_questions=_check_path_list(
            _require_key(raw, "new_questions"),
            "new_questions",
            (QUESTIONS_PREFIX,),
        ),
        wiki_writes=_check_path_list(
            _require_key(raw, "wiki_writes"),
            "wiki_writes",
            WIKI_OR_MB_PREFIXES,
        ),
        # Optional (default []) for backwards compat with pre-G4 agent replies.
        # Lenient: non-knowledge/source/ entries are dropped, not rejected — a stray
        # citation must never force a mechanical fallback (Phase 2 Goal 1).
        cited_sources=_filter_path_list(
            raw.get("cited_sources", []),
            "cited_sources",
            (SOURCE_PREFIX,),
        ),
        converged=_check_converged(_require_key(raw, "converged")),
        notes=_check_notes(_require_key(raw, "notes")),
    )


def append_citation_record(
    jsonl_path,
    *,
    cycle_id: int,
    problem: str,
    cited_sources: list[str],
) -> None:
    """Append one citation record to the sidecar JSONL.

    Goal 4 of js/feat/research-synthesis. The cycle-log row carries only a
    `cites_src` count for human readability; the full per-cycle path list
    lives here so `docs/tools/promotion_candidates.py` can count cross-cycle
    citations and propose source → concept promotions.

    Format: one JSON object per line, fields:
        cycle_id, problem, cited_sources, ts (ISO timestamp).

    Goal 9 of js/feat/research-synthesis: when the env var
    ``EINSTEIN_SHADOW_ARM`` is set (e.g. ``A`` or ``B``), the value is
    recorded in an ``arm`` field. This lets the shadow A/B
    promotion gate read per-arm citation counts from the shared sidecar
    JSONL after `run_shadow(cleanup=True)` has deleted the arm cycle-logs.
    Absent env var → no ``arm`` field (backwards compat with pre-G9 records).

    Creates the parent directory if needed. Thread-safe within a single
    autonomous-loop process (single-writer append).
    """
    import datetime as _dt
    import os as _os
    from pathlib import Path

    p = Path(jsonl_path)
    p.parent.mkdir(parents=True, exist_ok=True)
    record = {
        "cycle_id": int(cycle_id),
        "problem": str(problem),
        "cited_sources": list(cited_sources),
        "ts": _dt.datetime.now(_dt.timezone.utc).isoformat(),
    }
    arm = _os.environ.get("EINSTEIN_SHADOW_ARM")
    if arm:
        record["arm"] = arm
    with p.open("a", encoding="utf-8") as f:
        f.write(json.dumps(record) + "\n")


def parse_response(text: str) -> InnerAgentResponse:
    """Parse + validate a raw agent reply (the text body of claude -p stdout).

    Pipeline:
      1. strip leading/trailing whitespace
      2. unwrap a single ```json ... ``` fence if present
      3. extract the first balanced JSON object (raw_decode tolerates
         trailing text)
      4. validate fields

    Every failure raises InnerAgentOutputError with the specific
    constraint that broke.
    """
    stripped = _strip_fences(text)
    raw = _extract_first_json_value(stripped)
    return validate(raw)
