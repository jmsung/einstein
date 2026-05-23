---
type: source
kind: paper
title: Constructive Discrepancy Minimization by Walking on the Edges
authors: Shachar Lovett, Raghu Meka
year: 2012
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1203.5747
source_local: ../raw/2012-lovett-constructive-discrepancy-minimization-walking.pdf
topic: general-knowledge
cites:
---

# Constructive Discrepancy Minimization by Walking on the Edges

**Authors:** Shachar Lovett, Raghu Meka  ·  **Year:** 2012  ·  **Source:** https://arxiv.org/abs/1203.5747

## One-line
A simple constrained-Brownian-motion algorithm ("Edge-Walk") gives the first elementary constructive proof of Spencer's "six standard deviations suffice" theorem for set-system discrepancy.

## Key claim
For any set system $(V,\mathcal{S})$ with $|V|=n$, $|\mathcal{S}|=m\geq n$, a randomized $\tilde{O}((n+m)^3)$ algorithm produces a coloring $\chi:V\to\{-1,1\}$ with $\chi(S) < K\sqrt{n\log(m/n)}$ (with $K=13$ when $m=n$), matching Spencer's non-constructive bound across all $m,n$ (sharper than Bansal's SDP bound by a $\sqrt{\log(m/n)}$ factor).

## Method
Edge-Walk: starting at $x_0\in[-1,1]^n$, take small Gaussian steps $X_t = X_{t-1}+\gamma U_t$ where $U_t\sim\mathcal{N}(V_t)$ is sampled in the linear subspace orthogonal to all "nearly-hit" variable constraints ($|x_i|\geq 1-\delta$) and discrepancy constraints ($|\langle x-x_0,v_j\rangle|\geq c_j-\delta$). A win-win martingale argument (Gaussian tail bound + $\ell_2$-norm potential via $\mathbb{E}\|X_T\|^2\leq n$ vs. $\gamma^2\sum\mathbb{E}[\dim V_t]$) shows $\geq n/2$ variable constraints get hit, yielding a partial coloring; recursion on unfixed coordinates gives the full coloring.

## Result
Main partial coloring lemma (Theorem 4): given vectors $v_1,\dots,v_m$ with $\sum_j \exp(-c_j^2/16)\leq n/16$, the walk finds $x\in[-1,1]^n$ with $|\langle x-x_0,v_j\rangle|\leq c_j\|v_j\|_2$ and $|x_i|\geq 1-\delta$ on at least $n/2$ coordinates, in time $O((n+m)^3\delta^{-2}\log(nm/\delta))$. Also yields constructive Srinivasan-type bound $O(\sqrt{t}\log n)$ in the Beck–Fiala bounded-degree setting (Theorem 3).

## Why it matters here
General background; no direct arena tie. Closest relevance is methodological — constrained-random-walk / Brownian-motion-in-polytope is a constructive optimization primitive that could inform combinatorial-feasibility problems (extremal graph, Sidon-set, autocorrelation) where partial-coloring style "fix half the variables, recurse" arguments apply.

## Open questions / connections
- Beck–Fiala conjecture $\mathrm{disc}(\mathcal{S})=O(\sqrt{t})$ remains open; this work matches only the $O(\sqrt{t}\log n)$ constructive bound, not Banaszczyk's non-constructive $O(\sqrt{t\log n})$.
- Can Edge-Walk be derandomized? Can it be extended to give true $\{-1,0,1\}$ partial colorings (not just fractional $[-1,1]$)?
- Extends Beck's entropy method constructively and is strictly stronger in some regimes (tolerates $\Omega(n)$ sets with discrepancy $1/n$ vs. entropy method's $O(n/\log n)$).

## Key terms
discrepancy minimization, Spencer six standard deviations, Edge-Walk, constrained Brownian motion, partial coloring lemma, Beck entropy method, Beck-Fiala conjecture, Bansal SDP, martingale tail bound, Gaussian random walk, Banaszczyk, Srinivasan, set-system coloring, constructive algorithm
