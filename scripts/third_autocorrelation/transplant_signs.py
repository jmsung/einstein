"""Sign-field transplant control (Hadamard, council 2026-06-10).

Calibrates whether sign topology ALONE fixes the P4 basin: impose a donor's
sign field on our magnitudes, frozen-sign optimize (f = s · v², existing
kernel), then free re-opt at full support. Prediction: the leader's sign field
on our magnitudes lands within ~5e-6 of the leader's 1.4523043 after free
re-opt. If it does, sign-field synthesis (extrapolating fragmentation past the
leader's 4705 runs) is the jump move; if it lands at our level instead,
magnitudes carry basin information too and synthesis needs both.

Usage:
    uv run python scripts/third_autocorrelation/transplant_signs.py \\
        --signs <donor.json> --magnitudes <ours.json>
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np

from einstein.third_autocorrelation.optimizer import (
    arena_c,
    frozen_sign_descent,
    lbfgs_masked,
    load_warmstart,
    neg_run_count,
)

RESULTS = Path("results/problem-4-third-autocorrelation")
ARENA_1 = 1.4523043331832
FROZEN_BETAS = [1e5, 1e6, 1e7, 1e8, 1e9, 1e10]
FREE_BETAS = [1e5, 3e5, 1e6, 3e6, 1e7, 3e7, 1e8, 1e9, 1e10, 1e11, 1e12, 1e13]


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--signs", required=True, help="donor solution (sign field source)")
    ap.add_argument("--magnitudes", required=True, help="recipient solution (|f| source)")
    ap.add_argument("--iters", type=int, default=1500)
    args = ap.parse_args()

    s_donor = load_warmstart(args.signs)
    f_ours = load_warmstart(args.magnitudes)
    if len(s_donor) != len(f_ours):
        raise SystemExit(f"length mismatch: {len(s_donor)} vs {len(f_ours)}")

    s = np.where(s_donor >= 0, 1.0, -1.0)
    v_init = np.sqrt(np.abs(f_ours))
    print(
        f"donor neg_runs={neg_run_count(s_donor)}  donor C={arena_c(s_donor):.13f}\n"
        f"recipient neg_runs={neg_run_count(f_ours)}  recipient C={arena_c(f_ours):.13f}"
    )

    f_frozen, c_frozen = frozen_sign_descent(s, v_init, FROZEN_BETAS, args.iters)
    print(f"frozen-sign:  C={c_frozen:.13f}  neg_runs={neg_run_count(f_frozen)}", flush=True)

    full_mask = np.ones(len(f_frozen), dtype=bool)
    f_free, c_free = lbfgs_masked(f_frozen, FREE_BETAS, mask=full_mask, max_iter=2000)
    print(
        f"free re-opt:  C={c_free:.13f}  neg_runs={neg_run_count(f_free)}\n"
        f"vs leader {ARENA_1:.13f}: delta {ARENA_1 - c_free:+.3e}"
    )

    RESULTS.mkdir(parents=True, exist_ok=True)
    out = RESULTS / f"transplant-{c_free:.12f}.json"
    with open(out, "w") as fh:
        json.dump(
            {
                "values": f_free.tolist(),
                "score": c_free,
                "n": len(f_free),
                "neg_runs": neg_run_count(f_free),
                "tag": "transplant",
            },
            fh,
        )
    print(f"saved {out}")


if __name__ == "__main__":
    main()
