---
type: source
kind: paper
title: On the Erdős Discrepancy Problem
authors: Ronan Le Bras, C. Gomes, B. Selman
year: 2014
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1407.2510
source_local: ../raw/2014-bras-erd-discrepancy-problem.pdf
topic: general-knowledge
cites:
---

# On the Erdős Discrepancy Problem

**Authors:** Ronan Le Bras, C. Gomes, B. Selman  ·  **Year:** 2014  ·  **Source:** https://arxiv.org/abs/1407.2510

## One-line
SAT-based streamlined search extends the longest known $\pm 1$ sequence of discrepancy 3 from 17,000 to 127,645, and proves this bound tight for completely multiplicative sequences.

## Key claim
$E_2(3) = 127{,}646$: every completely multiplicative $\pm 1$ sequence of length $\geq 127{,}646$ has discrepancy $\geq 4$, settling the Erdős discrepancy conjecture for CMSs up to $C = 3$. The bound is tight (a length-127,645 witness exists), and inductive construction gives $E_1(4) > 9 \cdot 127{,}645 = 1{,}148{,}805$.

## Method
SAT encoding of the discrepancy automaton (state $s_j^{(m,d)}$ tracks partial sums along HAP with common difference $d$) plus XNOR constraints for multiplicativity ($p_{id} \leftrightarrow p_i \oplus p_d$). Core technique is **streamlining** — adding observed regularities (periodicity $x_i = x_{i \bmod p}$, partial multiplicativity $\text{mult}(x,m,l)$, Walters-prefix $\text{walters}(x,w)$) to tunnel the search into structured subspaces. Plingeling/Lingeling do the heavy lifting; UNSAT proof in DRUP format (335 GB).

## Result
- $E_2(3) = 127{,}646$ (tight; previously known: longest discrepancy-3 sequence had length 17,000).
- Streamliner `walters(730)` finds a length-127,645 CMS in ~1.5 hours; ~60 hours to prove UNSAT at 127,646.
- For EDP1, `mult(700,20000)` yields a length-31,500 sequence of discrepancy 2 in ~14 hours (vs. 10 days for length 13,900 unstreamlined).
- Inductive period-$p$ construction: any sequence of length $|x|$ and discrepancy $C$ lifts to length $9|x|$, discrepancy $C+1$ (or $81|x|$, $C+2$) given a "discrepancy mod $p$" seed sequence. Yields $E_1(4) > 1{,}148{,}805$.

## Why it matters here
General background; no direct arena tie. Closest relevance is methodological: SAT/CP **streamlining as a tunneling heuristic** — imposing observed partial structure (periodicity, multiplicativity, prefix-match) to escape unstructured search — is a transferable tactic for arena problems with combinatorial structure (Sidon sets, packing graphs, autocorrelation $\pm 1$ sequences).

## Open questions / connections
- Polymath5 / Tao's 2015 resolution of the full Erdős discrepancy conjecture supersedes this for the unrestricted case but not the multiplicative-tight-bound machinery.
- The 335 GB DRUP proof is beyond standard checkers — proof-trimming/compression is an open practical bottleneck for SAT-certified math results.
- Inductive $9|x| \to C+1$ lift suggests larger $C$ may need analytical (not SAT) arguments; what's the right algebraic framework (character sums, multiplicative function theory) for $C \geq 4$?

## Key terms
Erdős discrepancy problem, completely multiplicative sequence, homogeneous arithmetic progression, SAT encoding, streamlined search, tunneling, Walters sequence, Matryoshka sequence, DRUP proof, Plingeling, Lingeling, periodic lift construction, Beck-Fiala, Spencer's theorem
