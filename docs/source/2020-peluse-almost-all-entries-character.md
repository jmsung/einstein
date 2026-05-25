---
type: source
kind: paper
title: Almost all entries in the character table of the symmetric group are multiples of any given prime
authors: Sarah Peluse, Kannan Soundararajan
year: 2020
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/2010.12410v2
source_local: ../raw/2020-peluse-almost-all-entries-character.pdf
topic: general-knowledge
cites: 
---

# Almost all entries in the character table of the symmetric group are multiples of any given prime

**Authors:** Sarah Peluse, Kannan Soundararajan  ·  **Year:** 2020  ·  **Source:** http://arxiv.org/abs/2010.12410v2

## One-line
Resolves Miller's conjecture: for any fixed prime $q$, the proportion of entries in the character table of $S_N$ not divisible by $q$ tends to $0$ as $N \to \infty$.

## Key claim
For $N$ large and any prime $q \le (\log N)/(\log\log N)^2$, the number of entries $\chi^\lambda_\mu$ in the character table of $S_N$ that are not divisible by $q$ is $O(p(N)^2 N^{-1/(12q)})$, where $p(N)$ is the partition function.

## Method
Combines two ingredients: (i) Frobenius/Murnaghan–Nakayama vanishing — if $\lambda$ is a $t$-core then $\chi^\lambda_\mu = 0$ whenever $\mu$ has a part of size $t$; (ii) a $q$-adic reduction lemma — collapsing $q$ equal parts of size $m$ into one part of size $qm$ preserves $\chi^\lambda_\mu \pmod q$. Iterating (ii) until no part repeats $\ge q$ times yields a partition $\tilde\mu$ whose largest part exceeds $\frac{\sqrt{6N}}{2\pi}(\log N)(1+1/(5q))$ for all but exponentially few $\mu$ (proven via generating-function / saddle-point analysis of $\prod (1-z^n)^{-1}$ truncated at high $q$-powers, using Mahler/de Bruijn estimates for partitions into powers of $q$).

## Result
Theorem 1: at most $O(p(N)^2 N^{-1/(12q)})$ non-divisible entries, uniformly for primes $q \le (\log N)/(\log\log N)^2$. Proposition 1 quantifies $t$-core dominance: if $\mu$ has a part $\ge \frac{\sqrt{6N}}{2\pi}(\log N)(1+1/A)$, then $\chi^\lambda_\mu = 0$ for all but $O(p(N)(\log N/N)^{1/(2A)})$ partitions $\lambda$. Proposition 2 controls the $q$-adic reduction: the largest part of $\tilde\mu$ exceeds $\frac{\sqrt{6N}}{2\pi}(\log N)(1+1/(5q))$ except for $O(p(N)\exp(-N^{1/(15q)}))$ partitions $\mu$.

## Why it matters here
General background; no direct arena tie — character-table divisibility for $S_N$ is not on the 23-problem inventory. Indirect value: the proof technique (generating-function saddle-point estimates for partition statistics restricted to atypical largest-part regimes, Hardy–Ramanujan asymptotics) is a reusable analytic-combinatorics template for any extremal-partition or rare-event-on-Young-diagram question.

## Open questions / connections
- Divisibility by higher prime powers ($q^k$): the argument does not extend; Miller's data suggest density $\to 1$ but no proof.
- Density of *zeros* in the character table: Proposition 1 gives $\ge C/\log N$; whether positive density is unknown (cf. Larsen–Miller for finite simple groups of Lie type, where almost every entry is zero).
- Quantitative bottleneck: the $N^{-1/(12q)}$ rate is limited by Lemma 5 of Morotti ($t$-core count); improving that lemma improves Theorem 1.

## Key terms
character table, symmetric group $S_N$, Miller's conjecture, $t$-core partition, Murnaghan–Nakayama rule, hook length, Hardy–Ramanujan asymptotic, Erdős–Lehner, partitions into prime powers, Mahler partition problem, generating function saddle point, Plancherel measure
