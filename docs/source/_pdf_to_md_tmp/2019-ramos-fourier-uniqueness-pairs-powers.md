# arXiv:1910.04276v1[math.CA]9Oct2019

## FOURIER UNIQUENESS PAIRS OF POWERS OF INTEGERS

JOAO˜ P. G. RAMOS AND MATEUS SOUSA

Abstract. We prove, under certain conditions on (α, β), that each Schwartz function f such that f(±nα) = f(±nβ) = 0, ∀n ≥ 0 must vanish identically, complementing a series of recent results involving uncertainty principles, such as the pointwise interpolation formulas by Radchenko and Viazovska and the Meyer–Guinnand construction of self-dual crystaline measures.

1. Introduction Given an integrable function f : R → C, we deﬁne its Fourier transform by f(ξ) :=

f(x)e2πix·ξ dx. (1) Let us consider the following classical problem in Fourier analysis:

R

Question 1. Given a collection C of functions f : R → C, what conditions can we impose on two sets A, A ⊂ R to ensure that the only function f ∈ C such that f(x) = 0 for every x ∈ A and f(ξ) = 0 for every ξ ∈ A is the zero function?

Inspired by the notion of Heisenberg uniqueness pairs introduced by Hedenmalm and Montes-Rodrı´gues in [9], (see also [8, 11]), we refer to such pair of sets (A, A) as a Fourier uniqueness pair for C for a natural reason: the values of f(x) for x ∈ A and f(ξ) for ξ ∈ B determine at most one function f ∈ C. For simplicity, when A = A, we will say that A is a Fourier uniqueness set for C.

Perhaps the most classical result which answers such a question is the celebrated Shannon– Whittaker interpolation formula, which states that a function f ∈ L2(R) whose Fourier transform f is supported on the interval [−δ/2,δ/2] is given by the formula

∞

f(k/δ)sinc(δx − k),

f(x) =

k=−∞

where convergence holds both in the L2(R) sense and uniformly on the real line, and sinc(x) = sin(πxπx). This means that the pair 1δZ and R\[−δ/2,δ/2] forms a Fourier uniqueness pair for the collection C = L2(R). More recently, Radchenko and Viazovska [15] obtained

2010 Mathematics Subject Classiﬁcation. 42A38. Key words and phrases. Fourier transform, uniqueness pairs.

1

a related interpolation formula for Schwartz functions: there are even functions ak ∈ S(R) such that, for any given even function f : R → C that belongs to the Schwartz class S(R), one has the following identity:

∞

f(x) =

k=0

∞

√

f(

k)ak(x) +

k=0

√

f(

k) ak(x), (2)

where the right-hand side converges absolutely. This interpolation result has as immediate consequence: the set Z+ of square roots of non-negative integers is a Fourier uniqueness set for the collection of even1 Schwartz functions.

The two theorems we just presented to motivate our question are, in fact, also instances of the intimate relationship between interpolation and summation formulas. Indeed, as previously mentioned, the Shannon–Whittaker interpolation formula is directly related to the Poisson summation formula

f(m) =

f(n),

m∈Z

n∈Z

and the result by Radchenko and Viazovska is, in fact, a by-product of the development of several summation formulas, having relationship to modular forms and the sphere packing problem (see, for instance, [5, 6, 16]). In fact, the lower bound for the Fourier analysis problem corresponding to the sphere packing problem (see [3]) is directly related to the Poisson summation formula for lattices: if Λ ⊂ Rn is a lattice with fundamental region having volume 1, then

f(λ∗),

f(λ) =

λ∗∈Λ∗

λ∈Λ

where Λ∗ denotes the dual lattice of Λ. Also, in [4], the authors need a summation formula stemming from an Eisenstein series E6, which implies, in particular, that for each radial Schwartz function f : R12 → C, there exists constants cj > 0 such that

cjf( 2j) = − f(0) +

f(0) −

cj f( 2j).

j≥1

j≥1

These concepts seem to be all tethered to the notion of crystaline measures and self-duality, as discussed in [12, 13, 14]. A crystaline measure is essentially a tempered distribution with locally ﬁnite support whose Fourier transform has these same properties. For instance, Poisson summation implies that

δZ = δZ, which shows that the usual delta distribution at the integers is not only a crystaline measure, but also a self-dual one with respect to the Fourier transform. Meyer then discusses

1In [15], the authors also have results for functions which are not even, but we chose to present this version to keep technicalities to a minimum.

other examples of crystaline measures with certain self-duality properties, and, similarly to the strategy used by Radchenko and Viazovska, uses modular forms to construct explicity examples of non-zero crystaline measures µ supported in {±

√k + a,k ∈ Z}, for a ∈ {9,24,72}. It is interesting to point out that Meyer calls out the readers attention to the highly unexplored problem of analyzing when there is a non-zero crystaline measure µ such that both itself and its Fourier transform have support on a given locally ﬁnite set {λk : k ∈ Z}.

Back to Fourier uniqueness pairs, while both the Shannon–Whittaker and Radchenko– Viazovska results provide Fourier uniqueness pairs by means of interpolation identities, and such explicit formulas are not always available and usually depend on special properties of the sets involved, which are somewhat rigid. In the case of the Shannon–Whittaker formula, the set 1δZ plays an special role because of the Poisson summation formula. In the case of the Radchenko–Viazovska interpolation, the set Z+ becomes important due to special properties of certain modular forms involved in their proofs. Perturbing these sets breaks down the proofs of these theorems, and sometimes even the existence of such interpolation formulas. Nevertheless, the Fourier uniqueness pair property is inherently less rigid as a condition than an interpolation formula, which might lead to uniqueness results even in the absence of possible interpolation formulas.

For instance, deﬁne a set Λ ⊂ R to be uniformly separated if there is a number δ = δ(Λ) > 0 such that |λ − λ | > δ whenever λ,λ ∈ Λ and λ = λ . Given an uniformly separated set Λ, we deﬁne its lower density and upper density, respectively, as the numbers

|Λ ∩ [x − R,x + R]| 2R

D−(Λ) = liminf

inf

(3)

x∈R

R→∞

|Λ ∩ [x − R,x + R]| 2R

D+(Λ) = limsup

sup

. (4)

x∈R

R→∞

And when these numbers coincide we call it the density of Λ. As a corollary of the work of Beurling [1] and Kahane [10] about sampling sets, any pair Λ and R\[−2πδ,2πδ] forms uniqueness sets for L2(R) if Λ is uniformly separated and D−(Λ) > δ. This means: any uniformly separated set that is more dense than 1δZ produces a pair of uniqueness sets for L2(R), and one can readily see that this condition, at least in terms of density, is essentially sharp just by analysing subsets of 1δZ.

