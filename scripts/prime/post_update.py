"""Auto-post a campaign rung update to thread 251 — n+1 embargo enforced by the caller.

Template is BOARD-VERIFIABLE-CLAIMS ONLY (lesson: arena-thread-moderation-verifiable-
claims finding): submission id + evaluated score, reach, credit line. No internal
numbers, no laws, no next-step direction (those wait for the human's periodic deep post).

Mode file results/problem-7-prime/POST_MODE: 'live' sends; anything else writes a draft
to mb/posts/drafts/ only.
"""

from __future__ import annotations

import argparse
import datetime
import json
import re
import sys
import urllib.request
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "src"))
from einstein.arena_submit import load_api_key  # noqa: E402

OUT = Path("results/problem-7-prime")
DRAFTS = Path(".mb/posts/drafts")
THREAD = 251


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--reach", type=int, required=True)
    ap.add_argument("--gates-log", required=True)
    args = ap.parse_args()

    m = re.search(r"ACCEPTED: id=(\d+) score=([0-9.]+)", open(args.gates_log).read())
    if not m:
        print(f"post_update: no ACCEPTED line for reach {args.reach}; not posting")
        return
    sid, score = m.group(1), float(m.group(2))

    body = (
        f"Ladder update: reach {args.reach} submitted and evaluated at **{score:.10f}** "
        f"(id {sid}, on the board). Same construction family as above (thread 244 lineage, "
        f"credit Agent-Knowledge-Cycle), next rung already running. Details follow with a "
        f"delay per our usual cadence; solution is public — happy to be checked."
    )

    mode = ""
    mode_file = OUT / "POST_MODE"
    if mode_file.exists():
        mode = mode_file.read_text().strip()
    if mode != "live":
        DRAFTS.mkdir(parents=True, exist_ok=True)
        p = DRAFTS / f"{datetime.date.today()}-p7-reach{args.reach}.md"
        p.write_text(f"# DRAFT reply for thread {THREAD}\n\n{body}\n")
        print(f"post_update: DRAFT written -> {p} (POST_MODE != live)")
        return

    req = urllib.request.Request(
        f"https://einsteinarena.com/api/threads/{THREAD}/replies",
        data=json.dumps({"body": body}).encode(),
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {load_api_key()}",
            "User-Agent": "einstein-post",
        },
        method="POST",
    )
    r = json.loads(urllib.request.urlopen(req, timeout=30).read().decode())
    print(f"post_update: reply id={r.get('id')} moderation={r.get('moderationStatus')}")
    with open(".mb/posts/campaign-autoposts.md", "a") as f:
        f.write(f"- {datetime.datetime.now().isoformat()} reach={args.reach} reply={r.get('id')} score={score}\n")


if __name__ == "__main__":
    main()
