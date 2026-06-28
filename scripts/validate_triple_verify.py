"""Validation test for JSAgent claim #7: triple-verify catches fake scores /
evaluator drift (the P9/P14/P17 failure mode — one local evaluator silently
disagreeing with the arena truth).

This is a VALIDATION test, not an A/B: it measures the safeguard's catch-rate and
false-alarm-rate. triple_verify_radius scores a config three independent ways
(numpy `fast`, mpmath `exact`, scipy `cross`) and passes iff all agree within `tol`
AND the radius is feasible. We:

  1. No-false-alarm: on N feasible configs with NO drift, it must PASS (FPR ~ 0).
  2. Catch drift: inject a known drift δ into ONE path (monkeypatch `common_radius`,
     simulating a drifted local evaluator). For δ above tol it must FLAG (passed=False,
     "disagreement"); for δ below tol it must NOT flag (numerical noise is tolerated).

A high catch-rate above tol + ~0 false alarms = claim #7 supported.

Run: uv run python scripts/validate_triple_verify.py
"""

from __future__ import annotations

import json
from pathlib import Path

import numpy as np

from einstein.ablation_packing import evaluator as ev


def _feasible_configs(n_configs: int, n_circles: int = 12) -> list[np.ndarray]:
    """Cold-init configs; their `common_radius` is feasible by construction
    (r = min(half-min-pairgap, wall)), so a correct verifier must PASS them."""
    return [ev.cold_init(n_circles, seed) for seed in range(n_configs)]


def run(n_configs: int = 200) -> dict:
    configs = _feasible_configs(n_configs)
    real_common_radius = ev.common_radius  # the un-drifted numpy path

    # 1) No-false-alarm baseline (δ = 0)
    false_alarms = sum(0 if ev.triple_verify_radius(c).passed else 1 for c in configs)

    # 2) Drift injection across magnitudes around tol (1e-9)
    deltas = [0.0, 1e-12, 1e-10, 1e-9, 1e-8, 1e-6, 1e-3, 1e-1]
    catch = {}
    try:
        for d in deltas:
            # simulate a drifted local evaluator: the `fast` path reads d too high,
            # while exact/cross stay correct -> a real disagreement triple-verify must catch.
            ev.common_radius = (lambda c, _d=d: real_common_radius(c) + _d)
            flagged = sum(1 for c in configs if not ev.triple_verify_radius(c).passed)
            catch[d] = flagged / len(configs)
    finally:
        ev.common_radius = real_common_radius  # always restore

    tol = 1e-9
    above = [d for d in deltas if d > tol]
    below = [d for d in deltas if 0 < d <= tol]
    catch_above = min(catch[d] for d in above)          # worst-case catch above tol
    falsealarm_below = max(catch[d] for d in below)      # worst-case flag below tol (noise)

    verdict = {
        "n_configs": n_configs,
        "tol": tol,
        "false_alarm_rate_no_drift": false_alarms / n_configs,
        "catch_rate_by_delta": catch,
        "min_catch_rate_above_tol": catch_above,
        "max_falsealarm_below_tol": falsealarm_below,
        "supported": (false_alarms == 0 and catch_above == 1.0),
    }
    return verdict


def main() -> int:
    v = run()
    print("Claim #7 — triple-verify catches evaluator drift")
    print(f"  configs: {v['n_configs']}  tol: {v['tol']:.0e}")
    print(f"  false-alarm rate (no drift): {v['false_alarm_rate_no_drift']:.0%}")
    print("  catch rate by injected drift δ:")
    for d, r in v["catch_rate_by_delta"].items():
        mark = "  (≤tol: should NOT flag)" if 0 < d <= v["tol"] else ("  (>tol: must flag)" if d > v["tol"] else "  (control)")
        print(f"    δ={d:>7.0e} -> caught {r:>4.0%}{mark}")
    print(f"\n  => min catch above tol: {v['min_catch_rate_above_tol']:.0%}; "
          f"false alarms below tol: {v['max_falsealarm_below_tol']:.0%}")
    print(f"  VERDICT: claim #7 {'SUPPORTED' if v['supported'] else 'NOT supported'}")

    out = Path("results/ablation-mechanism/triple-verify.json")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(v, indent=2))
    print(f"\nwrote {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
