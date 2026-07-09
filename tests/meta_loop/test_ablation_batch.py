"""Tests for the resumable batch runner (Goal 3) — fake solve_fn, no sessions."""

from __future__ import annotations

import sys
from pathlib import Path

import pytest

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
    (co / "knowledge" / "wiki" / "problems").mkdir(parents=True)
    (co / "knowledge" / "wiki" / "problems" / "2-foo.md").write_text("SOTA scores here")
    receipt = ar.audit_checkout(co)
    assert receipt["passed"] is False
    assert "knowledge/wiki" in receipt["leaked_answer_key_files"]


def test_audit_checkout_does_not_flag_code_with_firewall_substring_names(tmp_path):
    # regression: a clean-room still has tool code like leaderboard_standings.py /
    # solution_artifact.py — filenames contain firewall substrings but are NOT
    # answer-key data; the receipt must pass.
    co = tmp_path / "einstein-cold"
    (co / "scripts").mkdir(parents=True)
    (co / "scripts" / "leaderboard_standings.py").write_text("# tool")
    (co / "src").mkdir(parents=True)
    (co / "src" / "solution_artifact.py").write_text("# tool")
    receipt = ar.audit_checkout(co)
    assert receipt["passed"] is True and receipt["leaked_answer_key_files"] == []


def test_audit_checkout_flags_solution_dumps(tmp_path):
    co = tmp_path / "einstein-cold"
    (co / "x").mkdir(parents=True)
    (co / "x" / "solution-best.json").write_text("{}")
    (co / "problems" / "4" / "solutions").mkdir(parents=True)
    (co / "problems" / "4" / "solutions" / "best.json").write_text("{}")
    receipt = ar.audit_checkout(co)
    assert receipt["passed"] is False
    assert len(receipt["leaked_answer_key_files"]) == 2


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
    # resume seed 1: the remaining 3 are run (cold needs no KB), no dupes
    ar.run_experiment(probs, [1], _fake_solver, results_dir=res, checkout_root=co)
    recs = ca.load_records(log)
    cold1 = [r for r in recs if r["arm"] == "cold" and r["seed"] == 1]
    assert len(cold1) == 6  # exactly the 6 problems, not 3 + 6
    assert len({r["problem_id"] for r in cold1}) == 6


# ---------------- counterbalanced order + crash-resilient resume (v2) ----------------


def test_counterbalanced_order_varies_banked_per_seed(tmp_path):
    co = _checkout(tmp_path)
    res = tmp_path / "results"
    ar.run_experiment(_problems(), [1, 2], _fake_solver, results_dir=res, checkout_root=co)
    warm = [r for r in ca.load_records(res / "runs.jsonl") if r["arm"] == "warm"]
    pid = "csq-n12"  # sequence_index 2
    banked = {
        s: next(r["lessons_read"] for r in warm if r["problem_id"] == pid and r["seed"] == s)
        for s in (1, 2)
    }
    assert banked[1] != banked[2]  # different rotation → different #lessons banked


def test_warm_per_cell_resume_after_crash(tmp_path):
    co = _checkout(tmp_path)
    res = tmp_path / "results"
    probs = _problems()
    calls = {"warm": 0}

    def crashy(problem, cfg, seed, spec):
        if cfg.write_kb:  # warm only
            calls["warm"] += 1
            if calls["warm"] > 3:
                raise RuntimeError("simulated crash")
        return _fake_solver(problem, cfg, seed, spec)

    with pytest.raises(RuntimeError):
        ar.run_experiment(probs, [1], crashy, results_dir=res, checkout_root=co)
    warm1 = [
        r for r in ca.load_records(res / "runs.jsonl") if r["arm"] == "warm" and r["seed"] == 1
    ]
    assert 0 < len(warm1) < 6  # some cells durable, sequence incomplete

    # resume with a clean solver → continues from the on-disk KB, no dupes
    summary = ar.run_experiment(probs, [1], _fake_solver, results_dir=res, checkout_root=co)
    warm1 = [
        r for r in ca.load_records(res / "runs.jsonl") if r["arm"] == "warm" and r["seed"] == 1
    ]
    assert len(warm1) == 6 and len({r["problem_id"] for r in warm1}) == 6
    assert "warm-seed1" in summary["resumed"]


def test_resume_falls_back_when_kb_inconsistent(tmp_path):
    co = _checkout(tmp_path)
    res = tmp_path / "results"
    res.mkdir(parents=True)
    log = res / "runs.jsonl"
    probs = _problems()
    # plant 3 WARM records but NO on-disk KB (simulating a lost/corrupt KB)
    order = ca.cyclic_order(probs, 1)
    for pid in order[:3]:
        sidx = next(p.sequence_index for p in probs if p.problem_id == pid)
        ca.append_record(
            ca.RunRecord(
                pid,
                "warm",
                1,
                sidx,
                0.05,
                0.05,
                1.0,
                0.0,
                1,
                0.0,
                [(0, 0.05)],
                1,
                sidx,
                0,
                ca.EMPTY_KB_HASH,
                "deadbeef",
            ),
            log,
        )
    # KB dir does not exist → lesson_count 0 ≠ 3 done → fallback purges + reruns fresh
    ar.run_experiment(probs, [1], _fake_solver, results_dir=res, checkout_root=co)
    warm1 = [r for r in ca.load_records(log) if r["arm"] == "warm" and r["seed"] == 1]
    assert len(warm1) == 6 and len({r["problem_id"] for r in warm1}) == 6


# ---------------- air-gap HARD GATE (audit is a gate, not a receipt) ----------------


def test_assert_clean_checkout_passes_on_clean_room(tmp_path):
    co = tmp_path / "einstein-cold"
    (co / "src").mkdir(parents=True)
    receipt = ar.assert_clean_checkout(co)
    assert receipt["passed"] is True


def test_assert_clean_checkout_raises_on_leaked_wiki(tmp_path):
    co = tmp_path / "einstein-cold"
    (co / "knowledge" / "wiki").mkdir(parents=True)
    with pytest.raises(ar.AirGapViolation):
        ar.assert_clean_checkout(co)


def test_assert_clean_checkout_raises_on_missing_checkout(tmp_path):
    with pytest.raises(ar.AirGapViolation):
        ar.assert_clean_checkout(tmp_path / "does-not-exist")


def test_run_experiment_aborts_before_running_on_dirty_checkout(tmp_path):
    # A leaked wiki in either arm checkout must abort the batch BEFORE any compute
    # (pre-flight hard gate) — no records written.
    co = _checkout(tmp_path)
    (co / "einstein-warm" / "knowledge" / "source").mkdir(parents=True)
    res = tmp_path / "results"
    with pytest.raises(ar.AirGapViolation):
        ar.run_experiment(_problems(), [1], _fake_solver, results_dir=res, checkout_root=co)
    # gate fired before the run: no run records
    assert not (res / "runs.jsonl").exists() or ca.load_records(res / "runs.jsonl") == []
