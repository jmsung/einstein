---
type: source
kind: paper
title: A Hermite WENO reconstruction for fourth order temporal accurate schemes based on the GRP solver for hyperbolic conservation laws
authors: Zhifang Du, Jiequan Li
year: 2017
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1801.00270
source_local: ../raw/2017-du-hermite-weno-reconstruction-fourth.pdf
topic: general-knowledge
cites:
---

# A Hermite WENO reconstruction for fourth order temporal accurate schemes based on the GRP solver for hyperbolic conservation laws

**Authors:** Zhifang Du, Jiequan Li  ·  **Year:** 2017  ·  **Source:** https://arxiv.org/abs/1801.00270

## One-line
A fifth-order Hermite WENO (HWENO) reconstruction is built atop the two-stage fourth-order GRP-based Lax–Wendroff solver, reusing already-computed cell-interface values to approximate the cell-averaged gradient (first moment) instead of evolving it separately.

## Key claim
The resulting GRP4-HWENO5 scheme attains fourth-order temporal and fifth-order spatial accuracy while invoking the HWENO reconstruction only twice per step (vs four times in standard RK-WENO5), with the gradient $\Delta u_j$ obtained "for free" from the GRP interface values $\hat u^{n+1/2}_{j\pm 1/2}$ via the Newton–Leibniz formula $\Delta u_j = (\hat u_{j+1/2} - \hat u_{j-1/2})/h$.

## Method
The two-stage Lax–Wendroff time stepping ($t^n \to t^{n+1/2} \to t^{n+1}$) uses the generalized Riemann problem (GRP) solver to produce interface values $(u^n_{j+1/2}, (\partial u/\partial t)^n_{j+1/2})$, which feed both the numerical flux and—newly—the HWENO reconstruction's first-moment input. HWENO uses three stencils $S^{(-1)}, S^{(0)}, S^{(1)}$ with linear weights $9/80, 29/80, 21/40$ summing reconstructions from $(\bar u_{j-1}, \bar u_j, \Delta u_{j-1})$, $(\bar u_{j-1}, \bar u_j, \bar u_{j+1})$, and $(\bar u_j, \bar u_{j+1}, \Delta u_{j+1})$; nonlinear weights follow WENO-Z with $\tau_z = |\beta^{(1)} - \beta^{(-1)}|$. The 2D extension uses dimension-by-dimension reconstruction with Gaussian quadrature points on interfaces.

## Result
On smooth Euler tests the scheme achieves the designed 5th-order spatial convergence with $L^1$/$L^\infty$ errors smaller than GRP4-WENO5 at matched CPU cost (e.g., $L^1 \approx 1.43\text{e-}12$ vs $5.99\text{e-}12$ at 640 cells). On Titarev–Toro, large-pressure-ratio Riemann (ratio $10^4$), double-Mach reflection, and 2D vortex-sheet Riemann problems, GRP4-HWENO5 resolves more fine-scale structure than GRP4-WENO5 thanks to its more compact stencil and lower numerical dissipation. A subtle accuracy caveat: naive boundary-derivative interpolation degrades to third order; the authors use the wider 4-cell formula $\partial_x u|_{j+1/2} = (\bar u_{j-1} - 15\bar u_j + 15\bar u_{j+1} - \bar u_{j+2})/(12h)$ instead.

## Why it matters here
General background; no direct arena tie — this is computational PDE / shock-capturing numerics, orthogonal to the arena's discrete-geometry / extremal / autocorrelation problem families. The only loose conceptual cousin is the "reuse intermediate values to save reconstruction work" pattern, which echoes how triple-verify reuses optimizer state rather than re-deriving from scratch.

## Open questions / connections
- Extension of HWENO+GRP4 to unstructured meshes (authors flag as nontrivial future work).
- Whether multi-derivative Runge–Kutta methods (Christlieb et al., Turaci–Öziş) could replace the two-stage construction for even higher order.
- Boundary-cell derivative reconstruction: can a third-order GRP solver (Qian–Li–Wang 2014) eliminate the wide-stencil workaround?

## Key terms
Hermite WENO, HWENO, WENO-Z, generalized Riemann problem, GRP solver, Lax–Wendroff, two-stage fourth-order, hyperbolic conservation laws, finite volume, Euler equations, shock capturing, Cauchy–Kowalevski, smoothness indicators, characteristic decomposition
