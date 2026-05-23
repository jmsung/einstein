---
type: source
kind: paper
title: Differentially Private Non-Convex Optimization under the KL Condition with Optimal Rates
authors: Michael Menart, Enayat Ullah, Raman Arora, Raef Bassily, Cristóbal Guzmán
year: 2023
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/2311.13447v2
source_local: ../raw/2023-menart-differentially-private-non-convex-optimization.pdf
topic: general-knowledge
cites:
---

arXiv:2311.13447v2[cs.LG]3Apr2024

Differentially Private Non-Convex Optimization under the KL Condition with Optimal Rates

Michael Menart *† Enayat Ullah ‡† Raman Arora § Raef Bassily¶ Crist´obal Guzma´n ||

Abstract

We study private empirical risk minimization (ERM) problem for losses satisfying the (γ, κ)-KurdykaŁojasiewicz (KL) condition, that is, the empirical loss F satisﬁes F(w) − minw F(w) ≤ γκ ∇F(w) κ. The Polyak-Łojasiewicz (PL) condition is a special case of this condition when κ = 2. Speciﬁcally, we study this problem under the constraint of ρ zero-concentrated differential privacy (zCDP). When κ ∈ [1, 2] and the loss function is Lipschitz and smooth over a sufﬁciently large region, we provide a new algorithm based on variance reduced gradient descent that achieves the rate O˜

√d n√ρ

κ on the excess empirical risk, where n is the dataset size and d is the dimension. We further show that this rate is nearly optimal. When κ ≥ 2 and the loss is instead Lipschitz and weakly convex, we show it is possible to achieve the rate O˜

![image 1](<2023-menart-differentially-private-non-convex-optimization_images/imageFile1.png>)

![image 2](<2023-menart-differentially-private-non-convex-optimization_images/imageFile2.png>)

![image 3](<2023-menart-differentially-private-non-convex-optimization_images/imageFile3.png>)

√d n√ρ

κ with a private implementation of the proximal point method. When the KL parameters are unknown, we provide a novel modiﬁcation and analysis of the noisy gradient descent algorithm and show that this algorithm achieves a rate of O˜

![image 4](<2023-menart-differentially-private-non-convex-optimization_images/imageFile4.png>)

![image 5](<2023-menart-differentially-private-non-convex-optimization_images/imageFile5.png>)

![image 6](<2023-menart-differentially-private-non-convex-optimization_images/imageFile6.png>)

√d n√ρ

2κ

![image 7](<2023-menart-differentially-private-non-convex-optimization_images/imageFile7.png>)

![image 8](<2023-menart-differentially-private-non-convex-optimization_images/imageFile8.png>)

4−κ adaptively, which is nearly optimal when κ = 2. We further show that, without assuming the KL condition, the same gradient descent algorithm can achieve fast convergence to a stationary point when the gradient stays sufﬁciently large during the run of the algorithm. Speciﬁcally, we show that this algorithm can approximate stationary points of Lipschitz, smooth (and possibly nonconvex) objectives with rate as fast as O˜

![image 9](<2023-menart-differentially-private-non-convex-optimization_images/imageFile9.png>)

![image 10](<2023-menart-differentially-private-non-convex-optimization_images/imageFile10.png>)

√d

![image 11](<2023-menart-differentially-private-non-convex-optimization_images/imageFile11.png>)

n√ρ and never worse than O˜

![image 12](<2023-menart-differentially-private-non-convex-optimization_images/imageFile12.png>)

![image 13](<2023-menart-differentially-private-non-convex-optimization_images/imageFile13.png>)

√d n√ρ

1/2 . The latter rate matches the best known rate for methods that do not rely on variance reduction.

![image 14](<2023-menart-differentially-private-non-convex-optimization_images/imageFile14.png>)

![image 15](<2023-menart-differentially-private-non-convex-optimization_images/imageFile15.png>)

![image 16](<2023-menart-differentially-private-non-convex-optimization_images/imageFile16.png>)

# 1 Introduction

As modern machine learning techniques have increasingly relied on optimizing non-convexobjectives, characterizing our ability to solve such problems has become increasingly important. Due to the inherent limitations of solving non-convex optimization problems, that is, the intractability of approximating global minimizers, work in this area has largely focused on approximating stationary points [FLLZ18, CDHS17, GL13,

![image 17](<2023-menart-differentially-private-non-convex-optimization_images/imageFile17.png>)

*Department of Computer Science & Engineering, The Ohio State University, menart.2@osu.edu †Equal Contribution ‡Department of Computer Science, The Johns Hopkins University, enayat@jhu.edu §Department of Computer Science, The Johns Hopkins University, arora@cs.jhu.edu ¶Department of Computer Science & Engineering and the Translational Data Analytics Institute (TDAI), The Ohio State University,

bassily.1@osu.edu

||Institute for Mathematical and Computational Engineering, Faculty of Mathematics and School of Engineering, Pontiﬁcia Universidad Cato´lica de Chile, crguzmanp@mat.uc.cl

ACD+22, FSS+19], or has imposed further restrictions on the loss function. In the latter camp, numerous possible assumptions have been proposed, such as the restricted secant inequality [ZY13] or star/quasar convexity [HSS20]. Perhaps the most promising such condition is the Polyak-Łojasiewicz (PL) condition [Pol63], and its generalization, the Kurdyka-Łojasiewicz (KL) condition [Kur98]1. A function F : Rd → R satisﬁes the (γ,κ)-KL condition if for all w ∈ Rd it holds that,

{F(w)} ≤ γκ  ∇F(w;S) κ (1)

F(w) − min

w

That is, the loss lower bounds the gradient norm. The PL condition is the special case where κ = 2. Both the KL and PL settings have been the subject of numerous works [KNS16, FSS18, SMS22]. The KL condition, in addition to being weaker than many of the previously mentioned conditions, has led to a number of strong convergence rate results. Furthermore, an increasingly rich literature has shown that overparameterized models such as neural networks satisfy the KL condition in a number of scenarios [BBM18, CP18, LZB22, SMS22].

On the other hand, the reliance of modern machine learning techniques on large datasets has caused growing concern over user privacy. Overparameterized models are of particular concern due to their ability to memorize training data [Swe21, CLE+19, FZ20, BBF+21]. In response to this concern, differential privacy (DP) has arisen as the most widely accepted method for ensuring the privacy of individuals present in a dataset. Unfortunately, it has been shown in a variety of settings that differentially private learning has fundamental limitations. As a result, characterizing these limitations has been the subject of numerous recent works.

Non-convex optimization under differential privacy is still not well understood. For example, in regards to the task of approximating stationary points in the DP setting, there are still gaps between existing upper and lower bounds [ABG+23]. Furthermore, for the problem of approximating global minimizers of non-convex loss functions under DP, it has been shown the best possible rate is only O nǫ d ), even if the optimization algorithm is allowed exponential running time [GTU23]. In the PL setting however, it has been shown that rates of O˜ n d

![image 18](<2023-menart-differentially-private-non-convex-optimization_images/imageFile18.png>)

2ǫ2 on the excess empirical risk are achievable [WYX17, LGR23]. Interestingly, this matches the optimal rate for DP optimization in the (much more restrictive) strongly convex setting, and subsequently lower bounds for this setting show the rate is optimal [BST14]. However, note that while the PL condition admits a large class of non-convex functions, it is still strong enough to exclude many convex functions. In contrast, any convex function satisﬁes the (R,1)-KL condition at least in the radius R ball around the minimizer. This can be obtained directly from the deﬁnition of convexity and the CauchySchwarz inequality. Given the promising (but limited) results for PL functions, the question arises whether similar results can be obtained for the more general class of objectives satisfying the KL condition, particularly since recent work has shown this generalization allows one to capture common models outside the reach of the PL condition [SMS22]. In this work, we answer this question in the afﬁrmative, and show that the KL assumption leads to fast rates under differential privacy, even in the absence of convexity. We further provide algorithms which are adaptive in the KL parameters. These results widen the range of non-convex models we can train effectively under DP.

![image 19](<2023-menart-differentially-private-non-convex-optimization_images/imageFile19.png>)

- 1.1 Contributions


In this work, we develop the ﬁrst algorithms for differentially private empirical risk minimization (ERM) under the (γ,κ)-KL condition without any convexity assumption. We show that for sufﬁciently smooth

![image 20](<2023-menart-differentially-private-non-convex-optimization_images/imageFile20.png>)

1These conditions are sometimes also referred to as the gradient domination condition. Further, the KL condition is sometimes phrased in terms of h(F(w) − minw{F(w)}), for some nondecreasing function h, akin to its ﬁrst appearance [Lez62]. In our work we instead focus on the (commonly studied) case where h is a monomial.

√d nǫ

κ on the excess empirical risk for any κ ∈ [1,2]. For κ ≥ 2, we give an algorithm which attains the same rate for the strictly larger class of weakly convex functions. This rate is new for any κ = 2. We further show this rate is near optimal when 1+ Ω(1) ≤ κ ≤ 2 by leveraging existing lower bounds for convex functions satisfying the growth condition. For 1 ≤ κ ≤ 2, we obtain our upper bound via a novel variant of the Spider algorithm, ﬁrst proposed in [FLLZ18]. This method allows us to leverage the reduced sensitivity of privatizing gradient differences to add less noise, an observation that has been leveraged in several other works studying the problem of ﬁnding stationary points under differential privacy [ABG+23, MS23]. We also leverage a novel round structure (i.e. the number of steps before the gradient estimator is reset) for our private Spider algorithm. Whereas previous works have largely used ﬁxed round lengths, our analysis crucially relies on variable round lengths with adaptive stopping. In the case where κ ≥ 2, we obtain our upper bound using a differentially private implementation of the approximate proximal point method.

![image 21](<2023-menart-differentially-private-non-convex-optimization_images/imageFile21.png>)

functions it is possible to achieve a rate of O˜

![image 22](<2023-menart-differentially-private-non-convex-optimization_images/imageFile22.png>)

For both these algorithms, our analysis leverages the fact that the KL condition forces large gradients during the run of the algorithm. We further show that these larger gradient norms allow us to add more noise “for free”, and thus better control the privacy budget. We use this observation to run Spider with a higher noise level than, for example, one would see without the KL condition [ABG+23].

Leveragingthis intuition, we further develop a simple variant of noisy gradientdescent that automatically scales the noise proportional to the gradient norm. We provide a novel analysis to show this algorithm achieves the rate O˜

√d nǫ

2κ 4−κ

+ n 1 κ/2 under the (γ,κ)-KL condition when κ ∈ [1,2]. This rate is

![image 23](<2023-menart-differentially-private-non-convex-optimization_images/imageFile23.png>)

![image 24](<2023-menart-differentially-private-non-convex-optimization_images/imageFile24.png>)

![image 25](<2023-menart-differentially-private-non-convex-optimization_images/imageFile25.png>)

![image 26](<2023-menart-differentially-private-non-convex-optimization_images/imageFile26.png>)

√d nǫ

2/3 in the slowest regime (κ = 1). This result is adaptive and requires no prior knowledge of the KL parameters. We additionally prove that this same gradient descent algorithm can achieve fast convergence guarantees even when the KL condition does not hold. In this case where no KL assumption is made, we settle for convergence to a stationary point as approximating a global minimizer is intractable, in general. Speciﬁcally, we show that when the trajectory of noisy gradient descent encounters mostly points with large gradient norm, the algorithm ﬁnds a point with gradient norm O˜

![image 27](<2023-menart-differentially-private-non-convex-optimization_images/imageFile27.png>)

- O˜ n2 dǫ2 when κ = 2 (i.e. nearly optimal) and is O˜


![image 28](<2023-menart-differentially-private-non-convex-optimization_images/imageFile28.png>)

![image 29](<2023-menart-differentially-private-non-convex-optimization_images/imageFile29.png>)

√

![image 30](<2023-menart-differentially-private-non-convex-optimization_images/imageFile30.png>)

d

nǫ . We further establish that in the worst case, the algorithm ﬁnds a point with gradient norm at most O˜

![image 31](<2023-menart-differentially-private-non-convex-optimization_images/imageFile31.png>)

√

1/2 , recovering the best known rate for noisy gradient descent in this setting.

![image 32](<2023-menart-differentially-private-non-convex-optimization_images/imageFile32.png>)

d nǫ

![image 33](<2023-menart-differentially-private-non-convex-optimization_images/imageFile33.png>)

- 1.2 Related Work


Differentially private optimization by now has a rich literature spanning over a decade. Much of this attention has been directed at the convex setting [CMS11, JKT12, KST12, BST14, TTZ14, TTZ15, BFTGT19, FKT20, AFKT21, BGN21]. The study of differentially private optimization in the non-convex setting is comparatively newer, but has nonetheless been growing rapidly [WYX17, GTU23, ABG+23, GLOT23].

Currently, research into DP non-convex optimization under the KL condition speciﬁcally has been restricted to the special case of the PL condition. Assuming that the loss is Lipschitz, smooth, and satisﬁes the PL condition, the works [WYX17, LGR23] obtained the rate of O˜ n2 dǫ2 on the excess empirical risk. This rate is optimal because of existing lower bounds for the strongly convex setting [BST14]. More recently, [YHL+22] studied the (more general) minmax optimization problems under differential privacy when the primal objective is assumed to be PL, although the rates therein are slower. Alternatively, in the convex setting, [ALD21] characterized the optimal rates for DP optimization under an assumption known as the growth condition. When convexity is assumed, the KL condition and the growth condition are equivalent [BNPS17, Theorem 5.2]. Further, convex functions satisfying the growth condition are a strict subset of (general) KL functions.

![image 34](<2023-menart-differentially-private-non-convex-optimization_images/imageFile34.png>)

There are also a number of works which have studied optimization under the KL condition without pri-

vacy considerations. The early works [Pol63, Lez62] were the ﬁrst to show that for gradient descent, linear convergence rates are possible when the objective is smooth and satisﬁes the PL condition. More recently, [BBM18] showed that under an additional assumption known as the interpolation condition, stochastic gradient descent also achieves linear convergence. The works [LZB22, SMS22] studied more general variants of the PL/KL conditions called the PL*/KL* conditions respectively. Speciﬁcally, these works study convergence when the condition holds only over a subset of Rd.

# 2 Preliminaries

Empirical Risk Minimization Let X be a data domain and let S = {x1,...,xn} ∈ Xn be a dataset of n points. Let f : Rd × X → R be a loss function and deﬁne the empirical risk/loss as F(w;S) =

n i=1 f(w;xi). We denote the set of global minimizers as W∗ = argminw F(w;S), which we assume is nonempty. We assume we are given some starting point w0 ∈ Rd and deﬁne the closest global minimizer to w0 as w∗. That is w∗ = argminw∈W∗ { w0 − w }. As W∗ may be non-convex, multiple such minimizers may exist, but it sufﬁces to select one arbitrarily. We consider the problem of minimizing the excess empirical risk, deﬁned at a point w as F(w;S) − F(w∗;S). We assume throughout that f is L0-Lipschitz continuous over some ball (to be deﬁned later). We will denote the d-dimensional ball centered at w of radius B as BB(w).

1 n

![image 35](<2023-menart-differentially-private-non-convex-optimization_images/imageFile35.png>)

KL* Condition Since assuming the loss satisﬁes the KL condition over all of Rd is unrealistic in practice (and indeed impossible if Lipschitzness is assumed), several works have proposed the modiﬁed KL* condition [SMS22, LZB22]. The exact deﬁnition of this condition varies. We use the following deﬁnition.

- Deﬁnition 1. A function F : Rd → R satisﬁes the (γ,κ)-KL* condition on S ⊂ Rd w.r.t. w′ ∈ Rd if ∀w ∈ S it holds that γκ ∇F(w) κ ≥ F(w) − F(w′).


We will take w′ = w∗ (i.e. the closest global minimizer to w0) unless otherwise stated. In this case, under the KL* condition, one equivalently has γ1(F(w) − F(w∗))1/κ ≤  ∇F(w) . Prior work studying the PL*/KL* condition has generally further assumed F(w∗) = 0, but we will avoid this assumption for the sake of generality [LZB22, SMS22]. We note that the condition is often phrased so that the constant γ has no exponent, however this deﬁnition will ease notation in our analysis; a conversion to the standard deﬁnition is straightforward. For our algorithms, we will show that it is sufﬁcient for the KL* condition to hold in a ball around an initial point w0. Our guarantees could alternatively be phrased under the condition that the KL* assumptions holds in a ball around w∗, (see Remark 1, Appendix A).

![image 36](<2023-menart-differentially-private-non-convex-optimization_images/imageFile36.png>)

Relevant to our discussion will also be the notion of the (λ,τ)-growth condition, which states that for any w ∈ Rd, it holds that F(w) − F(w∗) ≥ λτ w − w∗ τ. When the loss function is also assumed to be convex, the KL and growth conditions are in fact equivalent up to parameterization. See Appendix A for more details.

Loss bound We assume throughoutthat one is given a bound F0 ≥ 0 such that F(w0;S)−F(w∗;S) ≤ F0 for some w0 ∈ Rd. However, as our results will assume the KL condition holds at w0, one always has the worst case bound F0 ≤ γκLκ0 by the fact that the loss is L0-Lipschitz.

Differential Privacy (DP): We consider primarily the notion of zero concentrated differential privacy (zCDP). For the purpose of referencing existing work, we also deﬁne approximate DP.

- Deﬁnition 2 (ρ-zCDP [BS16]). An algorithm A is ρ-zCDP if for all datasets S and S′ differing in one data point and all α ∈ (1,∞), it holds that Dα(A(S)||A(S′)) ≤ ρα, where Dα is the α-Renyi´ divergence.
- Deﬁnition 3 ((ǫ,δ)-DP [DMNS06]). An algorithm A is (ε,δ)-differentially private if for all datasets S and S′ differing in one data point and all events E in the range of the A, we have, P (A(S) ∈ E) ≤ eεP (A(S′) ∈ E) + δ.


zCDP guarantees imply approximate DP guarantees. Speciﬁcally, we note that for any δ > 0 and ǫ ≤ log(1/δ), (ǫ,δ)-DP guarantees can be obtained from our results by setting ρ = O ǫ2/ log(1/δ) [BS16, Proposition 1.3].

![image 37](<2023-menart-differentially-private-non-convex-optimization_images/imageFile37.png>)

Weak Convexity A function F : Rd → R is L˜1-weakly convex w.r.t. · if for all 0 ≤ λ ≤ 1 and w,v ∈ Rd one has f(λw + (1 − λ)v) ≤ λf(w) + (1 − λ)f(v) + L˜

1λ(1−λ)

2 w − v 2.

![image 38](<2023-menart-differentially-private-non-convex-optimization_images/imageFile38.png>)

# 3 Optimal Algorithm for 1 ≤ κ ≤ 2

![image 39](<2023-menart-differentially-private-non-convex-optimization_images/imageFile39.png>)

- Algorithm 1 KL Spider


![image 40](<2023-menart-differentially-private-non-convex-optimization_images/imageFile40.png>)

Require: Dataset S = {x1,...,xn}, Privacy parameter ρ > 0, Failure probability β > 0, Initial point w0 ∈ Rd, Loss bound F0 ≤ (L0γ)κ, KL* parameters (γ,κ), Lipschitz parameter L0, Smoothness parameter L1

- 1: w0,0 = w0, Φˆ0 = F0
- 2: c = 1 + F

2−κ κ

![image 41](<2023-menart-differentially-private-non-convex-optimization_images/imageFile41.png>)

0

1 64γ2L1

![image 42](<2023-menart-differentially-private-non-convex-optimization_images/imageFile42.png>)

- 3: K = (1 + 64(1/F0)

2−κ

![image 43](<2023-menart-differentially-private-non-convex-optimization_images/imageFile43.png>)

κ γ2L1) log(F0) + κ log n

√ρ

![image 44](<2023-menart-differentially-private-non-convex-optimization_images/imageFile44.png>)

![image 45](<2023-menart-differentially-private-non-convex-optimization_images/imageFile45.png>)

γL0√d , β′ = Kβ γL

![image 46](<2023-menart-differentially-private-non-convex-optimization_images/imageFile46.png>)

![image 47](<2023-menart-differentially-private-non-convex-optimization_images/imageFile47.png>)

0

√

![image 48](<2023-menart-differentially-private-non-convex-optimization_images/imageFile48.png>)

Kd n√ρF01/κ

![image 49](<2023-menart-differentially-private-non-convex-optimization_images/imageFile49.png>)

![image 50](<2023-menart-differentially-private-non-convex-optimization_images/imageFile50.png>)

2−κ

- 4: σˆ = L

0

√K n√ρ

![image 51](<2023-menart-differentially-private-non-convex-optimization_images/imageFile51.png>)

![image 52](<2023-menart-differentially-private-non-convex-optimization_images/imageFile52.png>)

![image 53](<2023-menart-differentially-private-non-convex-optimization_images/imageFile53.png>)

- 5: for k = 1,...,K do
- 6: Φˆk = max 1cΦˆk−1, min 32γL0

![image 54](<2023-menart-differentially-private-non-convex-optimization_images/imageFile54.png>)

√

![image 55](<2023-menart-differentially-private-non-convex-optimization_images/imageFile55.png>)

Kd log(1/β′) n√ρ

![image 56](<2023-menart-differentially-private-non-convex-optimization_images/imageFile56.png>)

![image 57](<2023-menart-differentially-private-non-convex-optimization_images/imageFile57.png>)

κ

,F0

- 7: Tk = (F0/Φˆk)

2−κ

![image 58](<2023-menart-differentially-private-non-convex-optimization_images/imageFile58.png>)

κ , σk = Φˆ

1/κ k

√TkK γn√ρ

![image 59](<2023-menart-differentially-private-non-convex-optimization_images/imageFile59.png>)

![image 60](<2023-menart-differentially-private-non-convex-optimization_images/imageFile60.png>)

![image 61](<2023-menart-differentially-private-non-convex-optimization_images/imageFile61.png>)

- 8: ∇k,0 = n1 ni=1 ∇f(wk,0;xi) + bk,0 where bk,0 ∼ N(0,Idσˆ2)

![image 62](<2023-menart-differentially-private-non-convex-optimization_images/imageFile62.png>)

- 9: t = 0
- 10: while t ≤ Tk and  ∇t,k ≥ 87γΦˆ1k/κ do

![image 63](<2023-menart-differentially-private-non-convex-optimization_images/imageFile63.png>)

- 11: ηk,t = 4γL 1

![image 64](<2023-menart-differentially-private-non-convex-optimization_images/imageFile64.png>)

1 ∇k,t

Φ ˆ1k/κ

- 12: wk,t+1 = wk,t − ηk,t∇k,t
- 13: ∆k,t+1 = n1 ni=1[∇f(wk,t+1;xi) − ∇f(wk,t;xi)] + bk,t+1, where bk,t+1 ∼ N(0,Idσk2)

![image 65](<2023-menart-differentially-private-non-convex-optimization_images/imageFile65.png>)

- 14: ∇k,t+1 = ∇k,t + ∆k,t+1
- 15: t = t + 1
- 16: end while
- 17: wk+1,0 = wk,t−1
- 18: end for
- 19: Return w¯ = wK+1,0


![image 66](<2023-menart-differentially-private-non-convex-optimization_images/imageFile66.png>)

Algorithm Overview Algorithm 1 is roughly an implementation of noisy Spider with some key differences. Similar to Spider, the algorithm runs over K rounds. At the start of any round k, a noisy minibatch gradient estimate ∇k,0, is computed. Throughout the rest of the round, the gradient is estimated using the change in the gradient between iterates. That is, for some t ≥ 0, ∇k,t = ∇k,0 + tj=1 ∆k,j, where each ∆k,j corresponds to an estimate of a gradient difference. After each gradient estimate is obtained, a standard (normalized) gradient descent update step is performed.

In contrast to traditional Spider, at the start of each round k ∈ [K], a target excess risk threshold, Φˆk, is set. The algorithm then uses this threshold to deﬁne an adaptive stopping mechanism for the round. The stopping condition is needed for the event where the excess risk of the update iterate falls below Φˆk before the end of the phase. If this happens, the loss lower bound (and hence the gradient norm lower bound) will not be strong enough for the subsequent iterate. Consequently, the noise added for privacy could be too large and cause the trajectory of the algorithm to diverge. As such, we check to see if the loss has fallen below the target threshold before performing any update. We do this indirectly by checking the gradient norm and using the KL condition, as bounding the sensitivity of the loss itself (to ensure privacy) is more delicate. Our implementation also uses varying phase lengths such that the length of the k’th phase is roughly (1/Φˆk)(2−κ)/κ (note the exponent is non-negative since κ ≤ 2). Speciﬁcally, the phases get longer as the algorithm progresses. This is due to the fact that as the excess risk decreases, the lower bound on the gradient norm (induced by the KL condition) becomes weaker, leading to progressively slower convergence. We have the following guarantee on the Algorithm.

κ−1 κ

1/κ 0

- Theorem 1. Let γ > 0, κ ∈ [1,2]. There exists B = O˜ F


![image 67](<2023-menart-differentially-private-non-convex-optimization_images/imageFile67.png>)

γL1 + F

0 γ such that if f is L0-Lipschitz and L1-smooth over BB(w0), Algorithm 1 is ρ-zCDP. Further, if F(·;S) satisﬁes the (γ,κ)-KL* condition over BB(w0), with probability at least 1 − β the output of Algorithm 1 satisﬁes

![image 68](<2023-menart-differentially-private-non-convex-optimization_images/imageFile68.png>)

√

![image 69](<2023-menart-differentially-private-non-convex-optimization_images/imageFile69.png>)

κ

κ

2−κ

![image 70](<2023-menart-differentially-private-non-convex-optimization_images/imageFile70.png>)

κ γ2L1 n√ρ

γL0

d 1 + (1/F0)

![image 71](<2023-menart-differentially-private-non-convex-optimization_images/imageFile71.png>)

γL0 dK log(1/β′) n√ρ

![image 72](<2023-menart-differentially-private-non-convex-optimization_images/imageFile72.png>)

= O˜

F( ¯w;S) − F(w∗;S) = O

,

![image 73](<2023-menart-differentially-private-non-convex-optimization_images/imageFile73.png>)

![image 74](<2023-menart-differentially-private-non-convex-optimization_images/imageFile74.png>)

![image 75](<2023-menart-differentially-private-non-convex-optimization_images/imageFile75.png>)

![image 76](<2023-menart-differentially-private-non-convex-optimization_images/imageFile76.png>)

2−κ

κ γ2L1) log(F0) + κ log n

