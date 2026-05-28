# docs/tools/ — autonomous-loop tooling

Programmatic tools that let JSAgent run itself. The wiki layer
(`docs/wiki/`) is the knowledge it acts on; this directory is the
machinery that acts. Together they form the agent-driven discovery
loop described in [`mb/active/feat-autonomous-loop.md`](../../../mb/active/feat-autonomous-loop.md).

## Tool index

| Tool | Purpose |
|---|---|
| [`refresh_qmd.sh`](refresh_qmd.sh) | Re-index `docs/wiki/` and `docs/source/` in qmd. Run at cycle-end. |
| [`wiki_graph.py`](wiki_graph.py) | Wiki gap detector (FLT-style). Surfaces missing concepts / connections / chains / umbrellas; can auto-file top-3 as open questions. |
| [`gap_search.py`](gap_search.py) | For each open question, query arxiv (math categories) and append `## Suggested sources`. |
| [`concept_inventory.py`](concept_inventory.py) | Walks problem frontmatter, classifies referents as well-covered / under-sourced / missing-page / orphan-or-singleton. |
| [`pdf_to_md.py`](pdf_to_md.py) | Thin wrapper around `opendataloader-pdf` (Java backend) for math-aware PDF → markdown. |
| [`seed_ingest.py`](seed_ingest.py) | Two-step bulk arxiv ingest: `propose` searches per concept + writes a candidates JSON; `apply` downloads approved PDFs and writes `docs/source/` entries. Supports `--auto-approve-above THRESHOLD` for relevance-thresholded auto-ingest. |
| [`concept-search-terms.yaml`](concept-search-terms.yaml) | Slug → literature-vocabulary mapping consumed by `seed_ingest propose`. Curated; agent-coined slugs that have no literature analog get an empty list (intentionally-unmapped). |
| [`strategy_picker.py`](strategy_picker.py) | Reads `docs/agent/skill-library.md` + problem category, applies the autoresearch 1+1 rule (prior + novel). Also exports `convergence_detect()`. |
| [`calibrate.sh`](calibrate.sh) | Device-agnostic recalibration wrapper: runs `scripts/local_benchmark.py`, prints drift vs prior, prints sample router invocations. |
| [`cycle_runner.sh`](cycle_runner.sh) | Per-cycle discipline wrapper. Run after every cycle: `refresh_qmd` → `wiki_graph --file-questions` → `gap_search` → promotion-log check. |
| [`monitor.py`](monitor.py) | Read-only progress dashboard. Parses `docs/agent/cycle-log.md` and prints totals, outcomes, recent cycles. |
| [`claude_headless.py`](claude_headless.py) | Shared wrapper for non-interactive Claude Code invocations. Used by the inner-agent inside each cycle. |
| [`inner_agent_prompt.py`](inner_agent_prompt.py) | Builds the inner-agent prompt template (problem context + wiki excerpts + budget). |
| [`inner_agent_output.py`](inner_agent_output.py) | Structured-output schema + validator for inner-agent responses (Goal 7.3). |
| [`inner_agent_gates.py`](inner_agent_gates.py) | Pre-cycle resource gates: kill switch (`EINSTEIN_INNER_AGENT=0`), sentinel file (`mb/.inner-agent-disabled`), daily budget. |
| [`inner_agent_budget.py`](inner_agent_budget.py) | CLI + library for the daily token-budget ledger (`mb/logs/inner-agent-budget.md`). |
| [`notify_milestone.py`](notify_milestone.py) | macOS notification helper — fires a banner when `auto_submit` accepts a new arena record. |
| [`distill_paper.py`](distill_paper.py) | Distill a single `docs/raw/<id>.pdf` (or arxiv URL) into a `docs/source/<id>.md` LLM-distillation. |
| [`llm_distill.py`](llm_distill.py) | Lower-level LLM distillation primitive used by `distill_paper` + `seed_ingest` apply step. |
| [`select_top.py`](select_top.py) | Pick the top-N candidates from a `*-candidates.json` (used inside the seed-ingest pipeline). |
| [`seed-authors.yaml`](seed-authors.yaml) | Author-list seed for `seed_ingest propose` (broad-stroke literature sweep). |
| [`wiki_lint.py`](wiki_lint.py) | Wiki health lint — cite hygiene, broken refs, orphans, attribution. Hard fails drop the inner-agent sentinel via `cycle_runner.sh`. |

The top-level orchestrator lives one directory up at
[`scripts/autonomous_loop.py`](../../scripts/autonomous_loop.py) — see
"Running the loop" below.

## The cycle, end-to-end

