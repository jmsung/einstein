---
type: source
kind: paper
title: Wide Network Learning with Differential Privacy
authors: Huanyu Zhang, Ilya Mironov, Meisam Hejazinia
year: 2021
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2103.01294
source_local: ../raw/2021-zhang-wide-network-learning-differential.pdf
topic: general-knowledge
cites:
---

# Wide Network Learning with Differential Privacy

**Authors:** Huanyu Zhang, Ilya Mironov, Meisam Hejazinia  ·  **Year:** 2021  ·  **Source:** https://arxiv.org/abs/2103.01294

## One-line
Differentially-private empirical risk minimization (ERM) for models with sparse gradients, with application to wide neural networks (embedding layers, word2vec).

## Key claim
For non-convex DP-ERM under a gradient-sparsity assumption, the expected gradient norm scales as $O(\mathrm{poly}(\log p)/n^{1/4})$ rather than $O(\mathrm{poly}(\sqrt{p})/n^{1/4})$ — log instead of polynomial dependence on parameter dimension $p$.

## Method
Two algorithms. (i) For ERM with the assumption that the dataset partitions into $m$ subsets each having $\ell_0$-sparse gradient sum (sparsity $c_1$), apply DP-SGD where each step uses the **NumericSparse** sparse-vector technique to release only the top-$c_1$ coordinates plus Laplace noise, then strong-composition over $T$ iterations. (ii) For wide nets, **Algorithm 3**: clip per-sample gradients ($S_1$), aggregate, run a DP top-$\gamma p$ **selection** (exponential mechanism / sparse vector / Durfee–Rogers), clip again ($S_2$), add Gaussian noise only on the selected coordinates, update.

## Result
**Theorem 2** (non-convex, smooth, $\|\nabla\ell\|_\infty\le c_2$, $\|\nabla\ell\|_2\le G$): $\mathbb{E}\frac{1}{T}\sum_t\|\nabla L(w_t)\|_2^2 = O\!\big(\tfrac{G(c_1 c_2+\sqrt{KD})}{\varepsilon}\cdot(\tfrac{m}{n}+\tfrac{1}{\sqrt{n}})\big)$. Convex version: excess risk $O\!\big(\tfrac{D_w(G+c_1 c_2)}{\varepsilon}(\tfrac{m}{n}+\tfrac{1}{\sqrt{n}})\big)$. **Lemma 7**: for generalized linear models, input $c_1$-sparsity implies gradient $c_1$-sparsity. Empirically on Brown corpus word2vec (1K vocab, 100-dim embeddings, $\varepsilon=30$, $\delta=10^{-5}$), DP-Sparse with exponential-mechanism selection beats DP-SGD in train/test loss, and Secret-Sharer canary-rank histograms remain near-uniform (chi-sq p-values $\ge 0.31$ at $n_c\le 9$).

## Why it matters here
General background; no direct arena tie. None of the 23 Einstein Arena problems involve differential privacy, neural-net training, or empirical risk minimization — this paper's domain (privacy-preserving ML) is orthogonal to sphere packing, autocorrelation, kissing numbers, and the other arena categories.

## Open questions / connections
- Better privacy accountant for the composed selection + Gaussian-noise mechanism (authors note their bound is $\log(T/\delta)$ looser than Rényi DP-SGD; left as open problem).
- Removing the requirement that the dataset partition cleanly into $m$ sparsity-similar subsets — a strong structural assumption.
- Extending beyond GLMs: when does sparse input $\Rightarrow$ sparse gradient hold for deeper architectures past the embedding layer?

## Key terms
differential privacy, DP-SGD, empirical risk minimization, sparse gradients, sparse vector technique, exponential mechanism, Gaussian mechanism, moments accountant, strong composition, word embedding, generalized linear model, Secret Sharer