where K,β′ are as deﬁned in Algorithm 1, namely K = (1 + 64(1/F0)

![image 77](<2023-menart-differentially-private-non-convex-optimization_images/imageFile77.png>)

√

√ρ

2−κ

![image 78](<2023-menart-differentially-private-non-convex-optimization_images/imageFile78.png>)

![image 79](<2023-menart-differentially-private-non-convex-optimization_images/imageFile79.png>)

γL0√d , and β′ = Kβ γL

Kd n√ρF01/κ

0

.

![image 80](<2023-menart-differentially-private-non-convex-optimization_images/imageFile80.png>)

![image 81](<2023-menart-differentially-private-non-convex-optimization_images/imageFile81.png>)

![image 82](<2023-menart-differentially-private-non-convex-optimization_images/imageFile82.png>)

![image 83](<2023-menart-differentially-private-non-convex-optimization_images/imageFile83.png>)

![image 84](<2023-menart-differentially-private-non-convex-optimization_images/imageFile84.png>)

Note the result can be further simpliﬁed by setting F0 = (L0γ)κ (which is always possible by the KL condition) which makes (1/F0)

κL1

2−κ

κ γ2L1 = γ

L20−κ. We defer the proof of privacy to Appendix B.1, as it is a standard application of the privacy guarantees of the Gaussian mechanism and composition. In the following, we focus on proving the convergence guarantee of the algorithm.

![image 85](<2023-menart-differentially-private-non-convex-optimization_images/imageFile85.png>)

![image 86](<2023-menart-differentially-private-non-convex-optimization_images/imageFile86.png>)

Convergence Proof for Algorithm 1 Our ability to assume loss properties hold only over BB(w0) (rather than Rd) hinges on bounding the trajectory of the algorithm. We assume for the following lemmas that the conditions of Theorem 1 hold.

- Lemma 1. For any k ∈ [K] and t ∈ [Tk] corresponding to iterates of Algorithm 1, it holds with probability


κ−1 κ

1/κ 0

1 that wk,t ∈ BB(w0) for some B = O˜ F

![image 87](<2023-menart-differentially-private-non-convex-optimization_images/imageFile87.png>)

γL1 + F

0 γ .

![image 88](<2023-menart-differentially-private-non-convex-optimization_images/imageFile88.png>)

The implication of this result is that the algorithm starts in, and never leaves the KL region around w0. Thus the KL property holds at every iterate of the algorithm. We provide a proof in Appendix B.3. Note

1/κ 0

that any L1-smooth function is also L′1-smooth for L′1 > L1. Thus the F

γL1 term in the distance bound can

![image 89](<2023-menart-differentially-private-non-convex-optimization_images/imageFile89.png>)

be made negligible by running the algorithm with L1 ≥ F0(2−κ)/2/γ (although this may increase the rate depending on F0 and γ).

Our utility proof for Algorithm 1, will crucially rely on the following lemma which bounds the gradient error at any step in terms of the excess risk target, Φˆk.

- Lemma 2. With probability at least 1 − β, for every k ∈ [K] and t ∈ [Tk] indexing the iterates of the algorithm, one has that  ∇k,t − ∇F(wk,t;S) ≤ 81γ Φˆ1k/κ. Proof. The gradient estimates are generated by using exact gradients plus Gaussian noise, thus


![image 90](<2023-menart-differentially-private-non-convex-optimization_images/imageFile90.png>)

 ∇k,t − ∇F(wk,t; S) 2

t

= ∇F(wk,0; S) + bk,0 +

j=1

∇F(wk,j; S) − ∇F(wk,j−1; S) + bk,j − ∇F(wk,t; S) 2 =

t

bk,j

j=0

2

.

We can use Gaussian concentration results, see [JNG+19, Lemma 2], to conclude that for any τ ≥ 0,

√K

2

![image 91](<2023-menart-differentially-private-non-convex-optimization_images/imageFile91.png>)

. Thus, under the settings of σˆ = L

- P [ ∇k,t − ∇F(wk,t;S) ≥ τ] ≤ 2 exp − τ


0

n√ρ and σk = Φˆ

![image 92](<2023-menart-differentially-private-non-convex-optimization_images/imageFile92.png>)

![image 93](<2023-menart-differentially-private-non-convex-optimization_images/imageFile93.png>)

2d(ˆσ2+ Tj=1k σk2)

![image 94](<2023-menart-differentially-private-non-convex-optimization_images/imageFile94.png>)

√TkK

1/κ k

![image 95](<2023-menart-differentially-private-non-convex-optimization_images/imageFile95.png>)

2−κ

γn√ρ and Tk = (F0/Φˆk)

κ , one has that with probability at least 1 − β′ that:

![image 96](<2023-menart-differentially-private-non-convex-optimization_images/imageFile96.png>)

![image 97](<2023-menart-differentially-private-non-convex-optimization_images/imageFile97.png>)

![image 98](<2023-menart-differentially-private-non-convex-optimization_images/imageFile98.png>)

![image 99](<2023-menart-differentially-private-non-convex-optimization_images/imageFile99.png>)

![image 100](<2023-menart-differentially-private-non-convex-optimization_images/imageFile100.png>)

 ∇k,t − ∇F(wk,t;S) ≤ 2 dlog(1/β′)(ˆσ + Tkσk)

![image 101](<2023-menart-differentially-private-non-convex-optimization_images/imageFile101.png>)

![image 102](<2023-menart-differentially-private-non-convex-optimization_images/imageFile102.png>)

2L0 Kdlog(1/β′) n√ρ

2 Kdlog(1/β′) γn√ρ

κ−1 κ

2−κ κ

Φˆ

![image 103](<2023-menart-differentially-private-non-convex-optimization_images/imageFile103.png>)

![image 104](<2023-menart-differentially-private-non-convex-optimization_images/imageFile104.png>)

+

k F

=

![image 105](<2023-menart-differentially-private-non-convex-optimization_images/imageFile105.png>)

![image 106](<2023-menart-differentially-private-non-convex-optimization_images/imageFile106.png>)

0

![image 107](<2023-menart-differentially-private-non-convex-optimization_images/imageFile107.png>)

![image 108](<2023-menart-differentially-private-non-convex-optimization_images/imageFile108.png>)

- (i)

≤

2L0 Kdlog(1/β′) n√ρ

![image 109](<2023-menart-differentially-private-non-convex-optimization_images/imageFile109.png>)

![image 110](<2023-menart-differentially-private-non-convex-optimization_images/imageFile110.png>)

![image 111](<2023-menart-differentially-private-non-convex-optimization_images/imageFile111.png>)

+

2 Kdlog(1/β′) γn√ρ

![image 112](<2023-menart-differentially-private-non-convex-optimization_images/imageFile112.png>)

![image 113](<2023-menart-differentially-private-non-convex-optimization_images/imageFile113.png>)

![image 114](<2023-menart-differentially-private-non-convex-optimization_images/imageFile114.png>)

F01/κ

- (ii)


![image 115](<2023-menart-differentially-private-non-convex-optimization_images/imageFile115.png>)

4L0 Kdlog(1/β′) n√ρ

(iii)

≤

≤

![image 116](<2023-menart-differentially-private-non-convex-optimization_images/imageFile116.png>)

![image 117](<2023-menart-differentially-private-non-convex-optimization_images/imageFile117.png>)

1 8γ

Φˆ1k/κ.

![image 118](<2023-menart-differentially-private-non-convex-optimization_images/imageFile118.png>)

Above, (i) uses Φˆk ≤ F0. Step (ii) uses that F0 ≤ (γL0)κ by the KL condition and Lipschitzness. Step (iii) uses the fact that Φˆk ≥ 32γL0

√

κ

![image 119](<2023-menart-differentially-private-non-convex-optimization_images/imageFile119.png>)

Kd log(1/β′) n√ρ

.

![image 120](<2023-menart-differentially-private-non-convex-optimization_images/imageFile120.png>)

![image 121](<2023-menart-differentially-private-non-convex-optimization_images/imageFile121.png>)

√

κ

![image 122](<2023-menart-differentially-private-non-convex-optimization_images/imageFile122.png>)

Kd log(1/β′) n√ρ

Finally, we observe that for all k ∈ [K], Φˆk ≥ 32γL0

and 2−2κ ≥ 0. Hence, the total number of iterations of the algorithm is at most

![image 123](<2023-menart-differentially-private-non-convex-optimization_images/imageFile123.png>)

![image 124](<2023-menart-differentially-private-non-convex-optimization_images/imageFile124.png>)

![image 125](<2023-menart-differentially-private-non-convex-optimization_images/imageFile125.png>)

K

Tk ≤ K F0

k=1

n√ρ 32γL0 Kd log(1/β′)

![image 126](<2023-menart-differentially-private-non-convex-optimization_images/imageFile126.png>)

![image 127](<2023-menart-differentially-private-non-convex-optimization_images/imageFile127.png>)

![image 128](<2023-menart-differentially-private-non-convex-optimization_images/imageFile128.png>)

κ 2−κκ

![image 129](<2023-menart-differentially-private-non-convex-optimization_images/imageFile129.png>)

≤ K

n√ρF01/κ γL0

![image 130](<2023-menart-differentially-private-non-convex-optimization_images/imageFile130.png>)

√

![image 131](<2023-menart-differentially-private-non-convex-optimization_images/imageFile131.png>)

![image 132](<2023-menart-differentially-private-non-convex-optimization_images/imageFile132.png>)

Kd

2−κ

.

Thus by the deﬁnition of β′, over the run of the algorithm, we have with probability at least 1−β that every gradient estimate satisﬁes the desired error bound.

![image 133](<2023-menart-differentially-private-non-convex-optimization_images/imageFile133.png>)

![image 134](<2023-menart-differentially-private-non-convex-optimization_images/imageFile134.png>)

![image 135](<2023-menart-differentially-private-non-convex-optimization_images/imageFile135.png>)

![image 136](<2023-menart-differentially-private-non-convex-optimization_images/imageFile136.png>)

We can now prove the main theorem.

Proof of Theorem 1. In the following, we condition on the high probability event that the gradient errors are bounded, as shown in Lemma 2. Further, recall that by Lemma 1 the trajectory {wk,t}k∈[K],t∈[Tk] is contained in BB(w0) with probability 1, and that the (γ,κ)-KL* conditions holds over this set.

We will show that at the end of the the k’th phase (i.e. the k’th iteration of the outer loop), the excess risk is at most Φˆk. First, consider the case where at some point during the phase the gradient norm stopping condition is reached. In this case, the condition in the while loop ensures  ∇k,t ≤ 87γ Φˆ1k/κ. Thus by Lemma 2 and a triangle inequality we have  ∇F(wk,t;S) ≤ 87γΦˆ1k/κ + 81γ Φˆ1k/κ = γ1Φˆ1k/κ. Then by the KL assumption we have that F(wk,t;S) − F(w∗;S) ≤ γκ ∇F(wk,t;S) κ ≤ γκ(γ1Φˆ1k/κ)κ ≤ Φˆk, as desired.

![image 137](<2023-menart-differentially-private-non-convex-optimization_images/imageFile137.png>)

![image 138](<2023-menart-differentially-private-non-convex-optimization_images/imageFile138.png>)

![image 139](<2023-menart-differentially-private-non-convex-optimization_images/imageFile139.png>)

![image 140](<2023-menart-differentially-private-non-convex-optimization_images/imageFile140.png>)

![image 141](<2023-menart-differentially-private-non-convex-optimization_images/imageFile141.png>)

We thus turn towards analyzing the alternative case, where the ﬁnal iterate of the phase is wk,T

, using an induction argument. Speciﬁcally, under the inductive assumption that F(wk,0;S) − F(w∗;S) ≤ Φˆk−1, we will show that F(wk,T

k

;S)−F(w∗;S) ≤ Φˆk. For the base case, we clearly have F(w0,0;S)−F(w∗;S) ≤ Φˆ0 = F0. Using smoothness and the setting of ηk,t, we can obtain the following descent inequality,

k

1 4L1 ∇k,t − ∇F(wk,t;S) 2.

1 16γL1 ∇k,t Φ ˆ1k/κ −

F(wk,t;S) − F(wk,t+1;S) ≥

![image 142](<2023-menart-differentially-private-non-convex-optimization_images/imageFile142.png>)

![image 143](<2023-menart-differentially-private-non-convex-optimization_images/imageFile143.png>)

We leave the derivation of the above inequality to Lemma 9 in Appendix B.2. We now can use the fact that updates are only performed when  ∇k,t ≥ 87γ Φˆ1k/κ and the bound on the gradient estimate error derived in

![image 144](<2023-menart-differentially-private-non-convex-optimization_images/imageFile144.png>)

- Lemma 2 to obtain


1 32γ2L1

1 256γ2L1

1 64γ2L1

Φˆ2k/κ. Summing over all Tk = (F0/Φˆk)

Φˆ2k/κ −

Φˆ2k/κ ≥

F(wk,t;S) − F(wk,t+1;S) ≥

![image 145](<2023-menart-differentially-private-non-convex-optimization_images/imageFile145.png>)

![image 146](<2023-menart-differentially-private-non-convex-optimization_images/imageFile146.png>)

![image 147](<2023-menart-differentially-private-non-convex-optimization_images/imageFile147.png>)

κ−2

2 iterations yields F(wk,0,S) − F(wk,T

![image 148](<2023-menart-differentially-private-non-convex-optimization_images/imageFile148.png>)

1 64γ2L1

1 64γ2L1

2−κ κ

TkΦˆ2k/κ =

0 Φˆk. We then have the following manipulation leveraging the inductive hypothesis,

;S) ≥

![image 149](<2023-menart-differentially-private-non-convex-optimization_images/imageFile149.png>)

F

![image 150](<2023-menart-differentially-private-non-convex-optimization_images/imageFile150.png>)

![image 151](<2023-menart-differentially-private-non-convex-optimization_images/imageFile151.png>)

k

1 64γ2L1

2−κ κ

0 Φˆk

F(wk,0;S) − F(w∗;S) + F(w∗;S) − F(wk,T

;S) ≥

![image 152](<2023-menart-differentially-private-non-convex-optimization_images/imageFile152.png>)

F

![image 153](<2023-menart-differentially-private-non-convex-optimization_images/imageFile153.png>)

k

1 64γ2L1c

2−κ κ

Φˆk−1 + F(w∗;S) − F(wk,T

0 Φˆk−1 1 − F

;S) ≥

![image 154](<2023-menart-differentially-private-non-convex-optimization_images/imageFile154.png>)

F

![image 155](<2023-menart-differentially-private-non-convex-optimization_images/imageFile155.png>)

k

1 64γ2L1c

2−κ κ

Φ ˆk−1 ≥ F(wk,T

;S) − F(w∗;S) Φˆk ≥ F(wk,T

![image 156](<2023-menart-differentially-private-non-convex-optimization_images/imageFile156.png>)

![image 157](<2023-menart-differentially-private-non-convex-optimization_images/imageFile157.png>)

0

k

;S) − F(w∗;S). The last step follows because 1 − F

k

2−κ κ

64γ2L1c = 1c and 1cΦˆk ≤ Φˆk−1. We have now shown that ﬁnal iterate of each phase has excess risk at most Φˆk.

1

![image 158](<2023-menart-differentially-private-non-convex-optimization_images/imageFile158.png>)

![image 159](<2023-menart-differentially-private-non-convex-optimization_images/imageFile159.png>)

![image 160](<2023-menart-differentially-private-non-convex-optimization_images/imageFile160.png>)

![image 161](<2023-menart-differentially-private-non-convex-optimization_images/imageFile161.png>)

0

√

κ

![image 162](<2023-menart-differentially-private-non-convex-optimization_images/imageFile162.png>)

Now, all that remains is to show that ΦˆK ≤ 32γL0

Kd log(1/β′) n√ρ

. Noting that we have ΦˆK ≤ max 1c KF0, 32γL0

![image 163](<2023-menart-differentially-private-non-convex-optimization_images/imageFile163.png>)

![image 164](<2023-menart-differentially-private-non-convex-optimization_images/imageFile164.png>)

√

√

κ

κ

![image 165](<2023-menart-differentially-private-non-convex-optimization_images/imageFile165.png>)

it sufﬁces to show that 1c KF0 ≤ γL

Kd log(1/β′) n√ρ

![image 166](<2023-menart-differentially-private-non-convex-optimization_images/imageFile166.png>)

d n√ρ

0

. The inequality

![image 167](<2023-menart-differentially-private-non-convex-optimization_images/imageFile167.png>)

![image 168](<2023-menart-differentially-private-non-convex-optimization_images/imageFile168.png>)

![image 169](<2023-menart-differentially-private-non-convex-optimization_images/imageFile169.png>)

![image 170](<2023-menart-differentially-private-non-convex-optimization_images/imageFile170.png>)

![image 171](<2023-menart-differentially-private-non-convex-optimization_images/imageFile171.png>)

![image 172](<2023-menart-differentially-private-non-convex-optimization_images/imageFile172.png>)

√ρ γL0

log(F0)+κ log( n

√d n√ρ

![image 173](<2023-menart-differentially-private-non-convex-optimization_images/imageFile173.png>)

κ

√d )

KF0 ≤ γL

![image 174](<2023-menart-differentially-private-non-convex-optimization_images/imageFile174.png>)

![image 175](<2023-menart-differentially-private-non-convex-optimization_images/imageFile175.png>)

![image 176](<2023-menart-differentially-private-non-convex-optimization_images/imageFile176.png>)

- 1


log(c) ≤ K. Using the fact that log(1 + x) ≥ 1+xx for x ≥ 0, we can obtain that log(c) = log(1 + 1/[64F

0

is equivalent to

![image 177](<2023-menart-differentially-private-non-convex-optimization_images/imageFile177.png>)

![image 178](<2023-menart-differentially-private-non-convex-optimization_images/imageFile178.png>)

![image 179](<2023-menart-differentially-private-non-convex-optimization_images/imageFile179.png>)

![image 180](<2023-menart-differentially-private-non-convex-optimization_images/imageFile180.png>)

c

![image 181](<2023-menart-differentially-private-non-convex-optimization_images/imageFile181.png>)

κ−2 κ

κ−2 κ

0 γ2L1)−1. It thus sufﬁces to have K ≥ (1 + 64(1/F0)

0 γ2L1]) ≥ (1 + 64F

![image 182](<2023-menart-differentially-private-non-convex-optimization_images/imageFile182.png>)

![image 183](<2023-menart-differentially-private-non-convex-optimization_images/imageFile183.png>)

√ρ γL0

κ γ2L1) log(F0) + κ log n

2−κ

![image 184](<2023-menart-differentially-private-non-convex-optimization_images/imageFile184.png>)

d , which is satisﬁed by the algorithm.

![image 185](<2023-menart-differentially-private-non-convex-optimization_images/imageFile185.png>)

![image 186](<2023-menart-differentially-private-non-convex-optimization_images/imageFile186.png>)

![image 187](<2023-menart-differentially-private-non-convex-optimization_images/imageFile187.png>)

√

![image 188](<2023-menart-differentially-private-non-convex-optimization_images/imageFile188.png>)

![image 189](<2023-menart-differentially-private-non-convex-optimization_images/imageFile189.png>)

![image 190](<2023-menart-differentially-private-non-convex-optimization_images/imageFile190.png>)

![image 191](<2023-menart-differentially-private-non-convex-optimization_images/imageFile191.png>)

- 3.1 Lower Bound


We now demonstrate a lower bound showing that our upper bound is nearly optimal. To do this, we leverage an existing lower bound from [ALD21] for functions exhibiting the growth condition. In Theorem 6 in

τ τ−1

√

−1

![image 192](<2023-menart-differentially-private-non-convex-optimization_images/imageFile192.png>)

![image 193](<2023-menart-differentially-private-non-convex-optimization_images/imageFile193.png>)

d λnǫ

τ−1 L0

Appendix B.4, we extend their result to smooth functions and give a lower bound of Ω (τ)

![image 194](<2023-menart-differentially-private-non-convex-optimization_images/imageFile194.png>)

![image 195](<2023-menart-differentially-private-non-convex-optimization_images/imageFile195.png>)

on excess empirical risk of (ǫ,δ)-DP procedures for convex functions satisfying (λ,τ)-growth. Combining this result with the fact that the (γ1, κ−κ1)-growth condition and convexity implies the (γ,κ)-KL condition (Theorem 5.2 (ii) in [BNPS17], restated as Lemma 6), yields the following lower bound.

![image 196](<2023-menart-differentially-private-non-convex-optimization_images/imageFile196.png>)

![image 197](<2023-menart-differentially-private-non-convex-optimization_images/imageFile197.png>)

Corollary 1. Let B,L0,L1 > 0 and 1 < κ ≤ 2 such that κ = 1 + Ω(1). For any ρ-zCDP algorithm, A, there exists a dataset, S, point w0 ∈ Rd, and loss function f such that f is L0-Lipschitz and L1smooth over BB(w0) and F(·;S) is (γ,κ)-KL, for which the output of A has expected excess empirical risk Ω˜ γL

√

κ

![image 198](<2023-menart-differentially-private-non-convex-optimization_images/imageFile198.png>)

d n√ρ

0

.

![image 199](<2023-menart-differentially-private-non-convex-optimization_images/imageFile199.png>)

![image 200](<2023-menart-differentially-private-non-convex-optimization_images/imageFile200.png>)

Note the bound is independent of B and L1. More details on how to obtain Corollary 1 from the result of [ALD21] can be found in Appendix B.5.

# 4 Algorithm for κ ≥ 2

![image 201](<2023-menart-differentially-private-non-convex-optimization_images/imageFile201.png>)

- Algorithm 2 (KL) Proximal Point Method


![image 202](<2023-menart-differentially-private-non-convex-optimization_images/imageFile202.png>)

Require: Dataset S, Privacy parameter ρ, zCDP Optimizer for SC loss A, Initial point w0 ∈ Rd, Initial loss bound, F0 ≥ 0, Failure probability β, Lipschitz parameter L0, Weak convexity L˜1

- 1: T = (1 + 32F

κ−2 κ

![image 203](<2023-menart-differentially-private-non-convex-optimization_images/imageFile203.png>)

0 γ2L˜1) log(F0) + κ log n

√ρ γL0

![image 204](<2023-menart-differentially-private-non-convex-optimization_images/imageFile204.png>)

![image 205](<2023-menart-differentially-private-non-convex-optimization_images/imageFile205.png>)

√

![image 206](<2023-menart-differentially-private-non-convex-optimization_images/imageFile206.png>)

d

- 2: β′ = Tβ

![image 207](<2023-menart-differentially-private-non-convex-optimization_images/imageFile207.png>)

- 3: for t = 1 ...T do
- 4: Ft(w;S) := F(w;S) + L˜1 w − wt−1 2
- 5: wt = A(Ft,wt−1, Tρ ,β′)

![image 208](<2023-menart-differentially-private-non-convex-optimization_images/imageFile208.png>)

- 6: end for
- 7: Return wT


![image 209](<2023-menart-differentially-private-non-convex-optimization_images/imageFile209.png>)

In this section, we assume the loss F(·;S) is L˜1-weakly convex and that the empirical loss satisﬁes the (γ,κ)-KL* condition for κ ≥ 2. We avoid making a smoothness assumption in this regime. When κ > 2 and the KL* condition holds in a region with small excess risk, the loss functions cannot be smooth (unless it is the constant function). To elaborate, one can show that the loss upper bound implied by smoothness and the loss lower bound implied by the KL* condition lead to a contradiction. Instead of smoothness, we consider the (strictly weaker) assumption of weak convexity. As convex functions are weakly convex with L˜1 = 0, this setting is a strict relaxation of the loss assumptions considered by [ALD21]. Despite this, we achieve essentially the same rate as theirs. Moreover, in Theorem 8 in Appendix C, we give a lower bound of nǫ 1 κ, which establishes that our rate is tight (at least) for d = 1. Its proof adapts the construction in [ALD21, Theorem 5] from a lower bound on excess population risk under pure, (ǫ,0)-DP to that on excess empirical risk under approximate, (ǫ,δ)-DP. The lower bound holds for convex functions satisfying the growth condition and thus satisfying the KL condition, via Lemma 6.

![image 210](<2023-menart-differentially-private-non-convex-optimization_images/imageFile210.png>)

Our algorithm in this case is simply a differentially private implementation of the approximate proximal point method. This method has been used in prior work for non-KL functions to approximate stationary points [DG19, DD19a, BGM21]. We have the following guarantee for this method.

√

![image 211](<2023-menart-differentially-private-non-convex-optimization_images/imageFile211.png>)

κ−2 κ

Td log (n2 log2 (1/β′)/dβ′)

- Theorem 2. Let γ > 0, κ ≥ 2, There exists B = O˜ L


0 γ2 and a subroutine A such that if f is Lipschitz then Algorithm 2 is ρ-zCDP. If F(·;S) also satisﬁes the (γ,κ)-KL* condition and L˜1-weak convexity over BB(w0), then with probability at least 1 − β the output of Algorithm

![image 212](<2023-menart-differentially-private-non-convex-optimization_images/imageFile212.png>)

L˜1(1 +

n√ρ ) + L0F

0

![image 213](<2023-menart-differentially-private-non-convex-optimization_images/imageFile213.png>)

![image 214](<2023-menart-differentially-private-non-convex-optimization_images/imageFile214.png>)

![image 215](<2023-menart-differentially-private-non-convex-optimization_images/imageFile215.png>)

- 2 has excess risk, F(wT;S) − F(w∗;S), at most


![image 216](<2023-menart-differentially-private-non-convex-optimization_images/imageFile216.png>)

![image 217](<2023-menart-differentially-private-non-convex-optimization_images/imageFile217.png>)

κ−2 κ

γL0 Tdlog(n2 log2 (1/β′)/dβ′) n√ρ

0 γ2L˜1) n√ρ

κ

κ

![image 218](<2023-menart-differentially-private-non-convex-optimization_images/imageFile218.png>)

γL0 d(1 + F

= O˜

O

.

![image 219](<2023-menart-differentially-private-non-convex-optimization_images/imageFile219.png>)

![image 220](<2023-menart-differentially-private-non-convex-optimization_images/imageFile220.png>)

![image 221](<2023-menart-differentially-private-non-convex-optimization_images/imageFile221.png>)

![image 222](<2023-menart-differentially-private-non-convex-optimization_images/imageFile222.png>)

κ−2 κ

√ρ

0 γ2L˜1) log(F0) + κ log n

γL0√d and β′ = β/T, as deﬁned in Algorithm 2. Note the term

![image 223](<2023-menart-differentially-private-non-convex-optimization_images/imageFile223.png>)

![image 224](<2023-menart-differentially-private-non-convex-optimization_images/imageFile224.png>)

