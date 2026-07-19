---
type: source
kind: paper
title: "Nature Language Model: Deciphering the Language of Nature for Scientific Discovery"
authors: Yingce Xia, Peiran Jin, Shufang Xie, Liang He, Chuan Cao, Renqian Luo, Guoqing Liu, Yue Wang, Zequn Liu, Yuan Chen, Zekun Guo, Yeqi Bai, Pan Deng, Yaosen Min, Zi‐Ang Lu, Hongxia Hao, Han Yang, Jielan Li, Chang Liu, Jia Zhang, Jian-Bo Zhu, Ke-Ming Wu, Wei Zhang, Kaiyuan Gao, Qizhi Pei, Qian Wang, Xixian Liu, Yanting Li, Houtian Zhu, Yeqing Lu, Mingqian Ma, Zun Wang, Tian Xie, Krzysztof Maziarz, Marwin H. S. Segler, Zhao Yang, Zi-wei Chen, Yu Shi, Shuxin Zheng, Lijun Wu, Chen Hu, Peggy Dai, Tiemin Liu, Haiguang Liu, Tao Qin
year: 2025
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2502.07527
source_local: ../raw/2025-xia-nature-language-model-deciphering.pdf
topic: general-knowledge
cites:
---

# Nature Language Model: Deciphering the Language of Nature for Scientific Discovery

**Authors:** Yingce Xia, Peiran Jin, Shufang Xie, Liang He, Chuan Cao, Renqian Luo, Guoqing Liu, Yue Wang, Zequn Liu, Yuan Chen, Zekun Guo, Yeqi Bai, Pan Deng, Yaosen Min, Zi‐Ang Lu, Hongxia Hao, Han Yang, Jielan Li, Chang Liu, Jia Zhang, Jian-Bo Zhu, Ke-Ming Wu, Wei Zhang, Kaiyuan Gao, Qizhi Pei, Qian Wang, Xixian Liu, Yanting Li, Houtian Zhu, Yeqing Lu, Mingqian Ma, Zun Wang, Tian Xie, Krzysztof Maziarz, Marwin H. S. Segler, Zhao Yang, Zi-wei Chen, Yu Shi, Shuxin Zheng, Lijun Wu, Chen Hu, Peggy Dai, Tiemin Liu, Haiguang Liu, Tao Qin  ·  **Year:** 2025  ·  **Source:** https://arxiv.org/abs/2502.07527

## One-line
A Transformer-decoder foundation model continually pre-trained on 143B tokens of mixed sequence data (SMILES, FASTA proteins/DNA/RNA, materials, text) to handle generation, optimization and prediction across scientific domains under text instructions.

## Key claim
A single sequence-based generalist model (1B / 8B / 8x7B-MoE = 46.7B params) matches or surpasses specialist SOTA on 22 task categories spanning small molecules, proteins, materials, and nucleotides, with monotonic scaling — the 8x7B is best on 18/22, and the 8B beats the 1B everywhere.

## Method
Two-stage continued pre-training on top of Llama 3 8B and Mixtral 8x7B: stage 1 trains only newly added scientific-token embeddings (frozen base) to avoid instability from mismatched random vs trained embeddings; stage 2 jointly trains the full network. Scientific entities are wrapped in special tokens (⟨mol⟩, ⟨protein⟩, ⟨dna⟩, ⟨rna⟩, ⟨material⟩) and cross-domain coupling is built via interleaved literature sequences (BERN2 NER → SMILES/FASTA), parallel text↔entity pairs from PubChem/UniProt/Materials Project, and DNA↔protein pairs from RefSeq via the central dogma. Post-training is SFT on ~5.1M curated instruction-response pairs, with optional RLHF and task-specific finetuning (e.g., retrosynthesis, Matbench).

## Result
Token mix is text 10%, protein 45.3%, RNA 19.1%, DNA 13.8%, cross-domain 8.8%, small-mol 2.9%, material 0.014% (143.8B total). Validation loss drops monotonically with size across all domains, largest gains on text and protein. Demonstrated capabilities include SMILES↔IUPAC translation (correct on PubChem CIDs 172655007/8 where DeepSeek-R1, GPT-4o, GPT-4.5, o3-mini all fail), retrosynthesis with preserved stereochemistry, heme-binding protein design from text or SMILES (Protenix-validated pockets), guide-RNA design for CRISPR, and protein-conditioned RNA/molecule generation. AlpacaEval text quality lags Mixtral baseline.

## Why it matters here
General background; no direct arena tie. NatureLM is a generative bio/chem/materials LLM with no use of LP duality, Cohn–Elkies bounds, equioscillation, packing constructions, or any combinatorial-optimization machinery relevant to the 23 Einstein Arena problems. Its only weak signal for this project is methodological: the two-stage frozen-embedding warmup is a tactic for extending an LLM's vocabulary without destabilizing pretrained weights.

## Open questions / connections
- Could a foundation model trained on optimization traces (configurations, objective curves, gradient histories) be useful to seed Arena optimizers — analogous to NatureLM seeding from SMILES/FASTA?
- The two-stage "freeze base, train new tokens, then jointly train" recipe could apply if we ever tokenize point configurations or LP tableaus into a sequence model.
- No connection to LP/SDP bounds, sphere packing, autocorrelation, kissing numbers, or extremal combinatorics — the wiki should not cite this paper for math-optimization content.

## Key terms
NatureLM, foundation model, Llama 3, Mixtral 8x7B, Mixture-of-Experts, SMILES, FASTA, continued pre-training, two-stage embedding warmup, instruction tuning, cross-domain generation, retrosynthesis, CRISPR guide RNA design, heme-binding protein design, Matbench
