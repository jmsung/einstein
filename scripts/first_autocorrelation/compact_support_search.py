"""Compact-support-targeting search for P2 (Goal 1/2 of p2-record-breakthrough).

The lever (see `docs/wiki/findings/p2-record-gate-no-cheap-certificate.md` and
`dead-end-p2-compact-support-basin-floor.md`): arena #1/#2 (OrganonAgent, CHRONOS,
tied to 1e-13 at C=1.5028609073611) live in a *compact-support* basin — ~74489 of
90000 cells nonzero. Every basin we ever landed was *full*-support, because the
shared `exp(v)` parameterization can't produce exact zeros. We never *searched*
for a compact-support config; we only ever polished into full-support ones.

This script does the one untried thing: a **support-shrinking schedule** of
contiguous-window masks + **v** squared **L-BFGS multistart with cold seeds**
(NOT warm-started from our full-support basin). f = mask * v**2 keeps support
compact by construction (zeros outside the window are gradient fixed points).

Support *position* is irrelevant to C (translation-invariant), so the schedule is
1-D over window *width* only.

Compute routing (axioms A4): sequential L-BFGS per run ⇒ CPU; multistart ⇒
multiprocess across cores, one torch thread per worker (Apple Accelerate
single-thread workers — see findings/m5-max-utilization-strategy.md). GPU sits
idle on sequential L-BFGS; do not route to MPS.

Honest-EV note: two independent agents tied to 1e-13 is strong evidence the
compact-support floor is already found. Expected outcome is honest-zero; this
search exists to *confirm* that by actually trying the untried door, not to bet
on beating it.

Usage (overnight, Goal 2):
    uv run python scripts/first_autocorrelation/compact_support_search.py \
        --workers 10 --seeds-per-width 8 --time-budget 36000
"""

from __future__ import annotations

import argparse
import json
import time
from concurrent.futures import ProcessPoolExecutor, as_completed
from pathlib import Path

import numpy as np

from einstein.first_autocorrelation.optimizer import lbfgs_vsq, window_mask

RESULTS = Path("results/problem-2-first-autocorrelation")
ARENA_1 = 1.5028609073611  # OrganonAgent #1
MIN_IMPROVEMENT = 1e-8

# β-cascade: low β first (smooth, escapes the seed) → high β (tracks the true max).
DEFAULT_BETAS = [1e5, 5e5, 1e6, 5e6, 1e7, 1e8, 1e9, 1e10, 1e11, 1e12, 1e13]
# Support fractions to scan — around and including the leader's 74489/90000≈0.8277.
DEFAULT_FRACS = [0.74, 0.78, 0.81, 0.8277, 0.845, 0.87, 0.90, 0.95, 1.0]
SEED_KINDS = ["cos", "parab", "gauss", "uniform", "bimodal"]


def cold_seed(width: int, n: int, mask: np.ndarray, kind: str, rng) -> np.ndarray:
    """A diverse cold seed v0 (length n, zero outside mask) — NOT from our basin.

    Returns v0 with f0 = mask * v0**2 a positive bump of the requested shape.
    """
    t = np.linspace(0.0, 1.0, width)
    if kind == "cos":
        bump = np.sin(np.pi * t) + 0.05
    elif kind == "parab":
        bump = 4.0 * t * (1.0 - t) + 0.05
    elif kind == "gauss":
        bump = np.exp(-((t - 0.5) ** 2) / (2 * 0.18**2)) + 0.05
    elif kind == "bimodal":
        bump = (
            np.exp(-((t - 0.32) ** 2) / (2 * 0.10**2))
            + np.exp(-((t - 0.68) ** 2) / (2 * 0.10**2))
            + 0.05
        )
    else:  # uniform
        bump = rng.uniform(0.3, 1.0, width)
    bump = bump * (1.0 + 0.05 * rng.standard_normal(width))  # break symmetry
    bump = np.maximum(bump, 1e-6)
    v0 = np.zeros(n, dtype=np.float64)
    v0[np.flatnonzero(mask)] = np.sqrt(bump)
    return v0


def run_one(args: dict) -> dict:
    """One (width, seed) optimization. Top-level for ProcessPoolExecutor pickling."""
    import torch

    torch.set_num_threads(1)  # one BLAS thread per worker; parallelism is across tasks

    n, width, kind, seed = args["n"], args["width"], args["kind"], args["seed"]
    rng = np.random.default_rng(seed)
    mask = window_mask(n, width)
    v0 = cold_seed(width, n, mask, kind, rng)
    f_opt, c_opt = lbfgs_vsq(
        v0,
        args["betas"],
        mask=mask,
        max_iter=args["max_iter"],
        history_size=args["history_size"],
    )
    support = int(np.count_nonzero(f_opt > 0))
    return {
        "width": width,
        "kind": kind,
        "seed": seed,
        "score": c_opt,
        "support": support,
        "f": f_opt,
    }


