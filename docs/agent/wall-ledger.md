# Wall ledger — append-only record of walls and the wisdom that broke them

The compounding engine for [wall-hit-escalation](../../.claude/rules/wall-hit-escalation.md).
Every time the agent hits a wall, it **greps this file FIRST** — if the obstruction
class matches a past row, jump straight to the recorded resolving move instead of
re-grinding. A ruled-out family is wisdom too: record it so no future cycle wastes
compute rediscovering it.

## How to use
- **On any wall:** grep this file for the obstruction (keywords: problem id, the
  metric, the failed approach class). If matched → apply the resolving move directly.
- **After escalating:** append one row below, even if the move failed (failure rules
  out a family).

## Schema
`date | problem | obstruction (the WHY) | attempts that failed | wisdom consulted | resolving move | outcome | finding`

## Walls

| date | problem | obstruction | failed attempts | wisdom consulted | resolving move | outcome | finding |
|---|---|---|---|---|---|---|---|
| 2026-06-06 | P4 third-autocorrelation | Basin is a **discrete, broadband, aperiodic sign topology**; continuous descent is trapped in its starting sign homotopy class and no low-dim ansatz can represent the optimal sign field | smooth-max polish, basin-hop, LP fixed-point, diverse-seed escape, larger-n cascade, neg-content nudge, greedy-noise, fine cascade, frozen-sign + periodic sweep, sign-flip hop, spectral Fourier sign-texture (all cap ~1.4525 or worse; leader=1.4523, target=1.4522) | wiki: equioscillation, Cohn/LP-duality, P2 compact-support family; council: Tao+Hilbert+Hadamard (converged: discrete sign topology) + Cohn (dual) | (a) `frozen_sign_descent` f=s·v² validated; (b) Cohn signed dual SDP; (c) escape topology sampling | **no record yet** — all construction/ansatz/local moves ruled out; dual collapses to ~1.0 (loose); record requires the *specific* sign topology seeded directly (it is incompressible, cannot be parameterized or locally searched) | `findings/p4-basin-is-discrete-sign-topology.md`, `findings/p4-fragmentation-not-fraction-shared-envelope.md`, `findings/dead-end-p4-negative-content-ceiling.md` |

## Lesson distilled (meta)
The dominant time-sink is **brute-forcing past a wall instead of escalating to wisdom
at the 2nd failure.** The council diagnoses obstructions and rules out whole families
in minutes; the wiki holds the prior dead-ends. Escalate early, record the wall, and
the next encounter is a lookup, not a re-grind.
