---
type: source
kind: paper
title: CMA-ES with Learning Rate Adaptation
authors: Masahiro Nomura, Youhei Akimoto, Isao Ono
year: 2024
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/2401.15876v2
source_local: ../raw/2024-nomura-cma-es-learning-rate-adaptation.pdf
ingested_for_concept: cma-es-with-warmstart.md
cites:
  - ../wiki/concepts/cma-es-with-warmstart.md
  - ../wiki/problems/9-*.md
  - ../wiki/problems/15-*.md
  - ../wiki/problems/16-*.md
---

# arXiv:2401.15876v2[cs.NE]26Sep2024

## CMA-ES with Learning Rate Adaptation

## 1

MASAHIRO NOMURA∗, Tokyo Institute of Technology, Japan YOUHEI AKIMOTO, University of Tsukuba & RIKEN AIP, Japan ISAO ONO, Tokyo Institute of Technology, Japan

The covariance matrix adaptation evolution strategy (CMA-ES) is one of the most successful methods for solving continuous black-box optimization problems. A practically useful aspect of CMA-ES is that it can be used without hyperparameter tuning. However, the hyperparameter settings still have a considerable impact on performance, especially for difficult tasks, such as solving multimodal or noisy problems. This study comprehensively explores the impact of learning rate on CMA-ES performance and demonstrates the necessity of a small learning rate by considering ordinary differential equations. Thereafter, it discusses the setting of an ideal learning rate. Based on these discussions, we develop a novel learning rate adaptation mechanism for CMA-ES that maintains a constant signal-to-noise ratio. Additionally, we investigate the behavior of CMA-ES with the proposed learning rate adaptation mechanism through numerical experiments and compare the results with those obtained for CMA-ES with a fixed learning rate and with population size adaptation. The results show that CMA-ES with the proposed learning rate adaptation works well for multimodal and/or noisy problems without extremely expensive learning rate tuning.

CCS Concepts: • Mathematics of computing → Continuous optimization. Additional Key Words and Phrases: covariance matrix adaptation evolution strategy, black-box optimization, learning rate adaptation ACM Reference Format: Masahiro Nomura, Youhei Akimoto, and Isao Ono. 2024. CMA-ES with Learning Rate Adaptation. ACM Trans. Evol. Learn. 1, 1, Article 1 (January 2024), 28 pages. https://doi.org/10.1145/3698203

### 1 INTRODUCTION

The covariance matrix adaptation evolution strategy (CMA-ES) [Hansen 2016; Hansen and Ostermeier 2001] is among the most successful methods available for solving continuous black-box optimization problems; its effectiveness has been confirmed through various real-world applications [Fujii et al. 2018; Ha and Schmidhuber 2018; Huang et al. 2022; Kikuchi et al. 2021a,b; Maki et al. 2020; Nomura et al. 2021; Piergiovanni et al. 2020; Purucker and Beel 2023; Tanabe et al. 2021; Tian et al. 2023; Volz et al. 2018]. CMA-ES performs optimization by updating the multivariate Gaussian distribution; that is, it first samples candidate solutions from the distribution and then updates the distribution parameters (i.e., the mean vector 𝑚 and covariance matrix Σ = 𝜎2𝐶) based on the objective function 𝑓 . This update is partly based on the natural gradient descent [Akimoto et al. 2010; Ollivier et al. 2017] of the expected 𝑓 , and 𝑚 and 𝐶 in CMA-ES are updated to reduce the expected

∗Corresponding author

Authors’ addresses: Masahiro Nomura, nomura.m.ad@m.titech.ac.jp, Tokyo Institute of Technology, 4259 Nagatsutacho,¯ Midori Ward, Yokohama, Kanagawa, Japan, 226-0026; Youhei Akimoto, akimoto@cs.tsukuba.ac.jp, University of Tsukuba & RIKEN AIP, 1-1-1 Tennodai, Tsukuba, Ibaraki, Japan, 305-8573; Isao Ono, isao@c.titech.ac.jp, Tokyo Institute of Technology, 4259 Nagatsutacho,¯ Midori Ward, Yokohama, Kanagawa, Japan, 226-0026.

Permission to make digital or hard copies of all or part of this work for personal or classroom use is granted without fee provided that copies are not made or distributed for profit or commercial advantage and that copies bear this notice and the full citation on the first page. Copyrights for components of this work owned by others than the author(s) must be honored. Abstracting with credit is permitted. To copy otherwise, or republish, to post on servers or to redistribute to lists, requires prior specific permission and/or a fee. Request permissions from permissions@acm.org.

© 2024 Copyright held by the owner/author(s). Publication rights licensed to ACM. 2688-3007/2024/1-ART1 $15.00 https://doi.org/10.1145/3698203

evaluation value. CMA-ES is practically useful as it is a quasi-hyperparameter-free algorithm; practitioners can use it without hyperparameter tuning because default values are provided for all hyperparameters through theoretical analysis and extensive empirical evaluations. Specifically, the hyperparameter values are automatically computed using dimension 𝑑 and population size 𝜆, where 𝜆 = 4 + ⌊3ln(𝑑)⌋ by default.

Although the default 𝜆 value works well for various unimodal problems, increasing it can help solve difficult tasks, such as solving multimodal and additive noise problems [Hansen and Kern 2004; Nishida and Akimoto 2016, 2018]. However, in a black-box scenario, determining the problem structure of 𝑓 is challenging. Thus, determining the appropriate 𝜆 value in advance is also challenging, and online adaptation of 𝜆 has been proposed to address the issue [Hellwig and Beyer 2016; Nguyen and Hansen 2017; Nishida and Akimoto 2016, 2018]. Population size adaptation (PSA)-CMA-ES [Nishida and Akimoto 2018] is a representative 𝜆 adaptation mechanism that has exhibited promising performance for difficult tasks, including multimodal and additive noise problems.

It has been observed that, in CMA-ES, increasing 𝜆 has an effect similar to decreasing the 𝑚 learning rate, that is, 𝜂𝑚 [Miyazawa and Akimoto 2017]1. Indeed, the 𝑚 and Σ learning rates, that is, 𝜂, is another hyperparameter that critically affects performance. An excessively large 𝜂 value results in unstable parameter updates, whereas an excessively small value degrades search efficiency. Miyazawa and Akimoto [Miyazawa and Akimoto 2017] reported that CMA-ES with even a relatively small 𝜆 (e.g., 𝜆 = √

𝑑) solves multimodal problems through an appropriate setting of 𝜂. However, determining the appropriate 𝜂 value is difficult in practice because prior knowledge is often limited and hyperparameter tuning entails expensive numerical investigations.

Therefore, online adaptation of 𝜂 based on the problem difficulty constitutes an important advancement as it will allow practitioners to safely use CMA-ES without requiring prior knowledge or expensive trial-and-error calculations. In particular, we believe that 𝜂 adaptation is more advantageous than 𝜆 adaptation from a practical perspective because the former is more suitable for parallel implementations. For example, practitioners often wish to specify a certain number of workers as the value of 𝜆 value to avoid wasting computational resources. However, 𝜆 adaptation may not always effectively utilize the available resources, as the values vary during the optimization process. By contrast, 𝜂 adaptation allows complete exploitation of the available resources because the value of 𝜆 is fixed as the maximum number of workers. Moreover, in 𝜂 adaptation, the parameters are regularly updated, whereas CMA-ES with 𝜆 adaptation does not progress until all 𝜆 solutions are evaluated, making it difficult to determine the search termination point.

Although online 𝜂 adaptation itself is not new and several studies have attempted to adapt 𝜂

values in CMA-ES variants, these adaptations targeted speed-up [Gissler et al. 2022; Loshchilov et al. 2014; Nomura and Ono 2022]. One notable exception is the𝜂 adaptation proposed by Krause [Krause 2019] that aims to solve additive noise problems through new evolution strategies. However, it estimates the problem difficulty through resampling, that is, by repeatedly evaluating the same solution; thus, it is not suitable for solving (noiseless) multimodal problems. Furthermore, as it involves significant modifications of the internal parameters of the evolution strategies, applying it directly to CMA-ES is challenging.

This study aimed to develop CMA-ES to solve multimodal and additive noise problems without extremely expensive 𝜂 tuning or adjusting any other CMA-ES parameters except 𝜂. To achieve this, we first examined the impact of learning rate. Our results suggest that (i) difficult problems can be relatively easily solved by decreasing the learning rate and aligning the parameter behavior

1Note that, in Ref. [Miyazawa and Akimoto 2017], the rank-one update was excluded from CMA-ES. In this study, however, we consider CMA-ES including the rank-one update.

with the trajectory of an ordinary differential equation (ODE), and (ii) the optimal learning rate is approximately proportional to the signal-to-noise ratio (SNR). Based on these observations, we propose an 𝜂 adaptation mechanism for CMA-ES—called the learning rate adaptation (LRA)—that adapts 𝜂 to maintain a constant SNR. The key feature of the proposed method is that it does not require specific knowledge of the internal mechanism of the distribution-parameter update to estimate the SNR. Consequently, the proposed method is widely applicable to various CMA-ES variants, such as diagonal decoding (dd)-CMA [Akimoto and Hansen 2020], even though this study considers the most commonly used CMA-ES, which combines weighted recombination, step-size 𝜎 adaptation, rank-one update, and rank-𝜇 update.

It should be noted that our work focuses on well-structured multimodal problems rather than weakly structured ones, as in the previous studies on 𝜆 adaptation in CMA-ES [Nishida and Akimoto 2018]. Using our method alone cannot solve the weakly structured multimodal problems and may even be detrimental to these problems. To address such problems, we believe the integration of restart strategies (e.g., BIPOP-CMA-ES [Hansen 2009]) is necessary, which is beyond this study; thus, we have left it for future work.

This study extends a previous study [Nomura et al. 2023] as follows: In Section 3.2, we illustrate from an ODE perspective the reason why a small learning rate is essential for solving difficult problems. Thereafter, we discuss the optimal learning rate in Section 3.3, which indicates that the proposed method adapts the learning rate to a nearly optimal value. It should be noted that Section 3 presents entirely new information that was not included in the previous study [Nomura et al. 2023]. Thereafter, the performance differences for various 𝜆 values are discussed in Section 5.5. Finally, Section 5.6 presents a comprehensive comparison of LRA-CMA-ES and PSA-CMA-ES [Nishida and Akimoto 2018], a state-of-the-art 𝜆 adaptation method.

The remainder of this paper is organized as follows: Section 2 explains the CMA-ES algorithm and the information-geometric optimization (IGO) framework. Section 3 closely examines and explains the impact of the learning rate and presents the discussion for determining the ideal learning rate. Section 4 presents the proposed 𝜂 adaptation mechanism based on SNR estimation. Section 5 evaluates the performance of the proposed 𝜂 adaptation for noiseless and noisy problems. Finally, Section 6 concludes the paper and suggests future research directions.

2 BACKGROUND

- 2.1 CMA-ES


We consider minimizing the objective function 𝑓 : R𝑑 → R. CMA-ES employs a multivariate Gaussian distribution to generate candidate solutions, where the distribution N(𝑚,𝜎2𝐶) is parameterized through three elements: mean vector 𝑚 ∈ R𝑑, step-size 𝜎 ∈ R>0, and covariance matrix 𝐶 ∈ R𝑑×𝑑.

CMA-ES first initializes the 𝑚(0),𝜎(0), and 𝐶(0) parameters. Thereafter, the following steps are repeated until a predefined stopping criterion is met.

### Step 1. Sampling and Evaluation

At iteration 𝑡 + 1 (where 𝑡 begins at 0), 𝜆 candidate solutions 𝑥𝑖 (𝑖 = 1, 2, · · · ,𝜆) are sampled independently from N(𝑚(𝑡), (𝜎(𝑡))2𝐶(𝑡)), as follows:

𝑦𝑖 = √︁𝐶(𝑡)𝑧𝑖, (1) 𝑥𝑖 = 𝑚(𝑡) + 𝜎(𝑡)𝑦𝑖, (2)

where 𝑧𝑖 ∼ N(0,𝐼) and 𝐼 is the identity matrix. The solutions are evaluated on 𝑓 and sorted in ascending order. Let𝑥𝑖:𝜆 be the𝑖-th best candidate solution, that is, 𝑓 (𝑥1:𝜆) ⩽ 𝑓 (𝑥2:𝜆) ⩽ · · · ⩽ 𝑓 (𝑥𝜆:𝜆) for minimization. In addition, we let𝑦𝑖:𝜆 and 𝑧𝑖:𝜆 be the intermediate vectors in Equations (1) and (2) corresponding to 𝑥𝑖:𝜆.

