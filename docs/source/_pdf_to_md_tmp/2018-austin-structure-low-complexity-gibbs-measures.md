arXiv:1810.07278v3[math.PR]3May2019

THE STRUCTURE OF LOW-COMPLEXITY GIBBS MEASURES ON PRODUCT SPACES

By Tim Austin University of California, Los Angeles

Let K1, . . . , Kn be bounded, complete, separable metric spaces. Let λi be a Borel probability measure on Ki for each i. Let f :

i Ki −→ R be a bounded and continuous potential function, and let

µ(dx) ∝ ef(x)λ1(dx1) · · · λn(dxn) be the associated Gibbs distribution.

At each point x ∈ i Ki, one can deﬁne a ‘discrete gradient’ ∇f(x, · ) by comparing the values of f at all points which diﬀer from x in at most one coordinate. In case i Ki = {−1, 1}n ⊂ Rn, the discrete gradient ∇f(x, · ) is naturally identiﬁed with a vector in Rn.

This paper shows that a ‘low-complexity’ assumption on ∇f implies that µ can be approximated by a mixture of other measures, relatively few in number, and most of them close to product measures in the sense of optimal transport. This implies also an approximation to the partition function of f in terms of product measures, along the lines of Chatterjee and Dembo’s theory of ‘nonlinear large deviations’.

An important precedent for this work is a result of Eldan in the

case i Ki = {−1, 1}n. Eldan’s assumption is that the discrete gradients ∇f(x, · ) all lie in a subset of Rn that has small Gaussian width.

His proof is based on the careful construction of a diﬀusion in Rn which starts at the origin and ends with the desired distribution on the subset {−1, 1}n. Here our assumption is a more naive coveringnumber bound on the set of gradients {∇f(x, · ) : x ∈ i Ki}, and our proof relies only on basic inequalities of information theory. As a result, it is shorter, and applies to Gibbs measures on arbitrary product spaces.

1. Introduction. Let (K1,dK1), ... , (Kn,dKn) be nonempty, complete, separable metric spaces, all with diameter at most one. Let Cb(Ki) and Prob(Ki) denote the spaces of bounded continuous functions and Borel probability measures on Ki, respectively, and similarly for other topological spaces. Let · denote the uniform norm on any space of real-valued functions. Let λi ∈ Prob(Ki) be a ﬁxed reference measure for each i.

![image 1](<2018-austin-structure-low-complexity-gibbs-measures_images/imageFile1.png>)

MSC 2010 subject classiﬁcations: Primary 60B99; secondary 60G99, 82B20, 94A17 Keywords and phrases: nonlinear large deviations, Gibbs measures, gradient complex-

ity, dual total correlation, mixtures of product measures

1

Let f : ni=1 Ki −→ R be a bounded continuous function, and call it the ‘potential’. Let

- (1) µ(dx) :=

1 Z

![image 2](<2018-austin-structure-low-complexity-gibbs-measures_images/imageFile2.png>)

ef(x)

n

i=1

λi(dxi)

be the resulting Gibbs measure, where Z is the normalizing constant that makes µ a probability measure. In the language of statistical mechanics, Z is the ‘partition function’ of f.

Inside Cb( i Ki) lies the vector subspace of functions that have the form

- (2) x  → f1(x1) + ··· + fn(xn)


for some f1 ∈ Cb(K1), ... , fn ∈ Cb(Kn). We call such functions additively separable. The choice of f1, .. ., fn representing the function in (2) is unique up additive constants. If f is the function in (2), then its Gibbs measure factorizes as

n

1 Z

(efi(xi)λi(dxi)),

![image 3](<2018-austin-structure-low-complexity-gibbs-measures_images/imageFile3.png>)

i=1

so it is a product measure. In this special case we denote this Gibbs measure by ξf. Similarly, if g ∈ Cb(Ki) for some i, then we denote by ξg the Gibbs measure on Ki constructed from g and λi.

Consider again a general f ∈ Cb( i Ki). In the main result of this paper, we assume that f has ‘low complexity’ relative to the subspace of additively separable functions, and deduce a structure theorem for µ in terms of mixtures of product measures. In case |Ki| = 2 for each i, theorems of this kind originate in Chatterjee and Dembo’s work [CD16] introducing the theory of ‘nonlinear large deviations’. Chatterjee and Dembo’s main result gives an approximation to the partition function Z under such an assumption on f. More recently, works by Eldan [Eld] and Eldan and Gross [EG18] have uncovered the approximate structure of the measure µ itself, again in case |Ki| = 2. Our main theorem ﬁts a similar template to Eldan’s, but it applies to general product spaces and its proof is quite diﬀerent.

To explain the relevant notion of ‘low complexity’, ﬁx a reference element ∗i ∈ Ki for each i. Given x ∈ i Ki, i ∈ [n], and y ∈ Ki, we deﬁne

∂if(x,y) := f(x1,... ,xi−1,y,xi+1,... ,xn)−f(x1,... ,xi−1,∗i,xi+1,... ,xn). Thus, we replace the ith coordinate of x twice, ﬁrst with y and then with ∗i, and take the diﬀerence of the resulting values of f. This should be regarded

- as a discrete analog of the ‘partial derivative of f in the ith coordinate’.


Beware that the deﬁnition of ∂if depends on the choice of the reference point ∗i. We suppress this dependence in our notation, but return to this point after the statement of the main theorem below.

We assemble these new functions ∂if into the single function

∇f(x,y) :=

n

∂if(x,yi) x,y ∈

i=1

i

Ki .

For a ﬁxed point x ∈ i Ki, the function ∇f(x, · ) is additively separable. We refer to it as the discrete gradient of f at the point x.

If f ∈ Cb( i Ki) has the property that ∇f(x, ·) is the same function

for every x ∈ i Ki, then an easy exercise shows that f itself is additively separable. Beyond this case, we can make the weaker assumption that f has

relatively few diﬀerent gradients ∇f(x, ·) as x varies in i Ki, at least up to small errors. This is the notion of ‘low complexity’ that we need.

The statement of our main theorem involves two other concepts. The ﬁrst is a mode of approximation between measures on a product space, provided by an appropriate transportation metric. Endow the product space i Ki with the normalized Hamming average of the metrics dKi:

1 n

dn(x,y) :=

![image 4](<2018-austin-structure-low-complexity-gibbs-measures_images/imageFile4.png>)

n

dKi(xi,yi) x,y ∈

i=1

i

Ki .

If each Ki is just a ﬁnite alphabet with the discrete metric, then dn is the usual Hamming metric, normalized to have diameter 1. Now deﬁne the transportation metric over dn by

![image 5](<2018-austin-structure-low-complexity-gibbs-measures_images/imageFile5.png>)

- (3) dn(µ,ν) := inf λ


dn(x,y)λ(dx,dy) µ,ν ∈ Prob

i

Ki ,

where λ ranges over all couplings of µ and ν. This is a standard and well-studied construction of a metric on probability measures: see, for instance, [Dud02, Section 11.8].

The second concept we need is a quantity which measures the multivariate correlation in a joint distribution on an n-fold product space. There are many such quantities, but the one we need is called ‘dual total correlation’ or ‘DTC’, which goes back to work of Han in information theory [Han75]. The deﬁnition of DTC is recalled in Subsection 2.4 below. The recent paper [Aus] studies DTC in some depth. According to the main result of that paper, a small value of DTC implies that the joint distribution is close in dn to a mixture of relatively few product measures. The relevance

![image 6](<2018-austin-structure-low-complexity-gibbs-measures_images/imageFile6.png>)

