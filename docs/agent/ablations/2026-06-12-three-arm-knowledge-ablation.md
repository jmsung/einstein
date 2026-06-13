---
type: ablation-protocol
author: agent
drafted: 2026-06-12
status: protocol  # harness built (Goal 6); runs require fresh cold-start sessions
harness: src/einstein/meta_loop/ablation.py
prior_ablations:
  - 2026-05-03-surgical-removal-protocol.md
  - 2026-05-02-cold-vs-warm-p10-thomson.md
---

# 3-arm knowledge ablation — does the curated KB beat web search?

## The question

The cold-vs-warm audits measured *aggregate* wiki uplift; the surgical-removal
protocol isolates *individual page* contribution. Both compare "wiki" vs "no
wiki." Neither answers the question a reviewer will actually ask: **is the
curated knowledge base better than just letting the agent search the web?** If a
cold agent with web search climbs as fast as one with our wiki, the curation
work is not the source of the uplift — an honest, publishable negative result.

## The three arms

| Arm | Knowledge access | Tests |
|---|---|---|
| **A — curated wiki** | `docs/wiki/` only; no web | the curation hypothesis |
| **B — web search (firewalled)** | web only; no wiki | does generic retrieval suffice? |
| **C — model-only** | neither; training only | the floor — what the model already knows |

The experiment varies **reasoning support**, not **answer access**. Every arm
gets the problem statement; every arm is firewalled from the literal answer key.

## The firewall (the load-bearing control)

The result is meaningless if arm B can just read the leaderboard or this repo.
`ablation.is_firewalled` / `assert_allowed` block, for every arm:

- the arena host (`einsteinarena.com` + subdomains) — leaderboard + solutions;
- this repo (`jmsung/einstein`, `raw.githubusercontent.com/...`) — the wiki
  carries SOTA scores and solutions;
- solution dumps (`/solutions/`, `solution-best`, `/results/`, `/mb/problems/`);
- problem pages (`docs/wiki/problems/...`) — they print `score_current`.

`ablation.ANSWER_KEY_PROBES` is the canonical block-list the test suite asserts
on; `firewall_verified(probes)` must return True before any arm-B run starts.
General references (arxiv, wikipedia, mathoverflow) stay allowed — the arm may
*reason*, it just can't read the answer.

## Procedure

1. Pick the problem set — `stuck` problems with genuine headroom (Goal-1
   classifier), where reasoning support could actually move the score.
2. `build_run_matrix(problem_ids, seeds)` → the (problem × arm × seed) matrix.
   N seeds per (problem, arm) for a distribution, not a point estimate.
3. For each `RunSpec`: a **fresh cold-start Claude Code session** with the arm's
   knowledge access (autonomous self-execution would defeat the control — same
   caveat as the surgical-removal protocol). Arm B's web calls pass through
   `assert_allowed`.
4. Record each run's cycle trajectory (the cycle-log → `trajectory`).

## Measurement

Per run (local, no leaderboard):

- **climb-rate** — verified improvement per cycle (`ablation.climb_rate`);
- **dead-ends-avoided** — known dead-ends (from `docs/wiki/findings/`) the arm
  did *not* re-run (`dead_ends_avoided`) — the metric most directly testing the
  KB;
- **cycles-to-X%-of-floor** — cycles to close X% of the start→floor gap
  (`cycles_to_fraction_of_floor`); None when never reached (never silently 0).

Across seeds: `summarize_arm` (mean/median/stdev) + `rank_arms`. **Headline
reading:** A > B > C ⇒ the curated KB helps; A ≈ B ⇒ web search suffices (the
negative result we're prepared to report).

## Status

Harness + firewall built and tested (Goal 6, `tests/meta_loop/test_ablation.py`).
The runs themselves are the next step — queued, not yet executed.
