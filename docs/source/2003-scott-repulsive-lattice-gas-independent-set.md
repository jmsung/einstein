---
type: source
kind: paper
title: The repulsive lattice gas, the independent-set polynomial, and the Lovász local lemma
authors: Alexander D. Scott, Alan D. Sokal
year: 2003
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/cond-mat/0309352v2
source_local: ../raw/2003-scott-repulsive-lattice-gas-independent-set.pdf
topic: general-knowledge
cites:
---

# The repulsive lattice gas, the independent-set polynomial, and the Lovász local lemma

**Authors:** Alexander D. Scott, Alan D. Sokal  ·  **Year:** 2003  ·  **Source:** http://arxiv.org/abs/cond-mat/0309352v2

## One-line
Establishes an exact equivalence between the Lovász local lemma in probabilistic combinatorics and the non-vanishing of the independent-set polynomial (hard-core lattice-gas partition function) on a polydisc, then sharpens both via a Dobrushin–Shearer inductive argument.

## Key claim
The conclusion of the Lovász local lemma holds for dependency graph $G$ with event probabilities $\{p_x\}$ **iff** the multivariate independent-set polynomial $Z_G(w)$ is nonvanishing on the closed polydisc $\{|w_x| \le p_x\}$; the standard Lovász sufficient condition $p_x \le r_x \prod_{y \sim x}(1-r_y)$ is recovered as a special case of this analytic non-vanishing criterion.

## Method
Reformulates the LLL as a statement about zeros of the multivariate independent-set polynomial $Z_G(w) = \sum_{S \text{ indep}} \prod_{x \in S} w_x$, viewed as the grand partition function of a hard-core lattice gas. Uses the Mayer/cluster expansion and its alternating-sign property to characterize the region $R(W)$ of polydisc non-vanishing. Proves sufficient conditions by Dobrushin's inductive argument on $|X|$ (rather than by bounding Mayer terms term-by-term), yielding tree-interpretation bounds via self-avoiding-walk trees and pruned SAW-trees.

## Result
(i) Shearer/Dobrushin equivalence: LLL ⇔ $Z_G(-p) > 0$ on the relevant polydisc, with the conclusion $P(\bigcap_x \overline{A_x}) \ge Z_G(-p)$. (ii) A soft-core LLL generalization (Theorems 4.2, 5.4) handling $0 \le W(x,y) \le 1$ "soft" dependencies. (iii) Lopsided LLL extended to the polynomial framework. (iv) Quantitative bounds for $\mathbb Z^d$ hard-core gas: $\lambda_c(\mathbb Z^2) \in [27/256, 4/25] \approx [0.1055, 0.16]$ (Todo's numerical value $0.1193388\ldots$); general $\lambda_c(\mathbb Z^d) = \Theta(1/d)$ with lower bound $(2d-1)^{2d-1}/(2d)^{2d} \sim 1/(2ed)$ and upper bound $d^d/(d+1)^{d+1} \sim 1/(ed)$. (v) Tree case: $Z_T$ computable bottom-up from leaves via the recursion $w_{\text{eff}} \to w/(1+w_{\text{eff}})$.

## Why it matters here
Direct backbone for the **probabilistic-method** concept and any Einstein Arena problem using LLL-style existence arguments (extremal graph theory, Ramsey-flavored constructions, autocorrelation). The independent-set-polynomial / lattice-gas reframing also connects to packing/exclusion problems on graphs ($\mathbb Z^d$ hard-core gas) and gives a tight analytic criterion superior to the textbook LLL — useful when a tighter bound on $P(\bigcap \overline{A_x})$ is needed than the symmetric LLL provides.

## Open questions / connections
- Can the Dobrushin–Shearer inductive non-vanishing argument be extended beyond hard-core self-repulsion (multiaffine $Z_W$) to general repulsive lattice gases with multi-occupation?
- Is there a combinatorial polynomial analog of the LLL for *directed* dependency graphs? (Authors note: independent-set polynomial cannot be it, since exclusion is symmetric.)
- Sharper closure of the $\lambda_c(\mathbb Z^2)$ gap $[27/256, 4/25]$ via larger pruned-SAW-tree supertrees / cylinder transfer-matrix bounds; extends Guttmann, Todo's series-analysis / phenomenological-renormalization estimates.
- Extends Shearer (1985) and Dobrushin (1996) cluster-expansion convergence work; complements Alon–Spencer / Molloy–Reed probabilistic-method literature.

## Key terms
Lovász local lemma, independent-set polynomial, hard-core lattice gas, cluster expansion, Mayer expansion, polymer expansion, Shearer bound, Dobrushin induction, dependency graph, polydisc non-vanishing, self-avoiding-walk tree, lopsided LLL, alternating-sign Mayer coefficients, hard-core fugacity, $\lambda_c(\mathbb Z^d)$, probabilistic method
