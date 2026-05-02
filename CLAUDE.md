# einstein

JSAgent — an AI agent that solves hard math optimization problems on Einstein Arena, with a public knowledge base + behavioral rules co-evolved with the agent.

## Three layers, three contracts

This repo is the public artifact. It has three layers, each with its own contract:

| Layer | Path | Contract | What lives here |
|---|---|---|---|
| **Code** | `src/`, `scripts/`, `tests/`, `docs/`, `results/` | this file (below) | optimizer code, evaluators, per-problem scripts, public approach docs |
| **Wiki** | `wiki/` | [`wiki/CLAUDE.md`](wiki/CLAUDE.md) | math knowledge — concepts, techniques, personas, findings, problems, questions |
| **Rules** | `.claude/rules/` | [`.claude/CLAUDE.md`](.claude/CLAUDE.md) | behavioral rules for human + agent (one topic per file) |

`raw/` (gitignored) holds native originals; `source/` holds 1:1 LLM distillations. Both feed the wiki. Worktree tracking lives in `mb/` (private repo, sibling of cb).

## Goal

**Generalized math wisdom**, not arena rank. The agent solves problems, learns from failure, and writes back to the wiki. Each cycle compounds. Submission is a wisdom-verification tool, not a goal — minimum 6 hours between submissions per problem; user-approved each time. **No external posts** — all knowledge stays on this repo + wiki.

See [`mb/tracking/active/js-refactor-wiki-bootstrap.md`](../mb/tracking/active/js-refactor-wiki-bootstrap.md) for the full design rationale (during refactor; afterward see `wiki/home.md`).

## Setup

```bash
uv sync                                # install all deps
uv run python -m pytest tests/ -v      # run all tests
uv run ...                             # run scripts
modal run ...                          # GPU scripts (needs Modal account)
```

## Code conventions

### File organization
- `src/einstein/{problem}/` — per-problem subpackages (evaluators, verifiers)
- `src/einstein/optimizer.py`, `knowledge.py` — shared modules
- `scripts/{problem}/` — per-problem optimizer entry points (public)
- `tests/{problem}/` — per-problem pytest tests
- `docs/problem-{id}-{name}.md` — one public MD per problem (high-level approach + results only; deep wisdom goes in `wiki/`)
- `results/problem-{id}-{name}/` — result files (gitignored)

### Compute routing
Two first-class environments. Always route the workload before launching — see `wiki/techniques/compute-router.md` (when available) and `.claude/rules/compute-router.md`.

- **Local M5 Max (128GB)**: mpmath polish, sequential CPU optimizers (L-BFGS / NM / SLSQP), small basin-hopping, MPS float32 batch ops, large multistart with multiprocess
- **Modal A100/H100**: sustained float64 GPU parallel (parallel tempering, CMA-ES large-pop float64), large LP/SDP that's RAM-bound

### Triple-verify
Every score must be verified three ways before trusting: fast local evaluator, exact reimplementation, cross-check vs analytical bound or different method. If any two disagree, the score is fake.

### Submission discipline
- Submit ONLY when a result represents a qualitative new claim (novel basin, new approach, milestone, suspected verifier mismatch) — not every iteration
- Local triple-verify is the closed loop; submission is the second-rate signal that catches local↔arena drift
- User explicitly approves each submission
- Floor: **1 hour** between submissions on the same problem (avoid rapid-fire)
- Practical cadence: 1–3 submits per problem per week, sometimes zero
- No external posts (arena threads / blog / social) — wiki is the publication channel

## Workflow

`/where` → `/goal` → `/act` → `/commit` per the global skill set. Worktree state in `mb/tracking/active/<branch>.md`. Branch naming: `js/<type>/<description>`.

For math problems: every hard problem follows the **math-solving protocol** in `.claude/rules/math-solving-protocol.md` — understand → wiki-first → council dispatch → gap detect → research → distill → specialize → execute → look back → failure log.

## See also

- `wiki/home.md` — narrative front door of the math knowledge base
- `wiki/problems/_inventory.md` — concept-coverage compass across 23 problems
- `mb/tracking/progress.md` — branch state
