---
type: source
kind: paper
title: On even entries in the character table of the symmetric group
authors: Sarah Peluse
year: 2020
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2007.06652
source_local: ../raw/2020-peluse-even-entries-character-table.pdf
topic: general-knowledge
cites:
---

# On even entries in the character table of the symmetric group

**Authors:** Sarah Peluse  ·  **Year:** 2020  ·  **Source:** https://arxiv.org/abs/2007.06652

## One-line
Proves that almost every entry in the character table of the symmetric group $S_n$ is divisible by $p$ (as $n \to \infty$) for $p=2,3,5,7,11,13$, resolving Miller's conjecture for $p=2$.

## Key claim
**Theorem 1.1:** The density of odd entries in the character table of $S_n$ tends to $0$ as $n \to \infty$. **Theorem 1.2:** For $p \in \{2,3,5,7,11,13\}$, there exists $\delta_p > 0$ such that the density of entries not divisible by $p$ is $O_p(n^{-\delta_p})$. The restriction $p \le 13$ comes from where an independence threshold $\varepsilon_1(p) > 1/4$ holds.

## Method
Combines three classical tools: (i) Lemma 2.1 — collapsing $p$ equal parts of size $m$ in a cycle type $\mu$ into one part of size $pm$ preserves $\chi^\lambda_\mu \pmod p$; (ii) Murnaghan–Nakayama implies $\chi^\lambda_\mu = 0$ when $\lambda$ is a $t$-core and $\mu$ has a part of size $t$; (iii) Mellin-transform / saddle-point asymptotics (Rademacher, Grabner–Knopfmacher–Wagner) on generating functions of partition statistics $M_\mu(k) = \sum_{\mu_i = k p^j} \mu_i$. Chebyshev's inequality handles $p=2$ via $k=1,3,5$; for larger $p$ a quasi-independence argument over $\sim n^{1/4-\varepsilon_p}$ values of $k$ is needed.

## Result
For almost every partition $\mu$ of $n$, the "$p$-reduced" cycle type $\tilde\mu$ has largest part $\ge (1+\gamma_p)\tfrac{\sqrt 6}{2\pi}\sqrt n \log n$ — well above the typical largest part $\sim \tfrac{\sqrt 6}{2\pi}\sqrt n \log n$ — forcing $\tilde\mu_1$ into the regime where Lemma 2.3 guarantees most $\lambda$ are $\tilde\mu_1$-cores, hence $\chi^\lambda_{\tilde\mu}=0 \equiv \chi^\lambda_\mu \pmod p$. Quantitative rate: $O_p(n^{-\delta_p})$ density of $p$-indivisible entries for $p\le 13$.

## Why it matters here
General background; no direct arena tie. Relevant only as a methodological exemplar of saddle-point / Mellin-transform asymptotics on partition generating functions and of "$t$-core" combinatorial structure — techniques whose toolkit (Rademacher's formula, Hardy–Ramanujan circle method, Grabner–Knopfmacher–Wagner scheme) could conceivably inform sieve-theory or extremal-combinatorics problems but is not used by any current Einstein Arena problem.

## Open questions / connections
- Does the density of *zero* entries in $S_n$ character tables tend to a positive constant? (Data in Miller suggests yes; methods here say nothing.)
- Extending Theorem 1.2 beyond $p=13$ requires breaking the $\varepsilon_1(p) > 1/4$ barrier — needs genuine dependence between the $M_\mu(k)$ rather than the quasi-independence used here.
- Connects to Larsen–Miller (arXiv:2006.00847) on character-table sparsity for groups of Lie type.

## Key terms
symmetric group character table, Miller conjecture, $p$-divisibility, $t$-core partition, Murnaghan–Nakayama rule, hook length, Mellin transform, saddle-point asymptotics, Rademacher formula, partition statistics, Peluse, Grabner–Knopfmacher–Wagner
