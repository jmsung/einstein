---
type: source
kind: paper
title: "The Latent Space: Foundation, Evolution, Mechanism, Ability, and Outlook"
authors: Xinlei Yu, Zhangquan Chen, Yongbo He, Tianyu Fu, Cheng Yang, Chengming Xu, Yue Ma, Xiaobin Hu, Zhe Cao, Jie Xu, Guibin Zhang, Jiale Tao, Jiayi Zhang, Siyuan Ma, Kaituo Feng, Haojie Huang, Youxing Li, Rong Chen, Huacan Wang, Chenglin Wu, Z.Y. Su, Xiaogang Xu, Kelu Yao, Kun Wang, Chen Gao, Yue Liao, Ruqi Huang, Tao Jin, Cheng Tan, Jiang-She Zhang, Wenqi Ren, Yanwei Fu, Yong Liu, Yu Wang, Xiangyu Yue, Yu-Gang Jiang, Shuicheng Yan
year: 2026
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2604.02029
source_local: ../raw/2026-yu-latent-space-foundation-evolution.pdf
topic: general-knowledge
cites:
---

# arXiv:2604.02029v1[cs.AI]2Apr2026

![image 1](<2026-yu-latent-space-foundation-evolution_images/imageFile1.png>)

## The Latent Space: Foundation, Evolution, Mechanism, Ability, and Outlook

Xinlei Yu∗,⋆, Zhangquan Chen∗, Yongbo He∗, Tianyu Fu∗, Cheng Yang∗, Chengming Xu∗, Yue Ma∗, Xiaobin Hu∗,†, Zhe Cao, Jie Xu, Guibin Zhang, Jiale Tao, Jiayi Zhang, Siyuan Ma, Kaituo Feng, Haojie Huang, Youxing Li, Ronghao Chen, Huacan Wang, Chenglin Wu, Zikun Su, Xiaogang Xu, Kelu Yao, Kun Wang, Chen Gao, Yue Liao, Ruqi Huang, Tao Jin, Zhucun Xue, Cheng Tan†, Jiangning Zhang†, Wenqi Ren, Yanwei Fu, Yong Liu, Yu Wang, Xiangyu Yue†, Yu-Gang Jiang†, Shuicheng Yan†

∗ Core Contributors † Core Supervisors ⋆ Organizer

National University of Singapore, Fudan University, Tsinghua University, Zhejiang University, Shanghai Artificial Intelligence Laboratory, Renmin University of China, The Chinese University of Hong Kong, The Hong Kong University of Science and Technology, DeepWisdom, Nanjing University, Shanghai Jiatong University, Nanyang Technological University, Tencent Hunyuan, QuantaAlpha, Beijing University of Posts and Telecommunications, Zhejiang Lab, University of Chinese Academy of Sciences, Hong Kong University of Science and Technology (Guangzhou), Sun Yat-sen University

https://github.com/YU-deep/Awesome-Latent-Space

Latent space is rapidly emerging as a native substrate for language-based models. While modern systems are still commonly understood through explicit token-level generation, an increasing body of work shows that many critical internal processes are more naturally carried out in continuous latent space than in human-readable verbal traces. This shift is driven by the structural limitations of explicit-space computation, including linguistic redundancy, discretization bottlenecks, sequential inefficiency, and semantic loss. As a result, research on latent space has expanded from early latent reasoning into a broader landscape spanning planning, modeling, perception, memory, collaboration, and embodiment. However, the literature remains fragmented across mechanisms, modalities, and tasks, lacking a unified perspective on how latent space is defined, classified, and studied.

This survey aims to provide a unified and up-to-date landscape of latent space in language-based models. We organize the survey into five sequential perspectives: Foundation, Evolution, Mechanism, Ability, and Outlook. We begin by delineating the scope of latent space, distinguishing it from explicit or verbal space and from the latent spaces commonly studied in generative visual models. We then trace the field’s evolution from early exploratory efforts to the current large-scale expansion. To organize the technical landscape, we examine existing work through the complementary lenses of mechanism and ability. From the perspective of Mechanism, we identify four major lines of development: Architecture, Representation, Computation, and Optimization. From the perspective of Ability, we show how latent space supports a broad capability spectrum spanning Reasoning, Planning, Modeling, Perception, Memory, Collaboration, and Embodiment. Beyond consolidation, we discuss the key open challenges, and outline promising directions for future research. We hope this survey serves not only as a reference for existing work, but also as a foundation for understanding latent space as a general computational and systems paradigm for next-generation intelligence.

We will continue to update this paper and its associated GitHub repository, and we warmly welcome contributions from the community. Should you identify any related work that has not been included, please feel free to notify us via Github or email: xinleiyu88@gmail.com, czq23@mails.tsinghua.edu.cn, ben0xiaobin0hu1@nus.edu.sg.

Contents

- 1 Introduction 3
- 2 Foundation: What is Latent Space? 5

- 2.1 Concept . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5
- 2.2 Comparison with Explicit Space . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6

- 2.2.1 Representational Properties . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6
- 2.2.2 Functional Capabilities . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7


- 2.3 Comparison with Generative Visual Models . . . . . . . . . . . . . . . . . . . . . . . . . . . . 8


- 3 Evolution: How Did Latent Space Develop? 9

- 3.1 Prototype . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9
- 3.2 Formation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 10
- 3.3 Expansion . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 11
- 3.4 Outbreak . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 12


- 4 Mechanism: How Does Latent Space Work? 13

- 4.1 Architecture . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 15

- 4.1.1 Backbone . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 15
- 4.1.2 Component . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 16
- 4.1.3 Auxiliary Model . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 19


- 4.2 Representation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 20

- 4.2.1 Internal . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 21
- 4.2.2 External . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 24
- 4.2.3 Learnable . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 25
- 4.2.4 Hybrid . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 26


- 4.3 Computation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 27

- 4.3.1 Compressed . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 27
- 4.3.2 Expanded . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 29
- 4.3.3 Adaptive . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 30
- 4.3.4 Interleaved . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 32


- 4.4 Optimization . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 33


- 4.4.1 Pre-training . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 33
- 4.4.2 Post-training . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 34
- 4.4.3 Inference . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 36


- 5 Ability: What Does Latent Space Enable? 37

- 5.1 Reasoning . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 37
- 5.2 Planning . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 39
- 5.3 Modeling . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 40
- 5.4 Perception . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 41
- 5.5 Memory . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 42
- 5.6 Collaboration . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 42
- 5.7 Embodiment . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 43


- 6 Outlook: What is Next? 44

- 6.1 Perspective . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 45
- 6.2 Challenge . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 46
- 6.3 Future . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 46


- 7 Conclusion 48


![image 2](<2026-yu-latent-space-foundation-evolution_images/imageFile2.png>)

![image 3](<2026-yu-latent-space-foundation-evolution_images/imageFile3.png>)

![image 4](<2026-yu-latent-space-foundation-evolution_images/imageFile4.png>)

![image 5](<2026-yu-latent-space-foundation-evolution_images/imageFile5.png>)

![image 6](<2026-yu-latent-space-foundation-evolution_images/imageFile6.png>)

![image 7](<2026-yu-latent-space-foundation-evolution_images/imageFile7.png>)

![image 8](<2026-yu-latent-space-foundation-evolution_images/imageFile8.png>)

Reasoning Planning Modeling Perception Memory Collaboration Embodiment

![image 9](<2026-yu-latent-space-foundation-evolution_images/imageFile9.png>)

![image 10](<2026-yu-latent-space-foundation-evolution_images/imageFile10.png>)

![image 11](<2026-yu-latent-space-foundation-evolution_images/imageFile11.png>)

![image 12](<2026-yu-latent-space-foundation-evolution_images/imageFile12.png>)

CoCoMix

IMM

Heima

AURORA

![image 13](<2026-yu-latent-space-foundation-evolution_images/imageFile13.png>)

UniVLA ThinkAct

![image 14](<2026-yu-latent-space-foundation-evolution_images/imageFile14.png>)

LCR-SER

ArchitectureRepresentationComputationOptimization

PHD-Tran.

![image 15](<2026-yu-latent-space-foundation-evolution_images/imageFile15.png>)

![image 16](<2026-yu-latent-space-foundation-evolution_images/imageFile16.png>)

![image 17](<2026-yu-latent-space-foundation-evolution_images/imageFile17.png>)

![image 18](<2026-yu-latent-space-foundation-evolution_images/imageFile18.png>)

MAS4TS

![image 19](<2026-yu-latent-space-foundation-evolution_images/imageFile19.png>)

Huginn

AlignVLM

G-MemLLM

![image 20](<2026-yu-latent-space-foundation-evolution_images/imageFile20.png>)

![image 21](<2026-yu-latent-space-foundation-evolution_images/imageFile21.png>)

PILOT ATP-Latent

DLCM

![image 22](<2026-yu-latent-space-foundation-evolution_images/imageFile22.png>)

![image 23](<2026-yu-latent-space-foundation-evolution_images/imageFile23.png>)

![image 24](<2026-yu-latent-space-foundation-evolution_images/imageFile24.png>)

![image 25](<2026-yu-latent-space-foundation-evolution_images/imageFile25.png>)

Looped Trans.

LaViT

CoMEM CoMEM-Agent PolarMem

![image 26](<2026-yu-latent-space-foundation-evolution_images/imageFile26.png>)

KVCA

![image 27](<2026-yu-latent-space-foundation-evolution_images/imageFile27.png>)

![image 28](<2026-yu-latent-space-foundation-evolution_images/imageFile28.png>)

OccVLA

![image 29](<2026-yu-latent-space-foundation-evolution_images/imageFile29.png>)

![image 30](<2026-yu-latent-space-foundation-evolution_images/imageFile30.png>)

Dreamer

![image 31](<2026-yu-latent-space-foundation-evolution_images/imageFile31.png>)

![image 32](<2026-yu-latent-space-foundation-evolution_images/imageFile32.png>)

![image 33](<2026-yu-latent-space-foundation-evolution_images/imageFile33.png>)

PonderLM-2

VL-JEPA HIVE

![image 34](<2026-yu-latent-space-foundation-evolution_images/imageFile34.png>)

Wormhole

![image 35](<2026-yu-latent-space-foundation-evolution_images/imageFile35.png>)

![image 36](<2026-yu-latent-space-foundation-evolution_images/imageFile36.png>)

LCDrive

CoLT

![image 37](<2026-yu-latent-space-foundation-evolution_images/imageFile37.png>)

![image 38](<2026-yu-latent-space-foundation-evolution_images/imageFile38.png>)

Ouro

LoopFormer

![image 39](<2026-yu-latent-space-foundation-evolution_images/imageFile39.png>)

![image 40](<2026-yu-latent-space-foundation-evolution_images/imageFile40.png>)

###### ...

...

...

...

...

...

...

![image 41](<2026-yu-latent-space-foundation-evolution_images/imageFile41.png>)

![image 42](<2026-yu-latent-space-foundation-evolution_images/imageFile42.png>)

![image 43](<2026-yu-latent-space-foundation-evolution_images/imageFile43.png>)

![image 44](<2026-yu-latent-space-foundation-evolution_images/imageFile44.png>)

C2C

LatBot VITA

HCoT

CGC-VTD

![image 45](<2026-yu-latent-space-foundation-evolution_images/imageFile45.png>)

![image 46](<2026-yu-latent-space-foundation-evolution_images/imageFile46.png>)

KAVA SALS CLaRa

LFJ

![image 47](<2026-yu-latent-space-foundation-evolution_images/imageFile47.png>)

![image 48](<2026-yu-latent-space-foundation-evolution_images/imageFile48.png>)

CTRLS

![image 49](<2026-yu-latent-space-foundation-evolution_images/imageFile49.png>)

ThoughtComm Interlat LatentMas

![image 50](<2026-yu-latent-space-foundation-evolution_images/imageFile50.png>)

![image 51](<2026-yu-latent-space-foundation-evolution_images/imageFile51.png>)

COCONUT

3DThinker CoVT

![image 52](<2026-yu-latent-space-foundation-evolution_images/imageFile52.png>)

LatentGuard

![image 53](<2026-yu-latent-space-foundation-evolution_images/imageFile53.png>)

![image 54](<2026-yu-latent-space-foundation-evolution_images/imageFile54.png>)

![image 55](<2026-yu-latent-space-foundation-evolution_images/imageFile55.png>)

![image 56](<2026-yu-latent-space-foundation-evolution_images/imageFile56.png>)

![image 57](<2026-yu-latent-space-foundation-evolution_images/imageFile57.png>)

![image 58](<2026-yu-latent-space-foundation-evolution_images/imageFile58.png>)

SoftCoT

Motus LangForce

![image 59](<2026-yu-latent-space-foundation-evolution_images/imageFile59.png>)

iCLP

![image 60](<2026-yu-latent-space-foundation-evolution_images/imageFile60.png>)

![image 61](<2026-yu-latent-space-foundation-evolution_images/imageFile61.png>)

LatentBreak

![image 62](<2026-yu-latent-space-foundation-evolution_images/imageFile62.png>)

![image 63](<2026-yu-latent-space-foundation-evolution_images/imageFile63.png>)

![image 64](<2026-yu-latent-space-foundation-evolution_images/imageFile64.png>)

![image 65](<2026-yu-latent-space-foundation-evolution_images/imageFile65.png>)

Soft Thinking

LRP

![image 66](<2026-yu-latent-space-foundation-evolution_images/imageFile66.png>)

LaSER

![image 67](<2026-yu-latent-space-foundation-evolution_images/imageFile67.png>)

![image 68](<2026-yu-latent-space-foundation-evolution_images/imageFile68.png>)

![image 69](<2026-yu-latent-space-foundation-evolution_images/imageFile69.png>)

Primitives

DeltaKV

UniCog

![image 70](<2026-yu-latent-space-foundation-evolution_images/imageFile70.png>)

![image 71](<2026-yu-latent-space-foundation-evolution_images/imageFile71.png>)

![image 72](<2026-yu-latent-space-foundation-evolution_images/imageFile72.png>)

SIM-CoT

LatentLens

ColaVLA

...

...

...

...

...

...

...

![image 73](<2026-yu-latent-space-foundation-evolution_images/imageFile73.png>)

![image 74](<2026-yu-latent-space-foundation-evolution_images/imageFile74.png>)

![image 75](<2026-yu-latent-space-foundation-evolution_images/imageFile75.png>)

LARES

LVR LS

CCoT Assorted

![image 76](<2026-yu-latent-space-foundation-evolution_images/imageFile76.png>)

![image 77](<2026-yu-latent-space-foundation-evolution_images/imageFile77.png>)

PRE

LatentVLA RD-VLA Future-VLA LaST-VLA

![image 78](<2026-yu-latent-space-foundation-evolution_images/imageFile78.png>)

MemGen

HYP1/2

![image 79](<2026-yu-latent-space-foundation-evolution_images/imageFile79.png>)

![image 80](<2026-yu-latent-space-foundation-evolution_images/imageFile80.png>)

![image 81](<2026-yu-latent-space-foundation-evolution_images/imageFile81.png>)

![image 82](<2026-yu-latent-space-foundation-evolution_images/imageFile82.png>)

FR-Ponder

![image 83](<2026-yu-latent-space-foundation-evolution_images/imageFile83.png>)

![image 84](<2026-yu-latent-space-foundation-evolution_images/imageFile84.png>)

SpiralFormer PonderLM-3 AdaPonderLM

![image 85](<2026-yu-latent-space-foundation-evolution_images/imageFile85.png>)

![image 86](<2026-yu-latent-space-foundation-evolution_images/imageFile86.png>)

![image 87](<2026-yu-latent-space-foundation-evolution_images/imageFile87.png>)

![image 88](<2026-yu-latent-space-foundation-evolution_images/imageFile88.png>)

Latent

DMLR

CODI

VisMem

L2-VMAS

![image 89](<2026-yu-latent-space-foundation-evolution_images/imageFile89.png>)

![image 90](<2026-yu-latent-space-foundation-evolution_images/imageFile90.png>)

![image 91](<2026-yu-latent-space-foundation-evolution_images/imageFile91.png>)

![image 92](<2026-yu-latent-space-foundation-evolution_images/imageFile92.png>)

![image 93](<2026-yu-latent-space-foundation-evolution_images/imageFile93.png>)

![image 94](<2026-yu-latent-space-foundation-evolution_images/imageFile94.png>)

![image 95](<2026-yu-latent-space-foundation-evolution_images/imageFile95.png>)

I2B-LPO

LIVR

CoLaR

![image 96](<2026-yu-latent-space-foundation-evolution_images/imageFile96.png>)

![image 97](<2026-yu-latent-space-foundation-evolution_images/imageFile97.png>)

FlashMem

LatentMem

![image 98](<2026-yu-latent-space-foundation-evolution_images/imageFile98.png>)

![image 99](<2026-yu-latent-space-foundation-evolution_images/imageFile99.png>)

![image 100](<2026-yu-latent-space-foundation-evolution_images/imageFile100.png>)

![image 101](<2026-yu-latent-space-foundation-evolution_images/imageFile101.png>)

![image 102](<2026-yu-latent-space-foundation-evolution_images/imageFile102.png>)

PLaT

Laser

COT2

...

...

...

...

...

...

...

![image 103](<2026-yu-latent-space-foundation-evolution_images/imageFile103.png>)

![image 104](<2026-yu-latent-space-foundation-evolution_images/imageFile104.png>)

![image 105](<2026-yu-latent-space-foundation-evolution_images/imageFile105.png>)

![image 106](<2026-yu-latent-space-foundation-evolution_images/imageFile106.png>)

![image 107](<2026-yu-latent-space-foundation-evolution_images/imageFile107.png>)

LaTRO

LatentSeek HRPO

LF-Steering

VTI

LAPA

![image 108](<2026-yu-latent-space-foundation-evolution_images/imageFile108.png>)

![image 109](<2026-yu-latent-space-foundation-evolution_images/imageFile109.png>)

![image 110](<2026-yu-latent-space-foundation-evolution_images/imageFile110.png>)

![image 111](<2026-yu-latent-space-foundation-evolution_images/imageFile111.png>)

![image 112](<2026-yu-latent-space-foundation-evolution_images/imageFile112.png>)

BoLT

LatentPrompt

Mirage

ATE

LatentEvolve

![image 113](<2026-yu-latent-space-foundation-evolution_images/imageFile113.png>)

![image 114](<2026-yu-latent-space-foundation-evolution_images/imageFile114.png>)

![image 115](<2026-yu-latent-space-foundation-evolution_images/imageFile115.png>)

![image 116](<2026-yu-latent-space-foundation-evolution_images/imageFile116.png>)

![image 117](<2026-yu-latent-space-foundation-evolution_images/imageFile117.png>)

![image 118](<2026-yu-latent-space-foundation-evolution_images/imageFile118.png>)

SoftCoT++

LTO LTPO SofT-GRPO

GANPO

LaCoT VLPO

SRPO GLaD

![image 119](<2026-yu-latent-space-foundation-evolution_images/imageFile119.png>)

![image 120](<2026-yu-latent-space-foundation-evolution_images/imageFile120.png>)

NextMem

![image 121](<2026-yu-latent-space-foundation-evolution_images/imageFile121.png>)

![image 122](<2026-yu-latent-space-foundation-evolution_images/imageFile122.png>)

![image 123](<2026-yu-latent-space-foundation-evolution_images/imageFile123.png>)

![image 124](<2026-yu-latent-space-foundation-evolution_images/imageFile124.png>)

![image 125](<2026-yu-latent-space-foundation-evolution_images/imageFile125.png>)

LatentTTS

ConceptLM

![image 126](<2026-yu-latent-space-foundation-evolution_images/imageFile126.png>)

![image 127](<2026-yu-latent-space-foundation-evolution_images/imageFile127.png>)

![image 128](<2026-yu-latent-space-foundation-evolution_images/imageFile128.png>)

![image 129](<2026-yu-latent-space-foundation-evolution_images/imageFile129.png>)

Latent-SFT

MaD-Mix

CogSense

CLAP

![image 130](<2026-yu-latent-space-foundation-evolution_images/imageFile130.png>)

...

...

...

...

...

...

...

- Figure 1 Overview of the latent space methods classified by two axes: four main Mechanisms (Section 4) and seven key Abilities (Section 5). Within our classification system, a single method may be affiliated with one or more mechanisms and capabilities. For the visualization in this figure, we adopt the most appropriate classification for each method; a comprehensive elaboration of these categories will be presented in the main text.


- 1 Introduction


Recent advances in language-based models, including Large Language Models (LLMs), Vision-Language Models (VLMs), Vision-Language-Action models (VLAs), and agentic systems built on language backbones, are still commonly understood through explicit token-level generation, where inputs, outputs, and even intermediate reasoning are expressed in human-readable form [202, 219, 254]. Yet this token-centric framing is increasingly insufficient [11, 58, 186]. Because computation in such models fundamentally unfolds through continuous activations, latent space is increasingly being reconceived not as a hidden implementation detail, but as a machine-native substrate, such as reasoning [58, 243, 295], perception [11, 137], memory [264, 273], communication [290, 300], and action [69, 142]. This shift is driven in part by the structural limitations of explicit space, its redundancy, discretization bottleneck, sequential decoding cost, and potential loss of fine-grained information, especially in complex, multimodal, or long-horizon settings. By contrast, latent-space computation offers a more continuous, compact, and expressive medium that can support higher-fidelity representations and more flexible allocation of computation.

Research has therefore moved far beyond the initial framing of latent space as latent reasoning alone.What began as an attempt to internalize chain-of-thought into continuous states has rapidly expanded into a broader

continuous & flexible

#### Contents

efficient

![image 131](<2026-yu-latent-space-foundation-evolution_images/imageFile131.png>)

Outbreak

(2025.12-Future)

Foundation

![image 132](<2026-yu-latent-space-foundation-evolution_images/imageFile132.png>)

![image 133](<2026-yu-latent-space-foundation-evolution_images/imageFile133.png>)

- (Section 2) Evolution

- (Section 3)

Mechanism

- (Section 4) Ability

- (Section 5) Outlook

- (Section 6)


hinenative

hfidelity

hig

![image 134](<2026-yu-latent-space-foundation-evolution_images/imageFile134.png>)

Expansion

mac

![image 135](<2026-yu-latent-space-foundation-evolution_images/imageFile135.png>)

![image 136](<2026-yu-latent-space-foundation-evolution_images/imageFile136.png>)

(2025.8-2025.11)

![image 137](<2026-yu-latent-space-foundation-evolution_images/imageFile137.png>)

generalization

![image 138](<2026-yu-latent-space-foundation-evolution_images/imageFile138.png>)

opera bility

Formation

![image 139](<2026-yu-latent-space-foundation-evolution_images/imageFile139.png>)

![image 140](<2026-yu-latent-space-foundation-evolution_images/imageFile140.png>)

(2025.4-2025.7)

![image 141](<2026-yu-latent-space-foundation-evolution_images/imageFile141.png>)

![image 142](<2026-yu-latent-space-foundation-evolution_images/imageFile142.png>)

![image 143](<2026-yu-latent-space-foundation-evolution_images/imageFile143.png>)

expressiveness

Prototype

scalability

(Previous-2025.3)

Foundation: What is it?

Evolution: How it developed?

![image 144](<2026-yu-latent-space-foundation-evolution_images/imageFile144.png>)

![image 145](<2026-yu-latent-space-foundation-evolution_images/imageFile145.png>)

Reasoning

Backbone Component

![image 146](<2026-yu-latent-space-foundation-evolution_images/imageFile146.png>)

Auxiliary Model

![image 147](<2026-yu-latent-space-foundation-evolution_images/imageFile147.png>)

Architecture

Planning

Perspective

![image 148](<2026-yu-latent-space-foundation-evolution_images/imageFile148.png>)

![image 149](<2026-yu-latent-space-foundation-evolution_images/imageFile149.png>)

Internal External

![image 150](<2026-yu-latent-space-foundation-evolution_images/imageFile150.png>)

Modeling

Learnable Hybrid

Representation

![image 151](<2026-yu-latent-space-foundation-evolution_images/imageFile151.png>)

Perception

![image 152](<2026-yu-latent-space-foundation-evolution_images/imageFile152.png>)

![image 153](<2026-yu-latent-space-foundation-evolution_images/imageFile153.png>)

![image 154](<2026-yu-latent-space-foundation-evolution_images/imageFile154.png>)

![image 155](<2026-yu-latent-space-foundation-evolution_images/imageFile155.png>)

Compressed Expanded

![image 156](<2026-yu-latent-space-foundation-evolution_images/imageFile156.png>)

Memory

Challenge

Adaptive Interleaved

Computation

![image 157](<2026-yu-latent-space-foundation-evolution_images/imageFile157.png>)

Collaboration

![image 158](<2026-yu-latent-space-foundation-evolution_images/imageFile158.png>)

Pretraining

Posttraining

![image 159](<2026-yu-latent-space-foundation-evolution_images/imageFile159.png>)

![image 160](<2026-yu-latent-space-foundation-evolution_images/imageFile160.png>)

Future

Embodiment

Optimization

Inference-time

Mechanism: How it works?

Ability: What it enables?

Outlook: What is next?

- Figure 2 Outline of the survey, including five sections and sequential questions: Foundation: What is Latent Space? (Section 2), Evolution: How Did Latent Space Develop? (Section 3), Mechanism: How Does Latent Space Work? (Section 4), Ability: What Does Latent Space Enable? (Section 5), and Outlook: What is Next? (Section 6)


systems paradigm spanning new modalities, new interaction settings, and new design choices [27, 99, 297]. However, this growth has also fragmented the literature in at least three ways: by application object, e.g., latent reasoning, visual understanding, and embodied action; by mechanism, e.g., architecture design, representation choice, computation pattern, and optimization strategy; and by scenario, spanning text, vision, multi-agent systems, and embodied environments. Existing reviews mainly focus on latent reasoning or implicit reasoning as a reasoning-specific phenomenon. What remains missing is a unified perspective that treats latent space as a broader computational and systems paradigm across modalities, paradigms, mechanisms, and capabilities.

To address this gap, we organize the survey around five sequential questions that move from conceptual grounding to future outlook, as illustrated in Figure 2: What is latent space? How did it develop? How does it work? What does it enable? What is next? These questions define the macro-level narrative of the paper: Foundation (Section 2) delineates the concept of latent space and clarifies its relation to explicit space

and to latent space in generative visual models; Evolution (Section 3) traces how the field progressed from prototype exploration to rapid outbreak; Mechanism (Section 4) explains how latent space is instantiated and operationalized; Ability (Section 5) examines what latent computation enables across downstream capabilities; and Outlook (Section 6) synthesizes open challenges and future directions. This five-question narrative is intentionally sequential. This organization allows us to preserve a clear narrative while also comparing diverse methods through shared principles and capability outcomes, rather than through task-specific labels alone.

Within this sequential narrative, our technical synthesis is anchored by a two-dimensional taxonomy shown in Figure 1. The first axis, Mechanism, asks how latent space is built and used, and covers four major lines: Architecture, Representation, Computation, and Optimization. The second axis, Ability, asks what latent space enables, and covers seven major capability domains: Reasoning, Planning, Modeling, Perception, Memory, Collaboration, and Embodiment. This design lets us preserve a clear survey-level storyline while also comparing diverse methods through shared design principles and shared capability outcomes, rather than through task-specific labels alone.

Contributions

- • We clarify the conceptual scope of latent space in language-based models, distinguishing it from explicit or verbal space and from the latent spaces commonly studied in generative visual models.
- • We provide a unified review of how latent space has evolved from early latent reasoning into a broader multimodal and systems-level research paradigm.
- • We introduce a two-dimensional taxonomy across Mechanism and Ability, offering a common framework for organizing otherwise fragmented methods and applications.
- • We provide a comprehensive collection of resources, including illustrative figures, structured tables, accessible links, and repositories, to facilitate further research and community engagement.


###### 2 Foundation: What is Latent Space?

As an emerging paradigm, the exploration of the latent space within language models has exhibited immense potential and vast room for further development. Accordingly, this section provides a preliminary elaboration covering its formal definition and comparisons with existing paradigms.

- 2.1 Concept


In language-based models, i.e., classic autoregressive models, encompassing LLMs, VLMs, VLAs, and derivative systems with language backbone, the entire operational process unfolds explicitly within the explicit space, or the verbal space [202]. The most immediate and externally observable domain is: the discrete space of linguistic symbols in which inputs and outputs are expressed. Formally, this space is defined by a vocabulary that specifies the language model’s next-token predictions. In this space, language is represented as overt verbalized units, i.e., subword-level tokens [168], that are directly interpretable by humans. The training objective of a language model is typically formulated in this explicit space, since the model learns to assign probabilities to symbol sequences and to predict the next token given a textual prefix.

However, a language-based model does not operate solely on discrete symbols. To compute over language, it first maps tokens into internal continuous representations and transforms them through multiple layers of nonlinear computation. This gives rise to what is commonly called the latent space: the continuous, learned representational space in which the model encodes and manipulates information that is not explicitly verbalized at the token level. More precisely, the latent space of a language model can be understood as the family of hidden-state spaces, within which contextual, semantic, syntactic, and relational features of an input are jointly represented in this space. A token sequence in the explicit space is thus mapped to a trajectory of latent space, and these latent states are subsequently projected back into the verbal space to yield a probability distribution over possible next tokens. Furthermore, this latent space could be expanded into a

discrete & symbolic

continuous & flexible

Representational Properties

inefficient

efficient

![image 161](<2026-yu-latent-space-foundation-evolution_images/imageFile161.png>)

![image 162](<2026-yu-latent-space-foundation-evolution_images/imageFile162.png>)

![image 163](<2026-yu-latent-space-foundation-evolution_images/imageFile163.png>)

![image 164](<2026-yu-latent-space-foundation-evolution_images/imageFile164.png>)

semantically lossy

humanreadable

machinenative

highfidelity

![image 165](<2026-yu-latent-space-foundation-evolution_images/imageFile165.png>)

![image 166](<2026-yu-latent-space-foundation-evolution_images/imageFile166.png>)

![image 167](<2026-yu-latent-space-foundation-evolution_images/imageFile167.png>)

![image 168](<2026-yu-latent-space-foundation-evolution_images/imageFile168.png>)

![image 169](<2026-yu-latent-space-foundation-evolution_images/imageFile169.png>)

![image 170](<2026-yu-latent-space-foundation-evolution_images/imageFile170.png>)

Explicit Space

Latent Space

![image 171](<2026-yu-latent-space-foundation-evolution_images/imageFile171.png>)

![image 172](<2026-yu-latent-space-foundation-evolution_images/imageFile172.png>)

![image 173](<2026-yu-latent-space-foundation-evolution_images/imageFile173.png>)

![image 174](<2026-yu-latent-space-foundation-evolution_images/imageFile174.png>)

interpretability

operability

evaluability

generalization

![image 175](<2026-yu-latent-space-foundation-evolution_images/imageFile175.png>)

![image 176](<2026-yu-latent-space-foundation-evolution_images/imageFile176.png>)

![image 177](<2026-yu-latent-space-foundation-evolution_images/imageFile177.png>)

Functional Capabilities

expressiveness scalability

controllability

- Figure 3 Comparison of the explicit space and latent space of the language models, including their representational properties and functional capabilities.


unified space beyond language that maps modality-specific inputs into continuous internal representations. We further provide a formal definition and formulation in Section 4.

- 2.2 Comparison with Explicit Space


To further elucidate the unique characteristics of the latent space, we conduct a comparative analysis with the traditional explicit space, or verbal space, across several critical dimensions [141, 231, 232]. As demonstrated in Figure 3, this comparison highlights a paradigm shift in the representational properties and functional capabilities of the two language models.

- 2.2.1 Representational Properties


The two distinct paradigms of language models, i.e., explicit space and latent space, exhibit fundamental differences in their representational forms, information processing modes, and practical performances. The latent space uses a Machine-native vectorized representation that is Continuous, Flexible, Efficient, and capable of preserving High-fidelity semantic information.

Human-readable v.s. Machine-native. In the explicit space, every state is expressed as a sequence of natural language tokens drawn from a finite vocabulary. This endows the generated trajectories with direct human readability and verifiability [219, 254].

By contrast, the latent space is a machine-native representational paradigm that lacks direct human legibility. Its core representations are high-dimensional real-valued vectors, where individual dimensions do not have a straightforward correspondence to human-interpretable semantic, structural, or perceptual features [148, 239]. Tailored for the intrinsic operational logic of language models, the latent representation and operations can be processed by the model, without the need for transformations of human-readable signals, reducing computational redundancy from additional encoding/decoding overhead [58, 167, 273].

Discrete & Symbolic v.s. Continuous & Flexible. Explicit-space representations are redundant, discrete, and symbolic. For instance, a chain-of-thought trace for a complex reasoning problem may span thousands of tokens [219]. Each token is a discrete symbol whose meaning is grounded in linguistic convention, and the relationship to other tokens is expressed through positional and grammatical structure [92, 238]. This decoding pattern is, in part, a redundancy and inflexibility: the majority of tokens serve textual coherence rather than substantive semantic contents [40, 234]. They ensure grammaticality, maintain topic continuity, and satisfy the autoregressive constraint that each token be a plausible continuation of the preceding sequence and be mapped into a finite discrete token, obligations that have no intrinsic connection to the logical structure of the autoregressive generation [35, 138, 239].

Conversely, latent space exhibits inherent continuity and flexibility. It encapsulates core semantic information in a continuous form, discarding superficial linguistic redundancies and symbolic mapping [58, 174, 294]. Liberated from the constraints of discrete tokenization and autoregressive linguistic conventions, this nature confers upon latent space distinct advantages in bolstering representational capacity: in reasoning models, it elevates explicit reasoning trajectories onto continuous manifolds [181, 298]; in visual scenarios, it enables smoother multimodal operations (e.g., fusion, alignment, and interaction) within latent spaces marked by a narrower modality gap [183, 227, 264]; in collaboration, it inherently serves as a more fitting medium for information storage and transmission [48, 300]. In essence, the continuous and flexible properties enable language-based models to prioritize the intrinsic semantic essence, unlocking potential across diverse tasks.

Inefficient v.s. Efficient. Conventional autoregressive generation operates entirely within an explicit discrete space, and this paradigm inherently introduces at least three fundamental inefficiencies [233, 277]: First, linguistic redundancy: as the main medium of explicit space, natural language introduces unavoidable structural and semantic redundancy, further reducing the efficiency [35, 92]; Second, representational transformation inefficiency: the model is forced to transfer representations through a narrow, explicit channel at every generation step, including intermediate steps [107, 153]. This mandatory conversion introduces unnecessary and high representational conversion costs. Third, sequential decoding overhead: discrete tokenization locks generation into a strictly sequential pipeline: each token requires a full model forward pass and vocabulary-wide probability calculation. This sequential paradigm not only has low computational efficiency but also increases computational burden [4, 94]; In contrast, latent space methods bypass these inefficiencies, e.g., removing mandatory representation conversion in inter-agent communication [48, 290, 300], and efficient recurrent or looped computation patterns [50, 167].

Semantically-lossy v.s. High-fidelity. Explicit-space representations are prone to semantic loss. When a model externalizes its internal continuous state as a token sequence, the mapping from latent activations to discrete symbols imposes a quantization bottleneck: a finite vocabulary and the combinatorial constraints of natural language delimit what can be expressed [159, 221]. As a result, fine-grained uncertainty, intermediate computational traces, cross-modal alignments, and other structures that are difficult to render in language may be compressed, distorted, or discarded. In this sense, natural language constitutes a semantically lossy transformation of the underlying computational state.

Latent-space representations, by contrast, preserve information with higher fidelity. By avoiding discretization and linguistic rendering, latent variables can carry rich, continuous information between computational steps, including content that is inexpressible in natural language and representations that naturally support multimodal structure. This perspective motivates a growing line of work directly in latent space, such as continuous thoughts [58, 174, 294], latent memory [65, 264, 273], and latent visual reasoning [95, 251], etc.

- 2.2.2 Functional Capabilities


The latent space, as a machine-native representational space, possesses multiple key functional capabilities that distinguish it from the explicit space, including Operability, Expressiveness, Scalability, Generalization,

- as well as Evaluability, controllability, and interpretability, which collectively underpin its utility in various advanced computational and representational tasks.


Operability. As a machine-native representational space, the operability of latent space characterizes its utility as a structured, differentiable manifold that serves as several internal computational substrates. This operability seamlessly enables direct calculations (such as concatenation, linear combination, etc.) and also advanced operations, e.g., controllable semantic steering [84, 250], active intervention [49, 98, 295], iterative interleaving [20, 111], and visual latent thinking [183, 211, 276]. On the contrary, the discrete tokens in the explicit space are inherently non-differentiable and lack the support of a continuous, structured manifold, rendering the aforementioned fine-grained, advanced semantic operations infeasible and permitting only limited, indirect token-level operations.

Expressiveness. It serves as a core capacity for internalizing and manipulating complex, high-dimensional, and even non-linguistic information. In contrast to natural language, which is constrained by a discrete vocabulary and grammatical conventions, representations within latent space provide a substantially richer representational substrate. In principle, it can express the representation including but not limited to the

whole explicit space, enabling efficient communication [252, 290, 300], visual perception [11, 28, 251], embodied action planning [14, 69], latent memory formation [264, 273], etc.

Scalability. It follows naturally from the compactness and parallelizability of vectorized representations. Latent-space approaches are therefore well-positioned to benefit from continued scaling of longer reasoning trajectories [117, 164, 188, 220], deeper agent interaction turns [265, 290], and test-time compute [50, 262, 274].

Generalization. It further bolsters the ability to generalize effectively to inputs distinct from those encountered during training, which capture abstract semantic structures rather than superficial linguistic patterns. By embedding abstract semantic concepts into a latent space, models gain improved cross-domain transfer and zero-shot generalization, enabling the transfer of learned abstractions to previously unseen tasks and domains. Transfer learning [195, 270], and cross-domain robustness [37, 177, 264, 273] have all been empirically shown to benefit from such informative latent representations.

Evaluability & Controllability & Interpretability. This denotes the ability of humans or automated systems to evaluate, control, observe, interpret, and audit the autoregressive generation process. For explicit generation, the resulting generation traces are evaluable, controllable, and interpretable, as each intermediate step is represented in a human-readable format [6, 89, 108]. In principle, systems built upon explicit reasoning mechanisms can integrate human-aligned verification or automated consistency checks. In contrast, machine-native latent space representations make it inherently difficult for humans to perform granular, direct evaluation, control, and interpretation of the generation process, posing potential challenges to model evaluability, controllability, and interpretability (Section 6.2).

- 2.3 Comparison with Generative Visual Models


The latent space of generative visual models is derived from a VAE-style framework [85], which learns a probabilistic mapping from high-dimensional observations to a compact continuous representation. Subsequent work introduced discrete latent codes via VQ-VAE [201], and the decisive step toward scalable synthesis was taken by latent diffusion models [162], which demonstrated that diffusion processes operating in a perceptually compressed latent space could achieve both computational efficiency and high sample fidelity. Extensions to video generation, including VideoLDM [12] and related architectures, further organized this space along a spatiotemporal axis, encoding appearance and motion as jointly structured representations.

Despite the shared reliance on learned continuous representations, the latent spaces of generative visual models and large language models differ fundamentally in their geometric structure, representational organization, and conditioning regimes.

Training Objective. The latent space of generative visual models is explicitly shaped by a reconstruction objective, which anchors the learned geometry to the statistical structure of the visual signal [12, 200]. This produces a relatively smooth, locally Euclidean manifold in which linear interpolation between encoded points yields perceptually coherent intermediates, and in which distances carry interpretable perceptual meaning. Rather than a reconstruction objective, language model hidden states are organized by a predictive criterion, next-token prediction in autoregressive models [13], with no explicit constraint on the geometry of the space.

Structure. Latent space of visual generative models maintains an explicit spatiotemporal structure: the latent tensor of an image is a spatial grid of patch-level codes [43, 150], and that of a video extends this grid along the temporal axis, with motion treated as a first-class representational element. This structural regularity reflects the continuous, compositional nature of visual scenes, in which spatial proximity and temporal coherence are strong inductive priors. On the contrary, the latent space of a language model focuses on the linguistic semantics and is devoid of spatial topology or physical dynamics.

Controllability. Precise control over visual generation is exercised through dedicated architectural pathways integrated into the model itself [278]. These signals include pose sequences, depth maps, segmentation masks, and reference images, affording fine-grained, spatially localized control over the generated output by conditioning applied directly within the representational substrate.

###### Prototype

###### Formation

###### Expansion

###### Outbreak

(Previous-2025.3)

(2025.4-2025.7)

(2025.8-2025.1)

###### (2025.12-Future)

400

theory validation early exploration

theory systematization technical formation all-round outbreak

technical maturation paradigm/scenario expansion

300

200

![image 178](<2026-yu-latent-space-foundation-evolution_images/imageFile178.png>)

![image 179](<2026-yu-latent-space-foundation-evolution_images/imageFile179.png>)

![image 180](<2026-yu-latent-space-foundation-evolution_images/imageFile180.png>)

![image 181](<2026-yu-latent-space-foundation-evolution_images/imageFile181.png>)

100

0

25

25

26

25

25

26

25

25

25

25

25

25

26

25

Previous

Future

Jul-

Feb-

Feb-

Dec-

Apr-

Jan-

Jun-

Aug-

Oct-

Nov-

Sep-

Mar-

Mar-

May-

- Figure 4 Timeline of representative works in the evolution of latent space research, organized into four developmental stages: Prototype (Section 3.1), Formation (Section 3.2), Expansion (Section 3.3), and Outbreak (Section 3.4) stages, where the horizontal axis denotes the month, and vertical axis indicates the number of the latent-level works.


###### 3 Evolution: How Did Latent Space Develop?

- As large language models have demonstrated outstanding performance across a range of natural language understanding and reasoning tasks, the exploration of their latent spaces has undergone a remarkably rapid and transformative evolution. In this section, we trace the developmental trajectory of this emerging paradigm, organizing the literature into four chronologically and thematically coherent stages (Figure 4): (1) Prototype (Previous – Mar 2025), where pioneering works first demonstrated the feasibility of moving reasoning from discrete token sequences into continuous latent representations; (2) Formation (Apr – Jul 2025), where theoretical foundations were established and systematic evaluations emerged, with research primarily centered on textual latent reasoning and initial explorations into multimodal settings; (3) Expansion (Aug – Nov 2025), where the field rapidly diversified into visual tasks, embodied action, multi-agent collaboration, and other application paths; and (4) Outbreak (Dec 2025 – Present), where explosive growth drove architectural innovation, advanced optimization, rigorous theoretical analysis, and cross-modal integration toward maturity.


- 3.1 Prototype


The prototype stage marks the genesis of latent space reasoning, where researchers first question whether large language models must articulate every intermediate reasoning step in natural language. In this stage, Theory Validation and Early Exploration begin to use continuous representations as an alternative substrate.

Theory Validation. Before the first latent systems appeared, several works laid essential groundwork by revealing that reasoning-like behavior is already encoded in the internal representations of language models. Represented by HCoT [122], early precursors show that a full CoT trace can be compressed into a compact special-token representation via contrastive semantic alignment, suggesting that much of the information in explicit CoT is redundant for the model itself. Meanwhile, Zhang and Viteri [277] discovers latent thinking vectors by extracting steering vectors from model activations, and demonstrates that injecting these vectors

- at inference time can elicit CoT-like reasoning without any fine-tuning or explicit prompting. From a theoretical perspective, Hu et al. [66] offers a Hopfieldian interpretation, framing reasoning as transitions across representation spaces with grounding in cognitive neuroscience. Furthermore, Latent Space Chainof-Embedding [217] demonstrates that LLMs can perform self-evaluation through latent embeddings rather than explicit verbal outputs. Together, these precursors establish a critical insight: the capacities of language models are not fundamentally bound to discrete token sequences, but are already substantially encoded in their latent spaces.


Early Exploration. Building on these insights, the initial stage produced a series of high-impact works that gradually shaped the initial direction of latent space reasoning. COCONUT [58] proposes the first complete framework for reasoning in continuous latent space, feeding the last hidden state back as the next input embedding to form a loop of continuous thoughts that bypasses the discrete vocabulary bottleneck. Its

key finding is that continuous thought vectors can encode superpositions of multiple potential next steps, enabling emergent breadth-first search in latent space. Along a similar compression-based direction, CCoT [31] introduces contemplation tokens that compress explicit reasoning chains into dense latent form. At the same time, Liu et al. [117] augments the KV cache with latent embeddings via an offline coprocessor, keeping the decoder entirely frozen. Both demonstrate that latent representation can be injected into existing models through parameter-efficient adaptation without inference latency overhead.

Subsequently, Huginn [50] proposes using recurrent depth to scale test-time compute in latent space, iterating a shared transformer block a variable number of times to perform all reasoning implicitly without specialized reasoning data. SoftCoT [243] provides the first plug-in approach to latent space, projecting instance-specific soft thought tokens into the frozen backbone’s representation space to avoid catastrophic forgetting.

Taken together, the prototype stage establishes the feasibility of latent-space reasoning, but it also exposes its first major bottleneck: the field still lacks a systematic account of why latent reasoning works, when it outperforms explicit CoT, and how it should be evaluated beyond isolated proof-of-concept demonstrations. In other words, the central challenge at this stage is not capability alone, but interpretability, formalization, and comparability. These limitations directly motivate the next stage, where the community moves from scattered prototypes toward theoretical systematization, benchmark construction, and more principled technical design.

- 3.2 Formation


The formation stage advances from the prototype-stage insights toward building a more practically meaningful research program. This period is primarily centered on textual latent reasoning and is characterized by two advances: Theoretical Systematization that explains why it works, Technical Formation that works on how well it works, and initial explorations of extension into multimodal and embodied settings.

Theory Systematization. The most transformative contribution of this stage is the theoretical understanding of continuous thought mechanisms. These theoretical works provide formal guarantees for the expressiveness and computational advantages of latent space, grounding the empirical successes of the prototype stage in rigorous mathematical frameworks. Zhu et al. [294] (Reasoning by Superposition) provide the first formal complexity analysis, proving that continuous thought vectors acting as superposition states can encode multiple search frontiers simultaneously, offering a rigorous explanation for COCONUT’s empirically observed behavior. CoT2 [52] further quantifies the relationship between parallelism and embedding dimension and introduces continuous supervision and reinforcement learning for continuous thought optimization. Saunshi et al. [167] prove that looped transformers with latent iterations can express strictly more complex computations than standard transformers, establishing theoretical separation results for recurrent-depth architectures.

Technical Formation. The formation stage also witnesses important methodological innovations that translate the prototypes into more practical and versatile latent techniques. These advances span both representation design and optimization strategies, progressively expanding the toolkit available. On the representation front, a series of works explored latent representation design: Assorted [181] proposes mixing latent discrete tokens with text tokens to achieve shorter traces with improved accuracy; CODI [174] formalizes a self-distillation procedure where the same model serves as both teacher and student to generate reasoning chains in explicit and latent spaces respectively; and BoLT [164] shifts attention to pretraining, treating web text as compressed outcomes of thought processes and using bootstrapping for data-efficient pretraining.

On the optimization front, represented by HRPO [266], System-1.5 [214], and CoLaR [188], a family of methods respectively introduced latent reinforcement methods, adaptive computation allocation between language and latent spaces, and dynamic inference-time controllable compression. These works demonstrate that latent optimization can be optimized end-to-end and adaptively allocated across different modalities.

Another characteristic of this stage is that latent-level models begin extending beyond text-only LLMs. While the primary focus remains on textual reasoning, several pioneering efforts demonstrate the broader applicability of the latent space paradigm across modalities. Mirage [251] enables VLMs to think visually by recasting hidden states as latent visual tokens interleaved with text, implementing internal visual manipulation analogous to human mental imagery. UniVLA [14] introduces task-centric latent actions for cross-embodiment robot policies, learning latent action representations from internet-scale video. These early multimodal explorations

demonstrate that the latent space paradigm is not confined to textual reasoning but may constitute a general framework applicable across modalities and embodiment types.

Despite these advances, the formation stage remains constrained by a second bottleneck: most methods are still developed and evaluated within relatively narrow settings, with text-centric assumptions, limited downstream diversity, and weak integration across memory, planning, communication, and action. As a result, the field has learned how to make latent reasoning more principled, but not yet how to make it broadly useful across heterogeneous scenarios. This gap naturally drives the next stage, where the main question shifts from “can latent reasoning be formalized?” to “how far can the latent-space paradigm generalize across domains, modalities, and system settings?”

- 3.3 Expansion


The expansion stage transforms latent space research from a text-centric landscape into a multi-modal, multi-domain ecosystem. This stage witnesses rapid diversification along concurrent dimensions. The period is marked by the Technical Maturation of domain-specific innovations and Paradigm/Scenario Expansion of cross-cutting themes such as latent memory, test-time scaling, and RL-based optimization.

Technical Maturation. In the LLM domain, latent methods evolve from proof-of-concept to more sophisticated systems that address challenges in memory, scalability, optimization, and domain-specific applications. The research landscape broadens considerably, with multiple sub-directions developing in parallel. Represented by MemGen [273], a line of works pioneers latent memory for agents, interweaving reasoning and memory so that planning, procedural, and working memory types emerge without explicit supervision. On the test-time scaling front, LTPO [258] treats latent thought vectors as optimizable parameters with online policy gradient; Ouro [296] moves optimization into pretraining via looped language models; and You et al. [262] enables parallel test-time scaling through stochastic sampling strategies with a latent reward model for trajectory selection. For RL-driven optimization, SofT-GRPO [291] solves the differentiability challenge of applying RL to continuous latent reasoning through Gumbel-reparameterized policy optimization. In the interleaving and hybrid direction, SpiralThinker [155] and CLaRa [59] propose text-latent iterative interleaving and unified retrieval-augmented generation in shared continuous spaces, respectively. Additionally, domain-specific applications emerge, including search-and-recommendation unification [177], code language model interpretability [172], and System 1/2 dual-architecture communication [33].

Paradigm/Scenario Expansion. The expansion stage sees an explosion of visual latent-level methods, establishing the paradigm of thinking in visual space as a complement to textual reasoning. These methods enable VLMs to perform internal visual manipulation and reasoning directly in latent representations, bypassing the information loss incurred by converting visual content into discrete text tokens. Represented by LVR [95] and Monet [211], a family of works introduces autoregressive reasoning in the visual embedding space, generating latent states interleaved with text for fine-grained visual understanding. 3DThinker [28] further extends this to 3D mental simulation from limited 2D views by aligning latent representations with

- 3D foundation models. Another line address latent visual tasks: VisMem [264] proposes cognitively inspired short-term and long-term latent vision memory modules, while CoMEM [230] scales continuous memory for visual agents. Works such as Latent Sketchpad [276] and LaCoT [183] further explore visual scratchpads for planning and variational inference for visual reasoning, respectively.


The expansion stage gives birth to latent communication as a new paradigm for multi-agent systems. Unlike traditional text-based inter-agent communication, latent communication enables direct exchange of continuous representations, offering higher bandwidth and lower latency. C2C [48] introduces direct semantic communication between LLMs via KV-cache projection and fusion. [290] develops a theoretical framework for mind-to-mind latent thought communication, while LatentMAS [300] demonstrates latent collaboration through shared latent working memory, significantly reducing output tokens while improving accuracy.

The embodied domain also expands significantly during this stage, with latent representations becoming a central tool for learning and transferring robotic manipulation and navigation skills. Self-supervised pretraining from unlabeled video emerged as a key methodology. Represented by LAPA [256] and LAWM [196], a line of self-supervised methods pioneers latent action pretraining from unlabeled video data through world modeling. OccVLA [118] integrates implicit 3D occupancy supervision for interpretable trajectory planning, while

SRPO [45] applies RL with latent world representations for VLA training. ATE [281] enables data-efficient VLA adaptation through unified latent guidance, achieving substantial real-world cross-embodiment gains.

However, rapid expansion also introduces a new bottleneck: the field becomes increasingly fragmented. Once latent-space methods spread across language, vision, multi-agent systems, and embodiment, the main challenge is no longer lack of applications, but lack of unification. Different works adopt different architectural assumptions, optimization objectives, evaluation criteria, and latent interfaces, making it difficult to compare methods or identify stable design principles. This fragmentation sets the stage for the outbreak period, in which the research frontier shifts toward architectural specialization, optimization sophistication, and more mature attempts to consolidate latent space as a first-class computational paradigm.

- 3.4 Outbreak


The outbreak stage represents an explosive acceleration of the field, characterized by the All-roundOutbreak of all research threads. The maturity of this stage is reflected in many hallmarks: architectural and representational specialization, with purpose-built models designed specifically for latent representation; computation and optimization sophistication, with methods addressing fine-grained challenges such as exploration collapse and latent reward encoding; Moreover, multi-scenario surge, with unified frameworks spanning language, vision, action, and multi-agent systems.

All-round Outbreak. A defining feature of this stage is the increasing specialization of model architectures. Rather than merely adapting standard transformer backbones via shallow recurrence or iterative decoding, recent work has developed architectures explicitly designed to support latent computation as a first-class mechanism. These models generally aim to improve the controllability, efficiency, and expressiveness of reasoning in latent space.

Representative examples include Dreamer [86] and LoopFormer [72], which introduce depth-recurrent designs that combine sequence attention with depth-wise computation and elastic looping, thereby enabling budgetaware reasoning and more flexible compute allocation. MLRA [121] further revises the attention mechanism through low-rank projections, while DLCM [158] shifts the granularity of latent computation from token-level operations toward concept-level reasoning with adaptive conceptual boundaries. Collectively, these studies suggest that architectural development is moving beyond incremental modifications to sequence models toward dedicated latent-space systems.

Alongside architectural specialization, optimization strategies for latent space also become substantially more sophisticated. For example, ReLaX [280] and Active Latent Planning [292] advance latent-space exploration by moving beyond imitation-based learning toward more explicit reinforcement-learning-based planning. At the same time, Özeren and Aßenmacher [149] demonstrate, through a systematic analysis, that reinforcement learning remains sensitive to design choices and continues to face persistent optimization challenges. LED [189] addresses post-training exploration collapse by leveraging entropy variation across recurrent depth. In contrast, Latent Thinking Optimization [41] shows that latent thoughts can themselves encode reward-relevant information, thereby opening the possibility of directly optimizing latent trajectories without relying exclusively on external reward models. Overall, these developments indicate that optimization is becoming an independent axis of progress rather than a secondary concern.

In visual tasks, recent studies demonstrate that latent space supports increasingly complex forms of multi-step and interleaved inference. ILVR [39] and CrystaL [283], for instance, explore visual-text interleaved reasoning and report the emergence of visual latent representations during the reasoning process. LIVR [100] and Mull-Tokens [160] further extend this line of work by pushing visual reasoning more fully into latent space and by proposing modality-agnostic latent thinking mechanisms. Related efforts such as VL-JEPA [21] and DMLR [111] further expand the design space of visual reasoning and highlight the growing diversity of methodological formulations in this area.

A similar expansion is also evident in multi-agent systems, where latent communication evolves from preliminary demonstrations into more structured frameworks for coordination and representation sharing. Dery et al. [38] propose latent-space communication via K-V cache alignment with lightweight adapters, enabling translation between heterogeneous internal states. L2-VMAS [265] and Wormhole [124] extend this perspective to visual and heterogeneous multi-agent settings, while LatentMem [47] introduces shared latent memory mechanisms

###### Table 1 General notations used throughout the paper.

Symbol Space Description

- V token space discrete vocabulary/token IDs H latent space continuous hidden space Rd M model space set of models/modules/components

- W parameter space parameters within the model


- D data space the whole training and test data

- x V input

- y V output r V generation trajectory

E V matrix embedding W V projection matrix q,k,v V query, key, value h H hidden state of one token H H hidden state of token sequence

- z H latent representation Φ M whole framework Φback M backbone Φcomp M functional component Φaux M auxiliary model θ W model parameters R – reward function L – loss function




for multi-agent experience accumulation. These works suggest that latent communication is becoming an important mechanism for scalable inter-agent coordination.

The embodied VLA setting provides another major area of expansion. Here, latent representations increasingly serve as a unifying interface for perception, generation, and action, and latent action modeling is emerging as a central design paradigm. Motus [10] and VLA-JEPA [184] exemplify this trend by developing unified latent action world models that integrate action generation and environment understanding within a shared latent space. Villa-X [26] and JALA [131] further improve the expressiveness and scalability of latent action modeling, while CoWVLA [249] introduces world-model reasoning in latent motion space. Additional work, including WholeBodyVLA [77], SwiftVLA [142], and LoLA [213], reinforces the view that latent action representations are becoming increasingly central to VLA pretraining and deployment.

- At the same time, the outbreak stage surfaces the next-order bottleneck for the field as a whole: once latentspace methods become specialized, powerful, and widespread, the hardest problem is no longer demonstration but consolidation. The open questions now concern standardization of latent interfaces, principled evaluation across modalities, alignment between latent efficiency and interpretability, and the integration of latent computation into broader agentic systems. In this sense, the outbreak stage does not mark the end of the story; rather, it reveals that the next phase of progress will likely depend on turning a rapidly growing collection of techniques into a coherent science and harness engineering for latent computation.


- 4 Mechanism: How Does Latent Space Work?


Mechanism concerns how latent space is instantiated, structured, and operationalized within a model, beyond the high-level question of why it is useful. Existing methods differ not only in where latent variables are introduced, but also in how they are represented, how computation is carried out through them, and at which stage they are shaped or exploited. To organize this design space, we categorize latent-space mechanisms along four complementary axes: Architecture (Section 4.1) characterizes the structural role of latent space in the model, including whether it is embedded in the backbone, realized as a dedicated component, or supported by

![image 182](<2026-yu-latent-space-foundation-evolution_images/imageFile182.png>)

![image 183](<2026-yu-latent-space-foundation-evolution_images/imageFile183.png>)

![image 184](<2026-yu-latent-space-foundation-evolution_images/imageFile184.png>)

![image 185](<2026-yu-latent-space-foundation-evolution_images/imageFile185.png>)

![image 186](<2026-yu-latent-space-foundation-evolution_images/imageFile186.png>)

CoE COCONUT Soft Thinking

CODI SoftCoT

AURORA AlignVLM UniVLA

HCoT SoftCoT SoftCoT++

VTI

![image 187](<2026-yu-latent-space-foundation-evolution_images/imageFile187.png>)

![image 188](<2026-yu-latent-space-foundation-evolution_images/imageFile188.png>)

![image 189](<2026-yu-latent-space-foundation-evolution_images/imageFile189.png>)

![image 190](<2026-yu-latent-space-foundation-evolution_images/imageFile190.png>)

![image 191](<2026-yu-latent-space-foundation-evolution_images/imageFile191.png>)

![image 192](<2026-yu-latent-space-foundation-evolution_images/imageFile192.png>)

![image 193](<2026-yu-latent-space-foundation-evolution_images/imageFile193.png>)

COT2 SALS IVT-LR

OccVLA

KAVA 3DThinker CoVT

SIM-CoT

3DThinker CoVT

![image 194](<2026-yu-latent-space-foundation-evolution_images/imageFile194.png>)

CoCoMix

![image 195](<2026-yu-latent-space-foundation-evolution_images/imageFile195.png>)

![image 196](<2026-yu-latent-space-foundation-evolution_images/imageFile196.png>)

![image 197](<2026-yu-latent-space-foundation-evolution_images/imageFile197.png>)

![image 198](<2026-yu-latent-space-foundation-evolution_images/imageFile198.png>)

![image 199](<2026-yu-latent-space-foundation-evolution_images/imageFile199.png>)

![image 200](<2026-yu-latent-space-foundation-evolution_images/imageFile200.png>)

![image 201](<2026-yu-latent-space-foundation-evolution_images/imageFile201.png>)

LCDrive

![image 202](<2026-yu-latent-space-foundation-evolution_images/imageFile202.png>)

![image 203](<2026-yu-latent-space-foundation-evolution_images/imageFile203.png>)

![image 204](<2026-yu-latent-space-foundation-evolution_images/imageFile204.png>)

CoLaR CoMEM ThinkAct MemGen

![image 205](<2026-yu-latent-space-foundation-evolution_images/imageFile205.png>)

CoLaR CTRLS

![image 206](<2026-yu-latent-space-foundation-evolution_images/imageFile206.png>)

LatentMas

Mull-Tokens OneLatent

![image 207](<2026-yu-latent-space-foundation-evolution_images/imageFile207.png>)

![image 208](<2026-yu-latent-space-foundation-evolution_images/imageFile208.png>)

SkiLa

![image 209](<2026-yu-latent-space-foundation-evolution_images/imageFile209.png>)

![image 210](<2026-yu-latent-space-foundation-evolution_images/imageFile210.png>)

OccVLA

![image 211](<2026-yu-latent-space-foundation-evolution_images/imageFile211.png>)

FR-Ponder LaDiR

![image 212](<2026-yu-latent-space-foundation-evolution_images/imageFile212.png>)

![image 213](<2026-yu-latent-space-foundation-evolution_images/imageFile213.png>)

![image 214](<2026-yu-latent-space-foundation-evolution_images/imageFile214.png>)

Auxiliary Model Internal

![image 215](<2026-yu-latent-space-foundation-evolution_images/imageFile215.png>)

![image 216](<2026-yu-latent-space-foundation-evolution_images/imageFile216.png>)

![image 217](<2026-yu-latent-space-foundation-evolution_images/imageFile217.png>)

ETD LS

AR

![image 218](<2026-yu-latent-space-foundation-evolution_images/imageFile218.png>)

![image 219](<2026-yu-latent-space-foundation-evolution_images/imageFile219.png>)

MCOUT

C2C

![image 220](<2026-yu-latent-space-foundation-evolution_images/imageFile220.png>)

TaH

VisMem ColaVLA RISER

![image 221](<2026-yu-latent-space-foundation-evolution_images/imageFile221.png>)

![image 222](<2026-yu-latent-space-foundation-evolution_images/imageFile222.png>)

![image 223](<2026-yu-latent-space-foundation-evolution_images/imageFile223.png>)

![image 224](<2026-yu-latent-space-foundation-evolution_images/imageFile224.png>)

LIVR CoLT

External Learnable

HCoT

![image 225](<2026-yu-latent-space-foundation-evolution_images/imageFile225.png>)

![image 226](<2026-yu-latent-space-foundation-evolution_images/imageFile226.png>)

![image 227](<2026-yu-latent-space-foundation-evolution_images/imageFile227.png>)

Palette

Component

![image 228](<2026-yu-latent-space-foundation-evolution_images/imageFile228.png>)

AURORA Assorted CoMEM

![image 229](<2026-yu-latent-space-foundation-evolution_images/imageFile229.png>)

Architecture Representation

Heima Huginn Looped Trans.

![image 230](<2026-yu-latent-space-foundation-evolution_images/imageFile230.png>)

DCA

![image 231](<2026-yu-latent-space-foundation-evolution_images/imageFile231.png>)

![image 232](<2026-yu-latent-space-foundation-evolution_images/imageFile232.png>)

![image 233](<2026-yu-latent-space-foundation-evolution_images/imageFile233.png>)

Ouro

![image 234](<2026-yu-latent-space-foundation-evolution_images/imageFile234.png>)

![image 235](<2026-yu-latent-space-foundation-evolution_images/imageFile235.png>)

![image 236](<2026-yu-latent-space-foundation-evolution_images/imageFile236.png>)

Hybrid

Backbone

![image 237](<2026-yu-latent-space-foundation-evolution_images/imageFile237.png>)

UniVLA

![image 238](<2026-yu-latent-space-foundation-evolution_images/imageFile238.png>)

Mechanism

![image 239](<2026-yu-latent-space-foundation-evolution_images/imageFile239.png>)

LAPA Ouro

![image 240](<2026-yu-latent-space-foundation-evolution_images/imageFile240.png>)

![image 241](<2026-yu-latent-space-foundation-evolution_images/imageFile241.png>)

Pretraining

CCoT CODI KAVA RoT

![image 242](<2026-yu-latent-space-foundation-evolution_images/imageFile242.png>)

![image 243](<2026-yu-latent-space-foundation-evolution_images/imageFile243.png>)

Compressed

![image 244](<2026-yu-latent-space-foundation-evolution_images/imageFile244.png>)

CoCoMix Looped Trans.

![image 245](<2026-yu-latent-space-foundation-evolution_images/imageFile245.png>)

![image 246](<2026-yu-latent-space-foundation-evolution_images/imageFile246.png>)

![image 247](<2026-yu-latent-space-foundation-evolution_images/imageFile247.png>)

Computation Optimization

![image 248](<2026-yu-latent-space-foundation-evolution_images/imageFile248.png>)

DeltaKV

Expanded

![image 249](<2026-yu-latent-space-foundation-evolution_images/imageFile249.png>)

PonderLM-2

![image 250](<2026-yu-latent-space-foundation-evolution_images/imageFile250.png>)

Posttraining Inference

Huginn

![image 251](<2026-yu-latent-space-foundation-evolution_images/imageFile251.png>)

LaTRO

![image 252](<2026-yu-latent-space-foundation-evolution_images/imageFile252.png>)

Adaptive

SoftCoT++ COT2 PCCoT LatentTTS

![image 253](<2026-yu-latent-space-foundation-evolution_images/imageFile253.png>)

![image 254](<2026-yu-latent-space-foundation-evolution_images/imageFile254.png>)

![image 255](<2026-yu-latent-space-foundation-evolution_images/imageFile255.png>)

![image 256](<2026-yu-latent-space-foundation-evolution_images/imageFile256.png>)

ReaRec CoLaR HRPO LatentR3 Mirage MemGen

![image 257](<2026-yu-latent-space-foundation-evolution_images/imageFile257.png>)

![image 258](<2026-yu-latent-space-foundation-evolution_images/imageFile258.png>)

Interleaved

![image 259](<2026-yu-latent-space-foundation-evolution_images/imageFile259.png>)

![image 260](<2026-yu-latent-space-foundation-evolution_images/imageFile260.png>)

![image 261](<2026-yu-latent-space-foundation-evolution_images/imageFile261.png>)

System-1.5

![image 262](<2026-yu-latent-space-foundation-evolution_images/imageFile262.png>)

Latent-SFT

![image 263](<2026-yu-latent-space-foundation-evolution_images/imageFile263.png>)

![image 264](<2026-yu-latent-space-foundation-evolution_images/imageFile264.png>)

![image 265](<2026-yu-latent-space-foundation-evolution_images/imageFile265.png>)

Latent-SFT 3DThinker SemCoT

![image 266](<2026-yu-latent-space-foundation-evolution_images/imageFile266.png>)

![image 267](<2026-yu-latent-space-foundation-evolution_images/imageFile267.png>)

![image 268](<2026-yu-latent-space-foundation-evolution_images/imageFile268.png>)

Ouro TaH LWS

Assorted

![image 269](<2026-yu-latent-space-foundation-evolution_images/imageFile269.png>)

SoftCoT++

![image 270](<2026-yu-latent-space-foundation-evolution_images/imageFile270.png>)

PLR

![image 271](<2026-yu-latent-space-foundation-evolution_images/imageFile271.png>)

![image 272](<2026-yu-latent-space-foundation-evolution_images/imageFile272.png>)

Latent-GRPO VisMem LWS Monet ReLaX Latent-RL

![image 273](<2026-yu-latent-space-foundation-evolution_images/imageFile273.png>)

![image 274](<2026-yu-latent-space-foundation-evolution_images/imageFile274.png>)

![image 275](<2026-yu-latent-space-foundation-evolution_images/imageFile275.png>)

![image 276](<2026-yu-latent-space-foundation-evolution_images/imageFile276.png>)

![image 277](<2026-yu-latent-space-foundation-evolution_images/imageFile277.png>)

![image 278](<2026-yu-latent-space-foundation-evolution_images/imageFile278.png>)

DLCM PRE I2B-LPO PLaT

Mirage LVR

![image 279](<2026-yu-latent-space-foundation-evolution_images/imageFile279.png>)

![image 280](<2026-yu-latent-space-foundation-evolution_images/imageFile280.png>)

LatentSeek SR LatentEvolve LTO

![image 281](<2026-yu-latent-space-foundation-evolution_images/imageFile281.png>)

Laser

![image 282](<2026-yu-latent-space-foundation-evolution_images/imageFile282.png>)

![image 283](<2026-yu-latent-space-foundation-evolution_images/imageFile283.png>)

![image 284](<2026-yu-latent-space-foundation-evolution_images/imageFile284.png>)

![image 285](<2026-yu-latent-space-foundation-evolution_images/imageFile285.png>)

![image 286](<2026-yu-latent-space-foundation-evolution_images/imageFile286.png>)

![image 287](<2026-yu-latent-space-foundation-evolution_images/imageFile287.png>)

MemGen VisMem Monet ILVR DMLR

![image 288](<2026-yu-latent-space-foundation-evolution_images/imageFile288.png>)

![image 289](<2026-yu-latent-space-foundation-evolution_images/imageFile289.png>)

![image 290](<2026-yu-latent-space-foundation-evolution_images/imageFile290.png>)

![image 291](<2026-yu-latent-space-foundation-evolution_images/imageFile291.png>)

![image 292](<2026-yu-latent-space-foundation-evolution_images/imageFile292.png>)

AL-CoT SpiralFormer

![image 293](<2026-yu-latent-space-foundation-evolution_images/imageFile293.png>)

![image 294](<2026-yu-latent-space-foundation-evolution_images/imageFile294.png>)

![image 295](<2026-yu-latent-space-foundation-evolution_images/imageFile295.png>)

![image 296](<2026-yu-latent-space-foundation-evolution_images/imageFile296.png>)

![image 297](<2026-yu-latent-space-foundation-evolution_images/imageFile297.png>)

I2B-LPO ATP-Latent

![image 298](<2026-yu-latent-space-foundation-evolution_images/imageFile298.png>)

![image 299](<2026-yu-latent-space-foundation-evolution_images/imageFile299.png>)

LTPO DMLR ITR

- Figure 5 Representative works operate in accordance with latent space mechanisms. We classify all methods into four lines based on diverse ways of utilizing the latent space, including: Architecture (Section 4.1), Representation (Section 4.2), Computation (Section 4.3), and Optimization (Section 4.4).


an auxiliary model; Representation (Section 4.2) describes the form of latent variables, distinguishing internal, external, learnable, and hybrid representations. Computation (Section 4.3) captures how the latent space participates in information processing, including compressed, expanded, adaptive, or interleaved computation. Optimization (Section 4.4) focuses on when and how latent space is induced, aligned, or refined, spanning pre-training, post-training, and inference-time mechanisms. These four mechanistic types provide a unified lens for comparing diverse approaches and clarify the major design choices that govern how latent spaces are constructed and used in modern language-based systems.

General Notation and Formalization. Based on the notations in Table 1, we first formalize the standard autoregressive generation paradigm. Given an input sequence x ∈ V, a model Φθ defines a conditional distribution over the output sequence y ∈ V:

y ∼ Φθ(· | x). (1)

where generation is performed purely in token space: the model predicts each output token conditioned on the input and the previously generated context. Although the computation is internally carried out through continuous hidden states h ∈ H, the generation interface itself remains token-to-token.

Latent-space methods extend this formulation by introducing an additional latent representation z ∈ H, such that generation is conditioned not only on the observable input x but also on a continuous latent variable:

y ∼ Φθ(· | x,z), (2)

where z denotes a latent representation in the latent space H. Compared with standard autoregressive generation, the latent variable z provides an additional channel for encoding information that may be difficult to express directly in token space, such as global semantics, multimodal features, intermediate reasoning states, structural constraints, or other task-relevant factors.

###### Table 2 Overview of the Backbone (Section 4.1.1) based architecture. We compare the hidden dimension, layer, size, and architectural feature of these backbones.

Date Backbone Paper Code Dimension Layer Size Feature

- 01/25 Heima [173] Paper Code 4096 72 19B encoder-decoder/progressive/adaptive decoding

- 02/25 Huginn [50] Paper Code 5280 8 3.5B decoder-only/recurrent depth/shared recurrent block/test-time


- 02/25 Looped Trans. [167] Paper - 5120 24 1.5B decoder-only/looped model/looping-based regularization

- 03/25 MoLAE [127] Paper - 512 12 0.1B mixture of latent experts/shared projection/lower dimension

- 04/25 PHD-Trans. [223] Paper - 2048 16 1.2B decoder-only/cache management/sliding window attention


- 09/25 PonderLM2 [267] Paper Code 2048 24 0.5B/1.4B decoder-only/iterative refinement/Jacobi-style parallel updates

- 10/25 Ouro [296] Paper - 2048 24/48 1.4B/2.6B decoder-only/recursive inference/parameter-shared loop 12/25 DLCM [158] Paper - 1536 32 2.3B encoder-decoder/large concept model/hierarchical/heterogeneous


- 01/26 Dreamer [86] Paper - 1024 16/32 1B/2B depth-recurrent/sequence-depth-sparse attention mixture

- 02/26 LoopFormer [72] Paper Code 2048 - - decoder-only/elastic-depth looped transformer

- 03/26 MLRA [121] Paper Code 3072 24 2.9B multi-head low-rank attention/four-way tensor parallelism decoding


Under this perspective, the central question is not merely whether a method uses latent variables, but how latent space is instantiated and integrated into the generation process. This motivates the mechanism-oriented taxonomy in this survey.

- 4.1 Architecture


Recent advances in latent-level methods have catalyzed a profound rethinking of the established architectural design paradigms for models operating in explicit representational spaces [66]. Departing from the exclusive reliance on conventional autoregressive frameworks, an increasing number of studies have pioneered innovative mechanisms that enable core computations within latent spaces, where high-level cognitive processes [104], e.g., reasoning, perception, and planning, can be conducted with substantially enhanced efficiency and expressiveness. This transformative shift extends far beyond a mere change of representational domain; it encapsulates a fundamental evolution in the architectural philosophy of modern neural models [294].

This emerging paradigm reveals that latent space is evolving from an isolated technical heuristic into a general, foundational architectural principle. To answer the core question: what architectures are utilized to learn the latent space?, we distinguish these methods by the location where latent space H is integrated into Φ, with a focus on the structure of the latent system within model space Φ = Φback,Φcomp,Φaux . As reported in

- Table 2 and Table 3, we classify all existing architecture-driven methods into three categories:


Mechanism: Architecture

- • Backbone (Section 4.1.1): endows the main model with native latent capacity through recurrent, looping, recursive structures, thereby making an architectural primitive.
- • Component (Section 4.1.2): employs generation, projection heads, alignment, control, storage, or other components, which allow latent functions while preserving the main model skeleton.
- • Auxiliary Model (Section 4.1.3): utilizes an extra model to provide supervision signals or intermediate features to guide or supplement the host model.


- 4.1.1 Backbone


In this category, latent computation is intrinsically embedded in the primary generative architecture rather than introduced via an external auxiliary module. Formally, the backbone itself carries out an iterative or structured transition over latent states:

ht+1 = Φback(h1:t,x,y1:t), (3)

where each subsequent output token is produced based on the updated hidden state, under this formulation, the latent operation constitutes a native operational mechanism of Φback(·) itself, meaning that the reasoning

or intermediate transformation process is realized internally within the backbone, without requiring any additional component.

Existing backbone-based methods can be broadly understood from three complementary perspectives: Parameter-shared, Iterative Refinement, and Augmented. Rather than simply following the explicit-level counterparts, these works revisit the backbone design itself to offer a promising path.

Parameter-shared Backbone. From the perspective of parameter sharing, a representative line of work replaces a deep stack of distinct layers with a smaller set of reusable modules applied repeatedly. However, in this paradigm, the recurrent depth or times is typically fixed. Huginn [50], for example, adopts a decoder-only architecture, but compensates for the shallow explicit depth by introducing a shared recurrent block that is reused across multiple depth steps. This design substantially reduces the number of unique parameters while enabling test-time scaling, where additional recurrent steps can be applied during inference to trade compute for performance. Looped Trans. [167] further develops this idea by enforcing an explicit layer-looping mechanism. A key technical feature is its looping-based regularization, which stabilizes the hidden-state dynamics under repeated application of the same transformation and encourages convergence of iterative representations. In a related efficiency-oriented setting, PHD-Trans. [223] explores how such recurrent computation can remain practical under long-context decoding. It integrates cache management with sliding-window attention, reducing memory overhead while preserving the benefits of repeated updates.

Iterative Backbone. This paradigm highlights the iterative process and dynamic updating, with variable or learnable depth allocation. For instance, Ouro [296] introduces a recursive inference framework whose iterations can serve as an alternative scaling axis, analogous to increasing architectural depth, showing that repeated application of parameter-shared transformations can yield consistent gains. LoopFormer [72] introduces an elastic-depth looped transformer, where the number of loop iterations is not fixed but can vary across inputs or computational budgets. This makes recurrent-depth execution more flexible and better aligned with the complexity of individual examples. PonderLM2 [267] is a representative method in this category. Built as a decoder-only model, it employs iterative refinement via Jacobi-style parallel updates. Instead of strictly following the standard autoregressive regime, where each forward pass advances the prediction by one token, it also performs multi-step hidden-state evolution in parallel, enabling richer internal computation while retaining decoding efficiency.

Augmented Backbone. Beyond these two designs, several works explore augmented architectures at different granularities. For example, Heima [223] and DLCM [158], unlike most encoder-only designs, employ hierarchical encoder-decoder architectures to organize latent computation. The latter one also shifts computation from tokens to a compressed concept space, with more efficient semantic operations. Dreamer [86] and MLRA [121] design sequence-depth sparse attention mixtures and low-rank attention, respectively, making multi-step latent transitions computationally tractable and efficient. In addition, MoLAE [127] designs an architecture of reformulating the mixture of latent experts in lower dimension.

Summary. Overall, backbone-oriented methods represent the most intrinsic form of architecture-level latent modeling. Parameter-sharing approaches improve efficiency by reusing subsets of layers or models; iterative-refinement methods further enhance flexibility by enabling dynamic, adaptive iterations; and augmentation-based designs provide a broader view of architectural shifts. This shift provides the foundation for more flexible, computation-aware, and cognitively expressive generative systems.

- 4.1.2 Component


This paradigm preserves the original backbone architecture but augments it with functional modules that construct, transform, store, or retrieve latent representations. Formally, a component produces and is then injected into the backbone decoding process:

z = Φcomp (h,x), (4)

where the backbone Φback(·) remains the principal generator, while the extra component Φcomp(·) acts as a plug-in operator over latent space, and the output z will be used in Equation 2.

Such a design preserves the backbone architecture while equipping it with a latent mechanism to facilitate or guide downstream generation. It covers a broad family of modules that operate on latent spaces while leaving

###### Table 3 Overview of the Component (Section 4.1.2) and Auxiliary Model (Section 4.1.3) based architecture, respectively. We compare the modality, backbone, the type of the component module or external model, function, and scenario. Here, (VQ)-AE, SAE, MLP, Q-Former, LoRA, and JEPA denote (vector quantized) variational autoencoder, multilayer perceptron, querying transformer, low-rank adaptation, and joint embedding predictive architecture, respectively.

Date Method Paper Code Modality Backbone Module/Model Function Scenario Component

###### 12/24 AURORA [11] Paper Code vision LLaVA1.5-13B VQ-VAE vision generation visual perception

- 01/25 LF-Steering [250] Paper - text LLaMA2-7B SAE semantic projection semantic consistency

- 02/25 AlignVLM [137] Paper - vision LLaMA3.2-1B/3B mixed layers vision alignment document understanding 02/25 CoCoMix [186] Paper Code text GPT2-0.1B/0.4B/1.4B SAE concept extraction interpretability/efficiency


- 02/25 IMM [148] Paper - text GPT2-0.1B vector library memory bank long-horizon/safety 05/25 SoftCoT++ [244] Paper Code text LLaMA3.1-8B linear layer semantic projection exploration/zero-shot/scaling 05/25 CoLaR [188] Paper Code text LLaMA3.2-1B MLP embedding generation dynamic reasoning/efficiency 05/25 CoMEM [229] Paper Code vision Qwen2/2.5-VL-7B Q-Former memory generation visual reasoning/long-horizon/efficiency 07/25 ThinkAct [69] Paper Code action Qwen2.5-VL-7B Q-Former action projection embodied manipulation/long-horizon

- 09/25 OccVLA [118] Paper - action PaliGemma2-3B transformer feature injection spatial understanding

- 09/25 FR-Ponder [62] Paper - text LLaMA3-8B/other 4 MLP trigger dynamic reasoning/efficiency/generalization

- 09/25 MemGen [273] Paper Code text SmolLM3-3B/Qwen3-8B LoRA trigger/generation experimental memory/generalization

- 10/25 HYP1/2 [33] Paper - text GPT2-0.1B/Qwen3-0.6B transformer messages exchange latent reasoning/communication


- 10/25 LaDiR [83] Paper Code text LLaMA3.1-8B VAE decoder semantic encoding exploration/diffusion-augmented


- 10/25 ETD [87] Paper - text OLMo-2-1B encoder-decoder token generation multi-step reasoning/zero-shot


- 10/25 CoMEM-Agent [230] Paper Code vision Qwen2.5-VL-7B/other 1 Q-Former memory generation GUI agent/long-horizon

- 10/25 Kelp [101] Paper Code text Qwen3-8B MLP trigger risk detection/efficiency

- 10/25 AR [64] Paper - text LLaMA3.1-8B/Gemma2-9B SAE feature generation safety/multi-hop reasoning

- 10/25 LS [276] Paper Code vision Gemma3-12B/other 2 VAE decoder vision generation visual imagination/visual understanding

- 11/25 TaH [49] Paper Code text Qwen3-0.6B/1.7B MLP decider dynamic reasoning/complex reasoning

11/25 SpiralThinker [155] Paper - text LLaMA3.2-7B MLP semantic projection latent reasoning/complex reasoning 11/25 VisMem [264] Paper Code vision Qwen2.5-VL-7B/other 8 LoRA memory generation visual understanding/visual reasoning 11/25 VITA [136] Paper Code action PaliGemma-3B encoder-decoder feature encoding embodied manipulation 12/25 LiteReason [55] Paper - text Qwen2.5-7B MLP semantic projection latent reasoning/efficiency 12/25 Palette [129] Paper - vision Qwen3-1.7B/other 2 VAE decoder token generation exploration/latent reasoning 12/25 JEPA-Reasoner [110] Paper - text transformer-based JEPA chains generation complex reasoning/robustness

- 12/25 LoLA [213] Paper - action Qwen2.5-VL-7B transformer feature alignment embodied manipulation/long-horizon








12/25 ColaVLA [152] Paper Code action LLaVA-v1.5-7B forward layer vision projection planning/autonomous driving 12/25 iCLP [25] Paper Code text Qwen2.5-0.5B/3B/7B VAE token generation latent planning/efficiency

- 01/26 LaST0 [128] Paper - action DeepSeek-LLM-1.5B MLP action projection embodied manipulation/efficiency

- 01/26 RB-CoT [63] Paper - text LLaMA3.1-8B/other 5 SAE feature generation multi-step reasoning/prompting

- 01/26 RISER [257] Paper Code text Qwen2.5-7B/other 3 vector library reusable chains zero-shot/generalization

- 01/26 Fast-ThinkAct [70] Paper - action Qwen2.5-VL-3B MLP action projection embodied manipulation/efficiency

- 01/26 GeoSteer [84] Paper - text Qwen3-8B/other 3 VAE projection complex reasoning/consistency

- 01/26 PREGEN [169] Paper - vision Qwen2.5-VL-7B/other 3 mixed layers embedding generation video retrieval/zero-shot

- 01/26 PILOT [289] Paper - text Qwen2.5-1.5B/other 2 MLP guidance synthesis robustness/generalization

- 01/26 PLaT [207] Paper Code text GPT2-0.1B linear layer semantic projection exploration/efficiency/generalization

- 01/26 ATP-Latent [292] Paper Code text LaMA3.2-1B VAE decoder token generation latent reasoning/generalization

- 01/26 ReGuLaR [205] Paper Code text LLaMA-3.2-1B VAE chain rendering latent reasoning/efficiency

- 02/26 CoLT [293] Paper - text LLaMA3.2-1B transformer decoder state unpacking tool calling/efficiency


- 02/26 PolarMem [30] Paper Code vision Qwen2.5-VL-7B/other 7 graph topology state storage long-horizon/hallucination mitigation


- 02/26 G-MemLLM [242] Paper - text GPT2-0.1B/LLaMA3.1-8B gated logic memory bank long-horizon/multi-hop reasoning


- 02/26 L2-VMAS [265] Paper Code vision Qwen3-VL-8B/other 8 vector library dual vision memory multi-agent collaboration/long-horizon


- 02/26 LatentMem [47] Paper Code text Qwen3-4B/LLaMA3.1-8B LoRA memory generation multi-agent collaboration


- 02/26 Interpeter [82] Paper - text LLaMA3.2-1B/other 2 LoRA ability transfer domain adaptation


- 02/26 Wormhole [124] Paper Code vision Qwen3-VL-2B/other 6 encoder-decoder vision projection multi-agent collaboration Auxiliary Model


- 09/24 HCoT [122] Paper - text LLaMA2-7B/13B LLM chain generation efficiency/generalization

02/25 SoftCoT [243] Paper Code text LLaMA3.1-8B LLM chain generation efficiency/generalization/zero-shot 05/25 UniVLA [14] Paper Code action Prismatic-7B vision encoder feature generation embodied manipulation/scaling 07/25 CTRLS [226] Paper - text LLaMA3.2-3B/Qwen2.5-3B external model state generation exploration/latent reasoning

- 09/25 SIM-CoT [220] Paper Code text GPT2-0.1B/other 3 LLM semantic alignment latent reasoning/efficiency




- 09/25 SSM-VLA [19] Paper - action LLaVA1.5-7B latent action model feature generation embodied manipulation/decision

- 09/25 LatentEvolve [274] Paper Code text LLaMA3.2-3B/other 3 LLM token generation experimental memory

- 10/25 3DThinker [28] Paper Code vision Qwen2.5-VL-7B/other 7 vision model feature generation spatial understanding/visual reasoning

10/25 SemCoT [61] Paper Code text LLaMA2-7B/Mistral-7B LLM alignment/generation complex reasoning/efficiency 11/25 LaRe [135] Paper - vision Qwen2.5-7B/Vicuna-7B diffusion model vision reconstruction visual understanding/efficiency

- 11/25 CoVT [156] Paper Code vision Qwen2.5-VL-7B vision model feature generation visual understanding/visual reasoning

- 12/25 SwiftVLA [142] Paper Code action SmolVLM-0.5B vision model feature generation embodied manipulation/efficiency


- 12/25 LCDrive [187] Paper - action Qwen3-0.5B world model feature generation autonomous driving/efficiency 12/25 VL-JEPA [21] Paper - vision LLaMA3.2-1B JEPA vision projection classification/retrieval 12/25 WholeBodyVLA [77] Paper Code action Prismatic-7B latent action model feature encoding embodied manipulation 12/25 SkiLa [197] Paper Code vision Qwen2.5-VL-7B vision encoder vision generation visual imagination/visual understanding


- 01/26 LatentVLA [235] Paper - action Qwen2.5-VL-3B latent action model feature generation planning/autonomous driving

- 01/26 LaViT [227] Paper Code vision Qwen2.5-VL-3B vision teacher model chain generation visual reasoning/efficiency/robustness

- 01/26 RoT [216] Paper Code vision Qwen3-VL-4B/other 2 vision encoder vision projection visual reasoning/accelerating/efficiency

- 02/26 MM-CoT [171] Paper - vision Qwen2.5-VL-7B diffusion model vision reconstruction visual imagination/visual understanding


- 02/26 VaLR [73] Paper - vision Qwen2.5-VL-7B vision encoder vision alignment visual imagination/visual reasoning


- 02/26 HIVE [284] Paper - vision Huginn-3.5B vision encoder vision injection visual reasoning/efficiency


- 02/26 DW-VLA [75] Paper - action InternVL3-2B extra encoder vision projection planning/autonomous driving


- 02/26 OneLatent [133] Paper - vision DeepSeek-MoE-3B vision encoder vision projection visual reasoning/efficiency

02/26 Future-VLA [44] Paper - action Qwen3-VL-4B vision encoder feature generation embodied planning/efficiency

- 03/26 LaST-VLA [132] Paper Code action InternVL3-2B/8B vision model feature generation spatial-temporal reasoning




the backbone largely frozen. We categorize existing approaches into five component families: Generation, Projection, Alignment, Control, and Storage, in view of their functional characteristics.

Generation Component. A major line of this part aims to construct intermediate latent states in hidden space, allowing the model to synthesize new implicit objectives, subgoals, or reasoning states that are not previously available as explicit symbols. A representative paradigm is realized as discrete tokens or a soft chain evolving rather than through explicit verbalized chains. For instance, ETD [87] introduces an encode–think–decode mechanism that shifts part of the process into latent computation without requiring explicit verbalization. At the same time, Palette [129], iCLP [25], ATP-Latent [292], and ReGuLaR [205] employ VAE-style components to modulate high-level contexts and encourage diverse exploration. At a coarser granularity, JEPA-Reasoner [110] formulates reasoning as a chain of latent predictions under a JEPA-style framework, thereby decoupling latent reasoning from surface token generation.

Beyond latent trajectory generation, another line of work leverages non-trajectory latent signals, e.g., compressed embeddings, activation-space features, or learned steering vectors. CoLaR [188], for example, enables more efficient silent reasoning through embedding prediction and control. More broadly, AR [64] and RB-CoT [63] both employ SAE to generate interpretable feature directions in activation space, while PILOT [289] synthesizes latent guidance vectors via an MLP to steer decoding. Additionally, MemGen [273], VisMem [264], and LatentMem [47] also adopt LoRA attached to the backbone to weave latent memories as an injection.

This idea has also been extended to the multimodal setting, where latent variables serve not only as semantic states but also as vision carriers. Recent works, such as AURORA [11], introduce a variational autoencoder to synthesize perception tokens, enabling richer visual understanding. CoMEM [229] and its agent variant CoMEM-Agent [230] deploy querying transformers to produce compact visual memory tokens, showing potential in long-horizon tasks. In addition, SteerVAD [18] generates related latent frame-level vision embeddings from mixed layers for video-based tasks, and Latent Sketchpad [276] uses a VAE decoder to generate intermediate visual imaginations during multi-step visual reasoning.

Projection Component. This category does not primarily synthesize new latent content, but instead improves reasoning or control by projecting existing internal representations into a different target space. Several works attach lightweight linear layers, e.g., SoftCoT++ [244] and PLaT [207], or MLPs, such as SpiralThinker [155] and LiteReason [55], that project hidden states into a target semantic space. Besides, LF-Steering [250] trains an SAE to project activations into a semantic subspace to ensure semantic consistency.

In another typical path, projection serves as a bridge across modalities or agents. Wormhole [124] connects heterogeneous visual agents through an encoder–decoder bridge that projects each agent’s visual representation into a shared latent space. OccVLA [118] projects 3D spatial features via a transformer adapter, improving unified multimodal understanding. Furthermore, as embodied scenarios advance, more researchers are focusing on action projection. For instance, LCLA [182] and LaST0 [128] attach MLP projectors in embodied manipulation. ThinkAct [69] and Fast-ThinkAct [70] both attach Q-former and MLP heads to project visual reasoning traces into robot action spaces. Combining both, VITA [136] adopts an encoder–decoder architecture to encode visual-action context into one latent representation, unifying perception and control in manipulation, while ColaVLA [152] introduces a forward layer that projects visual features into the action-planning space.

Alignment Component. While generation creates and projection reshapes, alignment ensures the transformed latent is anchored to something meaningful. These components enforce correspondence between latent representations and external grounding signals, whether visual features, task semantics, or cross-domain knowledge. AlignVLM [137] redesigns the cross-modal fusion layers, introducing mixed alignment layers that more faithfully bind visual tokens to textual semantics, while PREGEN [169] aligns generated video embeddings to retrieval-relevant textual semantics. Aligned with generative priors, LaDiR [83] and LoLA [213] align hidden states into diffusion-compatible or transformer-based semantic spaces, ensuring consistency with desirable grounding signals. Extending to cross-domain scenes, Interpreter [82] uses LoRA to transfer latent abilities across domains, aligning source-domain competencies with target-domain representations.

Control Component. It determines when and how the model enters, exits, or delegates latent modes. Rather than generating content, they act as meta-level switches or routers that adaptively modulate the generation process. To provide switching signals, FR-Ponder [62] trains a small MLP gating head to predict whether a

given input requires extended latent pondering, and TaH [49] positions a small MLP-style decider at each layer that votes on whether to enter a latent deliberation phase, enabling dynamic budget allocation in latent manifolds. MemGen [273] incorporates a trigger, implemented via LoRA or entropy signals, that determines when memory should be invoked, while Kelp [101] similarly uses an MLP-based module for risk-sensitive inputs in safety scenarios.

Storage Component. Storage components maintain persistent latent states across steps, turns, or episodes, enabling models to accumulate, compress, and retrieve information without relying on the finite context window. IMM [148] and L2-VMAS [265] introduce a differentiable vector library that acts as a latent memory bank, and G-MemLLM [242] scales this with a gated write–read logic that selectively updates memory. Further, PolarMem [30] replaces the flat vector store with a graph-topology structure that clusters and links visual memory across episodes.

Summary. Component-based methods preserve the backbone architecture while augmenting it with plug-in latent modules that construct, transform, align, control, or store internal representations for downstream generation. Rather than replacing the backbone, these components operate as functional operators over latent space, enhancing reasoning, grounding, controllability, and memory with minimal architectural disruption. Existing approaches can be broadly organized into five families: generation components that synthesize latent reasoning states; projection components that map hidden representations into task-relevant spaces; alignment components that anchor latents to external semantics or priors; control components that regulate latent computation adaptively; and storage components that maintain persistent latent storage.

- 4.1.3 Auxiliary Model


Here, the latent guidance signal is introduced by an external auxiliary model, rather than being natively induced within the backbone or instantiated by an internal functional component. Concretely, an auxiliary model first produces a latent representation and then is used to condition, guide, or refine the generation process of the host model:

z = Φaux(x), (5)

where the latent introduction is outsourced to auxiliary model Φaux(·) to replenish the host model Φback(·), then z will be injected into the autoregressive process in Equation 2.

This paradigm introduces a functional division of labour: the host model retains responsibility for downstream prediction, while the auxiliary model either shapes its learning objective or enriches its internal representations. The resulting works bifurcate cleanly into two families according to what the auxiliary model contributes: Supervision-oriented approaches that provide training signals, and Feature-oriented approaches that provide intermediate representations.

Supervision-oriented Auxiliary Model. For the methods in this paradigm, the auxiliary models supply signals that guide the host model with semantic constraints, regularization, and supervision. The most direct strategy is to leverage another language model serving as a teacher to generate expressive traces. For instance, HCoT [122] and LaViT [227] instantiate assistant models to generate explicit reasoning chains, whose internal representations are then distilled into the host hidden states. SoftCoT [243] extends this paradigm by projecting the auxiliary chain into a continuous latent embedding rather than discrete token sequences, yielding soft supervision compatible with gradient-based fine-tuning. For finer-grained supervision, some methods focus on aligning the host latent representations with those of an external reference model. SIM-CoT [220] and SemCoT [61] couple addition models whose hidden states function as semantic anchors, and train the host to reproduce these representations within its own latent space via a contrastive objective.

Another group treats the auxiliary model as a state generator whose outputs define structured training targets over latent trajectories. CTRLS [226] uses a small LLM to synthesise intermediate reasoning states that serve as exploration waypoints within the host latent space. LatentEvolve [274] extends this idea to evolutionary optimisation, employing an auxiliary model to generate candidate token sequences that drive iterative refinement of memory representations. CoLT [293] takes a more task-specific stance, assigning a tinyscale auxiliary model to decompose latent tool-calling states into interpretable intermediate representations that supervise the internal planning phase.

Feature-oriented Auxiliary Model. These auxiliary models shift the locus to features available for the host model, generating and injecting intermediate representations directly into the computation graph. This paradigm is especially prevalent in multimodal and embodied settings, where the heterogeneity between modalities, i.e., language, vision, and action, creates representational bottlenecks. A sizeable cohort of methods employs dedicated vision models whose outputs supplement or supplant the host’s own visual representations. CoVT [156] frames this injection as a chain of visual thought, wherein auxiliary vision models iteratively construct intermediate visual representations analogous to the token-level reasoning steps of textual CoT. 3DThinker [28] pairs a specialised 3D foundation model that provides spatially-grounded geometric priors. Further works, including LaRe [135], MM-CoT [171], and VaLR [73], leverage diffusion-architected generative models. Given a visual input, they reconstruct or imagine visual states whose latent codes are fed to the host model as an enriched perceptual context, enabling forms of visual imagination. OneLatent [133] and RoT [216] use a vision encoder to render textual reasoning into latent visual spaces. In addition, SkiLa [197] and VL-JEPA [21] further explore vision projection in generative and self-supervised regimes, respectively.

In embodied and autonomous systems, the role of the auxiliary model shifts to policy grounding and environment perception. UniVLA [14] incorporates a dedicated vision encoder to generate task-specific feature sequences, and SSM-VLA [19] introduces a VLM-based auxiliary that bridges visual perception and motor action within a state-space framework. SwiftVLA [142] and LaST-VLA [132] introduce spatial-temporal information through vision auxiliary, proving particularly beneficial for long-horizon manipulation tasks that demand coherent temporal reasoning. In autonomous driving, LCDrive [187] and DW-VLA [75] incorporate world models and extra vision encoders, respectively, as auxiliary feature sources, grounding consistent representations of scene dynamics. Future-VLA [44] takes this further by conditioning action generation on auxiliary-predicted future visual features, effectively rendering the auxiliary model as a predictive look-ahead mechanism. In addition, WholeBodyVLA [77] and LatentVLA [235] extend this to whole-body humanoid control by employing a latent action model as a feature encoder whose representations capture joint-level coordination structure.

Summary. The auxiliary-model paradigm introduces latent guidance through an external model rather than the backbone itself. Such auxiliary models either provide supervision signals to shape the backbone’s latent space or supply intermediate features that enrich its internal computation, making this paradigm particularly effective for complex reasoning, multimodal understanding, and embodied decision-making.

- 4.2 Representation


The transition from discrete token sequences to the continuous latent space H necessitates a precise definition of the core information carrier: the latent representation z ∈ H. Unlike discrete tokens x ∈ V, which are constrained to a predefined vocabulary, latent representations reside on a continuous, high-dimensional manifold, enabling substantially richer semantic expressivity [8, 58, 243].

Two central questions motivate the study of these methods: what information does a latent representation encode, and how is it integrated into the generative pipeline? The answers fundamentally determine the representational capacity, training dynamics, and generalization behavior of the resulting system. To provide a coherent organizational framework, we propose a taxonomy that classifies existing methods along two orthogonal axes: the subject of the representation (how z is structurally constructed, i.e., whether it is computed natively within the backbone or generated by a structurally independent module) and its parameterization (whether the construction process relies on fixed model states or incorporates dedicated trainable modules). As illustrated in Figure 6 and Table 4, the intersection of these axes yields a comprehensive taxonomy comprising four distinct paradigms, detailed as follows:

### Representation

![image 300](<2026-yu-latent-space-foundation-evolution_images/imageFile300.png>)

Forward Pass

![image 301](<2026-yu-latent-space-foundation-evolution_images/imageFile301.png>)

![image 302](<2026-yu-latent-space-foundation-evolution_images/imageFile302.png>)

External Represent.

###### ⋯

LM

Assistant

###### LM

![image 303](<2026-yu-latent-space-foundation-evolution_images/imageFile303.png>)

![image 304](<2026-yu-latent-space-foundation-evolution_images/imageFile304.png>)

Hidden State KV Cache

...

Embed.

Embed.

Inject the external states from pre-trained foundation models, teacher language model, etc.

Utilize the internal states including token embeddings, hidden states, KV caches, etc.

Internal External

![image 305](<2026-yu-latent-space-foundation-evolution_images/imageFile305.png>)

![image 306](<2026-yu-latent-space-foundation-evolution_images/imageFile306.png>)

![image 307](<2026-yu-latent-space-foundation-evolution_images/imageFile307.png>)

Learned Represent.

Learned Represent.

![image 308](<2026-yu-latent-space-foundation-evolution_images/imageFile308.png>)

External Represent. Learnable Param.

LM Learnable Param.

###### LM

![image 309](<2026-yu-latent-space-foundation-evolution_images/imageFile309.png>)

![image 310](<2026-yu-latent-space-foundation-evolution_images/imageFile310.png>)

![image 311](<2026-yu-latent-space-foundation-evolution_images/imageFile311.png>)

![image 312](<2026-yu-latent-space-foundation-evolution_images/imageFile312.png>)

![image 313](<2026-yu-latent-space-foundation-evolution_images/imageFile313.png>)

...

Learn by trainable modules, including continuous virtual tokens, lightweight adapters, etc.

First use trainable modules to create representations, then inject them into the backbone.

Hybrid

Learnable

###### Figure 6 The schematic diagram of Representation mechanism, including four sub-types: Internal (Section 4.2.1), External (Section 4.2.2), Learnable (Section 4.2.3), and Hybrid (Section 4.2.4).

Mechanism: Representation

- • Internal (Section 4.2.1): operates directly on activations produced during the backbone’s forward pass, including token embeddings, intermediate hidden states, and KV caches.
- • External (Section 4.2.2): derived from a structurally independent auxiliary system (e.g., a pre-trained encoder), and injects these exogenous signals into the backbone as conditioning inputs or supervision targets while the auxiliary source remains frozen.
- • Learnable (Section 4.2.3): constructed by dedicated trainable modules (e.g., continuous virtual tokens or lightweight adapters) that are embedded directly into the backbone and optimized end-to-end under specific task objectives.
- • Hybrid (Section 4.2.4): combines the Learnable and External paradigms sequentially by first using trainable modules to create specialized representations, then injecting these states as exogenous signals into the backbone for conditioning or latent supervision.


- 4.2.1 Internal


In the internal paradigm, z is derived exclusively from endogenous activations generated during the backbone’s standard forward pass, without introducing any additional parameters. Let Φback consist of L transformer blocks decomposed as:

Φback = ϕhead ◦ ϕL ◦ ··· ◦ ϕl ◦ ··· ◦ ϕ1 ◦ ϕemb, (6)

where ϕemb : V → Rd maps discrete tokens to continuous embeddings via the embedding matrix E ∈ R|V|×d, each transformer block ϕl : Rd×T → Rd×T processes the full sequence of T tokens, and ϕhead projects the final hidden states back to the vocabulary space. Let htl ∈ Rd denote the hidden state of token t at layer l, and let Hl = h1l ,...,hTl ∈ RT×d collect all token states at layer l. The latent representation is then a deterministic readout:

z = g({Hl}l∈S), (7)

- where g(·) is a parameter-free aggregation function applied over the set of layer activations S (e.g., index selection, mean pooling across tokens, or a fixed linear combination over layers). Depending on which


- Table 4 Overview of the Internal (Section 4.2.1), External (Section 4.2.2), Learnable (Section 4.2.3), and Hybrid


- (Section 4.2.4) representation. We compare the modality, backbone, representation subject, and scenario.


Date Method Paper Code Modality Backbone Subject Scenario Internal

###### 10/24 CoE [217] Paper Code text LLaMA2-7B/other 6 embedding/hidden state label-free self-evaluation

- 10/24 VTI [119] Paper Code vision LLaVA1.5-7B/other 2 hidden state hallucination mitigation

- 12/24 COCONUT [58] Paper Code text GPT2-0.1B the last hidden state latent reasoning/efficiency 05/25 Soft Thinking [287] Paper - text LLaMA3.1-8B/other 3 weighted embedding latent reasoning/efficiency 05/25 CoT2 [52] Paper Code text GPT2-0.1B weighted embedding exploration/complex reasoning 05/25 CGC-VTD [212] Paper Code vision Chameleon-7B/other 2 hidden state hallucination mitigation

- 08/25 LFJ [237] Paper - text Vicuna-7B/other 4 hidden state jailbreak attack

- 09/25 SIM-CoT [220] Paper Code text LaMA3.2-1B/3B/8B hidden state latent reasoning/efficiency

- 10/25 LatentBreak [140] Paper - text LLaMA2-7B/other 8 hidden state jailbreak attack

10/25 SALS [139] Paper - text LLaMA2-7B/Mistral-7B compressed kv-cache accelerating/efficiency 10/25 IVT-LR [20] Paper Code vision Qwen2-VL-7B/Chameleon-7B image embedding/hidden state visual reasoning/efficiency

- 11/25 LRP [253] Paper - vision Qwen-VL-2.5/Gemma3-12B hidden state/attention weight abstention/generalization

- 11/25 LatentMAS [300] Paper Code text Qwen3-4B/8B/14B hidden state/kv-cache multi-agent collaboration

- 01/26 CLReg [191] Paper - text LLaMA3.1-8B/other 2 hidden state forgetting mitigation

- 01/26 CausalEmbed [71] Paper - vision PaliGemma-3B/Qwen2.5-VL-3B the last hidden state visual document retrieval

- 02/26 LT-Tuning [123] Paper Code text LLaMA3.2-1B/3B/8B weighted embedding/hidden state latent reasoning/dynamic reasoning


- 02/26 JLT [81] Paper - text LLaMA3.1-8B hidden state jailbreak defense


- 02/26 ThinkRouter [241] Paper - text Qwen3-8B/other 3 weighted embedding dynamic reasoning/efficiency External

- 02/25 CODI [174] Paper Code text GPT2-0.1B/LLaMA3.2-1B teacher hidden state latent reasoning/efficiency

- 02/25 SoftCoT [243] Paper Code text LLaMA3.1-8B assistant hidden state efficiency/generalization/zero-shot 07/25 GoK [16] Paper - text Mistral-7B pretrained embedding exploration/diverse generation

- 09/25 OccVLA [118] Paper - action PaliGemma2-3B pretrained 3D occupancy token spatial understanding

- 10/25 KaVa [91] Paper - text LLaMA3.2-1B/other 2 teacher compressed kv-cache latent reasoning/efficiency

- 10/25 3DThinker [28] Paper Code vision Qwen2.5-VL-7B/other 7 pretrained 3D token spatial understanding/visual reasoning

- 11/25 COVT [156] Paper Code vision Qwen2.5-VL-7B pretrained visual token visual understanding/visual reasoning

- 12/25 Mull-Tokens [160] Paper - vision Qwen2.5-VL-7B pretrained multimodal token latent reasoning


12/25 LCDrive [187] Paper - action Qwen3-0.5B pretrained action/world model token autonomous driving/efficiency 12/25 SkiLa [197] Paper Code vision Qwen2.5-VL-7B pretrained sketch token visual imagination/understanding 12/25 VL-JEPA [21] Paper - vision LLaMA3.2-1B pretrained text embedding classification/retrieval 02/26 LaRA-VLA [5] Paper Code action Qwen3-VL-8B pretrained visual/action token embodied manipulation 02/26 OneLatent [133] Paper - vision DeepSeek-MoE-3B pretrained hidden state visual reasoning/efficiency 03/26 LaSER [80] Paper - text Qwen3-0.6B/other 5 teacher hidden state complex reasoning/dense retrieval

Learnable

05/25 CoLaR [188] Paper Code text LLaMA3.2-1B compressed reasoning embedding dynamic reasoning/efficiency 05/25 Comma [185] Paper - text LLaMA3.2-1B learnable latent token generalization

- 07/25 CTRLS [226] Paper - text LLaMA3.2-3B/Qwen2.5-3B iteratively updated latent states exploration/latent reasoning

- 08/25 MCOUT [154] Paper - vision LLaMA3.2-1B fused thought embedding visual reasoning/latent reasoning

- 09/25 LatentGuard [179] Paper - text Gemini2.5 Pro disentangled latent code security/attacks refusal

- 09/25 MARCOS [115] Paper - text Qwen2.5-0.5B/3B iteratively updated latent states latent reasoning/efficiency

- 10/25 C2C [48] Paper Code text Qwen3-0.6B/Qwen2.5-0.5B fused kv-cache multi-agent collaboration

- 11/25 Interlat [42] Paper - text Qwen2.5-7B/other 2 adapted hidden state multi-agent collaboration

- 12/25 LIVR [100] Paper - vision Qwen3-VL-4B learnable latent token visual reasoning/multi-task


- 01/26 KVCA [38] Paper - text Gemma2-2B aligned kv-cache inter-agent communication

- 01/26 TCLA [144] Paper - action Qwen2.5-VL-7B/other 23 learnable latent action token embodied manipulation

- 01/26 UniCog [116] Paper Code text Qwen3-8B/other 3 learnable latent mind cognitive reasoning/interpretability

- 02/26 CoLT [293] Paper - text LLaMA3.2-1B latent tool calling tool calling/efficiency


- 02/26 DeltaKV [57] Paper Code text LLaMA3.1-8B/other 3 compressed kv-cache complex reasoning/efficiency


- 02/26 MAS4TS [163] Paper - text Qwen3-VL-235B reconstructed latent trajectory visual reasoning/time series analysis Hybrid


- 09/24 HCoT [122] Paper - text LLaMA2-7B/13B special CoT token efficiency/generalization 12/24 AURORA [11] Paper Code vision LLaVA1.5-13B discrete perception token visual perception 12/24 DCA [117] Paper - text Gemma2-2B augmented kv-cache latent reasoning/zero-shot

- 02/25 Assorted [181] Paper - text LLaMA3.2-1B/3B/8B compressed CoT token latent reasoning/efficiency 05/25 CoMEM [229] Paper Code vision Qwen2-VL-7B/Qwen2.5-VL-7B latent memory visual reasoning/long-horizon/efficiency 05/25 UniVLA [14] Paper Code action Prismatic-7B latent action token embodied manipulation/scaling 07/25 DEP [157] Paper Code text Qwen2.5-7B/32B compressed embedding personalization

09/25 GainRouter [288] Paper - text Qwen3-4B latent codebook of strategy priors latent reasoning/adaptive reasoning

- 09/25 MemGen [273] Paper Code text SmolLM3-3B/Qwen3-8B latent memory experimental memory/generalization

- 10/25 Latent-SFT [37] Paper Code text LLaMA3.2-1B/other 2 compressed CoT token latent reasoning/efficiency

10/25 ThoughtComm [290] Paper - text Qwen3-0.6B/other 4 latent thought multi-agent collaboration 11/25 CLaRa [59] Paper Code text Mistral-7B/Phi4-Mini-3.8B compressed representation retrieval/efficiency

- 11/25 EBM-CoT [29] Paper - text Qwen2.5-7B/other 5 latent thought latent reasoning/efficiency


11/25 Monet [211] Paper Code vision Qwen2.5-VL-7B latent thought visual reasoning/generalization 11/25 VisMem [264] Paper Code vision Qwen2.5-VL-7B/other 8 latent visual memory visual understanding/visual reasoning 11/25 LatBot [105] Paper - action InternVL3.5-2B latent action token embodied manipulation 11/25 VITA [136] Paper Code action PaliGemma-3B dynamics-unified token embodied manipulation 12/25 iCLP [25] Paper Code text Qwen2.5-0.5B/3B/7B latent plan latent planning/efficiency 12/25 Motus [10] Paper Code action Qwen3-VL-2B latent action token embodied manipulation

- 01/26 RB-CoT [63] Paper - text LLaMA3.1-8B/other 5 prompt-sensitive latent token multi-step reasoning/prompting

- 02/26 LatentChem [259] Paper Code text Qwen3-8B latent thought/molecular token chemical reasoning


- 02/26 UniLACT [51] Paper - action GPT2-0.1B latent action token embodied manipulation/generalization






















activation type is extracted, internal representations manifest in three principal forms: Hidden State, Weighted Embedding, and Cache.

Internal Hidden State. As the most prevalent form, intermediate activations are extracted to provide a continuous summary of the model’s evolving computation. Common instantiations include taking the last hidden state of position T, or computing a mean-pooled representation across all tokens at a particular layer l:

z = hTL or

T

1 T

htl. (8)

t=1

For example, COCONUT [58] establishes a foundational pattern for continuous generation by feeding the last hidden state directly back as the next input embedding, bypassing discrete vocabulary projection and forming a recurrent loop of continuous “thoughts”. SIM-CoT [220] and LatentMAS [300] adopt this recurrent paradigm. Beyond direct generation, the rich semantic geometry of hidden states proves valuable in downstream applications. For instance, CoE [217] constructs chains of embeddings from pooled hidden states to perform label-free self-evaluation. In multimodal settings, internal activations frequently serve as diagnostic and corrective signals: VTI [119] and CGC-VTD [212] dynamically probe intermediate hidden states to detect and mitigate visual hallucinations. Final hidden states have also been repurposed as compressed visual-semantic summaries: IVT-LR [20] fuses them with image embeddings for efficient visual reasoning, while CausalEmbed [71] projects them into dense representations for visual document retrieval. Because these states natively encode pre-trained knowledge, CLReg [191] further leverages them as a regularizer to mitigate catastrophic forgetting. The high expressivity of endogenous states is, however, a double-edged sword from a security perspective. On the offensive side, LFJ [237] and LatentBreak [140] exploit hidden-state vulnerabilities to mount latent jailbreak attacks that bypass discrete text-level filters. Conversely, JLT [81] monitors these same signals defensively, using them to detect malicious intent and improve jailbreak robustness.

Internal Weighted Embedding. This form replaces hard token sampling with a soft, probability-weighted combination over the vocabulary embedding matrix E ∈ R|V|×d. Let α ∈ R|V| denote a weight vector derived from the model’s output logits (i.e., via softmax); the latent representation is:

z = E⊤α, α = softmax(o), (9)

where o ∈ R|V| denotes the pre-softmax logits. Because α lies in the probability simplex, z is constrained to the convex hull of the vocabulary embedding vectors.

This differentiable relaxation forms a superposition of candidate token embeddings [52, 287], enabling gradient flow through the discrete generation step and facilitating parallel exploration of the reasoning space. LT-Tuning [123] builds on this property with a context-prediction fusion mechanism that exploits predictive semantic guidance from the vocabulary embedding space to construct robust latent thoughts. ThinkRouter [241] further leverages the continuous nature of z for confidence-aware routing, dynamically switching between continuous latent thinking and discrete token generation based on model uncertainty.

Internal Cache. The third form treats accumulated key-value pairs as structured latent memory, enabling efficient context reuse without recomputation. Given the hidden states Hl ∈ RT×d, the cache representations are computed via learned projection matrices:

kl = HlWlk, vl = HlWlv, (10) where Wlk,Wlv ∈ Rd×d

k project the sequence into the key and value spaces of the attention heads.

By treating these compressed tensors as operational memory, SALS [139] exploits sparse attention patterns over the KV cache to accelerate inter-step computation and improve inference efficiency. LatentMAS [300] extends this to multi-agent collaboration, using the KV cache as a shared, continuous working memory that enables agents to coordinate without explicit textual communication. In the multimodal domain, LRP [253] combines attention weights and hidden states to capture richer visual semantics, demonstrating improved abstraction and generalization on complex visual tasks.

Summary. The internal paradigm converts endogenous model activations into parameter-free latent representations, entirely bypassing the discrete vocabulary bottleneck. By treating standard computational byproducts

###### as versatile semantic assets, it demonstrates that intrinsic model states carry sufficient representational capacity to support continuous reasoning, accelerate inference, and enable robust downstream analysis.

- 4.2.2 External


In the external paradigm, z originates from an auxiliary encoder Φaux that is structurally independent of the backbone. Given an auxiliary input xaux, which may coincide with x or belong to a different modality:

z = Φaux(xaux), (11)

where Φaux is kept frozen during backbone training. Because Φaux and Φback operate in distinct latent manifolds with potentially mismatched dimensionalities (daux ̸= dback), z requires explicit structural alignment before integration. Depending on its functional role, this paradigm operates in two modes.

First, as a conditioning input to guide backbone generation, z is first aligned to the backbone’s native latent space via a learned projection ψ : Rd

back (e.g., a linear map or MLP), and the backbone conditions its output on the projected signal:

→ Rd

aux

zˆ = ψ(z), y ∼ Φback(· | [zˆ; x]), (12) where [zˆ; x] denotes a latent integration mechanism such as prefix concatenation or cross-attention injection. Second, as a supervision target for representation alignment or knowledge distillation, z serves as a dense, non-verbalized supervision target. The backbone’s internal state h is trained to match the projected external signal. This continuous supervision transfers rich semantic priors from Φaux to the backbone without the information bottleneck imposed by discrete token generation. Based on the modality and functional role of Φaux, we identify three directions: Reasoning Priors, Perceptual Priors, and Embodied Priors.

External Reasoning Priors. Here, the auxiliary source operates in the semantic domain to supply the backbone with structured logic and cognitive traces. A prevalent strategy is knowledge distillation from an expert reasoning model. CODI [174] formalizes this via a self-distillation loop in which the frozen teacher’s hidden states serve as continuous supervision targets, guiding the implicit reasoning of the student. SoftCoT [243] extends this concept to explicit injection: a lightweight assistant model generates speculative reasoning chains that are projected into soft-token embeddings and prepended to the backbone input, creating a gradient-compatible conditioning signal that substantially improves zero-shot generalization. KaVa [91] bypasses intermediate output tokens entirely by distilling the teacher’s compressed KV cache, directly transferring structured attention states as compact latent priors.

External Perceptual Priors. Here, pre-trained vision encoders or specialized multimodal auxiliary models supply spatially, temporally, or structurally rich feature maps to augment a primarily textual backbone. 3DThinker [28] injects spatially grounded 3D tokens from a specialized auxiliary network to supply geometric priors that the base model cannot derive from two-dimensional inputs alone. SkiLa [197] leverages pre-trained sketch tokens to interleave intermediate visual thoughts with textual reasoning, explicitly grounding the model’s spatial understanding. VL-JEPA [21] employs pre-trained embeddings from a predictive-coding model in an abstract representation space to improve cross-modal classification and retrieval. COVT [156] uses an auxiliary vision model to iteratively extract visual tokens and fuse them into the backbone to construct continuous visual thought chains. OneLatent [133] demonstrates that hidden states from a strong visionlanguage model can condense rich perceptual and OCR context into a single latent token for highly efficient visual reasoning. Mull-Tokens [160] generalizes this injection with modality-agnostic latent tokens derived from an auxiliary system, enabling uniform latent reasoning across both linguistic and visual substrates.

External Embodied Priors. This direction, prevalent in embodied models and autonomous driving, relies on auxiliary models to generate structured latent representations of environmental dynamics, 3D geometry, and future actions. OccVLA [118] applies pre-trained 3D occupancy tokens as a supervisory signal to impart fine-grained spatial understanding without requiring explicit 3D inputs at inference time. LCDrive [187] incorporates an external world model to generate action and scene tokens that inject temporally consistent representations of scene dynamics, grounding the host model’s navigational reasoning. LaRA-VLA [5] bridges continuous perception and motor control by utilizing pre-trained visual and action tokens, enabling a

smooth transition from explicit multimodal supervision to internalized latent reasoning for complex embodied manipulation.

Summary. The external paradigm provides a principled approach to bridging modality gaps and circumventing the discrete token bottleneck by injecting structured knowledge from independent auxiliary systems. By aligning reasoning, perceptual, and embodied priors as either dynamic conditioning signals or dense supervision targets, it endows the backbone with continuous reasoning capabilities and complex structural constraints without modifying the backbone’s parameters. This demonstrates that a foundation model’s representational scope is not strictly bounded by its native architecture: leveraging specialized latent priors offers a scalable pathway to expand semantic reach while keeping the backbone largely frozen.

- 4.2.3 Learnable


In the learnable paradigm, z is actively constructed by a parameterized module Φcomp with learnable parameters θ that is directly embedded within the backbone architecture (e.g., continuous virtual tokens or lightweight adapters). Let c denote an optional conditioning context, such as the input x, intermediate hidden states h, or the empty set (c = ∅). The latent representation is formulated as:

z = Φcomp(c; θ). (13)

Unlike the external paradigm, Φcomp is structurally coupled with the backbone. The parameters θ are optimized end-to-end driven by specific task objectives (either independently with a frozen backbone or jointly with θback). Depending on the targeted optimization objective, learnable representations manifest in three primary forms: Compression Learning, Distribution Learning, and Alignment Learning.

Compression Learning. The first class is driven by information-bottleneck principles, optimizing Φcomp to compress explicit data into dense, continuous vectors. CoLaR [188] learns to aggregate consecutive reasoning tokens into compressed embeddings using a variance-preserving scaling factor. CoLT [293] employs supervised learning to condense long reasoning trajectories into continuous seed tokens for parametric tool calls. In the multimodal domain, LIVR [100] imposes a visual bottleneck during training, requiring the model to learn implicit spatial compressions without relying on explicit textual descriptions. At the memory level, DeltaKV [57] encodes residual differences between successive cache states to substantially compress long-term reasoning overhead.

Distribution Learning. The second class abandons deterministic point mappings, instead optimizing Φcomp to capture the underlying stochastic distributions and structural manifolds of reasoning. CTRLS [226] formulates reasoning as a Markov decision process and models state transitions via Dirichlet distributions to capture epistemic uncertainty. MARCOS [115] employs a conditional hidden Markov model with step-level latent variables, relying on variational training to learn stochastic continuous representations. UniCog [116] formulates cognitive distributions as a latent variable model, optimizing an evidence lower bound to project activations into a high-dimensional sparse space. LatentGuard [179] learns to model the latent space using a VAE, manipulating the resulting semantic distributions to enable robust refusal of adversarial inputs.

Alignment Learning. The third class optimizes Φcomp to construct cross-space projections, bridging rigid boundaries such as distinct modalities or heterogeneous agent architectures. KVCA [38] learns a globally shared latent manifold Σ via cross-attention to translate KV caches between architecturally heterogeneous models. C2C [48] trains a neural MLP to directly project KV caches between specific models by aligning their terminal-layer representations. Interlat [42] optimizes communication adapters via a weighted JensenShannon divergence to align transmitted hidden states with the receiving agent’s internal representations. This paradigm also bridges modalities: MCOUT [154] learns cross-modal attention fusion while penalizing entropy collapse; MAS4TS [163] learns to reconstruct predictive numerical trajectories from visual time-series plots; and TCLA [144] aligns noisy observational signals with clean, VLM-prompted latent action targets for embodied manipulation.

Summary. The learnable paradigm excels at acquiring latent structures explicitly optimized for specific downstream objectives, breaking free from the rigid semantic boundaries imposed by textual pre-training. This flexibility allows models to encode non-verbal modalities (e.g., complex spatial layouts and embodied actions) and support high-bandwidth inter-agent collaboration. However, granting unconstrained optimization

###### access to continuous spaces introduces the risk of manifold overfitting: modules may memorize the noise in supervision signals, yielding highly specialized representations that sacrifice zero-shot generalization. Rigorous regularization, including enforced structural sparsity, variance-preserving normalizations, and controlled belief-shift tuning, which is therefore essential to maintain broad utility.

- 4.2.4 Hybrid


The hybrid paradigm utilizes a dedicated, structurally independent module Φcomp with learnable parameters θ to construct a structured latent representation. Let c denote a conditioning context drawn from the input x or auxiliary features. The hybrid representation is formulated as:

z = Φcomp(c; θ). (14)

Crucially, unlike the Learnable paradigm, Φcomp remains architecturally disjoint from the backbone Φback. Once constructed, z is deployed in the same manner as the External paradigm: it acts either as an exogenous conditioning signal injected into a typically frozen backbone (serving as a learned alignment bridge), or as a rich, optimized supervision target for latent distillation. This approach can be summarized into three functional categories: Traces, Grounding, and Augmentation.

Traces. The first branch distills discrete reasoning trajectories into compact continuous vectors that guide the backbone without the latency of explicit chain-of-thought generation. HCoT [122] compresses multi-step reasoning into a specialized thought token injected into a frozen decoder to accelerate inference. Assorted [181] combines latent and text tokens by compressing reasoning segments via a VQ-VAE codebook. Latent-SFT [37] restricts the latent space to the column space of the pre-trained vocabulary matrix via induction-supervision masking. EBM-CoT [29] refines thought trajectories toward lower-energy regions via Langevin dynamics calibration. GainRouter [288] learns a codebook of discrete strategy priors to condition single-pass decoding on continuous thinking vectors. ThoughtComm [290] employs a sparsity-regularized autoencoder to transmit latent thoughts between agents. For specialized domains, LatentChem [259] aligns projected molecular representations with linguistic spaces, while iCLP [25] and RB-CoT [63] generate prompt-sensitive latent plans to guide multi-step reasoning.

Grounding. The second branch translates continuous sensory or control signals into structured latent tokens, grounding the frozen backbone in physical reality. In the visual domain, AURORA [11] trains a VQ-VAE to produce discrete visual latent codes that enhance spatial perception, while Monet [211] generates continuous embeddings as intermediate visual thoughts via multi-stage distillation. In embodied robotics, UniVLA [14] derives task-centric latent actions from heterogeneous videos and projects them into a unified action space. LatBot [105] decomposes latent actions into discrete motion and scene tokens; Motus [10] extracts pixel-level delta actions via optical flow; UniLACT [51] constructs depth-aware latent action representations from RGB-D frames; and VITA [136] maps visual-action dynamics into unified codebooks.

Augmentation. The third branch condenses large contextual histories into compressed soft prompts or dynamically augmented cache states, extending effective context beyond standard window limits. DCA [117] generates latent embeddings via an offline coprocessor and appends them directly to the KV cache, enriching context without altering the decoding architecture. CLaRa [59] encodes lengthy documents into compact memory tokens via a salient compressor trained on synthetic data, enabling end-to-end optimization of the retrieval representation space. DEP [157] isolates user-specific interaction patterns via a sparse autoencoder and injects them as soft prompts for personalized generation. In multimodal settings, VisMem [264] and CoMEM [229] construct dedicated visual memory tokens that distill episodic experiences for long-horizon planning, while MemGen [273] integrates episodic representations into computation for self-evolving behavior.

Summary. Hybrid representations are particularly suited to complex, multimodal, or domain-specialized settings in which the gap between raw inputs and the backbone’s textual manifold creates bottlenecks that neither purely internal nor purely learnable approaches can adequately resolve. By first constructing a task-specific latent representations via targeted learnable acquisition and subsequently deploying it as a structured external conditioning signal, hybrid approaches achieve a dual advantage: semantic fidelity, grounding representations in the raw input modality; and computational efficiency, sparing the backbone from processing raw, high-dimensional inputs at inference time.

##### Computation

... ...

Compress the volume of chains/caches/intermediate representations, etc.

Expand the depth or width by recurrent/looped/ parallel, superposition, etc.

Compressed Expanded

![image 314](<2026-yu-latent-space-foundation-evolution_images/imageFile314.png>)

...

Improve the adaptive ability via dynamic/selective/ iterative updating, etc.

Enable interleaved mediums by explicit-latent/textvision/reasoning-memory, etc.

Adaptive Interleaved

- Figure 7 The schematic diagram of Computation mechanism, including four sub-types: Compressed (Section 4.3.1), Expanded (Section 4.3.2), Adaptive (Section 4.3.3), and Interleaved (Section 4.3.4).


- 4.3 Computation


In recent years, research on latent-level computation has advanced rapidly, reflecting a broader departure from the conventional paradigm in which language models perform inference through fixed-depth, token-by-token generation [46, 297]. Instead, a growing body of work aims to equip models with more flexible, efficient, and scalable computational mechanisms by shifting part of the reasoning process to the latent space.

To enable a systematic analysis, a central question to consider is: what kinds of computational operations are performed in the latent space? From this perspective, existing methods can be organized along the dimension of operation, yielding four major categories. Specifically, based on their underlying computational operations, as illustrated in Figure 7 and Table 5, we classify existing approaches into four representative types:

Mechanism: Computation

- • Compressed (Section 4.3.1): reduces the volume of explicit traces, internal states and crossmodal features, enhancing the efficiency while preserving expressiveness.
- • Expanded (Section 4.3.2): increases the effective computation by expanding computation along depth or width by recurrent, looped, parallel, superposition, and structural designs, enabling higher information bandwidth.
- • Adaptive (Section 4.3.3): allocates computation adaptively instead of a fixed budget by dynamic depth, width, shortcuts, halting, semantic-unit boundaries adaptation, and control adaptation, balancing capacity and efficiency flexibly.
- • Interleaved (Section 4.3.4): interleave heterogeneous generation medias to bridge explicit-latent, language-vision, reasoning-memory, or planning-perception.


- 4.3.1 Compressed


This paradigm subsumes approaches that project an explicit trajectory r ∈ V onto a semantically dense latent representation z. A compression operator Φ(·) acts upon the intermediate hidden states h to yield:

z = Φ(h), |z| ≪ |h|, (15)

where Φ(·) may be realized as both a functional component Φcomp(·) or the backbone Φback itself, reducing autoregressive overhead while preserving the semantic fidelity requisite for faithful downstream decoding.

- Table 5 Overview of the Compressed (Section 4.3.1), Expanded (Section 4.3.2), Adaptive (Section 4.3.3), and Interleaved


- (Section 4.3.4) computation. We compare the modality, backbone, computational operation, and scenario.


Date Method Paper Code Modality Backbone Operation Scenario Compressed

###### 09/24 HCoT [122] Paper - text LLaMA2-7B/13B semantic alignment efficiency/generalization

- 12/24 CCoT [31] Paper - text LLaMA2-7B variable sequence latent reasoning/efficiency 02/25 SoftCoT [243] Paper Code text LLaMA3.1-8B semantic projection efficiency/generalization/zero-shot

- 02/25 CODI [174] Paper Code text GPT2-0.1B/LLaMA3.2-1B self distillation latent reasoning/efficiency/generalization 05/25 CoLaR [188] Paper Code text LLaMA3.2-1B dynamic compaction dynamic reasoning/efficiency

10/25 KaVa [91] Paper - text LLaMA3.2-1B/other 2 cache distillation latent reasoning/efficiency 10/25 SALS [139] Paper - text LLaMA2-7B/Mistral-7B cache projection accelerating/efficiency

- 01/26 LatentVLA [235] Paper - action Qwen2.5-VL-3B vision projection planning/autonomous driving

- 01/26 RoT [216] Paper Code vision Qwen3-VL-4B/other 2 text-to-vision rendering visual reasoning/accelerating/efficiency

- 02/26 DeltaKV [57] Paper Code text LLaMA3.1-8B/other 3 semantic residual encoding complex reasoning/efficiency


- 02/26 OneLatent [133] Paper - vision DeepSeek-MoE-3B text-to-vision rendering visual reasoning/efficiency


- 02/26 Future-VLA [44] Paper - action Qwen3-VL-4B information densification embodied planning/efficiency Expanded


- 02/25 Huginn [50] Paper Code text Huginn-3.5B recurrent depth latent reasoning/scaling

- 02/25 Loop [167] Paper - text decoder-only-1.5B looped transformer exploration/multi-step reasoning 05/25 SoftCoT++ [244] Paper Code text LLaMA3.1-8B parallel paths exploration/zero-shot/scaling

- 05/25 CoT2 [52] Paper Code text GPT2-0.1B parallel sampling exploration/complex reasoning

- 06/25 PCCoT [224] Paper Code text GPT2-0.1B/LLaMA3.2-1B parallel iteration latent reasoning/efficiency 10/25 Bubbles [113] Paper Code text decoder-only-1.9B/other 3 parallel width scaling/zero-shot/unsupervised learning 10/25 ETD [87] Paper - text OLMo-2-1B recursive iteration multi-step reasoning/zero-shot 10/25 LatentTTS [262] Paper Code text GPT2-0.1B/LLaMA3.2-1B parallel sampling latent reasoning/exploration/scaling


- 10/25 Latent-SFT [37] Paper Code text LLaMA3.2-1B/other 2 chain superposition latent reasoning/efficiency

- 10/25 Ouro [296] Paper - text LoopLM-1.4B/2.6B looped model pretraining scaling/efficiency/faithful reasoning

12/25 ColaVLA [152] Paper Code action LLaVA-v1.5-7B hierarchical parallel planning/autonomous driving

- 01/26 PLR [193] Paper - text transformer-based parallel width sequential recommendation

- 01/26 Laser [218] Paper Code vision Qwen2.5-VL-7B feature superposition visual reasoning/efficiency/generalization

- 02/26 RD-VLA [198] Paper - action MiniVLA-0.5B recurrent-depth embodied planning/decision


- 02/26 LoopFormer [72] Paper Code text decoder-only elastic looped transformer latent reasoning/scaling Adaptive


- 05/25 System-1.5 [214] Paper - text LLaMA3.2-1B dynamic shortcuts cognitive reasoning/efficiency

- 09/25 FR-Ponder [62] Paper - text LLaMA3-8B/other 4 instance-adaptive steering dynamic reasoning/efficiency/generalization

11/25 TaH [49] Paper Code text Qwen3-0.6B/1.7B selective iterations dynamic reasoning/complex reasoning 11/25 LWS [146] Paper Code text LLaMA3.2-1B adaptive halting dynamic reasoning/efficiency 12/25 DLCM [158] Paper - text DLCM-2.3B concept boundaries concept-level/zero-shot/scaling

- 01/26 PRE [125] Paper Code text GPT-J-6B/LLaMA3.2-8B selective extraction latent reasoning/multi-hop reasoning

- 01/26 I2B-LPO [36] Paper Code text Qwen3-14B/Qwen2.5-37B dynamic branching exploration/policy optimization

- 01/26 RISER [257] Paper Code text Qwen2.5-7B/other 3 adaptive steering zero-shot/generalization

- 01/26 PLaT [207] Paper Code text GPT2-0.1B dynamic termination exploration/efficiency/generalization

- 01/26 Dreamer [86] Paper - text Dreamer-1B/2B depth-recurrent attention latent reasoning/scaling/efficiency

- 02/26 AL-CoT [267] Paper - text PonderLM2-0.5B/1.4B token-level adaption latent reasoning/dynamic reasoning

02/26 SpiralFormer [263] Paper - text Pythia-1.4B/other 3 looped transformers efficiency/scaling 03/26 PonderLM-3 [97] Paper - text PonderLM2-0.5B token-wise adaption latent reasoning/efficiency

- 03/26 AdaPonderLM [180] Paper - text Pythia-1.4B/other 4 token-wise adaptive depth latent reasoning/efficiency Interleaved




12/24 AURORA [11] Paper Code vision LLaVA1.5-13B text/perception visual perception

- 02/25 Assorted [181] Paper - text LLaMA3.2-1B/3B/8B text/latent latent reasoning/efficiency


06/25 Mirage [251] Paper Code vision Qwen2.5-VL-7B text/vision latent visual imagination/generalization

- 08/25 LCR-SER [177] Paper - text transformer-based history/reasoning working memory/search&recommendation

- 09/25 LVR [95] Paper Code vision Qwen2.5-VL-3B/7B text/vision latent visual understanding/zero-shot

- 09/25 MemGen [273] Paper Code text SmolLM3-3B/Qwen3-8B reasoning/memory experimental memory/generalization

- 10/25 SwiReasoning [175] Paper Code text Qwen3-8B/other 3 explicit/latent reasoning latent reasoning/efficiency

10/25 IVT-LR [20] Paper Code vision Qwen2-VL-7B/Chameleon-7B text latent/vision latent visual reasoning/efficiency 10/25 3DThinker [28] Paper Code vision Qwen2.5-VL-7B/other 7 text/3D latent spatial understanding/visual reasoning

- 10/25 LS [276] Paper Code vision Gemma3-12B/other 2 text/vision latent visual imagination/visual understanding

- 11/25 SpiralThinker [155] Paper - text LLaMA3.2-7B text/latent latent reasoning/complex reasoning

11/25 VisMem [264] Paper Code vision Qwen2.5-VL-7B/other 8 short/long vision memory visual understanding/visual reasoning 11/25 CLaRa [59] Paper Code text Mistral-7B/Phi4-Mini-3.8B retrieval/generation retrieval/efficiency 11/25 Monet [211] Paper Code vision Qwen2.5-VL-7B text/vision latent visual reasoning/generalization 12/25 LiteReason [55] Paper - text Qwen2.5-7B reasoning/latent latent reasoning/efficiency 12/25 ILVR [39] Paper Code vision Qwen2.5-VL-7B/Qwen3-VL-8B text/vision latent visual understanding/efficiency 12/25 DMLR [111] Paper Code vision Qwen2.5-VL-7B/other 5 text/perception visual understanding/grounding

- 12/25 SkiLa [197] Paper Code vision Qwen2.5-VL-7B text/vision latent visual imagination/visual understanding






- 01/26 FlashMem [65] Paper - text Qwen2.5-1.5B/other 3 reasoning/memory working memory/efficiency

- 02/26 L2-VMAS [265] Paper Code vision Qwen3-VL-8B/other 8 perception/thinking multi-agent collaboration/long-horizon


- 02/26 MM-CoT [171] Paper - vision Qwen2.5-VL-7B text/vision latent visual imagination/visual understanding


- 02/26 LatentMem [47] Paper Code text Qwen3-4B/LLaMA3.1-8B text/memory multi-agent collaboration










- 02/26 LT-Tuning [123] Paper Code text LLaMA3.2-1B/3B/8B text/latent latent reasoning/dynamic reasoning


- 02/26 ThinkRouter [241] Paper - text Qwen3-8B/other 3 explicit/latent reasoning dynamic reasoning/efficiency




Compressed computation aims to reduce the cost of explicit intermediate computation by mapping verbose reasoning trajectories or high-dimensional hidden states into compact latent representations, while preserving the semantic information necessary for accurate downstream decoding. Rather than eliminating reasoning altogether, this paradigm seeks to retain inferential content in a more information-dense form, thereby improving efficiency across textual, internal, and cross-modal reasoning processes in three forms: Traces Compression, States Compression, and Features Compression.

Traces Compression. Recent work on this direction can be organized around a shared goal: preserving inferential fidelity while reducing explicit trace lengths. HCoT [122] and SoftCoT [243] emphasize semantic alignment across abstraction levels, with HCoT [122] using hierarchical compression to skip redundant intermediate tokens and SoftCoT [243] projecting reasoning into a continuous soft-token space that decouples reasoning depth from discrete trace length, thereby supporting zero-shot transfer without task-specific retraining. In parallel, CCoT [31] models compression as variable-length latent allocation, assigning shorter representations to simpler inferences and richer ones to more complex deductions, while CODI [174] and CoLaR [188] focus on adaptive compaction through self-distillation and dynamic token-level control, respectively.

States Compression. A complementary and potentially deeper form of compression targets not the decoded token sequence but the internal cache, whose linear growth with sequence length has become a major bottleneck for long-context and reasoning-intensive inference. Recent work explores three main approaches. KaVa [91] formulates KV-cache compression as a knowledge distillation problem, training a student model to match the output distribution of a teacher operating over the full cache. SALS [139] instead adopts a lightweight, training-free strategy by projecting the cache into a low-rank principal subspace, arguing that the dominant directions are sufficient to preserve attention patterns with bounded error. DeltaKV [57] exploits the high correlation between KV-caches across successive reasoning steps, storing semantically compressed residuals rather than full cache states, and reports particularly strong gains on multi-step reasoning tasks where inter-step redundancy is greatest.

Features Compression. Recent work on latent-space compression has moved beyond text to multimodal and embodied settings, where the main bottleneck is the high-dimensional visual and action representations used in perception–action loops such as autonomous driving, robot manipulation, and embodied navigation. In visual reasoning, RoT [216] renders intermediate reasoning states as low-resolution image patches rather than token sequences, enabling subsequent steps to operate over compressed visual structure, OneLatent [133] learns a single latent visual token that distills the image context needed for downstream reasoning, achieving competitive performance with a drastically reduced visual token budget. In embodied control, LatentVLA [235] projects visual inputs into compact action latents for real-time planning, showing that low-dimensional representations can retain the information necessary for closed-loop decision making, while Future-VLA [44] extends this idea by learning future-conditioned latents that incorporate anticipated states without increasing dimensionality.

Summary. Overall, compressed reasoning can be understood as a unifying paradigm for trading explicit length for latent density. Across explicit traces, internal states, and cross-modal representations, existing methods share the same central objective: to preserve reasoning fidelity while reducing the computational and memory overhead associated with verbose intermediate representations. This suggests that effective reasoning need not always remain fully tokenized or fully materialized, and that semantically compact representations may provide a scalable foundation for efficient inference in increasingly complex reasoning systems.

- 4.3.2 Expanded


In this category, it augments the effective computational capacity of the model by extending latent computation along the depth or width dimensions. Formally, the model iterates over a step-T, width-K:

h(t+1k) = Φ h(tk) Kk=1 , t = 1,...,T, k = 1,...,K, (16)

- where h(tk) denotes the k-th latent trajectory at step t, and all K paths share a common initialization h(0).


Expanded methods increase the effective computational capacity by enlarging the latent process along different dimensions. Rather than relying on a single fixed forward pass, they enable the model to trade extra latent computation for stronger ability, improved faithfulness, and better adaptability across tasks, which could be classified into three types of expansion: Depth Expansion, Width Expansion, and Structural Expansion.

Depth Expansion. Depth-expanding approaches increase effective compute by reusing the same or structurally similar layers across multiple recurrent passes, allowing the model to iteratively refine a latent representation before producing an output. In recurrent pretraining, Huginn [50] introduces a lightweight model trained from scratch with recurrent depth, where a fixed transformer block is applied for a variable number of thinking steps, thereby decoupling parameter count from inference-time compute and enabling test-time scaling without adding parameters. RD-VLA [198] extends this paradigm to embodied models and shows that recurrent latent refinement improves long-horizon manipulation planning. In looped transformers, Loop [167] demonstrates that repeatedly applying the full decoder stack can induce genuinely multi-step reasoning rather than simply approximating a deeper fixed network , while LoopFormer [72] adds inputadaptive looping to allocate depth dynamically according to task complexity . From a pretraining perspective, Ouro [296] shows favorable scaling behavior along the looping dimension, with gains in faithfulness and efficiency . Relatedly, ETD [87] proposes an encode-think-decode framework in which a latent thought state is iteratively refined before decoding, yielding strong zero-shot generalization on arithmetic and commonsense tasks without explicit chain-of-thought supervision.

Width Expansion. These methods contrast with other approaches by allocating compute across multiple parallel hypotheses or latent trajectories, thereby prioritizing broad exploration over sequential refinement. This paradigm appears in several recent frameworks, SoftCoT++ [244] instantiates multiple parallel reasoning paths in continuous embedding space and aggregates them before decoding, achieving zero-shot performance gains that scale monotonically with the number of paths without requiring path-specific supervision. A similar principle underlies LatentTTS [262], which performs concurrent latent tree search and prunes partial hypotheses with a learned value function. PCCoT [224] further extends this idea by enabling multiple latent chains to run in parallel and exchange information at synchronization points, improving efficiency while preserving solution diversity; likewise, CoT2 [52] shows that parallel sampling in continuous thought space substantially benefits even GPT2-scale models on compositional reasoning tasks. In specialized settings, Bubbles [113] formulates width expansion as parallel “bubbles" whose pooled representations support zeroshot and unsupervised learning at scale, while PLR [193] applies parallel latent reasoning to sequential recommendation, where diverse latent representations better capture user preference uncertainty than a single deterministic pass.

Structural Expansion. A smaller but conceptually distinct line of work departs from simply increasing the depth or width of the computation graph and instead introduces new topological primitives for composing latent information across positions, modalities, or levels of control. Latent-SFT [37] supervises models on superposed latent chains—continuous compressions of multi-step reasoning trajectories—rather than their token-level realizations, thereby reducing decoding cost while preserving reasoning performance. Extending a similar superposition principle to visual reasoning, Laser [218] fuses multi-scale visual features into a shared latent representation instead of processing each resolution independently. At the system level, ColaVLA [152] decomposes VLA modeling into parallel but interactive high-level semantic reasoning and low-level motor planning streams, linked through cross-attention across temporal scales, which better aligns linguistic abstraction with continuous control.

Summary. In this part, approaches enrich latent reasoning by scaling computation along three complementary dimensions: depth, width, and structure. Depth expansion emphasizes iterative refinement through recurrent or looped computation, width expansion promotes parallel exploration over multiple latent hypotheses, and structural expansion introduces richer topologies for composing information across trajectories, positions, or modalities. Together, these methods share a common goal of improving reasoning performance by increasing effective calculation in latent space, while avoiding a proportional increase in model parameters.

- 4.3.3 Adaptive


In this part, methods generalize the Expanded framework by conditioning both recurrence depth T and trajectory width K on the input complexity of x, rather than prescribing them as fixed hyperparameters. A learned halting functional T governs instance-specific termination, yielding a variable-horizon computation:

h(t+1k) = Φ h(tk) Kk=1 , (17)

where t ∈ [1,T] and k ∈ [1,K] may be determined at the granularity of tokens boundaries, or other adaptive strategies based on the current hidden states by a halting function T (·):

(T, K) = T (ht; x), (18)

where the halting function could be a explicit component, or be internalized the model. This input-conditioned allocation concentrates reasoning depth where warranted by task difficulty, realizing a principled trade-off between computational frugality and expressive capacity.

Adaptive computation allows the model to allocate computational resources dynamically according to the complexity of the input, rather than relying on a fixed recurrence depth or trajectory width. In this setting, the amount, structure, and locus of computation become input-dependent, enabling the model to balance efficiency and capacity more flexibly. Existing methods can be broadly understood from three perspectives: Depth/Width Adaptation, Semantic Adaptation, and Control Adaptation.

Depth/Width Adaptation. A natural axis for adaptive computation is depth, that is, the number of steps applied. Building on this principle, TaH [49] proposes a think-and-halt mechanism that allows a shared-weight iterative model to exit early on easy tokens while allocating additional refinement steps to harder ones. LWS [146] similarly treats halting as a learned policy, jointly optimizing an auxiliary stopping variable with the language modeling objective. Moving from depth-wise iteration to latent-chain guidance, PLaT [207] learns when to terminate latent token generation before decoding, explicitly trading off depth against efficiency. At the architectural level, Dreamer [86] and SpiralFormer [263] replace fixed-depth stacks with weight-tied recurrent transformers, demonstrating that depth adaptivity can be achieved not only through learned halting policies but also through recurrent designs.

While depth adaptation modulates the length of the computational chain, width adaptation modulates its branching structure, i.e., the parallel hypotheses or policy trajectories explored at each step. I2B-LPO [36] learns to expand its branching factor in regions of high uncertainty and to collapse branches where confidence is sufficient, demonstrating that width adaptation is particularly impactful in long-horizon reasoning tasks where premature commitment to a single reasoning path leads to systematic failure.

Semantic Adaptation. This paradigm allocates computation at the finest granularity by assigning different budgets to individual tokens or semantic units within a single forward pass. For example, AL-CoT [267] applies token-level adaptation within the semantic, assigning more refinement steps to difficult tokens. A similar idea is developed in PonderLM-3 [97] and AdaPonderLM [180], which endow individual tokens with learned depth or halting decisions, enabling heterogeneous per-token computation and stronger semantic consistency. In contrast, DLCM [158] shifts adaptation from tokens to semantically coherent concepts that may span multiple tokens.

Control Adaptation. This part refers to methods that regulate computation through control signals, e.g., learned activation vectors, routing policies, or extraction mechanisms. System-1.5 [214] introduces cognitive shortcuts that allow to bypass intermediate transformer blocks according to estimated input difficulty. FR-Ponder [62] extends this idea through instance-adaptive activation steering, routing each input through a dynamically selected subset of representational subspaces based on early-layer features. RISER [257] similarly treats adaptation as the composition of latent reasoning skills encoded as steering directions in activation space, enabling zero-shot generalization to unseen tasks without gradient-based updating. Complementarily, PRE [125] shows that selective extraction of intermediate-layer representations as reversed signals, outperforming reliance on final-layer outputs.

Summary. In summary, adaptive methods generalize fixed-budget recurrent reasoning into an inputconditioned computation paradigm. Across depth/width adaptation, semantic adaptation, and control adaptation, the common goal is to allocate computation more selectively: spending more resources on difficult inputs, uncertain reasoning branches, or critical semantic units, while preserving efficiency on simpler cases. Taken together, these approaches suggest that the future of adaptive methods lie not merely in increasing computation, but in learning where, when, and how to use it most effectively.

- 4.3.4 Interleaved


This paradigm constructs a heterogeneous generation sequence by alternating discrete token embeddings in V with continuous latent in H, yielding interleaved generation:

r = r1, z1, r2, z2, ..., rM, zN , ri ∈ V, zj ∈ H, (19)

where the r generation trajectory, achieving a synergistic coupling of explicit symbolic reasoning and implicit neural computation.

Interleaved computation views reasoning as a heterogeneous sequential process in which discrete tokens and continuous latents are alternated within a unified trajectory. Compared with purely token-based or purely latent reasoning, this paradigm provides a more flexible interface for allocating computation across explicit symbolic steps and implicit neural operations. Existing work can be broadly grouped into three categories: Explicit-latent Interleaving, Modality Interleaving, and Task Interleaving.

Explicit-latent Interleaving. Hybrid generation interleaves natural-language tokens with latent internal states within a single trajectory, motivated by the observation that many intermediate steps need not be fully verbalised and can therefore be executed more efficiently without degrading performance. Early empirical support comes from Assorted [181], which shows that replacing selected verbal chain-of-thought steps with latent activations preserves downstream accuracy while substantially reducing token usage. Subsequent work extends this idea in two main directions. One line studies fixed or curriculum-based interleaving schemes: SpiralThinker [155] progressively internalises explicit reasoning steps through a spiral curriculum, and LiteReason [55] demonstrates that even a lightweight model can learn a form of mixed explicit–latent reasoning. A second line makes the explicit–latent boundary itself adaptive: SwiReasoning [175] learns a step-level switching policy via reinforcement learning, LT-Tuning [123] incorporates latent-thought positions into instruction tuning, and ThinkRouter [241] routes queries to different reasoning depths at the system level to balance efficiency and accuracy.

Modality Interleaving. When generation over non-textual inputs such as visual imagination, or perceptual feature maps, latent representations are not merely an efficiency mechanism but a representational requirement, since the underlying information cannot be fully captured in discrete text. Modality-interleaving methods therefore integrate continuous perceptual latents with linguistic tokens, allowing models to perform intermediate reasoning in the latent domain. Early work such as AURORA [11] established this paradigm by inserting explicit perceptual reasoning steps. Subsequent studies, including Mirage [251], LVR [95], VisMem [264], and Monet [211], showed that directly interleaving vision latents into architectures improves visual tasks without relying on textual scene descriptions.

A related line of work extends interleaving to multiple latent types: IVT-LR [20] couples text and vision activations through cross-attention, while SkiLa [197], LS [276], and MM-CoT [171] use visual latents as an internal sketchpad that supports subsequent language reasoning. Beyond two-dimensional perception, 3DThinker [28] incorporates spatial latents for geometric and spatial reasoning, and DMLR [111] together with ILVR [39] shows that sparse latent interleaving can preserve strong grounding performance while reducing computational cost.

Task Interleaving. A third family views interleaving not as a mechanism for mixing token types or modalities, but as a means of coordinating heterogeneous functional modules such as memory stores, retrieval components, generative heads, and agent sub-processes. Its defining feature is that the interleaved latent stream carries task-specific structured signals, e.g., retrieved evidence, episodic memory traces, or inter-agent communications, rather than general-purpose reasoning states. In single-model settings, this idea primarily appears as memory–reasoning integration: LCR-SER explicitly interleaves a compressed history buffer with ongoing inference for sequential recommendation [177]; MemGen [273], VisMem [264] and FlashMem [65] equip models with persistent working memory through, respectively, generated memory tokens; and CLaRa [59] interleaves retrieval and generation in a jointly trained latent lookup framework, rather than treating retrieval as an external pipeline. In multi-agent settings, interleaving further serves as a coordination protocol across asynchronously operating agents: LatentMem [47] introduces a shared latent memory that supports implicit communication during collaborative problem solving, while L2-VMAS [265] alternates perceptual and planning streams across agents to maintain a coherent joint world model in long-horizon embodied tasks.

Summary. Interleaved computation generalises the generation process beyond a homogeneous token stream by allowing models to alternate between symbolic outputs and latent computations. This design improves efficiency when some intermediate steps need not be verbalised, expands representational capacity when generation must operate over non-textual modalities, and enables tighter coordination when multiple functional modules or agents interact within a shared trajectory. Taken together, these studies suggest that interleaving is not merely a decoding strategy, but a general principle for organising hybrid computation systems that combine explicit interpretability with implicit computational power.

- 4.4 Optimization


Latent space optimization generally happens at three stages: pre-training, post-training, and inference. The three stages differ mainly in what is optimized: during pre-training and post-training, the optimized variable is typically model parameters θ ∈ W (or a subset of them); during inference, the model parameters are mostly fixed (sometimes also be trained), and the optimized variable is instead an inference-time state, such as a latent representation z ∈ H or a generation trajectory r ∈ V. For each stage, we categorize methods based on two aspects: supervision, that specifies what provides the learning signal; objective, that captures the purpose behind each loss component for latent optimization. Based on underlying computational operations, we categorize existing methods into three representative types:

Mechanism: Optimization

- • Pre-training (Section 4.4.1): starts with a randomly initialized model and trains it from the scratch, enabling native latent-level abilities.
- • Post-training (Section 4.4.2): enhances the ability of pre-trained models, with diverse supervision signals and objectives, learning the latent space.
- • Inference (Section 4.4.3): focuses on inference manipulation of latent states, allowing dynamic adjustment.


- 4.4.1 Pre-training


During the pre-training stage, z is trained jointly with the base model from scratch, the objective is to learn model parameters from large-scale pre-training data D. Formally, the optimization variable is θ ∈ Φ, and the objective can be written as:

θ⋆ = arg min θ∈Φ

E(x,y)∼D [L(x,y,z;Φθ)], (20)

where θ ∈ Φ ⊆ W denotes the set of trainable parameters in pre-training, and L trains the whole system end-to-end.

Optimization at this stage mostly relies on simple, scalable supervision already well-established for explicitspace training, rather than more sophisticated supervision that requires human annotation or elaborate processing. To stabilize training, optional auxiliary losses are designed to regulate the latent space. In total, these methods fall into three types: Autoregressive Supervision, Auxiliary Supervision, and Reinforcement.

Autoregressive Supervision Pre-Training. This category focuses on internalizing reasoning as a natural byproduct of next-token prediction or recurrent looping, without explicitly matching intermediate representations. Implementing Jacobi-iteration-based parallel training, PonderLM-2 [267] efficiently computes recursive latent thoughts without strict causal blocking. Exploring recurrent depth scaling through looped transformer layers, Looped Trans. [167] natively simulates complex reasoning via continuous latent updates. Scaling looped language models up to 2.6 billion parameters, Ouro [296] utilizes an entropy-regularized objective for consistent latent reasoning. To address scaling efficiency, PHD-Trans. [223] optimizes predictions via dynamic exploration of continuous states. To maintain stability in dynamic scenarios, AL-CoT [268] employs continuous state prediction objectives.

Auxiliary Supervision Pre-Training. This direction explicitly guides the formation of the latent space geometry through auxiliary semantics, contrastive learning, or reconstruction objectives. Optimizing continuous

semantic concepts via cross-entropy and reconstruction losses, CoCoMix [186] implicitly guides multi-task textual predictions. Incorporating InfoNCE and cross-entropy, LARES [112] aligns latent representations for sequential recommendation. Introducing latent action pretraining via VQ-VAE, LAPA [255] learns discretized latent actions directly from unannotated videos. Aligning visual latent spaces from videos with proprioceptive action spaces, CLAP [272] utilizes contrastive pretraining for robust embodied manipulation. Bypassing full visual dynamic reconstruction, JALA [131] derives predictive action embeddings jointly aligned with inverse dynamics and sparse physical actions. Focusing on mean squared error and task losses, CARE [176] scales multi-task prediction for embodied manipulation. Utilizing cross-entropy and mean squared error, ConceptLM [126] learns latent representations natively for efficient multi-task prediction.

Reinforcement Pre-Training. This category integrates reward signals directly into the foundational pretraining phase to actively shape latent thought trajectories. Integrating reinforcement signals, LoopRPT [190] reframes next-token prediction as a reasoning task via noisy latent rollouts, optimizing intermediate representations to compress effective reasoning into fewer iterations from the very beginning of the lifecycle.

Summary. Methods at this stage embed latent reasoning capacity directly into model parameters during large-scale training, foregoing the need for human annotation or elaborate supervision. The dominant approach is autoregressive prediction over continuous states, where looped or recurrent architectures naturally develop latent reasoning through standard next-token objectives. Auxiliary losses serve a regularizing role, shaping the geometry of the latent space without disrupting scalability. A nascent thread introduces reinforcement signals at pre-training time, aiming to instill efficient reasoning trajectories before any fine-tuning occurs.

- 4.4.2 Post-training


During the post-training stage, z is further optimized via fine-tuning on a pre-trained model. Thanks to the reduced data requirements compared to pre-training, post-training supervision can involve more sophisticated data augmentation or specialized loss designs. Many methods focus on defining an additional signal to supervise the latent variable, as supervision on explicit variables alone may not be sufficient. Again, the optimized variable is still model parameters, but the optimization is now restricted to a post-training objective:

θ⋆ = arg min θ∈W

θ(·|x) [R(x,r,z)], (21)

E(x,y)∼D [L(x,y,z;Φθ)] − β Er∼Φ

where the formulation subsumes supervised fine-tuning, preference optimization, and reinforcement-learningbased alignment. In latent-space methods, post-training often specializes in refining how latent variables are induced, controlled, or aligned with downstream objectives. Based on the supervision signals, there are three types, including: Explicit Supervision, Implicit Supervision, and Reinforcement Learning.

Explicit Supervision Fine-Tuning. This category optimizes latent reasoning by applying loss functions solely to the final human-readable output, without providing step-by-step targets for the continuous representations. Fine-tuning continuous variables via specific task losses, LATPC [260] enhances safety and robustness against jailbreak attacks. Using task loss alignment, GainRouter [288] dynamically routes features to enable fast and adaptive latent reasoning. Steering hidden states on a learned latent manifold, GeoSteer [84] ensures faithful and logically consistent reasoning trajectories. Fine-tuning models with cross-entropy and regularization, PILOT [289] internalizes the strategic oversight of large models into intrinsic latent guidance. Focusing on next-token prediction and alignment, TS [2] utilizes cross-entropy to streamline latent reasoning.

Implicit Supervision Fine-Tuning. This approach provides explicit gold targets for latent representations using knowledge distillation, contrastive alignment, or step-wise reconstruction signals.

Distillation-based methods anchor latent states to teacher-provided signals. SPOT [32] compresses explicit reasoning trajectories into compact latent tokens by anchoring them to corresponding teacher spans, while SemCoT [61] distills ground-truth reasoning into semantically aligned implicit tokens to accelerate computation. Latent-SFT [37] takes a different angle, redefining latent tokens as vocabulary-space superpositions and training them with KL divergence and cross-entropy losses.

Contrastive learning constitutes another prominent technique. LTA-Thinker [206] and EPR-Latent [215] employ contrastive objectives to optimize latent thought distributions and refine intermediate representations, respectively, while ReaRec [192] applies the same principle to sequential recommendation. EBM-CoT [29] further combines contrastive signals with regularization to improve overall latent reasoning efficiency.

###### Table 6 Overview of the Pre-training (Section 4.4.1), Post-training (Section 4.4.2), and Inference (Section 4.4.3) optimization. We compare the modality, backbone, computational operation, and scenario. Here, Recon., CE, InfoNCE, KL, MSE, and CL denote reconstruction, cross-entropy, information noise-contrastive estimation, Kullback–Leibler divergence, mean squared error, and contrastive learning, respectively.

Date Method Paper Code Modality Backbone Supervision Objective Scenario Pre-training

- 10/24 LAPA [255] Paper - action LWM-7B Recon. action quantization/prediction embodied manipulation/transferring

- 02/25 CoCoMix [186] Paper Code text GPT2-0.1B/0.4B/1.4B CE/Recon. multi-task prediction interpretability/efficiency

- 02/25 Looped Trans. [167] Paper - text decoder-only-1.5B CE/regularization next-token prediction latent reasoning/complex reasoning

- 04/25 PHD-Trans. [223] Paper - text decoder-only-1.2B CE next-token prediction scaling/efficiency/exploration

- 05/25 LARES [112] Paper - text transformer-based InfoNCE/CE/reward alignment/next-token prediction sequential recommendation


- 09/25 PonderLM-2 [267] Paper Code text PonderLM-2-0.5B/1.4B joint CE next-token prediction latent reasoning/efficiency

- 10/25 Ouro [296] Paper - text Ouro-1.4B/2.6B CE/KL/task loss prediction/stability efficiency/consistency/exploration

- 01/26 CLAP [272] Paper - action Qwen3-VL-4B CE/Recon./task loss quantization/alignment/prediction embodied manipulation/transferring

- 01/26 CARE [176] Paper - action Prismatic-7B MSE/task loss multi-task prediction embodied manipulation/scaling

- 02/26 AL-CoT [268] Paper - text PonderLM2-0.5B/1.4B CE/task loss prediction/stability latent reasoning/dynamic reasoning

02/26 ConceptLM [126] Paper Code text GPT2-0.1B/other 5 CE/MSE multi-task prediction latent reasoning/efficiency 02/26 JALA [131] Paper - action InternVL3-2B task loss alignment/prediction embodied manipulation/scaling 03/26 LoopRPT [190] Paper - text Ouro-1.4B/2.6B reward/KL/task loss next-token prediction/sampling complex reasoning/efficiency/scaling

Post-training

11/24 LaTRO [22] Paper Code text Mistral-7B/other 2 self reward/KL finetuning/sampling latent reasoning/zero-shot

- 01/25 LATPC [260] Paper Code text LLaMA3-8B/other 3 task loss finetuning safety/roubustness/jailbreak attack

03/25 ReaRec [192] Paper - text LLaMA3.1-8B CE/KL/InfoNCE prediction/sampling sequential recommendation 05/25 CoLaR [188] Paper Code text LLaMA3.2-1B MSE/reward/task loss prediction/sampling/finetuning dynamic reasoning/efficiency 05/25 LARES [112] Paper - text transformer-based CE/reward/KL alignment/sampling sequential recommendation

- 05/25 HRPO [266] Paper Code text Qwen2.5-7B/other 2 reward/KL sampling latent reasoning/complex reasoning

- 05/25 LatentR3 [282] Paper Code text Qwen2.5-1.5B CE/reward next-token prediction/sampling recommendation/efficiency

- 06/25 EPR-Latent [215] Paper Code text GPT2-0.1B/other 2 MSE/task loss contrast/finetuning latent reasoning/efficiency


- 06/25 Mirage [251] Paper Code vision Qwen2.5-VL-7B CE/reward/task loss next-token prediction/sampling visual imagination/generalization


- 09/25 LTA-Thinker [206] Paper Code text Qwen2.5-7B/Qwen3-8B CE/KL/task loss finetuning/alignment/contrast latent reasoning/scaling

- 09/25 GainRouter [288] Paper - text Qwen3-4B task loss alignment/finetuning latent reasoning/adaptive reasoning

- 09/25 MemGen [273] Paper Code text SmolLM3-3B/Qwen3-8B CE/reward finetuning/sampling experimental memory/generalization

- 10/25 Latent-SFT [37] Paper Code text LLaMA3.2-1B/other 2 KL/CE finetuning latent reasoning/efficiency

10/25 3DThinker [28] Paper Code vision Qwen2.5-VL-7B/other 7 CE/reward/task loss finetuning/sampling/alignment spatial understanding/visual reasoning 10/25 SemCoT [61] Paper Code text LLaMA2-7B/Mistral-7B CE/CL contrast/alignment complex reasoning/efficiency 11/25 SofT-GRPO [291] Paper Code text DeepSeek-R1-1.5B/other 2 KL/reward sampling/stability latent reasoning/generalization 11/25 EBM-CoT [29] Paper - text Qwen2.5-7B/other 5 CE/regularization next-token prediction latent reasoning/efficiency

- 11/25 VisMem [264] Paper Code vision Qwen2.5-VL-7B/other 8 reward sampling/alignment visual understanding/visual reasoning






11/25 SCM [208] Paper - text DeepSeek-R1-7B/other 3 KL/reward sampling latent reasoning

- 11/25 LWS [146] Paper Code text LLaMA3.2-1B CE/reward/task loss prediction/alignment/sampling dynamic reasoning/efficiency

- 11/25 Monet [211] Paper Code vision Qwen2.5-VL-7B CE/reward/task loss finetuning/alignment/sampling visual reasoning/generalization

- 12/25 ReLaX [280] Paper - text Qwen2.5-3B/other 4 reward/regularization sampling exploration/generalization


- 12/25 RL-Latent [149] Paper Code text Qwen2.5-1.5B CE/reward/KL prediction/finetuning/sampling latent reasoning/complex reasoning


- 01/26 I2B-LPO [36] Paper Code text Qwen3-14B/Qwen2.5-37B self-reward/KL sampling exploration/policy optimization










- 01/26 GeoSteer [84] Paper - text Qwen3-8B /other 3 Recon./KL/task loss alignment complex reasoning/consistency

- 01/26 DLR [170] Paper - text LLaMA2-1B/7B reward/regularization sampling/stability/contrast exploration/efficiency

- 01/26 PILOT [289] Paper - text Qwen2.5-1.5B/other 2 CE/regularization finetuning/alignment robustness/generalization

- 01/26 ATP-Latent [292] Paper Code text LaMA3.2-1B CE/KL/reward finetuning/sampling latent reasoning/generalization

- 01/26 GANPO [76] Paper - text Gemma2-2B/LLaMA3-8B CE/regularization alignment preference optimizatio

- 01/26 BNPO [102] Paper - action Qwen2.5-VL-3B/7B Recon./task loss alignment/sampling efficiency/generalization

- 01/26 LaViT [227] Paper Code vision Qwen2.5-VL-3B CE/Recon./task loss next-token prediction/alignment visual reasoning/efficiency/robustness

- 01/26 RoT [216] Paper Code vision Qwen3-VL-4B/other 2 MSE/CE finetuning/prediction visual reasoning/accelerating/efficiency

- 02/26 CogSense [96] Paper - vision Qwen3-VL-8B MSE/CE/task loss finetuning/prediction/alignment visual imagination/generalization


- 02/26 MaD-Mix [236] Paper - vision LLaVA-OneVision-0.5B/7B task loss alignment visual reasoning/efficiency


- 02/26 TS [2] Paper - text Qwen2.5-0.5B/1.5B CE next-token prediction/alignment latent reasoning/efficiency


- 02/26 Reason-IAD [24] Paper Code vision Qwen2.5- VL-7B/other 3 self-reward sampling/alignment visual detection


- 02/26 RLTT [222] Paper - text Ouro-2.6B reward/regularization sampling/alignment latent reasoning/generalization

- 03/26 SPOT [32] Paper - text DeepSeek-R1-7B CE/task loss prediction/alignment/finetuning latent reasoning/efficiency Inference


10/24 VTI [120] Paper Code vision LLaVA1.5-7B/other 2 CL contrast hallucination mitigation 05/25 SoftCoT++ [244] Paper Code text LLaMA3.1-8B CL contrast/sampling exploration/zero-shot/scaling 05/25 LatentSeek [98] Paper Code text LLaMA3.1-8B self-reward sampling forgetting alleviation/scaling 05/25 SR [295] Paper Code text LLaMA3.1-8B/other 4 self-reward sampling/alignment exploration/efficiency

- 08/25 LatentPrompt [17] Paper - text Mistral-7B self-reward/task loss sampling prompt optimization

- 09/25 LatentEvolve [274] Paper Code text LLaMA3.2-3B/other 3 self-reward/Recon. sampling/finetuning experimental memory


- 09/25 LTO [41] Paper - text Huginn-3.5B/other 4 reward/KL sampling/finetuning/alignment efficiency/scaling

- 10/25 LTPO [258] Paper Code text LLaMA3.1-8B/other 3 self reward sampling/alignment generalization/unsupervised learning

- 11/25 L2V-CoT [270] Paper - vision LLaVA-Next-8B/other 4 task loss contrast/alignment transferring/visual reasoning

- 12/25 DMLR [111] Paper Code vision Qwen2.5-VL-7B/other 5 self-reward sampling/alignment visual understanding/grounding


- 01/26 TGR [298] Paper - text Qwen3-8B/other 3 self-reward sampling exploration/long-horizon

- 02/26 STIR [178] Paper Code text DeepSeek-R1-7B/other 3 CL/self-reward sampling/alignment/contrast complex reasoning/efficiency


- 02/26 ITR [88] Paper - text LLaMA2-0.2B KL/task loss sampling complex reasoning/efficiency


- 02/26 REVIS [225] Paper Code text Qwen2.5-VL-7B/other 4 CL contrast/alignment hallucination mitigation


- 02/26 GTS [209] Paper - text GPT2-0.1B/LLaMA3.2-1B reward/KL sampling/ailgnment exploration/latent reasoning

02/26 Control++ [228] Paper - vision LLaVA1.5-7B task loss alignment hallucination mitigation

- 03/26 ∇-Reasoner [210] Paper - text Qwen-2.5-7B/other 2 reward/KL sampling/alignment complex reasoning/exploration






###### Reconstruction objectives are especially prevalent in multimodal settings, where aligning across modalities demands explicit feature-level supervision. LaViT [227] jointly predicts next tokens and reconstructs visual features to align cross-modal reasoning, and RoT [216] takes a distinctive approach by rendering chain-ofthought as images and applying MSE together with cross-entropy. BNPO [102] uses reconstruction and task losses to align embodied action spaces. Methods such as Mirage [251], 3DThinker [28], VisMem [264],

Monet [211], and CogSense [96] further demonstrate the breadth of this paradigm across visual imagination, spatial reasoning, and generalization tasks.

Reinforcement Learning. To mitigate geometric drift, this sub-category leverages policy gradients, rewards, and preference signals to autonomously discover efficient latent trajectories.

Self-rewarding mechanisms form one important thread, where the model itself provides the training signal without external annotation. LaTRO [22] formulates reasoning as a variational sampling process optimized via the model’s own probability estimates, and I2B-LPO [36] employs an iterative information bottleneck with self-rewards for thorough latent policy exploration. MemGen [273] similarly relies on targeted self-rewards to enhance generalization.

A further set of methods introduces specialized regularizers to stabilize or enrich the optimization landscape. SofT-GRPO [291] applies Gumbel reparameterization for stable group relative policy optimization, GANPO [76] introduces an adversarial regularizer to robustify preference optimization, and DLR [170] combines contrastive stability constraints with reward signals for directed latent exploration. HRPO [266] takes a hybrid approach, using a learnable gate to progressively integrate continuous hidden states with discrete tokens. CoLaR [188], LWS [146], LatentR3 [282], and Reason-IAD [24] round out the landscape by applying reward-driven optimization to dynamic trajectory prediction, sequential recommendation, and visual spatial understanding. KL divergence regularization also serves as a recurring stabilization mechanism across many methods. LARES [112], RL-Latent [149], SCM [208], and ATP-Latent [292] all incorporate KL penalties alongside reward objectives to prevent excessive deviation from the reference policy during latent space optimization. ReLaX [280] further addresses premature convergence through strict reward regularization, and RLTT [222] distributes rewards across the full trajectory to improve alignment.

Summary. Compared to pre-training, post-training affords greater flexibility in supervision design, enabling richer signals such as distillation, contrastive alignment, and reward-based feedback to refine latent representations. A central tension in this stage is whether to supervise latent variables explicitly through gold targets or implicitly through output-level task losses alone. Reinforcement learning methods go further by treating latent trajectory discovery as a policy optimization problem, allowing models to autonomously identify compact and efficient reasoning paths without relying on predetermined supervision.

- 4.4.3 Inference


For inference-time latent optimization, the model weights θ are usually frozen (also could be trained) and the latent states z are directly manipulated at test time. Unlike pre-training and post-training, inference-time methods treat z itself as the optimization variable. Formally, let θ denote the trained parameters, then the optimized variable becomes ω, with:

z⋆ = arg min ω∈Ω

J (z;x,Φθ). (22)

where Ω is the feasible region of the variable, and J is the inference-time objective, final output is then generated conditioned on the optimized inference-time state. The part includes Scaling, Tuning, and Guidance.

Inference Scaling. This category focuses on exploring the latent space by generating multiple candidate trajectories and employing reward-based heuristics to identify the optimal reasoning path. Employing a continuous-space classifier as a latent reward model, LTO [41] aggressively prunes incorrect thinking patterns during inference. Performing manifold-informed latent foresight search, TGR [298] scores candidate latent anchors to encourage smooth trajectories and diverse long-horizon exploration. Reformulating latent exploration as conditional sampling over continuous thought representations, GTS [209] utilizes a Gaussian Thought Sampler to predict context-dependent perturbation distributions. Applying self-reward sampling, LatentSeek [98] effectively alleviates catastrophic forgetting during continuous generation. Employing selfrewards, SR [295] samples and aligns soft reasoning explorations to maximize efficiency. Leveraging the latent semantic space, LatentPrompt [17] automatically evaluates and optimizes prompts via intrinsic self-rewards. Utilizing KL divergence and task losses, ITR [88] guides inference-time sampling to greatly improve complex reasoning efficiency. Enhancing visual understanding and grounding, DMLR [111] implements continuous self-reward sampling and alignment.

Inference Tuning. This approach shifts from trial-and-error stochastic search to continuous, gradientbased optimization executed directly on the latent variables or policy during the forward pass. Optimizing intermediate latent thought vectors on the fly, LTPO [258] utilizes an online policy gradient method guided by an intrinsic confidence-based reward. Integrating differentiable optimization over token logits, ∇-Reasoner [210] refines the policy directly within the decoding loop via gradient descent in the continuous sample space. Combining self-reward and reconstruction losses, LatentEvolve [274] dynamically samples and fine-tunes experimental memory states through test-time scaling.

Inference Guidance. This category applies targeted structural constraints, contrastive logic, or sparse interventions to dynamically guide latent representations and prevent hallucinations. Steering internal activations via sparse interventions, REVIS [225] mitigates object hallucination in large vision-language models by extracting pure visual information vectors. Internalizing contrastive learning and self-rewards, STIR [178] introduces a value-modulated trajectory intervention that dynamically injects context-specific impulses via anchor-based gating. Perturbing latent thoughts via specialized initial tokens, SoftCoT++ [244] uses contrastive learning to enforce diversity among soft representations. Utilizing contrastive learning at inference time, VTI [120] successfully mitigates hallucinations in massive visual models. Contrasting visual features at test time, L2V-CoT [270] tightly aligns transferring and visual reasoning capabilities through latent intervention. Preventing visual hallucinations dynamically, Control++ [228] applies highly targeted task losses during the alignment generation process.

Summary. Unlike parameter-level optimization, inference-time methods treat latent states themselves as the optimization variable while keeping model weights fixed. The key distinction among approaches lies in the search strategy: scaling methods explore the latent space stochastically through reward-guided trajectory selection, optimization methods apply gradient updates directly to latent variables during decoding, and guidance methods impose structural or contrastive constraints to correct latent representations on the fly, particularly to suppress hallucinations.

###### 5 Ability: What Does Latent Space Enable?

The latent space, as a machine-native representational substrate within large models, unlocks a spectrum of emergent capabilities that transcend the boundaries of explicit token-level processing. In this section, we systematically examine these capabilities along seven dimensions: Reasoning (Section 5.1) concerns the ability to carry out deduction and relational computation through continuous internal states; Planning (Section 5.2) emphasizes the prospective organization of solution trajectories, resource allocation, and multi-step decisionmaking; Modeling (Section 5.3) focuses on the characterization, interpretability, controllability, and scalable depth of latent representations themselves; Perception (Section 5.4) enables models to preserve and manipulate rich, spatially structured information for more faithful visual understanding; Memory (Section 5.5) supports compact, persistent, and adaptive knowledge retention across contexts; Collaboration (Section 5.6) allows multiple agents to exchange semantic content directly through latent channels rather than discrete language alone; and Embodiment (Section 5.7) extends latent computation into physical interaction, supporting grounded action, predictive foresight, spatial imagination, and transfer across heterogeneous bodies. As depicted in Figure 8, each dimension reflects a distinct facet of intelligence that latent representations uniquely empower, ranging from internal logical deduction to physical interaction with the environment.

- 5.1 Reasoning


Reasoning in latent space refers to the capacity of large models to perform logical deduction, relational computation, and conclusion generation through internal continuous representations rather than through explicit token-by-token verbalization. The shift from explicit CoT reasoning [219] to latent reasoning represents a fundamental paradigm change: instead of articulating every intermediate step in natural language, models learn to think within a continuous, high-dimensional latent manifold [58, 294].

This paradigm offers substantial advantages in computational efficiency, representational capacity, and the ability to encode superpositions of multiple reasoning paths simultaneously. We organize this rapidly expanding landscape along six abilities: Implicit Inference without full verbalization, Compact Trace that condenses long

Reasoning

Planning

![image 315](<2026-yu-latent-space-foundation-evolution_images/imageFile315.png>)

![image 316](<2026-yu-latent-space-foundation-evolution_images/imageFile316.png>)

![image 317](<2026-yu-latent-space-foundation-evolution_images/imageFile317.png>)

![image 318](<2026-yu-latent-space-foundation-evolution_images/imageFile318.png>)

![image 319](<2026-yu-latent-space-foundation-evolution_images/imageFile319.png>)

![image 320](<2026-yu-latent-space-foundation-evolution_images/imageFile320.png>)

![image 321](<2026-yu-latent-space-foundation-evolution_images/imageFile321.png>)

![image 322](<2026-yu-latent-space-foundation-evolution_images/imageFile322.png>)

![image 323](<2026-yu-latent-space-foundation-evolution_images/imageFile323.png>)

![image 324](<2026-yu-latent-space-foundation-evolution_images/imageFile324.png>)

![image 325](<2026-yu-latent-space-foundation-evolution_images/imageFile325.png>)

![image 326](<2026-yu-latent-space-foundation-evolution_images/imageFile326.png>)

![image 327](<2026-yu-latent-space-foundation-evolution_images/imageFile327.png>)

implicit inference

compact trace

continuous refinement

branching path

modal generalization

controlable exploration

efficient search

adaptive budget

sequential decision

Modeling

Perception

![image 328](<2026-yu-latent-space-foundation-evolution_images/imageFile328.png>)

![image 329](<2026-yu-latent-space-foundation-evolution_images/imageFile329.png>)

![image 330](<2026-yu-latent-space-foundation-evolution_images/imageFile330.png>)

![image 331](<2026-yu-latent-space-foundation-evolution_images/imageFile331.png>)

![image 332](<2026-yu-latent-space-foundation-evolution_images/imageFile332.png>)

![image 333](<2026-yu-latent-space-foundation-evolution_images/imageFile333.png>)

![image 334](<2026-yu-latent-space-foundation-evolution_images/imageFile334.png>)

![image 335](<2026-yu-latent-space-foundation-evolution_images/imageFile335.png>)

![image 336](<2026-yu-latent-space-foundation-evolution_images/imageFile336.png>)

![image 337](<2026-yu-latent-space-foundation-evolution_images/imageFile337.png>)

![image 338](<2026-yu-latent-space-foundation-evolution_images/imageFile338.png>)

rich expression

self inspection

robust control

scalable computation

multimodal inference

heuristic imagination

faithful grounding

Memory

Collaboration

![image 339](<2026-yu-latent-space-foundation-evolution_images/imageFile339.png>)

![image 340](<2026-yu-latent-space-foundation-evolution_images/imageFile340.png>)

![image 341](<2026-yu-latent-space-foundation-evolution_images/imageFile341.png>)

![image 342](<2026-yu-latent-space-foundation-evolution_images/imageFile342.png>)

![image 343](<2026-yu-latent-space-foundation-evolution_images/imageFile343.png>)

![image 344](<2026-yu-latent-space-foundation-evolution_images/imageFile344.png>)

![image 345](<2026-yu-latent-space-foundation-evolution_images/imageFile345.png>)

![image 346](<2026-yu-latent-space-foundation-evolution_images/imageFile346.png>)

![image 347](<2026-yu-latent-space-foundation-evolution_images/imageFile347.png>)

![image 348](<2026-yu-latent-space-foundation-evolution_images/imageFile348.png>)

working retention

persistent mind

semantic fidelity

shared cognition

heterogeneous interoperability

multimodal recal

Embodiment

![image 349](<2026-yu-latent-space-foundation-evolution_images/imageFile349.png>)

![image 350](<2026-yu-latent-space-foundation-evolution_images/imageFile350.png>)

![image 351](<2026-yu-latent-space-foundation-evolution_images/imageFile351.png>)

![image 352](<2026-yu-latent-space-foundation-evolution_images/imageFile352.png>)

![image 353](<2026-yu-latent-space-foundation-evolution_images/imageFile353.png>)

![image 354](<2026-yu-latent-space-foundation-evolution_images/imageFile354.png>)

![image 355](<2026-yu-latent-space-foundation-evolution_images/imageFile355.png>)

unsupervised grounding

implicit thinking

predictive foresight

spatial cognition

generalized transfer

Figure 8 Core abilities brought by the latent space, including: Reasoning (Section 5.1), Planning (Section 5.2), Modeling

- (Section 5.3), Perception (Section 5.4), Memory (Section 5.5), Collaboration (Section 5.6), and Embodiment (Section 5.7).


chains into compact states, Continuous Refinement that sustains and revises thought in latent form, Branching Path over multiple candidates, and Modal Generalization beyond text-only settings.

Implicit Inference. A central motivation for moving reasoning into latent space is the growing evidence that explicit CoT, while interpretable, is often redundant and fundamentally constrained by the discrete, sequential nature of language. Converging evidence from CoT compression [122, 277], implicit capability elicitation [22, 99], and latent self-evaluation [217] shows that reasoning-like behavior is already substantially encoded in the continuous activation spaces of pretrained models. Further analyses establish latent reasoning as a distinct computational mode encompassing richer, non-sequential inference [27, 63], collectively challenging the assumption that reasoning must be externalized in tokens. Building on these insights, COCONUT [58] demonstrated that continuous thought vectors can encode superpositions of multiple reasoning paths, enabling emergent breadth-first search and showing that models can infer internally before committing to language.

Compact Trace. One major ability unlocked by latent space is compressing explicit CoT into far more compact internal states without losing its problem-solving value. A broad range of supervision and post-training studies [31, 61, 173, 174, 215, 220, 288] shows that long reasoning traces can be absorbed into compact latent states while preserving much of their functional value. This evidence suggests that already-trained models can

acquire compressed reasoning ability with only modest additional overhead. The collective evidence indicates that reasoning chains can be preserved in representations orders of magnitude more compact, revealing fundamental redundancy in token-level reasoning.

Continuous Refinement. Beyond compressing existing CoT, latent space also supports the ability to sustain, blend, and iteratively revise thought as a continuous state. Soft token methods [208, 243, 287] replace discrete sampling with probability-weighted embedding mixtures or learned concept-level blending, while stochastic refinement through diffusion [83] and Markov dynamics [115] enables revision of earlier reasoning decisions. Energy-based consistency enforcement [29] and theoretical analyses of vocabulary-space superposition [37, 52] further show that such latent states can preserve coherence while remaining amenable to simultaneous optimization. Thought augmentation and contextualization [123, 129, 164, 185, 206] enrich this refinement ability by fusing task-relevant and background knowledge and modulating reasoning through targeted interventions.

Branching Path. The continuous nature of latent space enables fundamentally new reasoning topologies that let models explore several candidate trajectories at once. Parallel latent reasoning [113, 224, 244, 262] demonstrates simultaneous search through soft path sampling, stochastic width, and Jacobi iteration, reducing wall-clock latency while maintaining quality. Hybrid latent-explicit systems [155, 175, 181, 241] further suggest that models can flexibly alternate between compact internal search and selective externalization when beneficial. Studies of dual-system orchestration [33] reinforce this view, indicating that strong reasoners benefit from coordinating multiple reasoning paths and modes rather than committing to a single linear trace.

Modal Generalization. A key indicator of the maturity of latent reasoning is its ability to generalize beyond text-only settings. Modality-agnostic continuous thought [154, 160] demonstrates that the latent reasoning paradigm applies across linguistic, visual, and heterogeneous substrates, while cross-modal transfer and efficiency techniques [133, 171, 216, 270] show that this capability can move across modalities with increasing compactness. We defer detailed treatment of visual latent reasoning to the Perception subsection

- (Section 5.4).

Beyond vision, domain-specific applications spanning chemical synthesis [3], narrative generation [55], novelty discovery [16], and joint-embedding prediction [110] demonstrate broad applicability. Structured spatialtemporal reasoning [203, 247] extends this generalization to geometric and temporal domains, while faithfulness and controllability studies [64, 205, 257, 279] show that latent reasoning can remain reliable as it moves across settings.

- 5.2 Planning


Planning concerns the search for optimal trajectories through the solution landscape, where the continuous, differentiable nature of the latent manifold admits gradient-based policy optimization and iterative trajectory refinement. Unlike reasoning, which focuses on logical deduction within a given context, planning emphasizes the prospective organization of computation, determining where to allocate resources, how to explore the solution space, and when to terminate search [207, 240]. We examine latent planning through four abilities: Controllable Exploration over internal solution paths, Search Efficiency in navigating the latent manifold, Adaptive Budget allocation that matches compute to difficulty, and Sequential Decision in downstream interactive tasks.

Controllable Exploration. A central ability in latent planning is controlling internal solution trajectories rather than merely generating the next token greedily. RL-based trajectory optimization [41, 258, 266, 291] shows that continuous thought representations can be directly improved via policy gradients, Gumbel reparameterization, and test-time refinement. Training stability and diversity remain active challenges, addressed through exploration collapse prevention [36], systematic design analysis [149], and contrastive reward shaping [170]. These works collectively establish that latent geometry enables deliberate trajectory improvement that is fundamentally difficult in discrete token space.

Efficient Search. The latent manifold provides a natural substrate where geometric smoothness and continuity can be exploited for efficient navigation. Exploration restoration and trajectory diversification [189, 280, 295] maintain reasoning variety through entropy exploitation, latent decoding, and controlled embedding exploration,

while geometry-guided search [98, 178, 298] leverages intrinsic manifold properties for instance-level targeting and long-context foresight.

Adaptive Budget. A defining characteristic of latent planning is dynamic, input-dependent resource allocation. Adaptive depth and horizon determination [62, 146, 207, 292] adjusts reasoning depth through instance-level steering, RL-based stopping, dynamic termination, and active budget determination, investing computation proportionally to problem complexity.

Sequential Decision. Latent planning has been productively deployed in sequential decision-making domains, where the temporal structure of user behavior or system states naturally maps onto trajectory optimization in latent space.In recommendation, retrieval,and cross-domain adaptation [54, 112, 177, 188, 193, 204, 271, 282], latent planning improves sequential prediction, re-ranking, and transfer by maintaining and refining internal trajectories over time. In multi-step planning and tool use [25, 102, 226, 269, 289, 293], it supports sustained state tracking, optimization over intermediate decisions, and tighter control of multimodal agents, and further extends to reparameterizing the action space itself—compressing recurrent low-entropy scaffolds into compact latent action units to directly reduce the effective decision horizon while preserving executability. The breadth of these applications, spanning recommendation systems, information retrieval, tool use, action representation learning, and conversational AI, establishes latent planning as a versatile paradigm that extends well beyond the scope of traditional reasoning benchmarks.

- 5.3 Modeling


Modeling encompasses the ability to characterize, inspect, and shape latent representations within large language models. While reasoning and planning concern what models compute in latent space, modeling focuses on what latent representations let us understand and control about the computation itself. We structure this dimension into four abilities: Rich Expression to encode complex computation, Self Inspection that makes internal states analyzable, RobustControl over risky or unstable behavior, and ScalableComputation that expands capacity through latent recurrence.

Rich Expression. Rigorous analysis increasingly shows that latent space supports a richer computational capacity than explicit token-only reasoning. Expressiveness analyses [239, 294] prove that continuous thought vectors encode multiple search frontiers simultaneously and achieve provably greater expressiveness than CoT, while monitorability analysis [89] reveals the associated trade-offs between efficiency and interpretability. Fundamental limitation results [166, 301] show that exploration and execution cannot be simultaneously optimized within fixed budgets, and that reasoning depth correlates weakly with correctness under certain conditions. Cognitive and domain-specific frameworks [66, 172] frame reasoning as transitions across representation spaces, extending insights from neuroscience to program understanding, together clarifying both the power and the boundaries of latent reasoning.

Self Inspection. Understanding the internal dynamics of latent reasoning is critical because latent space increasingly supports direct inspection of what the model is representing and how those states evolve. Validity probing [107, 285] examines whether latent tokens encode genuine reasoning or exploit artifacts and whether models truly reason step-by-step or develop qualitatively different strategies. Transparency and visualization methods [23, 116, 145] make internal representations interpretable through latent debate, geometry visualization, polarity-aware probing, and cognitive analysis. Representation-level analysis [143, 161] demonstrates information preservation and reveals rich semantic dimensions beyond task performance, while information flow studies [125, 195] uncover multi-hop reasoning paths and cross-lingual transition mechanisms. Practical steering [82, 84] further suggests that inspection is not merely descriptive, but can directly support targeted improvements.

Robust Control. Latent space provides a powerful but double-edged lever for model safety, because the same representations that enable strong performance can also be manipulated for both attack and defense. On the one hand, attack vectors [140, 237] exploit latent fusion and feedback-based gradients, alongside backdoor triggers embedded in latent CoT. On the other hand, layered defense mechanisms [101, 179, 250, 260] provide controllable steering, adversarial training, feature activation steering, and streaming risk detection. Training-phase safety [6, 76, 191] addresses adversarial regularization, contrastive unlearning, and human preference modeling, underscoring that robust latent control is essential for building safe systems.

Scalable Computation. Modeling also highlights the ability of latent systems to expand effective depth and capacity without proportionally expanding explicit token generation. Formal expressiveness results [167] confirm that looped transformers with latent iterations express strictly more complex computations than feedforward counterparts. Recurrent-block scaling [1, 50, 87, 296] iterates shared blocks for test-time compute, scales looped pretraining, introduces encode-think-decode architectures, and demonstrates out-of-distribution generalization. Progressive refinement and architectural variants [72, 86, 130, 263] extend this flexibility through depth-recurrent attention, elastic depth, and multi-resolution recursion. Adaptive depth allocation [49, 97, 180, 214] further enables dynamic computation through selective iteration, dual-process routing, and token-wise pondering.

Beyond recurrence, concept-level and efficiency innovations [121, 158] operate on adaptive semantic boundaries and achieve KV cache efficiency, while representation-level design [17, 157, 204, 223] bypasses discrete bottlenecks in prompt optimization, pretraining scaling, and deployed system efficiency.

- 5.4 Perception


Perception in latent space addresses the fundamental challenge of enabling large models, particularly VLMs, to understand, represent, and process visual information in continuous, high-fidelity latent spaces. Current VLMs still face a critical bottleneck: converting rich visual content into discrete text tokens inevitably discards spatial structure, fine-grained detail, and relational geometry [11, 95]. Latent perception overcomes this limitation by preserving dense, spatially-structured information that discrete tokenization necessarily destroys, enabling models to reason about visual content with the richness and nuance of human perception. We organize latent perception into three progressively deeper abilities: Multimodal Inference over internal visual representations, Heuristic Imagination for generative manipulation and 3D understanding, and Faithful Grounding that improves output faithfulness through representation-level intervention.

Multimodal Inference. A primary thrust is enabling VLMs to reason about visual content through internal latent representations rather than text-mediated descriptions. Foundational latent visual reasoning [95, 211] demonstrated that generating and updating latent visual states alongside text enables fine-grained visual understanding unattainable through text-only reasoning. Follow-up work [21, 39, 100, 183, 218] shows that this visual inference ability can remain both accurate and efficient through selective computation, coarse-to-fine processing, and joint embedding prediction without pixel-level reconstruction. Multimodal coordination and alignment studies [20, 73, 96, 111, 169, 225, 283, 284] further show that structured visual latents can be enriched, stabilized, and generalized to temporal domains.

Heuristic Imagination. Latent perception also enables VLMs to perform visual heuristic imagination, generating and manipulating internal visual representations as part of the reasoning process, analogous to human mental imagery. This capability is valuable for tasks requiring spatial reasoning, 3D understanding, or visual planning that cannot be adequately expressed in text. Internal visual imagination [28, 251] empower latent manipulation and align VLM features with 3D foundation models, while visual scratchpads [156, 197, 276] introduce sketching mechanisms that capture dense spatial and geometric information through continuous visual tokens. Perceptual fidelity preservation [135, 227] ensures that latent visual representations maintain fidelity during distillation and dynamically refocuses attention across modality gaps.

Faithful Grounding. A critical application of latent perception is improving the faithfulness of VLM outputs by intervening at the representation level, addressing the pervasive problem of hallucination. Hallucination mitigation via latent steering and architectural alignment [120, 137] corrects visual-textual misalignments and addresses root causes, while perceptual grounding tokens [11] provide auxiliary signals through depth maps and detection outputs. Representation analysis and diagnostics [9, 90, 246, 253] reveal when perceptual failures occur and support calibrated uncertainty estimation. Domain-specific deployment in industrial and video anomaly detection [18, 24] demonstrates practical reliability improvements. These methods collectively establish latent perception as a powerful mechanism for reducing the gap between what models see and what they report, with direct implications for the reliability of deployed vision-language systems.

- 5.5 Memory

Memory has emerged as a necessary complement to LLMs, whose stateless architecture needs external mechanisms to retain knowledge across inference steps [68]. Yet token-based memory introduces its own bottleneck: representing accumulated context as discrete sequences inflates prompt length, degrades retrieval fidelity, and prevents the gradient-based optimization needed for adaptive memory consolidation. Latent memory resolves this by encoding persistent knowledge as continuous vectors, enabling compact cross-context retention with superior fidelity and adaptability. We organize latent memory into three progressively broader abilities: Working Retention for cache intervention, Persistent Mind evolution for self-evolving knowledge stores, and Multimodal Recall grounding across visual and embodied modalities.

Working Retention. Continuous latent representations transform the KV cache from a passive record into an actively managed working memory that can be augmented, compressed, and consolidated far beyond what discrete token sequences allow. Differentiable cache injection and selective token retention schemes [117, 223] demonstrate that models can deliberate asynchronously and scale to longer sequences without proportional memory growth, while low-rank and cross-layer compression [57, 139] confirm that latent key-vector structure can be exploited to reduce cache footprint without sacrificing representational fidelity. Intrinsic consolidation [65] further shows that working memory can be synthesized directly from the model’s own transient reasoning states, where uncertainty-driven triggering eliminates the need for auxiliary encoders.

Persistent Mind. Latent representations unlock a qualitatively different memory regime where knowledge stores persist across context resets, update selectively, and differentiate into specialized functions through experience alone. Gated and generative approaches [242, 273, 286] establish that latent slots can be durably maintained through differentiable selective writing while being dynamically synthesized on demand, with planning, procedural, and working memory faculties emerging without explicit cognitive supervision. Selfevolving and retrieval-unified methods [59, 274] further demonstrate that these stores improve across queries through dual-phase episodic and procedural consolidation, and can collapse external document retrieval into the same continuous space as generation, enabling end-to-end optimization; this persistent memory regime extends naturally to multi-agent settings [47], where role-conditioned composition resolves homogenization and token-overhead bottlenecks inherent to shared context.

Multimodal Recall. Latent space imposes a structural memory barrier for visual and embodied agents: spatial layout, widget details, and temporal continuity are lost in conversion, rendering token-based memory incapable of sustaining perceptual grounding during extended generation [229, 264]. Continuous encoding methods [229, 230] prove that VLMs can compress multimodal knowledge into fixed-length embeddings compatible with frozen backbones. Unlike text-based memory under long prompts, these methods scale performance monotonically with memory depth. Cognitively structured variants [264] further reveal that organizing latent stores into complementary perceptual and semantic modules prevents systematic drift, establishing continuous latent memory as the essential substrate for anchoring complex tasks.

- 5.6 Collaboration


Collective intelligence in agent systems has traditionally been mediated by natural language [60]. Yet language constitutes an inherent bottleneck: compressing internal representations into discrete tokens discards semantic nuance, increases communication latency, and breaks the gradient pathways required for joint optimization [48, 300]. Latent collaboration addresses these limitations by enabling agents to exchange continuous representations, preserving richer internal states and supporting a more expressive form of collective collaboration. We organize latent collaboration into three progressively broader abilities: Semantic Fidelity for lossless inter-agent state transfer via latent channels, Shared Cognition for identifying and evolving shared latent thought structures across agents, and Heterogeneous Interoperability for extending latent collaboration across diverse model families and modalities without architectural coupling.

Semantic Fidelity. Continuous representations unlock the most structurally immediate advance in multiagent collaboration: replacing token-based message passing with direct latent state transfer that preserves the full semantic content of each agent’s internal representations. Work on KV-cache and hidden-state communication [42, 48, 300] demonstrates that agents can exchange internal states without intermediate decoding, with theoretical analyses confirming that it has strictly higher expressiveness and lower complexity

than text-based counterparts. Complementary alignment approaches [38] further show that a shared latent space can be learned across heterogeneous models, establishing a unified high-bandwidth collaboration channel without modifying any pre-trained parameters.

Shared Cognition. Latent representations further make the structure of shared cognition between agents identifiable and continuously evolvable, a capability that text communication fundamentally lacks. Formal latent variable analyses [47, 265, 290] prove that shared and private thought components between agents can be identified from observable outputs nonparametrically, with the global topology of thought-sharing relationships also theoretically recoverable. Strategy evolution methods [194] demonstrate that agents can update collaborative strategies by reflecting on text embeddings and propagating these reflections into external latent vectors, where stable, disentangled strategic styles emerge over long horizons without model fine-tuning.

Heterogeneous Interoperability. Latent space also enables coordination across agents of different architectures, specializations, and modalities through a shared continuous substrate rather than task-specific natural language protocols. Agent Primitives [79] show that recurring MAS interaction patterns can be abstracted into reusable latent building blocks that generalize across tasks without manual role engineering. Visual latent frameworks [124, 265] further demonstrate that perceptual and reasoning trajectories in multimodal systems can be decoupled into complementary latent memories to overcome the performance-degrading scaling wall of text-centric communication, and that the visual interface of VLMs can serve as a model-agnostic port for injecting heterogeneous reasoning traces directly into a receiver’s perceptual pathway, enabling training-free cross-family collaboration without pair-specific translators.

- 5.7 Embodiment


Embodied agents confront a data bottleneck that no purely linguistic domain faces as acutely: every increment in physical diversity, e.g., new hardware morphologies, viewpoints, and task environments, invalidates existing labeled demonstrations and forces platform-specific re-collection that does not transfer [14, 114, 142]. Action in latent space compounds this by severing the continuous geometric and causal structure that manipulation requires, collapsing spatially rich dynamics into a symbolic bottleneck that discards depth, temporal continuity, and cross-embodiment correspondence. Latent representations dissolve all three failure modes simultaneously, enabling action semantics to emerge from unlabeled video, deliberate reasoning to be internalized as continuous state trajectories, and spatial priors to be distilled directly into policy backbones without instrumentation or re-annotation. We organize latent embodiment into five progressively broader abilities: Unsupervised Grounding for deriving transferable action representations from unlabeled video without embodiment-specific labels, Implicit Thinking for internalizing multi-step planning as continuous latent computation without explicit chain-of-thought generation, Predictive Foresight for simulating future states in latent space to generate dense training signals and guide real-time decision-making, Spatial Cognition for reconstructing 3D/4D geometric structure from 2D observations within the policy latent space, and Generalized Transfer for bridging heterogeneous hardware morphologies through a shared body-agnostic latent substrate.

Unsupervised Grounding. The most consequential advantage latent representations confer on embodied AI is the ability to ground action semantics from internet-scale video without any teleoperation labels, converting the scarcity of robot demonstrations from a structural ceiling into a surmountable bottleneck. Quantization and continuous codebook approaches establish that inter-frame visual transitions can be compressed into latent action tokens that generalize across embodiments and outperform label-supervised models in low-data regimes [14, 196, 255], while grounding fidelity improves further when latent objectives are constrained by physical trajectory priors, contrastive proprioceptive alignment, or disentangled structure-and-motion decomposition [10, 34, 105, 131, 249, 272]. Spatial and temporal structure serve as auxiliary grounding signals that sharpen action-relevance and suppress task-irrelevant distractors, as confirmed by frameworks that jointly address geometric and temporal bottlenecks [19] and by pretraining pipelines that interleave cross-viewpoint alignment with latent action learning [74, 77], collectively demonstrating that the quality of the latent action space, not the quantity of labeled data, is the primary determinant of downstream manipulation generalization.

Implicit Thinking. Continuous representations enable a qualitatively different mode of embodied cognition: replacing the latency-dominated, linguistically bottlenecked chain-of-thought with compact latent trajectories that carry multi-step deliberation directly into the action generation pathway. Reinforcement-learned visual plan latents and their distilled successors [69, 70] show that embodied reasoning can be grounded in action-

aligned visual rewards and compressed into a handful of continuous tokens, achieving long-horizon planning and few-shot adaptation at a fraction of the inference cost of textual alternatives. Curriculum-based approaches that progressively internalize explicit chain-of-thought supervision into pure latent computation [5], architectures that iterate action predictions through recurrent latent refinement at constant memory [198], and frameworks that unify visual dynamics, spatial priors, and proprioceptive states within a single token-efficient reasoning space [128, 132, 136, 152, 187, 235] collectively establish that latent reasoning is not merely more efficient than symbolic alternatives but strictly more expressive for the continuous, spatial domain of physical control.

Predictive Foresight. Latent representations uniquely enable embodied agents to simulate future states without generating pixels, allowing imagined outcomes to serve as training supervision and real-time decision guidance rather than expensive auxiliary outputs. JEPA-style pretraining [184] demonstrates that predicting target-encoder latents of future frames in a leakage-free regime yields dynamics abstractions robust to camera motion and background variation, while world-model-derived latent distances [45] provide dense progress rewards that resolve the sparsity bottleneck of VLA reinforcement learning, achieving near-complete task mastery within two hundred RL steps from a sparse-reward baseline. Frameworks that generate foresight and action within the same latent autoregressive pass [44, 69] further demonstrate that action-aligned visual rewards and reviewable visual look-aheads can be produced in a single forward pass, establishing latent-space future simulation as a training and deployment mechanism that discrete token prediction fundamentally cannot replicate.

Spatial Cognition. Physical manipulation imposes a 3D geometric demand on policies trained from 2D observations, and latent representations are uniquely positioned to reconstruct spatial structure without requiring explicit depth sensors or 3D annotations. Knowledge distillation of frozen geometry-aware encoders into LLM visual token representations [51, 53, 142] demonstrates that aligning policy latents with 3D and 4D structural features injects spatial priors into the backbone without architectural modification, enabling precise contact-rich manipulation where appearance-only latents systematically fail. Treating dense 3D occupancy as both a latent predictive output and a supervisory signal [118] shows that volumetric spatial awareness can be developed from auto-annotated 2D data alone, while jointly addressing geometric and temporal grounding bottlenecks [19, 74] confirms that geometry-aware encoding and cross-viewpoint alignment are complementary and mutually necessary, establishing latent spatial imagination as the representational prerequisite for precise physical interaction under realistic sensor constraints.

Generalized Transfer. Cross-hardware deployment is the structural bottleneck that prevents generalist embodied intelligence from scaling: every morphological change invalidates action spaces and demands platformspecific retraining that cannot amortize across the growing diversity of robotic hardware. Latent action spaces resolve this by functioning as body-agnostic abstraction layers where semantically equivalent motions from heterogeneous embodiments converge, enabling zero-shot cross-platform deployment and data-efficient adaptation without access to task rewards or target-platform demonstrations [77, 176, 281]. Language-action disentanglement via Bayesian decomposition [106] and state-aware latent re-representation [213] further demonstrate that the same latent substrate simultaneously resolves instruction-following collapse and supports multi-modal cross-task generalization, while navigation-oriented latent alignment [182] confirms that the body-agnostic latent principle extends from manipulation to embodied navigation, establishing continuous latent action spaces as the necessary foundation for embodied intelligence that must generalize across hardware morphology, task distribution, and physical environment simultaneously.

- 6 Outlook: What is Next?


The preceding sections survey latent space in large models from multiple angles: its foundational definition and comparison with explicit space, its evolutionary trajectory from early exploration to a full-fledged research paradigm, the technical mechanisms spanning architecture, representation, computation, and optimization that govern latent processing, and the diverse abilities it unlocks across reasoning, planning, modeling, perception, memory, collaboration, and embodiment. Together, these advances demonstrate both the breadth and the momentum of the latent-space paradigm, while also revealing structural limitations and open questions. This section synthesizes these observations into a set of perspectives, challenges, and future directions.

- 6.1 Perspective


The rise of latent space signals a fundamental reorientation in the study of language-based intelligence. Rather than treating latent space as a incidental byproduct of computation, recent research increasingly positions them as a primary substrate. In this perspective, we formulate this survey in four sequential lenses: Foundation (Section 2) intrinsically clarifies what latent space is; Evolution (Section 3) reveals how it has grown from an emerging idea into a broad research paradigm; Mechanism (Section 4) explains through what technical designs is realized; and Ability (Section 5) shows what it enables within the latent space. Viewed as a whole, these dimensions suggest that latent space is a promising candidate basis for the next generation of general-purpose intelligent systems.

Foundation. From a foundational standpoint, latent space should be understood not merely as an auxiliary hidden representation, but as a machine-native space that redefines where language-based autoregressive models compute with the semantic information [66, 239, 301]. Relative to explicit space (or verbal space) [67, 141, 231, 232], its central value lies in four representational properties: machine-native, continuous, flexible & efficient, and high-fidelity, and four functional capabilities: operable, expressive, scalability, and generalized, which reduces the redundancy, discretization bottleneck, inefficiency, and semantic loss inherent in verbalized computation. In this sense, the latent paradigm marks a shift from human-aligned generation to machineoptimal computation. At the same time, this shift introduces a constitutive tension: the gains in efficiency, expressiveness. Thus, the foundational significance of latent space is not only technical but epistemic: it changes both what models compute and how that computation can be understood, laying the groundwork for next-generation models to transcend token-centric operation.

Evolution. The evolutionary trajectory of latent-space research suggests that the field is moving from sprout toward all-round outbreak, in terms of not only the number of the works but also the diversity of paradigms. The early stage established feasibility by showing that reasoning-relevant structure already resides in internal activations and can, in part, bypass explicit verbalization. The subsequent foundation stage supplied theoretical justification, and initial multimodal extensions, thereby converting isolated demonstrations into a coherent research agenda. The later expansion and outbreak stages reveal a further transition: latent space is no longer treated as a compression trick for textual reasoning alone [27, 99, 297], but as a general framework spanning visual cognition, memory, collaboration, and embodied action. This progression indicates that latent space is best viewed not as a transient optimization of autoregressive models, but as an emerging systems principle for next-generation general intelligence.

Mechanism. From a mechanistic perspective, the survey implies that progress in latent space is driven by the co-design of four interdependent dimensions: architecture, representation, computation, and optimization. The key issue is not simply whether a model contains latent variables, but what architectures are utilized, what representations are instantiated, how computation is operated through them, and at how they are optimized. This taxonomy reveals an important trend: the field is gradually moving from heuristic usage toward systematic principle, from externally integrated to internally enabled, from static and fixed to dynamic and adaptive, and from conventional designs to multiple paradigms. Accordingly, future research is less about adding latent space to existing models than about designing models whose primary core is intrinsically latent.

Ability. In terms of ability, the most consequential contribution of latent space is that it broadens the functional scope of intelligence beyond explicit-space models. The survey shows that latent space of language-based models supports not only enhanced reasoning, but also planning, modeling, perception, memory, communication, and embodiment. What unifies these capacities is that they all require structures that are difficult, costly, or fundamentally lossy to externalize in natural language. Latent space therefore acts as a common substrate for general integration across modalities, timescales, and agents. Under this view, its ultimate promise lies not in replacing explicit textual tokens, but in enabling models to coordinate heterogeneous forms of information within a shared continuous latent space. The strongest long-term implication is that latent space may become the principal medium of general-purpose models.

Overall, the perspective presented in this survey about latent space suggests that from its foundational properties to its historical expansion, from its underlying mechanisms to its emerging abilities, latent space consistently points toward a common conclusion: future intelligent systems may rely increasingly on latent rather than purely verbal computation as their primary operating principle.

- 6.2 Challenge


Despite its growing promise as a machine-native substrate for computation, latent space still faces several fundamental obstacles before it can serve as a reliable foundation for general-purpose intelligent systems. The same properties that make latent representations powerful, their continuity, compression, flexibility, and expressive capacity, also make them difficult to inspect, assess, and govern, resulting relatively low Evaluability, Controllability, and Interpretability. Together, these issues reveal that progress in latent space depends not only on improving capability, but also on making latent computation more observable, steerable, and understandable.

Evaluability. A central challenge for latent-space reasoning methods lies in their limited evaluability. Unlike explicit reasoning traces [93, 199], latent trajectories are not directly accessible to human inspection, which makes it inherently difficult to determine whether an intermediate computation is correct, complete, or even relevant to the task at hand [41, 104, 301]. This opacity substantially constrains process-level verification: researchers are often unable to distinguish between genuinely structured intermediate reasoning and representations that merely correlate with the correct output. Consequently, the evaluation of latent reasoning systems still relies predominantly on final-answer accuracy or on post hoc verbalization, both of which offer only indirect and potentially incomplete evidence about the actual reasoning process [99, 285].

Although some recent studies have begun to propose benchmarking strategies for latent-space reasoning [56], the field still lacks mature and widely accepted protocols for supervision and evaluation [166, 301]. Existing approaches remain fragmented across tasks, datasets, and measurement criteria, and there is as yet no standardized framework for assessing the faithfulness, robustness, or internal consistency of latent reasoning trajectories. Such benchmark fragmentation and metric inconsistency make fair comparison across methods difficult, hinder cumulative progress, and complicate the identification of genuine methodological advances.

- As a result, improving evaluability remains one of the most pressing open problems for the development of latent reasoning models.


Controllability. Although latent space is, in principle, a highly operable substrate for computation and control, achieving reliable and generalizable manipulation of latent representations remains a substantial challenge in practice [130, 275, 297]. Fine-grained interventions on hidden states can indeed reshape model behavior in useful and sometimes remarkably precise ways; however, such interventions often suffer from relatively low controllability. The central difficulty lies not merely in identifying where and how to intervene, but in determining how high-level semantic intentions should be specified so that they are simultaneously machineactionable, sufficiently precise, and intelligible to human operators [147, 165, 299]. This tension exposes a deeper gap between continuous internal dynamics and discrete, interpretable objectives. Consequently, the development of truly controllable latent systems requires more than local steering techniques alone: it calls for principled mechanisms that can map explicit goals, safety requirements, and resource constraints onto internal computational processes in a robust and adaptive manner.

Interpretability. The difficulty lies in the very nature of latent representations: they are high-dimensional, distributed, and often deeply entangled, so that neither individual dimensions nor their induced trajectories map neatly onto stable semantic concepts [201, 252, 299]. What emerges is a representational space of immense expressive power, but one whose internal organization is resistant to human understanding. This opacity makes it challenging to explain why a model reaches a particular conclusion, to trace how information is transformed across successive stages of computation, or to determine where error and misalignment first arise [9, 103, 166, 301]. More importantly, the problem is not simply epistemic but institutional: systems that reason through inscrutable latent operations may become more powerful while simultaneously becoming less auditable, less diagnosable, and less accountable. Thus, there is still rooms for the interpretability study.

6.3 Future

Looking ahead, the next decisive step for latent space research is not merely to produce better latent reasoning methods, but to establish latent space as the native substrate of machine intelligence. What is emerging from current progress is a broader architectural shift: explicit language may remain the interface for instruction, generation, and verification, while latent space increasingly becomes the internal workspace where models think, understand, simulate, remember, and act. In this sense, the future of latent space is not simply about

improving efficiency, but about redefining where general-purpose operations happens.

Theory. A central priority for future research is to move beyond empirical success toward a principled theoretical understanding of latent-space intelligence [58]. Rather than merely showing that latent works in practice, the field must explain how and why latent spaces support computation, under what conditions they outperform explicit token-level space, and what forms of reasoning are genuinely native to latent space. In this sense, the key question is not simply whether latent reasoning is more efficient than verbalized reasoning, but when it is more operable, more expressive, more scalable, and more generalizable as a computational substrate. More broadly, the field must progress from scattered theoretical validation to a unified framework for latent representation, latent computation, and the capability gains they enable.

There is therefore an indispensable need for a foundational theory of latent space. Existing work has begun to provide formal accounts of its expressiveness and computational advantages [56, 252, 294], but a systematic theory remains underdeveloped [107, 166, 239, 285, 301]. Future research should clarify not only how latent reasoning operates, but also why, when, and under what constraints it surpasses explicit or verbal reasoning. This requires a deeper account of the geometry, semantics, optimization dynamics, and computational organization of latent trajectories, so that latent reasoning can be understood as more than an effective engineering technique.

Equally important is a principled formulation of explicit and latent spaces as two complementary representational regimes within language-based intelligence [143, 239, 297, 301]. The central issue is not whether latent computation will replace language, but how symbolic and continuous representations differ in expressive capacity, computational function, and communicative role. Within such a framework, explicit language may remain the externally accessible interface for instruction, generation, and verification, while latent space serves as the internal workspace for reasoning, abstraction, memory, simulation, and planning. The theoretical goal is to explain how these two spaces interact, what kinds of information and operations are most naturally allocated to each, and what trade-offs emerge in their coordination.

Future work must also develop a principled theory of trustworthy latent space. Because latent trajectories are inherently opaque to direct human inspection, progress cannot rely on outcome-level performance alone [58,

- 99, 297]. Instead, the field needs rigorous frameworks for evaluability, controllability, and interpretability, together with standardized benchmarks and supervision protocols, to assess the faithfulness, robustness, and internal consistency of latent computation. Without such foundations, benchmark fragmentation and metric inconsistency will continue to obstruct fair comparison and cumulative progress.

Ultimately, the future of latent-space research lies in transforming latent space from an empirical method into a principled theory: one that formally explains its computational advantages, formalizes its relation to explicit space, and renders its hidden processes evaluable, controllable, and interpretable.

Multimodal. The survey suggests that the future of multimodal intelligence, e.g., visual models and embodied models, should not be understood as the mere addition of more sensory channels to language models. Rather, the more consequential shift is the emergence of latent space as a shared computational workspace, in which language, vision, action, memory, and inter-agent communication can be jointly processed within continuous representations. In this view, latent space is no longer a secondary device for compressing reasoning traces, but a machine-native substrate that supports the internal organization of general-purpose intelligence across modalities and timescales.

This perspective implies a first major direction for future research: the transition from text-mediated multimodality to modality-native multimodality latent computation. Existing multimodal systems often rely on translating non-linguistic inputs into textual or tokenized forms before higher-level operation takes place [7, 114, 261]. By contrast, the survey highlights that latent representations can preserve high-fidelity information, reduce modality gaps, and support smoother fusion, alignment, and interaction than explicit symbolic channels. The long-term goal, therefore, is not simply to describe perception in language, but to enable models to operate within visual, spatial, and action-oriented latent spaces directly.

A second direction concerns the evolution from isolated multimodal models to integratedmultimodalsystems [95,

- 100, 135, 264].Across its ability-oriented taxonomy, the survey emphasizes that latent space enables not only reasoning, but also planning, modeling, perception, memory, collaboration, and embodiment. What unifies these capabilities is that they all involve structures that are difficult, costly, or lossy to externalize in natural


language. For this reason, the future of multimodal AI is likely to depend on architectures in which perception, world modeling, memory formation, communication, and action planning are coordinated through a common latent substrate rather than through loosely coupled modules or additional calculations.

Overall, the survey points toward a broader conclusion: the future of multimodal model lies not in expanding token-centric generation to more modalities, but in establishing a unified latent computational substrate for cross-modal reasoning, memory, communication, and embodied interaction. Under this framework, explicit language is likely to remain the interface for instruction, reporting, and verification, whereas latent space increasingly becomes the internal medium in which models think, simulate, coordinate, and act.

Downstream Task. Future downstream progress should be understood as a broader shift in which explicit language remains the interface for instruction, supervision, and verification, while latent space increasingly serves as the internal workspace for computation. Under this view, the most promising downstream tasks are those whose intermediate states are poorly captured by discrete verbal traces, including search-intensive reasoning [58, 99, 297], sequential planning [56, 252], visual perception [261, 261], long-horizon memory [68], multi-agent coordination [60], and embodied control [114]. Across these settings, latent representations offer a unified substrate for compact search, continuous refinement, richer visual grounding, persistent memory, higher-bandwidth coordination, and transferable action abstractions; accordingly, future systems are likely to perform most internal inference, planning, and state evolution in latent space, and externalize only final outputs or strategically selected checkpoints. More broadly, the survey suggests that the central opportunity of latent space lies in moving from text-centric problem solving toward persistent internal state management across heterogeneous tasks and modalities, although realizing this promise will require principled progress in evaluation, control, interpretability, and interface standardization.

Governable. A promising future direction is to develop latent space into an observable and governable substrate. Although latent representations are continuous, compact, and expressive, these same properties also make them difficult to evaluate, control, and interpret. Future work should therefore go beyond improving latent reasoning accuracy, and instead establish a full methodology for trustworthy latent computation: benchmark suites that assess the faithfulness and robustness of latent trajectories; supervision strategies that provide process-level signals rather than only final-answer feedback; controllable latent interfaces that align internal dynamics with explicit goals, resource budgets, and safety requirements; and explainable frameworks that identify semantic structure, causal pathways, and failure sources in latent representations. Such efforts would help bridge the gap between the efficiency of machine-native computation and the need for human oversight, potentially enabling latent space to serve as a dependable substrate.

- 7 Conclusion


In this survey, we have presented a systematic review of latent space in language-based models from five complementary perspectives: foundation, evolution, mechanism, ability, and outlook. Taken together, these perspectives suggest that latent space should be a substrate that may fundamentally reshape how intelligent language models deal with diverse information. We further show that the development of this field has rapidly progressed from early explorations of latent reasoning to a broader and increasingly unified research paradigm spanning language, vision, memory, collaboration, and embodied action.

To systematically organize this promising landscape, we propose a taxonomy along two orthogonal axes: mechanism orientation and ability orientation. On the axis of Mechanism, we classify four key types: architecture, representation, computation, and optimization, which defines how latent space is operationalized. On the axis of Ability, we expand the single type in previous surveys to seven main functional categories: reasoning, planning, modeling, perception, memory, collaboration, and embodiment. Across these dimensions, a consistent trend becomes visible: Latent space brings a fundamental transformation to model mechanisms while pushing the boundaries of model capabilities.

- At the same time, the promise of latent space must be considered together with its unresolved challenges. As increasingly more cognition is internalized into continuous hidden computation, the resulting processes become harder to evaluate, control, and interpret. Future progress will therefore depend not only on improving empirical performance, but also on establishing stronger theoretical foundations, more reliable benchmarks and supervision protocols, and more transparent as well as controllable latent mechanisms. Overall, the


central conclusion of this survey is that latent space holds the potential to become a foundational principle for language-based models. We hope that this survey offers a coherent foundation for future research and serves as a valuable reference for future researchers.

References

- [1] Awni Altabaa, Siyu Chen, John Lafferty, and Zhuoran Yang. Unlocking out-of-distribution generalization in transformers via recursive latent space reasoning. CoRR, abs/2510.14095, 2025. doi: 10.48550/ARXIV.2510.14095. https://doi.org/10.48550/arXiv.2510.14095.
- [2] Ido Amos, Avi Caciularu, Mor Geva, Amir Globerson, Jonathan Herzig, Lior Shani, and Idan Szpektor. Latent reasoning with supervised thinking states. CoRR, abs/2602.08332, 2026. doi: 10.48550/ARXIV.2602.08332. https://doi.org/10.48550/arXiv.2602.08332.
- [3] Daniel P. Armstrong, Zlatko Joncev, Andres M. Bran, and Philippe Schwaller. Synthstrategy: Extracting and formalizing latent strategic insights from llms in organic chemistry. CoRR, abs/2512.01507, 2025. doi: 10.48550/ARXIV.2512.01507. https://doi.org/10.48550/arXiv.2512.01507.
- [4] Arip Asadulaev, Rayan Banerjee, Fakhri Karray, and Martin Takác. Your latent reasoning is secretly policy improvement operator. CoRR, abs/2511.16886, 2025. doi: 10.48550/ARXIV.2511.16886. https://doi.org/10. 48550/arXiv.2511.16886.
- [5] Shuanghao Bai, Jing Lyu, Wanqi Zhou, Zhe Li, Dakai Wang, Lei Xing, Xiaoguang Zhao, Pengwei Wang, Zhongyuan Wang, Cheng Chi, Badong Chen, and Shanghang Zhang. Latent reasoning VLA: latent thinking and prediction for vision-language-action models. CoRR, abs/2602.01166, 2026. doi: 10.48550/ARXIV.2602.01166. https://doi.org/10.48550/arXiv.2602.01166.
- [6] Sarah Ball, Simeon Allmendinger, Frauke Kreuter, and Niklas Kühl. Human preferences in large language model latent space: A technical analysis on the reliability of synthetic data in voting outcome prediction. CoRR, abs/2502.16280, 2025. doi: 10.48550/ARXIV.2502.16280. https://doi.org/10.48550/arXiv.2502.16280.
- [7] Tadas Baltrusaitis, Chaitanya Ahuja, and Louis-Philippe Morency. Multimodal machine learning: A survey and taxonomy. IEEE Trans. Pattern Anal. Mach. Intell., 41(2):423–443, 2019. doi: 10.1109/TPAMI.2018.2798607. https://doi.org/10.1109/TPAMI.2018.2798607.
- [8] Yoshua Bengio, Aaron C. Courville, and Pascal Vincent. Representation learning: A review and new perspectives. IEEE Trans. Pattern Anal. Mach. Intell., 35(8):1798–1828, 2013. doi: 10.1109/TPAMI.2013.50. https://doi. org/10.1109/TPAMI.2013.50.
- [9] Davide Berasi, Matteo Farina, Massimiliano Mancini, Elisa Ricci, and Nicola Strisciuglio. Not only text: Exploring compositionality of visual representations in vision-language models. In IEEE/CVF Conference on Computer Vision and Pattern Recognition, CVPR 2025, Nashville, TN, USA, June 1115, 2025, pages 24917–24927. Computer Vision Foundation / IEEE, 2025. doi: 10.1109/CVPR52734. 2025.02320. https://openaccess.thecvf.com/content/CVPR2025/html/Berasi_Not_Only_Text_Exploring_ Compositionality_of_Visual_Representations_in_Vision-Language_CVPR_2025_paper.html.
- [10] Hongzhe Bi, Hengkai Tan, Shenghao Xie, Zeyuan Wang, Shuhe Huang, Haitian Liu, Ruowen Zhao, Yao Feng, Chendong Xiang, Yinze Rong, Hongyan Zhao, Hanyu Liu, Zhizhong Su, Lei Ma, Hang Su, and Jun Zhu. Motus: A unified latent action world model. CoRR, abs/2512.13030, 2025. doi: 10.48550/ARXIV.2512.13030. https://doi.org/10.48550/arXiv.2512.13030.
- [11] Mahtab Bigverdi, Zelun Luo, Cheng-Yu Hsieh, Ethan Shen, Dongping Chen, Linda G. Shapiro, and Ranjay Krishna. Perception tokens enhance visual reasoning in multimodal language models. In IEEE/CVF Conference on Computer Vision and Pattern Recognition, CVPR 2025, Nashville, TN, USA, June 1115, 2025, pages 3836–3845. Computer Vision Foundation / IEEE, 2025. doi: 10.1109/CVPR52734.2025.

00363. https://openaccess.thecvf.com/content/CVPR2025/html/Bigverdi_Perception_Tokens_Enhance_ Visual_Reasoning_in_Multimodal_Language_Models_CVPR_2025_paper.html.

- [12] Andreas Blattmann, Tim Dockhorn, Sumith Kulal, Daniel Mendelevitch, Maciej Kilian, Dominik Lorenz, Yam Levi, Zion English, Vikram Voleti, Adam Letts, Varun Jampani, and Robin Rombach. Stable video diffusion: Scaling latent video diffusion models to large datasets. CoRR, abs/2311.15127, 2023. doi: 10.48550/ARXIV. 2311.15127. https://doi.org/10.48550/arXiv.2311.15127.


- [13] Tom B. Brown, Benjamin Mann, Nick Ryder, Melanie Subbiah, Jared Kaplan, Prafulla Dhariwal, Arvind Neelakantan, Pranav Shyam, Girish Sastry, Amanda Askell, Sandhini Agarwal, Ariel Herbert-Voss, Gretchen Krueger, Tom Henighan, Rewon Child, Aditya Ramesh, Daniel M. Ziegler, Jeffrey Wu, Clemens Winter, Christopher Hesse, Mark Chen, Eric Sigler, Mateusz Litwin, Scott Gray, Benjamin Chess, Jack Clark, Christopher Berner, Sam McCandlish, Alec Radford, Ilya Sutskever, and Dario Amodei. Language models are few-shot learners. In Hugo Larochelle, Marc’Aurelio Ranzato, Raia Hadsell, Maria-Florina Balcan, and Hsuan-Tien Lin, editors, Advances in Neural Information Processing Systems 33: Annual Conference on Neural Information Processing Systems 2020, NeurIPS 2020, December 6-12, 2020, virtual, 2020. https://proceedings.neurips.cc/ paper/2020/hash/1457c0d6bfcb4967418bfb8ac142f64a-Abstract.html.
- [14] Qingwen Bu, Yanting Yang, Jisong Cai, Shenyuan Gao, Guanghui Ren, Maoqing Yao, Ping Luo, and Hongyang Li. Univla: Learning to act anywhere with task-centric latent actions. CoRR, abs/2505.06111, 2025. doi: 10.48550/ARXIV.2505.06111. https://doi.org/10.48550/arXiv.2505.06111.
- [15] Xizhou Bu, Jiexi Lyu, Fulei Sun, Ruichen Yang, Zhiqiang Ma, and Wei Li. LAOF: robust latent action learning with optical flow constraints. CoRR, abs/2511.16407, 2025. doi: 10.48550/ARXIV.2511.16407. https: //doi.org/10.48550/arXiv.2511.16407.
- [16] Mateusz Bystronski, Mikolaj Holysz, Grzegorz Piotrowski, Nitesh V. Chawla, and Tomasz Kajdanowicz. Large language models as innovators: A framework to leverage latent space exploration for novelty discovery. CoRR, abs/2507.13874, 2025. doi: 10.48550/ARXIV.2507.13874. https://doi.org/10.48550/arXiv.2507.13874.
- [17] Mateusz Bystronski, Grzegorz Piotrowski, Nitesh V. Chawla, and Tomasz Kajdanowicz. Latentprompt: Optimizing promts in latent space. CoRR, abs/2508.02452, 2025. doi: 10.48550/ARXIV.2508.02452. https://doi.org/10.48550/arXiv.2508.02452.
- [18] Zhaolin Cai, Fan Li, Huiyu Duan, Lijun He, and Guangtao Zhai. Steering and rectifying latent representation manifolds in frozen multi-modal llms for video anomaly detection. arXiv preprint arXiv:2602.24021, 2026.
- [19] Zhejia Cai, Yandan Yang, Xinyuan Chang, Shiyi Liang, Ronghan Chen, Feng Xiong, Mu Xu, and Ruqi Huang. Seeing space and motion: Enhancing latent actions with spatial and dynamic awareness for VLA. CoRR, abs/2509.26251, 2025. doi: 10.48550/ARXIV.2509.26251. https://doi.org/10.48550/arXiv.2509.26251.
- [20] Chao Chen, Zhixin Ma, Yongqi Li, Yupeng Hu, Yinwei Wei, Wenjie Li, and Liqiang Nie. Reasoning in the dark: Interleaved vision-text reasoning in latent space. CoRR, abs/2510.12603, 2025. doi: 10.48550/ARXIV.2510.12603. https://doi.org/10.48550/arXiv.2510.12603.
- [21] Delong Chen, Mustafa Shukor, Théo Moutakanni, Willy Chung, Jade Yu, Tejaswi Kasarla, Allen Bolourchi, Yann LeCun, and Pascale Fung. VL-JEPA: joint embedding predictive architecture for vision-language. CoRR, abs/2512.10942, 2025. doi: 10.48550/ARXIV.2512.10942. https://doi.org/10.48550/arXiv.2512.10942.
- [22] Haolin Chen, Yihao Feng, Zuxin Liu, Weiran Yao, Akshara Prabhakar, Shelby Heinecke, Ricky Ho, Phil Mui, Silvio Savarese, Caiming Xiong, and Huan Wang. Language models are hidden reasoners: Unlocking latent reasoning capabilities via self-rewarding. CoRR, abs/2411.04282, 2024. doi: 10.48550/ARXIV.2411.04282. https://doi.org/10.48550/arXiv.2411.04282.
- [23] Lihu Chen, Xiang Yin, and Francesca Toni. Latent debate: A surrogate framework for interpreting LLM thinking. CoRR, abs/2512.01909, 2025. doi: 10.48550/ARXIV.2512.01909. https://doi.org/10.48550/arXiv.2512.01909.
- [24] Peng Chen, Chao Huang, Yunkang Cao, Chengliang Liu, Wenqiang Wang, Mingbo Yang, Li Shen, Wenqi Ren, and Xiaochun Cao. Reason-iad: Knowledge-guided dynamic latent reasoning for explainable industrial anomaly detection. CoRR, abs/2602.09850, 2026. doi: 10.48550/ARXIV.2602.09850. https://doi.org/10.48550/arXiv. 2602.09850.
- [25] Sijia Chen and Di Niu. iclp: Large language model reasoning with implicit cognition latent planning. CoRR, abs/2512.24014, 2025. doi: 10.48550/ARXIV.2512.24014. https://doi.org/10.48550/arXiv.2512.24014.
- [26] Xiaoyu Chen, Hangxing Wei, Pushi Zhang, Chuheng Zhang, Kaixin Wang, Yanjiang Guo, Rushuai Yang, Yucen Wang, Xinquan Xiao, Li Zhao, Jianyu Chen, and Jiang Bian. villa-x: Enhancing latent action modeling in vision-language-action models. CoRR, abs/2507.23682, 2025. doi: 10.48550/ARXIV.2507.23682. https: //doi.org/10.48550/arXiv.2507.23682.
- [27] Xinghao Chen, Anhao Zhao, Heming Xia, Xuan Lu, Hanlin Wang, Yanjun Chen, Wei Zhang, Jian Wang, Wenjie Li, and Xiaoyu Shen. Reasoning beyond language: A comprehensive survey on latent chain-of-thought reasoning. CoRR, abs/2505.16782, 2025. doi: 10.48550/ARXIV.2505.16782. https://doi.org/10.48550/arXiv.2505.16782.


- [28] Zhangquan Chen, Manyuan Zhang, Xinlei Yu, Xufang Luo, Mingze Sun, Zihao Pan, Yan Feng, Peng Pei, Xunliang Cai, and Ruqi Huang. Think with 3d: Geometric imagination grounded spatial reasoning from limited views. CoRR, abs/2510.18632, 2025. doi: 10.48550/ARXIV.2510.18632. https://doi.org/10.48550/arXiv.2510.18632.
- [29] Zhikang Chen, Sen Cui, Deheng Ye, Yu Zhang, Yatao Bian, and Tingting Zhu. Think consistently, reason efficiently: Energy-based calibration for implicit chain-of-thought. CoRR, abs/2511.07124, 2025. doi: 10.48550/ ARXIV.2511.07124. https://doi.org/10.48550/arXiv.2511.07124.
- [30] Zhisheng Chen, Tingyu Wu, Zijie Zhou, Zhengwei Xie, Ziyan Weng, and Yingwei Zhang. Polarmem: A training-free polarized latent graph memory for verifiable multimodal agents. CoRR, abs/2602.00415, 2026. doi: 10.48550/ARXIV.2602.00415. https://doi.org/10.48550/arXiv.2602.00415.
- [31] Jeffrey Cheng and Benjamin Van Durme. Compressed chain of thought: Efficient reasoning through dense representations. CoRR, abs/2412.13171, 2024. doi: 10.48550/ARXIV.2412.13171. https://doi.org/10.48550/ arXiv.2412.13171.
- [32] Yunlong Chu, Minglai Shao, Yuhang Liu, Bing Hao, Yumeng Lin, Jialu Wang, and Ruijie Wang. Spot: Spanlevel pause-of-thought for efficient and interpretable latent reasoning in large language models. arXiv preprint arXiv:2603.06222, 2026.
- [33] Julian Coda-Forno, Zhuokai Zhao, Qiang Zhang, Dipesh Tamboli, Weiwei Li, Xiangjun Fan, Lizhu Zhang, Eric Schulz, and Hsiao-Ping Tseng. Exploring system 1 and 2 communication for latent reasoning in llms. CoRR, abs/2510.00494, 2025. doi: 10.48550/ARXIV.2510.00494. https://doi.org/10.48550/arXiv.2510.00494.
- [34] Weisheng Dai, Kai Lan, Jianyi Zhou, Bo Zhao, Xiu Su, Junwen Tong, Weili Guan, and Shuo Yang. Conla: Contrastive latent action learning from human videos for robotic manipulation. CoRR, abs/2602.00557, 2026. doi: 10.48550/ARXIV.2602.00557. https://doi.org/10.48550/arXiv.2602.00557.
- [35] Grégoire Delétang, Anian Ruoss, Paul-Ambroise Duquenne, Elliot Catt, Tim Genewein, Christopher Mattern, Jordi Grau-Moya, Li Kevin Wenliang, Matthew Aitchison, Laurent Orseau, Marcus Hutter, and Joel Veness. Language modeling is compression. In The Twelfth International Conference on Learning Representations, ICLR 2024, Vienna, Austria, May 7-11, 2024. OpenReview.net, 2024. https://openreview.net/forum?id=jznbgiynus.
- [36] Huilin Deng, Hongchen Luo, Yue Zhu, Long Li, Zhuoyue Chen, Xinghao Zhao, Ming Li, Jihai Zhang, Mengchang Wang, Yang Cao, and Yu Kang. IIB-LPO: latent policy optimization via iterative information bottleneck. CoRR, abs/2601.05870, 2026. doi: 10.48550/ARXIV.2601.05870. https://doi.org/10.48550/arXiv.2601.05870.
- [37] Jingcheng Deng, Liang Pang, Zihao Wei, Shicheng Xu, Zenghao Duan, Kun Xu, Yang Song, Huawei Shen, and Xueqi Cheng. Llm latent reasoning as chain of superposition. CoRR, abs/2510.15522, 2025. doi: 10.48550/ ARXIV.2510.15522. https://doi.org/10.48550/arXiv.2510.15522.
- [38] Lucio M. Dery, Zohar Yahav, Henry Prior, Qixuan Feng, Jiajun Shen, and Arthur Szlam. Latent space communication via K-V cache alignment. CoRR, abs/2601.06123, 2026. doi: 10.48550/ARXIV.2601.06123. https://doi.org/10.48550/arXiv.2601.06123.
- [39] Shuai Dong, Siyuan Wang, Xingyu Liu, and Zhongyu Wei. Interleaved latent visual reasoning with selective perceptual modeling. CoRR, abs/2512.05665, 2025. doi: 10.48550/ARXIV.2512.05665. https://doi.org/10. 48550/arXiv.2512.05665.
- [40] Yihong Dong, Yuchen Liu, Xue Jiang, Bin Gu, Zhi Jin, and Ge Li. Rethinking repetition problems of llms in code generation. In Wanxiang Che, Joyce Nabende, Ekaterina Shutova, and Mohammad Taher Pilehvar, editors, Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), ACL 2025, Vienna, Austria, July 27 - August 1, 2025, pages 965–985. Association for Computational Linguistics, 2025. https://aclanthology.org/2025.acl-long.48/.
- [41] Hanwen Du, Yuxin Dong, and Xia Ning. Latent thinking optimization: Your latent reasoning language model secretly encodes reward signals in its latent thoughts. CoRR, abs/2509.26314, 2025. doi: 10.48550/ARXIV.2509.

26314. https://doi.org/10.48550/arXiv.2509.26314.

- [42] Zhuoyun Du, Runze Wang, Huiyu Bai, Zouying Cao, Xiaoyong Zhu, Bo Zheng, Wei Chen, and Haochao Ying. Enabling agents to communicate entirely in latent space. CoRR, abs/2511.09149, 2025. doi: 10.48550/ARXIV. 2511.09149. https://doi.org/10.48550/arXiv.2511.09149.
- [43] Patrick Esser, Robin Rombach, and Björn Ommer. Taming transformers for high-resolution image synthesis. In IEEE Conference on Computer Vision and Pattern Recognition, CVPR 2021, virtual, June 19-25, 2021, pages 12873–12883. Computer Vision Foundation / IEEE, 2021. doi: 10.1109/CVPR46437.


- 2021.01268. https://openaccess.thecvf.com/content/CVPR2021/html/Esser_Taming_Transformers_for_ High-Resolution_Image_Synthesis_CVPR_2021_paper.html.
- [44] Jingjing Fan, Yushan Liu, Shoujie Li, Botao Ren, Siyuan Li, Xiao-Ping Zhang, Wenbo Ding, and Zhidong Deng. Future-vla: Forecasting unified trajectories under real-time execution. arXiv preprint arXiv:2602.15882, 2026.
- [45] Senyu Fei, Siyin Wang, Li Ji, Ao Li, Shiduo Zhang, Liming Liu, Jinlong Hou, Jingjing Gong, Xianzhong Zhao, and Xipeng Qiu. SRPO: self-referential policy optimization for vision-language-action models. CoRR, abs/2511.15605,

2025. doi: 10.48550/ARXIV.2511.15605. https://doi.org/10.48550/arXiv.2511.15605.

- [46] Sicheng Feng, Gongfan Fang, Xinyin Ma, and Xinchao Wang. Efficient reasoning models: A survey. Trans. Mach. Learn. Res., 2025, 2025. https://openreview.net/forum?id=sySqlxj8EB.
- [47] Muxin Fu, Guibin Zhang, Xiangyuan Xue, Yafu Li, Zefeng He, Siyuan Huang, Xiaoye Qu, Yu Cheng, and Yang Yang. Latentmem: Customizing latent memory for multi-agent systems. CoRR, abs/2602.03036, 2026. doi: 10.48550/ARXIV.2602.03036. https://doi.org/10.48550/arXiv.2602.03036.
- [48] Tianyu Fu, Zihan Min, Hanling Zhang, Jichao Yan, Guohao Dai, Wanli Ouyang, and Yu Wang. Cache-tocache: Direct semantic communication between large language models. CoRR, abs/2510.03215, 2025. doi: 10.48550/ARXIV.2510.03215. https://doi.org/10.48550/arXiv.2510.03215.
- [49] Tianyu Fu, Yichen You, Zekai Chen, Guohao Dai, Huazhong Yang, and Yu Wang. Think-at-hard: Selective latent iterations to improve reasoning language models. CoRR, abs/2511.08577, 2025. doi: 10.48550/ARXIV.2511.08577. https://doi.org/10.48550/arXiv.2511.08577.
- [50] Jonas Geiping, Sean McLeish, Neel Jain, John Kirchenbauer, Siddharth Singh, Brian R. Bartoldson, Bhavya Kailkhura, Abhinav Bhatele, and Tom Goldstein. Scaling up test-time compute with latent reasoning: A recurrent depth approach. CoRR, abs/2502.05171, 2025. doi: 10.48550/ARXIV.2502.05171. https://doi.org/10.48550/ arXiv.2502.05171.
- [51] Manish Kumar Govind, Dominick Reilly, Pu Wang, and Srijan Das. Unilact: Depth-aware rgb latent action learning for vision-language-action models. arXiv preprint arXiv:2602.20231, 2026.
- [52] Halil Alperen Gozeten, Muhammed Emrullah Ildiz, Xuechen Zhang, Hrayr Harutyunyan, Ankit Singh Rawat, and Samet Oymak. Continuous chain of thought enables parallel exploration and reasoning. CoRR, abs/2505.23648,

2025. doi: 10.48550/ARXIV.2505.23648. https://doi.org/10.48550/arXiv.2505.23648.

- [53] Minghao Guo, Meng Cao, Jiachen Tao, Rongtao Xu, Yan Yan, Xiaodan Liang, Ivan Laptev, and Xiaojun Chang. Glad: Geometric latent distillation for vision-language-action models. CoRR, abs/2512.09619, 2025. doi: 10.48550/ARXIV.2512.09619. https://doi.org/10.48550/arXiv.2512.09619.
- [54] Zihao Guo, Jian Wang, Ruxin Zhou, Youhua Liu, Jiawei Guo, Jun Zhao, Xiaoxiao Xu, Yongqi Liu, and Kaiqiao Zhan. S2gr: Stepwise semantic-guided reasoning in latent space for generative recommendation. CoRR, abs/2601.18664, 2026. doi: 10.48550/ARXIV.2601.18664. https://doi.org/10.48550/arXiv.2601.18664.
- [55] Alexander Gurung, Nikolay Malkin, and Mirella Lapata. Lightweight latent reasoning for narrative tasks. CoRR, abs/2512.02240, 2025. doi: 10.48550/ARXIV.2512.02240. https://doi.org/10.48550/arXiv.2512.02240.
- [56] Thilo Hagendorff and Sarah Fabi. Beyond chains of thought: Benchmarking latent-space reasoning abilities in large language models. CoRR, abs/2504.10615, 2025. doi: 10.48550/ARXIV.2504.10615. https://doi.org/10. 48550/arXiv.2504.10615.
- [57] Jitai Hao, Qiang Huang, Yaowei Wang, Min Zhang, and Jun Yu. Deltakv: Residual-based KV cache compression via long-range similarity. CoRR, abs/2602.08005, 2026. doi: 10.48550/ARXIV.2602.08005. https://doi.org/10. 48550/arXiv.2602.08005.
- [58] Shibo Hao, Sainbayar Sukhbaatar, DiJia Su, Xian Li, Zhiting Hu, Jason Weston, and Yuandong Tian. Training large language models to reason in a continuous latent space. CoRR, abs/2412.06769, 2024. doi: 10.48550/ ARXIV.2412.06769. https://doi.org/10.48550/arXiv.2412.06769.
- [59] Jie He, Richard He Bai, Sinead Williamson, Jeff Z. Pan, Navdeep Jaitly, and Yizhe Zhang. Clara: Bridging retrieval and generation with continuous latent reasoning. CoRR, abs/2511.18659, 2025. doi: 10.48550/ARXIV.2511.18659. https://doi.org/10.48550/arXiv.2511.18659.
- [60] Junda He, Christoph Treude, and David Lo. Llm-based multi-agent systems for software engineering: Literature review, vision, and the road ahead. ACM Trans. Softw. Eng. Methodol., 34(5):124:1–124:30, 2025. doi: 10.1145/3712003. https://doi.org/10.1145/3712003.


- [61] Yinhan He, Wendy Zheng, Yaochen Zhu, Zaiyi Zheng, Lin Su, Sriram Vasudevan, Qi Guo, Liangjie Hong, and Jundong Li. Semcot: Accelerating chain-of-thought reasoning through semantically-aligned implicit tokens. CoRR, abs/2510.24940, 2025. doi: 10.48550/ARXIV.2510.24940. https://doi.org/10.48550/arXiv.2510.24940.
- [62] Yixin He and Lumingyuan Tang. Learning to ponder: Adaptive reasoning in latent space. CoRR, abs/2509.24238,

2025. doi: 10.48550/ARXIV.2509.24238. https://doi.org/10.48550/arXiv.2509.24238.

- [63] Zhenghao He, Guangzhi Xiong, Bohan Liu, Sanchit Sinha, and Aidong Zhang. Reasoning beyond chainof-thought: A latent computational mode in large language models. CoRR, abs/2601.08058, 2026. doi: 10.48550/ARXIV.2601.08058. https://doi.org/10.48550/arXiv.2601.08058.
- [64] Lukas Helff, Ruben Härle, Wolfgang Stammer, Felix Friedrich, Manuel Brack, Antonia Wüst, Hikaru Shindo, Patrick Schramowski, and Kristian Kersting. Activationreasoning: Logical reasoning in latent activation spaces. CoRR, abs/2510.18184, 2025. doi: 10.48550/ARXIV.2510.18184. https://doi.org/10.48550/arXiv.2510.18184.
- [65] Yubo Hou, Zhisheng Chen, Tao Wan, and Zengchang Qin. Flashmem: Distilling intrinsic latent memory via computation reuse. CoRR, abs/2601.05505, 2026. doi: 10.48550/ARXIV.2601.05505. https://doi.org/10.48550/ arXiv.2601.05505.
- [66] Lijie Hu, Liang Liu, Shu Yang, Xin Chen, Zhen Tan, Muhammad Asif Ali, Mengdi Li, and Di Wang. Understanding reasoning in chain-of-thought from the hopfieldian view. CoRR, abs/2410.03595, 2024. doi: 10.48550/ARXIV. 2410.03595. https://doi.org/10.48550/arXiv.2410.03595.
- [67] Xiaobin Hu, Yunhang Qian, Jiaquan Yu, Jingjing Liu, Peng Tang, Xiaozhong Ji, Chengming Xu, Jiawei Liu, Xiaoxiao Yan, Xinlei Yu, et al. The landscape of medical agents: A survey. Authorea Preprints, 2025.
- [68] Yuyang Hu, Shichun Liu, Yanwei Yue, Guibin Zhang, Boyang Liu, Fangyi Zhu, Jiahang Lin, Honglin Guo, Shihan Dou, Zhiheng Xi, Senjie Jin, Jiejun Tan, Yanbin Yin, Jiongnan Liu, Zeyu Zhang, Zhongxiang Sun, Yutao Zhu, Hao Sun, Boci Peng, Zhenrong Cheng, Xuanbo Fan, Jiaxin Guo, Xinlei Yu, Zhenhong Zhou, Zewen Hu, Jiahao Huo, Junhao Wang, Yuwei Niu, Yu Wang, Zhenfei Yin, Xiaobin Hu, Yue Liao, Qiankun Li, Kun Wang, Wangchunshu Zhou, Yixin Liu, Dawei Cheng, Qi Zhang, Tao Gui, Shirui Pan, Yan Zhang, Philip Torr, Zhicheng Dou, Ji-Rong Wen, Xuanjing Huang, Yu-Gang Jiang, and Shuicheng Yan. Memory in the age of AI agents. CoRR, abs/2512.13564, 2025. doi: 10.48550/ARXIV.2512.13564. https://doi.org/10.48550/arXiv.2512.13564.
- [69] Chi-Pin Huang, Yueh-Hua Wu, Min-Hung Chen, Yu-Chiang Frank Wang, and Fu-En Yang. Thinkact: Visionlanguage-action reasoning via reinforced visual latent planning. CoRR, abs/2507.16815, 2025. doi: 10.48550/ ARXIV.2507.16815. https://doi.org/10.48550/arXiv.2507.16815.
- [70] Chi-Pin Huang, Yunze Man, Zhiding Yu, Min-Hung Chen, Jan Kautz, Yu-Chiang Frank Wang, and Fu-En Yang. Fast-thinkact: Efficient vision-language-action reasoning via verbalizable latent planning. CoRR, abs/2601.09708,

2026. doi: 10.48550/ARXIV.2601.09708. https://doi.org/10.48550/arXiv.2601.09708.

- [71] Jiahao Huo, Yu Huang, Yibo Yan, Ye Pan, Yi Cao, Mingdong Ou, Philip S. Yu, and Xuming Hu. Causalembed: Auto-regressive multi-vector generation in latent space for visual document embedding. CoRR, abs/2601.21262,

2026. doi: 10.48550/ARXIV.2601.21262. https://doi.org/10.48550/arXiv.2601.21262.

- [72] Ahmadreza Jeddi, Marco Ciccone, and Babak Taati. Loopformer: Elastic-depth looped transformers for latent reasoning via shortcut modulation. arXiv preprint arXiv:2602.11451, 2026.
- [73] Byungwoo Jeon, Yoonwoo Jeong, Hyunseok Lee, Minsu Cho, and Jinwoo Shin. Vision-aligned latent reasoning for multi-modal large language model. CoRR, abs/2602.04476, 2026. doi: 10.48550/ARXIV.2602.04476. https://doi.org/10.48550/arXiv.2602.04476.
- [74] Youngjoon Jeong, Junha Chun, and Taesup Kim. Learning to act robustly with view-invariant latent actions. CoRR, abs/2601.02994, 2026. doi: 10.48550/ARXIV.2601.02994. https://doi.org/10.48550/arXiv.2601.02994.
- [75] Feiyang Jia, Lin Liu, Ziying Song, Caiyan Jia, Hangjun Ye, Xiaoshuai Hao, and Long Chen. Driveworld-vla: Unified latent-space world modeling with vision-language-action for autonomous driving. CoRR, abs/2602.06521,

2026. doi: 10.48550/ARXIV.2602.06521. https://doi.org/10.48550/arXiv.2602.06521.

- [76] Enyi Jiang, Yibo Jacky Zhang, Yinglun Xu, Andreas Haupt, Nancy M. Amato, and Sanmi Koyejo. Latent adversarial regularization for offline preference optimization. CoRR, abs/2601.22083, 2026. doi: 10.48550/ ARXIV.2601.22083. https://doi.org/10.48550/arXiv.2601.22083.
- [77] Haoran Jiang, Jin Chen, Qingwen Bu, Li Chen, Modi Shi, Yanjie Zhang, Delong Li, Chuanzhe Suo, Chuang Wang, Zhihui Peng, and Hongyang Li. Wholebodyvla: Towards unified latent VLA for whole-body loco-manipulation


- control. CoRR, abs/2512.11047, 2025. doi: 10.48550/ARXIV.2512.11047. https://doi.org/10.48550/arXiv.2512. 11047.
- [78] Nan Jiang, Ziming Wu, De-Chuan Zhan, Fuming Lai, and Shaobing Lian. DART: distilling autoregressive reasoning to silent thought. In Christos Christodoulopoulos, Tanmoy Chakraborty, Carolyn Rose, and Violet Peng, editors, Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing, EMNLP 2025, Suzhou, China, November 4-9, 2025, pages 5100–5108. Association for Computational Linguistics, 2025. doi: 10.18653/V1/2025.EMNLP-MAIN.256. https://doi.org/10.18653/v1/2025.emnlp-main.256.
- [79] Haibo Jin, Kuang Peng, Ye Yu, Xiaopeng Yuan, and Haohan Wang. Agent primitives: Reusable latent building blocks for multi-agent systems. CoRR, abs/2602.03695, 2026. doi: 10.48550/ARXIV.2602.03695. https://doi.org/10.48550/arXiv.2602.03695.
- [80] Jiajie Jin, Yanzhao Zhang, Mingxin Li, Dingkun Long, Pengjun Xie, Yutao Zhu, and Zhicheng Dou. Laser: Internalizing explicit reasoning into latent space for dense retrieval. arXiv preprint arXiv:2603.01425, 2026.
- [81] Sri Durga Sai Sowmya Kadali and Evangelos E Papalexakis. Jailbreaking leaves a trace: Understanding and detecting jailbreak attacks from internal representations of large language models. arXiv preprint arXiv:2602.11495, 2026.
- [82] Ilay Kamai, Marc-Huertas Company, Mike J Smith, and Hagai B Perets. Talking with the latents–how to convert your llm into an astronomer. arXiv preprint arXiv:2602.09670, 2026.
- [83] Haoqiang Kang, Yizhe Zhang, Nikki Lijing Kuang, Nicklas Majamaki, Navdeep Jaitly, Yi-An Ma, and Lianhui Qin. Ladir: Latent diffusion enhances llms for text reasoning. CoRR, abs/2510.04573, 2025. doi: 10.48550/ ARXIV.2510.04573. https://doi.org/10.48550/arXiv.2510.04573.
- [84] Kentaro Kazama, Daiki Shirafuji, and Tatsuhiko Saito. Geosteer: Faithful chain-of-thought steering via latent manifold gradients. CoRR, abs/2601.10229, 2026. doi: 10.48550/ARXIV.2601.10229. https://doi.org/10.48550/ arXiv.2601.10229.
- [85] Diederik P. Kingma and Max Welling. Auto-encoding variational bayes. In Yoshua Bengio and Yann LeCun, editors, 2nd International Conference on Learning Representations, ICLR 2014, Banff, AB, Canada, April 14-16, 2014, Conference Track Proceedings, 2014. http://arxiv.org/abs/1312.6114.
- [86] Jonas Knupp, Jan Hendrik Metzen, Jeremias Bohn, Georg Groh, and Kristian Kersting. Depth-recurrent attention mixtures: Giving latent reasoning the attention it deserves. CoRR, abs/2601.21582, 2026. doi: 10.48550/ARXIV.2601.21582. https://doi.org/10.48550/arXiv.2601.21582.
- [87] Yeskendir Koishekenov, Aldo Lipani, and Nicola Cancedda. Encode, think, decode: Scaling test-time reasoning with recursive latent thoughts. CoRR, abs/2510.07358, 2025. doi: 10.48550/ARXIV.2510.07358. https: //doi.org/10.48550/arXiv.2510.07358.
- [88] Deqian Kong, Minglu Zhao, Aoyang Qin, Bo Pang, Chenxin Tao, David Hartmann, Edouardo Honig, Dehong Xu, Amit Kumar, Matthew Sarte, Chuan Li, Jianwen Xie, and Ying Nian Wu. Inference-time rethinking with latent thought vectors for math reasoning. CoRR, abs/2602.06584, 2026. doi: 10.48550/ARXIV.2602.06584. https://doi.org/10.48550/arXiv.2602.06584.
- [89] Tomek Korbak, Mikita Balesni, Elizabeth Barnes, Yoshua Bengio, Joe Benton, Joseph Bloom, Mark Chen, Alan Cooney, Allan Dafoe, Anca D. Dragan, Scott Emmons, Owain Evans, David Farhi, Ryan Greenblatt, Dan Hendrycks, Marius Hobbhahn, Evan Hubinger, Geoffrey Irving, Erik Jenner, Daniel Kokotajlo, Victoria Krakovna, Shane Legg, David Lindner, David Luan, Aleksander Madry, Julian Michael, Neel Nanda, Dave Orr, Jakub Pachocki, Ethan Perez, Mary Phuong, Fabien Roger, Joshua Saxe, Buck Shlegeris, Martín Soto, Eric Steinberger, Jasmine Wang, Wojciech Zaremba, Bowen Baker, Rohin Shah, and Vladimir Mikulik. Chain of thought monitorability: A new and fragile opportunity for AI safety. CoRR, abs/2507.11473, 2025. doi: 10.48550/ARXIV.2507.11473. https://doi.org/10.48550/arXiv.2507.11473.
- [90] Benno Krojer, Shravan Nayak, Oscar Mañas, Vaibhav Adlakha, Desmond Elliott, Siva Reddy, and Marius Mosbach. Latentlens: Revealing highly interpretable visual tokens in llms. CoRR, abs/2602.00462, 2026. doi: 10.48550/ARXIV.2602.00462. https://doi.org/10.48550/arXiv.2602.00462.
- [91] Anna Kuzina, Maciej Pioro, Paul N. Whatmough, and Babak Ehteshami Bejnordi. Kava: Latent reasoning via compressed kv-cache distillation. CoRR, abs/2510.02312, 2025. doi: 10.48550/ARXIV.2510.02312. https: //doi.org/10.48550/arXiv.2510.02312.


- [92] Tamera Lanham, Anna Chen, Ansh Radhakrishnan, Benoit Steiner, Carson Denison, Danny Hernandez, Dustin Li, Esin Durmus, Evan Hubinger, Jackson Kernion, Kamile Lukosiute, Karina Nguyen, Newton Cheng, Nicholas Joseph, Nicholas Schiefer, Oliver Rausch, Robin Larson, Sam McCandlish, Sandipan Kundu, Saurav Kadavath, Shannon Yang, Thomas Henighan, Timothy Maxwell, Timothy Telleen-Lawton, Tristan Hume, Zac Hatfield-Dodds, Jared Kaplan, Jan Brauner, Samuel R. Bowman, and Ethan Perez. Measuring faithfulness in chain-of-thought reasoning. CoRR, abs/2307.13702, 2023. doi: 10.48550/ARXIV.2307.13702. https://doi.org/ 10.48550/arXiv.2307.13702.
- [93] Tamera Lanham, Anna Chen, Ansh Radhakrishnan, Benoit Steiner, Carson Denison, Danny Hernandez, Dustin Li, Esin Durmus, Evan Hubinger, Jackson Kernion, Kamile Lukosiute, Karina Nguyen, Newton Cheng, Nicholas Joseph, Nicholas Schiefer, Oliver Rausch, Robin Larson, Sam McCandlish, Sandipan Kundu, Saurav Kadavath, Shannon Yang, Thomas Henighan, Timothy Maxwell, Timothy Telleen-Lawton, Tristan Hume, Zac Hatfield-Dodds, Jared Kaplan, Jan Brauner, Samuel R. Bowman, and Ethan Perez. Measuring faithfulness in chain-of-thought reasoning. CoRR, abs/2307.13702, 2023. doi: 10.48550/ARXIV.2307.13702. https://doi.org/ 10.48550/arXiv.2307.13702.
- [94] Yaniv Leviathan, Matan Kalman, and Yossi Matias. Fast inference from transformers via speculative decoding. In Andreas Krause, Emma Brunskill, Kyunghyun Cho, Barbara Engelhardt, Sivan Sabato, and Jonathan Scarlett, editors, International Conference on Machine Learning, ICML 2023, 23-29 July 2023, Honolulu, Hawaii, USA, volume 202 of Proceedings of Machine Learning Research, pages 19274–19286. PMLR, 2023. https://proceedings.mlr.press/v202/leviathan23a.html.
- [95] Bangzheng Li, Ximeng Sun, Jiang Liu, Ze Wang, Jialian Wu, Xiaodong Yu, Hao Chen, Emad Barsoum, Muhao Chen, and Zicheng Liu. Latent visual reasoning. CoRR, abs/2509.24251, 2025. doi: 10.48550/ARXIV.2509.24251. https://doi.org/10.48550/arXiv.2509.24251.
- [96] Boyi Li, Yifan Shen, Yuanzhe Liu, Yifan Xu, Jiateng Liu, Xinzhuo Li, Zhengyuan Li, Jingyuan Zhu, Yunhan Zhong, Fangzhou Lan, Jianguo Cao, James M. Rehg, Heng Ji, Ismini Lourentzou, and Xu Cao. Toward cognitive supersensing in multimodal large language model. CoRR, abs/2602.01541, 2026. doi: 10.48550/ARXIV.2602.01541. https://doi.org/10.48550/arXiv.2602.01541.
- [97] He Li, Feichen Song, Boyi Zeng, Shixiang Song, Zhiqin John Xu, Ziwei He, and Zhouhan Lin. Ponderlm-3: Adaptive token-wise pondering with differentiable masking. arXiv preprint arXiv:2603.02023, 2026.
- [98] Hengli Li, Chenxi Li, Tong Wu, Xuekai Zhu, Yuxuan Wang, Zhaoxin Yu, Eric Hanchen Jiang, Song-Chun Zhu, Zixia Jia, Ying Nian Wu, and Zilong Zheng. Seek in the dark: Reasoning via test-time instance-level policy gradient in latent space. CoRR, abs/2505.13308, 2025. doi: 10.48550/ARXIV.2505.13308. https: //doi.org/10.48550/arXiv.2505.13308.
- [99] Jindong Li, Yali Fu, Li Fan, Jiahong Liu, Yao Shu, Chengwei Qin, Menglin Yang, Irwin King, and Rex Ying. Implicit reasoning in large language models: A comprehensive survey. CoRR, abs/2509.02350, 2025. doi: 10.48550/ARXIV.2509.02350. https://doi.org/10.48550/arXiv.2509.02350.
- [100] Kelvin Li, Chuyi Shang, Leonid Karlinsky, Rogério Feris, Trevor Darrell, and Roei Herzig. Latent implicit visual reasoning. CoRR, abs/2512.21218, 2025. doi: 10.48550/ARXIV.2512.21218. https://doi.org/10.48550/arXiv. 2512.21218.
- [101] Xiaodan Li, Mengjie Wu, Yao Zhu, Yunna Lv, YueFeng Chen, Cen Chen, Jianmei Guo, and Hui Xue. Kelp: A streaming safeguard for large models via latent dynamics-guided risk detection. CoRR, abs/2510.09694, 2025. doi: 10.48550/ARXIV.2510.09694. https://doi.org/10.48550/arXiv.2510.09694.
- [102] Yongqi Li, Hao Lang, Tieyun Qian, and Yongbin Li. Controlling multimodal conversational agents with coverage-enhanced latent actions. CoRR, abs/2601.07516, 2026. doi: 10.48550/ARXIV.2601.07516. https: //doi.org/10.48550/arXiv.2601.07516.
- [103] You Li, Chi Chen, Yanghao Li, Fanhu Zeng, Kaiyu Huang, Jinan Xu, and Maosong Sun. Imagination helps visual reasoning, but not yet in latent space. arXiv preprint arXiv:2602.22766, 2026.
- [104] Zirui Li, Xuefeng Bai, Kehai Chen, Yizhi Li, Jian Yang, Chenghua Lin, and Min Zhang. Dynamics within latent chain-of-thought: An empirical study of causal structure. CoRR, abs/2602.08783, 2026. doi: 10.48550/ARXIV. 2602.08783. https://doi.org/10.48550/arXiv.2602.08783.
- [105] Zuolei Li, Xingyu Gao, Xiaofan Wang, and Jianlong Fu. Latbot: Distilling universal latent actions for visionlanguage-action models. CoRR, abs/2511.23034, 2025. doi: 10.48550/ARXIV.2511.23034. https://doi.org/10. 48550/arXiv.2511.23034.


- [106] Shijie Lian, Bin Yu, Xiaopeng Lin, Laurence T. Yang, Zhaolong Shen, Changti Wu, Yuzhuo Miao, Cong Huang, and Kai Chen. Langforce: Bayesian decomposition of vision language action models via latent action queries. CoRR, abs/2601.15197, 2026. doi: 10.48550/ARXIV.2601.15197. https://doi.org/10.48550/arXiv.2601.15197.
- [107] Jia Liang and Liangming Pan. Do latent-cot models think step-by-step? A mechanistic study on sequential reasoning tasks. CoRR, abs/2602.00449, 2026. doi: 10.48550/ARXIV.2602.00449. https://doi.org/10.48550/ arXiv.2602.00449.
- [108] Hunter Lightman, Vineet Kosaraju, Yuri Burda, Harrison Edwards, Bowen Baker, Teddy Lee, Jan Leike, John Schulman, Ilya Sutskever, and Karl Cobbe. Let’s verify step by step. In The Twelfth International Conference on Learning Representations, ICLR 2024, Vienna, Austria, May 7-11, 2024. OpenReview.net, 2024. https://openreview.net/forum?id=v8L0pN6EOi.
- [109] Pengxiao Lin, Zhengan Chen, and Zhi-Qin John Xu. Identity bridge: Enabling implicit reasoning via shared latent memory. CoRR, abs/2509.24653, 2025. doi: 10.48550/ARXIV.2509.24653. https://doi.org/10.48550/ arXiv.2509.24653.
- [110] Bingyang Kelvin Liu, Ziyu Patrick Chen, and David P. Woodruff. Jepa-reasoner: Decoupling latent reasoning from token generation. CoRR, abs/2512.19171, 2025. doi: 10.48550/ARXIV.2512.19171. https://doi.org/10. 48550/arXiv.2512.19171.
- [111] Chengzhi Liu, Yuzhe Yang, Yue Fan, Qingyue Wei, Sheng Liu, and Xin Eric Wang. Reasoning within the mind: Dynamic multimodal interleaving in latent space. CoRR, abs/2512.12623, 2025. doi: 10.48550/ARXIV.2512.12623. https://doi.org/10.48550/arXiv.2512.12623.
- [112] Enze Liu, Bowen Zheng, Xiaolei Wang, Wayne Xin Zhao, Jinpeng Wang, Sheng Chen, and Ji-Rong Wen. LARES: latent reasoning for sequential recommendation. CoRR, abs/2505.16865, 2025. doi: 10.48550/ARXIV.2505.16865. https://doi.org/10.48550/arXiv.2505.16865.
- [113] Houjun Liu, Shikhar Murty, Christopher D. Manning, and Róbert Csordás. Thoughtbubbles: an unsupervised method for parallel thinking in latent space. CoRR, abs/2510.00219, 2025. doi: 10.48550/ARXIV.2510.00219. https://doi.org/10.48550/arXiv.2510.00219.
- [114] Huaping Liu, Di Guo, and Angelo Cangelosi. Embodied intelligence: A synergy of morphology, action, perception and learning. ACM Comput. Surv., 57(7):186:1–186:36, 2025. doi: 10.1145/3717059. https://doi.org/10.1145/ 3717059.
- [115] Jiayu Liu, Zhenya Huang, Anya Sims, Enhong Chen, Yee Whye Teh, and Ning Miao. MARCOS: deep thinking by markov chain of continuous thoughts. CoRR, abs/2509.25020, 2025. doi: 10.48550/ARXIV.2509.25020. https://doi.org/10.48550/arXiv.2509.25020.
- [116] Jiayu Liu, Yinhe Long, Zhenya Huang, and Enhong Chen. Unicog: Uncovering cognitive abilities of llms through latent mind space analysis. CoRR, abs/2601.17897, 2026. doi: 10.48550/ARXIV.2601.17897. https: //doi.org/10.48550/arXiv.2601.17897.
- [117] Luyang Liu, Jonas Pfeiffer, Jiaxing Wu, Jun Xie, and Arthur Szlam. Deliberation in latent space via differentiable cache augmentation. In Aarti Singh, Maryam Fazel, Daniel Hsu, Simon Lacoste-Julien, Felix Berkenkamp, Tegan Maharaj, Kiri Wagstaff, and Jerry Zhu, editors, Forty-second International Conference on Machine Learning, ICML 2025, Vancouver, BC, Canada, July 13-19, 2025, volume 267 of Proceedings of Machine Learning Research. PMLR / OpenReview.net, 2025. https://proceedings.mlr.press/v267/liu25bc.html.
- [118] Ruixun Liu, Lingyu Kong, Derun Li, and Hang Zhao. Occvla: Vision-language-action model with implicit 3d occupancy supervision. CoRR, abs/2509.05578, 2025. doi: 10.48550/ARXIV.2509.05578. https://doi.org/10. 48550/arXiv.2509.05578.
- [119] Sheng Liu, Haotian Ye, Lei Xing, and James Zou. Reducing hallucinations in vision-language models via latent space steering, 2024. https://arxiv.org/abs/2410.15778.
- [120] Sheng Liu, Haotian Ye, and James Zou. Reducing hallucinations in large vision-language models via latent space steering. In The Thirteenth International Conference on Learning Representations, ICLR 2025, Singapore, April 24-28, 2025. OpenReview.net, 2025. https://openreview.net/forum?id=LBl7Hez0fF.
- [121] Songtao Liu, Hongwu Peng, Zhiwei Zhang, Zhengyu Chen, and Yue Guo. Multi-head low-rank attention. arXiv preprint arXiv:2603.02188, 2026.


- [122] Tianqiao Liu, Zui Chen, Zitao Liu, Mi Tian, and Weiqi Luo. Expediting and elevating large language model reasoning via hidden chain-of-thought decoding. CoRR, abs/2409.08561, 2024. doi: 10.48550/ARXIV.2409.08561. https://doi.org/10.48550/arXiv.2409.08561.
- [123] Weihao Liu, Dehai Min, and Lu Cheng. Latent thoughts tuning: Bridging context and reasoning with fused information in latent tokens. CoRR, abs/2602.10229, 2026. doi: 10.48550/ARXIV.2602.10229. https://doi.org/ 10.48550/arXiv.2602.10229.
- [124] Xiaoze Liu, Ruowang Zhang, Weichen Yu, Siheng Xiong, Liu He, Feijie Wu, Hoin Jung, Matt Fredrikson, Xiaoqian Wang, and Jing Gao. The vision wormhole: Latent-space communication in heterogeneous multi-agent systems. arXiv preprint arXiv:2602.15382, 2026.
- [125] Xukai Liu, Ye Liu, Jipeng Zhang, Yanghai Zhang, Kai Zhang, and Qi Liu. Layer-order inversion: Rethinking latent multi-hop reasoning in large language models. CoRR, abs/2601.03542, 2026. doi: 10.48550/ARXIV.2601.03542. https://doi.org/10.48550/arXiv.2601.03542.
- [126] Yuliang Liu, Yunchong Song, Yixuan Wang, Kewen Ge, Alex Lamb, Qipeng Guo, Kai Chen, Bowen Zhou, and Zhouhan Lin. Next concept prediction in discrete latent space leads to stronger language models. CoRR, abs/2602.08984, 2026. doi: 10.48550/ARXIV.2602.08984. https://doi.org/10.48550/arXiv.2602.08984.
- [127] Zehua Liu, Han Wu, Ruifeng She, Xiaojin Fu, Xiongwei Han, Tao Zhong, and Mingxuan Yuan. Molae: Mixture of latent experts for parameter-efficient language models. arXiv preprint arXiv:2503.23100, 2025.
- [128] Zhuoyang Liu, Jiaming Liu, Hao Chen, Jiale Yu, Ziyu Guo, Chengkai Hou, Chenyang Gu, Xiangju Mi, Renrui Zhang, Kun Wu, Zhengping Che, Jian Tang, Pheng-Ann Heng, and Shanghang Zhang. Last0: Latent spatio-temporal chain-of-thought for robotic vision-language-action model. CoRR, abs/2601.05248, 2026. doi: 10.48550/ARXIV.2601.05248. https://doi.org/10.48550/arXiv.2601.05248.
- [129] Rujiao Long, Yang Li, Xingyao Zhang, Weixun Wang, Tianqianjin Lin, Xi Zhao, Yuchi Xu, Wenbo Su, Junchi Yan, and Bo Zheng. Reasoning palette: Modulating reasoning via latent contextualization for controllable exploration for (v)lms. CoRR, abs/2512.17206, 2025. doi: 10.48550/ARXIV.2512.17206. https://doi.org/10. 48550/arXiv.2512.17206.
- [130] Wenquan Lu, Yuechuan Yang, Kyle Lee, Yanshu Li, and Enqi Liu. Latent chain-of-thought? decoding the depth-recurrent transformer. CoRR, abs/2507.02199, 2025. doi: 10.48550/ARXIV.2507.02199. https: //doi.org/10.48550/arXiv.2507.02199.
- [131] Hao Luo, Ye Wang, Wanpeng Zhang, Haoqi Yuan, Yicheng Feng, Haiweng Xu, Sipeng Zheng, and Zongqing Lu. Joint-aligned latent action: Towards scalable vla pretraining in the wild, 2026. https://arxiv.org/abs/2602.21736.
- [132] Yuechen Luo, Fang Li, Shaoqing Xu, Yang Ji, Zehan Zhang, Bing Wang, Yuannan Shen, Jianwei Cui, Long Chen, Guang Chen, et al. Last-vla: Thinking in latent spatio-temporal space for vision-language-action in autonomous driving. arXiv preprint arXiv:2603.01928, 2026.
- [133] Bo Lv, Yasheng Sun, Junjie Wang, and Haoxiang Shi. Onelatent: Single-token compression for visual latent reasoning. arXiv preprint arXiv:2602.13738, 2026.
- [134] Jonathan Lys, Vincent Gripon, Bastien Pasdeloup, Lukas Mauch, Fabien Cardinaux, and Ghouthi Boukli Hacene. Inner loop inference for pretrained transformers: Unlocking latent capabilities without training. arXiv preprint arXiv:2602.14759, 2026.
- [135] Jizheng Ma, Xiaofei Zhou, Geyuan Zhang, Yanlong Song, and Han Yan. Multimodal reasoning via latent refocusing. arXiv preprint arXiv:2511.02360, 2025.
- [136] Xiangkai Ma, Lekai Xing, Han Zhang, Wenzhong Li, and Sanglu Lu. Unifying perception and action: A hybridmodality pipeline with implicit visual chain-of-thought for robotic action generation. CoRR, abs/2511.19859,

2025. doi: 10.48550/ARXIV.2511.19859. https://doi.org/10.48550/arXiv.2511.19859.

- [137] Ahmed Masry, Juan A. Rodríguez, Tianyu Zhang, Suyuchen Wang, Chao Wang, Aarash Feizi, Akshay Kalkunte Suresh, Abhay Puri, Xiangru Jian, Pierre-André Noël, Sathwik Tejaswi Madhusudhan, Marco Pedersoli, Bang Liu, Nicolas Chapados, Yoshua Bengio, Enamul Hoque, Christopher Pal, Issam H. Laradji, David Vázquez, Perouz Taslakian, Spandana Gella, and Sai Rajeswar. Alignvlm: Bridging vision and language latent spaces for multimodal understanding. CoRR, abs/2502.01341, 2025. doi: 10.48550/ARXIV.2502.01341. https://doi.org/ 10.48550/arXiv.2502.01341.
- [138] Clara Meister, Tiago Pimentel, Patrick Haller, Lena A. Jäger, Ryan Cotterell, and Roger Levy. Revisiting the uniform information density hypothesis. In Marie-Francine Moens, Xuanjing Huang, Lucia Specia, and


- Scott Wen-tau Yih, editors, Proceedings of the 2021 Conference on Empirical Methods in Natural Language Processing, EMNLP 2021, Virtual Event / Punta Cana, Dominican Republic, 7-11 November, 2021, pages 963–980. Association for Computational Linguistics, 2021. doi: 10.18653/V1/2021.EMNLP-MAIN.74. https: //doi.org/10.18653/v1/2021.emnlp-main.74.
- [139] Junlin Mu, Hantao Huang, Jihang Zhang, Minghui Yu, Tao Wang, and Yidong Li. SALS: sparse attention in latent space for KV cache compression. CoRR, abs/2510.24273, 2025. doi: 10.48550/ARXIV.2510.24273. https://doi.org/10.48550/arXiv.2510.24273.
- [140] Raffaele Mura, Giorgio Piras, Kamile Lukosiute, Maura Pintor, Amin Karbasi, and Battista Biggio. Latentbreak: Jailbreaking large language models through latent space feedback. CoRR, abs/2510.08604, 2025. doi: 10.48550/ ARXIV.2510.08604. https://doi.org/10.48550/arXiv.2510.08604.
- [141] Humza Naveed, Asad Ullah Khan, Shi Qiu, Muhammad Saqib, Saeed Anwar, Muhammad Usman, Naveed Akhtar, Nick Barnes, and Ajmal Mian. A comprehensive overview of large language models. ACM Trans. Intell. Syst. Technol., 16(5):106:1–106:72, 2025. doi: 10.1145/3744746. https://doi.org/10.1145/3744746.
- [142] Chaojun Ni, Cheng Chen, Xiaofeng Wang, Zheng Zhu, Wenzhao Zheng, Boyuan Wang, Tianrun Chen, Guosheng Zhao, Haoyun Li, Zhehao Dong, Qiang Zhang, Yun Ye, Yang Wang, Guan Huang, and Wenjun Mei. Swiftvla: Unlocking spatiotemporal dynamics for lightweight VLA models at minimal overhead. CoRR, abs/2512.00903,

2025. doi: 10.48550/ARXIV.2512.00903. https://doi.org/10.48550/arXiv.2512.00903.

- [143] Giorgos Nikolaou, Tommaso Mencattini, Donato Crisostomi, Andrea Santilli, Yannis Panagakis, and Emanuele Rodolà. Language models are injective and hence invertible. CoRR, abs/2510.15511, 2025. doi: 10.48550/ ARXIV.2510.15511. https://doi.org/10.48550/arXiv.2510.15511.
- [144] Alexander Nikulin, Ilya Zisman, Albina Klepach, Denis Tarasov, Alexander Derevyagin, Andrei Polubarov, Nikita Lyubaykin, and Vladislav Kurenkov. Vision-language models unlock task-centric latent actions. CoRR, abs/2601.22714, 2026. doi: 10.48550/ARXIV.2601.22714. https://doi.org/10.48550/arXiv.2601.22714.
- [145] Alex Ning and Vainateya Rangaraju. Visualizing LLM latent space geometry through dimensionality reduction. CoRR, abs/2511.21594, 2025. doi: 10.48550/ARXIV.2511.21594. https://doi.org/10.48550/arXiv.2511.21594.
- [146] Alex Ning, Yen-Ling Kuo, and Gabe Gomes. Learning when to stop: Adaptive latent reasoning via reinforcement learning. CoRR, abs/2511.21581, 2025. doi: 10.48550/ARXIV.2511.21581. https://doi.org/10.48550/arXiv. 2511.21581.
- [147] Kyle O’Brien, David Majercak, Xavier Fernandes, Richard Edgar, Jingya Chen, Harsha Nori, Dean Carignan, Eric Horvitz, and Forough Poursabzi-Sangdeh. Steering language model refusal with sparse autoencoders. CoRR, abs/2411.11296, 2024. doi: 10.48550/ARXIV.2411.11296. https://doi.org/10.48550/arXiv.2411.11296.
- [148] José Ignacio Orlicki. Beyond words: A latent memory approach to internal reasoning in llms. CoRR, abs/2502.21030, 2025. doi: 10.48550/ARXIV.2502.21030. https://doi.org/10.48550/arXiv.2502.21030.
- [149] Enes Özeren and Matthias Aßenmacher. Reinforcement learning for latent-space thinking in llms. CoRR, abs/2512.11816, 2025. doi: 10.48550/ARXIV.2512.11816. https://doi.org/10.48550/arXiv.2512.11816.
- [150] William Peebles and Saining Xie. Scalable diffusion models with transformers. In IEEE/CVF International Conference on Computer Vision, ICCV 2023, Paris, France, October 1-6, 2023, pages 4172–4182. IEEE, 2023. doi: 10.1109/ICCV51070.2023.00387. https://doi.org/10.1109/ICCV51070.2023.00387.
- [151] Guangyue Peng, Zongchao Chen, Wen Luo, Yuntao Wen, Wei Li, Ruixiang Feng, Ran Le, Chen Yang, Zhenwei An, Yang Song, Tao Zhang, and Houfeng Wang. Measuring and mitigating post-hoc rationalization in reverse chain-of-thought generation. CoRR, abs/2602.14469, 2026. doi: 10.48550/ARXIV.2602.14469. https://doi.org/ 10.48550/arXiv.2602.14469.
- [152] Qihang Peng, Xuesong Chen, Chenye Yang, Shaoshuai Shi, and Hongsheng Li. Colavla: Leveraging cognitive latent reasoning for hierarchical parallel trajectory planning in autonomous driving. CoRR, abs/2512.22939,

2025. doi: 10.48550/ARXIV.2512.22939. https://doi.org/10.48550/arXiv.2512.22939.

- [153] Jacob Pfau, William Merrill, and Samuel R. Bowman. Let’s think dot by dot: Hidden computation in transformer language models. CoRR, abs/2404.15758, 2024. doi: 10.48550/ARXIV.2404.15758. https://doi.org/10.48550/ arXiv.2404.15758.
- [154] Tan-Hanh Pham and Chris Ngo. Multimodal chain of continuous thought for latent-space reasoning in visionlanguage models. CoRR, abs/2508.12587, 2025. doi: 10.48550/ARXIV.2508.12587. https://doi.org/10.48550/ arXiv.2508.12587.


- [155] Shengmin Piao and Sanghyun Park. Spiralthinker: Latent reasoning through an iterative process with text-latent interleaving. CoRR, abs/2511.08983, 2025. doi: 10.48550/ARXIV.2511.08983. https://doi.org/10.48550/arXiv. 2511.08983.
- [156] Yiming Qin, Bomin Wei, Jiaxin Ge, Konstantinos Kallidromitis, Stephanie Fu, Trevor Darrell, and Xudong Wang. Chain-of-visual-thought: Teaching vlms to see and think better with continuous visual tokens. CoRR, abs/2511.19418, 2025. doi: 10.48550/ARXIV.2511.19418. https://doi.org/10.48550/arXiv.2511.19418.
- [157] Yilun Qiu, Tianhao Shi, Xiaoyan Zhao, Fengbin Zhu, Yang Zhang, and Fuli Feng. Latent inter-user difference modeling for LLM personalization. In Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing, EMNLP 2025, Suzhou, China, November 4-9, 2025, pages 10599–10617. Association for Computational Linguistics, 2025. doi: 10.18653/V1/2025.EMNLP-MAIN.536. https://doi.org/10.18653/v1/ 2025.emnlp-main.536.
- [158] Xingwei Qu, Shaowen Wang, Zihao Huang, Kai Hua, Fan Yin, Rui-Jie Zhu, Jundong Zhou, Qiyang Min, Zihao Wang, Yizhi Li, Tianyu Zhang, He Xing, Zheng Zhang, Yuxuan Song, Tianyu Zheng, Zhiyuan Zeng, Chenghua Lin, Ge Zhang, and Wenhao Huang. Dynamic large concept models: Latent reasoning in an adaptive semantic space. CoRR, abs/2512.24617, 2025. doi: 10.48550/ARXIV.2512.24617. https://doi.org/10.48550/arXiv.2512.24617.
- [159] Alec Radford, Jong Wook Kim, Chris Hallacy, Aditya Ramesh, Gabriel Goh, Sandhini Agarwal, Girish Sastry, Amanda Askell, Pamela Mishkin, Jack Clark, Gretchen Krueger, and Ilya Sutskever. Learning transferable visual models from natural language supervision. In Marina Meila and Tong Zhang, editors, Proceedings of the 38th International Conference on Machine Learning, ICML 2021, 18-24 July 2021, Virtual Event, volume 139 of Proceedings of Machine Learning Research, pages 8748–8763. PMLR, 2021. http://proceedings.mlr.press/v139/ radford21a.html.
- [160] Arijit Ray, Ahmed Abdelkader, Chengzhi Mao, Bryan A. Plummer, Kate Saenko, Ranjay Krishna, Leonidas J. Guibas, and Wen-Sheng Chu. Mull-tokens: Modality-agnostic latent thinking. CoRR, abs/2512.10941, 2025. doi: 10.48550/ARXIV.2512.10941. https://doi.org/10.48550/arXiv.2512.10941.
- [161] Benjamin Z. Reichman, Adar Avsian, and Larry Heck. Emotions where art thou: Understanding and characterizing the emotional latent space of large language models. CoRR, abs/2510.22042, 2025. doi: 10.48550/ARXIV.2510.

22042. https://doi.org/10.48550/arXiv.2510.22042.

- [162] Robin Rombach, Andreas Blattmann, Dominik Lorenz, Patrick Esser, and Björn Ommer. High-resolution image synthesis with latent diffusion models. In IEEE/CVF Conference on Computer Vision and Pattern Recognition, CVPR 2022, New Orleans, LA, USA, June 18-24, 2022, pages 10674–10685. IEEE, 2022. doi: 10.1109/CVPR52688.2022.01042. https://doi.org/10.1109/CVPR52688.2022.01042.
- [163] Weilin Ruan and Yuxuan Liang. Visual reasoning over time series via multi-agent system. CoRR, abs/2602.03026,

2026. doi: 10.48550/ARXIV.2602.03026. https://doi.org/10.48550/arXiv.2602.03026.

- [164] Yangjun Ruan, Neil Band, Chris J. Maddison, and Tatsunori Hashimoto. Reasoning to learn from latent thoughts. CoRR, abs/2503.18866, 2025. doi: 10.48550/ARXIV.2503.18866. https://doi.org/10.48550/arXiv.2503.18866.
- [165] Sabrina Sadiekh, Elena Ericheva, and Chirag Agarwal. Polarity-aware probing for quantifying latent alignment in language models. In Fortieth AAAI Conference on Artificial Intelligence, Thirty-Eighth Conference on Innovative Applications of Artificial Intelligence, Sixteenth Symposium on Educational Advances in Artificial Intelligence, AAAI 2026, Singapore, January 20-27, 2026, pages 37896–37903. AAAI Press, 2026. doi: 10.1609/AAAI.V40I44.

41126. https://doi.org/10.1609/aaai.v40i44.41126.

- [166] Subramanyam Sahoo, Aman Chadha, Vinija Jain, and Divya Chaudhary. When shallow wins: Silent failures and the depth-accuracy paradox in latent reasoning. arXiv preprint arXiv:2603.03475, 2026.
- [167] Nikunj Saunshi, Nishanth Dikkala, Zhiyuan Li, Sanjiv Kumar, and Sashank J. Reddi. Reasoning with latent thoughts: On the power of looped transformers. In The Thirteenth International Conference on Learning Representations, ICLR 2025, Singapore, April 24-28, 2025. OpenReview.net, 2025. https://openreview.net/ forum?id=din0lGfZFd.
- [168] Rico Sennrich, Barry Haddow, and Alexandra Birch. Neural machine translation of rare words with subword units. In Proceedings of the 54th Annual Meeting of the Association for Computational Linguistics, ACL 2016, August 7-12, 2016, Berlin, Germany, Volume 1: Long Papers. The Association for Computer Linguistics, 2016. doi: 10.18653/V1/P16-1162. https://doi.org/10.18653/v1/p16-1162.


- [169] Gabriele Serussi, David Vainshtein, Jonathan Kouchly, Dotan Di Castro, and Chaim Baskin. PREGEN: uncovering latent thoughts in composed video retrieval. CoRR, abs/2601.13797, 2026. doi: 10.48550/ARXIV.2601.13797. https://doi.org/10.48550/arXiv.2601.13797.
- [170] Lianlei Shan, Han Chen, Yixuan Wang, Zhenjie Liu, and Wei Li. Latent-space contrastive reinforcement learning for stable and efficient LLM reasoning. CoRR, abs/2601.17275, 2026. doi: 10.48550/ARXIV.2601.17275. https://doi.org/10.48550/arXiv.2601.17275.
- [171] Yifei Shao, Kun Zhou, Ziming Xu, Mohammad Atif Quamar, Shibo Hao, Zhen Wang, Zhiting Hu, and Biwei Huang. Learning modal-mixed chain-of-thought reasoning with latent embeddings. CoRR, abs/2602.00574, 2026. doi: 10.48550/ARXIV.2602.00574. https://doi.org/10.48550/arXiv.2602.00574.
- [172] Arushi Sharma, Vedant Pungliya, Christopher J. Quinn, and Ali Jannesari. Analyzing latent concepts in code language models. CoRR, abs/2510.00476, 2025. doi: 10.48550/ARXIV.2510.00476. https://doi.org/10.48550/ arXiv.2510.00476.
- [173] Xuan Shen, Yizhou Wang, Xiangxi Shi, Yanzhi Wang, Pu Zhao, and Jiuxiang Gu. Efficient reasoning with hidden thinking. CoRR, abs/2501.19201, 2025. doi: 10.48550/ARXIV.2501.19201. https://doi.org/10.48550/ arXiv.2501.19201.
- [174] Zhenyi Shen, Hanqi Yan, Linhai Zhang, Zhanghao Hu, Yali Du, and Yulan He. CODI: compressing chain-ofthought into continuous space via self-distillation. In Christos Christodoulopoulos, Tanmoy Chakraborty, Carolyn Rose, and Violet Peng, editors, Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing, EMNLP 2025, Suzhou, China, November 4-9, 2025, pages 677–693. Association for Computational Linguistics, 2025. doi: 10.18653/V1/2025.EMNLP-MAIN.36. https://doi.org/10.18653/v1/2025.emnlp-main. 36.
- [175] Dachuan Shi, Abedelkadir Asi, Keying Li, Xiangchi Yuan, Leyan Pan, Wenke Lee, and Wen Xiao. Swireasoning: Switch-thinking in latent and explicit for pareto-superior reasoning llms. CoRR, abs/2510.05069, 2025. doi: 10.48550/ARXIV.2510.05069. https://doi.org/10.48550/arXiv.2510.05069.
- [176] Jiaqi Shi, Xulong Zhang, Xiaoyang Qu, and Jianzong Wang. CARE: multi-task pretraining for latent continuous action representation in robot control. CoRR, abs/2601.22467, 2026. doi: 10.48550/ARXIV.2601.22467. https://doi.org/10.48550/arXiv.2601.22467.
- [177] Teng Shi, Weicong Qin, Weijie Yu, Xiao Zhang, Ming He, Jianping Fan, and Jun Xu. Bridging search and recommendation through latent cross reasoning. CoRR, abs/2508.04152, 2025. doi: 10.48550/ARXIV.2508.04152. https://doi.org/10.48550/arXiv.2508.04152.
- [178] Zhenning Shi, Yijia Zhu, Junhan Shi, Xun Zhang, Lei Wang, and Congcong Miao. Internalizing LLM reasoning via discovery and replay of latent actions. CoRR, abs/2602.04925, 2026. doi: 10.48550/ARXIV.2602.04925. https://doi.org/10.48550/arXiv.2602.04925.
- [179] Huizhen Shu, Xuying Li, and Zhuo Li. Latentguard: Controllable latent steering for robust refusal of attacks and reliable response generation. CoRR, abs/2509.19839, 2025. doi: 10.48550/ARXIV.2509.19839. https: //doi.org/10.48550/arXiv.2509.19839.
- [180] Shixiang Song, He Li, Zitong Wang, Boyi Zeng, Feichen Song, Yixuan Wang, Zhiqin John Xu, Ziwei He, and Zhouhan Lin. Adaponderlm: Gated pondering language models with token-wise adaptive depth. arXiv preprint arXiv:2603.01914, 2026.
- [181] DiJia Su, Hanlin Zhu, Yingchen Xu, Jiantao Jiao, Yuandong Tian, and Qinqing Zheng. Token assorted: Mixing latent and text tokens for improved language model reasoning. In Aarti Singh, Maryam Fazel, Daniel Hsu, Simon Lacoste-Julien, Felix Berkenkamp, Tegan Maharaj, Kiri Wagstaff, and Jerry Zhu, editors, Fortysecond International Conference on Machine Learning, ICML 2025, Vancouver, BC, Canada, July 13-19, 2025, volume 267 of Proceedings of Machine Learning Research. PMLR / OpenReview.net, 2025. https: //proceedings.mlr.press/v267/su25g.html.
- [182] Nitesh Subedi, Adam Haroon, Samuel T. K. Tetteh, Prajwal Koirala, Cody H. Fleming, and Soumik Sarkar. LCLA: language-conditioned latent alignment for vision-language navigation. CoRR, abs/2602.07629, 2026. doi: 10.48550/ARXIV.2602.07629. https://doi.org/10.48550/arXiv.2602.07629.
- [183] Guohao Sun, Hang Hua, Jian Wang, Jiebo Luo, Sohail A. Dianat, Majid Rabbani, Raghuveer Rao, and Zhiqiang Tao. Latent chain-of-thought for visual reasoning. CoRR, abs/2510.23925, 2025. doi: 10.48550/ARXIV.2510.23925. https://doi.org/10.48550/arXiv.2510.23925.


- [184] Jingwen Sun, Wenyao Zhang, Zekun Qi, Shaojie Ren, Zezhi Liu, Hanxin Zhu, Guangzhong Sun, Xin Jin, and Zhibo Chen. Vla-jepa: Enhancing vision-language-action model with latent world model, 2026. https: //arxiv.org/abs/2602.10098.
- [185] Yuchang Sun, Yanxi Chen, Yaliang Li, and Bolin Ding. Enhancing latent computation in transformers with latent tokens. CoRR, abs/2505.12629, 2025. doi: 10.48550/ARXIV.2505.12629. https://doi.org/10.48550/arXiv. 2505.12629.
- [186] Jihoon Tack, Jack Lanchantin, Jane Yu, Andrew Cohen, Ilia Kulikov, Janice Lan, Shibo Hao, Yuandong Tian, Jason Weston, and Xian Li. LLM pretraining with continuous concepts. CoRR, abs/2502.08524, 2025. doi: 10.48550/ARXIV.2502.08524. https://doi.org/10.48550/arXiv.2502.08524.
- [187] Shuhan Tan, Kashyap Chitta, Yuxiao Chen, Ran Tian, Yurong You, Yan Wang, Wenjie Luo, Yulong Cao, Philipp Krähenbühl, Marco Pavone, and Boris Ivanovic. Latent chain-of-thought world modeling for end-to-end driving. CoRR, abs/2512.10226, 2025. doi: 10.48550/ARXIV.2512.10226. https://doi.org/10.48550/arXiv.2512.10226.
- [188] Wenhui Tan, Jiaze Li, Jianzhong Ju, Zhenbo Luo, Jian Luan, and Ruihua Song. Think silently, think fast: Dynamic latent compression of LLM reasoning chains. CoRR, abs/2505.16552, 2025. doi: 10.48550/ARXIV.2505.16552. https://doi.org/10.48550/arXiv.2505.16552.
- [189] Wenhui Tan, Fiorenzo Parascandolo, Enver Sangineto, Jianzhong Ju, Zhenbo Luo, Qian Cao, Rita Cucchiara, Ruihua Song, and Jian Luan. Restoring exploration after post-training: Latent exploration decoding for large reasoning models. CoRR, abs/2602.01698, 2026. doi: 10.48550/ARXIV.2602.01698. https://doi.org/10.48550/ arXiv.2602.01698.
- [190] Guo Tang, Shixin Jiang, Heng Chang, Nuo Chen, Yuhan Li, Huiming Fan, Jia Li, Ming Liu, and Bing Qin. Looprpt: Reinforcement pre-training for looped language models. arXiv preprint arXiv:2603.19714, 2026.
- [191] Haoran Tang and Rajiv Khanna. From logits to latents: Contrastive representation shaping for LLM unlearning. CoRR, abs/2601.22028, 2026. doi: 10.48550/ARXIV.2601.22028. https://doi.org/10.48550/arXiv.2601.22028.
- [192] Jiakai Tang, Sunhao Dai, Teng Shi, Jun Xu, Xu Chen, Wen Chen, Wu Jian, and Yuning Jiang. Think before recommend: Unleashing the latent reasoning power for sequential recommendation. CoRR, abs/2503.22675,

2025. doi: 10.48550/ARXIV.2503.22675. https://doi.org/10.48550/arXiv.2503.22675.

- [193] Jiakai Tang, Xu Chen, Wen Chen, Jian Wu, Yuning Jiang, and Bo Zheng. Parallel latent reasoning for sequential recommendation. CoRR, abs/2601.03153, 2026. doi: 10.48550/ARXIV.2601.03153. https://doi.org/10.48550/ arXiv.2601.03153.
- [194] Wenlong Tang. Learning evolving latent strategies for multi-agent language systems without model fine-tuning. CoRR, abs/2512.20629, 2025. doi: 10.48550/ARXIV.2512.20629. https://doi.org/10.48550/arXiv.2512.20629.
- [195] Hinata Tezuka and Naoya Inoue. The transfer neurons hypothesis: An underlying mechanism for language latent space transitions in multilingual llms. In Christos Christodoulopoulos, Tanmoy Chakraborty, Carolyn Rose, and Violet Peng, editors, Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing, EMNLP 2025, Suzhou, China, November 4-9, 2025, pages 31742–31792. Association for Computational Linguistics,

2025. doi: 10.18653/V1/2025.EMNLP-MAIN.1618. https://doi.org/10.18653/v1/2025.emnlp-main.1618.

- [196] Bahey Tharwat, Yara Nasser, Ali Abouzeid, and Ian Reid. Latent action pretraining through world modeling. CoRR, abs/2509.18428, 2025. doi: 10.48550/ARXIV.2509.18428. https://doi.org/10.48550/arXiv.2509.18428.
- [197] Jintao Tong, Jiaqi Gu, Yujing Lou, Lubin Fan, Yixiong Zou, Yue Wu, Jieping Ye, and Ruixuan Li. Sketch-inlatents: Eliciting unified reasoning in mllms. CoRR, abs/2512.16584, 2025. doi: 10.48550/ARXIV.2512.16584. https://doi.org/10.48550/arXiv.2512.16584.
- [198] Yalcin Tur, Jalal Naghiyev, Haoquan Fang, Wei-Chuan Tsai, Jiafei Duan, Dieter Fox, and Ranjay Krishna. Recurrent-depth VLA: implicit test-time compute scaling of vision-language-action models via latent iterative reasoning. CoRR, abs/2602.07845, 2026. doi: 10.48550/ARXIV.2602.07845. https://doi.org/10.48550/arXiv. 2602.07845.
- [199] Miles Turpin, Julian Michael, Ethan Perez, and Samuel R. Bowman. Language models don’t always say what they think: Unfaithful explanations in chain-of-thought prompting. In Alice Oh, Tristan Naumann, Amir Globerson, Kate Saenko, Moritz Hardt, and Sergey Levine, editors, Advances in Neural Information Processing Systems 36: Annual Conference on Neural Information Processing Systems 2023, NeurIPS 2023, New Orleans, LA, USA, December 10 - 16, 2023, 2023. http://papers.nips.cc/paper_files/paper/2023/hash/ ed3fea9033a80fea1376299fa7863f4a-Abstract-Conference.html.


- [200] Arash Vahdat, Karsten Kreis, and Jan Kautz. Score-based generative modeling in latent space. In Marc’Aurelio Ranzato, Alina Beygelzimer, Yann N. Dauphin, Percy Liang, and Jennifer Wortman Vaughan, editors, Advances in Neural Information Processing Systems 34: Annual Conference on Neural Information Processing Systems 2021, NeurIPS 2021, December 6-14, 2021, virtual, pages 11287–11302, 2021. https://proceedings.neurips.cc/ paper/2021/hash/5dca4c6b9e244d24a30b4c45601d9720-Abstract.html.
- [201] Aäron van den Oord, Oriol Vinyals, and Koray Kavukcuoglu. Neural discrete representation learning. In Isabelle Guyon, Ulrike von Luxburg, Samy Bengio, Hanna M. Wallach, Rob Fergus, S. V. N. Vishwanathan, and Roman Garnett, editors, Advances in Neural Information Processing Systems 30: Annual Conference on Neural Information Processing Systems 2017, December 4-9, 2017, Long Beach, CA, USA, pages 6306–6315,

2017. https://proceedings.neurips.cc/paper/2017/hash/7a98af17e63a0ac09ce2e96d03992fbc-Abstract.html.

- [202] Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones, Aidan N. Gomez, Lukasz Kaiser, and Illia Polosukhin. Attention is all you need. In Isabelle Guyon, Ulrike von Luxburg, Samy Bengio, Hanna M. Wallach, Rob Fergus, S. V. N. Vishwanathan, and Roman Garnett, editors, Advances in Neural Information Processing Systems 30: Annual Conference on Neural Information Processing Systems 2017, December 49, 2017, Long Beach, CA, USA, pages 5998–6008, 2017. https://proceedings.neurips.cc/paper/2017/hash/ 3f5ee243547dee91fbd053c1c4a845aa-Abstract.html.
- [203] Martina G. Vilas, Safoora Yousefi, Besmira Nushi, Eric Horvitz, and Vidhisha Balachandran. Tracing the traces: Latent temporal signals for efficient and accurate reasoning. CoRR, abs/2510.10494, 2025. doi: 10.48550/ARXIV.2510.10494. https://doi.org/10.48550/arXiv.2510.10494.
- [204] Chengbing Wang, Yang Zhang, Zhicheng Wang, Tianhao Shi, Keqin Bao, Fuli Feng, and Tat-Seng Chua. Decoding in latent spaces for efficient inference in llm-based recommendation. In Christos Christodoulopoulos, Tanmoy Chakraborty, Carolyn Rose, and Violet Peng, editors, Findings of the Association for Computational Linguistics: EMNLP 2025, Suzhou, China, November 4-9, 2025, pages 7591–7603. Association for Computational Linguistics, 2025. https://aclanthology.org/2025.findings-emnlp.401/.
- [205] Fanmeng Wang, Haotian Liu, Guojiang Zhao, Hongteng Xu, and Zhifeng Gao. Regular: Variational latent reasoning guided by rendered chain-of-thought. CoRR, abs/2601.23184, 2026. doi: 10.48550/ARXIV.2601.23184. https://doi.org/10.48550/arXiv.2601.23184.
- [206] Jiaqi Wang, Binquan Ji, Haibo Luo, Yiyang Qi, Ruiting Li, Huiyan Wang, Yuantao Han, Cangyi Yang, jiaxu Zhang, and Feiliang Ren. Lta-thinker: Latent thought-augmented training framework for large language models on complex reasoning. CoRR, abs/2509.12875, 2025. doi: 10.48550/ARXIV.2509.12875. https://doi.org/10. 48550/arXiv.2509.12875.
- [207] Jiecong Wang, Hao Peng, and Chunyang Liu. Latent chain-of-thought as planning: Decoupling reasoning from verbalization. CoRR, abs/2601.21358, 2026. doi: 10.48550/ARXIV.2601.21358. https://doi.org/10.48550/arXiv. 2601.21358.
- [208] Kang Wang, Xiangyu Duan, and Tianyi Du. Improving latent reasoning in llms via soft concept mixing. CoRR, abs/2511.16885, 2025. doi: 10.48550/ARXIV.2511.16885. https://doi.org/10.48550/arXiv.2511.16885.
- [209] Minghan Wang, Ye Bai, Thuy-Trang Vu, Ehsan Shareghi, and Gholamreza Haffari. Gts: Inference-time scaling of latent reasoning with a learnable gaussian thought sampler. arXiv preprint arXiv:2602.14077, 2026.
- [210] Peihao Wang, Ruisi Cai, Zhen Wang, Hongyuan Mei, Qiang Liu, Pan Li, and Zhangyang Wang. nabla-reasoner: Llm reasoning via test-time gradient descent in latent space. arXiv preprint arXiv:2603.04948, 2026.
- [211] Qixun Wang, Yang Shi, Yifei Wang, Yuanxing Zhang, Pengfei Wan, Kun Gai, Xianghua Ying, and Yisen Wang. Monet: Reasoning in latent visual space beyond images and language. CoRR, abs/2511.21395, 2025. doi: 10.48550/ARXIV.2511.21395. https://doi.org/10.48550/arXiv.2511.21395.
- [212] Weixing Wang, Zifeng Ding, Jindong Gu, Rui Cao, Christoph Meinel, Gerard de Melo, and Haojin Yang. Image tokens matter: Mitigating hallucination in discrete tokenizer-based large vision-language models via latent editing. CoRR, abs/2505.21547, 2025. doi: 10.48550/ARXIV.2505.21547. https://doi.org/10.48550/arXiv.2505.21547.
- [213] Xiaofan Wang, Xingyu Gao, Jianlong Fu, Zuolei Li, Dean Fortier, Galen Mullins, Andrey Kolobov, and Baining Guo. Lola: Long horizon latent action learning for general robot manipulation. CoRR, abs/2512.20166, 2025. doi: 10.48550/ARXIV.2512.20166. https://doi.org/10.48550/arXiv.2512.20166.
- [214] Xiaoqiang Wang, Suyuchen Wang, Yun Zhu, and Bang Liu. System-1.5 reasoning: Traversal in language and latent spaces with dynamic shortcuts. CoRR, abs/2505.18962, 2025. doi: 10.48550/ARXIV.2505.18962. https://doi.org/10.48550/arXiv.2505.18962.


- [215] Xinyuan Wang, Dongjie Wang, Wangyang Ying, Haoyue Bai, Nanxu Gong, Sixun Dong, Kunpeng Liu, and Yanjie Fu. Efficient post-training refinement of latent reasoning in large language models. In Fortieth AAAI Conference on Artificial Intelligence, Thirty-Eighth Conference on Innovative Applications of Artificial Intelligence, Sixteenth Symposium on Educational Advances in Artificial Intelligence, AAAI 2026, Singapore, January 20-27, 2026, pages 33692–33700. AAAI Press, 2026. doi: 10.1609/AAAI.V40I40.40659. https://doi.org/10.1609/aaai.v40i40.40659.
- [216] Yifan Wang, Shiyu Li, Peiming Li, Xiaochen Yang, Yang Tang, and Zheng Wei. Render-of-thought: Rendering textual chain-of-thought as images for visual latent reasoning. CoRR, abs/2601.14750, 2026. doi: 10.48550/ ARXIV.2601.14750. https://doi.org/10.48550/arXiv.2601.14750.
- [217] Yiming Wang, Pei Zhang, Baosong Yang, Derek F. Wong, and Rui Wang. Latent space chain-of-embedding enables output-free LLM self-evaluation. In The Thirteenth International Conference on Learning Representations, ICLR 2025, Singapore, April 24-28, 2025. OpenReview.net, 2025. https://openreview.net/forum?id=jxo70B9fQo.
- [218] Yubo Wang, Juntian Zhang, Yichen Wu, Yankai Lin, Nils Lukas, and Yuhan Liu. Forest before trees: Latent superposition for efficient visual reasoning. CoRR, abs/2601.06803, 2026. doi: 10.48550/ARXIV.2601.06803. https://doi.org/10.48550/arXiv.2601.06803.
- [219] Jason Wei, Xuezhi Wang, Dale Schuurmans, Maarten Bosma, Brian Ichter, Fei Xia, Ed H. Chi, Quoc V. Le, and Denny Zhou. Chain-of-thought prompting elicits reasoning in large language models. In Sanmi Koyejo, S. Mohamed, A. Agarwal, Danielle Belgrave, K. Cho, and A. Oh, editors, Advances in Neural Information Processing Systems 35: Annual Conference on Neural Information Processing Systems 2022, NeurIPS 2022, New Orleans, LA, USA, November 28 - December 9, 2022, 2022. http://papers.nips.cc/paper_files/paper/2022/ hash/9d5609613524ecf4f15af0f7b31abca4-Abstract-Conference.html.
- [220] Xilin Wei, Xiaoran Liu, Yuhang Zang, Xiaoyi Dong, Yuhang Cao, Jiaqi Wang, Xipeng Qiu, and Dahua Lin. Sim-cot: Supervised implicit chain-of-thought. CoRR, abs/2509.20317, 2025. doi: 10.48550/ARXIV.2509.20317. https://doi.org/10.48550/arXiv.2509.20317.
- [221] Xiuying Wei, Yunchen Zhang, Xiangguo Zhang, Ruihao Gong, Shanghang Zhang, Qi Zhang, Fengwei Yu, and Xianglong Liu. Outlier suppression: Pushing the limit of low-bit transformer language models. In Sanmi Koyejo, S. Mohamed, A. Agarwal, Danielle Belgrave, K. Cho, and A. Oh, editors, Advances in Neural Information Processing Systems 35: Annual Conference on Neural Information Processing Systems 2022, NeurIPS 2022, New Orleans, LA, USA, November 28 - December 9, 2022, 2022. http://papers.nips.cc/paper_files/paper/2022/ hash/6f6db140de9c9f111b12ef8a216320a9-Abstract-Conference.html.
- [222] Jonathan Williams and Esin Tureci. Prioritize the process, not just the outcome: Rewarding latent thought trajectories improves reasoning in looped language models. CoRR, abs/2602.10520, 2026. doi: 10.48550/ARXIV. 2602.10520. https://doi.org/10.48550/arXiv.2602.10520.
- [223] Bohong Wu, Shen Yan, Sijun Zhang, Jianqiao Lu, Yutao Zeng, Ya Wang, and Xun Zhou. Efficient pretraining length scaling. CoRR, abs/2504.14992, 2025. doi: 10.48550/ARXIV.2504.14992. https://doi.org/10.48550/ arXiv.2504.14992.
- [224] Haoyi Wu, Zhihao Teng, and Kewei Tu. Parallel continuous chain-of-thought with jacobi iteration. In Christos Christodoulopoulos, Tanmoy Chakraborty, Carolyn Rose, and Violet Peng, editors, Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing, EMNLP 2025, Suzhou, China, November 4-9, 2025, pages 914–926. Association for Computational Linguistics, 2025. doi: 10.18653/V1/2025.EMNLP-MAIN.47. https://doi.org/10.18653/v1/2025.emnlp-main.47.
- [225] Jialin Wu, Wei Shi, Han Shen, Peigui Qi, Kunsheng Tang, Zhicong Huang, Binghao Wang, and Zhou Yang. Revis: Sparse latent steering to mitigate object hallucination in large vision-language models. CoRR, abs/2602.11824,

2026. doi: 10.48550/ARXIV.2602.11824. https://doi.org/10.48550/arXiv.2602.11824.

- [226] Junda Wu, Yuxin Xiong, Xintong Li, Zhengmian Hu, Tong Yu, Rui Wang, Xiang Chen, Jingbo Shang, and Julian J. McAuley. CTRLS: chain-of-thought reasoning via latent state-transition. CoRR, abs/2507.08182, 2025. doi: 10.48550/ARXIV.2507.08182. https://doi.org/10.48550/arXiv.2507.08182.
- [227] Linquan Wu, Tianxiang Jiang, Yifei Dong, Haoyu Yang, Fengji Zhang, Shichaang Meng, Ai Xuan, Linqi Song, and Jacky Keung. Lavit: Aligning latent visual thoughts for multi-modal reasoning. CoRR, abs/2601.10129,

2026. doi: 10.48550/ARXIV.2601.10129. https://doi.org/10.48550/arXiv.2601.10129.

- [228] Mingrui Wu, Hao Chen, Jiayi Ji, Xiaoshuai Sun, Zhiyuan Liu, Liujuan Cao, Ming-Ming Cheng, and Rongrong Ji. Test-time computing for referring multimodal large language models. arXiv preprint arXiv:2602.19505, 2026.


- [229] Wenyi Wu, Zixuan Song, Kun Zhou, Yifei Shao, Zhiting Hu, and Biwei Huang. Towards general continuous memory for vision-language models. CoRR, abs/2505.17670, 2025. doi: 10.48550/ARXIV.2505.17670. https: //doi.org/10.48550/arXiv.2505.17670.
- [230] Wenyi Wu, Kun Zhou, Ruoxin Yuan, Vivian Yu, Stephen Wang, Zhiting Hu, and Biwei Huang. Autoscaling continuous memory for GUI agent. CoRR, abs/2510.09038, 2025. doi: 10.48550/ARXIV.2510.09038. https://doi.org/10.48550/arXiv.2510.09038.
- [231] Xingyu Wu, Sheng-Hao Wu, Jibin Wu, Liang Feng, and Kay Chen Tan. Evolutionary computation in the era of large language model: Survey and roadmap. IEEE Trans. Evol. Comput., 29(2):534–554, 2025. doi: 10.1109/TEVC.2024.3506731. https://doi.org/10.1109/TEVC.2024.3506731.
- [232] Zhiheng Xi, Wenxiang Chen, Xin Guo, Wei He, Yiwen Ding, Boyang Hong, Ming Zhang, Junzhe Wang, Senjie Jin, Enyu Zhou, Rui Zheng, Xiaoran Fan, Xiao Wang, Limao Xiong, Yuhao Zhou, Weiran Wang, Changhao Jiang, Yicheng Zou, Xiangyang Liu, Zhangyue Yin, Shihan Dou, Rongxiang Weng, Wenjuan Qin, Yongyan Zheng, Xipeng Qiu, Xuanjing Huang, Qi Zhang, and Tao Gui. The rise and potential of large language model based agents: a survey. Sci. China Inf. Sci., 68(2), 2025. doi: 10.1007/S11432-024-4222-0. https://doi.org/10.1007/s11432-024-4222-0.
- [233] Heming Xia, Zhe Yang, Qingxiu Dong, Peiyi Wang, Yongqi Li, Tao Ge, Tianyu Liu, Wenjie Li, and Zhifang Sui. Unlocking efficiency in large language model inference: A comprehensive survey of speculative decoding. In LunWei Ku, Andre Martins, and Vivek Srikumar, editors, Findings of the Association for Computational Linguistics, ACL 2024, Bangkok, Thailand and virtual meeting, August 11-16, 2024, volume ACL 2024 of Findings of ACL, pages 7655–7671. Association for Computational Linguistics, 2024. doi: 10.18653/V1/2024.FINDINGS-ACL.456. https://doi.org/10.18653/v1/2024.findings-acl.456.
- [234] Heming Xia, Chak Tou Leong, Wenjie Wang, Yongqi Li, and Wenjie Li. Tokenskip: Controllable chain-of-thought compression in llms. In Christos Christodoulopoulos, Tanmoy Chakraborty, Carolyn Rose, and Violet Peng, editors, Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing, EMNLP 2025, Suzhou, China, November 4-9, 2025, pages 3351–3363. Association for Computational Linguistics, 2025. doi: 10.18653/V1/2025.EMNLP-MAIN.165. https://doi.org/10.18653/v1/2025.emnlp-main.165.
- [235] Chengen Xie, Bin Sun, Tianyu Li, Junjie Wu, Zhihui Hao, XianPeng Lang, and Hongyang Li. Latentvla: Efficient vision-language models for autonomous driving via latent action prediction. CoRR, abs/2601.05611, 2026. doi: 10.48550/ARXIV.2601.05611. https://doi.org/10.48550/arXiv.2601.05611.
- [236] Wanyun Xie, Francesco Tonin, and Volkan Cevher. Mad-mix: Multi-modal data mixtures via latent space coupling for vision-language model training. CoRR, abs/2602.07790, 2026. doi: 10.48550/ARXIV.2602.07790. https://doi.org/10.48550/arXiv.2602.07790.
- [237] Wenpeng Xing, Mohan Li, Chunqiang Hu, Haitao XuNingyu Zhang, Bo Lin, and Meng Han. Latent fusion jailbreak: Blending harmful and harmless representations to elicit unsafe LLM outputs. CoRR, abs/2508.10029,

2025. doi: 10.48550/ARXIV.2508.10029. https://doi.org/10.48550/arXiv.2508.10029.

- [238] Fangzhi Xu, Zhiyong Wu, Qiushi Sun, Siyu Ren, Fei Yuan, Shuai Yuan, Qika Lin, Yu Qiao, and Jun Liu. Symbolllm: Towards foundational symbol-centric interface for large language models. In Lun-Wei Ku, Andre Martins, and Vivek Srikumar, editors, Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), ACL 2024, Bangkok, Thailand, August 11-16, 2024, pages 13091–13116. Association for Computational Linguistics, 2024. doi: 10.18653/V1/2024.ACL-LONG.707. https://doi.org/10. 18653/v1/2024.acl-long.707.
- [239] Kevin Xu and Issei Sato. A formal comparison between chain-of-thought and latent thought. CoRR, abs/2509.25239, 2025. doi: 10.48550/ARXIV.2509.25239. https://doi.org/10.48550/arXiv.2509.25239.
- [240] Liyan Xu, Mo Yu, Fandong Meng, and Jie Zhou. No global plan in chain-of-thought: Uncover the latent planning horizon of llms. CoRR, abs/2602.02103, 2026. doi: 10.48550/ARXIV.2602.02103. https://doi.org/10.48550/ arXiv.2602.02103.
- [241] Xin Xu, Tong Yu, Xiang Chen, Haoliang Wang, Julian McAuley, and Saayan Mitra. Thinkrouter: Efficient reasoning via routing thinking between latent and discrete spaces. arXiv preprint arXiv:2602.11683, 2026.
- [242] Xun Xu. G-memllm: Gated latent memory augmentation for long-context reasoning in large language models. CoRR, abs/2602.00015, 2026. doi: 10.48550/ARXIV.2602.00015. https://doi.org/10.48550/arXiv.2602.00015.
- [243] Yige Xu, Xu Guo, Zhiwei Zeng, and Chunyan Miao. Softcot: Soft chain-of-thought for efficient reasoning with llms. In Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (Volume


- 1: Long Papers), ACL 2025, Vienna, Austria, July 27 - August 1, 2025, pages 23336–23351. Association for Computational Linguistics, 2025. https://aclanthology.org/2025.acl-long.1137/.
- [244] Yige Xu, Xu Guo, Zhiwei Zeng, and Chunyan Miao. Softcot++: Test-time scaling with soft chain-of-thought reasoning. CoRR, abs/2505.11484, 2025. doi: 10.48550/ARXIV.2505.11484. https://doi.org/10.48550/arXiv. 2505.11484.
- [245] Zelai Xu, Wanjun Gu, Chao Yu, Yi Wu, and Yu Wang. Learning strategic language agents in the werewolf game with iterative latent space policy optimization. In Forty-second International Conference on Machine Learning, ICML 2025, Vancouver, BC, Canada, July 13-19, 2025, volume 267. PMLR / OpenReview.net, 2025. https://proceedings.mlr.press/v267/xu25h.html.
- [246] Zhongxing Xu, Zhonghua Wang, Zhe Qian, Dachuan Shi, Feilong Tang, Ming Hu, Shiyan Su, Xiaocheng Zou, Wei Feng, Dwarikanath Mahapatra, et al. Thinking in uncertainty: Mitigating hallucinations in mlrms with latent entropy-aware decoding. arXiv preprint arXiv:2603.13366, 2026.
- [247] Qiyao Xue, Weichen Liu, Shiqi Wang, Haoming Wang, Yuyang Wu, and Wei Gao. Reasoning path and latent state analysis for multi-view visual spatial reasoning: A cognitive science perspective. CoRR, abs/2512.02340,

2025. doi: 10.48550/ARXIV.2512.02340. https://doi.org/10.48550/arXiv.2512.02340.

- [248] Cheng Yan, Wuyang Zhang, Zhiyuan Ning, Fan Xu, Ziyang Tao, Lu Zhang, Bing Yin, and Yanyong Zhang. Breaking model lock-in: Cost-efficient zero-shot LLM routing via a universal latent space. In Fortieth AAAI Conference on Artificial Intelligence, Thirty-Eighth Conference on Innovative Applications of Artificial Intelligence, Sixteenth Symposium on Educational Advances in Artificial Intelligence, AAAI 2026, Singapore, January 20-27, 2026, pages 36483–36490. AAAI Press, 2026. doi: 10.1609/AAAI.V40I43.40970. https://doi.org/10.1609/aaai. v40i43.40970.
- [249] Fuxiang Yang, Donglin Di, Lulu Tang, Xuancheng Zhang, Lei Fan, Hao Li, Chen Wei, Tonghua Su, and Baorui Ma. Chain of world: World model thinking in latent motion, 2026. https://arxiv.org/abs/2603.03195.
- [250] Jingyuan Yang, Rongjun Li, Weixuan Wang, Ziyu Zhou, Zhiyong Feng, and Wei Peng. Lf-steering: Latent feature activation steering for enhancing semantic consistency in large language models. CoRR, abs/2501.11036,

2025. doi: 10.48550/ARXIV.2501.11036. https://doi.org/10.48550/arXiv.2501.11036.

- [251] Zeyuan Yang, Xueyang Yu, Delin Chen, Maohao Shen, and Chuang Gan. Machine mental imagery: Empower multimodal reasoning with latent visual tokens. CoRR, abs/2506.17218, 2025. doi: 10.48550/ARXIV.2506.17218. https://doi.org/10.48550/arXiv.2506.17218.
- [252] Zhipeng Yang, Junzhuo Li, Siyu Xia, and Xuming Hu. Internal chain-of-thought: Empirical evidence for layer-wise subtask scheduling in llms. In Christos Christodoulopoulos, Tanmoy Chakraborty, Carolyn Rose, and Violet Peng, editors, Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing, EMNLP 2025, Suzhou, China, November 4-9, 2025, pages 22536–22564. Association for Computational Linguistics, 2025. doi: 10.18653/V1/2025.EMNLP-MAIN.1147. https://doi.org/10.18653/v1/2025.emnlp-main.1147.
- [253] Jihan Yao, Achin Kulshrestha, Nathalie Rauschmayr, Reed Roberts, Banghua Zhu, Yulia Tsvetkov, and Federico Tombari. Reading between the lines: Abstaining from vlm-generated OCR errors via latent representation probes. CoRR, abs/2511.19806, 2025. doi: 10.48550/ARXIV.2511.19806. https://doi.org/10.48550/arXiv.2511.19806.
- [254] Shunyu Yao, Jeffrey Zhao, Dian Yu, Nan Du, Izhak Shafran, Karthik R. Narasimhan, and Yuan Cao. React: Synergizing reasoning and acting in language models. In The Eleventh International Conference on Learning Representations, ICLR 2023, Kigali, Rwanda, May 1-5, 2023. OpenReview.net, 2023. https://openreview.net/ forum?id=WE_vluYUL-X.
- [255] Seonghyeon Ye, Joel Jang, Byeongguk Jeon, Se June Joo, Jianwei Yang, Baolin Peng, Ajay Mandlekar, Reuben Tan, Yu-Wei Chao, Bill Yuchen Lin, Lars Liden, Kimin Lee, Jianfeng Gao, Luke Zettlemoyer, Dieter Fox, and Minjoon Seo. Latent action pretraining from videos. CoRR, abs/2410.11758, 2024. doi: 10.48550/ARXIV.2410.11758. https://doi.org/10.48550/arXiv.2410.11758.
- [256] Seonghyeon Ye, Joel Jang, Byeongguk Jeon, Se June Joo, Jianwei Yang, Baolin Peng, Ajay Mandlekar, Reuben Tan, Yu-Wei Chao, Bill Yuchen Lin, Lars Liden, Kimin Lee, Jianfeng Gao, Luke Zettlemoyer, Dieter Fox, and Minjoon Seo. Latent action pretraining from videos. In The Thirteenth International Conference on Learning Representations, ICLR 2025, Singapore, April 24-28, 2025. OpenReview.net, 2025. https://openreview.net/ forum?id=VYOe2eBQeh.


- [257] Wencheng Ye, Xiaoyang Yuan, Yi Bin, Pengpeng Zeng, Hengyu Jin, Liang Peng, and Heng Tao Shen. RISER: orchestrating latent reasoning skills for adaptive activation steering. CoRR, abs/2601.09269, 2026. doi: 10.48550/ ARXIV.2601.09269. https://doi.org/10.48550/arXiv.2601.09269.
- [258] Wengao Ye, Yan Liang, and Lianlei Shan. Thinking on the fly: Test-time reasoning enhancement via latent thought policy optimization. CoRR, abs/2510.04182, 2025. doi: 10.48550/ARXIV.2510.04182. https://doi.org/ 10.48550/arXiv.2510.04182.
- [259] Xinwu Ye, Yicheng Mao, Jia Zhang, Yimeng Liu, Li Hao, Fang Wu, Zhiwei Li, Yuxuan Liao, Zehong Wang, Zhiyuan Liu, et al. Latentchem: From textual cot to latent thinking in chemical reasoning. arXiv preprint arXiv:2602.07075, 2026.
- [260] Xin Yi, Yue Li, Dongsheng Shi, Linlin Wang, Xiaoling Wang, and Liang He. Latent-space adversarial training with post-aware calibration for defending large language models against jailbreak attacks. Expert Syst. Appl., 296:129101, 2026. doi: 10.1016/J.ESWA.2025.129101. https://doi.org/10.1016/j.eswa.2025.129101.
- [261] Shukang Yin, Chaoyou Fu, Sirui Zhao, Ke Li, Xing Sun, Tong Xu, and Enhong Chen. A survey on multimodal large language models. CoRR, abs/2306.13549, 2023. doi: 10.48550/ARXIV.2306.13549. https://doi.org/10. 48550/arXiv.2306.13549.
- [262] Runyang You, Yongqi Li, Meng Liu, Wenjie Wang, Liqiang Nie, and Wenjie Li. Parallel test-time scaling for latent reasoning models. CoRR, abs/2510.07745, 2025. doi: 10.48550/ARXIV.2510.07745. https://doi.org/10. 48550/arXiv.2510.07745.
- [263] Chengting Yu, Xiaobo Shu, Yadao Wang, Yizhen Zhang, Haoyi Wu, You Wu, Rujiao Long, Ziheng Chen, Yuchi Xu, Wenbo Su, et al. Spiralformer: Looped transformers can learn hierarchical dependencies via multi-resolution recursion. arXiv preprint arXiv:2602.11698, 2026.
- [264] Xinlei Yu, Chengming Xu, Guibin Zhang, Zhangquan Chen, Yudong Zhang, Yongbo He, Peng-Tao Jiang, Jiangning Zhang, Xiaobin Hu, and Shuicheng Yan. Vismem: Latent vision memory unlocks potential of visionlanguage models. CoRR, abs/2511.11007, 2025. doi: 10.48550/ARXIV.2511.11007. https://doi.org/10.48550/ arXiv.2511.11007.
- [265] Xinlei Yu, Chengming Xu, Zhangquan Chen, Bo Yin, Cheng Yang, Yongbo He, Yihao Hu, Jiangning Zhang, Cheng Tan, Xiaobin Hu, and Shuicheng Yan. Dual latent memory for visual multi-agent system. CoRR, abs/2602.00471, 2026. doi: 10.48550/ARXIV.2602.00471. https://doi.org/10.48550/arXiv.2602.00471.
- [266] Zhenrui Yue, Bowen Jin, Huimin Zeng, Honglei Zhuang, Zhen Qin, Jinsung Yoon, Lanyu Shang, Jiawei Han, and Dong Wang. Hybrid latent reasoning via reinforcement learning. CoRR, abs/2505.18454, 2025. doi: 10.48550/ARXIV.2505.18454. https://doi.org/10.48550/arXiv.2505.18454.
- [267] Boyi Zeng, He Li, Shixiang Song, Yixuan Wang, Ziwei He, Xinbing Wang, and Zhouhan Lin. Pretraining LLM with latent thoughts in continuous space. CoRR, abs/2509.23184, 2025. doi: 10.48550/ARXIV.2509.23184. https://doi.org/10.48550/arXiv.2509.23184.
- [268] Boyi Zeng, Yiqin Hao, He Li, Shixiang Song, Feichen Song, Zitong Wang, Siyuan Huang, Yi Xu, ZiWei He, Xinbing Wang, and Zhouhan Lin. Pretraining with token-level adaptive latent chain-of-thought. CoRR, abs/2602.08220,

2026. doi: 10.48550/ARXIV.2602.08220. https://doi.org/10.48550/arXiv.2602.08220.

- [269] Qingwen Zeng, Wenhao Huang, Zerui Xu, Zijie Guo, Yu Sun, Cheng Yang, Siru Ouyang, Jiri Gesi, Fang Wu, Jiayi Zhang, et al. Latent action reparameterization for efficient agent inference. In ICLR 2026 Workshop on Memory for LLM-Based Agentic Systems, 2026.
- [270] Yuliang Zhan, Xinyu Tang, Han Wan, Jian Li, Ji-Rong Wen, and Hao Sun. L2v-cot: Cross-modal transfer of chainof-thought reasoning via latent intervention. CoRR, abs/2511.17910, 2025. doi: 10.48550/ARXIV.2511.17910. https://doi.org/10.48550/arXiv.2511.17910.
- [271] Changshuo Zhang. Reasoning while recommending: Entropy-guided latent reasoning in generative re-ranking models. CoRR, abs/2601.13533, 2026. doi: 10.48550/ARXIV.2601.13533. https://doi.org/10.48550/arXiv.2601. 13533.
- [272] Chubin Zhang, Jianan Wang, Zifeng Gao, Yue Su, Tianru Dai, Cai Zhou, Jiwen Lu, and Yansong Tang. CLAP: contrastive latent action pretraining for learning vision-language-action models from human videos. CoRR, abs/2601.04061, 2026. doi: 10.48550/ARXIV.2601.04061. https://doi.org/10.48550/arXiv.2601.04061.
- [273] Guibin Zhang, Muxin Fu, and Shuicheng Yan. Memgen: Weaving generative latent memory for self-evolving agents. CoRR, abs/2509.24704, 2025. doi: 10.48550/ARXIV.2509.24704. https://doi.org/10.48550/arXiv.2509.24704.


- [274] Guibin Zhang, Fanci Meng, Guancheng Wan, Zherui Li, Kun Wang, Zhenfei Yin, Lei Bai, and Shuicheng Yan. Latentevolve: Self-evolving test-time scaling in latent space. CoRR, abs/2509.24771, 2025. doi: 10.48550/ARXIV. 2509.24771. https://doi.org/10.48550/arXiv.2509.24771.
- [275] Hanqing Zhang, Haolin Song, Shaoyu Li, Ming Zhou, and Dawei Song. A survey of controllable text generation using transformer-based pre-trained language models. ACM Comput. Surv., 56(3):64:1–64:37, 2024. doi: 10.1145/3617680. https://doi.org/10.1145/3617680.
- [276] Huanyu Zhang, Wenshan Wu, Chengzu Li, Ning Shang, Yan Xia, Yangyu Huang, Yifan Zhang, Li Dong, Zhang Zhang, Liang Wang, Tieniu Tan, and Furu Wei. Latent sketchpad: Sketching visual thoughts to elicit multimodal reasoning in mllms. CoRR, abs/2510.24514, 2025. doi: 10.48550/ARXIV.2510.24514. https: //doi.org/10.48550/arXiv.2510.24514.
- [277] Jason Zhang and Scott Viteri. Uncovering latent chain of thought vectors in language models. CoRR, abs/2409.14026, 2024. doi: 10.48550/ARXIV.2409.14026. https://doi.org/10.48550/arXiv.2409.14026.
- [278] Lvmin Zhang, Anyi Rao, and Maneesh Agrawala. Adding conditional control to text-to-image diffusion models. In IEEE/CVF International Conference on Computer Vision, ICCV 2023, Paris, France, October 1-6, 2023, pages 3813–3824. IEEE, 2023. doi: 10.1109/ICCV51070.2023.00355. https://doi.org/10.1109/ICCV51070.2023.00355.
- [279] Nonghai Zhang, Weitao Ma, Zhanyu Ma, Jun Xu, Jiuchong Gao, Jinghua Hao, Renqing He, and Jingwen Xu. Silence the judge: Reinforcement learning with self-verifier via latent geometric clustering. CoRR, abs/2601.08427,

2026. doi: 10.48550/ARXIV.2601.08427. https://doi.org/10.48550/arXiv.2601.08427.

- [280] Shimin Zhang, Xianwei Chen, Yufan Shen, Ziyuan Ye, and Jibin Wu. Relax: Reasoning with latent exploration for large reasoning models. CoRR, abs/2512.07558, 2025. doi: 10.48550/ARXIV.2512.07558. https://doi.org/10. 48550/arXiv.2512.07558.
- [281] Yang Zhang, Chenwei Wang, Ouyang Lu, Yuan Zhao, Yunfei Ge, Zhenglong Sun, Xiu Li, Chi Zhang, Chenjia Bai, and Xuelong Li. Align-then-steer: Adapting the vision-language action models through unified latent guidance. CoRR, abs/2509.02055, 2025. doi: 10.48550/ARXIV.2509.02055. https://doi.org/10.48550/arXiv.2509.02055.
- [282] Yang Zhang, Wenxin Xu, Xiaoyan Zhao, Wenjie Wang, Fuli Feng, Xiangnan He, and Tat-Seng Chua. Reinforced latent reasoning for llm-based recommendation. CoRR, abs/2505.19092, 2025. doi: 10.48550/ARXIV.2505.19092. https://doi.org/10.48550/arXiv.2505.19092.
- [283] Yang Zhang, Danyang Li, Yuxuan Li, Xin Zhang, Tianyu Xie, Mingming Cheng, and Xiang Li. Crystal: Spontaneous emergence of visual latents in mllms, 2026. https://arxiv.org/abs/2602.20980.
- [284] Yiming Zhang, Qiangyu Yan, Borui Jiang, and Kai Han. Multimodal latent reasoning via hierarchical visual cues injection. CoRR, abs/2602.05359, 2026. doi: 10.48550/ARXIV.2602.05359. https://doi.org/10.48550/arXiv. 2602.05359.
- [285] Yuyi Zhang, Boyu Tang, Tianjie Ju, Sufeng Duan, and Gongshen Liu. Do latent tokens think? A causal and adversarial analysis of chain-of-continuous-thought. CoRR, abs/2512.21711, 2025. doi: 10.48550/ARXIV.2512.

21711. https://doi.org/10.48550/arXiv.2512.21711.

- [286] Zeyu Zhang, Rui Li, Xiaoyan Zhao, Yang Zhang, Wenjie Wang, Xu Chen, and Tat-Seng Chua. Nextmem: Towards latent factual memory for llm-based agents. arXiv preprint arXiv:2603.15634, 2026.
- [287] Zhen Zhang, Xuehai He, Weixiang Yan, Ao Shen, Chenyang Zhao, Shuohang Wang, Yelong Shen, and Xin Eric Wang. Soft thinking: Unlocking the reasoning potential of llms in continuous concept space. CoRR, abs/2505.15778, 2025. doi: 10.48550/ARXIV.2505.15778. https://doi.org/10.48550/arXiv.2505.15778.
- [288] Haoyu Zheng, Zhuonan Wang, Yuqian Yuan, Tianwei Lin, Wenqiao Zhang, Zheqi Lv, Juncheng Li, Siliang Tang, Yueting Zhuang, and Hongyang He. Fast thinking for large language models. CoRR, abs/2509.23633, 2025. doi: 10.48550/ARXIV.2509.23633. https://doi.org/10.48550/arXiv.2509.23633.
- [289] Haoyu Zheng, Yun Zhu, Yuqian Yuan, Bo Yuan, Wenqiao Zhang, Siliang Tang, and Jun Xiao. PILOT: planning via internalized latent optimization trajectories for large language models. CoRR, abs/2601.19917, 2026. doi: 10.48550/ARXIV.2601.19917. https://doi.org/10.48550/arXiv.2601.19917.
- [290] Yujia Zheng, Zhuokai Zhao, Zijian Li, Yaqi Xie, Mingze Gao, Lizhu Zhang, and Kun Zhang. Thought communication in multiagent collaboration. CoRR, abs/2510.20733, 2025. doi: 10.48550/ARXIV.2510.20733. https://doi.org/10.48550/arXiv.2510.20733.


- [291] Zhi Zheng and Wee Sun Lee. Soft-grpo: Surpassing discrete-token LLM reinforcement learning via gumbelreparameterized soft-thinking policy optimization. CoRR, abs/2511.06411, 2025. doi: 10.48550/ARXIV.2511.

06411. https://doi.org/10.48550/arXiv.2511.06411.

- [292] Zhi Zheng and Wee Sun Lee. Beyond imitation: Reinforcement learning for active latent planning. CoRR, abs/2601.21598, 2026. doi: 10.48550/ARXIV.2601.21598. https://doi.org/10.48550/arXiv.2601.21598.
- [293] Fangwei Zhu and Zhifang Sui. Colt: Reasoning with chain of latent tool calls. CoRR, abs/2602.04246, 2026. doi: 10.48550/ARXIV.2602.04246. https://doi.org/10.48550/arXiv.2602.04246.
- [294] Hanlin Zhu, Shibo Hao, Zhiting Hu, Jiantao Jiao, Stuart Russell, and Yuandong Tian. Reasoning by superposition: A theoretical perspective on chain of continuous thought. CoRR, abs/2505.12514, 2025. doi: 10.48550/ARXIV. 2505.12514. https://doi.org/10.48550/arXiv.2505.12514.
- [295] Qinglin Zhu, Runcong Zhao, Hanqi Yan, Yulan He, Yudong Chen, and Lin Gui. Soft reasoning: Navigating solution spaces in large language models through controlled embedding exploration. In Aarti Singh, Maryam Fazel, Daniel Hsu, Simon Lacoste-Julien, Felix Berkenkamp, Tegan Maharaj, Kiri Wagstaff, and Jerry Zhu, editors, Forty-second International Conference on Machine Learning, ICML 2025, Vancouver, BC, Canada, July 13-19, 2025, volume 267 of Proceedings of Machine Learning Research. PMLR / OpenReview.net, 2025. https://proceedings.mlr.press/v267/zhu25ae.html.
- [296] Rui-Jie Zhu, Zixuan Wang, Kai Hua, Tianyu Zhang, Ziniu Li, Haoran Que, Boyi Wei, Zixin Wen, Fan Yin, He Xing, Lu Li, Jiajun Shi, Kaijing Ma, Shanda Li, Taylor Kergan, Andrew Smith, Xingwei Qu, Mude Hui, Bohong Wu, Qiyang Min, Hongzhi Huang, Xun Zhou, Wei Ye, Jiaheng Liu, Jian Yang, Yunfeng Shi, Chenghua Lin, Enduo Zhao, Tianle Cai, Ge Zhang, Wenhao Huang, Yoshua Bengio, and Jason Eshraghian. Scaling latent reasoning via looped language models. CoRR, abs/2510.25741, 2025. doi: 10.48550/ARXIV.2510.25741. https://doi.org/10.48550/arXiv.2510.25741.
- [297] Ruijie Zhu, Tianhao Peng, Tianhao Cheng, Xingwei Qu, Jinfa Huang, Dawei Zhu, Hao Wang, Kaiwen Xue, Xuanliang Zhang, Yong Shan, Tianle Cai, Taylor Kergan, Assel Kembay, Andrew Smith, Chenghua Lin, Binh Nguyen, Yuqi Pan, Yuhong Chou, Zefan Cai, Zhenhe Wu, Yongchi Zhao, Tianyu Liu, Jian Yang, Wangchunshu Zhou, Chujie Zheng, Chongxuan Li, Yuyin Zhou, Zhoujun Li, Zhaoxiang Zhang, Jiaheng Liu, Ge Zhang, Wenhao Huang, and Jason Eshraghian. A survey on latent reasoning. CoRR, abs/2507.06203, 2025. doi: 10.48550/ARXIV.2507.06203. https://doi.org/10.48550/arXiv.2507.06203.
- [298] Ren Zhuang, Ben Wang, and Shuifa Sun. The geometric reasoner: Manifold-informed latent foresight search for long-context reasoning. CoRR, abs/2601.18832, 2026. doi: 10.48550/ARXIV.2601.18832. https://doi.org/10. 48550/arXiv.2601.18832.
- [299] Andy Zou, Long Phan, Sarah Li Chen, James Campbell, Phillip Guo, Richard Ren, Alexander Pan, Xuwang Yin, Mantas Mazeika, Ann-Kathrin Dombrowski, Shashwat Goel, Nathaniel Li, Michael J. Byun, Zifan Wang, Alex Mallen, Steven Basart, Sanmi Koyejo, Dawn Song, Matt Fredrikson, J. Zico Kolter, and Dan Hendrycks. Representation engineering: A top-down approach to AI transparency. CoRR, abs/2310.01405, 2023. doi: 10.48550/ARXIV.2310.01405. https://doi.org/10.48550/arXiv.2310.01405.
- [300] Jiaru Zou, Xiyuan Yang, Ruizhong Qiu, Gaotang Li, Katherine Tieu, Pan Lu, Ke Shen, Hanghang Tong, Yejin Choi, Jingrui He, James Zou, Mengdi Wang, and Ling Yang. Latent collaboration in multi-agent systems. CoRR, abs/2511.20639, 2025. doi: 10.48550/ARXIV.2511.20639. https://doi.org/10.48550/arXiv.2511.20639.
- [301] Jiaxuan Zou, Yaozhong Xiong, and Yong Liu. Capabilities and fundamental limits of latent chain-of-thought. CoRR, abs/2602.01148, 2026. doi: 10.48550/ARXIV.2602.01148. https://doi.org/10.48550/arXiv.2602.01148.


