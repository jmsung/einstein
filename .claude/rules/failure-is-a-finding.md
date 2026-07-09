# Failure is a finding

Every dead-end becomes a `knowledge/wiki/findings/dead-end-<slug>.md` with the *why*. No exceptions.

**Why:** Tomorrow's breakthrough sits on yesterday's articulated obstruction. Riemann's notebooks, Tao's blog, Wiles's seven-year diary — all are full of failed approaches *with reasons*. Failure without articulated why is wasted compute. Failure with articulated why is data the next cycle stands on.

In this project specifically, failure findings have already paid for themselves multiple times: `findings/sdp-relaxation-uselessness` (P1), `findings/three-way-local-optimality-proof` (P1), `findings/equioscillation-active-triple-diagnostic` (P15/P16). Each one ruled out a class of approaches across multiple problems.

**How to apply:**

When an approach fails (does not improve the score, hits a wall, gets rejected, etc.), **before moving on**, write:

```yaml
---
type: finding
author: agent | human
drafted: YYYY-MM-DD
question_origin: problem-{id}
status: answered    # because the question "does X work?" got an answer (no)
related_concepts: [...]
cites: [...]
---

# Dead end: <approach name> on <problem / category>

## What we tried
- Concrete description; commands run; params used.

## Why it failed
- The OBSTRUCTION. This is the value of the page.
- Not "it didn't improve" — that's the symptom. Why didn't it improve?
- Examples of good obstruction articulation:
  - "SDP relaxation has rank-1 primal optimum; lifting destroys this and the bound becomes loose."
  - "Smooth-max β-cascade above 1e8 saturates float64 — gradient zeroes."
  - "minImprovement gate at 1e-7 with our delta of 8e-9 → silent rejection regardless of true score."

## What this rules out
- The class of approaches this failure invalidates. (Often broader than the specific approach.)

## What might still work
- The next door, given this obstruction.
```

**The "What might still work" section is load-bearing — not garnish.** It is where the
next cycle's breakthrough is pre-written. **Triggering incident (2026-06-08):** the P2
arena record (1.5028609 → 1.5028506, the branch's first record) came *verbatim* from
the "what might still work" of a dead-end finding written 4 days earlier
(`dead-end-p2-cold-seed-fixed-window.md` → warm self-pruning). The agent did not invent
the move that session; it executed a prescription the failure-log discipline had already
written down. So: when you write a dead-end, spend real effort on the next-door section —
name a *concrete, untried* operator, not a vague "try harder." And when you *start* a
problem, read the prior dead-ends' next-door sections first — the breakthrough may already
be on the page. See [n-agent-tie-not-global-min](../../knowledge/wiki/concepts/n-agent-tie-not-global-min.md).

**Filename pattern:** `knowledge/wiki/findings/dead-end-<approach>-<problem-or-class>.md`

**Threshold:** A "failure worth a finding" is one that would have been worth trying — i.e., the approach was reasonable a priori. Trivial misconfigurations don't qualify. The test: would a peer mathematician/agent have considered this approach and learned something from why it didn't work?

**Anti-pattern:** Going to the next approach without writing the finding. Each session's worth of failures = a session's worth of wisdom *only if filed*.

**Triggering pattern:** any session-end where ≥1 approach was abandoned without producing a finding for each. Block end-of-session until filed.

See also: [self-improvement-loop](self-improvement-loop.md), [math-solving-protocol](math-solving-protocol.md) step 10, [knowledge/wiki/findings/README](../../knowledge/wiki/findings/README.md).
