arXiv:1408.2568v1[math.CO]11Aug2014

ROTH’S THEOREM FOR FOUR VARIABLES AND ADDITIVE STRUCTURES IN SUMS OF SPARSE SETS

TOMASZ SCHOEN AND OLOF SISASK

Abstract. We show that if A ⊆ {1,...,N} does not contain any solutions to the equation x + y + z = 3w with the variables not all equal, then

N exp c(log N)1/7

|A|

,

![image 1](<2014-schoen-roth-theorem-four-variables_images/imageFile1.png>)

where c > 0 is some absolute constant. In view of Behrend’s construction, this bound is of the right shape: the exponent 1/7 cannot be replaced by any constant larger than 1/2.

We also establish a related result, which says that sumsets A + A + A contain long

arithmetic progressions if A ⊆ {1,...,N}, or high-dimensional subspaces if A ⊆ Fnq , even if A has density of the shape above.

1. Introduction

This paper is concerned with two types of problems in additive combinatorics, namely solving linear equations in subsets of abelian groups and ﬁnding additive structures in sumsets, with a focus on being able to deal with relatively sparse sets. We discuss these in turn, focusing on the historically most important case of sets of integers.

Roth-type results. Roth’s famous theorem on arithmetic progressions says that if a set A ⊆ [N] := {1, . . ., N} does not contain any non-trivial three-term arithmetic progressions, that is solutions to the equation x + z = 2y with x, y, z not equal, then |A| = o(N). In fact:

- Theorem 1.1 (Roth’s theorem [20]). Let r3(N) denote the largest size of a subset of [N] with no non-trivial three-term progressions. Then, for N large enough,


r3(N) = O

N log log N

![image 2](<2014-schoen-roth-theorem-four-variables_images/imageFile2.png>)

.

This theorem has been central to additive combinatorics, and improving the above bound has been the object of much research and has led to a wealth of interesting techniques being developed; see for example [28, 18, 5, 6, 24, 25, 3], to which we also refer for more history on the problem. It is not yet known, however, whether r3(N) = O(N/ logN); the current best upper bounds, due to Sanders [25] and Bloom [3], give

r3(N)

N (log N)1−o(1)

.

![image 3](<2014-schoen-roth-theorem-four-variables_images/imageFile3.png>)

![image 4](<2014-schoen-roth-theorem-four-variables_images/imageFile4.png>)

2010 Mathematics Subject Classiﬁcation. 11B30; 11B25.

1

By contrast, the best lower bound on r3(N), coming from constructions of large subsets of [N] with no non-trivial progressions, is of the form

N

r3(N)

![image 5](<2014-schoen-roth-theorem-four-variables_images/imageFile5.png>)

exp O(logN)1/2 and is due to Behrend [2] (but see also [12, 17]). Now, most proofs of Roth’s theorem easily extend to provide similar upper bounds for any translation invariant equation

c1x1 + · · · + ckxk = 0 where k 3, cj ∈ Z \ {0}, and c1 + · · · + ck = 01, (1.1) and Behrend’s argument extends directly to any such equation with one negative coeﬃcient and the rest positive, that is of the form a1x1 + · · · + alxl = by with the aj positive integers summing to b. Furthermore, a somewhat folklore philosophy was that whatever techniques worked for additive combinatorial problems involving three variables would also work for those involving four or more, and vice versa, with the bounds being similar. The work [26] of Sanders led to this being questioned in the context of sumsets, however, and the ﬁrst-named author and Shkredov [27] subsequently showed that much stronger bounds than those given for r3(N) above hold for equations in six or more variables. A representative example:

- Theorem 1.2 ([27]). Suppose A ⊆ [N] does not contain any solutions to x1+· · ·+x5 = 5y in distinct integers. Then

|A|

N exp Ω(log N)1/7

![image 6](<2014-schoen-roth-theorem-four-variables_images/imageFile6.png>)

.

Here one has an almost matching lower bound: Behrend’s construction gives sets A of size at least exp − O(log N)1/2 N that do not contain any solutions to this equation.

Around the same time, Bloom [4] established improved bounds for four and ﬁve variable equations, inspired by Sanders’s technique from [25]:

- Theorem 1.3 ([4]). Suppose A ⊆ [N] does not contain any non-trivial2 solutions to the equation in (1.1). Then

|A|

N (log N)k−2−oc(1).

![image 7](<2014-schoen-roth-theorem-four-variables_images/imageFile7.png>)

There thus remained an almost exponential gap between the lower and upper bounds for four and ﬁve variable equations. In this paper we show that one indeed has Behrendshape upper bounds for these. For example:

- Theorem 1.4. Suppose A ⊆ [N] does not contain any non-trivial solutions to the equation x + y + z = 3w. Then


N exp Ω(log N)1/7

|A|

.

![image 8](<2014-schoen-roth-theorem-four-variables_images/imageFile8.png>)

![image 9](<2014-schoen-roth-theorem-four-variables_images/imageFile9.png>)

1This is the translation invariance property. 2A solution (x1,...,xk) to (1.1) is called trivial if one can partition the index set [k] into parts on

which the variables xj are constant and the coeﬃcients cj sum to 0. For example (x,... ,x).

In the much-studied ﬁnite ﬁeld setting, where [N] is replaced by a vector space over a ﬁnite ﬁeld, we establish the following slightly stronger result.

- Theorem 1.5. Let q be a prime power and let A ⊆ Fnq be a set of size α qn. If A does not contain any non-trivial solutions to x + y + z = 3w, then


α exp −Ω n1/5 .

By contrast, the best bound known for three-term progressions in this setting comes from the intricate work of Bateman and Katz [1], who showed that if A ⊆ Fn3 is free of non-trivial three-term progressions then |A| 3n/n1+ǫ, where ǫ is some strictly positive constant.

Before we move on, let us make a quick remark about our arguments. These are somewhat diﬀerent to those of [27], which used the bounds of Sanders [26] for a result known as the Bogolyubov–Ruzsa lemma. However, the proof of this lemma used in turn an almost-periodicity result of Croot and the second-named author [10], and this will together with an insight from [26] be of key importance in our proofs. This is actually part of the motivation behind this paper: while one aim is to prove strong bounds for

- as close a problem as possible to Roth’s theorem, another is to attempt to illustrate the natural limitations of the ideas of [10, 26]. We thus give two diﬀerent proofs of Theorem 1.5 that demonstrate diﬀerent aspects of the results; see Section 3.


Structures in sumsets. Another big direction of additive combinatorics is to study the structure of sumsets A + B = {a + b : a ∈ A, b ∈ B} for various types of sets A and B in an abelian group. Here we focus on the case of three-fold sumsets 3A := A+A+A where A is a large subset of [N] or a ﬁnite abelian group G, as was ﬁrst tackled by Freiman, Halberstam and Ruzsa [13]. Suppose A ⊆ [N] has size at least αN, α > 0. The following lower bounds for the length of an arithmetic progression in 3A are known3.

Density range Length of AP in 3A α (log N)−1/3+o(1) Ncα3 F–H–R [13] α (log N)−1/2+o(1) Ncα2+o(1) Green [14] α (log N)−1/2+o(1) Ncα Sanders [22]

- α (log N)−1+o(1) Ncα1+o(1) Henriot [19]
- α (log N)−2+o(1) exp (α1/2+o(1) log N)1/2 Henriot [19]


Henriot [19] gives a useful and clear summary of the history of the problem, and we refer there for more information. Let us also mention that Henriot’s results are actually more powerful in the asymmetric case of sumsets A + B + C: in this setup [19] allows B and C to be much sparser, namely of densities around exp (−O(log N)c), as long as the density of A is more-or-less as above.

Here we prove the following, which is non-trivial in the range α exp −c(log N)1/5 .

![image 10](<2014-schoen-roth-theorem-four-variables_images/imageFile10.png>)

3Here and throughout the paper we let c and C denote unspeciﬁed positive absolute constants whose values need not be the same at diﬀerent occurrences.

- Theorem 1.6. Let A ⊆ [N] have size at least αN. Then 3A contains an arithmetic progression of length at least


α exp

c log N log3(2/α)

![image 11](<2014-schoen-roth-theorem-four-variables_images/imageFile11.png>)

1/2

.

The length of the progression here is of course much smaller than previous results for large densities, being on par with what is known for just A + A in this case, but when α gets small enough this theorem applies whereas those above do not. Let us mention, however, that there is a combinatorial argument due to Croot, Ruzsa and the ﬁrstnamed author [8] that guarantees arithmetic progressions in 2A := A + A of length around c log N/ log(2/α), which certainly extends the non-trivial density range further albeit with fairly short progressions. We thus know of quite diﬀerent behaviours for diﬀerent densities, but a lack of examples pervades. The best example we know of comes from [13]: there it is shown that, for any α < c, there is a set A ⊆ [N] of size at least αN for which 3A does not contain an arithmetic progression of length

