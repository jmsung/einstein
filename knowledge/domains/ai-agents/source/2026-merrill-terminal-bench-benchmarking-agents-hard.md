<!-- synced from knowledge-base — do not edit here; change upstream and re-pull -->
---
type: source
kind: paper
confidentiality: public
visibility: global
primary: ai-agents
domains: [ai-agents]
title: "Terminal-Bench: Benchmarking Agents on Hard, Realistic Tasks in Command Line Interfaces"
authors: [Mike A. Merrill, Alexander G Shaw, Nicholas Carlini, Boxuan Li, Harsh Raj, I. Bercovich, Lin Shi, J. Shin, Thomas Walshe, E. K. Buchanan, Junhong Shen, Guanghao Ye, Hao Lin, Jason Poulos, Maoyu Wang, Marianna Nezhurina, J. Jitsev, Di Lu, O. M. Mastromichalakis, Zhiwei Xu, Zizhao Chen, Yue Liu, Robert Zhang, L. Chen, Anurag Kashyap, Jan-Lucas Uslu, Jeffrey Li, Jianbo Wu, Minghao Yan, Song Bian, Vedang Sharma, Ke Sun, Steven Dillmann, Akshay Anand, Andrew Lanpouthakoun, Bardia Koopah, Changran Hu, E. Guha, Gabriel H. S. Dreiman, Jiacheng Zhu, Karl Krauth, Li Zhong, Niklas Muennighoff, Robert K. Amanfu, Shangyin Tan, Shreyas Pimpalgaonkar, Tushar Aggarwal, Xia Lin, Xin Lan, Xuandong Zhao, Yiqing Liang, Yuanli Wang, Zilong Wang, Changzhi Zhou, David Heineman, Hange Liu, H. Trivedi, John Yang, Junhong Lin, Manish Shetty, Michael Yang, Nabil Omi, Negin Raoof, Shanda Li, Terry Yue Zhuo, Wu Lin, Yiwei Dai, Yuxin Wang, Wenhao Chai, Shang Zhou, Dariush Wahdany, Ziyu She, Jiaming Hu, Zhikang Dong, Yuxuan Zhu, Sasha Cui, Ahson Saiyed, Arinbjörn Kolbeinsson, Jesse Hu, Christopher Rytting, Ryan Marten, Yixin Wang, A. Dimakis, A. Konwinski, Ludwig Schmidt]
year: 2026
source_url: https://arxiv.org/abs/2601.11868
drive_file_id: TODO
text_source: paperclip
ingested_by: agent
---

# Terminal-Bench: Benchmarking Agents on Hard, Realistic Tasks in Command Line Interfaces

**Authors:** Mike A. Merrill, Alexander G Shaw, Nicholas Carlini, Boxuan Li, Harsh Raj, I. Bercovich, Lin Shi, J. Shin, Thomas Walshe, E. K. Buchanan, Junhong Shen, Guanghao Ye, Hao Lin, Jason Poulos, Maoyu Wang, Marianna Nezhurina, J. Jitsev, Di Lu, O. M. Mastromichalakis, Zhiwei Xu, Zizhao Chen, Yue Liu, Robert Zhang, L. Chen, Anurag Kashyap, Jan-Lucas Uslu, Jeffrey Li, Jianbo Wu, Minghao Yan, Song Bian, Vedang Sharma, Ke Sun, Steven Dillmann, Akshay Anand, Andrew Lanpouthakoun, Bardia Koopah, Changran Hu, E. Guha, Gabriel H. S. Dreiman, Jiacheng Zhu, Karl Krauth, Li Zhong, Niklas Muennighoff, Robert K. Amanfu, Shangyin Tan, Shreyas Pimpalgaonkar, Tushar Aggarwal, Xia Lin, Xin Lan, Xuandong Zhao, Yiqing Liang, Yuanli Wang, Zilong Wang, Changzhi Zhou, David Heineman, Hange Liu, H. Trivedi, John Yang, Junhong Lin, Manish Shetty, Michael Yang, Nabil Omi, Negin Raoof, Shanda Li, Terry Yue Zhuo, Wu Lin, Yiwei Dai, Yuxin Wang, Wenhao Chai, Shang Zhou, Dariush Wahdany, Ziyu She, Jiaming Hu, Zhikang Dong, Yuxuan Zhu, Sasha Cui, Ahson Saiyed, Arinbjörn Kolbeinsson, Jesse Hu, Christopher Rytting, Ryan Marten, Yixin Wang, A. Dimakis, A. Konwinski, Ludwig Schmidt  ·  **Year:** 2026  ·  **Source:** https://arxiv.org/abs/2601.11868

## One-line
Introduces Terminal-Bench 2.0, a curated benchmark of 89 hard, realistic command-line tasks (each with a Docker env, instruction, oracle solution, and tests) used to evaluate frontier LLM agents.

## Key claim
Frontier model+agent combinations top out below 65% resolution rate (GPT-5.2 + Codex CLI at 62.9%, Claude Opus 4.5 + Terminus 2 at 57.8%, Gemini 3 Pro + Terminus 2 at 56.9%), while small models score near 3–15%; model selection dominates agent scaffold (e.g., GPT-5.2 vs GPT-5-Nano on Codex CLI = +52 percentage points).

## Method
Crowd-sourced 229 candidate tasks from 93 contributors, filtered to 89 via a multi-stage audit (oracle-solution CI check, contributor checklist, LLM-based mistake finder, ~3 reviewer-hours per task, adversarial exploit agent). Tasks run in Docker via the Harbor harness with sandboxed parallel containers; six agent scaffolds (Claude Code, Codex CLI, Gemini CLI, OpenHands, Mini-SWE-Agent, and a neutral testbed Terminus 2) are paired with 16 frontier/open-weight models across 32,155 trials. Failures are categorized using a MAST-derived 3-class taxonomy (Execution / Coherence / Verification) with an LLM-as-judge (GPT-5 high) achieving 90% agreement with human labels.

## Result
Top 13 leaderboard slots are proprietary models; best open-weight is Kimi K2 Thinking + Terminus 2 at 35.7%. Cost spans ~$1–$100 per full run, with no correlation between turn count or token volume and success. Empirical-vs-human difficulty correlation $r = 0.436$ ($p < 0.001$); 93.3% of human-hard tasks are also empirically hard, but 54.5% of human-medium tasks are empirically hard (models lack creative/adversarial reasoning). Execution errors (disobey-spec, step repetition) dominate on frontier closed models; open models show balanced failures across all three classes. Command-level failures range 9.2%–26.7%; "command not found" (24.1%) and invocation errors (9.6%) are the most common.

## Key terms
LLM agents, command-line interface, Terminal-Bench, Harbor harness, Terminus 2, Docker sandbox, agent scaffold, MAST taxonomy, failure mode analysis, LLM-as-judge, oracle solution, benchmark verification, resolution rate, frontier models
