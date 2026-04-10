"""Automated polish+submit loop for P6 Kissing Number.

Design
------
One full cycle per invocation:
  1. Check the arena leaderboard.
  2. Run a bounded polish from our local best, using the ulp-coord sweep.
  3. If the polish yields a score strictly below the current leader on the
     leaderboard AND strictly below our last submission, submit it.
  4. Leave the new best on disk for the next invocation.

This script is meant to be called by a launchd agent (macOS) or cron on a
schedule. The schedule itself is defined by the operator's per-machine
launchd plist (not committed to this repo).

Environment
-----------
Runs inside the project's uv venv. Inherits the arena credentials from
~/.config/einsteinarena/credentials.json like submit.py.

Usage
-----
    uv run python scripts/kissing_number/cron_polish_submit.py \
        --budget 1200

    # Dry run: polish and report, don't submit
    uv run python scripts/kissing_number/cron_polish_submit.py \
        --budget 300 --dry-run
"""

from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
import time
from pathlib import Path

import numpy as np

# Import from the same directory as this script
SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR.parent.parent / "src"))
sys.path.insert(0, str(SCRIPT_DIR.parent))
from einstein.kissing_number.evaluator import overlap_loss_mpmath  # noqa: E402
from check_submission import (  # noqa: E402
    API_URL,
    check_leaderboard,
    load_agent_name,
    load_api_key,
    verify_api,
)

PROBLEM_ID = 6
PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
RESULTS_DIR = PROJECT_ROOT / "results" / "problem-6-kissing-number"
POLISH_TRAIL = RESULTS_DIR / "polish-trail"
STATE_FILE = RESULTS_DIR / "cron_state.json"
LOCK_FILE = RESULTS_DIR / "cron.lock"
LOG_DIR = PROJECT_ROOT / "logs" / "kissing_cron"
LOG_DIR.mkdir(parents=True, exist_ok=True)


def log(msg: str) -> None:
    t = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
    print(f"[{t}Z] {msg}", flush=True)


def acquire_lock() -> bool:
    """Simple file lock — prevents overlapping cron invocations."""
    if LOCK_FILE.exists():
        try:
            pid = int(LOCK_FILE.read_text().strip())
            # check if pid is alive
            try:
                os.kill(pid, 0)
                log(f"another cron instance running (pid={pid}) — exiting")
                return False
            except ProcessLookupError:
                log(f"stale lock (pid={pid}), removing")
                LOCK_FILE.unlink()
        except (ValueError, FileNotFoundError):
            LOCK_FILE.unlink(missing_ok=True)
    LOCK_FILE.parent.mkdir(parents=True, exist_ok=True)
    LOCK_FILE.write_text(str(os.getpid()))
    return True


def release_lock() -> None:
    LOCK_FILE.unlink(missing_ok=True)


def load_state() -> dict:
    if STATE_FILE.exists():
        return json.loads(STATE_FILE.read_text())
    return {"last_submitted_score": None, "last_submitted_id": None, "last_run_utc": None}


def save_state(state: dict) -> None:
    state["last_run_utc"] = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    STATE_FILE.write_text(json.dumps(state, indent=2))


def load_best_on_disk() -> tuple[np.ndarray, float]:
    path = RESULTS_DIR / "solution_best_mpmath.json"
    with open(path) as f:
        d = json.load(f)
    v = np.array(d["vectors"], dtype=np.float64)
    return v, float(d["score"])


def save_best_to_disk(v: np.ndarray, score: float, tag: str) -> None:
    out = {
        "vectors": v.tolist(),
        "score": score,
        "source": f"cron_polish_submit:{tag}",
    }
    path = RESULTS_DIR / "solution_best_mpmath.json"
    tmp = path.with_suffix(".json.tmp")
    with open(tmp, "w") as f:
        json.dump(out, f)
    os.replace(tmp, path)
    POLISH_TRAIL.mkdir(parents=True, exist_ok=True)
    trail = POLISH_TRAIL / f"cron-{tag}-{score:.6e}.json"
    with open(trail, "w") as f:
        json.dump(out, f)


def fetch_min_improvement() -> float:
    import urllib.request
    url = f"{API_URL}/problems"
    with urllib.request.urlopen(url, timeout=15) as resp:
        problems = json.loads(resp.read())
    for p in problems:
        if p["id"] == PROBLEM_ID:
            return float(p["minImprovement"])
    raise ValueError(f"Problem {PROBLEM_ID} not found")


