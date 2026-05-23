---
type: source
kind: paper
title: "CMA-ES with Learning Rate Adaptation: Can CMA-ES with Default Population Size Solve Multimodal and Noisy Problems?"
authors: Masahiro Nomura, Youhei Akimoto, Isao Ono
year: 2023
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/2304.03473v3
source_local: ../raw/2023-nomura-cma-es-learning-rate-adaptation.pdf
ingested_for_concept: cma-es-with-warmstart.md
cites:
  - ../wiki/concepts/cma-es-with-warmstart.md
  - ../wiki/problems/9-*.md
  - ../wiki/problems/15-*.md
  - ../wiki/problems/16-*.md
---

# arXiv:2304.03473v3[cs.NE]14Sep2023

## CMA-ES with Learning Rate Adaptation: Can CMA-ES with Default Population Size Solve Multimodal and Noisy Problems?

Masahiro Nomura∗

Youhei Akimoto

Isao Ono

nomura.m.ad@m.titech.ac.jp Tokyo Institute of Technology Yokohama, Kanagawa, Japan

akimoto@cs.tsukuba.ac.jp University of Tsukuba & RIKEN AIP Tsukuba, Ibaraki, Japan

isao@c.titech.ac.jp Tokyo Institute of Technology Yokohama, Kanagawa, Japan

### ABSTRACT

The covariance matrix adaptation evolution strategy (CMA-ES) is one of the most successful methods for solving black-box continuous optimization problems. One practically useful aspect of the CMA-ES is that it can be used without hyperparameter tuning. However, the hyperparameter settings still have a considerable impact, especially for difficult tasks such as solving multimodal or noisy problems. In this study, we investigate whether the CMA-ES with default population size can solve multimodal and noisy problems. To perform this investigation, we develop a novel learning rate adaptation mechanism for the CMA-ES, such that the learning rate is adapted so as to maintain a constant signal-to-noise ratio. We investigate the behavior of the CMA-ES with the proposed learning rate adaptation mechanism through numerical experiments, and compare the results with those obtained for the CMA-ES with a fixed learning rate. The results demonstrate that, when the proposed learning rate adaptation is used, the CMA-ES with default population size works well on multimodal and/or noisy problems, without the need for extremely expensive learning rate tuning.

### CCS CONCEPTS

• Mathematics of computing → Continuous optimization.

### KEYWORDS

covariance matrix adaptation evolution strategy, black-box optimization

ACM Reference Format:

Masahiro Nomura, Youhei Akimoto, and Isao Ono. 2023. CMA-ES with Learning Rate Adaptation: Can CMA-ES with Default Population Size Solve Multimodal and Noisy Problems?. In Genetic and Evolutionary Computation Conference (GECCO ’23), July 15–19, 2023, Lisbon, Portugal. ACM, New York, NY, USA, 11 pages. https://doi.org/10.1145/3583131.3590358

### 1 INTRODUCTION

Among the existing methods for solving black-box continuous optimization problems, the covariance matrix adaptation evolution

∗Corresponding author

Permission to make digital or hard copies of all or part of this work for personal or classroom use is granted without fee provided that copies are not made or distributed for profit or commercial advantage and that copies bear this notice and the full citation on the first page. Copyrights for components of this work owned by others than the author(s) must be honored. Abstracting with credit is permitted. To copy otherwise, or republish, to post on servers or to redistribute to lists, requires prior specific permission and/or a fee. Request permissions from permissions@acm.org.

GECCO ’23, July 15–19, 2023, Lisbon, Portugal © 2023 Copyright held by the owner/author(s). Publication rights licensed to ACM. ACM ISBN 979-8-4007-0119-1/23/07...$15.00 https://doi.org/10.1145/3583131.3590358

strategy (CMA-ES) [8, 12] is one of the most successful. In the CMAES, optimization is performed by updating the multivariate normal distribution. That is, the CMA-ES first samples candidate solutions from the distribution and then updates the distribution parameters (i.e., the mean vector 𝑚 and covariance matrix Σ = 𝜎2𝐶) based on the objective function 𝑓 value. The CMA-ES update is partly based on the natural gradient descent [3, 21] of the expected 𝑓 , and𝑚 and 𝐶 in the CMA-ES are updated to decrease the expected evaluation value. One practically useful aspect of the CMA-ES is that it is a quasi-hyperparameter-free algorithm; that is, practitioners can use the CMA-ES without tuning its hyperparameters, because default values are provided for all hyperparameters based on theoretical analysis and extensive empirical evaluations. In detail, the hyperparameter values are automatically computed from the dimension 𝑑 and population size 𝜆 where, by default, 𝜆 = 4 + ⌊3ln(𝑑)⌋.

While the default 𝜆 works well for a wide range of unimodal problems, increasing 𝜆 from this default value can be helpful for difficult tasks such as solving multimodal and additive noisy problems [11, 18, 19]. However, in a black-box scenario, determining the problem structure of 𝑓 is challenging and, thus, determining the appropriate 𝜆 in advance is similarly challenging. To resolve this issue, online adaptation of 𝜆 has been proposed [13, 15, 17–19]. The population size adaptation (PSA)-CMA-ES [19] is a representative 𝜆 adaptation mechanism with promising performance when applied to difficult tasks, including multimodal and additive noisy problems.

It has been observed that, in the CMA-ES, increasing 𝜆 has an effect similar to decreasing the 𝑚 learning rate, i.e., 𝜂𝑚 [16]1. Indeed, the 𝑚 and Σ learning rate, i.e., 𝜂, is another hyperparameter that critically impacts performance. If 𝜂 is too high, the parameter update is unstable; however, an excessively small 𝜂 degrades the search efficiency. Miyazawa and Akimoto [16] reported that the CMA-ES with even a relatively small 𝜆 (e.g., 𝜆 = √

𝑑) solves multimodal problems, through appropriate setting of 𝜂. However, discovery of such an appropriate 𝜂 is difficult in practice, as prior knowledge is often limited and hyperparameter tuning requires extremely expensive numerical investigations. Therefore, the realization of online 𝜂 adaptation depending on the problem difficulty will constitute an important advance, as practitioners can then use the CMA-ES safely, without the need for prior knowledge or expensive trial-and-error calculations. In particular, we believe that 𝜂 adaptation has advantages over 𝜆 adaptation from a practical perspective, as the former is more suited to parallel implementation. For example, practitioners often wish to specify a certain number of workers as the value of 𝜆, to avoid wasting computing resources.

1Note that, in Ref. [16], the rank-one update was excluded from the CMA-ES. In this study, however, we consider the CMA-ES that includes the rank-one update. As an additional note, in [16], the notation 𝑐𝑚 is used instead of 𝜂𝑚.

However, 𝜆 adaptation may not fully utilize the available computing resources, depending on the variations in this value that occur during optimization. In contrast, with 𝜂 adaptation, the available resources can be fully exploited, as 𝜆 is fixed to the maximum number of workers. Moreover, with 𝜂 adaptation, the parameter update is regularly performed, whereas the CMA-ES with 𝜆 adaptation produces no progress until all 𝜆 solutions are evaluated. This fact makes it difficult to determine when to terminate the search.

Online adaptation of𝜂 itself is not new, and several previous studies attempted to adapt the 𝜂 values in CMA-ES variants; however, those adaptations targeted speed-up [7, 15, 20]. One notable exception is the 𝜂 adaptation proposed by Krause [14], which aims to solve additive noisy problems by introducing new evolution strategies2. However, in this approach, the problem difficulty is estimated through resampling, i.e., by repeating an evaluation of the same solution; thus, it is not suitable for solving (noiseless) multimodal problems. Furthermore, the internal parameters of the evolution strategies are greatly modified and, thus, their direct application to the CMA-ES is difficult.

The aim of this study is to determine whether the CMA-ES with default 𝜆 can solve multimodal and additive noisy problems without the need for extremely expensive 𝜂 tuning, and without adjusting the CMA-ES apart from 𝜂. To achieve this, we propose an 𝜂 adaptation mechanism for the CMA-ES, which we call the learning rate adaptation (LRA)-CMA-ES, through which 𝜂 is adapted to maintain a constant signal-to-noise ratio (SNR). The key feature of the proposed method is that specific knowledge of the internal mechanism of the distribution parameter update is not required in order to estimate the SNR. As a result, the proposed method is widely applicable to different CMA-ES variants (e.g., diagonal decoding (dd)-CMA [2]). This is despite the fact that the present study considers the most commonly used CMA-ES, which combines the weighted recombination, step-size 𝜎 adaptation, rank-one update, and rank-𝜇 update.

The remainder of this paper is organized as follows: Section 2 explains the CMA-ES algorithm, Section 3 presents the proposed 𝜂 adaptation mechanism based on the SNR estimation, Section 4 evaluates the proposed 𝜂 adaptation on noiseless and noisy problems and, finally, Section 5 concludes with a summary and a discussion of future work.

