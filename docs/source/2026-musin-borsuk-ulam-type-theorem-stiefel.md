---
type: source
kind: paper
title: Borsuk-Ulam type theorem for Stiefel manifolds and orthogonal mass partitions
authors: Oleg R. Musin
year: 2026
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/2603.18550v2
source_local: ../raw/2026-musin-borsuk-ulam-type-theorem-stiefel.pdf
topic: general-knowledge
cites: 
---

# Borsuk-Ulam type theorem for Stiefel manifolds and orthogonal mass partitions

**Authors:** Oleg R. Musin  ·  **Year:** 2026  ·  **Source:** http://arxiv.org/abs/2603.18550v2

## One-line
Extends Borsuk–Ulam theorems to Stiefel manifolds and uses them to bound the dimension $d$ in which $m$ measures can be simultaneously $2^n$-equipartitioned by any $n$ of $k$ mutually orthogonal hyperplanes.

## Key claim
Defining $\Delta^*(m,k,n)$ as the minimal $d$ guaranteeing $k$ mutually orthogonal hyperplanes such that any $n$ partition each of $m$ measures into $2^n$ equal parts, the paper proves
$$\frac{m\alpha_n(k)}{k} + \frac{k-1}{2} \le \Delta^*(m,k,n) \le m + (\beta_n(k)-1)\,2^{\lfloor \log_2 m\rfloor},$$
where $\alpha_n(k)=\sum_{i=1}^n \binom{k}{i}$ and $\beta_n(k)=\sum_{i=0}^{n-1}\binom{k-1}{i}$. For $n=k$ this matches the Mani-Levitska–Vrećica–Živaljević bound but with the *orthogonal* conclusion; for $n=2,\,m=2^j-1$ the bounds coincide: $\Delta^*(2^j-1,k,2)=2^{j-1}(k+1)-1$.

## Method
Equivariant cobordism theory for $G=(\mathbb{Z}/2)^k$ free actions (Conner–Floyd, Thom). Computes the cobordism class $[V_{n,k}]_G = \Gamma(n-1,\ldots,n-k)$ of the Stiefel manifold and reduces existence of equivariant zeros to non-vanishing of a polynomial product $\prod_\ell(\varepsilon_{\ell,1}a_1+\cdots+\varepsilon_{\ell,k}a_k)$ in the truncated ring $P(i_1,\ldots,i_k)=\mathbb{F}_2[a_1,\ldots,a_k]/(a_1^{i_1+1},\ldots,a_k^{i_k+1})$. The mass-partition application encodes the $\alpha_n(k)$ equipartition equations plus $\binom{k}{2}$ orthogonality conditions as equivariant maps on $V_{d,k}$, then verifies the polynomial inequality via highest-monomial analysis.

## Result
- Theorem 1.4 gives the general bound above; specializes to Theorem 1.3 (orthogonal version of Ramos/MLVZ) at $n=k$.
- Theorem 1.5: $\Delta^*(2^j-1,k,2)=2^{j-1}(k+1)-1$ — tight.
- Corollary 1.6: every finite measure in $\mathbb{R}^d$ admits $d$ mutually orthogonal hyperplanes whose every pair quarters $\mathbb{R}^d$ by measure (corrects an unproven claim of Makeev).
- Theorem 1.7: same orthogonal partition can be achieved with all hyperplanes through the centers of mass, at cost $d \to 2m + (\beta_n(k)-1)2^{\lfloor\log_2 m\rfloor}$.
- Algorithmic: discrete $n=k=2$ case computable in $\Theta(N)$ time (Fakhrutdinov–Musin); polynomial for general $m,k,n$ but not optimal.

## Why it matters here
General background for the discrete-geometry / equivariant-topology toolkit; no direct Einstein Arena problem currently maps to orthogonal-hyperplane mass partition, but the polynomial-in-$\mathbb{F}_2[a_1,\ldots,a_k]/(\text{ideal})$ obstruction technique is the same machinery that bounds chromatic-number and Kneser-type problems, and the Stiefel-manifold cobordism class computation is a reusable lemma for any future arena problem invoking orthogonal-frame equivariance.

## Open questions / connections
- Optimal discrete algorithms for orthogonal $(m,k,n)$ partitioning beyond $n=k=2$ (raised explicitly by the author).
- Tightening upper bound for $n<k$ — only $n=k$ and $(n=2,\, m=2^j-1\text{ or }2^j-2)$ are tight; the gap remains open for general $(m,k,n)$.
- Extends/corrects Makeev [13], Blagojević–Karasev [5], Mejia–Simon–Zhang [16]; refines the Chan–Chen–Frick–Hull [6] Stiefel BUT theorem via cobordism rather than cohomological index.
- The $\mathbb{F}_2$-polynomial non-vanishing reduction may give cleaner re-derivations of MLVZ-style upper bounds (Remark 1).

## Key terms
Borsuk–Ulam theorem, Stiefel manifold, equivariant cobordism, ham-sandwich theorem, mass partition, orthogonal hyperplanes, pancake theorem, Conner–Floyd, Smith homomorphism, $(\mathbb{Z}/2)^k$-action, equivariant index, Musin, Mani-Levitska–Vrećica–Živaljević, Ramos bound, Makeev problem
