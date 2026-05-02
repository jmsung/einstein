# Axioms — L0 invariants

L0 rules. Require explicit human approval to change. Slim by design — if a rule is at L0, removing it would break something fundamental.

## A1 — Triple verification

Every score MUST be verified three ways before trusting:

1. Fast local evaluator (the optimization loop)
2. Exact / independent reimplementation (different code path)
3. Cross-check against a known analytical bound or different method

If any two disagree, the score is fake — debug before proceeding. See [triple-verify](triple-verify.md) for the procedure.

**Why L0:** local-evaluator drift from arena verifier has caused real damage (P9 hidden, P14 tolerance, P17 strict-tol trap). Single-evaluator scores are not trustworthy. Triple-verify is the floor.

## A2 — No external posts

All wisdom and knowledge sharing happens on this repo + wiki. Never on:
- Einstein Arena discussion threads
- Blog posts (personal or company)
- Social media
- Slack / Discord public channels

The repo + wiki *is* the publication channel — auditable, version-controlled, growing in commits. External posts duplicate effort, drift from the canonical record, and invite low-quality reply threads.

**Why L0:** the wiki is the artifact; external posts dilute it. Also: the wiki is built for *math wisdom*, not promotion.

## A3 — Solution backup

Solutions are the most important artifact. Never lose a solution.

- **When**: after any optimizer run that produces a new record or competitive score; before any destructive operation; after arena submission; during `/worktree-done`.
- **Where**: `mb/tracking/problem-{id}-{slug}/solutions/` with filename `solution-{branch}-{score}.json`. Maintain a `solution-best.json` symlink/copy.
- **Reproduction recipe** in tracking `strategy.md`: exact command, key params (seeds, iterations, phase order), expected score range, time estimate.

**Why L0:** solutions are the crystallized output of long compute campaigns. Loss is irrecoverable; cost is high. The publication-layer rule (`scripts/promote_to_mb.py`) keeps the publication layer clean by construction.

## A4 — Compute pre-audit

Before launching ANY compute job (local or cloud):

1. **Profile** the bottleneck stage. Identify whether it's parallelizable.
2. **Match** to compute environment via the [compute-router](compute-router.md) decision matrix.
3. **Run the GPU benchmark** if Modal: `python -m einstein.gpu_tempering.benchmark --solution <path>`. Follow its recommendation (`STAY ON CPU` / `USE GPU VANILLA` / `CONSIDER TRITON`).
4. **Cost estimate** for Modal: `hours × $/hr`. Only proceed if speedup > 3× over local.
5. **Verify GPU utilization** > 50% if running on Modal. Below 50%, the workload is wrong-fit.

**Why L0:** running sequential Python on GPU wastes money AND is slower than CPU. Running parallel float64 on local CPU is a wall-clock disaster. Pre-audit catches both.

## Submission policy (not an axiom — a rule)

Submit ONLY when a result represents a qualitative new claim. Local triple-verify is the closed loop; submission is the second-rate signal that catches local↔arena drift.

- User explicitly approves each submission
- Floor: 1 hour between submissions on the same problem
- Practical cadence: 1–3 submits per problem per week, sometimes zero
- Never to defend rank, never for incremental polish, never promotional

(Was old A2 — demoted from axiom because it's procedural, not invariant.)

## What's NOT in the axioms

These are deliberately demoted from L0:
- ~~Top-3 + human approval gate for submission~~ → submit only for verification, much narrower
- ~~Public-repo-security~~ → cb is the public artifact; mb is private; no separate "secret methodology" layer
- ~~Never push branches to remote~~ → branches push freely; nothing to hide
- ~~Publication-layer discipline~~ → still real, but a tooling rule (`promote_to_mb.py`), not an axiom

The slim list above is the actual L0. Everything else is procedure that can be tuned.
