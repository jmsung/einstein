---
type: source
kind: paper
title: Minimizing the Number of Carries in Addition
authors: N. Alon
year: 2012
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1209.1131
source_local: ../raw/2012-alon-minimizing-number-carries-addition.pdf
topic: general-knowledge
cites:
---

# Minimizing the Number of Carries in Addition

**Authors:** N. Alon  ·  **Year:** 2012  ·  **Source:** https://arxiv.org/abs/1209.1131

## One-line
Proves that balanced digits $\{-(p-1)/2,\ldots,(p-1)/2\}$ minimize the probability of carry when adding random one-digit numbers in any odd prime base $p$.

## Key claim
For every odd prime $p$, the probability of carry when adding two random independent one-digit numbers using any fixed set of $p$ digits in base $p$ is at least $\frac{p^2-1}{4p^2}$, confirming the Diaconis–Shao–Soundararajan conjecture for all primes (previously known only asymptotically with a tower-function threshold $p_0(\epsilon)$).

## Method
Reformulates the carry-minimization problem as a sumset question in $\mathbb{Z}_{p^2}$: minimize ordered pairs $(a,b) \in A \times A$ with $a+b \notin A$, where $A \subset \mathbb{Z}_{p^2}$ has $|A|=p$ and elements pairwise distinct mod $p$. The bound follows almost immediately from Pollard's 1975 generalization of the Cauchy–Davenport theorem applied with $m=p^2$, $A=B$, $r=(p-1)/2$, giving $N_1+\cdots+N_r \geq r(2p-r)$.

## Result
At least $r(p-r) = \frac{(p-1)(p+1)}{4} = \frac{p^2-1}{4}$ ordered pairs sum outside $A$, yielding the tight bound $\frac{p^2-1}{4p^2}$. Extension via Pollard's $k$-set theorem (Theorem 4.1): for any $k \geq 2$, balanced digits minimize carry probability, which equals $\Pr[|S_k| > (p-1)/2]$ for $S_k$ a sum of $k$ uniform variables on $\{-(p-1)/2,\ldots,(p-1)/2\}$. The bound holds even when distinct digit sets are used for each summand and the result.

## Why it matters here
General background; no direct arena tie. Possible relevance to combinatorial/additive-number-theory problems involving sumsets, coset representatives, or extremal configurations in $\mathbb{Z}_n$ — Pollard's inequality is a sharper tool than Cauchy–Davenport for such extremal questions.

## Open questions / connections
- Conjecture remains open for non-prime bases $b$ (composite moduli break the coprimality condition $(x-y,m)=1$ that Pollard's theorem requires).
- Related results for addition in $\mathbb{Z}_p$ (rather than $\mathbb{Z}_{p^2}$) appear in Lev (2001), "Linear equations over $\mathbb{Z}/p\mathbb{Z}$ and moments of exponential sums."
- Connects to Borodin–Diaconis–Fulman (2010) framework of carries as one-dependent determinantal processes.

## Key terms
carry probability, balanced digits, Cauchy-Davenport theorem, Pollard's theorem, sumset inequality, additive combinatorics, modular addition, coset representatives, Diaconis-Shao-Soundararajan conjecture, Alon, $\mathbb{Z}_{p^2}$, extremal sumsets