### Step 2. Compute Evolution Paths

The weighted averages 𝑑𝑦 = 𝑖 𝜇=1𝑤𝑖𝑦𝑖:𝜆 and 𝑑𝑧 = 𝑖 𝜇=1𝑤𝑖𝑧𝑖:𝜆 of the intermediate vectors are calculated using the parent number 𝜇 ⩽ 𝜆 and weight function 𝑤𝑖, where 𝑖 𝜇=1𝑤𝑖 = 1. The evolution paths are updated as follows:

𝑝𝜎(𝑡+1) = (1 − 𝑐𝜎)𝑝𝜎(𝑡) + √︁𝑐𝜎(2 − 𝑐𝜎)𝜇𝑤𝑑𝑧, (3) 𝑝𝑐(𝑡+1) = (1 − 𝑐𝑐)𝑝𝑐(𝑡) + ℎ𝜎(𝑡+1)√︁𝑐𝑐(2 − 𝑐𝑐)𝜇𝑤𝑑𝑦, (4)

where 𝜇𝑤 = 1/ 𝑖 𝜇=1𝑤𝑖2, 𝑐𝜎, and 𝑐𝑐 are the cumulation factors, and ℎ𝜎(𝑡+1) is the Heaviside function, which is defined as follows [Hansen and Auger 2014]:

1 if ∥𝑝𝜎(𝑡+1)∥2

1−(1−𝑐𝜎)2(𝑡+1) < 2 + 𝑑4+1 𝑑, 0 otherwise.

ℎ𝜎(𝑡+1) =

(5)

##### Step 3. Update Distribution Parameters The distribution parameters are updated as follows [Hansen and Auger 2014]:

𝑚(𝑡+1) = 𝑚(𝑡) + 𝑐𝑚𝜎(𝑡)𝑑𝑦, (6) 𝜎(𝑡+1) = 𝜎(𝑡) exp min 1,

#### ∥𝑝𝜎(𝑡+1)∥ E[∥N(0,𝐼)∥]

𝑐𝜎 𝑑𝜎

− 1 , (7)

𝐶(𝑡+1) = 1 + (1 − ℎ𝜎(𝑡+1))𝑐1𝑐𝑐(2 − 𝑐𝑐) 𝐶(𝑡)

(8)

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

√

𝑑 1 − 41𝑑 + 211𝑑2 denotes the expected Euclidean norm of the sample of a standard normal distribution and 𝑐𝑚 is the learning rate for 𝑚, which is typically set to 1. 𝑐1 and 𝑐𝜇 are the learning rates for the rank-one and -𝜇 updates of 𝐶, respectively, and 𝑑𝜎 is the damping factor for the 𝜎 adaptation.

where E[∥N(0,𝐼)∥] ≈

### 2.2 IGO

The IGO [Ollivier et al. 2017] framework is a unified framework for stochastic search methods. Given a family of probability distributions parameterized by 𝜃 ∈ Θ, the original objective function 𝑓 is transformed into a new objective function 𝐽𝜃 that is defined in the distribution-parameter space Θ.

For the family of Gaussian distributions, the IGO algorithms recover the pure rank-𝜇-update CMA-ES, eliminating the 𝜎 adaptation and rank-one update from the procedures in Section 2.1. To investigate the effects of learning rates on CMA-ES, we focus on their properties within the context of the IGO framework with a family of Gaussian distributions in Section 3. This section presents the background of the IGO framework.

Instead of minimizing the original objective 𝑓 over the input domain R𝑑, IGO maximizes a new objective 𝐽𝜃 over the distribution-parameter domain Θ. Let 𝑢 : [0, 1] → R be a bounded, non-increasing function, and 𝑃𝜃 be the Lebesgue measure on R𝑑 corresponding to the probability density 𝑝(𝑥;𝜃). We define the utility function𝑊𝜃𝑓 as

𝑊𝜃𝑓 (𝑥) = 𝑢(𝑞𝜃 (𝑥)), (9)

where 𝑞𝜃 (𝑥) is the quantile function that is defined as 𝑞𝜃 (𝑥) := 𝑃𝜃 [𝑦 : 𝑓 (𝑦) ⩽ 𝑓 (𝑥)] for minimization. The objective updating 𝜃, given the current distribution parameters 𝜃(𝑡), is defined as the

expectation of the weighted quantile function𝑊𝜃𝑓(𝑡) (𝑥) over 𝑝(𝑥;𝜃): 𝐽𝜃(𝑡) (𝜃) = E𝑥∼𝑝(𝑥;𝜃)[𝑊𝜃𝑓(𝑡) (𝑥)]. (10)

The objective 𝐽𝜃(𝑡) (𝜃) is maximized based on the natural gradient [Amari and Douglas 1998; Amari and Nagaoka 2000]. By using the “log-likelihood trick” under some mild conditions, the vanilla gradient can be calculated as

∇𝜃 𝐽𝜃(𝑡) (𝜃) = E𝑥∼𝑝(𝑥;𝜃)[𝑊𝜃𝑓(𝑡) (𝑥)∇𝜃 ln𝑝(𝑥;𝜃)]. (11) The natural gradient is obtained through the product of the inverse of the Fisher information matrix 𝐹 at 𝜃(𝑡) and the vanilla gradient as follows:

∇˜𝜃 𝐽𝜃(𝑡) (𝜃) = E𝑥∼𝑝(𝑥;𝜃)[𝑊𝜃𝑓(𝑡) (𝑥)∇˜𝜃 ln𝑝(𝑥;𝜃)], (12) where ∇˜𝜃 ln𝑝(𝑥;𝜃) = 𝐹−1∇𝜃 ln𝑝(𝑥;𝜃).

In practice, the integral cannot be calculated in a closed form and is therefore estimated using the Monte Carlo method as follows:

#### ∑︁𝜆

1 𝜆

𝑊𝜃𝑓(𝑡) (𝑥𝑖)∇˜𝜃 ln𝑝(𝑥𝑖;𝜃), (13)

∇˜𝜃 𝐽𝜃(𝑡) (𝜃) ≈

𝑖=1

where {𝑥𝑖}𝑖𝜆=1 are 𝜆 i.i.d. samples obtained from probability distribution 𝑝(𝑥𝑖;𝜃). The IGO algorithms implement the IGO framework using the estimated natural gradient, whose updated equation is as

follows:

∑︁𝜆

𝑊𝜃𝑓(𝑡) (𝑥𝑖) 𝜆

∇˜𝜃 ln𝑝(𝑥𝑖;𝜃(𝑡)), (14)

𝜃(𝑡+1) = 𝜃(𝑡) + 𝜂

𝑖=1

where 𝜂 denotes the learning rate. In practice,𝑊𝜃𝑓(𝑡) (𝑥𝑖) is also estimated based on the ranking of {𝑥𝑖}𝑖𝜆=1.

As elucidated herein, the IGO framework, with a family of Gaussian distributions, recovers the rank-𝜇-update CMA-ES [Akimoto et al. 2010; Ollivier et al. 2017]. If the distribution parameter 𝜃 = (𝑚⊤, vec(𝐶)⊤)⊤, then [Akimoto et al. 2010]:

𝑥 −𝑚 vec((𝑥 −𝑚)(𝑥 −𝑚)⊤ −𝐶)

∇˜𝜃 ln𝑝(𝑥;𝜃) =

. (15) Thus, Eq. (14) can be rewritten as

#### ∑︁𝜆

𝑊𝜃𝑓(𝑡) (𝑥𝑖) 𝜆 (𝑥𝑖 −𝑚(𝑡)), (16)

𝑚(𝑡+1) = 𝑚(𝑡) + 𝜂

𝑖=1

#### ∑︁𝜆

𝑊𝜃𝑓(𝑡) (𝑥𝑖)

𝐶(𝑡+1) = 𝐶(𝑡) + 𝜂

𝜆 (𝑥𝑖 −𝑚(𝑡))(𝑥𝑖 −𝑚(𝑡))⊤ −𝐶(𝑡) . (17) Consequently, by ignoring the 𝜎 adaptation and rank-one update in CMA-ES, assuming 𝑐𝑚 = 𝑐𝜇(:= 𝜂), and considering that 𝑤𝑖 in CMA-ES is an approximation of𝑊𝜃𝑓(𝑡) (𝑥𝑖)/𝜆 in the IGO update, the 𝑚 and 𝐶 updates through the IGO algorithm (Eqs. (16) and (17), respectively) align with those of CMA-ES (Eqs. (6) and (8), respectively).

𝑖=1

### 3 LEARNING RATE IMPACT

In this section, we discuss the impact of the learning rate on CMA-ES. First, Section 3.1 summarizes existing research on adjusting the population size, which is a common practice for difficult tasks, such as multimodal problems, and the relation between the population size and learning rate. In Section 3.2, we discuss the behavior from the perspective of ODEs for small learning rates. Consequently, we demonstrate that difficult problems can be solved by reducing the learning rate (i.e., closer to the solution of the ODE). However, it should be noted that an excessively small learning rate can reduce the search efficiency. Therefore, Section 3.3 discusses the determination of the optimal learning rate.

### 3.1 Relation Between Population Size and Learning Rate

Previous studies generally focused on increasing the population size 𝜆 to solve multimodal problems. Hansen and Kern [2004] reported that CMA-ES with a sufficiently large population size can often solve multimodal problems with high probability. Based on this observation, Auger and Hansen [2005] proposed IPOP-CMA-ES, which doubles the population size with each restart. Although these studies considered CMA-ES with default learning rates, Miyazawa and Akimoto [2017] experimentally evaluated the performance of CMA-ES using small learning rates and showed that multimodal problems, such as the Rastrigin function, can be solved by setting sufficiently small learning rates without using a large population size. This empirical observation suggests that the effect of increasing the population size is similar to that of decreasing the learning rate.

Here, we organize the relation between the population size and learning rate more formally. First, we examine the relation based on the results of quality gain analysis. For the infinite-dimensional Sphere function, the optimal value of the normalized step-size 𝜎¯∗, whose normalized step-size is

defined as 𝜎¯ := 𝜎𝜂𝑚𝑑/∥𝑚−𝑥∗∥ = O(𝜎𝜂𝑚), is 𝜎¯∗ = −𝜇𝑤 𝑖 𝜆=1𝑤𝑖E[N𝑖:𝜆] ≈ √︁2/𝜋𝜆 ∈ O(𝜆) [Akimoto et al. 2020; Arnold 2005]. Hence, the optimal step-size is 𝜎∗ ∈ O(𝜆/𝜂𝑚), which clearly demonstrates that increasing 𝜆 corresponds to decreasing 𝜂𝑚. In other words, as the population size increases or learning rate decreases, the optimal step-size increases. Miyazawa and Akimoto [2017] hypothesized that CMA-ES with small learning rates can solve multimodal problems owing to the effect of maintaining a large step-size.

Next, we offer another characterization of the relation between the population size and the learning rate, by viewing IGO algorithms as discretizations of stochastic differential equations (SDEs) [Jastrzębski et al. 2017]. For conciseness, we define 𝑔(𝜃) := E𝑥∼𝑝(𝑥;𝜃)[𝑊𝜃𝑓 (𝑥)∇˜𝜃 ln𝑝(𝑥;𝜃)] and let its Monte Carlo estimation𝑔ˆ(𝜆)(𝜃) := (1/𝜆) 𝑖 𝜆=1𝑔ˆ𝑖(𝜃), where𝑔ˆ𝑖(𝜃) := 𝑊𝜃𝑓 (𝑥𝑖)∇˜𝜃 ln𝑝(𝑥𝑖;𝜃), where 𝑔ˆ𝑖(𝜃) is an unbiased estimator of 𝑔(𝜃). Note that, in practice, 𝑊𝜃𝑓 must also be estimated using the Monte Carlo method; thus, 𝑔ˆ𝑖(𝜃) does not necessarily provide an unbiased estimation of 𝑔(𝜃). However, we assume the availability of𝑊𝜃𝑓 for this discussion. Subsequently, we denote the covariance of 𝑔ˆ𝑖(𝜃) as 𝑆(𝜃). By using this notation, the IGO update in Eq.(14) can be written as 𝜃(𝑡+1) = 𝜃(𝑡) + 𝜂𝑔ˆ(𝜆)(𝜃(𝑡)). Given a sufficiently large population size 𝜆, the following is valid according to the central limit theorem:

𝑔ˆ(𝜆)(𝜃) ∼ N 𝑔(𝜃),

1 𝜆

𝑆(𝜃) . (18)

Based on this result, we can rewrite Eq.(14) as follows:

𝜃(𝑡+1) = 𝜃(𝑡) + 𝜂𝑔(𝜃(𝑡)) + 𝜂(𝑔ˆ(𝜆)(𝜃(𝑡)) − 𝑔(𝜃(𝑡))), (19)

| | | | | | | | |
|---|---|---|---|---|---|---|---|
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |


−3 −2 −1 0 1 2 3

Fig. 1. Rastrigin function.

where 𝑔ˆ(𝜆)(𝜃(𝑡)) −𝑔(𝜃(𝑡)) ∼ N(0, (1/𝜆)𝑆(𝜃)). Hence, using the newly introduced random variable 𝜖𝜃 ∼ N(0,𝑆(𝜃)), the IGO update can be rewritten as follows:

𝜂 √

𝜃(𝑡+1) = 𝜃(𝑡) + 𝜂𝑔(𝜃(𝑡)) +

𝜖𝜃(𝑡) . (20) Consequently, we consider the following SDE:

𝜆

√︂𝜂 𝜆

𝑅(𝜃)𝑑𝑊 (𝑡), (21)

𝑑𝜃 = 𝑔(𝜃)𝑑𝑡 +

where 𝑅(𝜃)𝑅(𝜃)⊤ = 𝑆(𝜃) and {𝑊 (𝑡)} is the standard Wiener process. By discretizing the SDE using the Euler–Maruyama method [Kloeden et al. 1992], with the learning rate 𝜂, we obtain an equation identical to Eq. (20). Therefore, from the SDE perspective, the learning rate and the population size appear only in the form of the ratio 𝜂/𝜆, which implies that the effect of increasing 𝜆 is similar to that of decreasing 𝜂.

In summary, although previous studies primarily adjusted the population size for solving multimodal problems, we empirically and theoretically observed that increasing the population size and decreasing the learning rate have similar effects on the optimal step-size and noise.

### 3.2 Effect of Decreasing the Learning Rate from an ODE Perspective

When the learning rate approaches zero, the IGO algorithm is reduced to the following ODE [Akimoto et al. 2022]:

𝑑𝜃 𝑑𝑡

= E𝑥∼𝑝(𝑥;𝜃)[𝑊𝜃𝑓 (𝑥)∇˜𝜃 ln𝑝(𝑥;𝜃)]. (22) To illustrate the algorithm behavior from an ODE perspective, we consider minimizing the 1dimensional Rastrigin function 𝑓Rastrigin(𝑥) = 10 + 𝑥2 − 10cos(2𝜋𝑥), which is a well-structured multimodal problem (Fig. 1). Assuming that𝑊𝜃𝑓 = −𝑓 and parameterizing our Gaussian distribution using 𝜃 = (𝑚,𝑣), where 𝑚 is the mean and 𝑣 is the variance, the ODEs are calculated as follows:

𝑑𝑚 𝑑𝑡

= −2𝑚𝑣 − 20𝜋𝑣 sin(2𝜋𝑚) exp(−2𝜋2𝑣), (23)

𝑑𝑣 𝑑𝑡

= −2𝑣2 − 40𝜋2𝑣2 cos(2𝜋𝑚) exp(−2𝜋2𝑣). (24)

Figure 2 shows the ODE trajectories and gradient flows of the Rastrigin function. The experiments were conducted using initial distribution parameters 𝑚 = 3.0 and 𝑣 ∈ [0.02, 2.0]. It is evident that ODEs with large initial variances exhibit trajectories converging to the optimal solution (𝑚∗,𝑣∗) =

- (0, 0). Given that the algorithm behavior tends to approach the trajectory of the corresponding


Trajectory and gradient ﬂow on Rastrigin

| | | | | | | | |
|---|---|---|---|---|---|---|---|
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |


2.00

1.75

1.50

1.25

variance

1.00

0.75

0.50

0.25

0.00

0.0 0.5 1.0 1.5 2.0 2.5 3.0

mean

Trajectory with various learning rates

| |ODE solution<br><br>η = 10−5 η = 10−4 η = 10−3 η = 10−2<br><br>| | | | | | |
|---|---|---|---|---|---|---|---|
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |


2.5

2.0

variance

1.5

1.0

0.5

0.0

0.0 0.5 1.0 1.5 2.0 2.5 3.0

mean

Fig. 2. ODE trajectories and gradient flows of the Rastrigin function. The different colors (red, orange, yellow-orange, and yellow) of the ODE trajectories indicate different attractors.

Fig. 3. Typical parameter trajectories of the Rastrigin function under various learning rates (𝜂 = 10−5, 10−4, 10−3, 10−2). The ODE solution (black) is also illustrated for reference.

ODE, as the learning rate decreases, we hypothesize that such multimodal problems can be solved by adequately decreasing the learning rate and employing a sufficiently large variance.

To verify this hypothesis, we evaluated the behavior of the distribution parameters for various learning rates. For this, we employed the following discretized versions of Eq. (23) and (24) using the Euler method:

𝑚(𝑡+1) = 𝑚(𝑡) − 𝜂(2𝑚𝑣 + 20𝜋𝑣 sin(2𝜋𝑚) exp(−2𝜋2𝑣)), (25) 𝑣(𝑡+1) = 𝑣(𝑡) − 𝜂(2𝑣2 + 40𝜋2𝑣2 cos(2𝜋𝑚) exp(−2𝜋2𝑣)), (26)

where 𝜂 denotes the learning rate; we used 𝜂 values of 10−5, 10−4, 10−3, and 10−2. The initial distribution parameters were set as (𝑚,𝑣) = (3.0, 2.0). Figure 3 shows the typical behaviors of the parameter trajectories for various learning rates. It is evident that as the learning rate decreases, the corresponding trajectory approaches the ODE solution, which is also evident from the design of the Euler method. However, as the learning rate increases, the trajectory deviates from the ODE trajectory and tends to become trapped in the local optima, failing to find the optimal solution. These findings suggest the importance of setting a small learning rate for multimodal problems that can be solved by moving the distribution parameters along the ODE trajectory.

Although earlier discussions focused on multimodal problems, we believe that decreasing the learning rate is equally important for problems with unbiased additive noise, represented as 𝑓 (𝑥)+𝜖, where 𝜖 is an unbiased random variable, that is, E[𝜖] = 0. This is because, in cases with unbiased noise, the corresponding ODE remains unchanged compared with noiseless ones. That is, by decreasing the learning rate and aligning the parameter updates with the corresponding ODE trajectory, the distribution-parameter value can be guided closer to the optimal solution.

### 3.3 Optimal Learning Rate

Although setting a small learning rate can be beneficial for solving multimodal and noisy problems, as discussed in Section 3.2, using an excessively small value can result in slow convergence. In this section, we explore the optimal value of the learning rate.

For simplicity, we consider the minimization of E[𝑓 (𝑥)] = ∫ 𝑓 (𝑥)𝑝(𝑥;𝜃)𝑑𝑥 =: 𝐽 (𝜃) and assume that 𝐽 is twice differentiable. Additionally, we let Δ be an unbiased estimator of ∇˜ 𝐽 (𝜃). In this case,

the one-step update is 𝜃 − 𝜂 · Δ. Using the Taylor approximation, we obtain the following:

- 1

- 2


𝜂2Δ⊤𝐻Δ + 𝑜(𝜂2∥Δ∥2) (27) ≈ 𝐽 (𝜃) − 𝜂∇𝐽 (𝜃)⊤Δ +

𝐽 (𝜃 − 𝜂 · Δ) = 𝐽 (𝜃) − 𝜂∇𝐽 (𝜃)⊤Δ +

- 1

- 2


𝜂2Δ⊤𝐻Δ, (28)

where 𝐻 := ∇2𝐽 (𝜃). Considering the expectations over Δ, we obtain the following:

- 1

- 2


𝜂2 ∇ ˜ 𝐽 (𝜃)⊤𝐻∇˜ 𝐽 (𝜃) + Tr(𝐻 Cov[Δ]) . (29) Thereafter, the expected improvement is approximated as follows:

EΔ[𝐽 (𝜃 − 𝜂 · Δ)] ≈ 𝐽 (𝜃) − 𝜂∇𝐽 (𝜃)⊤∇˜ 𝐽 (𝜃) +

- 1

- 2


𝐽 (𝜃) − EΔ[𝐽 (𝜃 − 𝜂 · Δ)] ≈ 𝜂∇𝐽 (𝜃)⊤∇˜ 𝐽 (𝜃) −

𝜂2 ∇ ˜ 𝐽 (𝜃)⊤𝐻∇˜ 𝐽 (𝜃) + Tr(𝐻 Cov[Δ]) . (30)

By taking the derivative w.r.t. 𝜂 and solving it for zero, we approximate the optimal learning rate as follows:

∇𝐽 (𝜃)⊤∇˜ 𝐽 (𝜃) − 𝜂 ∇ ˜ 𝐽 (𝜃)⊤𝐻∇˜ 𝐽 (𝜃) + Tr(𝐻 Cov[Δ]) = 0 (31)

∇𝐽 (𝜃)⊤∇˜ 𝐽 (𝜃) ∇˜ 𝐽 (𝜃)⊤𝐻∇˜ 𝐽 (𝜃) + Tr(𝐻 Cov[Δ])

(32)

∴ 𝜂∗ ≈

= ∥∇˜ 𝐽 (𝜃)∥2𝐹 ∥∇˜ 𝐽 (𝜃)∥𝐻2 + Tr(𝐻 Cov[Δ])

, (33)

where 𝐹 is the Fisher information matrix of the 𝜃, and ∥∇˜ 𝐽 (𝜃)∥𝑀 = (∇˜ 𝐽 (𝜃)T𝑀∇˜ 𝐽 (𝜃))1/2 is the norm under 𝑀.

To obtain crucial insights into the determination of the optimal learning rate, we first assume 𝐻 ≈ 𝑐𝐹 for a positive constant 𝑐. This assumption is partially relevant in scenarios where the covariance matrix of CMA-ES successfully learns the shape of a quadratic function. This concept can be illustrated as follows: For a function 𝑓 (𝑥) = 12𝑥⊤𝐴𝑥, the Hessian 𝐻 is diag(𝐴, 0). Consequently, given that 𝐹 = diag(Σ−1, Σ−1 ⊗ Σ−1/2), if 𝐴 ∝ Σ−1, then, to a certain extent, the Hessian 𝐻 in the 𝑚-part approximates 𝑐𝐹 for some 𝑐 value; however, this does not apply to 𝐻 in the Σ-part. Based on this assumption, the optimal learning rate can be written as

1 𝑐 ·

1 1 + SNR−1 ∝

1 1 + SNR−1

. (34)

𝜂∗ ≈

where SNR := ∥∇˜ 𝐽 (𝜃)∥

2 𝐹

Tr(𝐹 Cov[Δ]) . A high SNR increases the 𝜂∗ value, which aligns with our intuitive expectations. In the next section, we propose an LRA mechanism based on these insights into the optimal learning rate.

- 4 LRA MECHANISM We consider the updating of the distribution parameters 𝜃𝑚 = 𝑚 and 𝜃Σ = vec(Σ), where vec is the vectorization operator and Σ = 𝜎2𝐶 for the standard CMA-ES. Let Δ𝑚(𝑡) = 𝑚(𝑡+1) − 𝑚(𝑡) and ΔΣ(𝑡) = vec(Σ(𝑡+1)−Σ(𝑡)) be the original updates of𝑚 and Σ, respectively. Subsequently, we introduce the learning rate factors𝜂𝑚(𝑡) and𝜂Σ(𝑡). The modified updates are performed as𝜃𝑚(𝑡+1) = 𝜃𝑚(𝑡) +𝜂𝑚(𝑡)Δ𝑚(𝑡) and 𝜃Σ(𝑡+1) = 𝜃Σ(𝑡) + 𝜂Σ(𝑡)ΔΣ(𝑡). Finally, 𝜂𝑚(𝑡) and 𝜂Σ(𝑡) are adapted individually.


### 4.1 Main Concept

We adapt the learning rate factor 𝜂 for the component 𝜃 (either 𝜃𝑚 = 𝑚 or 𝜃Σ = vec(Σ)) of the distribution parameters based on the SNR of the update as follows:

SNR := ∥E[Δ]∥2𝐹 Tr(𝐹 Cov[Δ])