of DTC to the present paper is therefore not surprising, but in fact we do not call on that result from [Aus] in our work below. Rather, the proof of the main theorem in the present paper is relatively self-contained, and happens to yield an upper bound on the DTC of the Gibbs measure (1) as a by-product.

Our main theorem decomposes µ as a mixture in a very concrete way:

by partitioning i Ki and conditioning on the parts. Given any probability space (K,µ) and measurable subset P ⊆ K of positive measure, we write

µ|P for the conditioned measure µ(·|P). Theorem (A). Let P be a partition of i Ki with the property that |∇f(x,z) − ∇f(y,z)| < δn whenever x,y lie in the same part of P. Then:

- (4)  ∇f(x, ·) − ∇f(y, ·) = sup z


- a) DTC(µ) < Hµ(P) + δn, where Hµ(P) is the Shannon entropy of the partition P according to µ,
- b) we have

P∈P

µ(P) · D(µ|P ξ∇f(y,·)) µ|P(dy) < Hµ(P) + δn,

where D denotes Kullback–Leibler divergence, and

- c) we have


![image 7](<2018-austin-structure-low-complexity-gibbs-measures_images/imageFile7.png>)

µ(P) · dn(µ|P,ξ∇f(y,·)) µ|P(dy) <

P∈P

![image 8](<2018-austin-structure-low-complexity-gibbs-measures_images/imageFile8.png>)

Hµ(P) n

- 1

![image 9](<2018-austin-structure-low-complexity-gibbs-measures_images/imageFile9.png>)

- 2


+ δ .

![image 10](<2018-austin-structure-low-complexity-gibbs-measures_images/imageFile10.png>)

In this theorem, part (c) follows directly from part (b) using Marton’s transportation-entropy inequality (Proposition 2.3 below) and H¨older’s inequality. We include both of these parts in the statement because both kinds of approximation by product measures have an intrinsic interest and potential applications. But most of the proof of Theorem A goes towards parts (a) and (b).

The deﬁnition of ∇f depends on the choice of the reference points ∗i.

However, if we write ∗′1, .. ., ∗′n for an alternative choice of reference points and write ∇′f for the alternative discrete gradients that result, then these discrete gradients are related by the cocycle equation

∇′f(x,y) = ∇f(x,y) − ∇f(x,(∗′1,... ,∗′n)).

As a result, if P satisﬁes (4) for the discrete gradients ∇f(x, ·), then it satisﬁes the analogous bounds for the discrete gradients ∇′f(x, ·) with δn loosened to 2δn. For this reason, the particular choice of the reference points ∗i has little eﬀect on Theorem A.

Theorem A is valuable in case Hµ(P) is small compared to n. This is implied if we have enough control on |P| itself: for instance, if we know that

- (5) covδn ∇f(x, ·) : x ∈ i


Ki , · ≤ eεn

for some small ε, where covδn(·, · ) denotes the smallest cardinality of a covering by sets of · -diameter less than δn.

Corollary (A′). If f satisﬁes (5), then there are (i) a partition P

of i Ki into at most eεn parts and (ii) a selection of additively separable functions gP for P ∈ P such that

µ(P) · D(µ|P ξgP ) < (ε + δ)n

P∈P

and

![image 11](<2018-austin-structure-low-complexity-gibbs-measures_images/imageFile11.png>)

![image 12](<2018-austin-structure-low-complexity-gibbs-measures_images/imageFile12.png>)

µ(P) · dn(µ|P,ξgP ) < (ε + δ)/2.

P∈P

(Informally: ‘most of the mass of µ is on conditioned measures µ|P, P ∈ P, that are close to products’.)

The argument from Theorem A to Corollary A′ is very short, but we include it explicitly after the proof of Theorem A in Section 3.

The proof of Theorem A brings together four basic results of information theory. All are well-known up to some routine manipulations, but Section 2 lays them out carefully. Then Section 3 completes the proof of Theorem A.

Subsequent sections explore some consequences and related results. First, Section 4 gives an approximate description of which product measures appear in the mixture promised by Corollary A′: see Proposition 4.1. The description takes the form of an approximate ﬁxed point equation for those measures in terms of f. It follows almost immediately from Theorem A itself. It is an analog of the main result in [EG18] for the case of the Hamming cube, although that paper provides various ﬁner details and applications that we do not pursue here.

Next, Section 5 turns Theorem A into an approximation for the normalizing constant Z in (1). This topic is the original concern of [CD16], and re-appears among the consequences of Eldan’s main result in [Eld].

Some further comparison with previous works. The simplest setting for Theorem A is a product of two-point alphabets. The works of Chatterjee and Dembo [CD16] and Eldan and Gross [Eld, EG18] are conﬁned to that case.

In [CD16], the authors assume that f is deﬁned on the whole of Rn, and then restrict it to the product subset {0,1}n. Then they quantify the ‘complexity’ of f in terms of its classical gradient in the sense of calculus, rather than the discrete quantity ∇f that we discuss above. Their main result is an estimate on the normalizing constant Z, roughly in terms of a variational formula over product measures. This work has now been generalized to other alphabets by Yan [Yan]. For Yan’s generalization, he retains the feature that the alphabets Ki are subsets of some given Banach spaces Vi, and that the complexity of f is measured by its Fre´chet derivative as a function on i Vi. It should be straightforward to move between this notion of ‘low complexity’ and ours, but we do not explore this further here.

In [Eld], Eldan also regards his state space as a subset of Rn. He uses the subset {−1,1}n, which is more convenient for his proofs. Like the assumption in Theorem A, Eldan’s ‘low-complexity’ assumption applies directly to the discrete gradient ∇f, not its relative from calculus. But his approach uses the embedding {−1,1}n ⊂ Rn in another very essential way. It relies on a diﬀusion process in Rn which starts at the origin and ends with the desired distribution on {−1,1}n. This approach seems quite diﬀerent from ours. One can regard the main contribution of the present paper as an alternative proof of something like Theorem A which (i) is simpler in the special case Ki = {−1,1} and (ii) generalizes easily to other product spaces. However,

- at some points Eldan’s estimates seem to be sharper than ours; we compare


- them more carefully in Subsection 3.3. In a subsequent work [EG18] Eldan and Gross have characterized which product measures appear in Eldan’s structure theorem in terms of the function f; Proposition 4.1 below is similar to their result.


Chatterjee and Dembo’s results in [CD16] were initially motivated by statistical physics or large deviations questions in certain highly symmetric models of random graphs. Chatterjee gives a careful introduction to this area in his monograph [Cha17], where Chapter 8 is given to the ‘nonlinear large deviations approach’. After applying the basic theory of nonlinear large deviations, these questions about random graphs lead to a class of highly nontrivial variational problems, which are successfully analyzed in [LZ17, BGLZ17]. Some related applications which require more than twopoint alphabets are described by Yan in [Yan]. Applications with two-point alphabets are treated again by Eldan and Gross in [Eld, EG18, EG], where

they obtain reﬁnements of some of the Chatterjee–Dembo estimates using Eldan’s new structural results. Another application discussed in [CD16] is to large deviations of the number of arithmetic progressions in a random arithmetic set, and the recent paper [BGSZ] gives a more complete analysis of this problem using Eldan’s approach.

In this paper we do not investigate whether our new results lead to any further improvements in those applications. In the case of large deviations of subgraph counts in Erd˝os–Re´nyi random graphs, the recent preprint [CD] achieves substantial improvements over the other works cited above by carefully ﬁnding and exploiting certain convex sets related to that problem.

