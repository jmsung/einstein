---
type: source
kind: paper
title: Some Remarks on the Erdős Distinct Subset Sums Problem
authors: Stefan Steinerberger
year: 2022
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/2208.12182v2
source_local: ../raw/2022-steinerberger-some-remarks-erd-distinct.pdf
topic: general-knowledge
cites:
---

# arXiv:2208.12182v2[math.NT]2Jan2023

## SOME REMARKS ON THE ERDOS˝ DISTINCT SUBSET SUMS PROBLEM

STEFAN STEINERBERGER

Abstract. Let {a1, . . . , an} ⊂ N be a set of positive integers, an denoting the largest element, so that for any two of the 2n subsets the sum of all elements is distinct. Erd˝os asked whether this implies an ≥ c·2n for some universal c > 0. We prove, slightly extending a result of Elkies, that for any a1, . . . , an ∈ R>0

2 n

sin x x

π 2n

cos (aix)2dx ≥

R

i=1

with equality if and only if all subset sums are 1-separated. This leads to a new proof of the currently best lower bound an ≥ 2/πn · 2n. The main new insight is that having distinct subset sums and an small requires the random variable X = ±a1 ± a2 ± · · · ± an to be close to Gaussian in a precise sense.

1. Introduction A problem of Erd˝s [11] is as follows: if {a1,...,an} ⊂ N is a set of positive integers, assumed to be ordered as a1 < a2 < ··· < an, such that for each of the 2n subsets the sum of all elements is unique, does this force an ≥ c · 2n for some universal c > 0? The problem is quite old. Erd˝s [13] refers to it as “perhaps my ﬁrst serious conjecture which goes back to 1931 or 32”. Since the sums over all subsets leads to 2n − 1 distinct positive integers, one has ni=1 ai ≥ 2n − 1 (sharp for the powers of 2) and an 2n/n. Currently, the best known bound is

2n √n

an ≥ (c − o(1))

where diﬀerent estimates for c have been given over the years c ≥ 1/4 Erd˝s and Moser [11]

- ≥ 2/33/2 Alon and Spencer [2] ≥ 1/√π Elkies [10]

- ≥ 1/

√

3 Bae [3] , Guy [15] ≥ 3/2π Aliev [1]

- ≥ 2/π Dubroﬀ, Fox and Xu [9].




The literature (see [1]) mentions an unpublished manuscript of Elkies and Gleason also showing c ≥ 2/π. Dubroﬀ, Fox and Xu give two diﬀerent proofs: one appeals to the Berry-Esseen Theorem, the other uses an isoperimetric principle of

2010 Mathematics Subject Classiﬁcation. 05D05, 05D40. Key words and phrases. Erd˝os Distinct Subset Sums, Random Walk. S.S. is supported by the NSF (DMS-2123224) and the Alfred P. Sloan Foundation.

1

Harper [17]. In the other direction, we note that the powers of 2, with an = 2n−1, are not extremal: already in 1968, Conway and Guy [8] (answering another question by Erd˝s [12]) produced a candidate construction showing that an ≤ 2n−2 is possible (see Bohman [5]). The currently best construction is due to Bohman [6] showing an ≤ 0.88008 · 2n−2, see also [4, 7, 18, 19, 20]. It is an interesting question whether relaxing the condition somewhat can give rise to interesting examples. More concretely, are there sets {a1,...,an} ⊂ N such that the subset sums attain (1 − o(1)) · 2n distinct values and an = o(2n)?

The main purpose of our paper is to give a new proof of c ≥ 2/π. Many arguments, starting with Erd˝s and Moser [11], have considered the random walk X = ±a1 ± a2 ± ··· ± an, where all signs are chosen independently and uniformly at random. If all subset sums are distinct, then all 2n possible outcomes of the random walk are equally likely and they are all at least distance 2 from each other. A well-known argument (see [3, 11, 15, 18]) exploits this by using

2n−1

n

4n − 1 3

2 2n

(2k − 1)2 =

n · a2n ≥

a2i = E(X2) ≥

i=1

k=1

- which shows c ≥ 1/√3. This was further reﬁned by Dubroﬀ, Fox and Xu [9] who


argued, using the Berry-Esseen theorem, that if a2n is relatively small compared to n i=1 a2i (the variance of the random walk), then the random walk is well-described by a Gaussian. Our argument will imply a somewhat converse result: unless the distribution of the random walk is close to a Gaussian (in a sense that will be made precise), the set cannot have distinct subset sums and an small. This leads to an interesting reformulation of the Erd˝s distinct subset sums problem as a problem in probability theory: whether it is possible for random walks with a large variance but relatively small largest stepsize to emulate a Gaussian distribution very well.