. Another instance of this density situation has to do with the aforementioned Heisenberg uniqueness pairs. In [9], the authors study pairs of sets (Γ,Λ), where Γ ⊂ R2, which is a ﬁnite disjoint union of smooth curves, and Λ ⊂ R2, which have the following property: whenever a measure µ supported in Γ, which is absolutely continuous with respect to the

arc length measure of Γ, has Fourier transform µ equal to zero on the set Λ, then µ = 0. If a pair (Γ,Λ) has this property, it is called a Heisenberg uniqueness pair. One of the main results of [9] is the following: Let Γ = {(x,y) ∈ R2 : xy = 1} be the hyperbola, and Λα,β be the lattice cross

(αZ × {0}) ∪ ({0} × βZ),

where α and β are positive numbers. Then (Γ,Λαβ) forms a Heisenberg uniqueness pair if and only if αβ ≤ 1. This provides yet another example of the interplay between concentration and uniqueness properties: there is a threshold of concentration one needs to ask in order to maintain the uniqueness property, and increasing the concentration does not aﬀect the uniqueness property.

By comparing the aforementioned interpolation theorems to the considerations in [14] about crystaline measures, one is naturally lead towards the following modiﬁed version of Meyer’s question: if a sequence is “more concentrated than

√

Z”, does it deﬁne a Fourier uniqueness set? For which notion of “more concentrated” could such a result possibly hold? We obtain partial progress towards this problem.

Theorem 1. Let 0 < α,β < 1 and f ∈ S(R). Then

- (A) If f(±log(n + 1))) = 0 and f(±nα) = 0 for every n ∈ N, then f ≡ 0.
- (B) Let (α,β) ∈ A, where


β 1 − α − β

α 1 − α − β

A = (α,β) ∈ [0,1]2: α + β < 1, and either α < 1 −

or β < 1 −

If f(±nα) = 0 and f(±nβ) = 0 for every n ∈ N, then f ≡ 0.

.

Theorem 1 will follow by complex analytic considerations. We will prove that f and f actually have better decay than usual Schwartz functions by using the fact that the sequence of zeros of f and f grows at a certain rate, as well as the information we can obtain about the zeros of their derivatives. Once the decay is obtained, we prove either f or f admits an analytic extension of ﬁnite order, and conclude f is the zero function by invoking the converse of Hadamard’s theorem about growth of zeros of an entire function of ﬁnite order. It will also become clear from the proof that the condition on the exponents (α,β) on part (ii) of theorem 1 is a barrier of our method. We postpone a more detailed discussion about sharpness of our results to the ﬁnal Section of this paper.

Lastly, in order to better compare our results with the ones in [14] and [15] we state the diagonal case of Theorem 1. Corollary 2. Let α < 1 −

√2

2 . Then, if f ∈ S(R) is such that f(±nα) = f(±nα) = 0 for each n ∈ N, it follows that f ≡ 0.

![image 1](<2019-ramos-fourier-uniqueness-pairs-powers_images/imageFile1.png>)

Figure 1. In blue, the closure of the region A, with the line α + β = 1 in black.

- 1.1. Organisation and notation. This article is organised as follows. In Section 2, we mention a couple of basic ideas associating the denseness of zeros of a function and its pointwise decay. In Section 3, we prove the ﬁrst assertion in Theorem 1, and in Section 4 we work upon the ideas in the previous Section to prove the second part of Theorem 1. Finally, in Section 5 we make remarks, mention some corollaries of our methods and state conjectures based on the proofs presented.

Throughout this manuscript, we will use Vinogradov’s modiﬁed notation A B or A = O(B) to denote the existence of an absolute constant C > 0 such that A ≤ C · B. If we allow C to explicitly depend upon a parameter τ, we will write A τ B. In general, C will denote an absolute constant that may change from line to line or from paragraph to paragraph in the argument. Finally, we adopt (1) as our normalisation for the Fourier transform.

2. Preliminaries

- 2.1. Zeros of Schwartz functions and decay. We begin by pointing out a few basic calculus facts.


- (I) First of all, by the mean value theorem, between two zeros of the k-th derivative of a function, there is a zero of the (k+1)-th derivative. This means as long as there is a sequence of zeros of f that converge to inﬁnity, by a simple induction argument, there is a sequence {a(mk)}m∈N such that


- (I.i) 0 < a(mk) < a(mk+1) and

lim

m→+∞

a(mk) = +∞.

- (I.ii) f(k)(a(mk)) = 0, and for every m ∈ Z.
- (I.iii) For all m ∈ N, it holds that [a(mk+1) ,a(mk)] is contained in the interval [am,am+k+1], where {an} are the zeros of the function f. This, in particular, implies


|a(mk+1) − am(k)| ≤ |am+k+1 − am|.

- (II) One can built an analogous sequence with negative zeros of the k-th derivative of f. Of course, the same can be done for [ f](k).


Given a function g ∈ S(R), we will use the following notation

|g(y)||y|k dy.

Ik(g) =

R

The integrals Ik(f) and Ik( f) will play an important role because of the following observation: whenever a point x lies in an interval of the form [am(k+1) ,a(mk)], Fourier inversion implies

|f(k)(x)| = |f(k)(x) − f(a(mk))|

(k)

f(y)(2πiy)k[e2πiyx − e2πiya

=

m ]dy

R

(5)

≤ (2π)k+1Ik+1( f)|x − a(mk)| ≤ (2π)kIk+1( f)|a(mk+1) − a(mk)|.

This means that the rate at which the zeros of the derivatives accumulate at inﬁnity provides extra decay for each derivative itself. We will use this observation iteratively to improve decay bounds on our functions.

- 2.2. Fourier transforms of functions with strong decay. In addition to connecting location of zeros to decay of functions, we need to connect decay of a function to properties of its Fourier transform. The next Lemma is going to be of crucial importance for us throughout the proof.


Lemma 3. Let f ∈ S(R) be such that there exist two constants C > 0, A > 1 for which |f(x)| e−C|x|A, ∀x ∈ R. Then its Fourier transform f can be extended to the whole complex plane as an analytic function with order at most AA−1. That is, for all ε > 0,

A A−1

+ε

| f(z)| ε e|z|

### .

Proof. Let z = ξ + iη ∈ C. Without loss of generality, in what follows we assume that Re(η) < 0. We simply write

