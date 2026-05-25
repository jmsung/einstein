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
      "dead_end_finding": <"docs/wiki/findings/dead-end-..." | null>,
      "new_questions": [<paths under docs/wiki/questions/>],
      "wiki_writes": [<paths under docs/wiki/ or mb/>],
      "converged": <bool>,
      "notes": "<<= 200 chars, single line>"
    }

Validation rules (each field surfaces a precise error on failure):

  - `strategy`         non-empty string
  - `score`            real number (int → coerced to float) or null;
                       bool is rejected (Python's isinstance(True, int) trap)
  - `payload`          dict or null
  - `dead_end_finding` null OR path starting with `docs/wiki/findings/dead-end-`
  - `new_questions`    list of strings, each starting with `docs/wiki/questions/`
  - `wiki_writes`      list of strings, each starting with `docs/wiki/` or `mb/`
  - `converged`        strict bool (not 0/1)
  - `notes`            single-line string, ≤ 200 chars

Tolerance: leading/trailing whitespace, ```json fences, and trailing text
after the JSON object are all stripped silently. The prompt instructs the
agent to emit JSON only, but real responses occasionally include a
trailing comment.
"""

from __future__ import annotations

import json
import re
from dataclasses import dataclass
from typing import Any

# ---------------- constants ----------------

MAX_NOTES_CHARS = 200
DEAD_END_PREFIX = "docs/wiki/findings/dead-end-"
QUESTIONS_PREFIX = "docs/wiki/questions/"
WIKI_OR_MB_PREFIXES = ("docs/wiki/", "mb/")

OUTPUT_SCHEMA = """{
  "strategy": "<one-line name of the approach tried this cycle>",
  "score": <float | null>,
  "payload": <object | null — solution payload for auto_submit, per-problem shape>,
  "dead_end_finding": <"docs/wiki/findings/dead-end-..." | null>,
  "new_questions": [<paths under docs/wiki/questions/ written this cycle>],
  "wiki_writes": [<all paths written under docs/wiki/ or mb/ this cycle>],
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


def _check_converged(v: Any) -> bool:
    # Strict bool — reject 0/1/etc to avoid silently treating int as truthy.
    if type(v) is not bool:
        raise InnerAgentOutputError(f"field 'converged': expected bool, got {type(v).__name__}")
    return v


def _check_notes(v: Any) -> str:
    if not isinstance(v, str):
        raise InnerAgentOutputError(f"field 'notes': expected string, got {type(v).__name__}")
    if "\n" in v:
        raise InnerAgentOutputError("field 'notes': must be single line (no newlines)")
    if len(v) > MAX_NOTES_CHARS:
        raise InnerAgentOutputError(f"field 'notes': {len(v)} chars > {MAX_NOTES_CHARS} max")
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
        converged=_check_converged(_require_key(raw, "converged")),
        notes=_check_notes(_require_key(raw, "notes")),
    )


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