Another variation on Chatterjee and Dembo’s original partition-function estimates appears in Augeri’s recent preprint [Aug]. She considers an arbitrary compactly supported probability measure λ on Rn and a continuously diﬀerentiable potential function f : Rn −→ R. By an elegant application of elementary convex analysis, she obtains a new upper bound on the partition function log ef dλ in terms of a covering-number estimate on the range of the derivative Df. From this upper bound she then derives improved estimates in several of the applications of nonlinear large deviations, including again large deviations for cycle counts in Erd˝os–Re´nyi random graphs.

Acknowledgements. I am grateful to Sourav Chatterjee, Amir Dembo and Ofer Zeitouni for some insightful conversations. Along with Ronen Eldan and an anonymous referee, they also made valuable suggestions about earlier versions of this paper.

2. The four principles in the proof of Theorem A. Our proof of Theorem A combines four basic principles from probability and information theory. This section recalls these in turn, and the next section assembles

- them into the proof.


2.1. A modiﬁed chain rule for Kullback–Leibler divergence. We assume familiarity with the basic properties of Shannon entropy and Kullback– Leibler divergence. A standard reference in the setting of discrete probability distributions is [CT06, Chapter 2]. The KL divergence D(µ γ) can be deﬁned for any pair of probability measures µ, γ on a general measurable space: it is +∞ unless µ ≪ γ, and in that case it is deﬁned by

dµ dγ

D(µ γ) := log

dµ

![image 13](<2018-austin-structure-low-complexity-gibbs-measures_images/imageFile13.png>)

(which may still equal +∞). This generalization and its properties can be found in [Pin64, Chapters 2 and 3] or [DZ10, Appendix D.3].

For KL divergence, we need the following modiﬁcation of the usual chain rule.

Lemma 2.1 (Modiﬁed chain rule). For any measurable space K, ﬁnite measurable partition P of K, and probability measures µ and γ on K, we have

- (6) D(µ γ) = −Hµ(P) + P∈P

µ(P)D(µ|P γ).

Proof. The usual chain rule for KL divergence gives

- (7) D(µ γ) = D([µ]P [γ]P) + P

µ(P)D(µ|P γ|P),

where [µ]P denotes the stochastic vector (µ(P))P∈P. Now observe that

D(µ|P γ|P) =

P

log

dµ|P dγ|P

![image 14](<2018-austin-structure-low-complexity-gibbs-measures_images/imageFile14.png>)

dµ|P

=

P

log γ(P)

dµ|P dγ

![image 15](<2018-austin-structure-low-complexity-gibbs-measures_images/imageFile15.png>)

dµ|P = D(µ|P γ) + log γ(P).

Inserting this into (7), we are left with the second right-hand term of (6), together with the quantity

D([µ]P [γ]P) +

P

µ(P)log γ(P) =

P

µ(P)log

µ(P) γ(P)

![image 16](<2018-austin-structure-low-complexity-gibbs-measures_images/imageFile16.png>)

+

P

µ(P)log γ(P)

= −Hµ(P).

![image 17](<2018-austin-structure-low-complexity-gibbs-measures_images/imageFile17.png>)

![image 18](<2018-austin-structure-low-complexity-gibbs-measures_images/imageFile18.png>)

![image 19](<2018-austin-structure-low-complexity-gibbs-measures_images/imageFile19.png>)

![image 20](<2018-austin-structure-low-complexity-gibbs-measures_images/imageFile20.png>)

2.2. Gibbs’ variational principle. Fix a probability space (K,λ) and let f : K −→ R be a bounded measurable function. As in the Introduction, the Gibbs measure on K associated to f and λ is deﬁned by

- (8) µ(dx) :=


ef(x) ef dλ

λ(dx).

![image 21](<2018-austin-structure-low-complexity-gibbs-measures_images/imageFile21.png>)

The importance of Gibbs measures is intimately related to Gibbs’ famous variational principle. Here we use it in the following form.

Proposition 2.2. If µ is the Gibbs measure associated to f, then

D(µ λ) − f dµ = −log ef dλ. For any other probability measure ν on K, we have

- (9) D(ν λ) − f dν = D(µ λ) − f dµ + D(ν µ).


If K is ﬁnite and λ is uniform, then (9) appears within the calculation in [CT06, equations (12.5)–(12.12)]. The same calculation gives the general case upon replacing H(·) with −D(· λ) throughout. In that generality it can be found in the proof of [DZ10, Lemma 6.2.13], and in the application of [Csi75, equation (2.6)] in Section 3, case (A) of that paper.

2.3. Marton’s transportation-entropy inequality. A classical inequality of Marton [Mar86, Mar96] provides the basic link between KL divergence relative to a product measure and the transportation metric (3). Most of the proof of Theorem A concerns information theoretic estimates, before Marton’s inequality turns these into a transportation-distance bound at the last step.

Proposition 2.3 (Marton’s transportation-entropy inequality). Let (Ki,dKi), i = 1,2,... ,n, be complete and separable metric spaces of diameter at most

1. If µ,ν ∈ Prob( i Ki) and ν is a product measure then

![image 22](<2018-austin-structure-low-complexity-gibbs-measures_images/imageFile22.png>)

- 1

![image 23](<2018-austin-structure-low-complexity-gibbs-measures_images/imageFile23.png>)

- 2n


![image 24](<2018-austin-structure-low-complexity-gibbs-measures_images/imageFile24.png>)

dn(µ,ν) ≤

D(µ ν).

![image 25](<2018-austin-structure-low-complexity-gibbs-measures_images/imageFile25.png>)

![image 26](<2018-austin-structure-low-complexity-gibbs-measures_images/imageFile26.png>)

![image 27](<2018-austin-structure-low-complexity-gibbs-measures_images/imageFile27.png>)

![image 28](<2018-austin-structure-low-complexity-gibbs-measures_images/imageFile28.png>)

Marton’s original presentation is only for measures on ﬁnite sets, but the proof works without change for products of general complete separable metric spaces. The only requirement is that they all have diameter at most one: this is why we assume that from the beginning of this paper. (If the diameters are larger but ﬁnite, this simply changes the factor of 1/2 in the inequality.) See [Mar96, Mar98, Dem97, Sam00] for various extensions of Proposition 2.3, and [Tal96] for a Gaussian analog.

- 2.4. DTC and a version of Han’s inequality. Given ﬁnite-valued random


variables ξ1, . .., ξn, their dual total correlation or DTC is

DTC(ξ1,... ,ξn) := H(ξ1,... ,ξn) −

n

H(ξi |ξ1,... ,ξi−1,ξi+1,... ,ξn).

i=1

For more general random variables valued in measurable spaces K1, . .., Kn, their DTC is

DTC(ξ1,... ,ξn) := sup

DTC([ξ1]P1,... ,[ξn]Pn),

P1,...,Pn

where the supremum runs over all tuples of ﬁnite measurable partitions Pi of the spaces Ki, and [ξi]Pi denotes the quantization of ξi by Pi.

DTC is one of several possible ways to quantify the correlation among n random variables. A classical family of inequalities due to Han [Han78, Theorem 4.1] includes the fact that DTC is always non-negative. DTC is studied carefully in [Aus], together with its simpler relative TC. In this paper we use DTC via an alternative formula in the setting of Gibbs measures.

Consider the spaces Ki and reference measures λi ∈ Prob(Ki) as in the Introduction. The next lemma is [Aus, Proposition 6.1, part (b)], along with the ﬁrst remark following its proof in that paper.

Lemma 2.4. If D(µ λ1 × ··· × λn) < ∞ then

n

D(µi,z λi)µ[n]\i(dz) − D(µ λ1 × ··· × λn),

DTC(µ) =

i=1

where

- • µ[n]\i is the projection of µ to j∈[n]\i Kj, and
- • (µi,z : z ∈ j∈[n]\i Kj) is a conditional distribution under µ of the ith coordinate given the other coordinates.


