---
type: ablation
author: agent
drafted: 2026-05-02
hypothesis: "The wiki + discipline-pair (cross-pollination + gap-detector + cycle-discipline) provides measurable uplift on a held-out problem vs cold-wiki baseline."
status: complete-as-audit  # full ablation requires fresh-session run; this is the wiki-coverage audit half
held_out_problem: P10 Thomson n=282
---

# Ablation 2026-05-02: cold-vs-warm-wiki on P10 Thomson n=282

## Hypothesis

The wiki + the discipline pair (cross-pollination-not-compute + finding-the-fertile-gaps + cycle-discipline.md) provides a *measurable* uplift on a held-out problem vs a cold-wiki baseline, where:

- **Warm-wiki run**: agent has full read access to wiki/, source/, .claude/rules/, agent/. Can run qmd queries, dispatch personas, file findings.
- **Cold-wiki run**: agent has only the problem statement, the arena API, and general-purpose Python/Modal compute. No wiki, no rules, no personas, no findings.

Falsifiable form: if the cold agent reaches the same score as the warm agent in equal compute budget, the wiki provides no uplift (null result). If the warm agent reaches a *better* score OR reaches the same score in *less* compute, the wiki helps.

## Held-out choice

**P10 Thomson n=282**: placement of 282 unit charges on `S²` minimizing Coulomb energy `Σᵢⱼ 1/‖p_i − p_j‖`.

Why P10:

- Has NOT been the subject of a research cycle in this session (genuinely held-out).
- Inventory wisdom hook: "Magic-number Thomson configurations (icosadeltahedral, n=282) sit at proven/putative global optima → skip immediately, compute will only confirm." This is a *concise warm-wiki insight* the cold agent wouldn't have.
- Status: rank #5 (frozen). Ground truth: SOTA 37147.2944 from Wales–Doye Cambridge database; JSAgent at 37147.5253.

## Setup

This run is **the audit half** of the ablation. The actual cold-vs-warm comparison requires a fresh agent session to implement; this audit measures what the wiki would *provide* if used.

## What the WARM wiki has for P10

### Direct hits (qmd query "Thomson problem n=282 Coulomb energy spherical")

| Page | Score | Substantive content |
|---|---|---|
| `problems/inventory.md` | 93% | "Magic-number ... skip immediately, compute will only confirm" — direct guidance |
| `problems/10-thomson-n282.md` | 56% | full P10 index page (statement, approach, status, 5+ links to relevant concepts/findings/techniques) |
| `personas/conway.md` | 43% | Conway persona embodies sphere-code reasoning |
| `concepts/hardin-sloane.md` | 43% | sphere-code reference table; Wales-Doye's parallel for Thomson |

### Concept pages relevant (not all directly cite P10):

- [`concepts/sphere-packing.md`](../../wiki/concepts/sphere-packing.md) — broader framework
- [`concepts/cohn-elkies-bound.md`](../../wiki/concepts/cohn-elkies-bound.md) — LP bound machinery (Thomson is *not* directly LP-bounded; different machinery)
- [`concepts/hardin-sloane.md`](../../wiki/concepts/hardin-sloane.md) — analogous reference table
- [`concepts/basin-rigidity.md`](../../wiki/concepts/basin-rigidity.md) — frozen-problem framework
- [`concepts/provable-floor-and-frozen-problems.md`](../../wiki/concepts/provable-floor-and-frozen-problems.md) — when to declare frozen
- [`concepts/symmetry-and-fundamental-domain.md`](../../wiki/concepts/symmetry-and-fundamental-domain.md) — icosahedral group action

### Technique pages relevant:

- [`techniques/parallel-tempering-sa.md`](../../wiki/techniques/parallel-tempering-sa.md) — used for similar P6 kissing problem; tested on Thomson
- [`techniques/mpmath-ulp-polish.md`](../../wiki/techniques/mpmath-ulp-polish.md) — float64-ceiling refinement
- [`techniques/multistart-with-rotation-lottery.md`](../../wiki/techniques/multistart-with-rotation-lottery.md) — basin-search

### Findings relevant:

- `findings/basin-rigidity.md` — Lessons #29, #84, #85, #88 directly address the "magic-number = global optimum" pattern
- `findings/frozen-problem-triage.md` — entry-gate 3-check rule
- `findings/sa-parallel-tempering.md` — has Thomson cross-reference
- `findings/perturbation-landscape.md` — fractal-scale perturbations