2. Results

- 2.1. Main Results. We start with a basic analytic characterization of what it means for a set of n positive real numbers to have the property that all subset sums are at least distance 1 from each other (if all numbers are integers, then this is the same as asking them to be distinct).


- Theorem 1. Let a1,...,an > 0 be positive, real numbers. Then


2 n

sin2πx 2πx

- 1

- 2n+1


cos(2πaix)2dx ≥

.

R

i=1

Equality occurs if and only if all subset sums are distance ≥ 1 from each other.

This result is very similar to the analytic approach of Elkies [10] based on Laurent series. If all ai are integers, the product is 2π-periodic which simpliﬁes the integral and recovers the characterization used by Elkies.

- Corollary 1 (Elkies [10]). Let a1,...,an > 0 be positive integers. Then 1


n

- 1

- 2n


cos(2πaix)2dx ≥ with equality if and only if all subset sums are distinct.

0

i=1

All cosines in the product are aligned around x = 0. A natural approach is thus to bound the contribution coming from a small interval around the origin of length ∼ 1/an. If an is too small, that contribution is too large (see Lemma 1) and this was Elkies’ original approach to prove c ≥ 1/π (see Lemma 1). The main novelty of our approach is to analyze the contribution coming from outside that interval. This leads to Corollary 2.

## Corollary 2. We have

2n √n

2 π

an ≥ (1 − o(1)) ·

.

While Corollary 2 itself does not tell us anything new, the proof establishes a connection to probability theory which will be discussed in §2.2 and §2.3.

- 2.2. Proof of Corollary 2: Outline. We use Theorem 1. The ﬁrst ingredient is a lower bound on how much the integrand contributes to the integral close to the origin where all the cosines are aligned.

- Lemma 1 (see Elkies [10]). Suppose that {a1,...,an} is a subset of the positive real numbers. Then

|x|≤ 4a1n

sin2πx 2πx

2 n

i=1

cos(2πaix)2dx ≥ (1 + o(1)) ·

- 1

- 2


1 an

1 √πn

.

This Lemma in conjunction with Theorem 1 already shows c ≥ 1/√π. The main new idea is to prove that contributions far away from the origin can also be analyzed and that they also contribute a substantial amount.

- Lemma 2. Let c > 0. Suppose that {a1,...,an} ⊂ R>0 has 1-separated subset sums and, for some ε > 0, we have a2n ≤ c · n−2/3−ε ni=1 a2i. Then, as n → ∞,


|x|≥ 4a1n

sin2πx 2πx

2 n

i=1

cos(2πaix)2dx ≥ (1 + o(1))

√2 − 1 2√π

n

i=1

a2i

−1/2

.

We note that this lower bound can be bounded from below in terms of an using the trivial bound ni=1 a2i ≤ n · a2n. Combining this with Theorem 1 and Lemma 1, we see that if all subset sums are 1-separated, then

- 1

- 2n+1 ≥ (1 + o(1))


- 1

- 2


1 an

1 √πn

+

√2 − 1 2√π

1 √n · an

=

1 + o(1) √2π√n · an

which shows c ≥ 2/π. Lemma 2 appears to be very technical but contains an interesting idea which will tell us something new. Lemma 2 can be written in a completely diﬀerent way (Theorem 2) and this alternative formulation is also how we are going to prove Lemma 2.

- 2.3. Subset Sums and Gaussian Densities. Let A = {a1,...,an} ⊂ R>0 be a set of positive reals. As already indicated above, we consider the random variable


X = ni=1 εiai where εi ∈ {−1,1} independently and with equal likelihood (also known as Rademacher random variables). This random variable is distributed

according to some probability measure µ on R. Note that we can write X = −

n

n

ai + 2

ai.

i=1

i=1 εi=1

If the minimal distance between the sum of two diﬀerent subsets of A is 1, then the minimal distance between any two distinct values of X is two. Moreover, by the subset sum condition, X assumes 2n distinct values which implies

2n

- 1

- 2n


|xi − xj| = 2.

µ =

δx

where min

i

i =j

i=1

