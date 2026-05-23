arXiv:1309.5936v1[math.ST]23Sep2013

NONPARAMETRIC GRAPHON ESTIMATION By Patrick J. Wolfe and Sofia C. Olhede University College London

We propose a nonparametric framework for the analysis of networks, based on a natural limit object termed a graphon. We prove consistency of graphon estimation under general conditions, giving rates which include the important practical setting of sparse networks. Our results cover dense and sparse stochastic blockmodels with a growing number of classes, under model misspeciﬁcation. We use proﬁle likelihood methods, and connect our results to approximation theory, nonparametric function estimation, and the theory of graph limits.

1. Introduction. Networks are fast becoming part of the modern statistical landscape (Durrett, 2007; Diaconis and Janson, 2008; Bickel and Chen, 2009; Choi, Wolfe and Airoldi, 2012; Fienberg, 2012; Zhao, Levina and Zhu, 2012; Arias-Castro and Grimmett, 2013; Ball, Britton and Sirl, 2013; Choi and Wolfe, 2013). Yet we lack a full understanding of their largesample properties in all but the simplest settings, hindering the development of models and inference tools that admit theoretical performance guarantees.

In this article we introduce a nonparametric framework for the analysis of networks, which relates to kernel-based random graph models (Janson, 2010; Sussman, Tang and Priebe, 2013), stochastic blockmodels (Airoldi et al., 2008; Rohe, Chatterjee and Yu, 2011), and degree-based models (Chatterjee, Diaconis and Sly, 2011; Bickel, Chen and Levina, 2011). We use this framework to establish consistency of likelihood-based network inference under general conditions, and to show convergence rates across a range of network regimes, from dense to sparse. Our framework thus addresses one of the biggest factors limiting the use of statistical network models in practice: a lack of ﬂexible and transparent analysis tools that admit coherent statistical interpretations (Fienberg, 2012).

Our methodology derives from a large-sample theory tailored to network data, in which well-deﬁned limiting objects play a role akin to the inﬁnite-dimensional functions that underpin classical nonparametric statistics (Bickel and Chen, 2009). An exchangeable stochastic network can be

![image 1](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile1.png>)

AMS 2000 subject classiﬁcations: Primary: 62G05; secondary: 05C80, 62G20 Keywords and phrases: graph limits; nonparametric regression; sparse random graphs;

statistical network analysis; stochastic blockmodels

1

viewed as a partial observation of this limiting object under Bernoulli sampling (Diaconis and Janson, 2008). Hence our theory is closely related to that of generalized linear models (Green and Silverman, 1994) and of contingency tables (Fienberg and Rinaldo, 2012), as well as to nonparametric function approximation. High-dimensional statistical theory in this setting is nascent, and so the linkages we develop below provide for a foundational understanding of nonparametric statistical network analysis.

2. Model elicitation. A network can be represented by an n×n data matrix A, whose ijth entry describes the relation between node i and node

- j of the network. In the most fundamental setting of graph theory, A is a symmetric, binary-valued contingency table: it is sparse yet structured, with


Aij ∈ {0,1} denoting the absence or presence of an edge between nodes i and j, and with ﬁxed, structural zeros along the main diagonal.

We call A an adjacency matrix, and model it as a realization of n2 independent Bernoulli trials. Independently for 1 ≤ i < j ≤ n, we have

- (2.1) Aij |pij ∼ Bernoulli(pij), Aji = Aij, Aii = 0.

Each Bernoulli trial Aij has success probability pij, which in turn we model using a bivariate function termed a graphon that derives from the theory of graph limits (Lov´asz, 2012).

A graphon is a nonnegative symmetric function, measurable and bounded, that represents a discrete network as an inﬁnite-dimensional analytic object. It is a basic characterization, allowing us to go from the discrete set of probabilities {pij}i<j to a limit object f (x,y) deﬁned on (0,1)2, independently of the network size. Various summaries of the network can be calculated as functionals of the graphon; for example, a network’s degree distribution is characterized by its graphon marginal 0 1 f (·,y) dy.

To model both dense and sparse networks, we allow the success probabilities pij appearing in (2.1) to depend on n. We link these to a scaled graphon ρnf (x,y) through a random sample {ξi}ni=1 of uniform variates, via a scale parameter ρn > 0 that speciﬁes the expected probability of a network edge:

- (2.2) pij = ρnf (ξi,ξj); {ξ1,... ,ξn} iid∼ Uniform(0,1), f (x,y) dxdy = 1.


Observe that EAij = Eξ pij = ρn for all 1 ≤ i < j ≤ n, and so ρn speciﬁes the sparsity of the generated network. We assume the sequence {ρn}n=2,3,... to be ﬁxed and monotone non-increasing.

This is a canonical model based on exchangeable random networks (Bickel and Chen, 2009; Bickel, Chen and Levina, 2011), and is also strongly related

to other statistical modeling paradigms. It relates the inﬁnite-dimensional graphon f (x,y) to the set of probabilities {pij}i<j sampled via ξ. This modeling strategy is similar to time series analysis, where a sampled autocovariance is related to an inﬁnite-dimensional spectral representation. As with an independent increments process, we may think of each ξi in (2.2) as a latent variable. Furthermore, ξi is associated with the ith network node, acting as a latent random index into the graphon. This reﬂects the fact that the observed ordering of the network nodes conveys no information.

Similarly, the ordering of a given graphon f (x,y) along the x and y axes has no inherent meaning; that is, f (x,y) has a built-in invariance to “rearrangements” of the x and y axes. This is similar to statistical shape analysis, where we seek to describe objects in a manner that is invariant to their orientation in Euclidean space. Thus f (x,y) represents an equivalence class of all symmetric functions that can be obtained from one another through measure-preserving transformations of [0,1].

This notion was formalized by Aldous (1981) and Hoover (1979) in the context of exchangeable inﬁnite arrays. Their eponymous theorem asserts that any such array admits a representation in terms of some f(x,y,α). This representation is unique up to measure-preserving transformation (Diaconis and Janson, 2008), and the value of α is not identiﬁable from a single network observation (Bickel and Chen, 2009). The Aldous–Hoover representation thus relates (2.2) to an exchangeable inﬁnite array {Aij}∞i,j=1 of binary random variables, such that for all n = 1,2,..., all permutations Π of {1,... ,n} and all a ∈ {0,1}n×n, we have that Pr(Aij = aij,1 ≤ i < j ≤ n) = Pr(Aij = aΠ(i)Π(j),1 ≤ i,j ≤ n).

By putting an observed n×n adjacency matrix A in correspondence with

a ﬁnite set of rows and columns of {Aij}∞i,j=1, we arrive at a model for exchangeable networks, or for sub-networks thereof. Exchangeability implies

that once we condition on the latent variable ξi associated to network node i, then all linkages Ai· to node i are conditionally independent and identically distributed. This follows from de Finetti’s representation of a sum of exchangeable indicator variables (Diaconis, 1977).

3. Main result. Our main result is that whenever a graphon f is H¨older continuous, and maximum likelihood ﬁtting is used to derive a nonparametric estimator of f from A, then this estimator will be consistent as long as ρn = ω n−1 log3 n , and its rate of convergence can be established.

To construct our estimator, we will calculate group averages after forming

- k groups from n nodes. Any such grouping can be represented as an integer partition of n via a vector h ∈ {2,... ,n}k, such that ka=1ha = n. Thus


may view n−1h as the probability mass function of a random variable with range {1,... ,k}, indexed via a cumulative distribution function H and its generalized inverse H−1:

⌊u⌋

1 n

- (3.1a) ha; u ∈ [0,k] , H(u) ∈ 0, hn1, h1+nh2,... ,1 ,

![image 2](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile2.png>)

![image 3](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile3.png>)

H−1(x) = inf

u∈[0,k]

- (3.1b) {H(u) ≥ x}; x ∈ (0,1] , H−1(x) ∈ {1,... ,k} .


H(u) =

![image 4](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile4.png>)

a=1

The central diﬃculty in constructing a nonparametric graphon estimator is that we do not know the ordering of our observed adjacency matrix A, relative to the ordered sample {ξ(i)}ni=1 indexing the graphon f. We thus deﬁne an estimator fˆ as a composition of two operations: ﬁrst we re-index the rows and columns of A according to some permutation Π of {1,... ,n}, and then we group them in accordance with H:

fˆ(x,y;h) = ρˆ−n1A¯H−1(x)H−1(y), ρˆn = n2 −1

i<j

Aij, (x,y) ∈ (0,1)2 ;

nH(b)

nH(a)

1 ha {hb − I(a = b)}

A¯ab =

AΠ(i)Π(j), 1 ≤ a,b ≤ k.

![image 5](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile5.png>)

j=nH(b−1)+1

i=nH(a−1)+1

We then deﬁne the mean-squared error of fˆ relative to f as inf

f σ(x),σ(y) − fˆ(x,y;h) 2 dxdy,

σ∈M (0,1)2

where M is the set of all measure-preserving bijections of the form σ: [0,1] → [0,1]. This error criterion is based on the so-called cut distance in the theory of graph limits (Lov´asz, 2012), and allows for all possible rearrangements of the axes of f (Choi and Wolfe, 2013).

Any estimator fˆ can be viewed as a Riemann sum approximation of f, and thus we must understand when such sums converge. Lebesgue’s criterion asserts that a bounded graphon on (0,1)2 is Riemann integrable if and only if it is almost everywhere continuous. A suﬃcient condition is that f is α-H¨older continuous for some 0 < α ≤ 1, where we write

|f (x,y) − f (x′,y′)| |(x,y) − (x′,y′)|α

- (3.2) f ∈ H¨olderα(M) ⇔ sup (x,y) =(x′,y′)∈(0,1)2


≤ M < ∞.

![image 6](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile6.png>)

This assumption ensures that f is uniformly continuous, so that its approximation error can be controlled through Riemann sums.

Under this model speciﬁcation, we obtain our main result, which we prove in Appendix A.

Theorem 3.1 (Consistency of smooth graphon estimation). Assume a sequence of graphon estimators fˆ(x,y;h) is ﬁtted under the model of (2.2), with k = ω(1) and h¯ = n/k the average group size, where

- 1. The graphon f is symmetric, bounded away from zero and α-Ho¨lder continuous, 0 < α ≤ 1;
- 2. The scaling sequence ρn satisﬁes ρn = ω n−1 log3 n , and maxn ρnf is bounded away from unity;
- 3. Every admissible partition H has group sizes bounded uniformly above


and below by h∨ = o(n), h∧ = ω(log1/2 n), and may be composed with any permutation Π of {1,... ,n} to yield fˆ(x,y;h).

Suppose furthermore that the minimum eﬀective sample size of every pos-

sible ﬁtted grouping, h2∧ ρn, and the average eﬀective sample size across all groupings, h¯2ρn, both grow suﬃciently rapidly in n:

h2∧ρn = ω log n , h¯2ρn = ω max h ¯2/n,1 log3 n .

Then if fˆ(x,y;h) is ﬁtted by blockmodel maximum proﬁle likelihood estimation as described in Section 4 below, the mean-squared error of fˆ satisﬁes

 .

 log h¯

![image 7](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile7.png>)

log2 (1/ρn)log n/h¯ nρn

2α

h∨ n

log (h∨/ρn) nα/2

OP

+

+

+

h¯2ρn

![image 8](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile8.png>)

![image 9](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile9.png>)

![image 10](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile10.png>)

![image 11](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile11.png>)

The terms appearing in this expression each stem from a diﬀerent portion of the nonparametric inference problem of graphon estimation, and will be derived and discussed in Section 5–7 below.

4. Nonparametric graphon approximation via blockmodels. To understand Theorem 3.1, we must ﬁrst describe how a particular class of statistical network model—the stochastic blockmodel—lends itself naturally to nonparametric approximation. Later, in Section 5, we will establish blockmodel consistency under model misspeciﬁcation, in settings ranging from dense (Chatterjee, 2012; Choi and Wolfe, 2013) to very sparse networks.

4.1. Stochastic blockmodels and nonparametric graphon approximation. A k-community blockmodel (k,z,θ) is a statistical network model that consists of two main components:

- 1. A community assignment function z: {1,... ,n} → {1,... ,k}. This mapping assigns each of n network nodes to exactly one of k groupings or “communities,” each of size ha,1 ≤ a ≤ k.


- 2. A block mean estimator θ: {1,... ,k}n × [0,1]n×n → [0,1]k×k. This assigns an interaction rate θab to every pair (a,b) of communities, based on the observations Aij : i ∈ z−1(a),j ∈ z−1(b) .


Any community assignment function z thus has two components: a vector h(z) = (h1,... ,hk) of community sizes equivalent to some H as deﬁned

- in (3.1a), and a permutation Πz of {1,... ,n} that re-orders the set of network nodes prior to applying the quantile function H−1(·/n) as deﬁned
- in (3.1b). Thus the community to which z assigns node i is determined by the composition H−1 ◦ Πz:


- (4.1) zi = H−1 {Πz(i)/n} , 1 ≤ i ≤ n.


Each z thus represents a re-ordering of the network nodes, followed by a partitioning of the unit interval. Each θab in turn describes the expected rate of interaction between the nodes in communities a and b.

If k grows with n, then the nonparametric properties of blockmodels come to the fore (Rohe, Chatterjee and Yu, 2011; Choi, Wolfe and Airoldi, 2012; Fishkind et al., 2013; Zhao, Levina and Zhu, 2012). In the theory of graph limits (Lov´asz, 2012), such a model is known as the “blowup” of a weighted graph to the domain (0,1)2, or as a “stepfunction approximation” of a given graphon f (x,y).

There are strong theoretical reasons why an arbitrary graphon should be well approximated by blocks (Lov´asz, 2012). These reasons stem from a fundamental result in combinatorics known as Szemere´di’s regularity lemma, which cuts across graph theory, analysis and number theory. In our context, this lemma suggests that any suﬃciently large graph behaves approximately like a (k,z,θ)-blockmodel for some k. However, this value of k may potentially be very large, and so regularizing strategies are needed to infer a blockmodel approximation with good risk properties while requiring relatively few degrees of freedom.

4.2. Fitting blockmodels to inhomogeneous random graphs. Once f (x,y) has been speciﬁed and a uniform random sample {ξi}ni=1 realized, our network reduces to a set of n2 Bernoulli(pij) trials that are conditionally independent given {ξi}ni=1. We refer to this as an inhomogeneous random graph model (Bollob´s, Janson and Riordan, 2007) for the observed data matrix A ∈ {0,1}n×n. From (2.2), the conditional log-probability of observing a given adjacency matrix A is

log Pr(A|{pij}i<j) =

{Aij log (pij) + (1 − Aij) log (1 − pij)}.

i<j

Adopting the notation of Choi, Wolfe and Airoldi (2012), we write the log-likelihood function of a blockmodel (k,z,θ) with respect to an observed data matrix A as

L(A;z,θ) =

i<j

Aij log θzizj + (1 − Aij)log 1 − θzizj , 1 ≤ i,j ≤ n

=

{Aij log θab + (1 − Aij) log (1 − θab)} , 1 ≤ a,b ≤ k

a≤b i∈z−1(a), j∈z−1(b)

=

Aij +

log θab

- i∈z−1(a),
- j∈z−1(b)


a≤b

(1 − Aij)

log (1 − θab)

- i∈z−1(a),
- j∈z−1(b)


a≤b

- (4.2) h2ab A ¯ab log θab + 1 − A¯ab log (1 − θab) ,

where A¯ab is the arithmetic average of the values of A in the (a,b)th block:

- (4.3) A¯ab =

1 h2ab

![image 12](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile12.png>)

- i∈z−1(a),
- j∈z−1(b)


Aij, h2ab =

ha

2 if a = b, hahb if a = b.

and ha is the size of the ath community. Note that this aligns with our earlier deﬁnition of fˆ, and that the quantities h2ab,A¯ab,θab all depend on the community assignment function z. The structural zeros along the main diagonal of A imply that hab diﬀers for diagonal blocks (a = b) relative to oﬀ-diagonal blocks. We see from (4.2) that for any ﬁxed assignment z ∈ {1,... ,k}n, the log-likelihood L(A;z,θ) of A will be maximized in θ ∈ [0,1]k×k by taking θab = A¯ab. This is because each sample proportion A¯ab is an extended maximum likelihood estimator for its expectation; “extended”, because we include the boundary {0,1}k×k of the parameter space, allowing for the possibility that θab = A¯ab ∈ {0,1}. Thus the extended maximum likelihood estimator coincides with the method of moments estimator for θab.

Note that (4.2) is a continuous function in θ, and so (by the extreme value theorem) L(A;z,θ) attains its supremum over the compact set [0,1]k×k. Thus we “proﬁle out” θ from the log-likelihood L(A;z,θ):

L(A;z) = max

θ∈[0,1]k×k

L(A;z,θ)

=

a≤b

h2ab A ¯ab log A¯ab + 1 − A¯ab log 1 − A¯ab

=

i<j

- (4.4) Aij log A¯zizj + (1 − Aij) log 1 − A¯zizj .


=

a≤b

Any maximizer of (4.4) over a ﬁxed, non-empty subset Zk ⊆ {1,... ,k}n is a maximum proﬁle likelihood estimator (MPLE) of z with respect to Zk. We may equivalently re-cast the problem of likelihood maximization as one of Bernoulli Kullback–Leibler divergence minimization, with

D p p′ = plog p p′ + (1 − p)log 1 1−−pp′

![image 13](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile13.png>)

![image 14](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile14.png>)

denoting the Kullback–Leibler divergence of a Bernoulli(p′) distribution from a Bernoulli(p) one.

