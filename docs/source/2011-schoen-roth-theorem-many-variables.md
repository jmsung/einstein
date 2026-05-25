---
type: source
kind: paper
title: Roth’s theorem in many variables
authors: T. Schoen, I. Shkredov
year: 2011
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1106.1601
source_local: ../raw/2011-schoen-roth-theorem-many-variables.pdf
topic: general-knowledge
cites:
---

# Roth's theorem in many variables

**Authors:** T. Schoen, I. Shkredov  ·  **Year:** 2011  ·  **Source:** https://arxiv.org/abs/1106.1601

## One-line
Establishes a near-Behrend upper bound for subsets of $\{1,\dots,N\}$ avoiding nontrivial solutions to any translation-invariant linear equation in $\geq 6$ variables.

## Key claim
If $A \subseteq \{1,\dots,N\}$ has no solution with distinct integers to $a_1 x_1 + \cdots + a_k x_k = 0$ ($\sum a_i = 0$, $k \geq 6$), then $|A| \ll N \exp(-c(\log N / \log\log N)^{1/6})$ — qualitatively close to Behrend's lower bound $N \exp(-C\sqrt{\log N})$.

## Method
Density-increment iteration on Bohr sets, but the increment is extracted *not* from a large Fourier coefficient — instead from finding a translate of a large Bohr set inside $a_1 \cdot A + a_2 \cdot A + a_3 \cdot A + a_4 \cdot A$. This containment is delivered by a local variant of Sanders' Bogolyubov–Ruzsa lemma (built on Croot–Sisask almost-periods and a local Chang spectral lemma), which keeps the Bohr-dimension growth at $O(\log^4(1/\alpha))$ per step — the key efficiency that yields the $1/6$ exponent.

## Result
For $k \geq 6$: $|A| \ll \exp(-c(\log N/\log\log N)^{1/6}) \cdot N$. Corollary for $x_1+x_2+x_3+x_4+x_5=5y$: same bound. Finite-field analogue ($\mathbb{F}_p^n$, $k \geq 6$): $|A| \ll_k p^n \exp(-c_p (k^3 \log p^n)^{1/5})$. Conditional on Polynomial Freiman–Ruzsa (Conjecture 7.2): $R(N) \ll N^{1-c}$ for invariant equations with $a_1=-a_2$, $a_3=-a_4$.

## Why it matters here
General background; no direct arena tie. The "find a big structured set inside a sumset, then increment" template is methodologically interesting for any extremal-combinatorics problem where Fourier-based increments stall — relevant lens for sieve-theory and Sidon/$B_h$-set problems if they ever appear, but not load-bearing for current 23 arena problems.

## Open questions / connections
- Sharp exponent: gap between $\exp(-c(\log N/\log\log N)^{1/6})$ upper and $\exp(-C\sqrt{\log N})$ Behrend lower remains; what's the truth?
- Does the technique extend to $k=3,4,5$ (notably $x+y=2z$, three-term APs)? The argument genuinely needs $k\geq 6$ to absorb four variables into the sumset.
- Polynomial Freiman–Ruzsa Conjecture (Conjecture 7.2 here) would upgrade the bound to $N^{1-c}$ — links this to the broader PFR program (since resolved by Gowers–Green–Manners–Tao in $\mathbb{F}_2^n$, 2023).

## Key terms
Roth's theorem, Behrend construction, invariant linear equation, Bohr set, density increment, Bogolyubov–Ruzsa lemma, Polynomial Freiman–Ruzsa conjecture, Sanders, Croot–Sisask, Chang's lemma, sumset structure, arithmetic progressions
