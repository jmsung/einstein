arXiv:1405.5800v2[math.NT]18Jun2014

A QUANTITATIVE IMPROVEMENT FOR ROTH’S THEOREM ON ARITHMETIC PROGRESSIONS

THOMAS F. BLOOM

Abstract. We improve the quantitative estimate for Roth’s theorem on threeterm arithmetic progressions, showing that if A ⊂ {1, . . . , N} contains no nontrivial three-term arithmetic progressions then |A| ≪ N(log log N)4/ log N. By the same method we also improve the bounds in the analogous problem over Fq[t] and for the problem of ﬁnding long arithmetic progressions in a sumset.

1. Introduction

In this paper we prove the following quantitative improvement for Roth’s theorem on arithmetic progressions.

- Theorem 1.1. If A ⊂ {1,...,N} contains no non-trivial three-term arithmetic progressions then


(log log N)4 log N

|A| ≪

N.

![image 1](<2014-bloom-quantitative-improvement-roth-theorem_images/imageFile1.png>)

This problem has a long history, the ﬁrst signiﬁcant quantitative bound being given by Roth [1953]. Let R(N) denote the size of the largest subset of {1,...,N} which contains no non-trivial three-term arithmetic progressions. For comparison the table below summarises the history of upper bounds for R(N).

![image 2](<2014-bloom-quantitative-improvement-roth-theorem_images/imageFile2.png>)

![image 3](<2014-bloom-quantitative-improvement-roth-theorem_images/imageFile3.png>)

![image 4](<2014-bloom-quantitative-improvement-roth-theorem_images/imageFile4.png>)

![image 5](<2014-bloom-quantitative-improvement-roth-theorem_images/imageFile5.png>)

Roth [1953] N/ log log N

![image 6](<2014-bloom-quantitative-improvement-roth-theorem_images/imageFile6.png>)

Szemer´edi [1990] and Heath-Brown [1987] N/(log N)c for some c > 0 Bourgain [1999] (log log N)1/2N/(logN)1/2 Bourgain [2008] (log log N)2N/(log N)2/3

![image 7](<2014-bloom-quantitative-improvement-roth-theorem_images/imageFile7.png>)

![image 8](<2014-bloom-quantitative-improvement-roth-theorem_images/imageFile8.png>)

![image 9](<2014-bloom-quantitative-improvement-roth-theorem_images/imageFile9.png>)

![image 10](<2014-bloom-quantitative-improvement-roth-theorem_images/imageFile10.png>)

![image 11](<2014-bloom-quantitative-improvement-roth-theorem_images/imageFile11.png>)

![image 12](<2014-bloom-quantitative-improvement-roth-theorem_images/imageFile12.png>)

![image 13](<2014-bloom-quantitative-improvement-roth-theorem_images/imageFile13.png>)

![image 14](<2014-bloom-quantitative-improvement-roth-theorem_images/imageFile14.png>)

![image 15](<2014-bloom-quantitative-improvement-roth-theorem_images/imageFile15.png>)

![image 16](<2014-bloom-quantitative-improvement-roth-theorem_images/imageFile16.png>)

![image 17](<2014-bloom-quantitative-improvement-roth-theorem_images/imageFile17.png>)

![image 18](<2014-bloom-quantitative-improvement-roth-theorem_images/imageFile18.png>)

Sanders [2012] N/(logN)3/4−o(1) Sanders [2011] (log log N)6N/ logN

![image 19](<2014-bloom-quantitative-improvement-roth-theorem_images/imageFile19.png>)

![image 20](<2014-bloom-quantitative-improvement-roth-theorem_images/imageFile20.png>)

![image 21](<2014-bloom-quantitative-improvement-roth-theorem_images/imageFile21.png>)

![image 22](<2014-bloom-quantitative-improvement-roth-theorem_images/imageFile22.png>)

![image 23](<2014-bloom-quantitative-improvement-roth-theorem_images/imageFile23.png>)

![image 24](<2014-bloom-quantitative-improvement-roth-theorem_images/imageFile24.png>)

![image 25](<2014-bloom-quantitative-improvement-roth-theorem_images/imageFile25.png>)

![image 26](<2014-bloom-quantitative-improvement-roth-theorem_images/imageFile26.png>)

The claimed bound of (log log N)5N/ logN in Sanders [2011] is due to a calculation error, and the method there in fact delivers (log log N)6N/ logN as in the table above. The best known lower bound has the shape R(N) ≫ N exp(−c√log N) for some absolute constant c > 0, due to Behrend [1946], and so Theorem 1.1 still leaves much to be desired.

![image 27](<2014-bloom-quantitative-improvement-roth-theorem_images/imageFile27.png>)

Not only does the method of this paper deliver a quantitative improvement but it manages to do so without the powerful combinatorial tools used in Sanders

- [2011], and instead operates almost entirely in ‘frequency space’, exploiting a new lemma concerning structural properties of the large Fourier spectrum inspired by a recent breakthrough in Roth’s theorem in Fnp by Bateman and Katz [2012]. In


![image 28](<2014-bloom-quantitative-improvement-roth-theorem_images/imageFile28.png>)

The author was supported by an EPSRC doctoral training grant.

1

particular, we hope that the methods in this paper could be used along with more combinatorial techniques to yield further quantitative progress.

The signiﬁcant new ingredient in the proof of Theorem 1.1 is a new lemma about the structural properties of the set of large Fourier coeﬃcients of a given set, which under certain circumstances oﬀers a quantitative improvement over a related wellknown lemma of Chang [2002]. As a further demonstration of the utility of this lemma we outline how it can be combined with the technique of Sanders [2008] to prove the following quantitative improvement to the problem of ﬁnding long arithmetic progressions in a sumset.

- Theorem 1.2. If A,B ⊂ {1,...,N} with both c1αN ≤ |A| ≤ |B| ≤ c2αN then A + B contains an arithmetic progression of length at least

exp cf(α) log N , where f(α) = α1/2/ log(1/α) and the constant c > 0 depends only on c1 and c2.

![image 29](<2014-bloom-quantitative-improvement-roth-theorem_images/imageFile29.png>)

By contrast, Sanders [2008] used Chang’s lemma to prove a similar result with f(α) = α, a result which was ﬁrst proved using a diﬀerent method by Green [2002]. This was subsequently improved by Croot,  Laba, and Sisask [2013] to f(α) = α1/2 (log(1/α))−3/2. The proof of Theorem 1.2 can be easily adapted to give a similar bound when the sizes of A and B are not comparable but in this situation the method of Croot,  Laba, and Sisask [2013] delivers superior bounds.

We shall present our method in a general setting, which will allow us to prove more general versions of Theorem 1.1 in both the integers and their ﬁnite-characteristic analogue Fq[t]. In general, we will be concerned with counting non-trivial solutions to equations of the shape

- (1) c1x1 + c2x2 + c3x3 = 0,


where c1 + c2 + c3 = 0. A trivial solution is one where x1 = x2 = x3. Applied to any such equation our method yields the following result over the integers.

- Theorem 1.3. If c1,c2,c3 ∈ Z\{0} are such that c1 + c2 + c3 = 0 and A ⊂ {1,...,N} contains no non-trivial solutions to (1) then

|A| ≪c

(log log N)4 log N

![image 30](<2014-bloom-quantitative-improvement-roth-theorem_images/imageFile30.png>)

N.

In particular, Theorem 1.1 follows by considering the coeﬃcients c = (1,1,−2). The polynomial ring Fq[t] is, in many respects, a ﬁnite-characteristic analogue of the integers, so we should expect a result of similar strength to hold. In Bloom

- [2012] the method of Sanders [2011] was adapted to give a quantitative result for


Fq[t]. In this paper we shall similarly prove an analogue of Theorem 1.3 for Fq[t]. As in Bloom [2012] the ﬁnite-characteristic property leads to a slight improvement in this case (due to the preponderance of subgroups).

