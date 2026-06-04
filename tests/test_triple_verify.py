"""Tests for src/einstein/triple_verify/core.py — dataclasses, tolerance,
registry, and dispatcher semantics (Goal 1, skeleton)."""

from __future__ import annotations

import json
import sys
from pathlib import Path

import pytest

_REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(_REPO / "src"))

from einstein.triple_verify import core  # noqa: E402
from einstein.triple_verify.core import (  # noqa: E402
    DEFAULT_TOLERANCE,
    Tolerance,
    TripleVerifier,
    TripleVerifyResult,
    register,
    run,
    verify,
)


@pytest.fixture(autouse=True)
def _clean_registry():
    core.clear_registry()
    yield
    core.clear_registry()


# ---------------- Tolerance ----------------


def test_tolerance_identical_agree():
    assert Tolerance().agree(1.5, 1.5)


def test_tolerance_within_abs_band():
    tol = Tolerance(abs_tol=1e-10, rel_tol=0.0)
    assert tol.agree(1.0, 1.0 + 5e-11)
    assert not tol.agree(1.0, 1.0 + 5e-10)


def test_tolerance_within_rel_band():
    tol = Tolerance(abs_tol=0.0, rel_tol=1e-8)
    # 1e6 * 1e-8 = 1e-2 allowed
    assert tol.agree(1e6, 1e6 + 5e-3)
    assert not tol.agree(1e6, 1e6 + 5e-1)


def test_tolerance_nan_never_agrees():
    nan = float("nan")
    assert not Tolerance().agree(nan, nan)
    assert not Tolerance().agree(1.0, float("inf"))


def test_default_tolerance_values():
    assert DEFAULT_TOLERANCE.abs_tol == 1e-10
    assert DEFAULT_TOLERANCE.rel_tol == 1e-8


# ---------------- TripleVerifyResult.as_dict ----------------


def test_result_as_dict_roundtrip():
    r = TripleVerifyResult(
        passed=True, problem_id=19, fast=2.6, exact=2.6, cross=2.6, reason="3-way agreement"
    )
    d = r.as_dict()
    assert d["passed"] is True
    assert d["fast"] == d["exact"] == d["cross"] == 2.6
    assert d["note"] == "3-way agreement"


def test_result_as_dict_omits_missing_numbers():
    r = TripleVerifyResult(passed=False, problem_id=7, reason="not_registered")
    d = r.as_dict()
    assert d == {"passed": False, "note": "not_registered"}


# ---------------- register / registry semantics ----------------


def test_register_requires_three_scorers_or_reason():
    with pytest.raises(ValueError):
        register(99, fast=lambda s: 1.0)  # missing exact + cross, no reason


def test_register_unavailable_reason_ok():
    v = register(99, unavailable_reason="no_third_check_available")
    assert v.unavailable_reason == "no_third_check_available"
    assert core.registered_ids() == [99]


def test_register_and_get():
    register(3, fast=lambda s: 1.0, exact=lambda s: 1.0, cross=lambda s: 1.0)
    assert core.get_verifier(3).problem_id == 3
    assert core.get_verifier(404) is None


# ---------------- verify: agreement rule ----------------


def _scorers(a, b, c):
    return dict(fast=lambda s: a, exact=lambda s: b, cross=lambda s: c)


def test_verify_three_way_agreement_passes():
    v = TripleVerifier(7, **_scorers(2.5, 2.5, 2.5))
    r = verify({}, v)
    assert r.passed
    assert r.reason == "3-way agreement"


def test_verify_two_way_mismatch_fails():
    v = TripleVerifier(7, **_scorers(2.5, 2.5, 9.9))
    r = verify({}, v)
    assert not r.passed
    assert "fast/cross differ" in r.reason and "exact/cross differ" in r.reason


def test_verify_full_disagreement_fails():
    v = TripleVerifier(7, **_scorers(1.0, 2.0, 3.0))
    r = verify({}, v)
    assert not r.passed
    assert "differ" in r.reason


def test_verify_unavailable_short_circuits():
    v = TripleVerifier(7, unavailable_reason="no_third_check_available")
    r = verify({}, v)
    assert not r.passed
    assert r.reason == "no_third_check_available"
    assert r.fast is None  # scorers never ran


def test_verify_scorer_raising_is_honest_zero():
    def boom(s):
        raise RuntimeError("kaboom")

    v = TripleVerifier(7, fast=lambda s: 1.0, exact=boom, cross=lambda s: 1.0)
    r = verify({}, v)
    assert not r.passed
    assert "exact-check raised RuntimeError" in r.reason
    assert r.fast == 1.0  # the number computed before the raise is preserved


# ---------------- run: dispatcher ----------------


def test_run_not_registered():
    r = run(404, "/nonexistent.json")
    assert not r.passed
    assert r.reason == "not_registered"


def test_run_loads_and_verifies(tmp_path):
    register(7, fast=lambda s: s["x"], exact=lambda s: s["x"], cross=lambda s: s["x"])
    p = tmp_path / "sol.json"
    p.write_text(json.dumps({"x": 4.2}))
    r = run(7, p)
    assert r.passed and r.fast == 4.2


def test_run_unwraps_payload(tmp_path):
    register(7, fast=lambda s: s["x"], exact=lambda s: s["x"], cross=lambda s: s["x"])
    p = tmp_path / "sol.json"
    p.write_text(json.dumps({"score": 4.2, "payload": {"x": 4.2}}))
    r = run(7, p)
    assert r.passed and r.fast == 4.2


def test_run_missing_file_is_honest_zero():
    register(7, fast=lambda s: 1.0, exact=lambda s: 1.0, cross=lambda s: 1.0)
    r = run(7, "/definitely/not/here.json")
    assert not r.passed
    assert "solution load failed" in r.reason
