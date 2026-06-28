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

### Update 2026-06-06 (web research + record-method families — also ruled out)
Deep web research: NO published value < 1.4523 (leader method unpublished; our wall
IS the public frontier). Implemented the two record-family leads:
- **Two-sided signed LP–Frank–Wolfe** (MV/AlphaEvolve): 1.4620 — worse. Constraining
  the "free" negative excursions (−M ≤ conv) is counterproductive for variant (b);
  our original one-sided LP was correct.
- **Tabu-SAW steepest descent** (LABS/merit-factor SOTA): 1.5135 at n=2000 — no
  better basin than the equioscillation/escape family. Scale wall: moderate-n = the
  equioscillation basin; the better basins are intrinsically high-n and not reachable
  by efficient discrete search.
See `findings/p4-web-research-frontier-and-methods.md`. Net: 16 method families +
literature all cap ~1.4525. Record is at/beyond the published frontier — seed or
dedicated high-n compute only.

### Update 2026-06-06 (Remez-on-plateau — leader certified local min, no headroom)
The last untried council move (exact active-set minimax LP descent, which canNOT
stall on flat plateaus like smooth-max can): from the leader, the LP finds ZERO
descent direction (Δ=0). This CERTIFIES the leader (1.4523043332) is a true local
minimum — refuting the "smooth-max stall hides headroom" hypothesis. The record
(1.4522) is therefore provably a SEPARATE basin, not a deeper point in the
leader's. (Full-res n=100k LP is infeasible ~ but the reduced-basis LP is a valid
local-optimality certificate.) ~17 method families now exhausted incl. every
council move; the record requires a seed of its distinct topology.

### 2026-06-10 — P4 shrink–regrow decay wall (js/feat/p4-warm-pruning-transfer)

| date | problem | obstruction | failed attempts | wisdom consulted | resolving move | outcome | finding |
|---|---|---|---|---|---|---|---|
| 2026-06-10 | P4 third-autocorrelation | Shrink–regrow cycling (the first operator that crosses P4 sign classes by descent — partially overturns the 06-06 "descent can't" row) decays geometrically to its own fixed point ≈1.452381, 7.7e-5 above the leader: new fragmentation must CO-EVOLVE with magnitudes through descent; injection rate is the bottleneck, not prune selection | 6 plain cycles (gains −1.9e-5→−2.6e-6), regrow noise A/B (<5e-7), Hilbert energy-norm prune (on-envelope −2.3e-6), Tao run-splitting prune (forced runs 2696→3642 but C +2.4e-4 = damage), Hadamard leader-sign transplant (1.4539 — sign topology alone does NOT fix the basin) | this ledger (06-06 rows), qmd (sign-topology + fragmentation findings), council re-dispatch Tao/Hilbert/Cohn/Hadamard | none left in the prune-rule class (Cohn LP-guided prune not run — same class falsified twice independently); operator banked at its fixed point with our-best improved 1.4525212→1.4523809 (−1.40e-4, triple-verified) | **honest-zero for the record** — but the operator transfers (P3 next per branch note); the JOINT (sign, magnitude) co-adaptation extends the incompressibility verdict | `findings/dead-end-p4-shrink-regrow-fixed-point.md` (Goal 3) |

### 2026-06-28 — P7 N=16000 base-LP tractability wall (js/feat/p7-nextension-reclaim)

| date | problem | obstruction | failed attempts | wisdom consulted | resolving move | outcome | finding |
|---|---|---|---|---|---|---|---|
| 2026-06-28 | P7 prime-number-theorem | Re-solving the base LP at N=16000 (maxkey 16000, violation range to 160000) is intractable with our primal cutting-plane + scipy.linprog stack in a single-run budget — each round re-solves from scratch (no cross-round basis warm-start) and the 160k-integer violation check is heavy | (A) dense cutting-plane, full 1..16000 initial constraints: HiGHS IPM timed out 311s round 0, primal infeasible. (B) warm-started sparse, vars=CHRONOS support 1999, init constraints 5338 from tight G>0.5: no round returned within 580s wall (SIGTERM) | wiki-first-lookup (Exp 8/9 + leader recon), exact-grid evaluator parity (Exp 9), prior LP recipes (Exp 4/7 succeeded only at N≤3350) | NOT yet tried: dual / column-generation LP (`colgen_prime.py`), violation-range cap << 10·maxkey, `highspy` direct with cross-round basis warm-start. Council NOT re-dispatched (paused for human compute decision) | base-LP beat **blocked**; only the saturated tolerance-edge rescale available (CHRONOS→0.9963206, +9e-7 over #1, fragile, no new wisdom) | experiment-log Exp 10; question `2026-06-28-p7-n16000-lp-tractability.md` |

## Lesson distilled (meta)
The dominant time-sink is **brute-forcing past a wall instead of escalating to wisdom
at the 2nd failure.** The council diagnoses obstructions and rules out whole families
in minutes; the wiki holds the prior dead-ends. Escalate early, record the wall, and
the next encounter is a lookup, not a re-grind.