### 2 CMA-ES

We consider minimization of the objective function 𝑓 : R𝑑 → R. The CMA-ES uses a multivariate normal distribution to generate candidate solutions, where the N(𝑚,𝜎2𝐶) distribution is parameterized by three elements: the mean vector 𝑚 ∈ R𝑑, the step-size 𝜎 ∈ R>0, and the covariance matrix 𝐶 ∈ R𝑑×𝑑.

The CMA-ES first initializes the𝑚(0),𝜎(0), and 𝐶(0) parameters. Then, the following steps are repeated until a pre-defined stopping criterion is satisfied. Step 1. Sampling and Evaluation At iteration 𝑡 + 1 (where 𝑡 begins at 0), 𝜆 candidate solutions 𝑥𝑖 (𝑖 =

- 1, 2, · · · ,𝜆) are sampled independently from N(𝑚(𝑡), (𝜎(𝑡))2𝐶(𝑡)),


2Note that there are already ESs that use a (fixed) 𝜂 smaller than one (i.e., rescaled mutations) [5, 6, 22].

as follows:

𝑦𝑖 = √︁𝐶(𝑡)𝑧𝑖, (1) 𝑥𝑖 = 𝑚(𝑡) + 𝜎(𝑡)𝑦𝑖, (2)

where 𝑧𝑖 ∼ N(0,𝐼), with 𝐼 being the identity matrix. The solutions are evaluated on 𝑓 and sorted in ascending order. We let 𝑥𝑖:𝜆 be the 𝑖-th best candidate solution 𝑓 (𝑥1:𝜆) ⩽ 𝑓 (𝑥2:𝜆) ⩽ · · · ⩽ 𝑓 (𝑥𝜆:𝜆). Additionally, we let 𝑦𝑖:𝜆 and 𝑧𝑖:𝜆 be random vectors corresponding to 𝑥𝑖:𝜆.

- Step 2. Computation of Evolution Paths Using the weight function 𝑤𝑖 and the parent number 𝜇 ⩽ 𝜆, the

weighted averages 𝑑𝑦 = 𝑖 𝜇=1 𝑤𝑖𝑦𝑖:𝜆 and 𝑑𝑧 = 𝑖 𝜇=1 𝑤𝑖𝑧𝑖:𝜆 are calculated. Then, the evolution paths are updated as follows:

𝑝𝜎(𝑡+1) = (1 − 𝑐𝜎)𝑝𝜎(𝑡) + √︁𝑐𝜎 (2 − 𝑐𝜎)𝜇𝑤𝑑𝑧, (3) 𝑝𝑐(𝑡+1) = (1 − 𝑐𝑐)𝑝𝑐(𝑡) + ℎ𝜎(𝑡+1)√︁𝑐𝑐(2 − 𝑐𝑐)𝜇𝑤𝑑𝑦, (4)

where 𝜇𝑤 = 1/ 𝑖 𝜇=1 𝑤𝑖2, 𝑐𝜎, and 𝑐𝑐 are the cumulation factors, and ℎ𝜎(𝑡+1) is the Heaviside function, which is defined as follows [9]:

ℎ𝜎(𝑡+1) =   

1 if ∥𝑝

(𝑡+1) 𝜎 ∥2

1−(1−𝑐𝜎)2(𝑡+1) < 2 + 𝑑4+1 𝑑, 0 otherwise.

(5)

- Step 3. Updating of Distribution Parameters The distribution parameters are updated as follows [9]:


𝑚(𝑡+1) = 𝑚(𝑡) + 𝑐𝑚𝜎(𝑡)𝑑𝑦, (6)

###### ∥𝑝𝜎(𝑡+1) ∥ E[∥N(0,𝐼)∥]

𝑐𝜎 𝑑𝜎

𝜎(𝑡+1) = 𝜎(𝑡) exp min 1,

− 1 , (7)

𝐶(𝑡+1) = 1 + (1 − ℎ𝜎(𝑡+1))𝑐1𝑐𝑐(2 − 𝑐𝑐) 𝐶(𝑡)

∑︁𝜇

⊤

+ 𝑐1 𝑝𝑐(𝑡+1) 𝑝𝑐(𝑡+1)

−𝐶(𝑡)

𝑤𝑖 𝑦𝑖:𝜆𝑦𝑖⊤:𝜆 −𝐶(𝑡)

+𝑐𝜇

,

𝑖=1

rank-one update

rank-𝜇 update

(8) whereE[∥N(0,𝐼)∥] ≈

√

𝑑 1 − 41𝑑 + 211𝑑2 is theexpected Euclidean

norm of the sample of a standard normal distribution; 𝑐𝑚 is the learning rate for 𝑚, usually set to 1; 𝑐1 and 𝑐𝜇 are the learning rates for the rank-one and -𝜇 updates of 𝐶, respectively; and 𝑑𝜎 is a damping factor for the 𝜎 adaptation.

### 3 LEARNING RATE ADAPTATION MECHANISM

We consider the updating of the distribution parameters 𝜃𝑚 = 𝑚 and 𝜃Σ = vec(Σ), where vec is the vectorization operator and Σ = 𝜎2𝐶 in the case of the standard CMA-ES. Let Δ𝑚(𝑡) = 𝑚(𝑡+1) −𝑚(𝑡) and ΔΣ(𝑡) = vec(Σ(𝑡+1) − Σ(𝑡)) be the original updates of 𝑚 and Σ, respectively. We introduce the learning rate factors 𝜂𝑚(𝑡) and 𝜂Σ(𝑡). The modified updates are performed in form 𝜃𝑚(𝑡+1) = 𝜃𝑚(𝑡) + 𝜂𝑚(𝑡)Δ𝑚(𝑡) and 𝜃Σ(𝑡+1) = 𝜃Σ(𝑡) +𝜂Σ(𝑡)ΔΣ(𝑡). We then adapt 𝜂𝑚(𝑡) and 𝜂Σ(𝑡) separately.

### 3.1 Main Concept

We adapt the learning rate factor 𝜂 for a component 𝜃 (either 𝜃𝑚 = 𝑚 or 𝜃Σ = vec(Σ)) of the distribution parameters based on the SNR of the update:

SNR := ∥E[Δ]∥2𝐹 Tr(𝐹 Cov[Δ])

= ∥E[Δ]∥2𝐹 E[∥Δ∥2𝐹] − ∥E[Δ]∥2𝐹

, (9)

where 𝐹 is the Fisher information matrix of the𝜃 for which𝜂 is to be updated, and ∥Δ∥𝐹 = (ΔT𝐹Δ)1/2 is the norm under 𝐹. The choice of Fisher metric gives invariance property against parameterization of the probability distribution. We attempt to adapt𝜂 so that SNR = 𝛼𝜂, where 𝛼 > 0 is a hyperparameter determining the target SNR.

The rationale behind this concept is as follows. Let us assume that 𝜂 is sufficiently small that the distribution parameters do not change significantly over 𝑛 iterations. That is, we assume 𝜃(𝑡+𝑘) ≈ 𝜃(𝑡)

for 𝑘 = 1, . . .,𝑛. Then, {Δ(𝑡+𝑘)}𝑛𝑘=−01 are roughly considered to be independently and identically distributed. Hence, 𝑛 steps of the

update read as

𝑛∑︁−1

Δ(𝑡+𝑘), (10a)

𝜃(𝑡+𝑛) = 𝜃(𝑡) + 𝜂

𝑘=0

≈ 𝜃(𝑡) + D 𝑛𝜂E[Δ],𝑛𝜂2 Cov[Δ] , (10b)

where D(𝐴,𝐵) is thedistributionwithexpectation𝐴 and (co)variance

𝐵. That is, by setting small 𝜂 and considering the results of 𝑛 = 1/𝜂 updates, we obtain an update that is more concentrated around the expected behavior than that expected for one update with 𝜂 = 1. The expected change of 𝜃 in 𝑛 = 1/𝜂 iterations measured by the squared Fisher norm, which approximates the Kullback-Leibler di-

vergence between 𝜃(𝑡) and 𝜃(𝑡+𝑛), is ∥E[Δ]∥2𝐹 + 𝜂 Tr(𝐹 Cov[Δ]), where the former and latter terms come from the signal and noise,

2 𝐹

respectively. The SNR over 𝑛 iterations is ∥E[Δ]∥

𝜂 Tr(𝐹 Cov[Δ]) = 𝜂1SNR. Therefore, maintaining SNR = 𝛼𝜂 implies maintaining the SNR as 𝛼 over 𝑛 = 1/𝜂 iterations, independently of 𝜂.

### 3.2 Signal-to-Noise Ratio Estimation

We estimate ∥E[Δ]∥2 and E[∥Δ∥2] for each component (𝑚 and Σ) with moving averages. We let E(0) = 0 and V(0) = 0, and update them as

