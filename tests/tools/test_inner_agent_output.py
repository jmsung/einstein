"""Tests for docs/tools/inner_agent_output.py (Goal 7.3 — schema + validator)."""

from __future__ import annotations

import json
import sys
from pathlib import Path

import pytest

_REPO = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(_REPO / "docs" / "tools"))

import inner_agent_output as iao  # noqa: E402

# ---------------- happy path ----------------


VALID_RESPONSE: dict = {
    "strategy": "basin-hopping with rotation lottery",
    "score": 2.6359830849175,
    "payload": {"radii": [0.1, 0.2], "centers": [[0, 0], [1, 1]]},
    "dead_end_finding": None,
    "new_questions": [
        "docs/wiki/questions/2026-05-24-p14-rotation-lottery.md",
    ],
    "wiki_writes": [
        "docs/wiki/questions/2026-05-24-p14-rotation-lottery.md",
        "mb/problems/14-circle-packing-square/experiment-log.md",
    ],
    "converged": False,
    "notes": "rotation-lottery surfaced a new question; score unchanged",
}


def test_parse_response_happy_path():
    text = json.dumps(VALID_RESPONSE)
    resp = iao.parse_response(text)
    assert resp.strategy == "basin-hopping with rotation lottery"
    assert resp.score == pytest.approx(2.6359830849175)
    assert resp.payload == VALID_RESPONSE["payload"]
    assert resp.dead_end_finding is None
    assert resp.new_questions == VALID_RESPONSE["new_questions"]
    assert resp.wiki_writes == VALID_RESPONSE["wiki_writes"]
    assert resp.converged is False
    assert "rotation-lottery" in resp.notes


def test_parse_response_with_dead_end():
    payload = dict(VALID_RESPONSE)
    payload["score"] = None
    payload["payload"] = None
    payload["dead_end_finding"] = "docs/wiki/findings/dead-end-rotation-lottery.md"
    payload["converged"] = True
    resp = iao.parse_response(json.dumps(payload))
    assert resp.score is None
    assert resp.payload is None
    assert resp.dead_end_finding.endswith("rotation-lottery.md")
    assert resp.converged is True


def test_parse_response_int_score_coerced_to_float():
    payload = dict(VALID_RESPONSE)
    payload["score"] = 3
    resp = iao.parse_response(json.dumps(payload))
    assert isinstance(resp.score, float)
    assert resp.score == 3.0


def test_parse_response_dead_end_finding_field_missing_is_ok():
    """dead_end_finding is the one optional field — absent → None."""
    payload = dict(VALID_RESPONSE)
    del payload["dead_end_finding"]
    resp = iao.parse_response(json.dumps(payload))
    assert resp.dead_end_finding is None


# ---------------- fence stripping + trailing text ----------------


def test_parse_response_strips_json_code_fence():
    text = f"```json\n{json.dumps(VALID_RESPONSE)}\n```"
    resp = iao.parse_response(text)
    assert resp.strategy == VALID_RESPONSE["strategy"]


def test_parse_response_strips_bare_fence():
    text = f"```\n{json.dumps(VALID_RESPONSE)}\n```"
    resp = iao.parse_response(text)
    assert resp.strategy == VALID_RESPONSE["strategy"]


def test_parse_response_tolerates_leading_prose():
    """Real agents sometimes prefix with a sentence; we find the first {."""
    text = "Here is my response, the JSON object follows: " + json.dumps(VALID_RESPONSE)
    resp = iao.parse_response(text)
    assert resp.strategy == VALID_RESPONSE["strategy"]


def test_parse_response_tolerates_trailing_text():
    text = json.dumps(VALID_RESPONSE) + "\n\nThat's the end of my response."
    resp = iao.parse_response(text)
    assert resp.strategy == VALID_RESPONSE["strategy"]


# ---------------- parse-level errors ----------------


def test_parse_response_no_json_object_raises():
    with pytest.raises(iao.InnerAgentOutputError, match="no JSON object"):
        iao.parse_response("the agent failed to emit JSON")


def test_parse_response_malformed_json_raises():
    with pytest.raises(iao.InnerAgentOutputError, match="JSON parse error"):
        iao.parse_response("{strategy: 'unquoted-key-is-malformed'}")


def test_parse_response_top_level_not_object_raises():
    with pytest.raises(iao.InnerAgentOutputError, match="not an object"):
        iao.parse_response(json.dumps(["a", "list", "not", "an", "object"]))


# ---------------- field-level errors ----------------


def test_missing_required_field():
    payload = dict(VALID_RESPONSE)
    del payload["strategy"]
    with pytest.raises(iao.InnerAgentOutputError, match="missing required field: 'strategy'"):
        iao.parse_response(json.dumps(payload))


def test_empty_strategy_rejected():
    payload = dict(VALID_RESPONSE)
    payload["strategy"] = "   "
    with pytest.raises(iao.InnerAgentOutputError, match="non-empty"):
        iao.parse_response(json.dumps(payload))


