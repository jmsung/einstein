"""Tests for the P11 (Tammes) mpmath ULP-polish adapter.

The generic engine is tested in tests/test_ulp_polish.py; here we pin the
problem-specific adapter:
- the mpmath min-distance reimplementation agrees with the arena float64
  evaluator on the canonical seed (triple-verify check #2), and
- polishing the seed never regresses and stays arena-valid (axiom-A1 loop).
"""

from __future__ import annotations

import importlib.util
import json
import sys
from pathlib import Path

import numpy as np
import pytest

_REPO = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(_REPO / "src"))

_SCRIPT = _REPO / "scripts" / "tammes" / "mpmath_ulp_polish.py"
_SEED = _REPO / "scripts" / "tammes" / "seeds" / "best.json"


def _load_module():
    spec = importlib.util.spec_from_file_location("tammes_ulp_polish", _SCRIPT)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def _seed() -> np.ndarray:
    return np.array(json.loads(_SEED.read_text())["vectors"], dtype=np.float64)


def test_mpmath_min_dist_matches_arena_evaluator():
    """Triple-verify check #2: the mpmath min-distance equals the arena float64
    score on the seed (different code path, same number)."""
    from einstein.tammes.evaluator import evaluate

    mod = _load_module()
    seed = _seed()
    arena = evaluate({"vectors": seed})
    exact = float(mod._min_dist_mp(seed, 60))
    assert abs(exact - arena) < 1e-12


@pytest.mark.slow
def test_polish_no_regression_and_valid():
    from einstein.tammes.evaluator import evaluate

    mod = _load_module()
    seed = _seed()
    start = evaluate({"vectors": seed})
    polished, info = mod.mpmath_ulp_polish(seed, dps=50, max_iter=2)
    assert info["score"] >= start - 1e-15, "polish must not regress"
    # arena re-score agrees with the reported score (closed loop)
    assert abs(evaluate({"vectors": polished}) - info["score"]) < 1e-12
    assert polished.shape == (50, 3)
