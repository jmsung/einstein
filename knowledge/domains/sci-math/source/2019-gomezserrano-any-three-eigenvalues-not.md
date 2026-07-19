---
type: source
kind: paper
title: Any three eigenvalues do not determine a triangle
authors: Javier G'omez-Serrano, Gerard Orriols
year: 2019
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1911.06758
source_local: ../raw/2019-gomezserrano-any-three-eigenvalues-not.pdf
topic: general-knowledge
cites:
---

# Any three eigenvalues do not determine a triangle

**Authors:** Javier G'omez-Serrano, Gerard Orriols  ·  **Year:** 2019  ·  **Source:** https://arxiv.org/abs/1911.06758

## One-line
Rigorous computer-assisted proof that two non-isometric triangles can share their 1st, 2nd, and 4th Dirichlet–Laplacian eigenvalues, refuting the strong form of Antunes–Freitas's spectral-determination conjecture for triangles.

## Key claim
**Theorem 1.1:** There exist two non-isometric triangles $T_A$ and $T_B$ with $\lambda_i(T_A)=\lambda_i(T_B)$ for $i=1,2,4$. Explicitly, $T_A$ has third vertex near $(0.63500,0.27500)$ and $T_B$ near $(0.84906,0.31995)$ (with the other two vertices fixed at $(0,0),(1,0)$), and the shared quotients are $\xi_{21}=\lambda_2/\lambda_1 \approx 1.67675$, $\xi_{41}=\lambda_4/\lambda_1 \approx 2.99372$. An open set of such pairs exists (Remark 1.2).

## Method
Two-pass rigorous eigenvalue enclosure via interval arithmetic (Arb library). **Pass 1:** Crouzeix–Raviart non-conforming FEM with Liu's a-posteriori bound (Thm 2.1: $\lambda_{h,k}/(1+C_h^2\lambda_{h,k})\le\lambda_k$) plus Gershgorin disks on a near-diagonalized matrix to locate spectral position and lower-bound $\lambda_5$. **Pass 2:** Method of Particular Solutions with Gopal–Trefethen "lightning Laplace" basis (Bessel $Y_0,Y_1$ at exponentially-clustered charges near vertices + Bessel $J_j$ at centroid) for root-exponential convergence; Barnett–Hassell tension bound (8)–(12) with explicit constants via Rellich's formula $\|\partial_n u_j\|_{L^2(\partial\Omega)}^2 = 2\lambda_j/\rho$ converts $L^2$-boundary residual into tight eigenvalue enclosure. Closed→open lift: Poincaré–Miranda theorem applied to sign changes of $\xi_{21}-\bar\xi_{21}$ and $\xi_{41}-\bar\xi_{41}$ on parallelogram boundaries in moduli space; per-side stability via eigenvalue monotonicity + scaling (Lemmas 3.3–3.5) reduces to finitely many triangle evaluations (40 subdivisions per side, ~42 CPU-hours, parallelized to <1 hour on 80 machines).

## Result
Two parallelograms around $A=(0.63500,0.27500)$ and $B=(0.84906,0.31995)$ in the third-vertex parameter space are validated: along their boundaries the signs of $\xi_{21}-1.67675$ and $\xi_{41}-2.99372$ flip in the Poincaré–Miranda pattern, forcing an interior root inside each. Hence both parallelograms contain a triangle realizing the same $(\xi_{21},\xi_{41})$ pair, yielding an isospectral $(λ_1,λ_2,λ_4)$ pair far from any explicitly-known isospectral configuration. Settles the negative direction of conjectures in Laugesen–Siudeja [35], Grieser–Maronna [23], and Lu–Rowlett [39].

## Why it matters here
General background; no direct arena tie. Demonstrates a transferable pattern useful for the agent: convert a closed equality condition into an open sign-change topological condition (Poincaré–Miranda / Brouwer-style) so that **interval arithmetic + tight enclosures + finite sampling** can prove existence — relevant any time the agent needs to certify a saddle/coincidence in moduli space (e.g., parameter-space verification for P5/P6/P11/P14/P17 where local↔arena drift is float-sensitive).

## Open questions / connections
- Do **any** three eigenvalues (e.g. $\lambda_1,\lambda_2,\lambda_3$) determine a triangle? Antunes–Freitas conjecture for $(\lambda_1,\lambda_2,\lambda_3)$ remains open.
- Is Chang–DeTurck's $N(T)$ (number of eigenvalues sufficient to distinguish $T$) uniformly bounded over all triangles?
- Extends Plum's homotopy method [49] and Liu–Oishi FEM bounds [37,38] by combining their strengths (global index location + local enclosure refinement) — pattern likely useful beyond triangles.
- Lightning Laplace solver (Gopal–Trefethen 2019) as a general tool for corner-singular PDE eigenproblems.

## Key terms
Dirichlet eigenvalues, Laplacian spectrum, isospectral triangles, hearing the shape of a drum, Method of Particular Solutions, lightning Laplace solver, Gopal–Trefethen, Crouzeix–Raviart FEM, Barnett–Hassell tension bound, Poincaré–Miranda theorem, Gershgorin disks, interval arithmetic, Arb library, computer-assisted proof, Faber–Krahn, Rellich formula, Antunes–Freitas conjecture