N2/log(1/α). (1.2)

- Theorem 1.6 thus gives an answer of the right shape exp((log N)c) for α = exp(−(log N)c), but with a gap in the exponent on the log N compared to (1.2).

These questions are also studied for subsets of vector spaces Fnq over ﬁnite ﬁelds Fq, where q is considered ﬁxed, but in this setting one generally looks at the dimensions of (aﬃne) subspaces found in sumsets rather than arithmetic progressions, for obvious reasons. See for example [15, 22, 23, 7] for more background. From the perspective of the present paper it is illuminating to consider what is known in this setting for 2A, 3A and 4A, for which the best bounds known for large densities are all due to Sanders. For 2A, it is shown in [23] that 2A contains an aﬃne subspace of dimension at least cαn for α C/n. Sumsets 3A are known [22] to contain aﬃne subspaces of dimension at least n − C/α, and sumsets 4A are known [26] to contain aﬃne subspaces of dimension at least n − C log4(2/α). Here we prove a result somewhat intermediate between the latter two:

- Theorem 1.7. Let A ⊆ Fn5 be a set of size at least α · 5n. Then 3A contains an aﬃne subspace of dimension at least cn/ log(2/α)3 − log(1/α).


We actually show somewhat more, namely that these three-fold sumsets contain lots of translates of the respective arithmetic progression or subspace; see Section 8 for further statements, and see also Section 9 for some further comparisons of 2A, 3A and 4A.

The rest of this paper is structured as follows. In the next section we set up some notation and describe some preliminaries on density increments, convolutions and almostperiodicity. In Section 3 we prove Theorem 1.5; indeed, we give two proofs as already mentioned. We then proceed to a proof of the general case, starting with a review of Bohr sets in Section 4 and the development of the appropriate almost-periodicity results in Section 5, and wrapping up with the density increment and iterative arguments in Sections 6 and 7. We then turn to structures in 3A in Section 8, and conclude with some remarks in Section 9.

2. Notation and preliminaries

- If A is a subset of a ﬁnite set X, we refer to µ(A) := µX(A) := |A|/|X| as the density of A (in X).


The density increment strategy. In proving the Roth-type theorems outlined above, we shall employ a so-called density increment strategy, as have most proofs of Roth’s theorem resulting in good bounds. This operates roughly as follows. Let G be [N] or Fnq. If A ⊆ G has density α but contains no non-trivial solutions to x + y + z = 3w, then one shows that A has increased density (1 + c(α))α on a translate of some ‘large substructure’ V of G – say a long progression in the case of [N] or a large subspace in the case of Fnq. Thus |A∩(x+V )| (1+c)α|V |. One then looks at (A−x)∩V , which is still solution-free by translation invariance, and tries to repeat the argument. One thus produces denser and denser solution-free sets on smaller and smaller substructures, but since a density can never increase beyond 1, the iteration must at some point terminate (provided the function c(α) is nice enough). Generally this means that the substructures on which one is iterating must have become trivial, so as long as the original density is large enough for the increased densities to reach 1 before the substructures become trivial, one has shown that the set must contain a solution to the equation.

Of course, all this is saying is roughly that we shall prove the result by induction; the whole game is to ﬁnd arguments to make the substructures V and the increments c(α) as large as possible, while keeping V nice enough to iterate. For many proofs of Roth’s theorem, the substructures on which one increments are directly related to the large Fourier coeﬃcients of A; for us this is not quite the case, the substructures being uncovered instead by the probabilistic almost-periodicity results of [10]. To state one of these results in detail, let us introduce some further notation.

Normalisations, Lp-norms, convolutions. Now, we have talked about densities above, and it is relatively standard practice in additive combinatorics these days to work with these rather than cardinalities of sets. An associated trend has been to furthermore use normalised convolutions and Lp norms. In this paper we shall ﬁnd it useful to work with both densities and cardinalities, as we shall operate relatively ‘locally’ later on. We thus speak of densities, but write, for an abelian group G, a subset X ⊆ G, a function f : G → C and a real number p 1,

µX := 1X/|X|, f pp :=

|f(x)|p, f ∗ g(x) :=

x∈G

f(y)g(x − y).

y∈G

Here and throughout, 1X denotes the indicator function of X, taking the value 1 if its input lies in X and 0 otherwise.

Convolutions really are central objects for us when pursuing a density increment strategy

- as outlined above. Indeed, the quantity 1A∗µV (x) is precisely |A∩(x−V )|/|V |, which is the relative density of A on x−V , and the number of solutions to our equation is precisely


1A ∗ 1A ∗ 1A ∗ 1−3·A(0). Crucially, however, we shall not prove our results by studying this function directly, as did most previous proofs, but we shall nevertheless deal with similar convolutions, and for this the key tools will be certain almost-periodicity results.

Almost-periodicity. Our main tool for showing properties of convolutions is the following Lp-almost-periodicity result, which is a version of the main theorem of [10], but with somewhat less detailed moment estimates in the probabilistic arguments; see for example [26, 7] for a proof.

- Theorem 2.1. Let p 2, ǫ ∈ (0, 1) and k ∈ N be parameters. Let A, L, S be ﬁnite subsets of an abelian group. Suppose |A + S| K|A|. Then there is a set T ⊆ S with |T| 0.99K−Cpk2/ǫ2|S| such that

1A ∗ 1L(· + t) − 1A ∗ 1L p ǫ|A||L|1/p for all t ∈ kT − kT.

The result thus says that, for two sets A and L, provided A is structured in the sense of not growing much under addition with some set S, one can ﬁnd lots of Lp-almostperiods of the convolution 1A ∗ 1L, these being elements t for which this function does not change by much (in Lp) upon translation by t.

We shall bootstrap this to other variants later on; let us now instead turn to the model setting, in which we can simply quote a similar result.

3. Two proofs in the finite field setting

Here we shall prove Theorem 1.5, which said that if a subset A ⊆ Fnq of density α does not contain any non-trivial solutions to the equation

x + y + z = 3w (3.1)

then α exp −cn1/5 . Note that, for this equation, a solution is trivial if and only if x = y = z = w, and that the result is trivial if q is divisible by 2 or 3, so we assume throughout that it is not. We shall actually give two diﬀerent proofs of this result, one more analytic and one more combinatorial – but both following the density increment strategy outlined in the previous section. It turns out that the former proof extends more easily to the setting of more general ﬁnite abelian groups, from which one can deduce Theorem 1.4, whereas the latter serves as inspiration for the later proofs ﬁnding structures in sumsets.

In both proofs we shall use the following bootstrapped version of Theorem 2.1, which is a specialisation of [7, Theorem 7.4].

- Theorem 3.1. Let p 2 and ǫ ∈ (0, 1). Let G = Fnq be a vector space over a ﬁnite ﬁeld and suppose A, L ⊆ G have µ(A) α. Then there is a subspace V of codimension


d Cpǫ−2 log(2/ǫα)2 log(2/α) such that, for each t ∈ V ,

1A ∗ 1L(· + t) − 1A ∗ 1L Lp ǫ|A||L|1/p.

First proof: via L∞-almost-periodicity of three-fold convolutions.

This proof is based on the fact that if A does not contain any non-trivial solutions to (3.1), then 1−3·A ∗ 1A ∗ 1A+A(0) = |A|, which is very small. Two-fold convolutions like this are, however, fairly continuous functions: we shall deduce from a certain almostperiodicity result that 1−3·A∗1A∗1A+A∗µV (0) is then also small for some large subspace V . If |A+A| is large, a simple averaging then implies that A has a density increment on a translate of V . If, on the other hand, |A + A| is small, then one is done by a similar, if slightly simpler, argument.

The relevant almost-periodicity result is the following, but note that this will be superseded by a slightly more eﬃcient and general version in Section 5.

Theorem 3.2. Let ǫ ∈ (0, 1) and let A, M, L ⊆ Fnq have µ(A), µ(M) α. Then there is a subspace V of codimension at most Cǫ−2 log(2/ǫα)2 log(2/α)2 such that

|1A ∗ 1M ∗ 1L(x + t) − 1A ∗ 1M ∗ 1L(x)| ǫ|A||M| for all x ∈ G and t ∈ V . In particular

|1A ∗ 1M ∗ 1L(0) − 1A ∗ 1M ∗ 1L ∗ µV (0)| ǫ|A||M|.

- Proof. Apply Theorem 3.1 with p = C log(2/α) and ǫ/2 to get a subspace V of the required codimension such that

