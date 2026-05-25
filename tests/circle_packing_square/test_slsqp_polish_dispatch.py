"""Tests for the P14 strict-tol manifest wire-fix (feat/p14-wire-slsqp).

Covers:
- Manifest resolves the new `slsqp_polish` entry as the P14 default.
- The seed file (`scripts/circle_packing_square/seeds/p14_canonical.json`) is
  present and well-formed — that's the in-repo replacement for the missing
  `results-temp/p14_top.json` that broke autonomous-loop cycles 47–49.
- newton_max retains explicit-pick safety: cli_args force `--pair-gap 0`.
- End-to-end smoke: invoking the wrapper script directly produces a strict-
  verified score and a well-formed result file.

The end-to-end smoke is fast (~1s — SLSQP from a known-good warm start
converges in ~5 iterations). Triple-verify lands inside the script itself
via `evaluator.evaluate_strict()`; this test re-verifies the result file
matches that shape.
"""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

import pytest

_REPO = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(_REPO / "src"))


# ---------------- manifest contract ----------------


def test_p14_default_is_slsqp_polish():
    """Wire-fix invariant: dispatch with strategy=None picks slsqp_polish, NOT
    newton_max. This is the user-facing fix the agent's cycle-51 question asked for."""
    from einstein.optimizer_dispatch import dispatch

    result = dispatch(problem_id=14, strategy=None, dry_run=True)
    assert result.optimizer == "slsqp_polish", (
        f"expected default optimizer to be slsqp_polish (the strict-tol wire-fix); "
        f"got {result.optimizer!r}"
    )


def test_p14_slsqp_polish_explicit_resolves():
    from einstein.optimizer_dispatch import dispatch

    result = dispatch(problem_id=14, strategy="slsqp_polish", dry_run=True)
    assert result.optimizer == "slsqp_polish"


def test_p14_newton_max_still_available_but_strict():
    """newton_max is kept (not removed) but its cli_args force --pair-gap 0
    so even an explicit pick honors axiom A1."""
    from einstein.optimizer_dispatch import dispatch, load_manifest

    # Explicit pick still resolves
    result = dispatch(problem_id=14, strategy="newton_max", dry_run=True)
    assert result.optimizer == "newton_max"

    # And the cli_args force strict-tol
    manifest = load_manifest()
    p14 = manifest[14]
    newton_args = p14["optimizers"]["newton_max"]["cli_args"]
    assert "--pair-gap" in newton_args
    pair_gap_idx = newton_args.index("--pair-gap")
    assert (
        newton_args[pair_gap_idx + 1] == "0"
    ), f"newton_max --pair-gap must be '0' (strict); got {newton_args[pair_gap_idx + 1]!r}"


# ---------------- seed file ----------------


def test_seed_file_present_and_well_formed():
    """The seed is the in-repo replacement for `results-temp/p14_top.json` (which
    is gitignored and was missing in cycles 47–49). Without it, the wire-fix
    can't bootstrap."""
    seed = _REPO / "scripts" / "circle_packing_square" / "seeds" / "p14_canonical.json"
    assert seed.is_file(), f"missing canonical seed at {seed}"

    data = json.loads(seed.read_text())
    circles = data.get("circles") or data
    assert isinstance(circles, list)
    assert len(circles) == 26, f"expected 26 circles, got {len(circles)}"
    for i, c in enumerate(circles):
        assert isinstance(c, list) and len(c) == 3, f"circle {i}: expected [cx, cy, r], got {c}"
        cx, cy, r = c
        assert 0 <= cx <= 1, f"circle {i}: cx={cx} outside [0, 1]"
        assert 0 <= cy <= 1, f"circle {i}: cy={cy} outside [0, 1]"
        assert 0 < r < 1, f"circle {i}: r={r} outside (0, 1)"


# ---------------- end-to-end smoke ----------------


@pytest.mark.slow
def test_slsqp_polish_strict_verified_score(tmp_path: Path) -> None:
    """Run the wrapper script standalone with an explicit --output, verify the
    result file contains a strict-tol-safe score that round-trips through
    evaluate_strict()."""
    from einstein.circle_packing_square.evaluator import evaluate_strict

    output = tmp_path / "result.json"
    script = _REPO / "scripts" / "circle_packing_square" / "slsqp_polish.py"

    proc = subprocess.run(
        ["uv", "run", "python", str(script), "--output", str(output)],
        cwd=str(_REPO),
        capture_output=True,
        text=True,
        timeout=120,
        check=False,
    )
    assert (
        proc.returncode == 0
    ), f"slsqp_polish exited {proc.returncode}\nstdout:\n{proc.stdout}\nstderr:\n{proc.stderr}"
    assert output.is_file()

    data = json.loads(output.read_text())
    assert "score" in data and "payload" in data
    score = data["score"]
    payload = data["payload"]
    assert isinstance(score, float)
    assert "circles" in payload
    assert len(payload["circles"]) == 26

    # Round-trip strict — the score must match what evaluate_strict reports;
    # this is the closed-loop axiom-A1 check.
    strict_score = evaluate_strict(payload)
    assert (
        abs(strict_score - score) < 1e-12
    ), f"strict evaluator disagrees: file says {score}, strict says {strict_score}"
    # And the score should be at/near the known rank-2 floor.
    assert 2.6359 < score < 2.6360, f"score {score} far from known rank-2 ≈ 2.6359830849"
