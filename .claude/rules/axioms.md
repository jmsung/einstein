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
- **Where**: `mb/problems/{id}-{slug}/solutions/` with filename `solution-{branch}-{score}.json`. Maintain a `solution-best.json` symlink/copy.
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

**Revised 2026-05-24**: human-approval gate replaced with an auto-submit gate chain for **new arena records only**. The autonomous loop may auto-submit IFF every gate below passes; otherwise the candidate is logged for human review.

Auto-submit gates (all must pass):

1. **Strict improvement over current arena #1 SOTA** — fetched live via `check_submission.check_leaderboard(problem_id)`. Our score must beat the arena leader by ≥ per-problem `minImprovement` (default 1e-8). Beating only our own prior best is NOT sufficient.
2. **Triple-verify passes** (per A1) — all 3 evaluators agree within tolerance. Any 2-way disagreement → no submit, write a finding.
3. **1-hour throttle per problem** — `mb/logs/auto-submit.md` is the source of truth; reject if last auto-submit for this problem_id < 1h ago.
4. **Daily cap** — default 5 auto-submissions/day across all problems. Configurable via env.
5. **Kill switch** — `EINSTEIN_AUTO_SUBMIT=0` disables all auto-submission. Default-on for the autonomous loop; set to 0 to revert to human-approved-only.
6. **Audit log mandatory** — every decision (submit / reject + reason) appended to `mb/logs/auto-submit.md`. Human reviews weekly.

Non-auto cases — still requires human approval:
- Polish that doesn't beat arena #1 (e.g. rank-#2 / #3 squeeze for points)
- "Tied SOTA with floor configuration" (e.g. P22/P23 score-2 floor pattern)
- Any submission flagged by triple-verify with disagreement
- Submissions to retired or hidden problems

Was old A2 (human-approved every submission) — replaced by the gate chain above. The rationale for the change: a more powerful agent should be allowed to claim new arena records without round-tripping through human approval; the safety comes from the verification gates, not from the human-in-the-loop. Reviewers please push back if the audit log shows abuse.

## What's NOT in the axioms

These are deliberately demoted from L0:
- ~~Top-3 + human approval gate for submission~~ → submit only for verification, much narrower
- ~~Public-repo-security~~ → cb is the public artifact; mb is private; no separate "secret methodology" layer
- ~~Never push branches to remote~~ → branches push freely; nothing to hide
- ~~Publication-layer discipline~~ → still real, but a tooling rule (`promote_to_mb.py`), not an axiom

The slim list above is the actual L0. Everything else is procedure that can be tuned.
