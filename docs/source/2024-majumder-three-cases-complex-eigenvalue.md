---
type: source
kind: paper
title: Three Cases of Complex Eigenvalue/Vector Distributions of Symmetric Order-Three Random Tensors
authors: Swastik Majumder, Naoki Sasakura
year: 2024
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2408.01030
source_local: ../raw/2024-majumder-three-cases-complex-eigenvalue.pdf
topic: general-knowledge
cites:
---

# Three Cases of Complex Eigenvalue/Vector Distributions of Symmetric Order-Three Random Tensors

**Authors:** Swastik Majumder, Naoki Sasakura  ·  **Year:** 2024  ·  **Source:** https://arxiv.org/abs/2408.01030

## One-line
Computes exact closed-form complex eigenvalue/vector distributions of symmetric order-three random tensors in three Lie-group-invariant settings ($O(N,\mathbb{R})$, $O(N,\mathbb{C})$, $U(N,\mathbb{C})$) by reducing each to a zero-dimensional four-fermi field theory partition function.

## Key claim
For the $U(N,\mathbb{C})$ case the signed distribution edge gives the largest eigenvalue $z_{\text{largest}} \sim 1.657\sqrt{N/\alpha}$, yielding an injective norm (geometric measure of entanglement) of $|C|_{\text{inj}} = 2.34335$ at $\alpha=N/2$, matching the prior numerical estimate $C_0 = 2.356248$ from Fitter–Lancien–Nechita. Transition point: $|v|_c = \sqrt{3\alpha/(8N)}$; edge: $|v|_{\text{edge}} = 0.603501\sqrt{\alpha/N}$.

## Method
Rewrite the eigenvector distribution $\rho(v) = \langle \det M(v,C) \prod \delta(f_a)\rangle_C$ as a partition function with auxiliary fermion pairs $(\psi,\bar\psi),(\varphi,\bar\varphi)$ and Lagrange multipliers $\lambda$; integrate out the Gaussian tensor $C$ and $\lambda$ to obtain a four-fermi action $S_2$. Split fermions into the 2D subspace spanned by $\{v,v^*\}$ versus its transverse complement, compute the transverse partition function in closed form via the identity $\exp(\partial_y G \partial_y)(yHy)^n$, and use Mathematica's `grassmann.m` for the parallel Grassmann integrals. Large-$N$ asymptotics via Lefschetz-thimble saddle-point on a contour integral representation.

## Result
Exact closed-form $\rho(v_R, v_I, \theta)$ for all three symmetry classes. Large-$N$ profiles $\rho \sim e^{Nh}$ with explicit $h$; the holomorphic ($O(N,\mathbb{R})$, $O(N,\mathbb{C})$) cases exhibit transition lines $l_{++} = l_{\tilde b}$ that *cross* the edge of the distribution — qualitatively different from the real symmetric case where the locally-stable region sits between edge and transition. The non-holomorphic $U(N,\mathbb{C})$ signed distribution is monotonic between edge and transition point and infinitely oscillatory beyond, matching the real-symmetric pattern; Monte Carlo with $N=5,8$ and $N_{\text{MC}}=10^4$–$10^5$ confirms the exact formulas and the signed↔genuine agreement near the edge.

## Why it matters here
General background; no direct arena tie. Potentially informs the tensor-eigenvalue / injective-norm machinery if any arena problem reduces to extremal tensor norms or random-tensor edge statistics (closest analogue: spherical $p$-spin / spin-glass complexity formulas in Appendix C, which already underlie some optimization-landscape reasoning).

## Open questions / connections
- Rigorous proof that the signed-distribution edge equals the genuine-distribution edge in the $U(N,\mathbb{C})$ (non-holomorphic) case — proven only for real symmetric tensors (Auffinger–Ben Arous–Černý 2013).
- Why do holomorphic cases lack a locally-stable region between edge and transition, while non-holomorphic cases retain it? Tied to absence of a bounded potential whose critical-point equation matches the holomorphic eigenvector equation.
- Extends Kent-Dobias–Kurchan (2021, 2022) complex landscapes and Sasakura's prior four-fermi series ([arXiv:2208.08837, 2209.07032, 2404.03385]); connects to Dartois–McKenna injective-norm work ([arXiv:2404.03627]).

## Key terms
random tensor, symmetric order-three tensor, complex eigenvector distribution, injective norm, geometric measure of entanglement, four-fermi theory, Lefschetz thimble, saddle-point method, spherical p-spin spin glass, Kac-Rice complexity, signed distribution, Sasakura
