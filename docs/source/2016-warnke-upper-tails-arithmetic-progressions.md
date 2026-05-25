---
type: source
kind: paper
title: Upper tails for arithmetic progressions in random subsets
authors: L. Warnke
year: 2016
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1612.08559
source_local: ../raw/2016-warnke-upper-tails-arithmetic-progressions.pdf
topic: general-knowledge
cites:
---

# Upper tails for arithmetic progressions in random subsets

**Authors:** L. Warnke  ·  **Year:** 2016  ·  **Source:** https://arxiv.org/abs/1612.08559

## One-line
Closes the long-standing log(1/p) gap in upper-tail estimates for the count of k-term arithmetic progressions (and Schur triples, and edges of induced random subhypergraphs of almost-linear k-uniform hypergraphs) in random subsets of $[n]$.

## Key claim
For $X = X_{k,n,p}$ counting length-$k$ APs in $[n]_p$ with $\mu = \mathbb{E}X$, $\log \mathbb{P}(X \geq (1+\varepsilon)\mu) = -\Theta(\min\{\mu, \sqrt{\mu}\log(1/p)\})$ for constant $\varepsilon$ — matching upper and lower bounds up to constants in the exponent.

## Method
Two new Chernoff-type concentration inequalities (Theorem 9 and a BK-inequality variant) that bound $X$ via $Z_C = \max_{J} \sum_{\alpha \in J} Y_\alpha$ subject to a Lipschitz-like cluster constraint $\sum_{\alpha \in J:\alpha \sim \beta} Y_\alpha \leq C$, with exponent scaling as $1/C$ rather than $1/C^2$. The proof uses a "forced-independence" factorial-moment argument extending the Janson–Ruciński deletion method and Spencer's disjoint-subfamily technique; lower bounds combine three deviation mechanisms (interval clustering, Paley–Zygmund on configurations, vertex-count fluctuations via Harris' inequality).

## Result
Theorem 4 (general): for almost-linear $k$-uniform $H_n$ with $e(H) \geq an^2$, $\Delta_2(H) \leq D$, the upper tail of $X = e(H_p)$ satisfies $\exp(-C(\varepsilon)\min\{\mu, \sqrt{\mu}\log(1/p)\}) \leq \mathbb{P}(X \geq (1+\varepsilon)\mu) \leq \exp(-c(\varepsilon)\min\{\mu, \sqrt{\mu}\log(e/p)\})$ with $c(\varepsilon) = b\min\{\varepsilon^3, \varepsilon^{1/2}\}$, $C(\varepsilon) = B\max\{1, \varepsilon^2\}$. Theorem 6 sharpens the $\varepsilon$-dependence: a sub-Gaussian regime $\exp(-ct^2/\mathrm{Var}\,X)$ for small deviations transitions near $t \sim (\mathrm{Var}\,X)^{2/3}$ to a "clustered" regime $\exp(-c\sqrt{t}\log(1/p))$, recovering the large-deviation rate function up to constants over essentially the full parameter range.

## Why it matters here
General background on upper-tail concentration for combinatorial counts in random discrete structures; no direct Einstein Arena problem tie — but the Janson–Ruciński deletion method and the cluster/Lipschitz Chernoff bounds are useful tools whenever the agent needs to bound deviations of polynomial functions of independent Bernoullis (e.g., random discrete sets, hypergraph edge counts, autocorrelation-type sums). Relates to sieve theory and combinatorics problem families.

## Open questions / connections
- Sub-Gaussian lower bounds in the regime $p \in (n^{-2/(k+1/3)}, n^{-1/(k-1)})$ with $t \geq \sqrt{\mathrm{Var}\,X}$ — author conjectures (9)–(10) hold for all $p \in (0, 1-\gamma]$, $t \geq \sqrt{\mathrm{Var}\,X}$.
- Extends Janson–Oleszkiewicz–Ruciński (2002) [22] and Janson–Ruciński (2011) [25] which left a $\log(1/p)$ gap; parallels Chatterjee (2012) and DeMarco–Kahn (2012) breakthroughs for triangle/clique counts.
- Determining precise constants (not just $\Theta$) in the exponent as $n \to \infty$ — see Chatterjee–Varadhan, Lubetzky–Zhao for the $G_{n,p}$ analogue.

## Key terms
upper tail, large deviations, arithmetic progressions, Schur triples, random hypergraphs, Chernoff bound, BK inequality, deletion method, Janson-Ruciński, Harris inequality, Paley-Zygmund, concentration of measure
