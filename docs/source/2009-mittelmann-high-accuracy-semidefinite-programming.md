---
type: source
kind: paper
title: High accuracy semidefinite programming bounds for kissing numbers
authors: Hans D. Mittelmann, Frank Vallentin
year: 2009
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/0902.1105v3
source_local: ../raw/2009-mittelmann-high-accuracy-semidefinite-programming.pdf
topic: general-knowledge
cites: 
---

# High accuracy semidefinite programming bounds for kissing numbers

**Authors:** Hans D. Mittelmann, Frank Vallentin  ·  **Year:** 2009  ·  **Source:** http://arxiv.org/abs/0902.1105v3

## One-line
Computes the Bachoc–Vallentin three-point SDP kissing-number bounds to ten significant digits for dimensions $3 \le n \le 24$ using arbitrary-precision SDP solvers, tightening every previously known upper bound.

## Key claim
The new SDP upper bounds $s_d(n)$ at $d=14$ are the best known for all $n \in \{3,\dots,24\}$; in particular $s_{14}(5) = 44.998996\ldots$ narrows $\kappa(5) \in \{40,\dots,45\}$ to $\{40,\dots,44\}$, and $s_{14}(16) \le 7355.81$ disproves the Conway–Sloane conjectured 16-dim periodic packing with average theta series $1 + 7680q^3 + 4320q^4 + 276480q^5 + \cdots$ (would require $\kappa(16) \ge 7680$).

## Method
Solves the Bachoc–Vallentin three-point SDP relaxation: minimize $1 + \sum_k a_k + b_{11} + \langle F_0, S_0^n(1,1,1)\rangle$ subject to PSD constraints on matrices $F_k$ and a $2\times 2$ block $b_{ij}$, plus SOS-multiplier polynomial identities in Jacobi polynomials $P_k^n$ (parameters $((n-3)/2,(n-3)/2)$) and symmetrized three-point matrices $S_k^n(u,v,t)$. Uses SDPA-GMP with 200–300 binary digits, relative stopping $10^{-30}$, and tuned `lambdaStar` (100–10000) — first-order solvers (SDPLR) and standard double-precision interior-point (SeDuMi) fail for $d > 10$ because the linear systems become extremely ill-conditioned near optimum even when the SDP itself is well-conditioned.

## Result
Table of $s_{11}(n), s_{12}(n), s_{13}(n), s_{14}(n)$ to 10 digits for $n = 3..24$. Highlights: $s_{14}(3)=12.38180947$, $s_{14}(4)=24.06628391$, $s_{14}(5)=44.99899685$ (proves $\kappa(5) \le 44$), $s_{14}(16)=7355.809036$ (down from previous 8312), $s_{11}(8)=240.0000\ldots$ and $s_{11}(24)=196560.0000\ldots$ (sharp). Runtime: 5–10 weeks per case at $d=12$ on Quad Core 2, down to 1–2.5 weeks at $d=13,14$ with quad-precision SDPA/CSDP. Open question 4.1: is $\lim_{d\to\infty} s_d(4) = 24$? (Would prove $D_4$ uniquely optimal and contradict universal optimality.)

## Why it matters here
Direct prior art for any Einstein Arena kissing-number / spherical-code problem: gives the tightest known SDP upper bounds across $n \le 24$ and pinpoints $n=5,9,10,\ldots,23$ as still-open gaps where the agent could attempt either tighter SDP relaxations or improved configurations. Also concretely demonstrates that triple-verify-level high-precision arithmetic (GMP, 200+ bits) is required to get reliable Bachoc–Vallentin numbers — directly relevant to the project's compute-router and triple-verify rules.

## Open questions / connections
- Is $\lim_{d\to\infty} s_d(4) = 24$? Settling this would characterize the $D_4$ root system / 24-cell as uniquely kissing-optimal in $S^3$ and rule out any 24-point universally optimal config (per Cohn–Conway–Elkies–Kumar).
- Can one close the residual gaps $\kappa(5)\in\{40,\dots,44\}$, $\kappa(9)\in[306,364]$, $\kappa(10)\in[500,554]$, etc. by going to $d \ge 15$ (where $s_{15}(4) = 23.063\ldots$ shows the bound is not yet saturated for $n=4$)?
- Extends Bachoc–Vallentin 2008 (limited to $n \le 10$, $d \le 10$); complements Pfender 2007 Delsarte improvements and Musin 2008 ($\kappa(4)=24$). Suggests four- and five-point SDP hierarchies as the next door.
- High-precision SDP solving (SDPA-GMP, quad-precision SDPA/CSDP) is the enabling tooling — same precision regime needed for Cohn–Elkies LP bounds in sphere packing.

## Key terms
kissing number, semidefinite programming, SDP bound, Bachoc-Vallentin, three-point bound, Jacobi polynomials, SDPA-GMP, arbitrary precision arithmetic, D4 root system, 24-cell, Conway-Sloane conjecture, average theta series, extremal modular form, universally optimal configuration, spherical codes
