---
type: finding
author: agent
drafted: 2026-05-25
question_origin: branch-js-feat-meta-loop
status: pending-first-run
related_concepts: []
related_techniques: []
cites:
  - meta-loop-design-from-literature.md
---

# Meta-loop first unattended run — distillation (scaffold)

## Status: pending the first actual run

This page is a *scaffold*. It exists so:

- the meta-loop's own audit trail visibly closes the gap → ingest → distill loop
  for this branch (per `cycle-discipline.md`);
- the operator (Jongmin) has a template to fill in the morning after the
  first unattended overnight run;
- subsequent meta-loop iterations have a stable target to update.

When the first run has happened and proposals have been reviewed, replace
this body with the real distillation and set `status: answered`.

## What this finding will cover when filled in

### 1. What did the meta-loop propose?

| date | proposal_id | type | target_path | gate decision | shadow | accepted? | commit |
|---|---|---|---|---|---|---|---|
| (pending) | … | … | … | accepted/rejected/shadow-pending | n/a | y/n | sha |

Per `meta-loop-design-from-literature.md`, the design predicts that a
disproportionate share of the *useful* proposals are `new_question` —
read-only artifacts that close gaps from the cycle log. Track whether
that prediction held.

### 2. Which proposals were obviously good?

- (pending)

A "good" proposal here means:
- the human accepted it on first read;
- the predicted regression list captured the actual risk;
- the evidence cycles cited were the right ones.

### 3. Which proposals were obviously bad — and what was the failure mode?

- (pending)

Per `failure-is-a-finding.md`, every rejected-but-reasonable proposal
should get its own dead-end finding. Index those here.

Predicted failure modes from the literature anchor:

- **Goodhart on cycle-log metrics** (HyperAgents). If the proposer optimizes
  *findings/cycle*, it may propose "write more dead-end findings even when
  they aren't useful." Watch for low-quality dead-end inflation.
- **Self-attribution asymmetry** (AHE). Predicted regressions of accepted
  proposals turn out wrong ~89% of the time. Track which actual regressions
  the proposer FORESAW.

### 4. What generalized vs what was math-specific?

The branch's core thesis (per the literature finding):

| Component | Predicted: portable | Predicted: math-specific |
|---|---|---|
| Proposal schema | ✅ | — |
| Gate chain | ✅ | "evidence" interpretation |
| Audit log writer | ✅ | column choices |
| Shadow A/B harness | ✅ | what Δ means |
| Filesystem-as-feedback | ✅ | which files |
| Inner loop | — | autonomous_loop.py |

Fill in after the first run: which of those predictions held when the
proposer actually ran. Surprising re-classifications go here.

### 5. What did the meta-loop *fail to surface* that the human noticed?

This is the most important section. The meta-loop has zero value if
the human ends up doing the same diagnosis manually anyway. Track:

- (pending)

### 6. Did the meta-loop budget hold?

- expected: ~5K tokens per propose() run, 1 run/day → ~150K/month
- actual: (pending)
- `mb/logs/meta-loop-budget.md` is the receipt

### 7. Shadow A/B results (Goal 5)

If any proposal triggered shadow A/B during the first run:

- proposal_id:
- n_cycles per arm:
- Δfindings/cycle:
- Δscore_changed/cycle:
- a_wins:
- promoted to applied?:

If no proposal triggered shadow A/B (likely for a first run of mostly
`new_question` type), note that and move on.

## Open questions to file (per `self-improvement-loop.md`)

- (pending — after the first run)

## How to operate this scaffold

When you (or a future agent in this branch) are ready to fill this in:

1. Run the meta-loop manually (or wait for the launchd schedule to fire):

   ```bash
   uv run python scripts/meta_loop.py diagnose
   uv run python scripts/meta_loop.py propose
   ```

2. Review pending proposals:

   ```bash
   uv run python scripts/meta_loop.py review --list
   uv run python scripts/meta_loop.py review
   ```

3. For shadow-pending proposals, fire the harness:

   ```bash
   uv run python scripts/meta_loop.py shadow <proposal_id> --n-cycles 10
   ```

4. Replace this scaffold with the real distillation; flip `status: answered`.

## See also

- [meta-loop-design-from-literature](meta-loop-design-from-literature.md)
- Branch: `js/feat/meta-loop` — `mb/active/js-feat-meta-loop.md`
- Schedule: `docs/ops/com.einstein.meta-loop.plist`
- CLI: `scripts/meta_loop.py` ({diagnose,propose,review,shadow})
