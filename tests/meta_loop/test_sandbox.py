"""Tests for src/einstein/meta_loop/sandbox.py — Goal 3 validator."""

from __future__ import annotations

import json
import sys
from pathlib import Path

import pytest

_REPO = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(_REPO / "src"))

from einstein.meta_loop.sandbox import (  # noqa: E402
    StepResult,
    ValidationReport,
    _SubprocResult,
    validate_proposed_tool,
)

# ---------------- fake runner ----------------


def _make_runner(responses: dict[str, _SubprocResult]):
    """Return a fake subprocess runner that dispatches on the leading args.

    The key in `responses` matches the first arg (e.g. "ruff", "python",
    "pytest"). The runner records calls in `recorded` for assertions.
    """
    recorded = []

    def runner(args, *, cwd=None, timeout=30):
        recorded.append({"args": args, "cwd": cwd, "timeout": timeout})
        # ruff: args = ['uv','run','ruff','check', ...]
        # import: args = [sys.executable, '-c', ...]
        # pytest: args = ['uv','run','pytest', ...]
        if "ruff" in args:
            return responses.get("ruff", _ok())
        if "pytest" in args:
            return responses.get("pytest", _ok())
        if any("-c" == a for a in args):
            return responses.get("import", _ok())
        raise AssertionError(f"unhandled fake call: {args}")

    return runner, recorded


def _ok(stdout: str = "ok\n") -> _SubprocResult:
    return _SubprocResult(ok=True, stdout=stdout, stderr="", returncode=0)


def _fail(stderr: str = "boom\n", returncode: int = 1) -> _SubprocResult:
    return _SubprocResult(ok=False, stdout="", stderr=stderr, returncode=returncode)


def _write_target(tmp_path: Path, body: str = "print('ok')\n") -> Path:
    proposed = tmp_path / "scripts" / "proposed"
    proposed.mkdir(parents=True)
    target = proposed / "mpmath-ulp-polish.py"
    target.write_text(body)
    return target


# ---------------- happy path ----------------


def test_validate_all_three_steps_run_and_pass(tmp_path: Path) -> None:
    target = _write_target(tmp_path)
    runner, recorded = _make_runner({})  # all default to _ok
    # Pytest will be skipped (no colocated test file)
    rep = validate_proposed_tool(target, repo_root=tmp_path, runner=runner)
    assert rep.passed
    names = [s.name for s in rep.steps]
    assert names == ["ruff", "import", "pytest"]
    # pytest skipped because no colocated test file
    pytest_step = next(s for s in rep.steps if s.name == "pytest")
    assert pytest_step.skipped is True
    # ruff + import actually ran
    assert sum(1 for r in recorded if "ruff" in r["args"]) == 1
    assert sum(1 for r in recorded if any("-c" == a for a in r["args"])) == 1


def test_validate_picks_up_colocated_test(tmp_path: Path) -> None:
    target = _write_target(tmp_path)
    tests_proposed = tmp_path / "tests" / "proposed"
    tests_proposed.mkdir(parents=True)
    (tests_proposed / "test_mpmath-ulp-polish.py").write_text("def test_x(): pass\n")
    runner, recorded = _make_runner({})
    rep = validate_proposed_tool(target, repo_root=tmp_path, runner=runner)
    pytest_step = next(s for s in rep.steps if s.name == "pytest")
    assert not pytest_step.skipped
    # pytest was actually invoked
    assert any("pytest" in r["args"] for r in recorded)


# ---------------- failure cases ----------------


def test_ruff_failure_marks_report_not_passed(tmp_path: Path) -> None:
    target = _write_target(tmp_path)
    runner, _ = _make_runner({"ruff": _fail("E501 line too long\n")})
    rep = validate_proposed_tool(target, repo_root=tmp_path, runner=runner)
    assert not rep.passed
    ruff_step = next(s for s in rep.steps if s.name == "ruff")
    assert not ruff_step.ok
    assert "E501" in ruff_step.stderr


def test_import_failure_marks_report_not_passed(tmp_path: Path) -> None:
    target = _write_target(tmp_path, body="def def\n")  # syntax error
    runner, _ = _make_runner({"import": _fail("SyntaxError: invalid syntax\n")})
    rep = validate_proposed_tool(target, repo_root=tmp_path, runner=runner)
    assert not rep.passed
    import_step = next(s for s in rep.steps if s.name == "import")
    assert "SyntaxError" in import_step.stderr


def test_pytest_failure_marks_report_not_passed(tmp_path: Path) -> None:
    target = _write_target(tmp_path)
    tests_proposed = tmp_path / "tests" / "proposed"
    tests_proposed.mkdir(parents=True)
    (tests_proposed / "test_mpmath-ulp-polish.py").write_text("def test_x(): assert False\n")
    runner, _ = _make_runner({"pytest": _fail("1 failed in 0.01s\n")})
    rep = validate_proposed_tool(target, repo_root=tmp_path, runner=runner)
    assert not rep.passed
    pytest_step = next(s for s in rep.steps if s.name == "pytest")
    assert not pytest_step.ok


def test_missing_target_raises(tmp_path: Path) -> None:
    with pytest.raises(FileNotFoundError):
        validate_proposed_tool(tmp_path / "nope.py", repo_root=tmp_path, runner=_make_runner({})[0])


# ---------------- never dispatches ----------------


def test_validator_never_calls_autonomous_loop(tmp_path: Path) -> None:
    """The validator must not invoke autonomous_loop or the optimizer manifest."""
    target = _write_target(tmp_path)
    runner, recorded = _make_runner({})
    validate_proposed_tool(target, repo_root=tmp_path, runner=runner)
    for call in recorded:
        joined = " ".join(call["args"])
        assert "autonomous_loop" not in joined
        assert "optimizer" not in joined or "ruff" in joined or "pytest" in joined


# ---------------- JSON serialization ----------------


def test_validation_report_to_dict_round_trip(tmp_path: Path) -> None:
    target = _write_target(tmp_path)
    runner, _ = _make_runner({})
    rep = validate_proposed_tool(target, repo_root=tmp_path, runner=runner)
    d = rep.to_dict()
    assert d["passed"] is True
    assert d["target_path"] == str(target)
    assert isinstance(d["steps"], list)
    # Each step has the expected fields
    for s in d["steps"]:
        assert "name" in s
        assert "ok" in s
        assert "skipped" in s


def test_validation_report_write_json(tmp_path: Path) -> None:
    target = _write_target(tmp_path)
    runner, _ = _make_runner({})
    rep = validate_proposed_tool(target, repo_root=tmp_path, runner=runner)
    out = tmp_path / "mb" / "proposals" / "pending" / "x" / "validation.json"
    written = rep.write_json(out)
    assert written == out
    loaded = json.loads(out.read_text())
    assert loaded["passed"] is True


# ---------------- step result equality / dataclass shape ----------------


def test_step_result_defaults() -> None:
    s = StepResult(name="ruff", ok=True)
    assert s.skipped is False
    assert s.returncode == 0


def test_validation_report_passed_skipped_counts_as_ok() -> None:
    rep = ValidationReport(
        target_path="x.py",
        steps=[StepResult(name="ruff", ok=True), StepResult(name="pytest", ok=False, skipped=True)],
    )
    assert rep.passed
