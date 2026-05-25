---
type: source
kind: paper
title: DeepSeek-V3.2: Pushing the Frontier of Open Large Language Models
authors: DeepSeek-AI, A. Liu, Aoxue Mei, B. Lin, Bing Xue, Bing-Li Wang, Bin Xu, Bochao Wu, Bowei Zhang, Chaofan Lin, Chen Dong, Chengda Lu, Chenggang Zhao, C. Deng, Chenhao Xu, C. Ruan, Damai Dai, Daya Guo, Dejian Yang, Deli Chen, Erhang Li, Fangqi Zhou, Fangyun Lin, Fucong Dai, Guangbo Hao, Guanting Chen, Guowei Li, H. Zhang, Hanwei Xu, Hao Li, Hao Liang, Haoran Wei, Haowei Zhang, Hao-sheng Luo, Haozhe Ji, Honghui Ding, Hongxuan Tang, Huan Cao, Huazuo Gao, Huixian Qu, Hui Zeng, Jialiang Huang, Jiashi Li, Jiaxin Xu, Jiewen Hu, JingChang Chen, Ji Xiang, Jingyang Yuan, Jing Cheng, Jinhua Zhu, Jun Ran, Junguang Jiang, Junjie Qiu, Junlong Li, Jun-Mei Song, Kai Dong, Kaige Gao, Kang Guan, Kexin Huang, Kexin Zhou, Ke-wei Huang, K. Yu, Lean Wang, Lecong Zhang, Lei Wang, Liang Zhao, Liangsheng Yin, Lihua Guo, Ling-Li Luo, Lin Ma, Litong Wang, Liyue Zhang, M. Di, M. Y. Xu, Mingchuan Zhang, Minghua Zhang, M. Tang, Mingxu Zhou, P. Huang, Peixin Cong, Peiyi Wang, Qiancheng Wang, Qihao Zhu, Qingyang Li, Qinyu Chen, Qiushi Du, Ruiling Xu, Ruiqi Ge, Ruisong Zhang, Ruizhe Pan, Runji Wang, Runqiu Yin, Runxin Xu, Ru Shen, Ruoyu Zhang, S. Liu, Shanghao Lu, Shangyan Zhou, Shanhuang Chen, Shaofei Cai, Shaoyuan Chen, Shengding Hu, Shengyu Liu, Shiqiang Hu, Shirong Ma, Shiyu Wang, Shuiping Yu, Shunfeng Zhou, Shuting Pan, Songyang Zhou, Tao Ni, Tao Yun, Tian Pei, Tian Ye, Tianyuan Yue, Wangding Zeng, Wen Liu, W. Liang, Wenjie Pang, Wenjing Luo, Wenjun Gao, Wentao Zhang, Xi Gao, Xiangwen Wang, Xiaoling Bi, Xiaodong Liu, Xiaohan Wang, Xiaokang Chen, Xiaokang Zhang, X. Nie, Xin Cheng, Xin Liu, Xin Xie, Xingchao Liu, Xingkai Yu, Xingyou Li, Xinyu Yang, Xinyuan Li, Xu Chen, Xuecheng Su, Xuehai Pan, Xuheng Lin, Xu Fu, Y. Q. Wang, Yang Zhang, Yanhong Xu, Yanru Ma, Yao Li, Yao Zhao, Yaofeng Sun, Yaohui Wang, Y. Qian, Yingpu Yu, Yichao Zhang, Yifan Ding, Yifan Shi, Yi Xiong, Ying He, Ying Zhou, Yinmin Zhong, Y. Piao, Yisong Wang, Yixiao Chen, Yixuan Tan, Yixuan Wei, Yiyang Ma, Yiyuan Liu, Yong Yang, Yongqiang Guo, Yongtong Wu, Yu Wu, Yuan Cheng, Y. Ou, Yuanfang Xu, Yuduan Wang, Yue Gong, Yuhan Wu, Yu-Hui Zou, Yukun Li, Yunfan Xiong, Yu-Wei Luo, Yu-mei You, Yuxuan Liu, Yuyang Zhou, Z. F. Wu, Z. Ren, Zehua Zhao, Z. Ren, Zhangli Sha, Zhe Fu, Zhean Xu, Zhenda Xie, Zhen-guo Zhang, Zhewen Hao, Zhibin Gou, Zhicheng Ma, Zhigang Yan, Zhihong Shao, Zhixian Huang, Zhiyu Wu, Zhuoshu Li, Zhuping Zhang, Zian Xu, Zihao Wang, Zihui Gu, Zijia Zhu, Ziling Li, Zipeng Zhang, Ziwei Xie, Ziyi Gao, Zizheng Pan, Z. Yao, B. Feng, Hui Li, J. Cai, J. Ni, Lei Xu, Meng Li, Ning Tian, R. J. Chen, R. Jin, S. Li, Shuang Zhou, T. Sun, X. Q. Li, Xiangyu Jin, Xiaojin Shen, Xiaosha Chen, Xinnan Song, Xinyi Zhou, Y. X. Zhu, Yanping Huang, Yao Li, Yi Zheng, Yuchen Zhu, Yunxiang Ma, Zhen Huang, Zhipeng Xu, Zhongyu Zhang, Dong-Li Ji, Jian Liang, Jianzhong Guo, Jin Chen, Leyi Xia, Miaojun Wang, Mingming Li, Peng Zhang, Ruyi Chen, Shangmian Sun, Shao-Kang Wu, Sheng-Ying Ye, T.Wang, W. Xiao, Wei An, Xianzu Wang, Xiaowen Sun, Xiaoxiang Wang, Ying Tang, Y. Zha, Ze-Na Zhang, Zhenghua Ju, Zhen Zhang, Z. Qu
year: 2025
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2512.02556
source_local: ../raw/2025-deepseekai-deepseek-v3-pushing-frontier-open.pdf
topic: general-knowledge
cites:
---

