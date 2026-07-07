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
from check_submission import (  # noqa: E402
    API_URL,
    check_leaderboard,
)

from einstein import auto_submit  # noqa: E402
from einstein import triple_verify as tv  # noqa: E402
from einstein.kissing_number.evaluator import overlap_loss_mpmath  # noqa: E402

# Absolute score margin the candidate must beat arena #1 by. Blocks ~1e-13
# float-noise "wins" that are indistinguishable from the leader. Overridden up
# to the arena's own minImprovement when that is larger.
DEFAULT_MARGIN_FLOOR = 1e-9

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
LOG_DIR = PROJECT_ROOT / "logs" / "kissing_cron"
LOG_DIR.mkdir(parents=True, exist_ok=True)

# Per-problem config — set by _configure() from CLI (default: P6 / n=594, back-compat).
# The whole kissing family shares this one loop; only (id, slug) change per problem:
#   6  kissing-number-d11      (n=594, solved)   24  kissing-number-d11-605 (n=605, open)
#   22 kissing-number-d12      (n=841)           25  kissing-number-d12-842 (n=842, open)
PROBLEM_ID = 6
RESULTS_DIR = PROJECT_ROOT / "results" / "problem-6-kissing-number"
POLISH_TRAIL = RESULTS_DIR / "polish-trail"
STATE_FILE = RESULTS_DIR / "cron_state.json"
LOCK_FILE = RESULTS_DIR / "cron.lock"


def _configure(problem_id: int, slug: str) -> None:
    """Point all per-problem paths at <id>-<slug>. Call once at start of main()."""
    global PROBLEM_ID, RESULTS_DIR, POLISH_TRAIL, STATE_FILE, LOCK_FILE
    PROBLEM_ID = problem_id
    RESULTS_DIR = PROJECT_ROOT / "results" / f"problem-{problem_id}-{slug}"
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    POLISH_TRAIL = RESULTS_DIR / "polish-trail"
    STATE_FILE = RESULTS_DIR / "cron_state.json"
    LOCK_FILE = RESULTS_DIR / "cron.lock"


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
        "uv",
        "run",
        "python",
        str(SCRIPT_DIR / "polish_ulp_coord.py"),
        "--warm-start",
        str(warm_start),
        "--dps",
        "50",
        "--budget",
        str(budget_sec),
        "--max-ulps",
        "2",
        "--max-sweeps",
        "8",
        "--row-order",
        "seq",
        "--seed",
        str(int(time.time()) % 100000),
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


def honest_score(v: np.ndarray) -> float:
    """The real objective on the polished vectors — NOT the polish's saved
    surrogate ``score``. Goal 2 proved the disk ``score`` can be a polish
    internal (``polish_ulp_coord``'s surrogate), so every submit decision
    re-scores from the vectors with the arena ground-truth evaluator.
    """
    return overlap_loss_mpmath(v, dps=50)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--budget", type=int, default=1200, help="polish budget in seconds")
    parser.add_argument("--dry-run", action="store_true", help="polish and report, do not submit")
    parser.add_argument(
        "--margin-floor",
        type=float,
        default=DEFAULT_MARGIN_FLOOR,
        help="absolute score margin the candidate must beat arena #1 by "
        "(blocks float-noise wins). Effective floor = max(this, arena minImprovement).",
    )
    parser.add_argument("--problem-id", type=int, default=6, help="arena problem id (6/24/22/25)")
    parser.add_argument(
        "--slug", default="kissing-number", help="results dir slug: results/problem-<id>-<slug>/"
    )
    args = parser.parse_args()
    _configure(args.problem_id, args.slug)

    if not acquire_lock():
        return 0
    try:
        log(f"=== cron tick p{PROBLEM_ID} (budget={args.budget}s dry_run={args.dry_run}) ===")
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

        # 3. Run polish (side effect: writes the improved config to disk)
        warm_start = RESULTS_DIR / "solution_best_mpmath.json"
        polish_log = LOG_DIR / f"polish-{int(time.time())}.log"
        surrogate, improved = run_polish_chain(warm_start, args.budget, polish_log)

        # 4. Honest score on the REAL objective — never trust the polish surrogate.
        v, _ = load_best_on_disk()
        score = honest_score(v)
        payload = {"vectors": v.tolist()}
        log(
            f"honest score (overlap_loss_mpmath dps50): {score:.10e} "
            f"(disk surrogate={surrogate:.4e}, improved={improved})"
        )

        # 5. Triple-verify the real objective three independent ways.
        tv_result = tv.run_payload(PROBLEM_ID, payload)
        log(f"triple-verify: passed={tv_result.passed} — {tv_result.reason}")

        # 6. Effective margin floor = max(arena minImprovement, our --margin-floor).
        try:
            arena_min = fetch_min_improvement()
        except Exception as e:
            log(f"minImprovement fetch failed ({e}); using --margin-floor only")
            arena_min = 0.0
        min_improvement = max(arena_min, args.margin_floor)

        minimize = auto_submit.PROBLEM_MINIMIZE.get(PROBLEM_ID)
        if minimize is None:
            log(f"P{PROBLEM_ID} absent from PROBLEM_MINIMIZE — refusing to guess direction")
            return 1

        # 7. Canonical 6-gate chain: kill / triple-verify / daily-cap / throttle /
        #    arena-#1 SOTA / POST+flock'd audit. Reuse the leader score fetched above.
        result = auto_submit.try_submit(
            PROBLEM_ID,
            payload,
            score,
            triple_verify=tv_result.as_dict(),
            min_improvement=min_improvement,
            minimize=minimize,
            arena_top1_score=float(leader["score"]),
            dry_run=args.dry_run,
        )
        if result.submitted:
            state["last_submitted_score"] = score
            arena_id = None
            if result.submission and result.submission.arena_response:
                arena_id = result.submission.arena_response.get("id")
            state["last_submitted_id"] = arena_id
            log(f"SUBMITTED: {result.reason} (arena_id={arena_id})")
        else:
            log(f"HELD at gate '{result.rejected_at_gate}': {result.reason}")
        save_state(state)

        log("=== cron tick done ===")
        return 0
    finally:
        release_lock()


if __name__ == "__main__":
    sys.exit(main())
