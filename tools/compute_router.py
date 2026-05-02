#!/usr/bin/env python3
"""compute_router.py — recommend local-cpu / local-mps / modal for a given workload.

Usage:
    python tools/compute_router.py --workload sequential --precision f64 --hours 8 --ram 16
    python tools/compute_router.py --workload parallel-batched --precision f32 --hours 12

Reads agent/local-calibration.json (produced by local_benchmark.py) for the
machine-specific calibration constants. If calibration is missing, falls back
to conservative defaults and prints a warning.

The recommendation is based on the decision matrix in
.claude/rules/compute-router.md. This is a thin programmatic wrapper —
the source of truth is the rule file.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


CALIBRATION = Path(__file__).parent.parent / "agent" / "local-calibration.json"


def load_calibration():
    if CALIBRATION.exists():
        return json.loads(CALIBRATION.read_text())
    print(f"warning: no calibration at {CALIBRATION}; using conservative defaults",
          file=sys.stderr)
    print("        run: python tools/local_benchmark.py", file=sys.stderr)
    return {
        "cpu_multi_core": {"matmul_4096_seconds": 5.0},
        "mps": {"mps_available": True, "matmul_4096_f32_seconds": 0.5},
        "ram": {"32GB": "ok", "64GB": "ok"},
    }


def route(workload: str, precision: str, hours: float, ram_gb: float):
    """Return (recommendation, rationale)."""
    cal = load_calibration()
    rules = []
    rec = None

    # Rule 1: mpmath / sequential CPU-only paths
    if workload in ("mpmath", "sequential", "lp", "nelder-mead", "lbfgs", "slsqp"):
        if ram_gb <= 64 and precision in ("mpmath", "f64"):
            return ("local-cpu", [
                "Sequential / mpmath workload — GPU sits idle.",
                "M5 Max CPU is the right home; cost = 0.",
                "If LP becomes RAM-bound (>96GB), then Modal — but try local first.",
            ])

    # Rule 2: float32 batched parallel — local MPS shines
    if workload in ("batched", "parallel-batched", "basin-hop-pop", "cma-es"):
        if precision == "f32" and cal.get("mps", {}).get("mps_available", False):
            return ("local-mps", [
                "Batched float32 — Apple Silicon MPS is built for this.",
                "Local cost = 0; iterates fast; no Modal startup overhead.",
                f"Calibration: ~{cal['mps'].get('matmul_4096_f32_seconds', '?')}s for 4096^3 f32 matmul.",
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
                f"RAM footprint {ram_gb}GB exceeds 128GB local headroom (with overhead).",
                "Modal multi-A100 / H100 with 80-160GB GPU RAM + node RAM is the right home.",
            ])
        return ("local-cpu", [
            f"RAM footprint {ram_gb}GB fits in 128GB local; HiGHS IPM scales fine on M5.",
            "Modal would add startup overhead with no compute benefit.",
        ])

    # Rule 5: multistart with 1000+ trials, quick each
    if workload == "multistart" and hours <= 4:
        return ("local-cpu", [
            "Many short trials parallel — multiprocess Pool on M5 cores wins.",
            "Local because: zero queue time, easy to interrupt, no $/hr.",
        ])

    # Default: be honest that we don't know
    return ("ambiguous — please specify workload more precisely", [
        f"Workload class '{workload}' not recognized in the matrix.",
        "See .claude/rules/compute-router.md for the canonical decision matrix.",
        "Or run 'python -m einstein.gpu_tempering.benchmark' for a GPU-specific call.",
    ])


def main():
    p = argparse.ArgumentParser(description="Recommend compute home for a workload.")
    p.add_argument("--workload", required=True,
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
    args = p.parse_args()

    rec, rationale = route(args.workload, args.precision, args.hours, args.ram)
    print(f"\nRecommendation: {rec}\n")
    for line in rationale:
        print(f"  - {line}")
    print()
    print("See .claude/rules/compute-router.md for the full decision matrix.")
    print("See agent/local-calibration.json for machine-specific constants.")


if __name__ == "__main__":
    main()
