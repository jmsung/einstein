# agent/

Self-improvement infrastructure. The third layer of the artifact (alongside `wiki/` the brain and `.claude/rules/` the policy). This is the **dynamics** layer — measures whether the agent actually self-improves over cycles.

## Layout

```
agent/
├── README.md           # this file
├── cycle-log.md        # append-only: every problem-attempt cycle, with deltas
├── skill-library.md    # ranked techniques by hit-rate per problem category
├── metrics.md          # running scoreboard: time-to-top-3, hit-rates, transfer
└── ablations/          # controlled experiments (cold-wiki vs warm-wiki, persona ablation)
```

## Why this layer exists

Without measurement, "self-improvement" is vibes. Four failure modes the agent layer catches:

1. **Memorization, not improvement** — agent does well on seen problems, no transfer. Caught by transfer count in `metrics.md`.
2. **Human-in-the-loop laundering** — every wiki page is human-authored; agent just stored them. Caught by `author: agent|human|hybrid` ratios in `metrics.md`.
3. **Compute-time effect** — agent #2 just had longer runs. Caught by score-per-GPU-hour in `metrics.md`.
4. **Cherry-picked cycles** — measure only what worked. Caught by `cycle-log.md` being append-only (no deletion) per `.claude/rules/cycle-discipline.md`.

## Cadence

| Trigger | Update |
|---|---|
| `/worktree-done` | Append one row to `cycle-log.md` |
| `/wiki-learn` | Update technique citation count in `skill-library.md` |
| Weekly Friday | Recompute `metrics.md` |
| Monthly | Run an ablation; new file in `ablations/` |

See `.claude/rules/cycle-discipline.md` for the enforcement rule.

## Status

Pilot. Authored 2026-05-02 alongside the wiki refactor. Will tighten as cycle data accumulates.
