---
type: home
author: hybrid
drafted: 2026-05-02
updated: 2026-05-23
status: live
---

# einstein-wiki — math wisdom from a self-improving agent

This wiki is a math knowledge base co-authored by a human and an AI agent through the practice of solving Einstein Arena problems. The arena is the **gym**. Math is the **verifiable system**. The agent is the **subject**. The wiki is the **artifact**.

## The thesis

Math is one of the few systems where an agent's claimed understanding can be **verified objectively**: the answer is right or wrong, the bound holds or doesn't, the score is reproducible. Most agent-capability benchmarks rely on judges, rubrics, or human evaluation — all noisy. Einstein Arena is brutal and exact. That makes it a near-ideal test bed for measuring how far a well-organized agent can actually push the limit of mathematics.

The plan: the agent solves problems, fails, reflects, writes back to this wiki, and keeps going. Wisdom compounds across cycles in the wiki the same way understanding compounds across generations in biological evolution — selection on what worked, retention of what generalizes, ruthless pruning of what didn't. Over time, the agent should become measurably better at solving hard math problems by *its own* effort, with this wiki as its persistent memory.

## What's in here

| Section | What lives there |
|---|---|
| [`problems/_inventory.md`](problems/_inventory.md) | concept-coverage compass across 23 arena problems (the project's compass) |
| [`personas/_synthesis.md`](personas/_synthesis.md) | the 12 stances drawn from how the great mathematicians actually work |
| [`concepts/`](concepts/) | WHAT-IS — durable mental models (LP duality, equioscillation, Cohn–Elkies bound, modular forms, basin rigidity, parameterization selection, …) |
| [`techniques/`](techniques/) | HOW-TO — concrete methods (parallel tempering, mpmath ulp polish, Remez exchange, SDP flag algebra, compute router, …) |
| [`personas/`](personas/) | embodied perspectives — Gauss, Riemann, Tao, Conway, Cohn, Razborov, Polya, Hilbert, Grothendieck, Atiyah, Wiles, … |
| [`findings/`](findings/) | specific Q→A pages with cites |
| [`problems/`](problems/) | one short index page per arena problem + the inventory matrix |
| [`questions/`](questions/) | open math questions awaiting research |
| [`../source/`](../source/) | distilled summaries of papers, repos, blogs (1:1 with the gitignored `../raw/`) — see [`../source/INDEX.md`](../source/INDEX.md) for the browsable manifest of the **197-paper corpus** |
| [`../.claude/rules/`](../.claude/rules/) | behavioral rules — the agent's policy layer |
| [`../tools/`](../tools/) | autonomous-loop tooling — see [`../tools/README.md`](../tools/README.md) for the full index (concept_inventory, seed_ingest, pdf_to_md, calibrate, monitor, wiki_lint, strategy_picker, autonomous_loop) |

## How knowledge gets in

```
single artifact      → /wiki-ingest <url>           (human-gated, atomic raw/+source/)
                       ├──→ ../raw/<stem>.pdf       (gitignored local cache)
                       └──→ ../source/<stem>.md     (in-git distillation)

bulk arxiv ingest    → docs/tools/seed_ingest.py    (agent-driven, batch)
                       propose / author-sweep / citation-crawl
                       → candidates JSON → human-approve → apply (parallel + batch JVM)

conversation insight → /wiki-learn                  (turns a session into wiki pages)
question / finding   → wiki/<category>/<slug>.md    (frontmatter author: agent|human|hybrid)
```

`raw/` is gitignored; `source/` is the canonical in-git record. Wiki pages are synthesized — by either human OR agent, with mandatory attribution and the same quality bar regardless of author. The agent reaches the wiki layer via the underlying tools (`qmd`, `wiki_graph`, `seed_ingest`, `wiki_lint`) — the `/wiki-*` skills sit on top for the human's interactive surface.

## How the agent solves a problem

The full procedure lives in [`../.claude/rules/math-solving-protocol.md`](../.claude/rules/math-solving-protocol.md). At a glance:

```
understand → wiki-first → council dispatch (questions, not solutions)
                       → gap detect → research → distill → wiki page
                       → specialize (n=2,3,4 by hand) → execute
                       → look back (generalize) → failure log → cycle
```

Compute is routed per workload: local workstation for sequential and float32 batch; Modal cloud for sustained float64 GPU. See [`techniques/compute-router.md`](techniques/compute-router.md) and [`../.claude/rules/compute-router.md`](../.claude/rules/compute-router.md).

## Operating principles

1. **Math wisdom is the goal**, not arena rank. Submission is verification only — minimum 1 hour between submissions per problem; user-approved.
2. **Failure is a finding** — every dead-end lands in `findings/dead-end-*.md` with the *why*. The next breakthrough sits on yesterday's articulated obstruction.
3. **Wiki-first lookup** — query the wiki before paraphrasing from training. The wiki is the project's source of truth.
4. **Attribution is mandatory** — `author: agent | human | hybrid` on every page. The cycle log measures self-improvement by tracking the mix.
5. **Compute routing** before launching — local CPU / local MPS / Modal cloud, per workload.
6. **Triple-verify** every score before trusting (fast eval + exact reimpl + cross-check vs analytical bound).
7. **No external posts** — the wiki is the publication channel.

See [`CLAUDE.md`](CLAUDE.md) for the full machine-readable contract.

## Why publish this

The wiki, the rules, the agent code, and the cycle log together form a **legible record** of an agent attempting to do real mathematics. If it works, it's evidence that well-organized self-learning can push the limit. If it doesn't, the record is itself the lesson — auditable, falsifiable, public. Either outcome is useful to the field.

## Status

Live as of 2026-05-23. Started 2026-05-02 from a private memory bank, scaled to a 197-paper source/ corpus + 180-page synthesis layer + autonomous orchestrator under `scripts/autonomous_loop.py` driving 22 cycles to date. The autonomous loop runs under `/loop` or cron via `docs/tools/cycle_runner.sh`; per-device compute calibrations live at `docs/agent/calibrations/<device-key>.json`. Conventions are still tightening — `docs/tools/wiki_lint.py` surfaces drift; `docs/source/INDEX.md` is the live paper manifest.