- Theorem 1.4. Let A ⊂ Fq[t]deg<n. If c1,c2,c3 ∈ Fq[t]\{0} are such that c1 + c2 + c3 = 0 and A contains no non-trivial solutions to (1) then


(log n)2 n

qn.

|A| ≪c

![image 31](<2014-bloom-quantitative-improvement-roth-theorem_images/imageFile31.png>)

We remark that if c1,c2,c3 ∈ Fq\{0} then the problem is much simpler and better bounds are available. In particular, Liu and Spencer [2009] proved that in this case

we have the upper bound |A| ≪c qn/n; when c1,c2,c3 ∈ Fp\{0} this bound was ﬁrst provided by Meshulam [1995]. It is also likely that the work of Bateman and Katz

[2012] in Fnp could be adapted to deliver a bound of |A| ≪c qn/n1+ǫ for some absolute constant ǫ > 0, when c1,c2,c3 ∈ Fq\{0}.

The core of our argument is a qualitatively stronger alternative to a well-known lemma of Chang [2002] concerning the additive structure of the large spectrum of the Fourier transform in ﬁnite groups. More particularly, if G is a ﬁnite abelian group and A ⊂ G with density α = |A|/ |G| then we deﬁne the large spectrum

∆η(A) as the set of characters γ ∈ G such that A(γ) ≥ η |A|. It follows immediately from Parseval’s theorem that |∆η(A)| ≤ η−2α−1, which is the best possible bound on the cardinality. Chang’s lemma shows that a smaller set can be found which additively ‘controls’ the spectrum. In particular, we say that ∆ is d-covered if there exists Λ of size |Λ| ≤ d such that

∆ ⊂

ǫλλ : ǫλ ∈ {−1,0,1} .

λ∈Λ

In this language, Chang’s lemma may be stated as follows.

- Theorem 1.5 (Chang [2002]). If A ⊂ G with density α = |A|/ |G| then ∆η(A) is d-covered for some

d ≪ η−2 log(1/α).

This important structural lemma has found many applications since, and in particular has been instrumental in the recent advances in Roth’s theorem. By contrast, in this paper our method does not directly use Chang’s lemma, but rather the following theorem which is, for some applications, much stronger.

- Theorem 1.6. If A ⊂ G with density α = |A| / |G| then there exists ∆′ ⊂ ∆η(A) of size |∆′| ≫ η |∆η(A)| which is d-covered for some


d ≪ η−1 log(1/α).

In particular, we can save a factor of η in the dimension while only losing a factor of η on the size of the set considered. We prove Theorem 1.6, or rather, a more general version, by considering the additive energy of large spectra, building on work by Shkredov [2008] and Bateman and Katz [2012].

For our applications we shall discuss the ideas leading to Theorem 1.6 in a general setting that also applies to covering ‘relative’ to a given set, which is needed for the density increment strategy used for Roth’s theorem.

2. Notation and definitions

We ﬁx some ﬁnite abelian group G with dual group G. Let N = |G|. For convenience we shall use the counting measure on both G and G. In particular all Lp norms on both G and G are deﬁned with respect to the counting measure, so that if f : G → C and p ≥ 1 then

1/p

|f(x)|p

|f(x)| ,

f p =

and f ∞ = sup x∈G

x

and similarly for ω : G → C. For any function f : G → C we deﬁne the Fourier transform f : G → C by

f(γ) =

f(x)γ(x). For all functions f,g : G → C we have Parseval’s identity f,g =

x

f(x)g(x) = N−1

![image 32](<2014-bloom-quantitative-improvement-roth-theorem_images/imageFile32.png>)

![image 33](<2014-bloom-quantitative-improvement-roth-theorem_images/imageFile33.png>)

f(γ) g(γ).

γ

x

If B ⊂ G and Γ ⊂ G then for any ǫ ∈ [0,2] we say that B has ǫ-control of Γ if for all x ∈ B and γ ∈ Γ we have

|1 − γ(x)| ≤ ǫ.

This condition will be important in several places; in general, the hypothesis of control presents no serious diﬃculties as we will just deﬁne the sets we are working with precisely so that they have the required control. The details will vary on the choice of the group G, and hence for most of the paper we simply present the necessary control hypothesis and take care of how to ensure it in our applications in the ﬁnal sections of the paper.

For any η ∈ [0,1] and f : G → C we deﬁne the spectrum

∆η(f) = γ ∈ G : f(γ) ≥ η f 1 and the level spectrum

∆˜η(f) = γ ∈ G : η f 1 ≤ f(γ) < 2η f 1 .

For 0 < δ ≤ 1 we shall use the convenient shorthand L(δ) to denote 2 + ⌈log(1/δ)⌉. Finally, it will often be convenient for certain sets to renormalise the counting measure to be compact; these sets will always be denoted by B (possibly with some subscripts or superscripts) and then for any A ⊂ G we deﬁne β(A) = |A ∩ B|/ |B|. In general, if we speak of A ⊂ B having relative density α then this means β(A) = α.

We will frequently abuse notation by conﬂating a set and its characteristic function; thus, for example, if Γ ⊂ G then Γ(γ) = 1 if γ ∈ Γ and 0 otherwise.

For any Γ ⊂ G and ω : G → R+ and integer m ≥ 1 we deﬁne the additive energy as

 .

 

m

m

γj′

ω(γ1)···ω(γm′ )Γ

γi −

E2m(ω,Γ) =

j=1

i=1

γ1,...,γm′

Similarly, we deﬁne the restricted energy as

 

  .

Et♯

γ′

γ −

1,t2(ω,Γ) =

ω(γ)Γ

γ∈∆1∪∆2

γ∈∆1

γ′∈∆2

∆1∈( G

),∆2∈( G

)

t1

t2

∆1∩∆2=∅

We write E2♯m for Em,m♯ and for any ω and Γ we deﬁne E0(ω,Γ) = E0♯(ω,Γ) = 1. Observe that E and E♯ diﬀer, not only in the restriction on repeating elements, but also in that the former is sensitive to permutations of the γi. We say that S is d-covered by Γ if there exists Λ ⊂ G of size |Λ| ≤ d such that

S ⊂ Γ − Γ + Λ ,

where

Λ =

ǫλλ : ǫλ ∈ {−1,0,1}

λ∈Λ

and  ∅  = {0}.

We say that ∆ is Γ-dissociated if for all k ≥ 1 and λ ∈ G there are at most 2k many pairs ∆1,∆2 of disjoint subsets of ∆ such that |∆1 ∪ ∆2| = k and

γ′ ∈ Γ + λ.

γ −

γ∈∆1

γ′∈∆2

Finally, we say that S has Γ-dimension of d if d is the size of the largest Γ-dissociated subset of S. We observe that the dimension is always at least 1 since any singleton set is trivially Γ-dissociated for all Γ ⊂ G. Furthermore, if ∆ is Γ-dissociated then it is also Γ′-dissociated for any translate Γ′ of Γ.

3. Additive energy

In this section we discuss the relationship between the dimension of a set and its additive energy. If a set has a very large dimension then almost all of the set is dissociated, and hence one would expect few additive relations between its elements, so it should have small additive energy. The following lemma veriﬁes this intuition.

- Lemma 3.1. If S ⊂ G has Γ-dimension |S| − k then for all m ≥ t1,t2 ≥ 0

Et♯

1,t2(S,Γ) ≤ 4k+m.

Proof. Let S = S0 ⊔ S1 where S0 is Γ-dissociated and |S1| = k. By separating the contribution from the subsets of S1 we obtain the estimate

Et♯

1,t2(S,Γ) =

∆1∈(

S t1

),∆2∈(

S t2

)

∆1∩∆2=∅

Γ

 

γ∈∆1

γ −

γ′∈∆2

γ′

 

≤

- 0≤r1≤t1
- 0≤r2≤t2


k r1

k r2

sup

λ

∆1∈( S

0 t1−r1

),∆2∈( S

0 t2−r2

)

∆1∩∆2=∅

Γ

 

