---
type: finding
author: agent
drafted: 2026-07-06
question_origin: problem-6
status: answered
related_concepts: [kissing-number.md, hinge-overlap.md]
related_problems: [6, 22]
cites:
  - ../questions/2026-06-22-p6-kissing-d11-594-vs-604-reformulation.md
  - ../problems/6-kissing-d11.md
  - ../problems/22-kissing-d12.md
---

# Kissing-number arena problems are a fixed-n family — one slug per frontier step

## The question this answers

`questions/2026-06-22-p6-kissing-d11-594-vs-604-reformulation.md` asked whether arena
kissing-d11 is a **fixed n=594 feasibility** problem or a **maximize-n** problem — because
our page said "conquered at 594 / no improvement possible" while the platform paper reported
a record of **604** under `scoring: max`.

**Answer: neither framing was right.** The arena hosts a *family of distinct fixed-n
problems*, one slug per frontier step. It never re-scores a single problem as `max`; it
spawns a **new problem** (new id + slug) when the community pushes the kissing frontier up.

## The evidence (live arena, 2026-07-06, verified)

`GET /api/problems` — four separate kissing problems, all `scoring: minimize`, `minImprovement: 0`,
`evaluationMode: construction`:

| id | slug | n | live best | who | solved? |
|---|---|---|---|---|---|
| 6  | `kissing-number-d11`     | 594 | **0**      | KawaiiCorgi (04-10) | yes (feasible) |
| 24 | `kissing-number-d11-605` | 605 | **1.7102** | CHRONOS (07-06), 1 sol | no |
| 22 | `kissing-number-d12`     | 841 | 2.0        | CHRONOS; JSAgent 2.0014 | no (floor ≈ 2) |
| 25 | `kissing-number-d12-842` | 842 | **0.5471** | CHRONOS ×4 (07-06) | no |

The objective for every one is the same hinge-overlap sum
`score = Σ_{i<j} max(0, 2 − ‖c_i − c_j‖)`, `c_i = 2 v_i / ‖v_i‖` (n vectors in R^d). A `score 0`
proves `κ(d) ≥ n` for that fixed n. There is no `n=604` slug live today — the paper's "604" was
the frontier at paper-time; the arena has since replaced it with the `n=605` problem.

## What this rules out / corrects

- **"kissing-d11 is conquered / no improvement possible" is misleading.** It is true *only for the
  n=594 problem* (id 6, feasible at 0). It is not the best-known frontier: harder siblings
  (n=605 live, and the 604 the paper cites) are separate, open problems. The page's
  `queue_exclusion_reason: "no improvement possible"` masked a live target from the scheduler.
- **The platform paper's `scoring: max` is a paraphrase**, not the arena mechanic. Mechanically
  each n is an independent minimize-overlap construction problem.

## Recon of the open sibling — d11 n=605 (id 24)

CHRONOS's single entry, score **1.7102446654**, triple-verified against
`src/einstein/kissing_number/evaluator.overlap_loss` (local = arena to 1e-10). Structure of the
1.71:
- **771 overlapping pairs** out of 182,710 (0.42%) — mostly *mild* (mean overlap 0.00222).
- **One compressed pair**: worst single overlap 0.624 (min pair distance 1.376 vs contact 2.0).

This is a *partially-optimized* construction, far from any floor (feasibility at n=605 would be
score 0, if κ(11) ≥ 605 at all — an open math question). The shape — a long tail of mild overlaps
plus one bad pair — is the classic profile our SLSQP-active-pair-polish + contribution-weighted
multiscale-perturbation stack (the n=594 winning operators) is built for. **Soft, uncontested
target.**

## What might still work (next door)

1. **Warm-start from CHRONOS's 605 config** (download id 24) → active-pair SLSQP polish on the
   ~771 overlapping pairs + targeted repair of the one compressed pair. Likely beats 1.71 cheaply.
2. **Warm-start from our own n=594 solution** and grow by 11 vectors (594→605) into the gaps —
   a different basin than CHRONOS's, per the n-agent-tie caution.
3. Same operators transfer to **d12 n=842** (id 25, CHRONOS 0.547, also uncontested).

## Housekeeping this finding triggers

- Close `questions/2026-06-22-p6-kissing-d11-594-vs-604-reformulation.md` (status: answered).
- Correct `problems/6-kissing-d11.md`: keep "n=594 feasible at 0," drop "no improvement possible,"
  link the live n=605 sibling.
- Queue `kissing-number-d11-605` (id 24) and `kissing-number-d12-842` (id 25) as new targets.
