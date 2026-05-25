---
type: source
kind: paper
title: Two extremal problems on intersecting families
authors: Hao Huang
year: 2018
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/1804.11269v1
source_local: ../raw/2018-huang-two-extremal-problems-intersecting.pdf
topic: general-knowledge
cites: 
---

# Two extremal problems on intersecting families

**Authors:** Hao Huang  ·  **Year:** 2018  ·  **Source:** http://arxiv.org/abs/1804.11269v1

## One-line
Settles (partially) two extremal-set-theory problems on intersecting and cross-intersecting $k$-uniform families: a Kupavskii bound on disjoint cross-intersecting pairs, and a disproof of Frankl's diversity conjecture just above $n=3k$.

## Key claim
(1) For $n \ge 2k^2$, any two disjoint cross-intersecting $\mathcal{A},\mathcal{B} \subset \binom{[n]}{k}$ satisfy $\min\{|\mathcal{A}|,|\mathcal{B}|\} \le \tfrac12 \binom{n-1}{k-1}$, and the quadratic range is tight up to a constant. (2) A Kneser-spectral bound $\min\{|\mathcal{A}|,|\mathcal{B}|\} \le \tfrac12 \binom{n-1}{k-1}\cdot \tfrac{n-2}{n-k-1}$ valid for all $n \ge 2k$. (3) For $3k < n < (2+\sqrt 3)k$ and $k$ large, there exists an intersecting $\mathcal{F} \subset \binom{[n]}{k}$ with $\mathrm{div}(\mathcal{F}) > \binom{n-3}{k-2}$, disproving Frankl's $n>3k$ diversity conjecture and Kupavskii's stronger Conjecture.

## Method
Three techniques: (a) Frankl's $(i,j)$-shifting combined with induction on $(n,k,l)$ to reduce cross-intersecting pairs to families supported on $[k+l]$; (b) Kneser-graph spectral method — expand characteristic vectors $\mathbf 1_\mathcal{A},\mathbf 1_\mathcal{B}$ in the eigenbasis of $KG(n,k)$ (eigenvalues $(-1)^{i+1}\binom{n-k-i}{k-i}$), then combine the disjointness equation $\langle \mathbf 1_\mathcal{A},\mathbf 1_\mathcal{B}\rangle=0$ with the cross-intersecting equation $\langle \mathbf 1_\mathcal{A}, M\mathbf 1_\mathcal{B}\rangle=0$ via triangle inequality on non-principal eigencomponents; (c) explicit construction using a non-uniform intersecting "trace" $\mathcal{H} \subset 2^{[6]}$ (10 triples covering each pair exactly twice — a $2$-$(6,3,2)$-like design) lifted to $\binom{[n]}{k}$, with asymptotic counting via the limit lemma $\binom{n-t}{k-i}/\binom{n}{k} \to \alpha^i(1-\alpha)^{t-i}$ for $k=\alpha n$.

## Result
Theorem 1.1: $\min\{|\mathcal{A}|,|\mathcal{B}|\} \le \tfrac12\binom{n-1}{k-1}$ for $n \ge 2k^2$. Theorem 1.3: $\min\{|\mathcal{A}|,|\mathcal{B}|\} \le \tfrac12\binom{n-1}{k-1}\cdot \tfrac{n-2}{n-k-1}$ for $n \ge 2k$, sharp at $n=2k$ (gives $\binom{2k-1}{k-1}/2$). Theorem 2.2: for $\alpha \in (2-\sqrt 3,\, 1)$, the lifted family from a specific 10-set design on $[6]$ has every "popular-element" coverage $|\mathcal F\setminus \mathcal F_x|$ asymptotically exceeding $\binom{n-3}{k-2}$, proving $\mathrm{div}(\mathcal F) > \binom{n-3}{k-2}$ for $3k<n<(2+\sqrt 3)k$. Two new conjectures (2.3, 2.4) propose the non-uniform extremal family at $n=2k+1$ and $n=2k$, verified by computer up to $n\le 6$.

## Why it matters here
General background for discrete-combinatorics/extremal-set-theory problems on Einstein Arena; specifically relevant whenever a problem reduces to cross-intersecting bounds, EKR-type extremal families, or Kneser-graph spectral methods — the Kneser eigenvalue trick in Theorem 1.3 is a transferable LP-bound-style technique (spectral two-equation system + triangle inequality) for intersecting-family problems.

## Open questions / connections
- Sharp value of $\min\{|\mathcal A|,|\mathcal B|\}$ for intermediate ranges $2k+1 \le n \le 2k^2$ — Theorem 1.3 is not sharp at $n=2k+1$.
- True threshold for Frankl's diversity conjecture: not $3k$; presumably near $(2+\sqrt 3)k \approx 3.732 k$, but exact value open.
- Non-uniform diversity extremal problem (Conjectures 2.3, 2.4) — open for $n>6$; connects to Brace-Daykin regular intersecting families and Ihringer-Kupavskii (powers-of-2 obstruction).
- Extends Pyber (1986) and Matsumoto-Tokushige (1989) cross-intersecting bounds by adding the disjointness constraint.

## Key terms
Erdős-Ko-Rado theorem, cross-intersecting families, disjoint families, diversity of intersecting families, Hilton-Milner theorem, Frankl shifting technique, Kneser graph spectrum, Kneser eigenvalues, Frankl diversity conjecture, Kupavskii conjecture, Lemons-Palmer, $(2-\sqrt 3)$ threshold