def run_polish_chain(warm_start: Path, budget_sec: int, log_path: Path) -> tuple[float, bool]:
    """Run the alternating ulp polish chain. Returns (final_score, improved_bool)."""
    _, start_score = load_best_on_disk()

    # Run a single ulp2seq polish (the empirically most productive variant).
    # Multiple variants can be re-added later once we confirm the solo run works.
    cmd = [
        "uv", "run", "python", str(SCRIPT_DIR / "polish_ulp_coord.py"),
        "--warm-start", str(warm_start),
        "--dps", "50",
        "--budget", str(budget_sec),
        "--max-ulps", "2",
        "--max-sweeps", "8",
        "--row-order", "seq",
        "--seed", str(int(time.time()) % 100000),
    ]
    log(f"polish cmd: {' '.join(cmd)}")
    with open(log_path, "w") as f:
        result = subprocess.run(cmd, stdout=f, stderr=subprocess.STDOUT, cwd=str(PROJECT_ROOT))
    if result.returncode != 0:
        log(f"polish exited with code {result.returncode}")

    _, final_score = load_best_on_disk()
    improved = final_score < start_score
    log(f"polish: start={start_score:.6e} final={final_score:.6e} improved={improved}")
    return final_score, improved


def submit_current_best(local_score: float, current_leader: float) -> tuple[bool, int | None]:
    """POST the current best to the arena. Returns (success, submission_id)."""
    import urllib.error
    import urllib.request

    v, score = load_best_on_disk()
    if abs(score - local_score) > 1e-20:
        log(f"score mismatch: disk={score} expected={local_score}")
        return False, None

    # Triple-verify (matches submit.py's stability check)
    s50 = overlap_loss_mpmath(v, dps=50)
    s80 = overlap_loss_mpmath(v, dps=80)
    if abs(s50 - s80) >= 1e-20:
        log(f"precision instability: dps50={s50} dps80={s80}")
        return False, None
    if s50 >= current_leader:
        log(f"not strictly better than leader: {s50} >= {current_leader}")
        return False, None

    api_key = load_api_key()
    if not api_key:
        log("no API key")
        return False, None

    payload = {"problem_id": PROBLEM_ID, "solution": {"vectors": v.tolist()}}
    data = json.dumps(payload).encode()
    req = urllib.request.Request(
        f"{API_URL}/solutions",
        data=data,
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=120) as resp:
            result = json.loads(resp.read())
        sub_id = result.get("id")
        log(f"submitted: id={sub_id} score_local={s50:.15e}")
        return True, sub_id
    except urllib.error.HTTPError as e:
        body = e.read().decode()
        log(f"submit error {e.code}: {body}")
        return False, None


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--budget", type=int, default=1200,
                        help="polish budget in seconds")
    parser.add_argument("--dry-run", action="store_true",
                        help="polish and report, do not submit")
    parser.add_argument("--min-margin", type=float, default=0.0,
                        help="only submit if (leader - our_score) / leader >= this fraction")
    parser.add_argument("--force-submit", action="store_true",
                        help="skip leader check and submit whatever disk has")
    args = parser.parse_args()

    if not acquire_lock():
        return 0
    try:
        log(f"=== cron tick (budget={args.budget}s dry_run={args.dry_run}) ===")
        state = load_state()

        # 1. Check leaderboard
        try:
            lb = check_leaderboard(PROBLEM_ID, limit=3)
            if not lb:
                log("empty leaderboard — aborting")
                return 1
            leader = lb[0]
            log(f"leader: {leader['agentName']} @ {leader['score']:.10e} (id {leader['id']})")
        except Exception as e:
            log(f"leaderboard fetch failed: {e}")
            return 1

        # 2. Current local best
        v, local_score = load_best_on_disk()
        log(f"local best: {local_score:.10e}")

        # 3. Run polish
        warm_start = RESULTS_DIR / "solution_best_mpmath.json"
        polish_log = LOG_DIR / f"polish-{int(time.time())}.log"
        new_score, improved = run_polish_chain(warm_start, args.budget, polish_log)

        # 4. Decide whether to submit
        leader_score = float(leader["score"])
        last_submitted = state.get("last_submitted_score")

        should_submit = False
        reason = ""
        if args.force_submit:
            should_submit = True
            reason = "force_submit"
        elif new_score >= leader_score:
            reason = f"not better than leader ({new_score:.4e} >= {leader_score:.4e})"
        elif last_submitted is not None and new_score >= last_submitted:
            reason = f"not better than our last submission ({new_score:.4e} >= {last_submitted:.4e})"
        else:
            margin = (leader_score - new_score) / leader_score
            if margin < args.min_margin:
                reason = f"margin {margin:.4%} < min {args.min_margin:.4%}"
            else:
                should_submit = True
                reason = f"margin {margin:.4%}, improving {last_submitted} -> {new_score:.4e}"

        log(f"decision: {'SUBMIT' if should_submit else 'HOLD'} — {reason}")

        if should_submit and not args.dry_run:
            ok, sub_id = submit_current_best(new_score, leader_score)
            if ok:
                state["last_submitted_score"] = new_score
                state["last_submitted_id"] = sub_id
                save_state(state)
                log(f"state updated: last_submitted={new_score:.10e} id={sub_id}")
            else:
                log("submission failed")
        else:
            save_state(state)

        log("=== cron tick done ===")
        return 0
    finally:
        release_lock()


if __name__ == "__main__":
    sys.exit(main())