E(𝑡+1) = (1 − 𝛽)E(𝑡) + 𝛽Δ˜ (𝑡), (11a) V(𝑡+1) = (1 − 𝛽)V(𝑡) + 𝛽∥Δ˜ (𝑡) ∥22, (11b)

respectively, where 𝛽 is a hyperparameter, Δ˜ (𝑡) is the update at iteration𝑡 in the local coordinate at which the 𝐹 at𝜃(𝑡) becomes the iden-

tity, and ∥·∥2 is the ℓ2-norm. We then regard 22−−2𝛽𝛽 ∥E∥22 − 2−𝛽2𝛽 V and V as the estimates of ∥E[Δ]∥22 and E[∥Δ∥22], respectively (See supplementary for the derivation).

The rationale behind our estimators is as follows. Let us suppose that 𝜂𝑚 and 𝜂Σ are sufficiently small for us to assume that the parameters 𝑚 and Σ do not significantly change over 𝑛 iterations. Then, the Δ˜ (𝑡+𝑖) (𝑖 = 0, ..,𝑛 − 1) are considered to be located on the same local coordinate and to be independently and identically

distributed. Then, ignoring the (1 − 𝛽)𝑛 terms, we have

𝛽 2 − 𝛽

Cov[Δ˜ ] . (12) (See the supplementary material for the derivation.) Therefore, we have E[∥E∥22] ≈ ∥E[Δ˜ ]∥22 + 2−𝛽𝛽 Tr(Cov[Δ˜ ]). Similarly, it is apparent that E[V] ≈ E[∥Δ˜ ∥22] = ∥E[Δ˜ ]∥22 + Tr(Cov[Δ˜ ]).

E(𝑡+𝑛) ∼ D E[Δ˜ ],

The SNR is then estimated as SNR := ∥E[Δ˜ ]∥2 Tr(Cov[Δ˜ ])

###### = ∥E[Δ˜ ]∥2 E[∥Δ˜ ∥2] − ∥E[Δ˜ ]∥2

, (13a)

∥E∥22 − 2−𝛽𝛽 V V − ∥E∥22

=: SNR. (13b)

≈

### 3.3 Learning Rate Factor Adaptation

We attempt to adapt 𝜂 so that SNR = 𝛼𝜂, where 𝛼 > 0 is the hyperparameter. This adaptation is expressed as

SNR 𝛼𝜂 − 1 , (14)

𝜂 ← 𝜂 exp min(𝛾𝜂, 𝛽)Π[−1,1]

where Π[−1,1] is the projection onto [−1, 1] and 𝛾 is a hyperparameter. If SNR > 𝛼𝜂, 𝜂 is increased, and vice versa. Because of these feedback mechanisms, SNR/(𝛼𝜂) is expected to remain in the vicinity of 1. In the above expression, the projection Π[−1,1] is introduced to prevent a significant change of 𝜂 in one iteration. The damping factor min(𝛾𝜂, 𝛽) is introduced for the following reasons. First, the factor 𝛽 is introduced to allow for the effect of the change of the previous 𝜂 to appear in SNR. Second, the factor 𝛾𝜂 is introduced to prevent 𝜂 from changing to a greater extent than the factor of exp(𝛾) or exp(−𝛾) in 1/𝜂 iterations. Following updating of 𝜂 by Eq. (14), we set the upper bound to 1 using 𝜂 ← min(𝜂, 1), to prevent unstable behavior. Allowing 𝜂 to take values exceeding 1 would accelerate the optimization; however, this aspect is not considered in the present study, as the aim is to safely solve difficult problems.

#### 3.4 Local Coordinate-System Definition We define the local coordinate system such that the Fisher infor-

mation matrices, 𝐹𝑚 and 𝐹Σ, corresponding to each component of the distribution parameters, 𝑚 and Σ, respectively, are the identity

matrices. It is well-known that 𝐹𝑚 = Σ−1 and 𝐹Σ = 2−1Σ−1 ⊗ Σ−1. Their square roots are √𝐹𝑚 = √Σ−1 and √𝐹Σ = 2−12

√Σ−1. Therefore, we define

√Σ−1 ⊗

√

Σ−1Δ𝑚, (15a) Δ˜ Σ = 2−21 vec(

Δ˜𝑚 =

√

√

Σ−1 vec−1(ΔΣ)

Σ−1). (15b)

#### 3.5 Covariance Matrix Decomposition Following computation of the updated covariance matrix Σ(𝑡+1) =

Σ(𝑡) + 𝜂Σ(𝑡) vec−1(ΔΣ(𝑡)), we must split the matrix into components 𝜎 and 𝐶. For this purpose, we adopt the following, simple strategy:

𝜎(𝑡+1) = det(Σ(𝑡+1)) 21𝑑 , (16a) 𝐶(𝑡+1) = (𝜎(𝑡+1))−2Σ(𝑡+1). (16b)

### 3.6 Step-Size Correction

When the learning rate for the 𝑚 update, i.e., 𝜂𝑚, is updated, the appropriate𝜎 changes. Through a quality gain analysis in which the expected improvement of the 𝑓 value in one step was analyzed, a previous study [1] demonstrated that the optimal 𝜎 is proportional to 1/𝜂𝑚 for infinite-dimensional convex quadratic functions. To maintain the optimal 𝜎 while 𝜂𝑚 varies, we correct 𝜎 after each 𝜂𝑚 update as follows:

𝜂𝑚(𝑡) 𝜂𝑚(𝑡+1)

𝜎(𝑡+1). (17)

𝜎(𝑡+1) ←

#### 3.7 Overall Procedure Algorithm 1 shows the overall LRA-CMA-ES procedure. In line

- 2 of Algorithm 1, CMA(·) receives the old parameters 𝑚(𝑡),𝜎(𝑡), and 𝐶(𝑡) and outputs new parameters 𝑚(𝑡+1),𝜎(𝑡+1), and 𝐶(𝑡+1) by running Steps 1–3 described in Sec. 2. Note that the inter-


nal parameters, such as the evolution paths 𝑝𝜎 and 𝑝𝑐, are updated and stored in CMA(·). They are now omitted for simplic-

ity. The subscript ·{𝑚,Σ} (e.g., as in 𝜂{𝑚,Σ}) indicates that there are parameters for 𝑚 and Σ, respectively. For example, E{(𝑚,𝑡+1Σ)} ← (1 − 𝛽{𝑚,Σ})E{(𝑚,𝑡) Σ} + 𝛽{𝑚,Σ}Δ˜ {(𝑡𝑚,) Σ} is an abbreviation for the following two update equations: E𝑚(𝑡+1) ← (1 − 𝛽𝑚)E𝑚(𝑡) + 𝛽𝑚Δ˜𝑚(𝑡) and EΣ(𝑡+1) ← (1 − 𝛽Σ)EΣ(𝑡) + 𝛽ΣΔ˜ Σ(𝑡).

### 4 EXPERIMENTS

In this study, we performed various experiments to investigate the following research questions (RQs):

- RQ1. Does the 𝜂 adaptation in the LRA-CMA-ES behave appropriately in accordance with the problem structure?
- RQ2. Can the LRA-CMA-ES solve multimodal and noisy problems even though a default 𝜆 is used? How does its efficiency compare to the CMA-ES with fixed 𝜂?
- RQ3. How does the performance change when the LRA-CMA-ES hyperparameters are changed?

This section is organized as follows: the experiment setups are described in Sec.4.1; in Sec.4.2, the 𝜂 adaptation in the LRA-CMAES for noiseless and noisy problems (RQ1) is demonstrated; in Sec. 4.3, we compare the LRA-CMA-ES with the CMA-ES with fixed 𝜂 values (RQ2); finally, in Sec. 4.4, our investigation of the effect of the LRA-CMA-ES hyperparameters (RQ3) is reported. Our code is available at https://github.com/nomuramasahir0/cma-learningrate-adaptation.

- 4.1 Experiment Setups


The benchmark problem definitions and initial distributions are listed in Table 1. In each case (except for the Rosenbrock function), the known global optimal solution is located at 𝑥 = 0. For the Rosenbrock function, the global optimal solution is 𝑥 = 1. Note that, although the Rosenbrock function has local minima, in our setting, it could be regarded as an almost unimodal problem. Similar to [11], we imposed additional bounds for the Ackley function. In the noisy problems, we considered the additive Gaussian noise 𝜖 ∼ N(0,𝜎𝑛2) with variance 𝜎𝑛2.

Algorithm 1 LRA-CMA-ES Input: 𝑚(0) ∈ R𝑑,𝜎(0) ∈ R>0,𝜆 ∈ N,𝛼, 𝛽{𝑚,Σ},𝛾 ∈ R Set: 𝑡 = 0,𝐶(0) = 𝐼,𝜂{(𝑚,0) Σ} = 1, E(0) = 0, V(0) = 0

