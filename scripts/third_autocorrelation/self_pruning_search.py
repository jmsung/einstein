"""Warm self-pruning support-shrinking search for P4 (js/feat/p4-warm-pruning-transfer).

P2's record operator (docs/wiki/findings/p2-warm-self-pruning-beats-record.md)
ported to the signed P4 objective. P4's honest-zero verdict predates the P2
record, so warm self-pruning is the prescribed untried operator (wall-hit
floor-claim rule).

Differences from the P2 campaign:
  1. Signed kernel f = mask·w — the masked re-opt may re-fragment signs inside
     the surviving support (the move the discrete-sign-topology obstruction
     says fixed-support descent can't make).
  2. No leader support target — the P4 leader is full-support, so the floor is
     a free hyperparameter: one chain per --floors fraction, parallel across
     cores (one BLAS thread per worker, axiom A4).
  3. Per-level sign-fragmentation diagnostic (neg_runs) — does pruning move us
     toward the leader's 4705 negative runs (ours: 823)?

Usage (Goal 2 campaign):
    uv run python scripts/third_autocorrelation/self_pruning_search.py \\
        --warmstart mb/problems/4-third-autocorrelation/solutions/solution-best.json \\
        --floors 0.95 0.9 0.8 0.65 0.5 --steps 10 --workers 5 --time-budget 36000
"""

from __future__ import annotations

import argparse
import json
import time
from concurrent.futures import ProcessPoolExecutor, as_completed
from pathlib import Path

import numpy as np

from einstein.third_autocorrelation.optimizer import (
    load_warmstart,
    neg_run_count,
    self_pruning_search,
    upsample,
)

RESULTS = Path("results/problem-4-third-autocorrelation")
ARENA_1 = 1.4523043331832  # OrganonAgent #1 (since 04-20)
MIN_IMPROVEMENT = 1e-4  # per 2026-04-08 /api/problems fetch — re-fetch live before submit

# β-cascade: P4's proven stable schedule (strategy.md) extended to 1e12 — the
# ratio-first masked surrogate keeps the LSE gap ≈ log(N)/β on a unit-scale
# quantity, so high β stays well-conditioned.
DEFAULT_BETAS = [1e4, 3e4, 1e5, 3e5, 1e6, 3e6, 1e7, 3e7, 1e8, 3e8, 1e9, 1e10, 1e11, 1e12]


def build_schedule(n: int, floor_support: int, steps: int) -> list[int]:
    """Support targets from just-below-full down to ``floor_support``, geometric."""
    lo = min(floor_support, n)
    hi = max(lo + 1, int(0.999 * n))
    fracs = np.linspace(0.0, 1.0, steps)
    targets = sorted({int(round(hi * (lo / hi) ** fr)) for fr in fracs}, reverse=True)
    return [t for t in targets if lo <= t < n]


def run_one(args: dict) -> dict:
    """One warm self-pruning chain for a single floor fraction. Top-level for pickling."""
    import torch

    torch.set_num_threads(1)  # one BLAS thread per worker; parallelism is across chains

    tag = args["tag"]

    def on_level(row: dict) -> None:
        print(
            f"      [{tag:>12}] target={row['target']:6d} supp={row['support']:6d} "
            f"C={row['score']:.13f} neg_runs={row['neg_runs']:5d}",
            flush=True,
        )

    best_f, best_c, trace = self_pruning_search(
        args["f_init"],
        args["betas"],
        args["schedule"],
        max_iter=args["max_iter"],
        history_size=args["history_size"],
        on_level=on_level,
    )
    return {
        "tag": tag,
        "score": best_c,
        "support": int(np.count_nonzero(best_f)),
        "neg_runs": neg_run_count(best_f),
        "f": best_f,
        "trace": trace,
    }