def save_sol(f: np.ndarray, c: float, tag: str) -> Path:
    RESULTS.mkdir(parents=True, exist_ok=True)
    path = RESULTS / f"compact-{tag}-{c:.12f}.json"
    support = int(np.count_nonzero(f > 0))
    with open(path, "w") as fh:
        json.dump(
            {"values": f.tolist(), "score": c, "n": len(f), "support": support, "tag": tag},
            fh,
        )
    return path


def triple_verify_best(f: np.ndarray) -> tuple[bool, str, float]:
    """Run the project's 3-way verifier on the best f. Returns (passed, reason, max_delta)."""
    from einstein.triple_verify import core

    r = core.verify({"values": f.tolist()}, core.get_verifier(2))
    nums = [r.fast, r.exact, r.cross]
    delta = max(abs(a - b) for i, a in enumerate(nums) for b in nums[i + 1 :])
    return r.passed, r.reason, delta


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--n", type=int, default=90000)
    ap.add_argument("--seeds-per-width", type=int, default=4)
    ap.add_argument("--workers", type=int, default=8)
    ap.add_argument("--max-iter", type=int, default=3000)
    ap.add_argument("--history-size", type=int, default=300)
    ap.add_argument("--time-budget", type=float, default=18000.0, help="seconds")
    ap.add_argument("--fracs", type=float, nargs="*", default=DEFAULT_FRACS)
    ap.add_argument("--betas", type=float, nargs="*", default=DEFAULT_BETAS)
    args = ap.parse_args()

    n = args.n
    widths = sorted({max(2, int(round(fr * n))) for fr in args.fracs})
    tasks = [
        {
            "n": n,
            "width": w,
            "kind": SEED_KINDS[s % len(SEED_KINDS)],
            "seed": 1000 * wi + s,
            "betas": list(args.betas),
            "max_iter": args.max_iter,
            "history_size": args.history_size,
        }
        for wi, w in enumerate(widths)
        for s in range(args.seeds_per_width)
    ]

    target = ARENA_1 - MIN_IMPROVEMENT
    print(f"n={n}  widths={widths}")
    print(f"arena #1 = {ARENA_1:.13f}   target < {target:.13f}")
    print(
        f"{len(tasks)} tasks ({len(widths)} widths × {args.seeds_per_width} seeds), "
        f"{args.workers} workers, budget {args.time_budget / 3600:.1f}h\n",
        flush=True,
    )

    t0 = time.time()
    best = {"score": float("inf"), "f": None}
    deadline = t0 + args.time_budget

    with ProcessPoolExecutor(max_workers=args.workers) as ex:
        futures = {ex.submit(run_one, t): t for t in tasks}
        done = 0
        for fut in as_completed(futures):
            done += 1
            r = fut.result()
            elapsed = time.time() - t0
            marker = ""
            if r["score"] < best["score"]:
                best = r
                save_sol(r["f"], r["score"], f"w{r['width']}-{r['kind']}")
                marker = "  <<< BEST"
                if r["score"] < target:
                    marker += "  *** BEATS ARENA #1 ***"
            print(
                f"[{done}/{len(tasks)} {elapsed / 60:5.1f}m] "
                f"w={r['width']} {r['kind']:>7} supp={r['support']:6d} "
                f"C={r['score']:.13f}{marker}",
                flush=True,
            )
            if time.time() > deadline:
                print("\n[time budget reached — cancelling pending tasks]", flush=True)
                for f2 in futures:
                    f2.cancel()
                break

    print(f"\n{'=' * 64}")
    print(f"best C = {best['score']:.16f}  (support {np.count_nonzero(best['f'] > 0)})")
    print(f"arena #1 = {ARENA_1:.16f}   delta = {ARENA_1 - best['score']:+.3e}")
    beats = best["score"] < target
    print(f"beats arena #1 by ≥minImprovement: {'YES' if beats else 'NO'}")

    if best["f"] is not None:
        passed, reason, delta = triple_verify_best(best["f"])
        print(f"triple-verify: passed={passed}  max_pairwise_delta={delta:.2e}  ({reason})")
        save_sol(best["f"], best["score"], "FINAL")
    print(f"total time: {(time.time() - t0) / 60:.1f} min")


if __name__ == "__main__":
    main()
