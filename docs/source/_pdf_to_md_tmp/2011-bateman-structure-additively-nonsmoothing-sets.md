arXiv:1104.2862v1[math.CO]14Apr2011

Structure in additively nonsmoothing sets

Michael Bateman and Nets Hawk Katz

Abstract

Sets with many additive quadruples are guaranteed to have many additive octuples, by Ho¨lder’s inequality. Sets with not many more than this are said to be additively nonsmoothing. We give a new proof of a structural theorem for nonsmoothing sets that originally appeared in work of the authors ([BK]) on the size of cap sets in F3N.

# 1 Introduction

In this paper we reprove a structural theorem from [BK] for sets that are not additively smoothing. The notion of additive smoothing was introduced in a recent paper by the authors, where the spectra of large cap sets (i.e., sets in F3N without any lines) are shown to be additively nonsmoothing. See [BK]. We begin by reviewing several deﬁnitions, including that of additively smoothing. The setting for this paper is an abelian group Z.

- Deﬁnition 1.1. For a set A ⊆ Z, and m = 1,2,3,... , we deﬁne the additive energies of A by

E2m(A) = |{(a1,... ,a2m) ∈ A2m: a1 + ··· + am = am+1 + ··· + a2m}|.

The quantity E4(A) is typically called the additive energy of A. The importance of the higher order energies is made clear in [BK], although the theorem here uses only E4 and E8.

- Deﬁnition 1.2. We say a set A is σ-smoothing if


E4(A)3 |A|2

E8(A) ∼ |A|σ

.

![image 1](<2011-bateman-structure-additively-nonsmoothing-sets_images/imageFile1.png>)

When we casually write that a set is “nonsmoothing”, we mean that it is σ-smoothing for a small value of σ; so for example, a set with exactly E8(A) = E4(A)

3

|A|2 is 0-smoothing. This deﬁnition measures the sharpness of the ﬁrst inequality in Proposition 2.1 below. We state the main theorem already, but encourage readers unfamiliar with the notion of additive

![image 2](<2011-bateman-structure-additively-nonsmoothing-sets_images/imageFile2.png>)

smoothing to skip to Section 2 for some examples. In this paper we prove the following structural theorem about sets with minimal additive smoothing. It essentially appeared in [BK] as Theorem 6.10. The signiﬁcant new ingredient here is the notion of sideways comity, which allows us to avoid some of the technicalities in the proof in [BK]. On the other hand, the function f here gives much worse dependence on σ than the function f from [BK].

Theorem 1.3. Fix τ0 > 0. There exists a function fτ0 : (0,1) → (0,∞) with fτ0(η) → 0 as η → 0 such that the following holds. Let ∆ ⊆ Z be a symmetric set (i.e., ∆ = −∆) of

size M. Let σ0 > 0. Assume that E4(∆′) ∼ M2+τ0 for every ∆′ ⊆ ∆ with |∆′| |∆|, and that ∆ is at most σ0-smoothing, i.e., E8(∆) M4+3τ0+σ0. Then there exists α ≥ 0 such that for j = 1,2,... ,Mα−fτ0(σ), we have sets Hj ⊆ Z, sets Xj ⊆ Z, and Bj ⊆ ∆ such that

|Hj| Mτ+α+fτ0(σ0),

|Xj| M1−τ−2α+fτ0(σ0),

|Hj − Hj| |Hj|1+fτ0(σ0), such that

|(Xj + Hj) ∩ Bj| M1−α−fτ0(σ0), and such that Bk ∩ Bj = ∅ unless k = j.

We remark that as a consequence of the estimates on |(Xj + Hj) ∩ ∆|, we also have lower bounds on |Hj|, and |Xj|. Further, by applying Freiman’s theorem, one can conclude that the set H is eﬃciently contained in a subspace or a coset progression, with the details depending on the speciﬁc setting Z.

We take a moment to state the asymmetric Balog-Szemeredi-Gowers theorem. This will help us ﬁnd subsets with good additive properties in sets with good comity and sideways comity. (Both of these terms will be deﬁned below.)

Lemma 1.4. Let B,C ⊂ Z be such that there are at least |B|1−η|C|2 additive quadruples of the form

b1 + c1 = b2 + c2

with b1,b2 ∈ B and c1,c2 ∈ C. Then there exists µ = µ(η, ||BC||), with µ(η, ||BC||) → 0 as η → 0, and there exist K ⊂ Z and X ⊂ Z with

![image 3](<2011-bateman-structure-additively-nonsmoothing-sets_images/imageFile3.png>)

![image 4](<2011-bateman-structure-additively-nonsmoothing-sets_images/imageFile4.png>)

- |B|

![image 5](<2011-bateman-structure-additively-nonsmoothing-sets_images/imageFile5.png>)

- |C|


|X| |B|µ

,

so that

|B ∩ (X + K)| |B|1−µ,

|K − K| |K|1+µ and there exists an element x ∈ Z so that

|C ∩ (x + K)| |C|1−µ. In particular, the last inequality implies

|K| |C|1−µ.

See [TV] Theorem 2.35 for a proof. Acknowledgements The ﬁrst author is supported by an NSF postdoctoral fellowship, DMS-0902490. The second author is partially supported by NSF grant DMS-1001607.

# 2 Examples

We give a quick corollary of H¨older’s inequality that motivates the deﬁnition of additively nonsmoothing.

- Proposition 2.1. If Z is ﬁnite, then for any set A, we have


E4(A)3 |A|2

E8(A) ≥

.

![image 6](<2011-bateman-structure-additively-nonsmoothing-sets_images/imageFile6.png>)

Further, we have

E8(A) ≤ |A|4E4(A). Proof. A straightforward calculation establishes the identity E2m(A) = |Z|2m−1

| 1A(ξ)|2m

ξ∈Z

for m = 1,2,... . (Here 1A is the Fourier transform of 1A,

1 |Z| x∈Z

f(x)e2πi ξ,x

f(ξ) =

![image 7](<2011-bateman-structure-additively-nonsmoothing-sets_images/imageFile7.png>)

and  ·,··  is a nondegenerate symmetric bilinear form. See [TV] Section 4.1 for details in our general setting.) When m = 1, this gives us

