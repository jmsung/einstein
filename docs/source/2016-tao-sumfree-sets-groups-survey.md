---
type: source
kind: paper
title: "Sumfree sets in groups: a survey"
authors: T. Tao, V. Vu
year: 2016
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1603.03071
source_local: ../raw/2016-tao-sumfree-sets-groups-survey.pdf
topic: general-knowledge
cites:
---

# Sumfree sets in groups: a survey

**Authors:** T. Tao, V. Vu  ·  **Year:** 2016  ·  **Source:** https://arxiv.org/abs/1603.03071

## One-line
Survey + new results on sum-free and sum-avoiding subsets in abelian groups, including a structural characterization of sets $A$ with $\varphi(A) \le k$ and a resolution of Erdős's zero-sum question.

## Key claim
If $A \subset G$ has $\varphi(A) \le k$ (no $k+1$-element sum-avoiding subset), then $A$ is covered, up to a bounded residual $C(k)$, by at most $k$ finite subgroups $H_1, \dots, H_m$ each meeting $A$ in density $\ge 1/C(k)$. Erdős's zero-sum conjecture for $k \ge 4$ is false in general (Mersenne-prime counterexamples) but true when $|G|$ has no small prime factors.

## Method
Standard additive-combinatorics inverse machinery (Balog–Szemerédi, Freiman's theorem in arbitrary abelian groups, Green–Ruzsa) to extract approximate coset progressions $H + P$ from high-additive-energy subsets, then iterate: peel off subgroups $H_1, \dots, H_m$ one at a time, enlarging "incorrect" $H$ to absorb torsion cosets (e.g. $H' = H + \{0, x\}$ when $2x \in H$). Argument is formulated in nonstandard analysis to manage the hierarchy of scales — yielding existential but Ackermann-or-worse $C(k)$.

## Result
**Theorem 3.1:** $\varphi(A) \le k \Rightarrow$ exists $\le k$ finite subgroups covering $A$ up to $C(k)$ residual elements, each with $|A \cap H_i| \ge |H_i|/C(k)$. **Theorem 4.5:** if $|G|$ has no prime factor $< C_0(k, \varepsilon)$, density tightens to $(1-\varepsilon)|H_i|$, forcing a zero-sum pair (Cor. 4.6). **Prop. 4.2:** in $\mathbb{Z}/2^n\mathbb{Z}$, $A = \{(4m+1)2^j\}$ has $\varphi(A) = 4$, $|A| = 2^{n-1}-1$, no $a_1 + a_2 = 0$. **Prop. 4.3:** $A = \{1,2,4\} \times H \subset \mathbb{Z}/7\mathbb{Z} \times H$ gives $k=4$ counterexample; generalizes to any Mersenne prime $2^k - 1$.

## Why it matters here
General background; no direct arena tie. Closest hooks: sum-free / Sidon-set techniques relevant to autocorrelation-style problems, and Freiman/Balog–Szemerédi as templates for inverse structure theorems that might inform discrete-combinatorics problems where "small doubling implies coset structure" reasoning could apply.

## Open questions / connections
- Order of magnitude of $\varphi(n)$ over the integers: gap between $(\log^{(2)} n)^{1/2-o(1)}$ (Shao) lower bound and $\exp(O(\sqrt{\log n}))$ (Ruzsa) upper bound remains huge.
- Whether $f(n) - n/3 \to \infty$ (Bourgain $n+2)/3$ lower vs Eberhard–Green–Manners $(1/3 + o(1))n$ upper) — sharpening the real-case Erdős sum-free bound.
- Classify exactly which finite groups admit a positive Erdős zero-sum answer; Mersenne-prime counterexamples force $C(k) \ge$ exponential in $k$.

## Key terms
sum-free set, sum-avoiding set, Erdős zero-sum conjecture, Freiman's theorem, Balog-Szemerédi theorem, coset progression, abelian group, Mersenne prime, Bourgain, Green-Ruzsa, Sudakov-Szemerédi-Vu, nonstandard analysis, inverse theorem, additive combinatorics
