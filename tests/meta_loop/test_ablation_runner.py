"""Tests for the production solve_fn (Goal 2) — headless claude fully mocked."""

from __future__ import annotations

import json
import sys
from dataclasses import dataclass
from pathlib import Path

import numpy as np

_REPO = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(_REPO / "src"))

from einstein.ablation_packing import evaluator as ev  # noqa: E402
from einstein.meta_loop import ablation_runner as ar  # noqa: E402
from einstein.meta_loop import compounding_ablation as ca  # noqa: E402


@dataclass
class FakeResult:
    ok: bool = True
    error_kind: str = ""
    cost_usd: float | None = 0.42
    input_tokens: int | None = 1000
    output_tokens: int | None = 500


def _problem(n=4):
    return ca.Problem(
        f"csq-n{n}", n=n, sequence_index=0, reference_optimum=0.25, statement="pack circles"
    )


def _spec(problem, arm, lessons=()):
    return (
        ca.build_session_spec(problem, arm, 1, run_kb=None)
        if not lessons
        else ca.SessionSpec(
            problem_id=problem.problem_id,
            arm=arm,
            seed=1,
            statement=problem.statement,
            allow_web=False,
            allow_personas=False,
            run_kb_readable=True,
            run_kb_path="x",
            accumulated_lessons=tuple(lessons),
        )
    )


def _checkout(tmp_path):
    for arm in ("cold", "warm"):
        (tmp_path / f"einstein-{arm}").mkdir(parents=True)
    return tmp_path


def _fake_run_writing(centers, lesson="did slsqp", techniques=("slsqp",), extra=None):
    """A fake headless_run that simulates the agent writing ablation_result.json."""

    def run(prompt, **kw):
        cwd = Path(kw["cwd"])
        obj = {
            "centers": [[float(x), float(y)] for x, y in centers],
            "lesson": lesson,
            "techniques": list(techniques),
        }
        if extra:
            obj.update(extra)
        (cwd / ar.RESULT_FILENAME).write_text(json.dumps(obj))
        run.last_prompt = prompt
        run.last_kw = kw
        return FakeResult()

    return run


# ---------------- prompt + tools ----------------


def test_prompt_embeds_cold_init_and_tools_have_no_web(tmp_path):
    root = _checkout(tmp_path)
    grid = ev.cold_init(4, ar._init_seed(4, 1))
    fake = _fake_run_writing(grid)
    solve = ar.make_solve_fn(root, headless_run=fake)
    solve(_problem(4), ca.ARM_CONFIGS[ca.Arm.COLD], 1, _spec(_problem(4), ca.Arm.COLD))
    # air-gap: no web/retrieval tool in the allow-list
    assert "WebSearch" not in ar.ALLOWED_TOOLS and "WebFetch" not in ar.ALLOWED_TOOLS
    assert "Task" not in ar.ALLOWED_TOOLS
    assert fake.last_kw["allowed_tools"] == ar.ALLOWED_TOOLS
    assert fake.last_kw["cwd"] == root / "einstein-cold"
    assert "starting configuration" in fake.last_prompt


def test_cold_prompt_has_no_lessons_warm_does(tmp_path):
    root = _checkout(tmp_path)
    p = _problem(4)
    grid = ev.cold_init(4, ar._init_seed(4, 1))

    cold_fake = _fake_run_writing(grid)
    ar.make_solve_fn(root, headless_run=cold_fake)(
        p, ca.ARM_CONFIGS[ca.Arm.COLD], 1, _spec(p, ca.Arm.COLD)
    )
    assert "Lessons you wrote" not in cold_fake.last_prompt

    warm_fake = _fake_run_writing(grid)
    ar.make_solve_fn(root, headless_run=warm_fake)(
        p,
        ca.ARM_CONFIGS[ca.Arm.WARM],
        1,
        _spec(p, ca.Arm.WARM, lessons=["use SLSQP r-as-variable"]),
    )
    assert "Lessons you wrote" in warm_fake.last_prompt
    assert "SLSQP r-as-variable" in warm_fake.last_prompt


# ---------------- harness-side scoring (agent cannot inflate) ----------------


def test_score_is_harness_computed_not_agent_reported(tmp_path):
    root = _checkout(tmp_path)
    p = _problem(4)
    grid = np.array([[0.25, 0.25], [0.25, 0.75], [0.75, 0.25], [0.75, 0.75]])  # true r = 0.25
    # agent ALSO writes a bogus inflated self-report; the runner must ignore it
    fake = _fake_run_writing(grid, extra={"score": 0.99, "radius": 0.99})
    res = ar.make_solve_fn(root, headless_run=fake)(
        p, ca.ARM_CONFIGS[ca.Arm.COLD], 1, _spec(p, ca.Arm.COLD)
    )
    assert res.score_final == 0.25  # the real radius, not 0.99
    assert res.score_final != 0.99


def test_missing_result_scores_at_cold_baseline(tmp_path):
    root = _checkout(tmp_path)
    p = _problem(4)

    def run_no_write(prompt, **kw):
        return FakeResult(ok=False, error_kind="timeout")

    res = ar.make_solve_fn(root, headless_run=run_no_write)(
        p, ca.ARM_CONFIGS[ca.Arm.COLD], 1, _spec(p, ca.Arm.COLD)
    )
    init = ev.cold_init(4, ar._init_seed(4, 1))
    assert res.score_final == res.score_coldinit == ev.common_radius(init)


def test_wrong_shape_result_scores_at_cold_baseline(tmp_path):
    root = _checkout(tmp_path)
    p = _problem(4)
    fake = _fake_run_writing(np.array([[0.5, 0.5], [0.6, 0.6]]))  # 2 centers, n=4 → rejected
    res = ar.make_solve_fn(root, headless_run=fake)(
        p, ca.ARM_CONFIGS[ca.Arm.COLD], 1, _spec(p, ca.Arm.COLD)
    )
    assert res.score_final == res.score_coldinit


# ---------------- warm lesson fallback + telemetry ----------------


def test_warm_gets_fallback_lesson_when_none_emitted(tmp_path):
    root = _checkout(tmp_path)
    p = _problem(4)
    grid = ev.cold_init(4, ar._init_seed(4, 1))
    fake = _fake_run_writing(grid, lesson=None)  # agent emits no lesson
    res = ar.make_solve_fn(root, headless_run=fake)(
        p, ca.ARM_CONFIGS[ca.Arm.WARM], 1, _spec(p, ca.Arm.WARM)
    )
    assert res.lesson_text  # non-empty so the Warm sanity check passes


def test_telemetry_captures_cost_and_scores(tmp_path):
    root = _checkout(tmp_path)
    p = _problem(4)
    grid = ev.cold_init(4, ar._init_seed(4, 1))
    tel: list = []
    fake = _fake_run_writing(grid)
    ar.make_solve_fn(root, headless_run=fake, telemetry=tel)(
        p, ca.ARM_CONFIGS[ca.Arm.COLD], 1, _spec(p, ca.Arm.COLD)
    )
    assert len(tel) == 1
    assert tel[0]["cost_usd"] == 0.42 and tel[0]["arm"] == "cold"
    assert "score_final" in tel[0]


def test_cold_init_shared_across_arms_for_same_seed(tmp_path):
    # paired design: same (problem, seed) → identical cold baseline both arms
    p = _problem(10)
    a = ev.cold_init(p.n, ar._init_seed(p.n, 2))
    b = ev.cold_init(p.n, ar._init_seed(p.n, 2))
    assert np.array_equal(a, b)