| 1A(ξ)|2

|A| = E2(A) = |Z|

ξ∈Z

which is just Plancherel’s equality for the function 1A. H¨older’s inequality yields E4(A) = |Z|3

| 1A(ξ)|4

ξ∈Z

 

 |Z|7

 |Z|

 

1 3

- 2

![image 8](<2011-bateman-structure-additively-nonsmoothing-sets_images/imageFile8.png>)

- 3


![image 9](<2011-bateman-structure-additively-nonsmoothing-sets_images/imageFile9.png>)

| 1A(ξ)|8

| 1A(ξ)|2

≤

ξ∈Z

ξ∈Z

= |A|23E8(A)13. This proves the ﬁrst claim. To prove the second claim, just note that E8(A) = |Z|7

![image 10](<2011-bateman-structure-additively-nonsmoothing-sets_images/imageFile10.png>)

![image 11](<2011-bateman-structure-additively-nonsmoothing-sets_images/imageFile11.png>)

| 1A(ξ)|8

ξ∈Z

≤ |Z|7 sup ξ∈Z

| 1A(ξ)|4

| 1A(ξ)|4

ξ∈Z

≤ |A|4|Z|3

| 1A(ξ)|4

ξ∈Z

= |A|4E4(A),

since | 1A(ξ)| ≤ ||ZA|| for any ξ. As examples of the two extremes, consider a “random” set A of size N in a subgroup H of size N1+ǫ. Given a1,a2,a3 ∈ A, we know

![image 12](<2011-bateman-structure-additively-nonsmoothing-sets_images/imageFile12.png>)

![image 13](<2011-bateman-structure-additively-nonsmoothing-sets_images/imageFile13.png>)

![image 14](<2011-bateman-structure-additively-nonsmoothing-sets_images/imageFile14.png>)

![image 15](<2011-bateman-structure-additively-nonsmoothing-sets_images/imageFile15.png>)

![image 16](<2011-bateman-structure-additively-nonsmoothing-sets_images/imageFile16.png>)

a1 + a2 − a3 ∈ H; further

a1 + a2 − a3 ∈ A

with probability N−ǫ = |A|−ǫ, since |A| = |H|N−ǫ. Hence we expect E4(A) ∼ |A|3−ǫ. By a similar calculation we expect E8(A) ∼ |A|7−ǫ. Note that this example achieves the maximal E8 allowed by the proposition above. On the other hand, if we let A be given by H +R where H is a subgroup of size N1−ǫ and R is a “random” set of size Nǫ, then

E4(A) = E4(H)E4(R) = N3−3ǫN2ǫ = N3−ǫ. However in this case

E8(A) = E8(H)E8(R) = N7−7ǫN4ǫ = N7−3ǫ.

Similarly if A is the union of (unrelated) subspaces Hj, for j = 1,2,... ,N 2ǫ where |Hj| = N1−2ǫ for each j, then

![image 17](<2011-bateman-structure-additively-nonsmoothing-sets_images/imageFile17.png>)

![image 18](<2011-bateman-structure-additively-nonsmoothing-sets_images/imageFile18.png>)

N 2ǫ

E4(A) ∼

![image 19](<2011-bateman-structure-additively-nonsmoothing-sets_images/imageFile19.png>)

E4(Hj) = N 2ǫ N3−32ǫ = N3−ǫ

![image 20](<2011-bateman-structure-additively-nonsmoothing-sets_images/imageFile20.png>)

![image 21](<2011-bateman-structure-additively-nonsmoothing-sets_images/imageFile21.png>)

j=1

and

N 2ǫ

E8(A) ∼

![image 22](<2011-bateman-structure-additively-nonsmoothing-sets_images/imageFile22.png>)

E8(Hj) = N 2ǫ N7−72ǫ = N7−3ǫ.

![image 23](<2011-bateman-structure-additively-nonsmoothing-sets_images/imageFile23.png>)

![image 24](<2011-bateman-structure-additively-nonsmoothing-sets_images/imageFile24.png>)

j=1

Note that these last two sets achieve the minimal E8 allowed by the proposition above.

# 3 A simple reduction

The bulk of the work in this paper goes toward proving the following theorem, which identiﬁes a large piece of the set ∆ with substantial structure. Theorem 1.3 then follows by repeatedly ﬁnding these large pieces until most of ∆ has been exhausted.

Theorem 3.1. Fix τ0 > 0. There exists a universal function fτ0 : (0,1) → (0,∞) with fτ0(η) → 0 as η → 0 such that the following holds. Let ∆ ⊆ Z be a symmetric set of size M. Let σ0 > 0 be such that E4(∆) ∼ M2+τ0 and such that ∆ is at most σ0-smoothing, i.e., E8(∆) M4+3τ0+σ0. Also assume that for every a ∈ ∆,

|{(b,c,d) ∈ ∆3: a − b = c − d}| M1+τ. Then there exists α ≥ 0, a symmetric set H ⊆ Z, and a symmetric set X ⊆ Z such that |H| Mτ+α+fτ0(σ0),

|X| M1−τ−2α+fτ0(σ0),

|H − H| |H|1+fτ0(σ0), and such that

|(X + H) ∩ ∆| M1−α−fτ0(σ0).

We remark that the symmetry conclusions on H and X are in place only to guarantee that after removing X + H from ∆, the remainder is still symmetric.

Proof of Theorem 1.3 given Theorem 3.1. Our ﬁrst fact allows us to assume that no a ∈ ∆ participates in too many quadruples, which is one of the hypotheses needed for Theorem

- 3.1.


- Proposition 3.2. If E4(∆′) M2+τ for every ∆′ ⊆ ∆ with |∆′| |∆|, then there is ∆ ⊆ ∆ with E4( ∆) M2+τ such that for each a ∈ ∆,


|{(b,c,d) ∈ ∆3: a = b + c − d}| M1+τ. In other words, no a participates in more than ∼ M1+τ quadruples. Proof. Observe that

|{(b,c,d) ∈ ∆3: a = b + c − d}| M2+τ,

a∈∆