where T = (1 + 32F

![image 225](<2023-menart-differentially-private-non-convex-optimization_images/imageFile225.png>)

![image 226](<2023-menart-differentially-private-non-convex-optimization_images/imageFile226.png>)

√

![image 227](<2023-menart-differentially-private-non-convex-optimization_images/imageFile227.png>)

Td log (n2 log2 (1/β′)/dβ′)

n√ρ in the radius bound will be o(1) in regime where the convergence guarantees are nontrivial. The privacy of Algorithm 2 is straightforward since the subroutine A is ρ-zCDP by the assumption. Algorithm 2 is then private by post processing and composition. To prove the convergence result, we will use the following fact about the strength of differentially private optimizers for strongly convex loss functions.

![image 228](<2023-menart-differentially-private-non-convex-optimization_images/imageFile228.png>)

![image 229](<2023-menart-differentially-private-non-convex-optimization_images/imageFile229.png>)

- Lemma 3. There exists an implementation of A which is ρ-zCDP and with probability at least 1 − β′ the

output of the algorithm has excess risk O L

2 0d log (n2 log2 (1/β′)/dβ′)

![image 230](<2023-menart-differentially-private-non-convex-optimization_images/imageFile230.png>)

L˜1n2ρ .

We provide the details for this result in Appendix E. Furthermore, as in Section 3, we only need the KL condition to hold over the trajectory of the algorithm. The following lemma allows us to utilize the KL property at every iterate generated by the algorithm.

- Lemma 4. Assume A is as described by Lemma 3 above. With probability at least 1 − β, w1,...,wT ∈

BB(w0) for some B = O˜ L

0

![image 231](<2023-menart-differentially-private-non-convex-optimization_images/imageFile231.png>)

L˜1 1 +

√

![image 232](<2023-menart-differentially-private-non-convex-optimization_images/imageFile232.png>)

Td log (n2 log2 (1/β′)/dβ′)

![image 233](<2023-menart-differentially-private-non-convex-optimization_images/imageFile233.png>)

n√ρ + L0F

![image 234](<2023-menart-differentially-private-non-convex-optimization_images/imageFile234.png>)

κ−2 κ

![image 235](<2023-menart-differentially-private-non-convex-optimization_images/imageFile235.png>)

0 γ2 .

The proof is deferred to Appendix C.1. The proof of Theorem 2 now follows similar steps to those used in Theorem 1, but is overall much simpler. One key difference is that, for each t ∈ [T], we need to use the KL condition to lower bound wt − wt−1 , rather than  ∇F(wt;S) . For this, note that the optimality conditions of Ft imply 2L˜1 wt∗ − wt−1 =  ∇F(wt∗;S) ≥ γ1(F(wt∗;S) − F(w∗;S))1/κ. The inequality comes from the KL condition. The full proof of Theorem 2 is in Appendix C.2.

![image 236](<2023-menart-differentially-private-non-convex-optimization_images/imageFile236.png>)

- 5 Adapting to KL condition


In this section, we present an alternative algorithm for ERM under the KL* condition. At the cost of weaker rates when κ < 2, our algorithm automatically adapts to κ and γ. This is in contrast to the Spider method presented previously which requires prior knowledge of κ and γ. Furthermore, we are able to obtain this result with a comparatively simple algorithm. That is, our algorithm is a simple modiﬁcation of the traditional noisy gradient descent algorithm seen frequently in the DP literature [BST14, WYX17, BFTGT19]. Throughout the following, we will use T + 1 to denote the highest value of t reached during the run of Algorithm 3.

![image 237](<2023-menart-differentially-private-non-convex-optimization_images/imageFile237.png>)

- Algorithm 3 Adaptive Noisy Gradient Descent


![image 238](<2023-menart-differentially-private-non-convex-optimization_images/imageFile238.png>)

Require: Dataset S, Privacy parameter ρ > 0, Probability β > 0, Initial point w0 ∈ Rd, Lipschitz parameter L0, Smoothness parameter L1

- 1: η = 2L1

![image 239](<2023-menart-differentially-private-non-convex-optimization_images/imageFile239.png>)

1

, t = 0, ρ0 = 0

- 2: while tj=0 ρt ≤ ρ2 do

![image 240](<2023-menart-differentially-private-non-convex-optimization_images/imageFile240.png>)

- 3: Nt = n 1 ni=1 ∇f(wt;xi) + ˆbt where ˆbt ∼ N(0,Idσˆ2) and σˆ = L

![image 241](<2023-menart-differentially-private-non-convex-optimization_images/imageFile241.png>)

√nρ01/4

![image 242](<2023-menart-differentially-private-non-convex-optimization_images/imageFile242.png>)

![image 243](<2023-menart-differentially-private-non-convex-optimization_images/imageFile243.png>)

- 4: ∇t = n1 ni=1 ∇f(wt;xi) + bt where bt ∼ N(0,Idσt2) and σt = max N

![image 244](<2023-menart-differentially-private-non-convex-optimization_images/imageFile244.png>)

t

![image 245](<2023-menart-differentially-private-non-convex-optimization_images/imageFile245.png>)

√

![image 246](<2023-menart-differentially-private-non-convex-optimization_images/imageFile246.png>)

dlog(n√ρ/β), 2L

![image 247](<2023-menart-differentially-private-non-convex-optimization_images/imageFile247.png>)

0

![image 248](<2023-menart-differentially-private-non-convex-optimization_images/imageFile248.png>)

n√ρ

![image 249](<2023-menart-differentially-private-non-convex-optimization_images/imageFile249.png>)

- 5: wt+1 = wt − η∇t
- 6: ρt = min L

2 0d log(n√ρ/β)

![image 250](<2023-menart-differentially-private-non-convex-optimization_images/imageFile250.png>)

![image 251](<2023-menart-differentially-private-non-convex-optimization_images/imageFile251.png>)

n2Nt2 , ρ2 +

![image 252](<2023-menart-differentially-private-non-convex-optimization_images/imageFile252.png>)

√ρ n

![image 253](<2023-menart-differentially-private-non-convex-optimization_images/imageFile253.png>)

![image 254](<2023-menart-differentially-private-non-convex-optimization_images/imageFile254.png>)

- 7: t = t + 1
- 8: end while


![image 255](<2023-menart-differentially-private-non-convex-optimization_images/imageFile255.png>)

- Theorem 3. Assume f is Lipschitz. Then running Algorithm 3 and releasing w0,...,wT is ρ-zCDP.

The proof is given in Appendix D.2, and relies on the fully adaptive composition theorem of [WRRW22]. Our aim is now to provide convergence guarantees when the loss satisﬁes the KL* condition over some region S ⊂ Rd. We here demonstrate an alternative way of deﬁning S which allows us to leverage the KL* condition (in contrast to assuming S is a ball). Deﬁne the threshold α = max F(w0;S),F(w∗;S) +

2(γκ/2 + L0) L

2 0 log(n√ρ/β)

![image 256](<2023-menart-differentially-private-non-convex-optimization_images/imageFile256.png>)

![image 257](<2023-menart-differentially-private-non-convex-optimization_images/imageFile257.png>)

n√ρ

![image 258](<2023-menart-differentially-private-non-convex-optimization_images/imageFile258.png>)

1/2

. Let I = {w : F(w;S) ≤ α} denote a lower level set of F(·;S). Note the second term in the max of α only handles the trivial case where w0 already has small excess risk. Observe that I may not be a path-connected set, thus we deﬁne S as the path-connected component of I that contains w0. That is, w′ ∈ S if there exists a continuous function w : [0,1] → I, such that w(0) = w0, w(1) = w′. Intuitively, S is the local “valley” of F(·;S) in which w0 resides. Furthermore, we can guarantee that the trajectory of Algorithm 3 stays in this valley for the duration of its run.

- Lemma 5. Assume F(·;S) is L1-smooth and L0-Lipschitz. If F(·;S) satisﬁes the (γ,κ)-KL* condition


over S w.r.t. wS∗ := arg min

w∈S

{F(w;S)}, then w.p. at least 1 − 2β, for all t ∈ [T], wt ∈ S.

The proof is deferred to Appendix D.4. Note we are assuming the KL* condition w.r.t. the minimizer over S (as opposed to the global minimizer) here. We also remark that an existing work, [GHN+23], argued the importance of public pretraining in the non-convex setting to ﬁnd some w0 in a convex subregion before training on private data. Alternatively, our result suggests meaningful convergence if the empirical loss over the localized region is instead KL. This may be more realistic in the overparameterized regime as existing work has shown such models tend to be non-convex (but KL) around the minimizer [LZB22]. Our convergence result for Algorithm 3 is as follows.

- Theorem 4. Let β,γ > 0, κ ∈ [1,2]. Let ρ ≥ 0 be s.t. L20 log(n√ρ/β)/(L1n) ≤


√ρ. Deﬁne pmax := (1 + 8γ2L1) log(F0) + 42−κκ log(n√ρ/[γL0]) . If F(·;S) is L1-smooth and L0-Lipschitz and satisﬁes the (γ,κ)-KL* condition over S (as described above) w.r.t. wS∗, then with probability at least 1−2β, Algorithm

![image 259](<2023-menart-differentially-private-non-convex-optimization_images/imageFile259.png>)

![image 260](<2023-menart-differentially-private-non-convex-optimization_images/imageFile260.png>)

![image 261](<2023-menart-differentially-private-non-convex-optimization_images/imageFile261.png>)

![image 262](<2023-menart-differentially-private-non-convex-optimization_images/imageFile262.png>)

- 3 ﬁnds wT such that F(wT;S) − F(wS∗;S) is at most


2κ 4−κ

max γ2, 1 L20 log(n√ρ/β) min{L1, 1}n√ρ

γL0 d log(n√ρ/β)pmax n√ρ

κ/2

κ 2−κ

![image 263](<2023-menart-differentially-private-non-convex-optimization_images/imageFile263.png>)

![image 264](<2023-menart-differentially-private-non-convex-optimization_images/imageFile264.png>)

![image 265](<2023-menart-differentially-private-non-convex-optimization_images/imageFile265.png>)

![image 266](<2023-menart-differentially-private-non-convex-optimization_images/imageFile266.png>)

pmax n√ρ

![image 267](<2023-menart-differentially-private-non-convex-optimization_images/imageFile267.png>)

+

+

.

O

![image 268](<2023-menart-differentially-private-non-convex-optimization_images/imageFile268.png>)

![image 269](<2023-menart-differentially-private-non-convex-optimization_images/imageFile269.png>)

![image 270](<2023-menart-differentially-private-non-convex-optimization_images/imageFile270.png>)

![image 271](<2023-menart-differentially-private-non-convex-optimization_images/imageFile271.png>)

![image 272](<2023-menart-differentially-private-non-convex-optimization_images/imageFile272.png>)

![image 273](<2023-menart-differentially-private-non-convex-optimization_images/imageFile273.png>)

Ignoring polylogarithmic terms and problem constants we can more simply write F(wT;S) − F(wS∗;S) = O˜

√

2κ 4−κ

κ/2 .

![image 274](<2023-menart-differentially-private-non-convex-optimization_images/imageFile274.png>)

+ n√ 1ρ

d n√ρ

![image 275](<2023-menart-differentially-private-non-convex-optimization_images/imageFile275.png>)

![image 276](<2023-menart-differentially-private-non-convex-optimization_images/imageFile276.png>)

![image 277](<2023-menart-differentially-private-non-convex-optimization_images/imageFile277.png>)

![image 278](<2023-menart-differentially-private-non-convex-optimization_images/imageFile278.png>)

![image 279](<2023-menart-differentially-private-non-convex-optimization_images/imageFile279.png>)

The simpliﬁcation in the theorem uses the fact that 2−κκ ≥ κ2 for all κ. We defer the proof of Theorem

![image 280](<2023-menart-differentially-private-non-convex-optimization_images/imageFile280.png>)

![image 281](<2023-menart-differentially-private-non-convex-optimization_images/imageFile281.png>)

- 4 to Appendix D.3. The overarching ideas of the proof are similar to those of Theorem 1. However, the adaptive nature of the algorithm makes the analysis much more delicate.


Observe that for κ = 2 (i.e. the PL condition) this obtains the rate O˜ n d2ρ + n√1ρ which essentially captures the optimal rate in this setting. The rate slows as κ decreases, and for κ = 1 we obtain a rate of O˜

![image 282](<2023-menart-differentially-private-non-convex-optimization_images/imageFile282.png>)

![image 283](<2023-menart-differentially-private-non-convex-optimization_images/imageFile283.png>)

![image 284](<2023-menart-differentially-private-non-convex-optimization_images/imageFile284.png>)

√d n√ρ

2/3 + √nρ1

![image 285](<2023-menart-differentially-private-non-convex-optimization_images/imageFile285.png>)

.

![image 286](<2023-menart-differentially-private-non-convex-optimization_images/imageFile286.png>)

![image 287](<2023-menart-differentially-private-non-convex-optimization_images/imageFile287.png>)

1/4

![image 288](<2023-menart-differentially-private-non-convex-optimization_images/imageFile288.png>)

![image 289](<2023-menart-differentially-private-non-convex-optimization_images/imageFile289.png>)

- 5.1 Convergence Guarantees without the KL Condition


One of the key properties of Algorithm 3 is that it leverages large gradients to better control the privacy budget. In fact, even in the absence of an explicit KL assumption, we can show that Algorithm 3 obtains strong convergence guarantees when large gradient norms are observed. We provide the following result on Adaptive Gradient Descent’s ability to approximate stationary points. Note that we cannot give excess risk guarantees in this case due to the fact ﬁnding approximate global minimizers of non-convex functions is intractable in this setting.

- Theorem 5. Assume f is L1-smooth and L0-Lipschitz. Let T + 1 denote the largest value attained by t during the run of Algorithm 3. Let t∗ be sampled from {0,...,T} with probability proportional to


√ρ

exp −n

![image 290](<2023-menart-differentially-private-non-convex-optimization_images/imageFile290.png>)

2L0  ∇F(wt;S) . This algorithm is 2ρ-zCDP and with probability at least 1 − 3β satisﬁes

![image 291](<2023-menart-differentially-private-non-convex-optimization_images/imageFile291.png>)

L0√F0L1d n√ρ

L0 log(n√ρ/β) √nρ1/4

1/2

![image 292](<2023-menart-differentially-private-non-convex-optimization_images/imageFile292.png>)

![image 293](<2023-menart-differentially-private-non-convex-optimization_images/imageFile293.png>)

![image 294](<2023-menart-differentially-private-non-convex-optimization_images/imageFile294.png>)

F0L1 T

![image 295](<2023-menart-differentially-private-non-convex-optimization_images/imageFile295.png>)

 ∇F(wt∗;S) = O min

,

+

![image 296](<2023-menart-differentially-private-non-convex-optimization_images/imageFile296.png>)

![image 297](<2023-menart-differentially-private-non-convex-optimization_images/imageFile297.png>)

![image 298](<2023-menart-differentially-private-non-convex-optimization_images/imageFile298.png>)

![image 299](<2023-menart-differentially-private-non-convex-optimization_images/imageFile299.png>)

![image 300](<2023-menart-differentially-private-non-convex-optimization_images/imageFile300.png>)

The proof is given in Appendix D.6. The best case scenario is when most gradients in the run of the algorithm are Ω(1). In this case, the algorithm attains T = Θ˜ min n√ρ, n

2ρ d iterations and the con-

![image 301](<2023-menart-differentially-private-non-convex-optimization_images/imageFile301.png>)

![image 302](<2023-menart-differentially-private-non-convex-optimization_images/imageFile302.png>)

√d nǫ

√d

![image 303](<2023-menart-differentially-private-non-convex-optimization_images/imageFile303.png>)

![image 304](<2023-menart-differentially-private-non-convex-optimization_images/imageFile304.png>)

vergence guarantee becomes O˜

n√ρ + √nρ1

. We note an existing work showed a lower bound Ω

![image 305](<2023-menart-differentially-private-non-convex-optimization_images/imageFile305.png>)

![image 306](<2023-menart-differentially-private-non-convex-optimization_images/imageFile306.png>)

![image 307](<2023-menart-differentially-private-non-convex-optimization_images/imageFile307.png>)

1/4

![image 308](<2023-menart-differentially-private-non-convex-optimization_images/imageFile308.png>)

![image 309](<2023-menart-differentially-private-non-convex-optimization_images/imageFile309.png>)

for approximating stationary points, although this is not directly comparable as the previously stated upper bound does not hold for all functions. In the worst case, the algorithm will achieve convergence guarantee O˜ d

√d n√ρ

2/3

1/4

![image 310](<2023-menart-differentially-private-non-convex-optimization_images/imageFile310.png>)

. By contrast, the best known rate for approximating stationary points is O˜

√nρ1/4 + √nρ1

![image 311](<2023-menart-differentially-private-non-convex-optimization_images/imageFile311.png>)

![image 312](<2023-menart-differentially-private-non-convex-optimization_images/imageFile312.png>)

![image 313](<2023-menart-differentially-private-non-convex-optimization_images/imageFile313.png>)

1/4

![image 314](<2023-menart-differentially-private-non-convex-optimization_images/imageFile314.png>)

![image 315](<2023-menart-differentially-private-non-convex-optimization_images/imageFile315.png>)

![image 316](<2023-menart-differentially-private-non-convex-optimization_images/imageFile316.png>)

[ABG+23], and the best known rate for methods which do not rely on variance reduced gradient estimates (as is more typical in practice) is O˜

√d n√ρ

√d n√ρ

1/2 rate obtained by noisy gradient descent as a worst case guarantee with minimal modiﬁcation to the algorithm itself, while also potentially achieving a much stronger rate.

1/2 [WYX17]. Our analysis recovers the O˜

![image 317](<2023-menart-differentially-private-non-convex-optimization_images/imageFile317.png>)

![image 318](<2023-menart-differentially-private-non-convex-optimization_images/imageFile318.png>)

![image 319](<2023-menart-differentially-private-non-convex-optimization_images/imageFile319.png>)

![image 320](<2023-menart-differentially-private-non-convex-optimization_images/imageFile320.png>)

![image 321](<2023-menart-differentially-private-non-convex-optimization_images/imageFile321.png>)

![image 322](<2023-menart-differentially-private-non-convex-optimization_images/imageFile322.png>)

The worst case guarantee comes from balancing the number of iterations that the algorithm performs (which increases when the gradient norms are large) with the minimum gradient norm over the trajectory. For simplicity, consider the scenario where every gradient in the trajectory has the same norm N > 0. Then clearly the minimum norm is also N, but in this case T = O˜ N

2n2ρ

d . Thus the convergence guarantee implies that N = O˜

![image 323](<2023-menart-differentially-private-non-convex-optimization_images/imageFile323.png>)

√

1/4

![image 324](<2023-menart-differentially-private-non-convex-optimization_images/imageFile324.png>)

Nn√ρ , which at worst means N = O˜ d

d

√nρ1/4 . More formal/general details are in the proof in Appendix D.6.

![image 325](<2023-menart-differentially-private-non-convex-optimization_images/imageFile325.png>)

![image 326](<2023-menart-differentially-private-non-convex-optimization_images/imageFile326.png>)

![image 327](<2023-menart-differentially-private-non-convex-optimization_images/imageFile327.png>)

![image 328](<2023-menart-differentially-private-non-convex-optimization_images/imageFile328.png>)

# Acknowledgements

RB’s and MM’s research is supported by NSF CAREER Award 2144532, NSF Award AF-1908281, and NSF Award 2112471. RA’s and EU’s research is supported, in part, by NSF BIGDATA award IIS-1838139 and NSF CAREER award IIS-1943251. CG’s research was partially supported by INRIA Associate Teams project, FONDECYT 1210362 grant, ANID Anillo ACT210005 grant, and National Center for Artiﬁcial Intelligence CENIA FB210017, Basal ANID.

# References

[ABG+23] Raman Arora, Raef Bassily, Toma´s Gonza´lez, Cristo´bal A Guzma´n, Michael Menart, and Enayat Ullah. Faster rates of convergence to stationary points in differentially private optimization. In Andreas Krause, Emma Brunskill, Kyunghyun Cho, Barbara Engelhardt, Sivan Sabato, and Jonathan Scarlett, editors, Proceedings of the 40th International Conference on Machine Learning, volume 202 of Proceedings of Machine Learning Research, pages 1060– 1092. PMLR, 23–29 Jul 2023.

[ACD+22] Yossi Arjevani, Yair Carmon, John C. Duchi, Dylan J. Foster, Nathan Srebro, and Blake Woodworth. Lower bounds for non-convex stochastic optimization. 199(1–2):165–214, jun 2022.

[AFKT21] Hilal Asi, Vitaly Feldman, Tomer Koren, and Kunal Talwar. Private stochastic convex optimization: Optimal rates in l1 geometry. In International Conference on Machine Learning, pages 393–403. PMLR, 2021.

[ALD21] Hilal Asi, Daniel Levy, and John C Duchi. Adapting to function difﬁculty and growth conditions in private optimization. In M. Ranzato, A. Beygelzimer, Y. Dauphin, P.S. Liang, and J. Wortman Vaughan, editors, Advances in Neural Information Processing Systems, volume 34, pages 19069–19081. Curran Associates, Inc., 2021.

[BBF+21] Gavin Brown, Mark Bun, Vitaly Feldman, Adam Smith, and Kunal Talwar. When is memorization of irrelevant training data necessary for high-accuracy learning? In Proceedings of the 53rd annual ACM SIGACT symposium on theory of computing, pages 123–132, 2021.

[BBM18] Raef Bassily, Mikhail Belkin, and Siyuan Ma. On exponential convergence of sgd in nonconvex over-parametrized learning. ArXiv, abs/1811.02564, 2018.

[BFTGT19] Raef Bassily, Vitaly Feldman, Kunal Talwar, and Abhradeep Guha Thakurta. Private stochastic convex optimization with optimal rates. Advances in Neural Information Processing Systems, 32, 2019.

- [BGM21] Raef Bassily, Cristo´bal Guzma´n, and Michael Menart. Differentially private stochastic optimization: New results in convex and non-convex settings. Advances in Neural Information Processing Systems, 34, 2021.
- [BGN21] Raef Bassily, Cristobal Guzman, and Anupama Nandi. Non-euclidean differentially private stochastic convex optimization. In Mikhail Belkin and Samory Kpotufe, editors, Proceedings of Thirty Fourth Conference on Learning Theory, volume 134 of Proceedings of Machine Learning Research, pages 474–499. PMLR, 15–19 Aug 2021.


[BNPS17] Je´roˆme Bolte, Trong Phong Nguyen, Juan Peypouquet, and Bruce W Suter. From error bounds to the complexity of ﬁrst-order descent methods for convex functions. Mathematical Programming, 165:471–507, 2017.

[BS16] Mark Bun and Thomas Steinke. Concentrated differential privacy: Simpliﬁcations, extensions, and lower bounds. In Martin Hirt and Adam Smith, editors, Theory of Cryptography, pages 635–658, Berlin, Heidelberg, 2016. Springer Berlin Heidelberg.

[BST14] Raef Bassily, Adam Smith, and Abhradeep Thakurta. Private empirical risk minimization: Efﬁcient algorithms and tight error bounds. In 2014 IEEE 55th Annual Symposium on Foundations of Computer Science, pages 464–473. IEEE, 2014.

[BUV14] Mark Bun, Jonathan Ullman, and Salil Vadhan. Fingerprinting codes and the price of approximate differential privacy. STOC ’14, page 1–10, New York, NY, USA, 2014. Association for Computing Machinery.

[CDHS17] Yair Carmon, John C. Duchi, Oliver Hinder, and Aaron Sidford. ”convex until proven guilty”: Dimension-free acceleration of gradient descent on non-convex functions. In Proceedings of the 34th International Conference on Machine Learning - Volume 70, ICML’17, page 654–663. JMLR.org, 2017.

[CH12] Kamalika Chaudhuri and Daniel Hsu. Convergence rates for differentially private statistical estimation. In Proceedings of the... InternationalConference on Machine Learning. International Conference on Machine Learning, volume 2012, page 1327. NIH Public Access, 2012.

[CLE+19] Nicholas Carlini, Chang Liu, Ulfar´ Erlingsson, Jernej Kos, and Dawn Song. The secret sharer: Evaluating and testing unintended memorization in neural networks. In 28th USENIX Security Symposium (USENIX Security 19), pages 267–284, 2019.

[CMS11] Kamalika Chaudhuri, Claire Monteleoni, and Anand D Sarwate. Differentially private empirical risk minimization. Journal of Machine Learning Research, 12(Mar):1069–1109, 2011.

[CP18] Zachary Charles and Dimitris Papailiopoulos. Stability and generalization of learning algorithms that converge to global optima. In Jennifer Dy and Andreas Krause, editors, Proceedings of the 35th International Conference on Machine Learning, volume 80 of Proceedings of Machine Learning Research, pages 745–754. PMLR, 10–15 Jul 2018.

- [DD19a] Damek Davis and Dmitriy Drusvyatskiy. Stochastic model-based minimization of weakly convex functions. SIAM J. Optim., 29(1):207–239, 2019.
- [DD19b] Damek Davis and Dmitriy Drusvyatskiy. Stochastic model-based minimization of weakly convex functions. SIAM Journal on Optimization, 29(1):207–239, 2019.


[DG19] Damek Davis and Benjamin Grimmer. Proximally guided stochastic subgradient method for nonsmooth, nonconvex problems. SIAM Journal on Optimization, 29(3):1908–1930, 2019.

[DMNS06] Cynthia Dwork, Frank McSherry, Kobbi Nissim, and Adam Smith. Calibrating noise to sensitivity in private data analysis. In Theory of cryptography conference, pages 265–284. Springer, 2006.

[FKT20] Vitaly Feldman, Tomer Koren, and Kunal Talwar. Private stochastic convex optimization: Optimal rates in linear time. In Proceedings of the 52nd Annual ACM SIGACT Symposium on Theory of Computing, STOC 2020, page 439–449, New York, NY, USA, 2020. Association for Computing Machinery.

[FLLZ18] Cong Fang, Chris Junchi Li, ZhouchenLin, and Tong Zhang. Spider: Near-optimal non-convex optimization via stochastic path-integrated differential estimator. In S. Bengio, H. Wallach, H. Larochelle, K. Grauman, N. Cesa-Bianchi, and R. Garnett, editors, Advances in Neural Information Processing Systems, volume 31. Curran Associates, Inc., 2018.

[FSS18] Dylan J Foster, Ayush Sekhari, and Karthik Sridharan. Uniform convergence of gradients for non-convex learning and optimization. In S. Bengio, H. Wallach, H. Larochelle, K. Grauman, N. Cesa-Bianchi, and R. Garnett, editors, Advances in Neural Information Processing Systems, volume 31. Curran Associates, Inc., 2018.

[FSS+19] Dylan J Foster, Ayush Sekhari, Ohad Shamir, Nathan Srebro, Karthik Sridharan, and Blake Woodworth. The complexity of making the gradient small in stochastic convex optimization. In Conference on Learning Theory, pages 1319–1345. PMLR, 2019.

[FZ20] Vitaly Feldman and Chiyuan Zhang. What neural networks memorize and why: Discovering the long tail via inﬂuence estimation. Advances in Neural Information Processing Systems, 33:2881–2891, 2020.

[GHN+23] Arun Ganesh, Mahdi Haghifam, Milad Nasr, Sewoong Oh, Thomas Steinke, Om Thakkar, Abhradeep Thakurta, and Lun Wang. Why is public pretraining necessary for private model training? In International Conference on Machine Learning, 2023.

[GL13] Saeed Ghadimi and Guanghui Lan. Stochastic ﬁrst-and zeroth-order methods for nonconvex

stochastic programming. SIAM Journal on Optimization, 23(4):2341–2368, 2013. [GLOT23] Arun Ganesh, Daogao Liu, Sewoong Oh, and Abhradeep Thakurta. Private (stochastic) non-

convex optimization revisited: Second-order stationary points and excess risks, 2023.

[GTU23] Arun Ganesh, Abhradeep Thakurta, and Jalaj Upadhyay. Universality of langevin diffusion for private optimization, with applications to sampling from rashomon sets. In The Thirty Sixth Annual Conference on Learning Theory, pages 1730–1773. PMLR, 2023.

[HLR19] Nicholas JA Harvey, Christopher Liaw, and Sikander Randhawa. Simple and optimal high-probability bounds for strongly-convex stochastic gradient descent. arXiv preprint arXiv:1909.00843, 2019.

[HSS20] Oliver Hinder, Aaron Sidford, and Nimit Sohoni. Near-optimal methods for minimizing starconvexfunctionsand beyond. In Jacob Abernethyand Shivani Agarwal, editors, Proceedingsof Thirty Third Conference on Learning Theory, volume 125 of Proceedings of Machine Learning Research, pages 1894–1938. PMLR, 09–12 Jul 2020.

[JKT12] Prateek Jain, Pravesh Kothari, and Abhradeep Thakurta. Differentially private online learning. In 25th Annual Conference on Learning Theory (COLT), pages 24.1–24.34, 2012.

[JNG+19] Chi Jin, Praneeth Netrapalli, Rong Ge, Sham M Kakade, and Michael I Jordan. A short note on concentration inequalities for random vectors with subgaussian norm. arXiv preprint arXiv:1902.03736, 2019.

[KNS16] Hamed Karimi, Julie Nutini, and Mark Schmidt. Linear convergence of gradient and proximalgradient methods under the polyak-łojasiewicz condition. In Paolo Frasconi, Niels Landwehr, Giuseppe Manco, and Jilles Vreeken, editors, Machine Learning and Knowledge Discovery in Databases, pages 795–811, Cham, 2016. Springer International Publishing.

[KST12] Daniel Kifer, Adam Smith, and Abhradeep Thakurta. Private convex empirical risk minimization and high-dimensional regression. In Conference on Learning Theory, pages 25–1, 2012.

[Kur98] Krzysztof Kurdyka. On gradients of functions deﬁnable in o-minimal structures. Annales de l’Institut Fourier, 48:769–783, 1998.

[Lez62] T. Lezanski. Uber¨ das minimumproblem von funktionalen in banachschen r¨aumen. Bull. Acad. Pol. Sci., 1962.

[LGR23] Andrew Lowy, Ali Ghafelebashi, and Meisam Razaviyayn. Private non-convexfederated learning without a trusted server. In Francisco Ruiz, Jennifer Dy, and Jan-Willem van de Meent, editors, Proceedings of The 26th International Conference on Artiﬁcial Intelligence and Statistics, volume 206 of Proceedings of Machine Learning Research, pages 5749–5786. PMLR, 25–27 Apr 2023.

[LZB22] Chaoyue Liu, Libin Zhu, and Mikhail Belkin. Loss landscapes and optimization in overparameterized non-linear systems and neural networks. Applied and Computational Harmonic Analysis, 59:85–116, 2022. Special Issue on Harmonic Analysis and Machine Learning.

[MS23] Tomoya Murata and Taiji Suzuki. DIFF2: differential private optimization via gradient differences for nonconvex distributed learning. In Andreas Krause, Emma Brunskill, Kyunghyun Cho, Barbara Engelhardt, Sivan Sabato, and Jonathan Scarlett, editors, International Conference on Machine Learning, ICML 2023, 23-29 July 2023, Honolulu, Hawaii, USA, volume 202 of Proceedings of Machine Learning Research, pages 25523–25548. PMLR, 2023.

[Pol63] Boris Polyak. Gradient methods for the minimisation of functionals. Ussr Computational Mathematics and Mathematical Physics, 3:864–878, 12 1963.

[SMS22] Kevin Scaman, Cedric Malherbe, and Ludovic Dos Santos. Convergence rates of non-convex stochastic gradient descent under a generic lojasiewicz condition and local smoothness. In Kamalika Chaudhuri, Stefanie Jegelka, Le Song, Csaba Szepesvari, Gang Niu, and Sivan Sabato, editors, Proceedings of the 39th International Conference on Machine Learning, volume 162 of Proceedings of Machine Learning Research, pages 19310–19327. PMLR, 17–23 Jul 2022.

[Swe21] Latanya Sweeney. Weaving technology and policy together to maintain conﬁdentiality. Journal of Law, Medicine and Ethics, 25(2-3):98–110, 2021.

- [TTZ14] Kunal Talwar, Abhradeep Thakurta, and Li Zhang. Private empirical risk minimization beyond the worst case: The effect of the constraint set geometry. arXiv preprint arXiv:1411.5417,


- 2014.


- [TTZ15] Kunal Talwar, Abhradeep Thakurta, and Li Zhang. Nearly optimal private lasso. In NIPS,


- 2015.


[WRRW22] Justine Whitehouse, Aaditya Ramdas, Ryan M. Rogers, and Zhiwei Steven Wu. Fully adaptive composition in differential privacy. In International Conference on Machine Learning, 2022.

[WYX17] Di Wang, Minwei Ye, and Jinhui Xu. Differentially private empirical risk minimization revisited: Faster and more general. Advances in Neural Information Processing Systems, 30, 2017.

[YHL+22] Zhenhuan Yang, Shu Hu, Yunwen Lei, Kush R Vashney, Siwei Lyu, and Yiming Ying. Differentially private sgda for minimax problems. In James Cussens and Kun Zhang, editors, Proceedings of the Thirty-Eighth Conference on Uncertainty in Artiﬁcial Intelligence, volume 180 of Proceedings of Machine Learning Research, pages 2192–2202. PMLR, 01–05 Aug 2022.

[ZY13] Hui Zhang and Wotao Yin. Gradient methods for convex minimization: better rates under weaker conditions. ArXiv, abs/1303.4645, 2013.

# A Relationship between Growth Condition and KL Condition

Deﬁnition 4 ((λ,τ)-growth). A function F : Rd → R satisﬁes (λ,τ)-growth if the set of minimizers W∗ := arg minw F(w) is non-empty, and

F(w) − F(wp) ≥ λτ w − wp τ where wp be the projection of w onto W∗.

- Lemma 6 (Theorem 5.2 (ii) in [BNPS17]). Let κ ≥ 1 and γ > 0. If F : Rd → R is convex and satisﬁes γ−1, κ−κ1 growth condition, then it satisﬁes (γ,κ)-KL condition.

![image 329](<2023-menart-differentially-private-non-convex-optimization_images/imageFile329.png>)

It is proven in [KNS16, Appendix A] that the KL condition with κ = 2 (i.e., the PL condition) implies quadratic growth. We present the following generalized version of this argument.

- Lemma 7. Assume F : Rd → R satisﬁes the (γ,κ)-KL condition for κ ≥ 1 and γ > 0. Let w ∈ Rd and let wp be the projection of w onto the set of optimal solutions, W∗ := arg minw F(w). Then it holds that


κ κ−1

κ κ−1

![image 330](<2023-menart-differentially-private-non-convex-optimization_images/imageFile330.png>)

F(w) − F(wp) ≥ γ 1 · κ−κ1

w − wp

![image 331](<2023-menart-differentially-private-non-convex-optimization_images/imageFile331.png>)

. Proof. Deﬁne F∗ = min

![image 332](<2023-menart-differentially-private-non-convex-optimization_images/imageFile332.png>)

![image 333](<2023-menart-differentially-private-non-convex-optimization_images/imageFile333.png>)

1

{F(w)} and g(w) = 1−11/κ[F(w) − F∗]1−

κ . We have

![image 334](<2023-menart-differentially-private-non-convex-optimization_images/imageFile334.png>)

![image 335](<2023-menart-differentially-private-non-convex-optimization_images/imageFile335.png>)

w∈Rd

2

 ∇g(w) 2 = ∇F(w) [F(w) − F∗]1/κ

(2)

![image 336](<2023-menart-differentially-private-non-convex-optimization_images/imageFile336.png>)

=  ∇F(w) 2 [F(w) − F∗]2/κ

(3)

![image 337](<2023-menart-differentially-private-non-convex-optimization_images/imageFile337.png>)

2/κ

=  ∇F(w) κ [F(w) − F∗]

1 γ2

≥

(4)

![image 338](<2023-menart-differentially-private-non-convex-optimization_images/imageFile338.png>)

![image 339](<2023-menart-differentially-private-non-convex-optimization_images/imageFile339.png>)

Consider the gradient ﬂow starting at a point w0 given by

dw(t) dt

= −∇g(w(t)), w(t)|t=0 = w0

![image 340](<2023-menart-differentially-private-non-convex-optimization_images/imageFile340.png>)

Note F is invex (i.e. its stationary points are global minimizers) because it is KL. Thus g is an invex function because it is the composition of monotonically increasing function and invex function. Further, because g is bounded from below (by 0), the path described above eventually reaches the minimum thus there exists T < +∞ such that F(w(T)) = F(w∗).

Note the length of the path is at least w0 − wp . We then have

T

dw(t) dt

g(w0) − g(wT) = −

 ∇g(w(t)),

dt

![image 341](<2023-menart-differentially-private-non-convex-optimization_images/imageFile341.png>)

0

T

 ∇g(w(t)) 2dt

=

0

- (i)

≥

1 γ

![image 342](<2023-menart-differentially-private-non-convex-optimization_images/imageFile342.png>)

T

0

 ∇g(w(t))

- (ii)


1 γ

≥

w0 − wp ,

![image 343](<2023-menart-differentially-private-non-convex-optimization_images/imageFile343.png>)

where (i) uses Eqn. (2) and (ii) uses the lower bound on the path length. Plugging in the deﬁnition of g then gives

F(w) − F(wp) ≥

1 − 1/κ γ

![image 344](<2023-menart-differentially-private-non-convex-optimization_images/imageFile344.png>)

w − wp

1 1−1/κ

![image 345](<2023-menart-differentially-private-non-convex-optimization_images/imageFile345.png>)

.

Note the bound is non-negative if κ ≥ 1. Finally, observing that 1−11/κ = κ−κ1 establishes the claim. Remark 1. Using the above result one can observe that if the KL condition holds over a ball of radius

![image 346](<2023-menart-differentially-private-non-convex-optimization_images/imageFile346.png>)

![image 347](<2023-menart-differentially-private-non-convex-optimization_images/imageFile347.png>)

![image 348](<2023-menart-differentially-private-non-convex-optimization_images/imageFile348.png>)

![image 349](<2023-menart-differentially-private-non-convex-optimization_images/imageFile349.png>)

![image 350](<2023-menart-differentially-private-non-convex-optimization_images/imageFile350.png>)

![image 351](<2023-menart-differentially-private-non-convex-optimization_images/imageFile351.png>)

κ−1 κ

- B ≥ κ−κ1γF


0 , then w∗ ∈ BB(w0). Then for some w′ ∈ Rd, a triangle inequality can then be used to obtain w′ − w∗ ≤ w0 − w′ + w0 − w∗ . This would allow one to phrase our results in terms of a ball centered at w∗.

![image 352](<2023-menart-differentially-private-non-convex-optimization_images/imageFile352.png>)

![image 353](<2023-menart-differentially-private-non-convex-optimization_images/imageFile353.png>)

# B Missing Proofs from Section 3

- B.1 Privacy of Algorithm 1

Lemma 8. Assume f is L0-Lipschitz and L1-smooth over BB(w∗) (where B is as given in Theorem 1). Then Algorithm 1 is 2ρ-zCDP.

Proof. First, by Lemma 1, every wk,t, k ∈ [K],t ∈ [Tk], is in BB(w∗), and thus the loss is Lipschitz and smooth at the iterates generated by the algorithm. The sensitivity of the minibatch gradient estimates (made in the outer loop) is then L

0

![image 354](<2023-menart-differentially-private-non-convex-optimization_images/imageFile354.png>)

n , and at most K such estimates are made. Smoothness guarantees the sensitivity of the gradient difference estimates (made in the inner loop) at some k ∈ [T], t ∈ [Tk] is ηk,tL1

![image 355](<2023-menart-differentially-private-non-convex-optimization_images/imageFile355.png>)

- n  ∇k,t ≤ n1Φˆ1k/κ since ηk,t = 4γL 1


![image 356](<2023-menart-differentially-private-non-convex-optimization_images/imageFile356.png>)

![image 357](<2023-menart-differentially-private-non-convex-optimization_images/imageFile357.png>)

1 ∇k,t

Φ ˆ1k/κ. Note at most Tk such estimates are made.

The zCDP guarantees of the Gaussian mechanism ensures that the process of generating each ∇k,0 is ρˆ-CDP with ρˆ = K1 . Similarly, we have that the process of generating each ∆k,t, t > 0, is ρk-zCDP with ρk = KTρ

![image 358](<2023-menart-differentially-private-non-convex-optimization_images/imageFile358.png>)

![image 359](<2023-menart-differentially-private-non-convex-optimization_images/imageFile359.png>)

k

. By the composition theorem for zCDP we then have the overall privacy, is at most

K k=1

ρ K + T

![image 360](<2023-menart-differentially-private-non-convex-optimization_images/imageFile360.png>)

k

t=1

ρ

![image 361](<2023-menart-differentially-private-non-convex-optimization_images/imageFile361.png>)

KTk = 2ρ.

![image 362](<2023-menart-differentially-private-non-convex-optimization_images/imageFile362.png>)

![image 363](<2023-menart-differentially-private-non-convex-optimization_images/imageFile363.png>)

![image 364](<2023-menart-differentially-private-non-convex-optimization_images/imageFile364.png>)

![image 365](<2023-menart-differentially-private-non-convex-optimization_images/imageFile365.png>)

- B.2 Descent Equation for Algorithm 1


- Lemma 9. With probability at least 1−β, for every k ∈ [K] and t ∈ [Tk] indexing iterates of the algorithm


 ∇k,t Φ ˆ1k/κ − 4L1

it holds that F(wk,t;S) − F(wk,t+1;S) ≥ 16γL1

 ∇k,t − ∇F(wk,t;S) 2

![image 366](<2023-menart-differentially-private-non-convex-optimization_images/imageFile366.png>)

![image 367](<2023-menart-differentially-private-non-convex-optimization_images/imageFile367.png>)

1

1

Proof. We start with a standard descent analysis. Since F(·;S) is L1-smooth, we have

L1 2

wk,t+1 − wk,t 2

F(wk,t;S) − F(wk,t+1;S) ≥  ∇F(wk,t;S),wk,t − wk,t+1 −

![image 368](<2023-menart-differentially-private-non-convex-optimization_images/imageFile368.png>)

L1ηk,t2 2  ∇k,t 2

= ηk,t ∇F(wk,t;S),∇k,t −

![image 369](<2023-menart-differentially-private-non-convex-optimization_images/imageFile369.png>)

ηk,tL1 2  ∇k,t 2 + ηk,t ∇F(wt;S) − ∇k,t,∇k,t

= ηk,t 1 −

![image 370](<2023-menart-differentially-private-non-convex-optimization_images/imageFile370.png>)

- (i) ≥ ηk,t

- 1

![image 371](<2023-menart-differentially-private-non-convex-optimization_images/imageFile371.png>)

- 2 −


ηk,tL1 2  ∇k,t 2 −

![image 372](<2023-menart-differentially-private-non-convex-optimization_images/imageFile372.png>)

ηk,t 2  ∇k,t − ∇F(wk,t;S) 2.

![image 373](<2023-menart-differentially-private-non-convex-optimization_images/imageFile373.png>)

- (ii)

≥

ηk,t 4  ∇k,t 2 −

![image 374](<2023-menart-differentially-private-non-convex-optimization_images/imageFile374.png>)

1 4L1 ∇k,t − ∇F(wk,t;S) 2

![image 375](<2023-menart-differentially-private-non-convex-optimization_images/imageFile375.png>)

- (iii=)


1 4L1 ∇k,t − ∇F(wk,t;S) 2

1 16γL1 ∇k,t Φ ˆ1k/κ −

![image 376](<2023-menart-differentially-private-non-convex-optimization_images/imageFile376.png>)

![image 377](<2023-menart-differentially-private-non-convex-optimization_images/imageFile377.png>)

Step (i) uses Young’s inequality. Step (ii) uses the fact that ηk,t ≤ 2L1

. This is because ηk,t = 1

![image 378](<2023-menart-differentially-private-non-convex-optimization_images/imageFile378.png>)

1

Φ ˆ1k/κ and updates are only performed when  ∇k,t ≥ 87γΦˆ1k/κ. Step (iii) uses the setting of ηt.

![image 379](<2023-menart-differentially-private-non-convex-optimization_images/imageFile379.png>)

![image 380](<2023-menart-differentially-private-non-convex-optimization_images/imageFile380.png>)

4γL1 ∇k,t

![image 381](<2023-menart-differentially-private-non-convex-optimization_images/imageFile381.png>)

![image 382](<2023-menart-differentially-private-non-convex-optimization_images/imageFile382.png>)

![image 383](<2023-menart-differentially-private-non-convex-optimization_images/imageFile383.png>)

![image 384](<2023-menart-differentially-private-non-convex-optimization_images/imageFile384.png>)

- B.3 Proof of Lemma 1 Due to the step size and the phases lengths, with probability 1, we have that,

wk,t − w0 ≤

K

k=1

1 4γL1

![image 385](<2023-menart-differentially-private-non-convex-optimization_images/imageFile385.png>)

Φˆ1k/κTk ≤

K

k=1

1 4F

![image 386](<2023-menart-differentially-private-non-convex-optimization_images/imageFile386.png>)

κ−2 κ

![image 387](<2023-menart-differentially-private-non-convex-optimization_images/imageFile387.png>)

0 γL1

Φˆ1k/κΦˆ

κ−2 κ

![image 388](<2023-menart-differentially-private-non-convex-optimization_images/imageFile388.png>)

k =

F

2−κ κ

![image 389](<2023-menart-differentially-private-non-convex-optimization_images/imageFile389.png>)

0 F

κ−1 κ

![image 390](<2023-menart-differentially-private-non-convex-optimization_images/imageFile390.png>)

0 4γL1

![image 391](<2023-menart-differentially-private-non-convex-optimization_images/imageFile391.png>)

K

k=1

1 c

![image 392](<2023-menart-differentially-private-non-convex-optimization_images/imageFile392.png>)

κ−1 κ

![image 393](<2023-menart-differentially-private-non-convex-optimization_images/imageFile393.png>)

k

Above, we use the fact that κ−κ1 ≥ 0 (since κ ≥ 1) to bound Φˆk ≤ F0. Since c > 1 we have, recalling K = (1 + 64F

![image 394](<2023-menart-differentially-private-non-convex-optimization_images/imageFile394.png>)

κ−2 κ

![image 395](<2023-menart-differentially-private-non-convex-optimization_images/imageFile395.png>)

0 γ2L1) log(F0) − κ log L

0

√

![image 396](<2023-menart-differentially-private-non-convex-optimization_images/imageFile396.png>)

d n√ρ ,

![image 397](<2023-menart-differentially-private-non-convex-optimization_images/imageFile397.png>)

![image 398](<2023-menart-differentially-private-non-convex-optimization_images/imageFile398.png>)

wk,t − w0 ≤

KF01/κ 4γL1

![image 399](<2023-menart-differentially-private-non-convex-optimization_images/imageFile399.png>)

=

F01/κ 4γL1

![image 400](<2023-menart-differentially-private-non-convex-optimization_images/imageFile400.png>)

+ 16F

κ−1 κ

![image 401](<2023-menart-differentially-private-non-convex-optimization_images/imageFile401.png>)

0 γ log(F0) + κ log

n√ρ L0

![image 402](<2023-menart-differentially-private-non-convex-optimization_images/imageFile402.png>)

![image 403](<2023-menart-differentially-private-non-convex-optimization_images/imageFile403.png>)

√

![image 404](<2023-menart-differentially-private-non-convex-optimization_images/imageFile404.png>)

d

.

- B.4 Lower Bound for Smooth Losses Satisfying Growth Condition


We provide the following extension of the lower bound on excess risk in [ALD21]. Our extension yields a lower bound for losses which satisfy (λ,τ)-growth and are L1 ≥ 0-smooth over a ball BR(w0), for any smoothness parameter L1 ≥ 0 and radius R > 0. In contrast, the setting of [ALD21] did not have the above smoothness and existence of a (large) ball BR(w0) assumption (over which smoothness and Lipschitzness holds). Further, [ALD21] provide a lower bound for constrained DP procedures, which is is based on a reduction from convex ERM over a constrained set of any diameter D [BST14]. In contrast, we are interested in lower bound for unconstrained procedures. Therefore, in Theorem 7, we extend the lower bound of [BST14] to the unconstrained setting. We then provide a reduction, closely following [ALD21],

from unconstrained convex ERM to unconstrained optimization of functions satisfying a growth condition. Finally, we note that our unconstrained lower bound in Theorem 7 holds pointwise for all values of the norm of optimal solution D, so it sufﬁces to construct a reduction for some choice of D. We show that for any given setting of problem parameters, there is a choice of D, for which the reduced instance satisﬁes the requisite properties.

- Theorem 6. Let L0,L1,B,λ ≥ 0,τ ≥ 2,τ = O(1),0 < ǫ ≤ 1,2−Ω(n) ≤ δ < n1. For any (ǫ,δ)-DP algorithm A, there exists a set W ⊂ Rd containing a ball of radius B, a dataset S and a convex loss


![image 405](<2023-menart-differentially-private-non-convex-optimization_images/imageFile405.png>)

function f such that for all x, the function w  → f(w;x) is L0-Lipschitz, L1-smooth over W, the empirical loss w  → F(w;S) satisﬁes (λ,τ)-growth, and

√

τ τ−1

F(w)] = Ω

  .

