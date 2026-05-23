arXiv:1101.5851v2[math.CA]2Apr2011

New bounds on cap sets

1

Michael Bateman and Nets Hawk Katz

June 5, 2018

Abstract

We provide an improvement over Meshulam’s bound on cap sets in F3N. We show that there exist universal ǫ > 0 and C > 0 so that any cap set in F3N has size at most C 3

N

N1+ǫ . We do this by obtaining quite strong information about the additive combinatorial properties of the large spectrum.

![image 1](<2011-bateman-new-bounds-cap-sets_images/imageFile1.png>)

# 1 Introduction

A set A ⊂ F3N is called a cap set if it contains no lines. In this paper, we will be concerned with proving the following theorem:

Theorem 1.1. There exists an ǫ > 0, and C < ∞ such that if A ⊆ F3N is a cap set, then

C N1+ǫ

|A| 3N ≤

.

![image 2](<2011-bateman-new-bounds-cap-sets_images/imageFile2.png>)

![image 3](<2011-bateman-new-bounds-cap-sets_images/imageFile3.png>)

The problem of the maximal size of cap sets is a characteristic 3 model for the problem of ﬁnding arithmetic progressions of length 3 in rather dense sets of integers. Meshulam [M95] , through a direct use of ideas of Roth, was able to show that there is a constant C so that any cap set A has density at most NC . Our result may be viewed as a very modest improvement over Meshulam’s result.

![image 4](<2011-bateman-new-bounds-cap-sets_images/imageFile4.png>)

Sanders [S11] recently showed that any subset of the integers whose density in {1,... ,M} is at least C(log logM)

5

logM must contain arithmetic progressions of length 3. This may be thought of as bringing the results known for arithmetic progressions almost to the level of Meshulam’s result. This has spurred further interest in improving Meshulam’s result in hopes that it might suggest a way of improving the results on arithmetic progressions.

![image 5](<2011-bateman-new-bounds-cap-sets_images/imageFile5.png>)

![image 6](<2011-bateman-new-bounds-cap-sets_images/imageFile6.png>)

1MSC 2010 classiﬁcation: 11T71,05D40

A rather concrete, though perhaps still out of reach, goal in this direction is a conjecture of Erd¨os and Turan: Conjecture 1.2. Suppose A ⊆ Z is such that

1 n

= ∞.

![image 7](<2011-bateman-new-bounds-cap-sets_images/imageFile7.png>)

n∈A

Then A contains an arithmetic progression of every length.

It is clear that the present paper is directly relevant only for ﬁnding 3-term progressions. However it is also easy to see, based purely on density considerations, that proving an estimate of the type in Theorem 1.1 in the integer setting would yield the 3-term case of the conjecture stated above. In fact, Polymath 6 [PM6] has recently been started with the goal of adapting the ideas of this paper to the integer setting. See [PM] for more information about so-called “polymath” projects in general.

While the research in this paper was well underway, Gowers [G] wrote a post on his blog suggesting that one could attack the problem of bounding cap sets by studying the additive structure of their large spectrum. This had been our approach as well and we wrote a reply [K1] sketching our rather strong results regarding that structure. In the course of a few days, we realized that we actually could convert our structural theory into an estimate on the size of cap sets. We recorded this [K2] in a second reply to Gowers’s blog. The current paper should be viewed as an elaboration of these two posts.

We describe our plan for proving Theorem 1.1. To prove this theorem we will prove a theorem about sets without unusually dense subspaces, a notion we make precise below. Deﬁnition 1.3. We say a set A has no strong increments if for every subspace V ⊆ F3N with d = codimV ≤ N2 , we have

![image 8](<2011-bateman-new-bounds-cap-sets_images/imageFile8.png>)

20dρ N

|A ∩ V | |V |

≤ ρ +

.

![image 9](<2011-bateman-new-bounds-cap-sets_images/imageFile9.png>)

![image 10](<2011-bateman-new-bounds-cap-sets_images/imageFile10.png>)

- Theorem 1.4. There exists an ǫ > 0, and C < ∞ such that if A ⊆ F3N is a cap set with no strong increments, then


|A| 3N ≤

C N1+ǫ

.

![image 11](<2011-bateman-new-bounds-cap-sets_images/imageFile11.png>)

![image 12](<2011-bateman-new-bounds-cap-sets_images/imageFile12.png>)

Major ingredients needed to prove this theorem are Proposition 3.3, Lemma 5.3, and Theorem 7.1. We combine them with a Fourier analytic argument in Section 8.

Proof. We deduce Theorem 1.1 from Theorem 1.4 using induction. Suppose that for every n ≤ N − 1 we have shown that if B ⊆ F3n is a cap set, then

C n1+ǫ

|B| 3n ≤

.

![image 13](<2011-bateman-new-bounds-cap-sets_images/imageFile13.png>)

![image 14](<2011-bateman-new-bounds-cap-sets_images/imageFile14.png>)

We aim for a contradiction: assume there exists a cap set A ⊆ F3N such that 3|AN| > NC1+ǫ. By Theorem 1.4, this implies A has a strong increment. Since A has a strong increment,

![image 15](<2011-bateman-new-bounds-cap-sets_images/imageFile15.png>)

![image 16](<2011-bateman-new-bounds-cap-sets_images/imageFile16.png>)

there exists an aﬃne subspace V ⊆ F3N with codimension ≤ N2 such that |A ∩ V | |V |

![image 17](<2011-bateman-new-bounds-cap-sets_images/imageFile17.png>)

20dρ N

≥ ρ +

![image 18](<2011-bateman-new-bounds-cap-sets_images/imageFile18.png>)

![image 19](<2011-bateman-new-bounds-cap-sets_images/imageFile19.png>)

20d N

) >

= ρ(1 +

![image 20](<2011-bateman-new-bounds-cap-sets_images/imageFile20.png>)

C (N − d)1+ǫ

![image 21](<2011-bateman-new-bounds-cap-sets_images/imageFile21.png>)

since the derivative of x1+C ǫ is uniformly bounded by 16CN−2−ǫ = 16ρN−1 whenever 0 < ǫ < 1. But we know that A ∩ V (in fact any subset of A) is a capset. This contradicts the

![image 22](<2011-bateman-new-bounds-cap-sets_images/imageFile22.png>)

induction hypothesis, yielding Theorem 1.1.

![image 23](<2011-bateman-new-bounds-cap-sets_images/imageFile23.png>)

![image 24](<2011-bateman-new-bounds-cap-sets_images/imageFile24.png>)

![image 25](<2011-bateman-new-bounds-cap-sets_images/imageFile25.png>)

![image 26](<2011-bateman-new-bounds-cap-sets_images/imageFile26.png>)

## 1.1 Proof Sketch

We sketch our plan for proving Theorem 1.4.

We will study the large spectrum ∆ of a cap set A with no strong increments. The reader should think of ∆, for a cap set of the size 3NN given by Meshulam’s estimate, as consisting of the positions at which the absolute value of the Fourier transform of A is around N12. The set ∆ should have cardinality approximately N3 (established in Section 3) and have about N7 additive quadruples (established in Section 4). Recall that an additive quadruple is a quadruple (x1,x2,x3,x4) of elements of ∆ with the property that

![image 27](<2011-bateman-new-bounds-cap-sets_images/imageFile27.png>)

![image 28](<2011-bateman-new-bounds-cap-sets_images/imageFile28.png>)

x1 + x2 = x3 + x4.

Similarly an additive octuple is an octuple (x1,x2,x3,x4,x5,x6,x7,x8) of elements of ∆ with

x1 + x2 + x3 + x4 = x5 + x6 + x7 + x8.

It is easy to see a priori that a set with many additive quadruples will have many additive octuples. In our case, a set with size N3, having N7 quadruples must have at least N15 octuples. (But it may have more octuples.) The number of octuples it has should be taken as an indication of its structure. If there are many octuples, it means that the sumset ∆ + ∆ looks like it has more additive structure than the set ∆. We then say the set ∆ is additively smoothing. (It becomes smoother under addition.) We show, however, that this cannot be the case for ∆, the large spectrum. We use the probabilistic method to do this, ﬁnding too much of the spectrum contained in a small subspace in the additively smoothing case. We establish this in Section 5. (This is somewhat reminiscent of the paper of Croot and Sisask [CS11] where random selections are used to uncover structure.)

Thus our set ∆ is entirely additively non-smoothing. This means it is already as smooth as it will become under a small number of additions. This makes its additive structure particularly easy to uncover as it is already present without adding the set to itself. This kind of idea was ﬁrst exploited in a paper of the second author with Koester [KK10] , and we use techniques quite similar to those found in that paper. We end up showing that the set ∆ should be thought of as looking like the sum of a very structured set K of size N ( that is to say that K is almost additively closed) with a very random set Λ of size N2. Section 6 contains the proof of a structural theorem for sets with substantial additive energy (i.e., many additive quadruples) but no additive smoothing.

We ﬁnd that this structure of ∆ is inconsistent with A’s being a cap set with no strong increments. The reason is that we can use Freiman’s theorem to place K inside a subspace H with relatively low dimension. We can essentially mod out by H, examining the “ﬁbers”, the intersections of A with translates of H⊥. We ﬁnd that the structure of ∆ makes the behavior of the ﬁbers unrealistic. This argument is suggested by a paper of Sanders [S10], and is carried out in Section 8.

One ﬁnal remark about the value of ǫ obtained in this paper: it is necessarily rather small (at least with our current argument). We discuss the reasons for this in a brief ﬁnal section and give some conjectures that, if true, would greatly improve the eﬃciency of our argument. we have not attempted to optimize ǫ (or even keep track of exact dependence on ǫ) throughout the paper.

Acknowledgements The ﬁrst author is supported by an NSF postdoctoral fellowship, DMS-0902490. The second author is partially supported by NSF grant DMS-1001607.

The authors also thank Izabella  Laba and Olof Sisask for pointing out an error in the statement of the asymmetric Balog-Szemeredi-Gowers theorem in a preliminary version of this paper.

# 2 Preliminaries

In this section, we record a few general results of which we will make frequent use throughout the paper. We begin with our favorite form of the Cauchy-Schwarz inequality.

- Lemma 2.1. Let S and T be ﬁnite sets and ρ a map ρ : S −→ T.


Let P be the set of pairs

P = {(s1,s2) : ρ(s1) = ρ(s2)}. Then

- |S|2

![image 29](<2011-bateman-new-bounds-cap-sets_images/imageFile29.png>)

- |T|


.

|P| ≥

Proof. Note that we can express |P| by |P| =

t∈T

|ρ−1(t)|2.

Applying the Cauchy-Schwarz inequality we see

1 |T|

|P| ≥

![image 30](<2011-bateman-new-bounds-cap-sets_images/imageFile30.png>)

|ρ−1(t)|)2 = |S|2 |T|

