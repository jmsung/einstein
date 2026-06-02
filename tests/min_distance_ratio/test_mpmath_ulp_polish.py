"""Tests for the P5 (Min Distance Ratio) mpmath ULP-polish adapter.

The generic engine is tested in tests/test_ulp_polish.py; here we pin the
problem-specific adapter:
- the mpmath (max/min)² reimplementation agrees with the arena float64
  evaluator on the seed (triple-verify check #2), and
- polishing the seed never *increases* the ratio and stays arena-valid.
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

_SCRIPT = _REPO / "scripts" / "min_distance_ratio" / "mpmath_ulp_polish.py"
_SEED = _REPO / "scripts" / "min_distance_ratio" / "seeds" / "best.json"


def _load_module():
    spec = importlib.util.spec_from_file_location("mdr_ulp_polish", _SCRIPT)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def _seed() -> np.ndarray:
    return np.array(json.loads(_SEED.read_text())["vectors"], dtype=np.float64)


def test_mpmath_ratio_matches_arena_evaluator():
    """Triple-verify check #2: the mpmath (max/min)² equals the arena score."""
    from einstein.min_distance_ratio.evaluator import evaluate

    mod = _load_module()
    seed = _seed()
    arena = evaluate({"vectors": seed})
    exact = float(mod._ratio_sq_mp(seed, 60))
    assert abs(exact - arena) < 1e-10


@pytest.mark.slow
def test_polish_no_increase_and_valid():
    from einstein.min_distance_ratio.evaluator import evaluate

    mod = _load_module()
    seed = _seed()
    start = evaluate({"vectors": seed})
    polished, info = mod.mpmath_ulp_polish(seed, dps=50, max_iter=2)
    # minimisation: the float64 score must not go UP
    assert info["score"] <= start + 1e-13, "polish must not increase the ratio"
    assert abs(evaluate({"vectors": polished}) - info["score"]) < 1e-10
    assert polished.shape == (16, 2)
