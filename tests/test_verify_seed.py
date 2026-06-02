"""Tests for scripts/verify_seed.py — the rank-current dispatch emitter.

One row per wired problem in EXPECTED (pinned rank-current basin score). The
parametrization runs only over ids present in BOTH the script's SPECS registry
and EXPECTED, so each manifest-coverage-sprint goal adds its row here.

Asserts, per wired problem:
  1. score_seed() reproduces the pinned rank-current score (deterministic).
  2. main() writes a result file the dispatch json_score_payload parser accepts.
  3. The manifest entry resolves to `verify_seed` and round-trips through dispatch.
"""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest

_REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(_REPO / "src"))

from einstein import optimizer_dispatch as od  # noqa: E402

# Load scripts/verify_seed.py as a module (scripts/ is not a package).
_VS_PATH = _REPO / "scripts" / "verify_seed.py"
_spec = importlib.util.spec_from_file_location("verify_seed", _VS_PATH)
verify_seed = importlib.util.module_from_spec(_spec)
sys.modules["verify_seed"] = verify_seed  # needed so the frozen dataclass resolves
_spec.loader.exec_module(verify_seed)  # type: ignore[union-attr]


# Pinned rank-current basin scores. abs tol 1e-9 — re-scoring is deterministic.
EXPECTED: dict[int, float] = {
    2: 1.5028628585991939,
    4: 1.4525211550468840,
}

WIRED = sorted(set(EXPECTED) & set(verify_seed.SPECS))


@pytest.mark.parametrize("pid", WIRED)
def test_score_seed_reproduces_rank_current(pid):
    score, seed, spec = verify_seed.score_seed(pid)
    assert score == pytest.approx(
        EXPECTED[pid], abs=1e-9
    ), f"P{pid} ({spec.slug}) drifted: {score!r} vs pinned {EXPECTED[pid]!r}"
    assert isinstance(seed, dict) and seed, "seed must be a non-empty dict"


@pytest.mark.parametrize("pid", WIRED)
def test_emitter_writes_parseable_result(pid, tmp_path):
    out = tmp_path / f"p{pid}.json"
    rc = verify_seed.main(["--problem-id", str(pid), "--output", str(out)])
    assert rc == 0
    score, payload, err = od._parse_result(out, "json_score_payload")
    assert err is None, f"P{pid} result unparseable: {err}"
    assert score == pytest.approx(EXPECTED[pid], abs=1e-9)
    assert isinstance(payload, dict) and payload


@pytest.mark.parametrize("pid", WIRED)
def test_manifest_entry_resolves_to_verify_seed(pid):
    manifest = od.load_manifest()
    entry = manifest.get(pid)
    assert entry is not None, f"P{pid} missing from manifest"
    r = od.dispatch(pid, dry_run=True)
    assert r.optimizer == "verify_seed", f"P{pid} default optimizer is {r.optimizer!r}"
    opt = entry["optimizers"]["verify_seed"]
    assert opt["result_parser"] == "json_score_payload"
    assert opt["cli_args"] == ["--problem-id", str(pid)]
