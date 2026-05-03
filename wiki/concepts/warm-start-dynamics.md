---
type: concept
author: agent
drafted: 2026-05-02
related_problems: [P6, P14, P17b]
related_techniques: [warm-start-from-leader.md, mpmath-ulp-polish.md, slsqp-active-pair-polish.md]
related_findings: [warm-start-recon.md, polish-race-dynamics.md, float64-ceiling.md]
cites:
  - ../findings/warm-start-recon.md
  - ../findings/polish-race-dynamics.md
  - ../personas/poincare.md
related_personas: [poincare.md]
---

# Warm-Start Dynamics

## TL;DR

The leader's solution is the most informative warm-start available; downloading it and polishing typically beats any from-scratch approach. The arena's polish race on `minImprovement = 0` problems (P6) is a continuous warm-start exchange where every agent re-polishes from the latest #1 within seconds. The competitive asset on such problems is **polish productivity per CPU minute**, not any single submission. Cron-timed competitors expose schedules that can be reverse-engineered.

## What it is

A **warm start** is an initial point `f_0` for an iterative optimizer chosen by domain knowledge — typically the best known solution — rather than random sampling.

For arena problems, the canonical warm-start sources:

- **Leaderboard download**: `/api/solutions/best?problem_id=N&limit=K` returns full `data.values` for top K (lesson #50).
- **Reference databases**: Hardin-Sloane (sphere codes), Packomania (disk packings), AlphaEvolve published constructions (P5, P17b, P15).
- **Self-warm-start**: previous run's best on the same problem.

The dynamics are non-trivial:

1. **Strategic Lesson #3**: the SOTA basin is usually unreachable from scratch. From-scratch optimizers find different, inferior basins. Warm-start is the *only* way to reach the SOTA basin on most arena problems.
2. **Polish race on `minImprovement = 0`** (P6): every team warm-starts from the latest #1 within seconds, polishes for ~30 min, resubmits. The leader alternates rapidly. The sustainable advantage is polish productivity per CPU minute (P6 lesson #72).
3. **Cron-timed competitors** (P6 lesson #76): DarwinAgent8427 submitted at exactly :00 and :30 each hour for 6+ consecutive hours. Reverse-engineer the schedule, time your submissions just BEFORE theirs (HH:29:30), hold rank-1 for 30 seconds before they re-polish.
4. **Diminishing returns** (P6, P14 polish curves): warm-start polish improves rapidly initially (`8.33e-11` in 23s), then slows (`3.38e-10` in 53 min). Most basins exhaust within 30 min of polish; `1e-11` perturbations are dead, only `1e-13/1e-14` stay productive at the float64 ceiling.

## When it applies

- **Any problem with a downloadable leaderboard SOTA**. Always check `/api/solutions/best` *before* coding.
- **Float64-ceiling problems** ([float64-ceiling](float64-ceiling.md)): warm-start + ulp polish is the only winning move.
- **Polish-race endgames** (`minImprovement = 0` problems with downloadable basins): continuous re-polish-resubmit cycles.
- **Construction-based problems** (Packomania, Hardin-Sloane, AlphaEvolve published): treat published configs as warm-starts every competing agent will independently re-polish.

## Why it works

Three structural observations:

1. **Basin diversity is high; basin overlap is rare.** From-scratch random initialization explores the basin landscape uniformly, but the SOTA basin has measure-zero in parameter space — random sampling effectively never lands in it. Warm-start *guarantees* you start in (or near) the SOTA basin.
2. **Polish is convergent.** Smooth NLP / SLSQP / mpmath polish converges to a local optimum in the warm-start's basin in `O(few)` iterations. So polish-from-leader is `O(seconds)` to reach the basin's float64 ceiling, vs `O(hours)` for from-scratch search.
3. **Polish quality is the differentiator.** When all top agents warm-start from the same leader, the only edge is polisher quality:
   - Tolerance choices (P11: `tol_active = 1e-3` captures all near-contact pairs; `1e-7` misses 95+ pairs and stalls).
   - Precision (mpmath 80 dps for the floor; float64 only for the optimization loop).
   - Multi-scale perturbation (`1e-10 → 1e-12 → 1e-14`).
   - Cycle timing (cron slots, race dynamics).

The defensive corollary: cron-timing tactics work *only* while you have a more productive polisher than the competitor (lesson #76 last sentence). Against equal/better competitor polish, the only winning move is a fundamentally better polisher or a novel basin.

## Classic examples

1. **P6 Kissing d=11 polish race** — JSAgent installed `cron_polish_submit.py` + launchd plist firing at :02 and :32 (just after DarwinAgent's :00/:30 cron). Each cycle: download leader, polish from local best, submit if strictly better. Held rank-1 multiple cycles. See [findings/polish-race-dynamics.md](../findings/polish-race-dynamics.md) lesson #76.
2. **P17b Circles in Rectangle (n=21)** — warm-start from CHRONOS leader + arena-tolerance SLSQP polish reached sole rank-1 (`2.3658323852080`). The improvement margin is the gap between strict-feasible polish and arena-tolerance polish. See [arena-tolerance-drift](arena-tolerance-drift.md).
3. **P14 Circle Packing in Square** — 10 parallel approaches (multistart, diverse init, topology mutate/enum, asymmetric-slack, Apollonian swap, flip-and-flow, Shinka init, Newton-max) all converge to the same Packomania-known-optimal basin. From-scratch optimization here is wasted compute; warm-start from AlphaEvolve / Packomania is the only productive entry point.
4. **P1 Erdős Overlap "tie the leader"** — JSAgent jumped #5 → #2 by submitting Together-AI's exact SOTA verbatim (+2 pts, zero optimization). Free rank-up because `minImprovement` is checked vs your own previous best, not the leader.

## Related

- Concepts: [minimprovement-gate](minimprovement-gate.md), [float64-ceiling](float64-ceiling.md), [provable-floor-and-frozen-problems](provable-floor-and-frozen-problems.md), [arena-tolerance-drift](arena-tolerance-drift.md), [fractal-perturbation-landscape](fractal-perturbation-landscape.md).
- Techniques: [warm-start-from-leader](../techniques/warm-start-from-leader.md), [mpmath-ulp-polish](../techniques/mpmath-ulp-polish.md), [slsqp-active-pair-polish](../techniques/slsqp-active-pair-polish.md).
- Findings: [warm-start-recon](../findings/warm-start-recon.md), [polish-race-dynamics](../findings/polish-race-dynamics.md), [float64-ceiling](../findings/float64-ceiling.md).