- 1: while stopping criterion not met do
- 2: 𝑚(𝑡+1),𝜎(𝑡+1),𝐶(𝑡+1) ← CMA(𝑚(𝑡),𝜎(𝑡),𝐶(𝑡))
- 3: // calculate parameter one-step differences
- 4: Δ𝑚(𝑡) ← 𝑚(𝑡+1) −𝑚(𝑡)
- 5: Σ(𝑡+1) ← 𝜎(𝑡+1)

2

𝐶(𝑡+1)

- 6: ΔΣ(𝑡) ← vec Σ(𝑡+1) − Σ(𝑡)
- 7: // local coordinate
- 8: Δ˜𝑚(𝑡) ←

√

Σ(𝑡)−1Δ𝑚(𝑡)

- 9: Δ˜ Σ(𝑡) ← 2−1/2vec √

Σ(𝑡)−1vec−1 ΔΣ(𝑡)

√

Σ(𝑡)−1

- 10: // update evolution paths and estimate SNR
- 11: E{(𝑚,𝑡+1Σ)} ← (1 − 𝛽{𝑚,Σ})E{(𝑚,𝑡) Σ} + 𝛽{𝑚,Σ}Δ˜ {(𝑡𝑚,) Σ}
- 12: V{(𝑚,𝑡+Σ1)} ← (1 − 𝛽{𝑚,Σ})V{(𝑚,𝑡)Σ} + 𝛽{𝑚,Σ}∥Δ˜ {(𝑡𝑚,) Σ}∥22
- 13: SNR{𝑚,Σ} ←

∥E{(𝑚,𝑡+1Σ)}∥22− 2−𝛽𝛽{𝑚,{𝑚,ΣΣ}}

V{(𝑚,𝑡+Σ1)} V{(𝑚,𝑡+Σ1)}−∥E{(𝑚,𝑡+1Σ)}∥22

- 14: // update learning rates
- 15: 𝜂{(𝑡𝑚,+1Σ)} ← 𝜂{(𝑡𝑚,) Σ} · exp min(𝛾𝜂{(𝑡𝑚,) Σ}, 𝛽{𝑚,Σ})Π[−1,1] SNR𝛼𝜂 {𝑚,Σ}

{𝑚,Σ}

− 1

- 16: 𝜂{(𝑡𝑚,+1Σ)} ← min(𝜂{(𝑡𝑚,+1Σ)}, 1)
- 17: // update parameters with adaptive learning rates
- 18: 𝑚(𝑡+1) ← 𝑚(𝑡) + 𝜂𝑚(𝑡+1)Δ𝑚(𝑡)
- 19: Σ(𝑡+1) ← Σ(𝑡) + 𝜂Σ(𝑡+1) vec−1(ΔΣ(𝑡))
- 20: // decompose Σ to 𝜎 and 𝐶
- 21: 𝜎(𝑡+1) ← det(Σ(𝑡+1)) 21𝑑 , 𝐶(𝑡+1) ← (𝜎(𝑡+1))−2Σ(𝑡+1)

- 22: // 𝜎 correction
- 23: 𝜎(𝑡+1) ← 𝜎(𝑡+1) (𝜂𝑚(𝑡)/𝜂𝑚(𝑡+1))
- 24: 𝑡 ← 𝑡 + 1
- 25: end while


In all experiments, we used the default 𝜆 = 4+⌊3ln𝑑⌋. As regards the LRA-CMA-ES hyperparameters, we set 𝛼 = 1.4, 𝛽𝑚 = 0.1, 𝛽Σ = 0.03, and 𝛾 = 0.1 based on preliminary experiments. As noted above, Sec. 4.4 reports our analysis of the sensitivity of these hyperparameters. The other internal parameters of the CMA-ES were set to the values recommended in [9].

### 4.2 Learning Rate Behavior

Figure 1 shows typical LRA-CMA-ES behavior on noiseless problems. It is apparent that 𝜂Σ retained relatively high values for the Sphere function. However, 𝜂Σ decreased significantly for the Ellipsoid and Rosenbrock functions. We believe that this behavior is undesirable, because the default 𝜂 already works well on these unimodal problems. We can increase 𝜂 by changing the hyperparameters of the proposed 𝜂 adaptation; however, this change may be detrimental as regards applications to multimodal problems.

It is apparent that 𝜂𝑚 was slightly smaller on multimodal problems than on unimodal problems. For the Rastrigin function in

##### Table 1: Definitions of benchmark problems and initial distributions used in experiments.

Definitions Initial Distributions 𝑓Sphere(𝑥) = 𝑑𝑖=1 𝑥𝑖2 𝑚(0) = [3, . . ., 3],𝜎(0) = 2 𝑓Ellipsoid(𝑥) = 𝑑𝑖=1(1000𝑑𝑖−−11𝑥𝑖)2 𝑚(0) = [3, . . ., 3],𝜎(0) = 2 𝑓Rosenbrock(𝑥) = 𝑑𝑖=−11(100(𝑥𝑖+1 − 𝑥𝑖2)2 + (𝑥𝑖 − 1)2) 𝑚(0) = [0, . . ., 0],𝜎(0) = 0.1 𝑓Ackley(𝑥) = 20 − 20 · exp(−0.2√︃

1 𝑑

𝑑 𝑖=1 𝑥𝑖2) + 𝑒 − exp(𝑑1 𝑑𝑖=1 cos(2𝜋𝑥𝑖)) 𝑚(0) = [15.5, . . ., 15.5],𝜎(0) = 14.5

𝑓Schaffer(𝑥) = 𝑑𝑖=−11(𝑥𝑖2 + 𝑥𝑖2+1)0.25 · [sin2(50 · (𝑥𝑖2 + 𝑥𝑖2+1)0.1) + 1] 𝑚(0) = [55, . . ., 55],𝜎(0) = 45 𝑓Rastrigin(𝑥) = 10𝑑 + 𝑑𝑖=1(𝑥𝑖2 − 10cos(2𝜋𝑥𝑖)) 𝑚(0) = [3, . . ., 3],𝜎(0) = 2 𝑓Bohachevsky(𝑥) = 𝑑𝑖=−11(𝑥𝑖2 + 2𝑥𝑖2+1 − 0.3cos(3𝜋𝑥𝑖) − 0.4cos(4𝜋𝑥𝑖+1) + 0.7) 𝑚(0) = [8, . . ., 8],𝜎(0) = 7 𝑓Griewank(𝑥) = 40001 𝑑𝑖=1 𝑥𝑖2 − Π𝑑𝑖=1 cos(𝑥𝑖/

√𝑖) + 1 𝑚(0) = [305, . . ., 305],𝜎(0) = 295

|Sphere Ellipsoid Rosenbrock Ackley| | | | | | | |Schaﬀer Rastrigin Bohachevsky| | | |Griewank| |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| | | | | | | | | | | | | | |
| | | | | | | | | | | | | | |
| | | | | | | | | | | | | | |
|0 2000 0 10000 0 20000 0 7000 0| | | | | | | |20000 0 200000 0 4000 0| | | |5000| |


106

102

f(m)

10−2

10−6

100

10−1

ηm

10−2

10−3

100

10−1

ηΣ

10−2

3

m

0

−3

100

(step-size)σ

10−3

10−6

100

√eig

10−3

10−6

Function Evaluations

##### Figure 1: Typical LRA-CMA-ES behavior on 10-dimensional (10-D) noiseless problems. The coordinates of 𝑚 and the square roots of the eigenvalues of 𝜎2𝐶 (denoted by √︁eig) are shown in different colors.

particular, 𝜂𝑚 and 𝜂Σ clearly decreased at the beginning of the optimization; this reflects the difficulty of optimization for multimodal problems. Subsequently, 𝜂 increased, as the optimization became as easy as that for a unimodal problem. This behavior demonstrates that the LRA-CMA-ES can adapt 𝜂 according to the difficulty of the search situation.

decreased. Through this adaptation, the SNR remained constant. Notably, similar behavior was obtained for the Noisy Rastrigin function, which featured both noise and multimodality.

### 4.3 Learning Rate Adaptation Effect

###### Figure 2 shows typical 𝜂 adaptation behavior on noisy problems.

The noise had an essentially negligible effect in the early stage and, thus, the 𝜂 behavior on the noisy problems was similar to that on the noiseless problems. However, as the optimization proceeded and the function value approached the same scale as the noise value, the noise began to have an critical effect. In response, 𝜂

Figures 3 and 4 show the performance of the LRA-CMA-ES and that oftheCMA-ESwith afixedlearning rate (𝜂𝑚,𝜂Σ ∈ {100, 10−1, 10−2}) on the noiseless problems. Note that the CMA-ES with 𝜂𝑚 = 1.0 and 𝜂Σ = 1.0 was the CMA-ES with the default 𝜂 (i.e., the original CMA-ES). Each trial was considered a success if 𝑓 (𝑚) reached the

###### Noisy Sphere