e2πiz·xf(x)dx.

f(z) =

R

By the decay property of f, it is easy to see that this integral is well-deﬁned for each z ∈ C, and Morera’s theorem tells us that this extension is, in fact, entire. For the assertion about its order, we have the trivial bound

e−2πηxe−C|x|A dx.

| f(z)| ≤

R

A A−1

+ε

In order to prove that the expression on the right hand side above is ε e|z|

, we split the real line as

R = Aη ∪ Bη ∪ Cη, where

Aη = x ∈ R: x −

2π|η| CA

1/(A−1)

≤ KA

2π|η| CA

1/(A−1)

,

- Bη = x ∈ R: x > (KA + 1)

2π|η| CA

1/(A−1)

,

- Cη = x ∈ R: x < (1 − KA)


2π|η| CA

1/(A−1)

,

and rewrite our integral as e−2πηxe−C|x|A dx =

e−2πηxe−C|x|A dx +

- R


Aη

### =: I1 + I2 + I3.

e−2πηxe−C|x|A dx +

Bη

e−2πηxe−C|x|A dx

Cη

On the interval over which we integrate in I1, −2πηx − C|x|A is at most (an absolute constant depending on A times) |η|

A

A−1. This holds because the center of the interval Aη is the critical point of −2πηx − C|x|A where this function attains its maximum. As we know that |Aη| A |η|

1

A−1, it follows that

A

1

A−1 . (6)

A−1eCA|η|

|I1| |η|

On either the interval deﬁning I2 or on the one deﬁning I3, we see that, for KA,C˜A > 0 large enough depending on A, it holds that

−2πηx − C|x|A ≤ −C˜A|x|A.

Therefore,

+∞

A

e−C A|x|A dx e−C A|η|

A−1 . (7) As (6) dominates (7), we obtain that

|I2| + |I3|

1 A−1

η

A

1

A−1 .

A−1eCA|η|

| f(z)| A |η|

As polynomials factors in |η| decay slower than any exponential e|η| , we ﬁnish the proof of the result, as |η| ≤ |z|.

As an immediate corollary, we obtain the following statement, which will be particularly useful in Section 3.

Corollary 4. Let f ∈ S(R) be such that, for each A > 1, there is a constant CA > 0 such that |f(x)| A e−CA|x|A, ∀x ∈ R. Then its Fourier transform can be extended to the whole complex plane as an analytic function with order at most 1.

3. Proof of (A)

- 3.1. Obtaining decay for f. The ﬁrst idea is to exploit the considerations in Section 2.1 to obtain decay for f. We must, however, obtain decay on the Fourier transform to somehow improve the decay on f we obtain at each step. The following Lemma is the key ingredient to this iteration scheme.


- Lemma 5. Let f ∈ S(R), and assume that f(±log(n + 1)) = 0 and f(±nα) = 0 for every n ∈ N, where β ∈ (0,1). Then, for |x| > log(k + 1) and |ξ| > (2j + 1)α, one has


|f(x)| ≤ k(2π)k((k + 1)!)3Ik( f)e−k|x| = τke−k|x|, | f(ξ)| ≤ (j + 1)!(22−απ)j+1αjIj(f)|ξ|j(α−1

(8)

α ) = Cj|ξ|j(α−1

α ).

Proof. We ﬁrst prove the assertion about f, as it will be also of interest to Lemma 6 in the next section. Let ξ ≥ 0. First we consider n such that ξ ∈ [nα,(n + 1)α]. This implies nα−1 ≤ 21−αξαα−1. By inequality (5), we have

| f(ξ)| ≤ |(n + 1)α − nα|I1(f) ≤ 2παnα−1I1(f) ≤ 22−απαxαα−1I1(f).

(9)

Now, by observation (I.i), as long as ξ > (2j + 1)α, we can conclude there is n ≥ j such that ξ ∈ [a(nj+1) ,a(nj)] ⊂ [nα,(n + j + 1)α]. This means nα−1 ≤ 21−αξαα−1, and therefore

|[ f](j)(ξ)| ≤ (2π)j|a(nj+1) − a(nj)|Ij+1(f) ≤ (2π)j+1|(n + j + 1)α − nα|Ij+1(f) ≤ α(j + 2)(2π)j+1nα−1Ij+1(f) ≤ 21−αα(j + 2)(2π)j+1ξαα−1Ij+1(f).

(10)

By the fundamental theorem of calculus and inequality (10) for j = 1, we have | f(ξ)| = | f((n + 1)α) − f(ξ)|

(n+1)α

[ f] (y)dy

=

(11)

ξ

≤ 3 · 21−α · (2π)2αI2(f)|(n + 1)α − nα|ξαα−1 ≤ 3 · 2 · (22−απ)2α2I2(f)ξ2(α−1

α ).

Inequality (11) exempliﬁes how one can use the concentration properties of the sequence nα in order to obtain decay for f and f. We can iterate these inequalities for higher order derivatives and obtain better decay. For instance, if we apply the same reasoning as in (11) for the ﬁrst derivative, we obtain

|[ f] (ξ)| = |[ f] (a(1)n+1) − [ f] (ξ)|

a(1)n+1 ξ

[ f] (y)dy

=

(12)

≤ 4 · 3 · (22−απ)3α2I3(f)ξ2(α−1

α ).

If we combine this new extra decay for [ f] with the fundamental theorem of calculus, as in

(11), we obtain for ξ > 2 that | f(ξ)| ≤ 4 · 3 · 2 · (22−απ)4α3I3(f)ξ3(α−1

α ). (13) By induction, one can iterate this process and obtain decay of the order of ξj(α−1

α ) for ξ > (2j + 1)α, More precisely,

| f(ξ)| ≤ (j + 1)!(22−απ)j+1αjIj(f)ξj(α−1

α ). (14)

Applying the same analysis for negative ξ yields the desired result for f. In order to obtain the asserted bound for f, we run the same scheme of proof, paying attention to the fact that, if {b(mk)}m∈Z denotes the sequence of zeros of f, in the sense of Section 4.1, then

[b(mk),b(mk+1) ] ⊂ [log(m + 1),log(m + k + 2)], and |b(mk) − b(mk+1) | ≤ log(1 +

k + 1 m + 1

k + 1 m + 1 ≤ (k + 1)2 · e−log(m+k+1).

) ≤

If x ≥ 0 belongs to the interval [b(mk),b(mk+1) ], then the expression above is bounded by (k + 1)2e−x. We leave out the details to the iteration procedure, for they essentially only replicate equations (11)–(14).