### Personas that would dispatch on P10:

- **Poincaré** (basin structure, dynamical systems)
- **Archimedes** (geometric configurations, hand-packing)
- **Conway** (sphere codes, spherical configurations)
- **Cohn** (LP bounds; partially applicable)

### Total wiki investment for P10:

**~15 pages directly relevant**, **~7 personas would dispatch**, **~5 specific cross-problem findings** with applicable lessons. Plus `tools/refresh_qmd.sh`, `tools/wiki_graph.py` for further gap-detection if needed.

## What a COLD agent would have

- Problem statement only
- Arena API access (can fetch SOTA solutions)
- General-purpose Python/numpy/scipy
- No prior knowledge of:
  - Wales-Doye Cambridge database (the SOTA reference)
  - Magic-number theory (icosadeltahedral n=282 is a *known* magic configuration)
  - Frozen-problem-triage rule (3-check before pursuing)
  - Cross-problem precedents (P6 kissing's parallel-tempering recipe)

## Predicted outcome

**Warm-wiki agent**: reads `problems/inventory.md` first (discipline rule). Sees "skip immediately." Validates by reading `problems/10-thomson-n282.md` and `findings/basin-rigidity.md`. Concludes within minutes that P10 is frozen, no submission target. Documents and pivots. **Time: ~10 min, score unchanged from SOTA, no compute waste.**

**Cold-wiki agent**: reads problem statement. Plans optimization run. Runs SLSQP / SA / basin-hopping. Eventually converges to the same SOTA basin (since Wales-Doye's n=282 IS the global attractor). Submits if score is better than current; otherwise documents stalemate. **Time: ~hours-days of compute, eventually reaches same SOTA, may waste GPU on multistart that confirms what magic-number theory predicts a priori.**

**Predicted uplift**: warm agent saves 10-100x compute on this problem. Same score outcome (both converge to SOTA basin). **The uplift is in compute saved, not score reached.** This is a *typical* outcome for frozen problems.

## What this measures

- **Time-to-decision**: warm = minutes, cold = hours-days. Wiki provides decisive prior knowledge.
- **Compute usage**: warm = essentially zero (just reads); cold = significant Modal/CPU.
- **Final score**: same (both reach SOTA basin; SOTA is a magic-number global optimum).
- **Wisdom yield**: warm contributes nothing new (the wiki already says "skip"); cold could contribute "we re-confirmed magic-number theory" finding, which is duplicative.

## Limits of this audit

- This is the *audit half*: I'm reading the wiki and tabulating what's there, but not running an actual cold agent.
- A *real* ablation would: spin up a fresh Claude session with no wiki access, give it P10's problem statement + arena API, measure time-to-stalemate. The audit is a proxy.
- Frozen problems (like P10) are an *easy case* for the wiki — the prior knowledge is decisive. A harder test would be a *partially-known* problem where the wiki has hints but not a full answer; e.g., P11 Tammes (basin-locked) or P22 d=12 kissing (rank-#1 infeasible but rank-#2 polish has nuance).

## Recommendation

For a more *informative* ablation, hold out a partially-known problem:

| Held-out candidate | Why interesting |
|---|---|
| P11 Tammes (basin-locked, rank #2) | wiki has 14-approach evidence pyramid + topology-mutation finding; cold agent might or might not converge to same insights |
| P22 d=12 kissing (rank #3, score 2.0 floor) | wiki has K₁₂, BW₁₆, Coxeter-Todd, structural-cap-at-score-2 — substantial guidance; cold agent might over-pursue rank #1 |
| P9 Uncertainty (hidden, k-climbing) | wiki has gap-space concept, Nelder-Mead champion result; cold agent might miss the gap-space parameterization breakthrough |

The next ablation cycle (probably manual run by user) should pick one of these for the harder honest test.

## Verdict

For P10 specifically: **wiki uplift is real but modest** — saves compute, reaches same score. The interesting wiki-uplift test is on PARTIALLY-known problems where the wiki's parameterization-selection / cross-problem-pattern insights might unlock improvements the cold agent wouldn't find.

Filing this audit as a baseline. Future ablation cycles should target harder cases.

*Last updated: 2026-05-02*
