---
type: source
kind: paper
title: Differentially Private Optimization with Sparse Gradients
authors: Badih Ghazi, Cristóbal Guzmán, Pritish Kamath, Ravi Kumar, Pasin Manurangsi
year: 2024
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/2404.10881v2
source_local: ../raw/2024-ghazi-differentially-private-optimization-sparse.pdf
topic: general-knowledge
cites:
---

arXiv:2404.10881v2[cs.LG]31Oct2024

Diﬀerentially Private Optimization with Sparse Gradients

Badih Ghazi1, Cristo´bal Guzm´n1,2, Pritish Kamath1, Ravi Kumar1, and Pasin Manurangsi1

1Google Research 2Institute for Mathematical and Computational Engineering, Faculty of Mathematics and School of Engineering, Pontiﬁcia Universidad Cato´lica de Chile

Abstract

Motivated by applications of large embedding models, we study diﬀerentially private (DP) optimization problems under sparsity of individual gradients. We start with new near-optimal bounds for the classic mean estimation problem but with sparse data, improving upon existing algorithms particularly for the high-dimensional regime. The corresponding lower bounds are based on a novel block-diagonal construction used in combination with existing DP mean estimation lower bounds. Next, we obtain pure- and approximate-DP algorithms with almost optimal rates for stochastic convex optimization with sparse gradients; the former represents the ﬁrst nearly dimension-independent rates for this problem. Furthermore, by introducing novel analyses of bias-reduction in mean estimation and randomly-stopped biased SGD we obtain nearly dimension independent rates for near stationary points for the empirical risk in nonconvex settings under approximate-DP.

# 1 Introduction

The pervasiveness of personally sensitive data in machine learning applications (e.g., advertising, public policy, and healthcare) has led to the major concern of protecting users’ data from their exposure. When releasing or deploying these trained models, diﬀerential privacy (DP) oﬀers a rigorous and quantiﬁable guarantee on the privacy exposure risk [19].

Consider neural networks whose inputs have categorical features with large vocabularies. These features can be modeled using embedding tables; namely, for a feature that takes K distinct values, we create trainable parameters w1,... ,wK ∈ Rk, and use wa as input to the neural network when the corresponding input feature is a. A natural outcome of such models is that the perexample gradients are guaranteed to be sparse; when the input feature is a, then only the gradient with respect to wa is non-zero. Given the prevalence of sparse gradients in practical deep learning applications, GPUs/TPUs that are optimized to leverage gradient sparsity are commercially oﬀered and widely used in industry [22, 43, 1, 25]. To leverage gradient sparsity, recent practical work has considered DP stochastic optimization with sparse gradients for large embedding models for diﬀerent applications including recommendation systems, natural language processing, and ads modeling [46, 21].

Despite its relevance and promising empirical results, there is limited understanding of the theoretical limits of DP learning under gradient sparsity. This gap motivates our work.

![image 1](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile1.png>)

![image 2](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile2.png>)

![image 3](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile3.png>)

![image 4](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile4.png>)

![image 5](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile5.png>)

Setting Upper bound Lower bound

![image 6](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile6.png>)

![image 7](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile7.png>)

![image 8](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile8.png>)

![image 9](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile9.png>)

![image 10](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile10.png>)

![image 11](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile11.png>)

![image 12](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile12.png>)

![image 13](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile13.png>)

![image 14](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile14.png>)

![image 15](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile15.png>)

![image 16](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile16.png>)

![image 17](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile17.png>)

![image 18](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile18.png>)

![image 19](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile19.png>)

√sd

√sd

εn (Thm. 3.2) 1 ∧ sln(d/εn(εn)) ∧

ε-DP 1 ∧ sεnlnd ∧

εn (Thm.

![image 20](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile20.png>)

![image 21](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile21.png>)

![image 22](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile22.png>)

![image 23](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile23.png>)

4.1) (ε,δ)-DP 1 ∧ (sln(d/s) ln(1/δ))

√

√

![image 24](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile24.png>)

![image 25](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile25.png>)

![image 26](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile26.png>)

![image 27](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile27.png>)

![image 28](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile28.png>)

![image 29](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile29.png>)

![image 30](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile30.png>)

![image 31](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile31.png>)

![image 32](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile32.png>)

1/4

1/4

d ln(1/δ)

d ln(1/δ)

εn (Thm. 3.4) 1 ∧ (sln(1/δ))

√εn ∧

√εn ∧

εn (Thm. 4.5)

![image 33](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile33.png>)

![image 34](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile34.png>)

![image 35](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile35.png>)

![image 36](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile36.png>)

![image 37](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile37.png>)

![image 38](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile38.png>)

![image 39](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile39.png>)

- Table 1: Rates for DP mean estimation with sparse data of unit ℓ2-norm. Bounds stated for constant success/failure probability, resp. We use a ∧ b to denote min(a,b). New results highlighted .

![image 40](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile40.png>)

![image 41](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile41.png>)

![image 42](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile42.png>)

Setting Guarantee

![image 43](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile43.png>)

![image 44](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile44.png>)

New Upper bound (sparse)

![image 45](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile45.png>)

Upper bound (non-sparse)

![image 46](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile46.png>)

![image 47](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile47.png>)

![image 48](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile48.png>)

![image 49](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile49.png>)

(ε,δ)-DP

![image 50](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile50.png>)

Cvx. ERM (sln(d) ln(1/δ))

![image 51](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile51.png>)

![image 52](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile52.png>)

1/4

![image 53](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile53.png>)

√εn ∧ Rε,δ (Thm. 7.1) Rε,δ SCO (sln(d) ln(1/δ))

![image 54](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile54.png>)

![image 55](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile55.png>)

![image 56](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile56.png>)

![image 57](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile57.png>)

![image 58](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile58.png>)

![image 59](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile59.png>)

![image 60](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile60.png>)

![image 61](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile61.png>)

1/4

![image 62](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile62.png>)

√εn ∧ Rε,δ + √1n (Thm. 7.6) Rε,δ + √1n

![image 63](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile63.png>)

![image 64](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile64.png>)

![image 65](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile65.png>)

![image 66](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile66.png>)

![image 67](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile67.png>)

![image 68](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile68.png>)

![image 69](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile69.png>)

![image 70](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile70.png>)

![image 71](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile71.png>)

ε-DP

![image 72](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile72.png>)

Cvx. ERM sln(εnd)

![image 73](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile73.png>)

![image 74](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile74.png>)

![image 75](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile75.png>)

1/3

∧ Rε (Thm. 7.1, 7.5) Rε

![image 76](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile76.png>)

![image 77](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile77.png>)

![image 78](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile78.png>)

![image 79](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile79.png>)

![image 80](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile80.png>)

SCO sln(εnd)

![image 81](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile81.png>)

![image 82](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile82.png>)

![image 83](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile83.png>)

1/3

∧ Rε + √1n (Thm. 7.6) Rε + √1n (ε,δ)-DP Emp. Grad. Norm (sln(d/s) ln

![image 84](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile84.png>)

![image 85](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile85.png>)

![image 86](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile86.png>)

![image 87](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile87.png>)

![image 88](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile88.png>)

![image 89](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile89.png>)

![image 90](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile90.png>)

![image 91](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile91.png>)

![image 92](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile92.png>)

![image 93](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile93.png>)

![image 94](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile94.png>)

3(1/δ))1/8

![image 95](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile95.png>)

(εn)1/4 ∧ Rε,δ 2/3 (Thm. 5.8) Rε,δ 2/3

![image 96](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile96.png>)

![image 97](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile97.png>)

![image 98](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile98.png>)

- Table 2: Rates for DP optimization with sparse gradients, compared to best-existing upper bounds in the non-sparse case. Bounds stated for constant success probability. Function parameters and polylog(n) factors omitted. Above Rε,δ = dln(1/δ)/[εn] and Rε = d/[εn]. Improvements


![image 99](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile99.png>)

![image 100](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile100.png>)

highlighted .

## 1.1 Our Results

We initiate the study of DP optimization under gradient sparsity. More precisely, we consider a stochastic optimization (SO) problem, min{FD(x) : x ∈ X}, where X ⊆ Rd is a convex set, and FD(x) = Ez∼D[f(x,z)], with f(·,z) enjoying some regularity properties, and D is a probability measure supported on a set Z. Our main assumption is gradient sparsity: for an integer 0 ≤ s ≤ d,

∀x ∈ X, z ∈ Z :  ∇f(x,z) 0 ≤ s ,

where y 0 denotes the number of nonzero entries of y. We also study empirical risk minimization (ERM), where given a dataset S = (z1,... ,zn) we aim to minimize FS(x) := n1 i∈[n] f(x,zi).

![image 101](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile101.png>)

Our results unearth three regimes of accuracy rates for the above setting: (i) the small dataset size regime where the optimal rate is constant, (ii) the large dataset size where the optimal rates are polynomial in the dimension and (iii) an intermediate dataset size regime characterized by a new high-dimensional rate1 (see Table 1 and Table 2, for precise rates). These results imply in particular that even for high-dimensional models, this problem is tractable under gradient sparsity. Without sparsity, these poly-logarithmic rates are unattainable in the light of known lower bounds [6].

![image 102](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile102.png>)

1We will generally refer to high-dimensional or nearly dimension-independent rates indistinguishably, meaning more precisely that the rates scale poly-logarithmically with the dimension.

In Section 3, we start with the fundamental task of ℓ2-mean estimation with sparse data (which reduces to ERM with sparse linear losses [6]). Here, we obtain new upper bounds (see Table 1). These rates are obtained by adapting the projection mechanism [35], with a convex relaxation that makes our algorithms eﬃcient. Note that for pure-DP, even our large dataset rate of

√

![image 103](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile103.png>)

sd/(εn) can be substantially smaller than the dense pure-DP rate of d/(εn) [6], whenever s ≪ d. For approximate-DP we also obtain a sharper upper bound by solving an ℓ1-regression problem of a noisy projection of the empirical mean over a random subspace. Its analysis combines ideas from compressed sensing [45] with sparse approximation via the Approximate Carathe´odory Theorem [36].

- In Section 4, we prove lower bounds that show the near-optimality of our algorithms. For pure-DP, we obtain a new lower bound of Ω(s log(d/s)/(nε)), which is based on a packing of sparse vectors. While this lower bound looks weaker than the standard Ω(d/(nε)) lower bound based on dense packings [23, 6], we design a novel bootstrapping via a block diagonal construction where each block contains a sparse lower bound as above. This, together with a padding argument [6], yields lower bounds for the three regimes of interest. For approximate-DP, we also use the block diagonal bootstrapping, where this time the blocks use classical ﬁngerprinting codes in dimension s [6, 39]. Our approximate-DP lower bounds, however, have a gap of ln(d/s)1/4 in the high-dimensional regime; we conjecture that the aforementioned compressed sensing-based upper bound is tight.
- In Section 5, we study DP-ERM with sparse gradients, under approximate-DP. We propose the use of stochastic gradient (SGD) with a mean estimation gradient oracle based on the results in Section 3. This technique yields nearly-tight bounds in the convex case (similar to ﬁrst row of Table 2), and for the nonconvex case the stationarity rates are nearly dimension independent (last row of Table 2). The main challenge here is the bias in mean estimation, which dramatically deteriorates the rates of SGD. Hence we propose a bias-reduction method inspired by the simulation literature [9]. This technique uses a random batch size in an exponentially increasing schedule and a telescopic estimator of the gradient which—used in conjunction with our DP mean estimation methods—provides a stochastic ﬁrst-order oracle that attains bias similar to the one of a full-batch algorithm, with moderately bounded variance. Note that using the full-batch in this case would lead to polynomially weaker rates; in turn, our method leverages the batch randomization to conduct a more careful privacy accounting based on subsampling and the fully-adaptive properties of DP [44]. The introduction of random batch sizes and the random evolution of the privacy budget leads to various challenges into analyzing the performance of SGD. First, we analyze a randomly stopped method, where the stopping time dictated by the privacy budget. Noting that the standard SGD analysis bounds the cumulative regret, which is a submartingale, we carry out this analysis by integrating ideas from submartingales and stopping times [37]. Second, this analysis only yields the desired rates with constant probability. Towards high-probability results, we leverage a private model selection [31] based on multiple runs of randomly-stopped SGD that exponentially boosts the success probability (details in Section 6).


In Section 7, we study further DP-SO and DP-ERM algorithms for the convex case. Our algorithms are based on regularized output perturbation with an ℓ∞ projection post-processing step. While this projection step is rather unusual, its role is clear from the analysis: it leverages the ℓ∞ bounds of noise addition, which in conjunction with convexity provides an error guarantee that also leverages the gradient sparsity. This algorithm is nearly-optimal for approximate DP. For pure-DP, the previous algorithm requires an additional smoothness assumption, hence we propose a second algorithm based on the exponential mechanism [33] run over a net of suitably sparse vectors. Neither of the pure-DP algorithms matches the lower bound for mean estimation (the gap in the exponent of the rate is of 1/6), but they attain the ﬁrst nearly dimension-independent rates for this problem.

## 1.2 Related Work

DP optimization is an extensively studied topic for over a decade (see [6, 7, 20], and the references therein). In this ﬁeld, some works have highlighted the role of model sparsity (e.g., using sparsitypromoting ℓ1-ball constraints) in near-dimension independent excess-risk rates for DP optimization, both for ERM and SCO [24, 40, 41, 4, 8, 15, 14]. These settings are unrelated to ours, as sparse predictors are typically related to dense gradients.

Another proposed assumption to mitigate the impact of dimension in DP learning is that gradients lie (approximately) in a low dimensional subspace [47, 26, 30, 29] or where dimension is substituted by a bound on the trace of the Hessian of the loss [32]. These useful results are unfortunately not applicable to our setting of interest, as we are interested in arbitrary gradient sparsity patterns for diﬀerent datapoints.

Substantially less studied is the role of gradient sparsity. Closely related to our work, Zhang et al. [46] studied approximate DP-ERM under gradient sparsity, with some stronger assumptions. Aside from an additional ℓ∞ bound on individual gradients, the following partitioning sparsity assumption is imposed: the dataset S can be uniformly partitioned into subsets S1,... ,Sm with a uniform gradient sparsity bound: for all k ∈ [m] and x ∈ X, z∈S

∇f(x,z) 0 ≤ c1. The work shows poly-logarithmic in the dimension rates, for both convex and nonconvex settings: for convex objectives the rate is polylogε√n(d), and in the nonconvex case is polylog√εn1/(4d). Our results only assume individual gradient sparsity, so on top of being more general, they are also faster and provably nearly optimal in the convex case. Another relevant work is Ghazi et al. [21], which studies the computational and utility beneﬁts for DP with sparse gradients in neural networks with embedding tables. With the caveat that variable selection on stochastic gradients is performed at the level of contributing buckets (i.e. rows of the embedding table), rather than on gradient coordinates, this work shows substantial improvements on computational eﬃciency and also on the resulting utility.

k

![image 104](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile104.png>)

![image 105](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile105.png>)

![image 106](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile106.png>)

![image 107](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile107.png>)

In Asi et al. [3], bias-reduction is used to mitigate the regularization bias in SCO. While they also borrow inspiration from [9], both their techniques and scope of their work are unrelated to ours.

## 1.3 Future Directions

Our work provides a number of structural results on DP optimization with sparse gradients. We hope these results inspire further research in this area, thus we highlight some open questions.

