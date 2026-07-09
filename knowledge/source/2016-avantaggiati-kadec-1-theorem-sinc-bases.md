---
type: source
kind: paper
title: Kadec-1/4 Theorem for Sinc Bases
authors: A. Avantaggiati, P. Loreti, P. Vellucci
year: 2016
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1603.08762
source_local: ../raw/2016-avantaggiati-kadec-1-theorem-sinc-bases.pdf
topic: general-knowledge
cites:
---

# Kadec-1/4 Theorem for Sinc Bases

**Authors:** A. Avantaggiati, P. Loreti, P. Vellucci  ·  **Year:** 2016  ·  **Source:** https://arxiv.org/abs/1603.08762

## One-line
Transfers the classical Kadec-1/4 stability bound from exponential bases in $L^2(-\pi,\pi)$ to sinc bases in the Paley–Wiener space $PW_\pi$, then extends it with a non-uniform power-law bound and a complex-perturbation bound governed by the Lamb–Oseen constant.

## Key claim
Three results for perturbed sinc systems $\{\mathrm{sinc}(\lambda_n - t)\}$ to remain Riesz bases of $PW_\pi$: (i) the classical $|\lambda_n - n| < 1/4$ transfers verbatim from exponentials to sinc; (ii) for real $\lambda_n - n = A/n^\alpha$ with $\alpha > 1/2$ and $0 < A < \tfrac{1}{\pi}\sqrt{1/(2\sqrt{2}\,\zeta(2\alpha))}$, the system is a Riesz basis (numerically $A \approx 0.443$ at $\alpha = 1$, exceeding Kadec's $1/4$); (iii) for complex $\lambda_n$, the stability bound is $|\lambda_n - n| < \tfrac{1}{\pi}\sqrt{3/(8\alpha)} \approx 0.218$, where $\alpha = 1.25643\ldots$ is the Lamb–Oseen constant.

## Method
Plancherel/Parseval transfer between $PW_\pi$ and $L^2(-\pi,\pi)$ via Fourier, reducing sinc-perturbation norms to exponential-perturbation norms in Kadec's original setup. For Theorem 2 (non-uniform real bound), expand the perturbed sinc in the unperturbed sinc basis, apply Hölder–Schwarz, and bound $\sum_n [1 - \mathrm{sinc}(A/n^\alpha)]$ via $\zeta(2\alpha)$. For Theorem 3 (complex bound), Taylor-expand $\mathrm{sinc}(\lambda_n - t)$ in $(\lambda_n - n)^k$, use Plancherel + Hilbert's double-series inequality to control diagonal and off-diagonal terms, then reduce the resulting series $x^{-1}(e^x - x - 1) = 1$ to a Lambert-$W$ equation whose root is the Lamb–Oseen constant.

## Result
Real uniform: $L < 1/4$ optimal (matches Kadec, with Ingham's counterexample at $1/4$). Real non-uniform power-law: bound $A < \tfrac{1}{\pi\sqrt{2\sqrt{2}\,\zeta(2\alpha)}}$, exceeding $1/4$ for $\alpha$ near $1$ (numerical table shows $A \approx 0.443$ admissible at $\alpha = 1$). Complex uniform: $L < \tfrac{1}{\pi}\sqrt{3/(8\alpha)} = 0.218492\ldots$, where $\alpha = -\tfrac{1}{2} - W_{-1}(-\tfrac{1}{2}e^{-1/2}) = 1.25643\ldots$ is transcendental (by Lindemann–Weierstrass, shown in earlier paper).

## Why it matters here
General background; no direct arena tie. Closest relevance is to functional-analytic stability bounds for non-uniform sampling / interpolation bases, which could inform parameterization choices for any arena problem whose feasible set is encoded as a perturbed lattice (e.g. autocorrelation, uncertainty); but no current Einstein Arena problem is a sinc-basis stability problem.

## Open questions / connections
- Optimality of the complex-case bound $\tfrac{1}{\pi}\sqrt{3/(8\alpha)}$ is explicitly left open — is the Lamb–Oseen constant the sharp threshold or an artifact of Hilbert's inequality?
- Extends Paley–Wiener (1934), Kadec (1964), Duffin–Eachus (1942), and Vellucci (2014) to sinc systems; relates to Avdonin, Khrushchev, Pavlov on Muckenhoupt-type generalizations.
- The non-uniform power-law bound exceeds Kadec's $1/4$ — does a similar non-uniform gain exist for the complex case?

## Key terms
Kadec-1/4 theorem, sinc basis, Riesz basis, Paley–Wiener space, cardinal series, Shannon sampling, non-uniform sampling, Lamb–Oseen constant, Lambert W function, exponential basis stability, Hilbert double-series inequality, Riemann zeta function
