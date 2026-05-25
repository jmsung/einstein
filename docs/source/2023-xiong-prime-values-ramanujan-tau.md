---
type: source
kind: paper
title: Prime values of Ramanujan's tau function
authors: Bo Xiong
year: 2023
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2311.12073
source_local: ../raw/2023-xiong-prime-values-ramanujan-tau.pdf
topic: general-knowledge
cites:
---

# Prime values of Ramanujan's tau function

**Authors:** Bo Xiong  ·  **Year:** 2023  ·  **Source:** https://arxiv.org/abs/2311.12073

## One-line
Proves that the set of primes occurring as values of Ramanujan's $\tau$-function has Dirichlet density at most $2/11$, so at least $9/11$ of primes are omitted from the image of $\tau$.

## Key claim
**Theorem 1.2:** For each $b \in \{2,4,6,7,8,9,10,\ldots,21\} \setminus \{3,5\}$ (i.e. 18 residues mod 23), the set $P_b \cap T$ of primes $\equiv b \pmod{23}$ that are **not** $\tau$-values satisfies $\pi_{P_b \cap T}(N) \gg N/\log N$. Consequently (Cor. 1.4), the set of primes not in the image of $\tau$ has Dirichlet density $\geq 9/11$, upgrading the prior $\pi_T(N) \gg \log N$ bound to $\pi_T(N) \gg N/\log N$.

## Method
Three-regime split on $k$ for $\tau(p^{2k})$ (odd primes only appear at odd squares $n = p^{2k}$): **small $k$ ($k=1,2$)** ruled out by Ramanujan's mod-23 congruence (Prop. 3.1) restricting $\tau(p^k)$ to residues $\{1,3,5,22\} \pmod{23}$; **large $k$** ruled out by Schinzel's lower bound on cyclotomic values, giving $|\tau(p^k)| > 3^{(121/52)(k+1)}$ so $\tau(p^{2k}) \notin [-N,N]$ once $k > \frac{\log N}{2\log 2}$; **middle $k$** bounded via Bombieri–van der Poorten's quantitative Roth theorem applied to the Thue equation $F_{2k}(x,y) = D$ where $\tau(p^{2k}) = F_{2k}(p^{11}, \tau(p)^2) = \prod_{j=1}^{k}(y_p - 4\cos^2(\pi j/(2k+1)) x_p)$.

## Result
The middle-regime count satisfies $\#(P \cap X_{2k} \cap [-N,N]) < N^{1/2} + N^{3/11} < N^{9/10}$, dominated by $N/\log N$ from PNT in arithmetic progressions on each of 18 residue classes. Combined this proves $\pi_{P_b \cap T}(N) \gg N/\log N$ and Dirichlet density $\geq 9/11$ for primes not in $\mathrm{Im}(\tau)$. Lehmer's smallest prime $\tau$-value remains $\tau(63001) = -80561663527802406257321747$.

## Why it matters here
General background; no direct arena tie. The Thue/Thue–Mahler reduction (factoring $F_{2k}(x,y) = \prod_j (y - \alpha_{j,k} x)$ over cyclotomic roots) and the Bombieri–van der Poorten quantitative Roth bound are reusable templates for any Diophantine-image sparsity argument; mod-23 (or analogous prime) congruence sieving is a useful pattern for restricting attainable residues in extremal/combinatorial enumerations.

## Open questions / connections
- Lehmer's conjecture ($\tau(n) \neq 0$) remains open; this paper sidesteps it by studying image density rather than the zero set.
- Can the $9/11$ density be improved toward $1$ (i.e. is the image of $\tau$ density-zero among primes)?
- Extends Murty–Murty–Shorey, Balakrishnan–Craig–Ono–Tsai, Bennett–Gherga–Patel–Siksek on explicit omitted values from finite identification to asymptotic density.
- Analogous statements for other weight-12 / level-1 Hecke eigenform coefficients?

## Key terms
Ramanujan tau function, modular forms, cusp form weight 12, Hecke multiplicativity, Deligne bound, Lehmer conjecture, mod-23 congruence, Thue equation, Thue–Mahler, cyclotomic polynomial, Schinzel primitive divisor, Bombieri–van der Poorten, quantitative Roth theorem, Dirichlet density, prime number theorem arithmetic progressions, omitted values, absolute height
