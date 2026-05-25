---
type: source
kind: paper
title: Erdős's integer dilation approximation problem and GCD graphs
authors: Dimitris Koukoulopoulos, Youness Lamzouri, Jared Duker Lichtman
year: 2025
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/2502.09539v1
source_local: ../raw/2025-koukoulopoulos-erd-integer-dilation-approximation.pdf
topic: general-knowledge
cites: 
---

# Erdős's integer dilation approximation problem and GCD graphs

**Authors:** Dimitris Koukoulopoulos, Youness Lamzouri, Jared Duker Lichtman  ·  **Year:** 2025  ·  **Source:** http://arxiv.org/abs/2502.09539v1

## One-line
Resolves a 1948 Erdős problem: any discrete set $A \subset \mathbb{R}_{>0}$ with positive upper logarithmic density must contain distinct $\alpha,\beta$ with $|n\alpha-\beta|<\varepsilon$ for some integer $n$.

## Key claim
**Theorem 1.** If $A \subset \mathbb{R}_{>0}$ is discrete with $\limsup_{x\to\infty} \frac{1}{\log x}\sum_{\alpha \in A\cap[1,x]} \frac{1}{\alpha} > 0$, then for every $\varepsilon>0$ there exist distinct $\alpha,\beta \in A$ and $n \in \mathbb{N}$ with $|n\alpha - \beta| < \varepsilon$ — in fact infinitely many such pairs.

## Method
Structure-vs-randomness dichotomy combined with the **second moment method** on shrunk approximation sets $N_\alpha = \bigcup_{n: P^-(n)>\alpha}(n\alpha - 1/2, n\alpha + 1/2)$ (Erdős's rough-number trick from his 1935 proof of $\sum 1/(a\log a)<\infty$ for primitive sets). The crucial pair correlation is controlled by the **bracket** $[\alpha,\beta] = H(\alpha/\beta)/\max(\alpha,\beta)$; when many brackets are small, the configuration is "structured" (rationals $a/q, b/r$ with large $\gcd(a,b)\gcd(q,r)$), forcing the analysis through the **GCD graph machinery** of Koukoulopoulos–Maynard's Duffin–Schaeffer proof, plus a Hauke–Vazquez–Walker variant that only fully determines denominator divisors $Q,R$. Final Euler-factor balance comes from a generalized **Behrend estimate** (1.6) for primitive sets.

## Result
Proves (1.9): $\sum_{\alpha \in A\cap[1,x]} 1/\alpha = o(\log x)$ whenever no $(\alpha,\beta,n)$ solution exists, contradicting positive upper log-density. The proof is "soft" — no quantitative rate analogous to Behrend's $\log x/\sqrt{\log\log x}$ — because Behrend's savings are spent balancing a summation over candidate divisor pairs $(A,B)$. The companion 1968 question of Erdős–Sárközy–Szemerédi (positive *lower* natural density hypothesis) remains open, as does the stronger condition (1.2).

## Why it matters here
General background; no direct arena tie. Could inform autocorrelation / Sidon-set problems where GCD-graph structure-vs-randomness arguments and Behrend-style primitive-set bounds appear, and provides a template for the "extract structured subset, apply known extremal bound" pattern.

## Open questions / connections
- Can the stronger Erdős condition (1.2) ($\sum 1/(\alpha\log\alpha) = \infty$) be handled by the same machinery?
- Can the method yield quantitative bounds (e.g. analog of (1.5) or (1.6)) under the extra assumption $A \subset \{a/q : a \text{ square-free}\}$?
- Extends Haight (1988, irrational-ratio case) and Koukoulopoulos–Maynard / Koukoulopoulos–Maynard–Yang / Hauke–Vazquez–Walker work on Duffin–Schaeffer to a rational-vertex setting.

## Key terms
Erdős integer dilation, Diophantine approximation, primitive sets, Behrend estimate, GCD graphs, Duffin–Schaeffer conjecture, second moment method, structure vs randomness, bracket of real numbers, rough numbers, Koukoulopoulos–Maynard, Haight theorem
