---
type: source
kind: paper
title: Band-Limited Maximizers for a Fourier Extension Inequality on the Circle, II
authors: J. Barker, C. Thiele, Pavel Zorin-Kranich
year: 2020
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2002.05118
source_local: ../raw/2020-barker-band-limited-maximizers-fourier-extension.pdf
topic: general-knowledge
cites:
---

# Band-Limited Maximizers for a Fourier Extension Inequality on the Circle, II

**Authors:** J. Barker, C. Thiele, Pavel Zorin-Kranich  ·  **Year:** 2020  ·  **Source:** https://arxiv.org/abs/2002.05118

## One-line
Rigorous computer-assisted proof that the constant function is the unique real-valued maximizer of the endpoint Tomas–Stein Fourier extension functional on $S^1$ among functions with Fourier modes supported in $|n| \le 120$, quadrupling the previous degree bound of $N=30$.

## Key claim
**Theorem 1:** For real-valued $f \in L^2(S^1)$ with $\hat f_n = 0$ for $|n| > 120$, $\Phi(f) \le \Phi(1)$ with equality iff $f$ is constant, where $\Phi(f) = \|\widehat{f\sigma}\|_{L^6(\mathbb{R}^2)}^6 / \|f\|_{L^2(S^1)}^6$. The proof reduces to positive semidefiniteness of $3N/2+1 = 181$ explicit matrices $(Q_{m,n})$ indexed by lattice triples $m_1+m_2+m_3=D$; the smallest computed eigenvalue is $\approx 3.7 \times 10^{-5}$ (at $D=0$), well above the rigorous error bound $2.3 \times 10^{-5}$ on the operator norm.

## Method
Reduce the extremizer problem (after sign/antipodal-symmetry reductions from [OTZ19]) to PSD checks on matrices whose entries are six-fold Bessel integrals $I_k = \int_0^\infty \prod_{j=1}^6 J_{k_j}(r)\, r\, dr$. Compute each $I_k$ in three pieces $[0,S] \cup [S,T] \cup [T,\infty)$ using 12-point Gauss–Legendre quadrature on the two compact pieces and a 4th-order asymptotic expansion of $J_n$ on the tail, with hand-derived analytic error bounds (Lemmas 3–5) totaling $\le 0.73 \times 10^{-9}$ per integral. All $1.6 \times 10^8$ distinct integrals computed in Arb arbitrary-precision interval arithmetic, C++/OpenMP/MPI on 94 cluster nodes, $\approx 16$ hours wall-time.

## Result
All 181 matrices verified PSD with smallest eigenvalue $\ge 3.6 \times 10^{-5}$, comfortably exceeding the $2.3 \times 10^{-5}$ operator-norm error margin. Smallest eigenvalue occurs at $D=0$ and decays empirically like $\approx 0.15\, N^{-1.74}$ (suggestively $\sim N^{-7/4}$). Small eigenvalues correspond to eigenvectors that are nearly radial functions of $\sqrt{n_1^2+n_2^2+n_3^2}$ — interpretable as Fourier-side bumps approximating antipodal Dirac deltas, the "natural competitor" to constants. Off-diagonal matrix entries concentrate on the surface $n_1^2+n_2^2+n_3^2 = m_1^2+m_2^2+m_3^2$ (the "yellow ellipse" phenomenon), ruling out any naive diagonal-dominance proof.

## Why it matters here
General background; no direct arena tie. The relevant transferable ideas are (a) the **computer-assisted-proof methodology** — reduce an analytic extremizer problem to a finite PSD check, then use interval arithmetic with hand-proved quadrature error bounds to make the numerical check rigorous; (b) the **antipodal-Dirac competitor** intuition for why constants barely win, which generalizes to other sharp-constant problems including sphere-packing-style extremal questions.

## Open questions / connections
- Prove asymptotically (all $N$) that $D=0$ gives the smallest eigenvalue and that $\lambda_{\min}(D=0) \sim N^{-7/4} > 0$, which would imply the full Tomas–Stein constant-maximizer conjecture on $S^1$.
- Find an analytic explanation for the secondary peak locus $n_1^2+n_2^2+n_3^2 = m_1^2+m_2^2+m_3^2$ in matrix entries; quantitative asymptotics here would likely be needed for any structural (non-computational) PSD proof.
- Understand the radial-profile universality of small-eigenvalue eigenvectors (Figure 9 collapse across $N \in \{40,\dots,120\}$) — possibly via a continuum limit / Sturm–Liouville-type operator.
- Extends [OTZ19] ($N=30$) and [OT17] (six-Bessel integral estimates); the $N \to \infty$ resolution remains open.

## Key terms
Tomas–Stein inequality, Fourier extension, sharp Fourier restriction, band-limited maximizer, Bessel function integral, Gauss–Legendre quadrature, asymptotic expansion, positive semidefinite matrix, interval arithmetic, Arb library, computer-assisted proof, antipodal symmetry, Thiele, Zorin-Kranich, equioscillation competitor
