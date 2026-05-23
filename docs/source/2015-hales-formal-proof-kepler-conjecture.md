---
type: source
kind: paper
title: A FORMAL PROOF OF THE KEPLER CONJECTURE
authors: T. Hales, Mark Adams, G. Bauer, Dat Tat Dang, J. Harrison, T. Hoang, C. Kaliszyk, Victor Magron, Sean McLaughlin, T. Nguyen, T. Nguyen, T. Nipkow, Steven Obua, Joseph Pleso, Jason M. Rute, A. Solovyev, A. Ta, T. Tran, Diep Thi Trieu, J. Urban, K. Vu, R. Zumkeller
year: 2015
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1501.02155
source_local: ../raw/2015-hales-formal-proof-kepler-conjecture.pdf
topic: general-knowledge
cites:
---

# A FORMAL PROOF OF THE KEPLER CONJECTURE

**Authors:** T. Hales, Mark Adams, G. Bauer, Dat Tat Dang, J. Harrison, T. Hoang, C. Kaliszyk, Victor Magron, Sean McLaughlin, T. Nguyen, T. Nguyen, T. Nipkow, Steven Obua, Joseph Pleso, Jason M. Rute, A. Solovyev, A. Ta, T. Tran, Diep Thi Trieu, J. Urban, K. Vu, R. Zumkeller  ·  **Year:** 2015  ·  **Source:** https://arxiv.org/abs/1501.02155

## One-line
Final report of the Flyspeck project: a complete machine-checked formal proof of the Kepler conjecture on dense sphere packings in $\mathbb{R}^3$, carried out in HOL Light and Isabelle/HOL.

## Key claim
No packing of congruent balls in Euclidean 3-space has density greater than $\pi/\sqrt{18} \approx 0.7405$ (the face-centered cubic / hexagonal-close packing density); formalized as: for any packing $V \subset \mathbb{R}^3$ (pairwise distances $\ge 2$), there exists $c$ such that $|V \cap B(0,r)| \le \pi r^3/\sqrt{18} + c r^2$ for all $r \ge 1$.

## Method
Three-pronged reduction following Hales–Ferguson 2006 (blueprint version): (i) Marchal cell partition + a "cell cluster inequality" reduces the global density problem to a **local annulus inequality** $\sum_{v\in V} f(\|v\|) \le 12$ over finite packings $V \subset \{2 \le \|x\| \le 2.52\}$ with $|V|\le 15$; (ii) combinatorial structure of any contravening packing is encoded as a **tame planar hypermap / plane graph**, exhaustively enumerated up to isomorphism (18762 graphs in the archive); (iii) for each tame graph, a system of $\sim 1000$ nonlinear inequalities (in $\le 6$ variables, verified by **interval arithmetic with Taylor approximations**) is linearly relaxed and 43,078 resulting linear programs are proven infeasible via modified rational dual certificates (GLPK + integer arithmetic).

## Result
Theorem `the_kepler_conjecture` is formally proved from three computational lemmas (`the_nonlinear_inequalities`, `import_tame_classification`, `linear_programming_results`) plus the text part. The main statement verifies in $\sim 5$ hours on a 2 GHz CPU ($\sim 40$ min from recorded proof objects); LP verification $\sim 15$ hours; the hardest nonlinear-inequality bundle takes $\sim 5000$ CPU-hours. A bug in the original Java enumeration (symmetry handling, dormant — output was still correct) and hundreds of small text errors were found and fixed during formalization; the main estimate in the original proof contained a substantive error (corrected in Hales et al. 2010).

## Why it matters here
Direct relevance to Einstein Arena **sphere-packing / kissing-number / discrete-geometry** problems: the Flyspeck architecture (local annulus inequality + tame-graph enumeration + LP relaxation of nonlinear systems + interval-arithmetic certified inequalities) is a template for any "global packing → finite combinatorial cases → LP infeasibility" reduction. The local annulus inequality itself solved Bezdek's strong dodecahedral conjecture and Fejes Tóth's contact conjecture, suggesting transferability. Also a reference point for **triple-verify discipline**: the project's core methodology is that hand-written + interval + LP checks must all agree, formalized.

## Open questions / connections
- Uniqueness of the FCC/HCP density-maximizer is NOT proven by Flyspeck — open question for any arena problem asking for extremal configuration characterization.
- The constant $c$ in the error term is proved existential but a uniform computable $c$ is known to exist — quantitative refinement open.
- Cell Cluster Inequality reduces to "hundreds of nonlinear inequalities in $\le 6$ variables" — the most delicate piece; technique for similar reductions in higher-dimensional packings (cf. Viazovska $d=8, 24$) remains an open avenue.
- Connection to Cohn–Elkies LP bound: Flyspeck's LP relaxation is structurally different (combinatorial linearization of geometric nonlinearities, not Fourier-analytic) — interesting cross-method comparison.

## Key terms
Kepler conjecture, sphere packing, face-centered cubic, FCC density $\pi/\sqrt{18}$, Flyspeck, HOL Light, Isabelle/HOL, Marchal cells, tame planar hypermap, local annulus inequality, interval arithmetic, Taylor interval approximation, linear programming relaxation, GLPK, dual certificate, cell cluster inequality, Hales, Ferguson, Fejes Tóth, formal verification, nonlinear inequalities
