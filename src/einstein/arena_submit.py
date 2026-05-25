"""arena_submit.py — central POST helper for Einstein Arena solutions.

Each per-problem `scripts/{problem}/submit.py` historically duplicated the
POST body, auth, and error-handling logic. This module centralizes that
into one helper so the autonomous loop (and any future submission path)
can submit through a single tested interface.

The helper does NOT enforce policy — that's `auto_submit.py`'s job (A2).
This is the raw POST + parse layer:

    submit_solution(problem_id, payload, expected_score=None, dry_run=False)
        -> SubmissionResult

Credentials load from `~/.config/einsteinarena/credentials.json` or the
`EINSTEIN_ARENA_API_KEY` env var. Base URL overridable via
`EINSTEIN_ARENA_BASE_URL` (defaults to https://einsteinarena.com).
"""
from __future__ import annotations

import json
import logging
import os
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

try:
    import requests  # type: ignore[import-not-found]
except ImportError:  # pragma: no cover — requests is a project dep
    requests = None  # type: ignore[assignment]

log = logging.getLogger("arena_submit")

DEFAULT_BASE_URL = "https://einsteinarena.com"
CREDENTIALS_PATH = Path.home() / ".config" / "einsteinarena" / "credentials.json"


@dataclass
class SubmissionResult:
    """Outcome of one POST to /api/solutions."""
    ok: bool
    problem_id: int
    http_status: int | None = None
    arena_response: dict | None = None
    error: str | None = None
    extra: dict = field(default_factory=dict)


def base_url() -> str:
    """Read the arena base URL from env, falling back to the canonical default."""
    return os.environ.get("EINSTEIN_ARENA_BASE_URL", DEFAULT_BASE_URL)


def load_api_key() -> str | None:
    """Load API key from credentials file or env. Returns None if absent.

    Order: credentials.json → env var. None signals "no key configured" —
    callers should report a clear error rather than POSTing without auth.
    """
    if CREDENTIALS_PATH.is_file():
        try:
            return json.loads(CREDENTIALS_PATH.read_text()).get("api_key")
        except (OSError, json.JSONDecodeError) as e:
            log.warning("credentials.json unreadable: %s", e)
    return os.environ.get("EINSTEIN_ARENA_API_KEY") or None


def submit_solution(
    problem_id: int,
    payload: dict,
    *,
    expected_score: float | None = None,
    api_key: str | None = None,
    dry_run: bool = False,
    timeout: int = 30,
    base_url_override: str | None = None,
    poster: Any = None,
) -> SubmissionResult:
    """POST {problem_id, solution: payload} to /api/solutions and parse the response.

    `payload` is the solution body shape the arena expects for this problem
    (e.g. {"vectors": [...]} or {"laguerre_double_roots": [...]}). The caller
    is responsible for the shape — this helper does not validate it.

    `expected_score` is informational only; the arena verifies server-side.
    Recorded in `result.extra["expected_score"]` for audit/log purposes.

    `dry_run=True` returns ok=False with `error="dry-run"` and the target URL
    in `extra["would_post_to"]` — useful for sanity-checking the request
    shape without making network calls.

    `poster` is a test seam — defaults to `requests.post`. Tests pass a mock.

    Failure taxonomy (returns ok=False):
      - no API key → error mentions credentials
      - dry_run → error="dry-run"
      - network exception → error starts "network failure:"
      - HTTP 4xx/5xx → error="HTTP <status>", http_status populated,
        arena_response populated if the body parsed as JSON
      - 2xx success → ok=True; arena_response is whatever the arena returned
        (or None if body wasn't valid JSON, e.g. empty response)
    """
    key = api_key if api_key is not None else load_api_key()
    if not key:
        return SubmissionResult(
            ok=False, problem_id=problem_id,
            error=(
                "no API key (set EINSTEIN_ARENA_API_KEY or "
                f"{CREDENTIALS_PATH})"
            ),
        )

    url = f"{base_url_override or base_url()}/api/solutions"
    body = {"problem_id": problem_id, "solution": payload}
    headers = {
        "Authorization": f"Bearer {key}",
        "Content-Type": "application/json",
    }
    extra: dict = {}
    if expected_score is not None:
        extra["expected_score"] = expected_score

    if dry_run:
        extra["would_post_to"] = url
        extra["body_keys"] = list(body.keys())
        return SubmissionResult(
            ok=False, problem_id=problem_id, error="dry-run", extra=extra,
        )

    if poster is None:
        if requests is None:  # pragma: no cover
            return SubmissionResult(
                ok=False, problem_id=problem_id,
                error="requests library not installed",
            )
        poster = requests.post

    log.info("POST %s problem_id=%d", url, problem_id)
    try:
        resp = poster(url, json=body, headers=headers, timeout=timeout)
    except Exception as e:
        # requests.exceptions.RequestException is the documented catch, but
        # mocks may raise other types; treat any post-time exception as
        # "network failure" rather than crash the loop.
        return SubmissionResult(
            ok=False, problem_id=problem_id,
            error=f"network failure: {type(e).__name__}: {e}",
            extra=extra,
        )

    status = getattr(resp, "status_code", None)
    arena_json: dict | None = None
    body_text = getattr(resp, "text", "") or ""
    if body_text:
        try:
            parsed = json.loads(body_text)
            if isinstance(parsed, dict):
                arena_json = parsed
            else:
                arena_json = {"raw": parsed}
        except (json.JSONDecodeError, ValueError):
            arena_json = None

    if status is None:
        return SubmissionResult(
            ok=False, problem_id=problem_id,
            arena_response=arena_json,
            error="response has no status code",
            extra=extra,
        )
    if status >= 400:
        return SubmissionResult(
            ok=False, problem_id=problem_id,
            http_status=status, arena_response=arena_json,
            error=f"HTTP {status}",
            extra=extra,
        )

    return SubmissionResult(
        ok=True, problem_id=problem_id,
        http_status=status, arena_response=arena_json,
        extra=extra,
    )