and hence there are fewer than ∼ C1 M elements a such that the summand is ≥ CM1+τ. We simply remove this set of a and note that the remaining set, which we call ∆, still has essentially full energy by hypothesis since it contains most elements of ∆.

![image 25](<2011-bateman-structure-additively-nonsmoothing-sets_images/imageFile25.png>)

![image 26](<2011-bateman-structure-additively-nonsmoothing-sets_images/imageFile26.png>)

![image 27](<2011-bateman-structure-additively-nonsmoothing-sets_images/imageFile27.png>)

![image 28](<2011-bateman-structure-additively-nonsmoothing-sets_images/imageFile28.png>)

![image 29](<2011-bateman-structure-additively-nonsmoothing-sets_images/imageFile29.png>)

Find ∆ satisfying the conclusion of Proposition 3.2 above. Importantly, the sets ∆j deﬁned below inherit this property (so we do not need to apply Proposition 3.2 more than once). Now we may apply Theorem 3.1 to ﬁnd α1,B1,H1,X1. Then let ∆1 = ∆ \ B1. Note that since |∆1| |∆|, ∆1 still has essentially full energy by the hypothesis of Theorem 1.3, and hence satisﬁes the hypotheses of Theorem 3.1. (The symmetry hypothesis is also satisﬁed, as mentioned immediately after the statement of Theorem 3.1.) Having deﬁned ∆j−1, apply Theorem 3.1 to ﬁnd αj,Bj,Hj,Xj, then deﬁne Bj = (Xj + Hj) ∩ ∆ and ∆j = ∆j−1 \ Bj. We may continue to ﬁnd blocks Bj until

- j−1
- k=1


Bk |∆|.

Not all the αj need to be equal, but we ﬁx this by pigeonholing to ﬁnd α such that

Bk

k: |Bk|∼N1−α±f(σ)

|∆| log M

.

![image 30](<2011-bateman-structure-additively-nonsmoothing-sets_images/imageFile30.png>)

![image 31](<2011-bateman-structure-additively-nonsmoothing-sets_images/imageFile31.png>)

![image 32](<2011-bateman-structure-additively-nonsmoothing-sets_images/imageFile32.png>)

![image 33](<2011-bateman-structure-additively-nonsmoothing-sets_images/imageFile33.png>)

![image 34](<2011-bateman-structure-additively-nonsmoothing-sets_images/imageFile34.png>)

An outline of the proof of Theorem 3.1 is as follows. First, we pigeonhole to ﬁnd D ⊆ ∆−∆ such that |∆ ∩ (x + ∆)| is approximately constant for x ∈ D and such that diﬀerences in

D account for most of the energy in ∆. D corresponds to the diﬀerences from a graph G ⊆ ∆×∆. We will measure how elements of D interact with each other and with elements of ∆ using quantities called comity, which was introduced in [BK] (and even to some degree in [KK]), and sideways comity, which we introduce here. When both of these quantities are small, we can make precise statements about the structure of ∆ by using the asymmetric Balog-Szemeredi-Gowers theorem above. The exact structure depends on |G|. See Section 7 for details on ﬁnding this structure. When either of these quantities is large, we may ﬁnd a graph G′ with |G′| >> |G| such that G′ still accounts for most of the energy of ∆. See Section 5 for the large comity case. See Section 6 for the large sideways comity case. This process terminates once we reach |G′| ∼ |∆|2, which happens after a controlled number of iterations. By this point, we must have achieved small comity and small sideways comity. See Section 8 for details about the iteration.

# 4 Additive structures

In this section we present some basic deﬁnitions.

- Deﬁnition 4.1. We deﬁne an additive structure α on ∆ at height α to be a pair (G,D), where G ⊆ ∆ × ∆ is a graph such that |G| ∼ M2−α, where D is a set such that a − b ∈ D for (a,b) ∈ G, and where |∆ ∩ (a − b + ∆)| is essentially constant for (a,b) ∈ G, i.e.,

sup

(a,b)∈G

|∆ ∩ (a − b + ∆)| ≤ 2 min

(a,b)∈G

|∆ ∩ (a − b + ∆)|.

- Deﬁnition 4.2. For any graph G, we deﬁne the energy of G:


E(G) =

x

|{(a,b) ∈ G: a − b = x}|2.

Note that this is just the number of quadruples in ∆ accounted for by pairs in the graph. The following proposition shows that we can ﬁnd an additive structure capturing most of the energy of ∆. This will help us start the iteration discussed in Section 8.

- Proposition 4.3. There exists an additive structure (G,D) at height α for some α ≤ 1−2τ such that


![image 35](<2011-bateman-structure-additively-nonsmoothing-sets_images/imageFile35.png>)

E(G)

M2+τ (log M)2

.

![image 36](<2011-bateman-structure-additively-nonsmoothing-sets_images/imageFile36.png>)

Proof. To see this, just note that

E4(∆) =

x

|∆ ∩ (x + ∆)|2 =

|∆ ∩ (x + ∆)|2.

x∈∆−∆

Since 0 ≤ |∆∩(x+∆)| ≤ |∆|, we can pigeonhole over log M scales to ﬁnd a set D ⊆ ∆−∆ such that

|∆ ∩ (x + ∆)|2

x∈D

M2+τ log M

![image 37](<2011-bateman-structure-additively-nonsmoothing-sets_images/imageFile37.png>)

and such that |∆ ∩ (x + ∆)| ∼ Mα+τ for some α ≥ 0 and every x ∈ D. Then deﬁne G = {(a,b) ∈ ∆2: a − b ∈ D}.

This pair (G,D) is an additive structure at height α. We now show that α can be taken ≤ 1−2τ . Note that

![image 38](<2011-bateman-structure-additively-nonsmoothing-sets_images/imageFile38.png>)

M2+τ log M

![image 39](<2011-bateman-structure-additively-nonsmoothing-sets_images/imageFile39.png>)

E(G) =

|{(b,d): (a,b) ∈ G and a − b = c − d}|.

a,c

We know that for each a ∈ ∆ there are at most ∼ M1−α many b ∈ ∆ such that (a,b) ∈ G (for otherwise we would violate the assumption of Theorem 3.1). Hence the summand on the right is bounded by ∼ M1−α. This implies that the summand is nonzero for a set |G′| of pairs (a,c), with

