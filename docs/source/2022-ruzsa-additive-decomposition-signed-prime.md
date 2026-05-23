---
type: source
kind: paper
title: Additive decomposition of signed prime
authors: Imre Z. Ruzsa
year: 2022
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/2204.14013v1
source_local: ../raw/2022-ruzsa-additive-decomposition-signed-prime.pdf
topic: general-knowledge
cites: 
---

# Additive decomposition of signed prime

**Authors:** Imre Z. Ruzsa  ·  **Year:** 2022  ·  **Source:** http://arxiv.org/abs/2204.14013v1

## One-line
Under the prime-tuple hypothesis, the set of signed primes $\{p : |p| > 3\}$ can be written as a sumset $A+B$ with each prime uniquely represented.

## Key claim
Assuming the prime-tuple hypothesis, there exist infinite sets $A, B \subset \mathbb{Z}$ (equivalently $A, B \subset \mathbb{N}$ with $A-B$) such that $A+B$ equals exactly the signed primes with $|p|>3$, and every such prime has a unique representation $p = a+b$. (Ostmann's original "inverse Goldbach" for positive primes alone remains open and is expected negative; admitting negative primes changes the answer.)

## Method
Greedy/inductive construction with dynamically growing **modular restrictions**: maintain prime-compatible pairs $(U_p, V_p) \subset \mathbb{Z}_p$ satisfying $(U\setminus V)-(V\setminus U)=\mathbb{Z}_p^*$, and at each step add a new element $x$ via the prime-tuple hypothesis (Dickson–Hardy–Littlewood) so that $x - B_{n-1}$ and $A_{n-1}-x+r_n$ are all prime. A probabilistic lemma (random $U/V$ assignment, pairing $(z,2z),(3z,4z),\dots$ and a $(3/4)^{(p-1)/2-n}$ failure bound) shows prime-compatible extensions exist whenever $|W| < (p-1)/2 - \log p/\log(4/3)$.

## Result
Theorems 1 and 2 are established conditionally on the prime-tuple hypothesis. The construction yields $A_n, B_n$ with $|A_n|, |B_n| \le n$, growing infinitely often, all pairwise differences prime, covering $r_1, r_2, \dots$ in order of absolute value. Bases $\pm 2, \pm 3$ are necessarily omitted; seed $A_2=\{1,11\}$, $B_2=\{6\}$ handles the $\bmod 5$ obstruction for $\pm 5$.

## Why it matters here
General background in additive combinatorics / sieve theory — illustrates the **prime-tuple (Dickson) hypothesis as a constructive lever** plus **modular obstruction management** via Chinese-remainder-style residue restrictions. Relevant to Einstein Arena sieve-theory and Sidon/sumset-style problems where one builds sets avoiding congruence collisions; no direct arena tie to a specific problem in the inventory.

## Open questions / connections
- Problem 3: can the existence of infinite $A, B \subset \mathbb{N}$ with $A+B \subset P$ be proved unconditionally (without prime-tuple hypothesis)? Recent twin-prime advances give infinite $A$ + arbitrarily large finite $B$.
- Problem 4: unconditional infinite $A, B \subset \mathbb{N}$ with no $a+b$ divisible by any prime $\equiv 1 \pmod 4$ (the $4k-1$ case is easy).
- Extends Elsholtz (2001, 2006) on Ostmann's inverse Goldbach negative direction; complements Granville (1990) showing primes contain general sumsets under the same hypothesis.

## Key terms
inverse Goldbach, Ostmann problem, signed primes, sumset decomposition, prime-tuple hypothesis, Dickson conjecture, twin prime, prime-compatible residues, Chinese remainder obstruction, additive combinatorics, sieve theory, Ruzsa, Elsholtz, Granville