![image 29](<2018-austin-structure-low-complexity-gibbs-measures_images/imageFile29.png>)

![image 30](<2018-austin-structure-low-complexity-gibbs-measures_images/imageFile30.png>)

![image 31](<2018-austin-structure-low-complexity-gibbs-measures_images/imageFile31.png>)

![image 32](<2018-austin-structure-low-complexity-gibbs-measures_images/imageFile32.png>)

In the form given by this lemma, the non-negativity of DTC is a sharpening of the usual logarithmic Sobolev inequality for product spaces. Indeed, this sharpening already appears implicitly inside standard proofs of that logarithmic Sobolev inequality: see the discussion at the end of [Aus, Section 6].

In case µ is the Gibbs measure of f, Lemma 2.4 turns into a simple expression for DTC(µ) in terms of ∇f. It plays a crucial role later in this paper.

Corollary 2.5. The Gibbs measure in (1) satisﬁes

- (10) DTC(µ) = D(ξ∇f(x,·) λ1 × ··· × λn)µ(dx) − D(µ λ1 × ··· × λn).


Proof. The additivity of KL divergence for product measures gives

n

D(ξ∇f(x,·) λ1 × ··· × λn)µ(dx) =

i=1

D(ξ∂if(x,·) λi)µ(dx).

Using this, the right-hand side of (10) matches the formula for DTC(µ) in Lemma 2.4, because ξ∂if(x,·) is precisely the conditional distribution of xi under µ given the other coordinates x[n]\i.

![image 33](<2018-austin-structure-low-complexity-gibbs-measures_images/imageFile33.png>)

![image 34](<2018-austin-structure-low-complexity-gibbs-measures_images/imageFile34.png>)

![image 35](<2018-austin-structure-low-complexity-gibbs-measures_images/imageFile35.png>)

![image 36](<2018-austin-structure-low-complexity-gibbs-measures_images/imageFile36.png>)

In the proof of Theorem A, the fact we really need is that the diﬀerence on the right-hand side of (10) is non-negative. However, Theorem A also provides a bound on DTC(µ). This actually oﬀers an alternative route to a decomposition of µ into near-product measures: the main result of [Aus] obtains such a decomposition precisely from a bound on DTC. We discuss this further at the end of Section 3.

3. Proof of Theorem A. We now return to the setting of Theorem A.

The measure µ and discrete gradient ∇f are both constructed from the potential function f. The proof of Theorem A depends on the following link between them.

Lemma 3.1. We have

∇f(x,x)µ(dx) = ∇f(x,y) ξ∇f(x,·)(dy)µ(dx). Proof. It suﬃces to prove that

- (11) ∂if(x,xi)µ(dx) = ∂if(x,y) ξ∂if(x,·)(dy)µ(dx)

for each i ∈ [n], for then we can just sum over i. The function ∂if(x, ·) depends only on x[n]\i, and ξ∂if(x,·) is the conditional distribution of xi under µ given the other coordinates x[n]\i. Therefore

∂if(x,y) ξ∂if(x,·)(dy) = Eµ ∂if(x,xi) x[n]\i , and (11) is the tower property of iterated conditional expectations. To prove Theorem A, we must bound both DTC(µ) and the expression

![image 37](<2018-austin-structure-low-complexity-gibbs-measures_images/imageFile37.png>)

![image 38](<2018-austin-structure-low-complexity-gibbs-measures_images/imageFile38.png>)

![image 39](<2018-austin-structure-low-complexity-gibbs-measures_images/imageFile39.png>)

![image 40](<2018-austin-structure-low-complexity-gibbs-measures_images/imageFile40.png>)

- (12) P


µ(P) D(µ|P ξ∇f(y,·))µ|P(dy).

The proof focuses on this expression, but also yields a bound on DTC(µ) as a by-product. This feature of our work bears a curious resemblance to another part of Eldan’s paper [Eld]. For a Gibbs measure µ deﬁned relative to a standard Gaussian distribution on Rn, rather than on a hypercube, [Eld, Theorem 4] gives an upper bound on the deﬁcit in the Gaussian logarithmic Sobolev inequality satisﬁed by µ in terms of the gradient complexity (measured using Gaussian width) of its potential function. In view of the relationship between DTC and deﬁcits in logarithmic Sobolev inequalities, already remarked following Lemma 2.4 above, our bound on DTC(µ) (Theorem A part (a)) could be an analog of that deﬁcit bound in [Eld]. We do not explore this connection further here.

To lighten notation during the rest of this section, let us abbreviate D ν

λi to D(ν)

i∈S

whenever S ⊆ [n] and ν ∈ Prob( i∈S Ki).

Before the formal proof, let us give an informal sketch highlighting the relevance of Lemma 3.1. In this sketch, we assume that Ki = {0,1} for each i. In this case each discrete gradient ∇f(x, ·) may be identiﬁed with a vector in Rn: its ith entry is

- (13) f(x1,x2,... ,xi−1,1,xi+1,... ,xn)−f(x1,x2,... ,xi−1,0,xi+1,... ,xn).


Conversely, any vector u ∈ Rn deﬁnes a linear function on {0,1}n using the Euclidean inner product: u(y) := i uiyi. If u is the vector given by (13),

- then u(y) agrees with our earlier deﬁnition of ∇f(x,y) if we choose the


reference points ∗i = 0 for each i.

To simplify this sketch further, let us also imagine that the discrete gradient ∇f(x, ·) takes only two distinct values in Rn, say u and v. (This is really a fantasy: a short exercise shows that, if f is not linear itself, then its discrete gradient function takes at least four distinct values. But the story is simplest if we pretend there are just two.)

Under these assumptions, we take the partition P to consist of P := {x : ∇f(x, ·) = u} and Pc := {x : ∇f(x, ·) = v}.

Assume further that neither of the values µ(P), µ(Pc) is close to zero. (If one of them is close to zero, then a slightly degenerate version of the ensuing discussion applies.) So we need to show that D(µ|P ξu) and D(µ|Pc ξv) are both small relative to n.

Here are the steps in the proof:

- • Gibbs’ variational principle lets us interpret this requirement another

way: µ|P must come close to saturating the variational inequality that characterizes the product measure ξu, meaning that

(14) D(µ|P)− u dµ|P is not much larger than D(ξu)− u dξu relative to n, and similarly when comparing µ|Pc with ξv.

- • For each of µ|P and µ|Pc separately, we have no clear way to control the gap in (14). But we can control the average of those two gaps over P and Pc, keeping in mind that ∇f(x, ·) equals u on P and v on Pc respectively. By Lemma 2.1, the average of the KL divergences is


µ(P) · D(µ|P) + µ(Pc) · D(µ|Pc) = D(µ) + Hµ(P), and by Corollary 2.5 this is equal to

D(ξ∇f(x,·))µ(dx) − DTC(µ) + Hµ(P)

= µ(P) · D(ξu) + µ(Pc) · D(ξv) − DTC(µ) + Hµ(P). The average of the required integrals is

µ(P) u dµ|P + µ(Pc) v dµ|Pc

=

u dµ +

P

v dµ

Pc

- = ∇f(x,x) µ(dx)
- = ∇f(x,y) ξ∇f(x,·)(dy)µ(dx)


= µ(P) u(y) ξu(dy) + µ(Pc) v(y) ξv(dy).

The equality of the third and fourth lines here is the crucial appearance of Lemma 3.1. Combining these calculations of averages, we arrive at

µ(P) · D(µ|P ξu) + µ(Pc) · D(µ|Pc ξv)

= µ(P) D(µ|P) − u dµ|P − µ(P) D(ξu) − u dξu

