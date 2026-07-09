"""P7 gate-chain finalizer: verify a candidate against the 5 pre-approved gates,
submit iff ALL pass, poll to terminal state, append the audit log.

Gates (mb/logs/auto-submit.md, human pre-approval 2026-07-03):
  1. Triple-verify PASS on the EVALUATOR-NORMALIZED pf (V1=V3 exact; V2 exact grid)
  2. Score >= live SOTA + minImprovement with >= 5e-6 cushion
  3. exactMaxC within the 1.0001 band with >= 1e-7 margin
  4. Payload <= 2000 keys, key 1 absent
  5. Poll /api/solutions/{id} to terminal state (evaluated | 404) and log

    uv run python scripts/prime/gate_and_submit.py --file <candidate.json> [--live]
"""

from __future__ import annotations

import argparse
import datetime
import json
import sys
import time
import urllib.request
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "src"))
from einstein.arena_submit import load_api_key, submit_solution  # noqa: E402
from einstein.prime.evaluator import compute_score_only, evaluate  # noqa: E402

ARENA_TOL = 1e-4
BASE = "https://einsteinarena.com/api"
AUDIT = Path(__file__).resolve().parents[2] / ".mb/logs/auto-submit.md"


def api(path: str, auth: bool = False):
    h = {"User-Agent": "einstein-gates"}
    if auth:
        h["Authorization"] = f"Bearer {load_api_key()}"
    req = urllib.request.Request(BASE + path, headers=h)
    return json.load(urllib.request.urlopen(req, timeout=30))


def evaluator_normalized(pf: dict[int, float]) -> dict[int, float]:
    out = {k: float(np.clip(v, -10.0, 10.0)) for k, v in pf.items()}
    s = sum(v / k for k, v in out.items() if k != 1)
    out[1] = float(np.clip(-s, -10.0, 10.0))
    return out


def exact_max_c(pf: dict[int, float]) -> float:
    keys = np.array(sorted(pf), dtype=np.int64)
    vals = np.array([pf[int(k)] for k in keys])
    xmax = 10 * int(keys[-1])
    worst = -1e18
    for st in range(1, xmax + 1, 200_000):
        en = min(st + 200_000, xmax + 1)
        xs = np.arange(st, en, dtype=np.int64)
        worst = max(worst, float(((xs[:, None] // keys[None, :]).astype(np.float64) @ vals).max()))
    return worst


def log_audit(lines: list[str]) -> None:
    stamp = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    with open(AUDIT, "a") as f:
        f.write(f"\n### gate_and_submit {stamp}\n" + "\n".join(f"- {ln}" for ln in lines) + "\n")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--file", required=True)
    ap.add_argument("--live", action="store_true", help="actually submit (default: gate-check only)")
    args = ap.parse_args()

    raw = json.load(open(args.file))["partial_function"]
    pf = {int(k): float(v) for k, v in raw.items()}
    audit: list[str] = [f"candidate: {args.file}"]
    fails: list[str] = []

    # Gate 4: payload shape
    if len(raw) > 2000:
        fails.append(f"G4 payload {len(raw)} keys > 2000")
    if 1 in pf:
        fails.append("G4 key 1 present in payload (wastes a slot)")

    # Gate 1: triple-verify on evaluator-normalized pf
    epf = evaluator_normalized(pf)
    v1 = compute_score_only({k: v for k, v in epf.items() if k >= 2})
    v2 = exact_max_c(epf)
    v3 = evaluate({"partial_function": {str(k): v for k, v in pf.items()}})
    audit.append(f"V1={v1:.10f} V2 maxC={v2:.10f} V3={v3:.10f}")
    if not (v3 > 0 and abs(v1 - v3) < 1e-9):
        fails.append(f"G1 triple-verify FAIL (V1={v1:.10f} V3={v3:.10f})")

    # Gate 3: band margin. The 0.999-margin rescale lands maxC at EXACTLY
    # 1+0.999e-4 = the 1e-7-margin threshold; allow float-representation dust
    # (1e-12) so the by-construction margin isn't rejected on the boundary.
    if not v2 <= 1.0 + ARENA_TOL - 1e-7 + 1e-12:
        fails.append(f"G3 band margin FAIL (maxC={v2:.10f})")

    # Gate 2: live SOTA + minImprovement + cushion
    probs = api("/problems")
    min_imp = next(p.get("minImprovement", 1e-8) for p in probs if p.get("id") == 7)
    lb = api("/solutions/best?problem_id=7&limit=1000")
    sota = max(e["score"] for e in lb if e.get("score") is not None)
    bar = sota + min_imp
    audit.append(f"live SOTA={sota:.10f} bar={bar:.10f} our={v1:.10f} cushion={v1 - bar:+.2e}")
    if v1 < bar + 5e-6:
        fails.append(f"G2 cushion FAIL (need >= bar+5e-6={bar + 5e-6:.10f}, have {v1:.10f})")

    if fails:
        print("GATES FAILED:\n  " + "\n  ".join(fails))
        log_audit(audit + [f"RESULT: HELD — {'; '.join(fails)}"])
        sys.exit(1)

    print(f"ALL GATES PASS — score {v1:.10f}, cushion {v1 - bar:+.2e}")
    if not args.live:
        print("(gate-check only; rerun with --live to submit)")
        log_audit(audit + ["RESULT: gates PASS (dry check, no submit)"])
        return

    res = submit_solution(7, {"partial_function": raw}, expected_score=v1)
    sid = (res.arena_response or {}).get("id")
    audit.append(f"POST {res.http_status} id={sid}")
    print("POST:", res.http_status, res.arena_response)
    if not res.ok or not sid:
        log_audit(audit + ["RESULT: POST FAILED"])
        sys.exit(1)

    # Gate 5: poll to terminal state
    for _ in range(120):  # up to 60 min
        time.sleep(30)
        try:
            d = api(f"/solutions/{sid}", auth=True)
            if d.get("status") == "evaluated":
                print(f"ACCEPTED: id={sid} score={d.get('score')}")
                log_audit(audit + [f"RESULT: ACCEPTED id={sid} score={d.get('score')}"])
                return
        except urllib.error.HTTPError as e:
            if e.code == 404:
                print(f"REJECTED-DELETED: id={sid}")
                log_audit(audit + [f"RESULT: REJECTED-DELETED id={sid} (404)"])
                sys.exit(1)
            raise
    print("still pending after 60 min — check manually")
    log_audit(audit + [f"RESULT: still pending after 60 min, id={sid}"])


if __name__ == "__main__":
    main()