#### = ∥E[Δ]∥2𝐹 E[∥Δ∥2𝐹] − ∥E[Δ]∥2𝐹

. (35)

The Fisher metric is selected as it offers invariance against probability distribution parameterization. We attempt to adapt 𝜂 such that SNR = 𝛼𝜂, where 𝛼 > 0 is a hyperparameter that determines the target SNR.

The following rationale is employed for selecting this concept: We assume that 𝜂 is sufficiently small such that the distribution parameters do not change significantly over 𝑛 iterations. Thus, we assume 𝜃(𝑡+𝑘) ≈ 𝜃(𝑡) for 𝑘 = 1, . . .,𝑛. Subsequently, {Δ(𝑡+𝑘)}𝑛𝑘=−01 are roughly considered as i.i.d. Hence, 𝑛 steps of the update are as follows:

𝑛∑︁−1

Δ(𝑡+𝑘) (36a)

𝜃(𝑡+𝑛) = 𝜃(𝑡) + 𝜂

𝑘=0

≈ 𝜃(𝑡) + D 𝑛𝜂E[Δ],𝑛𝜂2 Cov[Δ] , (36b) where D(𝐴,𝐵) is a distribution with expectation 𝐴 and (co)variance 𝐵. Thus, by setting a small 𝜂 value and considering the results of 𝑛 = 1/𝜂 updates, we obtain an update that is more concentrated around the expected behavior than that expected for an update using 𝜂 = 1. The expected change in 𝜃 over 𝑛 = 1/𝜂 iterations, measured using the squared Fisher norm, which approximates the Kullback–Leibler (KL) divergence between 𝜃(𝑡) and 𝜃(𝑡+𝑛), is ∥E[Δ]∥2𝐹 +𝜂 Tr(𝐹 Cov[Δ]), where the former and latter terms come from the signal and noise, respectively. The SNR over 𝑛 iterations is ∥E[Δ]∥

2 𝐹

𝜂Tr(𝐹 Cov[Δ]) = 𝜂1SNR. Therefore, maintaining SNR = 𝛼𝜂 implies maintaining the SNR at 𝛼 over 𝑛 = 1/𝜂 iterations, independent of 𝜂.

The rationale for using SNR can also be elucidated from the perspective of the optimal learning rate 𝜂∗ derived in Section 3.3. The results showed that 𝜂∗ ∝ 1/(1 + SNR−1) approximately holds under some assumptions. Additionally, we assume a relatively small SNR, for example, SNR ⪅ 1 (this assumption is validated in Appendix B). In this case, the approximation 1/(1 + SNR−1) ≈ SNR is roughly valid. Thus, 𝜂∗ ∝ SNR can be considered to be valid. As stated previously, we controlled 𝜂 such that SNR = 𝛼𝜂. Consequently, this leads to 𝜂 ∝ SNR, which is considered to be nearly optimal.

### 4.2 SNR Estimation

We estimate ∥E[Δ]∥2 and E[∥Δ∥2] for each component (𝑚 and Σ) using moving averages. We let E(0) = 0 and V(0) = 0, and update them as follows:

E(𝑡+1) = (1 − 𝛽)E(𝑡) + 𝛽Δ˜ (𝑡), (37a)

V(𝑡+1) = (1 − 𝛽)V(𝑡) + 𝛽∥Δ˜ (𝑡)∥22, (37b) where 𝛽 is a hyperparameter; Δ˜ (𝑡) is the update at iteration𝑡 in the local coordinate at which the 𝐹 at 𝜃(𝑡) becomes the identity; ∥·∥2 is the ℓ2-norm. Thereafter, 2−𝛽

2−2𝛽 ∥E∥22 − 2−𝛽2𝛽 V and V are considered estimates of ∥E[Δ]∥22 and E[∥Δ∥22], respectively (the derivation is included in Appendix A).

The rationale for our estimators is as follows. Suppose that 𝜂𝑚 and 𝜂Σ are sufficiently small for us to assume that the parameters 𝑚 and Σ do not change significantly over 𝑛 iterations. Subsequently, the Δ˜ (𝑡+𝑖) (𝑖 = 0, ..,𝑛 −1) are considered to be located on the same local coordinates and distributed

independently and identically. Then, ignoring the (1 − 𝛽)𝑛 terms, we obtain

𝛽 2 − 𝛽

E(𝑡+𝑛) ∼ D E[Δ˜ ],

Cov[Δ˜ ] . (38)

(Again, the derivationispresented in AppendixA.) Thus, wehaveE[∥E∥22] ≈ ∥E[Δ˜ ]∥22+2−𝛽𝛽 Tr(Cov[Δ˜ ]). Similarly, it is apparent that E[V] ≈ E[∥Δ˜ ∥22] = ∥E[Δ˜ ]∥22 + Tr(Cov[Δ˜ ]).

The SNR is then estimated as SNR := ∥E[Δ˜ ]∥2 Tr(Cov[Δ˜ ])

#### = ∥E[Δ˜ ]∥2 E[∥Δ˜ ∥2] − ∥E[Δ˜ ]∥2

(39a)

∥E∥22 − 2−𝛽𝛽 V V − ∥E∥22

=: SNR. (39b)

≈

### 4.3 Learning Rate Factor Adaptation

We attempt to adapt 𝜂 such that SNR = 𝛼𝜂, where 𝛼 > 0 is the hyperparameter. This adaptation is expressed as follows:

SNR 𝛼𝜂 − 1 , (40)

𝜂 ← 𝜂 exp min(𝛾𝜂, 𝛽)Π[−1,1]

where Π[−1,1] is the projection onto [−1, 1] and 𝛾 is a hyperparameter. If SNR > 𝛼𝜂, 𝜂 increases, and vice versa. Owing to these feedback mechanisms, SNR/(𝛼𝜂) is expected to remain near 1. In the above expression, the projection Π[−1,1] is introduced to prevent a significant change in 𝜂 during an iteration, and the damping factor min(𝛾𝜂, 𝛽) is introduced because of the following reasons. First, the factor 𝛽 is introduced to allow for the effect of the change in the previous 𝜂 value to appear in SNR. Second, the factor 𝛾𝜂 is introduced to prevent the 𝜂 value from changing more than exp(𝛾) or exp(−𝛾) over 1/𝜂 iterations. Based on the 𝜂 update through Eq. (40), the upper bound is set to 1 using 𝜂 ← min(𝜂, 1), to prevent unstable behavior. Although allowing 𝜂 values >1 would accelerate the optimization, we do not consider this because we aim to safely solve difficult problems.

### 4.4 Local Coordinate-System Definition

Although we estimate the SNR based on the updates Δ(·), naïvely accumulating these updates Δ(·) may result in unintentional behavior, as illustrated in the following example. Consider a scenario wherein 𝑝(𝑥;𝜃(𝑡)) = N(0, 100𝐼), 𝑝(𝑥;𝜃(𝑡+1)) = N(0, 50𝐼), and 𝑝(𝑥;𝜃(𝑡+2)) = N(0, 25𝐼). In this case, the covariance matrix of the distribution decreases at a constant rate. Consequently, each KL divergence is 𝐷KL(𝑝(𝑥;𝜃(𝑡))||𝑝(𝑥;𝜃(𝑡+1))) = 𝐷KL(𝑝(𝑥;𝜃(𝑡+1))||𝑝(𝑥;𝜃(𝑡+2))). This implies that the distribution is moving at a uniform pace in terms of the KL divergence. However, the updates are vec−1(ΔΣ(𝑡)) = 50𝐼 and vec−1(ΔΣ(𝑡+1)) = 25𝐼, whose scales are different. Thus, accumulating these effects will result in unintentional behavior.

To address these issues, we ensure parameterization invariance by defining the local coordinate system [Nishida and Akimoto 2016, 2018] such that the Fisher information matrices, 𝐹𝑚 and 𝐹Σ, corresponding to each component of the distribution parameters, 𝑚 and Σ, respectively, are the identity matrices. It is well-known that 𝐹𝑚 = Σ−1 and 𝐹Σ = 2−1Σ−1 ⊗ Σ−1, and their square roots are √𝐹𝑚 = √Σ−1 and √𝐹Σ = 2−12

√Σ−1. Therefore, we define Δ˜𝑚 =

#### √Σ−1 ⊗

√

Σ−1Δ𝑚, (41a) Δ˜ Σ = 2−21 vec(

√

√

Σ−1 vec−1(ΔΣ)

Σ−1). (41b)

Actually, in the previous example, the local coordinate system allows us to easily verify that vec−1(Δ˜ Σ(𝑡)) = vec−1(Δ˜ Σ(𝑡+1)). This observation aligns with intuitive expectations in view of the KL divergence and suggests the validity of accumulating the updates Δ˜ instead of the original Δ.

### 4.5 Covariance Matrix Decomposition

After updating the covariance matrix Σ(𝑡+1) = Σ(𝑡) + 𝜂Σ(𝑡) vec−1(ΔΣ(𝑡)), it must be split into 𝜎 and 𝐶. For this, we adopt the following strategy:

𝜎(𝑡+1) = det(Σ(𝑡+1)) 1

2𝑑 , (42a) 𝐶(𝑡+1) = (𝜎(𝑡+1))−2Σ(𝑡+1). (42b)

### 4.6 Step-size Correction

Updating the learning rate for the 𝑚, i.e., 𝜂𝑚, changes the appropriate 𝜎. Through a quality gain analysis that analyzed the expected 𝑓 value improvement in a single step, a previous study [Akimoto et al. 2020] demonstrated that the optimal 𝜎 value is proportional to 1/𝜂𝑚 for infinite-dimensional convex quadratic functions. Therefore, to maintain the optimal 𝜎 value under 𝜂𝑚 variations, we correct 𝜎 after each 𝜂𝑚 update as follows:

𝜂𝑚(𝑡) 𝜂𝑚(𝑡+1)

𝜎(𝑡+1) ←

𝜎(𝑡+1). (43)

### 4.7 Overall Procedure

Algorithm 1 presents the overall LRA-CMA-ES procedure. At Line 2, the old parameters 𝑚(𝑡),𝜎(𝑡), and𝐶(𝑡) are input intoCMA(·), which outputsnew parameters𝑚(𝑡+1),𝜎(𝑡+1), and𝐶(𝑡+1) by executing Steps 1–3 described in Section 2.1.

Note that the internal parameters such as the evolution paths 𝑝𝜎 and 𝑝𝑐, are updated and stored in CMA(·). However, these values were omitted for simplicity. The subscript ·{𝑚,Σ} (e.g., as in 𝜂{𝑚,Σ}) indicates that there are parameters for 𝑚 and Σ, respectively. For example, E{(𝑚,𝑡+1Σ)} ←

- (1 − 𝛽{𝑚,Σ})E{(𝑚,𝑡) Σ} + 𝛽{𝑚,Σ}Δ˜ {(𝑡𝑚,) Σ} is an abbreviation for the following two update equations: E𝑚(𝑡+1) ← (1 − 𝛽𝑚)E𝑚(𝑡) + 𝛽𝑚Δ˜𝑚(𝑡) and EΣ(𝑡+1) ← (1 − 𝛽Σ)EΣ(𝑡) + 𝛽ΣΔ˜ Σ(𝑡).


- 5 EXPERIMENTS This study included various experiments to investigate the following research questions (RQs):


- RQ1. Does the 𝜂 adaptation in LRA-CMA-ES behave appropriately in accordance with the problem structure?
- RQ2. Can LRA-CMA-ES solve multimodal and noisy problems even though a default 𝜆 value is used? How does its efficiency compare to that of CMA-ES with a fixed 𝜂 value?
- RQ3. How does the performance change with changes in LRA-CMA-ES hyperparameters?
- RQ4. How does the performance depend on the population size 𝜆?
- RQ5. What are the differences in the performances of LRA-CMA-ES, which adapts the learning rate, and PSA-CMA-ES [Nishida and Akimoto 2018], which adapts the population size?


The remainder of this section is organized as follows. The experimental setups are described in Section 5.1. Section 5.2 demonstrates𝜂 adaptation in LRA-CMA-ES for noiseless and noisy problems (RQ1). Section 5.3 compares LRA-CMA-ES with CMA-ES with fixed 𝜂 values (RQ2). Section 5.4 investigates the effects of LRA-CMA-ES hyperparameters (RQ3). Additional experimental results for the hyperparameters are presented in Appendix C. Section 5.5 evaluates the performance differences