|G′|

M2+τ log M

1 M1−α

=

![image 40](<2011-bateman-structure-additively-nonsmoothing-sets_images/imageFile40.png>)

![image 41](<2011-bateman-structure-additively-nonsmoothing-sets_images/imageFile41.png>)

M1+τ+α log M

,

![image 42](<2011-bateman-structure-additively-nonsmoothing-sets_images/imageFile42.png>)

and hence (after pigeonholing over subgraphs of G′ such that |∆∩(a−c+∆)| is essentially constant, which gives us the corresponding D′) that at least (logM2+Mτ)2 of the quadruples in ∆ come from a graph of height α′ with α′ ≤ 2−(1+τ +α) = 1−τ −α. Note that 1−τ −α decreases as α increases, and they are equal when α = 1−2τ . This proves the claim about the height, since either α or α′ is ≤ 1−2τ .

![image 43](<2011-bateman-structure-additively-nonsmoothing-sets_images/imageFile43.png>)

![image 44](<2011-bateman-structure-additively-nonsmoothing-sets_images/imageFile44.png>)

![image 45](<2011-bateman-structure-additively-nonsmoothing-sets_images/imageFile45.png>)

![image 46](<2011-bateman-structure-additively-nonsmoothing-sets_images/imageFile46.png>)

![image 47](<2011-bateman-structure-additively-nonsmoothing-sets_images/imageFile47.png>)

![image 48](<2011-bateman-structure-additively-nonsmoothing-sets_images/imageFile48.png>)

![image 49](<2011-bateman-structure-additively-nonsmoothing-sets_images/imageFile49.png>)

# 5 Comity

The goal of this section is to introduce the notion of comity and to prove Lemma 5.3, which tells us that either an additive structure has good comity, or the set ∆ admits an additive structure of lower height. Both the notion of comity and Lemma 5.3 appeared in [BK]. We start by introducing a convenient shorthand. For x ∈ ∆ − ∆, deﬁne

∆[x] = ∆ ∩ (x + ∆) = {a ∈ ∆: a − x ∈ ∆};

i.e., ∆[x] is the set of elements that participate (in the ﬁrst position) in a diﬀerence of x. To deﬁne comity, assume we are have an additive structure (G,D) at height α. By

interchanging sums and applying Cauchy-Schwarz we have

2

|∆[x] ∩ ∆[y]| =

1∆[x](a)

a∈∆ x∈D

x∈D y∈D

M3−2α. By pigeonholing over C log M scales, we can ﬁnd P ⊆ D × D and β such that

|∆[x] ∩ ∆[y]|

(x,y)∈P

M3−2α log M

, (5.1)

![image 50](<2011-bateman-structure-additively-nonsmoothing-sets_images/imageFile50.png>)

and such that |∆[x] ∩ ∆[y]| ∼ Mβ for (x,y) ∈ P. Note that this immediately implies |P| Mlog3−2Mα−β . We see below that paying attention to β is proﬁtable, which prompts the ﬁrst of our key deﬁnitions. Note that of course β ≤ τ + α since |∆[x]| ∼ Mτ+α.

![image 51](<2011-bateman-structure-additively-nonsmoothing-sets_images/imageFile51.png>)

- Deﬁnition 5.1. We say that an additive structure (G,D) at height α has comity µ if there exists β ≥ τ + α − µ and P ⊆ D × D such that |∆[x] ∩ ∆[y]| ∼ Mβ for (x,y) ∈ P, and such that |P| Mlog3−2Mα−β .


![image 52](<2011-bateman-structure-additively-nonsmoothing-sets_images/imageFile52.png>)

The computation above proves the following:

- Proposition 5.2. For any additive structure (G,D) at height α, there exists µ > 0 such that (G,D) has comity µ.


We remark that by the deﬁnition, if (G,D) has comity µ, then it also has comity µ′ for all µ′ ≥ µ. In Section 8 we will need to select a particular value, but this is of no consequence. We now prove that either our additive structure has small comity parameter, or there exists an additive structure at lower height. The key assumption in this lemma is the hypothesis of small additive smoothing; in fact, this is the only part of the structural theorem that requires it.

- Lemma 5.3. Let (G,D) be an additive structure on ∆ at height α such that E(G) M2+τ,


and let µ > 0. Assume E8(∆) M4+3τ+σ. Then either (G,D) has comity µ or there exists an additive structure (G′,D′) on ∆ at height ≤ α − µ + 2σ such that E(G′) M−2σE(G).

We remark that in our application σ will be much smaller than µ, so the height will decrease by essentially µ.

Proof. First, ﬁnd P and β as guaranteed by Proposition 5.2. Then deﬁne Dβ = {d ∈ ∆ − ∆: |∆ ∩ (d + ∆)| ≥ Mβ}|.

Note that for each (x,y) ∈ P (where P is obtained just as before the statement of the lemma) we have

|∆ ∩ (x − y + ∆)| ≥ |∆[x] ∩ ∆[y]| ≥ Mβ.

In other words, there are at least Mβ ways in which x − y can be written as a diﬀerence of pairs (c,d) ∈ ∆2, i.e., x − y ∈ Dβ. This is because if a ∈ ∆[x] ∩ ∆[y], then a − x = c, a − y = d for some c,d ∈ ∆, so x − y = d − c. There are Mβ such a giving us pairs (d,c) with x − y = d − c. Hence we have, using Cauchy-Schwarz,

M3−2α−β log M

![image 53](<2011-bateman-structure-additively-nonsmoothing-sets_images/imageFile53.png>)

|P| ≤

|D ∩ (z + D)|

x∈Dβ

![image 54](<2011-bateman-structure-additively-nonsmoothing-sets_images/imageFile54.png>)

≤ E4(D)|Dβ|

Since each x ∈ D has Mα+τ representations, (i.e., |∆ ∩ (x + ∆)| ∼ Mα+τ, ) we also know that

E4(D)(Mα+τ)4 E8(∆) M4+3τ+σ Hence

