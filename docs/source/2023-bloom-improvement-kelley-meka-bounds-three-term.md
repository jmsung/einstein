---
type: source
kind: paper
title: An improvement to the Kelley-Meka bounds on three-term arithmetic progressions
authors: Thomas F. Bloom, Olof Sisask
year: 2023
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2309.02353
source_local: ../raw/2023-bloom-improvement-kelley-meka-bounds-three-term.pdf
topic: general-knowledge
cites:
---

# An improvement to the Kelley-Meka bounds on three-term arithmetic progressions

**Authors:** Thomas F. Bloom, Olof Sisask  ·  **Year:** 2023  ·  **Source:** https://arxiv.org/abs/2309.02353

## One-line
A small modification to the Kelley–Meka almost-periodicity bootstrapping improves the upper bound on 3-AP-free subsets of $\{1,\dots,N\}$ from $\exp(-c(\log N)^{1/12})N$ to $\exp(-c(\log N)^{1/9})N$.

## Key claim
If $A \subseteq \{1,\dots,N\}$ has no non-trivial 3-term arithmetic progressions, then $|A| \le \exp(-c(\log N)^{1/9})N$ for some $c>0$ (Theorem 1); parallel improvements give $|A| \ll q^{n - cn^{1/7}}$ in $\mathbb{F}_q^n$ (Theorem 2), and an $O(L(\alpha)^5 L(\gamma)^2)$-codimension subspace on which $A+A$ has density $\ge 1-\gamma$ (Theorem 3).

## Method
Refines the Kelley–Meka argument at the almost-periodicity → Bohr-set bootstrapping step. Where Kelley–Meka use the trivial bound $\sum_\gamma |\widehat{\mu_{A_1}}(\gamma)|\,|\widehat{1_S}(\gamma)| \le \alpha_1^{-1/2}$ via Cauchy–Schwarz and Parseval, Bloom–Sisask replace $1_S$ by $\mu_A \circ \mu_A$ (using that the latter is pointwise large on the structured set $S$), yielding $\sum_\gamma |\widehat{\mu_{A_1}}(\gamma)|\,|\widehat{\mu_A}(\gamma)|^2 \le \alpha^{-1}$. Since $L(\alpha_1) \approx L(\alpha)^2$ in the Kelley–Meka iteration, this saves a logarithm. Chang's lemma + iterated density-increment then propagates the saving.

## Result
Theorem 1: $1/9$ exponent for integer 3-AP-free sets (vs. Kelley–Meka's $1/12$, Behrend lower bound $1/2$). Theorem 2: $1/7$ exponent in $\mathbb{F}_q^n$ (vs. $1/9$). Theorem 3: $A+A$ on affine subspace of codimension $O(L(\alpha)^5 L(\gamma)^2)$ (vs. Sanders $O(L(\alpha)^4 \gamma^{-2})$ and Kelley–Meka $O(L(\alpha)^5 L(\gamma)^4)$). Theorem 4: $A+A+A$ contains an AP of length $\exp(-O(L(\alpha)^2)) N^{\Omega(1/L(\alpha)^7)}$ (vs. prior $1/L(\alpha)^9$). Remarks indicate a more elaborate optimization yields $5/41$ but is omitted.

## Why it matters here
General background; no direct arena tie. The Kelley–Meka machinery (almost-periodicity, Bohr sets, density increment, Chang's lemma) is a template for extremal problems with progression/sumset structure — potentially relevant if any arena problem touches 3-AP-free sets, Roth-type extremal density, or sumset structure in $\mathbb{F}_q^n$.

## Open questions / connections
- Tighter bootstrapping via $\langle \mu_{A_1} \circ \mu_{A_1}, \mu_A \circ \mu_A \rangle$ — if small, get $k \approx \log L(\alpha)$; if large, feed back as additional density increment.
- Behrend lower bound is still $\exp(-c(\log N)^{1/2})$ — exponent gap $1/9$ vs $1/2$ remains the central open problem.
- Hunter–Pohoata applied Theorem 3 in $\mathbb{F}_2^n$ to improve Ramsey bounds for monochromatic subspaces — shows the machinery transfers across additive-combinatorial problems.

## Key terms
three-term arithmetic progression, Roth's theorem, Kelley-Meka, Behrend, almost-periodicity, Bohr set, Chang's lemma, density increment, bootstrapping, Fourier analytic, additive combinatorics, sumset, Bloom, Sisask