Our main question of interest will now be whether µ is close to a Gaussian (and, if so, in what sense). Consider ﬁrst a simple example: the set 1,2,...,2n−1 . It is easy to see that all subset sums are distinct (the uniqueness of binary expansion) and, following the construction, we see that µ is supported on all 2n odd numbers in [−2n,2n] roughly emulating a uniform distribution over that interval. A uniform distribution is not particularly close to a Gaussian overall. This will now be compared to a better construction: we take the ﬁrst 22 terms induced by the Conway-Guy sequence [8] (where 22 was chosen so as to be ‘large’ while still computationally feasible). We end up with a set {a1,...,a22} ⊂ N with distinct subset sums and a22 = 1051905 ∼ 0.51·221. The probability distribution of the associated random walk µ is shown in Figure 1. This is quite a bit closer to a Gaussian than uniform distribution would be. This is not a coincidence.

-2×107 -1×107 0 1×107 2×107

Figure 1. A histogram of the discrete measure µ derived from the ﬁrst 22 terms from the Conway-Guy sequence.

We start by trying to understand which Gaussian we should compare the distribution µ to. A Gaussian is uniquely determined by mean and variance. Since µ is symmetric around the origin, the expectation is EX = 0. Simultaneously, we have an explicit expression for the variance and

2

n

n

n

a2i. The probability density function of that Gaussian will be abbreviated as γ(x) =

E X2 = E

= E

εiai

εiεiaiaj =

i=1

i,j=1

i=1

 −

−1 .

−1/2

n

n

x2 2

1 √2π

a2i

a2i

exp

i=1

i=1

Note that γ is a smooth function while µ is a singular measure. To facilitate a comparison between the two, we will introduce a smoothed version of µ. Consider the normalized characteristic function h(x) = (1/2)·χ[−1,1]. Since both µ and h are probability measures, their convolution

2n

- 1

- 2


- 1

- 2n


(h ∗ µ)(x) =

χ[x

i−1,xi+1](x)

i=1

is also a probability measure. We observe that h ∗ µ is a sum of characteristic functions centered at the points xi at which µ is supported. Since µ is distributed over exponentially large scales, smoothing at scale 1 does not change any relevant characteristics. With this language in place, the second main result is as follows.

- Theorem 2. Let c > 0. Suppose {a1,...,an} ⊂ R>0 has 1-separated subset sums and a2n ≤ c · n−1/2 ni=1 a2i. Then, as n → ∞, we have


2 n

sin2πx 2πx

((h ∗ µ)(x) − γ(x))2 dx =

cos(2πaix)2dx + o(2−n).

R

|x|≥ 4a1n

i=1

We emphasize that h ∗ µ only assumes the values 0 and 2−n−1 (and the second value is assumed on 2n intervals of length 2). This implies that

−1/2

n

- 1

- 2√π


- 1

- 2n+1


(h ∗ µ)(x)2dx =

γ(x)2dx =

a2i

while

.

R

R

i=1

We also remark that the probability density of the random walk behaving similarly to a Gaussian was already used by Dubroﬀ, Fox and Xu who invoked the BerryEsseen theorem. Under a slightly stronger assumption (a2n ≤ c · n−2/3−ε ni=1 a2i) the Berry-Esseen theorem guarantees that

x

µ([−∞,x]) −

γ(y)dy = o(1)

sup

x∈R

−∞

which shows convergence of the cumulative distribution functions. Theorem 2 establishes that sets with distinct subset sums satisfy (using Theorem 1)

1 + o(1) 2n

((h ∗ µ)(x) − γ(x))2 dx ≤

R

measuring proximity of the probability density functions in the L2−sense.

- 2.4. Concluding Remarks. Theorem 2 has a fascinating implication insofar as it allows us to reinterpret the Erd˝s distinct subset sums problem (the general version with real numbers being 1-separated) as a genuine problem in probability theory asking whether particularly excellent random walks exist. More precisely, are there positive real numbers a1,...,an > 0 such that the random unbiased random walk X = ±a1 ± a2 ··· ± an has, simultaneously, (1) a large standard deviation, (2) a small largest element an and (3) the ability to approximate the normal distribution very well in a concrete sense?


Problem. Fix c > 0. As n → ∞, are there random walks X = ±a1 ± a2 ··· ± an such that the largest step size is small compared to the variance

√

largest stepsize = an ≤ c · n−1/3

VX.

and, simultaneously, X has a large variance and approximates a Gaussian well in the sense of

- 1

- 2√π


1 √

+

VX

1 + o(1) 2n+1

((h ∗ µ)(x) − γ(x))2 dx =

?

R

If there exist {a1,...,an} ⊂ N with distinct subset sums and an n−1/3−ε · 2n, then such random walks do indeed exists: this follows from combining Theorem 1, Theorem 2 and the computation carried out after the proof of Lemma 1.