###### Noisy Ellipsoid

###### Noisy Rastrigin

106

102

f(m)

10−2

100

10−1

ηm

10−2

10−3

100

10−1

ηΣ

10−2

10−3

3

m

0

−3

100

(step-size)σ

10−3

10−6

100

√eig

10−3

10−6

101 103 105

101 103 105

101 104

Function Evaluations

##### Figure 2: Typical LRA-CMA-ES behavior on 10-D noisy problems. The noise variance 𝜎𝑛2 was set to 1.

target value 10−8 before 107 function evaluations, or before a numerical error occurred as a result of excessively small 𝜎. In addition to the success rate, we also employed the SP1 [4], i.e., the average number of evaluations among successful trials until the target value was reached divided by the success rate. We performed 30 trials for each setting.

To compare the performance of these strategies on the selected noisy problems, we employed the empirical cumulative density function (ECDF) used in COCO, which is a platform for comparing continuous optimizers in a black-box setting [10]. Using 𝑁target target values, we recorded the number of evaluations until the (noiseless) 𝑓 (𝑚) reached each target value for the first time, with the maximum function evaluation set to 108. We collected data by running 𝑁trial independent trials, and obtained a total of 𝑁target·𝑁trial targets for each problem. We set the target values to 106−9(𝑖−1)/(𝑁target−1)

for𝑖 = 1, . . ., 𝑁target, with 𝑁target = 30. By running 𝑁trial = 20 trials, we had 600 targets for each problem. Figure 5 shows the percentage of target values achieved for each number of evaluations.

4.3.1 Noiseless Problems. We compared the success rates of the LRA-CMA-ES and the CMA-ES with fixed 𝜂 values, as shown in

Figure 3. For the multimodal problems, the CMA-ES with high 𝜂 often failed to reach the optimum. However, the CMA-ES with small 𝜂 had a high success rate, demonstrating the clear performance dependence on 𝜂. In contrast, the LRA-CMA-ES had a relatively good success rate even though no 𝜂 tuning was required. It is noteworthy that the LRA-CMA-ES succeeded in all trials on the Rastrigin function, even though the default sample size (e.g., 𝜆 = 15 for 𝑑 = 40) was used and 𝜂 was not tuned in advance.

The LRA-CMA-ES performance degraded on the Schaffer function with 𝑑 = 40. From the results indicating that the CMA-ES with an appropriately tuned, small 𝜂 achieved a relatively high success rate, the LRA-CMA-ES result may have been obtained because 𝜂 was not appropriately adapted in that case. We leave a further investigation for future work.

Figure 4 shows the SP1 results for the LRA-CMA-ES and the CMA-ES with fixed 𝜂 values. The CMA-ES with the default 𝜂

(𝜂𝑚 = 1.0,𝜂Σ = 1.0) outperformed the other methods on the unimodal problems; however, this performance degraded significantly on the multimodal problems as a result of optimization failure. In contrast, the CMA-ES with small 𝜂 sometimes exhibited good performance on such multimodal problems, but did not exhibit efficiency when applied to the unimodal and relatively easy multimodal problems. Therefore, for the CMA-ES with fixed 𝜂, a clear trade-off in efficiency exists depending on the 𝜂 setting. In contrast, the LRACMA-ES exhibited stable and relatively good performance when applied to unimodal and multimodal problems. Again, no tuning of 𝜂 was performed, which is extremely expensive in practice. There is scope for improvement of the LRA-CMA-ES performance on unimodal problems; however, the current sub-par performance can be somewhat mitigated by changing the hyperparameters. Again, we discuss the impact of the hyperparameters in Sec. 4.4.

4.3.2 Noisy Problems. Figure 5 shows the ECDF results for the LRA-CMA-ES and for the CMA-ES with fixed 𝜂 values. We considered two noise strengths: weak and strong, i.e., 𝜎𝑛2 = 1 and 106, respectively.

For the weak noise settings, the CMA-ES with small 𝜂 reached all target values. In contrast, the CMA-ES with large 𝜂 failed to approach the global optimum and yielded a sub-optimal solution. The LRA-CMA-ES achieved similar performance to the CMA-ES with small 𝜂 without tuning of 𝜂. For the strong noise settings, even the CMA-ES with small 𝜂 stopped improving the 𝑓 value before the global optimum was reached. In contrast, the LRA-CMA-ES continued to improve the 𝑓 value. Notably, the results for the Noisy Rastrigin function suggest that the LRA-CMA-ES can simultaneously handle both noise and multimodality.

### 4.4 Effects of Hyperparameters

Figure 6 shows the success rate and SP1 values with respect to 𝛼 on the 30-dimensional (30-D) noiseless Sphere, Schaffer, and Rastrigin functions. For the Sphere function, it is apparent that smaller SP1 could be achieved for a smaller 𝛼 value. However, excessively small 𝛼 yielded optimization failures for the multimodal problems. The current setting of 𝛼 = 1.4 seems reasonable, but further investigation is necessary.

Figure 7 shows the success rate and SP1 values with respect to 𝛽Σ. Clearly, excessively large 𝛽Σ caused optimization failures for

LRA

- ηm = 0.01,ηΣ = 0.1

- ηm = 0.01,ηΣ = 1.0


ηm = 0.1,ηΣ = 0.01

- ηm = 0.1,ηΣ = 1.0

- ηm = 1.0,ηΣ = 0.01


- ηm = 1.0,ηΣ = 0.1

- ηm = 1.0,ηΣ = 1.0


ηm = 0.01,ηΣ = 0.01

ηm = 0.1,ηΣ = 0.1

Sphere

Ellipsoid

Rosenbrock

Ackley

1.0

1.0

| | | | | | |
|---|---|---|---|---|---|
| | | | | | |
| | | | | | |


| | | | | | |
|---|---|---|---|---|---|
| | | | | | |
| | | | | | |
| | | | | | |


| | | | | | |
|---|---|---|---|---|---|
| | | | | | |
| | | | | | |
| | | | | | |


| | | | | | |
|---|---|---|---|---|---|
| | | | | | |
| | | | | | |
| | | | | | |


1.0

1.0

0.5

0.5

0.5

0.5

SuccessRate

0.0

0.0

0.0

0.0

10 20 30 40

10 20 30 40

10 20 30 40

10 20 30 40

Schaﬀer

Rastrigin

Bohachevsky

Griewank

| | | | | | |
|---|---|---|---|---|---|
| | | | | | |
| | | | | | |
| | | | | | |


1.0

1.0

1.0

1.0

0.5

0.5

0.5

0.5

0.0

0.0

0.0

0.0

10 20 30 40

10 20 30 40

10 20 30 40

10 20 30 40

Dimension

##### Figure 3: Success rate versus dimension (noiseless problems).

LRA

- ηm = 0.01,ηΣ = 0.1

- ηm = 0.01,ηΣ = 1.0


ηm = 0.1,ηΣ = 0.01

- ηm = 0.1,ηΣ = 1.0

- ηm = 1.0,ηΣ = 0.01


- ηm = 1.0,ηΣ = 0.1

- ηm = 1.0,ηΣ = 1.0


ηm = 0.01,ηΣ = 0.01

ηm = 0.1,ηΣ = 0.1

###### Sphere

###### Ellipsoid

###### Rosenbrock

###### Ackley

| | | | | |
|---|---|---|---|---|
| | | | | |
| | | | | |
| | | | | |
| | | | | |
| | | | | |
| | | | | |
| | | | | |
| | | | | |


| | | | | |
|---|---|---|---|---|
| | | | | |
| | | | | |
| | | | | |
| | | | | |
| | | | | |
| | | | | |
| | | | | |
| | | | | |
| | | | | |


| | | | | |
|---|---|---|---|---|
| | | | | |
| | | | | |
| | | | | |
| | | | | |
| | | | | |
| | | | | |
| | | | | |
| | | | | |
| | | | | |
| | | | | |


| | | | | |
|---|---|---|---|---|
| | | | | |
| | | | | |
| | | | | |
| | | | | |
| | | | | |
| | | | | |
| | | | | |
| | | | | |
| | | | | |
| | | | | |
| | | | | |
| | | | | |


- 104
- 105
- 106


- 104
- 105
- 106


- 104
- 105
- 106


- 104
- 105


10 20 30 40

10 20 30 40

10 20 30 40

10 20 30 40

SP1

###### Schaﬀer

###### Rastrigin

###### Bohachevsky

Griewank

- 104
- 105
- 106


| | | | | | | |
|---|---|---|---|---|---|---|
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |


| | | | | |
|---|---|---|---|---|
| | | | | |
| | | | | |
| | | | | |
| | | | | |
| | | | | |
| | | | | |
| | | | | |
| | | | | |
| | | | | |
| | | | | |
| | | | | |
| | | | | |
| | | | | |
| | | | | |
| | | | | |


