---
type: source
kind: paper
title: On divisibility by primes in columns of character tables of symmetric groups
authors: L. Morotti
year: 2019
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1902.02625
source_local: ../raw/2019-morotti-divisibility-primes-columns-character.pdf
topic: general-knowledge
cites:
---

# On divisibility by primes in columns of character tables of symmetric groups

**Authors:** L. Morotti  ·  **Year:** 2019  ·  **Source:** https://arxiv.org/abs/1902.02625

## One-line
For any prime $p$, the proportion of entries divisible by $p$ in certain columns of the character table of the symmetric group $S_n$ tends to $1$ as $n \to \infty$.

## Key claim
For prime $p$, $n \geq 2$, $c > \sqrt{3/2}\,\pi$, and $\lambda = (a_1^{b_1},\dots,a_h^{b_h}) \in \Omega_p(n)$ satisfying $p^s \leq b_i$ and $a_i p^s \geq c\sqrt{n}\log(n)$ for some $i,s$: for any $\mu \in K_p(\lambda)$,
$$\frac{|\{\alpha \in P(n) : \chi^\alpha_\mu \equiv 0 \pmod p\}|}{p(n)} \geq 1 - \frac{c^4 d \log(n)}{n^{c\pi/\sqrt{6} - 1/2}}$$
for some constant $d$, which tends to $1$ since the exponent $c\pi/\sqrt{6} - 1/2 > 0$.

## Method
Combinatorial / representation-theoretic. The proof reduces divisibility statements to counting $k$-core partitions via the Murnaghan–Nakayama formula: if $\mu$ has a large part, then a character value with that part as the first cycle vanishes mod $p$ unless the $k$-core (with $k = $ that part) is suitable. Lower bounds on $c_k(n)/p(n)$ come from a recursive bound $p(n) - c_k(n) \leq (k+1)p(n-k)$ combined with Hardy–Ramanujan asymptotics $p(m) \asymp e^{\pi\sqrt{2m/3}}/m$.

## Result
Establishes that $c_k(n)/p(n) \to 1$ when $k \geq c\sqrt{n}\log(n)$ with $c > \sqrt{3/2}\,\pi$ (Lemma 6), with explicit polynomial-rate convergence. Theorem 2 then transfers this to character-table columns whose cycle type $\mu$ (or its $p$-quotient associate $\mu^* = \lambda$) contains a sufficiently large part. Corollary 3: if $\lambda \in \Omega_p(n)$ has at most $\sqrt{n}/(c_p \log n)$ distinct parts, the column proportion of $p$-divisible entries tends to $1$. Extends Gluck's $p=2$ result to all primes and broader columns; insufficient to prove Miller's full conjecture that $E_p(n)/p(n)^2 \to 1$.

## Why it matters here
General background; no direct arena tie. This is pure representation theory of $S_n$ — character-table divisibility statistics — far from the optimization, sphere-packing, and discrete-geometry problems in the Einstein Arena.

## Open questions / connections
- Miller's Conjecture (full): does $E_p(n)/p(n)^2 \to 1$ for every prime $p$? This paper covers only certain columns, not the global count.
- Can the lower bound on $k$ (threshold $c\sqrt{n}\log n$ with $c > \sqrt{3/2}\,\pi$) be sharpened, e.g. to $k = \omega(\sqrt{n})$?
- Extends Gluck (2019, $p=2$) and Miller (2019, [3]); builds on Hardy–Ramanujan (1918) partition asymptotics and Olsson's $k$-core combinatorics.

## Key terms
character table, symmetric group $S_n$, partition function $p(n)$, $k$-core partition, $p$-quotient, Murnaghan–Nakayama formula, Hardy–Ramanujan asymptotics, Miller conjecture, Gluck parity, multipartition, divisibility by primes, modular representation theory
