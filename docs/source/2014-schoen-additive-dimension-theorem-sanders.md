---
type: source
kind: paper
title: ADDITIVE DIMENSION AND A THEOREM OF SANDERS
authors: T. Schoen, I. Shkredov
year: 2014
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1404.2044
source_local: ../raw/2014-schoen-additive-dimension-theorem-sanders.pdf
topic: general-knowledge
cites:
---

# ADDITIVE DIMENSION AND A THEOREM OF SANDERS

**Authors:** T. Schoen, I. Shkredov  ·  **Year:** 2014  ·  **Source:** https://arxiv.org/abs/1404.2044

## One-line
Sharper bounds on the additive dimension (maximal dissociated subset size) of sets in abelian groups that have small sumset, large additive energy, or large higher-moment energy.

## Key claim
For $A \subseteq G$ with $|A+A| \le K|A|$: $\dim(A) \ll \log|A| + K(\log K)^8 \log\log|A|$ (refining Sanders' $\dim(A) \ll K\log|A|$ for moderate $K$); and if $E(A) = |A|^3/K$ there is $B \subseteq A$ with $|B| \gg |A|/K^{25/8}$ and $\dim(B) \ll K^{7/8}\log|A|$ (improving Theorem 2's $K\log|A|$ to $K^{1-\gamma}\log|A|$).

## Method
Combines Rudin's inequality (all $L^p$ norms equivalent on dissociated sets) with Sanders' Bogolyubov–Ruzsa lemma to extract proper coset progressions $P \subseteq 2A - 2A$ of dimension $O(\log^6 K)$, Plünnecke–Ruzsa for $|kA|$ control, and Chang's covering lemma. For energy regimes, uses higher-energy decompositions $E_k$, $T_k$ via Fourier $\sum |\hat A(\xi)|^{2k}$ and a Croot–Sisask-based extraction of large subsets $X$ with $kX \subseteq 2A - 2A$.

## Result
Five main bounds: (i) Theorem 13 refined sumset bound above; (ii) Theorem 19 — if $E(A,B) = |A||B|^2/K$ then $\exists B^* \subseteq B$ with $\dim(B^*) \ll K(\log K)^{2+\varepsilon}(|B^*|/|B|)^2 \log|A|$; (iii) Theorem 20 above ($K^{7/8}$ exponent); (iv) Theorem 23 — if $E_{3/2}(A) = |A|^{5/2}/K^{1/2}$ then $\exists B$ with $|B| \gg |A|/K^2$, $\dim(B) \ll K^{3/4}\log|A|$; (v) Application (Theorem 25): for $A \subseteq \mathbb{F}_p$ with $|A| \ge e^{c\sqrt{\log p}}$, $\exists x$ with $0 < (A*A)(x) \ll e^{-O(\log^{1/4}|A|)} |A|$, resolving a Konyagin question.

## Why it matters here
General background; no direct arena tie. Additive combinatorics tooling (dissociated sets, sumset/energy dichotomies, coset progressions) is adjacent to Sidon-set and sum-free-set problems but the arena's 23 problems don't currently include a Freiman-type structural problem.

## Open questions / connections
- Gap to Polynomial Freiman–Ruzsa Conjecture: PFRC would give $\dim(A) \ll K^{o(1)} \log|A|$; current bounds $K^c \log|A|$ with $c > 0$.
- Sharpness of $|A^*| \gg c^{1/(2s-1)}|A|$ in Proposition 21 (matched by $H \cup \Lambda$ construction).
- Bateman–Katz cap-set machinery generalized to arbitrary abelian groups (Corollary 31) — extends [1,2] beyond $\mathbb{F}_p^n$.
- Multiple distinct dimension notions $\dim(A), d(A), d_*(A), \tilde d(A)$ with non-trivial inequalities still under exploration.

## Key terms
additive dimension, dissociated set, Sanders theorem, Freiman–Ruzsa, Plünnecke–Ruzsa, Chang covering lemma, Rudin inequality, additive energy, higher energy $E_k$, $T_k$, Bogolyubov lemma, coset progression, sumset, Croot–Sisask, Bateman–Katz, Konyagin convolution problem, abelian group, $\mathbb{F}_p$, cap set
