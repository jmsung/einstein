---
type: source
kind: paper
title: Topological boundary modes in isostatic lattices
authors: C. Kane, T. Lubensky
year: 2013
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1308.0554
source_local: ../raw/2013-kane-topological-boundary-modes-isostatic.pdf
topic: general-knowledge
cites:
---

# Topological boundary modes in isostatic lattices

**Authors:** C. Kane, T. Lubensky  ·  **Year:** 2013  ·  **Source:** https://arxiv.org/abs/1308.0554

## One-line
Establishes a topological band-theory framework for isostatic spring-mass lattices, predicting protected zero-frequency floppy modes localized at boundaries and domain walls.

## Key claim
Generalized Maxwell-Calladine index splits into local and topological parts, $\nu_S = \nu_S^L + \nu_S^T$, with the topological count on a surface indexed by reciprocal vector $G$ given by $\tilde\nu_T = G \cdot R_T / 2\pi$, where $R_T$ is a Bravais lattice vector built from BZ winding numbers of $\det Q(k)$.

## Method
"Square root" of the dynamical matrix $D = QQ^T$ via the off-diagonal block Hamiltonian $H = \begin{pmatrix} 0 & Q \\ Q^T & 0 \end{pmatrix}$ in symmetry class BDI, mapping the mechanical problem to SSH-type topological band theory. A Callias-style local index theorem ties zero-mode counts in a subregion to winding numbers $n_i = (2\pi i)^{-1}\oint_{C_i} \mathrm{Tr}[Q^{-1}\nabla_k Q]\,dk$ of $\det Q(k)$ along BZ cycles. Verified on a 1D rotor-spring chain (SSH-equivalent) and a deformed kagome lattice parameterized by $(x_1,x_2,x_3;z)$.

## Result
Deformed kagome phase diagram has 8 octants in $\mathrm{sgn}(x_1,x_2,x_3)$: two trivial ($R_T=0$, twisted-kagome class) and six topologically distinct phases related by $C_6$, with $R_T = \tfrac{1}{2}\sum_p a_p\,\mathrm{sgn}\,x_p$. Domain walls between $R_T^1$ and $R_T^2$ host $G\cdot(R_T^1-R_T^2)/2\pi$ protected floppy modes (or states of self-stress with opposite sign). Continuum elastic energy $f = \tfrac{K}{2}[(u_{xx}-a_1 u_{yy})^2 + 2a_4 u_{xy}^2]$ with $a_1 \propto x_1$ distinguishes phases via sign of $a_1$ (negative Poisson ratio when $a_1>0$); Rayleigh-wave penetration changes from $O(k_\|^{-1})$ to $O(k_\|^{-2})$ when $a_1<0$, with surface-angle threshold $\theta_c = \cot^{-1}\sqrt{|a_1|}$ controlling acoustic surface-mode count.

## Why it matters here
General background; no direct arena tie. The index-theorem framing (boundary count = bulk winding number) and the bulk-boundary correspondence may inform thinking about extremal lattices and rigidity constraints, but none of the 23 Einstein Arena problems are about phonon spectra or topological mechanics.

## Open questions / connections
- 3D extensions: do isostatic pyrochlore / cubic lattices realize analogues of strong topological insulators with protected surface modes?
- Topologically protected gapless points (Dirac-semimetal analogues) where $\det Q(k)$ has point zeros — not realized in deformed kagome but possible elsewhere.
- Connections to frustrated magnetism (cf. Lawler 2013) and to rigidity percolation thresholds via the local index $\nu_L^S$.

## Key terms
isostatic lattice, Maxwell-Calladine count, floppy modes, states of self-stress, topological band theory, SSH model, Su-Schrieffer-Heeger, Callias index theorem, winding number, deformed kagome, Bloch Hamiltonian, BDI symmetry class, Rayleigh surface waves, negative Poisson ratio, equilibrium matrix, Kane, Lubensky