![image 406](<2023-menart-differentially-private-non-convex-optimization_images/imageFile406.png>)

![image 407](<2023-menart-differentially-private-non-convex-optimization_images/imageFile407.png>)

 1 τ

d λnǫ

L0

EA[F(A(S);S) − inf

![image 408](<2023-menart-differentially-private-non-convex-optimization_images/imageFile408.png>)

![image 409](<2023-menart-differentially-private-non-convex-optimization_images/imageFile409.png>)

1 τ−1

w∈Rd

![image 410](<2023-menart-differentially-private-non-convex-optimization_images/imageFile410.png>)

Proof. The key to the proof is the following reduction, based on Proposition 3 of [ALD21]. Herein, the aim is to show that the existence of a DP optimizer for convex losses satisfying the growth condition implies the existence of an optimizer for general convex losses. More formally, consider a problem instance class where we are given a set W ⊂ Rd containing a ball of radius B, a dataset S ∈ Xn for some X, a function f(w;x) where w  → f(w;x) is L0-Lipschitz, L1-smooth over W for all x ∈ X and the empirical loss w  → F(w;S) satisﬁes (λ,τ)-growth. Note since these properties hold over W, they hold over the ball of radius B. If there exists an (ǫ,δ)-DP algorithm A, which for the above problem instance has expected excess empirical risk,

1 τ−1

F(w)] = o (τλτ)−

EA[F(A(S);S) − inf

∆(n,d,L0,L1,ǫ,δ) ,

![image 411](<2023-menart-differentially-private-non-convex-optimization_images/imageFile411.png>)

w

τ−2 τ−1

√

![image 412](<2023-menart-differentially-private-non-convex-optimization_images/imageFile412.png>)

1/τL1L

- 0,L1,ǫ,δ))1/τB

![image 413](<2023-menart-differentially-private-non-convex-optimization_images/imageFile413.png>)

L

- 1


then for D = max (∆(n,d,L0,L1,ǫ,δ))

![image 414](<2023-menart-differentially-private-non-convex-optimization_images/imageFile414.png>)

