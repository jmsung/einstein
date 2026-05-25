---
type: source
kind: paper
title: Regular Intersecting Families
authors: F. Ihringer, A. Kupavskii
year: 2017
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1709.10462
source_local: ../raw/2017-ihringer-regular-intersecting-families.pdf
topic: general-knowledge
cites:
---

# Regular Intersecting Families

**Authors:** F. Ihringer, A. Kupavskii  ·  **Year:** 2017  ·  **Source:** https://arxiv.org/abs/1709.10462

## One-line
Upper and lower bounds on the size of $k$-uniform intersecting families on $[n]$ in which every ground-set element has (approximately) the same degree.

## Key claim
A regular $k$-uniform intersecting family $\mathcal{F} \subset \binom{[n]}{k}$ has size $o\!\binom{n-1}{k-1}$ if and only if $k = o(n)$; for any $r$ and any $\alpha$-irregular family with $n > C(r,\alpha)\,k$, $|\mathcal{F}| \leq C \binom{n-r}{k-r}$.

## Method
Two complementary tools: (i) the Dinur–Friedgut junta approximation theorem for intersecting families, used to argue that a large $\alpha$-irregular family forces a high-degree element via a junta center (Theorems 9, 10); (ii) Delsarte's linear-programming bound on the Johnson scheme, applied with eigenvalues $P_{ji}$ from Lemma 17 and the MacWilliams transform, to derive a Hoffman-type bound $|\mathcal{F}| \leq \binom{n}{k} / \bigl(1 + \tfrac{k(n-k)(k-1)(n-k-2)}{(n-k)(k-1)(n-2)}\bigr)$ (Theorem 11/21) and to reprove Fürdi's $n \leq k^2-k+1$ result with projective-plane equality (Theorem 7).

## Result
For $n > k^2-k+1$ no regular $k$-uniform intersecting family exists; at $n = k^2-k+1$ the only example is a projective plane of order $k-1$. For $n = 2k$ with $k = 2^t \geq 4$, the maximum size is exactly $\binom{2k-1}{k} - 3$ (Theorem 25); for $k$ not a power of 2 the EKR bound $\binom{2k-1}{k}$ is achieved (Brace–Daykin). Construction $\mathcal{F} + \mathcal{G}$ using projective planes plus a disjoint regular family achieves $\Theta_c\!\binom{n-1}{k-1}$ for any $n > ck$.

## Why it matters here
General background for extremal-set-system / EKR-flavored problems in the Arena (e.g. autocorrelation, Sidon-set, and combinatorial-packing categories); supplies the Johnson-scheme LP / eigenvalue machinery and Hoffman-style bounds that generalize to Grassmann ($q$-Johnson) and other cometric schemes — useful template whenever an Arena problem reduces to a regular/symmetric extremal family on a Johnson-like scheme.

## Open questions / connections
- Do regular intersecting families exist for all sufficiently large $n,k$ with $k \geq (1+o(1))\sqrt{n}$? (Matches Ellis–Kalai–Lifshitz symmetric construction at $k \geq 1.1527\sqrt{n}$.)
- For $k-1$ not a prime power (and Bruck–Ryser–Chowla excluded orders 6, 10, 14, 21, 22, ...), what is the largest $n$ admitting a regular $k$-uniform intersecting family?
- Are there non-trivial cases beyond $(n,k) \in \{(7,3),(9,4)\}$ where the Delsarte LP bound (Theorem 21, $s=1$) is tight?
- A direct (non-asymptotic) Johnson-scheme proof of Theorem 9 avoiding the Hamming-cube junta detour.

## Key terms
Erdős–Ko–Rado theorem, intersecting family, regular family, symmetric family, Johnson scheme, association scheme, Delsarte LP bound, MacWilliams transform, Hoffman bound, projective plane, Dinur–Friedgut junta, Hilton–Milner, diversity, Bruck–Ryser–Chowla, Frankl, Füredi, Kupavskii, Ihringer