First, we conjecture that for approximate-DP mean estimation—similarly to the pure-DP casea lower bound Ω s log(d/s)ln(1/δ)/[nε] should exist; such construction could be bootstrapped with a block-diagonal dataset for a tight lower bound (Lemma 4.3). Second, for pure DP-SCO, we believe there should exist an algorithm attaining rates analog to those for mean estimation. Unfortunately, most of variants of output perturbation (including phasing [20, 4, 5]) cannot attain such rates. From a practical perspective, the main open question is whether our rates may be attained without prior knowledge of s; note that all our mean estimation algorithms (which carries over to our optimization results) depend crucially on knowledge of this parameter. While we can treat s as a hyperparameter, it would be highly beneﬁcial to design algorithms that automatically adapt to it.

![image 108](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile108.png>)

We believe our bias-reduction is of broader interest. For example, [28, 34] have shown strong negative results about bias in DP mean estimation. While similar lower bounds may hold for sparse estimation, bias-reduction allows us to amortize this error within an iterative method, preventing error accumulation.

Finally, there is no evidence of our nonconvex rate being optimal. While it is known that in

the dense case noisy SGD is not optimal [2], known acceleration approaches are based on variance reduction, which appears to be incompatible with our bias-reduction.

# 2 Notation and Preliminaries

In this work, · = · 2 is the standard Euclidean norm on Rd. We will also make use of ℓp-norms, where x p := j∈[d] |xj|p 1/p for 1 ≤ p ≤ ∞. For p = 0, we use the notation

x 0 = |{j ∈ [d] : xj = 0}|, i.e., the cardinality of the support of x. We denote the r-radius ball

centered at x of the p-norm in Rd by Bpd(x,r) := {y ∈ Rd : y − x p ≤ r}. Given s ∈ [d] and L > 0, the set of s-sparse vectors is (the scaling factor L is omitted in the notation for brevity)

Ssd := {x ∈ Rd : x 0 ≤ s, x 2 ≤ L}. (1) Note that Jensen’s inequality implies: if x 0 ≤ s and 1 ≤ p < q ≤ ∞, then x p ≤ s1/p−1/q x q.

Remark 2.1. The upper bound results in this paper hold even if we replace the set Ssd of sparse vectors by the strictly larger ℓ1 ball B1d(0,L√s) (inclusion follows from the aforementioned inequality). Note that while our upper bounds extend to the ℓ1 assumption above, our lower bounds work under the original sparsity assumption.

![image 109](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile109.png>)

Let f : X × Z  → R be a loss function. The function evaluation f(x,z) represents the loss incurred by hypothesis x ∈ X on datapoint z ∈ Z. In stochastic optimization (SO), we consider a data distribution D, and our goal is to minimize the expected loss under this distribution

minx∈X FD(x) := Ez∼D[f(x,z)] . (SO)

Throughout, we use x∗(D) to denote an optimal solution to (SO), which we assume exists. We note in passing that existence of such optimal solution is guaranteed when X is compact, but otherwise additional work is needed to assert such existence; on the other hand, if multiple optimal solutions exist, we can choose an arbitrary one (e.g., a minimal norm solution). In the empirical risk minimization (ERM) problem, we consider sample datapoints S = (z1,... ,zn) and our goal is to minimize the empirical error with respect to the sample

minx∈X FS(x) := n1 i∈[n] f(x,zi) . (ERM)

![image 110](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile110.png>)

We denote by x∗(S) an arbitrary optimal solution to (ERM), which we assume exists. Even when S is drawn i.i.d. from D, solutions (or optimal values) of (SO) and (ERM) do not necessarily coincide.

We present the deﬁnition of diﬀerential privacy (DP), deferring useful properties and examples to Appendix A. Let Z be a sample space, and X an output space. A dataset is a tuple S ∈ Zn, and datasets S,S′ ∈ Zn are neighbors (denoted as S ≃ S′) if they diﬀer in only one of their entries.

Deﬁnition 2.2 (Diﬀerential Privacy). Let A : Zn  → X. We say that A is (ε,δ)-(approximately) diﬀerentially private (DP) if for every pair S ≃ S′, we have for all E ⊆ X that

Pr[A(S) ∈ E] ≤ eε · Pr[A(S′) ∈ E] + δ. When δ = 0, we say that A is ε-DP or pure-DP.

The privacy and accuracy of some of the perturbation based methods we use to privatize our algorithms are based on the following simple facts (see e.g. [19]).

- Fact 2.3 (Laplace & Gaussian mechanisms). For all g : Zn  → Rd

- (a) If ℓ1-sensitivity of g is bounded, i.e., ∆g1 := supS≃S′ g(S) − g(S′) 1 < +∞, then AgLap(S) := g(S) + ξ where ξ ∼ Lap⊗d(∆g1/ε) is ε-DP.
- (b) If ℓ2-sensitivity of g is bounded, i.e., ∆g2 := supS≃S′ g(S) − g(S′) 2 < +∞, then AgN(S) :=


g(S) + ξ, where ξ ∼ N 0,σ2I for σ ≥ ∆

g 2

√

![image 111](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile111.png>)

2 log(1.25/δ)

![image 112](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile112.png>)

ε is (ε,δ)-DP.

- Fact 2.4 (Laplace & Gaussian concentration). Let σ > 0 and 0 < β < 1.


- (a) For ξ ∼ Lap(σ)⊗d: (i) ξ ∞ σ log(d/β) holds with probability 1 − β, and (ii) ξ 2

σ

√

![image 113](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile113.png>)

d log(d/β) holds with probability 1 − β.

- (b) For ξ ∼ N(0,σ2I), (i) ξ ∞ σ log(d/β) holds with probability 1 − β, (ii) ξ 2 σ


√

![image 114](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile114.png>)

![image 115](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile115.png>)

d + log(1/β) holds with probability 1 − β, and (iii) E ξ 22 = dσ2.

![image 116](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile116.png>)

# 3 Upper Bounds for DP Mean Estimation with Sparse Data

We ﬁrst study DP mean estimation with sparse data. Our ﬁrst result is that the projection mechanism [35] is nearly optimal, both for pure- and approximate-DP. In our case, we interpret the marginals on each of the d dimensions as the queries of interest: this way, the ℓ2-error on private query answers corresponds exactly to the ℓ2-norm estimation error. A key diﬀerence to the approach in [35] and related works is that we project the noisy answers onto the set K := B1d(0,L√s), which is a (coarse) convex relaxation of conv(Ssd). This is crucial to make our algorithm eﬃciently implementable.

![image 117](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile117.png>)

![image 118](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile118.png>)

- Algorithm 1 Projection Mechanism(¯z(S),ε,δ,n) Require: Vector z¯(S) = n1 ni=1 zi from dataset S ∈ (Ssd)n; ε,δ ≥ 0, privacy parameters


![image 119](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile119.png>)

![image 120](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile120.png>)

![image 121](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile121.png>)

√s

 

![image 122](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile122.png>)

Lap(σ)⊗d with σ = 2L

nε if δ = 0, N(0,σ2I) with σ2 = 8L

![image 123](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile123.png>)

z˜ = z¯(S) + ξ, with ξ ∼

2 ln(1.25/δ)

(nε)2 if δ > 0. return zˆ = argmin{ z − z˜ 2 : z ∈ K}, where K := B1d(0,L√s)



![image 124](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile124.png>)

![image 125](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile125.png>)

![image 126](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile126.png>)

- Lemma 3.1. In Algorithm 1, it holds that z ˆ − z¯(S) 2 ≤ 2L ξ ∞√s, almost surely. Proof. From the properties of the Euclidean projection, we have


![image 127](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile127.png>)

![image 128](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile128.png>)

z ˆ − z¯(S),zˆ − z˜ ≤ 0. (2) Hence,

(2)

z ˆ − z¯(S) 22 = z ˆ − z¯(S),zˆ − z˜ + z ˆ − z¯(S),ξ

≤ z ˆ − z¯(S),ξ ≤ 2 · max

u 1 · ξ ∞ = 2L ξ ∞√s,

![image 129](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile129.png>)

u,ξ ≤ 2 · max

u∈K

u∈K

where we used the fact that conv(Ssd) ⊆ K. We now provide the privacy and accuracy guarantees of Algorithm 1.

![image 130](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile130.png>)

![image 131](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile131.png>)

![image 132](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile132.png>)

![image 133](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile133.png>)

- Theorem 3.2. For δ = 0, Algorithm 1 is ε-DP, and with probability 1 − β:

z ˆ − z¯(S) 2 L · min

√

![image 134](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile134.png>)

sd ln(d/β)

![image 135](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile135.png>)

nε , sln(nεd/β) .

![image 136](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile136.png>)

![image 137](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile137.png>)

Proof. First, the privacy follows from the ℓ1-sensitivity bound of the empirical mean

∆1 = supS≃S′ z ¯(S) − z¯(S′) 1 = n1 supz,z′∈Ssd

![image 138](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile138.png>)

z − z′ 1 ≤ 2L

√s n ,

![image 139](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile139.png>)

![image 140](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile140.png>)

- together with Fact 2.3(a). For the accuracy, the ﬁrst term follows from Fact 2.4(a)-(ii), and the fact that Euclidean

projection does not increase the ℓ2-estimation error, and the second term follows from Lemma 3.1 with the fact that ξ ∞ ≤ O L

√s nε · log(d/β) holds with probability at least 1−β, by Fact 2.4(a)-

![image 141](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile141.png>)

![image 142](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile142.png>)

- (i).

![image 143](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile143.png>)

![image 144](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile144.png>)

![image 145](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile145.png>)

![image 146](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile146.png>)

Theorem 3.3. For δ > 0, Algorithm 1 is (ε,δ)-DP, and with probability 1 − β:

z ˆ − z¯(S) 2 L · min (

√

![image 147](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile147.png>)

d+

√

![image 148](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile148.png>)

log(1/β))

√

![image 149](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile149.png>)

ln(1/δ)

![image 150](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile150.png>)

nε , (slog(1/δ) log(d/β))

1/4

![image 151](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile151.png>)

√nε .

![image 152](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile152.png>)

Proof. The privacy guarantee follows from the ℓ2-sensitivity bound of the empirical mean, ∆2 = 2nL, together with Fact 2.3(b). For the accuracy, the ﬁrst term in the minimum follows from Fact 2.4(b)-

![image 153](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile153.png>)

- (ii), and the fact that Euclidean projection does not increase the ℓ2-estimation error. The second term follows from Lemma 3.1 and Fact 2.4(b)-(ii).




- Theorem 3.4. If 6exp{−cm} ≤ δ < sln(md/s2 ) (where c > 0 is a constant) and 0 < ε ≤ 1, then


![image 154](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile154.png>)

![image 155](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile155.png>)

![image 156](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile156.png>)

![image 157](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile157.png>)

## 3.1 Sharper Approximate DP Mean Estimation via Compressed Sensing

We propose Algorithm 2, a more accurate method for approximate-DP mean estimation based on compressed sensing [45]. The precise improvements relate to reducing the log(d) factor to log(d/s), and a faster rate dependence on the conﬁdence β. The idea is that for suﬃciently high dimensions a small number of random measurements suﬃces to estimate a noisy and approximately sparse signal. These properties follow from existing results in compressed sensing, which provide guarantees based on the ℓ2-norm of the noise, and the best sparse approximation in the ℓ2-norm (known as ℓ2-ℓ2-stable and noisy recovery) [45]. We will exploit such robustness in two ways: regarding the noise robustness, this property is used in order to perturb our measurements, which will certify the privacy; on the other hand, the approximate recovery property is used to ﬁnd a sparser approximation of our empirical mean. As the approximation is only used for analysis, we can resort on the Approximate Caratheodory Theorem to certify the existence of a sparse vector whose sparsity increases more moderately with n than the empirical average [36].

An interesting feature of this algorithm is that ℓ1-minimization promotes sparse solutions, and thus we expect our output to be approximately sparse: this is not a feature that we particularly exploit, but it may be relevant for computational and memory considerations. Furthermore, note that the ℓ1-minimization problem does not require exact optimality for the privacy guarantee, hence approximate solvers can be used without compromising the privacy.

![image 158](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile158.png>)

- Algorithm 2 is (ε,δ)-DP, and with probability 1 − δ/2 − β,


√

![image 159](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile159.png>)

![image 160](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile160.png>)

![image 161](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile161.png>)

![image 162](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile162.png>)

(s ln(d/s)ln(1/δ))1/4 √nε

(

d + ln(1/β)) ln(1/δ) nε

ln(1/β)ln(1/δ) nε

z ˆ−z¯(S) 2 Lmin

. (3)

+

,

![image 163](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile163.png>)

![image 164](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile164.png>)

![image 165](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile165.png>)

![image 166](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile166.png>)

![image 167](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile167.png>)

Algorithm 2 Gaussian ℓ1-Recovery(¯z(S),ε,δ,n) Require: z¯(S) = n1 i∈[n] zi ∈ Rd from dataset S ∈ (Ss,d)n; privacy parameters ε,δ > 0

![image 168](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile168.png>)

![image 169](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile169.png>)

![image 170](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile170.png>)

- m nε sln(1ln(d/s/δ))


![image 171](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile171.png>)

 

2 ln(1.25/δ)

z¯(S) + ξ, where ξ ∼ N(0,σ2Id×d) and σ2 = 8L

(nε)2 , if d < mln2 m, z˜ · 1{ z˜ 2 ≤ 2L}, where z˜ = arg min{ z 1 : Az = b}, A ∼ (N(0, m1 ))m×d,

![image 172](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile172.png>)

return zˆ =

![image 173](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile173.png>)



2 ln(2.5/δ)

b = Az¯(S) + ξ and ξ ∼ N(0,σ2Im×m) with σ2 = 18L

(nε)2 , else

![image 174](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile174.png>)

![image 175](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile175.png>)

Moreover, we have the following second moment estimate,

E[ z ˆ − z¯ 22] L2 min

dln(1/δ) (nε)2

,

![image 176](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile176.png>)

![image 177](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile177.png>)

s ln(d/s)ln(1/δ) nε

![image 178](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile178.png>)

.

Proof. First, if d < mln2 m, Algorithm 2 is (ε,δ)-DP by privacy of Gaussian noise addition and the post-processing property of DP. Moreover, its (high-probability and second moment) accuracy guarantees are direct from Fact 2.4.

Next, if d ≥ mln2 m, we start with the privacy analysis. Let S ≃ S′ and suppose they only diﬀer in their i-th entry. We note that due to our choice of m, A is an approximate restricted isometry with probability 1 − 3exp{−cm} [16] (where c is the same as in the theorem statement); in particular, letting K √ nε

, we have that for all v ∈ Rd which is (sK)-sparse

![image 179](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile179.png>)

![image 180](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile180.png>)

s ln(d/s) ln(1/δ)

3 2

- 1

![image 181](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile181.png>)

- 2


v 2 ≤ Av 2 ≤

v 2. Hence, due to our assumption on δ, the event above has probability at least 1 − δ/2, and therefore A(¯z − z¯′) 2 =

![image 182](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile182.png>)

1 n

3L n

A(zi − zi′) 2 ≤

,

![image 183](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile183.png>)

![image 184](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile184.png>)

where we used the fact that zi − zi′ is (2s)-sparse. We conclude by the choice of σ2 that Az¯ + ξ is (ε,δ)-DP, and thus z˜ is (ε,δ)-DP by postprocessing.

We now proceed to the accuracy guarantee. By [45, Theorem 3.6 (b)], under the same event as stated above (which has probability 1 − δ/2) we have

