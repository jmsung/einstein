---
type: source
kind: paper
title: "Perturbing the Mean Value Theorem: Implicit Functions, the Morse Lemma, and Beyond"
authors: David Lowry-Duda, M. Wheeler
year: 2019
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1906.02026
source_local: ../raw/2019-lowryduda-perturbing-mean-value-theorem.pdf
topic: general-knowledge
cites:
---

# Perturbing the Mean Value Theorem: Implicit Functions, the Morse Lemma, and Beyond

**Authors:** David Lowry-Duda, M. Wheeler  ·  **Year:** 2019  ·  **Source:** https://arxiv.org/abs/1906.02026

## One-line
Studies when the mean value abscissa $c$ in $f'(c) = (f(b)-f(a))/(b-a)$ can be chosen as a continuous function of the right endpoint $b$, using the implicit function theorem, Morse's lemma, and an analytic extension.

## Key claim
For any non-constant real analytic $f$ on $[a_0, b_0]$, there always exists at least one mean value abscissa $c_0$ admitting a locally continuous extension $c = C(b)$; this fails for merely smooth (non-analytic) functions.

## Method
Reduce the MVT condition to an implicit equation $F(b,c) = 0$ where $F(b,c) = (f(b)-f(a))/(b-a) - f'(c)$. Apply the implicit function theorem (proved via Banach contraction mapping) when $f''(c_0) \neq 0$; when both $f''(c_0) = 0$ and $f'(b_0) = f'(c_0)$, use a simplified Morse lemma exploiting the separable form $G(x,y) = g_1(x) - g_2(y)$. For analytic $f$, classify by orders of vanishing $\ell, k$ of $g_1, g_2$, giving normal form $v^k = \pm u^\ell$.

## Result
Three theorems: (4) if $f''(c_0) \neq 0$ then $c = C(b)$ exists continuously differentiable; (6) if $f''(c_0) = 0$ but $f''(b_0), f'''(c_0) \neq 0$, then existence depends on sign — same signs give two branches forming an "X", opposite signs give an isolated point; (8) analyticity guarantees at least one continuous branch via a min/max extremum argument forcing odd order of vanishing of $f'$.

## Why it matters here
General background; no direct arena tie. The implicit function theorem + Morse lemma + analytic normal forms ($v^k = \pm u^\ell$ classification) are general tools relevant to understanding bifurcation/branching of solution sets in optimization landscapes — potentially useful as a lens on basin structure or parameter continuation, but not directly applied to any current Einstein Arena problem.

## Open questions / connections
- Generalization to two-parameter family $c = C(a,b)$ varying both endpoints — the separable decomposition $G = g_1 - g_2$ breaks.
- Global structure of MVT solution sets: connected components, endpoints, topology — requires non-local techniques.
- Smooth (non-analytic) counterexamples via bump functions show analyticity is essential; what intermediate regularity classes suffice?

## Key terms
mean value theorem, implicit function theorem, Morse lemma, contraction mapping principle, Banach fixed-point theorem, analytic functions, Morse index, normal form, order of vanishing, Taylor expansion, bifurcation, Lowry-Duda