Algorithm 1 LRA-CMA-ES Input: 𝑚(0) ∈ R𝑑,𝜎(0) ∈ R>0,𝜆 ∈ N,𝛼, 𝛽{𝑚,Σ},𝛾 ∈ R Set: 𝑡 = 0,𝐶(0) = 𝐼,𝜂{(𝑚,0) Σ} = 1, E(0) = 0, V(0) = 0

- 1: while stopping criterion not met do
- 2: 𝑚(𝑡+1),𝜎(𝑡+1),𝐶(𝑡+1) ← CMA(𝑚(𝑡),𝜎(𝑡),𝐶(𝑡))
- 3: // calculate parameter one-step differences
- 4: Δ𝑚(𝑡) ← 𝑚(𝑡+1) −𝑚(𝑡)
- 5: Σ(𝑡+1) ← 𝜎(𝑡+1) 2𝐶(𝑡+1)
- 6: ΔΣ(𝑡) ← vec Σ(𝑡+1) − Σ(𝑡)
- 7: // local coordinate
- 8: Δ˜𝑚(𝑡) ←

√

Σ(𝑡)

−1Δ𝑚(𝑡)

- 9: Δ˜ Σ(𝑡) ← 2−1/2vec √

Σ(𝑡)

−1vec−1 ΔΣ(𝑡)

√

Σ(𝑡)

−1

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
- 21: 𝜎(𝑡+1) ← det(Σ(𝑡+1))21𝑑 , 𝐶(𝑡+1) ← (𝜎(𝑡+1))−2Σ(𝑡+1)

- 22: // 𝜎 correction
- 23: 𝜎(𝑡+1) ← 𝜎(𝑡+1)(𝜂𝑚(𝑡)/𝜂𝑚(𝑡+1))
- 24: 𝑡 ← 𝑡 + 1
- 25: end while


under various different population sizes (RQ4). Finally, Section 5.6 compares LRA-CMA-ES with PSA-CMA-ES (RQ5). Our code is available at https://github.com/nomuramasahir0/cma-learningrate-adaptation. The LRA-CMA-ESisalsoavailable athttps://github.com/CyberAgentAILab/cmaes[No-

mura and Shibata 2024], although the CMA-ES implementation there differs slightly from the one in our paper.

### 5.1 Experimental Setups

The benchmark problem definitions and initial distributions are presented in Table 1. In each case (except for the Rosenbrock function), the global optimal solution is at 𝑥 = 0. However, for the Rosenbrock function, it is at 𝑥 = 1. As unimodal problems, we employ the Sphere, Ellipsoid, and Rosenbrock functions. The reason for using unimodal problems is to ensure that the performance

Table 1. Definitions of benchmark problems and initial distributions used in the experiments.

Definitions Initial Distributions 𝑓Sphere(𝑥) = 𝑑𝑖=1 𝑥𝑖2 𝑚(0) = [3, . . ., 3],𝜎(0) = 2 𝑓Ellipsoid(𝑥) = 𝑑𝑖=1(1000𝑑𝑖−−11 𝑥𝑖 )2 𝑚(0) = [3, . . ., 3],𝜎(0) = 2 𝑓Rosenbrock(𝑥) = 𝑑𝑖=−11(100(𝑥𝑖+1 − 𝑥𝑖2)2 + (𝑥𝑖 − 1)2) 𝑚(0) = [0, . . ., 0],𝜎(0) = 0.1 𝑓Ackley(𝑥) = 20 − 20 · exp(−0.2√︃

1 𝑑

𝑑 𝑖=1 𝑥𝑖2) + 𝑒 − exp(𝑑1 𝑑𝑖=1 cos(2𝜋𝑥𝑖 )) 𝑚(0) = [15.5, . . ., 15.5],𝜎(0) = 14.5

𝑓Schaffer(𝑥) = 𝑑𝑖=−11(𝑥𝑖2 + 𝑥𝑖2+1)0.25 · [sin2(50 · (𝑥𝑖2 + 𝑥𝑖2+1)0.1) + 1] 𝑚(0) = [55, . . ., 55],𝜎(0) = 45 𝑓Rastrigin(𝑥) = 10𝑑 + 𝑑𝑖=1(𝑥𝑖2 − 10cos(2𝜋𝑥𝑖 )) 𝑚(0) = [3, . . ., 3],𝜎(0) = 2 𝑓Bohachevsky(𝑥) = 𝑑𝑖=−11(𝑥𝑖2 + 2𝑥𝑖2+1 − 0.3cos(3𝜋𝑥𝑖 ) − 0.4cos(4𝜋𝑥𝑖+1) + 0.7) 𝑚(0) = [8, . . ., 8],𝜎(0) = 7 𝑓Griewank(𝑥) = 40001 𝑑𝑖=1 𝑥𝑖2 − Π𝑑𝑖=1 cos(𝑥𝑖/

√𝑖) + 1 𝑚(0) = [305, . . ., 305],𝜎(0) = 295

of LRA-CMA-ES does not degrade significantly compared to CMA-ES with the default learning rate. The Ellipsoid function is an ill-conditioned problem, whereas the Rosenbrock function has dependencies between variables. Although the Rosenbrock function has local minima, in our study, it can be regarded as an almost unimodal problem. As well-structured multimodal problems, we employ the Ackley, Schaffer, Rastrigin, Bohachevsky, and Griewank functions. These problems are composed of a quadratic convex function and oscillatory nonconvex function, which resembles the noise. In the Ackley, Rastrigin, Bohachevsky, and Griewank functions, the oscillatory function is added to the convex function, whereas in the Schaffer function, the oscillatory function affects the convex function multiplicatively. This causes the Schaffer function to have fine oscillations around the optimal solution. Noteworthy, the optimization for the Griewank function gets easier as the dimension increases [Hansen and Kern 2004]. Similar to [Hansen and Kern 2004], we imposed additional bounds on the Ackley function. For noisy problems, we considered an additive Gaussian noise 𝜖 ∼ N(0,𝜎𝑛2) with 𝜎𝑛2 variance. It is worth noting that the proposed method maintains the affine invariance of CMA-ES because LRA-CMA-ES does not rely on a specific parameterization, as discussed in Section 4.4. Consequently, although many of the employed benchmark problems are separable, the experimental results obtained from a benchmark function can still be generalized to the experimental results of its rotated version.

In all the experiments (except for those in Section 5.5), we set the default 𝜆 = 4 + ⌊3ln𝑑⌋. The result when changing 𝜆 can be found in Ref. [Hansen and Kern 2004] and Section 5.5. For the dimension 𝑑, we employed 𝑑 ∈ {10, 20, 30, 40} for noiseless problems and 𝑑 = 10 for noisy problems. Additionally, we set the LRA-CMA-ES hyperparameters as 𝛼 = 1.4, 𝛽𝑚 = 0.1, 𝛽Σ = 0.03, and 𝛾 = 0.1 based on preliminary experiments. As noted above, Section 5.4 presents an analysis of the hyperparameters sensitivity. The values of other internal parameters of CMA-ES were set to those recommended in [Hansen and Auger 2014].

### 5.2 Learning Rate Behavior

Figure 4 shows the typical LRA-CMA-ES behaviors for noiseless problems, wherein 𝜂Σ maintained relatively large values for the Sphere function. However, it exhibits significantly smaller values for the Ellipsoid and Rosenbrock functions. We believe that this behavior is undesirable, because the default 𝜂 value already works well for these unimodal problems. Although 𝜂 can be increased by changing the hyperparameters of the proposed 𝜂 adaptation, this change may be detrimental for multimodal problems.

It is evident that 𝜂𝑚 is slightly smaller for multimodal problems than for unimodal problems. Particularly, for the Rastrigin function, 𝜂𝑚 and 𝜂Σ clearly decrease at the beginning of the optimization, which reflects the difficulty of multimodal problem optimization. Subsequently, 𝜂 increases as

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

###### 100

10−1

ηm

10−2

10−3

###### 100

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

Fig. 4. Typical LRA-CMA-ES behaviors for 10-dimensional (10-D) noiseless problems. The coordinates of 𝑚 and the square roots of the eigenvalues of 𝜎2𝐶 (denoted by √︁eig) are indicated with different colors.

optimization becomes as easy as that for a unimodal problem. This behavior demonstrates that LRA-CMA-ES can adapt 𝜂 according to the search difficulty.

Figure 5 shows the typical 𝜂 adaptation behavior for noisy problems. The noise has a negligible effect in the early stages; thus, the 𝜂 behavior for noisy problems is similar to that for noiseless problems. However, as the optimization proceeds and the function value approaches the same scale as that of the noise value, the noise starts having a critical effect. Consequently, the 𝜂 value decreases. This adaptation ensures that the SNR remains constant. Notably, similar behavior can be observed for the noisy Rastrigin function, which features both noise and multimodality.

- 5.3 Effects of LRA Figures 6 and 7 show the performances of LRA-CMA-ES and that of CMA-ES with a fixed learning rate (𝜂𝑚,𝜂Σ ∈ {100, 10−1, 10−2}) for the noiseless problems. Note that CMA-ES with 𝜂𝑚 = 1.0 and 𝜂Σ = 1.0 is the original CMA-ES with the default 𝜂 value. Each trial was considered successful if 𝑓 (𝑚) reached the target value 10−8 before 107 function evaluations or before a numerical error occurred because of an excessively small 𝜎. In addition to the success rate, we employed the SP1 value [Auger and Hansen 2005], which is the average number of evaluations among successful trials until achieving the target value divided by the success rate. 30 trials were conducted for each setting.


To compare the performances of these strategies for the noisy problems, we employed the empirical cumulative density function (ECDF) of COCO, a platform for comparing continuous optimizers in a black-box setting [Hansen et al. 2021]. Using 𝑁target target values, we recorded the number of evaluations until 𝑓 (𝑚) (noiseless) reached each target value for the first time, and set the maximum function evaluation to 108. We collected data by running 𝑁trial independent trials, and obtained a total of 𝑁target · 𝑁trial targets for each problem. Thereafter, we set the target values

###### Noisy Sphere

###### Noisy Ellipsoid

###### Noisy Rastrigin

106

102

f(m)

10−2

###### 100

10−1

ηm

10−2

10−3

###### 100

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

Fig. 5. Typical LRA-CMA-ES behaviors for 10-D noisy problems. The noise variance 𝜎𝑛2 was set to 1.

to 106−9(𝑖−1)/(𝑁target−1) for 𝑖 = 1, . . ., 𝑁target, with 𝑁target = 30. By executing 𝑁trial = 20 trials, 600 targets were obtained for each problem. Figure 8 shows the target value percentages obtained for each number of evaluations.

- 5.3.1 Noiseless Problems. We compared the success rates of LRA-CMA-ES and CMA-ES with fixed 𝜂 values, as shown in Figure 6. For the multimodal problems, CMA-ES with a large 𝜂 often failed to reach the optimum. However, CMA-ES with a small 𝜂 exhibited a high success rate, indicating a clear dependence on 𝜂. By contrast, LRA-CMA-ES exhibited a relatively good success rate, even though no 𝜂 tuning was required. It is noteworthy that LRA-CMA-ES succeeded in all trials for the Rastrigin function even though the default population size (e.g., 𝜆 = 15 for 𝑑 = 40) was used and 𝜂 was not tuned in advance.


However, LRA-CMA-ES performance for the Schaffer function degraded at 𝑑 = 40. From the results indicating that CMA-ES with an appropriately tuned, small 𝜂 achieved a relatively high success rate, the LRA-CMA-ES result may have been obtained because 𝜂 was not appropriately adapted in that case. This will be investigated in future work.

Figure 7 shows the SP1 results for LRA-CMA-ES and CMA-ES with fixed 𝜂 values. CMA-ES with the default 𝜂 values (𝜂𝑚 = 1.0,𝜂Σ = 1.0) outperformed the other methods for unimodal problems; however, the performance degraded significantly for multimodal problems owing to optimization

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

Fig. 6. Success rates according to the number of dimensions (noiseless problems).

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

Fig. 7. SP1 values according to the number of dimensions (noiseless problems). A missing point indicates the algorithm’s failure in all trials.

failures. By contrast, the CMA-ES with a small 𝜂 sometimes exhibited good performance for such multimodal problems; however, it was not efficient for unimodal and relatively easy multimodal problems. Therefore, for CMA-ES with a fixed 𝜂 value, a clear trade-off in efficiency exists based on the 𝜂 setting. By contrast, LRA-CMA-ES exhibited stable and relatively good performance for unimodal and multimodal problems. Again, 𝜂 was not tuned, which is significantly expensive in practice. There is scope for improvement of the LRA-CMA-ES performance on unimodal problems; however, the current sub-par performance can be somewhat mitigated by changing the hyperparameters. The effects of the hyperparameters are discussed in Section 5.4.