1 (log M)2

1 E4(D)

M6−4α−2β 1 (log M)2

|Dβ|

![image 55](<2011-bateman-structure-additively-nonsmoothing-sets_images/imageFile55.png>)

![image 56](<2011-bateman-structure-additively-nonsmoothing-sets_images/imageFile56.png>)

M2+τ−2β−σ.

![image 57](<2011-bateman-structure-additively-nonsmoothing-sets_images/imageFile57.png>)

We are now ready to deﬁne the graph (G′,D′) in the statement of the lemma. If β ≥ τ + α − µ, then we already have comity µ, by deﬁnition. So assume β < τ + α − µ. Then let

G˜ = {(a,b) ∈ ∆ × ∆: a − b ∈ Dβ}. By the estimate above, we have

|G˜| |Dβ|Mβ

1 (C log M)2

M2+τ−β−σ

![image 58](<2011-bateman-structure-additively-nonsmoothing-sets_images/imageFile58.png>)

M2+τ−β−23σ M2−α−32σ+µ,

![image 59](<2011-bateman-structure-additively-nonsmoothing-sets_images/imageFile59.png>)

![image 60](<2011-bateman-structure-additively-nonsmoothing-sets_images/imageFile60.png>)

because β < τ +α−µ; this is because we do not have comity µ. We are essentially done, but we must note that by deﬁnition of Dβ, a pair (a,b) ∈ G˜ satisﬁes |∆∩(a−b−∆)| Mβ, and the inequality goes in only one direction. To obtain an additive structure, we want essential equality. Nevertheless, this can be obtained by a further pigeonholing to ﬁnd G′ ⊆ G˜ such that |G′| log |G˜M| . Call the corresponding diﬀerence set D′. The computation immediately above proves the claim about the height. Further, this same estimate proves the estimate E(G′) M2+τ−2σ since each pair (a,b) ∈ G′ satisﬁes |∆ ∩ (a − b + ∆)| Mβ.

![image 61](<2011-bateman-structure-additively-nonsmoothing-sets_images/imageFile61.png>)

![image 62](<2011-bateman-structure-additively-nonsmoothing-sets_images/imageFile62.png>)

![image 63](<2011-bateman-structure-additively-nonsmoothing-sets_images/imageFile63.png>)

![image 64](<2011-bateman-structure-additively-nonsmoothing-sets_images/imageFile64.png>)

![image 65](<2011-bateman-structure-additively-nonsmoothing-sets_images/imageFile65.png>)

# 6 Sideways comity

The goal of this section is to introduce the notion of sideways comityand to prove Lemma

- 6.3, which tells us that an additive structure with good comity either also has good sideways comity, or the set ∆ admits an additive structure at lower height.


For the following discussion assume we have an additive structure (G,D) at height α with comity µ. We now give the second of our key deﬁnitions which is for another comity-like notion. First, deﬁne

Fx = {y ∈ D: (x,y) ∈ P},

where P is the set of pairs (x,y) such that |∆[x] ∩ ∆[y]| is large (close to Mτ+α−µ), as in the deﬁnition of comity, Deﬁnition 5.1. We know that

|Fx| M1−α+µ

because otherwise there exists a ∈ ∆[x] such that a participates in many more than M1+τ quadruples (and we have no such a, by assumption in Theorem 3.1). For each x ∈ D and a ∈ ∆[x], deﬁne the related sets

Fx,a = {b ∈ ∆: b − a ∈ Fx} Fa = {b ∈ ∆: b − a ∈ D}.

The sets Fx,a will be more important to us, but consider for a moment the sum

|Fb ∩ ∆[x]|.

x∈D b∈∆

It is straightforward to show that this is log 1M M3−2α by interchanging the sums, just as with

![image 66](<2011-bateman-structure-additively-nonsmoothing-sets_images/imageFile66.png>)

|∆[x] ∩ ∆[y]|.

x∈D y∈D

In fact, we can prove the following slightly reﬁned estimate, with nothing more than interchanging sums:

|∆[x] ∩ Fx,b| =

x∈D b∈∆

=

x∈D b∈∆ c

1∆[x](c)1b+Fx(c)

1∆[y](c) 1 log M

1∆[x](c)

x∈D c

y∈Fx

M3−2α

![image 67](<2011-bateman-structure-additively-nonsmoothing-sets_images/imageFile67.png>)

since the second-to-last display is equal to the sum in estimate 5.1 above, which can be seen by interchanging the sums. By pigeonholing, we can ﬁnd γ and Q ⊆ D × ∆ such that

|∆[x] ∩ Fx,b|

(x,b)∈Q

1 (log M)2

M3−2α (6.1)

![image 68](<2011-bateman-structure-additively-nonsmoothing-sets_images/imageFile68.png>)

and such that

|∆[x] ∩ Fx,b| ∼ Mγ

for (x,b) ∈ Q. Note that this implies |Q| (log 1M)2M3−2α−γ. All of this discussion motivates the following deﬁnition.

![image 69](<2011-bateman-structure-additively-nonsmoothing-sets_images/imageFile69.png>)

- Deﬁnition 6.1. We say an additive structure (G,D) at height α with comity µ has sideways comity ν if there exist γ ≥ τ + α − ν and Q ⊆ D × ∆ such that |∆[x] ∩ Fx,b| ∼ Mγ for (x,b) ∈ Q, and such that |Q| (log 1M)2M3−2α−γ.


![image 70](<2011-bateman-structure-additively-nonsmoothing-sets_images/imageFile70.png>)

The computation above proves the following: Proposition 6.2. For any additive structure (G,D) at height α and comity µ, there exists ν > 0 such that (G,D) has sideways comity ν.

Note that |∆[x]| ∼ Mτ+α; hence by the deﬁnition, having sideways comity ν requires Mτ+α ∼ |∆[x]| |Fx,b| ∼ N1−α+µ; in other words, we need α ≤ 1−2τ +O(ν +µ). Fortunately this is guaranteed by Proposition

![image 71](<2011-bateman-structure-additively-nonsmoothing-sets_images/imageFile71.png>)

- 4.3.