(

.

![image 31](<2011-bateman-new-bounds-cap-sets_images/imageFile31.png>)

t∈T

![image 32](<2011-bateman-new-bounds-cap-sets_images/imageFile32.png>)

![image 33](<2011-bateman-new-bounds-cap-sets_images/imageFile33.png>)

![image 34](<2011-bateman-new-bounds-cap-sets_images/imageFile34.png>)

![image 35](<2011-bateman-new-bounds-cap-sets_images/imageFile35.png>)

Here we introduce another variant of Cauchy Schwarz:

- Lemma 2.2. Let (X,m) be a measure space with total measure M. Let A1,... Ak be measurable subsets of X and 0 < ρ < 1 be a number (the density), so that m(Aj) ρM for each j. Suppose k >> ρ1. Then


![image 36](<2011-bateman-new-bounds-cap-sets_images/imageFile36.png>)

k

m(Aj ∩ Al) k2ρ2M.

j=1 l =j

Proof. Note that

k

m(Aj) = ρkM << k2ρ2M,

j=1

since kρ >> 1. Thus we may estimate the full sum

k

- k
- l=1


m(Aj ∩ Al).

j=1

Deﬁne c(x) to be the measurable function giving for each x, the number of sets Aj which contain x; i.e.,

k

1Aj(x).

c(x) =

j=1

Thus we would like to estimate

c(x)2 ≥

1 M

( c(x))2 = k2ρ2M.

![image 37](<2011-bateman-new-bounds-cap-sets_images/imageFile37.png>)

![image 38](<2011-bateman-new-bounds-cap-sets_images/imageFile38.png>)

![image 39](<2011-bateman-new-bounds-cap-sets_images/imageFile39.png>)

![image 40](<2011-bateman-new-bounds-cap-sets_images/imageFile40.png>)

![image 41](<2011-bateman-new-bounds-cap-sets_images/imageFile41.png>)

In what follows µ shall be a small exponent. We will frequently use expressions like NO(µ). The exponent will be bounded by Cµ for C a universal constant which varies from line to line in the paper. We illustrate this by the following version of the large families principle (this is the principle which says that most children belong to large families) which will be used extremely often in this paper.

- Lemma 2.3. Let M1,... MK > 0 be real numbers and let R > 0 be a real number. Suppose that Mj ≤ RNµ for each j and suppose that

K

j=1

Mj ≥ RKN−µ.

Then there exists a subset J of {1,... ,K} with |J| N−O(µ)K so that for each j ∈ J, we have Mj N−O(µ)R.

Proof. Let

J = {j : Mj N−10µR}. Suppose that |J| N−10µK. Then by the upper bound on Mj, we have that

j∈J

Mj N−9µRK,

while

j /∈J

Mj N−10µRK. Combining these two estimates gives us a contradiction. We take a moment to state the asymmetric Balog-Szemeredi-Gowers theorem which we will have occasion to use. A set B ⊂ F3N will be said to be µ-additively closed if

![image 42](<2011-bateman-new-bounds-cap-sets_images/imageFile42.png>)

![image 43](<2011-bateman-new-bounds-cap-sets_images/imageFile43.png>)

![image 44](<2011-bateman-new-bounds-cap-sets_images/imageFile44.png>)

![image 45](<2011-bateman-new-bounds-cap-sets_images/imageFile45.png>)

|B − B| NO(µ)|B|.

- Lemma 2.4. Let B,C ⊂ F3N so that there are at least N−η|B||C|2 additive quadruples of the form


b1 + c1 = b2 + c2

with b1,b2 ∈ B and c1,c2 ∈ C. Let L = ||BC||, and assume L N10. Then there exists µ depending only on η, with µ → 0 as η → 0, and there exist an µ-additively closed set

![image 46](<2011-bateman-new-bounds-cap-sets_images/imageFile46.png>)

K ⊂ F3N and a set X ⊂ F3N with

|X| NO(µ)|B| |C|

,

![image 47](<2011-bateman-new-bounds-cap-sets_images/imageFile47.png>)

so that

- |B ∩ (X + K)| N−O(µ)|B|,

and an element x ∈ F3N so that

- |C ∩ (x + K)| N−O(µ)|C|.


In particular, the last inequality implies |K| N−O(µ)|C|. An only slightly stronger form of this lemma appears in the book of Tao and Vu as Lemma

- 2.35. [TV06] Another way of stating this result which we will use frequently is to deﬁne


a function f with limt−→0 f(t) = 0 and to let µ = f(η). We will use this kind of notation frequently in the paper with the choice of f varying from line to line. Finally, we record the form of Freiman’s theorem which we shall use.

- Theorem 2.5. A µ additively closed set is contained in a subspace of dimension NO(µ).


Various improvements of the ﬁnite characteristic Freiman’s theorem have occured such as the result by Sanders [S08] but these only aﬀect the constant in our formulation. Even Ruzsa’s original version [R99] suﬃces.

# 3 Review of Meshulam’s argument, Fourier analysis in F3N, and sparsity of the spectrum

For the remainder of this paper A will be a subset of F3N with |A| = ρ3N >> N31+N ǫ with ǫ > 0 to be determined later. Moreover A shall be a cap set meaning that it contains no

![image 48](<2011-bateman-new-bounds-cap-sets_images/imageFile48.png>)

lines. A line in F3N is characterized by being a set with exactly three distinct elements a,b,c satisfying a + b + c = 0.

In this section we will establish some basic facts needed for our proof, and that are enough to obtain Meshulam’s bound of ∼ N1 on the density of capsets. Further, we shall prove a statement of the form “The spectrum ∆ does not have too much intersection with any small subspace.”

![image 49](<2011-bateman-new-bounds-cap-sets_images/imageFile49.png>)

We will assume that there are no strong increments for A in the sense of Deﬁnition 1.3. Precisely, we assume there is no hyperplane H so that A ∩ H has density ≥ ρ + 20Nρ in H and no subspace H of codimension d ≤ N2 so that A ∩H has density ≥ ρ + 20Nρd. We recall that a contradiction of this assumption will mean that every large cap set A has strong increments. This will contradict the existence of large cap sets.

![image 50](<2011-bateman-new-bounds-cap-sets_images/imageFile50.png>)

![image 51](<2011-bateman-new-bounds-cap-sets_images/imageFile51.png>)

![image 52](<2011-bateman-new-bounds-cap-sets_images/imageFile52.png>)

√3

√3

![image 53](<2011-bateman-new-bounds-cap-sets_images/imageFile53.png>)

![image 54](<2011-bateman-new-bounds-cap-sets_images/imageFile54.png>)

We deﬁne the character e : F3 −→ C by e(0) = 1,e(1) = −21 +

2 i,e(2) = −21 −

2 i. We will study the Fourier transform of the set A, namely

![image 55](<2011-bateman-new-bounds-cap-sets_images/imageFile55.png>)

![image 56](<2011-bateman-new-bounds-cap-sets_images/imageFile56.png>)

![image 57](<2011-bateman-new-bounds-cap-sets_images/imageFile57.png>)

![image 58](<2011-bateman-new-bounds-cap-sets_images/imageFile58.png>)

1 3N a∈A

Aˆ(x) =

e(a · x).

![image 59](<2011-bateman-new-bounds-cap-sets_images/imageFile59.png>)

As a consequence of the assumption that A is a large cap set without strong increments, we shall see that there is a signiﬁcant set ∆ of x for which |Aˆ(x)| is fairly large (the set ∆ will be called the spectrum of A) and we shall see that ∆ does not concentrate too much in

any fairly low dimensional subspace of F3N. Our ﬁrst nontrivial fact about Aˆ is that A − ρ has large L3 norm, and moreover that this large L3 norm is accounted for by the set of x where |Aˆ(x)| is large. Precisely:

Deﬁnition 3.1. Deﬁne

∆ = {x = 0: |Aˆ(x)| ρ2}.

We shall refer to the set ∆ as the spectrum of A and it shall be our central object of study for the remainder of the paper.

Note that with this deﬁnition, ∆ is symmetric, that is ∆ = −∆.

It is worth noting that the following proposition is the only place in the paper where we use the assumption that A is a capset speciﬁcally; the other parts of the paper use only the assumption that A has no strong increments.

- Proposition 3.2. If A is a capset, then


Moreover,

and

|Aˆ(x)|3 ρ3.

x =0

|Aˆ(x)|3 ρ3,

x∈∆

N3 |∆| N3+3ǫ.

Note that this proposition is already enough to obtain Meshulam’s estimate: in particular, it guarantees that the set ∆ deﬁned in the statement of the proposition is nonempty. This means there is at least one x such that | A(x)| ρ2. This guarantees the existence of a

hyperplane P such that the density of A ∩ P inside P is at least ρ + cρ2. Taking ρ large enough compared to N1 already contradicts the no-strong-increment hypothesis, yielding Meshulam’s estimate.

![image 60](<2011-bateman-new-bounds-cap-sets_images/imageFile60.png>)

In what follows, we prove this proposition. We consider

1 33N

Aˆ(x)3 =

x∈F3N

e((a + b + c) · x).

![image 61](<2011-bateman-new-bounds-cap-sets_images/imageFile61.png>)

x∈F3N a∈A b∈A c∈A

Summing ﬁrst in x, we see that this expression yields 3−2N mutiplied by the number of solutions of the equation a + b + c = 0 with a,b,c taken from A. Since we have assumed that A is a cap set, the only solutions occur when a = b = c. Thus

Aˆ(x)3 = 3−2N|A| = 3−Nρ.

x∈F3N

However, we observe that Aˆ(0) = ρ. Thus, given the size of A, we see that ρ3 dominates 3−Nρ and we conclude

|Aˆ(x)|3 ρ3. (3.1)

x =0

However, following the proof of Plancherel’s inequality, we see that

|Aˆ(x)|2 ≤

x =0

x∈F3N

Summing ﬁrst in x, we conclude

1 32N

|Aˆ(x)|2 =

e((a − b) · x).

![image 62](<2011-bateman-new-bounds-cap-sets_images/imageFile62.png>)

x∈F3N a∈A b∈B

|Aˆ(x)|2 ≤ 3−N|A| ≤ ρ. (3.2)

x =0

By the assumption that A has no strong codimension 1 increment, we conclude

|Aˆ(x)|

|A| N3N

=

![image 63](<2011-bateman-new-bounds-cap-sets_images/imageFile63.png>)

ρ N

. (3.3)

![image 64](<2011-bateman-new-bounds-cap-sets_images/imageFile64.png>)

Recall that

∆ = {x = 0 : |Aˆ(x)| ρ2}.

By selecting the implicit constant in the deﬁnition of ∆ correctly, we see combining inequalities 3.1 and 3.2 that

|Aˆ(x)|3 ρ3. (3.4)

x∈∆

Combining inequalities 3.3 and 3.4, we see that |∆| N3. Combining the deﬁnition of ∆ with 3.2 we get |∆| N3+3ǫ.

Now we prove a statement of the form “The spectrum ∆ does not have too much intersection with any small subspace.” Precisely:

- Proposition 3.3. Let A be a set without strong increments. Let ∆ be the spectrum, as in Deﬁnition 3.1. Then for any subspace W of F3N having dimension d ≤ N2 , we have


![image 65](<2011-bateman-new-bounds-cap-sets_images/imageFile65.png>)

|∆ ∩ W| dN1+2ǫ. Moreover for such a subspace W, we have the estimate

d N

|Aˆ(w)|2 ρ2

.

![image 66](<2011-bateman-new-bounds-cap-sets_images/imageFile66.png>)

w =0∈W

Here we see what the assumption of no higher codimension strong increments implies about the spectrum ∆. Let H be a subspace with codimension d < N2 , we let V be a dimension d subspace which is transverse to H (i.e., V + H = F3N) and we let W be the annihilator space of H. Then for any w = 0 ∈ W, we see that

![image 67](<2011-bateman-new-bounds-cap-sets_images/imageFile67.png>)

1 3N v∈V

Aˆ(w) =

(|A ∩ (H + v)| − 3−d|A|)e(v · w).

![image 68](<2011-bateman-new-bounds-cap-sets_images/imageFile68.png>)

Then we have

|Aˆ(w)|2 = 3d−2N

w =0∈W

(|A ∩ (H + v)| − 3−d|A|)2. (3.5)

v∈V

By getting an upper bound on the right hand side of equation 3.5, we can obtain an upper bound on |∆ ∩ W|, which is our goal.

To estimate the right hand side, we subdivide V = V + ∪ V −, where

V + = {v : |A ∩ (H + v)| − 3−d|A| ≥ 0} and

V − = {v : |A ∩ (H + v)| − 3−d|A| < 0}

We observe that since

(|A ∩ (H + v)| − 3−d|A|) = 0,

v∈V

we have

||A ∩ (H + v)| − 3−d|A|| =

||A ∩ (H + v)| − 3−d|A||. (3.6)

v∈V +

v∈V −

We observe that the hypothesis that A has no strong increments implies that for v ∈ V +, we have the estimate

d N

||A ∩ (H + v)| − 3−d|A|| 3−d|A|

.

![image 69](<2011-bateman-new-bounds-cap-sets_images/imageFile69.png>)

Thus simply using that |V | = 3d, we get the estimates

and

d N

||A ∩ (H + v)| − 3−d|A|| |A|

![image 70](<2011-bateman-new-bounds-cap-sets_images/imageFile70.png>)

v∈V +

(3.7)

d2 N2

||A ∩ (H + v)| − 3−d|A||2 3−d|A|2

![image 71](<2011-bateman-new-bounds-cap-sets_images/imageFile71.png>)

v∈V +

Now for v ∈ V −, we have the trivial estimate ||A ∩ (H + v)| − 3−d|A|| ≤ 3−d|A|. In light of equation 3.6 and estimate 3.7 this yields

(3.8)

d N

||A ∩ (H + v)| − 3−d|A||2 3−d|A|2

![image 72](<2011-bateman-new-bounds-cap-sets_images/imageFile72.png>)

v∈V −

Combining inequalities 3.8 and 3.9, gives the estimate

d N

||A ∩ (H + v)| − 3−d|A||2 3−d|A|2

.

![image 73](<2011-bateman-new-bounds-cap-sets_images/imageFile73.png>)

v∈V

Thus equation 3.5 gives

(3.9)

d N

|Aˆ(w)|2 ρ2

.

![image 74](<2011-bateman-new-bounds-cap-sets_images/imageFile74.png>)

w =0∈W

However, we recall that if w ∈ ∆, we have that

1 N2+2ǫ

|Aˆ(w)| ρ2 =

.

![image 75](<2011-bateman-new-bounds-cap-sets_images/imageFile75.png>)

Thus we get the desired estimate:

|∆ ∩ W| dN1+2ǫ.

# 4 Additive structure in the spectrum of large cap sets

In this section we establish that the spectrum has some nontrivial additive structure. Speciﬁcally, we prove it has N7−O(ǫ) additive quadruples.

- Proposition 4.1. Let A be a large cap set. Let ∆ be the spectrum of A and let ∆′ be any symmetric subset of ∆ with


- 1

![image 76](<2011-bateman-new-bounds-cap-sets_images/imageFile76.png>)

- 2|∆|.


|∆′| ≥

Let E4(∆′) be the number of additive quadruplets x1 +x2 = x3 +x4 with x1,x2,x3,x4 ∈ ∆′. Then

E(∆′) |∆|4 N5+5ǫ

.

![image 77](<2011-bateman-new-bounds-cap-sets_images/imageFile77.png>)

The argument for a major subset ∆′ of ∆ is no diﬀerent, so for convenience of notation we assume in fact ∆′ = ∆.

We retain the notation of the previous section considering ∆ the spectrum of a large cap set A. In particular, we have |A| >> N31+N ǫ, we have

![image 78](<2011-bateman-new-bounds-cap-sets_images/imageFile78.png>)

N3 |∆| N3+3ǫ,

we have for every x ∈ ∆, that | A(x)| N |A1+|ǫ, and we have that ∆ is symmetric, namely ∆ = −∆.

![image 79](<2011-bateman-new-bounds-cap-sets_images/imageFile79.png>)

From the lower bound on | A(x)|, we have for each x, an aﬃne hyperplane Hx, annihilated by x so that

ρ N1+ǫ

= |A| N1+ǫ

1 3|A| 3N

.

|A ∩ Hx| −

![image 80](<2011-bateman-new-bounds-cap-sets_images/imageFile80.png>)

![image 81](<2011-bateman-new-bounds-cap-sets_images/imageFile81.png>)

![image 82](<2011-bateman-new-bounds-cap-sets_images/imageFile82.png>)

Summing over ∆, we obtain

(|A ∩ Hx| −

x∈∆

|A| 3

) |A||∆| N1+ǫ

.

![image 83](<2011-bateman-new-bounds-cap-sets_images/imageFile83.png>)

![image 84](<2011-bateman-new-bounds-cap-sets_images/imageFile84.png>)

We wish to rewrite this as a double sum by introducing 1Hx, the indicator function of Hx.

(1Hx(y) −

x∈∆ y∈A

We interchange the order of the sums:

1 3

) |A||∆| N1+ǫ

.

![image 85](<2011-bateman-new-bounds-cap-sets_images/imageFile85.png>)

![image 86](<2011-bateman-new-bounds-cap-sets_images/imageFile86.png>)

(

y∈A

x∈∆

Now we apply H¨older’s inequality:

(1Hx(y) −

1 3

)) |A||∆| N1+ǫ

.

![image 87](<2011-bateman-new-bounds-cap-sets_images/imageFile87.png>)

![image 88](<2011-bateman-new-bounds-cap-sets_images/imageFile88.png>)

|A|3

4(

![image 89](<2011-bateman-new-bounds-cap-sets_images/imageFile89.png>)

y∈A

(1Hx(y) −

|

x∈∆

1 3

)|4)14

![image 90](<2011-bateman-new-bounds-cap-sets_images/imageFile90.png>)

![image 91](<2011-bateman-new-bounds-cap-sets_images/imageFile91.png>)

|A||∆| N1+ǫ

.

![image 92](<2011-bateman-new-bounds-cap-sets_images/imageFile92.png>)

Taking everything to the fourth power and simplifying, we get

y∈A

(1Hx(y) −

|

x∈∆

1 3

)|4

![image 93](<2011-bateman-new-bounds-cap-sets_images/imageFile93.png>)

|A||∆|4 N4+4ǫ

.

![image 94](<2011-bateman-new-bounds-cap-sets_images/imageFile94.png>)

Crudely expanding the sum, we get the apparently weaker inequality

We can rewrite this as

y∈F3N

|

(1Hx(y) −

x∈∆

1 3

)|4

![image 95](<2011-bateman-new-bounds-cap-sets_images/imageFile95.png>)

|A||∆|4 N4+4ǫ

.

![image 96](<2011-bateman-new-bounds-cap-sets_images/imageFile96.png>)

Π4α=1(1Hxα(y) −

y∈F3N x1,x2,x3,x4∈F3N

) |A||∆|4 N4+4ǫ

1 3

. (4.1)

![image 97](<2011-bateman-new-bounds-cap-sets_images/imageFile97.png>)

![image 98](<2011-bateman-new-bounds-cap-sets_images/imageFile98.png>)

We claim the estimate 4.1 says that the spectrum ∆ has substantial additive structure. This will be demonstrated by the following proposition.

- Proposition 4.2. Let x1,x2,x3, and x4 be non-zero elements of F3N. Then the expression


Π4α=1(1Hxα(y) −

y∈F3N

1 3

) 3N

![image 99](<2011-bateman-new-bounds-cap-sets_images/imageFile99.png>)

Moreover it vanishes unless an equality of the form ±x1 ± x2 ± x3 ± x4 = 0

holds. Proof. We introduce the Fourier transforms of the balanced function of the hyperplanes Hxα setting

1 3N

1 3

fα(z) =

)e(y · z).