def save_sol(f: np.ndarray, c: float, tag: str) -> Path:
    RESULTS.mkdir(parents=True, exist_ok=True)
    path = RESULTS / f"selfprune-{tag}-{c:.12f}.json"
    with open(path, "w") as fh:
        json.dump(
            {
                "values": f.tolist(),
                "score": c,
                "n": len(f),
                "support": int(np.count_nonzero(f)),
                "neg_runs": neg_run_count(f),
                "tag": tag,
            },
            fh,
        )
    return path


def triple_verify_best(f: np.ndarray) -> tuple[bool, str, float]:
    """Run the project's 3-way verifier on the best f. Returns (passed, reason, max_delta)."""
    import einstein.triple_verify.problems  # noqa: F401  (registers verifiers)
    from einstein.triple_verify import core

    r = core.verify({"values": f.tolist()}, core.get_verifier(4))
    nums = [r.fast, r.exact, r.cross]
    if any(x is None for x in nums):  # a verifier was unavailable / raised
        return r.passed, f"{r.reason} (incomplete numbers: {nums})", float("inf")
    delta = max(abs(a - b) for i, a in enumerate(nums) for b in nums[i + 1 :])
    return r.passed, r.reason, delta


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--n", type=int, default=100000)
    ap.add_argument(
        "--warmstart",
        required=True,
        help="JSON solution file to warm-start from (the verified full-support basin).",
    )
    ap.add_argument(
        "--floors",
        type=float,
        nargs="+",
        default=[0.95, 0.9, 0.8, 0.65, 0.5],
        help="Floor support fractions of n — one self-pruning chain per floor.",
    )
    ap.add_argument("--workers", type=int, default=5)
    ap.add_argument("--steps", type=int, default=10, help="support levels per chain")
    ap.add_argument("--max-iter", type=int, default=2000)
    ap.add_argument("--history-size", type=int, default=200)
    ap.add_argument("--time-budget", type=float, default=36000.0, help="seconds")
    ap.add_argument("--betas", type=float, nargs="*", default=DEFAULT_BETAS)
    args = ap.parse_args()

    n = args.n
    f = load_warmstart(args.warmstart)
    if len(f) != n:
        f = upsample(f, n)
    print(f"warmstart: {args.warmstart}  n={n}  neg_runs={neg_run_count(f)}")

    tasks = []
    for floor in args.floors:
        floor_support = int(round(floor * n))
        schedule = build_schedule(n, floor_support, args.steps)
        if not schedule:
            ap.error(f"--floor {floor} yields empty support schedule at n={n}")
        tasks.append(
            {
                "tag": f"floor{floor:.2f}",
                "f_init": f,
                "schedule": schedule,
                "betas": list(args.betas),
                "max_iter": args.max_iter,
                "history_size": args.history_size,
            }
        )

    target = ARENA_1 - MIN_IMPROVEMENT
    print(
        f"arena #1 = {ARENA_1:.13f}   record needs C < {target:.13f} (minImprovement {MIN_IMPROVEMENT:g})"
    )
    print(
        f"{len(tasks)} chains (floors {args.floors}), {args.workers} workers, "
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
                f"{r['tag']:>12} supp={r['support']:6d} neg_runs={r['neg_runs']:5d} "
                f"C={r['score']:.13f}{marker}",
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
    print(
        f"best C = {best['score']:.16f}  (support {np.count_nonzero(best['f'])}, "
        f"neg_runs {neg_run_count(best['f'])})"
    )
    print(f"arena #1 = {ARENA_1:.16f}   delta = {ARENA_1 - best['score']:+.3e}")
    beats = best["score"] < target
    print(f"beats arena #1 by ≥minImprovement: {'YES' if beats else 'NO'}")

    passed, reason, delta = triple_verify_best(best["f"])
    print(f"triple-verify: passed={passed}  max_pairwise_delta={delta:.2e}  ({reason})")
    save_sol(best["f"], best["score"], "FINAL")
    print(f"total time: {(time.time() - t0) / 60:.1f} min")


if __name__ == "__main__":
    main()