1A ∗ 1L(· + t) − 1A ∗ 1L p 2 1ǫ|A||L|1/p. Then, for r with 1/r + 1/p = 1, H¨older’s inequality gives

![image 12](<2014-schoen-roth-theorem-four-variables_images/imageFile12.png>)

1A ∗ 1M ∗ 1L(· + t) − 1A ∗ 1M ∗ 1L ∞ 1M r 1A ∗ 1L(· + t) − 1A ∗ 1L p

- 1

![image 13](<2014-schoen-roth-theorem-four-variables_images/imageFile13.png>)

- 2ǫ|A||M|(|L|/|M|)1/p,


whence the ﬁrst claim is proved. The second follows from the triangle inequality.

We now split into two cases, depending on whether the sumset A + A is large or not.

Large sumset. In the large sumset case, where µ(A + A) 2 1, we shall make use of the fact that 1−3·A ∗ 1A ∗ 1A+A(0) = |A| if A is free from solutions to (3.1), which means that the convolution 1−3·A ∗ 1A ∗ 1(A+A)c takes a really large value. Though perhaps not clear in this formulation, this argument was inspired by those of [9, 11].

![image 14](<2014-schoen-roth-theorem-four-variables_images/imageFile14.png>)

- Proposition 3.3. Let A ⊆ Fnq have density α and size at least 8. Suppose µ(A+A) 2 1 and that A does not contain any non-trivial solutions to (3.1). Then there is a subspace V of codimension at most C log(2/α)4 such that 1A ∗ µV (x) 2 3α for some x.


![image 15](<2014-schoen-roth-theorem-four-variables_images/imageFile15.png>)

![image 16](<2014-schoen-roth-theorem-four-variables_images/imageFile16.png>)

Recall that 1A ∗ µV (x) = |A ∩ (x − V )|/|V |, and so the conclusion says that A has massively increased density on some aﬃne subspace of low codimension.

- Proof. Apply Theorem 3.2 with M = −3 · A, L = A + A and ǫ = 1/8 to get a subspace V of the required codimension such that


1−3·A ∗ 1A ∗ 1A+A ∗ µV (0) 1−3·A ∗ 1A ∗ 1A+A(0) + 81|A|2.

![image 17](<2014-schoen-roth-theorem-four-variables_images/imageFile17.png>)

Since 1−3·A ∗ 1A ∗ 1A+A(0) = |A| |A|2/8, we thus have

1−3·A ∗ 1A ∗ 1A+A ∗ µV (0) 4 1|A|2, and so

![image 18](<2014-schoen-roth-theorem-four-variables_images/imageFile18.png>)

1−3·A ∗ 1A ∗ 1(A+A)c ∗ µV (0) 4 3|A|2. The left-hand side here is at most |A||(A + A)c| 1A ∗ µV ∞, and so we are done.

![image 19](<2014-schoen-roth-theorem-four-variables_images/imageFile19.png>)

Small sumset. That one can obtain a good density increment for A when A+A is small is well known, and a result almost suﬃcing for our purposes is contained in [26] – see e.g. Theorem 9.1 there. We shall however use the following.

- Proposition 3.4. Suppose A ⊆ Fnq has density α and µ(A + A) 12. Then there is a subspace V of codimension at most C(log 2/α)4 such that 1A ∗ µV (x) 2 3α for some x.


![image 20](<2014-schoen-roth-theorem-four-variables_images/imageFile20.png>)

![image 21](<2014-schoen-roth-theorem-four-variables_images/imageFile21.png>)

Proof. Apply Theorem 3.2 with M = A, L = −(A + A) and ǫ = 1/4 to get a subspace V of the required codimension such that

|1A ∗ 1A ∗ 1−(A+A)(0) − 1A ∗ 1A ∗ 1−(A+A) ∗ µV (0)| 14|A|2. But 1A ∗ 1A ∗ 1−(A+A)(0) = |A|2 since 1A ∗ 1A is supported on A + A, and so 1A ∗ 1A ∗ 1−(A+A) ∗ µV (0) 34|A|2. Since the left-hand side here is at most |A||A + A| 1A ∗ µV ∞, the result follows.

![image 22](<2014-schoen-roth-theorem-four-variables_images/imageFile22.png>)

![image 23](<2014-schoen-roth-theorem-four-variables_images/imageFile23.png>)

Note that we did not need to assume that A was free of solutions to any equations here.

Completing the proof: iterating. Combining these propositions, one immediately obtains Corollary 3.5. Let A ⊆ Fnq have density α and size at least 8. Suppose A does not contain any non-trivial solutions to (3.1). Then there is a subspace of codimension at most C log(2/α)4 such that 1A ∗ µV (x) 32α for some x.

![image 24](<2014-schoen-roth-theorem-four-variables_images/imageFile24.png>)

We now simply iterate this corollary to complete the proof.

Proof of Theorem 1.5. If A ⊆ G := Fnq has density α, size at least 8 and is free of nontrivial solutions to (3.1), then Corollary 3.5 gives us a subspace V G of codimension

- at most C log(2/α)4 and an element x ∈ G for which |(A − x) ∩ V | 2 3α|V |,


![image 25](<2014-schoen-roth-theorem-four-variables_images/imageFile25.png>)

that is, a subspace in which A−x has density at least 32α. Note that A−x is still free of non-trivial solutions to (3.1) by translation invariance. We then repeat this argument

![image 26](<2014-schoen-roth-theorem-four-variables_images/imageFile26.png>)

with G replaced by V , and so on, obtaining solution-free sets of increasing densities αj in spaces of lowering dimension nj, with α1 = α and n1 = n. Assuming αj 8q−n

at each stage, we thus have

j

nj+1 nj − C log(2/α)4 n − Cj log(2/α)4, and

αj+1 2 3αj 2 3 j α.

![image 27](<2014-schoen-roth-theorem-four-variables_images/imageFile27.png>)

![image 28](<2014-schoen-roth-theorem-four-variables_images/imageFile28.png>)

Since the density cannot increase beyond 1, this process must terminate with some j C log(2/α). If the claimed bound α exp −cn1/5 does not hold then we have nj n − Cj log(2/α)4 n/2 by the time of termination, and so running out of dimensions is not a reason for the process to terminate. Thus we must have αj < 8q−n

. But this is easily seen to imply the claimed bound anyway, and we are done.

j

Before we go on to give our second proof, let us make a quick remark about the types of solutions we have considered.

Remark 3.6. In the statement of Theorem 1.5 we forbade all non-trivial solutions to (3.1) in A, these being any non-constant quadruples (x, y, z, w) for which x+y+z = 3w. This has the eﬀect of forbidding A from containing solutions to certain other equations

- as well, such as non-trivial three-term arithmetic progressions – if x, y, z are distinct and lie in arithmetic progression, then the quadruple (x, y, z, y) solves our equation. Though we did not pursue this issue above for the sake of clarity of exposition, let us mention that incorporating a short additional argument in fact shows that the same bound holds if one only disallows solutions where all the variables are distinct, so that one is only disallowing solutions to this equation and not any ‘sub-equations’.


Second proof: via properties of three-fold sumsets. The following property of three-fold sumsets encodes the key to this proof.

Proposition 3.7. Let η ∈ (0, 1) and let A, B ⊆ Fnq be sets of densities α, β respectively. Then there is a subspace V of codimension at most C log(2/ηβ) log(2/α)3 and a set X ⊆ B with |X| 0.99|B| such that

|(x + V ) ∩ (B + A − A)| (1 − η)|V | for every x ∈ X.

Another way of putting the conclusion is that 1B+A−A ∗ µV (x) 1 − η for each x ∈ X.

Proof. Apply Theorem 3.1 with p = C log(2/ηβ), ǫ = 1/2 and L = B − A to get a subspace V of the required codimension such that

1A ∗ 1B−A(· + t) − 1A ∗ 1B−A p 2 1|A||B − A|1/p

![image 29](<2014-schoen-roth-theorem-four-variables_images/imageFile29.png>)

for each t ∈ V . Let X consist of all x ∈ B such that |(x + V ) ∩ (B + A − A)| (1 − η)|V |, so that if x ∈/ X then 1A ∗ 1B−A(x + t) = 0 for more than η|V | elements t ∈ V . Then

1A ∗ 1B−A(x)p <

η|V |

t∈V

x∈B\X

1A ∗ 1B−A(· + t) − 1A ∗ 1B−A pp 2 1

|A|p|B − A||V |.

![image 30](<2014-schoen-roth-theorem-four-variables_images/imageFile30.png>)

p

But 1A ∗ 1B−A(x) = |A| for each x ∈ B, and so this implies that |B \ X| < 21

