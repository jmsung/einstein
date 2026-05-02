# personas/

Embodied mathematician perspectives. Each file is a *stance* — how that mathematician sees a problem, the heuristics they reach for, what they fail at, the moves they're famous for.

Distinct from `mb/wiki/mathematician-council.md` (the old dispatch table): persona files are *substance* — read by the agent before invoking that persona's voice. Dispatch policy lives in [`../.claude/rules/council-dispatch.md`](../../.claude/rules/council-dispatch.md).

## Roster (21 total — to be populated in Goal 4)

**Core (10)** — runs by default on every problem:
- gauss.md, riemann.md, tao.md, conway.md, euler.md, poincare.md, erdos.md, noether.md, cohn.md, razborov.md

**Bench (6)** — triggered by problem category:
- viazovska.md (sphere packing), szemeredi.md (regularity), turan.md (graph theory), ramanujan.md (modular forms / hidden structure), archimedes.md (geometric intuition), hilbert.md (functional analysis / axiomatize)

**New (5)** — fill clear gaps in the existing council:
- polya.md — heuristics meta-coach ("How To Solve It")
- hadamard.md — inverse-problem framing ("pretend you have the answer")
- grothendieck.md — find the right framework so the problem dissolves
- atiyah.md — cross-field marriage of tools
- wiles.md — depth + multi-year persistence + descent through abstraction

**Synthesis** (`_synthesis.md`) — the 12 stances drawn from how all of them work.

## Page structure

```yaml
---
type: persona
author: human | hybrid
drafted: YYYY-MM-DD
trigger:
  categories: [...]            # which problem categories invoke this persona
  when_stuck_with: [...]       # signal phrases / failure modes that should pull them in
---
```

Body:
1. **Stance** — one paragraph: how they see the world
2. **Heuristics ranked** — 1, 2, 3, …
3. **When I'm stuck I ask…** — the questions they reach for
4. **I most often fail by…** — the failure mode of overusing this stance
5. **Famous moves** — with cites
6. **Dispatch trigger** — concrete categories / patterns

The point is: when an agent dispatches "Tao" for a problem, it READS the Tao page first to load the stance — not just the instruction "be Tao."
