"""Tests for docs/tools/promotion_candidates.py (Goal 4 of js/feat/research-synthesis)."""

from __future__ import annotations

import io
import json
import sys
from pathlib import Path

_REPO = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(_REPO / "docs" / "tools"))

import promotion_candidates as pc  # noqa: E402


def _jsonl(tmp_path: Path, records: list[dict]) -> Path:
    p = tmp_path / "cited-sources.jsonl"
    p.write_text("\n".join(json.dumps(r) for r in records) + "\n")
    return p


def test_counts_per_source_path(tmp_path: Path) -> None:
    """4 records: source X cited in 3 cycles (above threshold), Y in 1."""
    records = [
        {
            "cycle_id": 1,
            "problem": "P14",
            "cited_sources": ["knowledge/source/X.md", "knowledge/source/Y.md"],
        },
        {"cycle_id": 2, "problem": "P14", "cited_sources": ["knowledge/source/X.md"]},
        {"cycle_id": 3, "problem": "P19", "cited_sources": ["knowledge/source/X.md"]},
        {"cycle_id": 4, "problem": "P14", "cited_sources": []},
    ]
    jsonl = _jsonl(tmp_path, records)
    out = tmp_path / "promotion-candidates.md"
    n = pc.run(jsonl=jsonl, output=out, threshold=3)
    assert n == 1
    md = out.read_text()
    assert "knowledge/source/X.md" in md
    assert "3" in md  # count
    assert "1, 2, 3" in md or "1,2,3" in md  # cycle list
    assert "knowledge/source/Y.md" not in md


def test_threshold_respected(tmp_path: Path) -> None:
    """X cited 2 times → below default threshold 3 → no candidate."""
    records = [
        {"cycle_id": 1, "problem": "P14", "cited_sources": ["knowledge/source/X.md"]},
        {"cycle_id": 2, "problem": "P14", "cited_sources": ["knowledge/source/X.md"]},
    ]
    jsonl = _jsonl(tmp_path, records)
    out = tmp_path / "promotion-candidates.md"
    n = pc.run(jsonl=jsonl, output=out, threshold=3)
    assert n == 0
    md = out.read_text()
    assert "no candidates" in md.lower() or "(none)" in md.lower()


def test_dry_run_writes_to_stdout_and_skips_file(tmp_path: Path) -> None:
    records = [
        {"cycle_id": i, "problem": "P14", "cited_sources": ["knowledge/source/X.md"]} for i in range(5)
    ]
    jsonl = _jsonl(tmp_path, records)
    out = tmp_path / "promotion-candidates.md"
    stream = io.StringIO()
    n = pc.run(jsonl=jsonl, output=out, threshold=3, dry_run=True, out_stream=stream)
    assert n == 1
    assert not out.exists()
    s = stream.getvalue()
    assert "knowledge/source/X.md" in s


def test_empty_jsonl_writes_header_only(tmp_path: Path) -> None:
    jsonl = tmp_path / "cited-sources.jsonl"
    jsonl.write_text("")
    out = tmp_path / "promotion-candidates.md"
    n = pc.run(jsonl=jsonl, output=out, threshold=3)
    assert n == 0
    md = out.read_text()
    assert "Promotion candidates" in md or "promotion" in md.lower()


def test_malformed_lines_skipped(tmp_path: Path) -> None:
    """A bad JSON line is skipped, not fatal; valid lines still count."""
    jsonl = tmp_path / "cited-sources.jsonl"
    lines = [
        json.dumps({"cycle_id": 1, "problem": "P", "cited_sources": ["knowledge/source/X.md"]}),
        "this is not json {",
        json.dumps({"cycle_id": 2, "problem": "P", "cited_sources": ["knowledge/source/X.md"]}),
        json.dumps({"cycle_id": 3, "problem": "P", "cited_sources": ["knowledge/source/X.md"]}),
    ]
    jsonl.write_text("\n".join(lines) + "\n")
    out = tmp_path / "promotion-candidates.md"
    n = pc.run(jsonl=jsonl, output=out, threshold=3)
    assert n == 1  # X still hits threshold via 3 valid records


def test_missing_jsonl_returns_zero(tmp_path: Path) -> None:
    """Missing input file → graceful no-op."""
    jsonl = tmp_path / "does-not-exist.jsonl"
    out = tmp_path / "promotion-candidates.md"
    n = pc.run(jsonl=jsonl, output=out, threshold=3)
    assert n == 0
    assert out.exists()


def test_cli_argv_parsing(tmp_path: Path) -> None:
    jsonl = tmp_path / "cited-sources.jsonl"
    jsonl.write_text("")
    out = tmp_path / "candidates.md"
    rc = pc.main(["--jsonl", str(jsonl), "--output", str(out), "--threshold", "2"])
    assert rc == 0
    assert out.exists()


def test_gate_uses_distinct_cycles_not_total_cites(tmp_path: Path) -> None:
    """code-review S1: a source cited twice in ONE cycle must not over-count.
    Gate is on distinct cycles, not total cite occurrences."""
    records = [
        # X cited twice in cycle 1, once in cycle 2 = 3 total cites but only 2 distinct cycles
        {
            "cycle_id": 1,
            "problem": "P14",
            "cited_sources": ["knowledge/source/X.md", "knowledge/source/X.md"],
        },
        {"cycle_id": 2, "problem": "P14", "cited_sources": ["knowledge/source/X.md"]},
    ]
    jsonl = _jsonl(tmp_path, records)
    out = tmp_path / "promotion-candidates.md"
    # threshold 3: total-cites=3 would (wrongly) pass; distinct-cycles=2 correctly fails
    n = pc.run(jsonl=jsonl, output=out, threshold=3)
    assert n == 0, "should NOT promote — only 2 distinct cycles despite 3 total cites"
    # threshold 2: distinct-cycles=2 passes
    n2 = pc.run(jsonl=jsonl, output=out, threshold=2)
    assert n2 == 1