| | | | | |
|---|---|---|---|---|
| | | | | |
| | | | | |
| | | | | |
| | | | | |
| | | | | |
| | | | | |
| | | | | |
| | | | | |
| | | | | |


- 104
- 105
- 106


- 105

- 106

- 107


- 105
- 106


10 20 30 40

10 20 30 40

10 20 30 40

10 20 30 40

Dimension

##### Figure 4: SP1 versus dimension (noiseless problems).

the multimodal problems. However, setting an excessively small 𝛽Σ yielded slow convergence for the Rastrigin function. An additional

result (𝛽Σ ∈ {0.01, 0.02, ..., 0.05}) is presented in the supplementary material.

We also conducted similar experiments on the hyperparameters 𝛽𝑚 and 𝛾, to confirm their effects. These hyperparameters appear to have had a mild impact on the overall performance compared to 𝛼 and 𝛽Σ. (These results are also presented in the supplementary material.)

### 5 CONCLUSION

In this study, we developed a new learning rate adaptation mechanism with the aim of solving multimodal and noisy problems via the CMA-ES with a default population size. The basic concept of the resulting algorithm, LRA-CMA-ES, is to adapt the learning rate so

that the SNR can be kept constant. Experiments involving noiseless multimodal problems revealed that the proposed LRA-CMA-ES can adapt the learning rate appropriately depending on the search situation, and that it works well without tuning of the learning rate. In noisy experiments, the LRA-CMA-ES continued to yield improved solution quality. This performance was observed even for strong noise settings, which yielded problems that the CMA-ES with a fixed learning rate failed to solve. In conclusion, the LRA-CMA-ES with default population size facilitates solution of multimodal and noisy problems to some extent, without the need for tuning of the learning rate.

However, we acknowledge limitations of the proposed LRACMA-ES, which will direct our future work. First, we observed that the LRA-CMA-ES experienced many failures for the 40-D Schaffer function, although the CMA-ES with an appropriately small learning rate succeeded with high probability. We believe that detailed

LRA

- ηm = 0.01,ηΣ = 0.1

- ηm = 0.01,ηΣ = 1.0


ηm = 0.1,ηΣ = 0.01

- ηm = 0.1,ηΣ = 1.0

- ηm = 1.0,ηΣ = 0.01


- ηm = 1.0,ηΣ = 0.1

- ηm = 1.0,ηΣ = 1.0


ηm = 0.01,ηΣ = 0.01

ηm = 0.1,ηΣ = 0.1

Noisy Sphere (σn2 = 1)

Noisy Ellipsoid (σn2 = 1)

Noisy Rastrigin (σn2 = 1)

| | | |
|---|---|---|
| | | |
| | | |


| | | | |
|---|---|---|---|
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |


1.0

1.0

1.0

0.8

0.8

0.8

0.6

0.6

0.6

0.4

0.4

0.4

prob.ofreachedtargets

0.2

0.2

0.2

0.0

0.0

0.0

101 102 103 104 105 106 107 108

101 102 103 104 105 106 107 108

101 102 103 104 105 106 107 108

Noisy Sphere (σn2 = 106)

Noisy Ellipsoid (σn2 = 106)

Noisy Rastrigin (σn2 = 106)

1.0

1.0

0.8

| | |
|---|---|
| | |
| | |
| | |
| | |


| | |
|---|---|
| | |


| | | | |
|---|---|---|---|
| | | | |
| | | | |
| | | | |
| | | | |


0.8

0.8

0.6

0.6

0.6

0.4

0.4

0.4

0.2

0.2

0.2

0.0

0.0

0.0

101 102 103 104 105 106 107 108

101 102 103 104 105 106 107 108

101 102 103 104 105 106 107 108

Function Evaluations

##### Figure 5: Empirical cumulative density function on 10-D noisy problems, with 𝜎𝑛2 set to 1 or 106.

α vs. Success Rate and SP1 (d = 30,30 trials)

Sphere

Schaﬀer

Rastrigin

SP1SuccessRate

| | | | | | | | | | | | | |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| | | | | | | | | | | | | |
| | | | | | | | | | | | | |
| | | | | | | | | | | | | |


| | | | | | | | | | | | | |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| | | | | | | | | | | | | |
| | | | | | | | | | | | | |
| | | | | | | | | | | | | |


| | | | | | | | | | | | | |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| | | | | | | | | | | | | |
| | | | | | | | | | | | | |
| | | | | | | | | | | | | |


1.0

1.0

1.0

0.5

0.5

0.5

0.0

0.0

0.0

0.2 0.6 1.0 1.4 1.8 2.2 2.6 3.0 3.4 3.8 4.2

0.2 0.6 1.0 1.4 1.8 2.2 2.6 3.0 3.4 3.8 4.2

0.2 0.6 1.0 1.4 1.8 2.2 2.6 3.0 3.4 3.8 4.2

- 104
- 105


- 105
- 106


| | | | | | | | | | | | | |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| | | | | | | | | | | | | |
| | | | | | | | | | | | | |
| | | | | | | | | | | | | |
| | | | | | | | | | | | | |
| | | | | | | | | | | | | |
| | | | | | | | | | | | | |
| | | | | | | | | | | | | |
| | | | | | | | | | | | | |
| | | | | | | | | | | | | |


| | | | | | | | | | | | | |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| | | | | | | | | | | | | |
| | | | | | | | | | | | | |
| | | | | | | | | | | | | |
| | | | | | | | | | | | | |
| | | | | | | | | | | | | |
| | | | | | | | | | | | | |
| | | | | | | | | | | | | |
| | | | | | | | | | | | | |
| | | | | | | | | | | | | |


| | | | | | | | | | | | | |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| | | | | | | | | | | | | |
| | | | | | | | | | | | | |
| | | | | | | | | | | | | |
| | | | | | | | | | | | | |
| | | | | | | | | | | | | |
| | | | | | | | | | | | | |
| | | | | | | | | | | | | |
| | | | | | | | | | | | | |


- 105
- 106


0.2 0.6 1.0 1.4 1.8 2.2 2.6 3.0 3.4 3.8 4.2

0.2 0.6 1.0 1.4 1.8 2.2 2.6 3.0 3.4 3.8 4.2

0.2 0.6 1.0 1.4 1.8 2.2 2.6 3.0 3.4 3.8 4.2

##### Figure 6: Success rate and SP1 versus hyperparameter 𝛼 on 30-D noiseless problems (30 trials).

βΣ vs. Success Rate and SP1 (d = 30,30 trials)

Sphere

Schaﬀer

Rastrigin

SP1SuccessRate

| | | | | | | | | |
|---|---|---|---|---|---|---|---|---|
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |


| | | | | | | | | |
|---|---|---|---|---|---|---|---|---|
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |


| | | | | | | | | |
|---|---|---|---|---|---|---|---|---|
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |


1.0

1.0

1.0

0.5

0.5

0.5

0.0

0.0

0.0

0.01 0.05 0.09 0.13 0.17 0.21 0.25

0.01 0.05 0.09 0.13 0.17 0.21 0.25

0.01 0.05 0.09 0.13 0.17 0.21 0.25

- 104
- 105


- 105
- 106


- 105
- 106


| | | | | | | | | |
|---|---|---|---|---|---|---|---|---|
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |


| | | | | | | | | |
|---|---|---|---|---|---|---|---|---|
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |


| | | | | | | | | |
|---|---|---|---|---|---|---|---|---|
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |


0.01 0.05 0.09 0.13 0.17 0.21 0.25

0.01 0.05 0.09 0.13 0.17 0.21 0.25

0.01 0.05 0.09 0.13 0.17 0.21 0.25

##### Figure 7: Success rate and SP1 versus hyperparameter 𝛽Σ on 30-D noiseless problems (30 trials).

analysis of the behavior of the SNR adaptation mechanism is important to clarify the reasons for this failure. On a related note, our understanding of the appropriate hyperparameter setting in the proposed learning rate adaptation mechanism remains limited. Our experiments revealed that the hyperparameter setting affects the trade-off between stability and convergence speed. Through experiment, we identified the hyperparameters that perform relatively well on noiseless and noisy problems; however, development of better configuration methods is important. For example, the constant value O(1) is used for the cumulation factors 𝛽𝑚 and 𝛽Σ, but it may be more reasonable to have these factors depend on the parameter

degrees of freedom, i.e., 𝛽𝑚 = O(1/𝑑) and 𝛽Σ = O(1/𝑑2). A deeper understanding of the effects of the hyperparameters including 𝛼

is critical to increasing the reliability of the proposed LRA-CMAES. Finally, a performance comparison of learning rate adaptation against population size adaptation is another interesting direction for future research.

### ACKNOWLEDGMENTS

This study was partially supported by JSPS KAKENHI, grant number 19H04179.

### REFERENCES

