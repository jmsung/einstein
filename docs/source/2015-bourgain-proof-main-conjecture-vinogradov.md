---
type: source
kind: paper
title: Proof of the main conjecture in Vinogradov's mean value theorem for degrees higher than three
authors: J. Bourgain, C. Demeter, L. Guth
year: 2015
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1512.01565
source_local: ../raw/2015-bourgain-proof-main-conjecture-vinogradov.pdf
topic: general-knowledge
cites:
---

# Proof of the main conjecture in Vinogradov's mean value theorem for degrees higher than three

**Authors:** J. Bourgain, C. Demeter, L. Guth  ·  **Year:** 2015  ·  **Source:** https://arxiv.org/abs/1512.01565

## One-line
Settles Vinogradov's Main Conjecture for all degrees $n \geq 3$ by reducing it to a sharp $\ell^2$ decoupling inequality for the moment curve $\Gamma_n = \{(t,t^2,\dots,t^n)\}$ and proving that decoupling via multilinear harmonic analysis.

## Key claim
For all $s \geq 1$, $n,N \geq 2$, the Vinogradov system count satisfies $J_{s,n}(N) \lesssim_\varepsilon N^{s+\varepsilon} + N^{2s - n(n+1)/2 + \varepsilon}$ — matching the conjectured (and known-sharp up to $N^\varepsilon$) upper bound. Equivalently, the $\ell^2$-decoupling constant $V_{p,n}(\delta)$ for $\Gamma_n$ at the critical exponent $p = n(n+1)$ satisfies $V_{p,n}(\delta) \lesssim_\varepsilon \delta^{-\varepsilon}$.

## Method
Pure harmonic analysis — no number-theoretic efficient congruencing. Three ingredients: (i) a hierarchy of multilinear Kakeya-type inequalities for $k$-dimensional plates (Bennett–Carbery–Tao tubes, $k=n-1$), invoked via Brascamp–Lieb transversality on the $V_k(t) = \langle \Phi'(t),\dots,\Phi^{(k)}(t)\rangle$ spaces of the moment curve; (ii) a Bourgain–Guth induction-on-scales bootstrap equating linear and multilinear decoupling constants; (iii) a multi-scale iteration combining **ball inflation** (the new ingredient, Theorem 6.6 — enlarge spatial balls by factors $\frac{j+1}{j}$ to enable subsequent decouplings), **lower-dimensional decoupling** (arcs look $(k-1)$-dimensional at scale $\sigma^{-k+1}$), and $L^2$-orthogonality decoupling. The iteration tree is closed by solving a linear system (54) for weights $\omega_j,\eta_j$ and showing $\sum b_j \gamma_j > 1$ near the critical exponent.

## Result
$\ell^2$-decoupling for $\Gamma_n$: for $g:[0,1]\to\mathbb{C}$ and any ball $B \subset \mathbb{R}^n$ of radius $\delta^{-n}$, $\|E_{[0,1]}g\|_{L^{n(n+1)}(w_B)} \lesssim_\varepsilon \delta^{-\varepsilon}\big(\sum_{|J|=\delta} \|E_J g\|_{L^{n(n+1)}(w_B)}^2\big)^{1/2}$. This transfers to discrete restriction (Theorem 4.1) and to the Vinogradov count, including a generalization (Corollary 4.2) to arbitrary well-separated reals $X_i$ — not just integers. For $p > n(n+1)$ the $N^\varepsilon$ loss can be removed via a major/minor-arc argument.

## Why it matters here
General background; no direct arena tie. Relevant cross-cutting tools for Einstein Arena: decoupling/restriction machinery is the modern harmonic-analytic substitute for LP/SDP bounds on exponential-sum problems, and the moment-curve transversality identity (Lemma 6.3, Wronskian argument) is a clean template for "polynomial curves are non-degenerate against generic projections." Plausibly informs autocorrelation-inequality (P-class) reasoning where exponential-sum $L^p$ control bounds energies.

## Open questions / connections
- Extends Wooley's $n=3$ efficient-congruencing result ([18]) to all $n$ and to non-integer well-separated $X_i$.
- Implications for the asymptotic formula in Waring's problem (see Wooley [21]) and for $\zeta(1/2+it)$ moments via decoupling for the Riemann zeta function (Bourgain [5]).
- Open: can decoupling at the critical $p = n(n+1)$ be proved with $\delta^{-\varepsilon}$ replaced by a logarithm or constant? The endpoint sharpness question.
- The Brascamp–Lieb stability result of Bennett–Bez–Flock–Lee [3] used in Proposition 6.4 — generality and effective constants remain interesting.

## Key terms
Vinogradov mean value theorem, $\ell^2$ decoupling, moment curve, multilinear Kakeya, Bennett-Carbery-Tao, Brascamp-Lieb inequality, efficient congruencing, Bourgain, Demeter, Guth, Wooley, ball inflation, induction on scales, discrete restriction, Waring problem, exponential sums
