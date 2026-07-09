---
type: source
kind: paper
title: Perturbed interpolation formulae and applications
authors: João P. G. Ramos, Mateus Sousa
year: 2020
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/2005.10337v1
source_local: ../raw/2020-ramos-perturbed-interpolation-formulae-applications.pdf
topic: general-knowledge
cites: 
---

# Perturbed interpolation formulae and applications

**Authors:** João P. G. Ramos, Mateus Sousa  ·  **Year:** 2020  ·  **Source:** http://arxiv.org/abs/2005.10337v1

## One-line
Shows that classical and modern Fourier interpolation formulae (Shannon–Whittaker, Vaaler, Radchenko–Viazovska, Cohn–Kumar–Miller–Radchenko–Viazovska) remain valid when the interpolation nodes are perturbed, via a Banach-space "operator close to identity is invertible" principle.

## Key claim
If $T:B\to B$ satisfies $\|T-I\|<1$, then perturbations of interpolation nodes preserve uniqueness/reconstruction. Concretely: (i) a near-Kadec band-limited result valid for $\sup_k|\varepsilon_k| < 0.239$ (real) / $0.2125$ (complex), within $0.011$ of Kadec's sharp $1/4$; (ii) the Radchenko–Viazovska formula at nodes $\sqrt{k}$ survives perturbations $|\varepsilon_k|(1+k)^{5/4} < \delta$; (iii) analogous results for Vaaler (with derivatives, $L<0.111$) and for the $d=8,24$ Cohn–Kumar–Miller–Radchenko–Viazovska formulae.

## Method
Cast each interpolation map as a bounded operator $T$ on a weighted $\ell^2_s(\mathbb{N})$ space; show $\|I-T\|<1$ via Schur's test or the Hilbert–Schmidt test, exploiting decay estimates on interpolating basis functions. A core technical input (Theorem 1.5) sharpens the Radchenko–Viazovska uniform bounds to $|b_n^\pm(x)| \lesssim n^{1/4}\log^{3/2}(1+n)\,e^{-c|x|/\sqrt{n}}$ using modular-form generating-function machinery and Gelfand–Shilov-space characterizations. For band-limited cases the proofs route through discrete Hilbert-transform analogues rather than orthogonality.

## Result
- **Theorem 1.1 (Kadec-like):** PWπ reconstruction works for $L < 0.239$ real, $< 0.2125$ complex.
- **Theorem 1.3 (Vaaler perturbation):** PW₂π with $f$ and $f'$ recoverable from perturbed nodes when $L < 0.111$.
- **Theorem 1.4:** Radchenko–Viazovska even-Schwartz interpolation survives any node perturbation with $|\varepsilon_k| \lesssim k^{-5/4}$; yields a continuous family of self-dual crystalline measures supported on $\pm\sqrt{k+\varepsilon_k}$.
- **Theorem 5.10 / 5.12:** Analogous perturbation ranges $|\varepsilon_k| \lesssim k^{-C_0}$ for the $d=8,24$ interpolation-with-derivatives formulae and for odd Schwartz functions.
- **Corollary 5.8/5.9:** Real-even Fourier uniqueness pairs $(\pm n^\alpha, \pm n^\beta)$ recovered for $\alpha=\beta < 2/9$ by a new route (weaker than prior $1-\sqrt{2}/2 \approx 0.293$ in [25], but extensible in principle).

## Why it matters here
Directly informs the sphere-packing / modular-form interpolation machinery used in P3 (sphere packing $d=8,24$) and any arena problem that leans on Cohn–Elkies-style magic functions or self-dual crystalline measures; demonstrates that the rigid Radchenko–Viazovska node set $\sqrt{k}$ admits a continuous deformation, which is potentially relevant to constructing new uncertainty/sign-uncertainty extremizers tied to the Bourgain–Clozel–Kahane line of problems.

## Open questions / connections
- Can $\sup_x|a_n(x)| = O(1)$ be established (Question 1)? If yes, the perturbation range improves to $|\varepsilon_k| \lesssim k^{-1}$.
- Conjecture 6.2: is there a *uniform* $\theta>0$ (not decaying in $k$) such that $|\varepsilon_k|<\theta$ still gives unique recovery? Would imply full $\alpha \in (0,1/2)$ Fourier-uniqueness for $\{\pm n^\alpha\}$ pairs.
- Connects to Bondarenko–Radchenko–Seip (2020) on L-function-zero interpolation, Cohn–Gonçalves $d=12$ root uncertainty, and Meyer / Lev–Olevskii / Kurasov–Sarnak crystalline-measure constructions.

## Key terms
Fourier interpolation, Radchenko–Viazovska, Cohn–Kumar–Miller–Radchenko–Viazovska, Paley–Wiener space, Kadec 1/4 theorem, Vaaler interpolation, Shannon–Whittaker, crystalline measures, modular forms, sphere packing E8 Leech, Schur test, Hilbert–Schmidt operator, Gelfand–Shilov spaces, Fourier uniqueness pairs, magic function