0 c2(τ) , (∆(n,d,L (τ−1) 0 c3(τ)

dL0

,

L1nǫ , where c2(τ) = Ω(1) and

![image 415](<2023-menart-differentially-private-non-convex-optimization_images/imageFile415.png>)

![image 416](<2023-menart-differentially-private-non-convex-optimization_images/imageFile416.png>)

![image 417](<2023-menart-differentially-private-non-convex-optimization_images/imageFile417.png>)

c3(τ) = Ω(1) are speciﬁed later, there exists an (ǫ,δ)-DP algorithm A˜, such that for any L0-Lipschitz, convex, L1-smooth loss function w  → f˜(w;x) for all x, with minimizer norm w∗ = D, its excess risk is

τ−1 τ

EA˜[F˜(A˜(S);S) − inf

F˜(w)] = o D (∆(n,d,2L0,2L1,ǫ/k,δ/k))

![image 418](<2023-menart-differentially-private-non-convex-optimization_images/imageFile418.png>)

w∈Rd

τ τ−1 0

1

![image 419](<2023-menart-differentially-private-non-convex-optimization_images/imageFile419.png>)

![image 420](<2023-menart-differentially-private-non-convex-optimization_images/imageFile420.png>)

τ−1 L

where k is the smallest integer larger that log τ

22τ−3∆(n,d,2L0,2L1,ǫ/k,δ/k) .

![image 421](<2023-menart-differentially-private-non-convex-optimization_images/imageFile421.png>)

The main difference between above and the statement of [ALD21] is that unlike [ALD21], our reduction is for unconstrained procedures and is tailored to the aforementioned choice of diameter D.

The proof uses the construction of [ALD21], verifying that for the provided parameter settings, the assumptions hold. For simplicity of notation, let ∆ = ∆(n,L0,L1,ǫ,δ).

Let w0 be the origin. For a sequence of {λi}i to be instantiated later, deﬁne

1 τ−1

L0 2τλτi 2τ−2

![image 422](<2023-menart-differentially-private-non-convex-optimization_images/imageFile422.png>)

W˜i = w : w − wi−1 ≤

![image 423](<2023-menart-differentially-private-non-convex-optimization_images/imageFile423.png>)

F ˜i(w;S) = F(w;S) + λτi 2τ−2 w − wi−1 τ

where wi = A(F˜i,S). The function F˜i satisﬁes (λi2(τ−2)/τ,τ)-growth (over all of Rd). We now inspect its Lipschitzness and smoothness parameters over W˜i. By direct calculation, the Lipschitz parameter is

bounded by L0 + L0 = 2L0 The smoothness parameter is at most,

L0 2τλτi 2τ−2

L1 + λτi 2τ−2τ(τ − 1) w − wi−1 τ−2 = L1 + λτi 2τ−2τ(τ − 1)

![image 424](<2023-menart-differentially-private-non-convex-optimization_images/imageFile424.png>)

τ τ−1

τ−2

= L1 + (λi)

(L0)

τ−1 c1(τ),

![image 425](<2023-menart-differentially-private-non-convex-optimization_images/imageFile425.png>)

![image 426](<2023-menart-differentially-private-non-convex-optimization_images/imageFile426.png>)

τ−2 τ−1

![image 427](<2023-menart-differentially-private-non-convex-optimization_images/imageFile427.png>)

τ−2 τ−1 τ

1

τ−1 τ

)iλ for λ to be speciﬁed later. The above smoothness bound is a decreasing function in i, so what sufﬁces is to show that the above bound is smaller than 2L1 for the largest λi, which is λ1 = 2−(

τ−1(τ − 1). In [ALD21], λi is set as λi = 2−(

1

![image 428](<2023-menart-differentially-private-non-convex-optimization_images/imageFile428.png>)

![image 429](<2023-menart-differentially-private-non-convex-optimization_images/imageFile429.png>)

- τ−1 (τ−1)

![image 430](<2023-menart-differentially-private-non-convex-optimization_images/imageFile430.png>)

2

- τ−2 τ−1


where c1(τ) = 2

= τ

![image 431](<2023-menart-differentially-private-non-convex-optimization_images/imageFile431.png>)

![image 432](<2023-menart-differentially-private-non-convex-optimization_images/imageFile432.png>)

![image 433](<2023-menart-differentially-private-non-convex-optimization_images/imageFile433.png>)

)λ. From [AFKT21], λ = 4

τ−1 τ

![image 434](<2023-menart-differentially-private-non-convex-optimization_images/imageFile434.png>)

(τ−1) τ2

(τ−1)2

![image 435](<2023-menart-differentially-private-non-convex-optimization_images/imageFile435.png>)

τ2 ∆τ Dτ(τ−1)

, so we have,

![image 436](<2023-menart-differentially-private-non-convex-optimization_images/imageFile436.png>)

![image 437](<2023-menart-differentially-private-non-convex-optimization_images/imageFile437.png>)

1/τ ∆1/τ D

∆1/τ D

τ τ − 1

τ τ−1

τ−2

τ−2

τ−2

τ−1 τ

(L0)

τ−1c(τ) = 4

τ−1c1(τ) = c2(τ)

τ−1,

(λi)

(L0)

(L0)

![image 438](<2023-menart-differentially-private-non-convex-optimization_images/imageFile438.png>)

![image 439](<2023-menart-differentially-private-non-convex-optimization_images/imageFile439.png>)

![image 440](<2023-menart-differentially-private-non-convex-optimization_images/imageFile440.png>)

![image 441](<2023-menart-differentially-private-non-convex-optimization_images/imageFile441.png>)

![image 442](<2023-menart-differentially-private-non-convex-optimization_images/imageFile442.png>)

![image 443](<2023-menart-differentially-private-non-convex-optimization_images/imageFile443.png>)

![image 444](<2023-menart-differentially-private-non-convex-optimization_images/imageFile444.png>)

![image 445](<2023-menart-differentially-private-non-convex-optimization_images/imageFile445.png>)

τ−2 τ−1

1/τ

1∆1/τ(L0)

1

![image 446](<2023-menart-differentially-private-non-convex-optimization_images/imageFile446.png>)

τ−1

τ−1 (τ − 1). The choice of D ≥ L

τ τ τ−1

where c2(τ) = 4

τ

c2(τ) , ensures the above is at most L1, thereby establishing that the smoothness parameter is at most 2L1. The ﬁnal condition we want to ensure is that all the sets W˜i contain a ball of radius at least B. Since λi is decreasing in i, it sufﬁces to consider i = 1. We have,

![image 447](<2023-menart-differentially-private-non-convex-optimization_images/imageFile447.png>)

![image 448](<2023-menart-differentially-private-non-convex-optimization_images/imageFile448.png>)

![image 449](<2023-menart-differentially-private-non-convex-optimization_images/imageFile449.png>)

![image 450](<2023-menart-differentially-private-non-convex-optimization_images/imageFile450.png>)

L0 2τλτ12τ−2

![image 451](<2023-menart-differentially-private-non-convex-optimization_images/imageFile451.png>)

1 τ−1

- 1

![image 452](<2023-menart-differentially-private-non-convex-optimization_images/imageFile452.png>)

- 2τ


![image 453](<2023-menart-differentially-private-non-convex-optimization_images/imageFile453.png>)

=

1 τ−1

![image 454](<2023-menart-differentially-private-non-convex-optimization_images/imageFile454.png>)

τ − 1 τ

![image 455](<2023-menart-differentially-private-non-convex-optimization_images/imageFile455.png>)

1 τ

1 4

![image 456](<2023-menart-differentially-private-non-convex-optimization_images/imageFile456.png>)

L

![image 457](<2023-menart-differentially-private-non-convex-optimization_images/imageFile457.png>)

0

τ−1 τ

![image 458](<2023-menart-differentially-private-non-convex-optimization_images/imageFile458.png>)

D ∆1/τ

D ∆1/τ

1 τ−1

1 τ−1

![image 459](<2023-menart-differentially-private-non-convex-optimization_images/imageFile459.png>)

![image 460](<2023-menart-differentially-private-non-convex-optimization_images/imageFile460.png>)

= c3(τ)L

![image 461](<2023-menart-differentially-private-non-convex-optimization_images/imageFile461.png>)

![image 462](<2023-menart-differentially-private-non-convex-optimization_images/imageFile462.png>)

0

1 τ 1

1/τ

where c3(τ) = 1

. The choice of D ≥ Bk∆

τ−1 τ

![image 463](<2023-menart-differentially-private-non-convex-optimization_images/imageFile463.png>)

ensures the above is at least B. The rest of the proof repeats the arguments in [ALD21], to get,

![image 464](<2023-menart-differentially-private-non-convex-optimization_images/imageFile464.png>)

![image 465](<2023-menart-differentially-private-non-convex-optimization_images/imageFile465.png>)

![image 466](<2023-menart-differentially-private-non-convex-optimization_images/imageFile466.png>)

![image 467](<2023-menart-differentially-private-non-convex-optimization_images/imageFile467.png>)

1 τ−1 0 c3(τ)

1 τ−1

τ−1 τ

![image 468](<2023-menart-differentially-private-non-convex-optimization_images/imageFile468.png>)

![image 469](<2023-menart-differentially-private-non-convex-optimization_images/imageFile469.png>)

4

2τ

![image 470](<2023-menart-differentially-private-non-convex-optimization_images/imageFile470.png>)

L

τ−1 τ

E[F˜(A′(S);S)] − min

F˜(w;S) = o D (∆(n,d,2L0,2L1,ǫ/k,δ/k))

![image 471](<2023-menart-differentially-private-non-convex-optimization_images/imageFile471.png>)

w

√

![image 472](<2023-menart-differentially-private-non-convex-optimization_images/imageFile472.png>)

nǫ . This gives us that E[F˜(A′(S);S)] − minw F˜(w;S) = 0D

d

We now instantiate ∆(n,d,L0,L1,ǫ,δ) = L

0

![image 473](<2023-menart-differentially-private-non-convex-optimization_images/imageFile473.png>)

√

![image 474](<2023-menart-differentially-private-non-convex-optimization_images/imageFile474.png>)

- o L


d

nǫ . However, this contradicts our lower bound in Theorem 7 for unconstrained DP procedures for convex, L0-Lispchitz,

![image 475](<2023-menart-differentially-private-non-convex-optimization_images/imageFile475.png>)

√dL0

![image 476](<2023-menart-differentially-private-non-convex-optimization_images/imageFile476.png>)

Dnǫ ≤ L1-smooth (by our choice of D) losses.

![image 477](<2023-menart-differentially-private-non-convex-optimization_images/imageFile477.png>)

![image 478](<2023-menart-differentially-private-non-convex-optimization_images/imageFile478.png>)

![image 479](<2023-menart-differentially-private-non-convex-optimization_images/imageFile479.png>)

![image 480](<2023-menart-differentially-private-non-convex-optimization_images/imageFile480.png>)

![image 481](<2023-menart-differentially-private-non-convex-optimization_images/imageFile481.png>)

- B.5 Additional Details for Corollary 1 (Lower Bound)


In Theorem 6 (in Appendix B.4), an extension of [ALD21, Theorem 6], we show that for τ ≥ 2 and τ = Θ(1), the lower bound on the minimax optimal expected excess empirical risk, α, for (ǫ,δ)-DP ERM of functions which are smooth and Lipschitz over a ball of any ﬁnite radius B > 0 and globally satisfy convexity and (λ,τ)-growth, is

α = Ω˜ 

 1 (τ)

![image 482](<2023-menart-differentially-private-non-convex-optimization_images/imageFile482.png>)

1 τ−1

![image 483](<2023-menart-differentially-private-non-convex-optimization_images/imageFile483.png>)

√

![image 484](<2023-menart-differentially-private-non-convex-optimization_images/imageFile484.png>)

d λnǫ

L0

![image 485](<2023-menart-differentially-private-non-convex-optimization_images/imageFile485.png>)

τ τ−1

 .

![image 486](<2023-menart-differentially-private-non-convex-optimization_images/imageFile486.png>)

Lemma 6 gives that (λ,τ)-growth and convexity implies (γ,κ)-KL with λ = γ−1 and τ = κ−κ1. Further, if κ ≤ 2, then τ = κ−κ1 ≥ 2 and if κ = 1 + Ω(1) then τ = O(1). Thus we have the lower bound,

![image 487](<2023-menart-differentially-private-non-convex-optimization_images/imageFile487.png>)

![image 488](<2023-menart-differentially-private-non-convex-optimization_images/imageFile488.png>)

√

√

κ

κ

1−κ γL0

![image 489](<2023-menart-differentially-private-non-convex-optimization_images/imageFile489.png>)

![image 490](<2023-menart-differentially-private-non-convex-optimization_images/imageFile490.png>)

γL0

κ κ − 1

d nǫ

d nǫ

= Ω˜

α = Ω˜

.

![image 491](<2023-menart-differentially-private-non-convex-optimization_images/imageFile491.png>)

![image 492](<2023-menart-differentially-private-non-convex-optimization_images/imageFile492.png>)

![image 493](<2023-menart-differentially-private-non-convex-optimization_images/imageFile493.png>)

The last step uses the fact that κ = 1 + Ω(1). Finally, the existence of a ρ-zCDP algorithm with rate better than O˜ γL

√

κ

![image 494](<2023-menart-differentially-private-non-convex-optimization_images/imageFile494.png>)

d n√ρ

would imply the existence of an (ǫ,δ)-DP algorithm (see [BS16, Proposition 1.3]) with rate better than O˜ γL

0

![image 495](<2023-menart-differentially-private-non-convex-optimization_images/imageFile495.png>)

![image 496](<2023-menart-differentially-private-non-convex-optimization_images/imageFile496.png>)

√

κ

![image 497](<2023-menart-differentially-private-non-convex-optimization_images/imageFile497.png>)

d nǫ

0

, a contradiction.

![image 498](<2023-menart-differentially-private-non-convex-optimization_images/imageFile498.png>)

- B.6 Unconstrained Lower Bound for General Loss Functions


In this section, we provide an extension of the lower bound on excess risk of DP procedures for convex Lipschitz functions in the constrained setting [BST14] to the unconstrained setting. The key idea in the proof is to deﬁne a Lipschitz extension of the hard instance in [BST14] using the Huber regularizer. The dataset for our construction, as in [BST14], leverages ﬁngerprinting codes. The exact details of ﬁngerprinting codes are note needed for our proof below, but we defer the interested reader to [BUV14] for more details. The following result is used in the proof of the lower bound for functions satisfying (λ,τ)-growth for 2 ≤ τ = O(1) in Theorem 6.

- Theorem 7. Let 0 < ǫ ≤ 1,0 < δ < n1, D,L0 > 0. For any (ǫ,δ)-DP algorithm, there exists a dataset S, and a L0-Lipschitz,


![image 499](<2023-menart-differentially-private-non-convex-optimization_images/imageFile499.png>)

√

![image 500](<2023-menart-differentially-private-non-convex-optimization_images/imageFile500.png>)

dL0

nǫD -smooth convex loss function w  → f(w;x) for all x, such that its unconstrained minimizer, w∗ = argmin

![image 501](<2023-menart-differentially-private-non-convex-optimization_images/imageFile501.png>)

{F(w;S)}, has norm at most D, and

w

√

![image 502](<2023-menart-differentially-private-non-convex-optimization_images/imageFile502.png>)

d nǫ

EA[F(A(S);S) − F(w∗;S)] = Ω L0D min

,1 .

![image 503](<2023-menart-differentially-private-non-convex-optimization_images/imageFile503.png>)

Proof. Consider the loss function

F(w;S) =

n

1 n

![image 504](<2023-menart-differentially-private-non-convex-optimization_images/imageFile504.png>)

i=1

where H is the “Huber regularization” deﬁned as

w,xi + λH(w), (5)

H(w) =

w 2 if w ≤ 4D 4D w otherwise

(6)

d

Note that if N of the xi vectors are vectors in ± L

√0 d

and the rest are the zero vector, we have

![image 505](<2023-menart-differentially-private-non-convex-optimization_images/imageFile505.png>)

![image 506](<2023-menart-differentially-private-non-convex-optimization_images/imageFile506.png>)

n i=1 xi 2nλ . Thus we set λ = NL

n i=1 xi ≤ NL0. The empirical minimizer is w∗ = −

2nD so that w∗ ≤ D. We also remark that under this setting of λ that F is Lipschitz with parameter L′0 = L0 + 4λD ≤ 5L0.

0

![image 507](<2023-menart-differentially-private-non-convex-optimization_images/imageFile507.png>)

![image 508](<2023-menart-differentially-private-non-convex-optimization_images/imageFile508.png>)

Now we will show that any w which achieves small excess risk is close to w∗. Then we will use a lower

bound on this distance to lower bound the error (as in [BST14]). For any w such that w ≤ 4D have

n

1 n

xi + λ w 2 − w∗ 2

F(w;S) − F(w∗;S) = w − w∗,

![image 509](<2023-menart-differentially-private-non-convex-optimization_images/imageFile509.png>)

i=1

= 2λ w − w∗,−w∗ + λ w 2 − w∗ 2

= 2λ( w∗ 2 − w,w∗ ) + λ w 2 − w∗ 2

- 1

![image 510](<2023-menart-differentially-private-non-convex-optimization_images/imageFile510.png>)

- 2


- 1

![image 511](<2023-menart-differentially-private-non-convex-optimization_images/imageFile511.png>)

- 2


- 1

![image 512](<2023-menart-differentially-private-non-convex-optimization_images/imageFile512.png>)

- 2


w − w∗ 2 + λ w 2 − w∗ 2

w 2 +

w∗ 2 −

= 2λ

= λ w − w∗ 2

NL0 nD

w − w∗ 2

=

![image 513](<2023-menart-differentially-private-non-convex-optimization_images/imageFile513.png>)

where the fourth equality comes from a,b = 21( a 2+ b 2− a − b 2). Now [BST14, Lemma 5.1] gives that for N = min

![image 514](<2023-menart-differentially-private-non-convex-optimization_images/imageFile514.png>)

√

![image 515](<2023-menart-differentially-private-non-convex-optimization_images/imageFile515.png>)

d

ǫ ,n there exists a construction of the non-zero dataset vectors such that the output of any (ǫ,δ)-DP algorithm, A(S), must satisfy E[ A(S) − w∗ ] = Ω

![image 516](<2023-menart-differentially-private-non-convex-optimization_images/imageFile516.png>)

√dD

![image 517](<2023-menart-differentially-private-non-convex-optimization_images/imageFile517.png>)

Nǫ . Thus we have

![image 518](<2023-menart-differentially-private-non-convex-optimization_images/imageFile518.png>)

√

![image 519](<2023-menart-differentially-private-non-convex-optimization_images/imageFile519.png>)

d nǫ

E[F(A(S);S) − F(w∗;S)] = Ω L0D min

,1 .

![image 520](<2023-menart-differentially-private-non-convex-optimization_images/imageFile520.png>)

This lower bounds the excess loss for any w such that w ≤ 4D. Finally, note that any w′ such that

w′ ≥ 4D (i.e. a point outside the quadratic region of H) would also have high empirical risk because of the regularization term. Speciﬁcally, we have for any such w′ that

w′ L0N n

4DL0N n Further since w∗ ≤ D, we have F(w∗;S) ≤ NL

+ 4λD w′ ≥ 16λD2 −

F(w′;S) ≥ −

![image 521](<2023-menart-differentially-private-non-convex-optimization_images/imageFile521.png>)

![image 522](<2023-menart-differentially-private-non-convex-optimization_images/imageFile522.png>)

n + λD2. This gives

0

![image 523](<2023-menart-differentially-private-non-convex-optimization_images/imageFile523.png>)

√

![image 524](<2023-menart-differentially-private-non-convex-optimization_images/imageFile524.png>)

dDL0 nǫ

5L0DN n

F(w′;S) − F(w∗;S) ≥ 15λD2 −

= Ω

![image 525](<2023-menart-differentially-private-non-convex-optimization_images/imageFile525.png>)

![image 526](<2023-menart-differentially-private-non-convex-optimization_images/imageFile526.png>)

where the last step follows from the setting of λ. Combining the two cases ﬁnishes the proof.

![image 527](<2023-menart-differentially-private-non-convex-optimization_images/imageFile527.png>)

![image 528](<2023-menart-differentially-private-non-convex-optimization_images/imageFile528.png>)

![image 529](<2023-menart-differentially-private-non-convex-optimization_images/imageFile529.png>)

![image 530](<2023-menart-differentially-private-non-convex-optimization_images/imageFile530.png>)

# C Missing Results from Section 4

- C.1 Proof of Lemma 4


For any t ∈ [T], the stationarity conditions of Ft imply  ∇F(wt∗;S) = 2L˜1 wt∗ − wt−1 , and so by Lipschitzness wt∗ − wt−1 ≤ L

0

2L˜1. Further, we have by strong convexity and the accuracy guarantee of A that with probability 1 − β for any t ∈ [T] that wt − wt∗ = O √ 1

![image 531](<2023-menart-differentially-private-non-convex-optimization_images/imageFile531.png>)

![image 532](<2023-menart-differentially-private-non-convex-optimization_images/imageFile532.png>)

Ft(wt;S) − Ft(w∗

t ;S) = O L0

![image 533](<2023-menart-differentially-private-non-convex-optimization_images/imageFile533.png>)

![image 534](<2023-menart-differentially-private-non-convex-optimization_images/imageFile534.png>)

L˜1

√

![image 535](<2023-menart-differentially-private-non-convex-optimization_images/imageFile535.png>)

Td log (n2 log2 (1/β′)/dβ′)

L˜1n√ρ . Thus using the triangle inequality the overall magnitudes of the updates

![image 536](<2023-menart-differentially-private-non-convex-optimization_images/imageFile536.png>)

![image 537](<2023-menart-differentially-private-non-convex-optimization_images/imageFile537.png>)

√

![image 538](<2023-menart-differentially-private-non-convex-optimization_images/imageFile538.png>)

Td log (n2 log2 (1/β′)/dβ′)

L0 + L0

are bounded by wt∗ − wt−1 = O L˜ 1

n√ρ . In the following, let τ = √

![image 539](<2023-menart-differentially-private-non-convex-optimization_images/imageFile539.png>)

![image 540](<2023-menart-differentially-private-non-convex-optimization_images/imageFile540.png>)

![image 541](<2023-menart-differentially-private-non-convex-optimization_images/imageFile541.png>)

1

![image 542](<2023-menart-differentially-private-non-convex-optimization_images/imageFile542.png>)

Td log (n2 log2 (1/β′)/dβ′)

n√ρ . Since at most T iterations occur, we have

![image 543](<2023-menart-differentially-private-non-convex-optimization_images/imageFile543.png>)

![image 544](<2023-menart-differentially-private-non-convex-optimization_images/imageFile544.png>)

![image 545](<2023-menart-differentially-private-non-convex-optimization_images/imageFile545.png>)

 L0 +

wt − w0 = O 

L0 Tdlog(n2 log2 (1/β′)/dβ′) n√ρ

 T L˜1

![image 546](<2023-menart-differentially-private-non-convex-optimization_images/imageFile546.png>)

![image 547](<2023-menart-differentially-private-non-convex-optimization_images/imageFile547.png>)

![image 548](<2023-menart-differentially-private-non-convex-optimization_images/imageFile548.png>)

TL0(1 + τ) L˜1

= O

![image 549](<2023-menart-differentially-private-non-convex-optimization_images/imageFile549.png>)

= O

L0(1 + τ) L˜1

κ−2 κ

0 γ2L˜1) log(F0) − κ log

![image 550](<2023-menart-differentially-private-non-convex-optimization_images/imageFile550.png>)

(1 + F

![image 551](<2023-menart-differentially-private-non-convex-optimization_images/imageFile551.png>)

= O

L0(1 + τ) L˜1

κ−2 κ

0 γ2 log(F0) − κ log

![image 552](<2023-menart-differentially-private-non-convex-optimization_images/imageFile552.png>)

+ L0F

![image 553](<2023-menart-differentially-private-non-convex-optimization_images/imageFile553.png>)

 

 

![image 554](<2023-menart-differentially-private-non-convex-optimization_images/imageFile554.png>)

γL0 dlog(1/β′) n√ρ

![image 555](<2023-menart-differentially-private-non-convex-optimization_images/imageFile555.png>)

![image 556](<2023-menart-differentially-private-non-convex-optimization_images/imageFile556.png>)

![image 557](<2023-menart-differentially-private-non-convex-optimization_images/imageFile557.png>)

γL0 dlog(1/β′) n√ρ

![image 558](<2023-menart-differentially-private-non-convex-optimization_images/imageFile558.png>)

![image 559](<2023-menart-differentially-private-non-convex-optimization_images/imageFile559.png>)

.

- C.2 Proof of Theorem 2 (Convergence of PPM under the KL* Condition)


Proof of Theorem 2. In the following, we condition on the event that every run of A obtains excess risk at most aL

2 0d log (n2 log2 (1/β′)/dβ′)

L˜1n2ρ for some universal constant a. Since β′ = Tβ , this event happens w.p. at least 1 − β by Lemma 3. Further, under this same event, the KL condition holds at every wt, t ∈ [T], by Lemma 4.

![image 560](<2023-menart-differentially-private-non-convex-optimization_images/imageFile560.png>)

![image 561](<2023-menart-differentially-private-non-convex-optimization_images/imageFile561.png>)

2−κ κ

32γ2L1, Φˆ0 = F0 and

1

![image 562](<2023-menart-differentially-private-non-convex-optimization_images/imageFile562.png>)

Now deﬁne c = 1 + F

![image 563](<2023-menart-differentially-private-non-convex-optimization_images/imageFile563.png>)

0

Φˆt = max

1 c

Φˆt−1,min

![image 564](<2023-menart-differentially-private-non-convex-optimization_images/imageFile564.png>)

![image 565](<2023-menart-differentially-private-non-convex-optimization_images/imageFile565.png>)

aγL0 Tdlog(n2 log2 (1/β′)/dβ′) n√ρ

![image 566](<2023-menart-differentially-private-non-convex-optimization_images/imageFile566.png>)

![image 567](<2023-menart-differentially-private-non-convex-optimization_images/imageFile567.png>)

κ

,F0 .

We will ﬁrst prove by induction that F(wt;S) − F(w∗;S) ≤ Φˆt under the assumption that F(wt−1;S) − F(w∗;S) ≤ Φˆt−1. Clearly the base case is satisﬁed for Φˆ0.

To prove the induction step, we will proceed by contradiction. That is, assume by contradiction that F(wt;S) − F(w∗;S) > Φˆt.

Note Ft is L˜1-strongly convex since it is the sum of a L˜1 weakly convex function and a 2L˜1 strongly convex function [DD19b]. Let τ be an upper bound on the excess risk achieved by A on the strongly convex objective Ft. Then

L˜1 2

(i) ≤ F(wt−1;S) −

wt−1 − wt∗ 2 + τ

F(wt;S) = Ft(wt;S) ≤ Ft(wt∗;S) + τ

![image 568](<2023-menart-differentially-private-non-convex-optimization_images/imageFile568.png>)

L˜1 4

wt−1 − wt∗ 2 − τ (7)

=⇒ F(wt−1;S) − F(wt;S) ≥

![image 569](<2023-menart-differentially-private-non-convex-optimization_images/imageFile569.png>)

Inequality (i) uses the fact that Ft(wt∗;S) = F(wt∗;S) + L˜ which implies Ft(wt∗;S) ≤ F(wt−1;S)−L˜

- 1

![image 570](<2023-menart-differentially-private-non-convex-optimization_images/imageFile570.png>)

- 2 wt∗ − wt−1 2 ≤ Ft(wt−1;S) = F(wt−1;S),


2 0d log (n2 log2 (1/β′)/dβ′)T

- 1

![image 571](<2023-menart-differentially-private-non-convex-optimization_images/imageFile571.png>)

- 2 wt∗−wt−1 2. Recall we have τ ≤ aL


![image 572](<2023-menart-differentially-private-non-convex-optimization_images/imageFile572.png>)

L˜1n2ρ

by Lemma 3. Further, note by stationarity conditions for the regularized objective we have  ∇F(wt∗;S) = 2L˜1 wt∗ − wt−1 . (8)

By the assumption that F(wt∗;S)−F(w∗;S) ≥ Φˆt and the KL condition we have  ∇F(wt∗;S) ≥ γ1Φˆ1t/κ, and thus by Eqn. (8) we have wt∗ − wt−1 ≥ 2γ1L˜1

![image 573](<2023-menart-differentially-private-non-convex-optimization_images/imageFile573.png>)

Φˆ1t/κ. Applying Eqn. (7) gives

![image 574](<2023-menart-differentially-private-non-convex-optimization_images/imageFile574.png>)

(i)

1 32γ2L˜1

1 16γ2L˜1

Φˆ2t/κ − τ

Φˆ2t/κ,

≥

F(wt−1;S) − F(wt;S) ≥

![image 575](<2023-menart-differentially-private-non-convex-optimization_images/imageFile575.png>)

![image 576](<2023-menart-differentially-private-non-convex-optimization_images/imageFile576.png>)

√

κ

![image 577](<2023-menart-differentially-private-non-convex-optimization_images/imageFile577.png>)

Td log(n2 log2 (1/β′)/dβ′) n√ρ

where inequality (i) comes from the setting Φˆt ≥ aγL0

. Adding and subtracting F(w∗;S) on the left hand side and rearranging obtains

![image 578](<2023-menart-differentially-private-non-convex-optimization_images/imageFile578.png>)

![image 579](<2023-menart-differentially-private-non-convex-optimization_images/imageFile579.png>)

1 32c2/κγ2L˜1

Φˆ2t−/κ1

F(wt;S) − F(w∗;S) ≤ F(wt−1;S) − F(w∗;S) −

![image 580](<2023-menart-differentially-private-non-convex-optimization_images/imageFile580.png>)

- (i)

≤ Φˆt−1 −

1 32c2/κγ2L˜1

![image 581](<2023-menart-differentially-private-non-convex-optimization_images/imageFile581.png>)

Φˆ2t−/κ1

= 1 − Φ

2−κ κ

![image 582](<2023-menart-differentially-private-non-convex-optimization_images/imageFile582.png>)

t−1

1 32c2/κγ2L˜1

![image 583](<2023-menart-differentially-private-non-convex-optimization_images/imageFile583.png>)

Φ ˆt−1

- (ii) ≤ 1 − F


1 c

1 32cγ2L˜1

2−κ κ

Φˆt−1 ≤ Φˆt.

Φ ˆt−1 =

![image 584](<2023-menart-differentially-private-non-convex-optimization_images/imageFile584.png>)

![image 585](<2023-menart-differentially-private-non-convex-optimization_images/imageFile585.png>)

![image 586](<2023-menart-differentially-private-non-convex-optimization_images/imageFile586.png>)

0

Step (i) uses the inductive assumption that F(wt−1) − F(w∗;S) ≤ Φˆt−1. Inequality (ii) uses the fact that κ ≥ 2, c ≥ 1, and Φt−1 ≤ F0. This establishes a contradiction and thus completes the induction argument. We have now proven that F(wt;S) − F(w∗;S) ≤ Φˆt for all t ∈ {0,...,T}.

√

κ

![image 587](<2023-menart-differentially-private-non-convex-optimization_images/imageFile587.png>)

Td log(n2 log2 (1/β′)/dβ′) n√ρ

All that remains to prove convergence is to show that ΦˆT ≤ γL0

. We have

![image 588](<2023-menart-differentially-private-non-convex-optimization_images/imageFile588.png>)

![image 589](<2023-menart-differentially-private-non-convex-optimization_images/imageFile589.png>)

√

κ

![image 590](<2023-menart-differentially-private-non-convex-optimization_images/imageFile590.png>)

Td log(n2 log2 (1/β′)/dβ′) n√ρ

ΦˆT ≤ max 1c T F0, γL0

and

![image 591](<2023-menart-differentially-private-non-convex-optimization_images/imageFile591.png>)

![image 592](<2023-menart-differentially-private-non-convex-optimization_images/imageFile592.png>)

![image 593](<2023-menart-differentially-private-non-convex-optimization_images/imageFile593.png>)

1 c

![image 594](<2023-menart-differentially-private-non-convex-optimization_images/imageFile594.png>)

T

F0 ≤

![image 595](<2023-menart-differentially-private-non-convex-optimization_images/imageFile595.png>)

γL0 d log(n2 log2 (1/β′)/dβ′) n√ρ

![image 596](<2023-menart-differentially-private-non-convex-optimization_images/imageFile596.png>)

![image 597](<2023-menart-differentially-private-non-convex-optimization_images/imageFile597.png>)

κ

√ρ γL0

log(F0) + κ log n

![image 598](<2023-menart-differentially-private-non-convex-optimization_images/imageFile598.png>)

√

![image 599](<2023-menart-differentially-private-non-convex-optimization_images/imageFile599.png>)

![image 600](<2023-menart-differentially-private-non-convex-optimization_images/imageFile600.png>)

d log(n2 log2 (1/β′)/dβ′)

⇐⇒ T ≥

![image 601](<2023-menart-differentially-private-non-convex-optimization_images/imageFile601.png>)

log(c)

2−κ κ

κ−2 κ

0 γ2L˜1)−1, the setting of T = (1 + 32F

1

![image 602](<2023-menart-differentially-private-non-convex-optimization_images/imageFile602.png>)

![image 603](<2023-menart-differentially-private-non-convex-optimization_images/imageFile603.png>)

32γ2L˜1) ≥ (1 + 32F

Using the fact that log(c) = log 1 + F

![image 604](<2023-menart-differentially-private-non-convex-optimization_images/imageFile604.png>)

0

√ρ

κ−2 κ

0 γ2L˜1) log(F0) + κ log n

![image 605](<2023-menart-differentially-private-non-convex-optimization_images/imageFile605.png>)

![image 606](<2023-menart-differentially-private-non-convex-optimization_images/imageFile606.png>)

γL0√d sufﬁces to ensure convergence.

![image 607](<2023-menart-differentially-private-non-convex-optimization_images/imageFile607.png>)

![image 608](<2023-menart-differentially-private-non-convex-optimization_images/imageFile608.png>)

![image 609](<2023-menart-differentially-private-non-convex-optimization_images/imageFile609.png>)

![image 610](<2023-menart-differentially-private-non-convex-optimization_images/imageFile610.png>)

![image 611](<2023-menart-differentially-private-non-convex-optimization_images/imageFile611.png>)

![image 612](<2023-menart-differentially-private-non-convex-optimization_images/imageFile612.png>)

- C.3 Lower bound for κ ≥ 2


We give a lower bound on excess empirical risk for settings where the empirical risk satisﬁes (1,κ)-KL for κ ≥ 2, under approximate differential privacy.

- Theorem 8. Let κ ≥ 2,0 < ǫ ≤ ln2,0 < δ ≤ 161 (1 − e−ǫ),d ∈ N and B > 0. For any (ǫ,δ)-DP procedure A, there exists a data space X, a set W ⊆ Rd containing a ball of radius B, a dataset S and a convex loss function w  → f(w;x) which is 1-Lipschitz over W, the empirical loss w  → F(w;S) satisﬁes (1,κ)-KL, and


![image 613](<2023-menart-differentially-private-non-convex-optimization_images/imageFile613.png>)

1 4

EA F(A(S);S) − inf

F(w;S) ≥

![image 614](<2023-menart-differentially-private-non-convex-optimization_images/imageFile614.png>)

w∈Rd

1 nǫ

![image 615](<2023-menart-differentially-private-non-convex-optimization_images/imageFile615.png>)

κ

Proof. The proof adapts the construction of [ALD21], Theorem 5 from a lower bound on excess population risk under pure DP setting to that on excess empirical risk under approximate DP. We ﬁrst prove a lower bound for (1,τ)-growth functions, for τ ∈ (1,2]. We recall the one-dimensional, unconstrained (so W = Rd) construction in [ALD21], Theorem 5. The data space X = {−1,1}, and for a ∈ [0,1] to be speciﬁed later, deﬁne functions

f(w;1) = |w − a| w ≤ a |w − a|τ w > a

and f(w;−1) = |w + a|τ w ≤ −a |w + a| w > −a

The functions above are 1-Lipschitz. Consider two datasets S and S′ such that S contains 1+2ρ fraction of 1’s and the rest −1’s. Similarly, S′ contains 1−2ρ fraction of 1’s and the rest −1’s. The number of points differing between S and S′ is thus nρ. We set ρ = 1/nǫ to get 1ǫ differing points. The corresponding empirical risk functions are,

![image 616](<2023-menart-differentially-private-non-convex-optimization_images/imageFile616.png>)

![image 617](<2023-menart-differentially-private-non-convex-optimization_images/imageFile617.png>)

![image 618](<2023-menart-differentially-private-non-convex-optimization_images/imageFile618.png>)

F(w;S) =

F(w;S′) =

- 1 + ρ

![image 619](<2023-menart-differentially-private-non-convex-optimization_images/imageFile619.png>)

- 2


- 1 − ρ

![image 620](<2023-menart-differentially-private-non-convex-optimization_images/imageFile620.png>)

- 2


f(w;1) +

f(w;1) +

- 1 − ρ

![image 621](<2023-menart-differentially-private-non-convex-optimization_images/imageFile621.png>)

- 2


- 1 + ρ

![image 622](<2023-menart-differentially-private-non-convex-optimization_images/imageFile622.png>)

- 2


f(w;−1)

f(w;−1)

In the construction of [ALD21], Theorem 5, the above are their population risk functions “f1(x)” and “f−1(x)”. Their minimizers are wS∗ = a and wS∗′ = −a, with values (1 − ρ)a and (1 + ρ)a respectively. Note that the above functions are convex. Further, with a = ρ

- 1

![image 623](<2023-menart-differentially-private-non-convex-optimization_images/imageFile623.png>)

(τ−1)

![image 624](<2023-menart-differentially-private-non-convex-optimization_images/imageFile624.png>)

- 2 = 1 2(nǫ)


, [ALD21] showed

![image 625](<2023-menart-differentially-private-non-convex-optimization_images/imageFile625.png>)

1 τ−1

![image 626](<2023-menart-differentially-private-non-convex-optimization_images/imageFile626.png>)

that both functions w  → F(w;S) and w  → F(w;S′) exhibit (1,τ)-growth over all of R. For any (ǫ,δ)-DP algorithm A, we have that,

EA[F(A(S˜);S˜) − inf

F(w;S˜)]

sup

w

S˜∈{S,S′}

- 1

![image 627](<2023-menart-differentially-private-non-convex-optimization_images/imageFile627.png>)

- 2


EA F(A(S);S˜) − F(wS∗;S) + F(A(S′);S′) − F(wS∗′;S′) ≥ EA |A(S) − wS∗|τ + |A(S′) − wS∗′|τ ≥

≥

- 1

![image 628](<2023-menart-differentially-private-non-convex-optimization_images/imageFile628.png>)

- 2


(EA [|A(S) − wS∗| + |A(S′) − wS∗′|])τ ≥

1 4

(EA [|wS∗ − wS∗′|])τ

![image 629](<2023-menart-differentially-private-non-convex-optimization_images/imageFile629.png>)

τ τ−1

1 4

1 nǫ

![image 630](<2023-menart-differentially-private-non-convex-optimization_images/imageFile630.png>)

≥

![image 631](<2023-menart-differentially-private-non-convex-optimization_images/imageFile631.png>)

![image 632](<2023-menart-differentially-private-non-convex-optimization_images/imageFile632.png>)

where the second inequality uses the growth condition, the third uses that for 1 ≤ τ ≤ 2,|u + v|τ ≤ 2(|u|τ + |v|τ) and Jensen’s inequality; the fourth uses Lemma 2 of [CH12] and the ﬁnal inequality plugs in

computed distance between minimizers. Finally, the fact (Lemma 6) that convexity and 1, κ−κ1 -growth implies (1,κ)-KL establishes the 41 nǫ 1 κ lower bound for (1,κ)-KL functions.

![image 633](<2023-menart-differentially-private-non-convex-optimization_images/imageFile633.png>)

![image 634](<2023-menart-differentially-private-non-convex-optimization_images/imageFile634.png>)

![image 635](<2023-menart-differentially-private-non-convex-optimization_images/imageFile635.png>)

![image 636](<2023-menart-differentially-private-non-convex-optimization_images/imageFile636.png>)

![image 637](<2023-menart-differentially-private-non-convex-optimization_images/imageFile637.png>)

![image 638](<2023-menart-differentially-private-non-convex-optimization_images/imageFile638.png>)

![image 639](<2023-menart-differentially-private-non-convex-optimization_images/imageFile639.png>)

# D Missing Results from Section 5

- D.1 Gradient Error of Algorithm 3

- Lemma 10. Let T + 1 denote the ﬁnal value of t reached during the run of Algorithm 3. With probability at


least 1 − 2β under the randomness of Algorithm 3, for any t ∈ [T] s.t. σt = N

t

![image 640](<2023-menart-differentially-private-non-convex-optimization_images/imageFile640.png>)

√

![image 641](<2023-menart-differentially-private-non-convex-optimization_images/imageFile641.png>)

dlog(n√ρ/β), it holds that

![image 642](<2023-menart-differentially-private-non-convex-optimization_images/imageFile642.png>)

 ∇t − ∇F(wt;S) ≤ Nt ≤  ∇F(wt;S) +

L0 log(n√ρ/β) √nρ1/4

![image 643](<2023-menart-differentially-private-non-convex-optimization_images/imageFile643.png>)

![image 644](<2023-menart-differentially-private-non-convex-optimization_images/imageFile644.png>)

![image 645](<2023-menart-differentially-private-non-convex-optimization_images/imageFile645.png>)

![image 646](<2023-menart-differentially-private-non-convex-optimization_images/imageFile646.png>)

.

Further, if for any t ∈ [T], σt = 2L

0

![image 647](<2023-menart-differentially-private-non-convex-optimization_images/imageFile647.png>)

n√ρ then t = T and with probability at least 1 − 2β the above condition holds as well as  ∇T − ∇F(wT ;S) ≤ L0

![image 648](<2023-menart-differentially-private-non-convex-optimization_images/imageFile648.png>)

√

![image 649](<2023-menart-differentially-private-non-convex-optimization_images/imageFile649.png>)

d log(n√ρ/β)

![image 650](<2023-menart-differentially-private-non-convex-optimization_images/imageFile650.png>)

![image 651](<2023-menart-differentially-private-non-convex-optimization_images/imageFile651.png>)

n√ρ .

![image 652](<2023-menart-differentially-private-non-convex-optimization_images/imageFile652.png>)

Proof. Condition on the high probability event that for all t ∈ [T], ˆbt ≤ log(n√ρ/β)ˆσt = L0

![image 653](<2023-menart-differentially-private-non-convex-optimization_images/imageFile653.png>)

![image 654](<2023-menart-differentially-private-non-convex-optimization_images/imageFile654.png>)

√

![image 655](<2023-menart-differentially-private-non-convex-optimization_images/imageFile655.png>)

log(n√ρ/β) √nρ1/4 and bt ≤ dlog(n√ρ/β)σt = Nt. This event happens with probability at least 1 − 2β

![image 656](<2023-menart-differentially-private-non-convex-optimization_images/imageFile656.png>)

![image 657](<2023-menart-differentially-private-non-convex-optimization_images/imageFile657.png>)

![image 658](<2023-menart-differentially-private-non-convex-optimization_images/imageFile658.png>)

![image 659](<2023-menart-differentially-private-non-convex-optimization_images/imageFile659.png>)

![image 660](<2023-menart-differentially-private-non-convex-optimization_images/imageFile660.png>)

due to the concentration properties of Gaussian noise and the fact that at most n√ρ iterations are performed. Under this event we then have the following bound on the gradient error,

![image 661](<2023-menart-differentially-private-non-convex-optimization_images/imageFile661.png>)

 ∇t − ∇F(wt;S) ≤ Nt ≤  ∇F(wt;S) +

L0 log(n√ρ/β) √nρ1/4

![image 662](<2023-menart-differentially-private-non-convex-optimization_images/imageFile662.png>)

![image 663](<2023-menart-differentially-private-non-convex-optimization_images/imageFile663.png>)

![image 664](<2023-menart-differentially-private-non-convex-optimization_images/imageFile664.png>)

![image 665](<2023-menart-differentially-private-non-convex-optimization_images/imageFile665.png>)

.

The second part of the lemma statement comes from the fact that when σt = 2L

0

![image 666](<2023-menart-differentially-private-non-convex-optimization_images/imageFile666.png>)

n√ρ, ρt ≥ ρ2 and the stopping condition is triggered. The second error bound result again comes from the concentration of Gaussian noise.

![image 667](<2023-menart-differentially-private-non-convex-optimization_images/imageFile667.png>)

![image 668](<2023-menart-differentially-private-non-convex-optimization_images/imageFile668.png>)

![image 669](<2023-menart-differentially-private-non-convex-optimization_images/imageFile669.png>)

![image 670](<2023-menart-differentially-private-non-convex-optimization_images/imageFile670.png>)

![image 671](<2023-menart-differentially-private-non-convex-optimization_images/imageFile671.png>)

![image 672](<2023-menart-differentially-private-non-convex-optimization_images/imageFile672.png>)

- D.2 Proof of Theorem 3 (Privacy of Algorithm 3)

Proof. Denote T +1 as the highest value attained by the variable t during the run of the algorithm. Consider any round t ∈ [T]. We consider the privacy of the round conditional on wt−1. Speciﬁcally, for the process of generating the gradient and gradient norm estimates at the t’th step, the scale of Gaussian noise ensures this process is ρt-zCDP. Speciﬁcally,

ρt =

L0 nσˆ

![image 673](<2023-menart-differentially-private-non-convex-optimization_images/imageFile673.png>)

2

+

L0 nσt

![image 674](<2023-menart-differentially-private-non-convex-optimization_images/imageFile674.png>)

2

=

√ρ n

![image 675](<2023-menart-differentially-private-non-convex-optimization_images/imageFile675.png>)

![image 676](<2023-menart-differentially-private-non-convex-optimization_images/imageFile676.png>)

+ min

L20dlog(n√ρ/β) n2Nt2

![image 677](<2023-menart-differentially-private-non-convex-optimization_images/imageFile677.png>)

![image 678](<2023-menart-differentially-private-non-convex-optimization_images/imageFile678.png>)

,

ρ 2

![image 679](<2023-menart-differentially-private-non-convex-optimization_images/imageFile679.png>)

.

The ρ2-zCDP guarantee of releasing the ﬁrst T − 1 iterates is then certiﬁed by the stopping condition (i.e. t j=0 ρt ≤ ρ2) and the fully adaptive composition properties of zCDP. That is, [WRRW22, Theorem 1] guarantees the privacy of the overall process even if the privacy bound at each iteration is chosen adaptively (rather than ﬁxed a-priori as with standard composition theorems). Releasing the T’th iterate is also ρ2-zCDP because σT ≥ 2L

![image 680](<2023-menart-differentially-private-non-convex-optimization_images/imageFile680.png>)

![image 681](<2023-menart-differentially-private-non-convex-optimization_images/imageFile681.png>)

![image 682](<2023-menart-differentially-private-non-convex-optimization_images/imageFile682.png>)

0

![image 683](<2023-menart-differentially-private-non-convex-optimization_images/imageFile683.png>)

n√ρ and the sensitivity of any gradient estimate is at most L

![image 684](<2023-menart-differentially-private-non-convex-optimization_images/imageFile684.png>)

0

![image 685](<2023-menart-differentially-private-non-convex-optimization_images/imageFile685.png>)

n . Thus the overall algorithm is ρ-zCDP by composition.

![image 686](<2023-menart-differentially-private-non-convex-optimization_images/imageFile686.png>)

![image 687](<2023-menart-differentially-private-non-convex-optimization_images/imageFile687.png>)

![image 688](<2023-menart-differentially-private-non-convex-optimization_images/imageFile688.png>)

![image 689](<2023-menart-differentially-private-non-convex-optimization_images/imageFile689.png>)

- D.3 Proof of Theorem 4 (Convergence of Adaptive GD under KL* Condition)


In the following we deﬁne T + 1 as the highest attained value of t during the run of Algorithm 3 and deﬁne c := 1 + 8γ21L

.

![image 690](<2023-menart-differentially-private-non-convex-optimization_images/imageFile690.png>)

1

Before proceeding with the main proof, it will be useful to ﬁrst show that in the event that for some t > 0 one has σt = L

0

n√ρ, the algorithm has reached its convergence criteria and stops.

![image 691](<2023-menart-differentially-private-non-convex-optimization_images/imageFile691.png>)

![image 692](<2023-menart-differentially-private-non-convex-optimization_images/imageFile692.png>)

- Lemma 11. Let t > 0 and assume σt = 2L

0

![image 693](<2023-menart-differentially-private-non-convex-optimization_images/imageFile693.png>)

n√ρ. Then Algorithm 3 stops at iteration t and with probability at least 1 − 2β one has

![image 694](<2023-menart-differentially-private-non-convex-optimization_images/imageFile694.png>)

F(wt;S) − F(wS∗;S) = O

γL0 dlog(n√ρ/β) n√ρ

![image 695](<2023-menart-differentially-private-non-convex-optimization_images/imageFile695.png>)

![image 696](<2023-menart-differentially-private-non-convex-optimization_images/imageFile696.png>)

![image 697](<2023-menart-differentially-private-non-convex-optimization_images/imageFile697.png>)

![image 698](<2023-menart-differentially-private-non-convex-optimization_images/imageFile698.png>)

κ

+

γ2L20 log(n√ρ/β) n√ρ

![image 699](<2023-menart-differentially-private-non-convex-optimization_images/imageFile699.png>)

![image 700](<2023-menart-differentially-private-non-convex-optimization_images/imageFile700.png>)

![image 701](<2023-menart-differentially-private-non-convex-optimization_images/imageFile701.png>)

κ/2

Importantly, this rate is strictly faster than the convergence claimed by Theorem 2. The proof is given in Appendix D.5 and follows straightforwardly from the concentration of Gaussian noise and the KL condition.

Given this fact, we can proceed with the rest of the proof only considering the case where σt = √ Nt

![image 702](<2023-menart-differentially-private-non-convex-optimization_images/imageFile702.png>)

![image 703](<2023-menart-differentially-private-non-convex-optimization_images/imageFile703.png>)

dlog(n√ρ/β) for all t ∈ {0,...T}. We will ﬁrst prove (under the stated assumption) the following useful lemma which roughly states that the excess risk is monotonically nonincreasing up to a certain threshold. Note in the following, we use Φ, to denote exact excess loss quantities. This in contrast to the analysis of Section 3 where Φˆ was used to indicate target excess risk loss thresholds. For the rest of this section, we assume L

![image 704](<2023-menart-differentially-private-non-convex-optimization_images/imageFile704.png>)

2 0 log(n√ρ/β)

![image 705](<2023-menart-differentially-private-non-convex-optimization_images/imageFile705.png>)

![image 706](<2023-menart-differentially-private-non-convex-optimization_images/imageFile706.png>)

L1n ≤

√ρ, as per the statement of Theorem 4.

![image 707](<2023-menart-differentially-private-non-convex-optimization_images/imageFile707.png>)

- Lemma 12. Deﬁne Φt = F(wt;S)−F(wS∗;S). Assume F(·;S) is L1-smooth. Assume σt = N


√

t

d log(n√ρ/β)

![image 708](<2023-menart-differentially-private-non-convex-optimization_images/imageFile708.png>)

![image 709](<2023-menart-differentially-private-non-convex-optimization_images/imageFile709.png>)

![image 710](<2023-menart-differentially-private-non-convex-optimization_images/imageFile710.png>)

for all t ∈ [T]. Then with probability at least 1 − 2β we have for all t ∈ [T] that

L20 log(n√ρ/β) L1n√ρ

1 8L1  ∇F(wt;S) 2 −

![image 711](<2023-menart-differentially-private-non-convex-optimization_images/imageFile711.png>)

F(wt;S) − F(wt+1;S) ≥

(9)

![image 712](<2023-menart-differentially-private-non-convex-optimization_images/imageFile712.png>)

![image 713](<2023-menart-differentially-private-non-convex-optimization_images/imageFile713.png>)

![image 714](<2023-menart-differentially-private-non-convex-optimization_images/imageFile714.png>)

and if F(·;S) is also (γ,κ)-KL then

max γ2,1 L20 log(n√ρ/β) L1n√ρ

 

Φt+1 ≤ max   

κ/2

![image 715](<2023-menart-differentially-private-non-convex-optimization_images/imageFile715.png>)

Φt,2

![image 716](<2023-menart-differentially-private-non-convex-optimization_images/imageFile716.png>)

![image 717](<2023-menart-differentially-private-non-convex-optimization_images/imageFile717.png>)



Proof. Throughout the following we condition on the high probabity event that

L0 log(n√ρ/β) √nρ1/4

![image 718](<2023-menart-differentially-private-non-convex-optimization_images/imageFile718.png>)

![image 719](<2023-menart-differentially-private-non-convex-optimization_images/imageFile719.png>)

 ∇t − ∇F(wt;S) ≤ Nt ≤  ∇F(wt;S) +

.

![image 720](<2023-menart-differentially-private-non-convex-optimization_images/imageFile720.png>)

![image 721](<2023-menart-differentially-private-non-convex-optimization_images/imageFile721.png>)

which happens with probability at least 1−β by Lemma 10 (given in Appendix D.1). Now, standard descent lemma analysis yields

L1 2

wt+1 − wt 2

F(wt;S) − F(wt+1;S) ≥  ∇F(wt;S),wt − wt+1 −

![image 722](<2023-menart-differentially-private-non-convex-optimization_images/imageFile722.png>)

1 4L1  ∇F(wt;S) 2 −

1

8L1  ∇t − ∇F(wt;S) 2 ≥

=

![image 723](<2023-menart-differentially-private-non-convex-optimization_images/imageFile723.png>)

![image 724](<2023-menart-differentially-private-non-convex-optimization_images/imageFile724.png>)

L20 log(n√ρ/β) 8L1n√ρ

1 8L1  ∇F(wt;S) 2 −

![image 725](<2023-menart-differentially-private-non-convex-optimization_images/imageFile725.png>)

.

![image 726](<2023-menart-differentially-private-non-convex-optimization_images/imageFile726.png>)

![image 727](<2023-menart-differentially-private-non-convex-optimization_images/imageFile727.png>)

![image 728](<2023-menart-differentially-private-non-convex-optimization_images/imageFile728.png>)

This establishes the ﬁrst claim of the lemma.

{γ2,1}L20 log(n√ρ/β)

Continuing to the second claim, the above implies that if Φt ≥ max

![image 729](<2023-menart-differentially-private-non-convex-optimization_images/imageFile729.png>)

, we have by the KL condition that

L1n√ρ

![image 730](<2023-menart-differentially-private-non-convex-optimization_images/imageFile730.png>)

![image 731](<2023-menart-differentially-private-non-convex-optimization_images/imageFile731.png>)

L20 log(n√ρ/β) L1n√ρ

1 γ2

![image 732](<2023-menart-differentially-private-non-convex-optimization_images/imageFile732.png>)

Φ2t/κ ≥

 ∇F(wt;S) 2 ≥

. (10)

![image 733](<2023-menart-differentially-private-non-convex-optimization_images/imageFile733.png>)

![image 734](<2023-menart-differentially-private-non-convex-optimization_images/imageFile734.png>)

![image 735](<2023-menart-differentially-private-non-convex-optimization_images/imageFile735.png>)

Thus we have

L20 log(n√ρ/β) 8L1n√ρ

1 8L1  ∇F(wt;S) 2 −

![image 736](<2023-menart-differentially-private-non-convex-optimization_images/imageFile736.png>)

Φt − Φt+1 = F(wt;S) − F(wt+1;S) ≥

> 0 (11)

![image 737](<2023-menart-differentially-private-non-convex-optimization_images/imageFile737.png>)

![image 738](<2023-menart-differentially-private-non-convex-optimization_images/imageFile738.png>)

![image 739](<2023-menart-differentially-private-non-convex-optimization_images/imageFile739.png>)

2L20 log(n√ρ/β) L1n√ρ

κ/2

On the other hand, if Φt < γ

![image 740](<2023-menart-differentially-private-non-convex-optimization_images/imageFile740.png>)

then because using Eqn. (11) and the fact that  ∇F(wt;S) ≥ 0 we obtain

![image 741](<2023-menart-differentially-private-non-convex-optimization_images/imageFile741.png>)

![image 742](<2023-menart-differentially-private-non-convex-optimization_images/imageFile742.png>)

max γ2,1 L20 log(n√ρ/β) L1n√ρ

L20 log(n√ρ/β) L1n√ρ ≤ 2

κ/2

![image 743](<2023-menart-differentially-private-non-convex-optimization_images/imageFile743.png>)

![image 744](<2023-menart-differentially-private-non-convex-optimization_images/imageFile744.png>)

Φt+1 ≤ Φt +

.

![image 745](<2023-menart-differentially-private-non-convex-optimization_images/imageFile745.png>)

![image 746](<2023-menart-differentially-private-non-convex-optimization_images/imageFile746.png>)

![image 747](<2023-menart-differentially-private-non-convex-optimization_images/imageFile747.png>)

![image 748](<2023-menart-differentially-private-non-convex-optimization_images/imageFile748.png>)

2 0 log(n√ρ/β)

Above we use the assumption that L

![image 749](<2023-menart-differentially-private-non-convex-optimization_images/imageFile749.png>)

L1n√ρ ≤ 1. Thus combining these two inequalities we have Φt+1 ≤ max Φt,2 max{γ2,1}L20 log(n√ρ/β)

![image 750](<2023-menart-differentially-private-non-convex-optimization_images/imageFile750.png>)

![image 751](<2023-menart-differentially-private-non-convex-optimization_images/imageFile751.png>)

κ/2

![image 752](<2023-menart-differentially-private-non-convex-optimization_images/imageFile752.png>)

.

![image 753](<2023-menart-differentially-private-non-convex-optimization_images/imageFile753.png>)

![image 754](<2023-menart-differentially-private-non-convex-optimization_images/imageFile754.png>)

![image 755](<2023-menart-differentially-private-non-convex-optimization_images/imageFile755.png>)

L1n√ρ

![image 756](<2023-menart-differentially-private-non-convex-optimization_images/imageFile756.png>)

![image 757](<2023-menart-differentially-private-non-convex-optimization_images/imageFile757.png>)

![image 758](<2023-menart-differentially-private-non-convex-optimization_images/imageFile758.png>)

The next lemma establishes how quickly the loss decreases. Speciﬁcally, we show that the loss decreases by a constant fraction after a certain number of steps. The smaller the excess risk is, the more steps are required to achieve this decrease. Recall c := 1 + 8γ21L

.

![image 759](<2023-menart-differentially-private-non-convex-optimization_images/imageFile759.png>)

1

- Lemma 13. Let K > 0 and t ∈ [T] and assume the high probability event of Lemma 12 holds. Then for


κ−2 κ

K ≥ (1cΦt)

− 1 it holds that

![image 760](<2023-menart-differentially-private-non-convex-optimization_images/imageFile760.png>)

![image 761](<2023-menart-differentially-private-non-convex-optimization_images/imageFile761.png>)

max γ2,1 L20 log(n√ρ/β) min{L1,1}n√ρ

 

Φt+K ≤ max  

κ/2

1 c

![image 762](<2023-menart-differentially-private-non-convex-optimization_images/imageFile762.png>)

.

Φt,2

![image 763](<2023-menart-differentially-private-non-convex-optimization_images/imageFile763.png>)

![image 764](<2023-menart-differentially-private-non-convex-optimization_images/imageFile764.png>)

![image 765](<2023-menart-differentially-private-non-convex-optimization_images/imageFile765.png>)



Proof. We here condition on the high probability event that Lemma 12 holds (i.e. that the gradient error is bounded for the entire trajectory). We proceed with a proof by contradiction. Assume by contradiction that

max γ2,1 L20 log(n√ρ/β) min{L1,1}n√ρ

Φt+K > max  

κ/2  

1 c

![image 766](<2023-menart-differentially-private-non-convex-optimization_images/imageFile766.png>)

Φt,2

.

![image 767](<2023-menart-differentially-private-non-convex-optimization_images/imageFile767.png>)

![image 768](<2023-menart-differentially-private-non-convex-optimization_images/imageFile768.png>)

![image 769](<2023-menart-differentially-private-non-convex-optimization_images/imageFile769.png>)

By Lemma 12, this assumption implies the above inequality also holds for all Φt+j,j ∈ {0,...,K},

max γ2, 1 L20 log(n√ρ/β) L1n√ρ

max γ2, 1 L20 log(n√ρ/β) min{L1, 1}n√ρ

< Φt+K ≤ max  

 

 

max   

κ/2

κ/2

![image 770](<2023-menart-differentially-private-non-convex-optimization_images/imageFile770.png>)

![image 771](<2023-menart-differentially-private-non-convex-optimization_images/imageFile771.png>)

1 c

Φt+j, 2

Φt, 2

![image 772](<2023-menart-differentially-private-non-convex-optimization_images/imageFile772.png>)

![image 773](<2023-menart-differentially-private-non-convex-optimization_images/imageFile773.png>)

![image 774](<2023-menart-differentially-private-non-convex-optimization_images/imageFile774.png>)

![image 775](<2023-menart-differentially-private-non-convex-optimization_images/imageFile775.png>)

![image 776](<2023-menart-differentially-private-non-convex-optimization_images/imageFile776.png>)





max γ2, 1 L20 log(n√ρ/β) min{L1, 1}n√ρ

 

=⇒ max   

κ/2

![image 777](<2023-menart-differentially-private-non-convex-optimization_images/imageFile777.png>)

1 c

≤ Φt+j. (12)

Φt, 2

![image 778](<2023-menart-differentially-private-non-convex-optimization_images/imageFile778.png>)

![image 779](<2023-menart-differentially-private-non-convex-optimization_images/imageFile779.png>)

![image 780](<2023-menart-differentially-private-non-convex-optimization_images/imageFile780.png>)



The implication above uses the fact that 2 max{γ2,1}L20 log(n√ρ/β)

![image 781](<2023-menart-differentially-private-non-convex-optimization_images/imageFile781.png>)

min{L1,1}n√ρ

![image 782](<2023-menart-differentially-private-non-convex-optimization_images/imageFile782.png>)

![image 783](<2023-menart-differentially-private-non-convex-optimization_images/imageFile783.png>)

κ/2

2 max{γ2,1}L20 log(n√ρ/β)

![image 784](<2023-menart-differentially-private-non-convex-optimization_images/imageFile784.png>)

. We now sum over K steps and using the descent lemma (see Lemma 12, Eqn (9)). We have

L1n√ρ

![image 785](<2023-menart-differentially-private-non-convex-optimization_images/imageFile785.png>)

![image 786](<2023-menart-differentially-private-non-convex-optimization_images/imageFile786.png>)

K

F(wt;S) − F(wt+K;S) ≥

j=1

L20 log(n√ρ/β) 4L1n√ρ

1 4L1  ∇F(wt+j;S) 2 −

![image 787](<2023-menart-differentially-private-non-convex-optimization_images/imageFile787.png>)

![image 788](<2023-menart-differentially-private-non-convex-optimization_images/imageFile788.png>)

![image 789](<2023-menart-differentially-private-non-convex-optimization_images/imageFile789.png>)

![image 790](<2023-menart-differentially-private-non-convex-optimization_images/imageFile790.png>)

≮

- (i) ≥

K

j=1

1 4γ2L1

![image 791](<2023-menart-differentially-private-non-convex-optimization_images/imageFile791.png>)

Φ2t+/κj −

L20 log(n√ρ/β) 4L1n√ρ

![image 792](<2023-menart-differentially-private-non-convex-optimization_images/imageFile792.png>)

![image 793](<2023-menart-differentially-private-non-convex-optimization_images/imageFile793.png>)

![image 794](<2023-menart-differentially-private-non-convex-optimization_images/imageFile794.png>)

- (ii) ≥

K

j=1

- 1

![image 795](<2023-menart-differentially-private-non-convex-optimization_images/imageFile795.png>)

- 2γ2L1


Φ2t+/κj

- (iii)


κ−2 κ

(1cΦt)

![image 796](<2023-menart-differentially-private-non-convex-optimization_images/imageFile796.png>)

![image 797](<2023-menart-differentially-private-non-convex-optimization_images/imageFile797.png>)

≥

(

![image 798](<2023-menart-differentially-private-non-convex-optimization_images/imageFile798.png>)

2γ2L1

1 c

1 2cγ2L1

Φt)2/κ =

Φt (13)

![image 799](<2023-menart-differentially-private-non-convex-optimization_images/imageFile799.png>)

![image 800](<2023-menart-differentially-private-non-convex-optimization_images/imageFile800.png>)

Step (i) uses the KL condition. Step (ii) uses the fact that Eqn. (12) implies that for all j ∈ {0,...,K}, Φt+j ≥ 2γ

κ/2

2L20A n√ρ

. The second inequality uses the KL condition. Step (iii) uses the fact that Φt+j ≥

![image 801](<2023-menart-differentially-private-non-convex-optimization_images/imageFile801.png>)

![image 802](<2023-menart-differentially-private-non-convex-optimization_images/imageFile802.png>)

1 cΦt, by Eqn. (12), and the setting of K. Manipulating Inequality (13) above we have

![image 803](<2023-menart-differentially-private-non-convex-optimization_images/imageFile803.png>)

1 2cγ2L1

F(wt;S) − F(wt+K;S) = Φt − Φt+K ≥

Φt

![image 804](<2023-menart-differentially-private-non-convex-optimization_images/imageFile804.png>)

1 2cγ2L1

1 c

=⇒ Φt+K ≤ (1 −

)Φt =

Φt.

![image 805](<2023-menart-differentially-private-non-convex-optimization_images/imageFile805.png>)

![image 806](<2023-menart-differentially-private-non-convex-optimization_images/imageFile806.png>)

This establishes the contradiction and thus Φt+K ≤ max 1cΦt,2 max{γ2,1}L20 log(n√ρ/β)

![image 807](<2023-menart-differentially-private-non-convex-optimization_images/imageFile807.png>)

min{L1,1}n√ρ

![image 808](<2023-menart-differentially-private-non-convex-optimization_images/imageFile808.png>)

![image 809](<2023-menart-differentially-private-non-convex-optimization_images/imageFile809.png>)

![image 810](<2023-menart-differentially-private-non-convex-optimization_images/imageFile810.png>)

κ/2

.

![image 811](<2023-menart-differentially-private-non-convex-optimization_images/imageFile811.png>)

![image 812](<2023-menart-differentially-private-non-convex-optimization_images/imageFile812.png>)

![image 813](<2023-menart-differentially-private-non-convex-optimization_images/imageFile813.png>)

![image 814](<2023-menart-differentially-private-non-convex-optimization_images/imageFile814.png>)

We can now prove Theorem 4 itself. With the above two lemmas established, our primary concern is analyzing how the stopping conditions affect the convergence of the algorithm.

Proof of Theorem 4. Condition on the high probability event that Lemma 12 holds (i.e. that the gradient error is bounded for the entire trajectory). We will assume for the rest of the proof we assume that for all t ∈ [T] that

max γ2,1 L20 log(n√ρ/β) min{L1,1}n√ρ

κ/2

![image 815](<2023-menart-differentially-private-non-convex-optimization_images/imageFile815.png>)

Φt ≥ 2

(14)

![image 816](<2023-menart-differentially-private-non-convex-optimization_images/imageFile816.png>)

![image 817](<2023-menart-differentially-private-non-convex-optimization_images/imageFile817.png>)

Note that if for any t ∈ [T] the above inequality is not satisﬁed, by Lemma 12 the convergence guarantee of Theorem 4 is satisﬁed.

We now argue that the algorithm does not stop before convergence is reached by analyzing the stopping condition. It will be helpful to split the run of the algorithm into phases. We denote the ﬁrst phase as the set of iterates W1 = w0,w1,...,wK

;S) − F(wS∗;S) ≥

