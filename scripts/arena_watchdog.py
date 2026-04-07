"""Arena-wide leaderboard change detector.

Snapshots all problem leaderboards, then polls hourly for ANY change.
Detects new submissions, score updates, and rank changes across all problems.

Usage:
    uv run python scripts/arena_watchdog.py                    # poll hourly
    uv run python scripts/arena_watchdog.py --interval 1800    # poll every 30 min
    uv run python scripts/arena_watchdog.py --once             # single snapshot
"""

import argparse
import json
import time
import urllib.request

API_URL = "https://einsteinarena.com/api"


def fetch_all_leaderboards(limit=10):
    """Fetch leaderboards for all problems."""
    url = f"{API_URL}/problems"
    with urllib.request.urlopen(url, timeout=30) as resp:
        problems = json.loads(resp.read())

    snapshot = {}
    for p in problems:
        pid = p["id"]
        try:
            url = f"{API_URL}/solutions/best?problem_id={pid}&limit={limit}"
            with urllib.request.urlopen(url, timeout=15) as resp:
                lb = json.loads(resp.read())
            snapshot[pid] = {
                "title": p["title"],
                "entries": [
                    {"agent": s["agentName"], "score": s["score"], "id": s["id"]}
                    for s in lb
                ],
            }
        except Exception as e:
            print(f"  [P{pid} fetch error: {e}]", flush=True)

    return snapshot


def diff_snapshots(old, new):
    """Find differences between two snapshots."""
    changes = []
    for pid in new:
        old_entries = {e["agent"]: e for e in old.get(pid, {}).get("entries", [])}
        new_entries = {e["agent"]: e for e in new[pid]["entries"]}
        title = new[pid]["title"]
        for agent, entry in new_entries.items():
            if agent not in old_entries:
                changes.append({
                    "type": "new_entry", "problem": pid, "title": title,
                    "agent": agent, "score": entry["score"], "id": entry["id"],
                })
            elif entry["score"] != old_entries[agent]["score"]:
                changes.append({
                    "type": "score_change", "problem": pid, "title": title,
                    "agent": agent,
                    "old_score": old_entries[agent]["score"],
                    "new_score": entry["score"],
                    "old_id": old_entries[agent]["id"],
                    "new_id": entry["id"],
                })
    return changes


def print_snapshot_summary(snapshot):
    """Print compact summary."""
    ts = time.strftime("%Y-%m-%d %H:%M:%S")
    print(f"\n[{ts}] Arena snapshot ({len(snapshot)} problems):", flush=True)
    for pid in sorted(snapshot):
        entries = snapshot[pid]["entries"]
        title = snapshot[pid]["title"][:35]
        top = entries[0] if entries else None
        top_str = f"{top['agent']}: {top['score']:.10f}" if top else "empty"
        print(f"  P{pid:<3} {title:<37} #1={top_str}", flush=True)


def print_changes(changes):
    ts = time.strftime("%Y-%m-%d %H:%M:%S")
    print(f"\n{'='*60}", flush=True)
    print(f"[{ts}] CHANGES DETECTED: {len(changes)}", flush=True)
    print(f"{'='*60}", flush=True)
    for c in changes:
        if c["type"] == "new_entry":
            print(f"  NEW  P{c['problem']} {c['title']}: "
                  f"{c['agent']} entered at {c['score']:.10f} (id={c['id']})",
                  flush=True)
        elif c["type"] == "score_change":
            print(f"  UPD  P{c['problem']} {c['title']}: "
                  f"{c['agent']} {c['old_score']:.10f} → {c['new_score']:.10f} "
                  f"(id {c['old_id']}→{c['new_id']})",
                  flush=True)
    print(f"{'='*60}\n", flush=True)


def main():
    parser = argparse.ArgumentParser(description="Arena-wide change detector")
    parser.add_argument("--interval", type=int, default=3600, help="Poll interval (s)")
    parser.add_argument("--max-checks", type=int, default=24, help="Max polls")
    parser.add_argument("--once", action="store_true", help="Single snapshot")
    args = parser.parse_args()

    print("Arena Watchdog — detecting leaderboard changes", flush=True)
    print("Fetching initial snapshot...", flush=True)

    snapshot = fetch_all_leaderboards()
    print_snapshot_summary(snapshot)

    if args.once:
        return

    print(f"\nPolling every {args.interval // 60} min for up to "
          f"{args.max_checks} checks", flush=True)

    for check in range(1, args.max_checks + 1):
        print(f"\n... waiting {args.interval // 60} min "
              f"(check {check}/{args.max_checks}) ...", flush=True)
        time.sleep(args.interval)

        try:
            new_snapshot = fetch_all_leaderboards()
        except Exception as e:
            print(f"  [Fetch error: {e}]", flush=True)
            continue

        changes = diff_snapshots(snapshot, new_snapshot)
        if changes:
            print_changes(changes)
            print(">>> Arena is processing submissions! <<<", flush=True)
        else:
            ts = time.strftime("%H:%M:%S")
            print(f"[{ts}] No changes detected.", flush=True)

        snapshot = new_snapshot

    print("\nWatchdog finished.", flush=True)


if __name__ == "__main__":
    main()
