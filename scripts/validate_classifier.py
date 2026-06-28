"""Validation test for JSAgent claim #6: the trajectory classifier labels each
problem correctly (improving / solved-at-floor / stuck / unknown).

Not an A/B — an accuracy test against the documented spec (trajectory.classify):
  1. certificate present            -> SOLVED_AT_FLOOR (overrides everything)
  2. recent strict gain (≤ window)  -> IMPROVING
  3. open headroom (>0), no gain    -> STUCK
  4. otherwise                      -> UNKNOWN

We enumerate labeled scenarios covering all four classes plus the hard cases
(precedence, minimize vs maximize, the window boundary, empty trajectory) and
report accuracy. A correct classifier scores 100%; anything less is a real bug.

Run: uv run python scripts/validate_classifier.py
"""

from __future__ import annotations

import json
from pathlib import Path

from einstein.meta_loop.trajectory import Classification as C
from einstein.meta_loop.trajectory import TrajectoryPoint, classify


def _traj(scores):
    return [TrajectoryPoint(cycle_id=i, best_score=s) for i, s in enumerate(scores)]


# (name, scores, headroom, certificate, minimize, expected)
CASES = [
    # --- SOLVED_AT_FLOOR: a real certificate overrides everything ---
    ("cert+flat", [0.5, 0.5, 0.5], 0.1, "lp-dual-bound", True, C.SOLVED_AT_FLOOR),
    ("cert+still-improving (precedence)", [0.9, 0.7, 0.5], 0.1, "sdp-cert", True, C.SOLVED_AT_FLOOR),
    ("cert+empty-traj", [], None, "proof", True, C.SOLVED_AT_FLOOR),
    # --- IMPROVING: recent strict gain, no cert ---
    ("improving (minimize, decreasing)", [0.9, 0.7, 0.5], 0.1, None, True, C.IMPROVING),
    ("improving (maximize, increasing)", [0.1, 0.3, 0.5], 0.1, None, False, C.IMPROVING),
    ("improving overrides stuck (gain + headroom)", [0.9, 0.8, 0.5], 5.0, None, True, C.IMPROVING),
    ("tiny gain still counts (no noise threshold)", [0.5, 0.5, 0.5 - 1e-12], 0.1, None, True, C.IMPROVING),
    # --- STUCK: flat, no cert, open headroom ---
    ("stuck (flat + headroom)", [0.5, 0.5, 0.5], 0.2, None, True, C.STUCK),
    ("stuck (got worse + headroom)", [0.5, 0.6, 0.7], 0.2, None, True, C.STUCK),
    ("window boundary: improved early then flat -> stuck",
     [0.9, 0.5, 0.5, 0.5, 0.5], 0.2, None, True, C.STUCK),  # gain is outside last window=3
    # --- UNKNOWN: not enough signal ---
    ("unknown (flat, headroom=0)", [0.5, 0.5, 0.5], 0.0, None, True, C.UNKNOWN),
    ("unknown (flat, headroom None)", [0.5, 0.5, 0.5], None, None, True, C.UNKNOWN),
    ("unknown (empty traj, no cert)", [], 0.1, None, True, C.UNKNOWN),
]


def run() -> dict:
    rows, correct = [], 0
    by_class = {}
    for name, scores, headroom, cert, minimize, expected in CASES:
        got = classify(_traj(scores), headroom=headroom, certificate=cert, minimize=minimize)
        ok = got is expected
        correct += ok
        rows.append({"case": name, "expected": expected.value, "got": got.value, "ok": ok})
        d = by_class.setdefault(expected.value, [0, 0])
        d[0] += ok
        d[1] += 1
    n = len(CASES)
    return {
        "n_cases": n,
        "accuracy": correct / n,
        "per_class": {k: f"{v[0]}/{v[1]}" for k, v in by_class.items()},
        "supported": correct == n,
        "misses": [r for r in rows if not r["ok"]],
        "rows": rows,
    }


def main() -> int:
    v = run()
    print("Claim #6 — trajectory classifier accuracy")
    print(f"  cases: {v['n_cases']}  accuracy: {v['accuracy']:.0%}")
    print(f"  per-class (correct/total): {v['per_class']}")
    if v["misses"]:
        print("  MISSES:")
        for m in v["misses"]:
            print(f"    {m['case']}: expected {m['expected']}, got {m['got']}")
    print(f"  VERDICT: claim #6 {'SUPPORTED' if v['supported'] else 'NOT supported'}")
    print("  NOTE (robustness): the rule uses STRICT gain with no noise threshold — a "
          "1e-12 improvement reads as IMPROVING. Fine for verified best-scores; flag if "
          "trajectories are noisy.")
    out = Path("results/ablation-mechanism/classifier.json")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(v, indent=2))
    print(f"\nwrote {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
