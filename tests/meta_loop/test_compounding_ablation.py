"""Tests for the blank-slate Cold-vs-Warm knowledge-compounding ablation.

Covers pre-reg §10.8 obligations:
- build_ablation_repos.sh removes exactly the §7 paths (integration, tiny fixture);
- Cold KB provably empty at each problem start; Warm KB grows monotonically;
- metric math (gap_closed, Δ_k, H1/H2) on a synthetic fixture;
- the transcript auditor catches a planted violation.
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

import pytest

_REPO = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(_REPO / "src"))

from einstein.meta_loop import compounding_ablation as ca  # noqa: E402
from einstein.meta_loop.trajectory import TrajectoryPoint  # noqa: E402

# ---------------- arm isolation (one-variable invariant) ----------------


def test_arms_isolated_only_memory_loop_varies():
    assert ca.arms_isolated() is True
    cold = ca.ARM_CONFIGS[ca.Arm.COLD]
    warm = ca.ARM_CONFIGS[ca.Arm.WARM]
    # memory loop differs
    assert (cold.read_kb, cold.write_kb) == (False, False)
    assert (warm.read_kb, warm.write_kb) == (True, True)
    # everything else held equal (v1 §11: web + personas off for both)
    assert cold.allow_web == warm.allow_web is False
    assert cold.allow_personas == warm.allow_personas is False


def test_arms_isolated_breaks_if_web_differs(monkeypatch):
    broken = dict(ca.ARM_CONFIGS)
    broken[ca.Arm.WARM] = ca.ArmConfig(ca.Arm.WARM, read_kb=True, write_kb=True, allow_web=True)
    monkeypatch.setattr(ca, "ARM_CONFIGS", broken)
    assert ca.arms_isolated() is False  # web now varies → not a one-variable test


# ---------------- run KB ----------------


def test_run_kb_grows_reads_and_hashes(tmp_path):
    kb = ca.RunKB(tmp_path / "kb")
    assert kb.is_empty() and kb.lesson_count() == 0
    assert kb.state_hash() == ca.EMPTY_KB_HASH
    kb.write_lesson("csq-n10", "lesson one")
    kb.write_lesson("csq-n11", "lesson two")
    assert kb.lesson_count() == 2
    assert kb.read_lessons() == ["lesson one", "lesson two"]  # write order
    assert kb.state_hash() != ca.EMPTY_KB_HASH
    kb.wipe()
    assert kb.is_empty() and kb.state_hash() == ca.EMPTY_KB_HASH


def test_run_kb_read_cap_drops_whole_lessons(tmp_path):
    kb = ca.RunKB(tmp_path / "kb")
    kb.write_lesson("a", "x" * 10)
    kb.write_lesson("b", "y" * 10)
    kb.write_lesson("c", "z" * 10)
    # cap at 25 chars → first two fit (20), third would exceed → dropped, not truncated
    got = kb.read_lessons(max_chars=25)
    assert got == ["x" * 10, "y" * 10]


# ---------------- run matrix ----------------


def _problems(n=3):
    return [
        ca.Problem(f"p{i}", n=10 + i, sequence_index=i, reference_optimum=1.0, statement="s")
        for i in range(n)
    ]


def test_build_run_matrix_full_and_threaded():
    probs = _problems(3)
    matrix = ca.build_run_matrix(probs, [1, 2])
    assert len(matrix) == 3 * 2 * 2  # problems × arms × seeds
    # within a (seed, arm) block the problems run in sequence order (Warm threading)
    cold_seed1 = [r for r in matrix if r.seed == 1 and r.arm == ca.Arm.COLD]
    assert [r.sequence_index for r in cold_seed1] == [0, 1, 2]


# ---------------- gap_closed (DV §8) ----------------


def test_gap_closed_maximize():
    # cold-init 0.0, optimum 1.0, final 0.4 → 40% closed
    assert ca.gap_closed(0.0, 0.4, 1.0, minimize=False) == pytest.approx(0.4)


def test_gap_closed_clamped_and_degenerate():
    assert ca.gap_closed(0.0, 2.0, 1.0, minimize=False) == 1.0  # overshoot clamps to 1
    assert ca.gap_closed(0.0, -0.5, 1.0, minimize=False) == 0.0  # regress clamps to 0
    assert ca.gap_closed(1.0, 1.0, 1.0, minimize=False) == 0.0  # no gap → no room


def test_gap_closed_minimize():
    assert ca.gap_closed(2.0, 1.5, 1.0, minimize=True) == pytest.approx(0.5)


# ---------------- driver sanity invariants (§9) ----------------


def _compounding_solver(per_lesson_gain):
    def solve(problem, cfg, seed, spec):
        ci = 0.05
        frac = min(
            0.99, 0.5 + (per_lesson_gain * len(spec.accumulated_lessons) if cfg.read_kb else 0.0)
        )
        final = ci + frac * (problem.reference_optimum - ci)
        return ca.SolveResult(
            [TrajectoryPoint(0, ci), TrajectoryPoint(1, final)],
            score_coldinit=ci,
            score_final=final,
            lesson_text=f"lesson:{problem.problem_id}",
            attempted_techniques={"nelder-mead"},
        )

    return solve


def test_cold_kb_empty_each_problem_warm_grows(tmp_path):
    probs = _problems(4)
    cold = ca.run_arm_sequence(
        ca.Arm.COLD, 0, probs, _compounding_solver(0.1), ca.RunKB(tmp_path / "c")
    )
    # Cold: empty at every problem start, never reads, never persists
    assert all(r.kb_state_hash_before == ca.EMPTY_KB_HASH for r in cold)
    assert all(r.lessons_read == 0 and r.lessons_written == 0 for r in cold)

    warm = ca.run_arm_sequence(
        ca.Arm.WARM, 0, probs, _compounding_solver(0.1), ca.RunKB(tmp_path / "w")
    )
    # Warm: KB grows by one lesson per problem; reads == #lessons accumulated so far
    assert [r.lessons_read for r in warm] == [0, 1, 2, 3]
    assert all(r.lessons_written == 1 for r in warm)
    assert warm[-1].kb_state_hash_after != ca.EMPTY_KB_HASH


def test_warm_sanity_violation_when_no_lesson_persisted(tmp_path):
    def no_lesson_solver(problem, cfg, seed, spec):
        return ca.SolveResult([TrajectoryPoint(0, 0.05)], 0.05, 0.05, lesson_text=None)

    with pytest.raises(ca.SanityViolation):
        ca.run_arm_sequence(
            ca.Arm.WARM, 0, _problems(3), no_lesson_solver, ca.RunKB(tmp_path / "w")
        )


# ---------------- analysis (§9 H1/H2 on synthetic fixtures) ----------------


def _records_from(tmp_path, solver, seeds=(1, 2, 3)):
    probs = _problems(6)
    return ca.run_matrix(
        probs, list(seeds), solver, kb_root_for=lambda a, s: tmp_path / f"{a.value}-{s}"
    )


def test_analyze_supports_h1_and_h2_on_compounding_fixture(tmp_path):
    recs = [r.to_dict() for r in _records_from(tmp_path, _compounding_solver(0.08))]
    rep = ca.analyze(recs)
    assert rep.n_records == 36
    assert rep.warm_mean > rep.cold_mean
    assert rep.h1.supported is True
    assert rep.delta_slope > 0
    assert rep.h2.supported is True  # advantage grows with sequence position


def test_analyze_null_when_warm_equals_cold(tmp_path):
    # per_lesson_gain = 0 → Warm reads but gains nothing → Warm ≈ Cold
    recs = [r.to_dict() for r in _records_from(tmp_path, _compounding_solver(0.0))]
    rep = ca.analyze(recs)
    assert rep.warm_mean == pytest.approx(rep.cold_mean)
    assert rep.h1.supported is False
    assert rep.h2.supported is False  # the pre-committed honest negative


def test_delta_k_trend_ordered_by_sequence(tmp_path):
    recs = [r.to_dict() for r in _records_from(tmp_path, _compounding_solver(0.05))]
    dks = ca.delta_k_trend(recs)
    assert [d.sequence_index for d in dks] == [0, 1, 2, 3, 4, 5]
    assert all(d.delta >= 0 for d in dks)
    assert dks[-1].delta > dks[0].delta  # later advantage exceeds earlier


# ---------------- logging round-trip ----------------


def test_append_and_load_records_roundtrip(tmp_path):
    recs = _records_from(tmp_path, _compounding_solver(0.05))
    log = tmp_path / "runs.jsonl"
    for r in recs:
        ca.append_record(r, log)
    loaded = ca.load_records(log)
    assert len(loaded) == 36
    assert {r["arm"] for r in loaded} == {"cold", "warm"}
    assert all("kb_state_hash_before" in r for r in loaded)


# ---------------- transcript auditor (§10.7) ----------------


def test_auditor_passes_clean_cold_session():
    receipt = ca.audit_session(
        ["src/einstein/optimizer.py", "config/ablation_problems.yaml"],
        arm=ca.Arm.COLD,
        allow_web=False,
        own_kb_root=None,
    )
    assert receipt.passed is True and receipt.forbidden_hits == []


def test_auditor_catches_planted_violations():
    receipt = ca.audit_session(
        [
            "https://einsteinarena.com/leaderboard",  # answer key
            "https://arxiv.org/abs/1902.05438",  # web while off
            "/runs/warm-1/run-kb/lesson-000.md",  # foreign KB for a Cold session
            "src/einstein/optimizer.py",  # allowed
        ],
        arm=ca.Arm.COLD,
        allow_web=False,
        own_kb_root=None,
    )
    assert receipt.passed is False
    kinds = {h.split(":", 1)[0] for h in receipt.forbidden_hits}
    assert kinds == {"answer-key", "web", "foreign-kb"}


def test_auditor_warm_own_kb_allowed_foreign_blocked():
    own = "/runs/warm-1/run-kb"
    ok = ca.audit_session(
        [f"{own}/lesson-000.md"], arm=ca.Arm.WARM, allow_web=False, own_kb_root=own
    )
    assert ok.passed is True
    leak = ca.audit_session(
        ["/runs/warm-2/run-kb/lesson-000.md"], arm=ca.Arm.WARM, allow_web=False, own_kb_root=own
    )
    assert leak.passed is False and leak.forbidden_hits[0].startswith("foreign-kb")


# ---------------- build_ablation_repos.sh (integration, tiny git fixture) ----------------

# Knowledge rules the strip MUST remove; generic rules it MUST keep (pre-reg §7).
_REMOVED_RULES = [
    "wiki-first-lookup.md",
    "council-dispatch.md",
    "self-improvement-loop.md",
    "wall-hit-escalation.md",
    "cycle-discipline.md",
    "wiki-attribution.md",
    "ask-the-question-first.md",
    "failure-is-a-finding.md",
    "math-solving-protocol.md",
]
_KEPT_RULES = ["agent-stance.md", "triple-verify.md", "compute-router.md", "axioms.md", "README.md"]


def _git(args, cwd):
    subprocess.run(["git", *args], cwd=cwd, check=True, capture_output=True)


@pytest.fixture
def fixture_repo(tmp_path):
    """A tiny committed git repo mirroring the §7-relevant structure."""
    repo = tmp_path / "fixture"
    repo.mkdir()
    _git(["init", "-q"], repo)
    _git(["config", "user.email", "t@t"], repo)
    _git(["config", "user.name", "t"], repo)
    # knowledge layer (to be removed)
    for d in ("docs/wiki", "docs/source", "docs/agent"):
        (repo / d).mkdir(parents=True)
        (repo / d / "page.md").write_text("knowledge")
    # rules (mixed)
    (repo / ".claude/rules").mkdir(parents=True)
    for r in _REMOVED_RULES + _KEPT_RULES:
        (repo / ".claude/rules" / r).write_text("rule")
    # shared infra (to be kept)
    for d in ("src/einstein", "scripts", "tests"):
        (repo / d).mkdir(parents=True)
        (repo / d / "keep.py").write_text("# keep")
    # solution dumps (to be removed)
    (repo / "results").mkdir()
    (repo / "results" / "r.json").write_text("{}")
    (repo / "solution-best.json").write_text("{}")
    _git(["add", "-A"], repo)
    _git(["commit", "-qm", "fixture"], repo)
    return repo


def test_build_script_strips_exactly_the_frozen_paths(fixture_repo):
    script = _REPO / "scripts" / "build_ablation_repos.sh"
    out = fixture_repo / "build"
    res = subprocess.run(
        ["bash", str(script), "HEAD", str(out)],
        cwd=fixture_repo,
        capture_output=True,
        text=True,
    )
    assert res.returncode == 0, res.stderr  # self-verify must pass

    for arm in ("cold", "warm"):
        co = out / f"einstein-{arm}"
        # knowledge layer gone
        for d in ("docs/wiki", "docs/source", "docs/agent"):
            assert not (co / d).exists(), f"{arm}:{d} should be removed"
        # rules stripped to the keep-set
        for r in _REMOVED_RULES:
            assert not (co / ".claude/rules" / r).exists(), f"{arm}:{r} should be removed"
        for r in _KEPT_RULES:
            assert (co / ".claude/rules" / r).exists(), f"{arm}:{r} should be kept"
        # shared infra kept
        for d in ("src", "scripts", "tests"):
            assert (co / d).is_dir()
        # solution dumps gone
        assert not (co / "results").exists()
        assert not (co / "solution-best.json").exists()
        # manifest present
        assert (co / "AIR_GAP_MANIFEST.txt").exists()

    # Warm has an empty run KB; Cold does not
    assert (out / "einstein-warm" / "run-kb").is_dir()
    assert not (out / "einstein-cold" / "run-kb").exists()

    # cleanup worktrees registered against the fixture repo
    _git(["worktree", "remove", "--force", str(out / "einstein-cold")], fixture_repo)
    _git(["worktree", "remove", "--force", str(out / "einstein-warm")], fixture_repo)


# ---------------- counterbalanced order (pre-reg v2 §5) ----------------


def test_cyclic_order_is_a_latin_square():
    probs = _problems(6)  # sequence_index 0..5
    ids = [p.problem_id for p in sorted(probs, key=lambda p: p.sequence_index)]
    orders = [ca.cyclic_order(probs, s) for s in range(6)]
    for s, o in enumerate(orders):
        assert o == ids[s:] + ids[:s]  # rotation k=s
    for pos in range(6):  # each problem visits each position once over 6 seeds
        assert sorted(o[pos] for o in orders) == sorted(ids)


# ---------------- per-cell resume (crash-resilience, §9) ----------------


def test_run_arm_sequence_resume_skips_done_and_reuses_kb(tmp_path):
    probs = _problems(4)
    order = ca.cyclic_order(probs, 0)  # [p0,p1,p2,p3]
    kb = ca.RunKB(tmp_path / "w")
    # simulate a crash after the first 2 problems: KB already holds their lessons
    kb.write_lesson(order[0], "lesson 0")
    kb.write_lesson(order[1], "lesson 1")
    recs = ca.run_arm_sequence(
        ca.Arm.WARM,
        0,
        probs,
        _compounding_solver(0.1),
        kb,
        order=order,
        skip_done={order[0], order[1]},
    )
    assert {r.problem_id for r in recs} == {order[2], order[3]}  # only remaining solved
    assert kb.lesson_count() == 4  # KB not wiped; completed + new
    assert recs[0].lessons_read == 2  # the two already banked were read