+ µ(Pc) D(µ|Pc) − v dµ|Pc − µ(Pc) D(ξv) − v dξv

(15)

= −DTC(µ) + Hµ(P).

- • Since DTC is non-negative, the last line above is at most Hµ(P) ≤ log |P| = log 2. This is indeed small compared to n, and hence so


are both D(µ|P ξu) and D(µ|Pc ξv). Moreover, the last line above cannot be negative, since it is a positive combination of diﬀerences in the variational principle. So we also ﬁnd that DTC(µ) ≤ log 2.

Now we give the careful proof in full. Proof of Theorem A. Start by considering a single P ∈ P. For any

additively separable function g, Proposition 2.2 gives

D(µ|P ξg) = D(µ|P) − g dµ|P − D(ξg) − g dξg .

Let us average this identity over g = ∇f(x, ·) where x ∼ µ|P. The result is

D(µ|P ξ∇f(x,·))µ|P(dx)

= D(µ|P) − ∇f(x,y) µ|P(dy)µ|P(dx)

− D(ξ∇f(x,·))µ|P(dx) + ∇f(x,y) ξ∇f(x,·)(dy)µ|P(dx).

Now we average this equality over P ∈ P with the weights µ(P). The third right-hand term simpliﬁes according to the law of total probability:

P

µ(P) D(ξ∇f(x,·))µ|P(dx) = D(ξ∇f(x,·))µ(dx).

The fourth right-hand term simpliﬁes similarly. After these simpliﬁcations we are left with

P

µ(P) D(µ|P ξ∇f(y,·))µ|P(dy)

=

P

µ(P) · D(µ|P) −

P

µ(P) ∇f(x,y)µ|P(dy)µ|P(dx)

- (16) − D(ξ∇f(x,·))µ(dx) + ∇f(x,y)ξ∇f(x,·)(dy)µ(dx).


Next we re-write the right-hand side of (16) by considering separately (i) the KL-divergence terms and (ii) the double-integral terms:

- (i) By Lemma 2.1 and Corollary 2.5, we have

P

µ(P) · D(µ|P) − D(ξ∇f(x,·))µ(dx)

= D(µ) + Hµ(P) − D(µ) + DTC(µ) = Hµ(P) − DTC(µ).

- (ii) Using Lemma 3.1 to substitute for the second double integral in (16), and then using the law of total probability, the diﬀerence of those double-integral terms is equal to


P

µ(P) − ∇f(x,y)µ|P(dy)µ|P(dx) + ∇f(y,y)µ|P(dy)

=

P

µ(P) ∇f(y,y) − ∇f(x,y) µ|P(dy)µ|P(dx).

Inserting these calculations into (16) and re-arranging slightly, we arrive at the identity

- (17) DTC(µ) + P

µ(P) D(µ|P ξ∇f(y,·))µ|P(dy)

= Hµ(P) +

P

µ(P) ∇f(y,y) − ∇f(x,y) µ|P(dy)µ|P(dx).

This identity generalizes equation (15) in the proof-sketch above. By our assumption (4), we have

|∇f(y,y) − ∇f(x,y)| < δn

whenever x and y lie in the same cell of P. This implies that the average of double integrals on the right-hand side of (17) is less than δn, and so

- (18) DTC(µ) +


P

µ(P) D(µ|P ξ∇f(y,·))µ|P(dy) < Hµ(P) + δn.

Both terms on the left-hand side of (18) are non-negative, so conclusions (a) and (b) of Theorem A follow immediately. Conclusion (b) implies conclusion

(c) using Marton’s inequality (Proposition 2.3) and H¨older’s inequality:

P

≤

≤

![image 41](<2018-austin-structure-low-complexity-gibbs-measures_images/imageFile41.png>)

µ(P) dn(µ|P,ξ∇f(y,·))µ|P(dy)

![image 42](<2018-austin-structure-low-complexity-gibbs-measures_images/imageFile42.png>)

- 1

![image 43](<2018-austin-structure-low-complexity-gibbs-measures_images/imageFile43.png>)

- 2n


µ(P)

D(µ|P ξ∇f(y,·)) µ|P(dy)

P

![image 44](<2018-austin-structure-low-complexity-gibbs-measures_images/imageFile44.png>)

- 1

![image 45](<2018-austin-structure-low-complexity-gibbs-measures_images/imageFile45.png>)

- 2n


D(µ|P ξ∇f(y,·))µ|P(dy).

µ(P)

P

![image 46](<2018-austin-structure-low-complexity-gibbs-measures_images/imageFile46.png>)

![image 47](<2018-austin-structure-low-complexity-gibbs-measures_images/imageFile47.png>)

![image 48](<2018-austin-structure-low-complexity-gibbs-measures_images/imageFile48.png>)

![image 49](<2018-austin-structure-low-complexity-gibbs-measures_images/imageFile49.png>)

The proof above is quite insensitive to the structure of the spaces Ki. When Ki = {−1,1}, it yields similar results to those obtained from Eldan’s diﬀusion approach. But one can imagine ‘even smaller’ marginal spaces:

Question 3.2. Can the structural results be improved when Ki = {−1,1} and the reference measures λi are highly biased, for instance when

λi{1} = p ≪ 1 for each i? Next let us ﬁll in the proof of Corollary A′ from Theorem A. Proof of Corollary A′ from Theorem A. Let Q be a partition of

∇f(x, ·) : x ∈

i

Ki

into sets of  · -diameter less than δn, and let P be the pullback of Q under the map x  → ∇f(x, ·). Now pick an element yP in each P ∈ P which minimizes dn(µ|P,ξ∇f(y

![image 50](<2018-austin-structure-low-complexity-gibbs-measures_images/imageFile50.png>)

P,·)), and set gP := ∇f(yP, ·). The ﬁrst desired inequality follows from part (b) of Theorem A, and then the second follows by the same use of Proposition 2.3 as above.

![image 51](<2018-austin-structure-low-complexity-gibbs-measures_images/imageFile51.png>)

![image 52](<2018-austin-structure-low-complexity-gibbs-measures_images/imageFile52.png>)

![image 53](<2018-austin-structure-low-complexity-gibbs-measures_images/imageFile53.png>)

![image 54](<2018-austin-structure-low-complexity-gibbs-measures_images/imageFile54.png>)

3.1. Possible variations on Theorem A. The proof of Theorem A pivots around the identity (17). As Amir Dembo has emphasized to me, this identity may have other valuable consequences. The double integral on the right seems to deserve particular attention. In the proof above we simply use a uniform bound on the integrand ∇f(y,y)−∇f(x,y). Are there other ways to bound this double integral, perhaps by exploiting further the special structure of the Gibbs measure µ? The reward could be a result similar to Theorem A but with weaker hypotheses.

In a separate direction, one could try replacing the use of Marton’s inequality (Proposition 2.3) in Theorem A with a diﬀerent transportationentropy inequality. In [Dem97], Dembo proves several analogs of Proposi-

![image 55](<2018-austin-structure-low-complexity-gibbs-measures_images/imageFile55.png>)

- tion 2.3 that replace dn with various alternative transportation-like quantities. Those analogs then recover some powerful variations on product-space measure concentration that were previously discovered and used by Talagrand [Tal95]. It might be worth exploring a version of Theorem A part (c) for one of those alternative transportation-like quantities.


