---
type: source
kind: paper
title: On maximal product sets of random sets
authors: Daniele Mastrostefano
year: 2020
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2005.04663
source_local: ../raw/2020-mastrostefano-maximal-product-sets-random.pdf
topic: general-knowledge
cites:
---

# On maximal product sets of random sets

**Authors:** Daniele Mastrostefano  ·  **Year:** 2020  ·  **Source:** https://arxiv.org/abs/2005.04663

## One-line
Characterizes exactly when a random subset $A \subset \{1,\dots,N\}$ (each element kept independently with probability $\alpha$) has maximal product set $|AA| \sim |A|^2/2$ asymptotically almost surely.

## Key claim
For $A \in B(N,\alpha)$, $|AA| \sim |A|^2/2$ with probability $1-o(1)$ **if and only if** $\log(\alpha^2 (\log N)^{\log 4 - 1}) / \sqrt{\log\log N} \to -\infty$. This sharpens Cilleruelo–Ramana–Ramaré's sufficient condition $\alpha = o(1/\sqrt{\log N})$ and closes a gap leaving the regime $\alpha \asymp 1/\sqrt{\log N}$ undetermined.

## Method
Express $\mathbb{E}[X_A]$ where $X_A = (|A|^2+|A|)/2 - |AA|$ as a sum over $n \le N^2$ involving $\tau_N(n)$ (representations $n=jk$ with $j,k \le N$). Split by proximity of $\Omega(n)$ to $2\log\log N$ via an Erdős–Kac-style concentration (Turán–Kubilius), then Taylor-expand $(1-\alpha^2)^{\tau_N(n)/2}$ on the bulk and use trivial bounds on the tail. Sharp upper/lower bounds combine Selberg–Delange (Landau's theorem for $\pi_k(N^2)$), Norton's bounds on partial sums of $x^k/k!$, and Shiu's theorem.

## Result
The threshold function is $t(N) = (\log N)^{\log 4 - 1} \exp(\xi(N)\sqrt{\log\log N})$: maximality holds when $\alpha^2 t(N) \to 0$ for every $\xi(N) \to \infty$, and fails when this quantity is bounded away from 0. Also gives a new proof of Proposition 1.2 via Cauchy–Schwarz $|A|^4 \le |AA| \cdot E(A)$ on multiplicative energy. Implies the random model of shifted sums of two squares $Q_N - 1$ (where $\alpha \asymp 1/\sqrt{\log N}$) does have maximal product set.

## Why it matters here
General background; no direct arena tie. Closest possible relevance is to the additive/multiplicative-combinatorics flavor of $B_h$-set and Sidon-set problems (P19 family) — the technique of bounding multiplicative energy via Cauchy–Schwarz and the Erdős–Kac concentration of $\omega(n)$ are reusable tools for any random-construction argument on integer sets.

## Open questions / connections
- Extends Cilleruelo–Ramana–Ramaré (2017) and complements Ford (2008, 2018) on the multiplication-table problem and extremal product-set sizes.
- Leaves open the *deterministic* analogue: characterize $A \subset [N]$ with $|AA| \sim |A|^2/2$ — Ford's construction shows the random threshold is not the deterministic boundary.
- Sanna (2019) extends to iterated product sets $AA\cdots A$; further iteration thresholds remain to be sharpened.

## Key terms
product set, multiplicative energy, random subset model, Erdős–Kac theorem, Turán–Kubilius inequality, Selberg–Delange method, multiplication table problem, Ford, divisor function, $\Omega(n)$ prime factor counting, Shiu's theorem, Norton bounds, $B_h$ sets