γ∈∆1

γ −

γ′∈∆2

γ′ + λ

  .

Since S0 is Γ-dissociated, however, the inner summand is bounded above by 2t

1+t2

and the lemma follows.

For the main result of this section we need to convert a conclusion about the restricted additive energy to the full additive energy, for which the following lemma will suﬃce.

- Lemma 3.2. For any Γ ⊂ G, weight function ω : G → R+ and integer m ≥ 2 we have


ω −t

1−t2 2

E2m(ω,Γ) ≤ 24m(m!)2 ω 22m

sup

![image 34](<2014-bloom-quantitative-improvement-roth-theorem_images/imageFile34.png>)

((m − t1)!(m − t2)!)1/2

λ

0≤t1,t2≤m

Et♯

1,t2(ω,Γ+ λ).

Proof. We divide the range of summation of E2m according to the size of the subsets of {γ1,...,γm} and {γ1′,...,γm′ } consisting of elements that each occur with multiplicity 1. This leads to the upper bound

- (2) E2m(ω,Γ) ≤ 0≤l1,l2≤m

Gm−l

1

(ω)Gm−l

2

(ω)

m l1

m l2

sup

λ

Fλ(l1,l2)

where

Fλ(l1,l2) =

γ1,...,γl′2 γi =γj γi′ =γj′ i =j

ω(γ1)···ω(γl′

2

)Γ

 

l1

i=1

γi −

l2

j=1

γj′ − λ

 

and

- (3) Gk(ω) =

∗

∆ γ∈∆

ω(γ) ≤

k! (⌊k/2⌋)! γ

![image 35](<2014-bloom-quantitative-improvement-roth-theorem_images/imageFile35.png>)

ω(γ)2

k/2

,

the ﬁrst sum being restricted to those ordered k-tuples ∆ ∈ Gk where each element occurs with multiplicity at least 2. The sum Fλ(l1,l2) is almost a renormalised version of the restricted energy El♯

1,l2 except that it lacks the restriction γi = γj′ for all 1 ≤ i ≤ l1 and 1 ≤ j ≤ l2. To introduce this we partition Fλ(l1,l2) according to the number of common elements between the γi and γi′; thus

- (4) Fλ(l1,l2) ≤


min(l1,l2)

l1 i

i=0

l2 i

i! ω 22i (l1 − i)!(l2 − i)!El♯

1−i,l2−i(ω,Γ + λ).

Combining (2), (3) and (4) and simplifying the expression implies that E2m(ω,Γ) is at most

min(l1,l2)

ω 2 2i−l1−l2 i!(⌊(m − l1)/2⌋)!(⌊(m − l2)/2⌋)!

(m!)2 ω 22m

El♯

sup

1−i,l2−i(ω,Γ+λ).

![image 36](<2014-bloom-quantitative-improvement-roth-theorem_images/imageFile36.png>)

λ

i=0

0≤l1,l2≤m

Relabelling t1 = l1 − i and t2 = l2 − i this is at most (m!)2 ω 22m

ω 2 −t1−t2 sup

Et♯

1,t2(ω,Γ + λ)f(m,t1,t2) where

λ

0≤t1,t2≤m

m−max(t1,t2)

1 i!(⌊(m − t1 − i)/2⌋)!(⌊(m − t2 − i)/2⌋)!

f(m,t1,t2) =

.

![image 37](<2014-bloom-quantitative-improvement-roth-theorem_images/imageFile37.png>)

i≥max(t1,t2)

Finally, a tedious calculation using the elementary inequality n!/(⌊n/2⌋!)2 ≤ 2(n + 1)1/22n, valid for all n ≥ 0, shows that the inner sum is at most 24m((m−t1)!(m− t2)!)−1/2 and the lemma follows.

The ﬁnal technical lemma of this section provides a relationship between covering and dimension that will be important in the proof of Theorem 3.1.

- Lemma 3.3. Let Γ ⊂ G be a symmetric set. If ∆ ⊂ G has Γ-dimension r then


there is a partition G = Λ0 ⊔Λ1 where Λ0 is 2r-covered by Γ and for all γ ∈ Λ1 the set ∆ ∪ {γ} has Γ-dimension r + 1.

Proof. By hypothesis we can decompose ∆ as ∆0⊔∆1 where ∆0 is Γ-dissociated and |∆0| = r. Let ∆′ be the set of all γ ∈ G such that ∆0 ∪ {γ} is not Γ-dissociated. We claim that if we let Λ0 = ∆′ ∪ ∆0 and Λ1 = G\Λ0 then this is a suitable decomposition.

Firstly, let γ ∈ Λ1. By construction the set ∆0 ∪ {γ} is Γ-dissociated, and hence ∆ ∪ {γ} has Γ-dimension at least r + 1 by deﬁnition, since |∆0 ∪ {γ}| = r + 1. It remains to show that Λ0 is 2r-covered by Γ; for this, it suﬃces to show that

∆0 ∪ ∆′ ⊂ Γ − Γ + ∆0 + ∆0 . This is obvious for ∆0. Let γ ∈ ∆′. By construction ∆0 ∪ {γ} is not Γ-dissociated, and hence there exists k ≥ 1 and λ ∈ G such that there are more than 2k many triples (ǫ,∆′1,∆′2) such that ǫ ∈ {−1,0,1}, the sets ∆′1 and ∆′2 are disjoint subsets of ∆0 with |∆′1 ∪ ∆′2| + |ǫ| = k, and

γ2′ ∈ Γ + λ.

γ1′ −

ǫγ +

γ2′∈∆′2

γ1′ ∈∆′1

If there exists at least one such triple with ǫ = 0 and at least one with ǫ = 0 then it is easy to check that this implies that γ ∈ Γ−Γ+ ∆0 − ∆0 as required. If ǫ ≡ 0 for all such triples then this contradicts the Γ-dissociativity of ∆0. Hence we can assume that ǫ ∈ {−1,1} for all such triples; this is clearly impossible for k = 1, and for k > 1 we observe that by the pigeonhole principle there are strictly more than 2k−1 such triples with identical ǫ. This, however, is another contradiction to the Γdissociativity of ∆0, considering the translate Γ+λ−ǫγ. Thus γ ∈ Γ−Γ+ ∆0 − ∆0 as required, and the proof is complete.

The following theorem is crucial, and uses random sampling to prove a hereditary version of our earlier intuition: namely, if a set is such that every large subset is not eﬃciently covered then we must have particularly small additive energy. The argument is a variant on that used in [Bateman and Katz, 2012, Section 5]. There, however, they only wish to bound the 8-fold additive energy, whereas for our purposes we shall need to deal with the 2m-fold additive energy where m → ∞

- as N → ∞ (for our applications we shall in fact take m ≈ (log log N)1+o(1)), and hence we have taken care to make the dependence on m explicit.


We treat the constants in this argument, as in the rest of this paper, quite crudely; it is certainly possible to improve them, but such improvements would have a negligible eﬀect on the main results.

- Theorem 3.1. Let Γ ⊂ G be a symmetric set and ω : G → R+. Let m ≥ 2 and


d ≥ n ≥ 2 be such that m ≤ d/4 and ω 2 ≤ m1/2d−1 ω 1. Then either there is a ﬁnite set ∆ ⊂ G such that

n d

ω(γ) ≥

ω 1 and ∆ is 2d-covered by Γ, or

![image 38](<2014-bloom-quantitative-improvement-roth-theorem_images/imageFile38.png>)

γ∈∆

E2m(ω,Γ) ≤ 213m+6nm2md−2m ω 21m .

Proof. Without loss of generality we may suppose that ω 1 = 1. We ﬁrst observe that either we are in the ﬁrst case, or every subset ∆ ⊂ G which is 2d-covered by

Γ satisﬁes γ∈∆ ω(γ) ≤ nd−1, which we shall assume henceforth.

Let S ⊂ G be a random set of size at most d chosen by selecting d elements of G

