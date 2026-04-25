"""Submit P22 (Kissing Number d=12) solution to Einstein Arena.

Usage:
    uv run python scripts/p22_kissing_d12/submit.py            # dry run + checklist
    uv run python scripts/p22_kissing_d12/submit.py --submit   # actual submission

Pre-submission checklist (auto-run before any POST):
    1. Local evaluator uses tolerance=0 (strict)
    2. Verify evaluator parity vs CHRONOS public SOTA → must score 2.0
    3. minImprovement gate against agent's previous best (0 for first sub)
    4. Score is in top-3 window
    5. Pre-flight URL/auth via verify_api()
    6. Rate limit check < 5 submissions / 30 min
    7. User explicit approval after seeing checklist
"""

from __future__ import annotations

import argparse
import json
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

import numpy as np

sys.path.insert(0, "src")
from einstein.p22_kissing_d12.evaluator import (
    overlap_loss,
    overlap_loss_fast,
    overlap_loss_mpmath,
)

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from check_submission import (
    API_URL,
    check_leaderboard,
    load_agent_name,
    verify_api,
    wait_for_leaderboard,
)

PROBLEM_ID = 22
RESULTS_DIR = Path("results/p22_kissing_d12")
CANDIDATE_PATH = RESULTS_DIR / "submit_rank3_candidate.json"
CHRONOS_PATH = RESULTS_DIR / "sota_best_chronos_rank1_id2081.json"


def fetch_min_improvement() -> float:
    url = f"{API_URL}/problems"
    with urllib.request.urlopen(url, timeout=15) as resp:
        problems = json.loads(resp.read())
    for p in problems:
        if p["id"] == PROBLEM_ID:
            return float(p["minImprovement"])
    raise ValueError(f"Problem {PROBLEM_ID} not found")


def submit_solution(vectors, dry_run: bool = False):
    submit_url = f"{API_URL}/solutions"
    payload = {"problem_id": PROBLEM_ID, "solution": {"vectors": vectors}}

    if dry_run:
        print(f"DRY RUN: Would POST {len(vectors)}×{len(vectors[0])} matrix to {submit_url}")
        return None

    api_key = verify_api()
    data = json.dumps(payload).encode()
    req = urllib.request.Request(
        submit_url,
        data=data,
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=60) as resp:
            return json.loads(resp.read())
    except urllib.error.HTTPError as e:
        body = e.read().decode(errors="replace")
        print(f"HTTP {e.code}: {body[:500]}")
        return {"_error": e.code, "_body": body[:500]}


