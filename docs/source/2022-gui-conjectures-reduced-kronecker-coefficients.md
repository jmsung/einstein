---
type: source
kind: paper
title: Conjectures on the reduced Kronecker coefficients
authors: Tao Gui
year: 2022
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/2210.14668v4
source_local: ../raw/2022-gui-conjectures-reduced-kronecker-coefficients.pdf
topic: general-knowledge
cites: 
---

# Conjectures on the reduced Kronecker coefficients

**Authors:** Tao Gui  ·  **Year:** 2022  ·  **Source:** http://arxiv.org/abs/2210.14668v4

## One-line
Formulates and partially proves log-concavity conjectures for reduced Kronecker coefficients $\bar{g}^\nu_{\lambda\mu}$, extending Okounkov's log-concavity and Lam–Postnikov–Pylyavskyy's Schur log-concavity from $GL_n$ to symmetric-group stable tensor products.

## Key claim
For partitions $\lambda,\mu$ with $\frac{\lambda+\mu}{2}$ a partition, $\bar{g}^\nu_{\frac{\lambda+\mu}{2},\frac{\lambda+\mu}{2}} \geq \bar{g}^\nu_{\lambda,\mu}$ for all $\nu$ (Conjecture 5.1, verified for $|\lambda|,|\mu|\leq 11$, but later disproved by Zabrocki at $|\lambda|=|\mu|=12$, e.g. $\bar{g}^{(11^6)}_{4422,4422}=0$ but $\bar{g}^{(11^6)}_{5511,3333}=1$). Two stronger theorems are proved unconditionally: log-concavity along root directions for one-row $\lambda,\mu$ (Thm 5.4) and one-column $\lambda,\mu$ (Thm 5.6).

## Method
Reformulates the conjecture categorically via Sam–Snowden's $\mathrm{Rep}(S_\infty)$, whose Grothendieck-ring structure constants are the reduced Kroneckers. Proofs of the special cases use Rosas's combinatorial formulas for $g^\nu_{\lambda\mu}$ when $\lambda,\mu$ are both two-row or both hook-shape (lattice-point counts in rectangles $\Gamma(a,b,c,d)(x,y)$). Dimension corollary (Thm 5.3) lifts Lam–Postnikov–Pylyavskyy Schur-positivity via the exponential specialization $\mathrm{ex}_1(s_\lambda)=f^\lambda/|\lambda|!$.

## Result
Establishes $f^{\frac{\lambda+\mu}{2}[d]}\bigr.^{2} \geq f^{\lambda[d]} f^{\mu[d]}$ for $d\geq\max\{|\lambda|+\lambda_1,|\mu|+\mu_1\}$ (Thm 5.3, an inequality on SYT counts). Proves $\bar{g}^\nu_{(j),(k)} \geq \bar{g}^\nu_{(i),(l)}$ and the column analog whenever $i<j\leq k<l$, $j+k=i+l$. Notes the Murnaghan–Littlewood theorem makes Lam–Postnikov–Pylyavskyy a $|\nu|=|\lambda|+|\mu|$ degeneration.

## Why it matters here
General background; no direct arena tie — but the log-concavity-of-multiplicities lens (Okounkov heuristic, saturation, Schur-positivity) is shared technology with extremal-combinatorics and representation-stability arguments that could surface in Arena problems on combinatorial inequalities or symmetric-function bounds.

## Open questions / connections
- Find the right revision of Conjecture 5.1 given Zabrocki's $|\lambda|=|\mu|=12$ counterexamples (5 explicit partitions $\lambda \in \{(1^{16}),(1^{15}),(2,1^{14}),(3,1^{14}),(2,2,1^{13})\}$ at $\lambda=4422,\mu=4422$ vs $\lambda=5511,\mu=3333$).
- Prove (5.9) — the SYT-count analog of the Fomin–Fulton–Li–Poon sort1/sort2 conjecture — which doesn't follow directly from Lam–Postnikov–Pylyavskyy.
- Connections: Kirillov–Klyachko generalized saturation (refuted by Pak–Panova 2020), Huh–Matherne–Mészáros–St. Dizier Kostka log-concavity, equivariant log-concavity à la Matherne–Miyata–Proudfoot–Ramos.

## Key terms
reduced Kronecker coefficients, Littlewood–Richardson coefficients, Okounkov log-concavity conjecture, Schur log-concavity, saturation conjecture, Murnaghan–Littlewood theorem, Kirillov–Klyachko, Sam–Snowden Rep(S_infinity), symmetric group representations, stable tensor product, Schur positivity, standard Young tableaux
