<!-- synced from knowledge-base — do not edit here; change upstream and re-pull -->
---
type: source
kind: paper
confidentiality: public
visibility: global
primary: ai-agents
domains: [ai-agents, ai-ml, sci-stats]
title: Thought Communication in Multiagent Collaboration
authors: [Yujia Zheng, Zhuokai Zhao, Zijian Li, Yaqi Xie, Mingze Gao, Lizhu Zhang, Kun-Ning Zhang]
year: 2025
source_url: https://arxiv.org/abs/2510.20733
drive_file_id: TODO
text_source: paperclip
ingested_by: agent
---

# Thought Communication in Multiagent Collaboration

**Authors:** Yujia Zheng, Zhuokai Zhao, Zijian Li, Yaqi Xie, Mingze Gao, Lizhu Zhang, Kun-Ning Zhang  ·  **Year:** 2025  ·  **Source:** https://arxiv.org/abs/2510.20733

## One-line
Proposes "thought communication" — multi-agent LLMs exchange identified latent thoughts (mind-to-mind) instead of natural-language tokens, with identifiability guarantees for shared and private latent variables.

## Key claim
In a nonparametric latent variable model $H_t = f(Z_t)$ with $\ell_0$ sparsity regularization on the Jacobian $J_{\hat f}$, both **shared** and **private** latent thoughts between any pair of agents, *and* the binary thought-agent incidence structure $B(J_f)$, are identifiable up to permutation — without auxiliary information, weak supervision, or restricted function classes.

## Method
Formalize agent model states as $H_t = f(Z_t)$ for invertible twice-differentiable $f$; recover $\hat Z_t = \hat f^{-1}(H_t)$ via a sparsity-regularized autoencoder (reconstruction loss + $\ell_1$ on $J_{\hat f}$). Proofs use change-of-variable to write $J_{\hat f} = J_f J_{h^{-1}}$, then Hall's marriage theorem on a bipartite graph induced by the nonzero pattern of $J_{h^{-1}}$ to extract a permutation $\pi$, with $\ell_0$ regularization closing the implication to an equivalence. Practical framework THOUGHTCOMM routes each recovered latent dimension to relevant agents via the inferred structure and injects via prefix-tuning adapters.

## Result
Three identifiability theorems (Thm. 1 shared, Thm. 2 private, Thm. 3 structure) under a Jacobian-spanning assumption. Empirically on MATH with Llama-3-8B-Instruct and Qwen-3-1.7B, THOUGHTCOMM remains stable as debate rounds grow 2→6 while Multiagent Finetune degrades; latent dimension gains saturate around 512–1024; performance robust to 3–5 agents.

## Key terms
nonlinear ICA, identifiability, latent variable model, multi-agent LLM, sparsity regularization, Jacobian sparsity, $\ell_0$ regularization, Hall's marriage theorem, disentanglement, prefix tuning, sparse autoencoder, causal representation learning