Note that, considering the constraint on an being as small as possible and considering the structure of the ﬁrst term, it does seem like one would like to have many of the ai to be roughly comparable to an. The Conway-Guy [8] sequence has this property: for each ε > 0 at least n − cε log n terms satisfy ai ≥ (1 − ε)an. We also observe that for sets of that type, where many of the ai are comparable in size to an, one can draw additional information from Theorem 1

R

sinx x

2 n

π 2n

cos(aix)2dx =

.

i=1

The cosines are all aligned at x = 0, the contribution to the integral coming from close to the origin is really just a function of ni=1 a2i (see the comment after the proof of Lemma 1) and fairly independent of the arithmetic structure. The next interesting point is x = π/an: if we have ai = (1 + o(1))an for many 1 ≤ i ≤ n − 1, then many of the cosines will still be aligned at π/an. The only way to avoid a large contribution is to have an ai ∼ (1+o(1))an/2. So it is not inconceivable that Theorem 1 suggests a sort of multi-scale structure as being possibly favorable. The argument can then be continued for x = kπ/an for small k ∈ Z. As k gets larger, one would expect the cosines to decorrelate.

## 3.1. Proof of Theorem 1.

3. Proofs

Proof. As already mentioned, we will smooth µ by convolving with the normalized characteristic function h(x) = (1/2) · χ[−1,1]. Since both µ and h are probability measures, their convolution

2n

- 1

- 2n


(h ∗ µ)(x) =

i=1

- 1

- 2


χ[x

i−1,xi+1]

is also a probability measure. We observe that h ∗ µ is a sum of characteristic functions and its L1−norm is 1. Its L2−norm is minimized if and only if these characteristic functions do not overlap which is equivalent to mini =j |xi − xj| ≥ 2 and therefore, in turn, equivalent to all subset sums being at least distance 1 from

each other. Formally,

2

2n

1 4n R

- 1

- 2


h ∗ µ 2L2 =

χ[x

dx

i−1,xi+1]

i=1

2n

1 4n R

- 1

- 2


- 1

- 2


=

χ[x

χ[x

j−1,xj+1]dx

i−1,xi+1]

i,j=1

2n

1 4n R

1 2

- 1

- 2


≥

χ[x

χ[x

i−1,xi+1]dx

i−1,xi+1]

i=1

- 1

- 2n+1


- 1 4n

- 2n−1 =


.

=

This is the only inequality in the entire argument and is attained if and only if all xi are 2−separated. Using that the Fourier transform is unitary on L2 and sends convolution to products,

µ ∗ h 2L2 = µ ∗ h 2L2 = µ h 2L2 =

h(ξ)2 µ(ξ)2dξ.

R

It remains to compute the Fourier transforms: the Fourier transform of the characteristic function h is completely explicit

sin(2πξ) 2πξ

. The measure µ can itself be deﬁned as a convolution µ =

h(ξ) =

δ−a

δa

δ−a

δa

δ−a

δa

1

2

n

- 1

- 2 ∗


2

n

2 ∗ ··· ∗

. Using again that the Fourier transform sends convolution to products and δ−a

+

+

+

2

2

2

2

e2πi(−a

e2πia

iξ

i)ξ

δa

i

i

(ξ) =

= cos(2πaiξ) leads to

+

+

2

2

2

2

n

cos(2πaiξ). Thus

µ(ξ) =

i=1

2 n

- 1

- 2n+1


sin2πx 2πx

cos(2πaix)2dx ≥ with equality if and only if all subset sums of {a1,...,an} are 1-separated.

R

i=1

- 3.2. Proof of Corollary 1. Proof. If all ai are integers, then the product is 1−periodic and, together with


2

sin2π(x − k) 2π(x − k)

1 + cos(2πx) 2

=

,

k∈Z

this implies 2

2 n

n

1

sin2πx 2πx

cos(2πaix)2dx =

cos(2πaix)2dx.

(1 + cos(2πx))

R

0

i=1

i=1

To further evaluate the integral, we switch back to exponentials and note that

ix + e−4πia

e4πia

ix

1 2

cos(2πaix)2 =

+

4 leading to the integral

n

1

e2πix + e−2πix 2

ix + e−4πia

e4πia

ix

- 1

- 2n


1 +

.

1 +

2

0

i=1

Selecting the constant 1 in all terms leads to a contribution of 2−n. Any other choice of combinations from the big product leads to exponentials of the form exp(4πikx) where k ∈ Z \ {0} whenever all subset sums are distinct. Thus every other contributions leads to 0 and

n

1

- 1

- 2n


cos(2πaix)2dx ≥

0

i=1

if all subset sums are distinct. Conversely, if not all subset sums are distinct, then there is a corresponding choice of combinations in the product leading to a zero frequency: since all coeﬃcients are nonnegative, we see that the integral will then be larger than 2−n.