z ˆ − z¯ 2 ξ 2 + inf

z: z 0≤sK

z − z¯ 2.

For the ﬁrst term, we use Gaussian norm concentration to guarantee that with probability 1 − β,

![image 185](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile185.png>)

ξ 2 √m + ln(1/β) σ Ks ln(d/s) + ln

![image 186](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile186.png>)

L ln(1/δ) nε

1 β

![image 187](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile187.png>)

![image 188](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile188.png>)

![image 189](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile189.png>)

.

![image 190](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile190.png>)

![image 191](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile191.png>)

For the second term, by the Approximate Cara´theodory Theorem [36], the inﬁmum above is upper bounded by O(L/

√

K); for this, note that z¯ lies in the convex hull of Ssd. Given our choice of K, we have that, with probability 1 − δ/2 − β

![image 192](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile192.png>)

![image 193](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile193.png>)

[s ln(d/s)ln(1/δ)]1/4 √nε

ln(1/β)ln(1/δ) nε

z ˆ − z¯ 2 L

.

+

![image 194](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile194.png>)

![image 195](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile195.png>)

![image 196](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile196.png>)

We conclude by providing the second moment estimate, by a simple tail integration argument. First, by the law of total probability, and letting E be the event of A being an approximate restricted isometry,

E z ˆ − z¯ 22 ≤ E[ z ˆ − z¯ 22|E] + 9L2δ, where we also used that z ˆ 2 ≤ 2L and z ¯ 2 ≤ L, almost surely. Now, conditionally on E, we have that letting α L[sln(d/s) ln(1/δ)]

1/4

√nε (below c > 0 is an absolute constant),

![image 197](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile197.png>)

![image 198](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile198.png>)

∞

E[ z ˆ − z¯ 22|E] =

P z ˆ − z¯ 2 ≥ u (2u)du

0

∞

α2 2

≤

P z ˆ − z¯ 2 − α ≥ τ 2(α + τ)dτ

+

![image 199](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile199.png>)

0

∞

c(nε)2 L2 ln(1/δ)

α2 2

τ2 (α + τ)dτ α2 2

2exp −

≤

+

![image 200](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile200.png>)

![image 201](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile201.png>)

0

![image 202](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile202.png>)

ln(1/δ) nε

ln(1/δ) (nε)2 α2,

+ L2

+ 2αL

![image 203](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile203.png>)

![image 204](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile204.png>)

![image 205](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile205.png>)

where in the second inequality we used the previous high-probability upper bound (here c > 0 is an absolute constant), and in the last step we used that nε > ln(1/δ). Finally, by our assumptions on δ, 9L2δ α2, this concludes the proof.

![image 206](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile206.png>)

![image 207](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile207.png>)

![image 208](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile208.png>)

![image 209](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile209.png>)

![image 210](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile210.png>)

# 4 Lower Bounds for DP Mean Estimation with Sparse Data

We provide matching lower bounds to those from Section 3. Moreover, although the stated lower bounds are for mean estimation, known reductions imply analogous lower bounds for DP-ERM and DP-SCO [6, 7]. First, for pure-DP we provide a packing-type construction based on sparse vectors. This construction is used in a novel block-diagonal construction, which provides the right low/high-dimensional transition. On the other hand, for approximate-DP, a block diagonal reduction with existing ﬁngerprinting codes [12, 39], suﬃces to obtain lower bounds that exhibit a nearly tight low/high-dimensional transition. For simplicity, we consider the case of L = 1, i.e. Ssd = {z ∈ Rd : z 0 ≤ s, z 2 ≤ 1}; it is easy to see that any lower bound scales linearly in L.

- 4.1 Lower Bounds for Pure-DP Our main lower bound for pure-DP mechanisms is as follows.


Theorem 4.1. Let ε > 0 and s < d/2. Then the empirical mean estimation problem over Ssd satisﬁes

√

![image 211](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile211.png>)

![image 212](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile212.png>)

P  A(S) − z¯(S) 2 min 1, slog(εnd/[εn]),

sd

εn 1.

inf A:ε-DP

sup

![image 213](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile213.png>)

![image 214](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile214.png>)

S∈(Ssd)n

The statement above—as well as those which follow—should be read as “for all DP algorithms A, there exists a dataset S, such that the mean estimation error is lower bounded by α(n,d,ε,δ) with probability at least β(n,d,ε,δ)” (where in this case α min 1, slog(εnd/[εn]),

√

![image 215](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile215.png>)

![image 216](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile216.png>)

sd

εn and β 1).

![image 217](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile217.png>)

![image 218](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile218.png>)

We also introduce a strengthening of the worst-case lower bound, based on hard distributions. Deﬁnition 4.2. We say that a probability µ over Zn induces an (α,β)-distributional lower bound for (ε,δ)-DP mean estimation if infA: (ε,δ)-DP PS∼µ,A  A(S) − z¯(S) 2 ≥ α ≥ β.

Note this type of lower bound readily implies a worst-case lower bound. On the other hand, while the existence of hard distributions follows by the existence of hard datasets (by Yao’s minimax principle), we provide explicit constructions of these distributions, for the sake of clarity. For the pure case, in Lemma A.3 we show that an adaptation of known packing-type lower bounds [23] provides distributional lower bounds for mean estimation, and for the approximate case, we note that ﬁngerprinting distributions induce distributional lower bounds, e.g. [13, 15, 27].

Theorem 4.1 follows by combining the two results that we provide next. First, and our main technical innovation in the sparse case is a block-diagonal dataset bootstrapping construction, which turns a low-dimensional lower bound into a high-dimensional one. While we state this result for norm-bounded sparse data, any family where low-dimensional instances can be embedded into the high-dimensional ones by padding with zeros would enjoy a similar property.

- Lemma 4.3 (Block-Diagonal Lower Bound Bootstrapping). Let n0,t ∈ N. Let µ be a distribution over (Sst)n0 that induces an (α0,ρ0)-distributional lower bound for (ε,δ)-DP mean estimation. Then,


, dt , there exists µ˜ over (Ssd)n that induces an (α,ρ)distributional lower bound for (ε,δ)-DP mean estimation, where α α0nn0√ρ0K and ρ ≥ 1 − exp(−ρ0/8).

for any d ≥ t, n ≥ n0 and K ≤ min n n

![image 219](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile219.png>)

![image 220](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile220.png>)

0

![image 221](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile221.png>)

![image 222](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile222.png>)

Proof. Consider an n × d data matrix D whose rows correspond to datapoints of a dataset S, and whose columns correspond to their d features. We will indistinctively refer to S or D as needed (these are equivalent representations of a dataset). This data matrix will be comprised of K diagonal blocks, D1,... ,DK; in particular, outside of these blocks, the matrix has only zeros. These blocks are sampled i.i.d. from the hard distribution µ given by hypothesis. Denote µ˜ the law of D. Let now z¯k(Dk) ∈ Rt be the mean (over rows) of dataset Dk. Then, the mean (over rows) of dataset D is given by

n0 n

z ¯1(D1) ... z ¯K(DK) ,

z¯(D) =

![image 223](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile223.png>)

where [z1|... |zK] ∈ Rd denotes the concatenation of z1,... ,zK (note that if K < d/t, then the concatenation above needs to be padded with (d − tK)-zeros, which we omit for simplicity). Let A be an (ε,δ)-DP algorithm, and let Ak its output on the k-th block variables, then

K

K

n20 n2

n0 n

n n0Ak(D) − z¯k(Dk)

2 2

2 2

 A(D) − z¯(D) 22 =

Ak(D) −

=

.

z¯k(Dk)

![image 224](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile224.png>)

![image 225](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile225.png>)

![image 226](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile226.png>)

k=1

k=1

Let now Bk(D) := nn

Ak(D), and note it is (ε,δ)-DP w.r.t. Dk (as it is DP w.r.t. D); further, by the independence of D1,... ,DK, we can condition on (Dh)h =k, to conclude that the squared ℓ2-error  Bk(D) − z¯k(Dk) 22 must be at least α20, with probability at least ρ0 (both on Dk and the internal randomness of Bk). Letting Yk := 1{ Bk(D)−z¯k(Dk) 2≥α0}, we have

![image 227](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile227.png>)

0

K

ρ0K 2

α0n0 n

2ρ0K 2 ≥ P

P  A(D) − z¯(D) 22 ≥

Yk ≥

.

![image 228](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile228.png>)

![image 229](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile229.png>)

![image 230](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile230.png>)

k=1

We will now use a coupling argument to lower bound the probability above. First, we let U1,... ,UK i.i.d.∼ Unif([0,1]), and Wk = 1{Ui≥ρ0} which are i.i.d.. On the other hand, we deﬁne

pk(y1,... ,yk−1) := P[Yk = 1|Y1 = y1,... ,Yk−1 = yk−1] Y˜k := 1{U

k≥pk(Y˜1,...,Y˜k−1)}.

Noting that Y =d Y˜, and that Y˜k ≥ Wk almost surely, due to the fact that pk ≥ ρ0 almost surely (which it follows from the ℓ2-error argument discussed above), we have

P

K

ρ0K 2

Yk ≥

![image 231](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile231.png>)

k=1

= P

K

ρ0K 2 ≥ P

Y˜k ≥

![image 232](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile232.png>)

k=1

K

ρ0K 2 ≥ 1 − exp(−ρ0/8),

Wk ≥

![image 233](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile233.png>)

k=1

where we used the one-sided multiplicative Chernoﬀ bound. Therefore,  A(D) − z¯(D) 22 α0nn0

2

ρ0K, with probability 1 − exp(−ρ0/8). We conclude that µ˜ induces a (α,ρ)-distributional lower bound for (ε,δ)-DP mean estimation, as claimed.

![image 234](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile234.png>)

![image 235](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile235.png>)

![image 236](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile236.png>)

![image 237](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile237.png>)

![image 238](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile238.png>)

The above result needs as input a base lower bound. Here, packing-based constructions suﬃce.

- Theorem 4.4. Let ε > 0 and s < d/2. Then there exists a (α,ρ)-distributional lower bound for ε-DP mean estimation over (Ssd)n with α min 1, slog(εnd/s) and ρ = 1/2. Proof. By Lemma A.1, there exists a set P of 1/√2-packing vectors on Csd with log(|P|) s log(d/s). Lemma A.3 thus implies the desired lower bound.

![image 239](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile239.png>)

![image 240](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile240.png>)

![image 241](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile241.png>)

![image 242](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile242.png>)

![image 243](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile243.png>)

![image 244](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile244.png>)

With all the building blocks in place, we now prove Theorem 4.1. Proof of Theorem 4.1. We divide the analysis into the diﬀerent regimes of sample size n. First, if n slog(εd/s), then Theorem 4.4 provides an Ω(1) lower bound.

![image 245](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile245.png>)

Next we consider the case slog(εd/s) n dε. For s ≤ t ≤ d to be determined, let n0 = slog(εt/s). We choose t so that dt n n

![image 246](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile246.png>)

![image 247](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile247.png>)

![image 248](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile248.png>)

![image 249](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile249.png>)

![image 250](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile250.png>)

0

: this can be attained by choosing t εn ds log εn d . This implies in the context of Lemma 4.3 that K = dt n n

![image 251](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile251.png>)

![image 252](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile252.png>)

![image 253](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile253.png>)

![image 254](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile254.png>)

0

. By Theorem 4.4, this implies a lower bound α0 1, with constant probability 1/2 for sparse mean estimation in dimension t. By Lemma 4.3, we conclude a sparse mean estimation lower bound of α0nn0 K2 √ 1K slog(εnd/nε) holds with constant probability.

![image 255](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile255.png>)

![image 256](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile256.png>)

![image 257](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile257.png>)

![image 258](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile258.png>)

![image 259](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile259.png>)

![image 260](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile260.png>)

![image 261](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile261.png>)

On the other hand, if n dε, let n∗ dε. By the previous paragraph, for datasets of size n∗ the following lower bound holds, Ω slog(εnd/εn∗ ∗) ds. For any n > n∗, by Lemma A.2, we have the lower bound Ω ds nn∗

![image 262](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile262.png>)

![image 263](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile263.png>)

![image 264](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile264.png>)

![image 265](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile265.png>)

![image 266](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile266.png>)

![image 267](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile267.png>)

![image 268](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile268.png>)

![image 269](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile269.png>)

![image 270](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile270.png>)

√

![image 271](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile271.png>)

sd

![image 272](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile272.png>)

εn holds with constant probability.

![image 273](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile273.png>)

![image 274](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile274.png>)

![image 275](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile275.png>)

![image 276](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile276.png>)

- 4.2 Lower Bounds for Approximate-DP


While the lower bound for the approximate-DP case is similarly based on the block-diagonal reduction, its base lower bound follows more directly from the dense case.

- Theorem 4.5. Let ε ∈ (0,1], 2−o(n) ≤ δ ≤ n1+Ω(1)1 . Then the empirical mean estimation problem over Ssd satisﬁes


![image 277](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile277.png>)

√

![image 278](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile278.png>)

1/4

d ln(1/δ)

P  A(S) − z¯(S) 2 min 1, [sln(1/δ)]

√nε ,

inf

sup

nε 1.

![image 279](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile279.png>)

![image 280](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile280.png>)

![image 281](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile281.png>)

A: (ε,δ)-DP

S∈(Ssd)n

![image 282](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile282.png>)

Proof. We divide the analysis into the diﬀerent regimes of sample size n. First, if n s ln(1/δ)/ε, then embedding an s-dimensional lower bound construction [13]2 and padding it with zeros for the remaining d − s features, provides an Ω(1) lower bound with constant probability.

![image 283](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile283.png>)

2While [13] only provides 1-dimensional distributional lower bounds for approximate DP mean estimation, it is easy to convert these into higher dimensional lower bounds, see e.g. [15, 27].

√

![image 284](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile284.png>)

Next, we consider the case s ln(1/δ)/ε n d

ln(1/δ) √sε . Let n0 = s ln(1/δ)/ε, t = s,

![image 285](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile285.png>)

![image 286](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile286.png>)

![image 287](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile287.png>)

![image 288](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile288.png>)

and K = nn

d s, where the last inequality holds by our regime assumption. The classic sdimensional mean estimation lower bound by [13] provides a α0 1 lower bound with constant probability. Hence by Lemma 4.3, the sparse mean estimation problem satisﬁes a lower bound

![image 289](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile289.png>)

![image 290](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile290.png>)

0

√

1/4

K √ 1K [sln(1/δ)]

Ω α0nn0

![image 291](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile291.png>)

√εn , with constant probability. We conclude with the ﬁnal range, n d

![image 292](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile292.png>)

![image 293](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile293.png>)

![image 294](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile294.png>)

![image 295](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile295.png>)

![image 296](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile296.png>)

√

√

![image 297](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile297.png>)

![image 298](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile298.png>)

ln(1/δ) √sε . First, letting n∗ d

ln(1/δ) √sε , we note that

![image 299](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile299.png>)

![image 300](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile300.png>)

![image 301](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile301.png>)

![image 302](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile302.png>)

this sample size falls within the range of the previous analysis, which implies a lower bound with constant probability of [sln(1/δ)]

√ √s

1/4 ε√n∗

![image 303](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile303.png>)

d. Now, if n > n∗, by Lemma A.2, we conclude that the following lower bound holds with constant probability, Ω

![image 304](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile304.png>)

![image 305](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile305.png>)

