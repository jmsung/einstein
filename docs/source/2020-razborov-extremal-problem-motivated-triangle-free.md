---
type: source
kind: paper
title: An Extremal Problem Motivated by Triangle-Free Strongly Regular Graphs
authors: Alexander Razborov
year: 2020
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/2006.01937v1
source_local: ../raw/2020-razborov-extremal-problem-motivated-triangle-free.pdf
topic: general-knowledge
cites: 
---

# An Extremal Problem Motivated by Triangle-Free Strongly Regular Graphs

**Authors:** Alexander Razborov  ·  **Year:** 2020  ·  **Source:** http://arxiv.org/abs/2006.01937v1

## One-line
Introduces a semi-algebraic extremal relaxation of triangle-free strongly regular graphs and proves upper bounds on $a(\rho)$ — the maximum, over triangle-free $\rho$-regular graphs, of the minimum common-neighborhood density of a non-adjacent pair.

## Key claim
For $\rho \le 1/3$, $a(\rho) \le a_0(\rho)$, a piecewise-defined upper bound that is tight at $\rho = 2/5, 5/16, 3/10, 11/50$ (realized by $C_5$, Clebsch, Petersen, Higman–Sims). For small $\rho$ ($\le \rho_0 \approx 0.263$), the bound coincides with a purely combinatorial reformulation of the algebraic Krein condition $K_1 K_2 \ge 0$.

## Method
Flag-algebra-style density counting on the twin-free weighted reduction $(G,\mu)$ of triangle-free regular graphs, combined with light Cauchy–Schwarz ($\llbracket f^2 \rrbracket^{\sigma,\eta} \ge 0$) and linear-programming duality on densities of small subgraphs (types $I$, $P$, $N$, $E$, $D$, $Q_1$, $Q_2$). For $\rho \le \rho_0$ the proof bounds $\llbracket S_4^I(S_4^I + T_4^I)\rrbracket^{I,[1,2]}$ from both sides; a finiteness theorem uses an iterative neighborhood-doubling argument on a "small-weight" vertex set.

## Result
$a_0(\rho)$ is given piecewise: Krein root $\overline{\text{Krein}}(\rho)$ on $[0,\rho_0]$, a related $\widetilde{\text{Krein}}(\rho)$ on $[\rho_0,\rho_1]$ ($\rho_1 \approx 0.271$), $(1-3\rho)/2$ on $[\rho_1,\rho_2]$, an algebraic Improved$(\rho)$ on $[\rho_2, 9/32]$, then linear segments $\rho/3$, $2\rho - 1/2$, $5\rho/2$ up to $1/3$. Finiteness: for every $\epsilon > 0$ only finitely many $\rho$ satisfy $a(\rho) \ge \epsilon$ (bound double-exponential in $1/\epsilon$); every triangle-free graphon with $a(W) > 0$ is a finite step-function.

## Why it matters here
Demonstrates that flag-algebra densities give purely combinatorial proofs of algebraic spectral conditions (Krein bounds for SRGs) — directly relevant to einstein wiki techniques for SDP/flag-algebra approaches to extremal problems (P1 SDP-relaxation finding, autocorrelation, kissing-number LP duality). Shows a working template: detect a singular point in a continuous relaxation, then trace it back to a known algebraic invariant.

## Open questions / connections
- Can $a(\rho) \le \text{Krein}(\rho)$ be tightened at $\rho = 7/16, 5/28, 7/50$ to certify $M_{22}$, Gewirtz, Hoffman–Singleton as extremal? Or rule out the hypothetical Moore graph at $\rho = 57/3250$?
- Is there any rational $\rho \in (0, 1/3]$ with $a(\rho) = 0$ — i.e., no triangle-free $\rho$-regular weighted twin-free graph of diameter 2?
- Can $a(1/3)$ be computed exactly? Connects to Erdős–Simonovits and Brandt–Thomassé [BT05].
- General: can flag algebras be exported as a tool to rule out parameter sets for highly symmetric algebraic-combinatorial objects?

## Key terms
flag algebras, triangle-free strongly regular graphs, Krein conditions, edge density, common neighborhood, Cauchy-Schwarz inequality, semidefinite programming, graphon limits, Higman-Sims, Petersen, Clebsch, extremal combinatorics, Razborov, Erdős-Simonovits