- Lemma 6.3. Suppose (G,D) is an additive structure at height α with comity µ such that E(G) M2+τ. Then either the structure has sideways comity ν or there exists an additive structure (G′,D′) of height ≤ α + µ − ν2 such that E(G′) E(G)M−O(µ).


![image 72](<2011-bateman-structure-additively-nonsmoothing-sets_images/imageFile72.png>)

We remark that in our application µ will be much smaller than ν, so the height will decrease by essentially ν.

Proof of Lemma 6.3. We begin by considering a pair (x,b) ∈ Q. Recall that for each such pair we have

|∆[x] ∩ Fx,b| ∼ Mγ. (6.2) We now prove the following claim:

- Claim 6.4. For each (x,b) ∈ Q, we have |{a ∈ ∆[x]: |(a + b − ∆) ∩ ∆| Mγ−µ}| |∆[x]|M−µ.


Proof of Claim. The condition (6.2) immediately above tells us there are Mγ many c ∈ ∆[x] such that c − b = y for some y ∈ Fx. For each such c, there are at least Mτ+α−µ many a ∈ ∆[x] such that a − y ∈ ∆ (because y is in Fx, and because we have µ-comity). Summing over c ∈ ∆[x] gives us Mγ+τ+α−µ quadruples a+b = c+d with a ∈ ∆[x], b ﬁxed, c,d ∈ ∆, and any given a ∈ ∆[x] appearing no more than Mγ times. Hence there is a set ∆x,b ⊆ ∆[x] of size Mτ+α−µ such that

|∆ ∩ (a + b − ∆)| Mγ−µ for each a ∈ ∆x,b. This is precisely what we claimed.

![image 73](<2011-bateman-structure-additively-nonsmoothing-sets_images/imageFile73.png>)

![image 74](<2011-bateman-structure-additively-nonsmoothing-sets_images/imageFile74.png>)

![image 75](<2011-bateman-structure-additively-nonsmoothing-sets_images/imageFile75.png>)

![image 76](<2011-bateman-structure-additively-nonsmoothing-sets_images/imageFile76.png>)

It remains to construct the graph G′ claimed in the lemma. The set D′ will be contained in the set of diﬀerences x such that |∆ ∩ (x + ∆)| Mγ−µ, with an application of the pigeonhole principle required again, as in Lemma 5.3. It is worth noting that we will actually show that there are lots of pairs whose sum is in D′; by symmetry of ∆ we can conclude that the are the same number of pairs whose diﬀerence is in D′. For b ∈ ∆ deﬁne

Kb = {x: (x,b) ∈ Q}. We know from the deﬁnition of Q that

1 (log M)2

M3−2α−γ. (6.3)

|Kb| |Q|

![image 77](<2011-bateman-structure-additively-nonsmoothing-sets_images/imageFile77.png>)

b

Because of the claim, we know that every a ∈ ∪x∈Kb∆x,b satisﬁes

|∆ ∩ (a + b − ∆)| Mγ−µ. Our goal is to show

∆x,b |Kb|Mτ−1+2α. (6.4)

x∈Kb

Assuming (6.4), we are ﬁnally ready to deﬁne the graph G′ claimed in the statement of the lemma. Let G˜ be the set of all pairs (b,a) ∈ ∆ × ∆ such that

a ∈

∆x,b.

x∈Kb

Hence by estimates (6.4) and (6.3), we have

|G˜| =

∆x,b

b∈∆ x∈Kb

|Kb|Mτ−1+2α

b∈∆

1 (log M)2

M2+τ−γ

.

![image 78](<2011-bateman-structure-additively-nonsmoothing-sets_images/imageFile78.png>)

Once again, we pigeonhole to obtain G′ ⊆ G˜ with |∆ ∩ (a − b + ∆)| essentially constant when (a,b) ∈ G′. If the additive structure we started with has sideways comity ν, then we are done; so assume not. This means γ < τ + α − ν. Hence 2 + τ − γ − µ > 2 − α + ν − µ. This implies that the height of (G′,D′) is less than α − ν + µ, which ﬁnishes the proof modulo the estimate (6.4). We prove (6.4) now using Cauchy-Schwarz:

|∆x,b| =

x∈Kb

1∆x,b(a)

a∈ x∈Kb ∆x,b x∈Kb

![image 79](<2011-bateman-structure-additively-nonsmoothing-sets_images/imageFile79.png>)

![image 80](<2011-bateman-structure-additively-nonsmoothing-sets_images/imageFile80.png>)

∆x,b|

≤ |

x∈Kb

a

1∆[x](a))2