Further possibilities arise if we know more about the coordinate spaces Ki. We have already mentioned the case of two-point spaces in connection with the foundational papers [CD16] and [Eld], but other special examples are also worth considering. For example, if Ki = [0,1] for each i and if f : [0,1]n −→ R is diﬀerentiable, then we can imagine using its gradient Df in the usual sense of calculus as a substitute for our discrete gradient ∇f. Regarding Df as a function from [0,1]n to Rn, we can still measure its ‘complexity’ in terms of covering numbers, and seek a description of the corresponding Gibbs measures µ if this ‘complexity’ is small enough. Some of the steps above should adapt with little change, but a few sticking points stand out. Perhaps most important is Lemma 3.1, which depends on recognizing ξ∂i(x ·) as the conditional distribution of xi under µ given the other coordinates x[n]\i. This identiﬁcation does not carry over simply to a more ‘localized’ notion of gradient than ∇f. As a result, Lemma 3.1 would have to be replaced with a diﬀerent calculation, probably involving some extra terms whose control requires new methods or assumptions (perhaps on the second derivatives of f, by analogy with some of the estimates in [CD16]).

3.2. An alternative approach using the DTC bound. We have seen that

- conclusion (a) of Theorem A emerges naturally during the course of proving
- conclusion (b), and that conclusion (b) implies conclusion (c). However, according to [Aus, Theorem A], conclusion (a) by itself implies something like conclusion (c). To be precise, if µ is a probability measure on a product


space i Ki for which DTC(µ) ≤ r3n, then [Aus, Theorem A] asserts that µ can be a represented as a mixture

µ =

µy ν(dy)

L

such that (i) the mutual information in the mixture is at most DTC(µ) and (ii) there is a measurable family (ξy : y ∈ L) of product measures on i Ki satisfying

![image 56](<2018-austin-structure-low-complexity-gibbs-measures_images/imageFile56.png>)

dn(µy,ξy)ν(dy) < 2r.

L

In our setting, if we know that Hµ(P) + δn ≤ r3n,

- then this gives such a mixture representation of µ with mutual information at


most Hµ(P)+δn. This is a softer route with a similar conclusion to Theorem A part (c). It gives only a mixture with controlled mutual information, rather than a controlled number of terms, but one could then obtain the latter using [Aus18, Theorem 9.5]. However, this approach gives weaker estimates than the proof of Theorem A above, which exploits more directly the special nature of our Gibbs measures.

3.3. Comparison with Eldan’s main structure theorem. In this subsection C stands for several universal constants which are not computed explicitly. The value of C may change from one appearance to the next.

In [Eld], Eldan considers a Gibbs measure µ as in (1) on the space {−1,1}n. In this case, each discrete gradient ∇f(x, ·) may be identiﬁed with a vector in Rn: this is similar to (13) except using 1 and −1 instead of 1 and 0. (To be precise, this diﬀers from Eldan’s convention by a factor of 1/2, which aﬀects a few of the constants below.) Eldan measures the ‘complexity’ of f relative to linear functions by the Gaussian width of the set of its discrete gradients:

D(f) := GW ∇f(x, ·) : x ∈ {−1,1}n ∪ {0} .

This quantity is called the ‘Gaussian-width gradient complexity’ of f. Eldan’s main structure theorem [Eld, Theorem 3] represents a Gibbs measure µ as a mixture of other measures which (i) are mostly close to product measures in dn and (ii) on average carry almost as much entropy as µ itself, where the quality of these estimates depends on D(f).

![image 57](<2018-austin-structure-low-complexity-gibbs-measures_images/imageFile57.png>)

Let us write γ := D(f)/n for convenience. Speciﬁcally, after ﬁxing ε > 0 and also picking an auxiliary parameter α > 1, [Eld, Theorem 3] provides a mixture

µ = µθ m(dθ) over some space of parameters θ such that

- i) H(µ) − H(µθ)m(dθ) < Cεn and
- ii) there is a subset Θ of values of θ such that m(Θ) > 1 − n1 − α1 and such that every θ ∈ Θ satisﬁes


![image 58](<2018-austin-structure-low-complexity-gibbs-measures_images/imageFile58.png>)

![image 59](<2018-austin-structure-low-complexity-gibbs-measures_images/imageFile59.png>)

![image 60](<2018-austin-structure-low-complexity-gibbs-measures_images/imageFile60.png>)

![image 61](<2018-austin-structure-low-complexity-gibbs-measures_images/imageFile61.png>)

dn(µθ,ξvθ) ≤ C αγ/ε for some product measure ξvθ.

Eldan’s theorem gives other conclusions as well, such as bounds on the vectors vθ. The ingredients in Eldan’s mixture are ‘tilts’ of µ, whereas in our work they are the conditioned measures µ|P. We do not explore these features further here, although the special structure of tilts does seem to give an advantage in some of Eldan’s applications of his method (particularly the proof of [Eld, Theorem 1]).

By Sudakov’s minoration [LT11, Theorem 3.18] and the inequality  · 1 ≤ √n · 2, the covering numbers of a nonempty subset K ⊆ Rn are related to Gaussian width according to

![image 62](<2018-austin-structure-low-complexity-gibbs-measures_images/imageFile62.png>)

δ√n log covδn(K, · 1) ≤ C · GW(K) ∀δ > 0.

![image 63](<2018-austin-structure-low-complexity-gibbs-measures_images/imageFile63.png>)

![image 64](<2018-austin-structure-low-complexity-gibbs-measures_images/imageFile64.png>)

Also, our identiﬁcation of each discrete gradient with a vector in Rn satisﬁes  ∇f(x, ·) ≤  ∇f(x, ·) 1, where · denotes the uniform norm for functions on {−1,1}n as previously. Therefore, with γ as above, we have

- (19) log covδn {∇f(x, ·) : x ∈ {−1,1}n}, · ≤ C D(f)2 δ2n

![image 65](<2018-austin-structure-low-complexity-gibbs-measures_images/imageFile65.png>)

= C

γ2 δ2

![image 66](<2018-austin-structure-low-complexity-gibbs-measures_images/imageFile66.png>)

n

for all δ > 0. For a given δ, this gives (5) with ε = γ2/δ2 up to a multiplicative constant. Thus, assuming a bound on γ does not force a particular choice of ε and δ in (5), but sets up a trade-oﬀ between them.

After making a choice of δ in (19) and letting ε := γ2/δ2, the partition in Corollary A′ satisﬁes

- (20) H(µ) −

P

µ(P)H(µ|P) = Hµ(P) ≤ Cεn

for the approximation of entropies, and the conclusion of Corollary A′ gives

- (21)


γ √ε ≤ C max √ε, γ/√ε .

![image 67](<2018-austin-structure-low-complexity-gibbs-measures_images/imageFile67.png>)

![image 68](<2018-austin-structure-low-complexity-gibbs-measures_images/imageFile68.png>)

![image 69](<2018-austin-structure-low-complexity-gibbs-measures_images/imageFile69.png>)

![image 70](<2018-austin-structure-low-complexity-gibbs-measures_images/imageFile70.png>)

![image 71](<2018-austin-structure-low-complexity-gibbs-measures_images/imageFile71.png>)

µ(P) · dn(µ|P,ξgP ) ≤ C ε +

![image 72](<2018-austin-structure-low-complexity-gibbs-measures_images/imageFile72.png>)

![image 73](<2018-austin-structure-low-complexity-gibbs-measures_images/imageFile73.png>)

P

If ε ≤ γ2/3 then (20) matches Eldan’s conclusion (i) above up to a constant, and the right-hand side of (21) is C γ/√ε, which improves on Eldan’s conclusion (ii) when ε is very small.

![image 74](<2018-austin-structure-low-complexity-gibbs-measures_images/imageFile74.png>)

![image 75](<2018-austin-structure-low-complexity-gibbs-measures_images/imageFile75.png>)