# DeepSeek-V3.2: Pushing the Frontier of Open Large Language Models

**Authors:** DeepSeek-AI et al.  ·  **Year:** 2025  ·  **Source:** https://arxiv.org/abs/2512.02556

## One-line
An open-source LLM combining a sparse-attention architecture with large-scale RL post-training, reaching IMO/IOI gold-medal performance in a high-compute variant.

## Key claim
DeepSeek-V3.2 (with DSA sparse attention + scaled GRPO RL) matches GPT-5 on reasoning benchmarks; the Speciale variant achieves gold medals at IMO 2025 (35/42), CMO 2025 (102/126), IOI 2025 (492/600), and ICPC WF 2025 (10/12, 2nd place), with Codeforces rating 2701.

## Method
**DeepSeek Sparse Attention (DSA):** a lightning indexer (FP8 ReLU heads) computes scores $I_{t,s} = \sum_{j=1}^{H_I} w_{t,j}^I \cdot \mathrm{ReLU}(q_{t,j}^I \cdot k_s^I)$ to select top-$k$ key-value entries per query, reducing core attention from $O(L^2)$ to $O(Lk)$; instantiated under MLA's MQA mode. Continued pretraining uses a dense warm-up (KL-align indexer to attention distribution) then sparse training (943.7B tokens, $k{=}2048$). Post-training uses **scaled GRPO** with four stabilizers: unbiased K3 KL estimator, off-policy sequence masking (drop negative-advantage sequences when policy KL exceeds threshold $\delta$), Keep Routing (preserve MoE expert paths between inference/training), and Keep Sampling Mask (preserve top-p/top-k truncation across policies). Agentic capability comes from a synthesis pipeline generating 1,800+ environments and 85,000+ prompts.

## Result
On reasoning: AIME 2025 93.1 (Speciale 96.0), HMMT Feb 2025 92.5 (Speciale 99.2), IMOAnswerBench 78.3 (Speciale 84.5), HLE 25.1 (Speciale 30.6). On agentic: SWE-Verified 73.1, Terminal Bench 2.0 46.4, BrowseComp 67.6 with context management. DSA cuts long-context inference cost 3–6× vs DeepSeek-V3.1-Terminus at 128K. Post-training compute exceeds 10% of pretraining cost — a key scaling lever. Synthetic agentic data ablation: RL on synthetic-only data lifts Tau2Bench / MCP-Mark / MCP-Universe substantially over SFT baseline, proving generalization.

## Why it matters here
General background; no direct arena tie. The architectural ideas (sparse top-$k$ attention, GRPO stabilization tricks) and the test-time context-management strategies (Summary / Discard-75% / Discard-all) are potentially relevant if the einstein agent ever ingests long-trajectory tool-use logs or scales RL-style self-improvement, but the paper does not address math-optimization problems of the kind Einstein Arena targets (sphere packing, Sidon sets, etc.).

## Open questions / connections
- Token efficiency gap vs Gemini-3.0-Pro: how to compress reasoning chains without losing accuracy on proof-style problems?
- Can the synthetic-task pipeline be adapted to generate verifiable optimization problems (vs verifiable software/search tasks)?
- Optimal serial-vs-parallel test-time compute scaling (Summary vs Parallel-fewest-step) — left as future work.
- Relation to Native Sparse Attention (Yuan et al. 2025) — DSA appears to be a refinement specifically for MLA.

## Key terms
DeepSeek Sparse Attention, DSA, lightning indexer, top-k attention, MLA, MQA, GRPO, K3 KL estimator, off-policy sequence masking, Keep Routing, MoE, agentic task synthesis, IMO 2025, IOI 2025, Codeforces, context management, long-context reasoning
