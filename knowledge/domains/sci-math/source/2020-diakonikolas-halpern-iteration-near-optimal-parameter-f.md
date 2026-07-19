---
type: source
kind: paper
title: Halpern Iteration for Near-Optimal and Parameter-Free Monotone Inclusion and Strong Solutions to Variational Inequalities
authors: Jelena Diakonikolas
year: 2020
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2002.08872
source_local: ../raw/2020-diakonikolas-halpern-iteration-near-optimal-parameter-f.pdf
topic: general-knowledge
cites:
---

# Halpern Iteration for Near-Optimal and Parameter-Free Monotone Inclusion and Strong Solutions to Variational Inequalities

**Authors:** Jelena Diakonikolas  ·  **Year:** 2020  ·  **Source:** https://arxiv.org/abs/2002.08872

## One-line
A simple potential-function proof of Halpern iteration's convergence yields near-optimal, parameter-free algorithms for monotone inclusion and strong VI solutions, including convex-concave min-max with gradient-norm guarantees.

## Key claim
For $L$-cocoercive $F$ on a Hilbert space, the Halpern iteration $u_{k+1}=\lambda_{k+1}u_0+(1-\lambda_{k+1})(u_k-\tfrac{2}{L_{k+1}}F(u_k))$ with $\lambda_k=\Theta(1/k)$ and an adaptive doubling estimate $L_k$ achieves $\|F(u_k)\|\le\epsilon$ in $O(L\|u_0-u^*\|/\epsilon + \log(L/L_0))$ oracle queries — the first $1/k$ rate for monotone inclusion *without* knowing $L$. For $L$-Lipschitz monotone $F$, an inexact-resolvent variant achieves the same rate up to a log factor (improving the prior $1/\sqrt{k}$). For $m$-strongly-monotone $L$-Lipschitz $F$, restarting yields $\widetilde{O}((L/m)\log(1/\epsilon))$ — near-optimal and parameter-free.

## Method
Novel **potential function** $C_k=\tfrac{1}{L_k}\tfrac{\lambda_k}{1-\lambda_k}\|F(u_k)\|^2-\langle F(u_k),u_0-u_k\rangle$ with weights $A_k=k(k+1)/2$; show $A_{k+1}C_{k+1}\le A_kC_k$ via elementary algebra (no PEP / SDP computer-aided proof as in Lieder 2017 / Kim 2019). Unknown Lipschitz/cocoercivity constant handled by **backtracking doubling** on $L_k$ when the cocoercivity inequality $\langle F(u_k)-F(u_{k-1}),u_k-u_{k-1}\rangle\ge\tfrac{1}{L_k}\|F(u_k)-F(u_{k-1})\|^2$ fails. Constrained case uses **operator mapping** $G_\eta(u)=\eta(u-\Pi_U(u-F(u)/\eta))$ as a cocoercive surrogate; merely-monotone case couples Halpern with **inexact proximal/resolvent** evaluations (Catalyst-style).

## Result
Four matching upper/lower bounds in the operator oracle model: (a) cocoercive — $O(L\|u_0-u^*\|/\epsilon)$, tight up to $\log$; (b) monotone Lipschitz — $\widetilde{O}(LD/\epsilon)$; (c) strongly monotone Lipschitz — $\widetilde{O}((L/m)\log(1/\epsilon))$; (d) translates to convex-concave min-max with gradient-norm (stationarity) guarantees on **unbounded** domains, unlike optimality-gap bounds which require bounded $U$. Lower bounds derived via reductions from Ouyang–Xu (2019) min-max lower bound.

## Why it matters here
General background; no direct arena tie. The methodology — building a clean potential function for an algorithm previously only analyzed by PEP — is a transferable template for finite-step optimality proofs, but Einstein Arena problems are extremal/discrete/packing rather than monotone-VI. Possible tangential use: parameter-free step-size adaptation via the doubling-on-failure pattern could inform polish loops where the local Lipschitz constant is unknown.

## Open questions / connections
- Does the potential-based proof extend to non-Euclidean / Bregman settings (where Halpern is currently open)?
- Can the inexact-resolvent technique close the remaining $\log$ gap to the lower bound for monotone Lipschitz?
- Connection to PEP: which other computer-assisted convergence proofs admit elementary potential rewrites?
- Implicit regularization (convergence to minimum-norm fixed point) — preserved under the inexact and constrained variants?

## Key terms
Halpern iteration, monotone inclusion, variational inequality, cocoercive operator, nonexpansive map, resolvent, proximal point, strong solution, Stampacchia VI, Minty VI, convex-concave min-max, gradient-norm minimization, potential function, parameter-free algorithm, performance estimation problem, Lieder, Kim, Ouyang-Xu lower bound, Catalyst, operator mapping
