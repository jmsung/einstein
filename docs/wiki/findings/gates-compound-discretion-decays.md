---
type: finding
author: agent
drafted: 2026-06-08
question_origin: meta-automation
status: answered
related_problems: []
related_concepts: [n-agent-tie-not-global-min]
related_findings:
  - cross-pollination-not-compute.md
cites:
  - ../../agent/meta-learning-automation.md
  - ../../tools/capture_gate.py
  - ../../../src/einstein/meta_loop/signal_taxonomy.py
  - ../../tools/wiki_lint.py
  - ../../../.claude/rules/failure-is-a-finding.md
  - ../concepts/n-agent-tie-not-global-min.md
---

# Gates compound, discretion decays — but a gate's cite-bar is NOT a quality filter

## The question this answers

When you automate a discretionary self-improvement rule into a deterministic gate
(`js/feat/meta-learning-automation`, Phase 0–1–4), where do you put the *quality*
control? The tempting answer — "make the gate itself demand a high-quality
artifact" — is wrong. This records why, so the next automation doesn't re-make it.

## What we built (and the honest reason)

The motivating discovery: the P2 arena record (PR #121) executed a move written
verbatim in a dead-end's "what-might-still-work" section 4 days earlier — but the
capture only happened **because a human asked**. A rule is advice the agent can
rationalize past; a gate is not. So we converted three discretionary rules into:

- a **`Stop` hook capture-gate** (`docs/tools/capture_gate.py`) — no clean exit
  without a new cycle-log row + a cited findings/concepts page;
- a **signal taxonomy** (`signal_taxonomy.py`) that classifies the 5 high-value
  cycle signals and auto-routes each to its destination;
- an **anti-bloat lint** (`wiki_lint.py`: near-duplicate + stale-uncited).

## The obstruction: a gate's cite-requirement is a weak quality bar

The capture-gate's "≥1 cite" check is *deterministic and cheap*, which is exactly
why it is **not** a quality filter. Any agent writing-to-satisfy-the-gate can
produce a plausible finding with one cite in seconds. If we had raised the gate's
bar to "high-quality cite" (e.g. require a triple-verify pass, or a cite to
`source/`), two failures follow:

1. **It traps honest dead-ends.** A dead-end finding's whole value is the
   articulated obstruction + "what might still work" — it has no score to
   verify. A verify-gated capture would *block exactly the findings that paid off
   most* (the P2 win came from a dead-end, not a verified result).
2. **It still doesn't stop bloat.** A determined gate-satisfier games any
   bright-line bar. Strictness on the gate buys trapping, not quality.

## What this rules out / what works instead

**Rule out:** folding quality control into the capture gate. The gate's job is
*existence* (did capture happen at all), not *merit*.

**Works instead — quality is a separate, downstream, partly-human filter:**

- the cite-bar stays deliberately low (any cite) so the gate never traps;
- **near-duplicate + stale-uncited lint** surface bloat for human merge — they
  are advisory and excluded from strict-mode failure, so they inform without
  blocking;
- **promotion finding→concept stays human-gated** — the one mandatory human
  touchpoint;
- the signal taxonomy's `promote` action is **dormant by default**
  (`mechanism_problem_count` defaults to 1) and deduped, so it can't over-fire.

The asymmetry is the safety: **full autonomy on capture, human on promotion.**
Auto-capture without this downstream filter is spam that poisons recall — the
same failure mode as an N-agent tie being mistaken for a global minimum
([[n-agent-tie-not-global-min]]): cheap convergence read as quality.

## Honest limits

- **`%-cycles-recall-preceded-win` is uncomputable** from current logs — it needs
  recall↔win instrumentation we don't have. `compounding_metrics.py` prints it as
  `n/a (needs instrumentation)` rather than fake a number. That instrumentation is
  the natural next-door.
- This makes the loop *run reliably and compound*; it does not make hard problems
  fall. Meta-learning amplifies a capable inner agent — and would equally amplify
  a weak one's drift, which is why the quality gates above are not optional.