However, if ε > γ2/3 (equivalently, δ < γ2/3), then the right-hand side of (21) is C√ε. In this case we may reduce ε (equivalently, increase δ) and improve both of the bounds (20) and (21). So there is no value in using our estimates with ε > γ2/3. By contrast, Eldan’s bounds are still potentially useful in this range, which enables them to perform better than ours in some applications. We discuss an example at the end of Section 5.

![image 76](<2018-austin-structure-low-complexity-gibbs-measures_images/imageFile76.png>)

This comparison brings up an interesting puzzle:

Question 3.3. Suppose we begin with a bound on γ and then use (19)

- to establish the trade-oﬀ ε = γ2/δ2. Can we vary the proof of Theorem A so that there is some beneﬁt to choosing δ < γ2/3? This would mean that at least one of the left-hand sides of (20) and (21) is bounded more eﬀectively when δ < γ2/3 than when δ ≥ γ2/3. (I would guess that any improvement must be to (21).)


4. A characterization of the terms in the mixture. In this section, we suppose that the discrete gradient function

i

Ki −→ Cb

i

Ki : x  → ∇f(x, ·)

is Lipschitz from dn to the uniform norm · . Let

L := sup  ∇f(x, ·) − ∇f(y, ·) dn(x,y)

: x,y ∈

![image 77](<2018-austin-structure-low-complexity-gibbs-measures_images/imageFile77.png>)

i

Ki distinct

be its Lipschitz constant (beware: L is not the Lipschitz constant of f itself).

Let P be a partition of i Ki as in Corollary A′, and let yP ∈ P for P ∈ P be a selection of points that minimize the distances dn(µ|P,ξ∇f(y

![image 78](<2018-austin-structure-low-complexity-gibbs-measures_images/imageFile78.png>)

P,·)). Recall that the functions gP of Corollary A′ are then given by gP := ∇f(yP, ·).

Proposition 4.1. These data satisfy

P

µ(P) gP − ∇f(x, ·) ξgP(dx) ≤ δn + L

![image 79](<2018-austin-structure-low-complexity-gibbs-measures_images/imageFile79.png>)

Hµ(P) n

- 1

![image 80](<2018-austin-structure-low-complexity-gibbs-measures_images/imageFile80.png>)

- 2


+ δ .

![image 81](<2018-austin-structure-low-complexity-gibbs-measures_images/imageFile81.png>)

Assuming that the right-hand side here is small, this means that most of the probability vector (µ(P) : P ∈ P), when transferred to the list of functions (gP : P ∈ P), is on terms that satisfy the ‘approximate ﬁxed point’ equation

- (22) gP ≈ ∇f(x, ·) ξgP (dx).


Proof. Since yP ∈ P, our assumption (4) about P gives

gP − ∇f(x, ·) µ|P(dx) < δn ∀P ∈ P. On the other hand, the deﬁnition of L gives

![image 82](<2018-austin-structure-low-complexity-gibbs-measures_images/imageFile82.png>)

∇f(x, ·) µ|P(dx) − ∇f(x, ·) ξgP (dx) ≤ L · dn(µ|P,ξgP ) ∀P ∈ P.

Averaging over P with weights µ(P), the result follows by conclusion (c) of Theorem A and the triangle inequality.

![image 83](<2018-austin-structure-low-complexity-gibbs-measures_images/imageFile83.png>)

![image 84](<2018-austin-structure-low-complexity-gibbs-measures_images/imageFile84.png>)

![image 85](<2018-austin-structure-low-complexity-gibbs-measures_images/imageFile85.png>)

![image 86](<2018-austin-structure-low-complexity-gibbs-measures_images/imageFile86.png>)

In the special setting of {−1,1}n, the approximate equation (22) admits an alternative form which resembles its counterpart in [EG18] more closely. In that setting, we can identify each discrete gradient ∇f(x, ·) with a vector in Rn, as previously. Also, any product measure on {−1,1}n is uniquely speciﬁed by its barycentre in [−1,1]n. Let mP be the barycentre of ξgP for each P. After these identiﬁcations, equation (22) is equivalent to

- (23) mP ≈ tanh ∇f(x, ·) ξgP (dx) = tanh D f(mP) ,


where f is the harmonic extension of f to [−1,1]n (see [Eld, Subsubsection

- 3.1.1]), D f is its derivative in the usual sense of calculus, and tanh is applied coordinate-wise. Equation (23) is essentially the same as [EG18, equation


(8)].

Let us return to the formulation in terms of gP rather than mP, but derive from Proposition 4.1 a bound in terms of the Gaussian-width gradient complexity D(f) studied by Eldan. Let γ := D(f)/n, as previously; consider an auxiliary parameter δ > 0; and choose a partition P as promised by inequality (19) for this δ. Then (20) lets us turn Proposition 4.1 into

P

µ(P) gP − ∇f(x, ·) ξgP(dx) ≤ δn + CL

![image 87](<2018-austin-structure-low-complexity-gibbs-measures_images/imageFile87.png>)

γ2 δ2

+ δ ∀δ > 0

![image 88](<2018-austin-structure-low-complexity-gibbs-measures_images/imageFile88.png>)

(where once again C is a universal constant that we do not estimate explicitly, and may change value when it appears again below).

In the regime L ≥ Cn, which seems to be more relevant to applications, the second right-hand term above is the more signiﬁcant. To minimize it, we make the choice δ := γ2/3. Assuming also that γ is small, we are left with

P

µ(P) gP − ∇f(x, ·) ξgP (dx) ≤ γ2/3n + CLγ1/3 ≤ CLγ1/3.

A result of this ﬂavour is obtained by Eldan and Gross in [EG18, Theorem 9]. But their estimates have quite a diﬀerent shape from ours (for instance, they also involve the Lipschitz constant of f itself, not just that of ∇f), and a direct comparison seems diﬃcult.

5. Approximation of partition functions. One of the main potential applications of Theorem A is to the estimation of the partition function

ef dλ. By Proposition 2.2, it satisﬁes

- (24) log ef dλ ≥ f dν − D(ν λ)

for any probability measure ν on i Ki, with equality if and only if ν = µ, the Gibbs measure associated to f. A structural result like Theorem A allows

one to achieve approximate equality using a product measure ν on the righthand side. This can help us estimate the expression on the left.

Proposition 5.1. If f is L-Lipschitz for the metric dn and satisﬁes (5), then

- (25) log ef dλ ≤ sup ξ

f dξ − D(ξ λ) + (ε + δ)n +

![image 89](<2018-austin-structure-low-complexity-gibbs-measures_images/imageFile89.png>)

ε + δ 2

![image 90](<2018-austin-structure-low-complexity-gibbs-measures_images/imageFile90.png>)

L,

where the supremum runs over product measures on i Ki.

Remark. In case each Ki is ﬁnite and λi is uniform, standard manipulations turn (25) into

log

x

ef(x) ≤ sup

ξ

H(ξ) + f dξ + (ε + δ)n +

![image 91](<2018-austin-structure-low-complexity-gibbs-measures_images/imageFile91.png>)

ε + δ 2

![image 92](<2018-austin-structure-low-complexity-gibbs-measures_images/imageFile92.png>)

L.

This is the relevant form for many applications of nonlinear large deviations.

Proof. Let P be the partition implied by (5). Gibbs’ identity and Corollary 2.5 give

log ef dλ = f dµ − D(µ λ)

- (26) = f dµ + DTC(µ) − D(ξ∇f(y,·) λ)µ(dy). Using part (c) of Theorem A, we have

f dµ =

P

µ(P) f dµ|P

≤ f dξ∇f(y,·) µ(dy) + L

P

µ(P) dn(µ|P,ξ∇f(y,·))µ|P(dy)

