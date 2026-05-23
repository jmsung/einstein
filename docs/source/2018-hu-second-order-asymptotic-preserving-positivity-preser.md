---
type: source
kind: paper
title: A Second-Order Asymptotic-Preserving and Positivity-Preserving Exponential Runge-Kutta Method for a Class of Stiff Kinetic Equations
authors: Jingwei Hu, Ruiwen Shu
year: 2018
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1807.03728
source_local: ../raw/2018-hu-second-order-asymptotic-preserving-positivity-preser.pdf
topic: general-knowledge
cites:
---

# A Second-Order Asymptotic-Preserving and Positivity-Preserving Exponential Runge-Kutta Method for a Class of Stiff Kinetic Equations

**Authors:** Jingwei Hu, Ruiwen Shu  ·  **Year:** 2018  ·  **Source:** https://arxiv.org/abs/1807.03728

## One-line
A new exponential Runge-Kutta time-stepping scheme for stiff kinetic PDEs that is simultaneously second-order accurate, asymptotic-preserving as the Knudsen number $\varepsilon \to 0$, and preserves nonnegativity of the density $f$.

## Key claim
The scheme (2.6) with coefficients $w=1/2$, $b_1=b_2=1$, $a_0=a_1=a_2=1/3$ satisfies: (i) second-order accuracy for $\varepsilon=O(1)$ (Prop. 2.3); (ii) $f^n\ge0\Rightarrow f^{n+1}\ge0$ under the forward-Euler CFL $\Delta t\le \Delta t_{FE}/\max(b_1,b_2)$ (Prop. 2.2); (iii) as $\varepsilon\to 0$ with fixed $\Delta t$, it reduces to Heun's SSP-RK2 applied to the compressible Euler limit and drives $f^{n+1}$ to the local Maxwellian $M[U^{n+1}]$ (Prop. 3.1); (iv) discrete entropy decay $S[f^{n+1}]\le S[f^n]$ when coupled with upwind transport.

## Method
Build a four-stage scheme around the exact (or sufficiently accurate) homogeneous-collision propagator $\exp(sQ/\varepsilon)$ — for BGK this is closed-form $e^{-\eta s}g+(1-e^{-\eta s})M[g]$; for ES-BGK a two-point Gauss-Lobatto quadrature; for Boltzmann the Dimarco-Pareschi midpoint rule on $(f-M)e^{\mu t}$; for Fokker-Planck a symmetrized matrix exponential on $\tilde f=f/\sqrt{M}$. Stages interleave collision propagators with explicit transport increments and a convex combination with weight $w$, then Taylor-match order conditions $a_0+a_1+a_2=1$, $a_0=a_2$, $w(b_1+b_2)=1$, $wb_1b_2=1/2$.

## Result
Numerical tests on 1D BGK and Fokker-Planck (with $\varepsilon$ swept from $1$ down to $10^{-10}$) confirm second-order convergence in both kinetic and fluid regimes, with order reduction only in the intermediate $\varepsilon=O(\Delta t)$ band. Positivity is preserved in mixed-regime Riemann-style tests where the comparison IMEX scheme ARS(2,2,2) produces hundreds of negative cells. AP behavior is verified on $\varepsilon(x)$ profiles that span kinetic and fluid zones, matching an explicit SSP-RK2 reference at 10× larger $\Delta t$.

## Why it matters here
General background — kinetic-PDE numerics, not directly tied to any Einstein Arena problem. Marginal relevance to functional-inequality / autocorrelation problems only via shared tools (Maxwellian moments, entropy decay, SSP-RK2 time-stepping); no LP / SDP / sphere-packing / extremal-combinatorics content. No direct arena tie.

## Open questions / connections
- Uniform-in-$\varepsilon$ accuracy of AP schemes (intermediate-regime order reduction) explicitly left open.
- Positivity guarantee for the numerically computed matrix exponential (Fokker-Planck case) — currently patched by post-hoc zeroing of negative entries.
- Extension to higher than second order while keeping positivity + AP simultaneously remains unresolved (cf. ExpRK-V/F in [Li-Pareschi 2014]).

## Key terms
asymptotic-preserving scheme, positivity-preserving, exponential Runge-Kutta, BGK equation, ES-BGK, Boltzmann collision operator, kinetic Fokker-Planck, Vlasov-Poisson-Fokker-Planck, Knudsen number, compressible Euler limit, SSP-RK2, Heun's method, Strang splitting, entropy decay, H-theorem