## 3.3. Proof of Lemma 1.

Proof, close to Elkies [10]. Note that, for example, an ≥ 2n/n, already implies that the interval is very close to the origin where sin(2πx)/(2πx) ∼ 1 and thus

2 n

n

sin2πx 2πx

cos(2πaix)2dx = (1 − o(1)))

cos(2πaix)2dx.

|x|≤ 4a1n

|x|≤ 4a1n

i=1

i=1

On this interval, we have, for all 1 ≤ i ≤ n − 1 that cos(2πaix) ≥ cos(2πanx) and

n

cos(2πaix)2dx ≥

cos(2πanx)2ndx

|x|≤ 4a1n

|x|≤ 4a1n

i=1

A change of variables and evaluating the integral (see [10]) shows that

- 1

- 2πan |x|≤π


cos(2πanx)2ndx =

cos(x)2ndx

|x|≤ 4a1n

2

π 4n

- 1

- 2πan


2n n

=

- 1

- 2


1 an

1 √πn

, where evaluating cos(x)2ndx in terms of binomial coeﬃcients is classical [16]. This implies a lower bound on an since

= (1 + o(1))

2 n

- 1

- 2n+1


sin2πx 2πx

cos(2πaix)2dx

=

R

i=1

2 n

sin2πx 2πx

- 1

- 2


1 an

1 √πn

cos(2πaix)2dx ≥ (1 + o(1))

≥

|x|≤ 4a1n

i=1

showing that an ≥ 2n/√πn which is, in spirit, the original argument of Elkies. We note that, provided an is small, i.e. an = o( ni=1 a2i), one can Taylor expand the cosines and, for x small,

n

n

a2i which then leads to the slightly reﬁned estimate

cos(2πaix)2dx ∼ exp −4π2x2

i=1

i=1

−1/2

n

n

(1 + o(1)) 2√π

cos(2πaix)2dxdx ≥

a2i

.

|x|≤ 4a1n

i=1

i=1

At this point, we do not know of any argument that excludes the possibility that n− o(n) of the ai satisfy ai = (1 + o(1))an and this reﬁned estimate does not currently lead to any information diﬀerent from that provided by the cruder estimate above. Indeed, the Conway-Guy sequence is an example of a set with distinct subset sums and this type of behavior, perhaps extremal conﬁgurations do behave like that.

- 3.4. Technical Lemma. The goal of this section is to establish an upper bound on the diﬀerence between µ and the approximating Gaussian measure close to the origin. Lemma 3 will then quickly imply Theorem 2.


Lemma 3. Let c > 0. Suppose {a1,...,an} ⊂ R>0 has 1-separated subset sums and a2n ≤ c · n−1/2 ni=1 a2i. Then, as n → ∞, we have

2

n

n

sin(2πx) 2πx

dx = o(2−n).

cos(2πaix) − exp −2π2x2

a2i

|x|≤ 4a1n

i=1

i=1

Proof. The ﬁrst step is a Taylor expansion around x = 0

n

n

sin(2πx) 2πx

sin(2πx) 2πx

cos(2πaix) =

exp

log (cos(2πaix))

i=1

i=1

n

sin(2πx) 2πx

log 1 − 2π2a2ix2 + O(a4ix4)

≤

exp

i=1

n

sin(2πx) 2πx

−2π2a2ix2 + O(a4ix4)

=

exp

i=1

n

2+na4nx4) exp −2π2x2

= eO(x

a2i . The goal is to bound

i=1

2

n

n

sin(2πx) 2πx

cos(2πaix) − exp −2π2x2

a2i

X =

dx

|x|≤ 4a1n

i=1

i=1

which, considering asymptotic expansion, can be bounded as

n

2

2+na4nx4) − 1

eO(x

exp −4π2x2

a2i dx.

X ≤

|x|≤ 4a1n

i=1

This bound by itself is a little bit too crude but is reasonably close to the origin: note that the integrand is the product of two functions the ﬁrst of which is small

for small values of x and the second of which is small for large x. This suggests splitting the integral into the regions: for some 0 < δ < 1/(4an) to be optimized later, we write I1 = {x : |x| ≤ δ} and let I2 = {x : δ ≤ |x| ≤ 1/(4an)}. Provided δ2 + na2nδ4 = O(1), we can estimate the integral over I1 as

n

2

2+na4nx4) − 1