Equipped with this deﬁnition, observe that any MPLE zˆ(A,Zk) satisﬁes zˆ(A,Zk) = argmax

- (4.5) Aij log A¯zizj + (1 − Aij) log 1 − A¯zizj

= argmax

z∈Zk

max

θ∈[0,1]k×k

L(A;z,θ)

= argmin

z∈Zk

min

θ∈[0,1]k×k

i<j

D Aij θzizj

= argmin

z∈Zk i<j

D Aij A ¯zizj .

Maximizing the proﬁle log-likelihood of (4.4) to obtain an MPLE zˆ(A,Zk)

is thus equivalent to minimizing the sum of divergences i<j D Aij A ¯zizj . This sum serves as a proxy for its “oracle” counterpart based on the matrix

p ∈ [0,1]n×n of Bernoulli parameters of the underlying generative model. This corresponds to an idealized “best blockmodel approximation” of p.

With this in mind, we deﬁne an “oracle MPLE” z(p,Zk) in direct analogy

to (4.5). Let p¯(z)ab denote the arithmetic average of the h2ab elements of p in the (a,b)th block induced by z:

- (4.6) p¯(z)ab =

1 h2ab

![image 15](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile15.png>)

- i∈z−1(a),
- j∈z−1(b)


pij,

where we recall that h2ab also depends on the choice of community assignment function z. We then have

z¯(p,Zk) = argmax

z∈Zk i<j

- (4.7) pij log p¯zizj + (1 − pij) log 1 − p¯zizj


z∈Zk i<j

= argmin

D pij p ¯zizj .

z∈Zk i<j

Observe that neither zˆ(A,Zk) nor z¯(p,Zk) is unique, since permuting the community labels {1,... ,k} does not aﬀect the likelihood of community

assignment in (4.5) or (4.7). Even aside from the issue of label switching, we are not guaranteed uniqueness; see Chatterjee, Diaconis and Sly (2011) and Rinaldo, Petrovic´ and Fienberg (2013) for discussion of this issue in the speciﬁc context of network modeling, as well as Fienberg and Rinaldo (2012) in the general setting of log-linear models for sparse contingency tables.

5. Sparse blockmodel consistency under model misspeciﬁcation. We now establish that an observed matrix A ∈ {0,1}n×n of binary adjacencies yields “oracle” information on its generative p ∈ (0,1)n×n at a rate that depends both on the sparsity of the network and on the speed at which the admissible network community sizes grow with n. We show that for suitable sequences of sets Zk(n) ⊆ {1,... ,k}n of admissible blockmodels, the maximum proﬁle likelihood assignment method zˆ(A,Zk) implies that the likelihood risk of a ﬁtted blockmodel, as measured by summing the divergences D pij A ¯zˆizˆj , approaches the risk i<j D pij p ¯zizj of the best possible blockmodel approximation as n grows large.

Theorem 5.1 (proved in Appendix B) makes this statement precise and provides a set of suﬃcient conditions, driven primarily by the eﬀective sample size of each ﬁtted block.

Theorem 5.1 (Controlling excess blockmodel risk). For each n = 2,3,..., let A ∈ {0,1}n×n be the adjacency matrix of a simple random graph with independent Bernoulli(pij) edges, and consider a corresponding sequence of k-community blockmodel estimators, with k = k(n) a function of n. Assume:

- 1. The expected edge density n2 −1 i<j pij(n) of A does not approach 0 or 1 too rapidly in n: there exists a monotone non-increasing, strictly

positive sequence ρ¯(n), such that for all n suﬃciently large, ρ¯(n) ≤

n 2

−1

i<j pij(n) ≤ 1 − ρ¯(n).

![image 16](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile16.png>)

- 2. Likewise, no block density {p¯zizj(n)}i<j,z∈Zk(n) approaches 0 or 1 too rapidly in n: there exists a monotone non-increasing, strictly positive sequence ρ∧(n), such that ρ∧(n) ≤ ρ¯(n) and ρ∧(n) ≤ p¯zizj(n) ≤ 1 −

![image 17](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile17.png>)

ρ∧(n) for all z ∈ Zk(n), 1 ≤ i < j ≤ n and n suﬃciently large.

