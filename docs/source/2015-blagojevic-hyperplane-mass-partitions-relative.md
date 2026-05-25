---
type: source
kind: paper
title: Hyperplane mass partitions via relative equivariant obstruction theory
authors: Pavle V. M. Blagojevi'c, F. Frick, Albert Haase, G. Ziegler
year: 2015
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1509.02959
source_local: ../raw/2015-blagojevic-hyperplane-mass-partitions-relative.pdf
topic: general-knowledge
cites:
---

# Hyperplane mass partitions via relative equivariant obstruction theory

**Authors:** Pavle V. M. Blagojevi'c, F. Frick, Albert Haase, G. Ziegler  ·  **Year:** 2015  ·  **Source:** https://arxiv.org/abs/1509.02959

## One-line
Develops a join-scheme + relative equivariant obstruction theory framework that reduces the Grünbaum–Hadwiger–Ramos hyperplane mass-partition problem to counting equivalence classes of "$\ell$-equiparting" Gray-code matrices, settling several open cases of Ramos' conjecture.

## Key claim
The Ramos lower bound $\Delta(j,k) = \lceil 2^{k-1}j/k \rceil$ is tight in new cases: $\Delta(2,3)=5$, $\Delta(4,3)=10$, and $\Delta(2^t,2)=3\cdot 2^{t-1}$ for all $t\geq 1$ — derived from a parity/odd-count criterion on $\ell$-equiparting binary matrices.

## Method
Replaces the standard product configuration space $(S^d)^k$ with the **join** $X_{d,k}=(S^d)^{*k}$, equipped with the hyperoctahedral $S_k^\pm = (\mathbb{Z}/2)^k \rtimes S_k$ action; the non-free locus $X_{d,k}^{>1}$ provides a base map (independent of the masses up to homotopy) so **relative** equivariant obstruction theory (tom Dieck) applies even when $\dim X - \dim S(W_k\oplus U_k^{\oplus j})>1$. A Fox–Neuwirth/Björner–Ziegler cone stratification yields an explicit small regular $S_k^\pm$-CW model; obstruction cocycles are evaluated against masses concentrated on a **binomial-coefficient moment curve** $\hat\gamma(t)=(t,\binom{t}{2},\ldots,\binom{t}{d})$, turning the count of equipartitions into counting non-equivalent concatenated $k$-bit Gray codes with prescribed row transition counts.

## Result
**Theorem 1.4 (master criterion):** if the number of non-equivalent $\ell$-equiparting $k\times j2^k$ matrices is odd, then $\Delta(j,k)=\lceil 2^{k-1}j/k\rceil$. Applications: Theorem 1.5 gives all three $k=2$ branches $\Delta(2t-1,2)=3\cdot 2^{t-1}-1$, $\Delta(2t,2)=3\cdot 2^{t-1}$, $\Delta(2t+1,2)=3\cdot 2^{t-1}+2$ (uniform proof, fixing earlier flawed proofs of Mani-Levitska–Vrećica–Živaljević and Živaljević via Kummer's $p$-adic valuation lemma applied to $\binom{j}{\lfloor j/2\rfloor}$). Theorem 1.6 establishes $\Delta(2,3)=5$ (13 matrices) and $\Delta(4,3)=10$ (2015 matrices, computer-enumerated). Corollary 1.7: $\Delta(1,4)\leq 5$ and $\Delta(2,4)\leq 10$ via Hadwiger–Ramos reduction, narrowing Grünbaum's original $k=4$ conjecture to $\Delta(1,4)\in\{4,5\}$.

## Why it matters here
General background; no direct arena tie — this is equivariant-topology machinery for *discrete-geometry partition existence proofs*, not optimization. Closest arena resonance: techniques toolbox for problems where a counting/parity argument certifies a topological obstruction (and the moment-curve construction as the extremal example, echoing Avis 1984's lower-bound trick used elsewhere in the wiki).

## Open questions / connections
- Grünbaum's original $\Delta(1,4)=?$ open: is it 4 (conjecture) or 5 (this paper's upper bound)? Reduces to whether *some* $0$-equiparting $4\times 16$ matrix count is odd.
- General Ramos conjecture for $k\geq 4$ — need a closed-form parity of $N(j,k,d)$ for the Gray-code count; Table 1 suggests no obvious pattern.
- Whether the join-scheme + relative obstruction approach extends to constrained partitions (convex equipartitions à la [6], Nandakumar–Rao).
- Computer enumeration scales poorly past $k=3$ — open whether the count admits a generating-function / transfer-matrix form.

## Key terms
Grünbaum–Hadwiger–Ramos, hyperplane mass partition, equivariant obstruction theory, join configuration space, hyperoctahedral group, Fox–Neuwirth stratification, Gray code, moment curve, Ramos conjecture, Ham Sandwich theorem, Kummer's theorem, tom Dieck, Blagojević–Ziegler, Avis lower bound
