"""Tests for promote_to_mb.py — stdlib-only, no external fixtures."""

from __future__ import annotations

import json
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

import pytest

# Import the module under test
sys.path.insert(0, str(Path(__file__).resolve().parent))
from promote_to_mb import derive_problem, dest_filename, promote


# ---------- dest_filename ----------


class TestDestFilename:
    def test_milestone_prefix(self):
        name = dest_filename("milestone-id1315", 1.5263e-13)
        assert name.startswith("milestone-")
        assert "-id1315-" in name
        assert name.endswith(".json")

    def test_reserve_prefix(self):
        name = dest_filename("reserve-ulp-1.5263", 0.156)
        assert name.startswith("reserve-")
        assert "-ulp-1.5263-" in name

    def test_sota_prefix(self):
        name = dest_filename("sota-chronos-id1149", 0.156)
        assert name.startswith("sota-")
        assert "-chronos-id1149-" in name

    def test_submitted_prefix(self):
        name = dest_filename("submitted-id1315", 1e-5)
        assert name.startswith("submitted-")

    def test_unknown_prefix_defaults_to_promoted(self):
        name = dest_filename("custom-tag", 0.5)
        assert name.startswith("promoted-")
        assert "-custom-tag-" in name

    def test_date_present(self):
        import time

        today = time.strftime("%Y-%m-%d")
        name = dest_filename("milestone-test", 1.0)
        assert today in name

    def test_score_in_filename(self):
        name = dest_filename("milestone-test", 1.5263e-13)
        assert "1.5263e-13" in name


# ---------- derive_problem ----------


class TestDeriveProblem:
    def test_from_results_path(self):
        p = "results/problem-6-kissing-number/polish-trail/session-best.json"
        assert derive_problem(p) == "problem-6-kissing-number"

    def test_from_nested_path(self):
        p = "/abs/results/problem-18-uncertainty-principle/polish-trail/foo.json"
        assert derive_problem(p) == "problem-18-uncertainty-principle"

    def test_no_problem_in_path_returns_none(self):
        assert derive_problem("some/random/file.json") is None


# ---------- promote (with temp dirs) ----------


@pytest.fixture
def sandbox(tmp_path):
    """Create a sandbox with source file and MB structure."""
    # Source file
    src_dir = tmp_path / "results" / "problem-6-kissing-number" / "polish-trail"
    src_dir.mkdir(parents=True)
    src_file = src_dir / "session-test-best.json"
    src_file.write_text(json.dumps({"vectors": [[1, 2]], "score": 0.5}))

    # MB destination
    mb_root = tmp_path / "mb" / "docs" / "problem-6-kissing-number" / "solutions"
    mb_root.mkdir(parents=True)

    # Experiment log
    log_dir = tmp_path / "mb" / "docs" / "problem-6-kissing-number"
    (log_dir / "experiment-log.md").write_text("# Experiment Log\n")

    return {
        "src": src_file,
        "mb_root": tmp_path / "mb",
        "solutions_dir": mb_root,
        "log_file": log_dir / "experiment-log.md",
    }


class TestPromote:
    def test_dry_run_no_filesystem_changes(self, sandbox):
        before_files = set(sandbox["solutions_dir"].iterdir())
        log_before = sandbox["log_file"].read_text()

        promote(
            source=sandbox["src"],
            tag="milestone-test",
            score=0.5,
            problem="problem-6-kissing-number",
            force=False,
            dry_run=True,
            mb_root=sandbox["mb_root"],
        )

        after_files = set(sandbox["solutions_dir"].iterdir())
        assert before_files == after_files
        assert sandbox["log_file"].read_text() == log_before

    def test_promote_copies_file(self, sandbox):
        promote(
            source=sandbox["src"],
            tag="milestone-test",
            score=0.5,
            problem="problem-6-kissing-number",
            force=False,
            dry_run=False,
            mb_root=sandbox["mb_root"],
        )

        # Source still exists
        assert sandbox["src"].exists()

        # Destination exists
        dest_files = list(sandbox["solutions_dir"].glob("milestone-*.json"))
        assert len(dest_files) == 1

        # Content matches
        src_data = json.loads(sandbox["src"].read_text())
        dst_data = json.loads(dest_files[0].read_text())
        assert src_data == dst_data

    def test_refuse_clobber_without_force(self, sandbox):
        # First promotion
        promote(
            source=sandbox["src"],
            tag="milestone-test",
            score=0.5,
            problem="problem-6-kissing-number",
            force=False,
            dry_run=False,
            mb_root=sandbox["mb_root"],
        )

        # Second promotion with same tag — should fail
        with pytest.raises(FileExistsError):
            promote(
                source=sandbox["src"],
                tag="milestone-test",
                score=0.5,
                problem="problem-6-kissing-number",
                force=False,
                dry_run=False,
                mb_root=sandbox["mb_root"],
            )

    def test_force_allows_overwrite(self, sandbox):
        # First promotion
        promote(
            source=sandbox["src"],
            tag="milestone-test",
            score=0.5,
            problem="problem-6-kissing-number",
            force=False,
            dry_run=False,
            mb_root=sandbox["mb_root"],
        )

        # Second promotion with --force — should succeed
        promote(
            source=sandbox["src"],
            tag="milestone-test",
            score=0.5,
            problem="problem-6-kissing-number",
            force=True,
            dry_run=False,
            mb_root=sandbox["mb_root"],
        )

        dest_files = list(sandbox["solutions_dir"].glob("milestone-*.json"))
        assert len(dest_files) == 1

    def test_experiment_log_appended(self, sandbox):
        promote(
            source=sandbox["src"],
            tag="milestone-test",
            score=0.5,
            problem="problem-6-kissing-number",
            force=False,
            dry_run=False,
            mb_root=sandbox["mb_root"],
        )

        log_text = sandbox["log_file"].read_text()
        assert "promoted milestone-test @ 0.5" in log_text

    def test_experiment_log_idempotent(self, sandbox):
        for _ in range(2):
            promote(
                source=sandbox["src"],
                tag="milestone-test",
                score=0.5,
                problem="problem-6-kissing-number",
                force=True,
                dry_run=False,
                mb_root=sandbox["mb_root"],
            )

        log_text = sandbox["log_file"].read_text()
        # Should appear exactly once
        assert log_text.count("promoted milestone-test @ 0.5") == 1

    def test_refuse_non_json_without_force(self, sandbox):
        txt_file = sandbox["src"].parent / "data.txt"
        txt_file.write_text("not json")

        with pytest.raises(ValueError, match="non-JSON"):
            promote(
                source=txt_file,
                tag="milestone-test",
                score=0.5,
                problem="problem-6-kissing-number",
                force=False,
                dry_run=False,
                mb_root=sandbox["mb_root"],
            )