![image 306](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile306.png>)

![image 307](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile307.png>)

√

√ √s d

![image 308](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile308.png>)

d ln(1/δ)

![image 309](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile309.png>)

n∗ n

nε .

![image 310](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile310.png>)

![image 311](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile311.png>)

![image 312](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile312.png>)

![image 313](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile313.png>)

![image 314](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile314.png>)

![image 315](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile315.png>)

![image 316](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile316.png>)

![image 317](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile317.png>)

# 5 Bias-Reduction Method for DP-ERM with Sparse Gradients

We now start with our study of DP-ERM with sparse gradients. In this section and later, we will impose subsets of the following assumptions:

- (A.1) Initial distance: For SCO, x0 − x∗(D) ≤ D; for ERM, x0 − x∗(S) ≤ D.
- (A.2) Diameter bound: x − y ≤ D, for all x,y ∈ X.
- (A.3) Convexity: f(·,z) is convex, for all z ∈ Z.
- (A.4) Loss range: f(x,z) − f(y,z) ≤ B, for all x,y ∈ X, z ∈ Z.
- (A.5) Lipschitzness: f(·,z) is L-Lipschitz, for all z ∈ Z.
- (A.6) Smoothness: ∇f(·,z) is H-Lipschitz, for all z ∈ Z.
- (A.7) Individual gradient sparsity: ∇f(x,z) is s-sparse, for all x ∈ X and z ∈ Z.


The most natural and popular DP optimization algorithms are based on SGD. Here we show how to integrate the mean estimation algorithms from Section 3 to design a stochastic ﬁrst-order oracle that can be readily used by any stochastic ﬁrst-order method. The key challenge here is that estimators from Section 3 are inherently biased, which is known to dramatically deteriorate the convergence rates. Hence, we start by introducing a bias-reduction method.

## 5.1 Subsampled Bias-Reduced Gradient Estimator for DP-ERM

We propose Algorithm 3, inspired by a debiasing technique proposed in [9]. The idea is the following: we know that the Algorithm 2 would provide more accurate gradient estimators with larger sample sizes, and we will see that its bias improves analogously. We choose our batch size as a random variable with exponentially increasing range, and given such a realization we subtract the projection mechanism applied to the whole batch minus the same mechanism applied to both halves of this batch.3 This subtraction, together with a multiplicative and additive correction, results in the expected value of the outcome G(x) corresponding to the estimator with the largest batch size, leading to its expected accuracy being boosted by such large sample size, without necessarily utilizing such amount of data (in fact, the probability of such batch size being picked is polynomially smaller, compared to the smallest possible one). The caveat with this technique, as we will see, relates to a heavy-tailed distribution of outcomes, and therefore great care is needed for its analysis.

Instrumental to our analysis is the following truncated geometric distribution.

![image 318](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile318.png>)

3We follow the Blanchet-Glynn notation of O and E to denote the ‘odd’ and ‘even’ terms for the batch partition [9]; this partitioning is arbitrary.

![image 319](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile319.png>)

- Algorithm 3 Subsampled Bias-Reduced Gradient Estimator(x,S,N,ε,δ) Require: Dataset S = (z1,... ,zn) ∈ Zn, ε,δ > 0 privacy parameters, L-Lipschitz loss f(x,z) with

![image 320](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile320.png>)

![image 321](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile321.png>)

![image 322](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile322.png>)

![image 323](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile323.png>)

s-sparse gradient, x ∈ X, batch size parameter N ∼ TGeom(M) with M = ⌊log2(n)⌋ − 1 Let B ∼ Unif 2N n+1 , O,E a partition of B with |O| = |E| = 2N, I ∼ Unif([n]) G+N+1(x,B) = Gaussian ℓ1-Recovery(∇FB(x),ε/4,δ/4,2N+1) (Algorithm 2)

G−N(x,O) = Gaussian ℓ1-Recovery(∇FO(x),ε/4,δ/4,2N ) G−N(x,E) = Gaussian ℓ1-Recovery(∇FE(x),ε/4,δ/4,2N ) G0(x,I) = Gaussian ℓ1-Recovery(∇f(x,zI),ε/4,δ/4,1)

Return (below pk = P[TGeom(M) = k])

G(x) = p1

![image 324](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile324.png>)

N

G+N+1(x,B) − 12 G−N(x,O) + G−N(x,E) + G0(x,I)

![image 325](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile325.png>)

![image 326](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile326.png>)

![image 327](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile327.png>)

- Algorithm 4 Subsampled Bias-Reduced Sparse SGD(x0,S,ε,δ)


![image 328](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile328.png>)

![image 329](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile329.png>)

![image 330](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile330.png>)

![image 331](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile331.png>)

Require: Initialization x0 ∈ X; Dataset S = (z1,... ,zn) ∈ Zn; ε,δ, privacy parameters; stepsize η > 0; gradient oracle for L-Lipschitz and with s-sparse gradient loss f(·,z) t ← −1

![image 332](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile332.png>)

while 2ln 4δ ts−=01 3·2N16s+1n +1 2 + 2ε ts−=01 3·2N16s+1n +1 2 ≤ 21 and ts−=01 3·2N16s+1n +1 ≤ 41 do t ← t + 1 Nt ∼ TGeom(M) where M = ⌊log2(n)⌋ − 1 G(xt) = Subsampled Bias-Reduced Gradient Estimator(xt,S,Nt,ε/8,δ/4) (Alg. 3) xt+1 = ΠX xt − ηG(xt)

![image 333](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile333.png>)

![image 334](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile334.png>)

![image 335](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile335.png>)

![image 336](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile336.png>)

![image 337](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile337.png>)

![image 338](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile338.png>)

![image 339](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile339.png>)

![image 340](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile340.png>)

![image 341](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile341.png>)

![image 342](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile342.png>)

end while return

x ¯ = t+11 ts=0 xs if f(·,z) is convex , xtˆ where tˆ∼ Unif({0,... ,T}) iff(·,z) is not convex.

![image 343](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile343.png>)

![image 344](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile344.png>)

Deﬁnition 5.1. A random variable N has a truncated geometric distribution with parameter M ∈ N iﬀ its probability mass is supported on {0,... ,M}, with corresponding probabilities

CM/2k k ≤ M 0 k > M,

pk =

(4)

where CM = [2(1−2−(M+1))]−1 is the normalizing constant. Its law will be denoted by TGeom(M). Remark 5.2. Note that 1/2 ≤ CM ≤ 1. I.e., the normalizing constant of the truncated geometric distribution is uniformly bounded away from 0 and +∞.

We propose Algorithm 4, which interacts with the oracle given in Algorithm 3. For convenience, we will denote the random realization from the truncated geometric distribution used at iteration t by Nt. The idea is that, using the fully adaptive composition property of DP [44], we can run the method until our privacy budget is exhausted. Due to technical reasons, related to the biasreduction, we need to shift by one the termination condition in the algorithm. In particular, our algorithm goes over the reduced privacy budget of (ε/2,δ/2). The additional slack in the privacy budget guarantees that even with the extra oracle call the algorithm respects the privacy constraint.

- Lemma 5.3. Algorithm 4 is (ε,δ)-DP.


Proof. The proof is based on the fully adaptive composition theorem of diﬀerential privacy [44]. For this, we consider {At}t≥0, where A0(S) = (x0,N0) (here N0 the ﬁrst truncated geometric parameter), and inductively, At+1(At(S),S) for t ≥ 0 takes as input At(S) = (xt,Nt), computes G(xt) using the subsampled debiased gradient estimator (Algorithm 3), and performs a projected gradient step based on G(xt). Let Ht be the σ-algebra induced by (As)s=0,...,t.

Suppose now that At is (εt,δt)-DP, where (εt,δt) are Ht-measurable (we will later obtain these parameters), and let T := inf{t : ε[0:t] > ε/2, δ[0:t] > δ/2}, in the language of Theorem A.4 (notice that in the context of that theorem, we are choosing δ′ = δ′′ = δ/4). We ﬁrst claim that

(xt)t=0,...,T−1 is (ε/2,δ/2)-DP, which follows directly from Theorem A.4. Next, we will later show that εt ≤ ε/4 and δt ≤ δ/4, almost surely (this applies in particular to xT), and therefore by the composition property of DP, (xt)t≤T is (ε,δ)-DP.

Next, we provide the bounds on (εt,δt) required to conclude the proof. For this, we ﬁrst note that –conditionally on xt, Nt and Bt– the computation of G+N

(xt,Ot), G−N

t+1(xt,Bt), G−N

(xt,Et), is (3ε/32,3δ/16)-DP. Furthermore, by privacy ampliﬁcation by subsampling, this triplet of random variables is (ε′,δ′), with

t

t

2Nt+1 n

2Nt+1 n

2Nt+1 n

3ε 16

3δ 16

, δ′ =

ε′ = ln 1 +

(e3ε/32 − 1) ≤

,

![image 345](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile345.png>)

![image 346](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile346.png>)

![image 347](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile347.png>)

![image 348](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile348.png>)

![image 349](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile349.png>)

where we used above that ε ≤ 1. Similarly, we have that G0(x,I) is 16 εn, 16δn -DP. Therefore, by the basic composition theorem of DP, we have the following privacy parameters for the t-th

![image 350](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile350.png>)

![image 351](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile351.png>)

iteration of the algorithm εt = (3 · 2Nt+1 + 1)

δ 16n

ε 16n

, δt = (3 · 2Nt+1 + 1)

.

![image 352](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile352.png>)

![image 353](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile353.png>)

This proves in particular that (εt,δt) are Ht-measurable, and that εt ≤ ε/4, and δt ≤ δ/4 almost surely, which concludes the proof

![image 354](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile354.png>)

![image 355](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile355.png>)

![image 356](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile356.png>)

![image 357](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile357.png>)

## 5.2 Bias and Moment Estimates for the Debiased Gradient Estimator

We provide bias and second moment estimates for our debiased estimator of the empirical gradient. In summary, we show that this estimator has bias matching that of the full-batch gradient estimator, while at the same time its second moment is bounded by a mild function of the problem parameters.

√ √sln(d/s) ln(1/δ)

![image 358](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile358.png>)

- Lemma 5.4. Let d nε


. Algorithm 3, enjoys bias and second moment bounds

![image 359](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile359.png>)

![image 360](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile360.png>)

1/4

E[G(x) − ∇FS(x)|x] L[sln(d/s) ln(1/δ)]

√nε =: b, E[ G(x) 2|x] L

![image 361](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile361.png>)

![image 362](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile362.png>)

√

![image 363](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile363.png>)

2 ln(n)

s ln(d/s) ln(1/δ)

ε =: ν2. Proof. For simplicity, we assume without loss of generality that n is a power of 2, so that 2M+1 = n. Bias Let, for k = 0,... ,M, G+k+1(x) = E[G+N+1(x,B) | N = k,x], and

![image 364](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile364.png>)

G−k (x) = E[G−N(x,E) | N = k,x] = E[G−N(x,O) | N = k,x], where the last equality follows from the identical distribution of O and E. Noting further that G+k (x) = G−k (x) (which follows from the uniform sampling and the cardinality of the used datapoints), and using the law of total probability, we have

E[G(x) | x] = Mk=0 G+k (x) − G−k−1(x) + E[G0(x,I) | x]

= G+M+1(x) − G−0 (x) + E[G0(x,I) | x] = E[G+M+1(x) − ∇FS(x)|x] + ∇FS(x),

where we also used that E[G0(x,I) | x] = G−0 (x) (since I is a singleton). Next, by Theorem 3.4 E[G(x) | x] − ∇FS(x) ≤ E[G+M+1(x) − ∇FS(x)|x] L[sln(d/s) ln(1/δ)]

1/4

√nε . Second moment bound Using the law of total probability, and that O,E are a partition of B:

![image 365](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile365.png>)

![image 366](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile366.png>)

M

1 pk

E[ G(x) 2 | x] =

[G+N+1(x,B) − ∇FB(x)]

pkE

![image 367](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile367.png>)

k=0

- 1

![image 368](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile368.png>)

- 2pk


2

G−N(x,O) − ∇FO(x) + G−N(x,E) − ∇FE(x) + G0(x,I)

−

x,N = k

M

1 pk

2

≤ 2E[ G0(x,I) 2 | x] + 4

E G+N+1(x,B) − ∇FB(x)

x,N = k

![image 369](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile369.png>)

k=0

M

1 pk

2

2

+ G−N(x,E) − ∇FE(x)

E G−N(x,O) − ∇FO(x)

+

x,N = k .

![image 370](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile370.png>)

k=0

We now use Theorem 3.4, to conclude that

√

2

![image 371](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile371.png>)

2

s ln(d/s) ln(1/δ)

x,N = k L

E G+N+1(x,B) − ∇FB(x)

![image 372](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile372.png>)

2k+1ε maxA∈{O,E} E G−N(x,A) − ∇FA(x)

√

2

![image 373](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile373.png>)

2

s ln(d/s) ln(1/δ)

x,N = k L

![image 374](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile374.png>)

2kε E G0(x,I) 2 x L

√

![image 375](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile375.png>)

2

s ln(d/s) ln(1/δ)

ε . Recalling that M + 1 = log2 n and pk = 2−k, these bounds readily imply that E G(x) 2 ν2.

![image 376](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile376.png>)

![image 377](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile377.png>)

![image 378](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile378.png>)

![image 379](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile379.png>)

![image 380](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile380.png>)

## 5.3 Accuracy Guarantees for Subsampled Bias-Reduced Sparse SGD

The previous results provide useful information about the privacy, bias, and second-moment of our proposed oracle. Our goal now is to provide excess risk rates for DP-ERM. For this, we need to prove the algorithm runs for long enough, i.e., a lower bound on the stopping time of Algorithm 4,

T := inf t : 2ε < ε 2ln 4δ

![image 381](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile381.png>)

![image 382](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile382.png>)

t

s=0

3·2Ns+1+1 16n

![image 383](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile383.png>)

2 1/2

+ ε22

![image 384](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile384.png>)

t

3·2Ns+1+1

16n or 4δ <

![image 385](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile385.png>)

![image 386](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile386.png>)

s=0

t

(3·2Ns+1+1)δ

16n . (5)

![image 387](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile387.png>)

s=0

- 5.3.1 Lower Bounds on the Stopping Time


The proof of Lemma 5.4 implies that moments of G increase exponentially in M. This heavy-tailed behavior implies that T may not concentrate strongly enough to obtain high-probability lower bounds for T. What we will do instead is showing that with constant probability T behaves as desired.

To justify the approach, let us provide a simple in-expectation bound on how the privacy budget accumulates in the deﬁnition of T: letting εt = (3 · 2Nt+1 + 1)ε/[16n], we have that

t

2(t + 1)ε2 (16n)2

tε2 n

(t + 1)ε2 (16n)2

E (3 · 2N1+1 + 1)2 ≤

9E[22(N1+1)] + 1

ε2s =

,

E

![image 388](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile388.png>)

![image 389](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile389.png>)

![image 390](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile390.png>)

s=0

where in the last step we used that E 22(N1+1) = CM Mk=1+1 2k n. This in-expectation analysis can be used in combination with ideas from stopping times to establish bounds for T.

Lemma 5.5. Let 0 < δ < 1/n2. In the notation of Algorithm 4, let T be the stopping time deﬁned in eqn. (5). Then, there exists t = Cn/log(2/δ) (with C > 0 an absolute constant) such that

P[T ≤ t] ≤ 1/4. On the other hand,