η−1|B − A| 0.01|B|, which completes the proof.

![image 31](<2014-schoen-roth-theorem-four-variables_images/imageFile31.png>)

p

Corollary 3.8. Let η ∈ (0, 1) and let A, B, C ⊆ Fnq have µ(A), µ(C) α and µ(B) β. Then there is a subspace V of codimension at most C log(2/ηβ) log(2/α)3, an element

t ∈ Fnq and a set X ⊆ B + t with |X| 0.99|B| such that

|(x + V ) ∩ (A + B + C)| (1 − η)|V | for every x ∈ X.

Proof. Since t 1A ∗ 1C(t) = |A||C|, there is some t such that µ(A ∩ (t − C)) α2. Applying Proposition 3.7 with this intersection instead of A completes the proof.

Using this we give a second proof of Corollary 3.5, ﬁnding a good density increment.

Second proof of Corollary 3.5. Partition A = A1 ∪ A2 with |A1| = ⌈54|A|⌉ and apply Corollary 3.8 with η := α/2, B = C = −A1 and 3 · A2 in place of A. This gives us a subspace V of codimension at most C log(2/α)4, an element t and a set X ⊆ t−A with

![image 32](<2014-schoen-roth-theorem-four-variables_images/imageFile32.png>)

|X| 34|A| such that |(x + V ) ∩ (3 · A2 − A1 − A1)| (1 − η)|V | for each x ∈ X.

![image 33](<2014-schoen-roth-theorem-four-variables_images/imageFile33.png>)

Since A does not contain any non-trivial solutions to (3.1), A and 3 · A2 − A1 − A1 are disjoint, whence

|(x + V ) ∩ A| 2 1α|V | for each x ∈ X. (3.2) Since V is a subspace, this in fact holds for all x ∈ X + V . How large is this sumset? Well, if 1X ∗ µV (x) 32α for some x, then we would have a density increment of the kind we are after, so let us assume that 1X ∗ µV (x) < 23α for all x. Then

![image 34](<2014-schoen-roth-theorem-four-variables_images/imageFile34.png>)

![image 35](<2014-schoen-roth-theorem-four-variables_images/imageFile35.png>)

![image 36](<2014-schoen-roth-theorem-four-variables_images/imageFile36.png>)

1X ∗ µV (x) < 32α|X + V |,

|X| =

![image 37](<2014-schoen-roth-theorem-four-variables_images/imageFile37.png>)

x∈X+V

and so (3.2) holds for at least |X+V | 2 1|G| elements x. In other words, 1A∗µV (x) 12α for at least half of the elements of the group. Since the average of this function over the

![image 38](<2014-schoen-roth-theorem-four-variables_images/imageFile38.png>)

![image 39](<2014-schoen-roth-theorem-four-variables_images/imageFile39.png>)

whole group is α, we must have 1A ∗ µV (x) 32α for some x, and so we are done.

![image 40](<2014-schoen-roth-theorem-four-variables_images/imageFile40.png>)

Since Theorem 1.5 followed directly from Corollary 3.5, this completes the proof.

Extending the arguments. Both of these proofs of Theorem 1.5 can be extended to handle the case of sets of integers using the machinery of regular Bohr sets pioneered by Bourgain [5], each with their own sets of diﬃculties. It turns out this process is more straightforward for the ﬁrst proof, however, and so it is this that we shall present, starting in the next section with a review of the basic theory surrounding Bohr sets. The second proof is however very much related to the proofs we shall give for the results on structures in sums of sparse sets, as should become apparent.

4. Bohr sets and their elementary properties

When one wants to perform a density increment argument of the type we have just used in groups without a rich subgroup structure, it is by now rather established practice to turn to Bohr sets as a natural substitute for subspaces. In an abelian group G, we deﬁne these in terms of the dual group G of characters, consisting of homomorphisms from G to C× with the group operation given by pointwise multiplication.

Deﬁnition 4.1. Let Γ ⊆ G and let ρ 0. We deﬁne the Bohr set on these data by Bohr(Γ, ρ) = {x ∈ G : |γ(x) − 1| ρ for all γ ∈ Γ}.

We refer to |Γ| as the rank of the Bohr set, and ρ as its radius4. We say that Bohr(Γ′, ρ′) Bohr(Γ, ρ) is a sub-Bohr set if Γ′ ⊇ Γ and ρ′ ρ; note in particular that this implies containment as sets. We shall frequently need to scale the radii of our Bohr sets: if B = Bohr(Γ, ρ) and δ 0, then we write Bδ = Bohr(Γ, δρ).

We refer the reader to Section 4.4 in the book [29] of Tao and Vu for the proofs of the following lemmas and for more background5.

Lemma 4.2. Let Γ ⊆ G be a set of d characters, let ρ ∈ [0, 2], and let B = Bohr(Γ, ρ). Then we have the size estimate

|B| (ρ/2π)d|G| the doubling estimate

|B2| 6d|B|, and, for δ ∈ [0, 1], the decay estimate

|Bδ| (δ/2)3d|B|.

In particular |B + B| 6d|B|, since Bδ + Bǫ ⊆ Bδ+ǫ by the triangle inequality. Thus Bohr sets have fairly small doubling if d is small. Subspaces, however, enjoy the stronger property that |V + V | = |V | regardless of dimension, and this discrepancy in doubling constants reﬂects an underlying issue that means our argument becomes terribly ineﬃcient if we simply try to replace subspaces with Bohr sets. In giving a proof of Roth’s theorem with strong bounds, Bourgain [5] showed how to work around this issue, namely by working with pairs of Bohr sets (B, Bδ) with δ small, for which |B + Bδ| |B1+δ|. A priori this need not be close to |B|, but the following property ensures this. Deﬁnition 4.3 (Regularity). We say that a Bohr set B of rank d is regular if

|B1+δ| |B|

1 − 12d|δ|

1 + 12d|δ| whenever |δ| 1/12d.

![image 41](<2014-schoen-roth-theorem-four-variables_images/imageFile41.png>)

![image 42](<2014-schoen-roth-theorem-four-variables_images/imageFile42.png>)

- 4Note that these quantities are not well-deﬁned in terms of just the set itself, but we think of these data as being included in the deﬁnition of the Bohr set.
- 5The constants appearing here are somewhat diﬀerent to those in [29], as we have deﬁned Bohr sets in terms of quantities of the form |z − 1| rather than arg(z).


The constant 12 here is of course not particularly important, but we include it for deﬁniteness. Now, not all Bohr sets are regular, but it is a consequence of the doubling estimate |B| 6d|B1/2| that growth must be somewhat limited around some slight rescaling of B:

- Lemma 4.4. If B is a Bohr set, then there is a δ ∈ [21, 1] for which Bδ is regular.

![image 43](<2014-schoen-roth-theorem-four-variables_images/imageFile43.png>)

If B is regular of rank d we have the useful property that |B + Bδ| 2|B| whenever δ 1/12d. We also have the following useful consequence of regularity, resting simply on an application of the triangle inequality.

- Lemma 4.5. If B is a regular Bohr set of rank d and B′ ⊆ Bδ with δ ǫ/24d, then µB ∗ µB′ − µB L1(G) ǫ.

We require ﬁnally an arithmetic property of Bohr sets, which follows from the size estimate in Lemma 4.2 and the inclusion kB1/k = B1/k + · · · + B1/k ⊆ B.

- Lemma 4.6. Let N be a prime and let B ⊆ ZN be a Bohr set of rank d 1 and radius ρ ∈ [0, 2]. Then B contains an arithmetic progression of size at least 21πρN1/d.


![image 44](<2014-schoen-roth-theorem-four-variables_images/imageFile44.png>)

5. L∞-almost-periodicity relative to Bohr sets

To carry out the strategy of Section 3 with Bohr sets in place of groups, the ﬁrst thing we need to do is prove an appropriate analogue of Theorem 3.2. Of course, not only do we need to replace the subspace V in the conclusion with a Bohr set – which is entirely straightforward – but we are only allowed to assume density in a Bohr set rather than in a group. It turns out that this is also fairly straightforwardly achievable.

Almost-periodicity with dense sets. Recall Theorem 2.1, the Lp-almost-periodicity result for two-fold convolutions. From this we argue straightforwardly as with Theorem

- 3.2 to obtain the following L∞-almost-periodicity result for three-fold convolutions.


Theorem 5.1. Let ǫ ∈ (0, 1) and k ∈ N be parameters. Let A, M, L, S be ﬁnite subsets of an abelian group. Suppose |A + S| K|A| and η := |M|/|L| 1. Then there is a set T ⊆ S with |T| exp(−Ck2ǫ−2 log(2/η) log(2K)) |S| such that

