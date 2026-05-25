---
type: source
kind: paper
title: Two Conjectures in Ramsey-Turán Theory
authors: Jaehoon Kim, Younjin Kim, Hong Liu
year: 2018
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1803.04721
source_local: ../raw/2018-kim-two-conjectures-ramsey-tur-theory.pdf
topic: general-knowledge
cites:
---

# Two Conjectures in Ramsey-Turán Theory

**Authors:** Jaehoon Kim, Younjin Kim, Hong Liu  ·  **Year:** 2018  ·  **Source:** https://arxiv.org/abs/1803.04721

## One-line
Determines exact Ramsey-Turán densities $\varrho(K_3, K_s, \delta)$ for $s \in \{3,4,5\}$ at small $\delta$, and pins down $\mathrm{RT}(n, K_8, o(\sqrt{n \log n})) = n^2/4 + o(n^2)$.

## Key claim
For sufficiently small $\delta > 0$: $\varrho(K_3,K_3,\delta) = \tfrac14 + \tfrac{\delta}{2}$, $\varrho(K_3,K_4,\delta) = \tfrac13 + \tfrac{\delta}{2} + \tfrac{3\delta^2}{2}$, $\varrho(K_3,K_5,\delta) = \tfrac{2}{5} + \tfrac{\delta}{2}$ (confirming a 1979 Erdős–Sós conjecture); and $\mathrm{RT}(n,K_8,o(\sqrt{n\log n})) = n^2/4 + o(n^2)$ (answering Balogh–Hu–Simonovits).

## Method
Combines Szemerédi regularity (multicolour version) with a dependent random choice lemma to forbid "chubby" triangles in the reduced graph, then Füredi-style stability for $K_{p+1}$-free graphs to pin down the partition structure. A second proof for $\varrho(K_3,K_3,\delta)$ avoids regularity entirely via a direct max-degree extraction + max-cut argument. Lower bounds use unions of Turán graphs $T_s(n)$ with Brandt-dense almost-regular triangle-free graphs $F(n,d)$ embedded in parts; the $K_3 \vee K_6$ construction adds a 5-cycle clone-set gadget.

## Result
Three exact $\delta$-dependent densities for triangle-vs-clique 2-colour Ramsey-Turán; new phase-transition value $n^2/4$ for $K_8$ below the $\sqrt{n \log n}$ window — the first nontrivial exact extremal density at the third phase transition for an even clique. Also: for the slightly-sub-sublinear regime $g_s(n) = n / e^{\omega(n)(\log n)^{1-1/s}}$, $\mathrm{RT}(n,K_3,K_{2s-1},g_s(n)) = \tfrac12(1 - \tfrac{1}{R(3,s)-1})n^2 + o(n^2)$, tying the answer directly to off-diagonal Ramsey numbers $R(3,s)$.

## Why it matters here
General background; no direct arena tie. Closest relevance is Erdős-style extremal combinatorics with independence-number constraints — could inform discrete-geometry / extremal-graph problems where independence/anti-clique structure matters (P-class with `extremal_graph` or `combinatorics` categories), but no immediate optimizer hook.

## Open questions / connections
- Conjecture: $\varrho(K_3,K_6,\delta) = \tfrac{5}{12} + \tfrac{\delta}{2} + 2\delta^2$ (lower-bound construction given via 5-cycle clone gadget; matching upper bound open).
- Conjecture 8.1: $\varrho(K_3,K_{2s}) = \tfrac12(1 - 1/R(3,s))$ for all $s \geq 2$ — directly couples even-clique RT density to off-diagonal Ramsey numbers.
- Open: $\varrho(K_3,K_{2s-1})$ general Erdős–Hajnal–Simonovits–Sós–Szemerédi conjecture remains for $s \geq 3$ at $\delta \to 0$ limit; this paper gives the $g_s(n)$-regime evidence only.

## Key terms
Ramsey-Turán density, $\varrho(K_3,K_s,\delta)$, off-diagonal Ramsey number $R(3,k)$, Erdős–Sós conjecture, phase transition, Szemerédi regularity lemma, dependent random choice, Füredi stability, Bollobás–Erdős construction, triangle-free graph, independence number, max-cut partition, Brandt's theorem, Shearer's bound