n2 (n + 1)ln(4/δ) − 1 ≤ E[T] ≤

64n 9ln(4/δ)

.

![image 391](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile391.png>)

![image 392](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile392.png>)

Proof. Let A = ts−=01 3·2N16s+1n +1 2, and note that for t ≤ T + 1, A ≤ 1 almost surely. Then, we have that

![image 393](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile393.png>)

ε2 2

![image 394](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile394.png>)

![image 395](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile395.png>)

ε[0:t−1] = 2ln(4/δ)ε2A +

A ≤ 2ε 2ln(4/δ)A. Now, by eqn. (5) and the union bound,

![image 396](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile396.png>)

t−1

(3 · 2Nt+1 + 1) > 4n

![image 397](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile397.png>)

P[T ≤ t] ≤ P 2ε 2ln(4/δ)A > ε/2 + P

s=0

t−1

t−1

32n2 ln 4δ

3 · 2Nt+1 + 1 2 >

(3 · 2Nt+1 + 1) > 4n

≤ P

+ P

![image 398](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile398.png>)

![image 399](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile399.png>)

s=0

s=0

tln 4δ 16n2

t 4n

![image 400](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile400.png>)

9E[22(Nt+1)] + 1 +

≤

[6(M + 1) + 1]

![image 401](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile401.png>)

![image 402](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile402.png>)

tln 4δ 16n2

t 4n

![image 403](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile403.png>)

≤

[6log(n) + 1] ≤ 1/4,

[18n + 1] +

![image 404](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile404.png>)

![image 405](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile405.png>)

where the third step follows from Markov’s inequality and the fact that (Ns)s are i.i.d., and the last step follows from our choice of t = Cn/log(4/δ) with C > 0 suﬃciently small (here we use the fact that δ < 1/n2).

For the second part, we use that by the deﬁnition of T (eqn. (5))

![image 406](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile406.png>)

T

ε2 2

(3 · 2Ns+1 + 1)2 (16n)2

ε 2

4 δ

< 2ε2 ln

+

![image 407](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile407.png>)

![image 408](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile408.png>)

![image 409](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile409.png>)

![image 410](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile410.png>)

s=0

T

(3 · 2Ns+1 + 1)2 (16n)2 ∨

![image 411](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile411.png>)

s=0

=⇒ n2 < max 8ln

4 δ

![image 412](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile412.png>)

T

(3 · 2Ns+1 + 1)2 (16)2

,n

![image 413](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile413.png>)

s=0

T

3 · 2Ns+1 + 1 4

![image 414](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile414.png>)

s=0

T

3 · 2Ns+1 + 1 16n

1 4

<

![image 415](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile415.png>)

![image 416](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile416.png>)

s=0

Taking expectations and bounding the maximum by the sum allows us to use Wald’s identity as follows,

2(9n + 1) 162

3log(n) + 1 4 ≤ E[T + 1]ln

4 δ

n2 < E[T + 1] 8ln

+ n

![image 417](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile417.png>)

![image 418](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile418.png>)

![image 419](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile419.png>)

4 δ

(n + 1), which proves the claimed bound.

![image 420](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile420.png>)

The upper nound on E[T] is obtained similarly. Again, by eqn. (5), 32n2 ln(4/δ) ≥ E

T−1

9n 2

3 · 2Ns+1 + 1) 2 ≥ E[T]

.

![image 421](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile421.png>)

![image 422](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile422.png>)

s=0

Re-arranging terms provides the claimed lower bound.

![image 423](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile423.png>)

![image 424](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile424.png>)

![image 425](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile425.png>)

![image 426](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile426.png>)

- 5.3.2 Excess Empirical Risk in the Convex Setting


As a ﬁrst application, we study the accuracy guarantees of Algorithm 4 in the convex setting. We remark that these rates will be slightly weaker than those provided in Section 7, but this example is useful to illustrate the technique. Towards this goal, we analyze the cumulative regret of the algorithm, namely RT := Tt=0[FS(xt) − FS(x∗(S))]. Although this is a standard and well-studied object in optimization, we need to obtain bounds for this object when the stopping time T is random. The key observation here is that since T is a stopping time, the event {T ≥ t} is Ft−1measurable (here and throughout, Ft = σ((xs)s≤t) is the natural ﬁltration). This permits using our bias and second moment bounds similarly to the case where T is deterministic.4 Moreover, for the sake of analysis, we will consider Algorithm 4 as running indeﬁnitely, for all t ≥ 0. This would of course eventually violate privacy. However, since our algorithm stops at time T, then privacy is guaranteed as done earlier in this section.

Proposition 5.6. Let Rt := tt=0[FS(xt) − FS(x∗(S))], let T be the stopping time deﬁned in eqn. (5). Then

ην2 2

- 1

![image 427](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile427.png>)

- 2η


x0 − x∗(S) 2 + E[T + 1]

E[RT] ≤

+ Db ,

![image 428](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile428.png>)

where b and ν2 are deﬁned as in Lemma 5.4. Proof. By Proposition B.1 (see Appendix B),

E[RT] ≤ E

T

η 2 G(xt) 2 +  ∇F(xt) − G(xt),xt − x∗(S)

- 1

![image 429](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile429.png>)

- 2η


x0 − x∗(S) 2 +

![image 430](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile430.png>)

t=0

- 1

![image 431](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile431.png>)

- 2η


x0 − x∗(S) 2

= E

∞

η 2

E[1{T≥t} G(xt) 2|Ft−1] + E[1{T≥t} ∇F(xt) − G(xt),xt − x∗(S) |Ft−1]

+

![image 432](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile432.png>)

t=0

- 1

![image 433](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile433.png>)

- 2η


x0 − x∗(S) 2

= E

∞

η1{T≥t} 2

E[ G(xt) 2|Ft−1] + 1{T≥t}E[ ∇F(xt) − G(xt),xt − x∗(S) |Ft−1]

+

![image 434](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile434.png>)

t=0

where in the ﬁrst equality we used the tower property of the conditional expectation, and in the second equality we used that {T ≥ t} = {T ≤ t − 1}c is Ft−1-measurable.

Now, by Lemma 5.4, E[ ∇F(xt)−G(xt),xt−x∗(S) |Ft−1] ≤ Db and E[ G(xt) 2|Ft−1] ≤ ν2 (note that Ft−1 does not include the randomness of Nt, and therefore the bias and moment estimates as in the mentioned lemma hold), thus

- 1

![image 435](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile435.png>)

- 2η


E[RT] ≤

x0 − x∗(S) 2 + E[T + 1]

ην2 2

+ Db .

![image 436](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile436.png>)

![image 437](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile437.png>)

![image 438](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile438.png>)

![image 439](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile439.png>)

![image 440](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile440.png>)

We conclude with the constant probability guarantee for the biased and randomly stopped SGD, Algorithm 4.

![image 441](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile441.png>)

4This idea is related to the Wald identities [37]; however, we provide a direct analysis for the sake of clarity.

- Theorem 5.7. Consider a (SO) problem under convexity (Item (A.3)), initial distance (Item (A.1)), Lipschitzness (Item (A.5)) and gradient sparsity (Item (A.7)) assumptions. Let τ = ln(2C′/δn ), where C′ > 0 is an absolute constant. Let η = ν√Dτ , U = CD[ν√τ + bτ], where C > 0 is an absolute constant. Then Algorithm 4 satisﬁes

![image 442](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile442.png>)

![image 443](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile443.png>)

![image 444](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile444.png>)

![image 445](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile445.png>)

P FS(¯x) − FS(x∗(S)) ≤

U τ ≥ 1/2.

![image 446](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile446.png>)

Proof. We start by noting that

P FS(¯x) − FS(x∗(S)) >

U τ ≤ P {T ≤ τ} ∪ {RT > U} ≤ P T ≤ τ] + P[RT > U].

![image 447](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile447.png>)

For the ﬁrst event, by Lemma 5.5, we have that P[T ≤ τ] ≤ 1/4 (which determines C′). On the other hand, using Proposition 5.6 and Lemma 5.5, we have that for our choice of η, we have that

E[RT] ≤

Dν√τ 2

![image 448](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile448.png>)

![image 449](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile449.png>)

+ E[T + 1]D

ν 2√τ

![image 450](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile450.png>)

![image 451](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile451.png>)

+ b D[ν√τ + τb].

![image 452](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile452.png>)

In particular, for our choice of U (with C > 0 suﬃciently large),

P[RT > U] ≤

E[RT] U ≤

![image 453](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile453.png>)

1 4

![image 454](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile454.png>)

.

![image 455](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile455.png>)

![image 456](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile456.png>)

![image 457](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile457.png>)

![image 458](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile458.png>)

The above result implies a nearly optimal empirical excess risk rate for DP-SCO,

O LD

√

![image 459](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile459.png>)

ln n[s ln(d/s)ln3(1/δ)]1/4 √εn

![image 460](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile460.png>)

![image 461](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile461.png>)

,

but only with constant probability. We defer to the next section how to boost this guarantee to hold with arbitrarily high probability.

5.3.3 Near Stationary Points for the Empirical Risk

For nonconvex objectives it is known that obtaining vanishing excess risk is computationally difﬁcult. Hence, we study the more modest goal of approximating stationary points, i.e. points with small norm of the gradient. By combining known analyses of biased SGD with our bias-reduced oracle, we can establish bounds on the success probability of the algorithm.

- Theorem 5.8. Consider a (nonconvex) (SO) problem, under the following assumptions: Lipschitzness (Item (A.5)), smoothness (Item (A.6)), gradient sparsity (Item (A.7)), and the following initial suboptimality assumption: namely, that given our initialization x0 ∈ Rd, we know Γ > 0 such that


FS(x0) − FS(x∗(S)) ≤ Γ. (6) Let τ = ln(2C′/δn ) with C′ > 0 an absolute constant. Let η = HtνΓ 2 and U = C

√

![image 462](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile462.png>)

![image 463](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile463.png>)

ΓHτν + Lτb with C > 0 an absolute constant. Then Algorithm 4 satisﬁes P  ∇FS(xtˆ) 22 ≤ Uτ ≥ 1/2, and

![image 464](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile464.png>)

![image 465](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile465.png>)

![image 466](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile466.png>)

U τ

![image 467](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile467.png>)

√

ΓHL ln(n)ln(1/δ) + L2

![image 468](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile468.png>)

![image 469](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile469.png>)

[s ln(d/s)ln(1/δ)]1/4 √εn

.

![image 470](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile470.png>)

![image 471](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile471.png>)

Proof. First, given any U > 0, we have that

P  ∇FS(xtˆ) 2 >

![image 472](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile472.png>)

1 4

U τ ≤ P[T < τ] + P[T ∇FS(xtˆ) 22 > U] ≤

![image 473](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile473.png>)

![image 474](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile474.png>)

E[T ∇FS(xtˆ) 22] U

+

,

![image 475](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile475.png>)

where the last step follows by Lemma 5.5 and Chebyshev’s inequality, respectively. Next, by deﬁnition of tˆ and Proposition B.2 (see Appendix B.2),

T

E[(T + 1) ∇F(xtˆ) 22] = E

 ∇F(xt) 22

t=0

T

T

Γ η

ηH 2

 ∇F(xt),G(xt) − ∇F(xt)

 G(xt) 22 − E

≤

+

E

![image 476](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile476.png>)

![image 477](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile477.png>)

t=0

t=0

∞

∞

ηH 2

Γ η

E[1{T≥t} G(xt) 22] −

E[1{T≥t} ∇F(xt),G(xt) − ∇F(xt) ]

≤

+

![image 478](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile478.png>)

![image 479](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile479.png>)

t=0

t=0

∞

ηH 2

Γ η

P[T ≥ t]E E[ G(xt) 22|Ft−1]

≤

+

![image 480](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile480.png>)

![image 481](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile481.png>)

t=0

∞

P[T ≥ t]E E[ ∇F(xt),G(xt) − ∇F(xt)|Ft−1 ]

−

t=0

Γ η

ηH 2

E[T + 1]ν2 + E[T + 1]Lb √

≤

+

![image 482](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile482.png>)

![image 483](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile483.png>)

![image 484](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile484.png>)

ΓHτν + τLb,

where the third inequality holds since {T ≥ t} is Ft−1-measurable (see the proof of Proposition 5.6 for details), and the fourth inequality follows from Lemma 5.4, used the upper bound on E[T] from Lemma 5.5, and our choice for η. Selecting U = C

√

![image 485](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile485.png>)

ΓHτν + Lτb with C > 0 suﬃciently large,

we get E[T ∇F(xtˆ) 22]/U ≤ 1/4, concluding the proof. Proof. First, given any U > 0, we have that

![image 486](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile486.png>)

![image 487](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile487.png>)

![image 488](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile488.png>)

![image 489](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile489.png>)

P  ∇FS(xtˆ) 2 >

![image 490](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile490.png>)

U τ ≤ P[T < τ] + P[T ∇FS(xtˆ) 22 > U] ≤

1 4

![image 491](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile491.png>)

![image 492](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile492.png>)

E[T ∇FS(xtˆ) 22] U

+

,

![image 493](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile493.png>)

where the last step follows by Lemma 5.5 and Chebyshev’s inequality, respectively. Next, by

deﬁnition of tˆ and Proposition B.2 (see Appendix B.2),

T

E[(T + 1) ∇F(xtˆ) 22] = E

 ∇F(xt) 22

t=0

T

T

ηH 2

Γ η

 ∇F(xt),G(xt) − ∇F(xt)

 G(xt) 22 − E

≤

+

E

![image 494](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile494.png>)

![image 495](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile495.png>)

t=0

t=0

∞

∞

Γ η

ηH 2

E[1{T≥t} ∇F(xt),G(xt) − ∇F(xt) ]

E[1{T≥t} G(xt) 22] −

≤

+

![image 496](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile496.png>)

![image 497](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile497.png>)

t=0

t=0

∞

Γ η

ηH 2

P[T ≥ t]E E[ G(xt) 22|Ft−1]

≤

+

![image 498](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile498.png>)

![image 499](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile499.png>)

t=0

∞

P[T ≥ t]E E[ ∇F(xt),G(xt) − ∇F(xt)|Ft−1 ]

−

t=0

Γ η

ηH 2

E[T + 1]ν2 + E[T + 1]Lb √

≤

+

![image 500](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile500.png>)

![image 501](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile501.png>)

![image 502](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile502.png>)

ΓHτν + τLb,

where the third inequality holds since {T ≥ t} is Ft−1-measurable (see the proof of Proposition 5.6 for details), and the fourth inequality follows from Lemma 5.4, used the upper bound on E[T] from Lemma 5.5, and our choice for η. Selecting U = C

√

![image 503](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile503.png>)

ΓHτν + Lτb with C > 0 suﬃciently large, we get E[T ∇F(xtˆ) 22]/U ≤ 1/4, concluding the proof.

![image 504](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile504.png>)

![image 505](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile505.png>)

![image 506](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile506.png>)

![image 507](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile507.png>)

# 6 Boosting the Conﬁdence for the Bias-Reduced Stochastic Gradient Method

We conclude by providing a boosting method to amplify the success probability of our bias-reduced method. This private boosting method is a particular instance of a private selection method [31], and it is based on running a random number of independent runs of Algorithm 4 with noisy evaluations of their performance. Among the independent runs, we select the best performing one based on the noisy evaluations. This particular implementation sharpens some polylogarithmic factors that would appear for other private selection methods, such as Report Noisy Min [33, 19].

