#!/usr/bin/env python3
"""compute_router.py — recommend local-cpu / local-mps / modal for a given workload.

Device-aware: this repo can run on multiple Macs (the local workstation and smaller Macs
laptops, etc). Calibrations live one-per-device under
`docs/agent/calibrations/<device-key>.json`. The router fingerprints the
current device (`sysctl machdep.cpu.brand_string` + cores + memory tier),
loads the matching calibration, falls back to the most-recently-timestamped
sibling if there's no exact match, and falls back to conservative defaults
if no calibrations are present.

Usage:
    python scripts/compute_router.py --workload sequential --precision f64 --hours 8 --ram 16
    python scripts/compute_router.py --workload parallel-batched --precision f32 --hours 12
    python scripts/compute_router.py --show-device           # print device key + which calibration is used
"""
from __future__ import annotations

import argparse
import json
import platform
import re
import subprocess
import sys
from pathlib import Path

CALIBRATIONS_DIR = Path(__file__).parent.parent / "docs" / "agent" / "calibrations"


# ---------------- device fingerprint ----------------


def _sysctl(name: str) -> str | None:
    """Return sysctl value or None if not on macOS / sysctl missing."""
    try:
        out = subprocess.check_output(["sysctl", "-n", name], stderr=subprocess.DEVNULL)
        return out.decode().strip() or None
    except (FileNotFoundError, subprocess.CalledProcessError):
        return None


def _slug(s: str) -> str:
    s = s.lower()
    s = re.sub(r"[^a-z0-9]+", "-", s)
    return s.strip("-")


def _build_device_key(*, brand: str, cores: int, memory_bytes: int) -> str:
    """Compose a stable device key. Memory tier rounded to the nearest standard size."""
    mem_gb = round(memory_bytes / 1024**3)
    return f"{_slug(brand)}-{cores}c-{mem_gb}gb"


def device_key() -> str:
    """Fingerprint the current machine. Returns 'unknown-host' on non-macOS."""
    brand = _sysctl("machdep.cpu.brand_string") or platform.processor() or "unknown"
    cores_raw = _sysctl("hw.ncpu") or "0"
    mem_raw = _sysctl("hw.memsize") or "0"
    try:
        cores = int(cores_raw)
        memory_bytes = int(mem_raw)
    except ValueError:
        cores, memory_bytes = 0, 0
    if cores == 0 or memory_bytes == 0:
        return "unknown-host"
    return _build_device_key(brand=brand, cores=cores, memory_bytes=memory_bytes)


# ---------------- calibration loading ----------------


CONSERVATIVE_DEFAULTS: dict = {
    # Numbers tuned for "any Apple Silicon Mac — please run local_benchmark.py".
    # Real measurements live in docs/agent/calibrations/<device-key>.json and
    # override these on a per-device basis.
    "version": 1,
    "device": {"key": "conservative-default"},
    "cpu_multi_core": {"matmul_4096_seconds": 1.0, "gflops_estimate": 100},
    "mps": {"mps_available": True, "matmul_4096_f32_seconds": 0.1, "gflops_estimate": 1000},
    "mpmath": {"mpmath_available": True, "dps50_1k_iters_seconds": 0.05},
    "ram": {"32GB": "ok", "64GB": "unknown"},
}


def load_calibration(
    *,
    device_key_override: str | None = None,
    calibrations_dir: Path | None = None,
) -> tuple[dict, str]:
    """Load calibration for the current (or specified) device.

    Returns (calibration_dict, source) where source is one of:
      - "exact-match"          : <device-key>.json found
      - "fallback-most-recent" : no exact, used the newest sibling calibration
      - "conservative-default" : no calibrations on disk at all
    """
    key = device_key_override or device_key()
    cal_dir = calibrations_dir or CALIBRATIONS_DIR

    exact = cal_dir / f"{key}.json"
    if exact.is_file():
        return json.loads(exact.read_text()), "exact-match"

    if cal_dir.is_dir():
        siblings = sorted(cal_dir.glob("*.json"))
        if siblings:
            # Pick newest by timestamp field, falling back to file mtime
            def _ts(p: Path) -> str:
                try:
                    return json.loads(p.read_text()).get("timestamp", "")
                except (OSError, json.JSONDecodeError):
                    return ""
            siblings.sort(key=_ts, reverse=True)
            return json.loads(siblings[0].read_text()), "fallback-most-recent"

    return CONSERVATIVE_DEFAULTS.copy(), "conservative-default"


# ---------------- routing rules ----------------