, where K1 is the largest integer such that F(wK

1

1

1 cΦ0. Similarly deﬁne W2 = wK

;S) −

where K2 is the largest integer such that F(wK

,wK

1+1,...,wK

![image 818](<2023-menart-differentially-private-non-convex-optimization_images/imageFile818.png>)

2

2

1

F(wS∗;S) ≥ 1cΦK

, and so on for W3,W4,...,Wp. Our aim is to show the algorithm does not stop before convergence.

![image 819](<2023-menart-differentially-private-non-convex-optimization_images/imageFile819.png>)

1

First, we bound the largest value p can obtain without convergence. By Lemma 13 and Eqn. (14) we have ΦK

p ≤ c1p F0. Thus for p ≥ pmax := (1 + 8γ2L1) log(F0) + 42−κκ log(n√ρ/[γL0]) ≥ log(F0)+ 42−κκ log(n√ρ/[γL0])

![image 820](<2023-menart-differentially-private-non-convex-optimization_images/imageFile820.png>)

![image 821](<2023-menart-differentially-private-non-convex-optimization_images/imageFile821.png>)

![image 822](<2023-menart-differentially-private-non-convex-optimization_images/imageFile822.png>)

![image 823](<2023-menart-differentially-private-non-convex-optimization_images/imageFile823.png>)

![image 824](<2023-menart-differentially-private-non-convex-optimization_images/imageFile824.png>)

log(c) we have

![image 825](<2023-menart-differentially-private-non-convex-optimization_images/imageFile825.png>)

p ≤

ΦK

1 c

![image 826](<2023-menart-differentially-private-non-convex-optimization_images/imageFile826.png>)

pmax

F0 ≤

γL0 n√ρ

![image 827](<2023-menart-differentially-private-non-convex-optimization_images/imageFile827.png>)

![image 828](<2023-menart-differentially-private-non-convex-optimization_images/imageFile828.png>)

2κ 4−κ

![image 829](<2023-menart-differentially-private-non-convex-optimization_images/imageFile829.png>)

<

cγL0√pmaxdA n√ρ

![image 830](<2023-menart-differentially-private-non-convex-optimization_images/imageFile830.png>)

![image 831](<2023-menart-differentially-private-non-convex-optimization_images/imageFile831.png>)

![image 832](<2023-menart-differentially-private-non-convex-optimization_images/imageFile832.png>)

2κ 4−κ

![image 833](<2023-menart-differentially-private-non-convex-optimization_images/imageFile833.png>)

.

Thus if the algorithm has not converged it must be the case that p ≤ pmax. Let us thus assume p ≤ pmax for the following analysis.

The algorithm stops when Tt=0 ρt > ρ. We observe (denoting K0 = 0 for convenience)

T√ρ n

T

![image 834](<2023-menart-differentially-private-non-convex-optimization_images/imageFile834.png>)

ρt =

+

![image 835](<2023-menart-differentially-private-non-convex-optimization_images/imageFile835.png>)

t=0

T√ρ n

![image 836](<2023-menart-differentially-private-non-convex-optimization_images/imageFile836.png>)

≤

+

![image 837](<2023-menart-differentially-private-non-convex-optimization_images/imageFile837.png>)

T√ρ n

![image 838](<2023-menart-differentially-private-non-convex-optimization_images/imageFile838.png>)

≤

+

![image 839](<2023-menart-differentially-private-non-convex-optimization_images/imageFile839.png>)

L20dlog(n√ρ/β) n2

p

![image 840](<2023-menart-differentially-private-non-convex-optimization_images/imageFile840.png>)

![image 841](<2023-menart-differentially-private-non-convex-optimization_images/imageFile841.png>)

j=1

L20dlog(n√ρ/β) n2

p

![image 842](<2023-menart-differentially-private-non-convex-optimization_images/imageFile842.png>)

![image 843](<2023-menart-differentially-private-non-convex-optimization_images/imageFile843.png>)

j=1

L20dlog(n√ρ/β) n2

p

![image 844](<2023-menart-differentially-private-non-convex-optimization_images/imageFile844.png>)

![image 845](<2023-menart-differentially-private-non-convex-optimization_images/imageFile845.png>)

j=1

Kj

1 Nt2

![image 846](<2023-menart-differentially-private-non-convex-optimization_images/imageFile846.png>)

t=Kj−1

L20 log(n√ρ/β) 4L1n√ρ

Kj

![image 847](<2023-menart-differentially-private-non-convex-optimization_images/imageFile847.png>)

 ∇F(wt;S) 2 −

![image 848](<2023-menart-differentially-private-non-convex-optimization_images/imageFile848.png>)

![image 849](<2023-menart-differentially-private-non-convex-optimization_images/imageFile849.png>)

t=Kj−1

Kj

2  ∇F(wt;S) 2

![image 850](<2023-menart-differentially-private-non-convex-optimization_images/imageFile850.png>)

t=Kj−1

−1

The last step uses the fact that the KL condition and the loss lower bound assumed in Eqn. (14) implies  ∇F(wt;S) 2 ≥ L

2 0 log(n√ρ/β)

![image 851](<2023-menart-differentially-private-non-convex-optimization_images/imageFile851.png>)

L1n√ρ . Continuing, by the KL condition we have,

![image 852](<2023-menart-differentially-private-non-convex-optimization_images/imageFile852.png>)

![image 853](<2023-menart-differentially-private-non-convex-optimization_images/imageFile853.png>)

L20dlog(n√ρ/β) n2

T√ρ n

Kj

p

T

2γ2 Φ2K/κ

![image 854](<2023-menart-differentially-private-non-convex-optimization_images/imageFile854.png>)

![image 855](<2023-menart-differentially-private-non-convex-optimization_images/imageFile855.png>)

ρt ≤

+

![image 856](<2023-menart-differentially-private-non-convex-optimization_images/imageFile856.png>)

![image 857](<2023-menart-differentially-private-non-convex-optimization_images/imageFile857.png>)

![image 858](<2023-menart-differentially-private-non-convex-optimization_images/imageFile858.png>)

t=0

j=1

t=Kj−1

j

T√ρ n

L20dlog(n√ρ/β) n2

p

2γ2 Φ2K/κ

![image 859](<2023-menart-differentially-private-non-convex-optimization_images/imageFile859.png>)

![image 860](<2023-menart-differentially-private-non-convex-optimization_images/imageFile860.png>)

κ−2 κ

≤

![image 861](<2023-menart-differentially-private-non-convex-optimization_images/imageFile861.png>)

Φ

+

![image 862](<2023-menart-differentially-private-non-convex-optimization_images/imageFile862.png>)

![image 863](<2023-menart-differentially-private-non-convex-optimization_images/imageFile863.png>)

![image 864](<2023-menart-differentially-private-non-convex-optimization_images/imageFile864.png>)

Kj−1

j=1

j

T√ρ n

L20dlog(n√ρ/β) n2

p

2γ2 Φ2K/κ

![image 865](<2023-menart-differentially-private-non-convex-optimization_images/imageFile865.png>)

![image 866](<2023-menart-differentially-private-non-convex-optimization_images/imageFile866.png>)

κ−2 κ

![image 867](<2023-menart-differentially-private-non-convex-optimization_images/imageFile867.png>)

≤

Φ

+

![image 868](<2023-menart-differentially-private-non-convex-optimization_images/imageFile868.png>)

![image 869](<2023-menart-differentially-private-non-convex-optimization_images/imageFile869.png>)

![image 870](<2023-menart-differentially-private-non-convex-optimization_images/imageFile870.png>)

Kj

j=1

j

2γ2L20dlog(n√ρ/β) n2

T√ρ n

![image 871](<2023-menart-differentially-private-non-convex-optimization_images/imageFile871.png>)

![image 872](<2023-menart-differentially-private-non-convex-optimization_images/imageFile872.png>)

κ−4 κ

≤

![image 873](<2023-menart-differentially-private-non-convex-optimization_images/imageFile873.png>)

Kj .

Φ

pmax max j∈[p]

+

![image 874](<2023-menart-differentially-private-non-convex-optimization_images/imageFile874.png>)

![image 875](<2023-menart-differentially-private-non-convex-optimization_images/imageFile875.png>)

Thus, if T ≤ 12n√ρ, the algorithm has not stopped unless for some t ∈ [T] we have that Φt = O γL0

![image 876](<2023-menart-differentially-private-non-convex-optimization_images/imageFile876.png>)

![image 877](<2023-menart-differentially-private-non-convex-optimization_images/imageFile877.png>)

√

2κ 4−κ

d log(n√ρ/β)pmax n√ρ

![image 878](<2023-menart-differentially-private-non-convex-optimization_images/imageFile878.png>)

![image 879](<2023-menart-differentially-private-non-convex-optimization_images/imageFile879.png>)

![image 880](<2023-menart-differentially-private-non-convex-optimization_images/imageFile880.png>)

.

![image 881](<2023-menart-differentially-private-non-convex-optimization_images/imageFile881.png>)

![image 882](<2023-menart-differentially-private-non-convex-optimization_images/imageFile882.png>)

To ﬁnish the proof, we consider the convergence when the algorithm stops after T > 21n√ρ. Recall we are assuming the algorithm has run for at most p ≤ pmax number of phases (as otherwise the algorithm has converged). The number of iterations during each of each of these phases is at most Φ

![image 883](<2023-menart-differentially-private-non-convex-optimization_images/imageFile883.png>)

![image 884](<2023-menart-differentially-private-non-convex-optimization_images/imageFile884.png>)

κ−2 κ

![image 885](<2023-menart-differentially-private-non-convex-optimization_images/imageFile885.png>)

Kp . Thus the

algorithm has not stopped unless

κ−2 κ

Kp ≥

![image 886](<2023-menart-differentially-private-non-convex-optimization_images/imageFile886.png>)

pmaxΦ

n√ρ =⇒ ΦK

- 1

![image 887](<2023-menart-differentially-private-non-convex-optimization_images/imageFile887.png>)

- 2


p ≤

![image 888](<2023-menart-differentially-private-non-convex-optimization_images/imageFile888.png>)

2pmax n√ρ

![image 889](<2023-menart-differentially-private-non-convex-optimization_images/imageFile889.png>)

![image 890](<2023-menart-differentially-private-non-convex-optimization_images/imageFile890.png>)

κ 2−κ

![image 891](<2023-menart-differentially-private-non-convex-optimization_images/imageFile891.png>)

.

To summarize, we now have three different bounds on the excess depending on three possible events. The ﬁrst case is simply when ΦT ≤ 2 max{γ2,1}L20 log(n√ρ/β)

κ/2

![image 892](<2023-menart-differentially-private-non-convex-optimization_images/imageFile892.png>)

. The second case is

min{L1,1}n√ρ

![image 893](<2023-menart-differentially-private-non-convex-optimization_images/imageFile893.png>)

![image 894](<2023-menart-differentially-private-non-convex-optimization_images/imageFile894.png>)

κ/2

when ΦT ≥ 2 max{γ2,1}L20 log(n√ρ/β)

and T ≤ 12n√ρ, in which case we have shown ΦT =

![image 895](<2023-menart-differentially-private-non-convex-optimization_images/imageFile895.png>)

![image 896](<2023-menart-differentially-private-non-convex-optimization_images/imageFile896.png>)

min{L1,1}n√ρ

![image 897](<2023-menart-differentially-private-non-convex-optimization_images/imageFile897.png>)

![image 898](<2023-menart-differentially-private-non-convex-optimization_images/imageFile898.png>)

![image 899](<2023-menart-differentially-private-non-convex-optimization_images/imageFile899.png>)

√

2κ 4−κ

κ/2

. The ﬁnal case is when ΦT ≥ 2 max{γ2,1}L20 log(n√ρ/β)

d log(n√ρ/β)pmax n√ρ

![image 900](<2023-menart-differentially-private-non-convex-optimization_images/imageFile900.png>)

![image 901](<2023-menart-differentially-private-non-convex-optimization_images/imageFile901.png>)

O cγL0

![image 902](<2023-menart-differentially-private-non-convex-optimization_images/imageFile902.png>)

![image 903](<2023-menart-differentially-private-non-convex-optimization_images/imageFile903.png>)

and

min{L1,1}n√ρ

![image 904](<2023-menart-differentially-private-non-convex-optimization_images/imageFile904.png>)

![image 905](<2023-menart-differentially-private-non-convex-optimization_images/imageFile905.png>)

![image 906](<2023-menart-differentially-private-non-convex-optimization_images/imageFile906.png>)

![image 907](<2023-menart-differentially-private-non-convex-optimization_images/imageFile907.png>)

κ 2−κ

T > 21n√ρ, in which case we have shown ΦT ≤ p

![image 908](<2023-menart-differentially-private-non-convex-optimization_images/imageFile908.png>)

. Combining these results yields the theorem statement.

![image 909](<2023-menart-differentially-private-non-convex-optimization_images/imageFile909.png>)

n√ρ

max

![image 910](<2023-menart-differentially-private-non-convex-optimization_images/imageFile910.png>)

![image 911](<2023-menart-differentially-private-non-convex-optimization_images/imageFile911.png>)

![image 912](<2023-menart-differentially-private-non-convex-optimization_images/imageFile912.png>)

![image 913](<2023-menart-differentially-private-non-convex-optimization_images/imageFile913.png>)

![image 914](<2023-menart-differentially-private-non-convex-optimization_images/imageFile914.png>)

![image 915](<2023-menart-differentially-private-non-convex-optimization_images/imageFile915.png>)

![image 916](<2023-menart-differentially-private-non-convex-optimization_images/imageFile916.png>)

- D.4 Proof of Lemma 5


Proof. We will prove the lemma result by induction. For any t ∈ 0,...,T − 1, assuming wt ∈ S, we will show that wt+1 ∈ S. The base case for w0 holds because S is deﬁned to contain w0.

Before proceeding, we condition on the event that for all t ∈ {0,...,T − 1} we have that  ∇t − ∇F(wt;S) ≤  ∇F(wt;S) + L0

√

log(n√ρ/β) √nρ1/4 , which happens with probability at least 1 − 2β

![image 917](<2023-menart-differentially-private-non-convex-optimization_images/imageFile917.png>)

![image 918](<2023-menart-differentially-private-non-convex-optimization_images/imageFile918.png>)

![image 919](<2023-menart-differentially-private-non-convex-optimization_images/imageFile919.png>)

![image 920](<2023-menart-differentially-private-non-convex-optimization_images/imageFile920.png>)

by Lemma 10 in Appendix D.1.

To prove the induction step, let wt ∈ S. We divide the proof into two cases, depending on  ∇F(wt;S) . In the ﬁrst case, assume  ∇F(wt;S) < L

2 0 log(n√ρ/β)

1/2

![image 921](<2023-menart-differentially-private-non-convex-optimization_images/imageFile921.png>)

. In this case, we will roughly prove that wt+1 is in S because it has not moved too far from wt. Since wt ∈ S, the KL condition holds at wt. Thus the gradient norm bound and the KL condition imply F(wt;S) − F(wS∗;S) ≤ γL

n√ρ

![image 922](<2023-menart-differentially-private-non-convex-optimization_images/imageFile922.png>)

![image 923](<2023-menart-differentially-private-non-convex-optimization_images/imageFile923.png>)

2 0 log(n√ρ/β)

κ/2

![image 924](<2023-menart-differentially-private-non-convex-optimization_images/imageFile924.png>)

. Let R = 2 L

n√ρ

![image 925](<2023-menart-differentially-private-non-convex-optimization_images/imageFile925.png>)

![image 926](<2023-menart-differentially-private-non-convex-optimization_images/imageFile926.png>)

2 0 log(n√ρ/β)

1/2

![image 927](<2023-menart-differentially-private-non-convex-optimization_images/imageFile927.png>)

and recall we deﬁne the level set threshold as α = max F(w0;S),F(wS∗;S) + max F(w0;S),F(wS∗;S) + 2(γκ/2 + L0) L

L21n√ρ

![image 928](<2023-menart-differentially-private-non-convex-optimization_images/imageFile928.png>)

![image 929](<2023-menart-differentially-private-non-convex-optimization_images/imageFile929.png>)

2 0 log(n√ρ/β)

1/2

![image 930](<2023-menart-differentially-private-non-convex-optimization_images/imageFile930.png>)

. For any point w′ ∈ B(wt;R), by Lips-

n√ρ

![image 931](<2023-menart-differentially-private-non-convex-optimization_images/imageFile931.png>)

![image 932](<2023-menart-differentially-private-non-convex-optimization_images/imageFile932.png>)

chitzness one has F(w′;S) ≤ F(wt;S) − F(wS∗;s) + F(wS∗;S) + L0( ∇F(wt;S) +  ∇t − ∇F(wt;S) )

L0 log(n√ρ/β) √nρ1/4

L20 log(n√ρ/β) n√ρ

γL20 log(n√ρ/β) n√ρ

κ/2

1/2

![image 933](<2023-menart-differentially-private-non-convex-optimization_images/imageFile933.png>)

![image 934](<2023-menart-differentially-private-non-convex-optimization_images/imageFile934.png>)

![image 935](<2023-menart-differentially-private-non-convex-optimization_images/imageFile935.png>)

![image 936](<2023-menart-differentially-private-non-convex-optimization_images/imageFile936.png>)

≤ F(wS∗;S) + 2

+ L0

+

![image 937](<2023-menart-differentially-private-non-convex-optimization_images/imageFile937.png>)

![image 938](<2023-menart-differentially-private-non-convex-optimization_images/imageFile938.png>)

![image 939](<2023-menart-differentially-private-non-convex-optimization_images/imageFile939.png>)

![image 940](<2023-menart-differentially-private-non-convex-optimization_images/imageFile940.png>)

![image 941](<2023-menart-differentially-private-non-convex-optimization_images/imageFile941.png>)

![image 942](<2023-menart-differentially-private-non-convex-optimization_images/imageFile942.png>)

L20 log(n√ρ/β) n√ρ

1/2

![image 943](<2023-menart-differentially-private-non-convex-optimization_images/imageFile943.png>)

≤ F(wS∗;S) + 2(γκ/2 + L0)

≤ α.

![image 944](<2023-menart-differentially-private-non-convex-optimization_images/imageFile944.png>)

![image 945](<2023-menart-differentially-private-non-convex-optimization_images/imageFile945.png>)

Thus B(wt;R) ⊆ I. Since B(wt;R) is path connected and wt ∈ S, we have B(wt;R) ⊆ S by the deﬁnition

of S. Further, with probability at least 1 − β we have wt − wt+1 ≤ η( ∇F(wt;S) +  ∇t − ∇F(wt;S) )

L0 log(n√ρ/β) √nρ1/4

L20 log(n√ρ/β) n√ρ

1/2

![image 946](<2023-menart-differentially-private-non-convex-optimization_images/imageFile946.png>)

(i) ≤ η 2 ∇F(wt;S) +

(ii)

3 2L1

![image 947](<2023-menart-differentially-private-non-convex-optimization_images/imageFile947.png>)

![image 948](<2023-menart-differentially-private-non-convex-optimization_images/imageFile948.png>)

≤

≤ R

![image 949](<2023-menart-differentially-private-non-convex-optimization_images/imageFile949.png>)

![image 950](<2023-menart-differentially-private-non-convex-optimization_images/imageFile950.png>)

![image 951](<2023-menart-differentially-private-non-convex-optimization_images/imageFile951.png>)

![image 952](<2023-menart-differentially-private-non-convex-optimization_images/imageFile952.png>)

![image 953](<2023-menart-differentially-private-non-convex-optimization_images/imageFile953.png>)

=⇒ wt+1 ∈ BR(wt) Above, step (i) uses that the scale of noise in Algorithm 3 guarantees with high probability that  ∇t − ∇F(wt;S) . Step (ii) uses the assumption that  ∇F(wt;S) ≤ L

2 0 log(n√ρ/β)

1/2

![image 954](<2023-menart-differentially-private-non-convex-optimization_images/imageFile954.png>)

, the setting of R (above) and η = 2L1

n√ρ

![image 955](<2023-menart-differentially-private-non-convex-optimization_images/imageFile955.png>)

![image 956](<2023-menart-differentially-private-non-convex-optimization_images/imageFile956.png>)

. As we have previously show, BR(wt) ⊆ S, so we have shown wt+1 ∈ S. We now consider the second case where  ∇F(wt;S) ≥ L

![image 957](<2023-menart-differentially-private-non-convex-optimization_images/imageFile957.png>)

1

2 0 log(n√ρ/β)

![image 958](<2023-menart-differentially-private-non-convex-optimization_images/imageFile958.png>)

n√ρ . Consider the path parameterized by l ∈ [0,1] deﬁned by w(l) = wt + l(wt+1 − wt). By the update rule of Algorithm 3 and standard descent lemma analysis we have (using the smoothness of F(·;S))

![image 959](<2023-menart-differentially-private-non-convex-optimization_images/imageFile959.png>)

![image 960](<2023-menart-differentially-private-non-convex-optimization_images/imageFile960.png>)

L1 2

wt − w(l) 2

F(wt;S) − F(w(l);S) ≥  ∇F(wt;S),wt − w(l) −

![image 961](<2023-menart-differentially-private-non-convex-optimization_images/imageFile961.png>)

l2L1 2

wt − wt+1 2

≥ l ∇F(wt;S),wt − wt+1 −

![image 962](<2023-menart-differentially-private-non-convex-optimization_images/imageFile962.png>)

l2

l 4L1  ∇F(wt;S) 2 −

8L1  ∇t − ∇F(wt;S) 2 ≥

=

![image 963](<2023-menart-differentially-private-non-convex-optimization_images/imageFile963.png>)

![image 964](<2023-menart-differentially-private-non-convex-optimization_images/imageFile964.png>)

l2L20 log(n√ρ/β) 8L1n√ρ

l 4L1  ∇F(wt;S) 2 −

![image 965](<2023-menart-differentially-private-non-convex-optimization_images/imageFile965.png>)

![image 966](<2023-menart-differentially-private-non-convex-optimization_images/imageFile966.png>)

![image 967](<2023-menart-differentially-private-non-convex-optimization_images/imageFile967.png>)

![image 968](<2023-menart-differentially-private-non-convex-optimization_images/imageFile968.png>)

- (i)

≥ l

1 4L1  ∇F(wt;S) 2 −

![image 969](<2023-menart-differentially-private-non-convex-optimization_images/imageFile969.png>)

L20 log(n√ρ/β) 8L1n√ρ

![image 970](<2023-menart-differentially-private-non-convex-optimization_images/imageFile970.png>)

![image 971](<2023-menart-differentially-private-non-convex-optimization_images/imageFile971.png>)

![image 972](<2023-menart-differentially-private-non-convex-optimization_images/imageFile972.png>)

- (ii)


l 4L1  ∇F(wt;S) 2 ≥ 0.

≥

![image 973](<2023-menart-differentially-private-non-convex-optimization_images/imageFile973.png>)

2 0 log(n√ρ/β)

Step (i) uses the fact that l ≤ 1. Step (ii) uses the assumption that  ∇F(wt;S) ≥ L

![image 974](<2023-menart-differentially-private-non-convex-optimization_images/imageFile974.png>)

n√ρ . We have shown F(wt;S) ≥ F(w(l);S) for every l ∈ [0,1]. Thus {w(l)}l∈[0,1] ⊆ I, and because {w(l)}l∈[0,1] is path connected and contains wt ∈ S, we have {w(l)}l∈[0,1] ⊆ S and speciﬁcally wt+1 ∈ S.

![image 975](<2023-menart-differentially-private-non-convex-optimization_images/imageFile975.png>)

![image 976](<2023-menart-differentially-private-non-convex-optimization_images/imageFile976.png>)

![image 977](<2023-menart-differentially-private-non-convex-optimization_images/imageFile977.png>)

![image 978](<2023-menart-differentially-private-non-convex-optimization_images/imageFile978.png>)

![image 979](<2023-menart-differentially-private-non-convex-optimization_images/imageFile979.png>)

![image 980](<2023-menart-differentially-private-non-convex-optimization_images/imageFile980.png>)

- D.5 Proof of Lemma 11


Proof. First note that when σt = L

n√ρ then ρt > ρ and the algorithm stops. Furthermore, in this case we also have Nt ≤ L0

0

![image 981](<2023-menart-differentially-private-non-convex-optimization_images/imageFile981.png>)

![image 982](<2023-menart-differentially-private-non-convex-optimization_images/imageFile982.png>)

√

d log(n√ρ/β)

![image 983](<2023-menart-differentially-private-non-convex-optimization_images/imageFile983.png>)

![image 984](<2023-menart-differentially-private-non-convex-optimization_images/imageFile984.png>)

n√ρ , and thus by the concentration of the noise we have with probability at least 1 − β that

![image 985](<2023-menart-differentially-private-non-convex-optimization_images/imageFile985.png>)

![image 986](<2023-menart-differentially-private-non-convex-optimization_images/imageFile986.png>)

L0 log(n√ρ/β) √nρ1/4 The KL condition then implies that

L0 dlog(n√ρ/β) n√ρ

![image 987](<2023-menart-differentially-private-non-convex-optimization_images/imageFile987.png>)

![image 988](<2023-menart-differentially-private-non-convex-optimization_images/imageFile988.png>)

![image 989](<2023-menart-differentially-private-non-convex-optimization_images/imageFile989.png>)

![image 990](<2023-menart-differentially-private-non-convex-optimization_images/imageFile990.png>)

 ∇F(wt;S) ≤

+

![image 991](<2023-menart-differentially-private-non-convex-optimization_images/imageFile991.png>)

![image 992](<2023-menart-differentially-private-non-convex-optimization_images/imageFile992.png>)

![image 993](<2023-menart-differentially-private-non-convex-optimization_images/imageFile993.png>)

![image 994](<2023-menart-differentially-private-non-convex-optimization_images/imageFile994.png>)

γL0 dlog(n√ρ/β) n√ρ

γ2L20 log(n√ρ/β) n√ρ

κ

κ/2

![image 995](<2023-menart-differentially-private-non-convex-optimization_images/imageFile995.png>)

![image 996](<2023-menart-differentially-private-non-convex-optimization_images/imageFile996.png>)

![image 997](<2023-menart-differentially-private-non-convex-optimization_images/imageFile997.png>)

F(w;S) − F(wS∗;S) = O

+

![image 998](<2023-menart-differentially-private-non-convex-optimization_images/imageFile998.png>)

![image 999](<2023-menart-differentially-private-non-convex-optimization_images/imageFile999.png>)

![image 1000](<2023-menart-differentially-private-non-convex-optimization_images/imageFile1000.png>)

![image 1001](<2023-menart-differentially-private-non-convex-optimization_images/imageFile1001.png>)

![image 1002](<2023-menart-differentially-private-non-convex-optimization_images/imageFile1002.png>)

![image 1003](<2023-menart-differentially-private-non-convex-optimization_images/imageFile1003.png>)

![image 1004](<2023-menart-differentially-private-non-convex-optimization_images/imageFile1004.png>)

![image 1005](<2023-menart-differentially-private-non-convex-optimization_images/imageFile1005.png>)

- D.6 Proof of Theorem 5 (Adaptive Gradient Descent without KL Condition) In the following, we let T + 1 denote the largest value attained by t during the run of the algorithm.


Privacy Proof The prove privacy we will use the following lemma.

- Lemma 14. [BS16, Proposition 1.4] Any algorithm which is (ǫ,0)-DP is also (12ǫ2)-zCDP.


![image 1006](<2023-menart-differentially-private-non-convex-optimization_images/imageFile1006.png>)

The process of releasing w0,...,wT is ρ-zCDP by Theorem 3. We thus only need to handel the additional privacy loss incurred via the use of the exponential mechanism to select t∗. Speciﬁcally, the exponential mechanism guarantees (√ρ,0)-DP and is thus 12ρ-zCDP by Lemma 14. The overall privacy is then 2ρzCDP.

![image 1007](<2023-menart-differentially-private-non-convex-optimization_images/imageFile1007.png>)

![image 1008](<2023-menart-differentially-private-non-convex-optimization_images/imageFile1008.png>)

Convergence Proof Recall t∗ ∈ [T] is the index sampled by the exponential mechanism. Let N∗ = min t∈T

{ ∇F(wt;S) }. Note that the guarantees of the exponential mechanism (used to sample t∗) and scale of noise added to the gradient norm estimates we have with probability at least 1 − 2β that,

 ∇F(wt∗;S) =  ∇F(wt∗;S) − Nt∗ + Nt∗ − N∗ + N∗ ≤

4L0 log(n√ρ/β) n√ρ

L0 log(n√ρ/β) √nρ1/4

![image 1009](<2023-menart-differentially-private-non-convex-optimization_images/imageFile1009.png>)

![image 1010](<2023-menart-differentially-private-non-convex-optimization_images/imageFile1010.png>)

+ N∗, (15)

+

![image 1011](<2023-menart-differentially-private-non-convex-optimization_images/imageFile1011.png>)

![image 1012](<2023-menart-differentially-private-non-convex-optimization_images/imageFile1012.png>)

![image 1013](<2023-menart-differentially-private-non-convex-optimization_images/imageFile1013.png>)

![image 1014](<2023-menart-differentially-private-non-convex-optimization_images/imageFile1014.png>)

√d

![image 1015](<2023-menart-differentially-private-non-convex-optimization_images/imageFile1015.png>)

n√ρ, then Nt ≤ L

We will now proceed to bound N∗. First, if for any t one has σt = 2L

0

0

n√ρ and thus N∗ ≤ L

![image 1016](<2023-menart-differentially-private-non-convex-optimization_images/imageFile1016.png>)

![image 1017](<2023-menart-differentially-private-non-convex-optimization_images/imageFile1017.png>)

![image 1018](<2023-menart-differentially-private-non-convex-optimization_images/imageFile1018.png>)

![image 1019](<2023-menart-differentially-private-non-convex-optimization_images/imageFile1019.png>)

√

![image 1020](<2023-menart-differentially-private-non-convex-optimization_images/imageFile1020.png>)

d

0

n√ρ . The convergence guarantees are then satisﬁed by Eqn. (15). We now turn towards the more difﬁcult case where σt = N

![image 1021](<2023-menart-differentially-private-non-convex-optimization_images/imageFile1021.png>)

![image 1022](<2023-menart-differentially-private-non-convex-optimization_images/imageFile1022.png>)

√

dlog(n√ρ/β) for all t ∈ [T]. We start by analyzing the convergence of the algorithm in terms of the number of rounds T. By Lemma 12, Eqn. (9), we have with probability at least 1 − β that,

t

![image 1023](<2023-menart-differentially-private-non-convex-optimization_images/imageFile1023.png>)

![image 1024](<2023-menart-differentially-private-non-convex-optimization_images/imageFile1024.png>)

![image 1025](<2023-menart-differentially-private-non-convex-optimization_images/imageFile1025.png>)

L20 log(n√ρ/β) 8L1n√ρ

1 8L1  ∇F(wt;S) 2 −

![image 1026](<2023-menart-differentially-private-non-convex-optimization_images/imageFile1026.png>)

F(wt;S) − F(wt+1;S) ≥

.

![image 1027](<2023-menart-differentially-private-non-convex-optimization_images/imageFile1027.png>)

![image 1028](<2023-menart-differentially-private-non-convex-optimization_images/imageFile1028.png>)

![image 1029](<2023-menart-differentially-private-non-convex-optimization_images/imageFile1029.png>)

Summing over all iterates and rearranging gives,

T

1 T

 ∇F(wt;S) ≤

![image 1030](<2023-menart-differentially-private-non-convex-optimization_images/imageFile1030.png>)

t=1

![image 1031](<2023-menart-differentially-private-non-convex-optimization_images/imageFile1031.png>)

8F0L1 T

+

![image 1032](<2023-menart-differentially-private-non-convex-optimization_images/imageFile1032.png>)

L0 log(n√ρ/β) √nρ1/4

![image 1033](<2023-menart-differentially-private-non-convex-optimization_images/imageFile1033.png>)

![image 1034](<2023-menart-differentially-private-non-convex-optimization_images/imageFile1034.png>)

. (16)

![image 1035](<2023-menart-differentially-private-non-convex-optimization_images/imageFile1035.png>)

![image 1036](<2023-menart-differentially-private-non-convex-optimization_images/imageFile1036.png>)

We now consider the worst case guarantee for Algorithm 3. Recall N∗ = min

{ ∇F(wt;S) }. We can use N∗ to lower bound the number of iterations made by the algorithm. We have,

t∈T

L20dlog(n√ρ/β) n2

T√ρ 2n

T

T

1 Nt2 ≤

![image 1037](<2023-menart-differentially-private-non-convex-optimization_images/imageFile1037.png>)

![image 1038](<2023-menart-differentially-private-non-convex-optimization_images/imageFile1038.png>)

+

ρt =

![image 1039](<2023-menart-differentially-private-non-convex-optimization_images/imageFile1039.png>)

![image 1040](<2023-menart-differentially-private-non-convex-optimization_images/imageFile1040.png>)

![image 1041](<2023-menart-differentially-private-non-convex-optimization_images/imageFile1041.png>)

t=1

t=0

T√ρ 2n

TL20dlog(n√ρ/β) n2(N∗)2

![image 1042](<2023-menart-differentially-private-non-convex-optimization_images/imageFile1042.png>)

![image 1043](<2023-menart-differentially-private-non-convex-optimization_images/imageFile1043.png>)

.

+

![image 1044](<2023-menart-differentially-private-non-convex-optimization_images/imageFile1044.png>)

![image 1045](<2023-menart-differentially-private-non-convex-optimization_images/imageFile1045.png>)

Further by the stopping condition we have,

T

1 2

=⇒ T ≥

![image 1046](<2023-menart-differentially-private-non-convex-optimization_images/imageFile1046.png>)

√ρ 2n ≥

L20dlog(n√ρ/β) n2(N∗)2

ρ 2

![image 1047](<2023-menart-differentially-private-non-convex-optimization_images/imageFile1047.png>)

![image 1048](<2023-menart-differentially-private-non-convex-optimization_images/imageFile1048.png>)

+

![image 1049](<2023-menart-differentially-private-non-convex-optimization_images/imageFile1049.png>)

![image 1050](<2023-menart-differentially-private-non-convex-optimization_images/imageFile1050.png>)

![image 1051](<2023-menart-differentially-private-non-convex-optimization_images/imageFile1051.png>)

n2(N∗)2ρ L20dlog(n√ρ/β)

,n√ρ .

min

![image 1052](<2023-menart-differentially-private-non-convex-optimization_images/imageFile1052.png>)

![image 1053](<2023-menart-differentially-private-non-convex-optimization_images/imageFile1053.png>)

![image 1054](<2023-menart-differentially-private-non-convex-optimization_images/imageFile1054.png>)

By Eqn. (16) we also have,

1 T

N∗ ≤

![image 1055](<2023-menart-differentially-private-non-convex-optimization_images/imageFile1055.png>)

T

 ∇F(wt;S) ≤

t=1

![image 1056](<2023-menart-differentially-private-non-convex-optimization_images/imageFile1056.png>)

8F0L1 T

+

![image 1057](<2023-menart-differentially-private-non-convex-optimization_images/imageFile1057.png>)

L0 log(n√ρ/β) √nρ1/4

![image 1058](<2023-menart-differentially-private-non-convex-optimization_images/imageFile1058.png>)

.

![image 1059](<2023-menart-differentially-private-non-convex-optimization_images/imageFile1059.png>)

![image 1060](<2023-menart-differentially-private-non-convex-optimization_images/imageFile1060.png>)

Applying the above lower bound on T to the upper bound on N∗ we obtain,

3L0 F0L1dlog(n√ρ/β) nN∗√ρ

L0 log(n√ρ/β) √nρ1/4

![image 1061](<2023-menart-differentially-private-non-convex-optimization_images/imageFile1061.png>)

![image 1062](<2023-menart-differentially-private-non-convex-optimization_images/imageFile1062.png>)

![image 1063](<2023-menart-differentially-private-non-convex-optimization_images/imageFile1063.png>)

N∗ ≤

+

![image 1064](<2023-menart-differentially-private-non-convex-optimization_images/imageFile1064.png>)

![image 1065](<2023-menart-differentially-private-non-convex-optimization_images/imageFile1065.png>)

![image 1066](<2023-menart-differentially-private-non-convex-optimization_images/imageFile1066.png>)

![image 1067](<2023-menart-differentially-private-non-convex-optimization_images/imageFile1067.png>)

6L0 F0L1dlog(n√ρ/β) n√ρ

2L0 log(n√ρ/β) √nρ1/4

1/2

![image 1068](<2023-menart-differentially-private-non-convex-optimization_images/imageFile1068.png>)

![image 1069](<2023-menart-differentially-private-non-convex-optimization_images/imageFile1069.png>)

![image 1070](<2023-menart-differentially-private-non-convex-optimization_images/imageFile1070.png>)

=⇒ N∗ =

+

.

![image 1071](<2023-menart-differentially-private-non-convex-optimization_images/imageFile1071.png>)

![image 1072](<2023-menart-differentially-private-non-convex-optimization_images/imageFile1072.png>)

![image 1073](<2023-menart-differentially-private-non-convex-optimization_images/imageFile1073.png>)

![image 1074](<2023-menart-differentially-private-non-convex-optimization_images/imageFile1074.png>)

Combining this bound with Eqn. (15) we have with probability at least 1 − 3β that,

L0 log(n√ρ/β) √nρ1/4

![image 1075](<2023-menart-differentially-private-non-convex-optimization_images/imageFile1075.png>)

![image 1076](<2023-menart-differentially-private-non-convex-optimization_images/imageFile1076.png>)

8F0L1 T

![image 1077](<2023-menart-differentially-private-non-convex-optimization_images/imageFile1077.png>)

 ∇F( ¯w;S) ≤ min

+

,

![image 1078](<2023-menart-differentially-private-non-convex-optimization_images/imageFile1078.png>)

![image 1079](<2023-menart-differentially-private-non-convex-optimization_images/imageFile1079.png>)

![image 1080](<2023-menart-differentially-private-non-convex-optimization_images/imageFile1080.png>)

6L0 F0L1dlog(n√ρ/β) n√ρ

1/2

![image 1081](<2023-menart-differentially-private-non-convex-optimization_images/imageFile1081.png>)

![image 1082](<2023-menart-differentially-private-non-convex-optimization_images/imageFile1082.png>)

+

+

![image 1083](<2023-menart-differentially-private-non-convex-optimization_images/imageFile1083.png>)

![image 1084](<2023-menart-differentially-private-non-convex-optimization_images/imageFile1084.png>)

L0√F0L1d n√ρ

![image 1085](<2023-menart-differentially-private-non-convex-optimization_images/imageFile1085.png>)

![image 1086](<2023-menart-differentially-private-non-convex-optimization_images/imageFile1086.png>)

F0L1 T

,

= O min

![image 1087](<2023-menart-differentially-private-non-convex-optimization_images/imageFile1087.png>)

![image 1088](<2023-menart-differentially-private-non-convex-optimization_images/imageFile1088.png>)

![image 1089](<2023-menart-differentially-private-non-convex-optimization_images/imageFile1089.png>)

4L0 log(n√ρ/β) n√ρ

3L0 log(n√ρ/β) √nρ1/4

![image 1090](<2023-menart-differentially-private-non-convex-optimization_images/imageFile1090.png>)

![image 1091](<2023-menart-differentially-private-non-convex-optimization_images/imageFile1091.png>)

+

![image 1092](<2023-menart-differentially-private-non-convex-optimization_images/imageFile1092.png>)

![image 1093](<2023-menart-differentially-private-non-convex-optimization_images/imageFile1093.png>)

![image 1094](<2023-menart-differentially-private-non-convex-optimization_images/imageFile1094.png>)

![image 1095](<2023-menart-differentially-private-non-convex-optimization_images/imageFile1095.png>)

L0 log(n√ρ/β) √nρ1/4

1/2

![image 1096](<2023-menart-differentially-private-non-convex-optimization_images/imageFile1096.png>)

![image 1097](<2023-menart-differentially-private-non-convex-optimization_images/imageFile1097.png>)

.

+

![image 1098](<2023-menart-differentially-private-non-convex-optimization_images/imageFile1098.png>)

![image 1099](<2023-menart-differentially-private-non-convex-optimization_images/imageFile1099.png>)

# E Regularized Lipschitz Optimization

In this section, we consider a function f˜(w;x) = f(w;x) + L˜1 w − w0 2, where w  → f(w;x) is L0Lipschitz, L˜1-weakly convex for all x ∈ X, and w0 ∈ Rd. It is well known that in such case, the function w  → f˜(w;x) is L˜1 strongly convex (see, e.g. [DD19a, BGM21]). We denote the corresponding empirical risk as F˜(w;S) = n1 ni=1 f(w;xi) + L˜1 w − w0 2.

![image 1100](<2023-menart-differentially-private-non-convex-optimization_images/imageFile1100.png>)

2 0d

The following result is a rate of O˜ L

L˜1n2ρ on excess empirical risk via Noisy Gradient Descent, Algorithm 4. Multiple works have investigated closely related settings [FKT20, AFKT21], but due to our speciﬁc requirements (i.e. unconstrained setting and only assuming convexity of the regularized loss function) we provide a more tailored result here.

![image 1101](<2023-menart-differentially-private-non-convex-optimization_images/imageFile1101.png>)

2 0T

2ρ log2 (2/β)

1t and σ2 = 4L

Theorem 9. Let ρ > 0. Algorithm 4 with T = n

d , ηt = L˜1

n2ρ satisﬁes ρ-zCDP. Further, with probability at least 1 − β, the excess empirical risk of its output, w¯, is bounded as,

![image 1102](<2023-menart-differentially-private-non-convex-optimization_images/imageFile1102.png>)

![image 1103](<2023-menart-differentially-private-non-convex-optimization_images/imageFile1103.png>)

![image 1104](<2023-menart-differentially-private-non-convex-optimization_images/imageFile1104.png>)

L20dlog (n2 log2 (2/β)/dβ) L˜1n2ρ

F˜( ¯w;S) − F˜(w∗;S) = O

(17)

![image 1105](<2023-menart-differentially-private-non-convex-optimization_images/imageFile1105.png>)

![image 1106](<2023-menart-differentially-private-non-convex-optimization_images/imageFile1106.png>)

Algorithm 4 Noisy Gradient Descent Require: Dataset S, zCDP paramter ρ, initial point w0 ∈ Rd, probability β, Lipschitz parameter L0, Weak

![image 1107](<2023-menart-differentially-private-non-convex-optimization_images/imageFile1107.png>)

convexity L˜1, step size sequence {ηt}t, number of iterations T, noise standard deviation σ.

- 1: for t = 1 ...T − 1 do
- 2: ξt ∼ N(0,σ2I)
- 3: wt+1 = ΠB

L0 2L˜1

![image 1108](<2023-menart-differentially-private-non-convex-optimization_images/imageFile1108.png>)

(w0) wt − ηt ∇F˜(w;S) + ξt

- 4: end for
- 5: Return w¯ = T(T2+1) Tt=1 twt


![image 1109](<2023-menart-differentially-private-non-convex-optimization_images/imageFile1109.png>)

![image 1110](<2023-menart-differentially-private-non-convex-optimization_images/imageFile1110.png>)

Proof. The privacy proof is based on the observation that, even though the function w  → f˜(w;x) may not be Lispchitz, the sensitivity of the gradient, in every iteration, is controlled, since it is a sum of a Lipschitz and (data-independent) regularizer. In particular, the sensitivity of gradient at every iteration is bounded by 2L

0

n . With the stated noise variance, applying the guarantee of Gaussian mechanism for zCDP and composition [BS16], completes the privacy analysis.

![image 1111](<2023-menart-differentially-private-non-convex-optimization_images/imageFile1111.png>)

The utility proof is based on standard high-probability convergence analysis of (S)GD for strongly convex optimization [HLR19]. We ﬁrst show that the unconstrained minimizer, w∗, lies in the constrained set B L0

(w0). From the optimality criterion for unconstrained convex optimization, we have that 2L˜1 w∗ − w0 =  ∇F(w∗;S) ≤ L0. This implies that w∗ − w0 ≤ L

![image 1112](<2023-menart-differentially-private-non-convex-optimization_images/imageFile1112.png>)

2L˜1

0

2L˜1. This also gives us that the function w  → F˜(w;S) is 2L0-Lipschitz over the constrained set.

![image 1113](<2023-menart-differentially-private-non-convex-optimization_images/imageFile1113.png>)

From Gaussian concentration [JNG+19], we have that, with probability, at least 1 − β/2, for all t ∈ [T], ξt ≤ dlog (2T/β)σ. Further, conditioned on the above, we have from Lemma 4 in [HLR19], that with

![image 1114](<2023-menart-differentially-private-non-convex-optimization_images/imageFile1114.png>)

probability at least 1 − β,

T

L0 L˜1

![image 1115](<2023-menart-differentially-private-non-convex-optimization_images/imageFile1115.png>)

ξt,wt − w∗ = O

dlog (2T/β)σ log (2/β)T .

![image 1116](<2023-menart-differentially-private-non-convex-optimization_images/imageFile1116.png>)

t=1

The rest of the analysis is repeating the proof of Theorem 3.1 in [HLR19]. We get,

T

L20 L˜1T

σ2dlog (2T/β) L˜1T

1 T(T + 1)

F˜( ¯w;S) − F˜(w∗;S) = O

ξt,wt − w∗

+

+

![image 1117](<2023-menart-differentially-private-non-convex-optimization_images/imageFile1117.png>)

![image 1118](<2023-menart-differentially-private-non-convex-optimization_images/imageFile1118.png>)

![image 1119](<2023-menart-differentially-private-non-convex-optimization_images/imageFile1119.png>)

t=1

![image 1120](<2023-menart-differentially-private-non-convex-optimization_images/imageFile1120.png>)

L20 L˜1T

σ2dlog(2T/β) L˜1T

L0 dlog (2T/β)σ log (2/β) L˜1T

= O

+

+

![image 1121](<2023-menart-differentially-private-non-convex-optimization_images/imageFile1121.png>)

![image 1122](<2023-menart-differentially-private-non-convex-optimization_images/imageFile1122.png>)

![image 1123](<2023-menart-differentially-private-non-convex-optimization_images/imageFile1123.png>)

L20dlog (n2 log2 (2/β)/dβ) L˜1n2ρ where the last step follows by setting of σ and T.

= O

![image 1124](<2023-menart-differentially-private-non-convex-optimization_images/imageFile1124.png>)

![image 1125](<2023-menart-differentially-private-non-convex-optimization_images/imageFile1125.png>)

![image 1126](<2023-menart-differentially-private-non-convex-optimization_images/imageFile1126.png>)

![image 1127](<2023-menart-differentially-private-non-convex-optimization_images/imageFile1127.png>)

![image 1128](<2023-menart-differentially-private-non-convex-optimization_images/imageFile1128.png>)

