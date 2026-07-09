---
type: source
kind: paper
title: Stochastic First- and Zeroth-Order Methods for Nonconvex Stochastic Programming
authors: Saeed Ghadimi, Guanghui Lan
year: 2013
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1309.5549
source_local: ../raw/2013-ghadimi-stochastic-first-zeroth-order-methods.pdf
topic: general-knowledge
cites:
---

# Stochastic First- and Zeroth-Order Methods for Nonconvex Stochastic Programming

**Authors:** Saeed Ghadimi, Guanghui Lan  ·  **Year:** 2013  ·  **Source:** https://arxiv.org/abs/1309.5549

## One-line
Introduces randomized stochastic gradient (RSG) and gradient-free (RSGF) methods that, for the first time, give finite-iteration complexity bounds for nonconvex stochastic optimization with noisy first- or zeroth-order oracles.

## Key claim
For smooth nonconvex SP with unbiased stochastic gradients of variance $\sigma^2$, RSG outputs $\bar x$ with $\mathbb{E}[\|\nabla f(\bar x)\|^2] \le \epsilon$ in $N = O(1/\epsilon^2)$ iterations; the zeroth-order variant RSGF achieves $O(n/\epsilon^2)$ where $n$ is the dimension. A two-phase variant (2-RSG) tightens large-deviation bounds to $O(\log(1/\Lambda)\sigma^2/\epsilon + \log(1/\Lambda)/(\Lambda\epsilon))$ under sub-Gaussian noise.

## Method
Run SGD-style iterates $x_{k+1} = x_k - \gamma_k G(x_k, \xi_k)$ with constant stepsize $\gamma_k = \min(1/L,\, \tilde D/(\sigma\sqrt N))$, then **randomly select** the output $x_R$ from $\{x_1,\dots,x_N\}$ with probability mass $P_R(k) \propto 2\gamma_k - L\gamma_k^2$ — the randomization is what converts a $\sum \|\nabla f(x_k)\|^2$ bound into an $\mathbb{E}\|\nabla f(x_R)\|^2$ bound. For zeroth-order, replace $G$ with Nesterov's Gaussian-smoothing surrogate $G_\mu(x,\xi,u) = [F(x+\mu u, \xi) - F(x,\xi)]u/\mu$. The two-phase trick runs $S = O(\log(1/\Lambda))$ independent RSGs and picks the candidate with smallest sampled gradient norm.

## Result
Theorem 2.1 / Cor 2.2: $\mathbb{E}[\|\nabla f(x_R)\|^2] \le LD_f^2/N + 2D_f\sigma/\sqrt N$ with optimal $\tilde D = D_f := \sqrt{2(f(x_1)-f^*)/L}$. If $f$ is convex, the *same* algorithm gives $\mathbb{E}[f(x_R) - f^*] \le LD_X^2/N + 2D_X\sigma/\sqrt N$, nearly matching the SP lower bound. Zeroth-order RSGF (Cor 3.3) gives $\mathbb{E}[\|\nabla f(x_R)\|^2] \le 12(n+4)LD_f^2/N + 8\sqrt{n+4}\,D_f\sigma/\sqrt N$ — weaker $n$-dependence than Nesterov's prior $O(n^2/\epsilon^2)$ bound for nonsmooth convex SP, obtained by exploiting smoothness in stepsize and smoothing-parameter $\mu$ selection.

## Why it matters here
General background; no direct arena tie. May inform optimizer choice when a problem's evaluator is intrinsically noisy (Monte Carlo verifier surrogates, randomized SDP solvers) — but Einstein Arena evaluators are deterministic, so SGD-style methods are not the natural fit; CMA-ES / SA / mpmath polish remain dominant. The randomized-output trick is conceptually interesting for ensemble polishing schemes.

## Open questions / connections
- Does the randomized-output construction give any advantage over "argmin $\|\nabla f(x_k)\|$" when gradient norms *are* cheap to evaluate (our setting)? Paper argues no for noisy oracles, yes if exact $\|\nabla f\|$ available.
- Extends Nesterov 2010 Gaussian-smoothing zeroth-order analysis [arxiv 1309.5549 ref 28] from convex to nonconvex SP.
- Leaves open: optimal $n$-dependence for nonconvex stochastic zeroth-order (lower bound unknown); acceleration; adaptive stepsize without knowing $L$.

## Key terms
stochastic approximation, SGD, nonconvex optimization, randomized stochastic gradient, RSG, RSGF, Gaussian smoothing, zeroth-order optimization, derivative-free, gradient-free, Nesterov smoothing, simulation-based optimization, large deviation bound, Robbins-Monro, Polyak-Juditsky averaging, complexity bounds
