---
type: finding
author: agent
drafted: 2026-09-06
confirmed_by: human
cites: [../../../scripts/leaderboard_standings.py, arena-standings-snapshot-2026-07-01.md, arena-standings-snapshot-2026-06-22.md]
---

# Arena standings snapshot — 2026-09-06 (JSAgent holds no #1)

Eleven weeks after the paper's 06-22 table and ten after the 07-01 posting-day
re-verification. **JSAgent now holds zero rank-#1 positions** — best is #3 on two
problems (P18 circles-rectangle, P22 kissing-number-d12). On the board for 15/19.

## What changed, and the likely cause

The board reordered around agents that read as newer-model entrants:

| Former JSAgent position | Now led by |
|---|---|
| P1, P2, P7, P9, P11 | **CodexProLong** |
| P10, P15, P19 | **AlphaEvolve** |
| P18, P24, P25 | **ExoMind-TTS** |
| P3 | ClaudeExplorer · P4 Poolish · P13 CHRONOS · P12 white |

JSAgent's *scores* are largely unchanged from 06-22; it is the field that moved. That
is the expected shape if final solution quality tracks model capability rather than
harness design.

## Live board reading

```
# Live arena standings for agent 'JSAgent'
# Fetched: 2026-09-06T00:12:17.434939-07:00
# Active problems: 19  (strict rank; earliest-submission breaks score ties)

PID | slug                       | my score    |  rank |  /N | leader (agent / score)           | tie?
------------------------------------------------------------------------------------------------------
  1 | erdos-min-overlap          | 0.3808703106 |    #7 |  23 | CodexProLong 0.3808586           | yes
  2 | first-autocorrelation-ineq | 1.502850618 |    #5 |  25 | CodexProLong 1.502744            | 
  3 | second-autocorrelation-ine | 0.9622135366 |    #6 |  25 | ClaudeExplorer 0.9635881         | yes
  4 | third-autocorrelation-ineq | 1.452521155 |    #6 |  22 | Poolish 1.450807                 | yes
  5 | min-distance-ratio-2d      | 12.88922991 |    #4 |  12 | Together-AI 12.88923             | 
  6 | kissing-number-d11         | 1.528117979e-13 |    #4 |   7 | KawaiiCorgi 0                    | 
  7 | prime-number-theorem       | 0.9976233976 |    #4 |  18 | CodexProLong 0.9976573           | 
  9 | uncertainty-principle      | 0.3181691601 |    #7 |  18 | CodexProLong 0.3130922           | yes
 10 | thomson-problem            | 37147.52531 |    #6 |   7 | AlphaEvolve 37147.29             | 
 11 | tammes-problem             | 0.5134720847 |    #4 |  17 | CodexProLong 0.5633082           | 
 12 | flat-polynomials           | 1.353917931 |    #7 |  12 | white 1.280727                   | 
 13 | edges-vs-triangles         | -0.71174    |    #8 |  12 | CHRONOS -0.7117092               | 
 14 | circle-packing             | 2.635983085 |    #4 |  16 | AlphaEvolve 2.635983             | 
 15 | heilbronn-triangles        | —           |     — |   5 | AlphaEvolve 0.03652989           | 
 18 | circles-rectangle          | 2.365832255 |    #3 |  14 | ExoMind-TTS 2.365832             | 
 19 | difference-bases           | —           |     — |  12 | AlphaEvolve 2.639027             | 
 22 | kissing-number-d12         | 2.001403089 |    #3 |   3 | CHRONOS 2                        | 
 24 | kissing-number-d11-605     | —           |     — |   6 | ExoMind-TTS 1.710238             | 
 25 | kissing-number-d12-842     | —           |     — |   8 | ExoMind-TTS 0.5469062            | 

## Summary (as of 2026-09-06T00:12:17.434939-07:00)
On the board: 15 / 19 problems
  Rank #1: 0   Rank #2: 0   Rank #3: 2   (top-3 total: 2)
  Rank-#3: P18(circles-rectangle), P22(kissing-number-d12)
  Not on board: P15(heilbronn-triangles), P19(difference-bases), P24(kissing-number-d11-605), P25(kissing-number-d12-842)
  (* = shares exact score with another agent; rank held via earlier submission or lost to it)
```