(

x∈Kb

We have already noted that no a ∈ ∆ participates in more than N1−α diﬀerences in D; i.e., x∈K

1∆[x](a) N1−α. Hence the right side of the last display is less than

b

![image 81](<2011-bateman-structure-additively-nonsmoothing-sets_images/imageFile81.png>)

![image 82](<2011-bateman-structure-additively-nonsmoothing-sets_images/imageFile82.png>)

∆x,b| N1−α

|∆x,b|.

|

x∈Kb

x∈Kb

Rearranging terms and noting that x∈K

b

|∆x,b| ∼ |Kb|Mτ+α proves the estimate (6.4).

![image 83](<2011-bateman-structure-additively-nonsmoothing-sets_images/imageFile83.png>)

![image 84](<2011-bateman-structure-additively-nonsmoothing-sets_images/imageFile84.png>)

![image 85](<2011-bateman-structure-additively-nonsmoothing-sets_images/imageFile85.png>)

![image 86](<2011-bateman-structure-additively-nonsmoothing-sets_images/imageFile86.png>)

# 7 Finding structure with comity and sideways comity

The goal of this section is to show that when an additive structure has small comity and small sideways comity, we can ﬁnd substantial additive structure in the set ∆. Precisely, we have:

- Lemma 7.1. Fix τ > 0. There exists a function fτ : (0,1) → (0,∞) with fτ(η) → 0


- as η → 0 such that the following holds. Suppose an additive structure at height α has


comity µ, sideways comity ν, α ≤ 1−2τ , and E(G) M2+τ. Then there exists a set H with |H| Mτ+α+fτ(µ+ν) and X with |X| M1−τ−2α+fτ(µ+ν) such that

![image 87](<2011-bateman-structure-additively-nonsmoothing-sets_images/imageFile87.png>)

|H − H| |H|1+fτ(µ+ν)

|(X + H) ∩ ∆| M1−α−fτ(µ+ν).

The assumption α ≤ 1−2τ will be valid when we use this lemma because of Proposition 4.3. We remark that the functions fτ come from the asymmetric Balog-Szemeredi-Gowers theorem. The dependence on τ comes in the ratio of the sizes of the sets B,C in the statement of that theorem. The dependence on µ and ν enter into the parameter η in the statement of that theorem.

![image 88](<2011-bateman-structure-additively-nonsmoothing-sets_images/imageFile88.png>)

The proof of this lemma follows the idea of the proof of Lemma 6.9 in [BK]. Deﬁne E(A,B) = |{(a,b,c,d) ∈ A × B × A × B: a − b = c − d}|.

We will use sideways comity to obtain estimates on the quantity E(∆[x],Fx,a) for a typical x ∈ D and a ∈ ∆[x]. We show that, on average, this energy is nearly maximal; then the asymmetric Balog-Szemeredi-Gowers lemma allows us to conclude that Fx,a is the union of translates of an almost additively closed set. The key estimate is the following, which holds for any x ∈ D:

- Claim 7.2.


a∈∆[x]

![image 89](<2011-bateman-structure-additively-nonsmoothing-sets_images/imageFile89.png>)

|Fx|E(∆[x],Fx,a) ≥

|∆[x] ∩ Fx,b|2

b∈∆

Proof of Lemma 7.1 . Let’s ﬁrst use the claim to prove the lemma. We sum the estimate over x ∈ D. Note that the assumption of sideways comity is exactly what makes the right hand side large for a typical x ∈ D. Speciﬁcally, we have

x∈D a∈∆[x]

![image 90](<2011-bateman-structure-additively-nonsmoothing-sets_images/imageFile90.png>)

|∆[x] ∩ Fx,b|2

|Fx|E(∆[x],Fx,a) ≥

x∈D b∈∆

M3−2αMτ+α−ν (log M)2 ∼

![image 91](<2011-bateman-structure-additively-nonsmoothing-sets_images/imageFile91.png>)

M3+τ−α−ν (log M)2

,

![image 92](<2011-bateman-structure-additively-nonsmoothing-sets_images/imageFile92.png>)

where the last inequality follows from estimate 6.1 and sideways comity. Since |D| ∼ M2−τ−2α and |∆[x]| ∼ Mτ+α for all x ∈ D, we conclude there are (x,a) in D × ∆[x] such that

![image 93](<2011-bateman-structure-additively-nonsmoothing-sets_images/imageFile93.png>)

|Fx|E(∆[x],Fx,a) M1+τ−ν. The upper bound |Fx| M1−α+µ allows us to conclude

E(∆[x],Fx,a) M1+2τ+α−2ν−µ ∼ Mτ+αMτ+αM1−αM−O(µ+ν) ∼ |∆[x]|2|Fx,a|M−O(µ+ν).

We may apply the asymmetric BSG theorem to obtain the desired conclusion, namely that ∆[x] is essentially an almost additively closed set and Fx,a is essentially a bunch of translates of ∆[x]. We remark that we use here the fact |∆[x]| |Fx,a|, which gives us the right conditions for the asymmetric BSG theorem. This fact follows from the estimate Mτ+α M1−α+µ, which holds because α 1−2τ , by assumption. This completes the proof of Lemma 7.1 given the claim.

![image 94](<2011-bateman-structure-additively-nonsmoothing-sets_images/imageFile94.png>)

Proof of Claim. Fix x ∈ D. Then expand the square:

=

=

≤

=

≤

|∆[x] ∩ Fx,b|2

b∈∆

1Fx(c − b)1Fx(d − b)

b∈∆ c∈∆[x] d∈∆[x]

|{b ∈ ∆: c − b ∈ Fx and d − b ∈ Fx}|

c∈∆[x] d∈∆[x]

|{(d,y,y′) ∈ ∆[x] × Fx × Fx: c − y = d − y′}|

c∈∆[x]

|Fx,c ∩ (∆[x] − y′)|

c∈∆[x] y′∈Fx

c∈∆[x]

![image 95](<2011-bateman-structure-additively-nonsmoothing-sets_images/imageFile95.png>)

|Fx|E(∆[x],Fx,c).

The last inequality follows from Cauchy-Schwarz. This proves the claim, and hence the lemma.

![image 96](<2011-bateman-structure-additively-nonsmoothing-sets_images/imageFile96.png>)

![image 97](<2011-bateman-structure-additively-nonsmoothing-sets_images/imageFile97.png>)

![image 98](<2011-bateman-structure-additively-nonsmoothing-sets_images/imageFile98.png>)

![image 99](<2011-bateman-structure-additively-nonsmoothing-sets_images/imageFile99.png>)

![image 100](<2011-bateman-structure-additively-nonsmoothing-sets_images/imageFile100.png>)

![image 101](<2011-bateman-structure-additively-nonsmoothing-sets_images/imageFile101.png>)

![image 102](<2011-bateman-structure-additively-nonsmoothing-sets_images/imageFile102.png>)

![image 103](<2011-bateman-structure-additively-nonsmoothing-sets_images/imageFile103.png>)

# 8 Iteration

In this section we carry out the bookkeeping necessary for iteration of the main lemmas. First we iterate Lemma 5.3 to get the following:

- Lemma 8.1. Let (G,D) be an additive structure at height α such that E(G) M2+τ and such that E8(∆) M4+3τ+σ. Then there exists an additive structure (G′,D′) with comity


and height α′ ≤ α with E(G′) E(G)M−µ.

µ = logC1

![image 104](<2011-bateman-structure-additively-nonsmoothing-sets_images/imageFile104.png>)

![image 105](<2011-bateman-structure-additively-nonsmoothing-sets_images/imageFile105.png>)

σ

Proof. Apply Lemma 5.3 iteratively until we reach comity µ. Because we lower height by µ 2 at each iteration, we will achieve comity µ within ∼ µ1 iterations. The energy loss after k

![image 106](<2011-bateman-structure-additively-nonsmoothing-sets_images/imageFile106.png>)

![image 107](<2011-bateman-structure-additively-nonsmoothing-sets_images/imageFile107.png>)

1

µ = σC C1′ log σ1 << logC1

iterations is M−O(σCk). Since k µ 1, we have σCk ≤ σC

. This yields a structure (G′,D′), at height ≤ α with comity logC1

![image 108](<2011-bateman-structure-additively-nonsmoothing-sets_images/imageFile108.png>)

![image 109](<2011-bateman-structure-additively-nonsmoothing-sets_images/imageFile109.png>)

![image 110](<2011-bateman-structure-additively-nonsmoothing-sets_images/imageFile110.png>)

![image 111](<2011-bateman-structure-additively-nonsmoothing-sets_images/imageFile111.png>)

![image 112](<2011-bateman-structure-additively-nonsmoothing-sets_images/imageFile112.png>)

![image 113](<2011-bateman-structure-additively-nonsmoothing-sets_images/imageFile113.png>)

σ

and E(G′) E(G)M−µ.

![image 114](<2011-bateman-structure-additively-nonsmoothing-sets_images/imageFile114.png>)

![image 115](<2011-bateman-structure-additively-nonsmoothing-sets_images/imageFile115.png>)

![image 116](<2011-bateman-structure-additively-nonsmoothing-sets_images/imageFile116.png>)

![image 117](<2011-bateman-structure-additively-nonsmoothing-sets_images/imageFile117.png>)

![image 118](<2011-bateman-structure-additively-nonsmoothing-sets_images/imageFile118.png>)

![image 119](<2011-bateman-structure-additively-nonsmoothing-sets_images/imageFile119.png>)

σ

Our goal is to ﬁnd an additive structure on ∆ with comity and sideways comity ν⋆ with ν⋆ tending to zero as the nonsmoothing parameter σ0 tends to zero. We of course also want this additive structure to retain most of the energy of the set ∆. With this, we can apply Lemma 7.1 to obtain the additive structure we want.

By pigeonholing we can ﬁnd an additive structure (G0,D0) of height ≤ 1−2τ ; this is Proposition 4.3. We note that the assumption on height is necessary for Lemma 7.1, and that

![image 120](<2011-bateman-structure-additively-nonsmoothing-sets_images/imageFile120.png>)

during this iteration we will only lower the height, so the estimate on height persists. We then iterate Lemmas 8.1 and 6.3 as follows.

Fix a parameter ν⋆. This is the sideways comity we want to ﬁnd. Now we take σ0 small enough that

1 σ0

1 ν⋆

∼ log log ... log

,

![image 121](<2011-bateman-structure-additively-nonsmoothing-sets_images/imageFile121.png>)

![image 122](<2011-bateman-structure-additively-nonsmoothing-sets_images/imageFile122.png>)

so that (using notation from below) µk << ν⋆ whenever k ν 1⋆. The function f in the statement of Theorem 3.1 is obtained by taking ν⋆ << τ0 (the reason for this will be apparent at the end of this section), inverting the relationship between σ0 and ν⋆, and factoring in the loss from the asymmetric Balog-Szemeredi-Gowers theorem.

![image 123](<2011-bateman-structure-additively-nonsmoothing-sets_images/imageFile123.png>)

We now deﬁne a sequence of additive structures (Gj,Dj) as follows: given (Gj,Dj) at height αj with E(Gj) M2+τj and E8(∆) M4+3τj+σj, apply Lemma 8.1 to ﬁnd ( Gj, Dj) at height αj ≤ αj with comity µj = logC1

and E( Gj) E(Gj)M− µj. If ( Gj, Dj) has sideways comity ≤ ν⋆, apply Lemma 7.1 to obtain the desired structure.

![image 124](<2011-bateman-structure-additively-nonsmoothing-sets_images/imageFile124.png>)

![image 125](<2011-bateman-structure-additively-nonsmoothing-sets_images/imageFile125.png>)

σj

If not, then apply Lemma 6.3 with σj+1 = C µj to ﬁnd an additive structure (Gj+1,Dj+1) of height αj+1 ≤ αj − ν2⋆, such that E(Gj+1) E(Gj)M− µj. Since height drops by ν2⋆

![image 126](<2011-bateman-structure-additively-nonsmoothing-sets_images/imageFile126.png>)

![image 127](<2011-bateman-structure-additively-nonsmoothing-sets_images/imageFile127.png>)

- at each iteration, we must obtain sideways comity within ∼ ν1⋆ iterations. Note that our estimate on the height is valid since we arranged that µk << ν⋆ for k ν 1⋆ .


![image 128](<2011-bateman-structure-additively-nonsmoothing-sets_images/imageFile128.png>)

![image 129](<2011-bateman-structure-additively-nonsmoothing-sets_images/imageFile129.png>)

Hence there is k ν 1⋆ such that ( Gk, Dk) has comity µk ≤ ν⋆ and sideways comity ν⋆, and

![image 130](<2011-bateman-structure-additively-nonsmoothing-sets_images/imageFile130.png>)

k

j=0 µj) E(G0)M−O( µk) E(∆)M−ν⋆. Hence we apply Lemma 7.1 with comity ν⋆, sideways comity ν⋆, and E(Gk) M2+τ0−ν⋆.

E(Gk) E(G0)M−O(

# References

[BK] M. Bateman and N. H. Katz, New bounds on cap sets, http://lanl.arxiv.org/abs/1101.5851

[KK] N. H. Katz and P. Koester On Additive Doubling And Energy SIAM J Discrete Math. Vol. 24 (2010) 1684-1693

[TV] T. Tao, V. Vu, Additive Combinatorics, Cambridge Univ. Press, (2006)

- M. BATEMAN, DEPARTMENT OF MATHEMATICS, UCLA, LOS ANGELES CA bateman@math.ucla.edu
- N. KATZ, DEPARTMENT OF MATHEMATICS, INDIANA UNIVERSITY, BLOOMINGTON IN nhkatz@indiana.edu


