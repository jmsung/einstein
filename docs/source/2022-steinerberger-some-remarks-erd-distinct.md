---
type: source
kind: paper
title: Some Remarks on the Erdős Distinct Subset Sums Problem
authors: Stefan Steinerberger
year: 2022
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/2208.12182v2
source_local: ../raw/2022-steinerberger-some-remarks-erd-distinct.pdf
topic: general-knowledge
cites: 
---

# Some Remarks on the Erdős Distinct Subset Sums Problem

**Authors:** Stefan Steinerberger  ·  **Year:** 2022  ·  **Source:** http://arxiv.org/abs/2208.12182v2

## One-line
Reproves the best-known lower bound $a_n \geq (2/\pi - o(1)) \cdot 2^n/\sqrt{n}$ for Erdős's distinct subset sums problem via a Fourier-analytic identity, and reframes the problem as asking whether random walks can simultaneously have small largest step, large variance, and near-Gaussian distribution.

## Key claim
For any positive reals $a_1,\dots,a_n$, $\int_{\mathbb{R}} \left(\frac{\sin \pi x}{\pi x}\right)^2 \prod_{i=1}^n \cos(a_i x)^2 dx \geq \pi/2^n$, with equality iff all $2^n$ subset sums are $1$-separated; combined with bounds on near-origin and far-from-origin contributions, this yields $a_n \geq (2/\pi - o(1)) \cdot 2^n/\sqrt{n}$.

## Method
Fourier-analytic / $L^2$ approach: smooth the random-walk measure $\mu = \sum \delta_{x_i}/2^n$ by convolving with $h = \frac{1}{2}\chi_{[-1,1]}$, then use Parseval to convert $\|\mu*h\|_{L^2}^2$ into an integral of $\widehat{h}(\xi)^2 \prod \cos(2\pi a_i \xi)^2$. Bound the integral near the origin (Elkies-style, cosines aligned) and far from the origin (new contribution via $L^2$ comparison to the Gaussian density of the random walk). Berry-Esseen used as an auxiliary tool under $a_n^2 \leq c \cdot n^{-2/3-\varepsilon} \sum a_i^2$.

## Result
Best constant $c \geq 2/\pi$ reproved (matching Dubroff-Fox-Xu 2021). Theorem 2: if subset sums are $1$-separated and $a_n^2 \leq c \cdot n^{-1/2}\sum a_i^2$, then $\int |(h*\mu)(x) - \gamma(x)|^2 dx \leq (1+o(1))/2^n$ where $\gamma$ is the matching Gaussian — i.e., distinct subset sums with small $a_n$ forces the random walk's smoothed density to approximate a Gaussian in $L^2$. Conway-Guy best construction sits at $a_n \leq 0.88008 \cdot 2^{n-2}$.

## Why it matters here
Direct relevance to autocorrelation / Sidon-set / additive combinatorics arena problems via the Fourier-on-$\pm$-random-walk technique; the "integral of $\prod \cos(a_i x)^2$" identity is a transferable tool for distinct-difference / B$_h$-type extremal problems. Reinforces compute-router intuition: pure analytic identity, no optimizer needed for the bound.

## Open questions / connections
- Can a random walk simultaneously achieve $a_n \leq c \cdot n^{-1/3}\sqrt{\text{Var } X}$, large variance, AND $L^2$-close-to-Gaussian smoothed density? Existence would imply $a_n \ll n^{-1/3-\varepsilon} \cdot 2^n$.
- Multi-scale structure suggested by Theorem 1: aligning cosines at $x = k\pi/a_n$ hints that extremal sets may have terms clustering at $a_n, a_n/2, a_n/4, \dots$ (consistent with Conway-Guy).
- Can the $1/\sqrt{\pi n} + (\sqrt{2}-1)/(2\sqrt{\pi n})$ decomposition be tightened by analyzing more frequency regions $|x| \geq k/(4a_n)$?

## Key terms
Erdős distinct subset sums, Rademacher random walk, Conway-Guy sequence, Berry-Esseen theorem, Gaussian approximation, Fourier transform, Parseval identity, Elkies bound, subset sum separation, sum-distinct sets, additive combinatorics, $L^2$ density approximation