1A ∗ 1M ∗ 1L(· + t) − 1A ∗ 1M ∗ 1L ∞ ǫ|A||M| for all t ∈ kT − kT.

Proof. Apply Theorem 2.1 with parameters ǫ/2 and p to be speciﬁed to obtain a set T of almost-periods for 1A ∗ 1L. By H¨older’s inequality we then have, for p1 + 1q = 1 and any t ∈ kT − kT,

![image 45](<2014-schoen-roth-theorem-four-variables_images/imageFile45.png>)

![image 46](<2014-schoen-roth-theorem-four-variables_images/imageFile46.png>)

1A ∗ 1M ∗ 1L(· + t) − 1A ∗ 1M ∗ 1L ∞ 1M q 1A ∗ 1L(· + t) − 1A ∗ 1L p

- 1

![image 47](<2014-schoen-roth-theorem-four-variables_images/imageFile47.png>)

- 2ǫ|A||M|(|L|/|M|)1/p.


Picking p = 3 log(2|L|/|M|) yields the result.

Remark 5.2. Note that the set T one obtains does not in fact depend on M but only on |M|/|L|. Also, since the methods of [10] worked for non-abelian groups, a version of the above result holds for arbitrary groups, and one could also replace 1M and 1L by functions more general than indicator functions, but we shall only apply it in the above case.

Finally we shall bootstrap this to ﬁnd not only a large set of translates, but a structured set: a Bohr set of translates. The price we shall pay is that we shall need to assume that the set A interacts nicely with a Bohr set and not just an arbitrary set S. The main idea of the proof is to couple Theorem 5.1 with Chang’s theorem on the structure of large spectra, which was one of the main insights that led to the powerful results [26] of Sanders. To state this properly we shall need the Fourier transform; the results of the following subsection are the only ones in this paper that appeal to Fourier analysis.

Almost-periodicity with Bohr sets. For a function f : G → C on a ﬁnite abelian group G we deﬁne the Fourier transform f : G → C on the dual group G by

f(γ) :=

![image 48](<2014-schoen-roth-theorem-four-variables_images/imageFile48.png>)

f(x)γ(x).

x∈G

Writing Ex∈X = |X|−1 x∈X, the Fourier inversion formula, Parseval’s identity and the convolution identity then take the form

f(x) = Eγ∈ G f(γ)γ(x),

|f(x)|2 = Eγ∈ G | f(γ)|2, and

x∈G

f ∗ g(γ) = f(γ) g(γ). Finally, for a set X ⊆ G, write

Specδ(µX) := {γ ∈ G : | µX(γ)| δ} for the δ-large spectrum of µX = 1X/|X|. See [29] for more on all of this.

Chang’s theorem [29, Lemma 4.36] says that the large spectrum Specδ(µX) is ‘lowdimensional’: it is contained in the {−1, 0, 1}-span of a set of at most Cδ−2 log(1/µG(X)) characters. An immediate and useful consequence is that all the characters in Specδ(µX) can be approximately annihilated by a low-rank Bohr set if X is relatively dense in G. Sanders proved an eﬃcient version of such a consequence when X is a dense subset of a Bohr set rather than the group; the following is [22, Proposition 4.2].

- Proposition 5.3 (Chang–Sanders). Let δ, ν ∈ (0, 1]. Let G be a ﬁnite abelian group, let B = Bohr(Γ, ρ) ⊆ G be a regular Bohr set of rank d and let X ⊆ B. Then there is a set of characters Λ ∈ G and a radius ρ′ with


|Λ| ≪ δ−2 log(2/µB(X)) and ρ′ ≫ ρνδ2/d2 log(2/µB(X)) such that

|1 − γ(t)| ν for all γ ∈ Specδ(µX) and t ∈ Bohr(Γ ∪ Λ, ρ′).

The aforementioned bootstrapping can now take place via a standard argument.

Theorem 5.4 (L∞-almost-periodicity with Bohr sets). Let ǫ ∈ (0, 1). Let A, M, L be subsets of a ﬁnite abelian group G, and let B ⊆ G be a regular Bohr set of rank d and radius ρ. Suppose |A+S| K|A| for a subset S ⊆ B with µB(S) σ > 0, and assume η := |M|/|L| 1. Then there is a regular Bohr set B′ B of rank at most d + d′ and radius at least ρǫη1/2/d2d′, where

d′ ≪ ǫ−2 log2(2/ǫη) log(2/η) log(2K) + log(1/σ), such that

1A ∗ 1M ∗ 1L(· + t) − 1A ∗ 1M ∗ 1L ∞ ǫ|A||M| for all t ∈ B′. In particular,

1A ∗ 1M ∗ 1L ∗ µB′ − 1A ∗ 1M ∗ 1L ∞ ǫ|A||M|.

Proof. Begin by applying Theorem 5.1 to 1A ∗ 1M ∗ 1L with parameters ǫ and k := ⌈C log(2/ǫη)⌉ to obtain a set T ⊆ S with

µB(T) exp −Cǫ−2k2 log(2/η) log(2K) σ such that

1A ∗ 1M ∗ 1L(· + t) − 1A ∗ 1M ∗ 1L ∞ ǫ|A||M| for all t ∈ kT − kT. Fix some z ∈ T and set X = T − z, so that the above inequality holds for all t ∈ kX. Thus, by the triangle inequality,

1A ∗ 1M ∗ 1L ∗ µ(Xk) − 1A ∗ 1M ∗ 1L ∞ ǫ|A||M|,

where µX(k) := µX ∗· · ·∗µX with k copies of µX. It thus suﬃces to establish the theorem with 1A ∗ 1M ∗ 1L ∗ µ(Xk) in place of 1A ∗ 1M ∗ 1L, and so we switch now to this.

Noting that translating X does not aﬀect the conclusion of Proposition 5.3, apply this proposition to T = X +z with parameters δ = 1/2 and ν = ǫη1/2 together with Lemma

- 4.4 to get a regular Bohr set B′ B of the required rank and radius such that


|1 − γ(t)| ǫη1/2 for all γ ∈ Spec1/2(µX) and t ∈ B′. For any x ∈ G and t ∈ B′ we then have, by the Fourier inversion formula, triangle inequality and convolution identity,

|1A ∗ 1M ∗ 1L ∗ µ(Xk)(x + t) − 1A ∗ 1M ∗ 1L ∗ µ(Xk)(x)|

Eγ∈ G | 1A(γ)|| 1M(γ)|| 1L(γ)|| µX(γ)|k|γ(t) − 1|. (5.1) For each term in this average, consider whether γ ∈ Spec1/2(µX) or not. If γ ∈ Spec1/2(µX) we have |γ(t) − 1| ǫη1/2, and if not then | µX(γ)|k 1/2k ǫη1/2. Thus (5.1) is at most twice

