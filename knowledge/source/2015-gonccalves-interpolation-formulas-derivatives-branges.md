---
type: source
kind: paper
title: Interpolation Formulas With Derivatives in De Branges Spaces II
authors: F. Gonccalves, Friedrich Littmann
year: 2015
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1510.08383
source_local: ../raw/2015-gonccalves-interpolation-formulas-derivatives-branges.pdf
topic: general-knowledge
cites:
---

# Interpolation Formulas With Derivatives in De Branges Spaces II

**Authors:** F. Gonccalves, Friedrich Littmann  ·  **Year:** 2015  ·  **Source:** https://arxiv.org/abs/1510.08383

## One-line
Characterizes when entire functions in de Branges spaces $\mathcal{H}(E^\nu)$ can be reconstructed from values of the function and its derivatives at the real zeros of $B$, generalizing Vaaler's derivative-interpolation formula for Paley-Wiener spaces.

## Key claim
For Hermite-Biehler $E$ with $E'/E \in H^\infty(\mathbb{C}^+)$ and phase satisfying $\varphi'(t) \gtrsim 1$ on $T_B$, every $F \in \mathcal{H}(E^\nu)$ admits the interpolation $F(z) = \sum_{t \in T_B} \sum_{j=0}^{\nu-1} F^{(j)}(t) G_{\nu,j}(z,t)$ converging in $\mathcal{H}(E^\nu)$, with the frame equivalence $\sum_{t,j} |F^{(j)}(t)|^2 / K_\nu(t,t) \asymp \|F\|^2_{\mathcal{H}(E^\nu)}$; the uniform lower bound on $\varphi'$ is also necessary (Theorem 3), and $E'/E \in H^\infty(\mathbb{C}^+)$ is equivalent to $\mathcal{H}(E^\nu)$ being closed under differentiation for any $\nu \geq 2$ (Theorem 1).

## Method
De Branges reproducing-kernel Hilbert space theory: factor $E^\nu = A_\nu - iB_\nu$, construct the dual interpolation functions $G_{\nu,j}(z,t)$ from Taylor expansions of $B(z)^\nu/(z-t)^\nu$ at zeros $t \in T_B$, establish density of their span via the orthogonal decomposition $\mathcal{H}(E_aE_b) = E_a^* \mathcal{H}(E_b) \oplus E_b \mathcal{H}(E_a)$ and induction on $\nu$. Frame bounds are obtained via Hilbert-type inequalities (Montgomery-Vaaler) on the uniformly separated nodes $T_B$, and the $L^p$ extension (Theorem 15) uses a Pólya-Plancherel-type sampling bound plus singular-part / Cauchy-pole decomposition.

## Result
Three main theorems. (1) Equivalence: $E'/E \in H^\infty(\mathbb{C}^+) \Leftrightarrow \mathcal{H}(E^\nu)$ closed under differentiation for some/all $\nu \geq 1$. (2) Under that hypothesis plus $\varphi' \gtrsim 1$ on $T_B$, the derivative-interpolation series converges in $\mathcal{H}(E^\nu)$ and gives a (weighted) frame; removing any single node breaks the equivalence. (3) The phase bound $\varphi' \gtrsim 1$ on $T_B$ is necessary for the frame norm-equivalence. Corollary 5 applies this to homogeneous de Branges spaces $\mathcal{H}(E_\alpha^\nu)$ (built from Bessel functions $J_\alpha, J_{\alpha+1}$) yielding $\int |F|^2 |x|^{(2\alpha+1)\nu} dx \asymp \sum_{j,n} |F^{(j)}(a_{\alpha,n})|^2 |a_{\alpha,n}|^{(2\alpha+1)\nu}$ for $F$ of exponential type $\leq \nu$, recovering Vaaler-type formulas with Bessel-zero nodes.

## Why it matters here
Direct relevance to autocorrelation and Beurling-Selberg extremal problems: derivative-interpolation in de Branges spaces is the engine behind one-sided band-limited majorants used in large-sieve, Hilbert-type, Erdős-Turán, and $\zeta(s)$ bounds — and the constructive frame here gives a recipe for building such majorants when the standard $\mathcal{H}(E)$ (Shannon-Whittaker) machinery is insufficient. Anchors any arena problem reducible to "$L^1$ extremal function of exponential type $\tau$ with weight $|x|^{2\alpha+1}$".

## Open questions / connections
- Open: convergence in $\|\cdot\|_{H^p(E^\nu)}$ of the interpolation series for $1 \leq p < \infty$ (only uniform-on-compacta + pointwise shown; norm convergence conjectured but unproved).
- Open: equivalence of $E'/E \in H^\infty(\mathbb{C}^+)$ and bounded differentiation on $H^p(E^\nu)$ for $p \neq 2$ (no counterexample known).
- Extends Vaaler 1985 (PW derivative interpolation) and Gonccalves 2017 (Theorem A — first-derivative case in $\mathcal{H}(E^2)$); connects to Holt-Vaaler 1996, Carneiro-Littmann-Vaaler 2013 (Gaussian subordination).

## Key terms
de Branges spaces, Hermite-Biehler function, reproducing kernel, derivative interpolation, Paley-Wiener space, Beurling-Selberg extremal, exponential type, frame, Bessel zeros, homogeneous de Branges space, Hilbert-type inequality, phase function, Vaaler, autocorrelation, band-limited