- [1] Youhei Akimoto, Anne Auger, and Nikolaus Hansen. 2020. Quality gain analysis of the weighted recombination evolution strategy on general convex quadratic functions. Theoretical Computer Science 832 (2020), 42–67. https://doi.org/10. 1016/j.tcs.2018.05.015 Theory of Evolutionary Computation.
- [2] Youhei Akimoto and Nikolaus Hansen. 2020. Diagonal Acceleration for Covariance Matrix Adaptation Evolution Strategies. Evol. Comput. 28, 3 (2020), 405–435. https://doi.org/10.1162/evco_a_00260
- [3] Youhei Akimoto, Yuichi Nagata, Isao Ono, and Shigenobu Kobayashi. 2010. Bidirectional relation between CMA evolution strategies and natural evolution strategies. In International conference on parallel problem solving from nature. Springer, 154–163.
- [4] Anne Auger and Nikolaus Hansen. 2005. A restart CMA evolution strategy with increasing population size. In 2005 IEEE congress on evolutionary computation, Vol. 2. IEEE, 1769–1776.
- [5] H.-G. Beyer. 1998. Mutate Large, But Inherit Small! On the Analysis of Rescaled

Mutations in (1˜,𝜆˜)-ES with Noisy Fitness Data. In Parallel Problem Solving from Nature, 5, A. E. Eiben, T. Bäck, M. Schoenauer, and H.-P. Schwefel (Eds.). Springer, Heidelberg, 109–118.

- [6] H.-G. Beyer. 2000. Evolutionary Algorithms in Noisy Environments: Theoretical Issues and Guidelines for Practice. Computer Methods in Applied Mechanics and Engineering 186, 2–4 (2000), 239–267.
- [7] Armand Gissler, Anne Auger, and Nikolaus Hansen. 2022. Learning Rate Adaptation by Line Search in Evolution Strategies with Recombination. In Proceedings of the Genetic and Evolutionary Computation Conference (Boston, Massachusetts) (GECCO ’22). Association for Computing Machinery, New York, NY, USA, 630–638. https://doi.org/10.1145/3512290.3528760
- [8] Nikolaus Hansen. 2016. The CMA evolution strategy: A tutorial. arXiv preprint arXiv:1604.00772 (2016).
- [9] Nikolaus Hansen and Anne Auger. 2014. Principled design of continuous stochastic search: From theory to practice. In Theory and principled methods for the design of metaheuristics. Springer, 145–180.
- [10] Nikolaus Hansen, Anne Auger, Raymond Ros, Olaf Mersmann, Tea Tušar, and Dimo Brockhoff. 2021. COCO: A platform for comparing continuous optimizers in a black-box setting. Optimization Methods and Software 36, 1 (2021), 114–144.
- [11] Nikolaus Hansen and Stefan Kern. 2004. Evaluating the CMA evolution strategy on multimodal test functions. In International conference on parallel problem solving from nature. Springer, 282–291.
- [12] Nikolaus Hansen and Andreas Ostermeier. 2001. Completely derandomized self-adaptation in evolution strategies. Evolutionary computation 9, 2 (2001), 159–195.
- [13] Michael Hellwig and Hans-Georg Beyer. 2016. Evolution Under Strong Noise: A Self-Adaptive Evolution Strategy Can Reach the Lower Performance Bound

- The pcCMSA-ES. In Parallel Problem Solving from Nature – PPSN XIV, Julia Handl, Emma Hart, Peter R. Lewis, Manuel López-Ibáñez, Gabriela Ochoa, and Ben Paechter (Eds.). Springer International Publishing, Cham, 26–36.

- [14] Oswin Krause. 2019. Large-Scale Noise-Resilient Evolution-Strategies. In Proceedings of the Genetic and Evolutionary Computation Conference (Prague, Czech Republic) (GECCO ’19). Association for Computing Machinery, New York, NY, USA, 682–690. https://doi.org/10.1145/3321707.3321724
- [15] Ilya Loshchilov, Marc Schoenauer, Michele Sebag, and Nikolaus Hansen. 2014. Maximum likelihood-based online adaptation of hyper-parameters in CMA-ES. In International Conference on Parallel Problem Solving from Nature. Springer, 70–79.
- [16] Hidekazu Miyazawa and Youhei Akimoto. 2017. Effect of the Mean Vector Learning Rate in CMA-ES. In Proceedings of the Genetic and Evolutionary Computation Conference (Berlin, Germany) (GECCO ’17). Association for Computing Machinery, New York, NY, USA, 721–728. https://doi.org/10.1145/3071178.3071203
- [17] Duc Manh Nguyen and Nikolaus Hansen. 2017. Benchmarking CMAES-APOP on the BBOB Noiseless Testbed. In Proceedings of the Genetic and Evolutionary Computation Conference Companion (Berlin, Germany) (GECCO ’17). Association for Computing Machinery, New York, NY, USA, 1756–1763. https://doi.org/10. 1145/3067695.3084207
- [18] Kouhei Nishida and Youhei Akimoto. 2016. Population Size Adaptation for the CMA-ES Based on the Estimation Accuracy of the Natural Gradient. InProceedings of the Genetic and Evolutionary Computation Conference 2016 (Denver, Colorado, USA) (GECCO ’16). Association for Computing Machinery, New York, NY, USA, 237–244. https://doi.org/10.1145/2908812.2908864
- [19] Kouhei Nishida and Youhei Akimoto. 2018. PSA-CMA-ES: CMA-ES with Population Size Adaptation. In Proceedings of the Genetic and Evolutionary Computation Conference (Kyoto, Japan) (GECCO ’18). Association for Computing Machinery, New York, NY, USA, 865–872. https://doi.org/10.1145/3205455.3205467
- [20] Masahiro Nomura and Isao Ono. 2022. Towards a Principled Learning Rate Adaptation for Natural Evolution Strategies. In Applications of Evolutionary Computation, Juan Luis Jiménez Laredo, J. Ignacio Hidalgo, and Kehinde Oluwatoyin Babaagba (Eds.). Springer International Publishing, Cham, 721–737.


- [21] Yann Ollivier, Ludovic Arnold, Anne Auger, and Nikolaus Hansen. 2017. Information-geometric optimization algorithms: A unifying picture via invariance principles. Journal of Machine Learning Research 18, 18 (2017), 1–65.
- [22] I. Rechenberg. 1994. Evolutionsstrategie ’94. Frommann-Holzboog Verlag, Stuttgart.


### A DERIVATION FOR SECTION 3.2 A.1 Derivation of Eq. (12)

This section presents the detailed derivation of Eq. (12). By ignoring (1 − 𝛽)𝑛, E(𝑡+𝑛) can be approximately calculated as follows:

E(𝑡+𝑛) = (1 − 𝛽)E(𝑡+𝑛−1) + 𝛽Δ˜ (𝑡+𝑛−1)

= (1 − 𝛽) (1 − 𝛽)E(𝑡+𝑛−2) + 𝛽Δ˜ (𝑡+𝑛−2) + 𝛽Δ˜ (𝑡+𝑛−1)

= ...

𝑛∑︁−1

(1 − 𝛽)𝑖𝛽Δ˜ (𝑡+𝑛−1−𝑖)

= (1 − 𝛽)𝑛 E(𝑡) +

𝑖=0

𝑛∑︁−1

(1 − 𝛽)𝑖𝛽Δ˜ (𝑡+𝑛−1−𝑖).

≈

𝑖=0

Here, we assume the Δ˜ (·) are uncorrelated with each other; this corresponds to the scenario where 𝜂 is sufficiently small. In this case, we can ignore the dependence of𝑡, i.e., E[Δ˜ (𝑡+𝑛−1−𝑖)] =: E[Δ˜ ]. Thus,

𝑛∑︁−1

(1 − 𝛽)𝑖𝛽E[Δ˜ ].

E[E(𝑡+𝑛) ] =

𝑖=0

Here,

𝑛∑︁−1

1 · {1 − (1 − 𝛽)𝑛} 1 − (1 − 𝛽)

1 − (1 − 𝛽)𝑛 𝛽

(1 − 𝛽)𝑖 =

=

.

𝑖=0

Then, by ignoring (1 − 𝛽)𝑛, we can approximate E[E(𝑡+𝑛)] as follows:

E[E(𝑡+𝑛) ] = [1 − (1 − 𝛽)𝑛]E[Δ˜ ] ≈ E[Δ˜ ].

Next, we consider the covariance Cov[E(𝑡+𝑛)]:

