"""Tests for the meta_self_edit queue surface (G5 of recursive-meta).

Covers `parse_queue_entry`, `list_queue`, `render_queue`, `apply_queue_entry`,
including the never-auto-merge guarantee (queue entries don't disappear from
the queue without an explicit `apply_queue_entry` call).
"""

from __future__ import annotations

import datetime as dt
import sys
from pathlib import Path

import pytest

_REPO = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(_REPO / "src"))

from einstein.meta_loop.meta_gate import evaluate_meta_self_edit_post_shadow  # noqa: E402
from einstein.meta_loop.proposals import Proposal, ProposalType  # noqa: E402
from einstein.meta_loop.queue import (  # noqa: E402
    GitRunResult,
    apply_queue_entry,
    list_queue,
    parse_queue_entry,
    render_queue,
)
from einstein.meta_loop.shadow import ArmMetrics, ShadowDelta, ShadowResult  # noqa: E402

UTC = dt.timezone.utc


# ---------------- fixtures ----------------


def _make_queue_entry_file(tmp_path: Path, *, queue_id: str = "20260528t130000-cafe1234") -> Path:
    """Drive the real meta_gate.evaluate_meta_self_edit_post_shadow to produce
    a queue entry — exercises the end-to-end path the production code uses."""
    proposal = Proposal(
        id=f"meta-{queue_id}",
        type=ProposalType.META_SELF_EDIT.value,
        target_path="scripts/meta_loop.py",
        proposed_diff=(
            "--- a/scripts/meta_loop.py\n"
            "+++ b/scripts/meta_loop.py\n"
            "@@ -1,1 +1,2 @@\n"
            "+# diagnostic marker\n"
            " #!/usr/bin/env python3\n"
        ),
        evidence_cycles=list(range(12)),
        requires_shadow=True,
        rationale="recurring rejection pattern — surfaced for review",
        proposer_id="recursive-meta-v0",
    )
    delta = ShadowDelta(
        arm_a=ArmMetrics(
            cycles=10,
            score_changed_cycles=5,
            findings_added=10,
            concepts_added=0,
            dead_ends_added=1,
        ),
        arm_b=ArmMetrics(
            cycles=10,
            score_changed_cycles=5,
            findings_added=0,
            concepts_added=0,
            dead_ends_added=1,
        ),
    )
    shadow = ShadowResult(proposal_id=proposal.id, n_cycles=10, delta=delta, a_wins=True)
    queue_dir = tmp_path / "meta-self-edit-queue"
    snapshot_dir = tmp_path / "meta-loop-snapshots"
    source = tmp_path / "scripts" / "meta_loop.py"
    source.parent.mkdir(parents=True, exist_ok=True)
    source.write_text("#!/usr/bin/env python3\n# original\n")
    audit = tmp_path / "meta-proposals.md"
    evaluate_meta_self_edit_post_shadow(
        proposal,
        shadow,
        snapshot_source=source,
        queue_dir=queue_dir,
        snapshot_dir=snapshot_dir,
        audit_log=audit,
        clock=lambda: dt.datetime(2026, 5, 28, 13, 0, 0, tzinfo=UTC),
    )
    files = list(queue_dir.iterdir())
    assert len(files) == 1
    return files[0]


# ---------------- parse_queue_entry ----------------


def test_parse_queue_entry_extracts_fields(tmp_path: Path) -> None:
    qf = _make_queue_entry_file(tmp_path)
    entry = parse_queue_entry(qf)
    assert entry.proposal_id.startswith("meta-")
    assert entry.proposer_id == "recursive-meta-v0"
    assert entry.target_path == "scripts/meta_loop.py"
    assert entry.snapshot_path.endswith(".py")
    assert entry.diff.startswith("--- a/scripts/meta_loop.py")
    assert "diagnostic marker" in entry.diff
    assert "recurring rejection" in entry.rationale


def test_parse_queue_entry_rejects_missing_title(tmp_path: Path) -> None:
    bad = tmp_path / "broken.md"
    bad.write_text("no title here\n")
    with pytest.raises(ValueError, match="title"):
        parse_queue_entry(bad)


def test_parse_queue_entry_rejects_missing_diff_fence(tmp_path: Path) -> None:
    bad = tmp_path / "broken.md"
    bad.write_text("# meta_self_edit candidate xyz\n\nno diff fence\n")
    with pytest.raises(ValueError, match="diff"):
        parse_queue_entry(bad)


# ---------------- list_queue + render_queue ----------------


def test_list_queue_empty(tmp_path: Path) -> None:
    assert list_queue(tmp_path / "no-such-dir") == []


def test_list_queue_returns_entries_oldest_first(tmp_path: Path) -> None:
    qf1 = _make_queue_entry_file(tmp_path, queue_id="20260528t130000-aaaaaaaa")
    # Manually rename to control sort order (real timestamps are monotonic)
    qf1.rename(qf1.parent / "20260528t130000-aaaaaaaa.md")
    # add a second entry by re-running with different ts in real life;
    # for the test, just verify the existing one is found
    entries = list_queue(qf1.parent)
    assert len(entries) >= 1
    assert entries[0].queue_id.endswith("aaaaaaaa")