- at random, where we choose γ ∈ G with probability ω(γ). We claim that for k ≥ 0 the set S has Γ-dimension d − k with probability at most nk/k!.


For suppose we have selected d′ ≤ d elements of S, say S′, and suppose that S′ has Γ-dimension r. By Lemma 3.3 we can partition G = Λ0 ⊔ Λ1 such that Λ0 is 2d-covered by Γ and for all γ ∈ Λ1 the set S′ ∪ {γ} has Γ-dimension at least r + 1. Thus, in our model,

n d

P(dim(S′ ∪ {γ}) ≤ dim(S′)) ≤

ω(γ) ≤

,

![image 39](<2014-bloom-quantitative-improvement-roth-theorem_images/imageFile39.png>)

γ∈Λ0

since Λ0 is 2d-covered by Γ. From this estimate, combined with the trivial observations that the empty set has Γ-dimension 0 and that Γ-dimension is non-decreasing, it follows that the probability that S has Γ-dimension d − k is at most the probability that k events with probability at most n/d occur in d independent trials, which is at most

d k

nkd−k ≤ nk/k!

- as required. By Lemma 3.1 it follows that for all λ ∈ G and integers t1,t2 ≤ m we have


∞

(4n)k k!

EEt♯

1,t2(S,Γ + λ) ≤ 4m

= 4me4n.

![image 40](<2014-bloom-quantitative-improvement-roth-theorem_images/imageFile40.png>)

k=0

Let 1 ≤ k ≤ 2m. For any distinct γ1,...,γk ∈ G the probability that γ1,...,γk ∈ S is at least

d−k

k

d k

ω(γ1)···ω(γk) 1 −

ω(γi)

.

k!

i=1

Since k ≤ d/2 we have k! k d ≥ (d/2)k. Furthermore, by the Cauchy-Schwarz inequality

k

ω(γi) ≤ (2m)1/2 ω 2 ≤ 2md−1 ≤ 1/2, so that the second factor is at least

i=1

k

ω(γi) ≥ e−2m.

exp −d

i=1

It follows that the probability that γ1,...,γk ∈ S is at least 2−5mdkω(γ1)···ω(γk). By linearity of expectation, assuming t1 + t2 ≤ m,

1+t2Et♯

EEt♯

1,t2(S,Γ + λ) ≥ 2−5mdt

1,t2(ω,Γ + λ), and so, for all λ ∈ G and 0 ≤ t1,t2 ≤ m,

Et♯

1−t2. From Lemma 3.2 it follows that

1,t2(ω,Γ + λ) ≤ 27me4nd−t

 

 

2

(m!)1/2( ω −2 1 d−1)t ((m − t)!)1/2

E2m(ω,Γ) ≤ 211me4nm! ω 22m

.

![image 41](<2014-bloom-quantitative-improvement-roth-theorem_images/imageFile41.png>)

0≤t≤m

For brevity let r = ω −2 2 d−2 ≥ m−1. By the Cauchy-Schwarz inequality the inner factor is at most

m! (m − t)!

rt ≤ (m + 1)

(erm)t ≤ (m + 1)2(erm)m,

(m + 1)

![image 42](<2014-bloom-quantitative-improvement-roth-theorem_images/imageFile42.png>)

0≤t≤m

0≤t≤m

say. In particular

E2m(ω,Γ) ≤ 213me4nm2m ω 22m rm = 213me4nm2md−2m, and the lemma follows.

4. Structure in Spectra

The results in the previous section are extremely general, and can be used to deduce facts about the dimensions of arbitrary sets from lower bounds on their additive energy. We shall use them to derive a structural result about the large spectrum of a function f : G → C, and for this we require a lower bound on the additive energy of such spectra. A suitable lower bound was provided by Shkredov

- [2008], who showed that if A ⊂ G with density α = |A|/N and ∆ ⊂ ∆η(A) then E2m(∆,{0}) ≫ η2mα|∆|2m. A simpler proof of this fact was given in Shkredov
- [2009]; the following is a simple generalisation of this proof.


- Lemma 4.1. Let ǫ ∈ [0,1]. For any B ⊂ G and η ∈ [0,1] let f : B → C and ω : G → R+ be supported on G. Then for all integers m ≥ 1


  η

 .

2m

f 1 f 2m/(2m−1) |B|1/2m

E2m(ω,∆ǫ(B)) ≥ ω 21m

− ǫ

![image 43](<2014-bloom-quantitative-improvement-roth-theorem_images/imageFile43.png>)

To recover the bound of Shkredov we set B = G and let ǫ → 0. Proof. Let χ be deﬁned by letting χ(γ) = cγω(γ), where cγ f(γ) = f(γ) . By construction whenever ω(γ) = 0 we have f(γ) ≥ η f 1, whence

![image 44](<2014-bloom-quantitative-improvement-roth-theorem_images/imageFile44.png>)

f(x)χ(x) = N−1

f(γ) χ(γ) = N−1

ω(γ) f(γ) ≥ N−1η f 1 ω 1 . By Ho¨lder’s inequality, however,

![image 45](<2014-bloom-quantitative-improvement-roth-theorem_images/imageFile45.png>)

![image 46](<2014-bloom-quantitative-improvement-roth-theorem_images/imageFile46.png>)

x

γ

γ

2m−1

2m

|f(x)|2m/(2m−1)

B(x)|χ(x)|2m .

![image 47](<2014-bloom-quantitative-improvement-roth-theorem_images/imageFile47.png>)

≤

f(x)χ(x)

x

x

x

It remains to note that, by the triangle inequality,

2m

B(x)|χ(x)|2m = N−2m

cγω(γ)γ(x)

B(x)

x

γ

x

≤ N−2m

ω(γ1)···ω(γm′ ) B(γ1 + ··· + γm − γ1′ − ··· − γm′ ) .

γ1,...,γm′

It follows that η2m f 21m ω 21m ≤ f 22mm/(2m−1)

ω(γ1)···ω(γm′ ) B(γ1 + ··· − γm′ )

γ1,...,γm′

≤ f 22mm/(2m−1) |B|E2m(ω,∆ǫ(B)) + ǫ |B|  ω 21m ,

and the proof is complete.

Finally, we can prove the technical heart of our argument, the aforementioned alternative to Chang’s lemma. Again, for our application we need a fairly general statement, but at ﬁrst glance the reader should take B = G and any ǫ > 0, so that ∆ǫ(B) = {0}.

- Theorem 4.1. Suppose that f : B → C and let α = f 1 / f ∞ |B|. Let ω : G → R+ be supported on ∆η(f) and let 0 ≤ ǫ ≤ exp(−8L(η)L(α)). There is a set ∆′ ⊂ ∆η(f) such that


ω(γ) ≥ 2−12η ω 1 and ∆′ is 214L(α)η−1-covered by ∆ǫ(B). Proof. Without loss of generality we may suppose that ω 1 = 1. Suppose ﬁrst that

γ∈∆′

ω 2 ≥ 2−12L(α)−1/2η and let ∆′ be a random set selected by including γ ∈ G independently with probability 213η−1L(α)ω(γ). Then, if ∆′ is this randomly chosen set we have, by Chernoﬀ’s inequality, that |∆′| ≤ 214η−1L(α) with probability at least 7/8, say, and

ω(γ) ≥ 213η−1L(α) ω 22 ≥ 2−11η,

E

γ∈∆′

and hence by Markov’s inequality we have γ∈∆′ ω(γ) ≥ 2−12η with probability

- at least 1/2, and the lemma follows. Otherwise, we let n = m = L(α) and d = ⌊212η−1m⌋ and apply Lemmata 4.1


and 3.1. By the above we can suppose that ω 2 ≤ 2−12L(α)−1/2η ≤ m1/2d−1, as is necessary for the application of Lemma 3.1. Lemma 4.1 implies that

2m

f 1 f 2m/(2m−1) |B|1/2m

− ǫ.

E2m(ω;∆ǫ(B)) ≥ η

