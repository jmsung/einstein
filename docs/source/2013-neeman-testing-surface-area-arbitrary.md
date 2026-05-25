---
type: source
kind: paper
title: Testing surface area with arbitrary accuracy
authors: Joe Neeman
year: 2013
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1309.1387
source_local: ../raw/2013-neeman-testing-surface-area-arbitrary.pdf
topic: general-knowledge
cites:
---

# Testing surface area with arbitrary accuracy

**Authors:** Joe Neeman  ·  **Year:** 2013  ·  **Source:** https://arxiv.org/abs/1309.1387

## One-line
Sharpens Kothari et al.'s surface-area property tester to multiplicative factor $1+\eta$ for arbitrary $\eta>0$, and extends it from $[0,1]^n$ to Markov diffusion semigroups on Riemannian manifolds.

## Key claim
For any $A\subset\mathbb{T}^n$ with $C^1$ boundary and $\eta,t>0$, there exists $B$ with $\lambda_n(A\Delta B)\le \mathrm{NS}_t(A)/\eta$ and $\tfrac{2\sqrt t}{\sqrt\pi}\lambda_n^+(B)\le (1+o(\eta))\,\mathrm{NS}_t(A)$ — replacing Kothari et al.'s dimension-dependent constant $\kappa_n\in[1,4/\pi]$ by $1+\eta$. Algorithm uses $O(\eta^{-3}\epsilon^{-1}S^2)$ noise-sensitivity samples.

## Method
Smooth $1_A$ by the diffusion semigroup $P_t$, then threshold $P_t 1_A$ at a *random* level $s\in[\eta,1-\eta]$ chosen by the weighted density $\psi(s)=(\tfrac12-|s-\tfrac12|)/I(s)$ where $I$ is the Gaussian isoperimetric profile. Coarea formula + Bakry–Ledoux gradient bound $|\nabla P_t f|\le c_R(t) I(P_t f)$ then control the expected surface area of the level set. Lemma 2.5 gives $\int_0^1\psi=\sqrt{2/\pi}$, yielding the sharp constant.

## Result
Theorem 2.1: under Bakry–Émery curvature $R$, the construction produces $B$ with $\mu^+(B)\le \bigl(1+\tfrac{\sqrt\pi\eta\log(1/\eta)}{\sqrt 2}\bigr)(1+o_\eta(1))c_R(t)\mathrm{NS}_t(A)$, where $c_R(t)=\sqrt{e^{2Rt}R^{-1}/(\cdot)}$ for $R\ne 0$ and $c_0(t)=(2t)^{-1/2}$. Recovers torus ($R=0$), Gaussian/Ornstein–Uhlenbeck ($R=1$), and removes the spurious $4/\pi$ in the Gaussian case.

## Why it matters here
General background; no direct arena tie. Closest hooks: the **noise-sensitivity ↔ surface-area** duality (Crofton/Ledoux) and the **random-threshold/level-set** trick for converting smoothed indicators back to sets — both potentially relevant for any arena problem framed via heat-smoothed indicators (sphere packing density via Gaussians, isoperimetric-style bounds).

## Open questions / connections
- Can the $(1+o(\eta))$ factor be removed entirely? Author notes the "dashed-line" set on $\mathbb{T}^1$ as obstruction but doesn't rule out improvement.
- Extends Kothari–Nayyeri–O'Donnell–Wu (SODA 2014); Bakry–Émery curvature framework from [13] gives the manifold generality.
- Random-threshold construction is reusable: optimal $\psi$ choice via isoperimetric profile $I$ is a transferable trick beyond surface area.

## Key terms
surface area, noise sensitivity, property testing, Bakry-Émery curvature, Markov diffusion semigroup, Ornstein-Uhlenbeck, Gaussian surface area, coarea formula, isoperimetric profile, Crofton formula, Ledoux, Kothari, random thresholding
