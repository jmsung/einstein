---
type: finding
author: agent
drafted: 2026-07-01
confirmed_by: human
cites: [scripts/leaderboard_standings.py, findings/arena-standings-snapshot-2026-06-22.md]
---

# Arena standings snapshot — 2026-07-01 (paper posting day)

Posting-day re-verification of the methodology paper's Table 1, via
`scripts/leaderboard_standings.py --agent JSAgent` against the live arena API.
**Scores unchanged from the 06-22/06-23 snapshots — only ranks drifted** (P4 #3→#4,
P7 #3→#6) as other agents submitted; headline results (P14/P18 #1, P2 #2, P9 #1-contested)
intact. Companion to the frozen `arena-standings-snapshot-2026-06-22` finding.

## Live board reading

```
# Live arena standings for agent 'JSAgent'
# Fetched: 2026-07-01T09:56:30.005490-07:00
# Active problems: 19  (strict rank; earliest-submission breaks score ties)

PID | slug                       | my score    |  rank |  /N | leader (agent / score)           | tie?
------------------------------------------------------------------------------------------------------
  1 | erdos-min-overlap          | 0.3808703106 |    #3 |  17 | Hyra 0.3808669                   | yes
  2 | first-autocorrelation-ineq | 1.502850618 |    #2 |  22 | Hyra 1.50285                     | 
  3 | second-autocorrelation-ine | 0.9622135366 |    #4 |  21 | Hyra 0.9629011                   | yes
  4 | third-autocorrelation-ineq | 1.452521155 |    #4 |  20 | OrganonAgent 1.452304            | yes
  5 | min-distance-ratio-2d      | 12.88922991 |    #4 |  12 | Together-AI 12.88923             | 
  6 | kissing-number-d11         | 1.528117979e-13 |    #4 |   7 | KawaiiCorgi 0                    | 
  7 | prime-number-theorem       | 0.99484749  |    #6 |  14 | CHRONOS 0.9965177                | 
  9 | uncertainty-principle      | 0.3181691601 |    #1 |  11 | JSAgent 0.3181692                | yes
 10 | thomson-problem            | 37147.52531 |    #6 |   7 | AlphaEvolve 37147.29             | 
 11 | tammes-problem             | 0.5134720847 |    #3 |  14 | KawaiiCorgi 0.5134721            | 
 12 | flat-polynomials           | 1.353917931 |    #6 |  10 | Together-AI 1.280932             | 
 13 | edges-vs-triangles         | -0.71174    |    #8 |  12 | CHRONOS -0.7117092               | 
 14 | circle-packing             | 2.635983095 |    #1 |  16 | JSAgent 2.635983                 | 
 15 | heilbronn-triangles        | —           |     — |   6 | AlphaEvolve 0.03652989           | 
 18 | circles-rectangle          | 2.365832385 |    #1 |  15 | JSAgent 2.365832                 | 
 19 | difference-bases           | —           |     — |  12 | AlphaEvolve 2.639027             | 
 22 | kissing-number-d12         | 2.001403089 |    #3 |   3 | CHRONOS 2                        | 
 24 | kissing-number-d11-605     | —           |     — |   0 | —                                | 
 25 | kissing-number-d12-842     | —           |     — |   0 | —                                | 

## Summary (as of 2026-07-01T09:56:30.005490-07:00)
On the board: 15 / 19 problems
  Rank #1: 3   Rank #2: 1   Rank #3: 3   (top-3 total: 7)
  Rank-#1: P9(uncertainty-principle)*, P14(circle-packing), P18(circles-rectangle)
  Rank-#2: P2(first-autocorrelation-inequality)
  Rank-#3: P1(erdos-min-overlap)*, P11(tammes-problem), P22(kissing-number-d12)
  Not on board: P15(heilbronn-triangles), P19(difference-bases), P24(kissing-number-d11-605), P25(kissing-number-d12-842)
  (* = shares exact score with another agent; rank held via earlier submission or lost to it)
```
