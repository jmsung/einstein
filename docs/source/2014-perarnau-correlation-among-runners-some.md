---
type: source
kind: paper
title: Correlation Among Runners and Some Results on the Lonely Runner Conjecture
authors: G. Perarnau, O. Serra
year: 2014
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1407.3381
source_local: ../raw/2014-perarnau-correlation-among-runners-some.pdf
topic: general-knowledge
cites:
---

# Correlation Among Runners and Some Results on the Lonely Runner Conjecture

**Authors:** G. Perarnau, O. Serra  ·  **Year:** 2014  ·  **Source:** https://arxiv.org/abs/1407.3381

## One-line
Improves the best general gap-of-loneliness bound for the Lonely Runner Conjecture by exploiting pairwise correlations between runners' close-to-origin events.

## Key claim
For sufficiently large $n$ and every set of nonzero speeds $v_1,\dots,v_n$, there exists $t\in(0,1)$ with $\|tv_i\|\geq 1/(2n-2+o(1))$ for all $i$ — beating Chen's $1/(2n-1+2n^{-3})$.

## Method
Compute exact pairwise join probabilities $\Pr(A_i\cap A_j)$ for the "$i$-th runner is $\delta$-close to origin" events, via a piecewise-linear function $f(x,y)=\min(x,y)+\max(x+y-1,0)-2xy$ in terms of fractional parts $\varepsilon_{ij}=\{v_i\delta/\gcd(v_i,v_j)\}$. Apply Hunter's Bonferroni-type tree inequality $\Pr(\cup A_i)\leq \sum\Pr(A_i)-\sum_{ij\in T}\Pr(A_i\cap A_j)$ over a spanning tree built from $\varepsilon$-good pairs (ratios either close to 1 or $\geq(\gamma\delta)^{-1}$), found via Lemma 12 (pigeonhole on log-ratios) and an Erdős–Stone independent-set bound. Section 3 introduces dynamic circular interval graphs $G(t)$ where each runner owns an arc of length $1/n$.

## Result
- **Theorem 3:** gap $1/(2n-2+o(1))$ for general speeds (modest improvement over Chen $1/(2n-1+2n^{-3})$).
- **Theorem 4:** if $\sum_{i=2}^n 1/v_i$ diverges, gap $\geq 1/(2(n-\sum 1/v_i))$ — strong when speeds grow slowly.
- **Proposition 2:** $E(X^2)\geq 2\delta n(\delta(1+\Omega(1/\log\delta^{-1}))n+1)$.
- **Theorem 6:** at some $t$, either a runner is alone OR four runners are simultaneously almost-alone (extends Czerwiński–Grytczuk invisible-runner).
- **Proposition 22:** clean reproof of Chen–Cusick $1/(2n-3)$ bound when $2n-3$ is prime, via $p$-adic digit manipulation in $\mathbb{Z}_N$.

## Why it matters here
Direct relevance to Einstein Arena autocorrelation / Sidon / extremal-combinatorics problems where loneliness-style fractional-part gap bounds appear; the pairwise-correlation + Hunter-tree technique is a transferable lemma for "union bound is loose, exploit pairwise structure" situations. Adds a concrete numerical SOTA ($1/(2n-2+o(1))$) for the Lonely Runner Conjecture and the $f(x,y)$ exact formula for pairwise close-to-origin events.

## Open questions / connections
- Conjecture 21: $E(X^2)\geq(1+o(1))4\delta^2n^2+2\delta n$ — tight second-moment bound; Cilleruelo showed extremal sequence $v_i=i$ achieves $(12/\pi^2)\delta n\log n$ at $\delta=\Theta(1/n)$, leaving a $\log n$ gap.
- $k$-wise join probability conjecture: $\Pr(\cap_{i\in S}A_i)\geq c_k\delta^k$ with $c_k=(1+o_k(1))2^k$ — would tighten higher-order Bonferroni.
- Weak Lonely Runner (Spencer, Conjecture 16): some runner $j$ sees all others at distance $\geq 1/n$ — still open; dynamic interval graph $G(t)$ is a new attack surface.
- Extends/refines: Chen 1994 ($1/(2n-1+2n^{-3})$), Chen–Cusick 1999 (prime case), Czerwiński–Grytczuk invisible runner, Dubickas (fast-growing speeds via Peres–Schlag lacunary).

## Key terms
Lonely Runner Conjecture, gap of loneliness, Hunter inequality, Bonferroni-type inequality, pairwise correlation, fractional part, Erdős–Stone theorem, dynamic interval graph, invisible runner, Lovász Local Lemma, Chen bound, view-obstruction problem, lacunary sequences, $p$-adic expansion, almost-alone runner
