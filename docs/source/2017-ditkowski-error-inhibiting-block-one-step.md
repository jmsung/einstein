---
type: source
kind: paper
title: Error Inhibiting Block One-step Schemes for Ordinary Differential Equations
authors: A. Ditkowski, S. Gottlieb
year: 2017
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1701.08568
source_local: ../raw/2017-ditkowski-error-inhibiting-block-one-step.pdf
topic: general-knowledge
cites:
---

# Error Inhibiting Block One-step Schemes for Ordinary Differential Equations

**Authors:** A. Ditkowski, S. Gottlieb  ·  **Year:** 2017  ·  **Source:** https://arxiv.org/abs/1701.08568

## One-line
Constructs explicit block one-step ODE integrators whose global error is one order higher than their local truncation error, breaking the usual "global order = LTE order" assumption.

## Key claim
By choosing the coefficient matrices $A, B$ in $V_{n+1} = (A + \Delta t B f) V_n$ so that (C1) $\mathrm{rank}(A)=1$, (C2) the lone nonzero eigenvalue is $1$ with eigenvector $(1,\dots,1)^T$, (C3) $A$ is diagonalizable, and (C4) the leading local truncation error lies in the span of eigenvectors of $A$ corresponding to the zero eigenvalues, one obtains $\|E_n\| = O(\Delta t)\max_\nu \|\tau_\nu\|$ — i.e. the global error gains one order over the LTE for linear, variable-coefficient, and nonlinear ODEs.

## Method
Rewrite multistep schemes in block one-step form $V_{n+1} = Q_n V_n$ with $Q_n = A + \Delta t B F_n$ (a Type 3 DIMSIM in Butcher's taxonomy). Analyze the discrete Duhamel sum $E_n = Q^n E_0 + \Delta t \sum Q^{n-\nu-1}\tau_\nu$ and force $\tau_\nu$ to live in the $O(\Delta t)$-eigenspace of $Q$ so that $\|Q\tau_\nu\| = O(\Delta t)\|\tau_\nu\|$, suppressing accumulation. Constants in $A, B$ are solved to make the leading LTE coefficient vector collinear with the zero-eigenvalue eigenvectors of $A$.

## Result
Explicit $s=2$ scheme: LTE $O(\Delta t^2)$, global $O(\Delta t^3)$, verified on $u_t=-u^2$ and van der Pol (observed slopes $\approx 2.96$–$3.20$). Explicit $s=3$ schemes (three variants): LTE $O(\Delta t^3)$, global $O(\Delta t^4)$ (observed slopes $\approx 3.87$–$4.07$). A control Type-3 DIMSIM from Butcher [2] satisfying C1–C3 but violating C4 shows only second-order global error, confirming C4 is the operative condition.

## Why it matters here
General background; no direct arena tie — numerical-ODE machinery, not relevant to the discrete-geometry, sphere-packing, autocorrelation, or extremal-combinatorics families that dominate Einstein Arena. The "error lives in a designed eigenspace" trick is a generic numerical-analysis idea; no obvious lift to the wiki's optimization-on-finite-configurations setting.

## Open questions / connections
- Linear stability regions of these EIS methods (deferred by authors).
- Computational efficiency and storage vs standard Runge–Kutta / multistep methods.
- Whether the eigenspace-projection trick extends to multi-derivative or implicit Type-3 DIMSIM families.

## Key terms
error inhibiting schemes, block one-step methods, general linear methods, DIMSIM Type 3, local truncation error, global error, Lax-Richtmyer equivalence, Dahlquist barrier, discrete Duhamel principle, eigenspace projection, Ditkowski, Gottlieb, Butcher