- 3. The sizes {hzi(n)}1≤i≤n,z∈Zk(n) of all possible communities grow sufﬁciently rapidly in n: there exists a monotone strictly increasing sequence h∧(n) taking values in {2,... ,⌊n/k(n)⌋ such that for all n sufﬁciently large, h∧(n) ≤ minz∈Zk(n) {min1≤i≤n hzi(n)}.


Assume that the sequences Zk,ρ,ρ¯ ∧,h∧ are ﬁxed in advance and independent of all other quantities. Let h¯ = n/k ∈ [1,n], and suppose that the minimum eﬀective sample size of every possible ﬁtted block, h2∧ ρ∧, and the

average eﬀective sample size across all blocks, h¯2ρ¯, both grow suﬃciently rapidly in n:

h2∧ρ∧ = ω log n , h¯2ρ¯ = ω max h ¯2/n,1 log3 n .

Then for all sequences of subsets Zk ⊆ {1,... ,k}n that respect condition 3, we have as n → ∞ that for any choice of z ∈ Zk, deterministic or random,

A¯zizj∈{/ 0,1} D pij A ¯zizj i<j:A¯zizj∈{/ 0,1} pij

- (5.1) i<j:


![image 18](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile18.png>)

log n/h¯ nρ¯

D pij p ¯zizj i<j pij

1 h¯2ρ¯

= i<j

+ OP max

,

.

![image 19](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile19.png>)

![image 20](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile20.png>)

![image 21](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile21.png>)

k i<j Aij log A¯zizj + (1 − Aij) log 1 − A¯zizj ,

For zˆ(A,Zk) = argmaxz∈Z

A ¯zˆizˆj∈{/ 0,1}D pij A ¯zˆizˆj i<j:A¯zˆizˆj∈{/ 0,1} pij

- (5.2)


![image 22](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile22.png>)

 

max  

 .



![image 23](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile23.png>)

log2 (1/ρ∧)log n/h¯ nρ¯

log h¯ h¯2ρ¯

minz∈Zk i<jD pij p ¯zizj i<j pij

,

=

+OP

![image 24](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile24.png>)

![image 25](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile25.png>)

![image 26](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile26.png>)



These results also hold marginally with respect to the model of (2.2).

Theorem 5.1 is signiﬁcant because it gives conditions under which the excess risk of a ﬁtted blockmodel converges to zero, implying that blockmodel parameters can be estimated consistently even when the true generative model giving rise to A is unknown. It predicts diﬀerent rates of convergence for diﬀerent network sparsity regimes. Depending on the growth of k with n, either the ﬁrst or the second of two rate terms in (5.2) will dominate.

We may summarize these regimes as follows:

- 1. Dense networks: If ρ∧ and ρ¯ remain constant in n, and k grows with n as k = O(n3/4), then Theorem 5.1 predicts a convergence rate of at least log(n)/n. If instead k grows like nδ for 3/4 < δ < 1, then this rate will decrease to log n/n2(1−δ).

![image 27](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile27.png>)

- 2. Sparse networks: If ρ∧ and ρ¯ decrease like n−2γ for 0 < γ < 1/2, and k = O(n3/4−γ/2), then Theorem 5.1 predicts the rate log(n)3/2/n1/2−γ. If k grows like nδ for 3/4−γ/2 < δ < 1−γ, then this rate will decrease to log n/n2(1−δ−γ).


- 3. Ultra-sparse networks: If ρ∧ and ρ¯ decrease like log(n)3+β/n for β > 0, then Theorem 5.1 predicts rate log(n)−β/2 whenever k = O(n1/2), matching the regime of Choi, Wolfe and Airoldi (2012).


In each of these cases, the given conditions on ρ∧ can be relaxed accordingly.

Theorem 5.1 is the ﬁrst such result known for sparse or ultra-sparse networks—those for which ρ¯ = o(1), so that the average number of connections per node can grow sublinearly, here as slowly as logarithmically in n. This complements the recent result of Choi and Wolfe (2013) for ﬁxed-k ﬁtting of dense bipartite graphs—those for which ρ∧ and ρ¯ remain constant, so that the average number of connections per node grows linearly in n.

- Theorem 5.1 extends this regime, allowing for the growth of k with n, while also yielding an improved convergence rate of log(k)/n for dense graphs.


![image 28](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile28.png>)

To understand why Theorem 5.1 holds in this setting, we begin by conditioning on a choice of community assignment function z. Blocks of network edges then comprise independent sets of independent Bernoulli trials. Conditionally upon z, sample proportions A¯zizj |z of these blocks are thus independent Poisson–Binomial variates. Without additional restrictions, however, a ﬁtted block could be any size—even as small as a single Bernoulli trial. Thus it is necessary to constrain the set Zk ⊆ {1,... ,k}n of admissible blockmodels, and also to constrain the allowable global and local sparsity of the network, so that the eﬀective sample size of every possible A¯zizj |z grows in n. This ensures that all block-wise sample proportions A¯zizj |z behave like Normal variates in the large-sample limit, when appropriately standardized.

There are then two main technical challenges:

- 1. Double randomness: While every A¯zizj |z is amenable to analysis, choosing zˆ by proﬁle likelihood maximization introduces “double random-

ness,” coupling all blocks and precluding a direct analysis of A¯zˆizˆj. Instead, we take the approach of Choi, Wolfe and Airoldi (2012), and

show that results for A¯zizj |z hold uniformly for any choice of z — and therefore that they also hold for A¯zˆizˆj.

- 2. Likelihood zeros: The assumption that all pij ∈ (0,1) ensures that each D pij p ¯zizj is ﬁnite. However, D pij A ¯zˆizˆj will fail to be ﬁ-


nite if A¯zˆizˆj ∈ {0,1}, in which case the (ˆzi,zˆj)th block has saturated. Such blocks add 0 to the likelihood; their parameters are not estimable (Fienberg and Rinaldo, 2012). The theorem conditions allow us to control the probability of these likelihood zeros, by requiring the eﬀective sample size of each block to grow suﬃciently rapidly in n.

This latter point is particularly important, since only values in the interior of the parameter space [0,1]k×k are estimable (Fienberg and Rinaldo,

2012, Theorem 7). As in the case of additional structural zeros (Fienberg and Rinaldo, 2012, Corollary 8), the Fisher information matrix will be rankdeﬁcient, and the degrees of freedom must be adjusted accordingly in order to obtain correct inferential conclusions. This explains why the random denominator term is necessary in the left-hand side of (5.2).

We may connect this understanding to the three sparsity regimes described above: the case of dense networks, corresponding to the setting of exchangeable random graphs; that of sparse networks, where the density of network edges n2 −1 i<j pij decays as some power of n; and that of ultra-sparse networks, where the edge density decays at a rate approaching log(n)/n. This is the so-called connectivity threshold, above which an inhomogeneous random graph will be fully connected with probability approaching 1 as n → ∞ (Alon, 1995). If the edge density were instead to decay at a rate of 1/n—the extremely sparse setting of Bollob´s and Riordan (2009)—then the resulting networks would fail in general to be connected, and Poisson rather than Normal limiting behavior would hold for each block (Olhede and Wolfe, 2013).

6. From blockmodels to smooth graphon estimation. We now present our ﬁnal result leading to consistent graphon estimation. To go beyond conditional estimation of inhomogeneous random graphs via blockmodels, we will assume additional structure via graphon smoothness. This smoothness will in turn allow us to control estimation risk, by sending the main term in Theorem 5.1 to zero.

A blockmodel ﬁrst orders the rows and columns of A, and then groups its entries according to a vector of community sizes h ∈ {2,... ,n}k. This speciﬁes a partition H in accordance with (3.1a), which in turn induces a piecewise-constant approximation of the graphon f (x,y) along blocks. To see this, deﬁne the domain ωab ⊆ [0,1)2 of the (a,b)th block as

ωab = [H(a − 1),H(a)) × [H(b − 1),H(b)) , 1 ≤ a,b ≤ k,

and deﬁne the blockmodel approximation f¯(x,y;h) of f (x,y) via the local averages f¯ab,1 ≤ a,b ≤ k:

1 |ωab| ωab

f¯(x,y;h) = f¯H−1(x)H−1(y), f¯ab =

- (6.1) f (x,y) dxdy.


![image 29](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile29.png>)

If f (x,y) is smooth as well as bounded, then results from approximation theory allow the error f −f¯ to be controlled in any Lp norm, as a function of the maximum over all block diameters (h2a + h2b)1/2/n for 1 ≤ a,b ≤ k (DeVore, 1998, see also Lemma C.6).

Recall from (4.1) that any blockmodel community assignment vector z is a composition H−1 ◦ Πz for some partition H of [0,1] and permutation Πz of {1,... ,n}, so that zi = H−1 {Πz(i)/n} ,1 ≤ i ≤ n. From (4.6), we may express p¯(z) for any 1 ≤ a,b ≤ k as

1 h2ab i<j

pij I H−1 {Πz(j)/n} = b I H−1 {Πz(i)/n} = a

p¯(z)ab =

![image 30](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile30.png>)

nH(b)

nH(a) I(a =b)+(j−1) I(a=b)

1 h2ab

- (6.2) z (i) Π−z 1(j).


=

pΠ−1

![image 31](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile31.png>)

j=nH(b−1)+1

i=nH(a−1)+1

Thus p¯(z)ab is an average over h2ab graphon evaluations f ξΠ−1

z (j) , since the model of (2.2) asserts that pij(n) ∝ f (ξi,ξj). These evaluations occur at random points determined by {ξ1,... ξn} according to the inverse of the permutation Πz, while H determines the size of each block.

z (i),ξΠ−1

From this simple observation, we will show that it is possible to relate p¯(z)ab to f (x,y) by choosing an “oracle” permutation Πz(i) whose inverse yields the ordered sample {ξ(1),... ξ(n)}. To see this, ﬁrst note that whenever the H¨older condition of (3.2) is satisﬁed, we have by Lemma C.7 that

f ξ(i),ξ(j) = f n+1 i , n+1j + OP n−α/2 ,

![image 32](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile32.png>)

![image 33](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile33.png>)

because each ξ(i) converges in probability to its expectation i/(n + 1) at a rate no worse than n−1/2, and (3.2) relates this to f ξ(i),ξ(j) −f n+1 i , n+1j . Now take Πz(i) = (i)−1, where (i)−1 denotes the rank of ξi from smallest to largest, and observe that f ξΠ−1

![image 34](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile34.png>)

![image 35](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile35.png>)

z (j) evaluates to f ξ(i),ξ(j) . The key point is that when f is α-H¨older continuous, then convergence

z (i),ξΠ−1

of the ordered sample {ξ(i)}ni=1 governs convergence of the random averages comprising p¯(z)ab in (6.2). Indeed, if h∨ uniformly upper-bounds the largest possible community size, then by Lemma C.5, we have that

Πz = (·)−1 ⇒ ρ−n1p¯z(i)z(j) − f¯ ξ(i),ξ(j);h = OP n−α/2 + (n/h∨)−α , where we recall from (6.1) that f¯(x,y;h) is the local block average of f.

As a consequence, we can control the oracle estimation risk featured in

- Theorem 5.1 as follows.
- Theorem 6.1 (Controlling absolute risk). Assume in the scaled ex-


changeable graph model of (2.2) that:

- 1. The graphon f is a positive, symmetric function on (0,1)2, and is α-Ho¨lder continuous, 0 < α ≤ 1;


- 2. Furthermore, f is bounded away from zero and maxn ρnf is bounded away from unity;
- 3. Each set Zk(n) ⊆ {1,... ,k}n of admissible blockmodel assignments has the following property: If H is generated by some z ∈ Zk, then H−1 ◦ Π ∈ Zk for every permutation Π of {1,... ,n}.


Then for h∨(n) the largest community size in each Zk(n), the oracle likelihood risk in Theorem 5.1 satisﬁes

(6.3)

minz∈Zk i<j D pij p ¯zizj i<j pij

= OP n−α + (n/h∨)−2α .

![image 36](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile36.png>)

We prove this theorem in Appendix C by using the oracle choice of permutation (·)−1 to upper-bound the risk via a block approximation f¯(x,y;h) of f (x,y), based on some z∗ which achieves the minimum in (6.3). Conditions 1 and 2 are then suﬃcient to guarantee the claimed rate of approximation. Condition 3 ensures that H−1 ◦ (·)−1 ∈ Zk, since we do not know z∗ or the requisite ordering (·)−1 in advance.

7. Rates of convergence. We see directly that the rate of convergence in Theorem 6.1 depends on the H¨older continuity of f in two ways: through the convergence of the ordered sample {ξ(i)}ni=1 (variance), and through the rate at which h∨/n goes to zero in n (bias). This rate is also self-scaling relative to the sparsity of the network, as it does not depend on ρn.

In contrast, Theorem 5.1 depends strongly both on the network sparsity factor ρn, as well as the minimum and average admissible block sizes, h∧ and h¯. The conditions of Theorem 5.1 ensure that excess blockmodel risk can be controlled under model misspeciﬁcation, enabling groupings of nodes with good risk properties to be estimated, despite the variability of the data.

Together, the results of Theorems 5.1 and 6.1 enable us to establish meansquare graphon consistency at the rates indicated in Theorem 3.1, namely

 .

 log h¯

![image 37](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile37.png>)

log2 (1/ρn)log n/h¯ nρn

2α

h∨ n

log (h∨/ρn) nα/2

+

+

+

OP

h¯2ρn

![image 38](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile38.png>)

![image 39](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile39.png>)

![image 40](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile40.png>)

![image 41](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile41.png>)

The ﬁrst two terms come directly from Theorem 5.1, while the third is from

- Theorem 6.1. The ﬁnal term comes from relating the discrete quantities featured in these theorems to the graphon itself, and is driven in part by the fact that we do not know the ordering of the data relative to the Uniform(0,1)


variates {ξi}ni=1 by which the graphon is sampled. The O n−1/2 variance of the ordered sample {ξ(i)}ni=1 subsequently appears, and is modulated by the regularity of the graphon through its H¨older continuity exponent α.

8. Conclusion. In this article we have established a number of new results within a nonparametric framework for network inference, based on graphons as natural limiting objects. Understanding graphons as analytic objects, as well as the behavior of dense and sparse networks based on them, is fundamental to advancing our nonparametric understanding of networks.

To this end, we have established consistency of graphon estimation under general conditions, giving rates which include the important practical setting of sparse networks. By treating dense and sparse stochastic blockmodels with a growing number of classes, under model misspeciﬁcation, our results improve substantially upon what is currently known in the literature.

Our results link strongly to approximation theory, nonparametric function estimation, and the theory of graph limits, and thus provide for a foundational understanding of nonparametric statistical network analysis.

APPENDIX A: PROOF OF THEOREM 3.1 AND ITS LEMMAS A.1. Proof of Theorem 3.1. Proof. We note from Lemma A.1 that for (x,y) ∈ (0,1)2

fˆ(x,y;h) = ρˆ−n1A¯H−1(x)H−1(y) = 1 + OP n−1/2 ρ−n1A¯H−1(x)H−1(y).

Recalling the deﬁnition of A¯ab, we see that uniformly for all choices of H and Π, and for all 1 ≤ a,b ≤ k, we have 0 ≤ EA¯ab ≤ ρn sup(x,y)∈(0,1)2 f (x,y) and 0 ≤ EA¯2ab ≤ ρ2n sup(x,y)∈(0,1)2 f2 (x,y).

Since f is by hypothesis H¨older continuous on a bounded domain, it is

bounded, and thus A¯ab = OP ρn and A¯2ab = OP ρ2n by Markov’s inequality. We will thus expand the squared error term in the integrand of

the graphon mean-squared error pointwise, using the fact that the error term should be evaluated at the inﬁmum over measure preserving bijections. Therefore this error be upper-bounded by its evaluation at some σ∗ ∈ M, which we will choose in accordance with the proof of Lemma A.3 below:

2 dxdy

f σ(x),σ(y) − 1+OP n−1/2 ρ−n1A¯H−1(x)H−1(y)

inf

σ∈M (0,1)2

≤

2 dxdy + OP n−1/2

f σ∗(x),σ∗(y) − ρ−n1A¯H−1(x)H−1(y)

(0,1)2

≤

2 dxdy + OP n−1/2

f σ∗(x),σ∗(y) − ρ−n1A¯H−1(x)H−1(y)

f ˆ∈{/ 0,1}

≤ 2(sup f)

ρ−n1 D ρnf σ∗(x),σ∗(y) ρnfˆ(x,y;h) dxdy + OP n−1/2 ,

f ˆ∈{/ 0,1}

where the last two lines follow from Lemmas A.2 and C.9, respectively. By Lemma A.3, we have

2(supf)

·

ρ−n1 D ρnf σ∗(x),σ∗(x) ρnfˆ(x,y;h) dxdy = 2(supf)

f ˆ∈{/ 0,1}

A¯zizj∈{/ 0,1} D(pij ||A¯zizj) i<j:A¯zizj∈{/ 0,1} pij 1 + OP n−α/2

f (x,y) dxdy i<j:

![image 42](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile42.png>)

f ˆ∈{/ 0,1}

log (h∨/ρn) nα/2

log h∨ ρnn

+ OP

+

,

![image 43](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile43.png>)

![image 44](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile44.png>)

uniformly in z. The conditions of Theorem 3.1 are suﬃcient for Theorems 5.1 and 6.1 to hold, and so if fˆ is ﬁtted by maximum proﬁle likelihood, then we may substitute terms from Theorems 5.1 and 6.1 to obtain

·

ρ−n1 D ρnf σ∗(x),σ∗(x) ρnfˆ(x,y;h) dxdy = 2(supf)

2(supf)

f ˆ∈{/ 0,1}

![image 45](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile45.png>)

2 1 ρn log nh¯ nρn

, log

−2α + OP max h¯ log2ρh¯

f (x,y) dxdy· OP n−α + h n

![image 46](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile46.png>)

![image 47](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile47.png>)

![image 48](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile48.png>)

![image 49](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile49.png>)

![image 50](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile50.png>)

∨

n

f ˆ∈{/ 0,1}

+ OP

log (h∨/ρn) nα/2

+

![image 51](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile51.png>)

log h∨ ρnn

![image 52](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile52.png>)

.

![image 53](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile53.png>)

![image 54](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile54.png>)

![image 55](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile55.png>)

![image 56](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile56.png>)

A.2. Auxiliary lemmas needed for Theorem 3.1.

Lemma A.1. Assume the setting of Theorem 3.1. Then Eρˆn = ρn, varρˆn = O ρ2n/n .

Proof. Since i < j and k < l, we have that EAij |ξ = ρnf (ξi,ξj) and cov (Aij,Akl | ξ) = ρnf(ξi,ξj){1 − ρnf(ξi,ξj)} I (i = k)I (j = l). We ﬁrst use the law of total expectation to deduce

Eρˆn = n2 −1 i<j Eξ {ρnf (ξi,ξj)} = ρn (0,1)2 f(x,y)dxdy = ρn.

The necessary marginal variances and covariances can then be established hierarchically:

var(Aij) = Eξ {var(Aij | ξ)} + varξ {E(Aij |ξ)}

= {Eρnf(ξi,ξj)} {1 − Eρnf(ξi,ξj)} = ρn (1 − ρn), cov(Aij,Akl) =Eξ{cov(Aij,Akl|ξ)}+covξ{E(Aij|ξ) ,E(Akl |ξ)},(i,j) = (k,l).

Since Ef (ξi,ξj)f (ξk,ξl) = (0,1)2 f2(x,y)dxdy if i = k and j = l, and (0,1)2 f(x,y)dxdy 2 if i = k and j = l, we obtain when either i = k or

- j = l that


covξ (Aij,Akl) = covξ {E(Aij |ξ),E(Akl |ξ)}

= Eξ {ρnf(ξi,ξj)ρnf(ξk,ξl)} − Eξ {ρnf(ξi,ξj)} Eξ {ρnf(ξk,ξl)} ≤ ρ2n max{varf(ξi,ξj),var f(ξk,ξl)} ≤ ρ2n (0,1)2 {f(x,y)}2 dxdy − (0,1)2 f(x,y)dxdy 2 .

Because covξ {Aij,Akl} = 0 when all i,j and k,l are distinct, and since i = j and k = l, we obtain

varAij + n2 −2

varρˆn = n2 −2

i<j

i =k∪j =l

≤ n2 −2ρn (1 − ρn) + n2 −2

i =k∪j =l

cov (Aij,Akl)

cov (Aij,Akl) [I(i = k) + I(i = l)

+I(j = k) + I(j = l)] ≤ n2 −2ρn (1 − ρn) + 4n n2 −2ρ2n (0,1)2 {f(x,y)}2 dxdy − 1 .

The order term of O(ρ2n/n) follows, as ρ2n/n ≥ ρn/n2 ⇔ ρn ≥ 1/n, since ρn = ω n−1 log3 n .

![image 57](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile57.png>)

![image 58](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile58.png>)

![image 59](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile59.png>)

![image 60](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile60.png>)

Lemma A.2. Assume the setting of Theorem 3.1. Then

f σ(x),σ(x) −fˆ(x,y;h) 2 dxdy = OP e−(h2∧)ρn+2 log(1/ρn) .

sup

σ∈M f ˆ∈{0,1}

Proof. We apply Lemma B.2 to control i<j I A ¯ab ∈ {0,1} marginally, after observing that

f σ(x),σ(x) − fˆ(x,y;h) 2 dxdy ≤

sup

σ∈M f ˆ∈{0,1}

f ˆ∈{0,1}

hahb ≤ 2(ρnn)−2

= 2(ρnn)−2

4h2ab

a≤b:A¯ab∈{0,1}

a,b:A¯ab∈{0,1}

= 8(ρnn)−2

I A ¯ab ∈ {0,1} .

i<j

2ρ−n2 dxdy

![image 61](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile61.png>)

![image 62](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile62.png>)

![image 63](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile63.png>)

![image 64](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile64.png>)

Lemma A.3. Assume the setting of Theorem 3.1. Then for any z ∈ Zk,

- (A.1)

infσ∈M f ˆ∈{/ 0,1} ρ−n1 D ρnf σ(x),σ(y) ρnfˆ(x,y;h) dxdy f ˆ∈{/ 0,1} f (x,y) dxdy

![image 65](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile65.png>)

= i<j:

A¯zizj∈{/ 0,1} D(pij ||A¯zizj) i<j:A¯zizj∈{/ 0,1} pij 1 + OP nα/ 1 2 +OP log(nhα/∨/ρ2 n) + logρ h∨ nn .

![image 66](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile66.png>)

![image 67](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile67.png>)

![image 68](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile68.png>)

![image 69](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile69.png>)

Proof. We ﬁrst treat the numerator of (A.1), whose inﬁmum is over M, the set of all measure-preserving bijective maps of the form σ: [0,1] → [0,1]. We may write

0 ≤ inf

σ∈M f ˆ∈{/ 0,1}

ρ−n1 D ρnf σ(x),σ(y) ρnfˆ(x,y;h) dxdy

= infσ∈M a,b:A¯(z)

ab∈{/ 0,1} ω(z)ab ρ−n1 D ρnf σ(x),σ(y) A ¯(z)ab dxdy,

- (A.2)

since fˆ is constant on blocks. Observe that for each individual summand in (A.2), we may write

ω(z)ab

ρ−n1 D ρnf σ(x),σ(y) A ¯(z)ab dxdy

- (A.3)

=

H(b)

H(b−1)

H(a)

H(a−1)

ρ−n1 D ρnf(·) A ¯(z)ab dxdy

=

nH(b)

j=nH(b−1)+1

nH(a)

i=nH(a−1)+1

j n

![image 70](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile70.png>)

j−1 n

![image 71](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile71.png>)

i n

![image 72](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile72.png>)

i−1 n

![image 73](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile73.png>)

ρ−n1 D ρnf σ(x),σ(y) A ¯(z)ab dxdy.

We now restrict our choice of σ ∈ M to satisfy the following property:

- (A.4)


j n

![image 74](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile74.png>)

j−1 n

![image 75](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile75.png>)

Π(j) n

i n

![image 76](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile76.png>)

![image 77](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile77.png>)

f σ(x),σ(y) dxdy =

Π(j)−1 n

i−1 n

![image 78](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile78.png>)

![image 79](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile79.png>)

Π(i) n

![image 80](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile80.png>)

f (x,y)dxdy, 1 ≤ i,j ≤ n,

Π(i)−1 n

![image 81](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile81.png>)

for some permutation Π of {1,... ,n}. Such a choice of measure-preserving bijection can always be made, as it simply partitions the unit interval into n+1 subintervals of the form [(i − 1)/n,i/n) ,1 ≤ i ≤ n, and permutes their order in accordance with Π. We make this choice in order to preserve the

H¨older continuity of f on each domain (x,y) ∈ i−n1, ni × j−n1, nj , as will be shown below.

![image 82](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile82.png>)

![image 83](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile83.png>)

![image 84](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile84.png>)

![image 85](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile85.png>)

Thus we may write, combining (A.2)–(A.6),

- (A.5) inf

σ∈M f ˆ∈{/ 0,1}

ρ−n1 D ρnf σ(x),σ(y) ρnfˆ(x,y;h) dxdy

≤ min

Π∈Sn a,b:A¯ab∈{/ 0,1}

nH(b)

j=nH(b−1)+1

nH(a)

i=nH(a−1)+1

·

Π(j) n

![image 86](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile86.png>)

Π(j)−1 n

![image 87](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile87.png>)

Π(i) n

![image 88](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile88.png>)

Π(i)−1 n

![image 89](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile89.png>)

ρ−n1 D ρnf (x,y) A ¯(z)ab dxdy,

with Sn the set of permutations of {1,... ,n}. From Lemma A.4 we then obtain

n2

Π(j) n

![image 90](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile90.png>)

Π(j)−1 n

![image 91](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile91.png>)

Π(i) n

![image 92](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile92.png>)

Π(i)−1 n

![image 93](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile93.png>)

ρ−n1 D ρnf (x,y) A ¯(z)ab dxdy

= ρ−n1 D ρnf ξ(Π{i}),ξ(Π{j})

A ¯(z)ab +OP log (1/ρn) + log h2∨ n−α/2 ,

where ξ(Π{i}) is the Π(i)th element of the ordered sample {ξ(i)}ni=1. Starting from (A.5), we then have

inf

σ∈M f ˆ∈{/ 0,1}

ρ−n1 D ρnf σ(x),σ(y) ρnfˆ(x,y;h) dxdy

≤ min

Π∈Sn

1 n2

![image 94](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile94.png>)

a,b:A¯(z)ab∈{/ 0,1}

nH(b)

j=nH(b−1)+1

 

nH(a) I(a =b)+(j−1) I(a=b)

i=nH(a−1)+1

{1 + I (a = b)} + I (i = j)



· ρ−n1 D ρnf ξ(Π{i}),ξ(Π{j})

A ¯(z)ab + OP log (1/ρn) + log h2∨ n−α/2

≤

1 n2

![image 95](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile95.png>)

  2

i<j:A¯(z)zizj∈{/ 0,1}

ρ−n1 D pij A ¯(z)zizj +

1≤i≤n:A¯(z)zizi∈{/ 0,1}

ρ−n1 D ρnf (ξi,ξi) A ¯(z)zizi

  

+ OP log (1/ρn) + log h2∨ n−α/2 ,

- (A.6)


where we have chosen Π = (·)−1 ◦ Π−z 1, so that Π(i) = Π−z 1{i} −1, with (i)−1 the rank of ξi, from smallest to largest. This choice allows us to match each ξ(Π{i}) to the corresponding group assignment zi of the ith network node. To see this, recall from (4.1) that zi = H−1 {Πz(i)/n} ,1 ≤ i ≤ n, and

from (4.3) and (C.6) respectively that

A¯(z)ab =

p¯(z)ab =

nH(b)

nH(a) I(a =b)+(j−1) I(a=b)

1 h2ab

![image 96](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile96.png>)

j=nH(b−1)+1

i=nH(a−1)+1

z (i)Π−z 1(j),

AΠ−1

nH(b)

nH(a) I(a =b)+(j−1) I(a=b)

1 h2ab

z (i),ξΠ−1

z (j) .

ρnf ξΠ−1

![image 97](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile97.png>)

j=nH(b−1)+1

i=nH(a−1)+1

Note that p¯(z)ab = E A ¯(z)ab |ξ,z . Thus we relate each pij = ρnf (ξi,ξj) to the average A¯(z)zizj of the block to which it is assigned by z.

Continuing from (A.6), we appeal to Lemma A.5 to bound the diagonal term, thereby obtaining

ρ−n1 D ρnf σ(x),σ(y) ρnfˆ(x,y;h) dxdy

inf

σ∈M f ˆ∈{/ 0,1}

1 − n1 n 2 i<j:A¯(z)zizj ∈{/ 0,1}

![image 98](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile98.png>)

ρ−n1 D pij A ¯(z)zizj +OP log (1/ρn) + log h2∨ n−α/2

≤

![image 99](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile99.png>)

+log h2∨ (ρnn)−1 .

Lemma A.6 yields the denominator of (A.1), and the result follows by taking the ratio of these terms.

![image 100](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile100.png>)

![image 101](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile101.png>)

![image 102](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile102.png>)

![image 103](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile103.png>)

Lemma A.4. Assume the setting of Theorem 3.1. Then for 1 ≤ i,j ≤ n, (a,b) : A¯(z)ab ∈/ {0,1}

j n

i n

![image 104](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile104.png>)

![image 105](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile105.png>)

ρ−n1 D ρnf (x,y) A ¯(z)ab dxdy;

- (A.7) n2


j−1 n

i−1 n

![image 106](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile106.png>)

![image 107](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile107.png>)

= ρ−n1 D ρnf ξ(i),ξ(j) A ¯(z)ab +OP log (1/ρn) + log h2∨ n−α/2 .

Proof. The result follows from a Taylor series of the integrand of (A.7), which we will show to converge everywhere on the domain of integration, as long as A¯(z)ab ∈/ {0,1}. We begin by noting that whenever f ∈ H¨olderα(M), we have from Lemma C.7 that for all (x,y) ∈ i−n1, ni × j−n1, nj ,

![image 108](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile108.png>)

![image 109](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile109.png>)

![image 110](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile110.png>)

![image 111](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile111.png>)

E f (x,y) − f ξ(i),ξ(j) ≤ E f (x,y) − f n+1 i , n+1j

![image 112](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile112.png>)

![image 113](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile113.png>)

+ E f n+1 i , n+1j − f ξ(i),ξ(j) ≤ M 2−1/2(n + 1) −α + M {2(n + 2)}−α/2 .

![image 114](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile114.png>)

![image 115](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile115.png>)

From Markov’s inequality, f ξ(i),ξ(j) = f (x,y) + OP n−α/2 for every ﬁxed (x,y) in the domain of interest. Thus the following Taylor series holds

whenever f ∈ H¨olderα(M) and A¯(z)ab ∈/ {0,1}:

- (A.8) ρ−n1 D ρnf ξ(i),ξ(j) A ¯(z)ab = ρ−n1 D ρnf (x,y) A ¯(z)ab

+log

ρnf (x,y) 1 − ρnf (x,y) ·

![image 116](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile116.png>)

1 − A¯(z)ab A¯(z)ab

![image 117](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile117.png>)

f ξ(i),ξ(j) − f (x,y) +oP n−α/2 .

To bound the second term in (A.8), let l = infx∈(0,1) f(x,x) and u = supx∈(0,1) f(x,x). Since A¯(z)aa ∈/ {0,1}, we may bound the magnitudes of log A¯(z)aa,log 1 − A¯(z)aa via log h2a ≤ log h2∨ . Then

- (A.9) E log

ρnf (x,y) 1 − ρnf (x,y) ·

![image 118](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile118.png>)

1 − A¯(z)ab A¯(z)ab ≤ log (ρnl)−1

![image 119](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile119.png>)

+ log (1 − ρnu)−1 + 2log h2∨ .

The ﬁrst two terms in (A.9) are bounded by hypothesis, and then we apply Markov’s inequality to (A.8).

![image 120](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile120.png>)

![image 121](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile121.png>)

![image 122](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile122.png>)

![image 123](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile123.png>)

Lemma A.5. Assume the setting of Theorem 3.1. Then

- (A.10) n−2 1≤i≤n:A¯(z)zizi∈{/ 0,1}


ρ−n1 D ρnf (ξi,ξi) A ¯(z)zizi

= OP log (1/ρn) + ρ−n1 log h2∨ n−1 .

Proof. Let l = infx∈(0,1) f(x,x) and u = supx∈(0,1) f(x,x). Since A¯(z)aa ∈/

{0,1}, we may bound the magnitudes of log A¯(z)aa and log 1 − A¯(z)aa via log h2a ≤ log h2∨ . We bound the expectation of each summand in (A.10) for 1 ≤ i ≤ n

1 − ρnf (ξi,ξi) 1 − A¯(z)zizi

ρnf (ξi,ξi) A¯(z)zizi

+ ρ−n1 {1 − ρnf (ξi,ξi)}log

E f (ξi,ξi)log

![image 124](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile124.png>)

![image 125](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile125.png>)

≤ u log(ρnl)−1 + log h2∨ + ρ−n1 log (1 − ρnu)−1 + log h2∨

= O log (1/ρn) + ρ−n1 log h2∨ .

,

The result then follows from linearity of expectation and Markov’s inequality, as per Lemma A.4.

![image 126](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile126.png>)

![image 127](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile127.png>)

![image 128](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile128.png>)

![image 129](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile129.png>)

Lemma A.6. Assume the setting of Theorem 3.1. Then

1 − n1 ρn n2

f (x,y) dxdy =

f ˆ∈{/ 0,1}

![image 130](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile130.png>)

pij + OP n−α/2 .

![image 131](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile131.png>)

i<j:A¯(z)zizj∈{/ 0,1}

Proof. We start by discretizing the integral. We therefore write that

·

nH(b)

nH(a)

f (x,y) dxdy =

f ˆ∈{/ 0,1}

a,b:A¯(z)ab∈{/ 0,1}

j=nH(b−1)+1

i=nH(a−1)+1

j n

![image 132](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile132.png>)

j−1 n

![image 133](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile133.png>)

i n

pij ρnn2

![image 134](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile134.png>)

f (x,y) dxdy=

![image 135](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile135.png>)

i−1 n

A ¯(z)zizj∈{/ 0,1}

![image 136](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile136.png>)

j n

![image 137](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile137.png>)

·

j−1 n

![image 138](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile138.png>)

nH(b)

nH(a)

+

A ¯(z)ab∈{/ 0,1}

j=nH(b−1)+1

i=nH(a−1)+1

i n

![image 139](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile139.png>)

i−1 n

![image 140](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile140.png>)

f (x,y) − f ξ(i),ξ(j) dxdy,

where the latter term may be bounded using the technique of Lemma A.4, yielding

pij

ρnn2 = OP n−α/2 . Note i,j:A¯(z)

- (A.11) f ˆ∈{/ 0,1} f (x,y) dxdy − i,j:A¯(z)zizj∈{/ 0,1}


![image 141](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile141.png>)

zizj∈{/ 0,1} pii, so that

zizj∈{/ 0,1} pij+ 1≤i≤n:A¯(z)

zizj∈{/ 0,1} pij = 2 i<j:A¯(z)

zizj∈{/ 0,1} pii ≤ n−2 ni=1 Ef (ξi,ξi) = O n−1 .

E ρ−n1n−2 1≤i≤n:A¯(z)

Applying Markov’s theorem and combining the result with (A.11) then yields the stated result.

![image 142](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile142.png>)

![image 143](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile143.png>)

![image 144](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile144.png>)

![image 145](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile145.png>)

APPENDIX B: PROOF OF THEOREM 5.1 AND LEMMAS

B.1. Proof of Theorem 5.1. The proof is divided into four steps, with each the subject of a technical lemma proved in Section B.2.

Lemma B.1 yields the key ﬁrst step, which is to relate D pij A ¯zizj to D pij p ¯zizj for any z ∈ Zk, assuming that A¯zizj ∈/ {0,1}. This ensures that both terms are ﬁnite, and hence comparable. To obtain suﬃcient variance

reduction in this setting, every A¯zizj must concentrate to its mean p¯zizj, in that the ratio of mean to standard deviation must shrink. The minimum

eﬀective block sample size h2∧ ρ∧ must grow quickly enough that this takes place, even for the sparsest of all possible ﬁtted blocks.

- Lemma B.1. Assume conditions 1–3 of Theorem 5.1, and that h2∧ ρ∧ =

ω log h2∧ . Then 0 ≤ i<j:A¯zizj∈{/ 0,1} D pij A ¯zizj − D pij p ¯zizj

= OP

 

2log |Zk| + k+12 n 2 ρ ¯ i<j

![image 146](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile146.png>)

pij

, ∀z ∈ Zk.

Our next step relies on controlling Pr(A¯zizj ∈ {0,1}) uniformly in z, via

- Lemma B.2. Lemma B.2. Assume conditions 1–3 of Theorem 5.1. Then


i<j I A ¯zizj ∈ {0,1} = OP e−(h2∧)ρ∧+log(1/ρ¯)

i<j pij , ∀z ∈ Zk. This result shows that the set of all A¯zizj ∈ {0,1} has vanishing relative

cardinality relative to i<j pij, no matter which z ∈ Zk is chosen. It is a direct consequence of condition 3 of Theorem 5.1, which ensures that the

minimum ﬁtted block size is uniformly lower-bounded by h∧ = ω(1).

Lemma B.2 has two immediate consequences. First, we may apply it to conclude that

- (B.1) i<j:

A¯zizj∈{/ 0,1} pij i<j pij

![image 147](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile147.png>)

= 1 + OP e−(h2∧)ρ∧+log(1/ρ¯) , ∀z ∈ Zk.

Second, it enables us to substitute for the term i<j:A¯

zizj∈{/ 0,1} D pij p ¯zizj in Lemma B.1 as follows.

- Lemma B.3. Assume conditions 1–3 of Theorem 5.1. Then uniformly


for all z ∈ Zk, 0 ≤ i<j D pij p ¯zizj − i<j:A¯zizj∈{/ 0,1} D pij p ¯zizj

= OP e−(h2∧)ρ∧+log(1/ρ¯)

i<j pij . Thus whenever all of the above quantities are oP(1), we may combine

- Lemmas B.1 and B.3 with (B.1) to obtain our ﬁrst claimed result: for any choice of z ∈ Zk, deterministic or random, we have that


- (B.2) i<j:


A¯zizj∈{/ 0,1}D pij A ¯zizj − i<jD pij p ¯zizj i<j:A¯zizj∈{/ 0,1} pij

![image 148](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile148.png>)

(k+12 ) (n2)ρ¯ +e−(h2∧)ρ∧+log(1/ρ¯)

=OP 2 log|Zk|+

![image 149](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile149.png>)

whenever conditions 1–3 of Theorem 5.1 hold, h2∧ ρ∧ = ω log h2∧ and the argument of the right-hand side of (B.2) is oP(1). Under these condi-

tions, the numerator term of (B.2), when scaled by i<j pij, converges in probability to 0 and hence in law, whereas (B.1) converges in probability

to a non-zero constant. Thus by Slutsky’s theorem, their ratio converges in law, and hence also in probability as per (B.2). Separating terms on the left-hand side of (B.2), and then multiplying the latter numerator term by

i<j pij/ i<j pij, we obtain the ﬁrst result of result of Theorem 5.1, as stated in (5.1).

We now establish suﬃcient conditions for (B.2). We see immediately that

2 ρ∧ = ω log(1/ρ¯) must hold. Since Lemma B.1 requires that h2∧ ρ∧ = ω log h2∧ , we obtain the combined requirement

h∧

- (B.3) h2∧ρ∧ = ω max log h2∧,log(1/ρ¯) ⇐ h2∧ρ∧ = ω log n .


To see that this condition will be satisﬁed if the eﬀective sample size of every possible ﬁtted block is ω log n , ﬁrst note that h∧ ≤ n, and so log h2∧ = O log n . Now observe that because ρ∧ ≤ ρ¯, it follows that h2∧ρ∧ = ω log h2∧

implies h2∧ρ¯ = ω log h2∧ , or equivalently, log(1/ρ¯) = o log(h2∧/log h2∧) . Since h∧ ≤ n, this in turn implies log(1/ρ¯) = o log n . Thus h2∧ρ∧ = ω log n implies (B.3) as claimed.

To achieve convergence in probability, (B.2) also requires n2ρ¯ = ω log |Zk|+ k+1

2 . To simplify this requirement and obtain a suﬃcient condition, observe that log |Zk| ≤ nlog k, since Zk ⊆ {1,... ,k}n. Now write k+12 =

- k2 {1/2 + O(1)}, and let h¯ = n/k. From these simpliﬁcations we obtain ρ¯ = ω log(n/h¯)/n+h¯−2 , which is implied by h¯2ρ¯ = ω max h ¯2/n,1 log n .


Finally, observe that since the results above hold uniformly over all z ∈ Zk, they also hold for z = zˆ(A,Zk), the maximum proﬁle likelihood estimator of z. The following lemma relates this choice to its oracle counterpart z¯(p,Zk)—the best choice of z ∈ Zk—enabling us to strengthen (B.2).

Lemma B.4. Assume conditions 1 and 2 of Theorem 5.1. Then it follows from the arguments of Theorems 2 and 3 of Choi, Wolfe and Airoldi (2012) that for any zˆ(A,Zk) and z¯(p,Zk) as per (4.5) and (4.7),

(k+12 )log{(n2)/(k+12 )+1} (n2)ρ¯

0 ≤ i<j D pij p ¯zˆizˆj − D pij p ¯z¯iz¯j =OP log|Zk|+

![image 150](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile150.png>)

![image 151](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile151.png>)

(n2)ρ¯ log|Zk| i<j pij .

+ OP log(1/ρ3(∧n2) log)ρ¯ |Zk| 1+ 1+ 18

![image 152](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile152.png>)

![image 153](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile153.png>)

Since z¯(p,Zk) results in the minimum value of i<j D pij p ¯zizj , this diﬀerence is nonnegative. Its convergence in probability to 0 when suitably normalized is due to the maximizing properties of zˆ(A,Zk) and z¯(p,Zk). Thus we conclude that zˆ(A,Zk) serves as an empirical proxy for z¯(p,Zk).

To complete the proof, set z = zˆ(A,Zk) in (B.2) and combine it with

- Lemma B.4. Comparing terms, we see that the latter’s will dominate the rate of convergence, and so we upper-bound them using h¯ = n/k = ω(1),


subadditivity of the square root and the fact that n2 / k+12 ≤ h¯2. We thus obtain

i<j:A¯zˆizˆj∈{/ 0,1} D pij A ¯zˆizˆj − minz∈Zk i<j D pij p ¯zizj i<j pij

![image 154](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile154.png>)

(nh¯ )+(nh¯

+1

![image 155](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile155.png>)

![image 156](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile156.png>)

2 )log{h¯2(1+h¯−2)} (n2)ρ¯ , 2 log(ρ

−1

∧ )2 nlog(nh¯ ) (n2)ρ¯ 1+ nlog

(nh¯ )

![image 157](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile157.png>)

= OP max nlog

![image 158](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile158.png>)

![image 159](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile159.png>)

![image 160](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile160.png>)

![image 161](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile161.png>)

![image 162](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile162.png>)

![image 163](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile163.png>)

2(n2)ρ¯

9

![image 164](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile164.png>)

(nh¯ )+nh¯22 1+nh¯ log[h¯{1+o(1)}] n2ρ¯{1+o(1)} , log(1/ρ∧)

![image 165](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile165.png>)

2 log(n/h¯) nρ¯{1+o(1)} {1 + o(1)}

= OP max nlog

![image 166](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile166.png>)

![image 167](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile167.png>)

![image 168](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile168.png>)

![image 169](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile169.png>)

![image 170](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile170.png>)

= OP max

![image 171](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile171.png>)

h ¯−2(1+h/n¯ )log¯h ρ¯ ,max log

(n/h¯) nρ¯ , log(1/ρ∧)

2 log(n/h¯) nρ¯

![image 172](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile172.png>)

![image 173](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile173.png>)

![image 174](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile174.png>)

![image 175](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile175.png>)

![image 176](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile176.png>)

(n/h¯) nρ¯ max log

(n/h¯) nρ¯ ,log (1/ρ∧)

= OP max h ¯

−2{1+O(1)} log ¯h

ρ¯ , log

![image 177](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile177.png>)

![image 178](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile178.png>)

![image 179](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile179.png>)

- (B.4)


![image 180](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile180.png>)

2 log(n/h¯) nρ¯ ,

= OP max logh¯2ρ¯h¯, log(1/ρ∧)

![image 181](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile181.png>)

![image 182](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile182.png>)

where the ﬁnal line follows because log(n/h¯) = o(nρ¯) is needed for (B.4) to be oP(1), whereas ρ∧ ≤ ρ < 1/2 implies that log(1/ρ∧)2 > log(2)2 = ω log(n/h¯)/(nρ¯) . Thus we have derived the claimed rate of convergence, with a suﬃcient condition being that h¯2ρ¯ = ω max h ¯2/n,1 log3 n , since together h¯2ρ¯ = ω log n and ρ = ω log(n)3/n imply that (B.4) is oP(1).

To complete the proof of Theorem 5.1, we now re-interpret the above results under the scaled exchangeable random graph model of (2.2). Lemmas B.1–B.4 then hold for every realized value of ξ, and thus the implicit conditioning on ξ inherent to these results can be removed. Speciﬁcally, in

- Lemmas B.1 and B.4, we may marginalize (B.7) and (B.12) respectively via the law of total probability, noting that their right-hand sides do not depend on ξ. For Lemmas B.2 and B.3, we simply note that the bound of (B.8) holds for all ξ.


B.2. Proofs and auxiliary lemmas needed for Theorem 5.1. Lemma B.1. We write

D pij A ¯zizj − D pij p ¯zizj

i<j:A¯zizj ∈{/ 0,1}

p ¯zizj A¯zizj

1 − p¯zizj 1 − A¯zizj

pij log

=

+ (1 − pij)log

![image 183](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile183.png>)

![image 184](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile184.png>)

i<j:A¯zizj ∈{/ 0,1}

1 − p¯zizj 1 − A¯zizj

p ¯zizj A¯zizj

=

+ (1 − pij) log

pij log

![image 185](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile185.png>)

![image 186](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile186.png>)

a≤b:A¯ab∈{/ 0,1} i∈z−1(a), j∈z−1(b)

=

a≤b:A¯ab∈{/ 0,1}

log

p ¯ab A¯ab

![image 187](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile187.png>)

pij + log

- i∈z−1(a),
- j∈z−1(b)


=

a≤b:A¯ab∈{/ 0,1}

log

p ¯ab A¯ab

![image 188](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile188.png>)

h2abp¯ab + log

- (B.5)


h2ab D p ¯ab A ¯ab .

=

a≤b:A¯ab∈{/ 0,1}

1 − p¯ab 1 − A¯ab

![image 189](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile189.png>)

1 − p¯ab 1 − A¯ab

![image 190](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile190.png>)

(1 − pij)

- i∈z−1(a),
- j∈z−1(b)


h2ab (1 − p¯ab)

Since (B.5) is a sum of Kullback–Leibler divergences, it is nonnegative. To show its convergence when suitably normalized, we appeal to Lemma B.5 below, which implies the following under conditions 1–3 of Theorem 5.1 and the hypothesis h2∧ ρ∧ = ω log h2∧ :

For every ǫ > 0, eventually in n and with 1+/2 approaching arbitrarily

closely to 1/2,

ab∈{/ 0,1} h2ab D p ¯ab A ¯ab ≥ ǫ i<j pij

Pr maxz∈Zk a≤b:A¯

2 (k+12 ) 2 2ǫ i<j pij+12+(k+12 )

1+

≤ exp log |Zk| − ǫ i<j pij−

![image 191](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile191.png>)

![image 192](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile192.png>)

![image 193](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile193.png>)

- (B.6)

≤ exp log |Zk| − max

{ǫ i<j pij−1+(k+12 ),0} 2+12+(k+12 )/(ǫ i<j pij)

![image 194](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile194.png>)

![image 195](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile195.png>)

≤ exp log |Zk| − max

{ǫ(n2)ρ¯−1+(k+12 ),0} 2+12+(k+12 )/{ǫ(n2)ρ¯}

![image 196](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile196.png>)

![image 197](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile197.png>)

,

- (B.7)

where (B.6) follows as ǫ i<j pij ≥ 0 and (1+/2) k+12 ≥ 0 eventually in n, and (B.7) follows from condition 1 of Theorem 5.1, by which i<j pij(n) ≥

n 2 ρ ¯(n) eventually in n.

![image 198](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile198.png>)

![image 199](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile199.png>)

![image 200](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile200.png>)

![image 201](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile201.png>)

Lemma B.2. We will bound Pr(A¯zizj ∈ {0,1}) uniformly in z. Observe that for any 1 ≤ a ≤ b ≤ k, conditionally on any z ∈ Zk, we have by the arithmetic–geometric mean inequality that

Pr A ¯ab ∈ {0,1}|Z = z = Pr A ¯ab = 0|Z = z + Pr A ¯ab = 1|Z = z

=

- i∈z−1(a),
- j∈z−1(b)


(1 − pij) +

- i∈z−1(a),
- j∈z−1(b)


pij

- (B.8) ≤ (1 − p¯(z)ab)h2ab + (¯p(z)ab)h2ab .

Conditions 2 and 3 of Theorem 5.1 stipulate that for every pair (a,b) and every z ∈ Zk, eventually in n, ρ∧(n) ≤ p¯ab(n) ≤ 1 − ρ∧(n) and h∧(n) ≤ ha(n). Hence (B.8) implies that, eventually in n, for 1 ≤ a ≤ b ≤ k

![image 202](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile202.png>)

Pr A ¯ab ∈ {0,1}|Z = z ≤ (1 − ρ∧)h2ab + (1 −

√ρ∧)h2ab;

![image 203](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile203.png>)

⇒ max

a≤b

Pr A ¯ab ∈ {0,1}|Z = z ≤ 2(1 − ρ∧)(h2∧);

⇒ max

z∈Zk

max

i<j

- (B.9) Pr A ¯zizj ∈ {0,1}|Z = z ≤ 2(1 − ρ∧)(h2∧).


{ǫ i<j pij−1+(k+12 ),0} 2ǫ i<j pij+12+(k+12 )

≤ exp log |Zk| − ǫ i<j pij max

![image 204](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile204.png>)

![image 205](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile205.png>)

Since the conditional probability Pr A ¯zizj ∈ {0,1}|Z = z is upperbounded by (B.9) uniformly for every value of z ∈ Zk, this same bound also

holds after marginalizing out Z. Thus, eventually in n,

- (B.10) Pr A ¯zizj ∈ {0,1} ≤ 2(1 − ρ∧)(h2∧). Applying Markov’s inequality, we see that for any ǫ > 0, eventually in n,


Pr 



i<j

I A ¯zizj ∈ {0,1} ≥ ǫ

i<j

pij

Pr A ¯zizj ∈ {0,1} ǫ i<j pij

 ≤ i<j

![image 206](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile206.png>)

n 2 2(1 − ρ∧)(h2∧)

≤

![image 207](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile207.png>)

ǫ i<j pij ≤

2(1 − ρ∧)(h2∧) ǫρ¯

![image 208](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile208.png>)

2exp − h2∧ ρ∧ ǫρ¯

≤

![image 209](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile209.png>)

exp − h2∧ ρ∧ + log (1/ρ¯) (ǫ/2)

=

,

![image 210](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile210.png>)

where the second inequality follows directly from (B.10), the third inequality follows from condition 1 of Theorem 5.1, by which i<j pij(n) ≥ n2 ρ ¯(n) eventually in n, and the ﬁnal inequality follows from the fact that log (1 − ρ∧)(h2∧) = h2∧ log(1 − ρ∧) ≤ − h2∧ ρ∧.

![image 211](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile211.png>)

![image 212](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile212.png>)

![image 213](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile213.png>)

![image 214](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile214.png>)

Lemma B.3. First, we express the term of interest as a sum of nonnegative random variables:

D pij p ¯zizj −

D pij p ¯zizj =

i<j:A¯zizj∈{/ 0,1}

i<j

D pij p ¯zizj I(A¯zizj ∈ {0,1}).

i<j

To show the claimed convergence in probability, we write 0 ≤

D pij p ¯zizj I(A¯zizj ∈ {0,1})

i<j

= −

i<j

pij log p ¯zizj + (1 − pij)log 1 − p¯zizj I(A¯zizj ∈ {0,1})

≤ −

i<j

{pij log (pij) + (1 − pij)log (1 − pij)} I(A¯zizj ∈ {0,1})

+

i<j

pij log p ¯zizj + (1 − pij)log 1 − p¯zizj I(A¯zizj ∈ {0,1})

{pij log (¯p(z)ab) + (1 − pij) log (1 − p¯(z)ab)} I(A¯zizj ∈ {0,1})

= −

a≤b i∈z−1(a), j∈z−1(b)

h2ab {p¯(z)ab log (¯p(z)ab) + (1 − p¯(z)ab) log (1 − p¯(z)ab)} I(A¯ab ∈ {0,1})

= −

a≤b

h2ab(log 2)I(A¯ab ∈ {0,1})

≤

a≤b

I(A¯zizj ∈ {0,1}).

= (log 2)

i<j

The result then follows from Lemma B.2, which establishes that for every z ∈ Zk, we have i<j I(A¯zizj ∈ {0,1}) = OP e−(h2∧)ρ∧+log(1/ρ¯)

i<j pij under conditions 1–3 of Theorem 5.1.

![image 215](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile215.png>)

![image 216](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile216.png>)

![image 217](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile217.png>)

![image 218](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile218.png>)

Lemma B.4. In the notation of Choi, Wolfe and Airoldi (2012), deﬁne for any ﬁxed z ∈ Zk

L¯(z) =

pij log p¯zizj + (1 − pij)log 1 − p¯zizj ;

i<j

L¯(z) = argmin

D pij p ¯zizj .

⇒ z¯(p,Zk) = argmax

z∈Zk i<j

z∈Zk

where the implication follows directly from the deﬁnition of the “oracle” MPLE in z¯(p,Zk) in (4.7). Thus

D pij p ¯zˆizˆj − D pij p ¯z¯iz¯j = L¯(¯z) − L¯(ˆz), z,¯ zˆ ∈ Zk.

0 ≤

i<j

By construction, since z¯(p,Zk) maximizes L¯(z) over Zk, this diﬀerence is nonnegative. Similarly, from (4.5) we see that zˆ(A,Zk) maximizes L(A;z)

over Zk, and so L(A;zˆ) − L(A;z¯) ≥ 0. Hence, 0 ≤ L¯(¯z) − L¯(ˆz) ≤ L¯(¯z) − L¯(ˆz) + {L(A;zˆ) − L(A;z¯)} , z,¯ zˆ ∈ Zk

= L¯(¯z) − L(A;z¯) + L(A;zˆ) − L¯(ˆz)

- (B.11) ≤ L ¯(¯z) − L(A;z¯) + L(A;zˆ) − L¯(ˆz) ,

and so the result will follow from (B.11) if we can show that L ¯(¯z) − L(A;z¯) and L(A;zˆ) − L¯(ˆz) both converge in probability to zero when suitably renormalized. We accomplish this in the manner of Choi, Wolfe and Airoldi (2012, Theorem 2), who establish that maxz∈Zk L ¯(z) − L(A;z) / i<j pij converges as required. Since this result holds for the maximum over all z ∈ Zk, then it must also hold for both zˆ and z¯, and we can therefore apply this same result twice.

In particular, Theorem 2 of Choi, Wolfe and Airoldi (2012) shows that

for any ﬁxed n, whenever maxij logit p¯zizj is ﬁnite for all z ∈ Zk, it holds that for all nonempty Zk ⊆ {1,... ,k}n and any ǫ > 0,

- (B.12) Pr


pij

L(A;z) − L¯(z) ≥ 2ǫ

max



z∈Zk

i<j

≤ |Zk|exp k+12 log n2 / k+12 + 1 − ǫ i<j pij

ǫ i<j pij 2/2 i<j pij logit p¯zizj 2 + (1/3) ǫ i<j pij maxi<j logit p¯zizj

2exp −

+

![image 219](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile219.png>)

z∈Zk

From condition 2 of Theorem 5.1, we have that each pij(n) ∈ (0,1) eventually in n. This implies that maxij logit p¯zizj(n) will eventually be ﬁnite for all z ∈ Zk, and thus (B.12) holds eventually in n.

To simplify the right-hand side of (B.12), we upper-bound logit p¯zizj via maxi<j logit p¯zizj , which allows a factor of i<j pij to be canceled:

.

Pr 

pij

L(A;z) − L¯(z) ≥ 2ǫ

max

 ≤ |Zk|

z∈Zk

i<j

exp k+12 log n2 / k+12 + 1 − ǫ i<j pij

(ǫ2/2) i<j pij maxi<j logit p¯zizj 2 + (ǫ/3)maxi<j logit p¯zizj

2exp −

+

![image 220](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile220.png>)

z∈Zk

.

Next, we upper-bound maxi<j logit p¯zizj uniformly in z via maxz∈Zk maxi<j logit p¯zizj . This highlights the importance of bounding

pij away from 0 and 1. We may now sum over z ∈ Zk to obtain

Pr 

pij

L(A;z) − L¯(z) ≥ 2ǫ

max

 ≤ |Zk|

z∈Zk

i<j

exp 

pij

 k + 1 2

n 2

k + 1 2

log

/

+ 1 − ǫ



i<j

2/2) i<j pij

