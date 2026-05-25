"""Tests for src/einstein/arena_submit.py."""
from __future__ import annotations

import json
import sys
from pathlib import Path
from unittest.mock import MagicMock

import pytest

_REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(_REPO / "src"))

from einstein import arena_submit as asub  # noqa: E402


# ---------------- helpers ----------------


def _make_resp(*, status: int, body: str | dict = "") -> MagicMock:
    text = json.dumps(body) if isinstance(body, dict) else body
    m = MagicMock(status_code=status, text=text)
    return m


# ---------------- behavior ----------------


def test_no_api_key_returns_clear_error(monkeypatch: pytest.MonkeyPatch,
                                         tmp_path: Path) -> None:
    # Point credentials path at a non-existent file + clear env
    monkeypatch.setattr(asub, "CREDENTIALS_PATH", tmp_path / "missing.json")
    monkeypatch.delenv("EINSTEIN_ARENA_API_KEY", raising=False)

    r = asub.submit_solution(14, {"vectors": []})
    assert r.ok is False
    assert "no API key" in (r.error or "")
    assert r.problem_id == 14


def test_dry_run_does_not_post_and_records_target_url() -> None:
    poster = MagicMock()
    r = asub.submit_solution(
        14, {"vectors": [[1, 0]]},
        api_key="test-key",
        dry_run=True,
        poster=poster,
    )
    assert r.ok is False
    assert r.error == "dry-run"
    assert r.extra["would_post_to"].endswith("/api/solutions")
    assert "problem_id" in r.extra["body_keys"]
    poster.assert_not_called()


def test_successful_post_parses_json_response() -> None:
    poster = MagicMock(return_value=_make_resp(
        status=200, body={"id": 9999, "rank": 1, "score": 2.6359831}
    ))
    r = asub.submit_solution(
        14, {"vectors": [[1, 0]]},
        api_key="test-key",
        expected_score=2.6359831,
        poster=poster,
    )
    assert r.ok is True
    assert r.http_status == 200
    assert r.arena_response == {"id": 9999, "rank": 1, "score": 2.6359831}
    assert r.extra["expected_score"] == 2.6359831
    # POST called once with correct shape
    poster.assert_called_once()
    call = poster.call_args
    assert call.args[0].endswith("/api/solutions")
    assert call.kwargs["json"]["problem_id"] == 14
    assert call.kwargs["headers"]["Authorization"] == "Bearer test-key"


def test_http_4xx_returns_error_with_status_and_arena_body() -> None:
    poster = MagicMock(return_value=_make_resp(
        status=409, body={"error": "submission rate-limited"}
    ))
    r = asub.submit_solution(
        14, {"vectors": []},
        api_key="test-key",
        poster=poster,
    )
    assert r.ok is False
    assert r.http_status == 409
    assert "HTTP 409" in (r.error or "")
    assert r.arena_response == {"error": "submission rate-limited"}


def test_network_failure_is_caught_and_reported() -> None:
    def failing_post(*args, **kwargs):
        raise ConnectionError("dns failure")

    r = asub.submit_solution(
        14, {"vectors": []},
        api_key="test-key",
        poster=failing_post,
    )
    assert r.ok is False
    assert "network failure" in (r.error or "")
    assert "dns failure" in (r.error or "")


def test_malformed_json_response_does_not_crash_on_2xx() -> None:
    """If arena returns 200 with a non-JSON body (e.g. empty or HTML), we
    still return ok=True with arena_response=None — the POST succeeded
    regardless of parse outcome."""
    poster = MagicMock(return_value=_make_resp(status=200, body="<html>oops</html>"))
    r = asub.submit_solution(
        14, {"vectors": []},
        api_key="test-key",
        poster=poster,
    )
    assert r.ok is True
    assert r.http_status == 200
    assert r.arena_response is None


def test_api_key_loaded_from_credentials_file_when_not_passed(
        monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> None:
    cred = tmp_path / "credentials.json"
    cred.write_text(json.dumps({"api_key": "from-file-key", "agent_name": "JSAgent"}))
    monkeypatch.setattr(asub, "CREDENTIALS_PATH", cred)
    monkeypatch.delenv("EINSTEIN_ARENA_API_KEY", raising=False)

    poster = MagicMock(return_value=_make_resp(status=200, body={"ok": True}))
    r = asub.submit_solution(14, {"vectors": []}, poster=poster)
    assert r.ok is True
    assert poster.call_args.kwargs["headers"]["Authorization"] == "Bearer from-file-key"


def test_env_var_used_when_credentials_file_absent(
        monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> None:
    monkeypatch.setattr(asub, "CREDENTIALS_PATH", tmp_path / "missing.json")
    monkeypatch.setenv("EINSTEIN_ARENA_API_KEY", "from-env-key")

    poster = MagicMock(return_value=_make_resp(status=200, body={"ok": True}))
    r = asub.submit_solution(14, {"vectors": []}, poster=poster)
    assert r.ok is True
    assert poster.call_args.kwargs["headers"]["Authorization"] == "Bearer from-env-key"