- 5.3.2 Noisy Problems. Figure 8 shows the ECDF results for both LRA-CMA-ES and CMA-ES with


fixed 𝜂 values. We considered two noise strengths, weak and strong, that is, 𝜎𝑛2 = 1 and 106, respectively.

Under the weak-noise setting, CMA-ES with a small 𝜂 value reached all the target values. By contrast, CMA-ES with a large 𝜂 value failed to approach the global optimum and yielded a suboptimal solution. LRA-CMA-ES achieved similar performance to CMA-ES with a small 𝜂 value without tuning. However, under the strong-noise setting, even CMA-ES with a small 𝜂 stopped improving the 𝑓 value before reaching the global optimum. By contrast, LRA-CMA-ES continued

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

Fig. 8. Empirical cumulative density function for 10-D noisy problems, with 𝜎𝑛2 set to 1 or 106.

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

Fig. 9. Success rates and SP1 values with hyperparameter 𝛼 for 30-D noiseless problems (30 trials).

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

Fig. 10. Success rates and SP1 values with hyperparameter 𝛽Σ for 30-D noiseless problems (30 trials).

improving the 𝑓 value. Notably, the results for the noisy Rastrigin function suggest that LRA-CMAES can simultaneously handle both noise and multimodality.

### 5.4 Effects of Hyperparameters

Figure 9 shows the success rates and SP1 values with respect to 𝛼 for the 30-dimensional (30-D) noiseless Sphere, Schaffer, and Rastrigin functions. For the Sphere function, a lower SP1 value could be achieved with a smaller 𝛼 value. However, an excessively large 𝛼 results in optimization failures for multimodal problems. Therefore, the current setting of 𝛼 = 1.4 seems reasonable; however, further investigations are required.

Figure10shows thesuccess rates andSP1 values with respect to 𝛽Σ. We observe that anexcessively large 𝛽Σ causes optimization failures in the Rastrigin function. Conversely, an excessively small 𝛽Σ results in slow convergence. An additional result (𝛽Σ ∈ {0.01, 0.02, ..., 0.05}) is presented in Appendix C.

λ vs. Success Rate and SP1 (d = 30,30 trials)

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

14 28 42 56 70

14 28 42 56 70

14 28 42 56 70

- 104
- 105


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


- 105
- 106


14 28 42 56 70

14 28 42 56 70

14 28 42 56 70

- Fig. 11. Success rates and SP1 values with 𝜆 ∈ {14, 28, 42, 56, 70} for 30-D noiseless problems (30 trials).


We also conducted similar experiments on the hyperparameters 𝛽𝑚 and𝛾, to confirm their effects. These hyperparameters mildly impacted the overall performance compared to 𝛼 and 𝛽Σ (these results are also presented in Appendix C).

### 5.5 Effects of Population Size

Although we used the default population size, 𝜆 = 4+⌊3log(𝑑)⌋, in all the experiments, practitioners may want to employ different population sizes to fully utilize their parallel environments. In this section, we describe the experiments conducted to investigate the effects of population size.

Figure 11 shows the success rates and SP1 values with respect to 𝜆 ∈ {14, 28, 42, 56, 70} for the 30-D noiseless Sphere, Schaffer, and Rastrigin functions. Although the SP1 value worsens with a larger 𝜆 for the Rastrigin function, it appears to have a mild impact for the Sphere and Schaffer functions. Figure 12 shows typical behaviors of LRA-CMA-ES with 𝜆 ∈ {14, 42, 70} on the 30-D Sphere function. As 𝜆 increases, it can be observed that the learning rates (especially 𝜂𝑚) also generally increase linearly. This is because, as 𝜆 increases, the SNR also increases, allowing for a larger learning rate to maintain the target SNR. This phenomenon can also be theoretically explained as follows: The SNR analysis for the infinite-dimensional Sphere function in Appendix B shows that under the assumption of the optimal step-size, SNR ≈ 𝑂(𝜆/𝑑). In this case, increasing 𝜆 can linearly increase the SNR; therefore, it is expected that the learning rate can be kept linearly larger, which is consistent with our empirical findings. However, this analysis was conducted using the (infinite-dimensional) Sphere function; thus, this discussion cannot be directly applied to multimodal problems.

Additionally, we investigated the behavior for larger population sizes using various values of 𝜆 ∈ {500, 1000, 1500, 2000, 2500}, as shown in Figure 13. Compared to the results for 𝜆 ∈ {14, 28, 42, 56, 70}, the SP1 value remains almost constant for the Rastrigin function with respect to the 𝜆 value. However, in the Sphere and Schaffer functions, the SP1 value deteriorates slightly for larger 𝜆 values. This may be partially because the proposed method is designed to solve difficult problems (e.g., 𝜂𝑚,𝜂Σ ⩽ 1). Although more aggressive learning rate updates may improve the performance, such strategies were beyond the scope of this study.

### 5.6 LRA-CMA-ES vs. PSA-CMA-ES

We compared the performance of the proposed LRA-CMA-ES with that of PSA-CMA-ES [Nishida and Akimoto 2018], which is a state-of-the-art population size adaptation method. For a fair comparison, we employed almost the same procedure and hyperparameters for PSA-CMA-ES as those for the CMA-ES described in Section 2.1. The only difference was that PSA-CMA-ES required additional normalization factors (Eqs. (6) and (7) in [Nishida and Akimoto 2018]) to derive an approximate value for the parameter movement. For the step-size correction in PSA-CMA-ES, we used Blom’s approximation to calculate the weighted average of the expected value of normal-order statistics [Akimoto et al. 2020]. Additionally, we used the recommended values for the PSA-CMA-ES

###### λ = 14

λ = 42

λ = 70

0.10

0.10

0.10

| | | | |
|---|---|---|---|
| | | | |
| | | | |
| | | | |


| | | | |
|---|---|---|---|
| | | | |
| | | | |
| | | | |


| | | | |
|---|---|---|---|
| | | | |
| | | | |
| | | | |


0.07

0.07

0.07

ηm

0.04

0.04

0.04

0.01

0.01

0.01

0 10000 20000 30000 Function Evaluations

0 10000 20000 30000 Function Evaluations

0 10000 20000 30000 Function Evaluations

1.0

1.0

1.0

| | | | |
|---|---|---|---|
| | | | |
| | | | |
| | | | |


| | | | |
|---|---|---|---|
| | | | |
| | | | |
| | | | |


| | | | |
|---|---|---|---|
| | | | |
| | | | |
| | | | |


0.7

0.7

0.7

ηΣ

0.4

0.4

0.4

0.1

0.1

0.1

0 10000 20000 30000 Function Evaluations

0 10000 20000 30000 Function Evaluations

0 10000 20000 30000 Function Evaluations

40

hist() SNRm

100

50

20

50

25

0

0

0

0.00 0.05 0.10 0.15 0.20

0.00 0.05 0.10 0.15 0.20

0.00 0.05 0.10 0.15 0.20

40

hist() SNRΣ

50

100

20

0

0

0

0 1 2 3

0 1 2 3

0 1 2 3

- Fig. 12. LRA-CMA-ES behaviors on the 30-D Sphere function with 𝜆 ∈ {14, 42, 70}. 𝜂𝑚, 𝜂Σ, and the histograms of the estimated SNR w.r.t. 𝑚 and Σ, in this order from the top. The y-axes in 𝜂𝑚 and 𝜂Σ are shown on the linear scale rather than the log scale.

| | | | | | | |
|---|---|---|---|---|---|---|
| | | | | | | |
| | | | | | | |
| | | | | | | |


500 1000 1500 2000 2500

0.0

0.5

1.0

Sphere

| | | | | | | |
|---|---|---|---|---|---|---|
| | | | | | | |
| | | | | | | |
| | | | | | | |


500 1000 1500 2000 2500

0.0

0.5

1.0

Schaﬀer

| | | | | | | |
|---|---|---|---|---|---|---|
| | | | | | | |
| | | | | | | |
| | | | | | | |


500 1000 1500 2000 2500

0.0

0.5

1.0

Rastrigin

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


500 1000 1500 2000 2500

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


500 1000 1500 2000 2500

- 106
- 107


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


500 1000 1500 2000 2500

- 107
- 108


SP1SuccessRate

λ vs. Success Rate and SP1 (d = 30,30 trials)

- Fig. 13. Success rates and SP1 values with 𝜆 ∈ {500, 1000, 1500, 2000, 2500} for 30-D noiseless problems (30 trials).


hyperparameters [Nishida and Akimoto 2018]. The experimental settings were the same as those described in Section 5.3. All LRA-CMA-ES results were obtained from Section 5.3.

Figures 14 and 15 show the success rates and SP1 values, respectively, for the noiseless problems, wherein it is evident that PSA-CMA-ES exhibits better results than LRA-CMA-ES for most problems. Figure 16 illustrates the ECDF for noisy problems. The performance of LRA-CMA-ES is better than that of PSA-CMA-ES in most of the tested cases. For example, for the Rastrigin function with a strong-noise setting (bottom right of Figure 16), PSA-CMA-ES stopped improving the function value, whereas LRA-CMA-ES continued improving it. These results suggest that LRA-CMA-ES and PSA-CMA-ES are suitable for different problems. However, these performance differences can be mitigated to a certain degree by adjusting the hyperparameters of each method and do not necessarily suggest that there is a fundamental performance difference between learning rate and population size adaptations. Although we still argue that LRA is more practically useful than population size adaptation, as described in Section 1, a detailed comparison of these methods will be an interesting direction for future work.

LRA PSA

Sphere

Ellipsoid

Rosenbrock

Ackley

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

1.0

1.0

| | | | | | |
|---|---|---|---|---|---|
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |


| | | | | | |
|---|---|---|---|---|---|
| | | | | | |
| | | | | | |


| | | | | | |
|---|---|---|---|---|---|
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

0.0

0.0

0.0

0.0

10 20 30 40

10 20 30 40

10 20 30 40

10 20 30 40

Dimension

- Fig. 14. Performances of LRA-CMA-ES and PSA-CMA-ES: success rates according to the number of dimensions (noiseless problems).

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


10 20 30 40

- 104

Sphere

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


10 20 30 40

- 104
- 105


Ellipsoid

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


10 20 30 40

- 104
- 105
- 106


Rosenbrock

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


10 20 30 40

- 104
- 105


Ackley

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


10 20 30 40

- 105
- 106


Schaﬀer

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


10 20 30 40

105

Rastrigin

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


10 20 30 40

- 104
- 105


Bohachevsky

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


10 20 30 40

- 104
- 105


Griewank

Dimension

SP1

LRA PSA

- Fig. 15. Performaces of LRA-CMA-ES and PSA-CMA-ES: SP1 values according to the number of dimensions (noiseless problems).


### 6 CONCLUSION

This study presented the design principles and practices of LRA for CMA-ES. We first demonstrated that difficult problems can be solved relatively easily by decreasing the learning rate and ensuring that the parameter behavior was closer to the ODE trajectory. However, decreasing it excessively worsened the search efficiency. Therefore, we attempted to determine the optimal learning rate for maximizing the expected improvement, which was nearly proportional to the SNR under some assumptions. Based on these observations, we developed a new LRA mechanism to solve multimodal and noisy problems using CMA-ES without extremely expensive learning-rate tuning. The basic concept of the proposed algorithm, LRA-CMA-ES, is to adapt the learning rate such that the SNR can be kept constant, which is nearly optimal based on the optimal learning rate discussion. Experiments involving noiseless multimodal problems revealed that the proposed LRA-CMA-ES can adapt the learning rate appropriately depending on the search situation, and it works well without tuning the learning rate. Additionally, LRA-CMA-ES provided better solutions for noisy problems, even under strong-noise settings, which yielded problems that could not be solved by CMA-ES with a fixed learning rate. In conclusion, LRA-CMA-ES effectively facilitates the solving

LRA PSA

Noisy Sphere (σn2 = 1)

Noisy Ellipsoid (σn2 = 1)

Noisy Rastrigin (σn2 = 1)

| | | |
|---|---|---|
| | | |
| | | |
| | | |
| | | |
| | | |


| | | |
|---|---|---|
| | | |
| | | |


| | | | | |
|---|---|---|---|---|
| | | | | |
| | | | | |
| | | | | |
| | | | | |
| | | | | |


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


