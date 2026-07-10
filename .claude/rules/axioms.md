# Axioms — L0 invariants

L0 rules. Require explicit human approval to change. Slim by design — if a rule is at L0, removing it would break something fundamental.

## A1 — Triple verification

Every score MUST be verified three ways before trusting:

1. Fast local evaluator (the optimization loop)
2. Exact / independent reimplementation (different code path)
3. Cross-check against a known analytical bound or different method

If any two disagree, the score is fake — debug before proceeding. See [triple-verify](triple-verify.md) for the procedure.

**Why L0:** local-evaluator drift from arena verifier has caused real damage (P9 hidden, P14 tolerance, P17 strict-tol trap). Single-evaluator scores are not trustworthy. Triple-verify is the floor.

## A2 — Open participation, wiki-canonical (revised 2026-07-03, human-approved)

External sharing is **allowed and encouraged** — arena discussion threads first and
foremost (the platform's own contract asks for it: *"after you submit, share what you
learned"*). The wiki remains the canonical record. Guardrails:

1. **Wiki-canonical**: every post distills from a wiki finding/concept and links back.
   Posts never fork the record — if it isn't in the wiki yet, write the wiki page first.
2. **Share after the move lands, with an n+1 embargo** (revised 2026-07-04, human):
   findings post AFTER the corresponding submission is evaluated AND the *next* rung
   of the same campaign is already running/banked ("push first, run first"). Method
   details that would let a higher-compute rival leapfrog (laws, constants, next-step
   direction) get an explicit time delay — default: hold until the follow-up move is
   on the board; the user can set longer embargoes per item. Never leak a live edge.
3. **Human-gated, ALWAYS — no auto-post** (revised 2026-07-07, human-approved; supersedes
   the 07-04 campaign-loop carve-out): every external post requires explicit human
   approval + confirmation before sending. There is NO autonomous post path — the
   campaign loop and any autonomous loop DRAFT posts only (to `mb/posts/drafts/`) and
   keep moving; a human reviews the draft and sends it (`post_update.py … --send`).
   Auto-**submit** (A2 submission policy, 6-gate chain) remains the ONLY outward action
   the loop takes without a human. Rationale for tightening: the forward-progress loop and
   the outward post are decoupled — the loop never blocks on the human (it advances to the
   next action item immediately after submitting), and the human is never bypassed on what
   goes public. Both properties hold at once; that is the point.
4. **Quality bar**: numbers, verifiable claims, honest negatives — the field's norm.
5. **Board-verifiable claims lead** (learned 2026-07-04, 4-variant A/B): the arena's
   moderation queue passes only posts whose headline numbers it can replay against
   server data (an evaluated submission id + score). Internal/honest bases that were
   never submitted get the post REJECTED regardless of framing; present them only as
   derivations from a board-visible result. Naming other agents is fine (skill.md
   encourages it). See finding `arena-thread-moderation-verifiable-claims.md`.

**Why the flip** (was "No external posts", 2026-05): recon of the P7 threads (2026-07-03)
showed the field already shares its methods openly (MAOJIASONG posted their tolerance
exploit; Asper posts negatives), our cb repo is public anyway, and the platform +
operators' paper treat discussion as the core mechanism. Silence had ~zero competitive
value and real costs: no recognition, no lineage credit, no reply-thread intel. The
original A2 rationale (drift, duplicated effort) is preserved by guardrail #1.

**History**: JSAgent posted 3 P7 threads in 2026-04; A2 then froze posting in 05; the
one-paper carve-out (2026-06-22, methodology paper) is subsumed by this revision. The
methodology paper was made **personal/private** on 2026-07-09 (moved to `mb/paper/` and
purged from public cb history) — it is no longer a public arXiv artifact, and nothing in
this repo publishes it. Arena discussion posting (above) is unaffected.

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
