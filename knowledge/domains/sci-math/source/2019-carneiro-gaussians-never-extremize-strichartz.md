---
type: source
kind: paper
title: Gaussians never extremize Strichartz inequalities for hyperbolic paraboloids
authors: E. Carneiro, Lucas Oliveira, Mateus Sousa
year: 2019
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1911.11796
source_local: ../raw/2019-carneiro-gaussians-never-extremize-strichartz.pdf
topic: general-knowledge
cites:
---

# Gaussians never extremize Strichartz inequalities for hyperbolic paraboloids

**Authors:** E. Carneiro, Lucas Oliveira, Mateus Sousa  ·  **Year:** 2019  ·  **Source:** https://arxiv.org/abs/1911.11796

## One-line
Proves that Gaussian functions are not even critical points of the $L^p(\mathbb{R}^d) \to L^q(\mathbb{R}^{d+1})$ Fourier extension inequality on any hyperbolic paraboloid (mixed-signature quadratic form), for $1 < p < 2(d+1)/d$, $p \neq 2$.

## Key claim
**Theorem 1:** Let $S \subset \mathbb{R}^{d+1}$ be the hyperbolic paraboloid $\tau = Q(\xi) = \sum_j \sigma_j \xi_j^2$ with signs $\sigma_j \in \{\pm 1\}$ not all equal. For $1 < p < 2(d+1)/d$, the $L^2$-normalized Gaussian $g(\xi) = e^{-\pi|\xi|^2/2}$ does not satisfy the Euler–Lagrange equation of the extension inequality (whenever the inequality holds). Extends Christ–Quilodrán [1] from elliptic to hyperbolic case.

## Method
Compute $Tg$ explicitly (separable Gaussian integral), derive the first-variation Euler–Lagrange equation, and exploit hyperbolicity to factor the $t$-integral over $\xi_+$ and $\xi_-$ signature blocks. Differentiate the EL equation $k$ times in $r_\pm = |\xi_\pm|^2$ at $0$ to obtain moment identities $\int_0^\infty (\frac{p^2/d^2 + s^2(q-p)^2}{(q-1)^2 + 4s^2})^k B(s)\,ds = 0$ for all $k$. Change variables to a bounded interval and apply Weierstrass polynomial approximation to derive a contradiction (since $B \not\equiv 0$). A special "diagonal" exponent $p_d$ where $\frac{p_d/d}{q_d-1} = \frac{1}{2}$ is treated by restricting to $|\xi_+|^2 = |\xi_-|^2$.

## Result
For every hyperbolic paraboloid (mixed signature, $d \geq 2$) and every $p \in (1, 2(d+1)/d) \setminus \{2\}$, Gaussians fail the Euler–Lagrange equation, so they cannot be extremizers/critical points. Section 3 additionally shows for the $d=2$ saddle $\tau = \xi_1^2 - \xi_2^2$: (i) the auxiliary operator $K$ satisfies $K\mathbf{1} \equiv \infty$ (unlike paraboloid case), (ii) $K: L^2(\mathbb{R}^4) \to L^2(\mathbb{R}^4)$ is unbounded — $Kg$ involves a Bessel $K_0$ kernel with non-$L^2$ behavior — so Hundertmark–Zharnitsky's [4] approach does not transfer.

## Why it matters here
General background on extremizer analysis for Fourier-extension/Strichartz inequalities; informs the **Cohn-Elkies / magic-function** lineage of variational arguments and Euler–Lagrange techniques used in sphere-packing and autocorrelation problems. No direct Einstein Arena tie, but the *moment-via-polynomial-approximation* contradiction technique is a reusable analytic-combinatorial tool for ruling out Gaussian ansätze.

## Open questions / connections
- Sharp form / extremizers of the $L^2 \to L^4$ Strichartz inequality for the $d=2$ saddle $\tau = \xi_1^2 - \xi_2^2$ remain open — Foschi [3] and Hundertmark–Zharnitsky [4] paraboloid methods break (this paper shows why).
- What replaces Gaussians as candidate extremizers? Symmetry under $R(F)(\eta_1,\eta_2,\nu_1,\nu_2) = F(\nu_1,\eta_2,\eta_1,\nu_2)$ is suggestive but does not preserve tensor-product class.
- Extends Christ–Quilodrán [1] (elliptic case) to all mixed-signature surfaces; complements profile decomposition of Dodson–Marzuola–Pausader–Spirn [2].

## Key terms
Strichartz inequality, Fourier extension operator, hyperbolic paraboloid, saddle surface, Gaussian extremizer, Euler–Lagrange equation, critical point, Christ–Quilodrán, Foschi, Hundertmark–Zharnitsky, Weierstrass approximation, restriction conjecture, modified Bessel $K_0$, tensor product operator
