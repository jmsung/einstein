"""meta_loop.sandbox — Goal 3 read-only validator for proposed tools.

`validate_proposed_tool(path)` runs three checks on a
`scripts/proposed/<tool>.py` draft:

1. **ruff check** — the repo's lint config.
2. **import in subprocess** — catches `SyntaxError` and import-time
   errors without polluting the validator's `sys.modules`.
3. **colocated pytest** — if `tests/proposed/test_<tool>.py` exists, run
   it. Skip if absent (drafts may be test-less initially).

CRUCIAL: this never dispatches the tool against a real problem. The
validator is pure static + import + unit-test checks. A draft that passes
the validator still has to clear the shadow A/B + promotion gate before
the strategy_picker ever sees it.

Subprocess isolation rationale: Ning et al.'s code-as-harness survey
calls out "transactional shared program state" as a hard requirement —
in-process import of an unverified module could break the validator
itself, not just fail it. Subprocess is the hard boundary.

Output format: `ValidationReport` serializes to JSON; the shadow harness
writes it next to the proposal at `mb/proposals/pending/<id>/validation.json`.
"""

from __future__ import annotations

import json
import subprocess
import sys
from dataclasses import asdict, dataclass, field
from pathlib import Path

# ---------------- subprocess runner contract ----------------


@dataclass(frozen=True)
class _SubprocResult:
    ok: bool
    stdout: str
    stderr: str
    returncode: int


def _run(args: list[str], *, cwd: Path | None = None, timeout: int = 30) -> _SubprocResult:
    """Default subprocess runner — tests inject a fake via `runner=...`."""
    try:
        proc = subprocess.run(
            args,
            cwd=cwd,
            capture_output=True,
            text=True,
            timeout=timeout,
            check=False,
        )
    except (subprocess.TimeoutExpired, FileNotFoundError) as e:
        return _SubprocResult(ok=False, stdout="", stderr=str(e), returncode=-1)
    return _SubprocResult(
        ok=proc.returncode == 0,
        stdout=proc.stdout,
        stderr=proc.stderr,
        returncode=proc.returncode,
    )


SubprocRunner = type(_run)
"""Callable[[list[str], Path|None, int], _SubprocResult]."""


# ---------------- ValidationReport ----------------


@dataclass
class StepResult:
    """One validator step's outcome."""

    name: str  # "ruff" | "import" | "pytest"
    ok: bool
    skipped: bool = False
    stdout: str = ""
    stderr: str = ""
    returncode: int = 0


@dataclass
class ValidationReport:
    """Result of `validate_proposed_tool`.

    `passed` is True iff every non-skipped step passed. JSON-serializable
    via `to_dict()` for the proposal audit trail.
    """

    target_path: str
    steps: list[StepResult] = field(default_factory=list)

    @property
    def passed(self) -> bool:
        return all(s.ok or s.skipped for s in self.steps)

    def to_dict(self) -> dict:
        return {
            "target_path": self.target_path,
            "passed": self.passed,
            "steps": [asdict(s) for s in self.steps],
        }

    def write_json(self, path: Path) -> Path:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(self.to_dict(), indent=2) + "\n")
        return path


# ---------------- validator ----------------


def _check_ruff(target: Path, runner) -> StepResult:
    res = runner(
        ["uv", "run", "ruff", "check", str(target)],
        cwd=None,
        timeout=60,
    )
    return StepResult(
        name="ruff",
        ok=res.ok,
        stdout=res.stdout,
        stderr=res.stderr,
        returncode=res.returncode,
    )


def _check_import(target: Path, runner) -> StepResult:
    """Import the file as a fresh module in a subprocess.

    Uses `importlib.util.spec_from_file_location` so we don't have to
    munge `sys.path` for the validator caller. Any side-effect of
    import-time code (e.g. global registration) stays inside the
    subprocess and dies with it.
    """
    code = (
        "import importlib.util, sys\n"
        f"spec = importlib.util.spec_from_file_location('proposed_tool', r'{target}')\n"
        "if spec is None or spec.loader is None:\n"
        "    raise RuntimeError('spec_from_file_location returned None')\n"
        "mod = importlib.util.module_from_spec(spec)\n"
        "sys.modules['proposed_tool'] = mod\n"
        "spec.loader.exec_module(mod)\n"
    )
    res = runner(
        [sys.executable, "-c", code],
        cwd=None,
        timeout=30,
    )
    return StepResult(
        name="import",
        ok=res.ok,
        stdout=res.stdout,
        stderr=res.stderr,
        returncode=res.returncode,
    )


def _check_pytest(target: Path, repo_root: Path, runner) -> StepResult:
    """Run `tests/proposed/test_<tool>.py` if it exists; skip otherwise."""
    slug = target.stem
    test_path = repo_root / "tests" / "proposed" / f"test_{slug}.py"
    if not test_path.is_file():
        return StepResult(name="pytest", ok=True, skipped=True)
    res = runner(
        ["uv", "run", "pytest", str(test_path), "-x", "-q"],
        cwd=repo_root,
        timeout=120,
    )
    return StepResult(
        name="pytest",
        ok=res.ok,
        stdout=res.stdout,
        stderr=res.stderr,
        returncode=res.returncode,
    )


def validate_proposed_tool(
    target: Path,
    *,
    repo_root: Path | None = None,
    runner=None,
) -> ValidationReport:
    """Run ruff + import + colocated pytest on the proposed tool.

    Args:
        target: absolute path to the proposed tool, e.g.
            `<repo>/scripts/proposed/<slug>.py`. Must exist.
        repo_root: repo root for the colocated test lookup. Defaults to
            two parents up from `target` (i.e. `<repo>/scripts/proposed/`
            → `<repo>`).
        runner: subprocess wrapper, injectable for tests. Same signature
            as `_run` above.

    Never dispatches the tool against a live problem. The validator
    deliberately stays inside the static/import/unit-test envelope.
    """
    if not target.is_file():
        raise FileNotFoundError(f"target_path={target!r} not found")
    r = runner or _run
    root = repo_root or target.resolve().parents[2]
    report = ValidationReport(target_path=str(target))
    report.steps.append(_check_ruff(target, r))
    report.steps.append(_check_import(target, r))
    report.steps.append(_check_pytest(target, root, r))
    return report


__all__ = [
    "StepResult",
    "ValidationReport",
    "validate_proposed_tool",
]
