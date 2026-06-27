#!/usr/bin/env python3
"""Generate a cold-vs-warm markdown summary from an ablation runs.jsonl."""
import json, sys
from collections import defaultdict
from pathlib import Path

results_dir = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(
    "/Users/jmsung/projects/einstein/cb-js-feat-ablation-runner/results/ablation-heilbronn")
runs_path = results_dir / "runs.jsonl"
out_path = results_dir / "SUMMARY.md"

rows = [json.loads(l) for l in open(runs_path) if l.strip()]
expected = 36
final = len(rows) >= expected

# per problem x arm gap_closed
agg = defaultdict(lambda: defaultdict(list))
for r in rows:
    agg[r["problem_id"]][r["arm"]].append(r["gap_closed"])

probs = sorted(agg, key=lambda p: int(p.split("n")[1]))
mean = lambda x: sum(x) / len(x) if x else float("nan")

cold_all, warm_all = [], []
lines = []
lines.append("# Heilbronn ablation — cold vs warm KB\n")
lines.append(f"- Status: {'**FINAL**' if final else f'**INTERIM** ({len(rows)}/{expected} solves)'}")
lines.append("- Model: claude-haiku-4-5 · seeds 1,2,3 · timeout 600s · max-lesson-chars 4000")
lines.append("- Metric: `gap%` = fraction of the gap to the reference optimum closed (higher is better)\n")
lines.append("| problem | cold gap% | warm gap% | Δ (warm−cold) | seeds (c/w) |")
lines.append("|---|---|---|---|---|")
for p in probs:
    c, w = agg[p].get("cold", []), agg[p].get("warm", [])
    cold_all += c; warm_all += w
    cm, wm = mean(c) * 100, mean(w) * 100
    delta = wm - cm if (c and w) else float("nan")
    win = " ✅" if (c and w and wm > cm) else ""
    lines.append(f"| {p} | {cm:.1f}% | {wm:.1f}%{win} | {delta:+.1f} | {len(c)}/{len(w)} |")
cm_all, wm_all = mean(cold_all) * 100, mean(warm_all) * 100
lines.append(f"| **MEAN** | **{cm_all:.1f}%** | **{wm_all:.1f}%** | **{wm_all-cm_all:+.1f}** | {len(cold_all)}/{len(warm_all)} |")

wr = [r["lessons_read"] for r in rows if r["arm"] == "warm"]
warm_wins = sum(1 for p in probs if agg[p].get("cold") and agg[p].get("warm")
                and mean(agg[p]["warm"]) > mean(agg[p]["cold"]))
n_compared = sum(1 for p in probs if agg[p].get("cold") and agg[p].get("warm"))
lines.append("")
lines.append("## Takeaways")
verdict = "warm ahead" if wm_all > cm_all else "cold ahead" if cm_all > wm_all else "tie"
lines.append(f"- Mean gap closed: **warm {wm_all:.1f}% vs cold {cm_all:.1f}%** ({wm_all-cm_all:+.1f} pts) — {verdict}.")
lines.append(f"- Warm wins **{warm_wins}/{n_compared}** problems head-to-head.")
if wr:
    lines.append(f"- Warm KB accumulating: lessons_read ranged {min(wr)}→{max(wr)} per solve (cold always 0).")
if not final:
    lines.append(f"- ⚠️ Interim — {expected-len(rows)} solves remaining; numbers will shift.")

out_path.write_text("\n".join(lines) + "\n")
print(f"wrote {out_path} ({'FINAL' if final else 'interim'}, {len(rows)}/{expected})")
