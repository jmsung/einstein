---
type: source
kind: paper
title: The Chromatic Number of $\mathbb{R}^{n}$ with Multiple Forbidden Distances
authors: Eric Naslund
year: 2022
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2205.12312
source_local: ../raw/2022-naslund-chromatic-number-mathbb-multiple.pdf
topic: general-knowledge
cites:
---

# The Chromatic Number of $\mathbb{R}^{n}$ with Multiple Forbidden Distances

**Authors:** Eric Naslund  ·  **Year:** 2022  ·  **Source:** https://arxiv.org/abs/2205.12312

## One-line
Improves the asymptotic lower bound for the chromatic number of $\mathbb{R}^n$ when multiple distances are forbidden, and extends it to $(k{+}1)$-clique-free colorings via the partition rank method.

## Key claim
For the $m$-distance chromatic number, $\chi(\mathbb{R}^n; m) \ge (\Gamma_\chi \sqrt{m+1} + o(1))^n$ with the explicit constant $\Gamma_\chi = \tfrac{\pi}{2}\max_{x>0} \tfrac{1-e^{-x}}{\sqrt{x}} = 0.79983\ldots$, and more generally $\chi_k(\mathbb{R}^n; m) \ge (\Gamma_\chi \sqrt{(m+1)/k} + o(1))^n$ for $m \ge k \ge 1$.

## Method
Uses the **partition rank** method (a multivariable generalization of slice rank) applied to a tensor $J_k = F_{k+1} \cdot H_{k+1}$, where $F_{k+1}$ is a degree-$2\binom{k+1}{2}(p-1)$ polynomial detecting $(k{+}1)$-tuples with squared distances in $2p A_m$, and $H_{k+1}$ is a "distinctness indicator" zeroing out non-distinct tuples. Applied to the lattice subset $\{0,1,\ldots,l\}^n$ with distance set $A_m = \{1,\sqrt2,\ldots,\sqrt m\}$, this reduces the bound to a maximization over a truncated theta function $\theta(t;l) = \sum_{j=0}^{l} t^{\binom{j}{2}}$. Poisson summation gives a functional equation for $\theta$ that yields the explicit constant $\Gamma_\chi$.

## Result
For $A_m = \{1,\sqrt2,\ldots,\sqrt m\}$, the bound $(\Gamma_\chi\sqrt{m+1}+o(1))^n \le \chi(\mathbb{R}^n,A_m) \le (2(\sqrt m+1)+o(1))^n$ pins down the exponential growth rate up to a constant factor (matches Kupavskii's upper bound to within $2/\Gamma_\chi \approx 2.5$). Recovers Raigorodskii's $1.239566\ldots$ bound at $m=k=1$, improves small-$m$ tables of Gorskaya–Mitricheva–Protasov–Raigorodskii, and disproves their Conjecture 1 by showing the optimal truncation $l$ satisfies $l \le 2m+1$ (and $l < 2m$ asymptotically).

## Why it matters here
Demonstrates the **partition rank / slice rank** machinery applied to a Euclidean clique-avoidance problem with an explicit theta-function variational principle — directly relevant to extremal-graph / forbidden-distance arena problems and to any problem where a polynomial method bound reduces to a one-variable maximization. The connection to even integral lattices and the **double cap conjecture** (Theorem 6) is a template for lattice-theta-function bounds applicable to sphere-packing-adjacent arena problems.

## Open questions / connections
- Can the constant $\Gamma_\chi$ be improved to $C > 1$? A 26% improvement would yield a non-trivial upper bound for the lattice sphere-packing density $\Delta_n$ via Kupavskii's inequality.
- Is there an even integral lattice $\Lambda \subset \mathbb{R}^d$ with $\mu_\Lambda < \mu_{\mathbb{Z}} = 0.883337\ldots$? ($E_8$ and Leech both give $\approx 0.88407$, worse than Raigorodskii's $\sqrt3/2 = 0.866$ for the double cap bound.)
- Can the upper bound $\chi(\mathbb{R}^n; m) \le (c_1 m)^{c_2 n}$ be made polynomial in $m$? Erdős's question of whether $\chi(\mathbb{R}^2; m)$ grows polynomially remains open.

## Key terms
chromatic number of Euclidean space, forbidden distances, partition rank, slice rank, distinctness indicator, Frankl-Wilson, Hadwiger-Nelson, theta function, Poisson summation, Jacobi theta, double cap conjecture, even integral lattice, Raigorodskii, Kupavskii, Naslund, sphere packing density, $k$-clique chromatic number