def test_strategy_wrong_type():
    payload = dict(VALID_RESPONSE)
    payload["strategy"] = ["not", "a", "string"]
    with pytest.raises(iao.InnerAgentOutputError, match="strategy.*expected string"):
        iao.parse_response(json.dumps(payload))


def test_score_bool_rejected():
    """isinstance(True, int) is True — the validator must reject bool for score."""
    payload = dict(VALID_RESPONSE)
    payload["score"] = True
    with pytest.raises(iao.InnerAgentOutputError, match="score.*bool"):
        iao.parse_response(json.dumps(payload))


def test_score_string_rejected():
    payload = dict(VALID_RESPONSE)
    payload["score"] = "2.6"
    with pytest.raises(iao.InnerAgentOutputError, match="score.*expected number"):
        iao.parse_response(json.dumps(payload))


def test_payload_string_rejected():
    payload = dict(VALID_RESPONSE)
    payload["payload"] = "should be a dict or null"
    with pytest.raises(iao.InnerAgentOutputError, match="payload.*expected object"):
        iao.parse_response(json.dumps(payload))


def test_dead_end_finding_wrong_prefix_rejected():
    payload = dict(VALID_RESPONSE)
    payload["dead_end_finding"] = "docs/wiki/findings/some-other-finding.md"
    with pytest.raises(iao.InnerAgentOutputError, match="dead-end-"):
        iao.parse_response(json.dumps(payload))


def test_new_questions_must_be_list():
    payload = dict(VALID_RESPONSE)
    payload["new_questions"] = "docs/wiki/questions/foo.md"
    with pytest.raises(iao.InnerAgentOutputError, match="new_questions.*expected list"):
        iao.parse_response(json.dumps(payload))


def test_new_questions_wrong_prefix_rejected():
    payload = dict(VALID_RESPONSE)
    payload["new_questions"] = ["docs/wiki/findings/oops.md"]
    with pytest.raises(
        iao.InnerAgentOutputError, match="new_questions\\[0\\].*docs/wiki/questions/"
    ):
        iao.parse_response(json.dumps(payload))


def test_wiki_writes_wrong_prefix_rejected():
    payload = dict(VALID_RESPONSE)
    payload["wiki_writes"] = ["src/einstein/optimizer.py"]
    with pytest.raises(iao.InnerAgentOutputError, match="wiki_writes\\[0\\]"):
        iao.parse_response(json.dumps(payload))


def test_wiki_writes_accepts_mb_path():
    payload = dict(VALID_RESPONSE)
    payload["wiki_writes"] = ["mb/problems/14-circle-packing-square/experiment-log.md"]
    resp = iao.parse_response(json.dumps(payload))
    assert resp.wiki_writes[0].startswith("mb/")


def test_converged_int_rejected():
    """Strict bool — 0/1 is a frequent agent mistake."""
    payload = dict(VALID_RESPONSE)
    payload["converged"] = 0
    with pytest.raises(iao.InnerAgentOutputError, match="converged.*expected bool"):
        iao.parse_response(json.dumps(payload))


def test_notes_too_long_rejected():
    payload = dict(VALID_RESPONSE)
    payload["notes"] = "x" * (iao.MAX_NOTES_CHARS + 1)
    with pytest.raises(iao.InnerAgentOutputError, match="chars >"):
        iao.parse_response(json.dumps(payload))


def test_notes_newline_rejected():
    payload = dict(VALID_RESPONSE)
    payload["notes"] = "first line\nsecond line"
    with pytest.raises(iao.InnerAgentOutputError, match="single line"):
        iao.parse_response(json.dumps(payload))


def test_notes_wrong_type_rejected():
    payload = dict(VALID_RESPONSE)
    payload["notes"] = 42
    with pytest.raises(iao.InnerAgentOutputError, match="notes.*expected string"):
        iao.parse_response(json.dumps(payload))


# ---------------- validate() can be called on a pre-parsed dict ----------------


def test_validate_on_already_parsed_dict():
    """When --output-format=json gives us a dict directly, skip JSON parsing."""
    resp = iao.validate(dict(VALID_RESPONSE))
    assert resp.strategy == VALID_RESPONSE["strategy"]


def test_validate_rejects_non_dict_top_level():
    with pytest.raises(iao.InnerAgentOutputError, match="not an object"):
        iao.validate(["not", "a", "dict"])  # type: ignore[arg-type]


# ---------------- OUTPUT_SCHEMA round-trip ----------------


def test_output_schema_is_what_prompt_advertises():
    """Sanity: every required field in our validator appears in the schema string
    embedded in the prompt. If they drift, the agent and the parser disagree."""
    for required in (
        "strategy",
        "score",
        "payload",
        "dead_end_finding",
        "new_questions",
        "wiki_writes",
        "converged",
        "notes",
    ):
        assert required in iao.OUTPUT_SCHEMA, f"{required!r} missing from OUTPUT_SCHEMA"