![image 48](<2014-bloom-quantitative-improvement-roth-theorem_images/imageFile48.png>)

We have the trivial bound f 2m/(2m−1) ≤ f 1∞/2m f 1 1−1/2m, and hence if ǫ ≤ η2mα/2 then

E2m(ω;∆ǫ(B)) ≥ η2mα/2. By Lemma 3.1 either there is a set ∆′ such that

m d

ω(γ) ≥

![image 49](<2014-bloom-quantitative-improvement-roth-theorem_images/imageFile49.png>)

γ∈∆′

and ∆′ is 2d-covered by ∆ǫ(B), or

η2mα ≤ 219m+1m2md−2m. In particular,

d ≤ 210mη−1α−1/2m, which contradicts our initial choice of d and m, and the proof is complete.

Theorem 1.6 is a special case of this; to obtain it one simply sets B = G, lets ǫ → 0 and takes ω as the characteristic function of ∆η(f).

5. The density increment

In this section we show how to use the structural result Theorem 4.1 to obtain the usual density increment lemma which can be iterated to yield the main theorems. The density increment strategy originated with Roth [1953] but has seen various technical simpliﬁcations since which we incorporate here. Roughly speaking, the idea is to show that if A does not contain the expected number of solutions to (1) then it has large Fourier coeﬃcients, and this information can be translated into ﬁnding some group-like B ⊂ G such that |A ∩ B|/ |B| is larger than the expected |A|/N, and the argument can then be iterated until it halts due to the trivial bound |A ∩ B| ≤ |B|.

The ﬁrst lemma is the standard conversion of L2-information on the balanced function of a set to a density increment, a technique ﬁrst exploited for Roth’s theorem by Heath-Brown [1987] and Szemer´edi [1990].

- Lemma 5.1. Let f : B → [0,1] and f = f − αB, where α = f 1 / |B|. Suppose that


2

≥ να f 1 N. Then if B′ is a symmetric set such that for every γ ∈ Γ we have

f(γ)

γ∈Γ

B′(γ) ≥ 2−1 |B|, and furthermore |(2B′ + B)\B| ≤ 2−4να |B| then

f ∗ B′ ∞ ≥ (1 + 2−3ν)α|B′|. Proof. By hypothesis we have

2

2

≥ 2−2να f 1 |B′|2 N. In particular,

B′(γ)

f(γ)

γ

2

2

f ∗ B′ 22 = N−1

≥ 2−2να f 1 |B′|2 .

B′(γ)

f(γ)

γ

Expanding out the L2 norm we obtain that

|f ∗ B′(x)|2 + α2 B ∗ B′ 22 − 2α B ∗ B′,f ∗ B′ ≥ 2−2να f 1 |B′|2 . By hypothesis

x

B ∗ B′,f ∗ B′ − f 1 |B′|2 ≤ |B′|2 sup

f(z + x − y)

x,y∈B′

z ∈B

≤ |B′|2 |(2B′ + B)\B| ≤ 2−4ν f 1 |B′|2 .

It follows that

f ∗ B′ 22 ≥ (1 + 2−3ν)α f 1 |B′|2 . The left hand side is at most f 1 |B′| f ∗ B′ ∞ and the lemma follows.

The second lemma shows that if a set has small dimension then control on only a few elements gives control on the whole set.

- Lemma 5.2. If ∆ ⊂ G is d-covered by Γ then then there is Λ ⊂ G of size at most d such that if B has (4d)−1-control of Λ and Γ(1/8) then for every γ ∈ ∆ we have

B(γ) ≥ 2−1 |B|. Proof. By hypothesis there is some Λ ⊂ G such that |Λ| ≤ d and ∆ ⊂ Γ − Γ + Λ . Let γ ∈ ∆, so that there exists some γ0,γ1 ∈ Γ and ǫ ∈ {−1,0,1}Λ such that γ = γ0 − γ1 +

λ∈Λ

ǫλλ. By the triangle inequality, for every x ∈ B we have

|1 − γ(x)| ≤ |1 − γ0(x)| + |1 − γ1(x)| + d sup λ∈Λ

|1 − λ(x)| ≤ 1/2. It follows that

B(γ) − |B| ≤

x∈B

|1 − γ(x)| ≤ 2−1 |B| and the conclusion follows.

Finally, recalling Theorem 4.1 we see that to make use of Lemma 5.2 we will need to have good control on the spectrum of a given set. The following lemma gives a more useful criterion to ensure this.

- Lemma 5.3. If c > 0 and |(B + B′)\B| ≤ cǫ |B| then B′ has 2c-control of ∆ǫ(B). Proof. Choose γ such that B(γ) ≥ ǫ |B| and x ∈ B′. Then


|1 − γ(x)||B| ≤ ǫ−1

γ(y) −

γ(y)

y∈B

y∈B+x

≤ 2ǫ−1 |(B + B′)\B| ≤ 2c |B|.

We now combine all our tools thus far to prove the following eﬃcient density increment theorem.

- Theorem 5.1. Let B,B′ ⊂ G be any sets. Let A ⊂ B with density α = |A|/ |B|


and f : B′ → [−1,1] with density τ = f 1 / |B|. Let A(x) = A(x) − αB(x) and suppose that

2

= να f 1 |A|N. Then there is a ﬁnite set Λ ⊂ G of size

f(γ) A(γ)

γ

d = |Λ| ≤ 216L(τ)(να)−1 such that if a symmetric set B′′ ⊂ G has (4d)−1-control of Λ,

|(2B′′ + B)\B| ≤ 2−17να|B| , and

|(B′′ + B′)\B′| ≤ 2−4 exp(−24L(τ)L(να))|B′|

then there exists x such that

|(A − x) ∩ B′′| ≥ (1 + 2−16ν)α |B′′|. Proof. Let ∆ = ∆η(f) where η = να/2. In particular,

2

≤ 2−1να f 1 A 22 N ≤ 2−1να f 1 |A|N. In particular,

f(γ) A(γ)

γ ∈∆

2

≥ 2−1να f 1 |A|N.

f(γ) A(γ)

γ∈∆

We now perform a dyadic decomposition of ∆ into ∆i = ∆˜2iη(f), and apply Theorem 4.1 to each ∆i with the weight function

2

ω(γ) = f(γ) A(γ)

and

ǫ = exp(−24L(να)L(τ)) ≤ exp(−8L(η)L(τ)). Then, if ∆′i is the set provided by Theorem 4.1, we have

2

2

2−12

≤ (2iη)−1

f(γ) A(γ)

f(γ) A(γ)

γ∈∆i

γ∈∆′i

2

≤ 2 f 1

A(γ)

.

γ∈∆′i

Summing over all i ≥ 0 implies that

2

A(γ)

=

i γ∈∆′i

γ∈∆′

A(γ)

2

≥ 2−13να |A|N,

where ∆′ = ∪i≥0∆′i. Furthermore, since each ∆′i is 214L(τ)(2iη)−1-covered by ∆ǫ(B′) it follows that ∆′ is d-covered by ∆ǫ(B′) where

(2iη)−1 ≤ 216L(τ)(να)−1.

d ≤ 214L(τ)

i

Since B′′ satisﬁes |(B′′ + B′)\B′| ≤ 2−4ǫ |B′| it follows from Lemma 5.3 that B′′ has 2−3-control of ∆ǫ(B′). Hence by Lemma 5.2 there is a Λ of size d ≤ 216L(τ)(να)−1 such that if B′′ has (4d)−1-control of Λ then for every γ ∈ ∆′ we have

B′′(γ) ≥ 2−1 |B′′|. Since we also have |(2B′′ + B)\B| ≤ 2−17να |B| it follows from Lemma 5.1 that

|(A − x) ∩ B′′| ≥ (1 + 2−16ν)α |B′′| as required.

We now at last recall our purpose, which is to study the number of solutions to (1) in a given set A. This count is given by (c1 · A) ∗ (c2 · A),(−c3 · A) . It is now straightforward to use Parseval’s theorem and Theorem 5.1 to prove the following general density increment theorem, which shows that either this count is large or some dilation of A has increased density on some structured subset.

