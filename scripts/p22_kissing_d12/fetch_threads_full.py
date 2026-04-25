"""Fetch full body + replies for all P22 threads. Saves per-thread JSON."""

from __future__ import annotations

import datetime as _dt
import json
import sys
import urllib.error
import urllib.request
from pathlib import Path

BASE_URL = "https://einsteinarena.com/api"
SLUG = "kissing-number-d12"
RESULTS_DIR = Path("results/p22_kissing_d12")


def fetch_json(path: str):
    url = f"{BASE_URL}{path}"
    with urllib.request.urlopen(urllib.request.Request(url), timeout=30) as resp:
        return json.loads(resp.read())


def main() -> int:
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    ts = _dt.datetime.now(_dt.UTC).strftime("%Y%m%dT%H%M%SZ")

    threads = fetch_json(f"/problems/{SLUG}/threads")
    print(f"Found {len(threads)} threads.\n")

    all_full = []
    for t in threads:
        tid = t["id"]
        title = t.get("title", "?")
        print(f"--- Thread {tid}: {title} ---")
        # Try a few common paths for thread detail
        body_full = None
        for path in [
            f"/threads/{tid}",
            f"/problems/{SLUG}/threads/{tid}",
        ]:
            try:
                body_full = fetch_json(path)
                break
            except urllib.error.HTTPError:
                continue
        if body_full is None:
            # Fallback: keep the partial body from list endpoint
            body_full = t
            print("  (no detail endpoint; kept list-row body)")
        all_full.append(body_full)

        # Print a digest
        body_text = body_full.get("body", "") if isinstance(body_full, dict) else ""
        print(body_text)
        print()

        replies = body_full.get("replies") if isinstance(body_full, dict) else None
        if replies:
            print(f"  [{len(replies)} replies]")
            for r in replies:
                who = r.get("agentName", "?")
                when = r.get("createdAt", "")
                rbody = r.get("body", "")
                print(f"  --- reply by {who} @ {when} ---")
                print(f"  {rbody[:2000]}")
                print()

    out = RESULTS_DIR / f"threads_full_{ts}.json"
    with open(out, "w") as f:
        json.dump(all_full, f, indent=2)
    print(f"\nSaved → {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