We now describe, in a concise way, the iteration scheme to be undertaken. Since f ∈

- S(R), there is a constant D > 0 such that | f(ξ)| ≤ D.


Hence

Ik( f) ≤ D

≤ 2D

|ξ|k+j(α−1

α )dξ

|ξ|kdξ + Cj

|ξ|≤(1+j)α

|ξ|≤(1+j)α

1 k + 1

1 k + j αα−1 + 1

(1 + j)k+j(α−1

α )+1,

(1 + j)α(k+1) + Cj

- as long as we choose j ≥ (k1+2)−αα. Choosing j = j(k) ∼ (k1+2)−αα implies


1 k + 1

(k + 2)α 1 − α

- 1

- 2k + 2


(k + 2)α 1 − α

)−1

)α(k+1) + Cj

Ik( f) ≤ 2D

(1 +

(1 +

1 k2

1 k2

≤ Aα kα(k+1)−1 + Cj

= Aα kα(k+1)−1 + (j + 1)!(22−απ)j+1αjIj(f)

.

(15) We also observe that (8) for k = 1 implies

e−|x||x|j dx f j!. (16) Putting together (15), (16) together with (8), we obtain that

Ij(f) ≤ C(f)

R

|f(x)| ≤ k(2π)k((k + 1)!)3Ik( f)e−k|x| ≤ k(2π)k((k + 1)!)3Aα kα(k+1)−1 + (j + 1)!(2πα)jIj(f)

1 k2

e−k|x| ≤ eO(k logk)−k|x|,

(17) for |x| ≥ log(k + 1), where by O(k log k) we denote an expression that is bounded by Cαk log(k + 1), for some constant depending on α. Equation (17) implies, as k ≤ e|x| − 1

can be chosen arbitrarily, that for each A 1, there is cA > 0 such that |f(x)| f,A e−cA|x|A. (18)

- 3.2. Viewing f as an entire function. The ﬁnal part of the argument uses complex analysis to derive a contradiction. In fact, by Corollary 4, f is an entire function of order

- at most 1. The converse to Hadamard’s factorisation theorem then predicts that the sum of inverses of zeros of f raised to 1 + ε should converge, no matter which value of ε > 0 we choose. But we know that {±nα}n≥0 is contained in the set of zeros of f, therefore


n≥0

1 n(1+ε)α

< +∞.

This is a clear contradiction, as long as α < 1. The contradiction came from assuming that f  ≡ 0, and thus we have proved the ﬁrst part of Theorem 1.

4. Proof of (B)

- 4.1. Obtaining simultaneous decay. The ﬁrst key step of the proof is obtaining enough decay on f in order extend f as an analytic function. One of the key estimate for that will be an iteration scheme of inequality (5), which is the content of the next Lemmas


- Lemma 6. Let f ∈ S(R) and assume that f(±(n)α) = 0 and f(±nβ) = 0 for every n ∈ N, where 0 < α,β < 1. Then, for |x| > (k + 1)α and |ξ| > (j + 1)β, one has


|f(x)| ≤ (k + 1)!(22−απ)k+1αkIk( f)|x|k(α−1

α ) = Ck|x|k(α−1

α )

β−1

β−1

β = Cj|ξ|j

| f(ξ)| ≤ (j + 1)!(22−βπ)j+1βjIj(f)|ξ|j

β .

The proof of this Lemma is identical to that of Lemma 5, and we therefore skip it. Lemma 6 means that one can get very good decay for f(x) for large values of x by sacriﬁcing the potentially big constant

Ck = (k + 1)!(22−απ)k+1αkIk( f) = BkIk( f). The number Bk is easy to estimate by using Stirling’s formula. Indeed Bk ≤ Ce−(k+1)+(k+3/2) log(k+1)+klog(2πα) ≤ cαeklogk+(log(2πα)+1)k+32 logk

(19)

Meanwhile, the number Ik( f), although ﬁnite, might grow at an undesirable rate. Our next step is to control the integral Ik(f).

- Lemma 7. Let f ∈ S(R) and assume that f(±nα) = 0 and f(±nβ) = 0 for every n ∈ N, where 0 < α + β < 1. Then there exists τ = τ(α,β) > 0 such that


Ik(f) f,α,β e−τklogk+O(k).

Proof. From previous considerations, we know that it holds that

(k + 2)β 1 − β

- 1

- 2k + 2


1 k + 1

)β(k+1) + Cj

Ik( f) ≤ 2D

(1 +

(1 +

1 k2

≤ Aβ kβ(k+1)−1 + Cj

,

(k + 2)β 1 − β

)−1

(20)

where | f| ≤ D pointwise. We can now apply the same inequality to Ik(f), and obtain

1 k2

Ik(f) ≤ Aα kα(k+1)−1 + C j

, (21)

where j = j(k) ∼ (k1+2)−αα. Keeping in mind that

Ck = (k + 1)!(22−απ)k+1αkIk( f) = BkIk( f) Cj = (j + 1)!(22−βπ)j+1βjIj(f) = BjIj(f),

one can iterate inequalities (15) and (21). This means

Ik(f) ≤ Aα kα(k+1)−1 + B j(k)

1 k2

I j(k)( f)

≤ Aα kα(k+1)−1 + B j(k)

1 k2

1 ( j(k))2

Aβ j(k)β( j(k)+1)−1 + Cj( j(k))

Bj( j(k)) ( j(k))2

1 k2

Aβ j(k)β( j(k)+1)−1 +

= Aα kα(k+1)−1 + B j(k)

Ij( j(k))(f) . This chain of inequalities amounts to the following inequality

Ik(f) ≤ G(k) + H(k)Ij( j(k))(f), (22) where

- G(k) = Aα,β(kα(k+1)−1 + B j(k)

1 k2

j(k)β( j(k)+1)−1)

- H(k) = Aα,β


B j(k) Bj( j(k)) k2 j(k)2

.

An observation in order is that ρ(k) = j( j(k)) ∼ 1− αα 1− ββ k,

(23)

and

γ = 1− αα 1− ββ < 1 ⇔ α + β < 1. Since we assumed that α + β < 1, it implies γ < 1 and inequality (22) roughly translates

Ik(f) ≤ G(k) + H(k)Iγk(f), (24) and by iterating one gets

m−1

Ik(f) ≤

l=0

G(γlk)

l−1

H(γsk) + H(γm−1k)···H(γk)H(k)Iγmk(f). (25)

s=0

In order for our bounds to behave nicely, we assume at this point that Aα,β = 1 in (23), which is possible simply by dividing f by Aα,β at the cost of an extra constant depending only on α and β on the desired bounds. We estimate G using (19)

α

G(k) α eα(k+1) logk + e(1+β)

1−αk log k+O(k) ≤ eλklogk+E(k),

where

α 1 − α

,

λ = (1 + β)

- and E(k) = O(k). Now we estimate H in the same fashion

H(k) =

B j(k) Bj( j(k)) k2 j(k)2 α e(

α

1−α)klogk+O(k)eγklogk+O(k) ≤ eδklogk+E(k),

where

δ =

α 1 − α

+ γ =

α (1 − α)(1 − β)

,

- and F(k) = O(k). This means l−1


H(γs−1k) ≤ e ls−=11[δγsklogγsk+E(γsk)]

s=0

1−γl 1−γ k log k+E0(k)

≤ eδ

and therefore

m−1

l−1

H(γsk) + H(γm−1k)···H(γk)H(k)Iγmk(f)

G(γlk)

Ik(f) ≤

s=0

l=0

m−1

(26)

1−γm

1−γl

eλγlklogk+F(γlk)eδ

1−γ klogk+E0(k) + eδ

1−γ klogk+E0(k)Iγmk(f)

≤

l=0

1

1

≤ me(λ+δ)

1−γklogk+F0(k) + eδ

1−γklogk+E0(k)Iγmk(f).

Now, if we choose m ∼ −logγ k, and for simplicity assume I1(f) = 1, we have 2 Ik(f) ≤ e

λ+δ

1−γklogk+O(k).

The proof of the Lemma is then complete by taking τ = 1λ−+γδ. This choice is going to be important for us later on.

One direct consequence of Lemma 7 is that we obtain an explicit decay for f of the form | f(ξ)| ≤ e(1+

β−1 β

λ+δ

1−γ)klogk+O(k)|ξ|k

(27)

1−γ)klogk+ β−β1 klog|ξ|+O(k),

λ+δ

= e(1+

whenever (1 + 2k)β ≤ |ξ|. Now, if one chooses k ∼ |ξ|1 , the exponent in (27) becomes 1

β − 1 β

λ + δ 1 − γ

log |ξ| |ξ|1 + O(|ξ|1 ). As long as

log |ξ| +

1 +

1 − β β

1

λ + δ 1 − γ

, or equivalently

1 +

<

λ + δ 1 − γ

β 1 − β

> 1 +

1 − α − β + (2 − β2)α 1 − α − β

β 1 − β

(28)

=

1 + α − β(1 + αβ) 1 − α − β ·

β 1 − β

=

,

we can conclude that, for some 0 < θ < 1, | f(ξ)| f e−(1−θ)|ξ|

1

### , (29)

2Up to this point, we have neglected the error terms (E, F etc), but their sums with argument γlk are clearly still going to be O(k).

where θ > 0 is small, and (28) is obviously true for some admissible large , i.e, some number such that (1 + 2k)β < |ξ| ∼ k . We next connect this exponential decay we have achieved to the magnitude of Ik(f).

- Lemma 8. Let f ∈ S(R) such that


1

|f(x)| ≤ Cfe−(1−θ)|x|

δ . (30)

Then it holds that Ik(f) f,δ,θ Γ(δ(k + 1)). Proof. By (30), it follows that

1

e−(1−θ)|x|

δ |x|kdx.

Ik(f)

R

By the change variables x (1− tεθ)ε, we have

∞

2ε (1 − θ)k(ε+1)

2ε (1 − θ)k(ε+1)

1

e−|x|

e−ttε(k+1)−1dt =

ε |x|kdx =

Γ(ε(k + 1)), which directly implies the assertion of the Lemma.

R

0

- 4.2. Optimizing the exponent. It is important to point out that up to this point the only imposed condition on the pair (α,β) is that α + β < 1. This means that whenever f is a Schwartz function such that f(±nα) = 0 and f(±nβ) = 0, then inequality (29) holds for some small θ and ε satisfying (28). We now describe an iteration procedure to improve the decay obtained in the previous subsection, at the cost of extra constraints on the pair (α,β).


Let ( f) denote the inﬁmum of all > 0 obtained previously, such that (29) holds. That is, we let

β(1 + 1λ−+γδ) 1 − β

( f) =

.

Deﬁne (f) in the same fashion, exchanging the roles of α and β. The process that follows is a way to progressively decrease the magnitude of either (f) or ( f).

It follows from Lemma 8 that | f(x)| ≤ e(1+ (f))klogk+

β−1

β klog|ξ|+O(k). Deﬁne then the sequences (an,bn)n∈Z of exponents associated to f, f to be

b0 = ( f),a0 = (f), bn = (1 + an)

β 1 − β

α 1 − α

,an+1 = (1 + bn)

.

(31)

### Repeating the argument undertaken in Section 4.1, it holds that, for any ε > 0,

1

an+ε ,

|f(x)| f,ε e−Cn|x|

1

| f(ξ)| f,ε e−C˜n|ξ|

bn+ε ,

as long as the conditions bn > β and an > α are met for all n ≥ 0. We let, respectively to the deﬁnitions above,

- θ1(α,β) =

α (1 − α)(1 − β)

,

- θ2(α,β) =


β (1 − α)(1 − β)

.

A computation shows that we actually have an+1 = θ1 + γan, bn+1 = θ2 + γbn. (32)

As γ < 1, we see that both (an)n≥0 and (bn)n≥0 are convergent sequences, with limit L1(α,β) = lim

α 1 − α − β

,

an =

n→∞

β 1 − α − β

L2(α,β) = lim

bn =

.

n→∞

This implies that, for all ε > 0,

1

L1(α,β)+ε ,

|f(x)| f,ε e−C|x|

1

| f(ξ)| f,ε e−C˜|ξ|

L2(α,β)+ε .

(33)

Notice that, if (f) > L1(α,β) and ( f) > L2(α,β), then both sequences an,bn are decreasing, and (33) is the best exponential decay we could expect for f, f. Notice that the condition (28) gives us that ( f) > L2(α,β) as desired, which proves that the iteration scheme presented achieves, in fact, a better exponential decay for f, f than the original one.

Remark 1. If we let Sµν(R) denote the Gelfand-Shilov space of Schwartz functions ϕ such that

|ϕ(x)eh|x|1/ν|, sup ξ∈R

| ϕ(ξ)ek|ξ|1/ν| < +∞

sup

x∈R

for some k,h > 0, then we have actually proved that f ∈ S˜µν(R) := ∪ν0>ν,µ0>µSµν00(R), where ν = L1(α,β) and µ = L2(α,β). These function spaces are originally deﬁned through speciﬁc decay properties of the Schwartz seminorms ϕ  → xα∂βϕ ∞, and the equivalence to the higher-order decay statement above is proved through the seminorm decay. This procedure is in many ways analogous to the one undertaken here to obtain that f ∈ Sµν(R), and the relationship between our proof and these function spaces was recently brought to our attention. For more information on Gelfand-Shilov spaces, see, for instance, [2, 7] and the references therein.

- 4.3. Analytic continuation. We wish to derive a contradiction from the fact that f  ≡ 0. In order to do it, we prove that either f or f can be analytically extended with control on its order depending only on min{L1(α,β),L2(α,β)}. Without loss of generality, let α ≤ β. Therefore, L1(α,β) < L2(α,β) and, in case β ≤ 1−2α, then L1(α,β) < 1, and this contains the region A described in the introduction. We then appeal to Lemma 3, which enables us to conclude that f is extendable as an analytic function of order at most

1 1 − L1(α,β)

. By the converse to Hadamard’s factorisation theorem, we must have

n≥0

n−

β+ε

1−L1(α,β) < +∞,

for each ε > 0. Thus, we reach an immediate contradiction if β < 1 − L1(α,β).

As we supposed initially that α ≤ β, elementary calculations lead to the following observation: if (α,β) ∈ A, then each Schwartz function f such that f(±nα) = f(±nβ) = 0, ∀n ∈ N, then f ≡ 0. This ﬁnishes the proof of Theorem 1.

5. Remarks and complements

- 5.1. Spacing between zeros and bounds for f. In Sections 2, 3 and 4, we have seen how to obtain decay for a Schwartz function given we have information on the location of the zeros of its derivatives. A main feature, in particular, of the proof in Section 4 was that the sequence of zeros of the derivative f(k) satisﬁes a(nk) ∈ [nα,(n + k + 1)α], which enables us to bound


|a(nk+1) − a(nk)| ≤ Cα(k + 1)|a(nk+1) |−1−α

α , (34) if n > k + 1. A careful look into the proofs undertaken above relates the exponent of k on the left hand side above to the iteration scheme for optimizing the exponent performed in Section 4.2. Indeed, if we were able to improve the factor on the right hand side of (34)

from (k + 1) to (k + 1)ω,ω < 1, then the sequences an,bn above would take the form

b0 = ( f),a0 = (f), bn = (ω + an)

β 1 − β

α 1 − α

,an+1 = (ω + bn)

.

(35)

A simple computation shows that the limit of this new sequences is strictly smaller than the one we obtained in Section 4.2. This yields, as a consequence, an improvement on the set A of admissible exponents for Theorem 1, described in the introduction. For instance, if (35) holds, then

ωα(1 + (ω − 1)β) 1 − α − β

,

lim

an =

n→∞

ωβ(1 + (ω − 1)α) 1 − α − β

lim

bn =

.

n→∞

If α ≤ β and ω satisﬁes the equation

ω(1 + (ω − 1)β) = 1 − α − β, then the argument in Section 4.3 produces a contradiction whenever α+β < 1, which would be the biggest regime in which one expects a version of our main theorem to hold. This raises the question whether the decay in (34) can be improved. Unfortunately, the answer to this question is negative. Indeed, let a(0)n = nα as before. Consider {n ∈ N: nα ∈ [2j,2j+1)} = [nj,nj+1), and deﬁne the sequence {an(k)}, for n ∈ [nj,nj+1 − k) and j+11 2k/α < k < 2j/α, satisfying

a(nkj−1) < a(nkj) < (nj + 1)α, a(nk+1−1) >a(nk) > max(a(nk+1−1) − 2−10k(1−α)j/α,a(nk−1)).

(36) This satisﬁes, in particular, the growth requirements on the sequence from Section 2.1. For k > 2j/α,n ∈ [nj,nj+1), we let a(nk) be chosen arbitrarily satisfying (I.i) in the same section. The deﬁnition implies, in particular, that a(nk)

j+1 > a(0)n

j+k+1 − ≤k 2−10 (1−α)j/α >

(nj + k + 1)α − cα2−10(1−α)j/α. Therefore, |an(k)

j+1−a(nkj)| ≥ (nj +k+1)α−(nj +1)α−2−10(1−α)j/α ≥ αk·(nj +k+1)α−1−2−10(1−α)j/α.

As nj > 2j/α, the right hand side is controlled from below by a constand depending on α times k2−

(1−α)j

### α . As nj+1 ≤ 21/α2j/α, estimate (34) is sharp for k < 2j/α. Replicating the

same argument for all j > 1 and concatenating the sequences together implies the desired sharpness for all k ≥ 1.

Nevertheless, a question still remaining is whether a decay better than (34) can hold on average. We have used this estimate on the gap between zeros of the k−th derivative to obtain decay for f(k) pointwise. It could happen, though, that one obtains better decay averaging over large intervals, rather than doing pointwise evaluation. This intuitive thought is partially backed up by the fact that, for n ∈ [nj,nj+1 − k), the average gap

|a(nk+1) − a(nk)| is of the same order of 2−(1−α)j/α, as long as n − k ∼ 2j/α. We show here that this phenomenom does not happen in case the sequence of zeros {a(nk)} has structure similar to the counterexample above. Considering the bound (5), we wish to bound the average of f(k) over the interval [2j,2j+1). A computation shows that

 . (37)

 

nj+1

2j+1

- 1

- 2j


|a(l+1k) − al(k)|2

(2π)kIk+1( f)

|f(k)(x)|dx

−

2j

l=nj−k

Notice that each of the |a(l+1k) − a(lk)| terms is bounded by Cα · (k + 1)2−(1−α)j/α, for some absolute Cα > 0. Our problem is equivalent to the following: we have a sequence of N non-negative real numbers {cj}Nj=1 such that Nj=1 cj = A and 0 < cj ≤ B. What is the maximum of

N

c2j, (38)

j=1

and when is it attained? By ﬁxing all but 2 variables, it is easy to see that the maximum of (38) happens when the cj are all either B or 0. As

N

cj = A,

j=1

it holds that the optimal value happens when there are ∼ A/B diﬀerent j s for which cj = B, and then the maximal value of (38) is ∼ B ·A. Applying this analysis to (37) yields that

2j+1

|f(k)(x)|dx (2π)kIk+1( f)Cα · (k + 1)2−(1−α)j/α, (39)

−

2j

as long as k ≤ 2j/α, which is essentially the same as we obtained before. In order to prove that there is a sequence with the behaviour described above, we deﬁne a sequence {an(k)} of the following form: on the interval [nj,nj + k + 1), we deﬁne our sequence exactly as in (36); we then do the same construction as in (36) on [nj + k + 1,nj + 2(k + 1)), but with nj + k + 1 in place of nj. Similarly, we do it for each of the ∼ 2j/α/k intervals of the form

[nj + (k+1),nj +( +1)(k+1)). The sequence obtained that way will nearly maximise the square sums, in the sense that there are going to be ∼ 2j/α/k terms close to ∼ k2−(1−α)j/α, and the remaining ones will be close to zero. A computation shows that the bound (39) holds in the same way for this sequence.

These examples indicate that not much more can be improved in our methods in terms of the range of exponents A above without additional information about the location of the sequences of zeros {a(nk)}k≥0,n∈Z.

## 5.2. Generalisations of Theorem 1.

- 5.2.1. Conditions on the sets of zeros. One might wonder if the sequences in Theorem 1 being composed of powers and logarithms of integers plays an important role in our proofs, but it does not. The spacing of the zeros comes into the proofs in order to produce the ﬁrst decay estimates, and for that the important piece of information that plays a role is the bound (34), which comes from the distance between two consecutive zeros of the derivatives of f, and the growth condition of the sequence of zeros of f and f. In other


words, if f(±an) = f(±bn) = 0, then it is suﬃcient to have two positive numbers η and ω such that

η · ω > 1,

|ak+n − an| ≤ Ck|ak+n|−η, |bk+n − bn| ≤ Ck|bk+n|−ω,

(40)

in order to apply the same procedure as in Lemma 7 and obtain the initial degree of exponential decay. Now, in order to optimise the exponent as in subsection 4.2, we need

1

|an| ≤ Cn

1+η , |bn| ≤ Cn

(41)

1

1+ω ,

where (α,β) = (1+1η, 1+1ω) belong to the region A in Theorem 1. This means our results are stable under small perturbations of the sequences of zeros. In fact one can even delete

a large number of zeros and still get the same results. One should compare, for instance, to the interpolation result (2) mentioned in the introduction, whose proof, to the best of our knowledge, is rigid to the fact that the interpolation nodes are the square roots of the natural numbers, and the construction of the interpolation basis itself shows that one cannot remove any term from the sequence without breaking down the ﬁnal result.

- 5.2.2. Conditions on the functions. Another very natural question that arises from the results is if it is completely necessary to assume the functions involved are in the Schwartz class. Perhaps the result could hold with more relaxed conditions, but our proof rely


heavily on ﬁniteness of Ik(f) and Ik( f) for every k ≥ 0, and this implies, although not in a straightforward manner, that f is a Schwartz function. For the sake of completeness, we outline the proof of this fact.

First of all, by Fourier inversion and the Riemann-Lebesgue lemma, ﬁniteness of Ik( f) implies that f is of C∞ class with all derivatives bounded and converging to zero at inﬁnity. Now, we only need to prove polynomial decay of all the derivatives of f, and in order for that to be true we start by proving that f has polynomial decay. For a ﬁxed N > 0, we deﬁne the set

Ej,N = Ej = {x ∈ [2j,2j+1) : |x|Nf(x) > 1}. It follows from Chebychev‘s inequality that

2j+1

|f(x)||x|N dx ≤ 2−jNI2N(f),

|Ej| ≤

2j

This means there is y ∈ Ej and x ∈ [2j,2j+1)\Ej such that |x − y| ≤ 2−jNI2N(f). By the aforementioned fact that f is bounded, we have

|f(y)| ≤ |f(x) − f(y)| + |f(x)| ≤ Cf|x − y| + |x|−N N,f |y|−N.

Therefore f has polynomial decay of any order. Now, in order to propagate this decay to every derivative, we combine the fact that f is a bounded function and |f(x)| |x|−N with a Taylor series remainder argument in order to obtain |f (x)| |x|−N/2. This implies polynomial decay for f . Iterating this argument with higher order derivatives implies that f is of Schwartz class.

- 5.2.3. Radial versions for higher dimensions. A very natural generalisation one could think of is that of asking the same question for higher dimensional functions. Of course the notion of density would have to be redeﬁned for general functions of several variables since one can easily construct functions that vanish along uncountable sets, such as manifolds, but if one restricts its attention to the case of radial functions similar questions will naturally


arise. In fact, if we consider Srad(Rd) to be the class of radial Schwartz class on Rd, in [6] the authors study interpolation formulas in this radial setting, and dimensional diﬀerences come into the fold. This motivates the question: for which exponents (α,β) does the pair ({nα}n∈Z+,{nβ}n∈Z+) forms a Fourier uniqueness pair for Srad(Rd)? Turns out in our setting the same ideas already introduced here apply to this problem, and we outline the steps here.

Step 1: By replacing f(k) by the k-th order radial derivative ∂rkf, one can run the same game of intermediate zeros as in section 2.1 to get high order polynomial decay with loss on the constants involved in terms of Ik,d(f) and Ik,d( f), where

|g(x)||x|kdx.

Ik,d(g) =

Rd

One can also obtain analogues of Lemmas 7 and 8. More precisely, one gets the analogue of inequality (22) paying a dimensional constant, which means one can directly replicate

- Lemma 7 to obtain

| f(|ξ|)| f e−(1−θ)|ξ|

1

. (42)

- Lemma 8 for the d-dimensional setting will read as the estimate Ik,d(f) f,δ,θ Γ(δ(k + d)),


which can be applied in the same fashion in the rest of the iteration procedures to reach the same order of decay.

Step 2: Hadamard’s theorem on distribution of zeros of entire functions fails to work in the same fashion for several complex variable functions, so one cannot do the simply extend the radial functions involved to Cd. The alternative to this is observe that the Fourier transform of a radial function can be seen as a Hankel transform. We consider the following Hankel transform

∞

Hν(f)(ρ) :=

f(r)Aν(rρ)dr,

0

where Aν(s) = (2πs)νJν(2πs), and Jν is a Bessel function of ﬁrst kind. In this setting, if we consider f(r) = f(r)rd−1, which has the same zeros as f, then

f(ξ) = (2π)d2

### ( f)(|ξ|). By observing that the function Ad−2

Hd−2

2

can be extended as a real entire function satisfying the estimate

2

(ξ + iη)| d e2π|η|, it is clear that an analogue version of Lemma 3 holds for the Hankel transform.

|Ad−2

2

Step 3: In order to ﬁnish, we now combine the analytic extension property of the Hankel transform and its connections with the Fourier transform mention in Step 2, together with the decay mentioned in Step 1, one can invoke Hadamard’s theorem in the same fashion as before and conclude f has to be the zero function, as long as (α,β) ∈ A, where A is the set introduced in Theorem 1.

5.3. Open problems. Comparing Theorem 1 and (2), we see that there is a gap in area between the two pictures. The (α,β) = (1/2,1/2) point considered by Radchenko and Viazovska possesses a ‘quasi-uniqueness’ property, in the sense that there is essentially one real function who vanishes on the nodes ±

√n and belongs to the Schwartz class. We believe that the question of denseness of the sequences (±nα,±nβ) plays an important role in removing this rigidity condition, which is reﬂected on the following conjecture.

Conjecture. Let α,β ∈ (0,1) be such that α + β < 1. If f ∈ S(R) satisﬁes that f(±nα) = f(±nβ) = 0 for all n ≥ 0, then it holds that f ≡ 0.

Of course, Theorem 1 is partial progress towards this conjecture, but our techniques do not seem to be immediately susceptible to being generalised in order to conclude the full conjecture. On the other hand, another interesting problem that, as far as we know, is still largely unexplored is that of sequences that grow roughly as a power of an integer, but do not posses as strong tightness properties as in Section 5.2.1 above.

- Question 2. Let α,β ∈ (0,1) be such that α + β < 1. Under which conditions does it hold that, for two sequences (±cn,±dn)n≥0 such that

lim

n→∞

dn nβ

, lim

n→∞

cn nα

< +∞

and a function f ∈ S(R) such that f(±cn) = f(±dn) = 0,∀n ≥ 0, then f ≡ 0?

The ﬁrst natural guess is that a result of that kind should hold in the same range as Conjecture 5.3, but it would already be interesting if one could prove that the uniqueness property holds under the assumptions in Theorem 1. Finally, our last question concerns what happens on the critical case of Theorem 1.

- Question 3. Let α,β ∈ (0,1) be such that α + β = 1. Suppose f ∈ S(R) is a real function such that f(±anα) = f(±bnβ) = 0 holds for each natural number n ≥ 0. Under which conditions on a,b > 0 does it holds that f ≡ 0?


This type of questions remains heavily unexplored even in the α = β = 12 case, where we believe that a combination of our present techniques with those of [15] may be useful.

Acknowledgments

We would like to especially thank Felipe Gon¸calves and Danylo Radchenko for discussing these problems and ideas about Fourier uniqueness pairs with us. We would also like to thank Christoph Thiele for helpful suggestions during the development of this manuscript. We also thank Emanuel Carneiro and Lucas Oliveira for helpful comments and remarks. Finally, J.P.G.R. acknowledges ﬁnancial support from the Deutscher Akademischer Austauschdienst (DAAD).

### References

- [1] A. Beurling, Balayage of Fourier-Stieltjes transforms, Collected Works of Arne Beurling, vol. 2, Harmonic Analysis, Birkha¨user, Boston, 1989.
- [2] J. Chung, S.-Y. Chung and D. Kim, Characterizations of the Gelfand-Shilov spaces via Fourier transforms, Proc. Amer. Math. Soc. 124 (1996), no. 7, 2101–2108.
- [3] H. Cohn and N. Elkies, New upper bounds on sphere packings I, Ann. of Math. 157 (2003), no. 2, 689–714.
- [4] H. Cohn and F. Gon¸calves, An optimal uncertainty principle in twelve dimensions via modular forms, Invent. Math. 217 (2019), no. 3, 799–831.
- [5] H. Cohn, A. Kumar, S. D. Miller, D. Radchenko and M. Viazovska, The sphere packing problem in dimension 24, Ann. of Math. (2) 185 (2017), no. 3, 1017–1033.
- [6] H. Cohn, A. Kumar, S. D. Miller, D. Radchenko and M. Viazovska, Universal optimality of the E8 and Leech lattices and interpolation formulas, preprint at arXiv:1902.05438v2.
- [7] I.M. Gel’fand and G. Silov,ˇ Generalized functions. Vol. 2, Spaces of fundamental and generalized functions, Academic Press, New York-London, 1968.
- [8] S. Ghosh and R.K Srivastava, Heisenberg Uniqueness pairs for the Fourier transform on the Heisenberg group, preprint at arXiv:1810.06390v4.
- [9] H. Hedenmalm and A. Montes-Rodr´ıguez, Heisenberg uniqueness pairs and the Klein–Gordon equation, Ann. of Math. (2) 173 (2011), no. 3, 1507-1527.
- [10] J. Kahane, Sur les fonctions moyenne-p´eriodiques borne´es (French), Ann. Inst. Fourier, Grenoble 7

(1957), 293–314.

- [11] N. Lev, Uniqueness theorems for Fourier transforms, Bull. Sci. Math. 135 (2011), no. 2, 134–140.
- [12] N. Lev and A. Olevskii, Measures with uniformly discrete support and spectrum, C. R. Math. Acad. Sci. Paris 351 (2013), no. 15-16, 613-617.
- [13] N. Lev and A. Olevskii, Quasicrystal and Poisson’s summation formula, Invent. Math. 200 (2015), no. 2, 585-606.
- [14] Y. Meyer, Measures with locally ﬁnite support and spectrum, Rev. Mat. Iberoam. 33 (2017), no. 3, 1025–1036.
- [15] D. Radchenko and M. Viazovska, Fourier interpolation on the real line, Publ. Math. Inst. Hautes Etudes´ Sci. 129 (2019), 51–81.
- [16] M. Viazovska, The sphere packing problem in dimension 8, Ann. of Math. (2) 185 (2017), no. 3, 991–1015.


Joao˜ Pedro Ramos, Mathematical Institute, Universitat¨ Bonn, Endenicher Allee 60, 53115, Bonn, Germany.

E-mail address: jpgramos@math.uni-bonn.de

Mateus Sousa, Ludwig-Maximilans Universitat¨ Munchen,¨ Theresienstr. 39, 80333 Munchen,¨ Germany.

E-mail address: sousa@math.lmu.de