- Theorem 6.1. Let ε,δ > 0 such that δ ≤ ε/10. Then Algorithm 5 is (ε,δ)-DP. Let 0 < β < 1 and γ = min{1/2,3β/4}. In the convex case, Algorithm 5 attains excess risk


P FS(ˆx) − FS(x∗(S)) ≤ α ≥ 1 − β, where

√

ln n[s ln(d/s)ln3 ln(1/δ)/[βδ] ]1/4 √εn

![image 508](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile508.png>)

2 δ

1 β

B nε

α LD

ln

ln

. On the other hand, in the nonconvex case,

+

![image 509](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile509.png>)

![image 510](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile510.png>)

![image 511](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile511.png>)

![image 512](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile512.png>)

![image 513](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile513.png>)

P  ∇FS(ˆx) 2 ≤ α ≥ 1 − β, where

![image 514](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile514.png>)

√

[s ln(d/s)ln(ln(1/δ)/[βδ])]1/4 √εn

L nε

ln(1/δ) βδ

+ L2

![image 515](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile515.png>)

+

ln

ΓHL ln(n)ln

α

![image 516](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile516.png>)

![image 517](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile517.png>)

![image 518](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile518.png>)

![image 519](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile519.png>)

1 β

ln

![image 520](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile520.png>)

2 δ

![image 521](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile521.png>)

.

- Algorithm 5 Boosting Bias-Reduced SGD(S,ε,δ,K) Require: Dataset S ∼ Dn, ε,δ > 0 privacy parameters, random stopping parameter γ ∈ (0,1)


![image 523](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile523.png>)

![image 524](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile524.png>)

![image 525](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile525.png>)

K = γ1 ln 2δ for k = 1,... ,K do

![image 526](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile526.png>)

![image 527](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile527.png>)

Run Algorithm 4 with privacy budget (ε/12,(δ/[4K])2), xˆk its output and if f(·,z) convex then

Set sk = [FS(ˆxk) + ξk], where ξk ∼ Lap(λ), and λ = 12nεB. else

![image 528](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile528.png>)

Set sk = [ ∇FS(ˆxk) 2 + ξk], where ξk ∼ Lap(λ), and λ = 24nεL. end if Flip a γ-biased coin: with probability γ, return xˆ = xˆkˆ, where kˆ = arg minl≤k sl

![image 529](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile529.png>)

end for Return xˆ = xˆKˆ, where Kˆ = arg mink≤K sk

![image 530](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile530.png>)

Proof. The privacy analysis follows easily from [31]. First, by basic composition, we have that for each k the pair (ˆxk,sk) is (ε1,δ1)-DP, with ε1 = ε/6, and δ1 = (δ/[4K])2. By [31, Thm 3.4], the private selection with random stopping used in Algorithm 5 is such that xˆ is (3ε1+3√2δ1,√2δ1K+ δ/2)-DP; notice that

![image 531](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile531.png>)

![image 532](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile532.png>)

√

ε 2

δ

![image 533](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile533.png>)

![image 534](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile534.png>)

K ≤ ε, and

3ε1 + 3 2δ1 ≤

+ 3

2

![image 535](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile535.png>)

![image 536](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile536.png>)

![image 537](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile537.png>)

2δ1K + δ/2 ≤ δ, due to our choices of ε1,δ1. This proves that the algorithm is (ε,δ)-DP.

The accuracy of the algorithm closely follows [31, Theorem 3.3]. First, let κ be the number of runs the algorithm makes before stopping, and let α > 0 to be determined. Conditioning on κ

P FS(ˆx) − FS(x∗(S)) > α =

=

K

P FS(ˆx) − FS(x∗(S)) > α κ = k P[κ = k]

k=1

K

P FS(ˆx) − FS(x∗(S)) > α κ = k (1 − γ)k−1γ.

k=1

We will now bound the conditional probability above. By the subexponential tails of the Laplace distribution, we have that letting E := {(∀j ∈ [κ]) : |ξj| ≤ α′} (here, α′ > 0 is arbitrary),

nεα′ 12B

P[Ec|κ = k] = P (∃j ∈ [κ]) |ξk| > α′ κ = k ≤ 2k exp −

.

![image 538](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile538.png>)

Hence P FS(ˆx) − FS(x∗(S)) > α κ = k ≤ P FS(ˆx) − FS(x∗(S)) > α ∩ E κ = k + P[Ec|κ = k].

Next we have P FS(ˆx) − FS(x∗(S)) > α ∩ E κ = k ≤ P FS(ˆxkˆ) + ξkˆ − FS(x∗(S)) > α − α′ ∩ E κ = k

FS(ˆxk) + ξk − FS(x∗(S)) > α − α′ ∩ E κ = k ≤ P min

= P min

k∈[κ]

FS(ˆxk) − FS(x∗(S)) > α − 2α′ κ = k

k∈[κ]

k

≤ P FS(ˆx1) − FS(x∗(S)) > α − 2α′

, where in the last step we used that the runs are i.i.d.. We now choose α,α′ such that α−2α′ = U/τ (where U,τ are those from Theorem 5.7). Hence, P FS(ˆx) − FS(x∗(S)) > α κ = k ≤ 2−k + 2k exp −

nεα′ 12B

. We can now bound the failure probability as follows:

![image 539](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile539.png>)

K

P FS(ˆx) − FS(x∗(S)) > α ≤

k=1

- 1

![image 540](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile540.png>)

- 2


=

β 2

≤

![image 541](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile541.png>)

nεα′ 12B

2−k + 2K exp −

![image 542](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile542.png>)

(1 − γ)k−1γ

γ 1 − γ2

+

![image 543](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile543.png>)

2 γ

+

ln

![image 544](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile544.png>)

nεα′ 12B

2 γ

2 δ

exp −

ln

![image 545](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile545.png>)

![image 546](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile546.png>)

![image 547](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile547.png>)

nεα′ 12B

2 δ

exp −

,

![image 548](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile548.png>)

![image 549](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile549.png>)

where in the last step we used that γ = min{1/2,3β/4}. It is clear then that α′ = 12nεB ln 3 16β2 ln 2δ makes the probability above at most β. These choices lead to a ﬁnal bound

![image 550](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile550.png>)

![image 551](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile551.png>)

![image 552](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile552.png>)

√

ln n[s ln(d/s)ln3 ln(1/δ)/[βδ] ]1/4 √εn

![image 553](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile553.png>)

U τ

2 δ

B nε

1 β

+ 2α′ LD

α =

. For the nonconvex case, we need to replace B by 2L in the Laplace concentration bound.

+

ln

ln

![image 554](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile554.png>)

![image 555](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile555.png>)

![image 556](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile556.png>)

![image 557](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile557.png>)

![image 558](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile558.png>)

![image 559](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile559.png>)

Further, we consider the event { ∇F(ˆxk) 2 > α} (as opposed to the optimality gap event). This implies that we need to set α > 0 such that α − 2α′ ≥ U/τ from Theorem 5.8. This leads to

![image 560](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile560.png>)

K

nεγ 24L

(1 − γ)k−1γ.

2−k + 2K exp −

P FS(ˆx) 2 > α ≤

![image 561](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile561.png>)

k=1

The rest of the derivations are analogous.

![image 562](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile562.png>)

![image 563](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile563.png>)

![image 564](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile564.png>)

![image 565](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile565.png>)

# 7 DP Convex Optimization with Sparse Gradients via Regularized Output Perturbation

We conclude our work introducing another class of algorithms that attains nearly optimal rates for approximate-DP ERM and SO in the convex setting. These algorithms are based on solving a regularized ERM problem and privatizing its output by an output perturbation method. The main innovation of this technique is that we reduce the noise error by a · ∞-projection. This type of projection leverages the concentration of the noise in high-dimensions. We carry out an analysis that also leverages the convexity of the risk and the gradient sparsity to obtain these rates. The full description is included in Algorithm 6.

- Algorithm 6 Output Perturbation


![image 567](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile567.png>)

![image 568](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile568.png>)

Require: Dataset S = (z1,... ,zn) ∈ Zn, ε,δ ≥ 0 privacy params., f(·,z) L-Lipschitz convex function (if δ = 0 further assume H-smooth) with s-sparse gradient, λ ≥ 0 regularization param. Let x∗λ(S) = argminx∈X FSλ(x), where FSλ(x) := FS(x) + λ2 x 22

![image 569](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile569.png>)

√2sL λεn

 

![image 570](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile570.png>)

Lap(σ)⊗d with σ = 2

2H

λ + 1 if δ = 0, N(0,σ2I) with σ2 = 8L

![image 571](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile571.png>)

![image 572](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile572.png>)

x ˜ = x∗λ(S) + ξ, with ξ ∼

2 ln(1.25/δ)

[λεn]2 if δ > 0. return xˆ = argminx∈X x − x˜ ∞ (breaking ties arbitrarily)



![image 573](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile573.png>)

![image 574](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile574.png>)

## 7.1 DP-ERM via Output Perturbation

- Theorem 7.1. Consider an ERM problem under assumptions: initial distance (Item (A.1)), convexity (Item (A.3)), Lipchitzness (Item (A.5)) and gradient sparsity (Item (A.7)). Then, Algorithm 6 is (ε,δ)-DP, and it satisﬁes the following excess risk guarantees, for any 0 < β < 1:


- • If δ = 0, and under the additional assumption of smoothness (A.6) and unconstrained domain, X = Rd, then selecting λ = LD2H2 slog(εnd/β)

![image 575](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile575.png>)

![image 576](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile576.png>)

1/3

, it holds with probability 1 − β that

FS(ˆx) − FS(x∗(S)) L2/3H1/3D4/3 slog(εnd/β)

![image 577](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile577.png>)

1/3

.

- • If δ > 0 then selecting λ = DL · [slog(1/δ) log(d/β)]


1/4

√εn , we have with probability 1 − β that

![image 578](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile578.png>)

![image 579](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile579.png>)

![image 580](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile580.png>)

1/4

FS(ˆx) − FS(x∗(S)) LD · (slog(1/δ) log(d/β))

√εn .

![image 581](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile581.png>)

![image 582](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile582.png>)

Remark 7.2. For approximate-DP, the theorem above can also be proved if we replace assumption (Item (A.1)) by the diameter assumption (Item (A.2)). On the other hand, for the pure-DP case it is a natural question whether the smoothness assumption is essential. In Appendix 7.2, we provide a version of the exponential mechanism that works without the smoothness and unconstrained domain assumptions. This algorithm is ineﬃcient and it does require an structural assumption on the feasible set, but it illustrates the possibilities of more general results in the pure-DP setting.

Proof. We proceed by cases:

- • Case δ = 0. First, we prove that privacy of the algorithm. To do this, we ﬁrst establish a


bound on the ℓ1-sensitivity of the (quadratically) regularized ERM. Note that the ﬁrst-order optimality conditions in this case correspond to

1 λ∇FS(x∗λ(S)).

x∗λ(S) = −

![image 583](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile583.png>)

Therefore, if S ≃ S′, where S = (z1,... ,zn) and S = (z1′ ,... ,zn′ ) only diﬀer in one entry,

1 λ ∇FS(x∗λ(S)) − ∇FS′(x∗λ(S′)) 1

x∗λ(S) − x∗λ(S′) 1 ≤

![image 584](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile584.png>)

n

1 λn

 ∇f(x∗λ(S),zi) − ∇f(x∗λ(S′),zi′) 1

≤

![image 585](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile585.png>)

i=1

√

√

1 λn

2sH x∗λ(S) − x∗λ(S′) 2 + 2

![image 586](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile586.png>)

![image 587](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile587.png>)

(n − 1)

≤

2sL ≤

![image 588](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile588.png>)

√

√

n − 1 λn

1 λn

![image 589](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile589.png>)

![image 590](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile590.png>)

2sHL

2sL

4

+ 2

![image 591](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile591.png>)

![image 592](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile592.png>)

2√2sL λn

![image 593](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile593.png>)

2H λ

≤

+ 1 .

![image 594](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile594.png>)

![image 595](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile595.png>)

Above, in the third inequality we used the gradient sparsity (A.7), and the smoothness (A.6), assumptions. In the fourth inequality we used that the regularized ERM has ℓ2-sensitivity 4L

λn [10, 38, 18]. We conclude the privacy then by Fact 2.3(a). We also remark that by Fact 2.4(a)-(i), ξ ∞ L

![image 596](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile596.png>)

√s ln(d/β) λnε

![image 597](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile597.png>)

H λ + 1 , with probability 1 − β.

![image 598](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile598.png>)

![image 599](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile599.png>)

- • Case δ > 0. The privacy guarantee follows from the fact that the ℓ2-sensitivity of x∗λ(S) is 4L λn [10, 38, 18], together with Fact 2.3(b).


![image 600](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile600.png>)

√

![image 601](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile601.png>)

Moreover, by Fact 2.4(b)-(i), ξ ∞ L

ln(d/β) λnε , with probability 1 − β.

![image 602](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile602.png>)

We continue with the accuracy analysis, making a uniﬁed presentation for both pure and approximate DP. First, by the optimality conditions of the regularized ERM,

λ 2

FS(x∗λ(S)) − FS(x∗(S)) ≤

![image 603](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile603.png>)

x∗(S) 2 ≤

λ 2

D2. (7)

![image 604](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile604.png>)

We need the following key fact, which follows by the deﬁnitions of xˆ and x˜,

x ˆ − x∗λ(S) ∞ ≤ x ˆ − x˜ ∞ + x ˜ − x∗λ(S) ∞ ≤ 2 ξ ∞. (8) Using these two bounds, we proceed as follows

λ 2

λ 2

FS(ˆx) − FS(x∗(S)) ≤ FS(ˆx) − FS(x∗λ(S)) +

D2 ≤  ∇FS(ˆx),xˆ − x∗λ(S) +

D2

![image 605](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile605.png>)

![image 606](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile606.png>)

λ 2

≤  ∇FS(ˆx) 1 x ˆ − x∗λ(S) ∞ +

D2 ≤

![image 607](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile607.png>)

√

λ 2

D2,

![image 608](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile608.png>)

2sL ξ ∞ +

![image 609](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile609.png>)

where the second inequality follows by convexity of FS, and the fourth one by the gradient sparsity assumption and (8).

The conclusion follows by plugging in the respective bounds of λ and ξ ∞, for both pure and approximate DP cases.

![image 610](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile610.png>)

![image 611](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile611.png>)

![image 612](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile612.png>)

![image 613](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile613.png>)

## 7.2 A Pure DP-ERM Algorithm for Nonsmooth Losses

We now prove that the rates of pure DP-ERM in the convex case above can be obtained without the smoothness assumption, albeit with an ineﬃcient algorithm. This algorithm is based on the exponential mechanism, and it leverages the fact that the convex ERM with sparse gradient always has an approximate solution which is sparse. This result requires an additional assumption on the feasible set:

x ∈ X ∧ P ⊆ [d] =⇒ x|P ∈ X, (9)

where x|P ∈ Rd is the vector such that xP,j = xj if j ∈ P, and xP,j = 0 otherwise. We will say that X is sparsiﬁable if (9) holds. Note this property holds e.g. for ℓp-balls centered at the origin.

Lemma 7.3. Let X be a convex sparsiﬁable set. Consider the problem (ERM) under convexity (Item (A.3)), bounded diameter (Item (A.2)), Lipschitzness (Item (A.5)) and gradient sparsity (Item (A.7)), assumptions. If x∗(S) is an optimal solution of (ERM) and τ > 0, then there exists x˜ ∈ X such that x ˜ 0 ≤ 1/τ2, and

