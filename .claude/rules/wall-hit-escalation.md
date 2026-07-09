# Wall-hit escalation — when stuck, consult wisdom BEFORE more brute force

When you hit a wall, **STOP brute-forcing and escalate to the wiki + council first.**
This is REFUSING, like the cycle-start qmd query in [cycle-discipline](cycle-discipline.md):
do not launch another compute attempt until the escalation below is done.

**Why (the triggering incident):** On `js/feat/p4-record-breakthrough` (2026-06-06)
the agent hit the ~1.4525 basin wall and ran **10+ optimizer variants over hours**
(smooth-max, basin-hop, LP, escapes, neg-nudge, greedy-noise, fine cascade) before
consulting the wiki/council — and only when the human forced it. The council
(Tao/Hilbert/Cohn/Hadamard) then diagnosed the obstruction (discrete incompressible
sign topology) and ruled out whole families **in minutes**. Hours of compute would
have been saved by escalating at the 2nd failure. The wiki exists so the agent gets
smarter from past experience — brute force after a wall is the opposite of that.

## The wall trigger (any ONE — concrete, self-checkable)

You are at a wall when:
- **2 consecutive attempts** on the same objective fail to improve it past noise
  (Δ < the problem's `minImprovement`, or < 1e-3 relative), OR
- you have **retuned the same method ≥ 2×** (same algorithm class, new hyperparams), OR
- **≥ 3 compute launches** or **> ~30 min wall-clock** on one sub-goal with no metric gain, OR
- you catch yourself about to write *"let me try [a variant of what just failed]."*

If any holds, the next action is the escalation — NOT another run.

## The escalation (mandatory, in order)

1. **Name the obstruction** as a one-line question — write it to
   `knowledge/wiki/questions/` ([ask-the-question-first](ask-the-question-first.md)).
2. **Check accumulated wisdom FIRST** — before any new idea:
   - `grep` / read `docs/agent/wall-ledger.md` for this obstruction class. **If a
     past wall matches, jump straight to its recorded resolving move.** This is the
     compounding step — never re-grind a solved wall.
   - `qmd query` the problem + obstruction + "dead-end" against `einstein-wiki`
     ([wiki-first-lookup](wiki-first-lookup.md)).
3. **Re-dispatch the council** ([council-dispatch](council-dispatch.md)) — 3–5
   personas seeded with: the problem, **the attempts that failed AND why**, and the
   named obstruction. Each proposes ONE concrete NEW move *outside the failed class*.
   (This OVERRIDES "run council once per problem" — a wall is a re-trigger.)
4. **Implement the highest-conviction NEW move** before any further retuning of the
   failed approach.
5. **Append a wall-ledger row** (`docs/agent/wall-ledger.md`): obstruction, attempts
   tried, wisdom consulted, resolving move, outcome. Whether it worked or not — a
   ruled-out family is wisdom the next cycle stands on.

## Anti-patterns (explicitly forbidden)

- Running a 3rd+ variant of a failed approach without escalating.
- Treating council dispatch as recon-only ("already ran it at the start").
- Escalating to the human for a hint *before* re-dispatching the council and grepping
  the ledger — the wisdom layers come first; the human is the last resort
  ([the missing-info ladder](../../CLAUDE.md)).
- Hitting a wall and NOT writing a ledger row — the next agent re-grinds it.

## Floor claims need an untried operator OR a proof (don't close honest-zero prematurely)

Before declaring **"this is the floor / honest-zero / the record is unbeatable"** on a
record attempt, run this check — it is a *refusing* gate, like the escalation above:

1. **Is the "floor" just an N-agent empirical tie?** Several independent solutions
   converging to the same score is evidence of a **sharp shared basin**, not a proof of
   global optimality. Same-method searchers share parameterizations and operators, so
   they fall into the same basin — the tie measures the basin's attractor, not the
   absence of other basins. (Concept: [n-agent-tie-not-global-min](../../knowledge/wiki/concepts/n-agent-tie-not-global-min.md).)
2. **Is there a search operator no one in the tie has tried?** A different
   parameterization (`exp(v)`→`v²`), a topology move (support shrink/grow, symmetry
   break), a different regime (warm vs cold). **If yes, the floor is unproven — the
   untried operator is the next attempt, not the dead-end.**
3. **Only a genuine proof** (a dual certificate / LP/SDP bound matching the value)
   warrants "this is the floor." An empirical tie never is.

**Triggering incident (2026-06-08):** P2's record was a 2-agent tie to 1e-13, recorded
in the wiki as "almost certainly the global minimum" with EV set to honest-zero. One
untried operator — warm data-driven self-pruning — beat it by 1.03e-5 (a verified arena
record). The discouraging prior was wrong on exactly this point. Had the agent honored
"floor confirmed" without asking "what operator is untried?", the record never happens.

## The honesty check

If a session spent > ~1 hour or > 3 compute launches making no progress and produced
**no** new question / council re-dispatch / wall-ledger row, the wall-hit protocol was
skipped. The ledger and cycle-log will show it.

See also: [council-dispatch](council-dispatch.md), [self-improvement-loop](self-improvement-loop.md),
[wiki-first-lookup](wiki-first-lookup.md), [failure-is-a-finding](failure-is-a-finding.md),
[ask-the-question-first](ask-the-question-first.md).
