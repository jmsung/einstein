---
type: finding
author: agent
drafted: 2026-06-22
question_origin: paper-groundwork
status: answered
related_problems: [1, 2, 3, 4, 7, 9, 11, 14, 18, 22]
cites:
  - scripts/leaderboard_standings.py
  - ../../domains/ai-agents/source/2026-bianchi-einstein-arena-collective-intelligence.md
---

# Live arena standings snapshot — JSAgent, 2026-06-22

Verified directly against the live arena API (`/api/problems`, `/api/solutions/best`)
via `scripts/leaderboard_standings.py`. **Timestamp: 2026-06-22T21:37 PT.** This is the
canonical factual base for the methodology paper's results claims — it supersedes the
per-problem wiki frontmatter, which was stale (see "Corrections" below).

## Ranking method (matters — got it wrong once)

The arena ranks **strictly**, and **on exactly-equal scores the earliest submission
wins**. Verified on P1: Together-AI, JSAgent, and alpha_omega_agents all scored
`0.3808703105862199`; the arena ordered them by `createdAt` ascending (Together-AI
Mar 19 → #1, JSAgent Apr 7 → #2, alpha_omega Apr 10 → #3). A first sweep that
dense-ranked on the API's rounded score falsely tied JSAgent at #1 on P1 and
**overcounted rank-#1 as 5**. With the timestamp tiebreak the count is **4** — matching
the human's recollection, not the buggy sweep. Lesson: rank on full-precision score
**and** `createdAt`, never on the displayed/rounded value.

## JSAgent standings (15 of 17 active problems on the board)

| Rank | Count | Problems |
|---|---|---|
| **#1** | **4** | P2 first-autocorrelation · P9 uncertainty-principle\* · P14 circle-packing · P18 circles-rectangle |
| #2 | 1 | P1 erdős-min-overlap\* |
| #3 | 5 | P3 second-autocorrelation\* · P4 third-autocorrelation\* · P7 prime-number-theorem · P11 tammes · P22 kissing-d12 |
| not on board | — | P15 heilbronn-triangles · P19 difference-bases |

Top-3 on **10 of 17**. `*` = JSAgent shares an exact score with another agent on that
problem (rank decided by submission time).

- **P9 #1 is a tie held by earliest submission** — another agent matched the exact score
  but submitted later. Legitimate #1, but contested. State it as "rank-1 (tied, held on
  submission order)" in the paper.
- **P2, P14, P18 are clean #1** (strictly best score).
- **P1 is #2** — JSAgent's score is byte-identical to Together-AI's; they submitted ~3
  weeks earlier and hold #1.

## Standing among all agents (the "highest among all" claim — TRUE)

Tallied across all 17 problems:

| Metric | JSAgent | Runners-up |
|---|---|---|
| Rank-#1 count | **4 (highest)** | AlphaEvolve 3, Together-AI 3, KawaiiCorgi 2 |
| Top-3 count | **10 (highest)** | alpha_omega_agents 8, CHRONOS 7, OrganonAgent 4 |

JSAgent leads both the rank-#1 and the top-3 tables. This is the strongest single
defensible headline for the paper — more robust than any individual-problem rank, since
it doesn't hinge on a tie.

## Corrections to stale wiki frontmatter (per-problem pages need updating)

The live sweep contradicts several problem pages — they predate recent leaderboard
movement and should be reconciled (separate task):

- **P6 kissing-d11**: page says "conquered, #1"; live is **#4** (KawaiiCorgi holds 0; the
  604/exact-zero construction from the platform paper). Already flagged stale.
- **P9 uncertainty-principle**: page status "hidden"; live is **#1** (tied, held on time).
- **P14 circle-packing**: page "rank-2-frozen"; live is **#1**.
- **P1 erdős**: page "rank-2-frozen"; live confirms **#2**.
- **P2 first-autocorrelation**: page body said "displaced to #3"; live is **#1** (re-taken
  2026-06-09) — frontmatter `status: rank-1` was the correct field.

## Reproduce

```bash
uv run python scripts/leaderboard_standings.py --agent JSAgent
```
Public endpoints, no API key required. Re-run before any submission or paper revision —
standings move.
