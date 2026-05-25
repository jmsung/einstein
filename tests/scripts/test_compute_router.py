"""Tests for scripts/compute_router.py.

The router is a pure function over (workload, precision, hours, ram, calibration).
Tests use synthetic calibrations + monkey-patched device detection so they pass
regardless of the machine running them.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import pytest

_REPO = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(_REPO / "scripts"))

import compute_router as cr  # noqa: E402


# ---------------- device fingerprint ----------------


def test_device_key_format() -> None:
    """`device_key` returns kebab-case, lowercase, alnum + hyphen only."""
    key = cr.device_key()
    assert key == key.lower()
    assert " " not in key
    assert "." not in key
    # Should encode at least brand + cores; e.g. 'apple-m5-max-18c-128gb'
    assert "-" in key


def test_device_key_includes_core_count_and_memory_tier() -> None:
    """Two machines with same CPU brand but different cores/RAM get distinct keys."""
    k_18_128 = cr._build_device_key(brand="Apple M5 Max", cores=18, memory_bytes=128 * 1024**3)
    k_12_36 = cr._build_device_key(brand="Apple M5 Pro", cores=12, memory_bytes=36 * 1024**3)
    k_18_64 = cr._build_device_key(brand="Apple M5 Max", cores=18, memory_bytes=64 * 1024**3)
    assert k_18_128 != k_12_36
    assert k_18_128 != k_18_64
    # Order-stable shape: brand → cores → memory
    assert "18c" in k_18_128 and "128gb" in k_18_128
    assert "12c" in k_12_36 and "36gb" in k_12_36


# ---------------- calibration loading ----------------


def test_load_calibration_exact_match(tmp_path: Path) -> None:
    cal_dir = tmp_path / "cal"
    cal_dir.mkdir()
    sample = {
        "version": 1, "timestamp": "2026-05-23",
        "device": {"key": "apple-m5-max-18c-128gb"},
        "cpu_multi_core": {"matmul_4096_seconds": 0.33},
        "mps": {"mps_available": True, "matmul_4096_f32_seconds": 0.009},
        "ram": {"96GB": "ok"},
    }
    (cal_dir / "apple-m5-max-18c-128gb.json").write_text(json.dumps(sample))

    cal, source = cr.load_calibration(
        device_key_override="apple-m5-max-18c-128gb",
        calibrations_dir=cal_dir,
    )
    assert source == "exact-match"
    assert cal["cpu_multi_core"]["matmul_4096_seconds"] == 0.33


def test_load_calibration_falls_back_to_most_recent(tmp_path: Path) -> None:
    """When no exact match, use the most-recently-timestamped sibling calibration."""
    cal_dir = tmp_path / "cal"
    cal_dir.mkdir()
    # An older Air calibration
    (cal_dir / "apple-m4-air-8c-16gb.json").write_text(json.dumps({
        "version": 1, "timestamp": "2026-04-01",
        "device": {"key": "apple-m4-air-8c-16gb"},
        "cpu_multi_core": {"matmul_4096_seconds": 1.2},
    }))
    # A newer M5 Max calibration — should win
    (cal_dir / "apple-m5-max-18c-128gb.json").write_text(json.dumps({
        "version": 1, "timestamp": "2026-05-23",
        "device": {"key": "apple-m5-max-18c-128gb"},
        "cpu_multi_core": {"matmul_4096_seconds": 0.33},
    }))

    cal, source = cr.load_calibration(
        device_key_override="apple-m4-pro-12c-36gb",  # neither file
        calibrations_dir=cal_dir,
    )
    assert source == "fallback-most-recent"
    assert cal["cpu_multi_core"]["matmul_4096_seconds"] == 0.33  # the newer one


def test_load_calibration_no_files_uses_conservative_defaults(tmp_path: Path) -> None:
    cal_dir = tmp_path / "cal"
    cal_dir.mkdir()
    cal, source = cr.load_calibration(
        device_key_override="apple-m5-max-18c-128gb",
        calibrations_dir=cal_dir,
    )
    assert source == "conservative-default"
    # Defaults should still be a usable dict (not None)
    assert "cpu_multi_core" in cal
    assert "mps" in cal


# ---------------- route() rules ----------------


def _m5_cal() -> dict:
    return {
        "version": 1,
        "device": {"key": "apple-m5-max-18c-128gb"},
        "cpu_multi_core": {"matmul_4096_seconds": 0.33, "gflops_estimate": 418},
        "mps": {"mps_available": True, "matmul_4096_f32_seconds": 0.009, "gflops_estimate": 14900},
        "ram": {"96GB": "ok"},
        "mpmath": {"mpmath_available": True, "dps50_1k_iters_seconds": 0.012},
    }


def test_route_mpmath_goes_local_cpu() -> None:
    rec, _rationale = cr.route("mpmath", "mpmath", hours=4.0, ram_gb=8, cal=_m5_cal())
    assert rec == "local-cpu"


def test_route_sequential_lbfgs_goes_local_cpu() -> None:
    for wl in ("sequential", "lbfgs", "slsqp", "nelder-mead", "lp"):
        rec, _ = cr.route(wl, "f64", hours=2.0, ram_gb=16, cal=_m5_cal())
        assert rec == "local-cpu", f"{wl} should route local-cpu"


def test_route_batched_f32_with_mps_goes_local_mps() -> None:
    for wl in ("batched", "parallel-batched", "basin-hop-pop", "cma-es"):
        rec, _ = cr.route(wl, "f32", hours=2.0, ram_gb=8, cal=_m5_cal())
        assert rec == "local-mps", f"{wl} (f32) should route local-mps"


def test_route_sustained_parallel_f64_goes_modal() -> None:
    rec, _ = cr.route("parallel-tempering", "f64", hours=4.0, ram_gb=8, cal=_m5_cal())
    assert rec == "modal"
    rec, _ = cr.route("sa-tempering", "f64", hours=2.0, ram_gb=8, cal=_m5_cal())
    assert rec == "modal"


def test_route_large_lp_under_local_ram_stays_local() -> None:
    rec, _ = cr.route("lp-large", "f64", hours=4.0, ram_gb=64, cal=_m5_cal())
    assert rec == "local-cpu"


def test_route_large_lp_over_local_ram_goes_modal() -> None:
    rec, _ = cr.route("lp-large", "f64", hours=4.0, ram_gb=120, cal=_m5_cal())
    assert rec == "modal"


def test_route_multistart_short_goes_local() -> None:
    rec, _ = cr.route("multistart", "f64", hours=2.0, ram_gb=8, cal=_m5_cal())
    assert rec == "local-cpu"


def test_route_unknown_workload_returns_ambiguous() -> None:
    rec, _ = cr.route("???", "f64", hours=1.0, ram_gb=8, cal=_m5_cal())
    assert "ambiguous" in rec.lower()


# ---------------- CLI argument plumbing ----------------


def test_route_no_mps_falls_through_batched_rule() -> None:
    """When MPS isn't available, batched f32 shouldn't route to local-mps."""
    cal = _m5_cal()
    cal["mps"] = {"mps_available": False}
    rec, _ = cr.route("batched", "f32", hours=2.0, ram_gb=8, cal=cal)
    # Should NOT be local-mps; can be ambiguous or some non-mps fallback
    assert rec != "local-mps"
