---
type: source
kind: paper
title: The Kakeya Set conjecture over Z/NZ for general N
authors: Manik Dhar
year: 2021
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2110.14889
source_local: ../raw/2021-dhar-kakeya-set-conjecture-general.pdf
topic: general-knowledge
cites:
---

# The Kakeya Set conjecture over Z/NZ for general N

**Authors:** Manik Dhar  ·  **Year:** 2021  ·  **Source:** https://arxiv.org/abs/2110.14889

## One-line
Resolves the Kakeya set conjecture over $\mathbb{Z}/N\mathbb{Z}$ for arbitrary $N$ by combining a polynomial method on roots of unity with an inductive Chinese-remainder argument across prime power factors.

## Key claim
Every Kakeya set $S \subseteq (\mathbb{Z}/N\mathbb{Z})^n$ with $N = p_1^{k_1}\cdots p_r^{k_r}$ satisfies $|S| \geq N^n \prod_{i=1}^{r} (2(k_i + \lceil \log_{p_i}(n) \rceil))^{-n}$, which implies $|S| \geq C_{n,\varepsilon} N^{n-\varepsilon}$ for all $\varepsilon > 0$ (Hickman–Wright conjecture).

## Method
Polynomial method lifted to the complex torus: embed $(\mathbb{Z}/p^k\mathbb{Z})^n$ via $p^k$-th roots of unity and work with matrices over $\mathbb{Z}(\zeta)[z]/\langle z^{p^\ell} - 1\rangle$. A "Vandermonde" matrix $M_{p^\ell,n}$ encoding $z^{\langle u,v\rangle}$ is decoded from monomial evaluations on $m$-rich lines using Hasse derivatives and multiplicities; the mod-$p$ quotient map $\psi_{p^k}$ transfers rank bounds to $\mathbb{F}_p$. For composite $N$, an inductive Kronecker-product argument across prime power factors combines per-factor decoders.

## Result
For $(m,\varepsilon)$-Kakeya sets over $\mathbb{Z}/p^k\mathbb{Z}$: $|S| \geq \varepsilon \cdot m^n / (2(k + \lceil\log_p n\rceil))^n$; sharper $|S| \geq \varepsilon \cdot m^n (k+1)^{-n}(1+n/p)^{-n}$ when $p > n$. Recovers Saraf–Sudan–Kopparty–Dvir bound as $p \to \infty$. A matching construction shows the bound is near-sharp: explicit Kakeya sets of size $\leq p^{kn} k^{-n+1}(1-1/p)^{-n}$ in $(\mathbb{Z}/p^k\mathbb{Z})^n$ for $k = (p^{s+1}-1)/(p-1)$.

## Why it matters here
General background; no direct arena tie — Einstein Arena problems concern Euclidean sphere packing, autocorrelation, discrete geometry rather than Kakeya over rings. Could inform agent reasoning about polynomial-method bounds, rank arguments, and Chinese-remainder decompositions in extremal combinatorics, but no current arena problem directly invokes Kakeya machinery.

## Open questions / connections
- Resolves Minkowski-dimension Kakeya conjecture over $p$-adic integers $\mathbb{Z}_p$ and power series ring $\mathbb{F}_q[[x]]$ via Ellenberg–Oberlin–Tao reduction.
- Naive techniques here don't extend to $(m,\varepsilon)$-Kakeya bounds over general $\mathbb{Z}/N\mathbb{Z}$ — resolved in follow-up Dhar (2022, arXiv:2209.11443) using probabilistic arguments.
- Extends Dvir (2009) finite-field polynomial method and Dhar–Dvir (2021) square-free case; refines Arsovski (2021) prime-power case using multiplicities without $p$-adic analysis.

## Key terms
Kakeya set conjecture, polynomial method, Z/NZ, prime power ring, Chinese remainder theorem, Hasse derivatives, method of multiplicities, Vandermonde matrix, roots of unity, p-adic Kakeya, Dvir, Arsovski, Hickman-Wright, Saraf-Sudan, Kronecker product rank