Cov[E(𝑡+𝑛) ] = E[E(𝑡+𝑛) (E(𝑡+𝑛) )⊤] − E[[E(𝑡+𝑛) ]([E(𝑡+𝑛) ])⊤.

First, we find the exact expression of E(𝑡+𝑛) (E(𝑡+𝑛))⊤:

𝑛∑︁−1

###### (1 − 𝛽)2𝑖Δ˜ (𝑡+𝑛−1−𝑖) (Δ˜ (𝑡+𝑛−1−𝑖) )⊤

E(𝑡+𝑛) (E(𝑡+𝑛) )⊤ = 𝛽2

𝑖=0

𝑛∑︁−1

(1 − 𝛽)𝑖 (1 − 𝛽)𝑗Δ˜ (𝑡+𝑛−1−𝑖) (Δ˜ (𝑡+𝑛−1−𝑖) )⊤.

+ 2𝛽2

𝑖,𝑗=0:𝑖≠𝑗

Notethat,for𝑖, 𝑗 ∈ {0, · · ·𝑛−1}(𝑖 ≠ 𝑗),E[Δ˜ (𝑡+𝑛−1−𝑖) (Δ˜ (𝑡+𝑛−1−𝑗))⊤]

= E[Δ˜ ](E[Δ˜ ])⊤, as we assume that they are uncorrelated. For 𝑖 ∈ {0, · · ·𝑛 − 1}, E[Δ˜ (𝑡+𝑛−1−𝑖) (Δ˜ (𝑡+𝑛−1−𝑖))⊤] = E[Δ˜ ](E[Δ˜ ])⊤ + Cov[Δ˜ ]. Thus,

E[E(𝑡+𝑛) (E(𝑡+𝑛) )⊤]

𝑛∑︁−1

###### (1 − 𝛽)2𝑖 E[Δ˜ ](E[Δ˜ ])⊤ + Cov[Δ˜ ]

= 𝛽2

𝑖=0

𝑛∑︁−1

(1 − 𝛽)𝑖 (1 − 𝛽)𝑗E[Δ˜ ](E[Δ˜ ])⊤,

+ 2𝛽2

𝑖,𝑗=0:𝑖≠𝑗

𝑛∑︁−1

(1 − 𝛽)2𝑖 Cov[Δ˜ ].

= E[E(𝑡+𝑛) ](E[E(𝑡+𝑛) ])⊤ + 𝛽2

𝑖=0

Therefore,

Cov[E(𝑡+𝑛) ] = E[E(𝑡+𝑛) (E(𝑡+𝑛) )⊤] − E[[E(𝑡+𝑛) ]([E(𝑡+𝑛) ])⊤

𝑛∑︁−1

(1 − 𝛽)2𝑖 Cov[Δ˜ ].

= 𝛽2

𝑖=0

Here,

𝑛∑︁−1

1 − (1 − 𝛽)2𝑛 1 − (1 − 𝛽)2

1 − (1 − 𝛽)2𝑛 𝛽(2 − 𝛽)

(1 − 𝛽)2𝑖 =

=

.

𝑖=0

Thus, by ignoring (1 − 𝛽)2𝑛, we can approximate Cov[E(𝑡+𝑛)] as follows:

𝛽 2 − 𝛽

Cov[Δ˜ ],

Cov[E(𝑡+𝑛) ] = [1 − (1 − 𝛽)2𝑛]

𝛽 2 − 𝛽

Cov[Δ˜ ].

≈

Therefore, E(𝑡+𝑛) approximately follows the distribution

𝛽 2 − 𝛽

E(𝑡+𝑛) ∼ D E[Δ˜ ],

Cov[Δ˜ ] .

This completes the derivation of Eq. (12).

### A.2 Derivation of Estimates for ∥E[Δ˜ ]∥22

We organize the relation between E and Δ˜ by the following equation:

E[∥E∥22] = E[E]⊤𝐼E[E] + Tr(Cov[E]) ≈ ∥E[Δ˜ ]∥22 + Tr

𝛽 2 − 𝛽

Cov[Δ˜ ]

𝛽 2 − 𝛽

Tr(Cov[Δ˜ ]).

= ∥E[Δ˜ ]∥22 +

Now we apply the same arguments to V and obtain

###### E[V] = [1 − (1 − 𝛽)𝑡+1]E[∥Δ˜ ∥22]

≈ E[∥Δ˜ ∥22] = ∥E[Δ˜ ]∥22 + Tr(Cov[Δ˜ ]). By reorganizing these arguments, we obtain

2 − 𝛽 2 − 2𝛽

𝛽 2 − 2𝛽

∥E[Δ˜ ]∥22 ≈

E[∥E∥22] −

###### E[V].

This gives the rationale of the estimates 22−−2𝛽𝛽 ∥E∥22 − 2−𝛽2𝛽 V for ∥E[Δ˜ ]∥22.

### B ADDITIONAL EXPERIMENT RESULTS

Figure 8 shows the success rate and SP1 results with respect to 𝛽Σ ∈ {0.01, 0.02, ..., 0.05} on the 30-D noiseless Sphere, Schaffer, and Rastrigin functions. Clearly, the performance was not significantly affected by 𝛽Σ values within this range. However, similar to the case shown in Figure 7, an excessively small 𝛽Σ setting decelerated the convergence for the Rastrigin function.

Figures 9 and 10 show the success rate and SP1 values with respect to 𝛽𝑚 and 𝛾, respectively. The results show that the performance was relatively stable against these hyperparameters.

βΣ vs. Success Rate and SP1 (d = 30,30 trials)

Sphere

Schaﬀer

Rastrigin

SP1SuccessRate

| | | | | | | |
|---|---|---|---|---|---|---|
| | | | | | | |
| | | | | | | |
| | | | | | | |


| | | | | | | |
|---|---|---|---|---|---|---|
| | | | | | | |
| | | | | | | |
| | | | | | | |


| | | | | | | |
|---|---|---|---|---|---|---|
| | | | | | | |
| | | | | | | |
| | | | | | | |


1.0

1.0

1.0

0.5

0.5

0.5

0.0

0.0

0.0

0.01 0.02 0.03 0.04 0.05

0.01 0.02 0.03 0.04 0.05

0.01 0.02 0.03 0.04 0.05

- 104
- 105


- 105
- 106


- 105
- 106


| | | | | | | |
|---|---|---|---|---|---|---|
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |


| | | | | | | |
|---|---|---|---|---|---|---|
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |


| | | | | | | |
|---|---|---|---|---|---|---|
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |


0.01 0.02 0.03 0.04 0.05

0.01 0.02 0.03 0.04 0.05

0.01 0.02 0.03 0.04 0.05

##### Figure 8: Success rate and SP1 versus hyperparameter 𝛽Σ ∈ {0.01, 0.02, ..., 0.05} on 30-D noiseless problems.

βm vs. Success Rate and SP1 (d = 30,30 trials)

Sphere

Schaﬀer

Rastrigin

SP1SuccessRate

| | | | | | | |
|---|---|---|---|---|---|---|
| | | | | | | |
| | | | | | | |
| | | | | | | |


| | | | | | | |
|---|---|---|---|---|---|---|
| | | | | | | |
| | | | | | | |
| | | | | | | |


| | | | | | | |
|---|---|---|---|---|---|---|
| | | | | | | |
| | | | | | | |
| | | | | | | |


1.0

1.0

1.0

0.5

0.5

0.5

0.0

0.0

0.0

0.05 0.10 0.15 0.20 0.25

0.05 0.10 0.15 0.20 0.25

0.05 0.10 0.15 0.20 0.25

- 104
- 105


- 105
- 106


- 105
- 106


| | | | | | | |
|---|---|---|---|---|---|---|
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |


| | | | | | | |
|---|---|---|---|---|---|---|
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |


| | | | | | | |
|---|---|---|---|---|---|---|
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |


0.05 0.10 0.15 0.20 0.25

0.05 0.10 0.15 0.20 0.25

0.05 0.10 0.15 0.20 0.25

##### Figure 9: Success rate and SP1 versus hyperparameter 𝛽𝑚 on 30-D noiseless problems.

γ vs. Success Rate and SP1 (d = 30,30 trials)

Sphere

Schaﬀer

Rastrigin

SP1SuccessRate

| | | | | | | |
|---|---|---|---|---|---|---|
| | | | | | | |
| | | | | | | |
| | | | | | | |


| | | | | | | |
|---|---|---|---|---|---|---|
| | | | | | | |
| | | | | | | |
| | | | | | | |


| | | | | | | |
|---|---|---|---|---|---|---|
| | | | | | | |
| | | | | | | |
| | | | | | | |


1.0

1.0

1.0

0.5

0.5

0.5

0.0

0.0

0.0

0.05 0.10 0.15 0.20 0.25

0.05 0.10 0.15 0.20 0.25

0.05 0.10 0.15 0.20 0.25

- 104
- 105


- 105
- 106


- 105
- 106


| | | | | | | |
|---|---|---|---|---|---|---|
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |


| | | | | | | |
|---|---|---|---|---|---|---|
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |


| | | | | | | |
|---|---|---|---|---|---|---|
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |


0.05 0.10 0.15 0.20 0.25

0.05 0.10 0.15 0.20 0.25

0.05 0.10 0.15 0.20 0.25

##### Figure 10: Success rate and SP1 versus hyperparameter 𝛾 on 30-D noiseless problems.

