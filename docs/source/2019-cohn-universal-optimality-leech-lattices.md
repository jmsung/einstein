---
type: source
kind: paper
title: Universal optimality of the $E_8$ and Leech lattices and interpolation formulas
authors: Henry Cohn, Abhinav Kumar, Stephen D. Miller, D. Radchenko, M. Viazovska
year: 2019
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1902.05438
source_local: ../raw/2019-cohn-universal-optimality-leech-lattices.pdf
topic: general-knowledge
cites:
---

# Universal optimality of the $E_8$ and Leech lattices and interpolation formulas

**Authors:** Henry Cohn, Abhinav Kumar, Stephen D. Miller, D. Radchenko, M. Viazovska  ·  **Year:** 2019  ·  **Source:** https://arxiv.org/abs/1902.05438

## One-line
Proves that $E_8$ and the Leech lattice minimize energy for every completely monotonic potential of squared distance in $\mathbb{R}^8$ and $\mathbb{R}^{24}$, via a new Fourier interpolation formula for radial Schwartz functions.

## Key claim
**Theorem 1.4:** $E_8 \subset \mathbb{R}^8$ and the Leech lattice $\subset \mathbb{R}^{24}$ are *universally optimal* — they minimize $p$-energy for every potential $p(r) = g(r^2)$ with $g$ completely monotonic (inverse power laws, Gaussians, etc.), and are uniquely so among periodic configurations of the same density. This implies optimal sphere packing, minimal Epstein $\zeta_\Lambda(s)$, minimal theta $\Theta_\Lambda(it)$, and minimal height of the flat torus $\mathbb{R}^d/\Lambda$ (Corollary 1.5).

## Method
Cohn–Elkies / Yudin **linear programming bounds** for energy (Proposition 1.6): construct a radial Schwartz $f$ with $f(x) \le p(|x|)$ pointwise and $\hat f \ge 0$, giving energy lower bound $\rho \hat f(0) - f(0)$. Sharpness requires $f$ and $\hat f$ to match $p$ in value and radial derivative at lattice radii $\sqrt{2n}$ (single roots) and vanish to second order at dual-lattice radii. To produce such $f$, the authors prove a new **Fourier interpolation theorem (1.7)** reconstructing radial Schwartz $f$ on $\mathbb{R}^8$/$\mathbb{R}^{24}$ from $f, f', \hat f, \hat f'$ at radii $\sqrt{2n}$ ($n\ge 1$ or $n\ge 2$); the interpolation basis is built from **integral transforms of quasimodular forms**, extending Viazovska's 2016 magic-function construction. Positivity of the kernels is verified by rigorous **interval arithmetic** on elliptic integrals $E$, $K$, near diagonals, edges, and corners of $[0,1]^2$.

## Result
- Universal optimality + uniqueness for $E_8$ and Leech (Theorem 1.4).
- Interpolation formula (1.4): every radial Schwartz $f$ on $\mathbb{R}^8$ or $\mathbb{R}^{24}$ is determined by the four sequences $f(\sqrt{2n}), f'(\sqrt{2n}), \hat f(\sqrt{2n}), \hat f'(\sqrt{2n})$; the map $S_{rad}(\mathbb{R}^d) \to S(\mathbb{N})^4$ is an isomorphism (Theorem 1.9).
- Uniqueness of the optimal LP auxiliary functions for sphere packing in $\mathbb{R}^8$/$\mathbb{R}^{24}$ (Corollary 1.8).
- $\Lambda_d$ uniquely minimizes $\zeta_\Lambda(s)$ for all $s \in (0,\infty) \setminus \{d/2\}$ and $\Theta_\Lambda(it)$ for all $t > 0$, $d \in \{8,24\}$.

## Why it matters here
Canonical reference for the **Cohn–Elkies magic-function / LP-bound** technique that the wiki already treats as a primary tool — extends it from sphere packing to the full completely-monotonic-potential class, and supplies the *interpolation* mechanism (values + radial derivatives at $\sqrt{2n}$) that explains *why* the magic function exists in $d=8, 24$ and likely fails in $d=2$. Directly informs any arena problem touching lattice energies, theta-function extremality, Gaussian-core/LP-bound constructions, and sets the dimensional ceiling for "just copy the Viazovska trick" approaches.

## Open questions / connections
- **Open Problem 7.1:** does $f^{(j)}(\sqrt{kn}) = \hat f^{(j)}(\sqrt{kn}) = 0$ for $0 \le j < k$, $n \ge 0$ force $f \equiv 0$? Known for $(d,k)=(8,2),(24,2)$ and $k=1$ any $d$; open for $k > 2$.
- **Conjecture 7.2 / Open Problem 7.3:** for $d \ge 3$, the Gaussian-energy LP-optimal $\alpha$-independent radii $r_n$ should support an analogous interpolation formula — true numerically for general $d \ge 3$, but no explicit point set known outside $d=8,24$.
- **Conjecture 7.5** (since proved by Sardari 2021): hexagonal-lattice interpolation in $\mathbb{R}^2$ *fails* — distances grow as $CN^2/\sqrt{\log N}$, too sparse — so $d=2$ universal optimality (the remaining Cohn–Kumar conjecture) needs a different mechanism than the $E_8$/Leech strategy.
- Extends Radchenko–Viazovska (2019) Fourier interpolation on $\mathbb{R}$ (single roots) to double-root (value + derivative) interpolation in higher dimensions.

## Key terms
universal optimality, $E_8$ lattice, Leech lattice, Cohn-Elkies linear programming bound, magic function, Fourier interpolation, radial Schwartz function, completely monotonic potential, Gaussian core model, Epstein zeta function, theta series, quasimodular forms, Poisson summation, sphere packing, Viazovska, Cohn, Kumar, Miller, Radchenko, modular forms, interval arithmetic, elliptic integrals, hexagonal lattice, height of flat torus
