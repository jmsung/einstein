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

### Update 2026-06-06 (post-council moves, all ruled out)
After the council re-dispatch, implemented and ruled out every proposed move:
frozen-sign + periodic frag sweep (→2.5), discrete sign-flip hop from leader (all
edits worse, ~1.49), spectral Fourier sign-texture (leader-seeded → 1.60: sign
field is **incompressible**), Cohn signed dual SDP (collapses to ~1.0: loose), and
**sign-topology crossover** of the leader×ours parents (→1.49–1.50: the topology
is **non-recombinable** — autoconvolution is global, splicing breaks coherence).
Net: the optimal P4 sign topology is incompressible, non-recombinable, and a
strong local optimum — reachable only by its own dedicated search or a direct
seed. Independent construction/search is exhausted. **Resolving move: obtain the
record's sign pattern (seed) and escape it with `escape_from_seed.py` /
`frozen_sign_descent`.**

### Update 2026-06-06 (creative / discrete-global moves — also ruled out)
- **Low-autocorrelation sequences** (Legendre symbol, Rudin-Shapiro) × leader
  envelope → 1.77 / 1.75 (50% neg, near-Nyquist). They solve autoCORRELATION
  sidelobes, not this autoCONVOLUTION peak; and the leader's fragmentation
  (9410 sign changes ≈ period 10) is far from their Nyquist oscillation.
- **Simulated annealing on the sign field** (discrete global optimizer; magnitudes
  fixed at |leader|, FFT energy, Metropolis + periodic magnitude re-polish):
  best never drops below the leader; thermal moves wander to ~1.4529. The leader
  is a deep local optimum in *sign* space too.
- Live leaderboard (re-fetched): only OrganonAgent 1.4523 + ours 1.4525 exist at
  n=100k; no public 1.4522 — the record is private/unsubmitted. No new seed there.

**~15 method families now exhausted** (gradient, greedy, LP, escapes×4, periodic/
chirp/compact/multiscale/sequence constructions, frozen-sign, crossover, discrete
SA, dual). All cap at the leader (1.4523) or worse. The optimal sign topology is
incompressible, non-recombinable, a deep local optimum, and not a classical
sequence — it is genuinely only reachable by its own dedicated search/compute or a
direct seed. **Do not re-grind these; on the next P4 record attempt, start from a
seed of the target topology.**

## Lesson distilled (meta)
The dominant time-sink is **brute-forcing past a wall instead of escalating to wisdom
at the 2nd failure.** The council diagnoses obstructions and rules out whole families
in minutes; the wiki holds the prior dead-ends. Escalate early, record the wall, and
the next encounter is a lookup, not a re-grind.