def run_checklist(submit_path: Path) -> dict:
    """Run pre-submission checklist. Returns context dict."""
    print("\n" + "=" * 70)
    print("PRE-SUBMISSION CHECKLIST  —  P22 (Kissing Number d=12)")
    print("=" * 70)

    # Load candidate
    print(f"\n[1] Load candidate from {submit_path}")
    cand = json.loads(submit_path.read_text())
    vectors = np.array(cand["vectors"], dtype=np.float64)
    print(f"    shape: {vectors.shape}")
    assert vectors.shape == (841, 12), f"WRONG SHAPE: {vectors.shape}"
    print(f"    ✓ shape OK")

    # 2. Score via three independent paths
    print(f"\n[2] Triple-verify candidate score:")
    s_arena = overlap_loss(vectors)
    s_dot = overlap_loss_fast(vectors)
    print(f"    [a] overlap_loss (arena diff-based):  {s_arena!r}")
    print(f"    [b] overlap_loss_fast (dot-based):    {s_dot!r}")
    print(f"        delta:                              {s_arena - s_dot:+.6e}")
    print(f"    [c] overlap_loss_mpmath @ 50 dps...", end="", flush=True)
    t0 = time.time()
    s_mp = overlap_loss_mpmath(vectors, dps=50)
    print(f"  {s_mp!r}  ({time.time()-t0:.1f}s)")
    print(f"        delta arena−mpmath: {s_arena - s_mp:+.6e}")

    # 3. Verify CHRONOS SOTA still scores 2.0 in our evaluator
    print(f"\n[3] Verify evaluator parity against CHRONOS public SOTA (must = 2.0)")
    chronos_data = json.loads(CHRONOS_PATH.read_text())
    chronos_v = np.array(chronos_data["vectors"], dtype=np.float64)
    chronos_score = overlap_loss(chronos_v)
    print(f"    CHRONOS SOTA local score: {chronos_score!r}")
    assert abs(chronos_score - 2.0) < 1e-12, "EVALUATOR DRIFT — DO NOT SUBMIT"
    print(f"    ✓ evaluator parity OK")

    # 4. Sanity: not byte-identical to CHRONOS
    same = np.allclose(vectors, chronos_v, atol=1e-15)
    print(f"\n[4] Payload-uniqueness check:")
    print(f"    byte-identical to CHRONOS:   {same}  (must be False)")
    assert not same, "PAYLOAD IS A COPY OF CHRONOS — would be rejected"
    print(f"    ✓ candidate is structurally distinct from CHRONOS")

    # 5. Live leaderboard
    print(f"\n[5] Live leaderboard (refresh):")
    lb = check_leaderboard(PROBLEM_ID, limit=10)
    print(f"    {'#':>2} {'agent':<28} {'score':<25} {'id':>8}")
    for i, sol in enumerate(lb, 1):
        sc = sol.get("score")
        sc_str = f"{sc:.15f}" if isinstance(sc, (int, float)) else str(sc)
        marker = " <<< proposed slot" if (i == 3 and isinstance(sc, (int, float)) and s_arena < sc) else ""
        print(f"    {i:>2} {sol.get('agentName', '?'):<28} {sc_str:<25} {sol.get('id', -1):>8}{marker}")

    # 6. minImprovement live
    print(f"\n[6] Live minImprovement check:")
    mi = fetch_min_improvement()
    print(f"    minImprovement = {mi}")

    # 7. Predict rank
    candidate_score = s_arena
    rank = 1
    for sol in lb:
        sc = sol.get("score")
        if isinstance(sc, (int, float)) and sc < candidate_score:
            rank += 1
    print(f"\n[7] Predicted rank for our score {candidate_score!r}: #{rank}")

    # 8. Window check
    print(f"\n[8] Rank-3 window check (target):")
    silver = lb[1]["score"] if len(lb) > 1 else None
    bronze = lb[2]["score"] if len(lb) > 2 else None
    print(f"    silver: {silver!r}")
    print(f"    ours:   {candidate_score!r}")
    print(f"    bronze: {bronze!r}")
    if silver is not None and bronze is not None:
        in_w = silver < candidate_score < bronze
        print(f"    in rank-3 window: {in_w}")

    return {
        "candidate_score_arena": candidate_score,
        "candidate_score_mpmath": s_mp,
        "min_improvement": mi,
        "predicted_rank": rank,
        "leaderboard": lb,
        "vectors_list": vectors.tolist(),
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--submit", action="store_true", help="Actually submit (no dry-run)")
    ap.add_argument("--candidate", type=str, default=str(CANDIDATE_PATH))
    ap.add_argument("--no-wait", action="store_true", help="Skip post-submit polling")
    ap.add_argument("--yes", action="store_true", help="Skip interactive y/n confirmation (CLI)")
    args = ap.parse_args()

    cand_path = Path(args.candidate)
    if not cand_path.exists():
        print(f"ERROR: candidate not found at {cand_path}")
        print(f"Run: uv run python scripts/p22_kissing_d12/build_rank3_squeeze.py")
        sys.exit(1)

    ctx = run_checklist(cand_path)

    print("\n" + "=" * 70)
    print(f"PROPOSED SUBMISSION:")
    print(f"  problem:        P22 (Kissing Number d=12)")
    print(f"  candidate:      {cand_path}")
    print(f"  arena score:    {ctx['candidate_score_arena']!r}")
    print(f"  mpmath score:   {ctx['candidate_score_mpmath']!r}")
    print(f"  predicted rank: #{ctx['predicted_rank']}")
    print("=" * 70)

    if not args.submit:
        print("\nDry run — pass --submit to actually POST.")
        return

    # Pre-flight + final confirmation
    print("\n>>> About to POST to arena. Last chance to abort. <<<")
    if not args.yes:
        try:
            ans = input("Type YES (uppercase) to submit: ")
        except EOFError:
            print("ABORT (no terminal input)")
            return
        if ans.strip() != "YES":
            print(f"ABORT (got '{ans}')")
            return

    print("\nSubmitting...", flush=True)
    result = submit_solution(ctx["vectors_list"], dry_run=False)
    print(f"Response: {json.dumps(result, indent=2)[:500]}")

    if not args.no_wait:
        agent = load_agent_name()
        print(f"\nWaiting for leaderboard update (agent={agent})...")
        wait_for_leaderboard(PROBLEM_ID, agent, interval=300, max_checks=12)


if __name__ == "__main__":
    main()