```
┌────────────────────────────────────────────────────────────────┐
│ scripts/autonomous_loop.py  (outer orchestrator)               │
│                                                                │
│  1. load problem queue from docs/wiki/problems/*.md frontmatter│
│     (Tier S→A→B→C; skip frozen/conquered/blocked/hidden)       │
│                                                                │
│  2. pick top-priority active problem                           │
│                                                                │
│  3. inner_attempt(problem):                                    │
│     - category_for(problem_id)                                 │
│     - skill pick:                                              │
│       - default: einstein.bandit.thompson_proposer samples     │
│         per-category arms from skill-library counts            │
│         (Beta-Bernoulli posterior). Kill switch:               │
│         `EINSTEIN_BANDIT=0` → manifest strategy_picker path    │
│       - strategy_picker.pick_strategy still backs the fallback │
│         + supplies the row pattern reused by bandit updates    │
│     - [execute step — Phase 5 per-problem integration, TBD]    │
│     - at cycle end: einstein.bandit.update_counts rewrites the │
│       chosen technique's row in skill-library.md               │
│     - return result dict for the cycle-log row                 │
│                                                                │
│  4. append cycle-log row (docs/agent/cycle-log.md)             │
│                                                                │
│  5. shell out to docs/tools/cycle_runner.sh:                   │
│     a. refresh_qmd.sh         — keep search index hot          │
│     b. wiki_graph.py --file-questions                          │
│                               — surface fresh gap questions    │
│     c. gap_search.py          — enrich open questions w/ arxiv │
│     d. promotion-log check    — surface findings cited ≥3x     │
└────────────────────────────────────────────────────────────────┘
```

## Running the loop

### One-shot (interactive)

```bash
# Inspect the queue without doing anything
uv run python scripts/autonomous_loop.py --queue-only

# Plan the next cycle without writing anything
uv run python scripts/autonomous_loop.py --one-problem --dry-run

# Run one cycle for real
uv run python scripts/autonomous_loop.py --one-problem

# Run up to 3 cycles (will stop early if queue empties)
uv run python scripts/autonomous_loop.py --max-problems 3
```

### Under cron (every hour, say)

```cron
# Every hour, attempt one cycle — skip if a cycle ran in the last 15 min
0 * * * * cd /path/to/einstein/cb && \
  uv run python scripts/autonomous_loop.py --one-problem \
    --skip-if-recent 15 \
    >> mb/logs/autonomous-loop.log 2>&1
```

The `--skip-if-recent N` flag exits cleanly (status 0) if `cycle-log.md`
was modified within the last `N` minutes — avoids clobbering a manual
cycle that's still in flight. The concurrency lockfile at
`.autonomous-loop.lock` provides a separate guarantee against two
overlapping runs (exit 75 / `EX_TEMPFAIL` if another loop is running).

### Under Claude Code `/loop`

```text
/loop 30m scripts/autonomous_loop.py --one-problem --skip-if-recent 25
```

Pairs naturally with `monitor.py` in a second pane:

```bash
watch -n 60 uv run python docs/tools/monitor.py --recent 5
```

### One-shot recalibration (move to a new Mac, after macOS update, etc.)

```bash
bash docs/tools/calibrate.sh
```

Writes `docs/agent/calibrations/<device-key>.json` for the new machine
and prints a drift table vs the prior calibration if one existed.
`scripts/compute_router.py` picks up the new file automatically via
its sysctl-based device key.

## Cycle-discipline invariants

Per [.claude/rules/cycle-discipline.md](../../.claude/rules/cycle-discipline.md):

1. **One row per cycle**, no exceptions. Failures count. autonomous_loop
   appends honestly even for `scaffold-no-attempt` and
   `strategy-picked-no-execution` outcomes.
2. **`refresh_qmd.sh` before merge** — `cycle_runner.sh` step 1 takes care.
3. **`wiki_graph.py --file-questions` is mandatory** — step 2.
4. **Dead-end findings are mandatory** when an approach is abandoned —
   this is on the per-problem path that Phase 5 will canonicalize.
5. **`author:` frontmatter on every new wiki page** — checked by
   `wiki_attribution` lint, not by autonomous_loop directly.

Skipping any of the above silently breaks the self-improvement signal.
The cycle log is the audit trail; `monitor.py` is the read-only
projection of that trail.

## See also

- [`mb/active/feat-autonomous-loop.md`](../../../mb/active/feat-autonomous-loop.md) — the design + cycle-by-cycle progress for this branch
- [`docs/agent/cycle-log.md`](../agent/cycle-log.md) — the append-only audit trail
- [`docs/agent/skill-library.md`](../agent/skill-library.md) — technique hit-rate ledger consumed by `strategy_picker`
- [`docs/agent/calibrations/`](../agent/calibrations/) — per-device compute calibrations
- [`docs/wiki/findings/m5-max-utilization-strategy.md`](../wiki/findings/m5-max-utilization-strategy.md) — what 18-core + MPS + 128 GB unlocks
- [`docs/wiki/findings/dead-end-slug-as-arxiv-phrase-query.md`](../wiki/findings/dead-end-slug-as-arxiv-phrase-query.md) — why `concept-search-terms.yaml` exists
