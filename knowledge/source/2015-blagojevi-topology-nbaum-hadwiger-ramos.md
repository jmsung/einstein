---
type: source
kind: paper
title: Topology of the Grünbaum–Hadwiger–Ramos hyperplane mass partition problem
authors: Pavle V. M. Blagojević, F. Frick, Albert Haase, G. Ziegler
year: 2015
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1502.02975
source_local: ../raw/2015-blagojevi-topology-nbaum-hadwiger-ramos.pdf
topic: general-knowledge
cites:
---

# Topology of the Grünbaum–Hadwiger–Ramos hyperplane mass partition problem

**Authors:** Pavle V. M. Blagojević, F. Frick, Albert Haase, G. Ziegler  ·  **Year:** 2015  ·  **Source:** https://arxiv.org/abs/1502.02975

## One-line
A critical review of the Grünbaum–Hadwiger–Ramos hyperplane mass partition problem that documents gaps in several prior proofs and establishes a new exact value $\Delta(j,2) = \tfrac{1}{2}(3j+1)$ when $j-1$ is a power of $2$, $j \geq 5$.

## Key claim
$\Delta(2^t + 1, 2) = 3 \cdot 2^{t-1} + 2$ for $t \geq 2$ — i.e., $2^t+1$ masses in $\mathbb{R}^{3\cdot 2^{t-1}+2}$ admit a simultaneous equipartition by $2$ hyperplanes, confirming the Ramos lower bound is tight in this family. The paper also exposes essential gaps in prior claims by Mani-Levitska–Vrećica–Živaljević, Živaljević (2008, 2011/2015), and Ramos (1996).

## Method
Configuration-space / test-map scheme with the Weyl group $S_k^\pm = (\mathbb{Z}/2)^k \rtimes S_k$ acting on product configuration space $Y_{d,k} = (S^d)^k$ and test space $U_k^{\oplus j}$ (signed orthant-mass deviations). The new $\Delta(2^t+1,2)$ bound uses an equivariant degree calculation (equivariant Hopf theorem mod $|G|$) over a restricted bisector locus; the $\Delta(2,2)=3$ proof is a clean degree argument on a $\mathbb{Z}/4$-invariant circle in the bisector configuration. Gap analysis uses Fadell–Husseini index, Dickson polynomials, equivariant Poincaré duality, and explicit counterexamples to a key parity lemma.

## Result
- New: $\Delta(2^t+1, 2) = 3\cdot 2^{t-1}+2$ for $t \geq 2$ (Thm 5.1).
- Reproved: $\Delta(2,2)=3$ (Hadwiger) via degree (Thm 4.4); $\Delta(1,3)=3$ as corollary.
- General bounds restated: $\lceil (2^k-1)j/k \rceil \leq \Delta(j,k) \leq 2^{t+k-1}+r$ where $j=2^t+r$, $0\leq r\leq 2^t-1$; coincide giving $\Delta(2^{t+1}-1,2)=3\cdot 2^t-1$.
- Topological reduction $\Delta(j-m,k)\leq d-m$ from non-existence of an $S_k^\pm$-equivariant map $Y_{d,k}\to S(U_k^{\oplus j})$ (Thm 3.4) — a topological analog of Matschke's $\Delta(j,k)\leq \Delta(j+1,k)-1$.
- Negative: free configuration space $Z_{d,k}$ admits equivariant maps when $(2^k-1)j+2\geq dk$ — restricting to $Z_{d,k}$ cannot settle new Ramos cases (kills Živaljević 2008's route to $\Delta(1,4)=4$).

## Why it matters here
General background; no direct arena tie. Hyperplane equipartition / ham-sandwich machinery is adjacent to discrete-geometry problems but the 23 arena problems do not currently include a Grünbaum-style equipartition instance — relevance is methodological (equivariant obstruction, Fadell–Husseini index, configuration-space/test-map scheme as a template for Borsuk–Ulam-style impossibility arguments).

## Open questions / connections
- The last Grünbaum case $\Delta(1,4) = 4$ remains open; Živaljević's 2008 approach via $Z_{4,4}$ is shown to fail in principle.
- The Ramos conjecture $\Delta(j,k) = \lceil (2^k-1)j/k \rceil$ remains open in most $(j,k)$; current exact rows fill only a sparse table (see Table 2).
- Promised follow-up: relative equivariant obstruction theory on join configuration spaces $X_{d,k}$ (Blagojević–Frick–Haase–Ziegler, Doc. Math. 21 (2016)).
- Gap-fixing pattern (non-free actions break Poincaré-duality-based obstruction setups) is reusable diagnostic when reading older equivariant-topology papers.

## Key terms
Grünbaum–Hadwiger–Ramos problem, hyperplane mass partition, equipartition, ham-sandwich theorem, Borsuk–Ulam, Fadell–Husseini index, equivariant obstruction theory, configuration space/test map scheme, Weyl group $S_k^\pm$, Dickson polynomial, equivariant Hopf theorem, moment curve lower bound