- Theorem 5.2. Suppose that B′ ⊂ B ⊂ G and we have A1 ⊂ B′ and A2,A3 ⊂ B each with relative densities αi. Let α = 2−1 min(2−5,α1,α2,α3) and suppose that


|(B′ + B)\B| ≤ 2−2α|B| . Then either

- (5) A1 ∗ A2,A3 ≥ 2−2α1α2α3 |B||B′| or there is a ﬁnite set Λ ⊂ G of size


d = |Λ| ≤ 219L(α)α−1 such that if a symmetric set B′′ has (4d)−1-control of Λ,

|(2B′′ + B)\B| ≤ 2−19α|B|, and

|(B′′ + B′)\B′| ≤ 2−4 exp(−25L(α)2))|B′| then there exists x ∈ G and i ∈ {2,3} such that

|(Ai − x) ∩ B′′| ≥ (1 + 2−18)αi |B′′|. Proof. Let Ai = Ai − αiB for i = 2,3 and A1 = A1 − α1B′. We have

A3 ∗ A−1 (x)

A1 ∗ A2(x)A3(x) =

A1 ∗ A2(x)A3(x) − α2

x

x

x∈B

−α3

A1 ∗ A2(x) + α2α3

B ∗ A1(x).

x∈B

x∈B

Observe that if A′ is supported on B′ and A is supported on B then

x∈B

In particular,

A′ ∗ A(x) − |A′||A| ≤ |A′||(B′ + B)\B| ≤ 2−2 |A′||A|.

x

A1 ∗ A2(x)A3(x) ≤

x

A1 ∗ A2(x)A3(x) − 2−1α1α2α3 |B||B′|.

By the triangle inequality either (5) is true or

γ

A1(γ) A2(γ) A3(γ) ≥ 2−2α1α2α3 |B′||B|N.

Applying the Cauchy-Schwarz inequality it follows that

γ

2

A1(γ) A2(γ)

γ

2

A1(γ) A3(γ)

≥ 2−4 |A1|2 α22α23 |B|2 N2.

It follows that for some i ∈ {2,3} we have

2

≥ 2−2 |A1|α2i |B|N

A1(γ) Ai(γ)

γ

and the conclusion then follows from Theorem 5.1.

6. Polynomial rings

For the ﬁrst demonstration of this method we choose G = Fq[t]/(p(t)), where p(t) is some prime of degree n, so that N = qn, and q is some odd prime power. We denote this group by AN. This group is rich enough to mirror the behaviour of the integers, while it has the signiﬁcant technical advantage of ﬁnite characteristic.

We ﬁx some coeﬃcients c1,c2,c3 ∈ Fq[t]\{0} such that c1+c2+c3 = 0, and some ﬁnite set A ⊂ AN. We suppose that N is large enough so that these coeﬃcients are coprime to p(t), and hence each acts faithfully on AN. We wish to study the function that counts solutions to c1x1 + c2x2 + c3x3 = 0 with xi ∈ A, denoted by

- (6) Υc(A) = (c1 · A) ∗ (c2 · A),(−c3 · A) .

We note that Υc(A) is invariant under dilations and translations of A.

We recall that both AN and AN are Fq-vector spaces of dimension n. Furthermore, any a ∈ AN acts on AN by letting (aγ)(x) = γ(ax). The Bohr space of Γ ⊂ AN is deﬁned as

B(Γ) = {x ∈ AN : γ(x) = 1 for all γ ∈ Γ}. If B is a Bohr space then the frequency set of B is

[B] = {γ ∈ AN : γ(x) = 1 for all x ∈ B}, and we deﬁne the rank of B as the Fq-dimension of [B].

- Lemma 6.1. Every Bohr space is an Fq-subspace of AN, and conversely, every Fq-subspace of AN is a Bohr space. Furthermore if B is a Bohr space then


- (7) |B| = q−rk(B)N.


Proof. We ﬁrst claim that if V is a Fq-subspace of AN then |V ||[V ]| = N. Since V is closed under addition it is easy to check that if γ  ∈ [V ] then V (γ) = 0, and if γ ∈ [V ] then V (γ) = |V |, and hence by Parseval’s identity,

2

2

= |[V ]||V |2

|V |N =

V (γ)

V (γ)

=

γ

γ∈[V ]

which proves our initial claim. The rest of the lemma follows easily. Corollary 6.1. If B is a Bohr space and c ∈ AN\{0} then c · B is also a Bohr space and

rk(c · B) = rk(B).

Since Bohr spaces are closed under addition our density increment tool, Theorem 5.2, takes the following particularly simple form in this setting.

- Theorem 6.1. Suppose that B ⊂ AN is a Bohr space and we have A1,A2,A3 ⊂ B with relative densities αi = |Ai|/ |B|. Let α = min(α1,α2,α3). Then either


A1 ∗ A2,A3 ≫ α1α2α3 |B|2 or there is a Bohr space B′ ⊂ B of rank

rk(B′) ≤ rk(B) + O(L(α)α−1) such that there exists x ∈ AN and i ∈ {2,3} such that

|(Ai − x) ∩ B′|) ≥ (1 + Ω(1))αi |B′|.

We may then iterate this density increment in the usual fashion to obtain a lower bound on Υc(A), from which Theorem 1.4 follows easily.

- Theorem 6.2. Suppose that c ∈ (Fq[t]\{0})3 is such that c1 + c2 + c3 = 0 and N is suﬃciently large, depending only on c. For any A ⊂ AN


Υc(A) ≥ expq −Oc(L(α)2α−1) N2.

Proof. Let ℓ = max1≤i≤3 deg ci. Let K be maximal such that there exists a sequence of Bohr spaces

AN = B0 ⊃ B1 ⊃ ··· ⊃ BK, and a sequence of sets Ai ⊂ Bi with density αi = |Ai|/ |Bi| such that, for 0 ≤ i < K, there exists Λi+1 of size O(L(α)α−i 1) and ai ∈ AN\{0} such that there exist Γi with Bi = B(Γi) and

- (8) Γi+1 ⊂ (ai · {1,...,t3ℓ} · Γi) ∪ Λi+1 and for some absolute constant c > 0 we have

αi+1 ≥ (1 + c) αi, and furthermore Υc(Ai+1) ≤ Υc(Ai). In particular,

1 ≥ αK ≥ (1 + c)K α, and hence K ≪ L(α). Furthermore it follows from (8) and induction that for 1 ≤ J ≤ K, if Λ0 = {0}, there exist a′j ∈ AN\{0} for 0 ≤ j < J such that

ΓJ ⊂ ΛJ ∪

J−1

j=0

a′j · {1,...,t3ℓ(J−j)} · Λj, and so in particular

- (9) rk(BK) ≪ℓ K

K

j=0

|Λj| ≪ℓ KL(α)α−1

K−1

i=0

(1 + c)−i ≪ℓ L(α)2α−1.

We will demonstrate that

- (10) Υc(AK) ≫ α3 |BK|2 and the theorem follows from (7) and (9).


Let B′ = B({1,...,t3ℓ}·ΓK). We observe that a·B′ ⊂ BK for all a ∈ Fq[t] with deg a ≤ 3ℓ and if B′′ is a Bohr space of the shape a · B′ and a = 0 then

[B′′] ⊂ a−1 · {1,...,t3ℓ} · ΓK.

Consider B′′ = c1c2c3 · B′ and B(i) = c−i 1 · B′′ for 1 ≤ i ≤ 3. Since B(i) ⊂ BK for 1 ≤ i ≤ 3

(AK ∗ β(1) + AK ∗ β(2) + AK ∗ β(3))(x) = 3 |AK|, and so for some x ∈ BK

x∈BK

AK ∗ β(1)(x) + AK ∗ β(2)(x) + AK ∗ β(3)(x) ≥ 3αK.