def route(workload: str, precision: str, hours: float, ram_gb: float,
          cal: dict | None = None) -> tuple[str, list[str]]:
    """Return (recommendation, rationale). `cal` defaults to the auto-loaded one."""
    if cal is None:
        cal, _src = load_calibration()

    # Rule 1: mpmath / sequential CPU-only paths
    if workload in ("mpmath", "sequential", "lp", "nelder-mead", "lbfgs", "slsqp"):
        if ram_gb <= 96 and precision in ("mpmath", "f64"):
            return ("local-cpu", [
                "Sequential / mpmath workload — GPU sits idle.",
                "the local CPU is the right home; cost = 0.",
                "If LP becomes RAM-bound (>96GB), Modal — but try local first.",
            ])

    # Rule 2: float32 batched parallel — local MPS shines
    if workload in ("batched", "parallel-batched", "basin-hop-pop", "cma-es"):
        if precision == "f32" and cal.get("mps", {}).get("mps_available", False):
            mps_t = cal["mps"].get("matmul_4096_f32_seconds")
            mps_str = f"~{mps_t:.3f}s for 4096^3 f32 matmul" if mps_t else "MPS available"
            return ("local-mps", [
                "Batched float32 — Apple Silicon MPS is built for this.",
                "Local cost = 0; iterates fast; no Modal startup overhead.",
                f"Calibration: {mps_str}.",
            ])

    # Rule 3: sustained parallel float64 GPU — Modal
    if workload in ("parallel-tempering", "sa-tempering", "cma-es-large", "sdp-large"):
        if precision == "f64" and hours >= 1.0:
            return ("modal", [
                "Sustained parallel float64 — only Modal A100/H100 has the bandwidth.",
                "Local CPU would take 100x+ longer; local MPS is f32 only.",
                "Cost gate: estimate hours * $1.50-3.50/hr; require >3x speedup over local CPU.",
            ])

    # Rule 4: large LP / SDP that's RAM-bound
    if workload in ("lp-large", "sdp", "ipm-huge"):
        if ram_gb > 96:
            return ("modal", [
                f"RAM footprint {ram_gb}GB exceeds the local RAM headroom (with overhead).",
                "Modal multi-A100 / H100 with 80-160GB GPU RAM + node RAM is the right home.",
            ])
        return ("local-cpu", [
            f"RAM footprint {ram_gb}GB fits in local RAM; HiGHS IPM scales fine.",
            "Modal would add startup overhead with no compute benefit.",
        ])

    # Rule 5: multistart with 1000+ trials, quick each
    if workload == "multistart" and hours <= 4:
        return ("local-cpu", [
            "Many short trials parallel — multiprocess Pool on cores wins.",
            "Local because: zero queue time, easy to interrupt, no $/hr.",
            "the workstation gotcha: BLAS-bound workers contend on Accelerate threads — "
            "use single-thread BLAS or Python-bound work for linear MP scaling.",
        ])

    # Default: be honest that we don't know
    return ("ambiguous — please specify workload more precisely", [
        f"Workload class '{workload}' not recognized in the matrix.",
        "See .claude/rules/compute-router.md for the canonical decision matrix.",
        "Or run 'python -m einstein.gpu_tempering.benchmark' for a GPU-specific call.",
    ])


# ---------------- CLI ----------------


def main():
    p = argparse.ArgumentParser(description="Recommend compute home for a workload.")
    p.add_argument("--workload",
                   help="One of: mpmath, sequential, lp, lp-large, lbfgs, slsqp, "
                        "batched, parallel-batched, basin-hop-pop, cma-es, "
                        "parallel-tempering, sa-tempering, sdp, sdp-large, "
                        "multistart, ipm-huge")
    p.add_argument("--precision", default="f64",
                   choices=["f32", "f64", "mpmath"],
                   help="Required precision tier (default: f64)")
    p.add_argument("--hours", type=float, default=1.0,
                   help="Expected wall-clock hours (default: 1.0)")
    p.add_argument("--ram", type=float, default=16.0,
                   help="Expected RAM footprint in GB (default: 16)")
    p.add_argument("--show-device", action="store_true",
                   help="Print device key + which calibration is loaded, then exit.")
    args = p.parse_args()

    cal, source = load_calibration()
    key = device_key()
    if args.show_device:
        print(f"device-key:           {key}")
        print(f"calibration source:   {source}")
        print(f"calibration device:   {cal.get('device', {}).get('key', '?')}")
        print(f"calibration timestamp:{cal.get('timestamp', '?')}")
        return

    if not args.workload:
        p.error("--workload required (or use --show-device)")

    if source != "exact-match":
        print(f"warning: no exact calibration for device '{key}' "
              f"(using '{source}': '{cal.get('device', {}).get('key', '?')}')",
              file=sys.stderr)
        print(f"        run: python scripts/local_benchmark.py", file=sys.stderr)

    rec, rationale = route(args.workload, args.precision, args.hours, args.ram, cal=cal)
    print(f"\nRecommendation: {rec}\n")
    for line in rationale:
        print(f"  - {line}")
    print()
    print("See .claude/rules/compute-router.md for the full decision matrix.")
    print(f"See docs/agent/calibrations/{key}.json for the device calibration.")


if __name__ == "__main__":
    main()