| | | |
|---|---|---|
| | | |
| | | |


| | | | | |
|---|---|---|---|---|
| | | | | |
| | | | | |
| | | | | |
| | | | | |
| | | | | |


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

- Fig. 16. Performances of LRA-CMA-ES and PSA-CMA-ES: Empirical cumulative density function for 10-D noisy problems, with 𝜎𝑛2 set to 1 or 106.


of multimodal and noisy problems to a certain extent, eliminating the need for tuning the learning rate.

However, the proposed LRA-CMA-ES has some limitations, which will be addressed in future research. First, it experienced several failures for the 40-D Schaffer function, although CMA-ES with an appropriately small learning rate succeeded with a high probability. We believe that a detailed analysis of the SNR adaptation behavior is crucial to determine the reasons for this failure. On a related note, our understanding of the appropriate hyperparameter settings in the proposed LRA mechanism remains limited. Our experiments revealed that the hyperparameter settings affect the trade-off between stability and convergence speed. Through experiment, we identified the hyperparameters that perform relatively well for noiseless and noisy problems; however, better configuration methods must be developed. For example, the constant value O(1) is used for the cumulation factors 𝛽𝑚 and 𝛽Σ; however, it may be more reasonable to consider that these factors depend on the parameter degrees of freedom, that is, 𝛽𝑚 = O(1/𝑑) and 𝛽Σ = O(1/𝑑2). In addition, the method for determining the appropriate value of the target SNR 𝛼 can be refined further. The SNR analysis presented in Appendix B implies that 𝛼 = O(𝜆/𝑑) is reasonable for an infinitedimensional Sphere function. On the other hand, because this analysis cannot be directly applied to multimodal or noisy problems, there is still room to discuss the best method for determining 𝛼. A deeper understanding of the hyperparameter effects is crucial for improving the reliability of the proposed LRA-CMA-ES.

Additionally, LRA-CMA-ES, which mainly focuses on well-structured multimodal problems, alone cannot solve weakly structured ones, as discussed in Section 1. To address these situations, integrating restart strategies with LRA-CMA-ES is a promising direction.

Finally, developing a more rational LRA approach is an intriguing topic for future research. Although our discussion in Section 3.3 offers valuable insights into designing an ideal learning rate, it was based on several assumptions and has the potential for improvement. A more detailed theoretical study could result in a more rational design for learning rates, which is crucial for advancing this line of research.

ACKNOWLEDGMENTS This study was partially supported by JSPS KAKENHI, grant number 19H04179 and 23K11260.

### REFERENCES

Youhei Akimoto, Anne Auger, and Nikolaus Hansen. 2020. Quality Gain Analysis of the Weighted Recombination Evolution Strategy on General Convex Quadratic Functions. Theoretical Computer Science 832 (2020), 42–67. Youhei Akimoto, Anne Auger, and Nikolaus Hansen. 2022. An ODE Method to Prove the Geometric Convergence of Adaptive Stochastic Algorithms. Stochastic Processes and their Applications 145 (2022), 269–307. Youhei Akimoto and Nikolaus Hansen. 2020. Diagonal Acceleration for Covariance Matrix Adaptation Evolution Strategies. Evolutionary Computation 28, 3 (2020), 405–435. Youhei Akimoto, Yuichi Nagata, Isao Ono, and Shigenobu Kobayashi. 2010. Bidirectional Relation between CMA Evolution Strategies and Natural Evolution Strategies. In International Conference on Parallel Problem Solving from Nature. 154–163. Shun-Ichi Amari and Scott C Douglas. 1998. Why Natural Gradient?. In Proceedings of the IEEE International Conference on

Acoustics, Speech and Signal Processing, Vol. 2. 1213–1216. Shun-ichi Amari and Hiroshi Nagaoka. 2000. Methods of Information Geometry. Vol. 191. Dirk V. Arnold. 2005. Optimal Weighted Recombination. In Foundations of Genetic Algorithms. 215–237. Anne Auger and Nikolaus Hansen. 2005. A Restart CMA Evolution Strategy with Increasing Population Size. In IEEE

Congress on Evolutionary Computation, Vol. 2. IEEE, 1769–1776. Garuda Fujii, Youhei Akimoto, and Masayuki Takahashi. 2018. Exploring optimal topology of thermal cloaks by CMA-ES. Applied Physics Letters 112, 6 (2018). Armand Gissler, Anne Auger, and Nikolaus Hansen. 2022. Learning Rate Adaptation by Line Search in Evolution Strategies

with Recombination. In Proceedings of the Genetic and Evolutionary Computation Conference. 630–638. David Ha and Jürgen Schmidhuber. 2018. World Models. arXiv preprint arXiv:1803.10122 (2018). Nikolaus Hansen. 2009. Benchmarking a BI-population CMA-ES on the BBOB-2009 function testbed. In Proceedings of the

Genetic and Evolutionary Computation Conference: Late Breaking Papers. 2389–2396. Nikolaus Hansen. 2016. The CMA Evolution Strategy: A Tutorial. arXiv preprint arXiv:1604.00772 (2016). Nikolaus Hansen and Anne Auger. 2014. Principled Design of Continuous Stochastic Search: From Theory to Practice. In

Theory and Principled Methods for the Design of Metaheuristics. Springer, 145–180. Nikolaus Hansen, Anne Auger, Raymond Ros, Olaf Mersmann, Tea Tušar, and Dimo Brockhoff. 2021. COCO: A Platform for Comparing Continuous Optimizers in a Black-Box Setting. Optimization Methods and Software 36, 1 (2021), 114–144. Nikolaus Hansen and Stefan Kern. 2004. Evaluating the CMA Evolution Strategy on Multimodal Test Functions. In International Conference on Parallel Problem Solving from Nature. 282–291. Nikolaus Hansen and Andreas Ostermeier. 2001. Completely Derandomized Self-Adaptation in Evolution Strategies. Evolutionary Computation 9, 2 (2001), 159–195.

Michael Hellwig and Hans-Georg Beyer. 2016. Evolution Under Strong Noise: A Self-Adaptive Evolution Strategy Can Reach the Lower Performance Bound - The pcCMSA-ES. In International Conference on Parallel Problem Solving from Nature. 26–36.

Biwei Huang, Chaochao Lu, Liu Leqi, José Miguel Hernández-Lobato, Clark Glymour, Bernhard Schölkopf, and Kun Zhang.

2022. Action-Sufficient State Representation Learning for Control with Structural Constraints. In International Conference on Machine Learning. 9260–9279.

Stanisław Jastrzębski, Zachary Kenton, Devansh Arpit, Nicolas Ballas, Asja Fischer, Yoshua Bengio, and Amos Storkey. 2017. Three Factors Influencing Minima in SGD. arXiv preprint arXiv:1711.04623 (2017). Kotaro Kikuchi, Mayu Otani, Kota Yamaguchi, and Edgar Simo-Serra. 2021a. Modeling Visual Containment for Web Page Layout Optimization. In Computer Graphics Forum, Vol. 40. 33–44. Kotaro Kikuchi, Edgar Simo-Serra, Mayu Otani, and Kota Yamaguchi. 2021b. Constrained Graphic Layout Generation via

Latent Optimization. In Proceedings of the ACM International Conference on Multimedia. 88–96. Peter E Kloeden, Eckhard Platen, Peter E Kloeden, and Eckhard Platen. 1992. Stochastic Differential Equations. Oswin Krause. 2019. Large-Scale Noise-Resilient Evolution-Strategies. In Proceedings of the Genetic and Evolutionary

Computation Conference. 682–690. Ilya Loshchilov, Marc Schoenauer, Michele Sebag, and Nikolaus Hansen. 2014. Maximum Likelihood-based Online Adaptation of Hyper-parameters in CMA-ES. In International Conference on Parallel Problem Solving from Nature. 70–79.

Atsuo Maki, Naoki Sakamoto, Youhei Akimoto, Hiroyuki Nishikawa, and Naoya Umeda. 2020. Application of optimal control theory based on the evolution strategy (CMA-ES) to automatic berthing. Journal of Marine Science and Technology 25 (2020), 221–233.

Hidekazu Miyazawa and Youhei Akimoto. 2017. Effect of the Mean Vector Learning Rate in CMA-ES. In Proceedings of the Genetic and Evolutionary Computation Conference. 721–728. Duc Manh Nguyen and Nikolaus Hansen. 2017. Benchmarking CMAES-APOP on the BBOB Noiseless Testbed. In Proceedings of the Genetic and Evolutionary Computation Conference Companion. 1756–1763. Kouhei Nishida and Youhei Akimoto. 2016. Population Size Adaptation for the CMA-ES Based on the Estimation Accuracy of the Natural Gradient. In Proceedings of the Genetic and Evolutionary Computation Conference. 237–244.

Kouhei Nishida and Youhei Akimoto. 2018. PSA-CMA-ES: CMA-ES with Population Size Adaptation. In Proceedings of the Genetic and Evolutionary Computation Conference. 865–872.

Masahiro Nomura, Youhei Akimoto, and Isao Ono. 2023. CMA-ES with Learning Rate Adaptation: Can CMA-ES with Default Population Size Solve Multimodal and Noisy Problems?. In Proceedings of the Genetic and Evolutionary Computation Conference. 839–847.

Masahiro Nomura and Isao Ono. 2022. Towards a Principled Learning Rate Adaptation for Natural Evolution Strategies. In Applications of Evolutionary Computation. 721–737. Masahiro Nomura and Masashi Shibata. 2024. cmaes : A Simple yet Practical Python Library for CMA-ES. arXiv preprint arXiv:2402.01373 (2024). Masahiro Nomura, Shuhei Watanabe, Youhei Akimoto, Yoshihiko Ozaki, and Masaki Onishi. 2021. Warm Starting CMA-ES for Hyperparameter Optimization. In Proceedings of the AAAI Conference on Artificial Intelligence, Vol. 35. 9188–9196. Yann Ollivier, Ludovic Arnold, Anne Auger, and Nikolaus Hansen. 2017. Information-Geometric Optimization Algorithms: A Unifying Picture via Invariance Principles. Journal of Machine Learning Research 18, 18 (2017), 1–65. AJ Piergiovanni, Anelia Angelova, and Michael S Ryoo. 2020. Evolving Losses for Unsupervised Video Representation Learning. In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition. 133–142. Lennart Oswald Purucker and Joeran Beel. 2023. CMA-ES for Post Hoc Ensembling in AutoML: A Great Success and Salvageable Failure. In AutoML Conference 2023. Takumi Tanabe, Kazuto Fukuchi, Jun Sakuma, and Youhei Akimoto. 2021. Level Generation for Angry Birds with Sequential VAE and Latent Variable Evolution. In Proceedings of the Genetic and Evolutionary Computation Conference. 1052–1060.

Stephen Tian, Yancheng Cai, Hong-Xing Yu, Sergey Zakharov, Katherine Liu, Adrien Gaidon, Yunzhu Li, and Jiajun Wu. 2023. Multi-Object Manipulation via Object-Centric Neural Scattering Functions. In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition. 9021–9031.

Vanessa Volz, Jacob Schrum, Jialin Liu, Simon M Lucas, Adam Smith, and Sebastian Risi. 2018. Evolving Mario Levels in the Latent Space of a Deep Convolutional Generative Adversarial Network. In Proceedings of the Genetic and Evolutionary Computation Conference. 221–228.

- A DERIVATION FOR SECTION 4.2


- A.1 Derivations of Eq. (38)


This section presents the detailed derivation of Eq. (38). By ignoring (1 − 𝛽)𝑛, E(𝑡+𝑛) can be approximately calculated as follows:

E(𝑡+𝑛) = (1 − 𝛽)E(𝑡+𝑛−1) + 𝛽Δ˜ (𝑡+𝑛−1)

= (1 − 𝛽) (1 − 𝛽)E(𝑡+𝑛−2) + 𝛽Δ˜ (𝑡+𝑛−2) + 𝛽Δ˜ (𝑡+𝑛−1)

= ...

𝑛∑︁−1

(1 − 𝛽)𝑖𝛽Δ˜ (𝑡+𝑛−1−𝑖)

= (1 − 𝛽)𝑛E(𝑡) +

𝑖=0

𝑛∑︁−1

(1 − 𝛽)𝑖𝛽Δ˜ (𝑡+𝑛−1−𝑖).

≈

𝑖=0