FS(˜x) − FS(x∗(S)) ≤ L√sτ. Proof. Let x˜ ∈ Rd be deﬁned as

![image 614](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile614.png>)

xj if |x∗S,j| ≥ τ 0 otherwise.

x˜j =

Note that x˜ ∈ X since x∗(S) ∈ X and X is sparsiﬁable. Now we note that

(x∗S,j)2 τ2 ≤

1 τ2

x ˜ 0 ≤

.

![image 615](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile615.png>)

![image 616](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile616.png>)

j: |x∗S,j|≥τ

Finally, for the accuracy guarantee, we use convexity as follows,

FS(˜x) − FS(x∗(S)) ≤  ∇FS(˜x),xˆ − x∗(S) ≤  ∇FS(˜x) 1 x ˜ − x∗(S) ∞ ≤ L√sτ,

![image 617](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile617.png>)

where in the last step we used that ∇f(ˆx,zi) ∈ Ssd and the deﬁnition of x˜.

![image 618](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile618.png>)

![image 619](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile619.png>)

![image 620](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile620.png>)

![image 621](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile621.png>)

We present now the sparse exponential mechanism, which uses the result above to approximately solve (ERM) with nearly dimension-independent rates.

![image 622](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile622.png>)

- Algorithm 7 Sparse_Exponential_Mechanism


![image 623](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile623.png>)

Require: Dataset S = {z1,... ,zn} ⊆ Z, ε privacy parameter, f(·,z) L-Lipschitz convex function with s-sparse gradients and range bounded by B, 0 < β < 1 conﬁdence parameter Let τ > 0 be such that ln(d/τ3[τβ]) = L

√sεn B

![image 624](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile624.png>)

![image 625](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile625.png>)

![image 626](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile626.png>)

2

Let Nτ be a τ-net of 1/τ2-sparse vectors over X with |Nτ| ≤ 1/τ d 2 τ 3 1/τ

![image 627](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile627.png>)

Let xˆ be a random variable supported on Nτ such that P[ˆx = x] ∝ exp − εnB FS(x) Return xˆ

![image 628](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile628.png>)

![image 629](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile629.png>)

Remark 7.4. The bound on |Nτ| claimed in Algorithm 7 follows from a standard combinatorial argument (e.g. [42]). Moreover, it follows that |Nτ| τ d

1/τ2

.

![image 630](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile630.png>)

- Theorem 7.5. Let X be a convex sparsiﬁable set. Consider a problem (ERM) under bounded diameter (Item (A.2)), convexity (Item (A.3)), bounded range (Item (A.4)), Lipschitzness (Item (A.5)) and gradient sparsity (Item (A.7)), assumptions. Then Algorithm 7 satisﬁes with probability 1 − β

FS(ˆx) − FS(x∗(S)) L2/3B1/3

s εn

![image 631](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile631.png>)

ln

L√sεn B

![image 632](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile632.png>)

![image 633](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile633.png>)

d β

![image 634](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile634.png>)

1/3

.

Proof. Let x˜ be the vector whose existence is guaranteed by Lemma 7.3. By the high-probability guarantee of the exponential mechanism [19] with probability 1 − β,

FS(ˆx) − FS(˜x) ≤

B εn

![image 635](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile635.png>)

ln |Nτ| + ln(1/β)

B εn

![image 636](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile636.png>)

ln τβ d τ2

![image 637](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile637.png>)

![image 638](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile638.png>)

. Hence, using Lemma 7.3 with the upper bound above,

FS(ˆx) − FS(x∗(S)) ≤ FS(ˆx) − FS(˜x) + FS(˜x) − FS(x∗(S))

B εn

![image 639](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile639.png>)

ln(d/[τβ]) τ2

![image 640](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile640.png>)

+ L√sτ

![image 641](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile641.png>)

L2B

s εn

![image 642](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile642.png>)

ln

L√sεn B

![image 643](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile643.png>)

![image 644](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile644.png>)

d β

![image 645](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile645.png>)

3 1/3

,

where we used our choice of τ.

![image 646](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile646.png>)

![image 647](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile647.png>)

![image 648](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile648.png>)

![image 649](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile649.png>)

7.3 DP-SCO via Output Perturbation

We note that the proposed output perturbation approach (Algorithm 6) leads to nearly optimal population risk bounds for approximate-DP, by a diﬀerent tuning of the regularization parameter λ.

- Theorem 7.6. Consider a problem (SO) under bounded initial distance (Item (A.1)) (or bounded diameter, Item (A.2), if δ > 0), convexity (Item (A.3)), Lipschitzness (Item (A.5)), bounded range (Item (A.4)), and gradient sparsity (Item (A.7)). Then, Algorithm 6 is (ε,δ)-DP, and for 0 < β < 1,


- • If δ = 0, and under the additional assumption of smoothness (A.6) and unconstrained domain, X = Rd. Selecting λ = LD2H2 slog(εnd/β)

![image 650](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile650.png>)

![image 651](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile651.png>)

1/3

, then with probability 1 − β

FS(ˆx) − FS(x∗(D)) L2/3H1/3D4/3 slog(εnd/β)

![image 652](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile652.png>)

1/3

+ B ln(1n/β).

![image 653](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile653.png>)

![image 654](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile654.png>)

- • If δ > 0. Selecting λ = DL ln(n) ln(1n /β) +


√

1/2

![image 655](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile655.png>)

s ln(1/δ) ln(d/β) εn

, then with probability 1 − β

![image 656](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile656.png>)

![image 657](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile657.png>)

![image 658](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile658.png>)

√

![image 659](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile659.png>)

1/4

lnn + B) ln(1n/β).

FD(ˆx) − FD(x∗(D)) LD[sln(1/δ) log(d/β)]

![image 660](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile660.png>)

√εn + (LD

![image 661](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile661.png>)

![image 662](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile662.png>)

![image 663](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile663.png>)

Remark 7.7. Note ﬁrst that in the proof below we are not addressing the privacy of Algorithm 6, as this has already been proven in Theorem 7.1.

On the other hand, note that the same proof below –using the in-expectation generalization guarantees of uniformly stable algorithms [10]– provides a sharper upper bound for the expected

excess risk for the pure and approximate DP cases, which would hold w.p. 1 − β over the algorithm internal randomness

s log(d/β) εn

1/3

ES[FD(ˆx) − FD(x∗(D))] L2/3H1/3D4/3

,

![image 664](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile664.png>)

[s ln(1/δ)log(d/β)]1/4 √εn

ES[FD(ˆx) − FD(x∗(D))] LD

.

![image 665](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile665.png>)

![image 666](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile666.png>)

Proof. Using the ℓ2-sensitivity of x∗λ(S), ∆2 = λn4L, we have the following generalization bound [11]: with probability 1 − β/2

![image 667](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile667.png>)

![image 668](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile668.png>)

ln β 1 n

L2 λn

1 β

![image 669](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile669.png>)

FD(x∗λ(S)) − FS(x∗λ(S))

ln(n)ln

=: γ.

+ B

![image 670](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile670.png>)

![image 671](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile671.png>)

![image 672](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile672.png>)

The bound of (7) can be obviously modiﬁed by comparison with the population risk minimizer, x∗(D): in particular, the event above5 implies that

λ 2

x∗(D) 22 + γ λD2 + γ.

FD(x∗λ(S)) − FD(x∗(D)) FS(x∗λ(S)) − FS(x∗(D)) + γ ≤

![image 673](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile673.png>)

On the other hand, the bound (8) works exactly as in the proof of Theorem 7.1. Hence, we have that with probability 1 − β/2,

FD(ˆx) − FD(x∗(D)) FD(ˆx) − FD(x∗λ(S)) + λD2 + γ  ∇FD(ˆx),xˆ − x∗λ(S) + λD2 + γ 2L√s ξ ∞ +

L2 λn

![image 674](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile674.png>)

1 β

B √n

1 β

+ λD2 +

![image 675](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile675.png>)

ln

ln(n)ln

,

![image 676](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile676.png>)

![image 677](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile677.png>)

![image 678](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile678.png>)

![image 679](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile679.png>)

![image 680](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile680.png>)

where in the last step we used that  ∇FD(ˆx) 1 = Ez[∇f(ˆx,z)] 1 ≤ Ez[ ∇f(ˆx,z) 1] ≤ L√s (the last step which follows by the gradient sparsity), inequality (8), and the deﬁnition of γ.

![image 681](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile681.png>)

We proceed now by separately studying the diﬀerent cases for δ:

- • Case δ = 0. The bound above becomes

FD(ˆx) − F(x∗(D))

L2 λn

![image 682](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile682.png>)

s ln(d/β) ε

![image 683](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile683.png>)

H λ

![image 684](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile684.png>)

+ 1 + ln nln(1/β) + λD2 + B

![image 685](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile685.png>)

ln(1/β) n

![image 686](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile686.png>)

. Our choice of λ provides the claimed bound.

- • Case δ > 0. Here, the upper bound takes the form


![image 687](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile687.png>)

![image 688](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile688.png>)

L2 λn

s ln(d/β)ln(1/δ) ε

ln(1/β) n

FD(ˆx) − F(x∗(D))

+ ln(n)ln(1/β) + λD2 + B

. The proposed value of λ leads to the bound below that holds with probability 1 − β,

![image 689](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile689.png>)

![image 690](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile690.png>)

![image 691](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile691.png>)

![image 692](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile692.png>)

![image 693](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile693.png>)

![image 694](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile694.png>)

s ln(1/δ)log(d/β)

ln(1/β) n

ln nln(1/β) n

FD(ˆx) − FD(x∗(D)) B

+ LD

+

![image 695](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile695.png>)

![image 696](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile696.png>)

![image 697](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile697.png>)

εn (LD

√

![image 698](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile698.png>)

[s ln(1/δ)log(d/β)]1/4 √εn

ln(1/β) n

![image 699](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile699.png>)

ln n + B)

+ LD

.

![image 700](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile700.png>)

![image 701](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile701.png>)

![image 702](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile702.png>)

![image 703](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile703.png>)

![image 704](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile704.png>)

![image 705](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile705.png>)

![image 706](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile706.png>)

![image 707](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile707.png>)

5We also need concentration to upper bound FS(x∗(D))−FD(x∗(D)). However, this is easy to do by e.g. Hoeﬀding’s inequality, leading to a bound γ.

# Acknowledgements

C.G.’s research was partially supported by INRIA Associate Teams project, ANID FONDECYT 1210362 grant, ANID Anillo ACT210005 grant, and National Center for Artiﬁcial Intelligence CENIA FB210017, Basal ANID.

# References

- [1] G. Amirkhanyan and B. Fontaine. Building large scale recommenders using cloud TPUs, 2022. https://cloud.google.com/blog/topics/developers-practitioners/building-large-scale-recommend
- [2] R. Arora, R. Bassily, T. Gonza´lez, C. A. Guzm´an, M. Menart, and E. Ullah. Faster rates of convergence to stationary points in diﬀerentially private optimization. In ICML, pages 1060–1092, 2023.
- [3] H. Asi, Y. Carmon, A. Jambulapati, Y. Jin, and A. Sidford. Stochastic bias-reduced gradient methods. In NeurIPS, 2021.
- [4] H. Asi, V. Feldman, T. Koren, and K. Talwar. Private stochastic convex optimization: Optimal rates in L1 geometry. In ICML, pages 393–403, 2021.
- [5] H. Asi, D. Le´vy, and J. C. Duchi. Adapting to function diﬃculty and growth conditions in private optimization. In NeurIPS, pages 19069–19081, 2021.
- [6] R. Bassily, A. D. Smith, and A. Thakurta. Private empirical risk minimization: Eﬃcient algorithms and tight error bounds. In FOCS, pages 464–473, 2014.
- [7] R. Bassily, V. Feldman, K. Talwar, and A. Guha Thakurta. Private stochastic convex optimization with optimal rates. In NeurIPS, 2019.
- [8] R. Bassily, C. Guzm´an, and A. Nandi. Non-Euclidean diﬀerentially private stochastic convex optimization. In COLT, pages 474–499, 2021.
- [9] J. H. Blanchet and P. W. Glynn. Unbiased monte carlo for optimization and functions of expectations via multi-level randomization. In WSC, pages 3656–3667, 2015.
- [10] O. Bousquet and A. Elisseeﬀ. Stability and generalization. JMLR, 2:499–526, 2002.
- [11] O. Bousquet, Y. Klochkov, and N. Zhivotovskiy. Sharper bounds for uniformly stable algorithms. In COLT, pages 610–626, 2020.
- [12] M. Bun, J. R. Ullman, and S. P. Vadhan. Fingerprinting codes and the price of approximate diﬀerential privacy. In STOC, pages 1–10, 2014.
- [13] M. Bun, T. Steinke, and J. R. Ullman. Make up your mind: The price of online queries in diﬀerential privacy. In SODA, pages 1306–1325, 2017.
- [14] T. T. Cai, Y. Wang, and L. Zhang. The cost of privacy in generalized linear models: Algorithms and minimax lower bounds. arXiv preprint arXiv:2011.03900, 2020.
- [15] T. T. Cai, Y. Wang, and L. Zhang. The cost of privacy: Optimal rates of convergence for parameter estimation with diﬀerential privacy. Ann. Stat., 49(5):2825 – 2850, 2021.


- [16] E. Candes and T. Tao. Decoding by linear programming. TOIT, 51(12):4203–4215, 2005.
- [17] E. J. Cande`s and M. A. Davenport. How well can we estimate a sparse vector? Applied and Computational Harmonic Analysis, 34(2):317–323, 2013.
- [18] K. Chaudhuri, C. Monteleoni, and A. D. Sarwate. Diﬀerentially private empirical risk minimization. JMLR, 12:1069–1109, 2011.
- [19] C. Dwork and A. Roth. The algorithmic foundations of diﬀerential privacy. Found. Trends Theor. Comput. Sci., 9(3-4):211–407, 2014.
- [20] V. Feldman, T. Koren, and K. Talwar. Private stochastic convex optimization: optimal rates in linear time. In STOC, pages 439–449, 2020.
- [21] B. Ghazi, Y. Huang, P. Kamath, R. Kumar, P. Manurangsi, A. Sinha, and C. Zhang. Sparsitypreserving diﬀerentially private training of large embedding models. In NeurIPS, 2023.
- [22] A. Gunny, C. Garg, L. Dolgovs, and A. Subramaniam. Accelerating wide & deep recommender inference on GPUs, 2019. https://developer.nvidia.com/blog/accelerating-wide-deep-recommender-inference-on-gpus.
- [23] M. Hardt and K. Talwar. On the geometry of diﬀerential privacy. In STOC, pages 705–714, 2010.
- [24] P. Jain and A. G. Thakurta. (near) dimension independent risk bounds for diﬀerentially private learning. In ICML, pages 476–484, 2014.
- [25] N. Jouppi, G. Kurian, S. Li, P. Ma, R. Nagarajan, L. Nai, N. Patil, S. Subramanian, A. Swing, B. Towles, et al. TPU v4: an optically reconﬁgurable supercomputer for machine learning with hardware support for embeddings. In ISCA, 2023.
- [26] P. Kairouz, M. R. Diaz, K. Rush, and A. Thakurta. (Nearly) Dimension Independent Private ERM with AdaGrad Rates via Publicly Estimated Subspaces. In COLT, pages 2717–2746, 2021.
- [27] G. Kamath and J. R. Ullman. A primer on private statistics. CoRR, abs/2005.00010, 2020. URL https://arxiv.org/abs/2005.00010.
- [28] G. Kamath, A. Mouzakis, M. Regehr, V. Singhal, T. Steinke, and J. Ullman. A bias-varianceprivacy trilemma for statistical estimation, 2023.
- [29] Y. T. Lee, D. Liu, and Z. Lu. The power of sampling: Dimension-free risk bounds in private erm, 2024. URL https://arxiv.org/abs/2105.13637.
- [30] X. Li, D. Liu, T. Hashimoto, H. Inan, J. J. Kulkarni, Y. T. Lee, and A. G. Thakurta. When does diﬀerentially private learning not suﬀer in high dimensions? In NeurIPS’22, November 2022.
- [31] J. Liu and K. Talwar. Private selection from private candidates. In STOC, pages 298–309, 2019.
- [32] Y.-A. Ma, T. V. Marinov, and T. Zhang. Dimension independent generalization of dp-sgd for overparameterized smooth convex optimization. arXiv preprint arXiv:2206.01836, 2022.


- [33] F. McSherry and K. Talwar. Mechanism design via diﬀerential privacy. In FOCS, pages 94–103, 2007.
- [34] A. Nikolov and H. Tang. Gaussian noise is nearly instance optimal for private unbiased mean estimation. arXiv preprint arXiv:2301.13850, 2023.
- [35] A. Nikolov, K. Talwar, and L. Zhang. The geometry of diﬀerential privacy: the sparse and approximate cases. In STOC, pages 351–360, 2013.
- [36] G. Pisier. Remarques sur un re´sultat non publie´ de b. maurey. Se´minaire Analyse fonctionnelle (dit, pages 1–12, 1981.
- [37] J. S. Rosenthal. A ﬁrst look at rigorous probability theory. World Scientiﬁc Publishing Co. Pte. Ltd., Hackensack, NJ, second edition, 2006. ISBN 978-981-270-371-2; 981-270-371-3.
- [38] S. Shalev-Shwartz, O. Shamir, N. Srebro, and K. Sridharan. Stochastic convex optimization. In COLT, 2009.
- [39] T. Steinke and J. R. Ullman. Between pure and approximate diﬀerential privacy. J. Priv. Conﬁdentiality, 7(2), 2016.
- [40] K. Talwar, A. Thakurta, and L. Zhang. Private empirical risk minimization beyond the worst case: The eﬀect of the constraint set geometry. arXiv preprint arXiv:1411.5417, 2014.
- [41] K. Talwar, A. Thakurta, and L. Zhang. Nearly-optimal private LASSO. In NIPS, pages 3025–3033, 2015.
- [42] R. Vershynin. On the role of sparsity in compressed sensing and random matrix theory, 2009.
- [43] Z. Wang, Y. Wei, M. Lee, M. Langer, F. Yu, J. Liu, S. Liu, D. G. Abel, X. Guo, J. Dong, et al. Merlin hugeCTR: GPU-accelerated recommender system training and inference. In RecSys, 2022.
- [44] J. Whitehouse, A. Ramdas, R. Rogers, and S. Wu. Fully-adaptive composition in diﬀerential privacy. In ICML, pages 36990–37007, 2023.
- [45] P. Wojtaszczyk. Stability and instance optimality for Gaussian measurements in compressed sensing. Foundations of Computational Mathematics, 10:1–13, 2010.
- [46] H. Zhang, I. Mironov, and M. Hejazinia. Wide network learning with diﬀerential privacy. CoRR, abs/2103.01294, 2021.
- [47] Y. Zhou, S. Wu, and A. Banerjee. Bypassing the ambient dimension: Private SGD with gradient subspace identiﬁcation. In ICLR, 2021.


# Appendix A Auxiliary Privacy Results

We note the existence of packing sets of sparse vectors (e.g., Vershynin [42], Cande`s and Davenport [17]). Denote by Csd the set of all s-sparse vectors in {0,1/√s}d; note that Csd ⊆ Ssd.