If for some 1 ≤ i ≤ 3 we have AK ∗ β(i)(x) ≥ αK(1 + c) then this contradicts the maximality of K, letting BK+1 = B(i) and AK+1 = AK − x. Otherwise, for 1 ≤ i ≤ 3,

AK ∗ β(i)(x) ≥ (1 − 4c)αK.

If we let A′i = ci · ((AK − x) ∩ B′′) then we have satisﬁed the hypotheses required to apply Theorem 6.1. It follows that either (10) holds or we may choose BK+1 to be the sub-Bohr set of BK with control of Λ and AK+1 to be a translation of some

- A′i. Since |Λ| = O(α−K1L(α))


and

αK+1 ≥ (1 + Ω(1))(1 − 4c)αK ≥ (1 + c)αK if we choose c suﬃciently small, this contradicts the maximality of K and thus concludes the proof.

7. Integers

We now prove Theorem 1.3 by applying these methods to the case G = ZN, where N is some large prime. Analogously to the case G = AN we ﬁx some coeﬃcients c1,c2,c3 ∈ Z\{0}, all coprime to N, such that c1 + c2 + c3 = 0 and for A ⊂ ZN deﬁne Υc(A) as in (6). For Γ ⊂ ZN and ρ : Γ → [0,2] we deﬁne the Bohr set Bρ(Γ) as

{n ∈ ZN : |γ(n) − 1| < ρ(γ)} . We call Γ the frequency set of B and ρ the width, and deﬁne the rank of B to be the size of Γ. In fact, when we speak of a Bohr set we implicitly refer to the triple (Γ,ρ,Bρ(Γ)), since the set Bρ(Γ) does not uniquely determine the frequency set or the width. Furthermore, if ρ : Γ → [0,2] and ρ′ : Γ′ → [0,2] then we deﬁne ρ ∧ ρ′ : Γ ∪ Γ′ → [0,2] by

 

ρ(γ) if γ ∈ Γ\Γ′ ρ′(γ) if γ ∈ Γ′\Γ, and min(ρ(γ),ρ′(γ)) if γ ∈ Γ ∩ Γ′.

(ρ ∧ ρ′)(γ) =



We no longer have the convenient property of Bohr sets being closed under addition, but Bourgain [1999] observed that certain Bohr sets have a weak version of this property suitable for our applications. A Bohr set Bρ(Γ) of rank d is regular if for all |κ| ≤ 2−6d−1 we have

Bρ(1+κ)(Γ) − |Bρ(Γ)| ≤ 26d|κ||Bρ(Γ)|.

If B = Bρ(Γ) then we write B(λ) for the Bohr set Bλρ(Γ). For further discussion of Bohr sets and proofs of the following basic lemmas see, for example, [Tao and Vu, 2006, Chapter 4].

- Lemma 7.1. For any Bohr set B there exists λ ∈ [1/2,1] such that B(λ) is regular.


- Lemma 7.2. If ρ′ : Γ′ → [0,2] then

|Bρ∧ρ′(Γ ∪ Γ′)| ≥

γ∈Γ′

(ρ′(γ)/4)|Bρ(Γ)| .

Furthermore, if B is a Bohr set of rank d then |B(λ)| ≥ λO(d) |B|.

The following lemma follows easily from the observation that if c ∈ ZN\{0} then c · Bρ(Γ) = Bρ(c · Γ).

- Lemma 7.3. For any Bohr set B and c ∈ Z∗N the set c · B is also a Bohr set of rank rk(B), and furthermore for any λ > 0


c · (B(λ)) = (c · B)(λ).

The notion of regularity allows us to exert the required amount of additive control, and our density increment tool, Theorem 5.2, becomes the following.

- Theorem 7.1. There exists an absolute constant c > 0 such that the following holds. Let B ⊂ ZN be a regular Bohr set of rank d where d ≤ exp(cL(α)2). Let A1,A2 ⊂ B and A3 ⊂ B(δ), each with relative densities αi. Let α = min(c,α1,α2,α3) and suppose that B(δ) is also regular and cd−1α/4 ≤ δ ≤ cd−1α. Then either


- (11) A1 ∗ A2,A3 ≫ α1α2α3 |B||B(δ)| or there is a regular Bohr set B′ of rank

rk(B′) ≤ d + O(L(α)α−1) and size

- (12) |B′| ≥ exp(−O(L(α)2(d + L(α)α−1)))|B| such that there exists x ∈ ZN and i ∈ {1,2} with

|(Ai − x) ∩ B′| ≥ (1 + c)αi |B′|. Proof. We ﬁrst observe that since B is regular we have that

- (13) |(B(δ) + B)\B| ≪ dδ |B| ≤ 2−2α |B|,

provided δ is suﬃciently small. The hypotheses of Theorem 5.2 are now met, so that either (11) holds or there is a ﬁnite set Λ ⊂ G of size l = O(L(α)α−1) such that if a symmetric set B′ has (4l)−1-control of Λ,

- (14) |(2B′ + B)\B| ≤ 2−19α |B|, and
- (15) |(B′ + B(δ))\B(δ)| ≤ 2−4 exp(−25L(α)2))|B(δ)| then there exists x ∈ ZN and i ∈ {1,2} such that


|(Ai − x) ∩ B′| ≥ (1 + 2−18)αi |B′|.

Let ρ′ : Λ → [0,2] be deﬁned as ρ′(λ) = 1/4l for all λ ∈ Λ. If B = Bρ(Γ) then let B∗ = Bδρ∧ρ′(Γ∪Λ), and let B′ = B∗(δ′) for some δ′ to be chosen later, but chosen such that B′ is regular. Clearly, B′ is a regular Bohr set of rank d + O(L(α)α−1) with (4l)−1-control of Λ by choice of ρ′. Provided δ′ ≤ 1/2 we have that 2B′ ⊂ B(δ),

- and hence (14) is satisﬁed, arguing as for (13). Furthermore, since B(δ) is regular and B′ ⊂ B(δδ′) it follows that

|(B′ + B(δ))\B(δ)| ≪ dδ′ |B(δ)| ,

- and hence (15) is satisﬁed for some δ′ ≫ exp(−O(L(α)2)))d−1. Finally, by Lemma 7.2 we have


|B′| ≥ (δ′)O(l+d) |B∗| ≥ l−O(l)δd(δ′)O(l+d) |B|, and (12) follows from our bounds on δ, δ′ and l, and the proof is complete.

This density increment lemma may then be iterated in the standard fashion to yield a lower bound for Υc(A).

- Theorem 7.2. Let c ∈ (Z\{0})3 be such that c1 + c2 + c3 = 0. For any prime N suﬃciently large, depending only on c, and any A ⊂ ZN we have


Υc(A) ≥ exp −Oc L(α)4α−1 N2.

Theorem 1.3 follows by embedding {1,...,N} into a suitable subinterval I of ZN′, where N′ ≪c N is some prime large enough such that if x1,x2,x3 ∈ I is a solution to c1x1 + c2x2 + c3x3 = 0 in ZN′ then it is also a solution in {1,...,N}.

Proof. Let K be maximal such that there exists a sequence of regular Bohr sets ZN = B0 ⊃ B1 ⊃ ··· ⊃ BK,

each with frequency set Γi, rank di, width ρi and a sequence of sets Ai ⊂ Bi with density αi = |Ai|/ |Bi| such that, for 0 ≤ i < K we have

di+1 ≤ di + O(L(α)α−i 1) ≤ exp(O(L(α)2)),

- (16) |Bi+1| ≥ exp(−O(L(α)2(di + L(α)α−i 1)))|Bi|, αi+1 ≥ (1 + c) αi,


and furthermore Υc(Ai+1) ≤ Υc(Ai). In particular, this will follow provided Ai+1 is a subset of a dilation of a translation of Ai. We observe that

1 ≥ αK ≥ (1 + c)K α,

and hence K ≪ L(α). Furthermore, for 0 ≤ j ≤ K we have the estimate dj ≪ L(α)α−1, and so

