# Artifacts & Reproduction — *JSAgent: Compounding Mathematical Discovery Through Persistent Agent Memory*

This file maps the paper's load-bearing claims to public files in this repository and gives
exact, verified commands to reproduce them. It is honest about what is and is not reproducible.

**Repository:** `github.com/jmsung/einstein` · **Paper snapshot tag:** `paper-v1`
**Setup:** `uv sync` (installs deps incl. the `einstein` package and evaluators).

All commands below were run on 2026-06-23 and their outputs recorded verbatim.

---

## 1. What is public here

| Artifact | Path | Notes |
|---|---|---|
| Behavioral rules (the harness) | `.claude/rules/` | one rule per file; read into the agent each session |
| Knowledge base | `knowledge/wiki/` (concepts, techniques, findings, problems, questions), `knowledge/source/` | the durable artifact the paper is about |
| Self-improvement layer | `docs/agent/` | cycle-log, skill-library, metrics, wall-ledger |
| Per-problem optimizer code | `scripts/<problem>/`, `src/einstein/<problem>/` | search + evaluators |
| Committed construction seeds | `scripts/<problem>/seeds/best.json[.gz]` | in-repo, deterministic, no dependence on private data |
| Standings sweep | `scripts/leaderboard_standings.py` | hits the arena's public endpoints; no API key |

**Not public in this repo:** downloaded competitor SOTA files and run outputs under `results/`
(gitignored); the private memory-bank `mb/` (tracking, logs, some solution backups); and the
methodology paper (personal — kept in private `mb/paper/`). The *seeds above* are the in-repo,
self-contained constructions; they do not depend on those trees.

---

## 2. Reproducing the headline constructions

These re-score committed seeds through the audited evaluator (triple-verify checks #1+#2 in one
path). Scores are deterministic.

### P18 — circles in a rectangle (clean rank-#1, both snapshots)
```bash
uv run python scripts/verify_seed.py --problem-id 18
# → P18 (circles-rectangle): rank-current basin score = 2.36583238397775
```
Paper value: `2.3658323852`. Matches to ~9 significant figures; strictly feasible (the
uniform-radius-shrink fallback guarantees `evaluate_strict` agreement — see §P14/P18 of the paper).

### P14 — circle packing in a square (clean rank-#1, both snapshots)
P14 is not wired into `verify_seed.py`; score its committed seed directly:
```bash
uv run python -c "import json; from einstein.circle_packing_square import evaluator as e; \
d=json.load(open('scripts/circle_packing_square/seeds/p14_canonical.json')); \
print('evaluate      =', e.evaluate(d)); print('evaluate_strict=', e.evaluate_strict(d))"
# → evaluate       = 2.6359830849175245
# → evaluate_strict = 2.6359830849175245
```
Paper value: `2.6359830849`. `evaluate == evaluate_strict` ⇒ strictly feasible (tol = 0), i.e.
a legitimate near-ceiling result, not a tolerance-band exploit (paper §"Verifier tolerance
versus invalid exploitation").

### P2 — first autocorrelation inequality (former record, since surpassed)
The committed seed reproduces the **full-support basin**, not the record:
```bash
uv run python scripts/verify_seed.py --problem-id 2
# → P2 (first-autocorrelation): rank-current basin score = 1.50286285859919
```
The **record** value `1.5028506` (2026-06-08, rank #1 until surpassed by Hyra on 2026-06-23)
was produced by warm data-driven self-pruning, not by re-scoring this seed:
```bash
uv run python scripts/first_autocorrelation/self_pruning_search.py   # search; warm, multi-cycle
```
This is the honest distinction: the seed gives the basin; the record is the self-pruning output.
The methodology trace (dead-end finding → warm self-pruning → record) is documented in
`knowledge/wiki/findings/p2-warm-self-pruning-beats-record.md`.

---

## 3. Reproducing the standings snapshots

```bash
uv run python scripts/leaderboard_standings.py --agent JSAgent
```
Emits the live board (problem, JSAgent score, rank, leader). The paper reports two dated
snapshots (2026-06-22, 2026-06-23); the board is dynamic, so current output will differ —
that is by design (paper §3). Frozen 06-22 reading:
`knowledge/wiki/findings/arena-standings-snapshot-2026-06-22.md`.

---

## 4. What is *not* reproducible (stated plainly)

- **The agent trajectory.** Exact per-cycle model identities were not pinned (the agent ran on
  the strongest available Claude model over the campaign). The *constructions and verifier
  outcomes* are reproducible; the *sequence of agent actions* is auditable (cycle logs) but not
  bit-for-bit replayable.
- **Causal effect of the knowledge base.** No cold-vs-warm ablation has been run; the paper's
  memory-reuse evidence is observational. This is the stated primary next step.
- **Heavy search from cold.** The per-problem search scripts are stochastic and compute-heavy;
  re-running them need not reproduce the exact submitted float. The deterministic, auditable
  path is re-scoring the committed seeds (§2).

---

## 5. Environment

- `uv sync` pins dependencies via `pyproject.toml` / `uv.lock`.
- Python 3.13. Numerical compute: campaign-era work used a MacBook Air (M4) local plus Modal
  cloud for a few heavy campaigns (notably kissing d=11); since 2026-05-24 all work runs on a
  a local workstation (ample unified memory, MPS) with Modal retired. LLM inference: Claude Code (Max
  subscription).
- Known nondeterminism: multi-start search seeds, thread scheduling; the seed-rescoring and
  standings paths are deterministic.
