---
type: source
kind: paper
title: A tight structure theorem for sumsets
authors: A. Granville, A. Walker
year: 2020
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2006.01041
source_local: ../raw/2020-granville-tight-structure-theorem-sumsets.pdf
topic: general-knowledge
cites:
---

# A tight structure theorem for sumsets

**Authors:** A. Granville, A. Walker  ·  **Year:** 2020  ·  **Source:** https://arxiv.org/abs/2006.01041

## One-line
Proves the tight threshold $N \geq b - \ell$ above which the $N$-fold sumset $NA$ of a finite set $A = \{0 = a_0 < \cdots < a_{\ell+1} = b\}$ (with $\gcd = 1$) equals the full interval $\{0, \ldots, bN\}$ minus the two "exceptional" sets $E(A) \cup (bN - E(b-A))$.

## Key claim
**Theorem 1:** For $A \subset \mathbb{Z}_{\geq 0}$ with $0, b \in A$, $\gcd(A) = 1$, and $\ell$ interior elements, if $N \geq b - \ell$ then $NA = \{0, 1, \ldots, bN\} \setminus (E(A) \cup (bN - E(b-A)))$. The bound $b - \ell$ is tight: counterexamples exist at $N = b - \ell - 1$ for $A = \{0,1,\ldots,b\}\setminus\{a\}$ and $A = \{0,1,a+1,\ldots,b-1,b\}$ (and these are the only obstructions — Theorem 2).

## Method
Reduces the question to controlling $|kB|$ (growth of $k$-fold sumsets of $B = A \bmod b$ in $\mathbb{Z}/b\mathbb{Z}$) and $N_A^* = \max_a N_{a,A}$ (minimum length to hit each residue class). Applies **Kneser's theorem** to lower-bound $|kB| \geq \min(b, |(k-1)B| + 2)$ when $\ell \geq 2$, then pigeonhole on subsums to lift residue-class hits into integer-interval hits. The "$N \geq b - \ell$" threshold falls out by combining $|2B| \geq \min(b, \ell+3)$ with $N_A^* \leq b - \ell$.

## Result
Improves the prior progression of bounds: Nathanson's $N \geq b^2(\ell+1)$ → $\sum_{a \in A, a \neq 0}(a-1)$ (Wu–Chen–Chen) → $2\lfloor b/2 \rfloor$ (Granville–Shakan) → $b - \ell$ (this paper, conjectured in [1]). Theorem 2 classifies the only sets achieving the tight $b - \ell$ bound. A flexible extension shows $N \geq b - \ell - \Delta$ also works for larger $\Delta$ outside a finite catalogue of exceptional families.

## Why it matters here
General background; no direct arena tie. Additive-combinatorics structure theorems for $NA$ are tangentially relevant to discrete-combinatorics / sieve-theory problems where representability in restricted sumsets matters (e.g., Sidon-set adjacent questions), but no Einstein Arena problem is currently framed in Frobenius-postage-stamp terms.

## Open questions / connections
- Can the explicit exceptional families be characterized for all $\Delta$, or does the case count grow combinatorially without closed form?
- Extends Nathanson 1972, Wu–Chen–Chen 2011, Granville–Shakan 2020; cites Tao–Vu's *Additive Combinatorics* for Kneser.
- Potential application: tight-bound version of Iyer–Lazarev–Miller–Zhang's "more sums than differences" sets (cited as future use).

## Key terms
sumset structure theorem, Frobenius postage stamp problem, Kneser's theorem, $NA$ sumset, exceptional set $E(A)$, additive combinatorics, Granville, Walker, Nathanson, residue class pigeonhole, $\mathbb{Z}/b\mathbb{Z}$ subgroup stabilizer, gcd-1 finite integer set