![image 93](<2018-austin-structure-low-complexity-gibbs-measures_images/imageFile93.png>)

≤ f dξ∇f(y,·) µ(dy) +

![image 94](<2018-austin-structure-low-complexity-gibbs-measures_images/imageFile94.png>)

ε + δ 2

![image 95](<2018-austin-structure-low-complexity-gibbs-measures_images/imageFile95.png>)

- (27) L.


Inserting this bound and also part (a) of Theorem A into (26), we obtain

log ef dλ ≤ f dξ∇f(y,·)−D(ξ∇f(y,·) λ) µ(dy)+(ε+δ)n+

![image 96](<2018-austin-structure-low-complexity-gibbs-measures_images/imageFile96.png>)

ε + δ 2

L.

![image 97](<2018-austin-structure-low-complexity-gibbs-measures_images/imageFile97.png>)

Now we bound the integral over y by the supremum over all product measures ξ, as in (25).

![image 98](<2018-austin-structure-low-complexity-gibbs-measures_images/imageFile98.png>)

![image 99](<2018-austin-structure-low-complexity-gibbs-measures_images/imageFile99.png>)

![image 100](<2018-austin-structure-low-complexity-gibbs-measures_images/imageFile100.png>)

![image 101](<2018-austin-structure-low-complexity-gibbs-measures_images/imageFile101.png>)

Partition-function estimation was the heart of the original paper [CD16] which instigated research into nonlinear large deviations. A general discussion of the usefulness of such estimates is given in the Introduction to that paper. In [Yan], Yan extends Chatterjee and Dembo’s estimates from the cube {0,1}n to a more general class of products of subsets of Banach spaces. In the setting of {−1,1}n, Eldan shows how partition-function estimates can be derived from his main structure theorem in [Eld, Corollary 2]. One can compare Proposition 5.1 with Eldan’s results using the ideas from Subsec-

- tion 3.3, but I have not been able to recover the full strength of Eldan’s estimate as a consequence of Theorem A. This seems to be related to the discussion at the end of Subsection 3.3 above. In the notation of that discussion, the appropriate choice of ε for the proof of [Eld, Corollary 2] is


C

L n

![image 102](<2018-austin-structure-low-complexity-gibbs-measures_images/imageFile102.png>)

2/3

γ1/3,

which is generally much larger than the threshold ε = γ2/3 that marks the end of the usefulness of our estimates, as discussed in Subsection 3.3.

REFERENCES

[Aug] Fanny Augeri. Nonlinear large deviation bounds with applications to traces of Wigner matrices and cycles counts in Erd˝s–Re´nyi graphs. Preprint, available online at arXiv.org: 1810.01558.

[Aus] Tim Austin. Multi-variate correlation and mixtures of product measures. Preprint, available online at arXiv.org: 1809.10272. [Aus18] Tim Austin. Measure concentration and the weak Pinsker property. Publ. Math. Inst. Hautes Etudes´ Sci., 128:1–119, 2018.

[BGLZ17] Bhaswar B. Bhattacharya, Shirshendu Ganguly, Eyal Lubetzky, and Yufei Zhao. Upper tails and independence polynomials in random graphs. Adv. Math., 319:313–347, 2017.

[BGSZ] Bhaswar B. Bhattacharya, Shirshendu Ganguly, Xuancheng Shao, and Yufei Zhao. Upper tail large deviations for arithmetic progressions in a random set. Preprint, available online at arXiv.org: 1605.02994.

[CD] Nicholas Cook and Amir Dembo. Large deviations of subgraph counts in Erd˝s– Re´nyi random graphs. Preprint, available online at arXiv.org: 1809.11148.

[CD16] Sourav Chatterjee and Amir Dembo. Nonlinear large deviations. Adv. Math., 299:396–450, 2016.

[Cha17] Sourav Chatterjee. Large deviations for random graphs, volume 2197 of Lecture Notes in Mathematics. Springer, Cham, 2017. Lecture notes from the 45th Probability Summer School held in Saint-Flour, June 2015, Ecole´ d’Ete´´ de Probabilite´s de Saint-Flour. [Saint-Flour Probability Summer School].

[Csi75] I. Csisz´r. I-divergence geometry of probability distributions and minimization problems. Ann. Probability, 3:146–158, 1975. [CT06] Thomas M. Cover and Joy A. Thomas. Elements of information theory. WileyInterscience [John Wiley & Sons], Hoboken, NJ, second edition, 2006. [Dem97] Amir Dembo. Information inequalities and concentration of measure. Ann. Probab., 25(2):927–939, 1997.

[Dud02] R. M. Dudley. Real analysis and probability, volume 74 of Cambridge Studies in Advanced Mathematics. Cambridge University Press, Cambridge, 2002. Revised reprint of the 1989 original.

[DZ10] Amir Dembo and Ofer Zeitouni. Large deviations techniques and applications, volume 38 of Stochastic Modelling and Applied Probability. Springer-Verlag, Berlin, 2010. Corrected reprint of the second (1998) edition.

[EG] Ronen Eldan and Renan Gross. Exponential random graphs behave like mixtures of stochastic block models. Preprint, available online at arXiv.org: 1707.01227.

[EG18] Ronen Eldan and Renan Gross. Decomposition of mean-ﬁeld Gibbs distributions into product measures. Electron. J. Probab., 23:Paper No. 35, 24, 2018.

[Eld] Ronen Eldan. Gaussian-width gradient complexity, reverse log-sobolev inequalities and nonlinear large deviations. Preprint, available online at arXiv.org: 1612.04346.

[Han75] Te Sun Han. Linear dependence structure of the entropy space. Information and Control, 29(4):337–368, 1975. [Han78] Te Sun Han. Nonnegative entropy measures of multivariate symmetric correlations. Information and Control, 36(2):133–156, 1978.

[LT11] Michel Ledoux and Michel Talagrand. Probability in Banach spaces. Classics in Mathematics. Springer-Verlag, Berlin, 2011. Isoperimetry and processes, Reprint of the 1991 edition.

[LZ17] Eyal Lubetzky and Yufei Zhao. On the variational problem for upper tails in sparse random graphs. Random Structures Algorithms, 50(3):420–436, 2017. [Mar86] K. Marton. A simple proof of the blowing-up lemma. IEEE Trans. Inform. Theory, 32(3):445–446, 1986. [Mar96] K. Marton. Bounding d-distance by informational divergence: a method to prove measure concentration. Ann. Probab., 24(2):857–866, 1996. [Mar98] Katalin Marton. Measure concentration for a class of random processes. Probab. Theory Related Fields, 110(3):427–439, 1998. [Pin64] M. S. Pinsker. Information and information stability of random variables and processes. Holden-Day, Inc., San Francisco-California, 1964. [Sam00] Paul-Marie Samson. Concentration of measure inequalities for Markov chains and Φ-mixing processes. Ann. Probab., 28(1):416–461, 2000.

![image 103](<2018-austin-structure-low-complexity-gibbs-measures_images/imageFile103.png>)

- [Tal95] Michel Talagrand. Concentration of measure and isoperimetric inequalities in product spaces. Inst. Hautes Etudes´ Sci. Publ. Math., (81):73–205, 1995.


- [Tal96] M. Talagrand. Transportation cost for Gaussian and other product measures. Geom. Funct. Anal., 6(3):587–600, 1996.


[Yan] Jun Yan. Nonlinear large deviations: beyond the hypercube. Preprint, available online at arXiv.org: 1703.08887.

UCLA Mathematics Department, Box 951555, Los Angeles, CA 90095-1555, U.S.A. E-mail: tim@math.ucla.edu

