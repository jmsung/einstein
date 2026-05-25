---
type: source
kind: paper
title: "What Neural Networks Memorize and Why: Discovering the Long Tail via Influence Estimation"
authors: V. Feldman, Chiyuan Zhang
year: 2020
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2008.03703
source_local: ../raw/2020-feldman-what-neural-networks-memorize.pdf
topic: general-knowledge
cites:
---

# What Neural Networks Memorize and Why: Discovering the Long Tail via Influence Estimation

**Authors:** V. Feldman, Chiyuan Zhang  ·  **Year:** 2020  ·  **Source:** https://arxiv.org/abs/2008.03703

## One-line
Empirically validates the "long tail" theory of memorization by estimating, via subsampled retraining, how much each training example influences the network's accuracy on each test example.

## Key claim
On long-tailed natural image data, label memorization of atypical training examples is *necessary* for near-optimal generalization: memorized examples have higher marginal utility than random examples of equal count (ImageNet: $\sim 32\%$ of examples have $\mathrm{mem} \geq 0.3$ contributing $\sim 3.4\%$ accuracy vs $\sim 2.6\%$ for a random subset), and a substantial number of train–test pairs exist where a *single* memorized training example significantly raises accuracy on a visually-similar test example (1641 such pairs in ImageNet, 1298 with a unique influencer).

## Method
Define $\mathrm{mem}(A,S,i) := \Pr_{h\leftarrow A(S)}[h(x_i)=y_i] - \Pr_{h\leftarrow A(S\setminus i)}[h(x_i)=y_i]$ and analogous $\mathrm{infl}(A,S,i,j)$ for train–test pairs. Replace the infeasible leave-one-out estimator with a *subsampled* version $\mathrm{infl}_m$: train $t$ ($=2000$–$4000$) models on random subsets of size $m=0.7n$, then for each $i$ compare conditional accuracies on subsets that include vs exclude $i$ — yielding all $n$ memorization values and all $n \times n_{\text{test}}$ influence values from the *same* $t$ training runs, with variance $O(1/(pt))$ where $p=\min(m/n,1-m/n)$. Closely related to the Shapley value at $m=n/2$.

## Result
Lemma 2.1: $\mathbb{E}[(\mathrm{infl}_m - \mu_i)^2] \leq e^{-pt/16}/2 + 1/(pt) + 1/((1-p)t)$, so $O(1/\sigma^2)$ training runs suffice. Empirically on CIFAR-100 / ImageNet (ResNet50): memorization is concentrated on atypical / mislabeled / ambiguous examples; removing them hurts accuracy more than removing a random equal-size set; high-influence pairs are visually similar across class; results are stable across ResNet18 / Inception / DenseNet (Jaccard $\geq 0.7$). Training only the last layer on a frozen penultimate representation finds essentially no memorization (38 vs 18,099 examples above $\mathrm{mem} \geq 0.25$) — memorization lives in the *representation*, not the classifier head.

## Why it matters here
General background; no direct arena tie. The agent loop is symbolic/numerical optimization on 23 fixed problems, not statistical learning on long-tailed image data — there is no "training set" whose tail needs memorizing. The only loose analogy is methodological: subsampled leave-one-out is a clean way to attribute outcomes to individual ingredients, which could conceivably be borrowed if we ever want to estimate the marginal contribution of a wiki finding / persona to a solve.

## Open questions / connections
- Cheaper proxy estimators for $\mathrm{infl}_m$ that avoid retraining thousands of models (open at end of paper).
- Mechanistic question: *how* does SGD encode a rare example into the representation layers? — left for future work.
- Extends Feldman 2019 ([Fel19], arXiv:1906.05271) from theoretical generative model to empirical CIFAR-100 / ImageNet evidence; related to Jiang et al. consistency score (concurrent, [JZTM20]) and Koh–Liang influence functions ([KL17]).
- Implication: differential privacy / model compression / shorter training disproportionately harm accuracy on under-represented subpopulations ([BPS19]).

## Key terms
label memorization, subsampled influence, leave-one-out, long-tail distribution, Shapley value, generalization gap, interpolating classifiers, marginal utility, ResNet50, CIFAR-100, ImageNet, Feldman, Zhang, influence functions