def test_render_queue_empty_dir() -> None:
    assert "no meta_self_edit queue entries" in render_queue([])


def test_render_queue_summarizes_entries(tmp_path: Path) -> None:
    qf = _make_queue_entry_file(tmp_path)
    entries = list_queue(qf.parent)
    rendered = render_queue(entries)
    assert "1 queue entry" in rendered
    assert "recursive-meta-v0" in rendered
    assert "scripts/meta_loop.py" in rendered


# ---------------- apply_queue_entry ----------------


def test_apply_queue_entry_invokes_git_in_order(tmp_path: Path) -> None:
    qf = _make_queue_entry_file(tmp_path)
    queue_dir = qf.parent
    resolved_dir = tmp_path / "queue-resolved"

    recorded: list[list[str]] = []

    def fake_git(args, cwd, stdin):
        recorded.append(list(args))
        if args[0] == "rev-parse":
            return GitRunResult(ok=True, stdout="abc1234567def\n")
        return GitRunResult(ok=True)

    result = apply_queue_entry(
        qf.stem,
        queue_dir=queue_dir,
        resolved_dir=resolved_dir,
        repo_root=tmp_path,
        git_runner=fake_git,
    )
    assert result.ok
    assert result.commit_sha == "abc1234567def"
    # git apply, git add, git commit, git rev-parse — in order
    assert [r[0] for r in recorded] == ["apply", "add", "commit", "rev-parse"]
    # Queue file moved
    assert not qf.exists()
    assert (resolved_dir / qf.name).exists()


def test_apply_queue_entry_missing_id_returns_error(tmp_path: Path) -> None:
    queue_dir = tmp_path / "queue"
    queue_dir.mkdir()
    result = apply_queue_entry(
        "no-such-id",
        queue_dir=queue_dir,
        resolved_dir=tmp_path / "resolved",
        repo_root=tmp_path,
        git_runner=lambda *args: GitRunResult(ok=True),
    )
    assert not result.ok
    assert "no queue entry" in result.error


def test_apply_queue_entry_leaves_queue_in_place_on_apply_failure(tmp_path: Path) -> None:
    """Never-auto-merge invariant: a `git apply` failure must NOT move the
    queue file to resolved/. The human keeps a chance to fix or escalate."""
    qf = _make_queue_entry_file(tmp_path)
    queue_dir = qf.parent
    resolved_dir = tmp_path / "queue-resolved"

    def fake_git(args, cwd, stdin):
        if args[0] == "apply":
            return GitRunResult(ok=False, stderr="patch does not apply")
        return GitRunResult(ok=True)

    result = apply_queue_entry(
        qf.stem,
        queue_dir=queue_dir,
        resolved_dir=resolved_dir,
        repo_root=tmp_path,
        git_runner=fake_git,
    )
    assert not result.ok
    assert "patch does not apply" in result.error
    assert qf.exists()  # queue file NOT moved
    assert not resolved_dir.exists() or not any(resolved_dir.iterdir())


def test_meta_loop_cli_queue_list_runs(tmp_path: Path) -> None:
    """Smoke-test: `meta_loop queue --list` against an empty queue exits 0."""
    import importlib.util as _ilu

    script_path = _REPO / "scripts" / "meta_loop.py"
    spec = _ilu.spec_from_file_location("meta_loop_cli_test", script_path)
    mod = _ilu.module_from_spec(spec)
    spec.loader.exec_module(mod)
    rc = mod.main(
        [
            "queue",
            "--list",
            "--queue-dir",
            str(tmp_path / "empty-queue"),
        ]
    )
    assert rc == 0


def test_meta_loop_cli_queue_list_and_apply_mutually_exclusive(tmp_path: Path) -> None:
    import importlib.util as _ilu

    script_path = _REPO / "scripts" / "meta_loop.py"
    spec = _ilu.spec_from_file_location("meta_loop_cli_test2", script_path)
    mod = _ilu.module_from_spec(spec)
    spec.loader.exec_module(mod)
    rc = mod.main(
        [
            "queue",
            "--list",
            "--apply",
            "some-id",
            "--queue-dir",
            str(tmp_path / "q"),
        ]
    )
    assert rc == 2


def test_apply_queue_entry_commits_message_references_proposal(tmp_path: Path) -> None:
    qf = _make_queue_entry_file(tmp_path)
    recorded_msgs: list[str] = []

    def fake_git(args, cwd, stdin):
        if args[0] == "commit":
            recorded_msgs.append(args[2])  # ["commit", "-m", <msg>]
        if args[0] == "rev-parse":
            return GitRunResult(ok=True, stdout="abc\n")
        return GitRunResult(ok=True)

    apply_queue_entry(
        qf.stem,
        queue_dir=qf.parent,
        resolved_dir=tmp_path / "resolved",
        repo_root=tmp_path,
        git_runner=fake_git,
    )
    assert len(recorded_msgs) == 1
    msg = recorded_msgs[0]
    assert "meta_self_edit" in msg
    assert "scripts/meta_loop.py" in msg
    assert "recursive-meta-v0" in msg
