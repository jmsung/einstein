"""Tests for src/einstein/meta_loop/solution_artifact.py — Goal 3."""

from __future__ import annotations

import json
import sys
from pathlib import Path

_REPO = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(_REPO / "src"))

from einstein.meta_loop import solution_artifact as sa  # noqa: E402


def test_write_and_load_roundtrip(tmp_path):
    rec = sa.build_record(
        cycle_id=312,
        problem="P4-third-autocorrelation",
        ts="2026-06-12T00:00:00Z",
        start_score="1.4525",
        end_score="1.4520",
        outcome="improved-local",
        technique="warm-self-pruning.md",
        payload={"coeffs": [0.1, 0.2], "n": 60},
        notes="dispatch=remez score=1.452",
    )
    path = sa.write_artifact(tmp_path, 312, rec)
    assert path == tmp_path / "cycle-312.json"
    loaded = sa.load_artifact(tmp_path, 312)
    assert loaded["payload"] == {"coeffs": [0.1, 0.2], "n": 60}
    assert loaded["outcome"] == "improved-local"
    # key order is human-friendly: cycle_id first, payload before notes
    assert list(loaded.keys())[0] == "cycle_id"


def test_persist_cycle_from_result_dict(tmp_path):
    result = {
        "start_score": "2.001",
        "end_score": "2.001",
        "outcome": "no-change",
        "chosen_techniques": ["construction-survey.md", "second.md"],
        "payload": None,
        "notes": "autonomous_loop inner_attempt — category=kissing",
    }
    path = sa.persist_cycle(tmp_path, cycle_id=27, problem="P22-kissing-d12", result=result, ts="t")
    data = json.loads(path.read_text())
    assert data["cycle_id"] == 27
    assert data["technique"] == "construction-survey.md"  # first chosen
    assert data["payload"] is None  # strategy-only cycle still persisted


def test_persist_cycle_no_techniques(tmp_path):
    sa.persist_cycle(tmp_path, cycle_id=5, problem="P1-erdos", result={"outcome": "x"}, ts="t")
    assert sa.load_artifact(tmp_path, 5)["technique"] is None


def test_write_tolerates_nonjson_payload(tmp_path):
    """A payload with a non-JSON value (e.g. a Path) must not break persistence."""
    rec = sa.build_record(
        cycle_id=1,
        problem="P1",
        ts="t",
        start_score=None,
        end_score=None,
        outcome="x",
        technique=None,
        payload={"path": Path("/tmp/x"), "v": 3},
        notes=None,
    )
    sa.write_artifact(tmp_path, 1, rec)
    loaded = sa.load_artifact(tmp_path, 1)
    assert loaded["payload"]["path"] == "/tmp/x"  # stringified, not crashed


def test_list_artifact_ids(tmp_path):
    for cid in (3, 10, 7):
        sa.write_artifact(tmp_path, cid, {"cycle_id": cid})
    (tmp_path / "not-a-cycle.json").write_text("{}")
    (tmp_path / "cycle-notanint.json").write_text("{}")
    assert sa.list_artifact_ids(tmp_path) == {3, 7, 10}


def test_load_missing_is_none(tmp_path):
    assert sa.load_artifact(tmp_path, 999) is None


def test_list_artifact_ids_missing_dir(tmp_path):
    assert sa.list_artifact_ids(tmp_path / "nope") == set()