+2|Zk| exp − (ǫ

.

![image 221](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile221.png>)

[maxz∈Zk{maxi<j|logitp¯zizj|}]2+(ǫ/3) maxz∈Zk{maxi<j|logitp¯zizj|}

Condition 2 stipulates that every p¯zizj satisﬁes ρ∧(n) ≤ p¯zizj(n) ≤ 1 − ρ∧(n) eventually in n, so

![image 222](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile222.png>)

p ¯zizj(n) 1 − p¯zizj(n)

max

max

logit p¯zizj(n) = max z∈Zk

max

log

![image 223](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile223.png>)

i<j

i<j

z∈Zk

1 − p¯zizj(n) p¯zizj(n) ≤ max

p ¯zizj(n) 1 − p¯zizj(n)

= max

max

,log

max log

![image 224](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile224.png>)

![image 225](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile225.png>)

i<j

z∈Zk

![image 226](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile226.png>)

1 − ρ∧(n) ρ∧(n)

1 − ρ∧(n) ρ∧(n) ≤ log {1/ρ∧(n)} ,

,log

max log

max

![image 227](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile227.png>)

![image 228](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile228.png>)

![image 229](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile229.png>)

i<j

z∈Zk

which is ﬁnite, as condition 1 speciﬁes that 0 < ρ∧(n) < 1/2 for all n.

Finally, condition 1 of Theorem 5.1 ensures that n2 ρ ¯(n) ≤ i<j pij(n) eventually in n. Thus, recalling (B.11), we obtain the claimed result, since we have shown that for all n suﬃciently large,

Pr

pij

L(A;z) − L¯(z) ≥ 2ǫ

max



z∈Zk

i<j

≤ exp log |Zk| + k+12 log n2 / k+12 + 1 − ǫ n2 ρ ¯

n 2 ρ ¯

ǫ2/2 1 + (ǫ/3)/log (1/ρ∧) ≤ 4exp log |Zk|

+ 2exp log |Zk| −

![image 230](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile230.png>)

![image 231](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile231.png>)

log (1/ρ∧)2

(n2)ρ¯

+max k+12 log n2 / k+12 + 1 − ǫ n2 ρ, ¯ −

ǫ2/2

1+(ǫ/3)/log(1/ρ∧) .

![image 232](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile232.png>)

![image 233](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile233.png>)

log(1/ρ∧)2

![image 234](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile234.png>)

![image 235](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile235.png>)

![image 236](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile236.png>)

![image 237](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile237.png>)

Lemma B.5. Assume conditions 1–3 of Theorem 5.1 and the hypothesis

h∧

2 ρ∧ = ω log h2∧ , which together ensure that for every z ∈ Zk,

- (B.13)

![image 238](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile238.png>)

log h2ab /h2ab min (¯pab,1 − p¯ab)/√p¯ab

![image 239](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile239.png>)

![image 240](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile240.png>)

= o(1), 1 ≤ a ≤ b ≤ k.

Then for every ǫ > 0, we have eventually in n that

Pr

max

z∈Zk

a≤b:A¯ab∈{/ 0,1}

h2ab D p ¯ab A ¯ab ≥ ǫ

 ≤ exp

  log |Zk| −

ǫ − 12+ k+12

![image 241](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile241.png>)

2

![image 242](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile242.png>)

2ǫ + 12+ k+12

![image 243](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile243.png>)

  ,

with 1+/2 approaching arbitrarily closely to 1/2 from above, at the rate given by (B.13).

Proof. Observe that for any ﬁxed z ∈ Zk, we may re-express a≤b:A¯ab∈{/ 0,1} h2ab D p ¯ab A ¯ab as a sum of the terms whose moments will

be bounded by Lemma B.6:

a≤b:A¯ab∈{/ 0,1}

h2ab D p ¯ab A ¯ab =

a≤b

g h2abA¯ab , z ∈ Zk ﬁxed.

Here, setting Xn = h2abA¯ab in (B.17) of Lemma B.6, we deﬁne g h2abA¯ab as g h2abA¯ab

=

h2ab p ¯ab log Ap ¯¯ab

![image 244](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile244.png>)

ab

+ (1 − p¯ab)log 1 1−−Ap¯¯ab

![image 245](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile245.png>)

ab

if h2abA¯ab ∈ {1,... ,h2ab − 1}, 0 if h2abA¯ab ∈ {0,h2ab}.

By hypothesis, the conditions of Lemma B.6 apply for all 1 ≤ a ≤ b ≤ k and every z ∈ Zk, and so each g h2abA¯ab behaves like a chi-square variate on 1 degree of freedom in terms of its mth moment where m = 1,2,...

- (B.14)

E g h2abA¯ab m ≤

Γ m + 12 √π

![image 246](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile246.png>)

![image 247](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile247.png>)

![image 248](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile248.png>)

 



1 + O

 

![image 249](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile249.png>)

log h2ab /h2ab min (¯pab,1 − p¯ab) /√p¯ab

![image 250](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile250.png>)

![image 251](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile251.png>)

 

 



.

Controlling the moments of g h2abA¯ab enables us to apply a Bernstein concentration inequality due to Birge´ and Massart (1998, Lemma 8). To do so requires the existence of constants v2 and c such that

- (B.15) k+12 −1 a≤b


E g h2abA¯ab m ≤

m! 2

v2cm−2, m = 2,3,... .

![image 252](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile252.png>)

By hypothesis,

![image 253](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile253.png>)

 

 

 

 

log h2ab /h2ab min (¯pab,1 − p¯ab)/√p¯ab

Γ m + 12 √π

Γ m + 12 √π {1 + o(1)}

![image 254](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile254.png>)

![image 255](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile255.png>)

1 + O

=

![image 256](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile256.png>)

![image 257](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile257.png>)

![image 258](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile258.png>)

![image 259](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile259.png>)

![image 260](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile260.png>)

![image 261](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile261.png>)





- 3

![image 262](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile262.png>)

- 4


+ δ,

<

eventually in n, for every δ > 0. Thus we ﬁx v2 arbitrarily close to 3/4, and write v2 = 3+/4. To ensure that (B.15) is satisﬁed for each m, we then let c = 1.

We can see from (B.14) that these choices of v2,c yield

Γ m + 12 √π {1 + o(1)} , m = 2,3,...

−1

E g h2abA¯ab m ≤

![image 263](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile263.png>)

k+1 2

![image 264](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile264.png>)

![image 265](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile265.png>)

a≤b

Γ(m + 1) √π

, eventually in n,

<

![image 266](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile266.png>)

![image 267](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile267.png>)

m! 2

v2cm−2, m = 2,3,... ,

≤

![image 268](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile268.png>)

and thus (B.15) holds eventually in n. Lemma 8 of Birge´ and Massart (1998) then shows that for

Y =

g h2abA¯ab , with z ∈ Zk ﬁxed,

a≤b

the following concentration inequality holds for any ǫ > 0:

k+1

2 ǫ2/2 v2 + cǫ

Pr Y − EY ≥ k+12 ǫ ≤ exp −

![image 269](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile269.png>)

(ǫ − EY )2/2 k+1

⇒ Pr (Y ≥ ǫ) ≤ exp −

- (B.16) .


![image 270](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile270.png>)

2 v2 + c(ǫ − EY )

Observe that since EY ≥ 0, (B.16) still holds if we replace EY with an upper bound u, because for any u ≥ EY ≥ 0, the event Y − u ≥ ǫ implies the event Y − EY ≥ ǫ, and so Pr (Y − u ≥ ǫ) ≤ Pr (Y − EY ≥ ǫ). Thus, we may substitute the eventual upper bound u = (1+/2) k+12 ≥ EY from (B.14) into (B.16), where (1+/2) is arbitrarily close to 1/2. Substituting (1+/2) k+12 in place of EY in (B.16), along with the constants v2 = 3+/4 and c = 1, we see that for any ǫ > 0, eventually in n,

Pr(Y ≥ ǫ) ≤ exp

2

  −

  .

ǫ − 12+

k+1 2

/2

![image 271](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile271.png>)

![image 272](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile272.png>)

- 3+

![image 273](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile273.png>)

- 4 + ǫ − 12+


k+1 2

k+1 2

![image 274](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile274.png>)

Simplifying this expression and applying a union bound over all z ∈ Zk then yields the stated result.

![image 275](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile275.png>)

![image 276](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile276.png>)

![image 277](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile277.png>)

![image 278](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile278.png>)

- Lemma B.6. Let Xn denote a sequence of Poisson–Binomial variates,


each with mean µn, and deﬁne

- (B.17)

g(Xn) =

µn log X µn

![image 279](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile279.png>)

n

+ (n − µn)log n n−−Xµn

![image 280](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile280.png>)

n

if Xn ∈ {1,2,... ,n − 1}, 0 if Xn ∈ {0,n}.

If min(µn,n − µn) = ω µn log{max (µn,n − µn)} , then the moments of g(Xn) satisfy for m = 1,2,...

![image 281](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile281.png>)

E{g(Xn)m} ≤

Γ m + 21 √π

![image 282](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile282.png>)

![image 283](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile283.png>)

![image 284](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile284.png>)

1 + O

![image 285](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile285.png>)

µn log{max(µn,n − µn)} min (µn,n − µn)

![image 286](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile286.png>)

.

Proof. To simplify notation, we suppress the dependence of X and µ on n throughout; note, however, that m ∈ {1,2,...} is ﬁxed and so does not depend on n. Using the fact that g(0) = g(n) = 0, we write

E{g(X)m} =

n

k=0

g(k)m Pr (X = k), m = 1,2,...

=

n−1

k=1

g(k)m Pr(X = k)

= 



k1

k=1

+

k2−1

k=k1+1

+

n−1

k=k2



- (B.18) g(k)m Pr (X = k),

with k1,k2 chosen to balance the contribution of the central sum in (B.18) with that of the tail sums in (B.18):

- (B.19a) k1 = max 1, µ − 2µ(m + δ)log µ ,


![image 287](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile287.png>)

![image 288](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile288.png>)

- (B.19b) k2 = min µ + 2µ(m + δ)log(n − µ) ,n − 1


for any ﬁxed δ > 0. Since g(k) ≥ 0 for every value of k, (B.18) implies that

k1

k2−1

E{g(X)m} ≤ max

g(k)m

g(k)m Pr (X = k)

Pr (X = k) +

1≤k≤k1

k=1

k=k1+1

n−1

g(k)m

+ max

Pr (X = k)

k2<k<n

k=k2

k2−1

g(k)m Pr (X ≤ k1) +

g(k)m Pr (X = k)

≤ max

1≤k≤k1

k=k1+1

- (B.20)

We now bound the two tail terms in (B.20). From the deﬁnitions of k1 and k2 in (B.19), our hypothesis min (µ,n − µ) = ω µlog{max (µ,n − µ)} implies that eventually in n,

![image 289](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile289.png>)

- (B.21a) k1 = µ − ǫ1, ǫ1 ≥ 2µ(m + δ)log(µ),

![image 290](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile290.png>)

- (B.21b) k2 = µ + ǫ2, ǫ2 ≥ 2µ(m + δ)log(n − µ).

![image 291](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile291.png>)

Now recall the standard Chernoﬀ bounds for Poisson–Binomial variates, which hold for any ǫ > 0:

Pr(X ≤ µ − ǫ) ≤ exp −

ǫ2 2µ

![image 292](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile292.png>)

,

Pr(X ≥ µ + ǫ) ≤ exp −

ǫ2 2µ

![image 293](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile293.png>)

1 +

ǫ 3µ

![image 294](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile294.png>)

−1

.

Applying these bounds to X ≤ µ − ǫ1 and X ≥ µ + ǫ2, respectively, we conclude that eventually in n,

Pr (X ≤ k1) ≤ µ−(m+δ),

(B.22a)

Pr (X ≥ k2) ≤ exp −(m + δ)log(n − µ) 1 +

√

![image 295](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile295.png>)

- 2(m+δ)

![image 296](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile296.png>)

- 3


![image 297](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile297.png>)

log(n−µ) µ

![image 298](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile298.png>)

−1

- (B.22b) = (n − µ)−(m+δ) 1 + O log(nµ−µ) ,




g(k)m Pr (X ≥ k2).

+ max

k2<k<n

![image 299](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile299.png>)

![image 300](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile300.png>)

![image 301](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile301.png>)

with the hypothesis min(µ,n − µ) = ω µlog{max(µ,n − µ)} implying that µ = ω log(n − µ) .

This hypothesis also implies that 1 < µ < n−1 eventually in n. Since g(k) is strictly decreasing on 1 ≤ k < µ and strictly increasing on µ < k ≤ n −1, we have for m = 1,2,... that max1≤k≤k1 g(k)m = g(1)m ≤ (µlog µ)m and maxk2<k<n g(k)m = g(n − 1)m ≤ {(n − µ)log(n − µ)}m eventually in n.

Combining these two upper bounds with (B.20) and (B.22), we conclude that, eventually in n,

- (B.23) E{g(X)m} ≤ log(µ)mµ−δ +

k2−1

k=k1+1

g(k)m Pr(X = k)

+ log(n − µ)m(n − µ)−δ 1 + O

![image 302](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile302.png>)

log(n − µ) µ

![image 303](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile303.png>)

.

As a ﬁnal step, we bound kk2=−k1

1+1 g(k)m Pr (X = k) in (B.23). Recognizing g(k) from (B.17) as a scaled form of a Bernoulli Kullback–Leibler divergence, we have by the Taylor expansion of Lemma C.9 that

- (B.24) g(k) ≤

n(k − µ)2 2µ(n − µ)

![image 304](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile304.png>)

· 1 + 23 min(|kµ,n−µ−| µ) 1 − min(|kµ,n−µ−| µ) −3 , |k − µ| < min(µ,n − µ).

![image 305](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile305.png>)

![image 306](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile306.png>)

![image 307](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile307.png>)

Now, (B.21) implies that for all n suﬃciently large, |k − µ| ≤ 2µ(m + δ)log{max(µ,n − µ)} + 1 whenever k ∈ {k1,... ,k2}, and so

![image 308](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile308.png>)

|k − µ| min (µ,n − µ) ≤ 2(m + δ)

![image 309](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile309.png>)

![image 310](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile310.png>)

![image 311](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile311.png>)

µlog{max(µ,n − µ)} min (µ,n − µ)

![image 312](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile312.png>)

· 1 +

1 2µ(m + δ)log{max(µ,n − µ)}

![image 313](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile313.png>)

![image 314](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile314.png>)

= O

![image 315](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile315.png>)

µlog{max(µ,n − µ)} min(µ,n − µ)

![image 316](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile316.png>)

- (B.25) , k1 ≤ k ≤ k2,


![image 317](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile317.png>)

since the hypothesis min(µ,n − µ) = ω µlog{max (µ,n − µ)} implies that µ = ω(log n). From (B.25), we see that this hypothesis also implies that the Lagrange remainder term in (B.24) is o(1).

Therefore, we may use the Taylor expansion of (B.24) to obtain the upper bound

k2−1

g(k)m Pr (X = k)

k=k1+1

k2−1

m

m

n(k − µ)2 2µ(n − µ)

|k − µ| min(µ,n − µ)

1 + O

≤

![image 318](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile318.png>)

![image 319](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile319.png>)

k=k1+1

m

![image 320](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile320.png>)

µlog{max(µ,n − µ)} min(µ,n − µ)

n 2µ(n − µ)

=

- (B.26)


1 + O

![image 321](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile321.png>)

![image 322](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile322.png>)

k2−1

(k − µ)2m Pr (X = k) .

·

k=k1+1

Pr (X = k)

Noting that each term appearing in the sum of (B.26) is nonnegative, we see that

 (k − µ)2m Pr (X = k)

 

k2−1

k1

k2−1

n

(k − µ)2m Pr(X = k) ≤

+

+

k=k2

k=k1+1

k=0

k=k1+1

= E (X − µ)2m , m = 1,2,... ,

with each E (X − µ)2m an even-order central moment of the Poisson– Binomial random variable X.

Shaked and Shanthikumar (1994, Theorem 3.A.37) show that

Y ∼ Binomial(n,µ/n) is larger than X in the convex order, meaning that Eφ(X) ≤ Eφ(Y ) holds for all convex functions φ : R → R for which the expectations exist. Since the even-order central moments E(Y − µ)2m exist and are convex for all m = 1,2,..., it follows that

E (X − µ)2m ≤ E (Y − µ)2m , m = 1,2,... ,

where X is the Poisson–Binomial variate under study and the random variable Y ∼ Binomial(n,µ/n) has a matched mean.

As observed by Romanovsky (1923), the central moments of the Binomial distribution admit a recurrence relation that allows each of their leadingorder terms to be expressed in closed form:

with

E (Y − µ)2m = (2m − 1)!!(varY )m 1 + O

1 varY

![image 323](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile323.png>)

,

µ(n − µ) n

varY =

![image 324](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile324.png>)

max (µ,n − µ) n

=

![image 325](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile325.png>)

min (µ,n − µ)

= Θ min (µ,n − µ) . Thus we have from (B.26) that

k2−1

m

![image 326](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile326.png>)

µlog{max(µ,n − µ)} min(µ,n − µ)

n 2µ(n − µ)

g(k)m Pr(X = k) ≤

1 + O

![image 327](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile327.png>)

![image 328](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile328.png>)

k=k1+1

m

1 min (µ,n − µ)

µ(n − µ) n

1 + O

· (2m − 1)!!

![image 329](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile329.png>)

![image 330](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile330.png>)

![image 331](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile331.png>)

µlog{max(µ,n − µ)} min(µ,n − µ)

(2m − 1)!! 2m

- (B.27) ,


1 + O

=

![image 332](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile332.png>)

![image 333](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile333.png>)

where the combination of the O(·) terms follows because µ = ω(log n) is implied by the hypothesis that min(µ,n − µ) = ω µlog{max(µ,n − µ)} . Finally, combining (B.23) with (B.27), and noting that (2m − 1)!!/2m = Γ(m + 1/2)/√π, we obtain for any choice of δ > 0 and every ﬁxed m = 1,2,... that

![image 334](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile334.png>)

![image 335](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile335.png>)

![image 336](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile336.png>)

µlog{max(µ,n − µ)} min(µ,n − µ)

Γ(m + 1/2) √π

E {g(X)m} ≤ log(µ)mµ−δ+

1 + O

![image 337](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile337.png>)

![image 338](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile338.png>)

![image 339](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile339.png>)

![image 340](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile340.png>)

log(n − µ) µ

+ log(n − µ)m(n − µ)−δ 1 + O

,

![image 341](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile341.png>)

eventually in n. To complete the proof, observe that δ > 0 can be chosen for each m such that the terms log(µ)mµ−δ and log(n − µ)m(n − µ)−δ tend to 0 arbitrarily quickly in n, thus yielding the theorem.

![image 342](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile342.png>)

![image 343](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile343.png>)

![image 344](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile344.png>)

![image 345](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile345.png>)

APPENDIX C: PROOF OF THEOREM 6.1 AND LEMMAS C.1. Proof of Theorem 6.1. Proof. Recall that our aim is to establish (6.3), which asserts that

minz∈Zk i<j D pij p ¯zizj = OP n−α + (n/h∨)−2α · i<j pij . We will do so by upper-bounding this risk in terms of a random community assign-

ment vector z˜∗ that depends on the ordered sample {ξ(i)}ni=1 of Uniform(0,1) variates that index the graphon f. Convergence of this ordered sample to

the lattice (n + 1)−1(1,... ,n), coupled with the uniform continuity of f, as enforced by a H¨older assumption, will yield the result.

We proceed as follows. Let z∗ be any minimizer of i<j D pij p ¯zizj

over the set Zk of admissible blockmodel assignment vectors, and deﬁne z˜i∗ = Hk,z−1∗ {(i)−1/n}, with (i)−1 the rank of ξi from smallest to largest. Thus z˜∗ = Hk,z−1∗ ◦ (·)−1, and therefore by construction, condition 3 of the theorem ensures that z˜∗ ∈ Zk for any z∗ ∈ Zk. Hence we have the following upper bound:

D pij p ¯zizj ≤

min

z∈Zk

i<j

iz˜∗j =

D pij p ¯z˜∗

i<j

D p(i)(j) p ¯z˜∗

(i)z˜∗(j) ,

i<j

with equality stemming from the fact that the sum over all i < j is invariant to permutation, and hence we may re-order it in accordance with the ordered sample {ξ(i)}ni=1.

Conditions 1 and 2 of the theorem then imply that Lemma C.1 holds, thereby completing the proof.

![image 346](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile346.png>)

![image 347](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile347.png>)

![image 348](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile348.png>)

![image 349](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile349.png>)

C.2. Auxiliary lemmas needed for Theorem 6.1.

Lemma C.1. If rn → 0 in Lemma C.4, then

i<jD p(i)(j) p ¯z˜(i)z˜(i) i<j ρnf(ξi,ξj)

= OP rn2 .

![image 350](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile350.png>)

Proof. This follows from via Slutsky’s theorem, after combining the results of Lemmas C.2 and C.3:

−1

n 2

i<j f (ξi,ξj) = (0,1)2 f (x,y) dxdy + OP n−1/2 , ρn n2 −1 i<j D p(i)(j) p ¯z˜(i)z˜(i) = OP rn2 .

Since the denominator term converges in probability to a constant, it also converges in law. Thus by Slutsky’s theorem, the ratio converges in law to a constant, and hence it also converges in probability.

![image 351](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile351.png>)

![image 352](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile352.png>)

![image 353](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile353.png>)

![image 354](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile354.png>)

Lemma C.2. Let f be a symmetric measurable function on (0,1)2 with

bounded magnitude, and let {ξi}ni=1 be a random sample of Uniform(0,1) variates. Then

n 2

−1

i<j f (ξi,ξj) = (0,1)2 f (x,y) dxdy + OP n−1/2 .

Proof. The result follows from Chebyshev’s inequality. We obtain the necessary moments as

E n2 −1 i<j f (ξi,ξj) = (0,1)2 f (x,y) dxdy,

- (C.1)

Since |f (x,y)| is bounded by hypothesis, |cov {f (ξi,ξj),f (ξk,ξl)}| is also bounded. Furthermore, since elements of {ξ1,... ,ξn} are independent, any individual covariance term appearing in the sum of (C.1) can be nonzero only if (i = k) ∪ (i = l) ∪ (j = k) ∪ (j = l). Thus we conclude that

var n2 −1 i<j f (ξi,ξj)

= O n2

−2

i<j k<l {I(i = k) + I(i = l) + I(j = k) + I (j = l)} .

The right-hand side of this expression is O n−1 , and so Chebyshev’s inequality yields the result.

![image 355](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile355.png>)

![image 356](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile356.png>)

![image 357](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile357.png>)

![image 358](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile358.png>)

Lemma C.3. Whenever rn → 0 in (C.3) from Lemma C.4, we have that ρn n2 −1 i<j D p(i)(j) p ¯z˜(i)z˜(i) = OP rn2 .

Proof. The result follows by combining Lemmas C.4 and C.8. From Lemma C.4, we have directly that

ρ−n1 D p(i)(j) p ¯z˜(i)z˜(i) = ρ−n1 D p(i)(j) ρnf¯ ξ(i),ξ(j) + OP rn2 under the hypothesis that rn → 0, and thus

ρn n2 −1 i<j D p(i)(j) p ¯z˜(i)z˜(i)

= ρn n2 −1 i<j D p(i)(j) ρnf¯ ξ(i),ξ(j) + OP rn2

= ρn n2 −1 i<j D ρnf (ξi,ξj) ρnf¯(ξi,ξj) +OP rn2 ,

after re-ordering the sum and applying the identity pij = ρnf (ξi,ξj). The right-hand side of this expression is treated by Lemma C.8, which shows whenever max1≤a,b≤k ∆ab = o(1) in (C.20) that

- (C.2) ρn n2 −1 E i<j


var n2 −1 i<j f (ξi,ξj) = n2 −2 i<j k<l cov {f (ξi,ξj) ,f (ξk,ξl)} .

D ρnf (ξi,ξj) ρnf¯(ξi,ξj)

ρnM2 √2 max1≤a≤k ha/n 2α {1 + o(1)} min1≤a,b≤k min ρnf¯ab,1 − ρnf¯ab

![image 359](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile359.png>)

=

.

![image 360](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile360.png>)

Since (C.21) of Lemma C.8 upper-bounds each ∆ab by the ratio of terms ρnM √2 maxa ha/n α/min ρnf¯ab,1 − ρnf¯ab , we see that ∆ab = O (rn), and so the hypothesis rn → 0 is suﬃcient to imply that maxa,b ∆ab = o(1).

![image 361](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile361.png>)

We also see that the main term in (C.2) is O rn2 , since the quantity min1≤a,b≤k min f ¯ab,ρ−n1 − f¯ab ≤ sup(x,y)∈(0,1)2 f (x,y), and thus after applying Markov’s inequality via (C.2), we obtain the result.

![image 362](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile362.png>)

![image 363](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile363.png>)

![image 364](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile364.png>)

![image 365](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile365.png>)

- Lemma C.4. Let f be a symmetric H¨olderα(M) function on (0,1)2, with

f¯(x,y;h) = f¯H−1(x)H−1(y) its stepfunction approximation, and let {ξ(i)}ni=1 be an ordered sample of independent Uniform(0,1) random variables. As-

sume ρn > 0 and 0 < ρnf (x,y) < 1 everywhere on (0,1)2. Then for any z˜ such that Πz˜ = (·)−1, with (i)−1 denoting the rank of ξi from smallest to largest, we have

ρ−n1 D p(i)(j) p ¯z˜(i)z˜(i) = ρ−n1 D p(i)(j) ρnf¯ ξ(i),ξ(j) + OP rn2 whenever

(C.3) rn =

ρnM 2α/2 2n1α/−α2 + 2

![image 366](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile366.png>)

(max1≤a≤k ha)α+1+2α I(z˜(i)=˜z(j))

![image 367](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile367.png>)

nα

![image 368](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile368.png>)

min1≤a,b≤k min ρnf¯ab,1 − ρnf¯ab → 0.

Proof. We apply Taylor’s theorem, after ﬁrst establishing via Markov’s inequality that

(C.4) δn =

p¯z˜(i)z˜(i) − ρnf¯ ξ(i),ξ(j) min ρnf¯ ξ(i),ξ(j) ,1 − ρnf¯ ξ(i),ξ(j)

![image 369](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile369.png>)

= OP (rn).

To show (C.4), we lower-bound the denominator of δn, and then apply

- Lemma C.5 to upper-bound E|δn|:


ρn ρ−n1p¯z˜(i)z˜(i) − f¯ ξ(i),ξ(j) min1≤a,b≤k min ρnf¯ab,1 − ρnf¯ab ≤ rn.

E|δn| ≤ E

![image 370](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile370.png>)

We now apply Taylor’s theorem to expand D p(i)(j) p ¯z˜(i)z˜(i) as a function of δn about the point ρnf¯ ξ(i),ξ(j) . Writing p¯(i)(j) for ρnf¯ ξ(i),ξ(j) ,

we have that if rn → 0, then

p ¯z˜(i)z˜(i) − p¯(i)(j) p¯(i)(j) 1 − p¯(i)(j)

- D p(i)(j) p ¯z˜(i)z˜(i) − D p(i)(j) p ¯(i)(j) = p ¯(i)(j) − p(i)(j)


![image 371](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile371.png>)

2

p ¯z˜(i)z˜(i) − p¯(i)(j) p¯(i)(j) 1 − p¯(i)(j)

- 1

![image 372](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile372.png>)

- 2


+ oP ρnrn2

p(i)(j) 1 − 2¯p(i)(j) + p¯2(i)(j)

+

![image 373](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile373.png>)

p(i)(j) 1 − 2¯p(i)(j) + p¯2(i)(j) 2 max p ¯(i)(j),1 − p¯(i)(j) 2

p ¯(i)(j) − p(i)(j) max p ¯(i)(j),1 − p¯(i)(j)

δn2 + oP ρnrn2

=

δn +

![image 374](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile374.png>)

![image 375](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile375.png>)

- (C.5)

where the terms in (C.5) follow because, by Lemma C.6, p ¯(i)(j) − p(i)(j) ≤ ρnM √2 max1≤a≤k ha/n α, since f ∈ H¨olderα(M); also, since 0 < p¯(i)(j) < 1, we have that 1 − 2¯p(i)(j) /max p ¯(i)(j),1 − p¯(i)(j) < 1; and likewise we have max p ¯(i)(j),1 − p¯(i)(j) ≥ 1/2. Since f ∈ H¨olderα(M) is bounded by hypothesis, the right-hand side of (C.5) is OP ρnrn2 . The lemma follows from multiplying both sides of (C.5) by ρ−n1.

![image 376](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile376.png>)

![image 377](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile377.png>)

![image 378](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile378.png>)

![image 379](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile379.png>)

![image 380](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile380.png>)

Lemma C.5. Let f be a symmetric H¨olderα(M) function on (0,1)2, and

let {ξ(i)}ni=1 be an ordered sample of independent Uniform(0,1) variates. Let ρn > 0 and deﬁne for zi = H−1{Πz(i)/n}:

- (C.6)

p¯(z)ab =

1 h2ab

![image 381](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile381.png>)

nH(b)

j=nH(b−1)+1

nH(a) I(a =b)+(j−1) I(a=b)

i=nH(a−1)+1

ρnf ξΠ−1

z (i),ξΠ−1

z (j) .

Then for any z˜ such that Πz˜ = (·)−1, with (i)−1 denoting the rank of ξi from smallest to largest, we have

- (C.7) E ρ−n1 p¯z˜(i)z˜(j)−f¯ ξ(i),ξ(j)

≤ M 2α/2

21−α nα/2

![image 382](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile382.png>)

+

2(max1≤a≤k ha)α+1+2α I z ˜(i)= ˜z(j) nα

![image 383](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile383.png>)

.

Proof. Deﬁne the k × k matrix f˜ such that ρ−n1 p¯(˜z)ab = f˜(˜z)ab + OP n−α/2 when f is α-H¨older:

- (C.8)


< 2ρnM √2 max1≤a≤k ha/n α |δn| + 3ρn sup(x,y)∈(0,1)2 f (x,y) δn2 + oP ρnrn2 ,

![image 384](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile384.png>)

nH(b)

nH(a) I(a =b)+(j−1) I(a=b)

1 h2ab

−1

−1

z {(i)−1} n+1 , Π

z {(j)−1} n+1 .

f Π

f˜(z)ab =

![image 385](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile385.png>)

![image 386](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile386.png>)

![image 387](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile387.png>)

j=nH(b−1)+1

i=nH(a−1)+1

Note that f˜(˜z) is deterministic, since the set of admissible z˜ has been chosen such that Π−z 1 (i)−1 = i for all 1 ≤ i ≤ n. We will then obtain our claimed result by bounding the expectation of

- (C.9) ρ−n1 p¯z˜(i)z˜(j) − f¯ ξ(i),ξ(j)

≤ ρ−n1 p¯z˜(i)z˜(j) − f˜z˜

(i)z˜(j) + f ˜z˜

(i)z˜(j) − f¯(in,jn) + f ¯(in,jn) − f¯ ξ(i),ξ(j) .

We begin with the ﬁnal term in (C.9), for which Lemma C.7 immediately yields

- (C.10)

- E f ¯(in,jn)−f¯ ξ(i),ξ(j) ≤ M {2(n + 2)}−α/2+2M √2 max1≤a≤k ha/n α .


![image 388](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile388.png>)

Next we consider the ﬁrst term in (C.9). To bound its expectation, note

that both ρ−n1 p¯(˜z)ab and f˜(˜z)ab are averages over the same subset of indices (i,j). From (C.6) and (C.8), we then have that

E ρ−n1 p¯(˜z)ab − f˜(˜z)ab

≤

1 h2ab

![image 389](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile389.png>)

nH(b)

j=nH(b−1)+1

nH(a) I(a =b)+(j−1) I(a=b)

i=nH(a−1)+1

E f ξ(i),ξ(j) − f n+1 i , n+1j

![image 390](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile390.png>)

![image 391](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile391.png>)

- (C.11)

≤ 1 · M {2(n + 2)}−α/2 ,

- (C.12)

with the ﬁnal inequality following again from Lemma C.7. Since (C.12) holds uniformly over all z˜ and every 1 ≤ a,b ≤ k, we have bounded E ρ−n1 p¯z˜(i)z˜(j)− f˜z˜

(i)z˜(j) . It remains only to bound E f ˜z˜

(i)z˜(j) − f¯(in,jn) . We will do so using the following deterministic upper bound, which we prove below, and which holds uniformly over all z˜ and every 1 ≤ a,b ≤ k:

f ˜(˜z)ab − f¯(˜z)ab ≤ M

√

![image 392](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile392.png>)

2/(n + 1) α + M

√

![image 393](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile393.png>)

2 ha/n α (ha − 1)−1 I(a = b)

- (C.13)
- (C.14) ≤ M 2α/2 n−α {1 + 2α I (a = b)}.


Here the second inequality following because, by deﬁnition, any H(·) has min1≤a≤k ha ≥ 2.

(i)z˜(j) = f¯(in,jn), and so if (C.13) holds, then it applies to f ˜z˜

Lemma C.10 yields (in,jn) ∈ ωz˜(i)z˜(j) for any z˜; thus f¯z˜

(i)z˜(j) − f¯(in,jn) . Finally, summing (C.10), (C.12) and (C.14) to obtain (C.7) completes the proof.

To establish (C.13), let in = i/(n +1), and multiply f˜(˜z)ab from (C.8) by 1 = n2/n2 to obtain

f˜(˜z)ab =

=

nH(b)

nH(a) I(a =b)+(j−1) I(a=b)

n2 h2ab

![image 394](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile394.png>)

j=nH(b−1)+1

i=nH(a−1)+1

nH(b)

nH(a) I(a =b)+(j−1) I(a=b)

n2 h2ab

![image 395](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile395.png>)

j=nH(b−1)+1

i=nH(a−1)+1

1 n2

![image 396](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile396.png>)

f (in,jn) , 1 ≤ a < b ≤ k,

j n

![image 397](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile397.png>)

j−1 n

![image 398](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile398.png>)

i n

![image 399](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile399.png>)

i−1 n

![image 400](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile400.png>)

dxdy f (in,jn)

- (C.15)

·

j n

![image 401](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile401.png>)

j−1 n

![image 402](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile402.png>)

i n

![image 403](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile403.png>)

i−1 n

![image 404](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile404.png>)

[f (x,y) + {f (in,jn) − f (x,y)}] dxdy.

- (C.16)

From (C.15) we will obtain the left-hand side of (C.13), plus a remainder term when a = b, by writing

- (C.17)


n2 h2ab

=

![image 405](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile405.png>)

f˜(˜z)ab −

nH(b)

nH(a) I(a =b)+(j−1) I(a=b)

j=nH(b−1)+1

i=nH(a−1)+1

nH(b)

nH(a) I(a =b)+(j−1) I(a=b)

n2 h2ab

![image 406](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile406.png>)

j=nH(b−1)+1

i=nH(a−1)+1

j n

![image 407](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile407.png>)

j−1 n

![image 408](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile408.png>)

i n

![image 409](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile409.png>)

f (x,y) dxdy

i−1 n

![image 410](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile410.png>)

H(b)

H(a)

n2 hahb

 

f (x,y) dxdy a = b,

![image 411](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile411.png>)

H(b−1)

H(a−1)

= f˜(˜z)ab−

nH(b)

j n

y

y

n2 hb 2

![image 412](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile412.png>)

f (x,y) dxdy a = b.

−

![image 413](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile413.png>)

j−1 n

j−1 n



H(a−1)

![image 414](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile414.png>)

![image 415](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile415.png>)

j=nH(b−1)+1

We recognize the ﬁrst case in (C.17) as f¯(˜z)ab,a =b. Since f is symmetric, the

second case can be written

nH(b)

f¯(˜z)bb +

j=nH(b−1)+1

j n

![image 416](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile416.png>)

j−1 n

![image 417](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile417.png>)

n2 hb 2

2n2 h2b

−

![image 418](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile418.png>)

![image 419](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile419.png>)

y

n2 hb 2

−

![image 420](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile420.png>)

H(b−1)

y

j−1 n

![image 421](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile421.png>)

f (x,y) dxdy

nH(b)

j n

y

y

2n2 h2b

2n2 hb

1 hb − 1

![image 422](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile422.png>)

= f¯(˜z)bb +

f (x,y) dxdy

−

![image 423](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile423.png>)

![image 424](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile424.png>)

![image 425](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile425.png>)

j−1 n

j−1 n

H(b−1)

![image 426](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile426.png>)

![image 427](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile427.png>)

j=nH(b−1)+1

 

f (x,y) dxdy  

nH(b)

j n

y

1 hb − 1

1 hb

![image 428](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile428.png>)

= f¯(˜z)bb +

f¯(˜z)bb −

2n2

![image 429](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile429.png>)

![image 430](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile430.png>)

j−1 n

j−1 n



![image 431](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile431.png>)

![image 432](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile432.png>)

j=nH(b−1)+1

f ¯(˜z)bb − f (x,y) dxdy

  1

nH(b)

j n

y

1 hb − 1

![image 433](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile433.png>)

= f¯(˜z)bb +

2n2

 .

![image 434](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile434.png>)

![image 435](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile435.png>)

hb

j−1 n

j−1 n

![image 436](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile436.png>)

![image 437](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile437.png>)

j=nH(b−1)+1

Since f¯(x,y;h) = f¯(˜z)bb on the domain of interest ωbb = [H(b − 1),H(b))2, we conclude

nH(b)

j n

y

- 1 hb


![image 438](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile438.png>)

f ¯(˜z)bb − f (x,y) dxdy ≤ 1 · 1 · f ¯− f|ωbb L∞(ωbb) ≤ M

2n2

![image 439](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile439.png>)

j−1 n

j−1 n

![image 440](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile440.png>)

![image 441](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile441.png>)

j=nH(b−1)+1

√

2 hb/n α,

![image 442](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile442.png>)

with the latter inequality from (C.19) of Lemma C.6, since f ∈ H¨olderα(M). This yields the upper bound term in (C.13) speciﬁc to a = b. To derive the main term in (C.13), we return to (C.15), noting from Lemma C.7:

n2 h2ab

![image 443](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile443.png>)

nH(b)

nH(a) I(a =b)+(j−1) I(a=b)

j=nH(b−1)+1

i=nH(a−1)+1

j n

![image 444](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile444.png>)

j−1 n

![image 445](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile445.png>)

i n

![image 446](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile446.png>)

{f (in,jn) − f (x,y)} dxdy

i−1 n

![image 447](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile447.png>)

nH(a) I(a =b)+(j−1) I(a=b) i=nH(a−1)+1 · n2

nH(b)

1 h2ab

≤

![image 448](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile448.png>)

j=nH(b−1)+1

j n

i n

![image 449](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile449.png>)

![image 450](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile450.png>)

|f (in,jn) − f (x,y)| dxdy ≤ 1 · 1 · M

j−1 n

i−1 n

![image 451](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile451.png>)

![image 452](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile452.png>)

√

2/(n + 1) α.

![image 453](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile453.png>)

![image 454](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile454.png>)

![image 455](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile455.png>)

![image 456](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile456.png>)

![image 457](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile457.png>)

Lemma C.6. Let f be a H¨olderα(M) function on (0,1)2, with f¯(x,y;h) = f¯H−1(x)H−1(y) its stepfunction approximation. Then for all 0 < p ≤ ∞,

f − f¯ Lp((0,1)2) ≤ M √2max1≤a≤k ha/n α .

![image 458](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile458.png>)

Proof. Let ωab = [H(a − 1),H(a)) × [H(b − 1),H(b)) ⊆ (0,1)2, and

denote by f|ωab the restriction of f to ωab. By the deﬁnitions of f¯ab and f¯(x,y),

1 |ωab| ωab

f ¯ab − f (x,y) =

f x′,y′ dx′ dy′ − f (x,y) , (x,y) ∈ (0,1)2

![image 459](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile459.png>)

1 |ωab| ωab

⇒ f ¯(x,y) − f (x,y) ≤

f x′,y′ − f (x,y) dx′ dy′, (x,y) ∈ ωab

![image 460](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile460.png>)

1 |ωab| ωab

⇒ f ¯− f|ωab L∞(ωab) ≤

f x′,y′ − f (x,y) dx′ dy′, (x,y) ∈ ωab

![image 461](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile461.png>)

M |ωab| ωab

- (C.18) (x,y) − (x′,y′) α dx′ dy′, (x,y) ∈ ωab,

since |f (x,y) − f (x′,y′)| ≤ M |(x,y) − (x′,y′)|α = M {(x − x′)2 + (y − y′)2}α/2 holds on (0,1)2.

To simplify (C.18), note that the diameter sup(x,y),(x′,y′)∈ωab |(x,y) − (x′,y′)|

of the rectangular domain ωab evaluates to h2a + h2b/n, where ha = H(a)− H(a − 1). Thus (C.18) implies

![image 462](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile462.png>)

- (C.19) f ¯− f|ωab L∞(ωab) ≤ M h2a + h2b/n α, 1 ≤ a,b ≤ k,


≤

![image 463](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile463.png>)

![image 464](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile464.png>)

and so we immediately conclude f ¯− f L∞((0,1)2) ≤ M √2 maxa ha/n α. Thus for any 0 < p < ∞,

![image 465](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile465.png>)

f ¯(x,y) − (x,y) p dxdy

f ¯− f pL

p((0,1)2) =

(0,1)2

≤

(0,1)2

f ¯− f L∞((0,1)2)

p dxdy.

![image 466](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile466.png>)

![image 467](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile467.png>)

![image 468](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile468.png>)

![image 469](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile469.png>)

Lemma C.7. Let f be a H¨olderα(M) function on (0,1)2, and let {ξ(i)}ni=1 be an ordered sample of independent Uniform(0,1) random variables. Then, recalling that Eξ(i) = i/(n + 1), we have for 1 ≤ i,j ≤ n:

β

≤ Mβ {2(n + 2)}−αβ/2 , 0 < β ≤ 2;

E f ξ(i),ξ(j) − f n+1 i , n+1j

![image 470](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile470.png>)

![image 471](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile471.png>)

E f ¯ ξ(i),ξ(j) − f¯ n+1 i , n+1j ≤ M {2(n + 2)}−α/2 + 2M √2 max1≤a≤k ha/n α,

![image 472](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile472.png>)

![image 473](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile473.png>)

![image 474](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile474.png>)

where f¯(x,y;h) = f¯H−1(x)H−1(y) is the stepfunction approximation of f. Furthermore, we have for 1 ≤ i,j ≤ n that

√

2/(n+1) α, (x,y) ∈ i−n1, ni × j−n1, nj .

f n+1 i , n+1j − f (x,y) ≤ M

![image 475](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile475.png>)

![image 476](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile476.png>)

![image 477](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile477.png>)

![image 478](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile478.png>)

![image 479](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile479.png>)

![image 480](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile480.png>)

![image 481](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile481.png>)

Proof. Let in = Eξ(i) = i/(n + 1). Since f ∈ H¨olderα(M), it holds everywhere on (0,1)2 that

f ξ(i),ξ(j) − f (in,jn) β ≤ M (ξ(i),ξ(j)) − (in,jn) α β , 1 ≤ i,j ≤ n,

where |·| is the Euclidean metric on R2. By Jensen’s inequality, we have for any 0 < αβ ≤ 2 that for 1 ≤ i,j ≤ n,

E (ξ(i) − in)2 + (ξ(j) − jn)2 αβ/2 ≤ varξ(i) + varξ(j) αβ/2 ≤ {2(n + 2)}−αβ/2 ,

with the latter inequality via var ξ(i) = in(1 − in)/(n + 2) ≤ (1/4)/(n + 2). This proves the ﬁrst result. For the second, we use Lemma C.6 and a chaining argument, since f¯ is piecewise-constant on blocks:

f ¯ ξ(i),ξ(j) − f¯(in,jn) ≤ f ¯− f ξ(i),ξ(j) + f ξ(i),ξ(j) − f (in,jn)

+ f − f¯ (in,jn) ≤ f ξ(i),ξ(j) − f (in,jn) + 2M √2 max1≤a≤k ha/n α .

![image 482](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile482.png>)

Finally, f ∈ H¨olderα(M) implies for (x,y) ∈ i−n1, ni × j−n1, nj the uniform upper bound for 1 ≤ i,j ≤ n:

![image 483](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile483.png>)

![image 484](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile484.png>)

![image 485](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile485.png>)

![image 486](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile486.png>)

(in − x)2 + (jn − y)2 α/2

|f (in,jn) − f (x,y)| ≤ M sup (x,y)∈(i−n1,ni )×(j−n1,nj )

![image 487](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile487.png>)

![image 488](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile488.png>)

![image 489](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile489.png>)

![image 490](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile490.png>)

α/2

(1 − in)2 n2

(in)2 n2

.

,

≤ M max

2max

![image 491](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile491.png>)

![image 492](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile492.png>)

1≤i≤n

![image 493](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile493.png>)

![image 494](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile494.png>)

![image 495](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile495.png>)

![image 496](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile496.png>)

- Lemma C.8. Let f be a symmetric H¨olderα(M) function on (0,1)2, with


stepfunction approximation f¯(x,y;h) = f¯H−1(x)H−1(y), and let {ξ(i)}ni=1 be an ordered sample of independent Uniform(0,1) random variables. Then

whenever ρn > 0 and 0 < ρnf (x,y) < 1 everywhere on (0,1)2,

- (C.20) ρn n2 −1 Eξ i<j

D ρnf (ξi,ξj) ρnf¯(ξi,ξj)

≤

ρnM2 √2max1≤a≤k ha/n 2α min1≤a,b≤k min ρnf¯ab,1 − ρnf¯ab · max

![image 497](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile497.png>)

![image 498](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile498.png>)

1≤a,b≤k

1 + ∆ab 1 +

- 2

![image 499](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile499.png>)

- 3


1 + 2∆ab (1 − ∆ab)3

![image 500](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile500.png>)

,

where for f|ωab the restriction of f to ωab = [H(a − 1),H(a))×[H(b − 1),H(b)), we deﬁne

- (C.21)


ρnM √2max1≤a≤k ha/n α min ρnf¯ab,1 − ρnf¯ab

ρn f|ωab − f¯ab L

![image 501](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile501.png>)

∞(ωab)

∆ab =

min ρnf¯ab,1 − ρnf¯ab ≤

, 1 ≤ a,b ≤ k.

![image 502](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile502.png>)

![image 503](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile503.png>)

Proof. Since {ξi}ni=1 is a random sample of Uniform(0,1) variates, and f is symmetric, we have

- (C.22) ρn n2 −1 Eξ i<j

D ρnf (ξi,ξj) ρnf¯(ξi,ξj)

=

(0,1)2

ρ−n1 D ρnf(x,y) ρnf¯(x,y) dxdy.

Let p = ρnf¯ and δ = ρn(f − f¯) pointwise on (0,1)2, in order to apply

- Lemma C.9 to the integrand of (C.22), and deﬁne the following ratio: ∆ab =


ρn f|ωab − f¯ab L

∞(ωab) /min ρnf¯ab,1 − ρnf¯ab . We may then write

(0,1)2

ρ−n1 D ρnf(x,y) ρnf¯(x,y) dxdy

=

k

a=1

k

b=1 ωab

ρ−n1 D ρnf(x,y) ρnf¯ab dxdy

≤

k

a=1

k

b=1 ωab

ρ−n1

ρnf(x,y) − ρnf¯ab 2 2ρnf¯ab 1 − ρnf¯ab

![image 504](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile504.png>)

1 + ∆ab 1 +

- 2

![image 505](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile505.png>)

- 3


1 + 2∆ab (1 − ∆ab)3

![image 506](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile506.png>)

dxdy

≤ max

1≤a,b≤k

 

1 + ∆ab 1 + 23 (11+2∆−∆ ab

![image 507](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile507.png>)

![image 508](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile508.png>)

ab)3 2ρnf¯ab 1 − ρnf¯ab

![image 509](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile509.png>)

  ρn f − f¯ 2L

2((0,1)2).

Our ﬁnal step is to control the norms f|ωab − f¯ab L

∞(ωab) and f−f¯ 2L

2((0,1)2) in this bound. To do so, we apply Lemma C.6, which asserts that whenever f ∈ H¨olderα(M), we have for all 1 ≤ a,b ≤ k that

- (C.23)


∞(ωab) ≤ f − f¯ L2((0,1)2) ≤ M √2max1≤a≤k ha/n α .

f|ωab − f¯ab L

![image 510](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile510.png>)

The result follows from (C.23), since by hypothesis max ρnf¯ab,1 − ρnf¯ab ≥ 1/2 for every (a,b), and so

ρnM2 √2max1≤a≤k ha/n 2α min ρnf¯ab,1 − ρnf¯ab

ρn f − f¯ 2L

ρn f − f¯ 2L

![image 511](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile511.png>)

2((0,1)2)

2((0,1)2)

- 2ρnf¯ab 1 − ρnf¯ab ≤


min ρnf¯ab,1 − ρnf¯ab ≤

.

![image 512](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile512.png>)

![image 513](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile513.png>)

![image 514](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile514.png>)

![image 515](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile515.png>)

![image 516](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile516.png>)

![image 517](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile517.png>)

![image 518](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile518.png>)

Lemma C.9. Consider the Bernoulli Kullback–Leibler divergence quantities D (p|| p + δ) and D (p + δ ||p), where 0 < p < 1 and −p ≤ δ ≤ 1 − p.

If |δ| < min (p,1 − p), then the following bounds hold:

δ2 2p(1−p)

D(p || p+δ)−

−3

![image 519](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile519.png>)

|δ|

min(p,1−p) 1 − min(|p,δ|1−p)

δ2/{2p(1−p)} ≤ 23

,

![image 520](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile520.png>)

![image 521](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile521.png>)

![image 522](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile522.png>)

![image 523](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile523.png>)

δ2 2p(1−p)

D(p+δ || p)−

![image 524](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile524.png>)

δ2/{2p(1−p)} ≤ min(|p,δ|1−p) 1 + 23 1 + min(2p,|δ1|−p) 1 − min(|p,δ|1−p)

![image 525](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile525.png>)

![image 526](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile526.png>)

![image 527](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile527.png>)

![image 528](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile528.png>)

![image 529](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile529.png>)

−3

.

Now consider ρn,f,g > 0 such that 0 < ρnf,ρng < 1. Then |f − g|2 ≤ 2fρ−n1 D(ρnf || ρng).

Proof. The ﬁrst result follows by manipulating a Taylor series expansion of D (p|| p + δ) using the Lagrange form of the remainder. For some δ′,δ′′ satisfying 0 < |δ′| < |δ| and 0 < |δ′′| < |δ|, we have

- (C.24)


δ′′ 1−p

δ′ p

−3

−3

p2 1−

−(1−p)2 1+

![image 530](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile530.png>)

![image 531](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile531.png>)

D (p|| p + δ) = 2p(1δ2−p) 1 + 23 min(p,δ1−p)

max(p,1−p) .

![image 532](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile532.png>)

![image 533](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile533.png>)

![image 534](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile534.png>)

![image 535](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile535.png>)

The ﬁrst result then follows by controlling the scaled diﬀerence of the remainder terms appearing in (C.24), both of which are non-negative. We upper-bound this diﬀerence by the maximum of these two quantities, writing

δ′ p

δ′′ 1 − p

−3,(1 − p)2 1 +

−3

max p2 1 −

![image 536](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile536.png>)

![image 537](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile537.png>)

2

−3

≤ max(p,1 − p)

1 − |δ| /min (p,1 − p)

.

The second result follows similarly, by manipulating a Taylor series expansion of D (p + δ || p).

The ﬁnal result follows from rewriting D (ρnf ||ρng) as D (ρn(g + d)||ρng), with d = f −g. We ﬁrst bound the second derivative of D(ρn(g + d)||ρng) in d below by ρn/f, and then integrate twice, using that D (ρn(g + d)||ρng) = 0 if d = 0.

![image 538](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile538.png>)

![image 539](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile539.png>)

![image 540](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile540.png>)

![image 541](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile541.png>)

Lemma C.10. Let in = i/(n + 1) and jn = j/(n + 1). Then (in,jn) ∈ ωaibj, where ai and bj are deﬁned by

ai = H−1 (i/n) , bj = H−1 (j/n) , 1 ≤ a,b ≤ k, 1 ≤ i,j ≤ n. Proof. From the deﬁnition of ai we may directly compute

min{H−1(i/n),k}

H {ai} = H H−1 (i/n) = n−1

ha

a=1

= i/n if aa=1i ha = i, ≥ (i + 1)/n if aa=1i ha = i.

We also have that H (ai − 1) = H H−1 (i/n) − 1

min{H−1(i/n)−1,k}

= (i − 1)/n if aa=1i−1 ha = i − 1, ≤ (i − 2)/n if a a=1i−1 ha = i − 1.

= n−1

ha

a=1

We have by deﬁnition that ωaibj = H H−1 (i/n) − 1 ,H H−1 (i/n) ×

H H−1 (j/n) − 1 ,H H−1 (j/n) . Since H(·) and its inverse H−1(·) are non-decreasing functions, it follows that H H−1 (i/n) ≥ i/n ≥ i/(n+1) = in. Thus the claimed upper bound is respected. Furthermore, for the lower limit, H H−1 (i/n) − 1 ≤ (i − 1)/n ≤ in, as (i − 1)/n ≤ i/(n + 1) = in ⇔ i ≤ n + 1. Thus the claimed lower bound is also respected, and so by symmetry, we conclude that (in,jn) ∈ ωaibj.

![image 542](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile542.png>)

![image 543](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile543.png>)

![image 544](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile544.png>)

![image 545](<2013-wolfe-nonparametric-graphon-estimation_images/imageFile545.png>)

ACKNOWLEDGEMENTS

We thank David Choi for helpful insight into blockmodels. Work supported in part by the US Army Research Oﬃce under PECASE Award W911NF-09-1-0555 and MURI Award 58153-MA-MUR; by the UK EPSRC under Mathematical Sciences Leadership Fellowship EP/I005250/1, Established Career Fellowship EP/K005413/1 and Developing Leaders Award EP/L001519/1; by the UK Royal Society under a Wolfson Research Merit Award; and by Marie Curie FP7 Integration Grant PCIG12-GA-2012-334622 within the 7th European Union Framework Program.

REFERENCES

Airoldi, E. M., Blei, D. M., Fienberg, S. E. and Xing, E. P. (2008). Mixed membership stochastic blockmodels. J. Mach. Learn. Res. 9 1981–2014. Aldous, D. J. (1981). Representations for partially exchangeable arrays of random variables. J. Multivariate Anal. 11 581–598.

Alon, N. (1995). A note on network reliability. In Discrete Probability and Algorithms (D. Aldous, P. Diaconis, J. Spencer and J. M. Steele, eds.) 11–14. Springer-Verlag, New York.

Arias-Castro, E. and Grimmett, G. R. (2013). Cluster detection in networks using percolation. Bernoulli 19 676–719.

Ball, F., Britton, T. and Sirl, D. (2013). A network with tunable clustering, degree correlation and degree distribution, and an epidemic thereon. J. Math. Biol. 66 979– 1019.

Bickel, P. J. and Chen, A. (2009). A nonparametric view of network models and Newman–Girvan and other modularities. Proc. Natl. Acad. Sci. USA 106 21068–21073. Bickel, P. J., Chen, A. and Levina, E. (2011). The method of moments and degree distributions for network models. Ann. Statist. 39 2280–2301. Birg´e, L. and Massart, P. (1998). Minimum contrast estimators on sieves: Exponential bounds and rates of convergence. Bernoulli 4 329–375.

Bollobas,´ B., Janson, S. and Riordan, O. (2007). The phase transition in inhomogeneous random graphs. Random Structures Algorithms 31 3–122.

Bollobas,´ B. and Riordan, O. (2009). Metrics for sparse graphs. In Surveys in Combinatorics 2009 (S. Huczynska, J. D. Mitchell and C. M. Roney-Dougal, eds.) 211–287. Cambridge University Press, Cambridge, UK.

Chatterjee, S. (2012). Matrix estimation by universal singular value thresholding. Preprint arXiv:1212.1247. Chatterjee, S., Diaconis, P. and Sly, A. (2011). Random graphs with a given degree sequence. Ann. Appl. Probab.. 21 1400–1435. Choi, D. S., Wolfe, P. J. and Airoldi, E. M. (2012). Stochastic blockmodels with a growing number of classes. Biometrika 99 273–284. Choi, D. S. and Wolfe, P. J. (2013). Co-clustering separately exchangeable network

data. Ann. Statist. To appear (arXiv:1212.4093). DeVore, R. A. (1998). Nonlinear approximation. Acta numerica 7 51–150. Diaconis, P. (1977). Finite forms of de Finetti’s theorem on exchangeability. Synthese

36 271–281. Diaconis, P. and Janson, S. (2008). Graph limits and exchangeable random graphs. Rend. Mat. Appl. 28 33–61. Durrett, R. (2007). Random Graph Dynamics. Cambridge University Press, Cambridge, UK. Fienberg, S. E. (2012). A brief history of statistical models for network analysis and open challenges. J. Comput. Graph. Statist. 21 825–839. Fienberg, S. E. and Rinaldo, A. (2012). Maximum likelihood estimation in log-linear models. Ann. Statist. 40 996–1023. Fishkind, D. E., Sussman, D. L., Tang, M., Vogelstein, J. T. and Priebe, C. E.

(2013). Consistent adjacency-spectral partitioning for the stochastic block model when the model parameters are unknown. SIAM J. Matrix Anal. Appl. 34 23–39.

Green, P. J. and Silverman, B. W. (1994). Nonparametric Regression and Generalized Linear Models: A Roughness Penalty Approach. Chapman & Hall, London. Hoover, D. N. (1979). Relations on probability spaces and arrays of random variables. Princeton, NJ. Janson, S. (2010). Asymptotic equivalence and contiguity of some random graphs. Random Structures Algorithms 36 26–45. Lovasz,´ L. (2012). Large Networks and Graph Limits. American Mathematical Society,

Providence, RI. Olhede, S. C. and Wolfe, P. J. (2013). Degree-based network models. Rinaldo, A., Petrovic,´ S. and Fienberg, S. E. (2013). Maximum likelihood estimation

in the Beta model. Ann. Statist. 41 1085–1110. Rohe, K., Chatterjee, S. and Yu, B. (2011). Spectral clustering and the highdimensional stochastic blockmodel. Ann. Statist. 39 1878–1915. Romanovsky, V. (1923). Note on the moments of a Binomial (p + q)n about its mean. Biometrika 15 410–412. Shaked, M. and Shanthikumar, J. G. (1994). Stochastic Orders and Their Applications. Academic Press, Boston, MA.

Sussman, D. L., Tang, M. and Priebe, C. E. (2013). Universally consistent latent position estimation and vertex classiﬁcation for random dot product graphs. Ann. Statist. In press (arXiv:1207.6745).

Zhao, Y., Levina, E. and Zhu, J. (2012). Consistency of community detection in networks under degree-corrected stochastic block models. Ann. Statist. 40 2266–2292.

Department of Statistical Science University College London Gower Street London WC1E 6BT, UK E-mail: p.wolfe@ucl.ac.uk, s.olhede@ucl.ac.uk

