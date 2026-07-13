<!-- synced from knowledge-base — do not edit here; change upstream and re-pull -->
---
type: source
kind: paper
confidentiality: public
visibility: global
primary: ai-agents
domains: [ai-agents]
title: Nex-N1: Agentic Models Trained via a Unified Ecosystem for Large-Scale Environment Construction
authors: [Nex-AGI Team Yuxuan Cai, Luyao Chen, Qiaoling Chen, Yuyang Ding, Liwen Fan, Wenjie Fu, Yufei Gao, Honglin Guo, Pinxue Guo, Zhenhua Han, Zhengfu He, Hanglei Hu, Kai Hu, Shengjia Hua, Tianyu Huai, Baodai Huang, Lifeng Ji, Zhen Jiang, Zhikai Lei, Bufan Li, Jiahang Lin, Lizhi Lin, Jinxiu Liu, Shichun Liu, Ziming Liu, Yuchen Ni, Pengfang Qian, Yujiong Shen, Qingyu Shi, Wentao Shu, Peng Sun, Y. Suo, Tian Tang, Bo Tian, Guoteng Wang, Junzhe Wang, Peixin Wang, Zhi-Peng Xi, Hang Yan, Jie Yang, Zhixiong Yang, Tianchu Yao, Guangze Ye, Qi Yu, Shuo Zhang, Xinyue Zhang, Yiqi Zhang, Jiarong Zhao, Miao Zheng, Rui Zheng, Enyu Zhou, Jiazheng Zhou, Maosen Zhou, Yuhao Zhou, Tao Gui, Yi Zheng, Xinchi Chen, Jie Zhou, Siyuan Feng, Qin Chen, Liangjun He, Qi Zhang, Xu Huang, Xipeng Qiu]
year: 2025
source_url: https://arxiv.org/abs/2512.04987
drive_file_id: TODO
text_source: paperclip
ingested_by: agent
---

# Nex-N1: Agentic Models Trained via a Unified Ecosystem for Large-Scale Environment Construction

**Authors:** Nex-AGI Team (Yuxuan Cai, Luyao Chen, Qiaoling Chen, Yuyang Ding, et al.; project leads: Tao Gui, Yi Zheng, Xinchi Chen, Jie Zhou, Siyuan Feng, Qin Chen, Liangjun He, Qi Zhang, Xu Huang, Xipeng Qiu)  ·  **Year:** 2025  ·  **Source:** https://arxiv.org/abs/2512.04987

## One-line
A three-part infrastructure (NexAU runtime, NexA4A auto-framework generator, NexGAP data pipeline) that procedurally synthesizes diverse agent environments and trajectories, used to train the Nex-N1 family of agentic LLMs.

## Key claim
Scaling environment *construction* — not just data — via a unified ecosystem (recursive ReAct runtime + LLM-generated multi-agent frameworks + real-MCP grounding) yields agents that beat same-size open-source baselines and approach proprietary frontier models; e.g. DeepSeek-V3.1-Nex-N1 reaches $\tau_2$ 80.2, GAIA2 29.5, SWE-bench Verified 70.6, BFCL v4 65.3, vs DeepSeek-V3.1 base 42.8 / 21.9 / 66.0 / 56.3.

## Method
Three coupled systems: (1) **NexAU**, a recursive ReAct runtime where sub-agents are interchangeable with tools via a declarative YAML schema, supporting MCP, Skills, and GlobalStorage; (2) **NexA4A**, a MetaAgent + FrameworkBuilder + AgentBuilder pipeline that compiles natural-language framework specs into multi-agent hierarchies (1-34 nodes, 1-3 layers); (3) **NexGAP**, which uses curated real MCP tools as capability seeds, an inverse-frequency-weighted Problem Type Tree with persona/difficulty conditioning for query synthesis, supervisor-tool feedback loops (with binary visual judgments + capped repair iterations), and a Quality Assessment Agent that iteratively filters trajectories for truncation, hallucination, and reward hacking.

## Result
Across $\tau_2$-bench, GAIA 2, SWE-bench Verified, Terminal-Bench 2, BaxBench, and BFCL v4, Nex-N1 variants consistently beat their base models and same-size open-source peers; the largest variant surpasses GPT-5 on BFCL tool-use (65.3 vs 61.6). Framework-robustness experiments on a 100-instance SWE-bench Verified subset show stable scores across Terminus-2, Claude Code, and OpenHands (51.2 / 62 / 63.5). Human evaluations on project-development (43 samples) and webpage-creation (45 samples) show Nex-N1 winning or tying >50% of head-to-heads vs major models except Claude-Sonnet-4.5.

## Key terms
agentic scaling, ReAct, sub-agent-as-tool, Model Context Protocol (MCP), declarative YAML agent schema, multi-agent framework synthesis, SWE-bench Verified, $\tau_2$-bench, GAIA 2, BFCL, trajectory quality assessment, reward hacking