ǫη1/2 Eγ∈ G | 1A(γ)|| 1M(γ)|| 1L(γ)|. Using the trivial inequality | 1A(γ)| |A| and Cauchy-Schwarz plus Parseval a` la

1/2

1/2

Eγ∈ G | 1L(γ)|2

Eγ∈ G | 1M(γ)|| 1L(γ)| Eγ∈ G | 1M(γ)|2

= |M|1/2|L|1/2 ﬁnishes the proof, after replacing ǫ with ǫ/4.

Remark 5.5. The regime in which the above argument is set up to be eﬃcient is one in which A is thought of as extremely small, but structured in the sense of not expanding much under addition to a Bohr set, M as being of ‘medium’ size and L as being large. The main utility of this result over previous Fourier-analytic ones of this sort, then, stems from the fact that the dependence on |L|/|M| in the rank of B′ is only polylogarithmic rather than polynomial.

6. Obtaining density increments on Bohr sets

The following proposition drives the density increment argument.

- Proposition 6.1. Let G be a ﬁnite abelian group of order not divisible by 3, let B ⊆ G be a regular Bohr set of rank d and radius ρ, and let A ⊆ B have relative density µB(A) α. Assume that |B| (Cd/α)3d. If A does not contain any non-trivial


solutions to x + y + z = 3w, then A has relative density at least 54α on a translate of a Bohr set B′ B of rank at most d + d′ and radius at least ρα3/2/d5d′, where d′ ≪ log(2/α)4.

![image 49](<2014-schoen-roth-theorem-four-variables_images/imageFile49.png>)

As in the model case, we prove this diﬀerently in two cases depending on whether a particular sumset is large or not. In each case we make the further assumption that our given set A is dense also in a narrower sub-Bohr set.

The large sumset, solution-free case.

- Lemma 6.2. Let G be a ﬁnite abelian group of order not divisible by 3, let B ⊆ G be a regular Bohr set of rank d and radius ρ, and let A ⊆ B have relative density µB(A) α. Let B′ := Bδ be a regular sub-Bohr set with δ := 1/Cd such that |B1+3δ| 1.01|B|, and assume that A′ := A ∩ B′ satisﬁes µB′(A′) α and |A + A′| |A|/2α. If |A| C and A does not contain any non-trivial solutions to x+y +z = 3w, then 1A ∗µT ∞ 1.8α for some Bohr set T B of rank at most d + d′ and radius at least ρα1/2/d4d′, where d′ ≪ log4(2/α).


Proof. Deﬁne S := 3 · Bν′ where ν := 1/Cd, so that (using the assumption on |G|) S is a Bohr set of rank d and radius at least ρ/Cd2, and note that, by regularity,

|3 · A′ + S| |B(1+′ ν)| 2|B′| α 2|3 · A′|. (6.1) Apply Theorem 5.4 with −3 · A′ in place of A, S as deﬁned above, M := A, L := B1+3δ \ (A + A′) and ǫ := 401 . Our assumption |A + A′| |A|/2α implies that

![image 50](<2014-schoen-roth-theorem-four-variables_images/imageFile50.png>)

![image 51](<2014-schoen-roth-theorem-four-variables_images/imageFile51.png>)

|L| 1.01|B| − 21α|A| 0.501α |A|, (6.2) and so the parameter η of that theorem is certainly at least α. We may further take K = 2/α by (6.1), and so we get a Bohr set T S of rank at most d + d′ and radius

![image 52](<2014-schoen-roth-theorem-four-variables_images/imageFile52.png>)

![image 53](<2014-schoen-roth-theorem-four-variables_images/imageFile53.png>)

- at least ρα1/2/d4d′, where d′ C log4(2/α), such that


1−3·A′ ∗ 1A ∗ 1L ∗ µT − 1−3·A′ ∗ 1A ∗ 1L ∞ 40 1 |A′||A|. Now, since A does not contain any non-trivial solutions to x + y + z = 3w, we have

![image 54](<2014-schoen-roth-theorem-four-variables_images/imageFile54.png>)

1−3·A′ ∗ 1A ∗ 1A+A′(0) = |A′|.

Thus

1−3·A′ ∗ 1A ∗ 1L ∗ µT(0) 1−3·A′ ∗ 1A ∗ (1B

1+3δ

= 4039|A′||A| − |A′|

![image 55](<2014-schoen-roth-theorem-four-variables_images/imageFile55.png>)

- 19

![image 56](<2014-schoen-roth-theorem-four-variables_images/imageFile56.png>)

- 20|A′||A|,


− 1A+A′)(0) − 401 |A′||A|

![image 57](<2014-schoen-roth-theorem-four-variables_images/imageFile57.png>)

provided |A| 40. By the pigeonhole principle, then, there must be some element x for which

1A ∗ µT(x) 20 19|A|/|L| 1.8α, by (6.2).

![image 58](<2014-schoen-roth-theorem-four-variables_images/imageFile58.png>)

The small sumset case. Again, the case in which A + A′ is small can be handled a slightly simpler fashion.

- Lemma 6.3. Let A ⊆ G, let B ⊆ G be a regular Bohr set of rank d and radius ρ, and let

A′ ⊆ B have relative density µB(A′) α. If |A+A′| |A|/2α, then 1A∗µT ∞ 1.8α for some Bohr set T B of rank at most d + d′ and radius at least ρα1/2/d3d′, where d′ ≪ log4(2/α).

Proof. Let S = Bν where ν := 1/Cd, so that

|A′ + S| |B1+ν| α 2|A′|. Applying Theorem 5.4 with A′ in place of A, this set S, M := A, L := −A − A′ and ǫ := 101 , we may take η 2α and K := 2/α to get a Bohr set T S of rank at most d + d′ and radius at least ρα1/2/d3d′ where d′ C log4(2/α) such that

![image 59](<2014-schoen-roth-theorem-four-variables_images/imageFile59.png>)

![image 60](<2014-schoen-roth-theorem-four-variables_images/imageFile60.png>)

1A′ ∗ 1A ∗ 1−A−A′ ∗ µT − 1A′ ∗ 1A ∗ 1−A−A′ ∞

1

![image 61](<2014-schoen-roth-theorem-four-variables_images/imageFile61.png>)

10|A′||A|.

Now, 1A ∗1−A−A′(x) = |A| for any x ∈ −A′, and so 1A′ ∗1A ∗1−A−A′(0) = |A′||A|. Thus 1A′ ∗ 1A ∗ 1−A−A′ ∗ µT(0) 10 9 |A′||A|.

![image 62](<2014-schoen-roth-theorem-four-variables_images/imageFile62.png>)

Pigeonholing and using the assumption on |A + A′|, there is thus some x for which 1A ∗ µT(x) 10 9 |A|/|A + A′| 1.8α.

![image 63](<2014-schoen-roth-theorem-four-variables_images/imageFile63.png>)

Rescaling and putting the cases together. We need one ﬁnal tool in order to put the previous two lemmas together to prove Proposition 6.1, namely a simple averaging argument due to Bourgain [5] that in practice allows us to assume that a dense subset A of a Bohr set B is also large on a sub-Bohr set Bδ for some not-too-small δ.

- Lemma 6.4. Let B be a regular Bohr set of rank d, let A ⊆ B have relative density α, and let B′, B′′ ⊆ Bδ where δ α/Cd. Then either


- (i) there is an x ∈ B such that 1A ∗ µB′(x) 10 7 α and 1A ∗ µB′′(x) 10 7 α, or

![image 64](<2014-schoen-roth-theorem-four-variables_images/imageFile64.png>)

![image 65](<2014-schoen-roth-theorem-four-variables_images/imageFile65.png>)

- (ii) 1A ∗ µB′ ∞


5

5

4α or 1A ∗ µB′′ ∞

4α.

![image 66](<2014-schoen-roth-theorem-four-variables_images/imageFile66.png>)

![image 67](<2014-schoen-roth-theorem-four-variables_images/imageFile67.png>)

Proof. Since B is regular, picking the constant C large enough yields |1A ∗ µB ∗ µB′(0) − 1A ∗ µB(0)| µB ∗ µB′ − µB 1 40 1 α by Lemma 4.5, and similarly for B′′. Since 1A ∗ µB(0) = µB(A) = α, this implies that Ex∈B 1A ∗ µB′(x) + 1A ∗ µB′′(x) (2 − 201 )α,

![image 68](<2014-schoen-roth-theorem-four-variables_images/imageFile68.png>)

![image 69](<2014-schoen-roth-theorem-four-variables_images/imageFile69.png>)

and so there exists x ∈ B such that 1A ∗ µB′(x) + 1A ∗ µB′′(x) (2 − 201 )α. Fix such an x. If we are not in the second case of the conclusion, we then have

![image 70](<2014-schoen-roth-theorem-four-variables_images/imageFile70.png>)

1A ∗ µB′(x) (2 − 201 )α − 54α = 107 α, and similarly for B′′, and so we are done.

![image 71](<2014-schoen-roth-theorem-four-variables_images/imageFile71.png>)

![image 72](<2014-schoen-roth-theorem-four-variables_images/imageFile72.png>)

![image 73](<2014-schoen-roth-theorem-four-variables_images/imageFile73.png>)

Proof of Proposition 6.1. We start by rescaling our Bohr set so that A is large at two scales simultaneously: apply Lemma 6.4 with δ := α/Cd picked so that B′ := Bδ is regular, and with B′′ := Bδ′′ where δ′ := 1/Cd is picked so that this is regular and |B1+3′ δ′| 1.01|B′|. If we are in the second case of the conclusion of that lemma, then we have a density increment on a translate of a Bohr set of rank d and radius at least α/Cd2, in which case we are done. So assume instead that we get an element x ∈ B such that

1A ∗ µB′(x), 1A ∗ µB′′(x) 10 7 α, and let A′ := (A − x) ∩ B′, A′′ := (A − x) ∩ B′′; these sets thus have relative densities at least α′ := 107 α in their respective Bohr sets. Note by translation invariance that A′ also does not contain any non-trivial solutions to our equation.

![image 74](<2014-schoen-roth-theorem-four-variables_images/imageFile74.png>)

![image 75](<2014-schoen-roth-theorem-four-variables_images/imageFile75.png>)

Now, if |A′ + A′′| |A′|/2α′, then we apply Lemma 6.3 with (A′, A′′, B′′) in place of (A, A′, B) to get that

1A ∗ µT ∞ 1A′ ∗ µT ∞ 1.8α′ 4 5α, where T is a Bohr set of rank at most d + d′ and radius at least ρα3/2/d5d′, with d′ ≪ log4(2/α), and so we are done.

![image 76](<2014-schoen-roth-theorem-four-variables_images/imageFile76.png>)

If, on the other hand, |A′ + A′′| |A′|/2α′, then we apply Lemma 6.2 with (A′, A′′, B′) in place of (A, A′, B) to get precisely the same conclusion, provided that |A′| C. A quick computation using Lemma 4.2 shows that this is ensured by our assumption that |B| (Cd/α)3d, and so we are done.

7. The iterative argument

We now iterate the density increment result of the preceding section to prove our theorem.

- Theorem 7.1. Let G be a ﬁnite abelian group of order N not divisible by 3. If A ⊆ G does not contain any non-trivial solutions to x + y + z = 3w, then


|A|

N exp (c(log N)1/7)

.

![image 77](<2014-schoen-roth-theorem-four-variables_images/imageFile77.png>)

Proof. Initialise A1 = A, B(1) = Bohr({1}, 2) = G, d1 = 1, ρ1 = 2 and α1 = α = |A|/|G|. We run the following iterative scheme until the condition required for doing so fails.

If |B(j)| (Cdj/αj)3d

, then we apply Proposition 6.1 to our sets and parameters to produce a new Bohr set B(j+1) B(j) of rank dj and radius ρj satisfying

j

dj+1 dj + C log4(2/αj) Cj log4(2/α), ρj+1 ρjαj3/2/Cd5j log4(2/α)

and a set Aj+1 = (Aj − xj) ∩ B(j+1) ⊆ B(j+1) (for some xj) of relative density αj+1 4 5αj 4 5 j α. Note that Aj+1 has no non-trivial solutions to our equation by translation invariance.

![image 78](<2014-schoen-roth-theorem-four-variables_images/imageFile78.png>)

![image 79](<2014-schoen-roth-theorem-four-variables_images/imageFile79.png>)

Since the density of a set can never increase beyond 1, the growth of the αj implies that we must no longer be able to iterate this process when j = s for some s C log(2/α).

Thus we must have |B(s)| < (Cds/αs)3d

. On the other hand, by Lemma 4.2 we have |B(s)| (ρs/2π)d

s

|G|. Putting these together we certainly have |G| < (Cds/ρsαs)3ds . Now ds C log5(2/α), ρs (cα)Cs and αs α; putting these bounds in gives |G| < exp C log7(2/α) , which yields the bound of the theorem upon rearranging.

s

- Remark 7.2. With minor modiﬁcations, one can of course also prove a version of this theorem with A simply being dense in a Bohr set, rather than the full group; we omit the details.


8. Additive structures in sums of sparse sets

We turn now to the questions of structures in sumsets, proving Theorems 1.6 and 1.7. This will be somewhat easier work than in the previous few sections as the arguments are iteration-free and so do not require the machinery associated with regular Bohr sets. We do, however, require the analogue of Theorem 3.1 for arbitrary ﬁnite abelian groups, this being another specialisation of [7, Theorem 7.4]:

- Theorem 8.1. Let p 2 and ǫ ∈ (0, 1). Let G be a ﬁnite abelian group and let A, L ⊆ G be sets with µ(A) α. Then there is a Bohr set T of rank at most


d := Cpǫ−2 log(2/ǫα)2 log(2/α) and radius at least ǫα1/2/d such that, for each t ∈ T,

1A ∗ 1L(· + t) − 1A ∗ 1L p ǫ|A||L|1/p.

Using this in place of Theorem 3.1, the following can be proved in precisely the same way as Corollary 3.8.

- Proposition 8.2. Let η ∈ (0, 1) and let A, B, C ⊆ G have densities α, β, γ respectively. Then there is a Bohr set T ⊆ G of rank at most d := C log(2/ηβ) log(2/αγ)3 and radius at least (αγ)1/2/d, and an element t ∈ G, such that for any V ⊆ T there is a set X ⊆ B + t with |X| 0.99|B| such that

|(x + V ) ∩ (A + B + C)| (1 − η)|V | for every x ∈ X.

Note that if C = −A then we can reduce the radius to α1/2/d and take t = 0.

- Proposition 8.3. Let A, B, C be sets of densities α, β, γ respectively in a ﬁnite abelian group G, and let p 1. Then there is a Bohr set T ⊆ G of rank at most d := Cp (log 2/αγ)3 and radius at least (αγ)1/2/d such that, for any subset V ⊆ T of size at most β · 2p, there is a set X ⊆ B of size |X| 0.99|B| such that a translate of X + V is contained in A + B + C.


Proof. This follows immediately from the preceding proposition on taking η = 1/(β 2p+1), so that (1 − η)|V | > |V | − 1.

One can also prove this directly from Theorem 8.1 following the proof of [7, Theorem 1.4] but taking into account the very large ‘higher energy’ of 1A∗1B−A; this is, of course, very much related to the proof of Proposition 3.7.

We now have some easy corollaries. Theorem 1.6 follows immediately from

- Theorem 8.4. Let A, B, C ⊆ [N] be sets of densities α, β, γ. Then A+B +C contains X + P where X ⊆ B has |X| 0.99|B| and P is an arithmetic progression of length at least


1/2

log N log3(2/αγ)

exp c

− log(1/αβγ) .

![image 80](<2014-schoen-roth-theorem-four-variables_images/imageFile80.png>)

Proof. By the standard trick of embedding [N] into ZN′ for N′ a prime between 6N and 12N, it suﬃces to prove the statement with [N] replaced by ZN for N a prime, so we assume this setup instead.

1/2

Now apply Proposition 8.3 with p = C log log3(2/αγN )

to obtain a set X ⊆ B and a Bohr

![image 81](<2014-schoen-roth-theorem-four-variables_images/imageFile81.png>)

set T of rank d Cp log3(2/αγ) and radius at least cαγ/d satisfying that theorem’s conclusion. By Lemma 4.6, T contains an arithmetic progression of length at least (cαγ/d)N1/d. A quick calculation shows that the claimed arithmetic progression has length shorter than both this and β · 2p, whence we are done.

Note that this result can be non-trivial for α and γ as small as exp −c(log N)1/5 and for β even as small as exp −c(log N)1/2 . Also, since Bohr sets are extremely rich in additive structure, one can of course replace P in the conclusion by other kinds of sets, such as generalised arithmetic progressions, which can then be much larger. Just measuring the length of a single progression, as we have done above, is nevertheless a simple and useful measure of the strength of the method.

In the ﬁnite ﬁeld world we obtain the following generalisation of Theorem 1.7.

- Theorem 8.5. Let A, B, C ⊆ Fnq be sets of densities α, β, γ. Then A + B + C contains X + V where X ⊆ B has |X| 0.99|B| and V is an aﬃne subspace of dimension at least


cn log3(2/αγ)

− log(1/β) / log q.

![image 82](<2014-schoen-roth-theorem-four-variables_images/imageFile82.png>)

Proof. This follows just as before: applying Proposition 8.3 with p = cn/ log3(2/αγ), we obtain a large set X ⊆ B and a subspace T Fnq of dimension at least n−Cp log3(2/αγ) such that A + B + C contains a translate of X + V for any subset V ⊆ T of size less than β · 2p. Noting that this is less than |T| and letting V be a subspace of T of size between β · 2p/q and β · 2p then does the job.

Note that if q = 5, say, this can be non-trivial for α, γ as small as exp −cn1/3 and for β as small as 5−cn – in other words, |B| can be as small as a power of |G| in this setup. One can also reach such densities in the [N] world; see the next section.

- Remark 8.6. In the case that at A or C has very large density, the above results follow from those known for two-fold sumsets, with X being the whole of B even. The point here is thus that one can deal with much sparser sets, and the cost is only that one gets slightly fewer translates of the structure in A + B + C.


9. Concluding remarks

Other equations. We only dealt with the equation x + y + z = 3w in this paper, but it should be clear that one can deal with a general translation invariant equation c1x+c2y +c3z +c4w = 0 in precisely the same way, at least in the ﬁnite ﬁeld setting. In the more general setting one needs to make some small alterations related to the radii of the Bohr sets involved, but as in the former case the main diﬃculty is notational. A similar remark applies to equations in ﬁve variables, where precisely the same bounds hold.

Lower bounds in ﬁnite ﬁelds. What is the largest size of a subset of Fn5 with no non-trivial solutions to x + y + z = 3w? Just as for three-term progressions, we do not know of a Behrend-type example in this setting; indeed the best we know of comes from taking products of examples for small n, resulting in sets of size around θn for some θ < 5.

Small doubling instead of density. Clearly one could work with small-sumset conditions instead of density conditions in many of the proofs in this paper, but there is not much incentive to do so in view of the nature of the bounds and the presence of eﬀective ‘modelling lemmas’ in the settings of interest; see for example [16, Section 6].

Lower densities for the A + B + C problem in the integers. Theorem 8.4 found arithmetic progressions in A+B +C where one of the sets could have density as low as exp −c(log N)1/2 . To reach even lower densities, one can use the argument underlying [10, Theorem 1.9], again adding the idea of exploiting the higher energy of 1A ∗ 1B−A:

- Theorem 9.1. Let A, B, C ⊆ [N] be sets of densities α, β, γ. Then A+B +C contains an arithmetic progression of length at least


exp c

log N log(2/αγ)

![image 83](<2014-schoen-roth-theorem-four-variables_images/imageFile83.png>)

1/4

− log(1/β) .

This is worse than the bound in Theorem 8.4 for α = β = γ, but for certain density combinations it actually wins out. For example, it allows one to take α and γ to be as small as N−c provided β is a constant. (Note, however, that in this particular range one is guaranteed constant-length progressions already in A + C, as follows from [8].) An answer to the following question would thus be interesting.

Question 9.2. Suppose A, B ⊆ [N] have densities N−c and C ⊆ [N] has density exp −C(log N)2/3 . Must A + B + C contain an arithmetic progression of length tending to inﬁnity with N?

Correlations for 2A, 3A and 4A. Following on from the discussion of subspaces in sumsets in the introduction, let us oﬀer this perhaps illustrative comparison of results on correlations of 2A, 3A and 4A with subspaces, where A ⊆ Fnq has density α.

- • 2A contains 1−ǫ of an aﬃne subspace of codimension at most Cǫ−2−o(1) log(1/α)4.
- • 3A contains 1−ǫ of an aﬃne subspace of codimension at most C log(1/ǫα) log(1/α)3.
- • 4A contains all of an aﬃne subspace of codimension at most C log(1/α)4.


The ﬁrst and last bullets follow from Sanders’s work [26] (and directly from Theorem

- 3.2), and the middle one from Proposition 3.7. (Note also that the last bullet follows from the other two by inclusion-exclusion.) These results focus on the small density

case: when α is large some prior results can oﬀer better bounds; for example, for Fn2 Sanders showed in [22] that 2A contains 1 − ǫ of an aﬃne subspace of codimension at most Cα−2 log(1/ǫ), and codimension at most Cα−1 log(1/ǫ) in [23].

It is, however, far from clear where the truth lies for these results – not only in terms of the exponents on the logarithms but also in the qualitative diﬀerences between 3A and

- 4A. It may very well be that the result for 4A actually holds for 3A, as would have been expected prior to [26], and any proof of this is likely to be useful in proving Behrendshape bounds for Roth’s theorem itself. On the other hand, any demonstrations of a genuine diﬀerence between 3A and 4A, or three and four-variable equations, say, would also be very interesting.


References

- [1] M. Bateman and N. H. Katz, New bounds on cap sets, J. Amer. Math. Soc. 25 (2012), no. 2, 585–613. arXiv:1101.5851.


- [2] F. A. Behrend, On sets of integers which contain no three terms in arithmetical progression, Proc. Nat. Acad. Sci. U. S. A. 32, (1946). 331–332.
- [3] T. F. Bloom, A quantitative improvement for Roth’s theorem on arithmetic progressions, arXiv:1405.5800.
- [4] , Translation invariant equations and the method of Sanders, Bull. Lond. Math. Soc. 44

![image 84](<2014-schoen-roth-theorem-four-variables_images/imageFile84.png>)

(2012), no. 5, 1050–1067. arXiv:1107.1110.

- [5] J. Bourgain, On triples in arithmetic progression, Geom. Funct. Anal. 9 (1999), no. 5, 968–984.
- [6] , Roth’s theorem on progressions revisited, J. Anal. Math. 104 (2008) 155–192.

![image 85](<2014-schoen-roth-theorem-four-variables_images/imageFile85.png>)

- [7] E. Croot, I.  Laba and O. Sisask, Arithmetic progressions in sumsets and Lp-almost-periodicity, Combin. Probab. Comput. 22 (2013), no. 3, 351–365. arXiv:1103.6000.
- [8] E. Croot, I. Z. Ruzsa and T. Schoen, Arithmetic progressions in sparse sumsets, Combinatorial number theory, 157–164, de Gruyter, Berlin, 2007.
- [9] E. Croot and O. Sisask, A new proof of Roth’s theorem on arithmetic progressions, Proc. Amer. Math. Soc. 137 (2009), 805–809. arXiv:0801.2577.
- [10] , A probabilistic technique for ﬁnding almost-periods of convolutions, Geom. Funct. Anal. 20 (2010), no. 6, 1367–1396. arXiv:1003.2978.

![image 86](<2014-schoen-roth-theorem-four-variables_images/imageFile86.png>)

- [11] , Notes on proving Roth’s theorem using Bogolyubov’s method, http://people.math.gatech.edu/~ecroot/bogolyubov-roth2.pdf

![image 87](<2014-schoen-roth-theorem-four-variables_images/imageFile87.png>)

- [12] M. Elkin, An improved construction of progression-free sets, Israel J. Math. 184 (2011), 93–128. arXiv:0801.4310
- [13] G. A. Freiman, H. Halberstam, I. Z. Ruzsa, Integer sum sets containing long arithmetic progressions, Jour. London Math. Soc. 46 (2), 193–201, 1992.
- [14] B. Green, Arithmetic progressions in sumsets, Geom. Funct. Anal. 12 (2002), no. 3, 584–597.
- [15] , Finite ﬁeld models in additive combinatorics, Surveys in combinatorics 2005, 1–27, London Math. Soc. Lecture Note Ser., 327, Cambridge Univ. Press, Cambridge, 2005. arXiv:math/0409420.

![image 88](<2014-schoen-roth-theorem-four-variables_images/imageFile88.png>)

- [16] B. Green and I. Z. Ruzsa, Freiman’s theorem in an arbitrary abelian group, J. Lond. Math. Soc.

(2) 75 (2007), no. 1, 163–175. arXiv:math/0505198.

- [17] B. Green and J. Wolf, A note on Elkin’s improvement of Behrend’s construction, Additive number theory, 141–144, Springer, New York, 2010. arXiv:0810.0732.
- [18] D. R. Heath-Brown, Integer sets containing no arithmetic progressions, J. London Math. Soc. (2) 35 (1987), no. 3, 385–394.
- [19] K. Henriot, On arithmetic progressions in A + B + C, Int. Math. Res. Notices, ﬁrst published online June 11, 2013, doi:10.1093/imrn/rnt121. arXiv:1211.4917.
- [20] K. Roth, On certain sets of integers, J. London Math. Soc. 28 (1953), 104–109.
- [21] I. Z. Ruzsa, Solving a linear equation in a set of integers, I, Acta Arith. 65 (1993), 259–282.
- [22] T. Sanders, Additive structures in sumsets, Math. Proc. Cambridge Philos. Soc. 144 (2008), no. 2, 289–316. arXiv:math/0605520.
- [23] , Green’s sumset problem at density one half, Acta Arith. 146 (2011), no. 1, 91–101. arXiv:1003.5649.

![image 89](<2014-schoen-roth-theorem-four-variables_images/imageFile89.png>)

- [24] , On certain other sets of integers, J. Anal. Math. 116 (2012), 53–82. arXiv:1007.5444.

![image 90](<2014-schoen-roth-theorem-four-variables_images/imageFile90.png>)

- [25] , On Roth’s theorem on progressions, Ann. of Math. 174 (2011), no. 1, 619–636. arXiv:1011.0104.

![image 91](<2014-schoen-roth-theorem-four-variables_images/imageFile91.png>)

- [26] , On the Bogolyubov-Ruzsa lemma, Anal. PDE 5 (2012), no. 3, 627–655. arXiv:1011.0107.

![image 92](<2014-schoen-roth-theorem-four-variables_images/imageFile92.png>)

- [27] T. Schoen and I. Shkredov, Roth’s theorem in many variables, Israel J. Math. 199 (2014), no. 1, 287–308. arXiv:1106.1601.
- [28] E. Szemer´edi, Integer sets containing no arithmetic progressions, Acta Math. Hungar. 56 (1990), no. 1–2, 155–158.
- [29] T. Tao and V. H. Vu, Additive Combinatorics (CUP, 2006).


Faculty of Mathematics and Computer Science, Adam Mickiewicz University, Umultowska 87, 61-614 Poznan,´ Poland

E-mail address: schoen@amu.edu.pl

Department of Mathematics, KTH, 100 44 Stockholm, Sweden E-mail address: sisask@kth.se

