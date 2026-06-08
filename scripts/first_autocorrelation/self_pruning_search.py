"""Warm self-pruning support-shrinking search for P2 (Goal 2b/2c of p2-record-breakthrough).

Goal 1's cold-seed-on-fixed-window search dead-ended
(`docs/wiki/findings/dead-end-p2-cold-seed-fixed-window.md`): cold smooth-bump seeds
land +0.022 above arena #1 (can't reach even our own basin), and a pre-imposed
contiguous window is strictly worse than full support. The gap is structural.

The one open path the finding leaves is *warm self-pruning*, reconciling two
established dead-ends — pure polish can't *change* support
(`dead-end-p2-compact-support-basin-floor`) and cold seeds can't reach competitive
scores (this finding). The viable route is warm enough to be competitive AND
actively shrinking support:

  1. start from our near-converged *full-support* basin (warm),
  2. zero the smallest-|v| cells — the optimizer chooses *which*, not a contiguous
     window (this is the key difference from Goal 1),
  3. re-optimize v**2 L-BFGS with the full β-cascade, letting peak-locking set in,
  4. repeat, shrinking support toward the leaders' ~74489/90000.

Multistart over several starting basins runs across cores (one BLAS thread per
worker, axioms A4); each self-pruning chain is sequential L-BFGS ⇒ CPU, GPU idle.

Honest-EV note: two independent agents tied to 1e-13 is strong evidence the floor
is already found. Expected outcome is honest-zero; this confirms it by trying the
last untried door rather than betting on beating it.

Usage (Goal 2c, overnight):
    uv run python scripts/first_autocorrelation/self_pruning_search.py \
        --warmstarts mb/problems/2-first-autocorrelation/solutions-v2/best_1.502862793_n90000.json \
        --workers 10 --time-budget 36000
"""

from __future__ import annotations

import argparse
import json
import time
from concurrent.futures import ProcessPoolExecutor, as_completed
from pathlib import Path

import numpy as np

from einstein.first_autocorrelation.optimizer import (
    load_warmstart,
    self_pruning_search,
    upsample,
)

RESULTS = Path("results/problem-2-first-autocorrelation")
ARENA_1 = 1.5028609073611  # OrganonAgent #1
MIN_IMPROVEMENT = 1e-8
LEADER_SUPPORT = 74489  # OrganonAgent / CHRONOS compact-support nonzero count

# β-cascade: low β first (smooth) → high β (tracks the true max). Matches Goal 1.
DEFAULT_BETAS = [1e5, 5e5, 1e6, 5e6, 1e7, 1e8, 1e9, 1e10, 1e11, 1e12, 1e13]


def build_schedule(n: int, floor_support: int, steps: int) -> list[int]:
    """Support targets from just-below-full down to the leaders' support count.

    Geometric spacing — bigger cuts early (cheap, far from the floor), finer near
    the leader support where peak-locking structure matters.
    """
    lo = min(floor_support, n)
    hi = max(lo + 1, int(0.999 * n))
    fracs = np.linspace(0.0, 1.0, steps)
    targets = sorted({int(round(hi * (lo / hi) ** fr)) for fr in fracs}, reverse=True)
    return [t for t in targets if lo <= t < n]


def run_one(args: dict) -> dict:
    """One warm self-pruning chain from a single warm-start. Top-level for pickling."""
    import torch

    torch.set_num_threads(1)  # one BLAS thread per worker; parallelism is across chains

    tag = args["tag"]

    def on_level(row: dict) -> None:
        print(
            f"      [{tag:>24}] target={row['target']:6d} "
            f"supp={row['support']:6d} C={row['score']:.13f}",
            flush=True,
        )

    f_init = args["f_init"]
    best_f, best_c, trace = self_pruning_search(
        f_init,
        args["betas"],
        args["schedule"],
        max_iter=args["max_iter"],
        history_size=args["history_size"],
        on_level=on_level,
    )
    return {
        "tag": args["tag"],
        "score": best_c,
        "support": int(np.count_nonzero(best_f > 0)),
        "f": best_f,
        "trace": trace,
    }


def save_sol(f: np.ndarray, c: float, tag: str) -> Path:
    RESULTS.mkdir(parents=True, exist_ok=True)
    path = RESULTS / f"selfprune-{tag}-{c:.12f}.json"
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
    ap.add_argument(
        "--warmstarts",
        nargs="+",
        required=True,
        help="JSON solution files to warm-start chains from (full-support basins).",
    )
    ap.add_argument("--workers", type=int, default=8)
    ap.add_argument("--steps", type=int, default=12, help="support levels per chain")
    ap.add_argument("--floor-support", type=int, default=LEADER_SUPPORT)
    ap.add_argument("--max-iter", type=int, default=3000)
    ap.add_argument("--history-size", type=int, default=300)
    ap.add_argument("--time-budget", type=float, default=36000.0, help="seconds")
    ap.add_argument("--betas", type=float, nargs="*", default=DEFAULT_BETAS)
    args = ap.parse_args()

    n = args.n
    schedule = build_schedule(n, args.floor_support, args.steps)
    tasks = []
    for path in args.warmstarts:
        f = load_warmstart(path)
        if len(f) != n:
            f = upsample(f, n)
        tasks.append(
            {
                "tag": Path(path).stem[:24],
                "f_init": f,
                "schedule": schedule,
                "betas": list(args.betas),
                "max_iter": args.max_iter,
                "history_size": args.history_size,
            }
        )

    target = ARENA_1 - MIN_IMPROVEMENT
    print(f"n={n}  support schedule={schedule}")
    print(f"arena #1 = {ARENA_1:.13f}   target < {target:.13f}")
    print(
        f"{len(tasks)} warm chains, {args.workers} workers, "
        f"budget {args.time_budget / 3600:.1f}h\n",
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
                save_sol(r["f"], r["score"], r["tag"])
                marker = "  <<< BEST"
                if r["score"] < target:
                    marker += "  *** BEATS ARENA #1 ***"
            print(
                f"[{done}/{len(tasks)} {elapsed / 60:5.1f}m] "
                f"{r['tag']:>24} supp={r['support']:6d} "
                f"C={r['score']:.13f}{marker}",
                flush=True,
            )
            for row in r["trace"]:
                print(
                    f"      target={row['target']:6d} supp={row['support']:6d} "
                    f"C={row['score']:.13f}",
                    flush=True,
                )
            if time.time() > deadline:
                print("\n[time budget reached — cancelling pending tasks]", flush=True)
                for f2 in futures:
                    f2.cancel()
                break

    print(f"\n{'=' * 64}")
    if best["f"] is None:
        print("no result")
        return
    print(f"best C = {best['score']:.16f}  (support {np.count_nonzero(best['f'] > 0)})")
    print(f"arena #1 = {ARENA_1:.16f}   delta = {ARENA_1 - best['score']:+.3e}")
    beats = best["score"] < target
    print(f"beats arena #1 by ≥minImprovement: {'YES' if beats else 'NO'}")

    passed, reason, delta = triple_verify_best(best["f"])
    print(f"triple-verify: passed={passed}  max_pairwise_delta={delta:.2e}  ({reason})")
    save_sol(best["f"], best["score"], "FINAL")
    print(f"total time: {(time.time() - t0) / 60:.1f} min")


if __name__ == "__main__":
    main()
