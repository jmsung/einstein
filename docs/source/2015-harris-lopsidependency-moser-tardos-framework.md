---
type: source
kind: paper
title: Lopsidependency in the Moser-Tardos Framework
authors: David G. Harris
year: 2015
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1610.02420
source_local: ../raw/2015-harris-lopsidependency-moser-tardos-framework.pdf
topic: general-knowledge
cites:
---

# Lopsidependency in the Moser-Tardos Framework

**Authors:** David G. Harris  ·  **Year:** 2015  ·  **Source:** https://arxiv.org/abs/1610.02420

## One-line
A new convergence criterion for the Moser-Tardos resampling algorithm in the variable-assignment setting that exploits *agreement* between bad-events, yielding bounds that can exceed even Shearer's optimal LLL criterion.

## Key claim
For variable-assignment LLLL, MT terminates with probability 1 whenever $\mu(B) \ge P_\Omega(B)\sum_{Y\text{ orderable to }B}\prod_{B'\in Y}\mu(B')$, where "orderable" sets are built from sequential lopsidependency witnesses. For $k$-SAT with each variable in $L$ clauses, this improves the Gebauer-Szabó-Tardos bound $L \le 2^{k+1}/(e(k+1))$ to $L \le \frac{2^{k+1}(1-1/k)^k}{k-1} - \frac{2}{k}$.

## Method
Reanalysis (not modification) of the standard Moser-Tardos resampling algorithm via a refined witness-tree construction: only the *latest* occurrence of each variable is retained, and children of a tree node must form an "orderable" set (definition 1.1 — a sequential elimination property via lopsidependency witnesses $z_i$). On-line stochasticity replaces the resampling-table argument, allowing a tighter union bound over a pruned witness-tree space. A parallel RNC algorithm is also developed, matching the new criterion up to a $(1+\epsilon)$ slack.

## Result
- $k$-SAT bounded occurrence: $L \le \frac{2^{k+1}(1-1/k)^k}{k-1} - \frac{2}{k}$, strictly better than $2^{k+1}/(e(k+1))$ for small $k$.
- $k$-uniform $c$-colorable hypergraph: $L \le \frac{c^k(1-1/k)^{k-1}}{k(c-1)}$, interpolating between LLL and LLLL regimes.
- Second Hamiltonian cycle in $k$-regular graphs: simple proof for $k \ge 43$ (vs Haxell's $k \ge 23$ non-constructive, but with much simpler argument).
- Independent transversal: $b \ge 4\Delta - 1$ (constructive, beats Pegden's $b \ge 4\Delta$).
- Off-diagonal Ramsey $R(s,t)$: algorithmic coloring in time $n^{s/4+O(1)}$ matching Spencer's $\Omega_s((t/\log t)^{(s+1)/2})$ lower bound, plus an RNC variant.

## Why it matters here
General background; no direct arena tie. LLL/LLLL machinery is a general probabilistic-method tool for showing existence of combinatorial configurations — potentially relevant if any Einstein Arena problem reduces to "configuration avoiding bad-events with bounded lopsidependency" (e.g., extremal combinatorics or coloring-style problems), but no current arena problem in the inventory is directly framed this way.

## Open questions / connections
- Extends Moser-Tardos (2010), Pegden (2014), Bissacot et al (2011), Kolipaka-Szegedy (2011); explicitly goes *beyond* Shearer's criterion in the restricted variable-assignment class.
- Open: can the "orderable set" decomposition be derandomized as in Chandrasekaran-Goyal-Haeupler (2013)?
- Open: tightness of the $k$-SAT bound at small $k$ — gap between $L \le \frac{2^{k+1}(1-1/k)^k}{k-1} - \frac{2}{k}$ and the Kratochvíl-Savický-Tuza NP-completeness threshold.
- Connects to MT-distribution analysis (Haeupler-Saha-Srinivasan) used for problems where bad-events aren't resampled (e.g., blue $K_t$ in Ramsey).

## Key terms
Lovász Local Lemma, Lopsided Local Lemma, Moser-Tardos algorithm, Shearer criterion, resampling, witness tree, lopsidependency, orderable set, k-SAT bounded occurrence, hypergraph coloring, independent transversal, off-diagonal Ramsey number, second Hamiltonian cycle, variable-assignment LLLL, parallel RNC algorithm, probabilistic method
