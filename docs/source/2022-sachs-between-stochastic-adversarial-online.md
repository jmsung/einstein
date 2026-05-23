---
type: source
kind: paper
title: "Between Stochastic and Adversarial Online Convex Optimization: Improved Regret Bounds via Smoothness"
authors: Sarah Sachs, Hédi Hadiji, Tim van Erven, Cristóbal Guzmán
year: 2022
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/2202.07554v2
source_local: ../raw/2022-sachs-between-stochastic-adversarial-online.pdf
topic: general-knowledge
cites:
---

arXiv:2202.07554v2[cs.LG]8Jun2022

![image 1](<2022-sachs-between-stochastic-adversarial-online_images/imageFile1.png>)

BETWEEN STOCHASTIC AND ADVERSARIAL ONLINE CONVEX OPTIMIZATION: IMPROVED REGRET BOUNDS VIA SMOOTHNESS

![image 2](<2022-sachs-between-stochastic-adversarial-online_images/imageFile2.png>)

Sarah Sachs University of Amsterdam Korteweg-de Vries Institute for Mathematics s.c.sachs@uva.nl

Tim van Erven University of Amsterdam Korteweg-de Vries Institute for Mathematics tim@timvanerven.nl

Hedi´ Hadiji University of Amsterdam Korteweg-de Vries Institute for Mathematics hedi.hadiji@gmail.com

Cristobal´ Guzman´ University of Twente Department of Applied Mathematics Pontiﬁcia Universidad Cato´lica de Chile Institute for Mathematical and Computational Eng. c.a.guzmanparedes@utwente.nl

7. June 2022

ABSTRACT

Stochastic and adversarial data are two widely studied settings in online learning. But many optimization tasks are neither i.i.d. nor fully adversarial, which makes it of fundamental interest to get a better theoretical understanding of the world between these extremes. In this work we establish novel regret bounds for online convex optimization in a setting that interpolates between stochastic i.i.d. and fully adversarial losses. By exploiting smoothness of the expected losses, these bounds replace a dependence on the maximum gradient length by the variance of the gradients, which was previously known only for linear losses. In addition, they weaken the i.i.d. assumption by allowing, for example, adversarially poisoned rounds, which were previously considered in the expert and bandit setting. Our results extend this to the online convex optimization framework. In the fully i.i.d. case, our bounds match the rates one would expect from results in stochastic acceleration, and in the fully adversarial case they gracefully deteriorate to match the minimax regret. We further provide lower bounds showing that our regret upper bounds are tight for all intermediate regimes in terms of the stochastic variance and the adversarial variation of the loss gradients.

- 1 Introduction


Two of the main approaches for solving convex optimization problems under uncertain data are stochastic convex optimization (SCO) [Nemirovsky and Yudin, 1985, Shapiro et al., 2014] and online convex optimization (OCO) [Zinkevich, 2003]. These two models are very different in their assumptions and goals, despite the fact that they share many techniques. In SCO it is assumed that the loss functions follow an independent, identically distributed (i.i.d.) process, and the goal is to minimize the excess risk, which is the optimization error under the expected loss. By contrast, in OCO the losses can be choosen adversarially and the goal is to minimize the cumulative regret, which is the difference between the cumulative incurred losses over rounds against the best ﬁxed strategy in hindsight. Much less is known about what happens in between, in scenarios that interpolate between the i.i.d. and adversarial settings. This intermediate setting has drawn major attention in the recent years in the expert and bandit setting [Ito, 2021] [Amir et al., 2020] [Zimmert and Seldin, 2019], however, as mentioned in [Ito, 2021], little is known for online convex optimization. Our work studies this in a generalization of the OCO setting, in which nature chooses distributions for the data that may vary arbitrarily over time, and we provide regret bounds in terms of two quantities that measure

how adversarially these distributions are. The standard OCO setting corresponds to the case where the distributions are point-masses on adversarial data points.

Main Contribution. Our main contribution is a new analysis of optimistic online algorithms [Rakhlin and Sridharan, 2013a, Rakhlin and Sridharan, 2013b] that takes advantage of smoothness of the expected loss. This analysis allows for a gradual interpolation between worst-case adversarial regret bounds and the best known expected regret bounds in the stochastic case, and also provides quantiﬁable improvements for intermediate cases.1 To capture the full range between i.i.d. and fully adversarial settings, we consider a similar adversarial model as in [Rakhlin et al., 2011], i.e., nature chooses distributions Dt in iteration t, and the learner suffers loss ft(xt,ξt) with ξt ∼ Dt. Importantly, we do not assume that the distributions Dt are all the same, but they may vary adversarially over time.

To properly quantify the interpolation between the i.i.d. and fully adversarial settings in the regret bound, we introduce two parameters for the loss sequence. Namely the cumulative variance, σT, which captures the stochastic aspect of the learning task, i.e., the variance of the Dt; and the cumulative adversarial variation, ΣT, which captures the adversarial difﬁculties of the data, i.e., the difference between Eξ∼D

![image 4](<2022-sachs-between-stochastic-adversarial-online_images/imageFile4.png>)

![image 5](<2022-sachs-between-stochastic-adversarial-online_images/imageFile5.png>)

[∇f(·,ξ)]. With these two key

[∇f(·,ξ)] and Eξ∼D

t−1

t

quantities, our ﬁrst main result in Theorem 5 shows that the expected regret E[RT(u)], that is the difference of the cumulative losses of the learner and a ﬁxed solution in hindsight, is bounded by

√

E[RT(u)] = O D(¯σT + Σ¯T)

![image 6](<2022-sachs-between-stochastic-adversarial-online_images/imageFile6.png>)

T + LD2 , (1) where L is the smoothness constant of the expected functions Ft = Eξ∼D

[f(·,ξ)]. If, in addition, the functions Ft are µ-strongly convex, then in Theorem 7 we obtain

t

E[RT(u)] = O

1 µ

![image 7](<2022-sachs-between-stochastic-adversarial-online_images/imageFile7.png>)

σmax2 + Σ2max log T + LD2κ logκ .

Both bounds are tight: we prove matching lower bounds in Theorems 6 and 8. In Section 3.1 we show that our results match the known adversarial regret bounds as well as the best results in the i.i.d. case. For the latter, only the linear case was so far obtained directly via a regret analysis (see Sec. 5.2 in [Rakhlin and Sridharan, 2013a], and prior work [Hazan and Kale, 2010, Chiang et al., 2012]). Using optimistic mirror descent, they obtained the regret

![image 8](<2022-sachs-between-stochastic-adversarial-online_images/imageFile8.png>)

guarantee of RT(u) O( Tt=1  ∇f(xt,ξt) − mt 2), where mt denotes an optimistic guess of the gradient that is chosen before round t. In the i.i.d. case with the prediction mt = ∇f(xt−1,ξt−1), this can be shown to imply that

the expected regret is upper bounded by E[RT(u)] = O(σ√T + Tt=1 E[ ∇Ft(xt) − ∇Ft(xt−1) 2]), where σ denotes the variance of the stochastic gradients. This simpliﬁes to

![image 9](<2022-sachs-between-stochastic-adversarial-online_images/imageFile9.png>)

![image 10](<2022-sachs-between-stochastic-adversarial-online_images/imageFile10.png>)

√

![image 11](<2022-sachs-between-stochastic-adversarial-online_images/imageFile11.png>)

T) for the i.i.d. case with linear functions ∇Ft,

