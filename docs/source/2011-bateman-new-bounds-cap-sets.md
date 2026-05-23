---
type: source
kind: paper
title: New Bounds on cap sets
authors: M. Bateman, N. Katz
year: 2011
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1101.5851
source_local: ../raw/2011-bateman-new-bounds-cap-sets.pdf
topic: general-knowledge
cites:
---

# New Bounds on cap sets

**Authors:** M. Bateman, N. Katz  ·  **Year:** 2011  ·  **Source:** https://arxiv.org/abs/1101.5851

## One-line
First improvement over Meshulam's $O(3^N/N)$ bound on cap sets in $\mathbb{F}_3^N$, achieving $|A| \leq C \cdot 3^N / N^{1+\epsilon}$ for some universal $\epsilon > 0$.

## Key claim
There exist universal constants $\epsilon > 0$ and $C < \infty$ such that any cap set $A \subseteq \mathbb{F}_3^N$ (no three points summing to zero) satisfies $|A|/3^N \leq C/N^{1+\epsilon}$. The $\epsilon$ is small and unoptimized.

## Method
Fourier-analytic density-increment argument with deep additive-combinatorial structural analysis of the large spectrum $\Delta = \{x \neq 0 : |\hat{A}(x)| \gtrsim \rho^2\}$. Establishes $\Delta$ has $\sim N^3$ elements and $\sim N^7$ additive quadruples but cannot be "additively smoothing" (via a probabilistic/random-selection argument), forcing $\Delta$ to look like a sum $K + \Lambda$ of a structured set $K$ (almost additively closed, size $\sim N$) and a quasi-random set $\Lambda$ (size $\sim N^2$). Freiman's theorem places $K$ in a low-dimensional subspace $H$; fiber analysis of $A$ over $H^\perp$ then contradicts the no-strong-increment hypothesis.

## Result
Theorem 1.1: cap-set density $\leq C/N^{1+\epsilon}$. Theorem 1.4 (the engine): same bound holds for cap sets with no strong increments (subspace $V$ of codim $d \leq N/2$ with $|A \cap V|/|V| \geq \rho + 20d\rho/N$). Induction on $N$ converts Theorem 1.4 into Theorem 1.1. Theorem 7.1 (structural): spectrum decomposes as $\bigsqcup_{\lambda \in \Lambda} (\lambda + H_\lambda)$ with $|\Lambda| \gtrsim N^{2-f(\epsilon)}$, $|H_\lambda| \gtrsim N^{1-f(\epsilon)}$, $\dim H \lesssim N^{f(\epsilon)}$.

## Why it matters here
General background for extremal combinatorics / additive-combinatorics problems on Einstein Arena (cap-set-style, Sidon-set, sieve, autocorrelation); the spectrum-structure technique and the additive-smoothing dichotomy are reusable framings. No direct arena problem maps to cap-set bounds, but the methodology (Fourier + Balog-Szemerédi-Gowers + Freiman, density-increment iteration) recurs across sphere-packing LP arguments and Sidon-set extremal questions.

## Open questions / connections
- Conjecture 9.1: if $B, C \subset \mathbb{F}_3^N$ have $\geq |B||C|^2 N^{-\sigma}$ additive quadruples $b_1+c_1=b_2+c_2$, then $C$ lies in a subspace of dim $N^{O(\sigma)}$ (would replace asymmetric BSG iteration, improving $\epsilon$).
- Conjecture 9.2: any $N^\sigma$-additively-non-smoothing $\Delta$ admits additive structure with $N^{O(\sigma)}$ comity (would de-iterate the core argument).
- Polymath 6 ([PM6]) aims to transfer these ideas to integer Roth bounds; relates to Sanders' $C(\log\log M)^5/\log M$ Roth bound [S11].
- Extends Katz-Koester [KK10] additive-doubling/energy techniques; uses Sanders [S10] fiber-analysis idea; relies on Tao-Vu [TV06] form of asymmetric BSG.

## Key terms
cap set, Meshulam bound, $\mathbb{F}_3^N$, large spectrum, additive quadruples, additive octuples, additive smoothing, Balog-Szemerédi-Gowers, Freiman's theorem, density increment, Fourier analysis, Roth theorem, arithmetic progressions, Sanders, Katz, Bateman, Gowers, additive energy
