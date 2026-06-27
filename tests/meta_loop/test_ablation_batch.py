"""Tests for the resumable batch runner (Goal 3) — fake solve_fn, no sessions."""

from __future__ import annotations

import sys
from pathlib import Path

_REPO = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(_REPO / "src"))

from einstein.meta_loop import ablation_runner as ar  # noqa: E402
from einstein.meta_loop import compounding_ablation as ca  # noqa: E402
from einstein.meta_loop.trajectory import TrajectoryPoint  # noqa: E402


def _problems(n=6):
    return [
        ca.Problem(
            f"csq-n{10 + i}", n=10 + i, sequence_index=i, reference_optimum=1.0, statement="s"
        )
        for i in range(n)
    ]


def _fake_solver(problem, cfg, seed, spec):
    gain = 0.05 * len(spec.accumulated_lessons) if cfg.read_kb else 0.0
    ci, final = 0.05, 0.05 + min(0.99, 0.5 + gain) * (problem.reference_optimum - 0.05)
    return ca.SolveResult(
        [TrajectoryPoint(0, ci), TrajectoryPoint(1, final)],
        score_coldinit=ci,
        score_final=final,
        lesson_text=f"lesson:{problem.problem_id}",
        attempted_techniques={"nm"},
    )


def _checkout(tmp_path):
    for arm in ("cold", "warm"):
        (tmp_path / "co" / f"einstein-{arm}").mkdir(parents=True)
    return tmp_path / "co"


# ---------------- audit receipt ----------------


def test_audit_checkout_passes_on_clean_room(tmp_path):
    co = tmp_path / "einstein-cold"
    (co / "src").mkdir(parents=True)
    (co / "src" / "ok.py").write_text("x")
    receipt = ar.audit_checkout(co)
    assert receipt["passed"] is True
    assert receipt["leaked_answer_key_files"] == []
    assert receipt["web_tools_in_allowlist"] == []


def test_audit_checkout_flags_leaked_answer_key(tmp_path):
    co = tmp_path / "einstein-cold"
    (co / "docs" / "wiki" / "problems").mkdir(parents=True)
    (co / "docs" / "wiki" / "problems" / "2-foo.md").write_text("SOTA scores here")
    receipt = ar.audit_checkout(co)
    assert receipt["passed"] is False
    assert any("problems" in f for f in receipt["leaked_answer_key_files"])


# ---------------- run_experiment ----------------


def test_run_experiment_full_matrix_and_schema(tmp_path):
    co = _checkout(tmp_path)
    res = tmp_path / "results"
    summary = ar.run_experiment(
        _problems(), [1, 2, 3], _fake_solver, results_dir=res, checkout_root=co
    )
    assert summary["n_records"] == 36
    assert len(summary["ran"]) == 6  # 2 arms × 3 seeds sequences
    recs = ca.load_records(res / "runs.jsonl")
    assert {r["arm"] for r in recs} == {"cold", "warm"}
    # §10 schema fields present
    for field in ("problem_id", "gap_closed", "kb_state_hash_before", "lessons_read"):
        assert field in recs[0]
    # audit receipts written + all passed
    assert (res / "audit.jsonl").exists()
    assert all(a["passed"] for a in summary["audits"])


def test_run_experiment_resumes_skipping_completed(tmp_path):
    co = _checkout(tmp_path)
    res = tmp_path / "results"
    # first pass: seed 1 only
    s1 = ar.run_experiment(_problems(), [1], _fake_solver, results_dir=res, checkout_root=co)
    assert len(s1["ran"]) == 2 and s1["n_records"] == 12
    # second pass: seeds 1 and 2 — seed 1 already done, only seed 2 runs
    s2 = ar.run_experiment(_problems(), [1, 2], _fake_solver, results_dir=res, checkout_root=co)
    assert sorted(s2["skipped"]) == ["cold-seed1", "warm-seed1"]
    assert sorted(s2["ran"]) == ["cold-seed2", "warm-seed2"]
    assert s2["n_records"] == 24  # no duplicates


def test_run_experiment_purges_partial_sequence(tmp_path):
    co = _checkout(tmp_path)
    res = tmp_path / "results"
    res.mkdir(parents=True)
    log = res / "runs.jsonl"
    # plant a PARTIAL cold-seed1 (only 3 of 6 problems) as if interrupted
    probs = _problems()
    for p in probs[:3]:
        rec = ca.RunRecord(
            problem_id=p.problem_id,
            arm="cold",
            seed=1,
            sequence_index=p.sequence_index,
            score_coldinit=0.05,
            score_final=0.05,
            score_optimum_ref=1.0,
            gap_closed=0.0,
            cycles=1,
            wall_clock_s=0.0,
            trajectory=[(0, 0.05)],
            lessons_written=0,
            lessons_read=0,
            dead_ends_avoided=0,
            kb_state_hash_before=ca.EMPTY_KB_HASH,
            kb_state_hash_after=ca.EMPTY_KB_HASH,
        )
        ca.append_record(rec, log)
    assert len(ca.load_records(log)) == 3
    # resume seed 1: the partial cold sequence is purged + fully re-run (no dupes)
    ar.run_experiment(probs, [1], _fake_solver, results_dir=res, checkout_root=co)
    recs = ca.load_records(log)
    cold1 = [r for r in recs if r["arm"] == "cold" and r["seed"] == 1]
    assert len(cold1) == 6  # exactly the 6 problems, not 3 + 6
    assert len({r["problem_id"] for r in cold1}) == 6