K

di N ≥ exp(−O(L(α)4α−1))N.

|BK| ≥ exp −Oc L(α)2

i=0

We will demonstrate that

Υc(AK) ≫ exp(−O(dKL(α)2))|BK|2 and the theorem follows.

For brevity, let B′ = BK(ρ′), B′′ = B′(ρ′) = BK(ρ′ρ′′), and B′′′ = B′′(ρ′′′) = BK(ρ′ρ′′ρ′′′), where ρ′, ρ′′ and ρ′′′ will be chosen later, but chosen such that all Bohr sets considered are regular. Let

B(1) = c2c3 · B′′, B(2) = c1c3 · B′′, and B(3) = c2c3 · B′′′

so that in particular if ρ′′ ≪ 1/c1c2c3 we have B(i) ⊂ B′ for 1 ≤ i ≤ 3, and hence by the regularity of BK

AK ∗ β(i)(x) − |AK| ≤ |(B′ + BK)\BK| ≪ dρ′ |BK|.

x∈BK

In particular for any ǫ > 0 we may choose ρ′ ≫ǫ d−1αK such that

(AK ∗ β(1) + AK ∗ β(2) + AK ∗ β(3))(x) ≥ (3 − ǫ)|AK|,

x∈BK

and hence, for some x ∈ B, AK ∗ β(1)(x) + AK ∗ β(2)(x) + AK ∗ β(3)(x) ≥ (3 − ǫ)αK.

If AK ∗ β(i)(x) ≥ α(1 + c) for some 1 ≤ i ≤ 3 then this contradicts the maximality of K, letting BK+1 = B(i) and AK+1 = (AK − x) ∩ BK+1. In particular note that B(i) also has rank dK and

B(i) ≥ |B′′′| ≥ exp(−O(dKL(ρ′ρ′′ρ′′′)))|BK|,

and we shall see that our choices for the ρ parameters give the lower bound (16). Otherwise, for 1 ≤ i ≤ 3, if we choose ǫ suﬃciently small depending on c, then for 1 ≤ i ≤ 3

AK ∗ β(i)(x) ≥ (1 − c)αK. Let Ai = ci · (A′ − x) ∩ ci · B(i), and observe that

c3 · B(3) = c1c2c3 · B′′′ ⊂ (c1c2c3 · B′′)(ρ′′′),

and hence there exists ρ′′′ ≫ d−K1αK such that we are in a position to apply Theorem 7.1. In particular, either

Υc(AK) ≫ α3K |B′′||B′′′| ≫ exp(−O(dKL(α)2))|BK|2 or there is a regular Bohr set B♯ of rank

d♯ ≤ d + O(L(α)α−K1) and size

B♯ ≥ exp(−O(L(α)2(d+L(α)α−K1)))|B′′| ≥ exp(−O(L(α)2(d+L(α)α−K1)))|BK|, and i ∈ {1,2} such that

(Ai − x) ∩ B♯ ≥ (1 + Ω(1))(1 − c)αK B♯ ≥ (1 + c)αK B♯ ,

if we choose c suﬃciently small, which contradicts the maximality of K. This concludes the proof.

8. Arithmetic progressions in sumsets

In this section we sketch how our improved structural result for spectra may be combined with the methods of Sanders [2008] to prove Theorem 1.2. The diﬀerence lies in an improvement of the iteration lemma, Lemma 6.4 of Sanders [2008]. In particular, Theorem 1.2 follows immediately from the proof of Sanders [2008], replacing the use of its Lemma 6.4 by the following quantitatively superior version.

- Lemma 8.1. Let B ⊂ ZN be a regular Bohr set and A1,A2 ⊂ B with densities α1 and α2 respectively. For any σ ∈ (0,1] either


- (1) there is a regular Bohr set B′ = B(ρ) such that A1 + A2 contains at least a proportion 1 − σ of B′ and δ′ ≫ α2d−1, or
- (2) there is a regular Bohr set B′′ ⊂ B of rank rk(B′′) ≤ rk(B) + O(α−1L(σ))


and width

ρ(B′′) ≫ ρ(B)(rk(B))−1 exp(−O(L(σ)L(α))) such that for some absolute constant c > 0

A1 ∗ β′′ ∞ A2 ∗ β′′ ∞ ≥ α1α2(1 + c). Proof. Let Ai = Ai − αB, and B′ = B(ρ) for some suitable ρ ≫ α4d−1 such that

- B′ is regular. Arguing as in the proof of Lemma 6.4 in Sanders [2008] we see that either the ﬁrst case holds or there is some S ⊂ B′ and 1 ≤ i ≤ 2 such that


2

S(γ) ≫ αi |Ai||S|N.

Ai(γ)

γ∈ ZN

It follows from Theorem 5.1 that if we choose our Bohr set B′′ ⊂ B′ such that it has Ω(l−1)-control of Λ, where Λ is a set of size l ≪ α−i 1L(σ) and

|(B′′ + B′)\B′| ≪ exp(−L(σ)L(αi))|B′|

then Ai ∗ β′′ ≥ (1 + c)αi. The proof is then completed as in the proof of Lemma 6.4 in Sanders [2008].

Acknowledgements

The author would like to thank Julia Wolf and Trevor Wooley for their advice and helpful comments on a preliminary draft of this paper, and Kevin Henriot for pointing out several ﬂaws in an earlier version of the argument.

References Bateman, M. and N. H. Katz “New bounds on cap sets” J. Amer. Math. Soc. 25

(2012): 585–613. Behrend, F. A. “On sets of integers which contain no three terms in arithmetical progression” Proc. Nat. Acad. Sci. U. S. A. 32 (1946): 331–332. Bloom, T. F. “Translation invariant equations and the method of Sanders” Bull. Lond. Math. Soc. 44 (2012): 1050–1067. Bourgain, J. “On triples in arithmetic progression” Geom. Funct. Anal. 9 (1999): 968–984. Bourgain, J. “Roth’s theorem on progressions revisited” J. Anal. Math. 104 (2008): 155–192. Chang, M.-C. “A polynomial bound in Freiman’s theorem” Duke Math. J. 113

(2002): 399–419. Croot, E.,  Laba, I. and O. Sisask “Arithmetic progressions in sumsets and Lpalmost-periodicity” Combin. Probab. Comput. 22 (2013): 351–365.+ Green, B. “Arithmetic progressions in sumsets” Geom. Funct. Anal. 12 (2002): 584–597. Heath-Brown, D. R. “Integer sets containing no arithmetic progressions” J. London Math. Soc. 35 (1987): 385–394. Liu, Y.-R. and C. V. Spencer “A generalization of Roth’s theorem in function ﬁelds” Int. J. Number Theory 5 (2009): 1149–1154. Meshulam, R. “On subsets of ﬁnite abelian groups with no 3-term arithmetic progressions” J. Combin. Theory Ser. A 71 (1995): 168–172.

Roth, K. F. “On certain sets of integers” J. London Math. Soc. 28 (1953): 104–109. Sanders, T. “Additive structures in sumsets” Math. Proc. Cambridge Philos. Soc.

144 (2008): 289–316. Sanders, T. “On Roth’s theorem on progressions” Ann. of Math. 174 (2011): 619–

636. Sanders, T. “On certain other sets of integers” J. Anal. Math. 116 (2012): 53–82. Shkredov, I. D. “On sets of large trigonometric sums” Izv. Math. 72 (2008): 149–

168. Shkredov, I. D. “On sumsets of dissociated sets” Online J. Anal. Comb. 4 (2009). Szemer´edi, E. “Integer sets containing no arithmetic progressions” Acta Math. Hun-

gar. 56 (1990): 155–158. Tao, T., and V. Vu. Additive Combinatorics, 1st ed. Cambridge University Press, 2006.

Thomas Bloom, Department of Mathematics, University of Bristol, University Walk, Clifton, Bristol BS8 1TW, United Kingdom

E-mail address: matfb@bristol.ac.uk