(1Hxα(y) −

![image 100](<2011-bateman-new-bounds-cap-sets_images/imageFile100.png>)

![image 101](<2011-bateman-new-bounds-cap-sets_images/imageFile101.png>)

x∈F3N

Then we use the standard Fourier identity

1 3

Π4α=1(1Hxα(y) −

![image 102](<2011-bateman-new-bounds-cap-sets_images/imageFile102.png>)

y∈F3N

) = 3N

f1(z1)f2(z2)f3(z3)f4(z4).

z1+z2+z3+z4=0

We observe that fj(zj) vanishes unless zj = ±xj. The upper bound on the sum just follows from the triangle inequality.

![image 103](<2011-bateman-new-bounds-cap-sets_images/imageFile103.png>)

![image 104](<2011-bateman-new-bounds-cap-sets_images/imageFile104.png>)

![image 105](<2011-bateman-new-bounds-cap-sets_images/imageFile105.png>)

![image 106](<2011-bateman-new-bounds-cap-sets_images/imageFile106.png>)

To ﬁnish the proof of Proposition 4.1, we apply the inequality 4.1, the fact that |A| >>

3N

N1+ǫ, the proposition 4.2 and the fact that the spectrum ∆ is symmetric.

![image 107](<2011-bateman-new-bounds-cap-sets_images/imageFile107.png>)

# 5 Random selection argument for additively smoothing spectrum

In this section we study the additive properties of random subsets of the spectrum. We will show that they typically have very poor additive structure. This will allow us to conclude that, although the spectrum has many 4-tuples, it cannot have too many 8-tuples. The signiﬁcance of this will only be made clear in Section 6.

We deﬁned E4(∆) to be the number of additive quadruplets in ∆. We deﬁne E2m(∆) to be the number of additive 2m-tuples

x1 + x2 + ... xm = xm+1 + xm+2 + ... x2m, such that x1,x2,... ,x2m ∈ ∆. We let ∆(x) be the Fourier transform: ∆(y) =

1 3N x∈∆

e(y · x).

![image 108](<2011-bateman-new-bounds-cap-sets_images/imageFile108.png>)

Then

|∆(ˆ y)|2m,

E2m(∆) = 3(2m−1)N

y∈F3N

which can be sen by expanding the sum on the right, as in the proof of Plancherel’s theorem. We always have E2(∆) = |∆|. When we have nontrivial amounts of additive structure in the sense that say E2k(∆) >> |∆|k, we can lift this up to counts of higher-tuplets using H¨older’s inequality. (We use the inequality to bound the 2k-norm by the 2-norm and the 2m-norm.) We can view this process as a poor man’s Plunnecke theorem. We record this result for high E4 and high E8.

- Lemma 5.1. Let m > 2. Then


Suppose m > 3. Then

E4(∆)m−1 |∆|m−2

≤ E2m(∆).

![image 109](<2011-bateman-new-bounds-cap-sets_images/imageFile109.png>)

E8(∆)m3−1 |∆|m3−4

![image 110](<2011-bateman-new-bounds-cap-sets_images/imageFile110.png>)

≤ E2m(∆).

![image 111](<2011-bateman-new-bounds-cap-sets_images/imageFile111.png>)

![image 112](<2011-bateman-new-bounds-cap-sets_images/imageFile112.png>)

## 5.1 Discussion of additive smoothing

We are now ready to introduce the notion of additive smoothing. We keep in mind two examples of kinds of sets having additive structure. One kind of set consists of a subspace plus a random set. The other consists of a random subset of a subspace. We think of the ﬁrst kind of set as not being additively smoothing because as you add it to itself, its expansion rate stays essentially constant. This is the kind of example for which Lemma 5.1 is close to sharp. But the second kind of set, when added to itself, will quickly ﬁll out the subspace and its rate of additive expansion will shrink dramatically. The lack of additive structure smooths out under addition. This is the kind of example for which Lemma 5.1 is far from sharp.

We will momentarily deﬁne ∆ to be additively smoothing if E8(∆) is substantially larger than expected from Lemma 5.1 and our lower bound for E4(∆) obtained in Section 4. (Nonetheless, for the purposes of this paper, the gain in the exponent need only be O(ǫ).) We will deﬁne additive smoothing so that if ∆ is additively smoothing then for some not very large m (depending only on ǫ), we may expect to ﬁnd additive m-tuplets of ∆ in a randomly chosen set S of d elements.

Before we formally deﬁne the property of additive smoothing, we illustrate how the calculation works in the case ǫ = 0. In that case d ∼ N so that an element of ∆ (which has size N3) is chosen with probability N−2. We have a lower bound of N7 on E4(∆). Suppose

that we can improve on the lower bound of N15 for E8(∆) which we get from the ﬁrst part of Lemma 5.1 and in fact

E8(∆) > N15+δ for some δ > 0. Then from the second part of Lemma 5.1, we obtain the estimate

N(4+3δ)m+7−δ3 ≤ E2m(∆). Thus there is some m which depends only on δ so that

![image 113](<2011-bateman-new-bounds-cap-sets_images/imageFile113.png>)

![image 114](<2011-bateman-new-bounds-cap-sets_images/imageFile114.png>)

E2m(∆) >> N4m.

Thus the expected number of 2m-tuplets in S is >> 1. We will formally deﬁne additive smoothing to achieve the same eﬀect when ǫ is diﬀerent from 0.

## 5.2 Nonsmoothing of the spectrum

In this subsection we make rigorous the arguments of the last subsection.

- Deﬁnition 5.2. We deﬁne ∆ to be additively smoothing if there is some σ > 30ǫ so that E8(∆) >> N15+σ.


We are now in a position to state the main result of this section. Lemma 5.3. If ∆ is the spectrum of a large cap set without strong increments then ∆ is not additively smoothing.

We begin with a few comments about our proof strategy in this section. If S is a “random” subset of ∆, then we expect

2m

E2m(S) = |S| |∆|

E2m(∆).

![image 115](<2011-bateman-new-bounds-cap-sets_images/imageFile115.png>)

Thus we can show that E2m(∆) is small by showing that ES is small for a typical (somewhat large) subset S of ∆.

Now we ﬁx a particular number d and consider random subsets of ∆ of size d. We will take

d ∼ N1−ǫ (5.1)

with the explicit constant to be determined later. Our ﬁrst goal is to prove that we expect this subset to span a space of dimension d. More precisely:

- Deﬁnition 5.4. Let S be a set of d vectors x1,... ,xd ∈ F3N. We say that the set S has nullity k if the dimension of the span of S is d − k.


We will consider uniform random selections of sets of d elements from ∆. We can view these selections as d-fold repetitions of uniform selection without replacement. We will prove

- Lemma 5.5. A random selection S of size d from the spectrum ∆ has nullity at least k with probability 2−k.

Proof. Once we have completed our ﬁrst m choices, our selections x1,... ,xm span a vector space Wm with dimension no more than m. Thus |∆∩Wm| mN1+2ǫ by Proposition 3.3. We choose the constant in 5.1 so that the probability that the m + 1st element of S lies in Wm is bounded by d1 for all m ≤ d − 1. Note that since m ≤ d, this probability is bounded by

![image 116](<2011-bateman-new-bounds-cap-sets_images/imageFile116.png>)

|∆ ∩ Wm| |∆|

![image 117](<2011-bateman-new-bounds-cap-sets_images/imageFile117.png>)

≤

CdN1+2ǫ N3

![image 118](<2011-bateman-new-bounds-cap-sets_images/imageFile118.png>)

=

Cd N2−2ǫ ≤

![image 119](<2011-bateman-new-bounds-cap-sets_images/imageFile119.png>)

1 d

![image 120](<2011-bateman-new-bounds-cap-sets_images/imageFile120.png>)

provided d << N1−ǫ. Thus the probability that S has nullity at least k is bounded by the probability that for d independent events with probability d1 at least k occur. The probability that exactly k events from d independent events with probability d1 occur is exactly

![image 121](<2011-bateman-new-bounds-cap-sets_images/imageFile121.png>)

![image 122](<2011-bateman-new-bounds-cap-sets_images/imageFile122.png>)

g(k,d) =

d k

(d − 1)d−k dd

![image 123](<2011-bateman-new-bounds-cap-sets_images/imageFile123.png>)

.

The numbers g(k,d) decrease by a factor of more than 2 as k is increased by 1 as long as k > 2. This completes the proof of the lemma.

![image 124](<2011-bateman-new-bounds-cap-sets_images/imageFile124.png>)

![image 125](<2011-bateman-new-bounds-cap-sets_images/imageFile125.png>)

![image 126](<2011-bateman-new-bounds-cap-sets_images/imageFile126.png>)

![image 127](<2011-bateman-new-bounds-cap-sets_images/imageFile127.png>)

Now that we know our random subset is likely to have full rank, we estimate the number of 2m-tuples it contains in the case it does not have full rank. Given a set S with nullity k we will bound the number of possible additive 2m-tuplets between elements of S. Speciﬁcally:

- Lemma 5.6. A set S of size d and nullity k has E2m(S) Cmk2m.


Proof. We write a list E of all equations among elements of S which involve 2m or fewer elements of S. Because the nullity is k, the span of these equations has dimension at most k. We pick a basis B for E and the equations in B involve at most 2mk elements of S. Thus all of the equations of E involve at most 2mk elements of S. Thus there are at most

h(m,k) = 2m(2m)!

2mk 2m

,

additive 2m-tuplets from S. We refer to h(m,k) as the number of possible m-tuplets in S. Note that h(m,k) is a polynomial of degree 2m in k.

![image 128](<2011-bateman-new-bounds-cap-sets_images/imageFile128.png>)

![image 129](<2011-bateman-new-bounds-cap-sets_images/imageFile129.png>)

![image 130](<2011-bateman-new-bounds-cap-sets_images/imageFile130.png>)

![image 131](<2011-bateman-new-bounds-cap-sets_images/imageFile131.png>)

Proof of Lemma 5.3 . Now let S be a random selection of d elements from ∆. Then by

- Lemma 5.5, the probability that S has nullity k is 2−k. Thus the expected value of the number of possible 2m-tuples k≥0 h(m,k) is m k≥0 2−kk2m 1.


Now we will show that we have deﬁned additive smoothing so that the expected number of 2m-tuples is >> 1. This will give us a contradiction.

We know that d N1−ǫ. Thus our selection S will be expected to have >> 1 non-trivial 2m-tuples, whenever E2m(∆) >> N4m+2mǫ. (We simply calculate the probability that an individual 2m-tuple involves only elements of S.) Thus we may assume that

E2m(∆) N4m+8mǫ.

Using the fact that |∆| N3+3ǫ and the second part of Lemma 5.1, we get that E8(∆) N

15m+27mǫ−1−ǫ

m−1 . Choosing m suﬃciently large gives

![image 132](<2011-bateman-new-bounds-cap-sets_images/imageFile132.png>)

E8(∆) N15+27ǫ. The choice of m and hence the constants depend on ǫ but not on N.

![image 133](<2011-bateman-new-bounds-cap-sets_images/imageFile133.png>)

![image 134](<2011-bateman-new-bounds-cap-sets_images/imageFile134.png>)

![image 135](<2011-bateman-new-bounds-cap-sets_images/imageFile135.png>)

![image 136](<2011-bateman-new-bounds-cap-sets_images/imageFile136.png>)

# 6 Structure of robust additively non-smoothing sets

In this section, the only properties of the spectrum ∆ which we shall use are its size, its additive structure, and its non-additive smoothing. Consequently the results can be stated in somewhat more generality. We leave intact, however, the numerology coming from the case of spectrum of cap sets.

We will say that a symmetric set ∆ ⊂ F3N is a robust additively non-smoothing set of strength δ provided that we know its size:

N3 |∆| N3+δ (6.1) that we know how many additive quadruples can be made from any large subset of it, namely that if ∆′ ⊂ ∆ with |∆′| ≥ 53|∆| and ∆′ symmetric, we have

![image 137](<2011-bateman-new-bounds-cap-sets_images/imageFile137.png>)

E4(∆′) N7−δ (6.2) and that we have additive non-smoothing, namely

E8(∆) N15+δ (6.3)

and moreover that for each element a ∈ ∆, there are at most N4+δ quadruples of the form

±a ± b = ±c ± d

with b,c,d ∈ ∆. Let us pause to consider the case of ∆, the spectrum of a cap set with no strong increments. We know that the number of a ∈ ∆ participating in more than N4+O(ǫ) quadruplets

±a ± b = ±c ± d

is smaller than 101 |∆| since otherwise ∆ would have more quadruples and hence more octuples than allowed by Lemma 5.3. Let ∆′ be the remaining elements of ∆. Note that

![image 138](<2011-bateman-new-bounds-cap-sets_images/imageFile138.png>)

by its deﬁnition ∆′ is still symmetric. Note that any symmetric subset of ∆′ containing at least three ﬁfths of its elements must contain at least half the elements of ∆. Thus from

- Proposition 3.2, Proposition 4.1, and Lemma 5.3 we know that: Proposition 6.1. Let ∆ be the spectrum of a large capset with no strong increments. There is a subset ∆′ of ∆ so that ∆′ is a robust additively non-smoothing set of strength O(ǫ).


Returning to the setting of robust additively non-smoothing sets, we let, for the remainder of the section, the set ∆ be a robust additively non-smoothing set of strength δ.

Given a value x ∈ ∆ − ∆, we deﬁne m(x) to be the number of pairs (a,b) ∈ ∆ × ∆ so that a − b = x. Clearly we have

m(x)2.

E4(∆) =

x∈∆−∆

Given a robust additively non-smoothing set ∆ of strength δ, for each α, we may deﬁne Gα ⊂ ∆ × ∆, by

Gα = {(a,b) ∈ ∆ × ∆ : N1+α ≤ m(a,b) < 2N1+α}. By the dyadic pigeonhole principle, there is an α so that

|Gα|

N6−α−δ log N

.

![image 139](<2011-bateman-new-bounds-cap-sets_images/imageFile139.png>)

Moreover, we know that no a in ∆ participates in more that N4+δ quadruples. Thus no element a in ∆ participates in more than N3−α+δ pairs in Gα. Thus there are at least ∼ Nlog3−N2δ elements of ∆ each of which participate in at least ∼ N3log−αN−2δ pairs in Gα, by the large families principle (Lemma 2.3).

![image 140](<2011-bateman-new-bounds-cap-sets_images/imageFile140.png>)

![image 141](<2011-bateman-new-bounds-cap-sets_images/imageFile141.png>)

We now forget about optimizing our exponents and consolidate this information in a single deﬁnition.

- Deﬁnition 6.2. We say that (∆,G,D) is an additive structure at height α with ambiguity η if the following hold. We have


|∆| ≤ N3+η. We have

G ⊂ ∆ × ∆

with the property that for each (a,b) ∈ G we have that a − b ∈ D, and so that each d ∈ D has ∼ N1+α representations as a diﬀerence of a pair in G. We have |G| ∼ N6−α−η. Moreover there are at least N3−η elements of ∆ participating in at least N3−α−η sums each. Finally there are no more than N15+η additive octuples among elements of ∆.

We summarize what we have shown so far in a proposition.

Proposition 6.3. Given a robust additively non-smoothing set ∆ of strength δ we may ﬁnd G ⊂ ∆ × ∆, and D ⊂ ∆ − ∆ and α ≥ 0 so that (∆,G,D) is an additive structure at height α and ambiguity O(δ).

We now describe a slightly deeper property of additive structures at height α and ambiguity η. Given a structure (∆,G,D), for each x ∈ D, we deﬁne the set ∆G[x] to be the set of a ∈ ∆ so that there exists b ∈ ∆ with (a,b) ∈ G and a − b = x. In light of our deﬁnitions, we have for each x ∈ D that |∆G[x]| ∼ N1+α. We consider the quantity

K(∆,G,D) =

|∆G[x] ∩ ∆G[y]|. (6.4)

x∈D y∈D

Clearly K(∆,G,D) counts the number of triples (a,x,y) with a ∈ ∆G[x] and a ∈ ∆G[y]. Each element in a is contained in exactly as many sets ∆G[x] as it participates (in the ﬁrst position) in pairs in G. Thus we conclude that for (∆,G,D) an additive structure with height α and ambiguity η that

K(∆,G,D) =

|{x ∈ D: a ∈ ∆G[x]}|2 N9−2α−3η.

a∈∆

Now examining the equation (6.4) and dyadically pigeonholing, we observe that we can ﬁnd β so that there are at least N9−2α−β−4η pairs (x,y) so that for each such pair, we have Nβ ≤ |∆G[x] ∩ ∆G[y]| < 2Nβ.

- Deﬁnition 6.4. We say that the additive structure (∆,G,D) at height α and with ambiguity η has comity µ if we can ﬁnd the abovementioned β with β > 1 + α − µ. (Note that of course β ≤ 1 + α because |∆G[x] ∩ ∆G[y]| ≤ |∆G[x]| N1+α.)


- Lemma 6.5. Given an additive structure (∆,G,D) at height α and with ambiguity η either it has comity µ or there is an additive structure (∆,G′,D′) with height β − 1 < α − µ and ambiguity O(η).


We remark that this lemma contains the key use of the nonsmoothing hypothesis, which is hidden in the deﬁnition of “additive structure”.

Proof. We dyadically pigeonhole the equation (6.4) to ﬁnd β so that there is a set of at least N9−2α−β−4η pairs (x,y) so that for each such pair, we have Nβ ≤ |∆G[x] ∩ ∆G[y]| < 2Nβ. If it happens that β−1 > α−µ, then we are done. Otherwise, we will construct an additive structure at height β − 1.

Now any time that a ∈ ∆G[x]∩∆G[y], this means that we can write x = a−b and y = a−c. Thus we have x−y = c−b. We have between Nβ and 2Nβ representations of the diﬀerence x − y. It remains to determine how many such diﬀerences there are.

We have two distinct upper bounds on the number of such diﬀerences. First there are

N6−β+2η, since each diﬀerence is represented by ∼ Nβ pairs in ∆ × ∆ and there are only N6+2η such pairs. The second estimate is that there are N7−2β+O(η) many such diﬀerences, because otherwise E4(∆) would be much larger than N7 which would make E8(∆) larger than N15+η. The ﬁrst upper bound is most eﬀective (ignoring ambiguity) when β < 1 while the second is most eﬀective when β > 1. Our plan (modulo ambiguity) is that we shall rule out the case β < 1 and that we shall show that the second upper bound is tight up to a factor of NO(η). Both estimates will follow from the upper bound on E8(∆) and the Cauchy-Schwarz inequality, namely Lemma 2.1.

Since we have N9−2α−β−O(η) pairs (x,y) with at most N6−β+O(η) diﬀerences, by the Cauchy-Schwarz inequality, there must be at least N12−4α−β−O(η) additive quadruples in D, namely x − y = x′ − y′. (Here we let S be the set of pairs (x,y), we let T be the set of diﬀerences with ∼ Nβ representations as diﬀerence of ∆ and we let ρ be the diﬀerence map, ρ(x,y) = x − y. Then we can apply Lemma 2.1.) However since each diﬀerence x,y can be represented in N1+α ways as a diﬀerence in ∆, we can represent each quadruple in D as an octuple in ∆ in N4+4α ways. Thus there are at least N16−β−O(η) many such octuples which implies β ≥ 1 − O(η).

Thus we are in the regime where the estimate that there are at most N7−2β+O(η) many diﬀerences is most eﬀective. Suppose that there were only N7−2β−γ many such diﬀerences with γ >> η Then apply Cauchy-Schwarz again, we would see that there are at least N11−4α−O(η)+γ many quadruples in D which implies N15−O(η)+γ octuples in ∆, a contradiction with the nonsmoothing hypothesis in the deﬁnition of “additive structure”.

Thus taking D′ to be the diﬀerences x − y obtained from (x,y) so that Nβ ≤ |∆[x] ∩ ∆[y]| < 2Nβ and taking G′ to consist of representatives of these diﬀerences coming from the intersections (as in the second paragraph of this proof), we obtain an additive structure (∆,G′,D′) with height β − 1 < α − µ and ambiguity O(η).

![image 142](<2011-bateman-new-bounds-cap-sets_images/imageFile142.png>)

![image 143](<2011-bateman-new-bounds-cap-sets_images/imageFile143.png>)

![image 144](<2011-bateman-new-bounds-cap-sets_images/imageFile144.png>)

![image 145](<2011-bateman-new-bounds-cap-sets_images/imageFile145.png>)

Corollary 6.6. Given an additive structure (∆,G,D) at height α and with ambiguity η there is an additve structure (∆,G,D) at height α′ ≤ α with ambiguity µ and comity µ

with µ log 1 1

.

![image 146](<2011-bateman-new-bounds-cap-sets_images/imageFile146.png>)

![image 147](<2011-bateman-new-bounds-cap-sets_images/imageFile147.png>)

η

Proof. We iteratively apply Lemma 6.5 with comity µ ﬁxed by

K log η1

µ =

![image 148](<2011-bateman-new-bounds-cap-sets_images/imageFile148.png>)

![image 149](<2011-bateman-new-bounds-cap-sets_images/imageFile149.png>)

with K a large constant, and with the ambiguity increasing by a constant factor C in each iteration. Since α decreases by µ each time we don’t ﬁnd comity we need only ∼ µ1 iterations to achieve comity. At this point, we have ambiguity given by C

![image 150](<2011-bateman-new-bounds-cap-sets_images/imageFile150.png>)

log( 1

η )

![image 151](<2011-bateman-new-bounds-cap-sets_images/imageFile151.png>)

K η << µ, as long as K was chosen suﬃciently large.

![image 152](<2011-bateman-new-bounds-cap-sets_images/imageFile152.png>)

![image 153](<2011-bateman-new-bounds-cap-sets_images/imageFile153.png>)

![image 154](<2011-bateman-new-bounds-cap-sets_images/imageFile154.png>)

![image 155](<2011-bateman-new-bounds-cap-sets_images/imageFile155.png>)

![image 156](<2011-bateman-new-bounds-cap-sets_images/imageFile156.png>)

Now we begin to investigate what we can say about the shape of the set H of all pairs (b,c) in ∆×∆ having the property that b−c has at least N1+α−O(µ) representations in ∆×∆ for (∆,G,D) an additive structure with height α and ambiguity and comity µ. We will ﬁnd that the set H is rather thick in a product set whose projection has size N3−α−O(µ).

- Lemma 6.7. Let (∆,G,D) be an additive structure with height α and ambiguity and comity µ. Then there is a subset B ⊂ ∆ with |B| N3−α−O(µ) so that there is a set H ⊂ B × B with


|H| N−O(µ)|B|2, so that for any (b,c) ∈ H, the diﬀerence b − c has N1+α−O(µ) representations in ∆ × ∆. Proof. From the hypotheses, we have that

|∆G[x] ∩ ∆G[y]| N9−2α−O(µ),

x∈D y∈D

and that there are at least N8−3α−O(µ) pairs (x,y) for which |∆G[x] ∩ ∆G[y]| N1+α−O(µ).

Using the pigeonhole principle, we ﬁx one value of x for which there are N3−α−O(µ) choices of y so that

|∆G[x] ∩ ∆G[y]| N1+α−O(µ).

Again using the pigeonhole principle, we ﬁnd an a ∈ ∆ and a set Y ⊂ D so that a ∈ ∆G[y] for every for every y ∈ Y , so that |Y | = N3−α−O(µ) and so that for each y ∈ Y , we have

|∆G[x] ∩ ∆G[y]| N1+α−O(µ).

We notice that by deﬁnition a − Y ⊂ ∆. We choose B = a − Y Finally since each ∆G[y] has relative density N−O(µ) in ∆G[x], we have by Cauchy-Schwarz (Lemma 2.2) that

|∆G[y] ∩ ∆G[y′]| |Y |2N1+α−O(µ).

y∈Y y′∈Y

This implies that B satisﬁes the conclusion of the lemma. The reason is that by Lemma

- 2.3, we have a set Y˜ of pairs y,y′ so that |∆[y] ∩ ∆[y′]| N1+α−O(µ). This implies that a − y′ − (a − y) = y − y′ has at least N1+α−O(µ) representatives as a diﬀerence of two elements of ∆.


![image 157](<2011-bateman-new-bounds-cap-sets_images/imageFile157.png>)

![image 158](<2011-bateman-new-bounds-cap-sets_images/imageFile158.png>)

![image 159](<2011-bateman-new-bounds-cap-sets_images/imageFile159.png>)

![image 160](<2011-bateman-new-bounds-cap-sets_images/imageFile160.png>)

Now we are going to use Lemma 6.7 repeatedly to show that for any robust additively non-smoothing set of size δ we can ﬁnd an additive structure of ambiguity η with η log 1 1

![image 161](<2011-bateman-new-bounds-cap-sets_images/imageFile161.png>)

![image 162](<2011-bateman-new-bounds-cap-sets_images/imageFile162.png>)

δ

which breaks into dense blocks.

- Lemma 6.8. Let ∆ be a robust additively non-smoothing set of strength δ. Choose µ ∼


- 1


log δ1 . Then for some 0 ≤ α ≤ 1, there is an additive structure (∆,G,D) of height α and ambiguity µ and disjoint subsets B1,... BK of ∆ with each Bj satisfying |Bj| N3−α+O(µ) so that

![image 163](<2011-bateman-new-bounds-cap-sets_images/imageFile163.png>)

![image 164](<2011-bateman-new-bounds-cap-sets_images/imageFile164.png>)

K

Bj × Bj.

G ⊂

j=1

Note that since we are requiring that (∆,G,D) be an additive structure, this requires |G| N6−α−O(µ) which implies K Nα−O(µ).

Proof. Using Proposition 6.3 , Corollary 6.6, and Lemma 6.7. We can ﬁnd a subset B1 of ∆ so that for some choice of α, it has size at most N3−α+O(µ) and nevertheless B1 × B1 contains at least N6−2α−O(µ) pairs whose diﬀerences have N1+α−O(µ) representations as diﬀerences in ∆.

Having done this, we use the robustness property of ∆ to apply the same argument to ∆\(B1 ∪−B1). We continue removing sets from ∆ until we have exhausted half of ∆. Now one diﬃculty is that the disjoint sets B which we chose do not all have the same α. We use dyadic pigeonholing to resolve this for only a small cost in the number of sets. We call these sets B1,... ,BK. Now Lemma 6.7 guarantees us in each Bj × Bj, a subset Hj of cardinality at least N6−2α−O(µ) so that each diﬀerence in Hj is represented in ∆ × ∆ at least N1+α−O(µ) times. We denote by Dα the set of diﬀerences represented in ∆ × ∆ at least N1+α−O(µ) times, and note that

|Dα| N5−2α+O(µ),

lest there be enough quadruples in ∆ to violate the additive non-smoothing condition. Using the large families principle and pigeonholing, we ﬁnd some α′ α − O(µ) so that

at least N5−2α−O(µ) diﬀerences are represented at least N1+α′ many times in ∪jHj. We denote this set of diﬀerences as Dα′ . We let D be Dα′ and let G be a subset of ∪jHj consisting of N1+α′ representatives of each diﬀerence in D.

![image 165](<2011-bateman-new-bounds-cap-sets_images/imageFile165.png>)

![image 166](<2011-bateman-new-bounds-cap-sets_images/imageFile166.png>)

![image 167](<2011-bateman-new-bounds-cap-sets_images/imageFile167.png>)

![image 168](<2011-bateman-new-bounds-cap-sets_images/imageFile168.png>)

Our goal now will be to use will be to use Lemma 6.8 to ﬁnd almost additively closed sets E of size at least N1−f(δ) inside robust non-additively smoothing sets of strength δ. Here f : [0,1] −→ [0,∞) is some function with limt−→0 f(t) = 0. We will be employing such functions from now on in the paper. They, like constants, will change from line to line.

The project of ﬁnding additively closed sets will be easiest when we have additive structures of height essentially zero having ambiguity and comity µ. For this reason, we are about to deﬁne a stylized structure which generalizes this situation. We will eventually use the generalized version, replacing ∆ with the blocks Bj.

We will now deﬁne a µ-full stylized ρ-structure which is τ-energetic and has ambiguity and comity µ. (The error exponents µ are all the same.) This will be a set (∆′,G,D) where

|∆′| ∼ Nρ, (hence a ρ-structure) where G ⊂ ∆′ × ∆′ with

|G| > N2ρ−O(µ),

(this was the µ-fullness), where D is the set of diﬀerences in pairs in G and each diﬀerence represented Nτ and Nτ+O(µ) times, hence τ-energetic. Finally we assume that there are at least N3ρ−τ−O(µ) pairs (x,y) ∈ D × D so that

|∆′[x] ∩ ∆′[y]| Nτ−O(µ),

which is of course the µ-comity. We shall say that a set K is µ-additively closed provided that

|K − K| NO(µ)|K|, as in Section 2.

- Lemma 6.9. There is a function f : [0,1] −→ [0,∞) with


lim

f(t) = 0,

t−→0

so that the following holds. Let (∆′,G,D) be a µ-full stylized ρ-structure which is τenergetic and has ambiguity and comity µ. Then there is an f(µ) additively closed set K with

|K| Nτ−f(µ)

and a set X so that

|X| Nf(µ) |∆′| |K|

, so that

![image 169](<2011-bateman-new-bounds-cap-sets_images/imageFile169.png>)

|∆′ ∩ (X + K)| Nρ−f(µ).

Proof. We proceed essentially as in the proof of Lemma 6.7. We ﬁnd x ∈ D so that there is a set Y of y ∈ D with |Y | Nρ−O(µ) so that

|∆′G[x] ∩ ∆′G[y]| Nτ−O(µ),

for every y ∈ Y . As before, we use the pigeonhole principle to ﬁnd a ∈ ∆′ so that there is a subset Ya of Y so that for each y ∈ Ya, we have

a ∈ ∆′G[y] and so that

|Ya| Nρ−O(µ).

However Ya ⊂ a − ∆′. Thus we think of Ya as a dense part of a translate of −∆′. Now we know that

|∆′G[x] ∩ ∆′G[y]| Nρ+τ−O(µ).

y∈Ya

This precisely means that there are Nρ+τ−O(µ) triples (b,c,d) with b,c ∈ ∆′ and d ∈ ∆′[x] with a − b = d − c with a still ﬁxed. Applying Cauchy-Schwarz (see Lemma 2.1) we ﬁnd Nρ+2τ−O(µ) quadruples (d,c,d′,c′) with d,d′ ∈ ∆′[x] and c,c′ ∈ ∆′. As it happens, this is precisely the hypothesis of the asymmetric Balog-Szemeredi-Gowers theorem (Theorem

- 2.4) applied to ∆′ and ∆G[x]. The conclusion follows directly.


![image 170](<2011-bateman-new-bounds-cap-sets_images/imageFile170.png>)

![image 171](<2011-bateman-new-bounds-cap-sets_images/imageFile171.png>)

![image 172](<2011-bateman-new-bounds-cap-sets_images/imageFile172.png>)

![image 173](<2011-bateman-new-bounds-cap-sets_images/imageFile173.png>)

We are now prepared to state the main result of this section.

- Theorem 6.10. Let ∆ be a robust additively non-smoothing set of strength δ. As before


choose µ ∼ log1 1

. There is f : [0,1] −→ [0,∞) with

![image 174](<2011-bateman-new-bounds-cap-sets_images/imageFile174.png>)

![image 175](<2011-bateman-new-bounds-cap-sets_images/imageFile175.png>)

δ

lim

f(t) = 0,

t−→0

so that for some γ ≥ 0, there is an f(µ)-additively closed set K with |K| N1+γ−f(µ),

contained in ∆. In the event that we must have γ = O(f(µ)), for some 0 ≤ α ≤ 1 , we may ﬁnd pairwise disjoint subsets B1,... ,BM ⊂ ∆ with M Nα−O(µ) so that for each integer 1 ≤ j ≤ m, we have

N3−α−O(µ) |Bj| N3−α+O(µ), and moreover we ﬁnd for each j a µ-additively closed set Kj with

N1−f(µ) |Kj| N1+f(µ), together with a set Xj with

N2−α−f(µ) |Xj| N2−α+f(µ), so that

|Bj ∩ (Xj + Kj)| N3−α−f(µ). Further, there is a set D with |D| N5−2α−f(µ) so that each element of D has at least N1+α−f(µ) representations as a diﬀerence of elements of ∆ and so that for each j, the set of 4-tuples Qj = {(k1,d1,k2,d2) : k1,k2 ∈ Kj,d1,d2 ∈ D : k1 − d1 = k2 − d2} satisﬁes

|Qj| N7−2α−f(µ).

Moreover we may choose Kj to be contained in the set of diﬀerences having at least N5−2α−f(µ) representations as a diﬀerence between elements of D.

Proof. We apply Lemma 6.8 and restrict our attention to

K

Bj × Bj

G ⊂

j=1

where the Bj are the blocks obtained there. Now to G, we apply the argument used in the proof of Lemma 6.5.

That is, for any element x ∈ −(G), we study

∆G[x] = {a ∈ ∆ : ∃b ∈ ∆ : (a,b) ∈ G; a − b = x}. Here −(G) = {a − b: (a,b) ∈ G}. Then, we observe

|∆G[x] ∩ ∆G[y]| N9−2α−O(µ),

x,y∈−(G)

and we observe as before that there is some 1 + α ≥ β ≥ 1 − O(µ) so that there are at least N9−2α−β−O(µ) pairs (x,y) for which |∆G[x] ∩ ∆G[y]| Nβ. We note that when this

happens, for each a in the intersection ∆G[x] ∩ ∆G[y], we have x = a − b1 and y = a − b2. Here if a ∈ Bj, we must have b1 ∈ Bj and b2 ∈ Bj, since (a,b1),(a,b2) ∈ G. We argue

- as in the proof of Lemma 6.5, that there are at least N7−2β−O(µ) diﬀerences having Nβ


representations in

K

Bj × Bj.

j=1

If not, E8(∆) >> N15+δ. But

NβN7−2β−O(µ) ≤

K

Bj × Bj N6−α+O(µ),

j=1

which implies 7 − β ≤ 6 − α + O(µ), which implies 1 + α − O(µ) ≤ β. This gives us O(µ) comity for G.

Thus we have a set H of pairs x,y for which |∆G[x] ∩ ∆G[y]| N1+α−O(µ) and so that |H| N8−3α−O(µ). Now we use the pairwise disjointness of the blocks Bj to write the identity

K

|∆G[x] ∩ ∆G[y] ∩ Bj| N9−2α−O(µ) (6.5)

|∆G[x] ∩ ∆G[y]| =

j=1 (x,y)∈H

(x,y)∈H

Now we begin to use the comity of G. We ﬁrst eliminate from the second sum in equation

- 6.5 all terms for which the relative density of ∆G[x] in ∆G[y] ∩ Bj or the relative density of ∆G[y] in ∆G[x] ∩ Bj is smaller than N−Cµ for too large a constant C, again using the large families principle. By choosing C suﬃciently large we do not reduce the sum by a factor of more than 2. We dyadically pigeonhole to obtain the largest possible sum from those terms where N1+γ ≤ |∆G[x] ∩ ∆G[y] ∩ Bj| ≤ 2N1+γ. (We denote this set of (x,y) as Hγ,j), Thus we have reduced the sum by at most a factor of log N. We keep only those j for which


|∆G[x] ∩ ∆G[y] ∩ Bj| N9−3α−O(µ), (6.6)

(x,y)∈Hγ,j

which we can do without sacriﬁcing much by using again the large families principle.

We observe that for each x, there are at most N3−α+O(µ) choices of y so that (x,y) ∈ H. The reason is that any a ∈ ∆ belongs to at most N3−α+O(µ) sets ∆G[y] because G is contained in ∪jBj × Bj. However if there were more than N3−α+O(µ) choices of y so that (x,y) ∈ H then there would be elements a ∈ ∆G[x] which are contained in ∆G[y] for more than N3−α+O(µ) choices of y Thus, since we have at least N8−2α−γ−O(µ) triples (j,x,y) for which

|∆G[x] ∩ ∆G[y] ∩ Bj| N1+γ,

while at the same time

|∆G[x] ∩ Bj| N1+γ+O(µ),

(by the relative density of ∆G[y] in ∆G[x] ∩ Bj,) it must be that for most values of j, we have at least N8−3α−γ pairs (x,y) ∈ Hγ,j. This means, ﬁxing one such value of j (since at most N3−α+O(µ) values of y are paired with a given x) , there are at least N5−2α−γ−O(µ) diﬀerences x with N1+γ representations in G ∩ (Bj × Bj). We call this set Dj,γ.

Thus G ∩ (Bj × Bj) is µ-full and 1 + γ-energetic. Another way of describing the µ-fullness is that N5−2α−γ−O(µ) (up to NO(µ) factors) is the largest number of such x possible, purely based on the size of Bj ×Bj. Thus it must be that for a set of size N5−2α−γ−O(µ) many such x, there are N3−α−O(µ such y with (x,y) ∈ Hγ,j (yet again, by the large families principle). Thus (Bj,G ∩ (Bj × Bj),Dj,γ) has O(µ)-comity. Clearly (Bj,G ∩ (Bj × Bj),Dj,γ) is a

- 3 − α structure with ambiguity µ. Thus we are in a position to apply Lemma 6.9. This proves the ﬁrst part of the theorem. Indeed, since all our estimates were optimal up to NO(µ) factors, there is a set J of choices of j for which we could apply Lemma 6.9 with |J| Nα−O(µ).


To prove the second part, we consider in detail the case γ = 0. We will apply the argument proving Lemma 6.9 to all j ∈ J. This will give us µ-additive sets Kj and sets Xj with appropriate upper and lower bounds since we can assume ∆ contains no µ-additive sets with more than N1+f(µ) elements.

We will allow f to vary from line to line and we will express even quantities that are clearly O(µ) as f(µ).

We let D be the set of all diﬀerences x for which |∆[x]∩Bj| N1−f(µ) for at least Nα−f(µ) values of j ∈ J. For each value of j ∈ J , there are at least N8−3α−f(µ) pairs (x,y) ∈ D2 with |∆G[x] ∩ ∆G[y] ∩ Bj| N1−f(µ). Note that we may also restrict D to diﬀerences which cannot be represented in more than N1+f(µ) ways as diﬀerences of elements of Bj for more than Nα−f(µ) values in j and so that in each Bj our count of good pairs (x,y) consists only of pairs of diﬀerences which cannot be represent as diﬀerences in Bj in more than N1+f(µ) ways. Otherwise, we could choose γ > f(µ).

Now we recall the structure of the argument in Lemma 6.9. We chose an a ∈ Bj and a set Ba of size N3−α−f(µ) of the diﬀerences in which a participates, and a set Ka which is actually of the form ∆G[x]∩Bj and has size N1−f(µ). We ﬁnd N5−α−f(µ) additive quadruples made up of two elements of Ba and two elements of Ka. We may strip down Ka further to those elements which participate in at least N4−α−f(µ) of these quadruples and not harm our estimate on the number of quadruples between Ka and Ba. Now, we note that since Ba is a large subset of a translate of Bj, it must be that there are N2−f(µ) pairs (q1,q2) ∈ Ka2 with the property that q1 − q2 is represented N3−α−f(µ) times as a diﬀerence of elements of Bj. We let K1,j be the set of diﬀerences of Bj that can be represented in N3−α−f(µ) ways as diﬀerences in Bj. Because Bj contains no µ-additively closed set of size more

than N1+f(µ), we have that |K1,j| ≤ N1+f(µ). Otherwise we could apply the asymmetric Balog-Szemeredi-Gowers theorem, to obtain a µ-additively closed set, contained in Bj, as in the γ >> O(f(µ)) case.

We can replace N5−α−f(µ) quadruples q1 − q2 = x1 − x2 with q1,q2 ∈ K1,j and x1,x2 ∈ Ba by an equation of the form q = x1 −x2 with multiplicity at most N1+f(µ). Thus we obtain

- at least N4−α−f(µ) such equations. We rewrite the equation as x1 −q = x2 and use Cauchy


Schwarz to obtain N5−α−f(µ) quadruples x1 −q = x′1 −q′. We see then that without losing more than Nf(µ) factors in our estimates, we can replace Ka by K1,j. This is good since we have made it independent of the choice of a. Now we need only show that we can ﬁnd many quadruples not only between K1,j and Ba but between K1,j and D. This will give us the desired result.

To do this, we observe that we may delete from Ba a set with relative density N−f(µ) without harming our estimates on the number of quadruplets between Ba and K1,j. Our goal will be to cover a subset D′ by a disjoint union of subsets of the form Ba′ where Ba′ is a subset of Ba with relative density 1 − N−f(µ). To do this we observe that for any ﬁxed a1 ∈ Bj

|Ba1 ∩ Ba2| N4−α+f(µ).

a2

We can do this because the sum counts triples (x,a1,a2) with x a diﬀerence and a,a2 are parts of representations of it. We have assumed that we are only dealing with diﬀerences with fewer than N1+O(µ) representations. Here we are using that we are in the γ = 0 case,

Now we produce D′ as follows. We choose a1 and keep the set Ba1. We add all elements of Ba1 to D′ We choose Ba2 to have the minimal possible sized intersection with Ba1 and let Ba′2 be those elements in Ba2 that are not already in D′. We choose Ba3 to have minimal possible intersection with Ba1 ∪ Ba2. We continue in this way until we reach a k so that Ba′

no longer has relative density 1 − N−f(µ) in Bak. Because the average intersection |Ba ∩Ba′| is bounded by N1+f(µ), we get that k is at least N2−α−f(µ). Thus our set D′ has relative density at least N−f(µ) in D. Thus we have that K1,j has N7−2α−f(µ) quadruples with D′ and a fortiori with D.

k

Now we slightly reﬁne K1,j to K2,j consisting only to diﬀerences of elements of K1,j which participate in at least N5−α−f(µ) of the quadruples with D′. (We perform this reﬁnement in order to prove the very last claim of the theorem.) Since D′ is a disjoint union of sets with relative density N−f(µ) inside translates of Bj, it must be that K2,j still has N5−α−f(µ) quadruples with Bj. Thus we can apply the asymmetric Balog Szemeredi Gowers theorem to ﬁnd a subset Kj satisfying the conclusions of the theorem.

![image 176](<2011-bateman-new-bounds-cap-sets_images/imageFile176.png>)

![image 177](<2011-bateman-new-bounds-cap-sets_images/imageFile177.png>)

![image 178](<2011-bateman-new-bounds-cap-sets_images/imageFile178.png>)

![image 179](<2011-bateman-new-bounds-cap-sets_images/imageFile179.png>)

# 7 Structure of spectrum of large capsets with no strong increments

In this section, we transfer the results obtained in Theorem 6.10 over to the setting of the spectrum of large capsets with no strong increments. This turns out to be rather simple. The main ideas which we have not yet taken advantage of are Freiman’s theorem and the use of the estimate in Proposition 3.3 which bounds the number of elements of the spectrum in a subspace of dimension d by dN1+2ǫ.

We state the main result of the section.

- Theorem 7.1. Let ∆ be the spectrum of large capset without strong increments. There is a function f : [0,1] −→ [0,∞] with limt−→0 f(t) = 0 so that the following holds. There is a subspace H of F3N of dimension Nf(ǫ) and a set Λ ⊂ F3N of size N2−f(ǫ) so that for each element λ ∈ Λ, there is a subset Hλ ⊂ H with the properties that


|Hλ| N1−f(ǫ),

and the sets λ + Hλ are pairwise disjoint subsets of ∆. For any subspace W ⊂ F3N of dimension d, we have that W contains at most dNf(ǫ) elements of Λ.

Proof. As before we allow our function f to vary from line to line until we achieve the desired result.

In light of Theorem 2.5 and Proposition 3.3, any f(ǫ)-additively closed set in which the spectrum has N−f(ǫ) relative density, must be bounded in size by N1+f(ǫ). Therefore, we are in the γ = 0 case of Theorem 6.10. We know that there is a set ∆′ of density N−f(ǫ) in the spectrum ∆ which is contained in

M

Xj + Kj,

j=1

with M Nα−O(f(ǫ)), with each Kj an f(ǫ)-additively closed set (of size at least N1−f(ǫ) and at most N1+f(ǫ)) and with each set Xj of size N2−α±f(ǫ) . Moreover, each set Kj lies in the set K of diﬀerences having at least N5−2α−f(ǫ) representations as diﬀerences of elements of D, the diﬀerences among elements of the spectrum which have at least N1+α−f(ǫ) representations. In light of the non-additive smoothing property of ∆, we have that |K| N1+f(ǫ) since there can be at most N11−4α+f(ǫ) quadruplets among elements of D. We may eliminate all elements q of each Kj for which ∆ ∩ q + Xj does not have size at least N2−α−f(ǫ). Now we let K′ be the set of elements of K which appear in at least Nα−f(ǫ) many Kj. We can ﬁnd some Kj which has intersection of size N1−f(ǫ) with K′. Then K′ ∩ Kj = K′′ is a f(ǫ)-additively closed set with cardinality at least N1−f(ǫ). Moreover each element of K′′ is contained in Nα−f(ǫ) many Kj. Thus by pigeonholing

there are at least Nα−f(ǫ) many Kj so that |Kj ∩K′′| N1−f(ǫ). We only keep these j and replace Kj by Kj ∩ K′′. But by Theorem 2.5, we have that K′′ is contained in a subspace of dimension Nf(ǫ) which we call H.

This basically proves the ﬁrst part of the theorem. We have that a subset of the spectrum of density N−f(ǫ) is contained in K′′ + X, where X is the union of the Xj’s. We will pick Λ and the sets Hλ as follows: Find x1 in X so that at least N1−f(ǫ) elements of ∆ are contained in x1+K′′. Let ∆1 be the elements of ∆ contained in X+K′′ but not in x1+K′′. Let ∆1 be those elements of ∆ contained in x1 +K′′ and let Hx1 = ∆1 −x1. Note that Hx1 is contained in K′′ and therefore in H. Now we proceed iteratively. Find xj ∈ X so that there are at least N1−f(ǫ) elements of ∆j−1 in xj + K′′. When this is no longer possible, we terminate the process. Then we let ∆j be the elements of ∆j−1 not in xj + K′′ and we let ∆j be the ones that are. We let Hxj = ∆j − xj. We let Λ = {xj} after the iteration has terminated. Note that if

|(xj + K′′) ∩ ∆j−1| << N1−f(ǫ) for all remaining xj in X, then

j

(xi + K′′)| N3−f(ǫ),

|

i=1

so |Λ| N2−f(ǫ).

To prove the second part of the theorem, let S be any subset of Λ with some cardinality M. But S + H contains at least MN1−f(ǫ) elements of ∆. This contradicts Proposition

- 3.3 unless the span of S has dimension at least MNf(ǫ).


![image 180](<2011-bateman-new-bounds-cap-sets_images/imageFile180.png>)

![image 181](<2011-bateman-new-bounds-cap-sets_images/imageFile181.png>)

![image 182](<2011-bateman-new-bounds-cap-sets_images/imageFile182.png>)

![image 183](<2011-bateman-new-bounds-cap-sets_images/imageFile183.png>)

# 8 Contradiction

The goal of this section is to obtain a contradiction from the existence of large capsets without strong increments by using the result of Theorem 7.1. We begin by recording some easy consequences of Plancherel’s identity for the interaction between the Fourier transform of the characteristic function of a set and the Fourier transforms of its ﬁbers over a subspace.

For any set A ⊂ F3N, we deﬁne its Fourier transform Aˆ(x) =

1 3N a∈A

e(a · x).

![image 184](<2011-bateman-new-bounds-cap-sets_images/imageFile184.png>)

We state Plancherel’s identity:

- Proposition 8.1.

x∈F3N

|Aˆ(x)|2 = 3−N|A|.

We let H be a subspace of F3N and we let H⊥ be its annihilator. We let V be a subspace of the same dimension as H which is transverse to H⊥ i.e., V + H⊥ = F3N . We deﬁne the ﬁber AH,v for v ∈ V by

AH,v = A ∩ (H⊥ + v). If we have h ∈ H, then

Aˆ(h) = 3−N

v∈V

e(h · v)|AH,v|.

Thus we arrive at another form of Plancherel:

- Proposition 8.2.

h∈H

|Aˆ(h)|2 = |H|3−2N

v∈V

|AH,v|2.

Moreover

h =0∈H

|Aˆ(h)|2 = |H|3−2N

v∈V

(|AH,v| −

|A| |H|

![image 185](<2011-bateman-new-bounds-cap-sets_images/imageFile185.png>)

)2

Next, we consider the situation where we have a subspace H ⊂ F3N and a larger subspace K with H ⊂ K ⊂ F3N. We let V be a subspace transverse to H⊥ as before and we would like to consider the Fourier transforms of the ﬁbers of A, namely the sets AH,v. We can think of each ﬁber AH,v as being identiﬁed with a subset of H⊥ (by translation by v) and of course H⊥ can be identiﬁed with F3N/H. That is, we deﬁne functions AH,v : F3N/H −→ C by

AˆH,v(w) = |H| 3N a∈A

![image 186](<2011-bateman-new-bounds-cap-sets_images/imageFile186.png>)

H,v

e((a − v) · w).

The function AˆH,v(w) is well deﬁned on F3N\H since a − v is in H⊥. Next, we write down a version of Proposition 8.2 which shows how the L2 norms of the Fourier transforms of the ﬁbers on K\H with the L2 norm of the Fourier transform on K. We let W be a subspace transverse to K⊥ with V ⊂ W.

- Proposition 8.3. With H, K, V , and W as above,


1 |H| v∈V

|Aˆ(k)|2 =

|Aˆ(h)|2 +

![image 187](<2011-bateman-new-bounds-cap-sets_images/imageFile187.png>)

k =0∈K

h =0∈H

|AˆH,v(k)|2.

k =0∈K/H

Proof. Since clearly we have K⊥ ⊂ H⊥, there is a unique subspace W′ ⊂ W with W′ + K⊥ = H⊥. We have V + W′ = W.

We consider the following function on W,

|A| |K|

g(w) = |AK,w| −

.

![image 188](<2011-bateman-new-bounds-cap-sets_images/imageFile188.png>)

Clearly, in light of the second part of Proposition 8.2, the left hand side of the identity we are trying to prove is the normalized square of the L2 norm of the function g(w).

We now break up g as the sum of a function g0 which is constant on translates of W′ and functions gv with v running over V having mean zero and supported on the translate v + W′ of W′. Clearly the functions g0 and {gv} are pairwise orthogonal. The ﬁrst term on the right hand side of the identity is the normalized square L2 norm of the function g0. The second term on the right hand side represents the sum over v of the normalized square L2 norm of the functions gv. The identity is then an application of the Pythagorean theorem.

![image 189](<2011-bateman-new-bounds-cap-sets_images/imageFile189.png>)

![image 190](<2011-bateman-new-bounds-cap-sets_images/imageFile190.png>)

![image 191](<2011-bateman-new-bounds-cap-sets_images/imageFile191.png>)

![image 192](<2011-bateman-new-bounds-cap-sets_images/imageFile192.png>)

(We remark that Proposition 8.3 can simply be thought of as Plancherel for a “local Fourier transform” of A. Here, we localize to the translates of H⊥.

Now we are prepared to apply Proposition 8.3 to the setting in which A is large capset without strong increments and H is the subspace given to us by Theorem 7.1.

We let A be a large capset with no strong increments. As usual, f will be a function taking [0,1] to [0,∞] with limt−→0 f(t) = 0. We will vary f from line to line.

Then there is a subspace H with dimension Nf(ǫ) and a set Λ of size N2−f(ǫ) so that for each λ ∈ Λ there is a subset Hλ of H, so that |Hλ| > N1−f(ǫ) so that for each h ∈ Hλ, we have that

|Aˆ(h + λ)| N−1−f(ǫ)3−N|A|. We also have that the sets λ + Hλ are pairwise disjoint. Note therefore that

|Aˆ(h + λ)|2 N−f(ǫ)N3−2N|A|2 N−f(ǫ)3−N|A|.

λ∈Λ h∈Hλ

Thus the structured elements of the spectrum of A account for a large proportion of the squared L2 norm of the Fourier transform of A.

Now we would like to consider the ﬁbers AH,v, where H is the subspace we’ve been discussing. Because the capset A has no strong increments, we know that for each value v,

we have

|AH,v| ≤ ( |A| |H|

)(1 + Nf(ǫ)−1). We will now momentarily ﬁx the function f.

![image 193](<2011-bateman-new-bounds-cap-sets_images/imageFile193.png>)

However, we don’t have a good lower bound on |AH,v| in general. All we know is that sum of all the positive increments is equal to the sum of all the negative increments. (See the proof of Proposition 3.3.) We let Vbad be the set of all v ∈ V for which

√

|AH,v| ≤ ( |A| |H|

![image 194](<2011-bateman-new-bounds-cap-sets_images/imageFile194.png>)

)(1 − N2

f(ǫ)−1).

![image 195](<2011-bateman-new-bounds-cap-sets_images/imageFile195.png>)

(That is Vbad is the set of those v ∈ V for the which the ﬁber has a bad negative increment.) We know that

√

![image 196](<2011-bateman-new-bounds-cap-sets_images/imageFile196.png>)

f(ǫ)|V |. We deﬁne

|Vbad| N−

AH,v,

Abad =

v∈Vbad

and we let

A′ = A\Abad. We know that

√

![image 197](<2011-bateman-new-bounds-cap-sets_images/imageFile197.png>)

f(ǫ)|A|. Thus

|Abad| N−

√

![image 198](<2011-bateman-new-bounds-cap-sets_images/imageFile198.png>)

f(ǫ) 2

|Aˆ(h + λ)|2.

|Aˆbad(x)|2 N−

![image 199](<2011-bateman-new-bounds-cap-sets_images/imageFile199.png>)

x

λ∈Λ h∈Hλ

Thus removing Abad does not perturb the large spectrum of A too much.

(In making this precise, we now resume changing the function f from line to line, observing that we may take the next f to be larger than the previous √f.) We may ﬁnd a set Λ′ which is a subset of Λ with |Λ′| N2−f(ǫ) and so that for each λ ∈ Λ′ there is a subset Hλ′ of H so that for each λ ∈ Λ′ and each h ∈ Hλ′ we have

![image 200](<2011-bateman-new-bounds-cap-sets_images/imageFile200.png>)

|Aˆ′(h + λ)| N−1−f(ǫ)3−N|A|.

Thus from the point of view of the structure of the spectrum, we have that A′ is essentially as good as A. However, the set A′ has a big advantage over A in that we have good bounds on the Fourier transform of its ﬁbers. This is because the ﬁbers are either empty or close to size |HA|. Empty ﬁbers achieve no increments. On the other hand, ﬁbers which are close to average cannot have an increment too large, or else the set A will have a strong increment on a translate of a codimension 1 subspace of H⊥. Precisely, the estimate we get is

![image 201](<2011-bateman-new-bounds-cap-sets_images/imageFile201.png>)

|Aˆ′H,v(x)| 3−N|A|N−1+f(ǫ) = ρN−1+f(ǫ). (8.1)

(This is because the negative increment on density to pass from A to A′H,v does no more than to reduce the density by a factor of 1 − Nf(ǫ)−1 and the codimension of H is only

f(ǫ).) Should the Fourier transform of A′H,v exceed the above bound, then A will have a strong increment into a codimension one subspace of H⊥ + v.

Moreover, the set A′H,V is a large capset without strong increments (on subspaces of codimension no more than N2 −Nf(ǫ)) but with ǫ replaced by f(ǫ). Thus we see using Proposition

![image 202](<2011-bateman-new-bounds-cap-sets_images/imageFile202.png>)

- 3.3 that for any subspace L of F3N\H with dimension d, we have that


|Aˆ′H,v(x)|2 (|A|

)2dN−1+f(ǫ).

![image 203](<2011-bateman-new-bounds-cap-sets_images/imageFile203.png>)

3N

x∈L

This estimate is a version of the bound on the number of elements of the spectrum of A′H,V in W.

From this information together with the fact that no subspace K of dimension d contains more than dNf(ǫ) elements of Λ and hence of Λ′, we are ready to achieve a contradiction.

We introduce some measure spaces on which we will apply Lemma 2.2. For each v ∈ V , we deﬁne χv, a measure on F3N\H − {0} by

|Aˆ′H,v(x)|2.

χv(X) =

x∈X

Clearly the total measure of χv is bounded by 3−N|A|Nf(ǫ), by Plancherel. We now give a construction for sets which have large density for many of the measures χv.

Let Ξ ⊂ Λ′ with |Ξ| = d N1−f(ǫ). Then in light of the fact that Ξ + H contains at least dN1−f(ǫ) points x where A′(x) is large and in light of Proposition 8.3, there must be N−f(ǫ)|H| values of v for which span(Ξ) has density at least dN−2−f(ǫ) for χv, by the large families principle. (Here, by slight abuse of notation, the span is taken in F3N\H.)

We will take d ∼ N 23. Now let Π be any collection of N 38+O(√µ) subsets of Λ′ with cardinality N 32. We chose the exponents 32 and 83 somewhat arbitrarily. In particular, they allow us to apply Lemma 2.2. By pigeonholing, we may ﬁnd a set of v’s of cardinality |H|N−f(ǫ) for which at least N 83−f(ǫ) of the sets Ξ in Π have the property that span(Ξ) has density N−43−f(ǫ) for χv. From this and Lemma 2.2 we obtain the lower bound

![image 204](<2011-bateman-new-bounds-cap-sets_images/imageFile204.png>)

![image 205](<2011-bateman-new-bounds-cap-sets_images/imageFile205.png>)

![image 206](<2011-bateman-new-bounds-cap-sets_images/imageFile206.png>)

![image 207](<2011-bateman-new-bounds-cap-sets_images/imageFile207.png>)

![image 208](<2011-bateman-new-bounds-cap-sets_images/imageFile208.png>)

![image 209](<2011-bateman-new-bounds-cap-sets_images/imageFile209.png>)

![image 210](<2011-bateman-new-bounds-cap-sets_images/imageFile210.png>)

![image 211](<2011-bateman-new-bounds-cap-sets_images/imageFile211.png>)

χv(span(Ξ1) ∩ span(Ξ2)) χv(F3N\H) |H|N 38−f(ǫ). (8.2)

![image 212](<2011-bateman-new-bounds-cap-sets_images/imageFile212.png>)

![image 213](<2011-bateman-new-bounds-cap-sets_images/imageFile213.png>)

v∈V −Vbad Ξ1∈Π Ξ2∈Π

What this says is that modulo Nf(ǫ) terms, the average density (in χv measure) of an intersection span(Ξ1) ∩ span(Ξ2) is at least approximately N−38. This is rather large since the density of any single element of F3N\H is only approximately N−3 in light of the bound on the Fourier transforms of the ﬁbers, which follows from (8.1).

![image 214](<2011-bateman-new-bounds-cap-sets_images/imageFile214.png>)

We will now produce a random construction of Π. We choose each set of Π uniformly at random. We will write down an upper bound on the expected density in any χv of the intersection span(Ξ1) ∩ span(Ξ2) which contradicts the lower bound 8.2. We observe that if ρ is the density in χv of span(Ξ1) ∩ span(Ξ2) then

ρ ≤ N−3+O(f(ǫ))(3k − 1),

(because χv(x) N−4+O(f(ǫ),) where k is the nullity of the set Ξ1 ∪ Ξ2. We recall that there are no more than N 23+f(ǫ) elements of Λ′ in any subspace of dimension 2N 32. Thus as we choose the 2N 23 elements of Ξ1 and Ξ2, the probability of introducing nullity at each selection is bounded by N−43+f(ǫ). Thus the probability pk of having nullity k is bounded by

![image 215](<2011-bateman-new-bounds-cap-sets_images/imageFile215.png>)

![image 216](<2011-bateman-new-bounds-cap-sets_images/imageFile216.png>)

![image 217](<2011-bateman-new-bounds-cap-sets_images/imageFile217.png>)

![image 218](<2011-bateman-new-bounds-cap-sets_images/imageFile218.png>)

pk (N−32+f(ǫ))k.

![image 219](<2011-bateman-new-bounds-cap-sets_images/imageFile219.png>)

Thus the expected density of span(Ξ1)∩span(Ξ2) is O(N−113 +f(ǫ)). This contradicts (8.2), so we have just proved that ∆ cannot contain a set as thick in Λ + H as required by Theorem 7.1, which is a contradiction.

![image 220](<2011-bateman-new-bounds-cap-sets_images/imageFile220.png>)

Thus we have proved Theorem 1.4 and hence Theorem 1.1.

# 9 Epilogue on eﬃciency

The ǫ which we obtain in Theorem 1.1 is of necessity quite small. Like many arguments in analysis, ours does not aim for great eﬃciency and we seem to lose a factor in the size of ǫ in nearly every line of the argument. However, there are a few points in the argument where we lose signiﬁcantly more. The most notable of these are the use of the asymmetric Balog Szemeredi Gowers lemma and the discovery of the additive structure with comity in Corollary 6.6. What these two parts of the argument have in common is that they are iterative. One starts with a structure and seeks a certain property. If the property is lacking, one ﬁnds a structure which is in a certain sense better but which has cost us a factor in ǫ.

Iteration can be a powerful thing. It sometimes allows us to prove a very deep thing with very few words. The proof doesn’t care how many iterates must be calculated to implement it. We have a version of our argument which we will publish elsewhere that adds even another layer of iteration to the argument but spares us some of the diﬃculties of Theorem 6.10. But certainly, it is less eﬃcient than the argument presented here.

To improve eﬃciency, it is important to make the argument less iterative. In hopes of doing so, we leave the reader with two conjectures:

- Conjecture 9.1. Let N > 0 be a large parameter. (Constants may not depend on N.)

Suppose B and C are sets in F3N each of whose cardinality is bounded by N100. Suppose the number of quadruplets b1 + c1 = b2 + c2 with b1,b2 ∈ B and c1,c2 ∈ C is at least |B||C|2N−σ. Then C is contained in a subspace of dimension NO(σ).

- Conjecture 9.2. Suppose ∆ is a subset of F3N which is Nσ additively non-smoothing. (We may assume as in the previous conjecture that |∆| ≤ N100. Then ∆ admits an additive structure at some height with NO(σ) comity.


# References

[CS11] E. Croot and O. Sisask A Probabilistic Technique for Finding Almost-Periods of Convolutions To appear, GAFA

[G] T. Gowers What is Diﬃcult about the cap set problem http://gowers.wordpress.com/2011/01/11/what-is-diﬃcult-about-the-cap-set-problem/

- [K1] (M. Bateman and) N.H. Katz http://gowers.wordpress.com/2011/01/11/what-is-diﬃcult-about-the-cap-set-problem/ # comment-10533
- [K2] (M. Bateman and) N.H. Katz http://gowers.wordpress.com/2011/01/11/what-is-diﬃcult-about-the-cap-set-problem/ # comment-10540


[KK10] N. H. Katz and P. Koester On Additive Doubling And Energy SIAM J Discrete Math. Vol. 24 (2010) 1684-1693

[M95] R. Meshulam On subsets of ﬁnite abelian groups with no 3-term arithmetic progres-

sions J. Combin. Theory Ser. A Vol. 71 (1995) 168-172 [PM] Polymath on wikipedia. http://en.wikipedia.org/wiki/Polymath project#Polymath Project [PM6] Polymath 6: Improving the bounds for Roth’s theorem.

![image 221](<2011-bateman-new-bounds-cap-sets_images/imageFile221.png>)

![image 222](<2011-bateman-new-bounds-cap-sets_images/imageFile222.png>)

http://polymathprojects.org/2011/02/05/polymath6-improving-the-bounds-for-roths-theorem/ [R99] I. Ruzsa, An analog of Freiman’s theorem in groups, Structure theory of set addition,

Aste´risque No. 258 (1999) 323 - 329 [S08] T. Sanders A note on Freiman’s theorem in vector spaces Combin. Probab. Comput. 1Vol. 17 (2008) 297–305

- [S10] T. Sanders Structure in Sets with Logarithmic Doubling Arxiv 1002.1552


- [S11] T. Sanders On Roth’s theorem on Progressions Arxiv 1011.0104 [TV06] T. Tao, V. Vu, Additive Combinatorics, Cambridge Univ. Press, (2006)


- M. BATEMAN, DEPARTMENT OF MATHEMATICS, UCLA, LOS ANGELES CA bateman@math.ucla.edu
- N. KATZ, DEPARTMENT OF MATHEMATICS, INDIANA UNIVERSITY, BLOOMINGTON IN nhkatz@indiana.edu


