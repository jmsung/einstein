---
type: source
kind: paper
title: "Stochastic Gradient Descent-Ascent and Consensus Optimization for Smooth Games: Convergence Analysis under Expected Co-coercivity"
authors: Nicolas Loizou, Hugo Berard, G. Gidel, Ioannis Mitliagkas, Simon Lacoste-Julien
year: 2021
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2107.00052
source_local: ../raw/2021-loizou-stochastic-gradient-descent-ascent-consensus.pdf
topic: general-knowledge
cites:
---

# Stochastic Gradient Descent-Ascent and Consensus Optimization for Smooth Games: Convergence Analysis under Expected Co-coercivity

**Authors:** Nicolas Loizou, Hugo Berard, G. Gidel, Ioannis Mitliagkas, Simon Lacoste-Julien  ·  **Year:** 2021  ·  **Source:** https://arxiv.org/abs/2107.00052

## One-line
Provides the first last-iterate convergence guarantees for stochastic gradient descent-ascent (SGDA) and stochastic consensus optimization (SCO) on unconstrained stochastic variational inequality problems, without the standard bounded-variance assumption.

## Key claim
Under the new **expected co-coercivity (EC)** assumption — $\mathbb{E}_D\|\xi_v(x) - \xi_v(x^*)\|^2 \le \ell_\xi \langle \xi(x), x-x^*\rangle$ — and $\mu$-quasi-strong monotonicity, SGDA with constant stepsize $\alpha \le 1/(2\ell_\xi)$ converges linearly to a $O(\alpha\sigma^2/\mu)$ neighborhood: $\mathbb{E}\|x_k-x^*\|^2 \le (1-\alpha\mu)^k\|x_0-x^*\|^2 + 2\alpha\sigma^2/\mu$. With a stepsize-switching rule (constant for $k \le 4\lceil K\rceil$ then $\alpha_k = (2k+1)/((k+1)^2\mu)$, $K=\ell_\xi/\mu$) the rate becomes $O(1/k)$ to the exact solution. SCO inherits analogous guarantees and recovers tight deterministic CO rates as a corollary.

## Method
Generalizes the "expected smoothness" framework of Gower et al. (2019, SGD) to operator/VI settings via the EC condition, which is strictly weaker than bounded-variance and growth-condition assumptions. Introduces a stochastic reformulation of the VI problem using arbitrary sampling vectors $v \sim \mathcal{D}$ with $\mathbb{E}[v_i]=1$, giving closed-form expressions for $\ell_\xi$ and $\sigma^2$ under $b$-minibatch sampling: $\ell_\xi = \frac{n(b-1)}{b(n-1)}\ell + \frac{n-b}{b(n-1)}\ell_{\max}$. Proofs use standard Lyapunov-style descent on $\|x_k-x^*\|^2$ plus quasi-strong monotonicity; no Lipschitz continuity of $\xi$ is required.

## Result
- SGDA: linear convergence to neighborhood (constant $\alpha$), $O(1/k)$ to $x^*$ (switching rule).
- SCO: same regime with two stepsizes $\alpha < 1/(2\ell_\xi)$, $\gamma \le 1/(4L_H)$; neighborhood scales as $4(\alpha^2\sigma^2 + \gamma^2\sigma_H^2)/(\gamma\mu_H + \alpha\mu)$.
- Optimal minibatch size: $b^* = 1$ if $\sigma_1^2 \le \ell_{\max}$, else $b^* = (n\ell_{\max} - \frac{2}{\epsilon\mu}\cdot\sigma_1^2)/(n\ell_{\max} + \frac{2}{\epsilon\mu}\cdot\sigma_1^2)$ (approx).
- Deterministic CO and stochastic Hamiltonian gradient descent (SHGD) recovered as special cases; analysis tightens prior deterministic CO bounds.

## Why it matters here
General background; no direct arena tie. The Einstein Arena problems are deterministic geometric/extremal optimization, not stochastic min-max games — SGDA/SCO and the EC condition aren't on the critical path for sphere packing, kissing, autocorrelation, or LP-bound problems. Possible faint relevance to any GAN-flavored or adversarial sub-routine used internally, but the wiki's optimizer techniques (parallel tempering, mpmath polish, basin-hopping, SLSQP, Cohn-Elkies LP) don't overlap.

## Open questions / connections
- Can EC-style assumptions be adapted to non-finite-sum continuous-sampling regimes beyond singleton sampling (Appendix D leaves minibatch generalization open)?
- Quasi-strong monotonicity is the weakest tractable structure here — what's the analogous "right" assumption for the genuinely non-monotone GAN-training regime?
- Extends Gower et al. 2019 (SGD expected smoothness) and Loizou et al. 2020 (SHGD); relates to Mescheder et al. 2017 (CO), Chavdarova et al. 2019 (variance-reduced extragradient), Hsieh et al. 2020 (double-stepsize extragradient).

## Key terms
expected co-coercivity, stochastic variational inequality, SGDA, stochastic consensus optimization, quasi-strong monotonicity, Hamiltonian gradient descent, arbitrary sampling, minibatch complexity, last-iterate convergence, smooth games, min-max optimization, GAN training