E[RT(u)] = O(σ

which is a special case of (1), because σ = σ¯T and Σ¯T = 0 for i.i.d. losses, and ∇Ft(xt) = ∇Ft(xt−1) and L = 0 for linear functions. It is not immediately obvious how to generalize this result to general convex functions with smoothness L > 0, however. In this case, we can guess the appropriate regret bound based on known convergence results for stochastic accelerated gradient descent (SAGD) [Joulani et al., 2020, Ghadimi and Lan, 2012]: if we knew in advance that the losses would be i.i.d. and we did not care about computational efﬁciency, then we could run a new instance of SAGD for each round t. Summing the known rate for SAGD over t then gives E[RT(u)]

√

![image 12](<2022-sachs-between-stochastic-adversarial-online_images/imageFile12.png>)

O(σ

T + L) (for more details see the batch-to-online conversion in Appendix D). This raises the question if a similar bound can also be obtained directly via a regret analysis, without assuming i.i.d. observations in advance. This question is then answered by our result (1), which indeed reduces to this rate for general convex smooth i.i.d. functions, matching the aforementioned bound up to constants. We achieve this by using smoothness to bound E[ ∇Ft(xt) − ∇Ft(xt−1) 2] L E[ xt − xt−1 2], which can be canceled by a negative quadratic term that we obtain from an improved analysis of the regret. The use of this negative term in the analysis dates back to [Nemirovski, 2005], who used it to achieve an improved O(1/T) rate on the extra-gradient method.

In addition to unifying the analysis of these two extreme cases and obtaining the best known results via one algorithm (OFTRL (2) for convex functions and OFTRL on a surrogate loss (5) for strongly convex functions), our results give a new insight for intermediate cases. Thus, as a second main contribution we shed light on a setting which is neither fully adversarial nor i.i.d.. To illustrate this, we highlight some examples here, which received attention in the recent literature.

![image 13](<2022-sachs-between-stochastic-adversarial-online_images/imageFile13.png>)

1It is well-known that in the fully adversarial case smoothness does not yield asymptotic improvements on regret [Hazan, 2016], whereas for SCO improvements can be obtained only under low-noise [Ghadimi and Lan, 2012].

Adversarial corruptions: Consider i.i.d. functions with adversarial corruptions, as considered in the context of the expert and bandit settings in [Ito, 2021], [Amir et al., 2020]. If the (cumulative) corruption level is bounded by

a constant C, in [Ito, 2021] an expected regret bound of E[RT(u)] = O(RTs + CRTs ) was obtained, where RTs denotes the regret with respect to the uncorrupted data. In [Ito, 2021], the authors raised the question of whether it

![image 15](<2022-sachs-between-stochastic-adversarial-online_images/imageFile15.png>)

is possible to obtain regret bounds with a similar square-root dependence on the corruption level C for online convex optimization. Indeed, for this intermediate model, we derive a regret bound

√

![image 16](<2022-sachs-between-stochastic-adversarial-online_images/imageFile16.png>)

E[RT(u)] O(RTs + D

GC), for the general convex case from our Theorem 5. We elaborate on this in Section 4.2.

Random order models The random order model (ROM) dates back to [Kenyon, 1997] in combinatorial online learning. It has drawn attention in the online convex optimization community as an elegant relaxation of the adversarial model [Sherman et al., 2021, Garber et al., 2020]. Complementary to the results in [Sherman et al., 2021], we show that the dependence on G in the regret bound can be reduced to a dependence of σ, where σ denotes the variance of gradients in the uniform distribution over loss functions f1,...fT. That is,

![image 17](<2022-sachs-between-stochastic-adversarial-online_images/imageFile17.png>)

σ σ

E[RT(u)] O Dσ T log e

![image 18](<2022-sachs-between-stochastic-adversarial-online_images/imageFile18.png>)

,

where σ denotes a slightly weaker notion of variance (see Corollary 10). We derive these results from our main theorem under stronger assumptions than in [Sherman et al., 2021], but we also obtain a better rate with σ instead of G as the leading factor, so the results are not directly comparable. We also consider a variant of the random order model, which we call the multiple pass random order model (multi-pass ROM). This is inspired by multiple shufﬂe SGD and can be considered another intermediate example between adversarial and stochastic data. We elaborate on both examples, i.e., the ROM and multi-pass ROM in Section 4.3.

- 1.1 Related work


As mentioned in the previous section, our work is inspired by results in the gradual variation and in the stochastic approximation literature. The gradual variation literature dates back to [Hazan and Kale, 2010], with later extensions by [Chiang et al., 2012] and [Rakhlin and Sridharan, 2013a, Rakhlin and Sridharan, 2013b]. In addition to some technical relation to the aforementioned work, there is also a natural relation between our parameters σ¯T and Σ¯T to variational parameters in [Yang et al., 2013], [Hazan and Kale, 2010] or [Chiang et al., 2012]. However, as we elaborate in Remark 4, there are some fundamental differences between these variational parameters and σ¯T,Σ¯T, which prevent us from directly obtaining a smooth interpolation from these results. It is also interesting to note that there is some relation between Σ¯T and the path length parametersconsidered in dynamic regret bounds[Zhao et al., 2021, Zhao et al., 2020]. However, since their analysis targets a fundamentally different notion of regret, namely the dynamic regret, the results are incomparable.

With respect to the results, our ﬁndings are fundamentally different from the stochastic approximation literature, since we do not rely on the assumption that the data is following a distribution. However, we were inspired by analysis techniques and the convergence thresholds set by this literature. Our approach of obtaining accelerated rates by negative terms arising from smoothness in a regret bound has previously been used in the context of variational inequalities and saddle-point problems. Using this idea, [Nemirovski, 2005] obtained improved rates O(1/T) for the extra-gradient method. More recently [Joulani et al., 2020] showed that acceleration in stochastic convex optimization can beneﬁt by negative terms arising in optimistic FTRL via an anytime-online-to-batchconversion [Cutkosky, 2019]. Although an important inspiration for our approach, the techniques of [Joulani et al., 2020] do not directly carry over, because they evaluate gradients at the time-average of the algorithm’s iterates, making them much more stable than the last iterate, which comes up when controlling the regret. Algorithms used both in SCO and OCO follow a vast literature on stochastic approximation methods, e.g. [Robbins and Monro, 1951, Nemirovsky and Yudin, 1985, Polyak and Juditsky, 1992]. For this work, we are particularly interested in the more recent literature on acceleration in SCO [Ghadimi and Lan, 2012, Jain et al., 2018, Joulani et al., 2020]. In this research ﬁeld efﬁciency is traditionally measured in terms of excess risk. On the one hand, regret upper bounds can be converted into excess risk bounds, through the so-called online-to-batch conversions [Cesa-Bianchi et al., 2002]; on the other hand, excess risk guarantees do not directly lead to regret bounds, and even if they do some key features of the rates might be lost. These latter methods, known as batch-to-online conversions are discussed in Appendix D.

Outline In Section 2, after setting up notation and basic deﬁnitions, we introduce the stochastically extended adversarial model, a generalization of the standard adversarial model similar to the model used in smoothed analysis. Our main results can be found in Section 3. In Section 4 we illustrate our results by highlighting several special cases, such

as the random order model and the adversarially corrupted stochastic model. Finally, in Section 5 we set our ﬁndings into a broader context and give perspective for future work.

- 2 Setting


We recall the online convex optimization (OCO) problem. Here, we consider a sequence of convex functions f1,...fT deﬁned over a closed and bounded convex set X ⊆ Rd, which become available to the learner sequentially. In the

standard adversarial model, the learner chooses xt ∈ X in round t, then function ft is revealed and the learner suffers loss ft(xt). The success of the learner is measured against all ﬁxed u ∈ X. Hence, the goal of the learner is to

minimize the regret, that is, the difference between their cumulative loss Tt=1 ft(xt) and that of the best ﬁxed choice in hindsight, namely minu∈X Tt=1 ft(u). Throughout the paper we use the notation [T] = {1,...,T}. We follow the notation convention that δc denotes a Dirac measure at a point c, and · denotes the euclidean norm.

- 2.1 Stochastically Extended Adversarial Model


We extend the aforementioned adversarial model by letting nature choose a distribution Dt from a set of distributions. Then the learner suffers loss f(xt,ξt) where ξt ∼ Dt. Note that if the set of distributions is sufﬁciently rich, this model contains the standard adversarial model and the stochastic model as a special cases (see Examples 1,2). We introduce some notation to make this more precise. Let X ⊂ Rd be a closed convex set and Ξ a measurable space. Deﬁne f : X×Ξ → R and assume f(·,ξ) is convex over ξ ∈ Ξ. Suppose D is a set of probability distributions over Ξ. For any D ∈ D, we denote the gradient mean by ∇FD(x) := Eξ∼D [∇f(x,ξ)] and the function mean FD(x) := Eξ∼D [f(x,ξ)]. Furthermore, denote by σD2 an upper bound on the variance of the gradients

Eξ∼D ∇f(x,ξ) − ∇FD(x) 2 .

σD2 = max x∈X

We introduce some shorthand notation when distributions are indexed by rounds. Given t ∈ [T], we write Ft and σt2 instead of FD

(x) and σD2

, respectively. Let us now introduce the stochastically extended adversary protocol.

t

t

- Deﬁnition 1 (Stochastically Extended Adversary (SEA)). In each round t, the learner chooses xt ∈ X, the SEA picks Dt ∈ D. The learner and the SEA both observe a sample ξt ∼ Dt, and the learner suffers loss f(xt,ξt).


Note that the SEA model is closely related to the adversarial model considered in the context of smoothed analysis [Rakhlin et al., 2011, Haghtalab et al., 2022, Spielman and Teng, 2004]. However, in contrast to this line of work, we do not focus our attention to SEA distributions with sufﬁcient anti-concentration (c.f., Def. 1.1 in [Haghtalab et al., 2022]). Indeed, this restriction would exclude, among others, the fully adversarial case as described below. Note also that we assume that SEA has access to the realization ξt, hence, can choose distribution Dt+1 based on ξ1,...,ξt. This assumption is not relevant for the fully adversarial nor the i.i.d. setting. In the former, because there is no randomness, and in the latter because there is no change in distribution. However, it is relevant for some of the intermediate cases, and in particular in the random order model. The SEA model contains several common settings from the literature as special cases. To illustrate this, we list some examples.

- 1. Adversarial Model: The SEA chooses a Dirac measure δc

t ∈ D in each round. Then for any ξt ∼ δc

t

, the SEA selects f(·,ξt), and the model reduces to an adversary selecting directly the functions ft(·).

- 2. Stochastic I.I.D. Model: The SEA chooses a ﬁxed D ∈ D and selects Dt = D at each round t.
- 3. Adversarially Corrupted i.i.d. Model: The adversaryselects an i.i.d. source D and perturbsthe data with adversarial corruptions. This ﬁts in our framework by considering that, given a corruption level C 0, the SEA

chooses distributions Dt = D⊗δc

t

such that Tt=1 supx∈X Eξ∼D [∇f(x,ξ)] − Eξ′∼Dt [∇f(x,ξ′)] C.

- 4. Random Order Models (ROM): Among a ﬁxed family of losses F = (fi, i ∈ [n]), the SEA randomly picks functions in F via sampling without replacement, possibly performing multiple passes over the losses and reshufﬂing between the passes. Formally, deﬁne Ξ = [n], and ξt ∈ Ξ to be the t-th loss pick; if t ∈ [nk,n(k + 1)] for some k ∈ N, then the SEA chooses the distribution Dt = Unif(Ξ \ {ξs : s ∈ [nk + 1,n(t − 1)]}).


To quantify the hardness of the loss sequence, we introduce the cumulative stochastic variance and adversarial variation; we also deﬁne an average of these quantities. We denote by E the expectation taken with respect to the joint

distribution of (x1,ξ1,...,xT,ξT). Note that the choice of the adversary Dt can be random itself, as it depends on the past observations (of both the player’s actions and the realizations of the ξt’s). In this case, σt is also a random quantity.

- Deﬁnition 2 (Cumulative Stochastic Variance and Cumulative Adversarial Variation). Suppose the SEA chooses dis-

tributions D1,...,DT. Recall that σt2 is a shorthand for σD2

t

. The cumulative stochastic variance and the cumulative adversarial variance are deﬁned as

σ[1:(2)T] = E

T

t=1

σt2 and Σ(2)[1:T] = E

T

t=1

sup

x∈X

∇Ft(x) − ∇Ft−1(x) 2 .

We also let σ¯T and Σ¯T denote the square root of the average stochastic variance or adversarial variation, respectively; that is, σ¯T2 = σ[1:(2)T]/T and Σ¯2T = Σ(2)[1:T]/T.

Note that in the special case when all ft are fully adversarial, σ¯T = 0. On the contrary, in the stochastic case, i.e., if all for each round t, the distribution Dt is equal to a ﬁxed (but arbitrarily chosen) D, then Σ¯T = 0. In this case, σ¯T reduces to the common deﬁnition of the gradient variance upper bound in the SCO literature [Ghadimi and Lan, 2013, Ghadimi and Lan, 2012]. If however, the SEA chooses one distribution Di for the ﬁrst rounds and then switches to a different distribution Dj, then σ¯T can only be upper bounded by max(σi,σj). This upper bound can be pessimistic, however, for some results it gives a better intuition. For this purpose we also deﬁne the maximal stochastic variance and maximal adversarial variation.

- Deﬁnition 3 (Maximal Stochastic Variance and Maximal Adversarial Variation). Let σmax2 be an upper bound on all variances σt2. That is,


∇Ft(x) − ∇Ft−1(x) 2 .

E σt2 and Σ2max = max t∈[T]

σmax2 = max t∈[T]

E sup

x∈X

Remark 4. As we mentioned in the introduction, the cumulative stochastic variance and the adversarial variation have some similarities with parameters in gradual variation regret bounds. For linear functions µt,· , the bounds in [Hazan and Kale, 2010] involve the parameter VarT = Tt=1 µt − µ¯T 2 where µ¯T is the average of the gradients. For OCO with general convex functions, [Chiang et al., 2012] provide upper bounds on the regret in terms of the Lp-deviation Dp = Tt=1 supx∈X  ∇ft(x) − ∇ft−1(x) 2p. In Lemmas 13 and 14 in Appendix A, we show that in the SEA framework, both of these types of bounds are generally worse than ours, and that the difference can be arbitrarily large. In [Rakhlin and Sridharan, 2013b] the regret is bounded in terms of Tt=1 gt − Mt 2. As mentioned in the introduction, unless the loss functions are linear or the learner has knowledge of the gradient mean, Tt=1 gt−Mt 2 cannot directly be reduced to σ[1:(2)T] or Σ(2)[1:T].

- 2.2 Assumptions

In our analysis we will frequently use several of the following additional assumptions. Some of these were already mentioned in the introduction. We keep them all together here, for the convenience of the reader and clear reference. For any D ∈ D:

- (A0) the adversary has access to independent samples ξ ∼ D.
- (A1) the function f(·,ξ) is convex, and gradients are bounded by G a.s. when ξ ∼ D.
- (A2) the expected function FD is L-smooth, i.e, ∇FD is L-Lipschitz continuous.
- (A3) for any x ∈ X, the variance Eξ∼D[ ∇f(x,ξ) − ∇FD(x) 2] is ﬁnite.
- (A4) the expected function FD(·) is µ-strongly convex.


We assume that (A0) always holds. Assumptions (A1) ,(A2) and (A3) are standard in stochastic optimization, and are similar to common assumptions for online convex optimization. There, it is typically assumed that the adversarial samples ft(·) are convex (or even linear) and the gradient norms  ∇ft(·) are bounded. Note that we only require gradient Lipschitz continuity and strong convexity to hold for the expected loss.

3 Algorithms and Regret Bounds

- 3.1 Convex Smooth Functions


We use Optimistic Follow-the-Regularised-Leader (OFTRL) (see, e.g., [Joulani et al., 2017, Rakhlin and Sridharan, 2013a]) to minimize regret. Let (ηt)t∈[T] be a non-decreasing and positive sequence of

stepsizes, possibly tuned adaptively with the observations. At each step t, the learner makes an optimistic prediction Mt ∈ Rd and updates its iterates as

t−1

x 2 ηt

gs +

x,Mt +

xt = argmin

, (2)

![image 22](<2022-sachs-between-stochastic-adversarial-online_images/imageFile22.png>)

x∈X

s=1

where we denoted by gt = ∇f(xt,ξt) the observed gradient at time t. To state our results, we denote by E[·] the expectation with respect to the joint distribution of (x1,ξ1,...,xT,ξT). Our objective is to bound the average regret:

T

E[RT(u)] := E

gt,xt − u . The following theorem, proved in Appendix B.1, is our main result for convex functions.

t=1

- Theorem 5. Fix a user-speciﬁed parameter ν > 0. Under assumptions (A1) ,(A2) ,(A3) , OFTRL, with Mt = gt−1 and adaptive step-size ηt = D2/(ν + ts−=11 ηs gs − Ms 2), has regret

E[RT(u)] D 6 σ¯T + 3

√

![image 23](<2022-sachs-between-stochastic-adversarial-online_images/imageFile23.png>)

2Σ¯T

√

![image 24](<2022-sachs-between-stochastic-adversarial-online_images/imageFile24.png>)

T +

3√2DG 2

![image 25](<2022-sachs-between-stochastic-adversarial-online_images/imageFile25.png>)

![image 26](<2022-sachs-between-stochastic-adversarial-online_images/imageFile26.png>)

+ ν +

1 ν

![image 27](<2022-sachs-between-stochastic-adversarial-online_images/imageFile27.png>)

4D2G2 + 9L2D4 . (3)

The algorithm needs only the knowledge of D. With the extra knowledge of G and L, one can tune ν = LD2 + DG2 to get

E[RT(u)] O D σ ¯T + Σ¯T

√

![image 28](<2022-sachs-between-stochastic-adversarial-online_images/imageFile28.png>)

T + DG + LD2 . Moreover, if only convexity of the individual losses holds (A1) , then tuning ν = 2DG ensures the (deterministic) bound RT(u) 3√2DG√T + 4DG .

![image 29](<2022-sachs-between-stochastic-adversarial-online_images/imageFile29.png>)

![image 30](<2022-sachs-between-stochastic-adversarial-online_images/imageFile30.png>)

Without prior knowledge of the smoothness parameter, the best the player can do is to tune ν according to a guessed value L0. This affects the constants in the bound by an additive term of order (L0+L2/L0)D2; it would be interesting to determine if this is an inevitable price to pay for the lack of knowledge of L. A similar discussion can be held for G. Note that the worst-case regret bound of order DG√T always holds every time OFTRL is used in this article, even without smoothness. To avoid distraction, we will not recall this fact in the applications.

![image 31](<2022-sachs-between-stochastic-adversarial-online_images/imageFile31.png>)

The algorithm and analysis dwell on two ideas: the adaptive tuning of the learning rate a` la AdaHedge/AdaFTRL [McMahan, 2011, Orabona and Pa´l, 2018] with optimism, together with the fact that we keep a negative Bregman divergence term in the analysis, which is crucial to obtain our bound.

The upper bound in Theorem 5 is tight up to additive constants, as the following result shows.

- Theorem 6. For any learning algorithm, and for any pair of positive numbers (σ,Σ) there exists a function f :


X×Ξ → R and a sequence of distributions satisfying assumptions (A1) , (A2) ,(A3) with σ¯T σ and Σ¯T Σ such that

√

E[RT(u)] Ω D σ ¯T + Σ¯T

![image 32](<2022-sachs-between-stochastic-adversarial-online_images/imageFile32.png>)

T .

The proof, in Appendix B.2 relies on a lower bound from stochastic optimization [Agarwal et al., 2012, Nemirovsky and Yudin, 1985] together with the fact that we can construct a sequence of convex and L-smooth loss functions such that Σ¯T is in the order of the gradient norms G. Combining these insights with the lower bound Ω(DG

√

![image 33](<2022-sachs-between-stochastic-adversarial-online_images/imageFile33.png>)

T) [Orabona and Pa´l, 2018] gives the desired result.

- 3.2 Strongly Convex and Smooth Functions


Up to this point, we have only considered functions which satisfy the weaker set of assumptions (A1) ,(A2) ,(A3) . In this section, we show what improvements can be achieved if strong convexity also holds, that is, if (A4) is satisﬁed with some known parameter µ > 0. For gt = ∇f(xt,ξt), deﬁne the surrogate loss function

µ 2

x − xt 2 . (4)

ℓt(x) = gt,x − xt +

![image 34](<2022-sachs-between-stochastic-adversarial-online_images/imageFile34.png>)

We use Optimistic Follow-the-Leader (OFTL) on the surrogate losses. For each step t, the learner makes an optimistic prediction of the next gradient Mt ∈ Rd and selects

t−1

ℓs(x) + Mt,x . (5)

xt = argmin

x∈X

s=1

The next theorem is analogous to Theorem 5 for curved losses, and will be our main tool in establishing results for strongly convex losses; see Appendix B.3 for a proof.

- Theorem 7. Under assumptions (A1) –(A4) , the expected regret of OFTL with Mt = ∇f(xt−1,ξt−1) on surrogate loss functions ℓt deﬁned in (4) is bounded as

E[RT(u)]

1 µ

![image 36](<2022-sachs-between-stochastic-adversarial-online_images/imageFile36.png>)

T

t=1

1 t

![image 37](<2022-sachs-between-stochastic-adversarial-online_images/imageFile37.png>)

8σmax2 + 4E sup x∈X

∇Ft(x) − ∇Ft−1(x) 2 +

4D2L2 µ

![image 38](<2022-sachs-between-stochastic-adversarial-online_images/imageFile38.png>)

log 1 +

16L µ

![image 39](<2022-sachs-between-stochastic-adversarial-online_images/imageFile39.png>)

1 µ

![image 40](<2022-sachs-between-stochastic-adversarial-online_images/imageFile40.png>)

8σmax2 + 4Σ2max log T +

4D2L2 µ

![image 41](<2022-sachs-between-stochastic-adversarial-online_images/imageFile41.png>)

log 1 +

16L µ

![image 42](<2022-sachs-between-stochastic-adversarial-online_images/imageFile42.png>)

.

Note that OFTL requires no tuning besides the strong convexity parameter used in the surrogate losses. In particular, it is adaptive to the smoothness L.

Lower Bound The bound in Theorem 7 is tight, as the next result, proved in Appendix B.4 shows.

- Theorem 8. For any learning algorithm, and for any pair of positive numbers (σ,Σ) there exists a function f : X×Ξ → R and a sequence of distributions satisfying assumptions (A1) ,(A2) ,(A3) and (A4) with σmax σ and Σmax Σ such that


E[RT(u)] Ω

1 µ

![image 43](<2022-sachs-between-stochastic-adversarial-online_images/imageFile43.png>)

σmax2 + Σ2max log T .

- 4 Implications We derive consequences of our results from Section 3. Further examples can be found in Appendix E.


- 4.1 Interpolating Known Results: Fully Adversarial and i.i.d. Data A ﬁrst implication of our analysis is that we recoverboth the adversarialand i.i.d. rates, via a single adaptive algorithm.


Convex Case For adversarial data, σt = 0 for all t, and Σ2[1:T] G√2T. Thus, Theorem 5 guarantees a bound RT(u) O(DG√T), which is known to be the optimal rate up to the additive constants, cf. [Zinkevich, 2003] (note that the expectation does not act on the regret in this case). Simultaneously, if the data is i.i.d., then Theorem 5 guarantees that

![image 44](<2022-sachs-between-stochastic-adversarial-online_images/imageFile44.png>)

![image 45](<2022-sachs-between-stochastic-adversarial-online_images/imageFile45.png>)

√

![image 46](<2022-sachs-between-stochastic-adversarial-online_images/imageFile46.png>)

T + LD2 + DG . (6)

E[RT(u)] O Dσ

From standard online-to-batch conversion, this implies an excess risk for the related SCO problem of order O(Dσ/√T + D(LD + G)/T), which matches the well-known result by [Ghadimi and Lan, 2013] up to lower order terms. On the other hand, using batch-to-online conversion (see Appendix D) with the best known accelerated convergence result in SCO, gives O(Dσ

![image 47](<2022-sachs-between-stochastic-adversarial-online_images/imageFile47.png>)

√

![image 48](<2022-sachs-between-stochastic-adversarial-online_images/imageFile48.png>)

T + LD2) regret. Therefore, up to a constant, our result coincides with the best known results from SCO. Note that also generalizes the improvement obtained for linear functions in the i.i.d. setting in [Rakhlin and Sridharan, 2013a, Section 6.2].

Strongly Convex Case The adaptive interpolation between i.i.d. and adversarial rates also holds in the strongly convex case. For adversarial data, the bound of Theorem 7 is of order (G2/µ)logT, which is known to be the optimal worst-case rate, cf. [Hazan and Kale, 2011]. For i.i.d. data, the dependence on G2 improves to σ2, yielding a bound of order O((σ2/µ)logT + LD2κ logκ). This improvement is akin to improvements obtained by accelerated stochastic gradient descent in the context of stochastic optimization [Ghadimi and Lan, 2012, Joulani et al., 2020]. In fact, applying batch-to-online conversions and summing the optimization rates would yield a regret bound similar to ours; c.f. Appendix D.

- 4.2 Adversarially Corrupted Stochastic Data


We consider a natural generalization to online convex optimization of the corruption model considered in the bandit literature [Seldin and Slivkins, 2014, Zimmert and Seldin, 2019], also recently studied in [Ito, 2021] for prediction

with√C whereexpertCadvice.is the totalThere,amount ofthe authorperturbation.obtains a regretThey thenboundraisethattheisopenthe sumquestionof theofi.i.d.whether similarrate and of resultsa term couldof orderbe obtained for general convex losses. We provide a positive answer to this question in this section, with the regret bound in Corollary 9.

![image 49](<2022-sachs-between-stochastic-adversarial-online_images/imageFile49.png>)

In this model, the generating process of the losses is decomposed as a combination of losses coming from i.i.d. data, with a small additive adversarial perturbation. This ﬁts in the framework by setting ξt = (ξiid,t,ct) ∼ Dt = D ⊗ δc

t

and

f(x,ξt) = h(x,ξiid,t) + ct(x) where ct is the adversarial part of the losses selected by the adversary, and ξiid,t ∼ D is a sequence of identically distributed random variables. Note that, similarly to our inspirations [Ito, 2021, Seldin and Slivkins, 2014], and contrary to other corruption models for prediction with expert advice [Amir et al., 2020], we measure the regret against the perturbed data. Deﬁne F = Eξ∼D[h(·,ξ)], so that Ft(x) = F(x) + ct(x). The amount of perturbation is measured by a parameter C > 0 bounding

T

max

 ∇ct(x) C ,

x∈X

t=1

which is a natural measure of perturbation on the feedback used by the player (note that adding a constant to the perturbations does not change the regret). In this case, the adversarial perturbation on the loss does not affect the variance and σD2

= σD2 . The perturbation appears in the loss variation as for any t 2, for any x ∈ X,  ∇Ft(x) − ∇Ft−1(x) 2 2G ∇Ft(x) − ∇Ft−1(x)

t

= 2G ∇ct(x) − ∇ct−1(x) 2G  ∇ct(x) +  ∇ct−1(x) . Upon taking the supremum over x ∈ X and summing over t, we get (with the convention that c0 ≡ 0),

T

Σ(2)[1:T] =

 ∇ct(x) − ∇ct−1(x) 2 4GC .

sup

x∈X

t=1

Hence, Theorem 5 combined with the bounds on σ¯T and Σ¯T yields the following regret guarantee.

- Corollary 9. In the adversarially corrupted stochastic model, adaptive OFTRL enjoys the bound

E[RT(u)] = O Dσ

√

![image 51](<2022-sachs-between-stochastic-adversarial-online_images/imageFile51.png>)

T + D

√

![image 52](<2022-sachs-between-stochastic-adversarial-online_images/imageFile52.png>)

GC .

This regret bound is the sum of the i.i.d. rate for the unpertured source with a term sublinear in the amount of perturbations C, achieved without the prior knowledge of C. This provides an answer to the question of [Ito, 2021]. An interesting open question that remains would be to extend these results to strongly convex losses.

4.3 Random Order Models

We apply our results from Section 3 to the Random Order model. The online ROM was introduced by [Garber et al., 2020] as a way of restricting the power of the adversary in OCO. Our results highlight that the rates in the ROM model, which is not i.i.d., are almost the same as the rates of the i.i.d. model obtained via sampling in the same set of losses with replacement.

- Corollary 10. In the single-pass ROM with convex and L-smooth losses (fk)k∈[T], OFTRL (c.f. (2)) enjoys the regret bound


![image 53](<2022-sachs-between-stochastic-adversarial-online_images/imageFile53.png>)

σ1 σ1

T + LD2 + DG , where

E[RT(u)] O Dσ1 log e

![image 54](<2022-sachs-between-stochastic-adversarial-online_images/imageFile54.png>)

T

1 T

σ12 = max x∈X

![image 55](<2022-sachs-between-stochastic-adversarial-online_images/imageFile55.png>)

t=1

1 T

∇ft(x) −

T

∇fs(x)

![image 56](<2022-sachs-between-stochastic-adversarial-online_images/imageFile56.png>)

s=1

2

1 T

and σ12 =

T

max

![image 57](<2022-sachs-between-stochastic-adversarial-online_images/imageFile57.png>)

x∈X

t=1

1 T

∇ft(x) −

T

∇fs(x)

![image 58](<2022-sachs-between-stochastic-adversarial-online_images/imageFile58.png>)

s=1

2

.

Note that σ1 σ1 4G2, and that the logarithm of the ratio which appears in the bound is moderate in any reasonable scenario. The proof of Corollary 10 consists in controlling the adversarial variation and the cumulative variance thanks to the following lemma, proved in Appendix C.1.

Lemma 11. In the single-pass ROM, we have Σ(2)[1:T] 8G2 and σ¯[1:(2)T] Tσ12 log(2e2 σ12/σ12).

We would like to emphasize that our results are complementary to those of [Garber et al., 2020, Sherman et al., 2021]. The focus of these works is to relax the assumption that individual losses are convex, and to only require convexity of

the average loss function, leading to very different technical challenges. Inquiring if our results can also be achieved under the weaker assumptions of [Sherman et al., 2021] would be an interesting direction for future work.

We also consider the multi-pass ROM. Let P ∈ N denote the number of passes. From Lemma 11 and Corollary 10 we directly obtain

√

![image 60](<2022-sachs-between-stochastic-adversarial-online_images/imageFile60.png>)

σ1 σ1

E[RT(u)] O Dσ1 log e

T + DG

![image 61](<2022-sachs-between-stochastic-adversarial-online_images/imageFile61.png>)

![image 62](<2022-sachs-between-stochastic-adversarial-online_images/imageFile62.png>)

P + LD2 .

Combining Lemma 11 with Theorem 7 also gives the following corollary for strongly convex functions; see Appendix C.2 for a proof.

Corollary 12. Under the same assumption as in Theorem 7, the expected regret of the ROM is bounded by

σ12 µ

G2 µ

+ LD2κ logκ . For multi-pass ROM with P passes, we obtain

E[RT(u)] O

log T +

![image 63](<2022-sachs-between-stochastic-adversarial-online_images/imageFile63.png>)

![image 64](<2022-sachs-between-stochastic-adversarial-online_images/imageFile64.png>)

E[RT(u)] O

G2 µ

σ12 µ

log T +

![image 65](<2022-sachs-between-stochastic-adversarial-online_images/imageFile65.png>)

![image 66](<2022-sachs-between-stochastic-adversarial-online_images/imageFile66.png>)

G2 log P nµ

+ LD2κ log κ .

+

![image 67](<2022-sachs-between-stochastic-adversarial-online_images/imageFile67.png>)

- 5 Conclusion and future work


As we showed, exploitation of smoothness of the expected loss functions reduces the dependence of the regret bound on the maximal gradient norm to a dependence on the cumulative stochastic variance and the adversarial variation. Furthermore, we took a step towards a deeper theoretical understanding of the practically relevant intermediate scenarios. Our approach also opens several interesting new research directions. For instance, in the ROM, as mentioned in Section 4.3, an interesting question is whether a regret bound with dependence on σ instead of G can also be achieved with weaker assumptions as in [Sherman et al., 2021]. Another interesting question is whether it is possible to unify the analyses and algorithms for the strongly convex and convex case. So far our analyses of these cases were intrinsically different and the choice of the algorithm requires the knowledge of strong convexity constant µ. Since this knowledge might not be available, it is of practical interest to design an adaptive method which can automatically get the best rate without manually tuning for µ.

Social impact: this work is theoretical, and therefore does not entail any societal concerns.

Acknowledgements

Sachs, Hadiji and Van Erven were supported by the Netherlands Organization for Scientiﬁc Research (NWO) under grant number VI.Vidi.192.095. Guzma´n’s research is partially supported by INRIA through the INRIA Associate Teams project and the FONDECYT 1210362 project.

References

[Agarwal et al., 2012] Agarwal, A., Bartlett, P. L., Ravikumar, P., and Wainwright, M. J. (2012). Information-theoretic lower bounds on the oracle complexity of stochastic convex optimization. IEEE Transactions on Information Theory, 58(5):3235–3249.

[Amir et al., 2020] Amir, I., Attias, I., Koren, T., Mansour, Y., and Livni, R. (2020). Prediction with corrupted expert advice. In Advances in Neural Information Processing Systems 33 (NeurIPS), pages 14315–14325.

[Cesa-Bianchi et al., 2002] Cesa-Bianchi, N., Conconi, A., and Gentile, C. (2002). On the generalization ability of online learning algorithms. In Advances in Neural Information Processing Systems 14 (NeurIPS), volume 14.

[Chiang et al., 2012] Chiang, C.-K., Yang, T., Lee, C.-J., Mahdavi, M., Lu, C.-J., Jin, R., and Zhu, S. (2012). Online optimization with gradual variations. In Proceedings of the 25th AnnualConference on Learning Theory, volume 23 of Proceedings of Machine Learning Research, pages 6.1–6.20. PMLR.

[Cutkosky, 2019] Cutkosky, A. (2019). Anytime online-to-batch, optimism and acceleration. In Proceedings of the 36th International Conference on Machine Learning, volume 97 of Proceedings of Machine Learning Research, pages 1446–1454. PMLR.

[Garber et al., 2020] Garber, D., Korcia, G., and Levy, K. (2020). Online convex optimization in the random order model. In Proceedings of the 37th International Conference on Machine Learning, volume 119 of Proceedings of Machine Learning Research, pages 3387–3396. PMLR.

- [Ghadimi and Lan, 2012] Ghadimi, S. and Lan, G. (2012). Optimal stochastic approximation algorithms for strongly convex stochastic composite optimization i: A generic algorithmic framework. SIAM Journal on Optimization, 22(4):1469–1492.
- [Ghadimi and Lan, 2013] Ghadimi, S. and Lan, G. (2013). Stochastic ﬁrst- and zeroth-order methods for nonconvex stochastic programming. SIAM J. Optim., 23:2341–2368.


[Haghtalab et al., 2022] Haghtalab, N., Roughgarden, T., and Shetty, A. (2022). Smoothed analysis with adaptive adversaries. In 2021 IEEE 62nd Annual Symposium on Foundations of Computer Science (FOCS), pages 942–953. IEEE.

[Hazan, 2016] Hazan, E. (2016). Introduction to online convex optimization. Found. Trends Optim., 2(3?4):157?325.

- [Hazan and Kale, 2010] Hazan, E. and Kale, S. (2010). Extracting certainty from uncertainty: regret bounded by variation in costs. Machine Learning, 80:165–188.
- [Hazan and Kale, 2011] Hazan, E. and Kale, S. (2011). Beyond the regret minimization barrier: an optimal algorithm for stochastic strongly-convex optimization. In Proceedings of the 24th Annual Conference on Learning Theory, volume 19 of Proceedings of Machine Learning Research, pages 421–436. PMLR.


[Ito, 2021] Ito, S. (2021). On optimal robustness to adversarial corruption in online decision problems. In Advances in Neural Information Processing Systems 34 (NeurIPS), volume 34, pages 7409–7420.

[Jain et al., 2018] Jain, P., Kakade, S. M., Kidambi, R., Netrapalli, P., and Sidford, A. (2018). Accelerating stochastic gradient descent for least squares regression. In Conference On Learning Theory, pages 545–604. PMLR.

[Joulani et al., 2017] Joulani, P., Gyo¨rgy, A., and Szepesva´ri, C. (2017). A modular analysis of adaptive (non-) convex optimization: Optimism, composite objectives, and variational bounds. In International Conference on Algorithmic Learning Theory (ALT), pages 681–720. PMLR.

[Joulani et al., 2020] Joulani, P., Raj, A., Gyorgy, A., and Szepesva´ri, C. (2020). A simpler approach to accelerated optimization: iterative averaging meets optimism. In International Conference on Machine Learning, pages 4984–

4993. PMLR. [Kenyon, 1997] Kenyon, C. (1997). Best-ﬁt bin-packing with random order. In In 7th Annual ACM-SIAM Symposium on Discrete Algorithms, pages 359–364.

[McMahan, 2011] McMahan, B. (2011). Follow-the-regularized-leader and mirror descent: Equivalence theorems and l1 regularization. In Proceedings of the Fourteenth International Conference on Artiﬁcial Intelligence and Statistics, volume 15 of Proceedings of Machine Learning Research, pages 525–533. PMLR.

[Nemirovski, 2005] Nemirovski, A. (2005). Prox-method with rate of convergence o(1/t) for variational inequalities with lipschitz continuous monotone operators and smooth convex-concave saddle point problems. SIAM J. on Optimization, 15(1):229–251.

[Nemirovsky and Yudin, 1985] Nemirovsky, A. and Yudin, D. (1985). Problem complexity and method efﬁciency in

optimization. SIAM Review, 27(2):264–265. [Orabona, 2021] Orabona, F. (2021). A modern introduction to online learning. arXiv preprint: 1912.13213. [Orabona and Pa´l, 2018] Orabona, F. and Pa´l, D. (2018). Scale-free online learning. Theor. Comput. Sci., 716:50–69. [Polyak and Juditsky, 1992] Polyak, B. T. and Juditsky, A. B. (1992). Acceleration of stochastic approximation by

averaging. SIAM journal on control and optimization, 30(4):838–855.

- [Rakhlin and Sridharan, 2013a] Rakhlin, A. and Sridharan, K. (2013a). Online learning with predictable sequences. In Conference on Learning Theory, pages 993–1019. PMLR.
- [Rakhlin and Sridharan, 2013b] Rakhlin, A. and Sridharan, K. (2013b). Optimization, learning, and games with predictable sequences. In Advances in Neural Information Processing Systems 26 (NeurIPS), pages 3066–3074.


[Rakhlin et al., 2011] Rakhlin, A., Sridharan, K., and Tewari, A. (2011). Online learning: stochastic, constrained, and smoothed adversaries. In Advances in Neural Information Processing Systems 24 (NeurIPS), pages 1764–1772.

[Robbins and Monro, 1951] Robbins, H. and Monro, S. (1951). A stochastic approximation method. Annals of Mathematical Statistics, 22:400–407.

[Seldin and Slivkins, 2014] Seldin, Y. and Slivkins, A. (2014). One practical algorithm for both stochastic and adversarial bandits. In Proceedings of the 31st InternationalConference on Machine Learning, volume 32 of Proceedings of Machine Learning Research, pages 1287–1295. PMLR.

[Shapiro et al., 2014] Shapiro, A., Dentcheva, D., and Ruszczynski, A. (2014). Lectures on Stochastic Programming: Modeling and Theory, Second Edition. Society for Industrial and Applied Mathematics, USA.

[Sherman et al., 2021] Sherman, U., Koren, T., and Mansour, Y. (2021). Optimal rates for random order online optimization. In Advances in Neural Information Processing Systems 34 (NeurIPS), volume 34.

[Spielman and Teng, 2004] Spielman, D. A. and Teng, S.-H. (2004). Smoothed analysis of algorithms: Why the simplex algorithm usually takes polynomial time. Journal of the ACM (JACM), 51(3):385–463.

[Yang et al., 2013] Yang, T., Mahdavi, M., Jin, R., and Zhu, S. (2013). Regret bounded by gradual variation for online convex optimization. Machine Learning, 95(2):183–223.

- [Zhao et al., 2020] Zhao, P., Zhang, Y.-J., Zhang, L., and Zhou, Z.-H. (2020). Dynamic regret of convex and smooth functions. In Advances in Neural Information Processing Systems 33 (NeurIPS), pages 12510–12520.
- [Zhao et al., 2021] Zhao, P., Zhang, Y.-J., Zhang, L., and Zhou, Z.-H. (2021). Adaptivity and non-stationarity: Problem-dependent dynamic regret for online convex optimization. arXiv preprint arXiv:2112.14368.


[Zimmert and Seldin, 2019] Zimmert, J. and Seldin, Y. (2019). An optimal algorithm for stochastic and adversarial bandits. In Proceedings of the Twenty-Second International Conference on Artiﬁcial Intelligence and Statistics, volume 89 of Proceedings of Machine Learning Research, pages 467–475. PMLR.

[Zinkevich, 2003] Zinkevich, M. (2003). Online convex programming and generalized inﬁnitesimal gradient ascent. In Proceedings of the Twentieth International Conference on International Conference on Machine Learning, ICML’03, pages 928–935. AAAI Press.

- A Proofs of Section 2


Note that VarT = Tt=1  ∇ft(x) − µ∗T 2 can be understood as an empirical approximation of σ[1:(2)T]. The following lemma shows the relation of VarT to parameters σ[1:(2)T] and Σ(2)[1:T].

- Lemma 13. Deﬁne VarT = Tt=1  ∇ft(x) − µ∗T 2 with µ∗T = T1 Tt=1 ∇ft(x). In expectation with respect to distributions D1,...DT,

![image 71](<2022-sachs-between-stochastic-adversarial-online_images/imageFile71.png>)

E[VarT]

1 5

![image 72](<2022-sachs-between-stochastic-adversarial-online_images/imageFile72.png>)

σ[1:(2)T] + Σ(2)[1:T] .

Furthermore, there exists distributions such that E[VarT] is arbitrarily larger than σ[1:(2)T] + Σ(2)[1:T].

Proof. Since the distribution mean minimizes the least squares error, E[VarT] σ[1:(2)T] always holds. Using the same argument, we have

Σ(2)[1:T] =

T

t=1

∇Ft − ∇Ft−1 2 4

T

t=1

∇ft − ∇Ft 2 4

T

t=1

 ∇ft − µ∗T 2 = 4 VarT .

Consider X = [−1,1] and f(x,ξ) = ξx. Now suppose the SEA chooses truncated normal distribution with mean −2 for the ﬁrst T/2 rounds, then truncated normal distribution with mean 2 for the remaining rounds. Assume in both cases the variance is σ2 and truncation is in range [−G,G] for G > 0. Hence, for sufﬁciently large T,

µT = 0 and VarT = Tt=1 ft 2 ∝ TG2. However, σ[1:(2)T] is equal to Tσ2 which can be considerably smaller than TG2. The price for the distribution switch is captured with a small constant overhead by Σ(2)[1:T] 2G2. Thus, σ[1:(2)T] + Σ(2)[1:T] ∝ Tσ2 + 2G2.

![image 73](<2022-sachs-between-stochastic-adversarial-online_images/imageFile73.png>)

![image 74](<2022-sachs-between-stochastic-adversarial-online_images/imageFile74.png>)

![image 75](<2022-sachs-between-stochastic-adversarial-online_images/imageFile75.png>)

![image 76](<2022-sachs-between-stochastic-adversarial-online_images/imageFile76.png>)

- Lemma 14. Deﬁne Dp = Tt=1 supx∈X  ∇ft(x) − ∇ft−1(x) 2p . In the SEA framework,


- 1

![image 77](<2022-sachs-between-stochastic-adversarial-online_images/imageFile77.png>)

- 2


σ[1:(2)T] + Σ(2)[1:T] .

E[D2]

Furthermore, there exist instances such that E[D2] ≫ σ[1:(2)T] + Σ(2)[1:T].

Proof. We shall in fact prove that E[D2] max(σ[1:(2)T],Σ(2)[1:T]), which directly implies the ﬁrst part of the statement. Fix a time t 2 and let Gt−1 denote the σ-algebra generated by (x1,ξ1,...,ξt−1,xt). Then for any x ∈ X, the variable Ft(x) = E[ft(x)|Gt−1] is Gt−1-measurable, and we have

E  ∇ft(x) − ∇ft−1(x) 2 | Gt−1 sup

 ∇ft(x) − ∇ft−1(x) 2 Gt−1 sup x∈X

E sup

x∈X

E  ∇ft(x) − ∇Ft(x) 2 | Gt−1 = σt2

x∈X

since ft−1 = f(·,ξt−1) is Gt−1-measurable, and ∇Ft(x) = E ∇ft(x)|Gt−1 . Therefore, by conditioning on Gt−1 at time step t, and applying the tower rule, we obtain

E

T

 ∇ft(x) − ∇ft−1(x) 2 E

sup

x∈X

t=1

T

σt2 = σ[1:(2)T] .

t=1

The lower bound by Σ(2)[1:T] holds by a direct application of Jensen’s inequality, and by swapping suprema and expectations.

For the second part of the lemma, consider the d-dimensional euclidean ball X = Bd(1) ⊂ Rd, and Ξ = [d]. Deﬁne f(x,i) = x2i/2 .

Consider a fully stochastic (i.i.d.) SEA picking ξt ∈ [d] uniformly at random at every time step. Then Σ(2)[1:T] = 0. We shall now see that σ[1:(2)T] T/d. Indeed, for any x ∈ X and t ∈ [T], then Ft does not depend on t and its value is

d

- 1

![image 79](<2022-sachs-between-stochastic-adversarial-online_images/imageFile79.png>)

- 2d


x2i ,

F(x) = EI∼D[f(x,I)] =

i=1

which is a convex and smooth function. We can upper bound the variance, as for any x ∈ X,

d

1 d

EI∼D  ∇f(x,I) − ∇F(x) 2 EI∼D  ∇f(x,I) 2 = EI∼D xIeI 2 =

x2i

![image 80](<2022-sachs-between-stochastic-adversarial-online_images/imageFile80.png>)

i=1

1 d

.

![image 81](<2022-sachs-between-stochastic-adversarial-online_images/imageFile81.png>)

Therefore, after the taking the supremum over x ∈ X, we see that σt2 1/d. On the other hand, for any I,J ∈ [d], we have

 ∇f(x,I) − ∇f(x,J) 2 = xIeI − xJeJ 2 = (x2I + x2J)1{I = J} . The maximum in the ball of this difference is reached at x = √2/2(eI + eJ) and

![image 82](<2022-sachs-between-stochastic-adversarial-online_images/imageFile82.png>)

 ∇f(x,I) − ∇f(x,J) 2 = 1{I = J} . Therefore, if I and J are independent and uniformly distributed over [d], then

max

x∈X

1 d

 ∇f(x,I) − ∇f(x,J) 2 = P(I,J)∼D⊗D[I = J] = 1 −

E(I,J)∼D⊗D max x∈X

![image 83](<2022-sachs-between-stochastic-adversarial-online_images/imageFile83.png>)

2

1/4 .

Summarizing the above inequalities, we have built an example in which

E[D2]

T 4 ≫

T d

![image 84](<2022-sachs-between-stochastic-adversarial-online_images/imageFile84.png>)

![image 85](<2022-sachs-between-stochastic-adversarial-online_images/imageFile85.png>)

σ[1:(2)T] + Σ(2)[1:T] .

In particular, the expectation of the variation D2 can be arbitrarily larger than the cumulative variance, and our bounds are then tighter than those obtained via a direct application of known results.

![image 86](<2022-sachs-between-stochastic-adversarial-online_images/imageFile86.png>)

![image 87](<2022-sachs-between-stochastic-adversarial-online_images/imageFile87.png>)

![image 88](<2022-sachs-between-stochastic-adversarial-online_images/imageFile88.png>)

![image 89](<2022-sachs-between-stochastic-adversarial-online_images/imageFile89.png>)

- B Proofs of Section 3


- B.1 Proof of Theorem 5 To prove Theorem 5, we need the following well-known result from the literature.


 · 2. Further, let gt ∈ ∂ft(xt) and assume ηt ηt+1. Then the regret for OFTRL is bounded by

- Lemma 15. Suppose ft(·) are convex for all t ∈ [T] and ψt(·) = η2


![image 90](<2022-sachs-between-stochastic-adversarial-online_images/imageFile90.png>)

t

RT

T

D2 ηT

+

![image 91](<2022-sachs-between-stochastic-adversarial-online_images/imageFile91.png>)

t=1

1 ηt

gt − Mt, xt − xt+1 −

![image 92](<2022-sachs-between-stochastic-adversarial-online_images/imageFile92.png>)

xt+1 − xt 2 . (7)

Proof. Denote Ft(x) := ψt(x)+ ts−=11 fs(x). Note that Ft is η2

-strongly convex. Thus, Thm 7.29 in [Orabona, 2021] gives

![image 93](<2022-sachs-between-stochastic-adversarial-online_images/imageFile93.png>)

t

RT(u) ψT+1(u) − ψ1(x1)

T

1 ηt

gt − Mt,xt − xt+1 −

+

![image 94](<2022-sachs-between-stochastic-adversarial-online_images/imageFile94.png>)

t=1

xt − xt+1 2 + ψt(xt+1) − ψt+1(xt+1) .

2

Since ψt(x) − ψt+1(x) 0 and ψT+1(u) D

ηT , this gives

![image 95](<2022-sachs-between-stochastic-adversarial-online_images/imageFile95.png>)

T

D2 ηT

+

![image 96](<2022-sachs-between-stochastic-adversarial-online_images/imageFile96.png>)

t=1

1 ηt

gt − Mt, xt − xt+1 −

![image 97](<2022-sachs-between-stochastic-adversarial-online_images/imageFile97.png>)

xt+1 − xt 2 .

![image 98](<2022-sachs-between-stochastic-adversarial-online_images/imageFile98.png>)

![image 99](<2022-sachs-between-stochastic-adversarial-online_images/imageFile99.png>)

![image 100](<2022-sachs-between-stochastic-adversarial-online_images/imageFile100.png>)

![image 101](<2022-sachs-between-stochastic-adversarial-online_images/imageFile101.png>)

- Theorem 5. Fix a user-speciﬁed parameter ν > 0. Under assumptions (A1) ,(A2) ,(A3) , OFTRL, with Mt = gt−1 and adaptive step-size ηt = D2/(ν + ts−=11 ηs gs − Ms 2), has regret


3√2DG 2

√

√

![image 103](<2022-sachs-between-stochastic-adversarial-online_images/imageFile103.png>)

1 ν

2Σ¯T

![image 104](<2022-sachs-between-stochastic-adversarial-online_images/imageFile104.png>)

4D2G2 + 9L2D4 . (3)

![image 105](<2022-sachs-between-stochastic-adversarial-online_images/imageFile105.png>)

E[RT(u)] D 6 σ¯T + 3

+ ν +

T +

![image 106](<2022-sachs-between-stochastic-adversarial-online_images/imageFile106.png>)

![image 107](<2022-sachs-between-stochastic-adversarial-online_images/imageFile107.png>)

The algorithm needs only the knowledge of D. With the extra knowledge of G and L, one can tune ν = LD2 + DG2 to get

√

E[RT(u)] O D σ ¯T + Σ¯T

![image 108](<2022-sachs-between-stochastic-adversarial-online_images/imageFile108.png>)

T + DG + LD2 . Moreover, if only convexity of the individual losses holds (A1) , then tuning ν = 2DG ensures the (deterministic) bound RT(u) 3√2DG√T + 4DG .

![image 109](<2022-sachs-between-stochastic-adversarial-online_images/imageFile109.png>)

![image 110](<2022-sachs-between-stochastic-adversarial-online_images/imageFile110.png>)

- Proof of Theorem 5. Write gt = ∇f(xt,ξt) and denote by E the expectation with respect to all the randomness. Using the Optimistic FTRL bound from Lemma 15,


T

gt,xt − u

t=1

T

D2 ηT

gt − Mt, xt − xt+1 −

+

![image 111](<2022-sachs-between-stochastic-adversarial-online_images/imageFile111.png>)

t=1

T

T

D2 ηT

ηt 2

- 1

![image 112](<2022-sachs-between-stochastic-adversarial-online_images/imageFile112.png>)

- 2ηt


gt − Mt 2 −

+

![image 113](<2022-sachs-between-stochastic-adversarial-online_images/imageFile113.png>)

![image 114](<2022-sachs-between-stochastic-adversarial-online_images/imageFile114.png>)

t=1

t=1

- 1

![image 115](<2022-sachs-between-stochastic-adversarial-online_images/imageFile115.png>)

- 2ηt


xt − xt+1 2

xt − xt+1 2,

where the last inequality is obtained by separating the negative norm term in two parts, and keep half of it in the regret bound. Let us plug in the value ηt,

t−1

ηs gs − Ms 2

ηt = D2 ν +

s=1

−1

,

and use the fact that ηt D2/C to further upper bound the deterministic regret by

3 2

ν +

![image 116](<2022-sachs-between-stochastic-adversarial-online_images/imageFile116.png>)

T

T

ν 2D2

ηt gt − Mt 2 −

![image 117](<2022-sachs-between-stochastic-adversarial-online_images/imageFile117.png>)

t=1

t=1

xt − xt+1 2. (8)

To bound the second term above, we ﬁrst compute

T

ηt gt − Mt 2

t=1

2

T

T

ηs gs − Ms 2ηt gt − Mt 2

=

t=1

s=1

t−1

T

ηs gs − Ms 2 ηt gt − Mt 2 +

= 2

s=1

t=1

T

ηt2 gt − Mt 4 .

t=1

Since ηt D2/( ts−=11 ηs gs − Ms 2)

T

T t=1 ηt2 gt − Mt 4 T t=1 ηt gt − Mt 2

2D2

gt − Mt 2 +

![image 118](<2022-sachs-between-stochastic-adversarial-online_images/imageFile118.png>)

t=1

Now we use the fact X2 2A + BX implies X √2A + B for A,B > 0. Hence

![image 119](<2022-sachs-between-stochastic-adversarial-online_images/imageFile119.png>)

T

ηt gt − Mt 2 .

t=1

![image 120](<2022-sachs-between-stochastic-adversarial-online_images/imageFile120.png>)

T

T

T t=1 ηt2 gt − Mt 4 T t=1 ηt gt − Mt 2

ηt gt − Mt 2 D 2

gt − Mt 2 +

.

![image 121](<2022-sachs-between-stochastic-adversarial-online_images/imageFile121.png>)

t=1

t=1

Next we use ηt D2/ν and gt − Mt 2 4G2 to bound the last term. The sum satisﬁes Tt=1 ηt2 gt − Mt 4 (4G2D2/ν) Tt=1 ηt gt − Mt 2 and we can further bound the term above

![image 122](<2022-sachs-between-stochastic-adversarial-online_images/imageFile122.png>)

T

4D2G2 ν

gt − Mt 2 +

D 2

.

![image 123](<2022-sachs-between-stochastic-adversarial-online_images/imageFile123.png>)

All in all, we have

T

gt,xt − u

t=1

3√2D 2

![image 125](<2022-sachs-between-stochastic-adversarial-online_images/imageFile125.png>)

![image 126](<2022-sachs-between-stochastic-adversarial-online_images/imageFile126.png>)

![image 127](<2022-sachs-between-stochastic-adversarial-online_images/imageFile127.png>)

T

T

4D2G2 ν −

ν 2D2

gt − Mt 2 + ν +

![image 128](<2022-sachs-between-stochastic-adversarial-online_images/imageFile128.png>)

![image 129](<2022-sachs-between-stochastic-adversarial-online_images/imageFile129.png>)

t=1

t=1

xt+1 − xt 2 . (9)

Note that we have not used any assumption on the expected Ft’s, and in particular not the smoothness. Therefore, even if the expected losses are not smooth, our analysis already entails that if Mt G

3√2DG 2

T

√

4D2G2 ν

![image 130](<2022-sachs-between-stochastic-adversarial-online_images/imageFile130.png>)

![image 131](<2022-sachs-between-stochastic-adversarial-online_images/imageFile131.png>)

, (10)

4T + ν +

gt,xt − u

![image 132](<2022-sachs-between-stochastic-adversarial-online_images/imageFile132.png>)

![image 133](<2022-sachs-between-stochastic-adversarial-online_images/imageFile133.png>)

t=1

proving the ﬁnal claim of the statement. Let us now proceed with the proof of the ﬁner results. We use the value of Mt, together with the fact that (by convexity of a  → a 2), for any t 2,

gt − gt−1 2 4 gt − ∇Ft(xt) 2 + 4 ∇Ft(xt) − ∇Ft(xt−1) 2

+ 4 ∇Ft(xt−1) − ∇Ft−1(xt−1) 2 + 4 ∇Ft−1(xt−1) − gt−1 2 4 gt − ∇Ft(xt) 2 + 4L2 xt − xt−1 2

+ 4 ∇Ft(xt−1) − ∇Ft−1(xt−1) 2 + 4 ∇Ft−1(xt−1) − gt−1 2 . Therefore, using the inequality √a + b √a + √b, as well as g1 G and reorganizing the terms,

![image 134](<2022-sachs-between-stochastic-adversarial-online_images/imageFile134.png>)

![image 135](<2022-sachs-between-stochastic-adversarial-online_images/imageFile135.png>)

![image 136](<2022-sachs-between-stochastic-adversarial-online_images/imageFile136.png>)

![image 137](<2022-sachs-between-stochastic-adversarial-online_images/imageFile137.png>)

![image 138](<2022-sachs-between-stochastic-adversarial-online_images/imageFile138.png>)

T

T

gt − gt−1 2 G + 8

gt − ∇Ft(xt) 2

t=1

t=2

+ 2L

![image 139](<2022-sachs-between-stochastic-adversarial-online_images/imageFile139.png>)

T

xt − xt−1 2 + 2

t=2

![image 140](<2022-sachs-between-stochastic-adversarial-online_images/imageFile140.png>)

T

 ∇Ft(xt−1) − ∇Ft−1(xt−1) 2 .

t=2

The sum of the variations of xt’s can be cancelled thanks to the negative term in (9), as

3√2D 2

![image 141](<2022-sachs-between-stochastic-adversarial-online_images/imageFile141.png>)

2L

![image 142](<2022-sachs-between-stochastic-adversarial-online_images/imageFile142.png>)

![image 143](<2022-sachs-between-stochastic-adversarial-online_images/imageFile143.png>)

T

T−1

ν 2D2

xt+1 − xt 2 −

![image 144](<2022-sachs-between-stochastic-adversarial-online_images/imageFile144.png>)

t=1

t=1

xt+1 − xt 2 sup X 0

√

9L2D4 ν

ν 2D2

X2 =

![image 145](<2022-sachs-between-stochastic-adversarial-online_images/imageFile145.png>)

.

3

2LDX −

![image 146](<2022-sachs-between-stochastic-adversarial-online_images/imageFile146.png>)

![image 147](<2022-sachs-between-stochastic-adversarial-online_images/imageFile147.png>)

After replacing these bounds in (9), we have obtained the regret bound

![image 148](<2022-sachs-between-stochastic-adversarial-online_images/imageFile148.png>)

![image 149](<2022-sachs-between-stochastic-adversarial-online_images/imageFile149.png>)

T

T

T−1

√

![image 150](<2022-sachs-between-stochastic-adversarial-online_images/imageFile150.png>)

gt − ∇Ft(xt) 2 + 3

 ∇Ft+1(xt) − ∇Ft(xt) 2

gt,xt − u 6D

2D

t=1

t=1

t=1

3√2DG 2

4D2G2 ν

9L2D4 ν

![image 151](<2022-sachs-between-stochastic-adversarial-online_images/imageFile151.png>)

+ ν +

+

. (11)

+

![image 152](<2022-sachs-between-stochastic-adversarial-online_images/imageFile152.png>)

![image 153](<2022-sachs-between-stochastic-adversarial-online_images/imageFile153.png>)

![image 154](<2022-sachs-between-stochastic-adversarial-online_images/imageFile154.png>)

We will then take expectations in the inequality above. To bound the right-hand side, let us denote by Gt = σ(x1,ξ1,...,xt−1,ξt−1,xt), then ξt is distributed according to Dt given Gt, and since xt is Gt-measurable, therefore

E  ∇f(xt,ξt) − ∇Ft(xt) 2 | Gt Eξ∼D

t  ∇f(xt,ξ) − ∇Ft(xt) 2 sup

t  ∇f(x,ξ) − ∇Ft(x) 2 = σt2 . Therefore, by the tower rule,

Eξ∼D

x∈X

E  ∇f(xt,ξt) − ∇Ft(xt) 2 = E E  ∇f(xt,ξt) − ∇Ft(xt) 2 | Gt E σt2 . (12)

The ﬁnal result follows from taking expectations in (11), applying Jensen’s inequality, incorporating (12) and using the deﬁnitions of σ¯T and Σ¯T.

![image 155](<2022-sachs-between-stochastic-adversarial-online_images/imageFile155.png>)

![image 156](<2022-sachs-between-stochastic-adversarial-online_images/imageFile156.png>)

![image 157](<2022-sachs-between-stochastic-adversarial-online_images/imageFile157.png>)

![image 158](<2022-sachs-between-stochastic-adversarial-online_images/imageFile158.png>)

- B.2 Proof of Theorem 6


- Theorem 6. For any learning algorithm, and for any pair of positive numbers (σ,Σ) there exists a function f :


X×Ξ → R and a sequence of distributions satisfying assumptions (A1) , (A2) ,(A3) with σ¯T σ and Σ¯T Σ such that

√

E[RT(u)] Ω D σ ¯T + Σ¯T

![image 160](<2022-sachs-between-stochastic-adversarial-online_images/imageFile160.png>)

T .

- Proof of Theorem 6. Suppose we are given two parameters σˆT and ΣˆT, we show that there exists a sequence of distributions D1,...DT such that the expected regret is at least Ω(D(ˆσT + ΣˆT)√T). Let 1 a < b be constants


![image 161](<2022-sachs-between-stochastic-adversarial-online_images/imageFile161.png>)

such that a 2 1b. Since for any closed convex set there exist an afﬁne transformation which mapps it to the interval [a,b], we assume without loss of generality that X = [a,b].

![image 162](<2022-sachs-between-stochastic-adversarial-online_images/imageFile162.png>)

Suppose f : X×Ξ → R and let z(σ),z(Σ) ∈ R. Assume the gradients have the form ∇f(x,ξ) = z(σ) or ∇f(x,ξ) = z(Σ).

Assume SEA chooses each case with probability 1/2. The idea is to construct two sequences {zt(σ)}t∈[T] and {zt(Σ)}t∈[T] such that these sequences have at least Ω(DσˆT

√

√

T) and Ω(DΣˆT

![image 163](<2022-sachs-between-stochastic-adversarial-online_images/imageFile163.png>)

![image 164](<2022-sachs-between-stochastic-adversarial-online_images/imageFile164.png>)

T) expected regret, respectively. Therefore, let xt denote the learners choice in round t and deﬁne linearised regret with respect to {zt(σ)}t∈[T] and {zt(Σ)}t∈[T].

zt(Σ),xt − u .

zt(σ),xt − u and RTΣ = min u∈X

RTσ = min u∈X

t∈[T]

t∈[T]

Case RTΣ: Let G = ΣˆT. Deﬁne z : X → R, z (x) = 41bGx2. Then z is G-Lipschitz, smooth and z ′(x) ∈ [12G,G] for any x ∈ X. Let {εt}t∈[T] be an i.i.d. sequence of Rademacher random variables, that is, P [εt = 1] = P [εt = −1] = 1/2. The sequence {zt(Σ)}t∈[T] is deﬁned as

![image 165](<2022-sachs-between-stochastic-adversarial-online_images/imageFile165.png>)

![image 166](<2022-sachs-between-stochastic-adversarial-online_images/imageFile166.png>)

0 if t even εt z ′(xt) if t odd.

zt(Σ) =

Using that E[ε] = 0 together with the deﬁnition of zt(Σ) gives

T

zt(Σ),xt − u

Eε∼Rad RTΣ = Eε∼Rad min u∈X

t=1

  

  max

T

εt z ′(xt),u

= Eε∼Rad

u∈X

t=1 t odd

 max

 .

T 2

![image 167](<2022-sachs-between-stochastic-adversarial-online_images/imageFile167.png>)

G 4

εtu

Eε∼Rad

![image 168](<2022-sachs-between-stochastic-adversarial-online_images/imageFile168.png>)

u∈X

t=1

Now use that for a linear function l(x), maxx∈[a,b] l(x) = maxx∈{a,b} l(x) = l(a2+b) + |l(a2−b)|.

![image 169](<2022-sachs-between-stochastic-adversarial-online_images/imageFile169.png>)

![image 170](<2022-sachs-between-stochastic-adversarial-online_images/imageFile170.png>)

  max

 

T 2

![image 171](<2022-sachs-between-stochastic-adversarial-online_images/imageFile171.png>)

G 4

=

εtu

Eε∼Rad

![image 172](<2022-sachs-between-stochastic-adversarial-online_images/imageFile172.png>)

u∈{a,b}

t=1

 

 

 

  +

T/2

T/2

G 8

G 8

Gεt(a − b)

εt(a + b)

=

Eε∼Rad

Eε∼Rad

![image 173](<2022-sachs-between-stochastic-adversarial-online_images/imageFile173.png>)

![image 174](<2022-sachs-between-stochastic-adversarial-online_images/imageFile174.png>)

t=1

t=1

T

G 16

εt(a − b) .

=

Eε∼Rad

![image 175](<2022-sachs-between-stochastic-adversarial-online_images/imageFile175.png>)

Where we have used E[ε] = 0 again. Now we use that by deﬁnition D = supx,y∈X x − y .

GD 16

=

Eε∼Rad

![image 177](<2022-sachs-between-stochastic-adversarial-online_images/imageFile177.png>)

T

εt

t=1

√

1 32

![image 178](<2022-sachs-between-stochastic-adversarial-online_images/imageFile178.png>)

G2T.

D

![image 179](<2022-sachs-between-stochastic-adversarial-online_images/imageFile179.png>)

In the last step we have used the Khintchine inequality. Now note that G2 12 supx∈X z ′(x) 2 =

![image 180](<2022-sachs-between-stochastic-adversarial-online_images/imageFile180.png>)

- 1

![image 181](<2022-sachs-between-stochastic-adversarial-online_images/imageFile181.png>)

- 2 supx∈X z ′(x) − 0 2. Due to the deﬁnition of the sequence {zt(Σ)}t∈[T], if  ∇f(x,ξt) = 0, then ∇f(x,ξt−1) = 0. Thus, 12 supx∈X z ′(x) − 0 2 = 21 supx∈X ∇f(x,ξt) − ∇f(x,ξt−1) 2 for any t ∈ [T].


![image 182](<2022-sachs-between-stochastic-adversarial-online_images/imageFile182.png>)

![image 183](<2022-sachs-between-stochastic-adversarial-online_images/imageFile183.png>)

√

![image 184](<2022-sachs-between-stochastic-adversarial-online_images/imageFile184.png>)

G2T = T/(2T) Tt=1 supx∈X  ∇f(x,ξt) − ∇f(x,ξt−1) 2 = Σ¯T T/2. Setting the value G = ΣˆT completes this part of the proof.

![image 185](<2022-sachs-between-stochastic-adversarial-online_images/imageFile185.png>)

![image 186](<2022-sachs-between-stochastic-adversarial-online_images/imageFile186.png>)

Thus,

Case RTσ: We will show this part by contradiction. Suppose that D is a distribution such that the variance of the gradients σ is equal to σˆT. Suppose the SEA picks this distribution every round and assume for con-

tradiction that E[RTσ] o(Dσ√T). Using online-to-batch conversion gives a convergence bound of order o(Dσ/

![image 187](<2022-sachs-between-stochastic-adversarial-online_images/imageFile187.png>)

√

![image 188](<2022-sachs-between-stochastic-adversarial-online_images/imageFile188.png>)

T) which contradicts well-known lower bounds from stochastic optimization (c.f., [Agarwal et al., 2012, Nemirovsky and Yudin, 1985] Section 5).

![image 189](<2022-sachs-between-stochastic-adversarial-online_images/imageFile189.png>)

![image 190](<2022-sachs-between-stochastic-adversarial-online_images/imageFile190.png>)

![image 191](<2022-sachs-between-stochastic-adversarial-online_images/imageFile191.png>)

![image 192](<2022-sachs-between-stochastic-adversarial-online_images/imageFile192.png>)

- B.3 Proof of Theorem 7


We ﬁrst need a well known result for OFTL for strongly convex loss functions.

- Lemma 16. Suppose ft(·) are µ-strongly convex for all t ∈ [T] and ψt(·) = 0. Further, let mt : X → R denote the optimistic prediction, and gt ∈ ∂ft(xt), Mt ∈ ∂mt(xt). Then the regret for OFTRL is bounded by


T

tµ 2

xt − xt+1 2 .

RT(u)

gt − Mt,xt − xt+1 −

![image 193](<2022-sachs-between-stochastic-adversarial-online_images/imageFile193.png>)

t=1

This is a well known result and can be found in the literature, e.g., [Orabona, 2021]. We include a short proof for completeness.

Proof. Let F¯t(x) = ts−=11 ft(x) and Gt ∈ ∂F¯t+1(xt). Note that F¯t is [(t − 1)µ]-strongly convex. From standard analysis (see, e.g., [Orabona, 2021] Lem. 7.1) we obtain

T

[ft(xt) − ft(u)] = F¯T+1(xT+1) − F¯T+1(u)

+

![image 194](<2022-sachs-between-stochastic-adversarial-online_images/imageFile194.png>)

![image 195](<2022-sachs-between-stochastic-adversarial-online_images/imageFile195.png>)

t=1

0

T

[F¯t(xt) + ft(xt) =F¯t+1(xt)

−F¯t+1(xt+1)].

![image 196](<2022-sachs-between-stochastic-adversarial-online_images/imageFile196.png>)

![image 197](<2022-sachs-between-stochastic-adversarial-online_images/imageFile197.png>)

t=1

T

[F¯t+1(xt) − F¯t+1(xt+1)]

t=1

T

tµ 2

xt − xt+1 .

Gt,xt − xt+1 −

![image 198](<2022-sachs-between-stochastic-adversarial-online_images/imageFile198.png>)

t=1

Due to convexity, Gt ∈ ∂F¯t+1(xt) = ∂F¯t(xt) ∩ ∂ft(xt) and due to update operation 0 ∈ ∂F¯t(xt) ∩ ∂mt(xt). Thus, there exist gt ∈ ∂ft(xt) and Mt ∈ ∂mt(xt) such that Gt = gt − Mt, which completes the proof.

![image 199](<2022-sachs-between-stochastic-adversarial-online_images/imageFile199.png>)

![image 200](<2022-sachs-between-stochastic-adversarial-online_images/imageFile200.png>)

![image 201](<2022-sachs-between-stochastic-adversarial-online_images/imageFile201.png>)

![image 202](<2022-sachs-between-stochastic-adversarial-online_images/imageFile202.png>)

- Theorem 7. Under assumptions (A1) –(A4) , the expected regret of OFTL with Mt = ∇f(xt−1,ξt−1) on surrogate loss functions ℓt deﬁned in (4) is bounded as


E[RT(u)]

T

1 t

1 µ

∇Ft(x) − ∇Ft−1(x) 2 +

8σmax2 + 4E sup x∈X

![image 203](<2022-sachs-between-stochastic-adversarial-online_images/imageFile203.png>)

![image 204](<2022-sachs-between-stochastic-adversarial-online_images/imageFile204.png>)

t=1

4D2L2 µ

16L µ

1 µ

8σmax2 + 4Σ2max log T +

.

log 1 +

![image 205](<2022-sachs-between-stochastic-adversarial-online_images/imageFile205.png>)

![image 206](<2022-sachs-between-stochastic-adversarial-online_images/imageFile206.png>)

![image 207](<2022-sachs-between-stochastic-adversarial-online_images/imageFile207.png>)

4D2L2 µ

16L µ

log 1 +

![image 208](<2022-sachs-between-stochastic-adversarial-online_images/imageFile208.png>)

![image 209](<2022-sachs-between-stochastic-adversarial-online_images/imageFile209.png>)

- Proof of Theorem 7. Thanks to the strong convexity assumption (A4) ,


µ 2

Ft(xt) − Ft(x) xt − x,∇Ft(xt) −

x − xt 2 . Taking expectation and using the deﬁnition of ℓt gives

![image 211](<2022-sachs-between-stochastic-adversarial-online_images/imageFile211.png>)

µ 2

x − xt 2

E Ft(xt) − Ft(x) E xt − x,∇Ft(xt) −

![image 212](<2022-sachs-between-stochastic-adversarial-online_images/imageFile212.png>)

µ 2

x − xt 2

= E xt − x,∇f(xt,ξt) −

![image 213](<2022-sachs-between-stochastic-adversarial-online_images/imageFile213.png>)

µ 2

x − xt 2

= E xt − x,gt −

![image 214](<2022-sachs-between-stochastic-adversarial-online_images/imageFile214.png>)

= E[ℓt(xt) − ℓt(x)] . Now each function ℓt is µ-strongly convex, and ∇ℓt(xt) = gt. Thus we can apply Lemma 16

T

T

µt 2

xt − xt+1 2 .

ℓt(xt) − ℓt(x)

gt − Mt,xt − xt+1 −

![image 215](<2022-sachs-between-stochastic-adversarial-online_images/imageFile215.png>)

t=1

t=1

T

1 µt

µt 2

µt 4 −

xt − xt+1 2 .

gt − Mt 2 +

![image 216](<2022-sachs-between-stochastic-adversarial-online_images/imageFile216.png>)

![image 217](<2022-sachs-between-stochastic-adversarial-online_images/imageFile217.png>)

![image 218](<2022-sachs-between-stochastic-adversarial-online_images/imageFile218.png>)

t=1

where we used the inequality a,b 2 1c a 2 + 2c b 2. Once again, keeping the negative norm term is crucial. Indeed, using the convexity of x  → x 2 and the smoothness assumption on ∇Ft, we get that for t 2

![image 219](<2022-sachs-between-stochastic-adversarial-online_images/imageFile219.png>)

![image 220](<2022-sachs-between-stochastic-adversarial-online_images/imageFile220.png>)

gt − gt−1 2 4 gt − ∇Ft(xt) 2 + 4 ∇Ft(xt) − ∇Ft(xt−1) 2

+ 4 ∇Ft(xt−1) − ∇Ft−1(xt−1) 2 + 4 ∇Ft−1(xt−1) − gt−1 2 4 gt − ∇Ft(xt) 2 + 4L2 xt − xt−1 2

+ 4 ∇Ft(xt−1) − ∇Ft−1(xt−1) 2 + 4 ∇Ft−1(xt−1) − gt−1 2 . So that, upper bounding the ﬁrst term ℓ1(x1) − ℓ1(u) GD we get

T

ℓt(xt) − ℓt(u)

t=1

T

1 µt

4 gt − ∇Ft(xt) 2 + 4 gt−1 − ∇Ft−1(xt−1) 2 + 4 ∇Ft(xt−1) − ∇Ft−1(xt) 2

![image 221](<2022-sachs-between-stochastic-adversarial-online_images/imageFile221.png>)

t=2

T

4L2 µ(t + 1) −

µt 4

xt − xt+1 2 + GD . The indices can be simpliﬁed by noting that,

+

![image 222](<2022-sachs-between-stochastic-adversarial-online_images/imageFile222.png>)

![image 223](<2022-sachs-between-stochastic-adversarial-online_images/imageFile223.png>)

t=1

T

T

T

4 µt

4 µ(t − 1)

4 µt

gt − ∇Ft(xt) 2 . To recover

gt−1 − ∇Ft−1(xt−1) 2

gt−1 − ∇Ft−1(xt−1) 2

![image 224](<2022-sachs-between-stochastic-adversarial-online_images/imageFile224.png>)

![image 225](<2022-sachs-between-stochastic-adversarial-online_images/imageFile225.png>)

![image 226](<2022-sachs-between-stochastic-adversarial-online_images/imageFile226.png>)

t=2

t=2

t=1

T

T

T

4 µt ∇Ft(xt−1) − ∇Ft−1(xt) 2

8 µt

gt − ∇Ft(xt) 2 +

ℓt(xt) − ℓt(u)

![image 227](<2022-sachs-between-stochastic-adversarial-online_images/imageFile227.png>)

![image 228](<2022-sachs-between-stochastic-adversarial-online_images/imageFile228.png>)

t=2

t=1

t=1

T

4L2 µt −

µt 4

xt − xt+1 2 + GD . (13)

+

![image 229](<2022-sachs-between-stochastic-adversarial-online_images/imageFile229.png>)

![image 230](<2022-sachs-between-stochastic-adversarial-online_images/imageFile230.png>)

t=1

2

µt − µt4 0 . Therefore the second term can be bounded independently of T

Deﬁne the condition number κ = L/µ. Then, for t 16κ, we have 4L

![image 231](<2022-sachs-between-stochastic-adversarial-online_images/imageFile231.png>)

![image 232](<2022-sachs-between-stochastic-adversarial-online_images/imageFile232.png>)

⌈16κ⌉

⌈16κ⌉

4L2D2 µ

4L2 µt −

4L2D2 µ

1 t

µt 4

D2

log(1 + 16κ). Combining all bounds, and incorporating the deﬁnition of σmax and Σmax,

![image 233](<2022-sachs-between-stochastic-adversarial-online_images/imageFile233.png>)

![image 234](<2022-sachs-between-stochastic-adversarial-online_images/imageFile234.png>)

![image 235](<2022-sachs-between-stochastic-adversarial-online_images/imageFile235.png>)

![image 236](<2022-sachs-between-stochastic-adversarial-online_images/imageFile236.png>)

![image 237](<2022-sachs-between-stochastic-adversarial-online_images/imageFile237.png>)

t=1

t=1

1 µ

8σmax2 + 4Σ2max log T + 4D2Lκ log(1 + 16κ) + GD .

E[RT(u)]

![image 238](<2022-sachs-between-stochastic-adversarial-online_images/imageFile238.png>)

![image 239](<2022-sachs-between-stochastic-adversarial-online_images/imageFile239.png>)

![image 240](<2022-sachs-between-stochastic-adversarial-online_images/imageFile240.png>)

![image 241](<2022-sachs-between-stochastic-adversarial-online_images/imageFile241.png>)

![image 242](<2022-sachs-between-stochastic-adversarial-online_images/imageFile242.png>)

- B.4 Proof of Theorem 8


- Theorem 8. For any learning algorithm, and for any pair of positive numbers (σ,Σ) there exists a function f : X×Ξ → R and a sequence of distributions satisfying assumptions (A1) ,(A2) ,(A3) and (A4) with σmax σ and Σmax Σ such that


E[RT(u)] Ω

1 µ

![image 244](<2022-sachs-between-stochastic-adversarial-online_images/imageFile244.png>)

σmax2 + Σ2max log T .

- Proof of Theorem 8. Let σˆmax,Σˆmax be given parameters and set G = max(ˆσmax,Σˆmax/2). We want to show that there exist sequence of distributions D1,...DT such that


- 1. σmax = σˆmax and Σmax = Σˆmax.
- 2. E[RT(u)] cµ1(Σ2max + σmax2 )log T for some constant c > 0.

![image 245](<2022-sachs-between-stochastic-adversarial-online_images/imageFile245.png>)

- 3. F1,...,FT are µ-strongly convex.


Consider the iterations up to T − 3. From Corollary 20 in [Hazan and Kale, 2011] we obtain an Ω(µ1G2 log(T − 3)) lower bound on the expected regret. Thus, there exist a realization ξ1,...,ξT−3 and corresponding µ-strongly convex functions f(·,ξ1),...,f(·,ξT−3) such that with respect to this realization, RT(u) Ω(µ1G2 log(T − 3)). We now let δ1,...δT−3 be the Dirac measure corresponding to this realization. Then, σmax = 0 and maxt∈[T−3] supx∈X  ∇Ft(x) − ∇Ft−1(x) 2G. But we do not necessarily have that σmax = σˆmax and maxt∈[T−3] supx∈X  ∇Ft(x) − ∇Ft−1(x) = Σˆmax. To guarantee this we want to choose DT−2,DT−1,DT, such that

![image 246](<2022-sachs-between-stochastic-adversarial-online_images/imageFile246.png>)

![image 247](<2022-sachs-between-stochastic-adversarial-online_images/imageFile247.png>)

- 1. supx∈X  ∇FT−2(x) − ∇FT−1(x) = Σˆmax and  ∇FT−i(x) G for i = 1,2.
- 2. σT = σˆmax and  ∇FT(x) G.


To satisfy Condition 1, let DT−2,DT−1 be Dirac measures, such that ∇FT−2(x) = −∇FT−1(x) and  ∇FT−2(x) = 12Σˆmax. Then, by deﬁnition of G, we know that  ∇FT−2(x) G and supx∈X  ∇FT−2(x) − ∇FT−1(x) = Σˆmax. Condition 2 can be satisﬁed by setting DT to be any distribution with sufﬁcient variance. This gives

![image 248](<2022-sachs-between-stochastic-adversarial-online_images/imageFile248.png>)

T

1 µ

Σ2max + σmax2 log(T − 3) − E

E[RT(u)] c

f(xt,ξt) − f(u,ξt) . (14)

![image 249](<2022-sachs-between-stochastic-adversarial-online_images/imageFile249.png>)

t=T−2

Now it remains to show that the last term is negligible. Indeed, from the upper bound, we know

E

T

[f(xt,ξt) − f(u,ξt)]

t=T−2

3 (T − 2)µ

![image 250](<2022-sachs-between-stochastic-adversarial-online_images/imageFile250.png>)

Σ2max + σmax2 .

Hence, for any T 10, we get (T−32)µ Σ2max + σmax2 2 1µ Σ2max + σmax2 log(T) which together with (14) completes the proof.

![image 251](<2022-sachs-between-stochastic-adversarial-online_images/imageFile251.png>)

![image 252](<2022-sachs-between-stochastic-adversarial-online_images/imageFile252.png>)

![image 253](<2022-sachs-between-stochastic-adversarial-online_images/imageFile253.png>)

![image 254](<2022-sachs-between-stochastic-adversarial-online_images/imageFile254.png>)

![image 255](<2022-sachs-between-stochastic-adversarial-online_images/imageFile255.png>)

![image 256](<2022-sachs-between-stochastic-adversarial-online_images/imageFile256.png>)

C Missing Proofs of Section 4

We ﬁrst show the following general property of the variance for the ROM. This proposition will useful for showing the claims of this section.

Proposition 17. For any t ∈ [T], the variance of the ROM with respect to Dt satisﬁes

T T − t + 1

t  ∇f(x,ξ) − ∇Ft(x) 2

σ12, for any x ∈ X.

Eξ∼D

![image 257](<2022-sachs-between-stochastic-adversarial-online_images/imageFile257.png>)

Proof. For any x ∈ X, since ∇Ft(x) = Eξ∼D

[∇f(x,ξ)], we have Eξ∼D

t

t  ∇f(x,ξ) − ∇Ft(x) 2 Eξ∼D

t  ∇f(x,ξ) − ∇F1(x) 2 .

Now, let Tt ⊆ [T] denote a subset of indices of gradients which remain to be selected in round t, and let kt ∈ Tt−1 \ Tt be the index selected at round t. For any x ∈ X

1 T − t + 1 ξ∈T

t  ∇f(x,ξ) − ∇F1(x) 2 =

 ∇f(x,ξ) − ∇F1(x) 2

Eξ∼D

![image 259](<2022-sachs-between-stochastic-adversarial-online_images/imageFile259.png>)

t

1 T − t + 1

T T − t + 1

 ∇f(x,ξ) − ∇F1(x) 2

σ12 , (15)

![image 260](<2022-sachs-between-stochastic-adversarial-online_images/imageFile260.png>)

![image 261](<2022-sachs-between-stochastic-adversarial-online_images/imageFile261.png>)

ξ∈[n]

which is the claimed result.

![image 262](<2022-sachs-between-stochastic-adversarial-online_images/imageFile262.png>)

![image 263](<2022-sachs-between-stochastic-adversarial-online_images/imageFile263.png>)

![image 264](<2022-sachs-between-stochastic-adversarial-online_images/imageFile264.png>)

![image 265](<2022-sachs-between-stochastic-adversarial-online_images/imageFile265.png>)

- C.1 Proof of Lemma 11


Note that in any case, σ˜1 Tσ1, and therefore log(˜σ1/σ1) log(T). Thus Lemma 11 directly yields σ[1:(2)T] σ1T log(T). This means in particular that the rate of OFTRL in the ROM is never more than a factor √log T worse than the i.i.d. sampling with replacement rate of σ1

![image 266](<2022-sachs-between-stochastic-adversarial-online_images/imageFile266.png>)

√

![image 267](<2022-sachs-between-stochastic-adversarial-online_images/imageFile267.png>)

T; the next bound can often be much tighter. Lemma 11. In the single-pass ROM, we have Σ(2)[1:T] 8G2 and σ¯[1:(2)T] Tσ12 log(2e2 σ12/σ12). Proof of Lemma 11. Let us begin with the adversarial variation. We will show that deterministically (that is, for any order in which the losses are selected), for any x ∈ X,

4G2 (T − t + 2)2

∇Ft(x) − ∇Ft−1(x) 2

.

![image 268](<2022-sachs-between-stochastic-adversarial-online_images/imageFile268.png>)

With the same notation as in Proposition 17, recall that we denote by Tt ⊆ [T] the support of Dt and kt = Tt−1 \ Tt. We have |Tt | = T − t + 1 and for any x ∈ X,

2

1 T − t + 1 s∈T

1 T − t + 2 s∈T

∇Ft(x) − ∇Ft−1(x) 2 =

∇fs(x) −

∇fs(x)

![image 269](<2022-sachs-between-stochastic-adversarial-online_images/imageFile269.png>)

![image 270](<2022-sachs-between-stochastic-adversarial-online_images/imageFile270.png>)

t

t−1

1

=

![image 271](<2022-sachs-between-stochastic-adversarial-online_images/imageFile271.png>)

- (T − t + 1)(T − t + 2) s∈T

t

∇fs(x) −

1 T − t + 2∇fk

![image 272](<2022-sachs-between-stochastic-adversarial-online_images/imageFile272.png>)

t

(x)

2

2

![image 273](<2022-sachs-between-stochastic-adversarial-online_images/imageFile273.png>)

- (T − t + 2)2


1 (T − t + 1) s∈T

![image 274](<2022-sachs-between-stochastic-adversarial-online_images/imageFile274.png>)

t

∇fs(x)

2

2 (T − t + 2)2  ∇fk

(x) 2 .

+

![image 275](<2022-sachs-between-stochastic-adversarial-online_images/imageFile275.png>)

t

Thus, after maximising over x ∈ X, and taking expectations(note that the inequality holds almost surely) and summing over rounds t ∈ [T],

T

T

4G2 (T − t + 2)2

Σ(2)[1:T] = E

 ∇Ft(x) − ∇Ft−1(x) 2

8G2.

sup

![image 276](<2022-sachs-between-stochastic-adversarial-online_images/imageFile276.png>)

x∈X

t=1

t=1

Variance. From Proposition 17, we know that

T T − t + 1

σt2

σ12 Moreover, one can see that

![image 277](<2022-sachs-between-stochastic-adversarial-online_images/imageFile277.png>)

t  ∇f(x,ξ) − ∇F1(x) 2

E[σt2] E max x∈X

Eξ∼D

E Eξ∼D

t

 ∇f(x,ξ) − ∇F1(x) 2 = σ˜12 . (16)

max

x∈X

Let us introduce a threshold time step τ ∈ [T], of which we will set the value later. We upper bound E[σt2] by (15) for the rounds before τ and by (16) for the other rounds:

τ

T

τ

T

T T − t + 1

σt2

σt2 + E

σt2 E

σ12 + (T − τ)˜σ12 Now using standard bounds on the harmonic series,

E

![image 279](<2022-sachs-between-stochastic-adversarial-online_images/imageFile279.png>)

t=1

t=τ+1

t=1

t=1

T

τ

T T − τ + 1

1 n

1 T − t + 1

=

1 + log

.

![image 280](<2022-sachs-between-stochastic-adversarial-online_images/imageFile280.png>)

![image 281](<2022-sachs-between-stochastic-adversarial-online_images/imageFile281.png>)

![image 282](<2022-sachs-between-stochastic-adversarial-online_images/imageFile282.png>)

t=1

n=T−τ+1

Therefore for any τ ∈ [T − 1], we get

T

T T − τ + 1

σt2 Tσ12 1 + log

+ (T − τ)˜σ12 . (17)

E

![image 283](<2022-sachs-between-stochastic-adversarial-online_images/imageFile283.png>)

t=1

We now conclude by setting the appropriate value for τ. If Tσ12/ σ12 2, then log T log(2 σ12/σ12), and taking τ = T gives a bound of Tσ12(1 + log T) Tσ12(1 + log(2 σ12/σ12)), which is (better than) the claimed result.

Otherwise, we take τ = T − ⌊Tσ12/σ˜12⌋, then

(T − τ)˜σ12 = ⌊Tσ12/σ˜12⌋σ˜12 Tσ12 , and the argument of the logarithm can be bounded as

T T − τ + 1

1 σ12/σ˜12 − 1/T

T ⌊Tσ12/σ˜12⌋

![image 284](<2022-sachs-between-stochastic-adversarial-online_images/imageFile284.png>)

![image 285](<2022-sachs-between-stochastic-adversarial-online_images/imageFile285.png>)

![image 286](<2022-sachs-between-stochastic-adversarial-online_images/imageFile286.png>)

where we used the fact that Tσ12/ σ12 > 2. This yields the ﬁnal bound

2˜σ12 σ12

.

![image 287](<2022-sachs-between-stochastic-adversarial-online_images/imageFile287.png>)

E

T

2˜σ12 σ12

σt2 Tσ12 1 + log

![image 288](<2022-sachs-between-stochastic-adversarial-online_images/imageFile288.png>)

t=1

+ Tσ12 Tσ12 log

2e2σ˜12 σ12

![image 289](<2022-sachs-between-stochastic-adversarial-online_images/imageFile289.png>)

.

![image 290](<2022-sachs-between-stochastic-adversarial-online_images/imageFile290.png>)

![image 291](<2022-sachs-between-stochastic-adversarial-online_images/imageFile291.png>)

![image 292](<2022-sachs-between-stochastic-adversarial-online_images/imageFile292.png>)

![image 293](<2022-sachs-between-stochastic-adversarial-online_images/imageFile293.png>)

- C.2 Proof of Corollary 12 Corollary 12. Under the same assumption as in Theorem 7, the expected regret of the ROM is bounded by


G2 µ

σ12 µ

+ LD2κ logκ . For multi-pass ROM with P passes, we obtain

log T +

E[RT(u)] O

![image 294](<2022-sachs-between-stochastic-adversarial-online_images/imageFile294.png>)

![image 295](<2022-sachs-between-stochastic-adversarial-online_images/imageFile295.png>)

E[RT(u)] O

G2 µ

σ12 µ

log T +

![image 296](<2022-sachs-between-stochastic-adversarial-online_images/imageFile296.png>)

![image 297](<2022-sachs-between-stochastic-adversarial-online_images/imageFile297.png>)

G2 log P nµ

+ LD2κ log κ .

+

![image 298](<2022-sachs-between-stochastic-adversarial-online_images/imageFile298.png>)

Proof of Corollary 12. Single-pass ROM: From Theorem 7 we obtain (c.f. (13))

T

T

8 µt

4 µt ∇Ft(xt−1) − ∇Ft−1(xt) 2

gt − ∇Ft(xt) 2 +

E[RT(u)] E

![image 299](<2022-sachs-between-stochastic-adversarial-online_images/imageFile299.png>)

![image 300](<2022-sachs-between-stochastic-adversarial-online_images/imageFile300.png>)

t=1

t=2

4L2D2 µ

+ GD +

log(1 + 16κ). By Lemma 11, we have

![image 301](<2022-sachs-between-stochastic-adversarial-online_images/imageFile301.png>)

T

4

µt ∇Ft(xt−1) − ∇Ft−1(xt) 2 8G2. Furthermore, recall that by Proposition 17 E[σt2] T/(T − t + 1)σ12.

E

![image 302](<2022-sachs-between-stochastic-adversarial-online_images/imageFile302.png>)

t=2

T

T

8σ12 µ

T t(T − t + 1)

8 µ

8 µt

gt − ∇Ft(xt) 2

σ12

(2 + 2 log(T)).

E

![image 303](<2022-sachs-between-stochastic-adversarial-online_images/imageFile303.png>)

![image 304](<2022-sachs-between-stochastic-adversarial-online_images/imageFile304.png>)

![image 305](<2022-sachs-between-stochastic-adversarial-online_images/imageFile305.png>)

![image 306](<2022-sachs-between-stochastic-adversarial-online_images/imageFile306.png>)

t=1

t=1

Indeed, using a standard bound on the harmonic series,

T

T

T

T t(T − t + 1)

T − t + 1 + t − 1 t(T − t + 1)

1 t

1 T − t + 1

2 + 2 logT . Combining these bounds gives the ﬁrst part of the corollary.

=

+

![image 308](<2022-sachs-between-stochastic-adversarial-online_images/imageFile308.png>)

![image 309](<2022-sachs-between-stochastic-adversarial-online_images/imageFile309.png>)

![image 310](<2022-sachs-between-stochastic-adversarial-online_images/imageFile310.png>)

![image 311](<2022-sachs-between-stochastic-adversarial-online_images/imageFile311.png>)

t=1

t=1

t=1

Multi-pass ROM: The critical term to upper bound, is the differences of the means whenever a pass ends and a new pass starts. Thus, for P ∈ N passes, we need to control supx∈X ∇Ft(x) − ∇Ft−1(x) 2 for t = jn + 1, with j ∈ [P].

Inside the i-th pass, for k ∈ [n] we bound the k-th variation by sup

4G2 (n − k + 2)2

∇Fk(x) − ∇Fk−1(x) 2

, and we bound it by G2 between the passes, so that

![image 312](<2022-sachs-between-stochastic-adversarial-online_images/imageFile312.png>)

x∈X

T

4 µ

1 t

∇Ft(x) − ∇Ft−1(x) 2

sup

![image 313](<2022-sachs-between-stochastic-adversarial-online_images/imageFile313.png>)

![image 314](<2022-sachs-between-stochastic-adversarial-online_images/imageFile314.png>)

x∈X

t=1

P

n

P

1 in

4 µ

4 µ

1 (i − 1)n + k

∇Fk(x) − ∇Fk−1(x) 2 +

∇F1(x) − ∇Fn(x) 2

sup

sup

![image 315](<2022-sachs-between-stochastic-adversarial-online_images/imageFile315.png>)

![image 316](<2022-sachs-between-stochastic-adversarial-online_images/imageFile316.png>)

![image 317](<2022-sachs-between-stochastic-adversarial-online_images/imageFile317.png>)

![image 318](<2022-sachs-between-stochastic-adversarial-online_images/imageFile318.png>)

x∈X

x∈X

i=1

i=1

k=1

P

n

P

2G2 (n − k + 2)2

1 in

4 µ

1 (i − 1)n + k

4 µ

∇F1(x) − ∇Fn(x) 2

+

sup

![image 319](<2022-sachs-between-stochastic-adversarial-online_images/imageFile319.png>)

![image 320](<2022-sachs-between-stochastic-adversarial-online_images/imageFile320.png>)

![image 321](<2022-sachs-between-stochastic-adversarial-online_images/imageFile321.png>)

![image 322](<2022-sachs-between-stochastic-adversarial-online_images/imageFile322.png>)

![image 323](<2022-sachs-between-stochastic-adversarial-online_images/imageFile323.png>)

x∈X

i=1

i=1

k=1

16G2 µ

log P n

1 + 2

.

![image 324](<2022-sachs-between-stochastic-adversarial-online_images/imageFile324.png>)

![image 325](<2022-sachs-between-stochastic-adversarial-online_images/imageFile325.png>)

![image 326](<2022-sachs-between-stochastic-adversarial-online_images/imageFile326.png>)

![image 327](<2022-sachs-between-stochastic-adversarial-online_images/imageFile327.png>)

![image 328](<2022-sachs-between-stochastic-adversarial-online_images/imageFile328.png>)

![image 329](<2022-sachs-between-stochastic-adversarial-online_images/imageFile329.png>)

- D Batch-to-online Conversion


Consider the stochastic optimization problem minx∈X Eξ∼D [f(x,ξ)] and let x∗ denote a minimiser for this problem. Further, let A be any ﬁrst order stochastic optimization method with convergence guarantee

Eξ∼D [f(xt,ξ) − f(x∗,ξ)] c(t). As input A takes an initial iterate x1 and a sequence of i.i.d. samples {f(·,ξs)}s∈[t]. We let A(x1,{f(·,ξs)}s∈[t]) denote the output xt+1 of the stochastic optimization algorithm with respect to the given input. Now consider an OCO with f(·,ξ1),...f(·,ξT) and ξ1,...ξT are sampled i.i.d. from a distribution.

![image 330](<2022-sachs-between-stochastic-adversarial-online_images/imageFile330.png>)

Algorithm 1 Batch-to-online Input: Stochastic ﬁrst order method A

![image 331](<2022-sachs-between-stochastic-adversarial-online_images/imageFile331.png>)

- 1: for t = 1,2,...T do
- 2: play xt and suffer loss f(xt,ξt)
- 3: restart A and set xt+1 = A(x1,{f(·,ξs)}s∈[t])
- 4: end for


![image 332](<2022-sachs-between-stochastic-adversarial-online_images/imageFile332.png>)

This batch-to-online conversion trivially achieves Tt=1 c(t) expected regret. However, with this conversion, some aspects of the stochastic convergence bound are lost. Consider for instance a convergence rate c(t) = O(LD2/t +

Dσ/√t), from the the ﬁrst-order stochastic approximation method in [Ghadimi and Lan, 2013] and the accelerated version c(t) = O(LD2/t2 + Dσ/√t) [Ghadimi and Lan, 2012, Joulani et al., 2020]. In both cases, the functions are assumed to satisfy (A1) -(A3) . Batch-to-online conversion yields

![image 333](<2022-sachs-between-stochastic-adversarial-online_images/imageFile333.png>)

![image 334](<2022-sachs-between-stochastic-adversarial-online_images/imageFile334.png>)

√

√

![image 335](<2022-sachs-between-stochastic-adversarial-online_images/imageFile335.png>)

![image 336](<2022-sachs-between-stochastic-adversarial-online_images/imageFile336.png>)

T) and E[RT(u)] O(LD2 + Dσ

E[RT(u)] O(LD2 log T + Dσ

T). The beneﬁts of acceleration can be seen in the lower order terms. Now using standard online-tobatch [Cesa-Bianchi et al., 2002] conversion in the way back gives the convergence bounds

LD2 T

Dσ √T

log T T

Dσ √T

and E[f(xT,ξ) − f(x∗,ξ)] O

+ LD2

E[f(xT,ξ) − f(x∗,ξ)] O

,

+

![image 337](<2022-sachs-between-stochastic-adversarial-online_images/imageFile337.png>)

![image 338](<2022-sachs-between-stochastic-adversarial-online_images/imageFile338.png>)

![image 339](<2022-sachs-between-stochastic-adversarial-online_images/imageFile339.png>)

![image 340](<2022-sachs-between-stochastic-adversarial-online_images/imageFile340.png>)

![image 341](<2022-sachs-between-stochastic-adversarial-online_images/imageFile341.png>)

![image 342](<2022-sachs-between-stochastic-adversarial-online_images/imageFile342.png>)

In the case of accelerated stochastic approximation, the beneﬁts of acceleration are inevitably lost through batch-toonline and online-to-batch conversion.

- E Additional Examples for Intermediate Cases


We provide regret bounds for intermediate cases not discussed in the main body of the paper, namely the cases when the adversary selects slowly shifting distributions and when the adversary switches rarely between distributions.

Distribution shift: In this example, the SEA picks Dt and Dt−1, such that ∇Ft(x) is close to the mean of the previous distribution gradient ∇Ft−1(x). We shall consider two kinds of distribution shifts. Firstly, when the means

are close on average, that is, when (1/T) Tt=1 supx∈X  ∇Ft(x) − ∇Ft−1(x) 2 ε, secondly, when this holds for each iteration t, i.e., supx∈X  ∇Ft(x) − ∇Ft−1(x) 2 ε. We refer to the former as the average distribution shift case, and to the latter as the bounded distribution shift case.

For strongly convex functions, Theorem 7 directly yields the regret bound

1 µ

(σmax2 + ε)log T + D2Lκ logκ . For the considerably weaker assumption of an average distribution shift, we have

E[RT(u)] O

![image 344](<2022-sachs-between-stochastic-adversarial-online_images/imageFile344.png>)

![image 345](<2022-sachs-between-stochastic-adversarial-online_images/imageFile345.png>)

T

T

1 t2µ2

1 tµ

4 µ

∇Ft(x) − ∇Ft−1(x) 2 Σ(2)[1:T]

sup

Tε.

![image 346](<2022-sachs-between-stochastic-adversarial-online_images/imageFile346.png>)

![image 347](<2022-sachs-between-stochastic-adversarial-online_images/imageFile347.png>)

![image 348](<2022-sachs-between-stochastic-adversarial-online_images/imageFile348.png>)

x∈X

t=1

t=1

To obtain the ﬁrst inequality, we have used the Cauchy-Schwarz inequality together with the fact that √a + b √a +

![image 349](<2022-sachs-between-stochastic-adversarial-online_images/imageFile349.png>)

√

![image 350](<2022-sachs-between-stochastic-adversarial-online_images/imageFile350.png>)

![image 351](<2022-sachs-between-stochastic-adversarial-online_images/imageFile351.png>)

b, and the second inequality follows directly from the deﬁnition of the averaged distribution shift. Now suppose ε 1/T, then we obtain the following regret bound in case of average distribution shift.

E[RT(u)] O

σmax2 µ

1 µ

log T +

![image 352](<2022-sachs-between-stochastic-adversarial-online_images/imageFile352.png>)

+ D2Lκ logκ .

![image 353](<2022-sachs-between-stochastic-adversarial-online_images/imageFile353.png>)

Since Σ(2)[1:T] Tε for the average distribution shift, for convex and smooth functions, Theorem 5 entails that E[RT(u)] O D(σmax + √ε)

√

![image 354](<2022-sachs-between-stochastic-adversarial-online_images/imageFile354.png>)

T + DG + LD2 .

![image 355](<2022-sachs-between-stochastic-adversarial-online_images/imageFile355.png>)

Distribution switch: SEA switches c times between distributions D1,...,Dc ∈ D. These switches can happen at any round and the learner does not know when a switch occurs. In this case, we can upper bound Σ(2)[1:T] Σ2maxc. Thus, for strongly convex functions Theorem 7 directly yields

1 µ

σmax2 log T + Σ2max log c + D2Lκ logκ . And for convex smooth functions Theorem 5 gives

E[RT(u)] O

![image 356](<2022-sachs-between-stochastic-adversarial-online_images/imageFile356.png>)

√

T + DΣmax√c + DG + LD2 .

![image 357](<2022-sachs-between-stochastic-adversarial-online_images/imageFile357.png>)

![image 358](<2022-sachs-between-stochastic-adversarial-online_images/imageFile358.png>)

E[RT(u)] O Dσmax