Here, we assume the Δ˜ (·) are uncorrelated with each other; this corresponds to the scenario where 𝜂 is sufficiently small. In this case, we can ignore the dependence of 𝑡, that is, E[Δ˜ (𝑡+𝑛−1−𝑖)] =: E[Δ˜ ]. Thus,

𝑛∑︁−1

(1 − 𝛽)𝑖𝛽E[Δ˜ ].

E[E(𝑡+𝑛)] =

𝑖=0

where

𝑛∑︁−1

1 − (1 − 𝛽)𝑛 𝛽

1 · {1 − (1 − 𝛽)𝑛} 1 − (1 − 𝛽)

(1 − 𝛽)𝑖 =

=

.

𝑖=0

Subsequently, ignoring (1 − 𝛽)𝑛, we approximate E[E(𝑡+𝑛)] as

E[E(𝑡+𝑛)] = [1 − (1 − 𝛽)𝑛]E[Δ˜ ] ≈ E[Δ˜ ]. Next, we consider the covariance Cov[E(𝑡+𝑛)]:

Cov[E(𝑡+𝑛)] = E[E(𝑡+𝑛) (E(𝑡+𝑛))⊤] − E[E(𝑡+𝑛)](E[E(𝑡+𝑛)])⊤. We first determine the exact expression for E(𝑡+𝑛)(E(𝑡+𝑛))⊤ as follows:

𝑛∑︁−1

###### (1 − 𝛽)2𝑖Δ˜ (𝑡+𝑛−1−𝑖) (Δ˜ (𝑡+𝑛−1−𝑖))⊤

E(𝑡+𝑛) (E(𝑡+𝑛))⊤ = 𝛽2

𝑖=0

𝑛∑︁−1

###### (1 − 𝛽)𝑖(1 − 𝛽)𝑗Δ˜ (𝑡+𝑛−1−𝑖) (Δ˜ (𝑡+𝑛−1−𝑗))⊤.

+ 𝛽2

𝑖,𝑗=0:𝑖≠𝑗

Note that, for 𝑖, 𝑗 ∈ {0, . . .,𝑛 − 1}(𝑖 ≠ 𝑗), E[Δ˜ (𝑡+𝑛−1−𝑖)(Δ˜ (𝑡+𝑛−1−𝑗))⊤] = E[Δ˜ ](E[Δ˜ ])⊤ because we assume that they are not correlated. For 𝑖 ∈ {0, . . .,𝑛 − 1}, E[Δ˜ (𝑡+𝑛−1−𝑖)(Δ˜ (𝑡+𝑛−1−𝑖))⊤] = E[Δ˜ ](E[Δ˜ ])⊤ + Cov[Δ˜ ]. Thus,

###### E[E(𝑡+𝑛) (E(𝑡+𝑛))⊤]

𝑛∑︁−1

###### (1 − 𝛽)2𝑖 E[Δ˜ ](E[Δ˜ ])⊤ + Cov[Δ˜ ]

= 𝛽2

𝑖=0

𝑛∑︁−1

(1 − 𝛽)𝑖(1 − 𝛽)𝑗E[Δ˜ ](E[Δ˜ ])⊤,

+ 𝛽2

𝑖,𝑗=0:𝑖≠𝑗

𝑛∑︁−1

(1 − 𝛽)2𝑖 Cov[Δ˜ ].

= E[E(𝑡+𝑛)](E[E(𝑡+𝑛)])⊤ + 𝛽2

𝑖=0

Therefore,

Cov[E(𝑡+𝑛)] = E[E(𝑡+𝑛) (E(𝑡+𝑛))⊤] − E[E(𝑡+𝑛)](E[E(𝑡+𝑛)])⊤

𝑛∑︁−1

(1 − 𝛽)2𝑖 Cov[Δ˜ ].

= 𝛽2

𝑖=0

Here,

𝑛∑︁−1

1 − (1 − 𝛽)2𝑛 𝛽(2 − 𝛽)

1 − (1 − 𝛽)2𝑛 1 − (1 − 𝛽)2

(1 − 𝛽)2𝑖 =

=

.

𝑖=0

Thus, by ignoring (1 − 𝛽)2𝑛, Cov[E(𝑡+𝑛)] can be approximated as

𝛽 2 − 𝛽

Cov[Δ˜ ],

Cov[E(𝑡+𝑛)] = [1 − (1 − 𝛽)2𝑛]

𝛽 2 − 𝛽

Cov[Δ˜ ].

≈

Therefore, E(𝑡+𝑛) approximately follows the following distribution:

𝛽 2 − 𝛽

E(𝑡+𝑛) ∼ D E[Δ˜ ],

Cov[Δ˜ ] .

Thus, the derivation of Eq. (38) is complete.

- A.2 Derivation of Estimates for ∥E[Δ˜ ]∥22 We organized the relation between E and Δ˜ using the following equation:


E[∥E∥22] = E[E]⊤𝐼E[E] + Tr(Cov[E]) ≈ ∥E[Δ˜ ]∥22 + Tr

𝛽 2 − 𝛽

Cov[Δ˜ ]

𝛽 2 − 𝛽

= ∥E[Δ˜ ]∥22 +

Tr(Cov[Δ˜ ]).

Now, we apply the same arguments to V and obtain:

E[V] = [1 − (1 − 𝛽)𝑡+1]E[∥Δ˜ ∥22] ≈ E[∥Δ˜ ∥22] = ∥E[Δ˜ ]∥22 + Tr(Cov[Δ˜ ]).

By reorganizing these arguments, we obtain

2 − 𝛽 2 − 2𝛽

𝛽 2 − 2𝛽

∥E[Δ˜ ]∥22 ≈

E[∥E∥22] −

#### E[V].

2−2𝛽 ∥E∥22 − 2−𝛽2𝛽 V for ∥E[Δ˜ ]∥22.

This provides the rationale for estimating 2−𝛽

### B THEORETICAL AND EMPIRICAL INSIGHTS INTO SNR

In Section 4, we assumed that the signal-to-noise ratio (SNR) is relatively small, for example, SNR ⪅ 1, which validates the approximation 1/(1+SNR−1) ≈ SNR. In this section, we theoretically and empirically discuss the validity of SNR ⪅ 1.

To obtain useful insights into this SNR from a theoretical perspective, we considered observing it in a situation wherein the objective function is the sphere function 𝑓 (𝑥) = ∥𝑥∥2 and the covariance matrix is Σ = 𝜎2𝐼, where𝜎 = 𝜎¯ ∥𝑚𝑑 ∥ and𝜎¯ is called the normalized step-size. The quality gain analysis [Akimoto et al. 2020; Arnold 2005] implies that for a sufficiently large 𝑑, the distribution of the 𝑖th ranked solution among the 𝜆 candidate solutions is approximated as 𝑋𝑖:𝜆 = 𝑚 + 𝜎N𝑖:𝜆 ∥𝑚𝑚∥ + 𝜎N𝑖⊥, where N𝑖:𝜆 is the 𝑖th order statistics among 𝜆 normally distributed random variables and N𝑖⊥ is an independently distributed 𝑑 dimensional normal random vector with covariance matrix 𝐼 − 𝑚𝑚∥𝑚∥T2 if𝑚 ≠ 0. Using this approximation, we obtain Δ𝑚 = 𝜎 𝑖 𝜆=1𝑤𝑖N𝑖:𝜆 ∥𝑚 𝑚∥ +𝜎 𝑖 𝜆=1𝑤𝑖N𝑖⊥ . Let 𝒘 = (𝑤1, . . .,𝑤𝜆), 𝒏(𝜆) = (E[N1:𝜆], . . ., E[N𝜆:𝜆]). 𝑵(𝜆) is a matrix whose (𝑖, 𝑗)th element is E[N𝑖:𝜆N𝑗:𝜆]. Then, we obtain

𝑚 ∥𝑚∥

E[Δ𝑚] = 𝜎(𝒘T𝒏(𝜆))

E[Δ𝑚Δ𝑚T ] = 𝜎2(𝒘T𝑵(𝜆)𝒘)

, (44a)

𝑚𝑚T ∥𝑚∥2

𝑚𝑚T ∥𝑚∥2

+ 𝜎2∥𝒘∥2 𝐼 −

. (44b)

###### Sphere

###### Schaﬀer

###### Rastrigin

hist() SNRm

1000

2000

100

0

0

0

−0.02 0.00 0.02 0.04 0.06 0.08 0.10

−0.02 0.00 0.02 0.04 0.06 0.08 0.10

−0.02 0.00 0.02 0.04 0.06 0.08 0.10

20000

200

4000

hist() SNRΣ

100

10000

2000

0

0

0

0 1 2 3

0 1 2 3

0 1 2 3

- Fig. 17. Histogram of the estimated SNR in typical trials on 30-D noiseless problems. Estimated SNR with respect to (top) the mean vector 𝑚 and (bottom) the covariance matrix Σ. The SNR was estimated using the method described in Section 4.2.


Because 𝐹𝑚 = 𝜎−2𝐼, we obtain SNR =

𝜎−2∥E[Δ𝑚]∥2 𝜎−2 Tr(E[Δ𝑚Δ𝑚T ]) − 𝜎−2∥E[Δ𝑚]∥2

(45a)

= (𝒘T𝒏(𝜆))2

(45b)

𝒘T𝑵(𝜆)𝒘 + (𝑑 − 1)∥𝒘∥2 − (𝒘T𝒏(𝜆))2

(𝒘T𝒏(𝜆))2 (𝑑 − 1)∥𝒘∥2

(45c)

≈

(𝒘T𝒏(𝜆))2 ∥𝒘∥2

1 𝑑 − 1

(45d)

=

(𝒘T𝒏(𝜆))2 ∥𝒘∥2∥𝒏(𝜆)∥2

𝜆 𝑑 − 1

. (45e)

≈

Here, we used the following asymptotically true approximations for 𝜆 (See Eq. (A2) provided in [Akimoto et al. 2020]):

𝒘T𝑵(𝜆)𝒘 (𝒘T𝒏(𝜆))2

≈ 1 and ∥𝒏(𝜆)∥2

𝜆 ≈ 1. (46) It should be noted that (𝒘

T𝒏(𝜆) )2

∥𝒘∥2∥𝒏∥2 is upper bounded by 0.25 if only non-negative weights are used for the 𝑚-update, which aligns with our weight scheme. Therefore, we can expect that SNR ⪅ 1 holds if 𝜆 is not considerably large relative to 𝑑; for example, 𝜆 ⩽ 4(𝑑 − 1). Importantly, in difficult problems, such as multimodal problems, the SNR tends to be smaller than that in the sphere functions. Therefore, it should be noted that the assumption of SNR ≲ 1 becomes more easily valid for such difficult problems.

The main limitation of the aforementioned analysis is the assumption that the dimension 𝑑 and the population size 𝜆 are sufficiently large. To verify whether the assumption SNR ⪅ 1 works in practice, we conducted experiments using the LRA-CMA-ES for 30-dimensional Sphere, Schaffer, and Rastrigin functions using the same settings as those mentioned in Section 5.1, and 𝜆 = 14 for 𝑑 = 30. Figure 17 illustrates the typical behavior of the estimated SNR where it was estimated using the method described in Section 4.2. It should be noted that this value includes estimation errors. Although the estimated SNR for the covariance in the Sphere function tends to be slightly larger, it often remains under 1, particularly for more difficult problems such as the Rastrigin function. These results suggest that the assumption of SNR to be small, e.g., SNR ⪅ 1, appears to be valid to a certain degree even under finite dimensions and population sizes.

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

- Fig. 18. Success rate and SP1 values with hyperparameter 𝛽Σ ∈ {0.01, 0.02, ..., 0.05} on 30-D noiseless problems.


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

Fig. 19. Success rate and SP1 values with hyperparameter 𝛽𝑚 for 30-D noiseless problems.

### C ADDITIONAL EXPERIMENTAL RESULTS

Figure 18 shows the success rate and SP1 values with respect to 𝛽Σ ∈ {0.01, 0.02, ..., 0.05} for the 30-D noiseless Sphere, Schaffer, and Rastrigin functions. Clearly, the performance is not significantly affected by 𝛽Σ values within this range. However, as shown in Figure 10, an excessively small 𝛽Σ value decelerates the convergence for the Rastrigin function.

Figures 19 and 20 show the success rates and SP1 values for 𝛽𝑚 and 𝛾, respectively. The results show that the performance is relatively stable against these hyperparameters.

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

Fig. 20. Success rate and SP1 values with hyperparameter 𝛾 for 30-D noiseless problems.

