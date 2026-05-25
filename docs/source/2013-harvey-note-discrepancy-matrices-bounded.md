---
type: source
kind: paper
title: A note on the discrepancy of matrices with bounded row and column sums
authors: Nicholas J. A. Harvey
year: 2013
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1307.2159
source_local: ../raw/2013-harvey-note-discrepancy-matrices-bounded.pdf
topic: general-knowledge
cites:
---

# A note on the discrepancy of matrices with bounded row and column sums

**Authors:** Nicholas J. A. Harvey  ·  **Year:** 2013  ·  **Source:** https://arxiv.org/abs/1307.2159

## One-line
Generalizes a folklore Lovász-local-lemma discrepancy bound from bounded-degree hypergraphs to real matrices with bounded row/column $\ell_1$ sums.

## Key claim
**Theorem 2:** For an $n \times m$ real matrix $V$ with $|V_{i,j}| \le 1$, row $\ell_1$-norm $\le R$, column $\ell_1$-norm $\le \Delta$ (with $R \ge \max\{\Delta, 4\}$, $\Delta \ge 2$), there exists $y \in \{-1,+1\}^m$ with $\|Vy\|_\infty \le O(\sqrt{R \log(R\Delta)})$. Recovers the hypergraph bound $2\sqrt{R \ln(R\Delta)}$ (max edge size $R$, max degree $\Delta$) as the 0/1 special case.

## Method
Lovász Local Lemma applied to a **stratified** decomposition: each row is partitioned into level sets $S_{i,k} = \{j : \lfloor -\lg A_{i,j}\rfloor = k\}$ whose entries have magnitude $\approx 2^{-k}$. Per-level discrepancy bounded by Hoeffding ($\Pr[|X|>a] \le 2e^{-a^2/2\ell}$); dependencies controlled column-wise using $\|a_j\|_1 \le \delta$ to sum the LLL weights. Reduce Theorem 2 to a non-negative-matrix Theorem 3 by rescaling and splitting positive/negative entries.

## Result
**Theorem 3:** For non-negative $A$ with $\|\sum_j a_j\|_\infty \le 1$, $\|a_j\|_\infty \le \beta$, $\|a_j\|_1 \le \delta$, $\beta \le \min\{\delta/2, 1/4\}$, $\delta \le 1$, and $\alpha := \lg(\delta/\beta^2) \ge \sqrt{2}$: there is $y \in \{-1,+1\}^m$ with $\|Ay\|_\infty \le 16\alpha\sqrt{\beta}$. Author conjectures the $\log$ factor is removable: $\|Vy\|_\infty \le O(\sqrt{R})$ (Conjecture 7).

## Why it matters here
General background; no direct arena tie. Potentially relevant as a tool for **autocorrelation / discrepancy-style** problems where a $\pm 1$ assignment must balance many bounded linear forms — Hoeffding+LLL stratification is a reusable template. Related to Kadison-Singer / Marcus-Spielman-Srivastava ($\sqrt{\delta}$ bound) via Conjecture 9 unifying both as a matrix-valued discrepancy statement.

## Open questions / connections
- **Conjecture 7:** Can the $\sqrt{\log(R\Delta)}$ factor be removed, matching Beck-Fiala-style $O(\sqrt{R})$?
- **Conjecture 9:** PSD matrix generalization $\|\sum y_i A_i\| \le O(\sqrt{\delta})$ subsuming both Theorem 3 (diagonal case) and Marcus-Spielman-Srivastava (rank-1 / Kadison-Singer, $\sqrt{\delta}$).
- Extends Beck-Fiala (1981), Spencer's "six standard deviations" (1985), and Srinivasan's sparse-matrix discrepancy (1997).

## Key terms
discrepancy theory, Lovász local lemma, Beck-Fiala theorem, Spencer six standard deviations, hypergraph coloring, Hoeffding bound, stratification, bounded row sum, bounded column sum, Kadison-Singer, Marcus-Spielman-Srivastava, $\pm 1$ coloring