eO(x

exp −4π2x2

a2i dx

Y =

I1

i=1

n

≤ O(δ2 + na4nδ4) ·

exp −4π2x2

a2i dx

R

i=1

−1/2

n

1 2√π

a2i

= O(δ2 + na4nδ4) ·

.

i=1

We use a diﬀerent type of expansion for the second region: note that, for |x| < π/2,

x2 2

log (cos(x)) ≤ −

and thus, for |x| ≤ 1/(4an), cos(2πaix) ≤ exp −2π2x2a2i from which we deduce

n

n

1 4an

cos(2πaix) ≤ exp −2π2x2

a2i .

∀|x| ≤

0 ≤

i=1

i=1

Therefore the contribution of the integrand to X over I2, which is

Z =

I2

exp −2π2x2

n

sin(2πx) 2πx

a2i −

i=1

n

cos(2πaix)

i=1

2

dx,

can be trivially bounded from above by

Z ≤

=

2

n

2 δ

exp −2π2x2

a2i

dx ≤

I2

i=1

n

2 δ

1 8π2 ni=1 a2i

exp −4δ2π2

i=1

n

∞

xexp −4π2x2

a2i dx

δ

i=1

n

1

1 δ

exp −δ2

a2i .

a2i ≤

n i=1 a2i

i=1

We want all error estimates to be o(2−n) and achieve this by setting

δ = αn

n

a2i

i=1

−1/2

with αn an arbitrarily slowly growing sequence (think of αn = log log log n). We start by checking whether our ﬁrst asymptotic expansion is valid in this regime, i.e.

whether δ2 + na2nδ4 = O(1). Moser’s estimate implies ni=1 a2i 4n and thus δ2 + na2nδ4 = O(αn24−n) + O(na2nαn44−2n) = o(2−n). The next step is an estimate on Y . Importing our upper bound on an shows

Y ≤ O(δ2 + na4nδ4)

n

a2i

i=1

−1/2

na4nαn4

n

a2i

i=1

−5/2

n−ε

n

a2i

i=1

−1/2

which is O(n−ε2−n) = o(2−n). Finally, for the last error term,

n

2−n αn

1 δ

1

2

e−α

n = o(2−n).

exp −δ2

a2i ≤ 10

Z ≤

n i=1 a2i

i=1

This proves Lemma 3.

- 3.5. Proof of Theorem 2. Proof. Theorem 2 is a relatively easy consequence of Lemma 3. Recall that


 −

−1 

−1/2

n

n

x2 2

1 √2π

a2i

a2i

exp

γ(x) =

i=1

i=1

and γ(x) = exp(−2π2x2 ni=1 a2i). Using the Fourier transform we get that X =

|(h ∗ µ)(x) − γ(x)|2dx =

|( h ∗ µ)(x) − γ(x)|2dx

R

R

can be written as

X =

R

sin(2πx) 2πx

n

n

cos(2πaix) − exp −2π2x2

a2i

i=1

i=1

2

dx.

Lemma 3 implies that if {a1,...,an} ⊂ R>0 has 1-separated subset sums and a2n ≤ c · n−1/2 ni=1 a2i, then

2

n

n

sin(2πx) 2πx

dx = o(2−n)

cos(2πaix) − exp −2π2x2

a2i

|x|≤ 4a1n

i=1

i=1

implying that, by splitting the integral into {|x| ≤ 1/(4an)} and {|x| ≥ 1/(4an)},

2

n

n

sin(2πx) 2πx

dx + o(2−n).

cos(2πaix) − exp −2π2x2

a2i

X =

|x|≥ 4a1n

i=1

i=1

Using the upper bound on an

exp −4π2x2

|x|≥1/(4an)

n

n

∞

a2i dx ≤ 8an

xexp −4π2x2

1/(4an)

i=1

i=1

n i=1 a2i

π2 4

an n i=1 a2i

≤

exp −

a2n 1 n1/4

√n.

1 ( ni=1 a2i)1/2

e−c

a2i dx

With Moser’s estimate ni=1 a2i 4n one deduces

exp −2π2x2

n

a2i χ|x|≥ 1

4an

i=1

L2(R)

√n 1 2n

e−c

.

Using the triangle inequality in L2, we see that

Z =

=

sin(2πx) 2πx

n

sin(2πx) 2πx

i=1

n

cos(2πaix) − exp −2π2x2

i=1

n

a2i χ|x|≥ 1

4an

i=1

cos(2πaix)χ|x|≥ 1

4an

√n 1 2n

+ O e−c

L2(R)

.

Squaring both sides and using Theorem 1, we deduce

L2(R)

X = Z2 + o(2−n) =

|x|≥ 4a1n

sin2πx 2πx

2 n

cos(2πaix)2dx + o(2−n).

i=1

- 3.6. Proof of Lemma 2. Throughout this proof, we will abbreviate


−1 

 −

−1/2

n

n

x2 2

1 √2π

a2i

a2i

exp

γ(x) =

i=1

i=1

for the Gaussian approximating µ. Before proving Lemma 2, we quickly recall the Berry-Esseen theorem which, in our setting, says that

n i=1 a3i

x

γ(x)dx ≤

µ([−∞,x]) −

sup

.

( ni=1 a2i)3/2

x∈R

−∞

Assuming that a2n = O n−2/3−ε ni=1 a2i , one can bound this by

n i=1 a3i

n · a3n ( ni=1 a2i)3/2

3ε

n−

2 = o(1).

( ni=1 a2i)3/2

The way we will use this information is that, for any interval J ⊂ R µ(J) −

γ(x)dx = o(1).

J

Note that this argument was also used by Dubroﬀ, Fox and Xu [9] for J an interval centered at the origin whose length is proportional to a small multiple of the standard deviation of the Gaussian. We will quickly summarize their short argument at an appropriate place in the proof of Lemma 2.

Proof of Lemma 2. We start the argument with a lower bound on X =

|(µ ∗ h)(x) − γ(x)|2 dx. Taking a Fourier transform,

R

X =

R

sin(2πx) 2πx

n

n

cos(2πaix) − exp −2π2x2

a2i

i=1

i=1

2

dx.

We split the integral into two regions: |x| ≤ 1/(4an) and the remaining region. Lemma 3 implies that the integral over the ﬁrst region is o(2−n), it remains to

analyze the integral over the second region. Arguing exactly as in the proof of Theorem 2, we deduce that

2 n

sin2πx 2πx

cos(2πaix)2dx + o(2−n).

X =

|x|≥ 4a1n

i=1

The next argument is completely independent of all the previous arguments: we will derive a lower bound on the same quantity via a completely diﬀerent argument which will then imply Lemma 2. Recall that

|(µ ∗ h)(x) − γ(x)|2 dx.

X =

R

µ ∗ h only assumes the values 0,2−n−1 . Moreover, by the argument above,

(µ ∗ h)(x)dx −

sup

J⊂R

J interval J

γ(x)dx = o(1).

J

This leads to an amusing setting: we know that µ∗h approximates the Gaussian in probability over intervals. Simultaneously, µ ∗ h can only assume two values one of which is 0: thus, the local density of the Gaussian predicts the density of intervals in the region where µ ∗ h assumes its nonzero value 2−n−1. An example of what this could look like is shown in Fig. 2. We conclude with a simple proposition.

Proposition. Let µ be the probability density function of a N(0,σ2) Gaussian. Let (νn)n be a sequence of probability density functions such that

- (1) νn → µ in probability: for every interval J ⊂ R we have

lim

n→∞ J

νn(x)dx =

J

µ(x)dx

- (2) and νn(x) only assumes two values {0,zn} for some zn > 0.


Then

√2 − 1 2√πσ

(µ(x) − νn(x))2dx ≥

.

liminf

n→∞ R

Proof of the Proposition. The density of µ is simply given by µ(x) =

x2 σ2

1 √2πσ

- 1

- 2


exp −

.

We note that both Properties combined require (by taking J to be a small interval centered around the origin) that

1 √2πσ

zn ≥ max x∈R

liminf

µ(x) =

.

n→∞

Let now J be a small interval centered around x0 ∈ R, say J = (x0 − ε,x0 + ε). The two properties combined tell us what can be expected of νn: since

µ(x)dx = 2εµ(x0) + O(ε2) we have

J

µ(x)dx = 2εµ(x0) + O(ε2).

lim

νn(x)dx =

n→∞ J

J

This allows us to deduce that the fraction α of the interval J where νn assumes the value zn and the remaining fraction (1 − α) where it assumes the value 0 is determined by

αzn = µ(x0) + lower order terms. This tells us that

µ(x) zn

µ(x) zn

µ(x)2dx. The integral algebraically simpliﬁes to

(µ(x) − zn)2 + 1 −

(µ(x) − νn(x))2dx = (1 + o(1))

R

R

µ(x) zn

µ(x) zn

(µ(x) − zn)2 + 1 −

µ(x)2dx =

µ(x)(zn − µ(x))dx. At this point, we recall that, up to lower order terms, zn ≥ µ(0). Thus

R

R

1 2√πσ which is the desired result.

1 √2πσ −

1 √2πσ − µ(x) dx =

µ(x)(zn − µ(x))dx ≥

µ(x)

R

R

Figure 2. A step function assuming only two values approximating a Gaussian density.

At this point can we quickly note, in passing, the original argument of Dubroﬀ, Fox and Xu [9]: the Gaussian attains its maximum density at the origin and therefore

−1/2

n

1 √2π

1 + o(1) 2n+1 from which one deduces

a2i

≤ (1 + o(1)) · µ ∗ h L∞ =

γ(0) =

i=1

1/2

n

√n · an ≥

2 π · 2n.

a2i

≥ (1 + o(1))

i=1

We can now conclude by applying the Proposition. The variance σ of the molliﬁed random walk is, up to lower order terms, given by the variance of the random walk which is ni=1 a2i. Thus, applying the Proposition, as n becomes large,

√2 − 1 2√π ( ni=1 a2i)1/2

X ≥ (1 + o(1))

.

### References

- [1] I. Aliev, Siegel’s lemma and sum-distinct sets, Discrete Comput. Geom. 39 (2008), 59–66.
- [2] N. Alon and J. H. Spencer, The probabilistic method, 4th ed. Wiley, Hoboken, NJ, 2016.
- [3] J. Bae, On subset-sum-distinct sequences. Analytic number theory, Vol. 1, Progr. Math., 138, Birkh¨auser, Boston, 1996, 31–37.
- [4] E. Behrends, Tupel aus n nat¨urlichen Zahlen, fu¨r die alle Summen verschieden sind, und ein Masskonzentrations-Pha¨nomen. Elemente der Mathematik, 74 (2019), p. 114-130.
- [5] T. Bohman, A sum packing problem of Erd˝os and the Conway-Guy sequence. Proceedings of the American Mathematical Society, 124 (1968), 3627-3636.
- [6] T. Bohman, A construction for sets of integers with distinct subset sum, the electronic journal of combinatorics 5 (1998), R3.
- [7] P. Borwein and M. Mossinghoﬀ, Newman polynomials with prescribed vanishing and integer sets with distinct subset sums. Math. Comp. 72 (2003), no. 242, 787–800.
- [8] J.H. Conway and R.K. Guy, Sets of natural numbers with distinct sums, Notices Amer. Math. Soc. 15 (1968), 345.
- [9] Q. Dubroﬀ, J. Fox and M. W. Xu, A note on the Erdos distinct subset sums problem. SIAM Journal on Discrete Mathematics, 35 (2021), 322–324.
- [10] N. Elkies, An improved lower bound on the greatest element of a sum-distinct set of ﬁxed order, Journal of Combinatorial Theory, Series A Volume 41 (1986), p. 89–94
- [11] P. Erdo˝s, Problems and results in additive number theory, Colloque sur la Theorie des Nombres, Bruxelles, 1955, pp. 127–137, George Thone, Liege; Masson and Cie, Paris, 1956.
- [12] P P. Erd˝os, Quelques proble`mes de the´orie des nombres, Monographies de l’Enseignement Math´ematique, No. 6 , pp. 81–135, L’Enseignement Mathe´matique, Universite´, Geneva, 1963
- [13] P. Erd˝os, Problems and results on extremal problems in number theory, geometry, and combinatorics, Proceedings of the 7th Fischland Colloquium, I (Wustrow, 1988), Rostock. Math. Kolloq. , No. 38 (1989), 6–14
- [14] R. K. Guy, Unsolved Problems in Intuitive Mathematics, Vol. I, Number Theory, Problem C8, Springer-Verlag (1981).
- [15] R. K. Guy, Sets of integers whose subsets have distinct sums, Theory and practice of combinatorics, 141–154, North-Holland Math. Stud., 60, Ann. Discrete Math., 12, North-Holland, Amsterdam, (1982).
- [16] I. S. Gradstheyn and I. M. Ryhzik, Table of Integrals, Series, and Products, Academic Press, New York, 1980.
- [17] L. H. Harper, Optimal numberings and isoperimetric problems on graphs, J. Combin. Theory 1 (1966), 385–393.
- [18] B. Lindstr¨om, Om ett problem av Erdo˝s fo¨r talf¨oljder, Nordisk Matematisk Tidskrift Vol. 16, No. 1/2 (1968), pp. 29-33
- [19] W. F. Lunnon, Integer sets with distinct subset-sums. Math. Comp. 50 (1988), 297–320.
- [20] R. Maltby, Bigger and better subset-sum-distinct sets. Mathematika 44 (1997), no. 1, 56–60.


Department of Mathematics, University of Washington, Seattle, WA 98195, USA Email address: steinerb@uw.edu

