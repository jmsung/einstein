# Meta-learning automation — turning the self-improvement loop from discretionary to enforced

**Status:** Phase 0+1+4 done (`js/feat/meta-learning-automation`, PR #122);
**Phase 2 done** (`js/feat/meta-learning-inner-agent`, 2026-06-09) — the headless
inner agent is instrumented + reliability-fixed + cost-proven, verdict **CONDITIONAL
GO** for Phase 3 (`docs/wiki/findings/inner-agent-first-run.md`). Phase 3 (scheduler)
remains a follow-on, gated on this branch's two entry conditions.

**Audience:** this is an *agent-process* design doc, not math wisdom — hence `docs/agent/`
(next to `cycle-log.md` / `skill-library.md` it governs), not `docs/wiki/`.

---

## The discovery that motivated this (2026-06-08, P2)

The P2 arena record (1.5028609 → 1.5028506, the campaign's first record, PR #121) was
**not** invented in the session that submitted it. The winning operator — warm
data-driven self-pruning — was written, almost line-for-line, in the "what might still
work" section of a dead-end finding authored **4 days earlier**
(`dead-end-p2-cold-seed-fixed-window.md`), which itself built on a mechanism finding from
**5 weeks earlier** (`p2-peak-locking-hessian-mechanism.md`). The session executed a
prescription the failure-log discipline had already accumulated.

Honest attribution of the win (so we automate the *real* cause, not a flattering story):

- **Decisive:** the `failure-is-a-finding` discipline + the `v²`-parameterization concept.
  The wiki *compounded* — each dead-end's next-door section narrowed the search until the
  move was explicit.
- **Did NOT contribute:** the 1000s-of-ingested-papers corpus (the win rode on ~4 in-house
  P2 findings, zero external-paper citations for the key move); the council/persona loop
  (didn't fire that session).
- **Mixed:** the wiki *also misled* — it recorded the 2-agent tie as "global minimum,
  honest-zero expected." The record required *overriding* that documented prior.
- **The gap this exposes:** the capture only happened **because a human asked**. The rules
  said to do it; a rule is advice the agent can rationalize past.

Captured as durable wisdom this cycle: concept `n-agent-tie-not-global-min`, technique
`warm-self-pruning-compact-support`, and two rule edits (`failure-is-a-finding`,
`wall-hit-escalation`).

## The principle

**Discretion decays; gates compound.** Automating meta-learning is not "write more rules" —
it is converting the discretionary self-improvement rules into **deterministic gates**
(hooks) + an **unattended driver** (scheduler), with **quality control** (pruning) so
automatic capture doesn't degrade into spam.

## Current state — what already exists (~80%)

| Layer | File | Status |
|---|---|---|
| Outer loop over 23 problems | `scripts/autonomous_loop.py` | ✅ queue/filter/sort/record — **`inner_attempt()` has a wired LLM inner-agent path** (`_try_llm_path` → `claude_headless`, from feat-autonomous-loop Goal 7.7), **not yet proven for unattended use** |
| Capture + index discipline | `docs/tools/cycle_runner.sh` | ✅ refresh_qmd → wiki_graph gap-detect → gap_search → promotion check |
| Measurement | `docs/agent/{cycle-log,skill-library,metrics,promotion-log}.md` | ✅ |
| Recall | qmd + REFUSING cycle-start query (`cycle-discipline`) + council seeding | ✅ |
| Hook infra | `.claude/hooks/wall-detector.sh` (PostToolUse Bash) | ✅ — hooks already run |
| Knowledge | `docs/wiki/{concepts,techniques,findings,rules}` | ✅ |

The closed loop: **select → recall → attempt → detect-signal → capture → index → prune.**
Every arrow has an owner; "attempt" has a wired LLM inner-agent path (not yet proven for
unattended use) and "detect/capture" was discretionary (this branch makes it a gate).

## The four gaps and their fixes

### Gap 1 — `inner_attempt()`'s LLM path is wired but unproven for unattended use (Phase 2, DONE 2026-06-09)
**Resolved on `js/feat/meta-learning-inner-agent`:** added per-cycle telemetry
(`inner_agent_telemetry.py`), fixed the dominant failure mode (cited_sources
strict-parse → 40% fallback, now lenient-drop), pinned the capture-gate base
per-cycle, and added exact token+cost accounting via the json envelope. An
8-cycle pilot passed every quantitative criterion (0% fallback, 100% parse, 0
timeouts, 0 crashes, ~$0.27/cycle) → **CONDITIONAL GO** for Phase 3
(`docs/wiki/findings/inner-agent-first-run.md`, bar in
`docs/agent/inner-agent-readiness.md`). Original framing below.

`inner_attempt(problem)` already has a **headless Claude Code agent** path
(`_try_llm_path` → `claude_headless`, landed on feat-autonomous-loop Goal 7.7): it renders
the inner-agent prompt, runs the math-solving-protocol via `claude -p`, parses the
structured reply, and threads score/payload to auto-submit. What remains (Phase 2) is
*proving it for unattended use* — sustained reliability, cost/budget behavior, and quality
of the agent's captures across many cycles. Until then the loop is operated attended. Its
own branch; must be proven before Phase 3.

### Gap 2 — capture is discretionary (Phase 0, THIS branch — highest leverage)
Add a **`Stop` hook** (`.claude/hooks/capture-gate.sh`, mirroring `wall-detector.sh`) that
blocks session end unless, this cycle, there exists **(a)** a new `cycle-log.md` row AND
**(b)** at least one new/edited `findings/` or `concepts/` page with valid frontmatter +
≥1 cite. No *cited, verified* capture → no clean exit. This is exactly the mechanism that
was missing on 2026-06-08.

### Gap 3 — "high-quality signal" undefined (Phase 1, THIS branch)
Formalize a signal taxonomy in `record_cycle_row` (autonomous_loop.py) and auto-route:

| Signal (machine-detectable) | Auto-action |
|---|---|
| New record / top-3 | finding (positive) + propose technique + skill-library `top3++` |
| Dead-end (Δ<min after a wall) | `findings/dead-end-*.md` **with mandatory "what-might-still-work"** |
| Triple-verify disagreement | verifier-mismatch finding; flag submission |
| Mechanism verified on ≥2 problems | append to `promotion-log` (human-gated → concept) |
| Prior violated (e.g. a tie beaten) | finding + propose a rule edit |

### Gap 4 — no scheduler (Phase 3, BUILT 2026-06-09/10 — cron not yet armed)
**Status: built + supervised-tested on `js/feat/meta-learning-scheduler`.** Goal 0 cleared
Phase 2's entry conditions (R7 positive on write+cite branches, human R8 keep). Shipped:
`problem_priority.py` (priority = log-compressed headroom × category hit-rate ×
staleness, live-leaderboard our-score, empirical-Bayes prior, offline cache ladder),
`scheduled_cycle.py` (runs/day cap, hard timeout, run ledger; cron spec in docstring),
`scheduler_health.py` + `unattended-runbook.md`, connect-the-dots sibling-findings
injection, per-run cross-pollination surfacing. 7-run supervised rollout: reliability
green (15/17 LLM-path, ~$0.6/cycle, 0 spurious submits) but targeting initially ground
P12 from stale frontmatter + raw-headroom spread — fixed and live-verified (queue
P3→P10→P4). **Verdict: NOT yet unattended** — see
`docs/wiki/findings/scheduler-supervised-rollout-verdict.md` for the precondition list
(clean v2 attended window, weekly-audit habit, P7 onboarding).

## The non-negotiable: capture without pruning = spam (Phase 4, THIS branch)

Automatic self-capture, unchecked, fills the wiki with plausible-but-low-value findings the
agent writes to satisfy the gate — drift that *poisons recall*. Compounding requires quality
policing:

- **The capture-gate requires a *cited, verified* artifact** (not any file) — else it's gamed.
- **`skill-library` hit-rate demotion** — 0/N techniques demoted, not auto-suggested.
- **Promotion to concept stays human-gated** — the one mandatory human touchpoint.
- **Weekly `/wiki-audit`** (second cron) + a **finding-TTL/near-duplicate merge lint** (new,
  Phase 4).
- **Human review cadence** (~15 min/week) on `cycle-log` + `promotion-log`. Full autonomy on
  capture, human on promotion — that asymmetry is the safety.

## Phased rollout

- **Phase 0 — `Stop` capture-gate hook.** Cheapest, biggest behavior shift. (this branch)
- **Phase 1 — signal taxonomy + auto-route** in `record_cycle_row`. (this branch)
- **Phase 4 — anti-bloat lint** (finding-TTL / near-duplicate merge) + metrics view. (this branch)
- **Phase 2 — prove `inner_attempt()`'s headless agent** for unattended use. ✅ DONE
  (`js/feat/meta-learning-inner-agent`, CONDITIONAL GO).
- **Phase 3 — cron scheduler** for the unattended loop. (follow-on; gated on Phase 2's
  two entry conditions: a non-frozen pilot + human R8 spot-check.)

## How we'll know it's actually compounding (measure it, or it's theater)

Track in `docs/agent/metrics.md`:
- **time-to-record per problem** ↓
- **technique hit-rate trend** ↑
- **cite-reuse rate** — how often a new cycle cites a *prior* cycle's finding (direct
  evidence of compounding). If this isn't rising, the loop runs but doesn't compound.
- **% cycles where recall preceded the winning move.**

Honest framing: this makes the loop **run reliably and compound**; it does not guarantee hard
problems fall. Meta-learning amplifies a capable inner agent — and would equally amplify a
weak one's drift, which is why the quality gates are not optional.

## Open questions

- ~~What exactly counts as "verified" for the capture-gate's cite requirement (triple-verify
  pass? any cite? a cite to `source/`)?~~ **Resolved (Phase 0):** *any cite* — a non-empty
  `cites:` frontmatter list (canonical; 99/100 findings use it) OR an inline
  `docs/source/`/`docs/wiki/`/URL/arxiv reference. Triple-verify gates *submission*, not
  *capture*; the anti-bloat lint (Phase 4) + human promotion gate are the bloat counters, so
  the capture cite-bar stays low to avoid trapping honest dead-ends. (`docs/tools/capture_gate.py::has_cite`.)
- ~~Should the `Stop` hook hard-block or warn-then-log on first offense?~~ **Resolved (Phase 0):**
  mode is `EINSTEIN_CAPTURE_GATE` = `warn` (default) | `block` | `off`. Default `warn` on first
  rollout (non-trapping nag). `block` honors the Stop-hook `stop_hook_active` guard so it blocks
  at most once per stop-chain — never traps a session mid-debug. Per-cycle scoping via
  `EINSTEIN_CAPTURE_GATE_BASE` (default `main`; the autonomous loop sets it to pre-cycle HEAD).
  (`.claude/hooks/capture-gate.sh`.)
- ~~Signal-detection false-positive rate: how to keep `record_cycle_row` from over-firing the
  "promote" action.~~ **Resolved (Phase 1):** the human-gated `promote` (cross-problem
  mechanism) fires only at `mechanism_problem_count ≥ 2`, and the live loop passes the
  conservative default `1`, so it stays dormant until a real cross-cycle counter feeds it;
  routing additionally dedupes both the promotion-log candidate and the `rule_edit` proposal
  against what already exists. Routing never auto-promotes and never fabricates finding prose
  — the Phase-0 capture-gate enforces the prose got written.
  (`src/einstein/meta_loop/signal_taxonomy.py`, `scripts/autonomous_loop.py::_route_cycle_signals`.)