![image 708](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile708.png>)

- Lemma A.1. For all s and d such that s ≤ d/2, there exists a subset P ⊆ Csd such that |P| ≥ (d/s − 1/2)s/2 and for all u,v ∈ P, it holds that u − v 2 ≥ 1/√2.

![image 709](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile709.png>)

Proof. This follows from a simple packing-based construction (see, e.g., [17]). There are ds vectors in Csd, and for each vector v ∈ Csd, there are at most ⌊s/ d2⌋ many vectors u ∈ Csd such that

u−v 0 ≤ s/2 and hence u−v 2 ≤ 1/√2. Thus, we can greedily pick vectors to be C, guaranteeing that all vectors u,v ∈ Csd satisfy u − v 0 > s/2, and have |C| ≥ ds / ⌊s/ d2⌋ ≥ ds − 12 s/2.

![image 710](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile710.png>)

![image 711](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile711.png>)

![image 712](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile712.png>)

![image 713](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile713.png>)

![image 714](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile714.png>)

![image 715](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile715.png>)

![image 716](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile716.png>)

For completeness, we provide a classical dataset bootstrapping argument used for DP mean estimation lower bounds [6]. Whereas in the original reference this bootstrapping is achieved by appending dummy vectors which mutually cancel out with the goal of maintaining the structure of vectors, we simply append zero vectors as dummies as we do not need to satisfy an exact sparsity pattern.

- Lemma A.2 (Dataset bootstrapping argument from [6]). Suppose for some n, there exists a mechanism A such that for all S ∈ (Ssd)n, it holds with probability at least 1/2 that  A(S)−z¯(S) 2 ≤ C, for some C ≥ 0. Then for all n∗ < n, there exists a mechanism A′ such that for all S′ ∈ (Ssd)n∗, it holds with probability at least 1/2 that  A(S′) − z¯(S′) 2 ≤ C nn∗. Furthermore, A′ satisﬁes the same privacy guarantees as A, namely if A is ε-DP (or (ε,δ)-DP), then so is A′.

![image 717](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile717.png>)

Proof. Given mechanism A, consider mechanism A′ that for any dataset S′ ∈ (Ssd)n∗, builds dataset S by adding n − n∗ copies of 0 to S′ and returns nn∗A(S). From the guarantees of A, it holds that P[ A(S) − z¯(S) 2 ≤ C] ≥ 21. Since A′(S′) = nn∗A(S) and z¯(S′) = nn∗z¯(S), it follows that

![image 718](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile718.png>)

![image 719](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile719.png>)

![image 720](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile720.png>)

![image 721](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile721.png>)

P  A′(S′) − z¯(S′) 2 ≤ C

n n∗ ≥

![image 722](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile722.png>)

- 1

![image 723](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile723.png>)

- 2


. Since A′ just applies A once, it follows that A′ satisﬁes the same privacy guarantee as A.

![image 724](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile724.png>)

![image 725](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile725.png>)

![image 726](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile726.png>)

![image 727](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile727.png>)

Next we provide a generic reduction of existence of packing sets with pure-DP mean estimation lower bounds. Note however that the lower bounds we state work on the distributional sense.

- Lemma A.3 (Packing-based mean estimation lower bound, adapted from Hardt and Talwar [23],


Bassily et al. [6]). Let P ⊆ Rd be an α0-packing set of vectors with |P| = p. Then, there exists a distribution µ over Pn that induces an (α,ρ)-distributional lower bound for ε-DP mean estimation

with α = α20 min 1, log(εnp/2) and ρ = 1/2.

![image 728](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile728.png>)

![image 729](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile729.png>)

Proof. Let n∗ = log(εp/2). First, consider the case where n < n∗. We construct p datasets S1,... Sp where Sl consists of n copies of zl, and deﬁne µ = Unif({S1,... ,Sp}). Note that for all k = l, it holds that z ¯(Sk) − z¯(Sl) 2 ≥ α0. Suppose µ does not induce a distributional lower bound. Then there exists A which is ε-DP and has ℓ2-accuracy better than α0/2 w.p. at least 1/2: this implies in particular that

![image 730](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile730.png>)

- 1

![image 731](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile731.png>)

- 2


Pl∼Unif([p]) A(Sl) ∈ B2d(zl), α20) ≥

. For all distinct k, l, the datasets Sk and Sl diﬀer in all n entries, and hence for any ε-DP mechanism

![image 732](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile732.png>)

- A, it holds that P[A(Sl) ∈ B2d(zk, α20)] ≥ 21e−εn. However, by construction, B2d(zl, α20) are pairwise disjoint. Hence,


![image 733](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile733.png>)

![image 734](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile734.png>)

![image 735](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile735.png>)

p

p

p

1 p

PS∼µ[A(S) ∈ B2d(zk,α0/2)|S = zj]

PS∼µ[A(S) ∈ B2d(zk,α0/2)] =

1 ≥

![image 736](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile736.png>)

j=1

k=1

k=1

p

p

e−εnp 2

e−εn p

PS∼µ[A(S) ∈ B2d(zk,α0/2)|S = zk] ≥

≥

.

![image 737](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile737.png>)

![image 738](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile738.png>)

j=1

k=1

Thus, we get that n ≥ log(εp/2), which is a contradiction since we assumed n < n∗. Hence, µ induces an (α0/2,1/2)-distributional lower bound for ε-DP mean estimation. Next, consider the case where n > n∗. Then the previous argument together with Lemma A.2

![image 739](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile739.png>)

implies an (α,ρ)-lower bounded, where α = n2n∗ and ρ = 1/2, as desired.

![image 740](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile740.png>)

![image 741](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile741.png>)

![image 742](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile742.png>)

![image 743](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile743.png>)

![image 744](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile744.png>)

We will make use of the following fully adaptive composition property of DP, which informally states that for a prescribed privacy budget, a composition of (adaptively chosen) mechanisms whose privacy parameters are predictable, if we stop the algorithm before the (predictable) privacy budget is exhausted, the result of the full transcript is DP.

Theorem A.4 ((ε,δ)-DP Filter, [44]). Suppose (At)t≥0 is a sequence of algorithms such that, for any t ≥ 0, At is (εt,δt)-DP, conditionally on (A0:t−1) (in particular, (εt,δt)t is (At)t-predictable). Let ε > 0 and δ = δ′ + δ′′ be the target privacy parameters such that δ′ > 0,δ′′ ≥ 0. Let

![image 745](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile745.png>)

t

t

t

- 1

![image 746](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile746.png>)

- 2


1 δ′

ε2s, and δ[0:t] :=

ε2s +

ε[0:t] := 2ln

δs,

![image 747](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile747.png>)

s=0

s=0

s=0

and deﬁne the stopping time

T((εt,δt)t) := inf t : ε < ε[0:t+1] ∧ inf t : δ′′ < δ[0:t+1] .

Then, the algorithm A0:T(·)(·) is (ε,δ)-DP, where T(x) = T (εt(x),δt(x) t≥0.

# B Analysis of Biased SGD

Given the heavy-tailed nature of our estimators, our guarantees for a single run of SGD with biasreduced ﬁrst-order oracles only yields constant probability guarantees. Here we prove pathwise bounds that facilitate such analyses.

## B.1 Excess Empirical Risk: Convex Case

First, we provide a path-wise guarantee for a run of SGD with a biased oracle. Importantly, this guarantee is made of a method which runs for a random number of steps.

- Proposition B.1. Let (Ft)t be the natural ﬁltration, and T be a random time. Let (xt)t be the trajectory of projected SGD with deterministic stepsize sequence (ηt)t, and (biased) stochastic ﬁrstorder oracle G for a given function F. If x∗ ∈ arg min{F(x) : x ∈ X}, then the following event holds almost surely


T

- 1

![image 748](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile748.png>)

- 2ηt


[F(xt) − F(x∗)] ≤

t=0

T

x0 − x∗ 2 +

t=0

ηt 2  G(xt) 2 +  ∇F(xt) − G(xt),xt − x∗ .

![image 749](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile749.png>)

Proof. By convexity F(xt) − F(x∗) ≤  ∇F(xt),xt − x∗ =  ∇F(xt) − G(xt),xt − x∗

+ G(xt),xt − x∗

![image 750](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile750.png>)

![image 751](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile751.png>)

:=bt

≤ bt +  G(xt),xt − xt+1 +  G(xt),xt+1 − x∗ ≤ bt +

ηt 2  G(xt) 2 +

- 1

![image 752](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile752.png>)

- 2ηt


xt − xt+1 2 +  ∇G(xt),xt+1 − x∗

![image 753](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile753.png>)

(∗) ≤ bt +

- 1

![image 754](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile754.png>)

- 2ηt


1 ηt

ηt 2  G(xt) 2 +

xt+1 − xt,x∗ − xt+1

xt − xt+1 2 +

![image 755](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile755.png>)

![image 756](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile756.png>)

ηt 2  G(xt) 2 +

- 1

![image 757](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile757.png>)

- 2ηt


1 2ηt

xt − x∗ 2 −

xt+1 − x∗ 2,

= bt +

![image 758](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile758.png>)

![image 759](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile759.png>)

where the second inequality follows by the Young inequality, and step (∗) we used the optimality conditions of the projected SGD step:

ηtG(xt) + [xt+1 − xt],x − xt+1 ≥ 0 (∀x ∈ X). Therefore, summing up these inequalities, we obtain

T

- 1

![image 760](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile760.png>)

- 2η0


[F(xt) − F(x∗)] ≤

t=0

T

x0 − x∗ 2 +

t=0

Plugging in the deﬁnition of bt proves the result.

ηt 2  G(xt) 2 + bt .

![image 761](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile761.png>)

![image 762](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile762.png>)

![image 763](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile763.png>)

![image 764](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile764.png>)

![image 765](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile765.png>)

## B.2 Stationary Points: Nonconvex Case

- Proposition B.2. Let F satisfy (A.6), and let G be a biased ﬁrst-order stochastic oracle for F. Let (xt)t be the trajectory of SGD with oracle G, constant stepsize 0 < η ≤ 1/[2H], and initialization


x0 such that F(x0) − minx∈Rd F(x) ≤ Γ. Let T be a random time. Then the following event holds almost surely

T

Γ η

 ∇F(xt) 22 ≤

![image 766](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile766.png>)

t=0

ηH 2

+

![image 767](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile767.png>)

Proof. By smoothness of f, we have

T

 G(xt) 22 −

t=0

T

 ∇F(xt),G(xt) − ∇F(xt)

t=0

η2H 2  G(xt) 22

F(xt+1) − F(xt) ≤ −η ∇F(xt),G(xt) +

![image 768](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile768.png>)

η2H

2  G(xt) 22. Therefore,

≤ −η ∇F(xt) 22 − η ∇F(xt),G(xt) − ∇F(xt) +

![image 769](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile769.png>)

T

T

T

F(x0) − F(xT+1) η −

ηH 2

 ∇F(xt) 22 ≤

 ∇F(xt),G(xt) − ∇F(xt) +

 G(xt) 22

![image 770](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile770.png>)

![image 771](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile771.png>)

t=0

t=0

t=0

T

T

ηH 2

Γ η −

 ∇F(xt),G(xt) − ∇F(xt) +

 G(xt) 22.

≤

![image 772](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile772.png>)

![image 773](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile773.png>)

t=0

t=0

![image 774](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile774.png>)

![image 775](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile775.png>)

![image 776](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile776.png>)

![image 777](<2024-ghazi-differentially-private-optimization-sparse_images/imageFile777.png>)

