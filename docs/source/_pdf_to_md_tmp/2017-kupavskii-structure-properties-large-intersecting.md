arXiv:1710.02440v2[math.CO]5Feb2019

# Structure and properties of large intersecting families

Andrey Kupavskii∗

Abstract

We say that a family of k-subsets of an n-element set is intersecting, if any two of its sets intersect. In this paper we study diﬀerent extremal properties of intersecting families, as well as the structure of large intersecting families. We also give some results on k-uniform families without s pairwise disjoint sets, related to Erd˝os Matching Conjecture.

We prove a conclusive version of Frankl’s theorem on intersecting families with bounded maximal degree. This theorem, along with its generalizations to crossintersecting families, implies many results on the topic, obtained by Frankl, Frankl and Tokushige, Kupavskii and Zakharov and others.

We study the structure of large intersecting families, obtaining some general structural theorems which generalize the results of Han and Kohayakawa, as well as Kostochka and Mubayi.

We give degree and subset degree version of the Erd˝os–Ko–Rado and the Hilton– Milner theorems, extending the results of Huang and Zhao, and Frankl, Han, Huang and Zhao. We also extend the range in which the degree version of the Erd˝os Matching conjecture holds.

## 1 Introduction

Let [n] := {1, . . ., n} and denote 2[n] the power set of [n]. For integers a ≤ b we put [a, b] := {a, a + 1, . . ., b} and for integers 0 ≤ k ≤ n we denote [nk] the collection of all k-element subsets (k-sets) of [n]. Any collection of sets F ⊂ 2[n] we call a family. We call a family intersecting, if any two sets from it intersect. A “trivial” example of such family is all sets containing a ﬁxed element. We call a family non-trivial, if not all of its sets contain the same element.

![image 1](<2017-kupavskii-structure-properties-large-intersecting_images/imageFile1.png>)

![image 2](<2017-kupavskii-structure-properties-large-intersecting_images/imageFile2.png>)

One of the oldest and most famous results in extremal combinatorics is the Erd˝os– Ko–Rado theorem:

- Theorem 1 ([3]). Let n ≥ 2k > 0 and consider an intersecting family F ⊂ [nk] . Then


|F| ≤ nk−−11 . Moreover, for n > 2k the only families attaining this bound are the families of all k-sets containing a given element.

Answering a question of Erd˝os, Ko, and Rado, Hilton and Milner [16] found the largest non-trivial intersecting family of k-sets. Up to permutation of the ground sets, it is the family consisting of the set [2, k + 1] and all sets that contain 1 and intersect [2, k + 1]. Such family has size nk−−11 − n−k−k−11 + 1, which is much smaller than nk−−11 provided n is

![image 3](<2017-kupavskii-structure-properties-large-intersecting_images/imageFile3.png>)

∗Moscow Institute of Physics and Technology, Ecole Polytechnique F´ed´erale de Lausanne; Email: kupavskii@yandex.ru Research supported by the grant RNF 16-11-10014.

1

large as compared to k.

This paper is mostly concerned with the properties of large intersecting families. It is separated in several relatively independent parts covering diﬀerent topics. Below we give the summary of the topics covered and the structure of the paper.

- Section 3: In this section we give a conclusive version of the Frankl’s degree theorem (see Theorems 2, 3 in the next section). The main result gives the precise dependence of size of the family on (lower bound on) the number of sets not containing the most popular element. The result then is extended to cover the equality case, as well as the weighted case and the case of cross-intersecting families. It, in particular, strengthens the results of [5], [12], [24].
- Section 4: In this section we address the question, what is the structure of large intersecting families. Unlike in Section 3, where, due to the Kruskal-Katona theorem, we have to deal with lexicographical families only (for deﬁnitions and necessary results, see the next section), in this section we work with general families. We prove several results, which, in particular, cover a large part of results of [14], [20], and extend them much farther. One important advantage, as compared to the results of [20], is that the results do not require n to be large w.r.t. k.
- Section 5: In this section we obtain degree and subset degree versions of the Erd˝os-KoRado theorem and the Hilton-Milner theorem. This answers some of the questions posed by Huang and extends the results of [17], [13], [8].
- Section 6: In this section we obtain an upper bound on the minimum degree of a family


F ⊂ [nk] , which does not contain s pairwise disjoint sets. The results extends the analogous result of [17] for large k. The problem in question may be seen

as a degree vesion of the Erd˝os Matching Conjecture.

Some of the results in Section 4 depend on the results from Section 5, while Section 6 is relatively independent from the previous two sections. Section 6 is completely independent.

In the next section we give some of the deﬁnitions and results crucial for the paper. In Section 7 we give some concluding remarks and state several open problems.

## 2 Preliminaries

The degree δ(i) of an element i is the number of sets from the family containing it. For a family F the diversity γ(F) is the quantity |F|−∆(F), where ∆(F) is the maximal degree of an element in F. Below we discuss the connection between the diversity and the size of an intersecting family.

![image 4](<2017-kupavskii-structure-properties-large-intersecting_images/imageFile4.png>)

![image 5](<2017-kupavskii-structure-properties-large-intersecting_images/imageFile5.png>)

![image 6](<2017-kupavskii-structure-properties-large-intersecting_images/imageFile6.png>)

We will need the following result due to Kupavskii and Zakharov [24]. It is a slightly stronger version of Frankl’s result [5]:

- Theorem 2 ([24]). Let n > 2k > 0 and F ⊂ [nk] be an intersecting family. Then, if γ(F) ≥ nn−−uk−−11 for some real 3 ≤ u ≤ k, then


|F| ≤

n − 1 k − 1

+

n − u − 1 n − k − 1

−

n − u − 1 k − 1

. (1)

The bound from Theorem 2 is sharp for integer u, as witnessed by the example

Hu := {A ∈

[n] k

: [2, u] ⊂ A} ∪ {A ∈

[n] k

: 1 ∈ A, [2, u] ∩ A = ∅}.

We note that the case u = k of Theorem 2 is precisely the Hilton-Milner theorem.

To allow the reader to compare Theorem 2 and the original Frankl’s theorem, let us state it here.

- Theorem 3 ([5]). Let n > 2k > 0 and F ⊂ [nk] be an intersecting family. Then, if ∆(F) ≤ nk−−11 − n−k−u−11 for some integer 3 ≤ u ≤ k, then

|F| ≤

n − 1 k − 1

+

n − u − 1 n − k − 1

−

n − u − 1 k − 1

.

We note that Theorem 3 is immediately implied by Theorem 2, while in the other direction it is not true, even for the integer values of u.

One of the key ingredients in the proofs of several theorems is the Kruskal-Katona theorem. Below we state it in terms of lexicographical orderings. Let us ﬁrst give some deﬁnitions. A lexicographical order (lex) < on the sets from [nk] is an order, in which

![image 7](<2017-kupavskii-structure-properties-large-intersecting_images/imageFile7.png>)

- A < B iﬀ the minimal element of A \ B is smaller than the minimal element of B \ A.


For 0 ≤ m ≤ nk let L(m, k) be the collection of m largest sets with respect to lex. We say that two families A, B are cross-intersecting, if for any A ∈ A, B ∈ B we have

![image 8](<2017-kupavskii-structure-properties-large-intersecting_images/imageFile8.png>)

- A ∩ B = ∅.


- Theorem 4 ([21],[19]). Suppose that A ⊂ [na] , B ⊂ [nb] are cross-intersecting. Then the families L(|A|, a), L(|B|, b) are also cross-intersecting.


## 3 The complete diversity version of Frankl’s theorem

In this section we study in detail the relationship between the diversity of an intersecting family and its size. First, note that, if the value of diversity is given precisely, then it is very easy to determine the largest intersecting family with such diversity using Theorem 4. Studying the size of an intersecting family with given upper bounds on diversity is not interesting: in general, the smaller the diversity is, the larger families with such diversity exist.

In this section we obtain a strengthened version of Theorem 2, which will tell exactly, how large an intersecting family may be, given a lower bound on its diversity. We give all “extremal” values of diversity and the sizes of the corresponding families.

The diﬃculty to obtain such a version of Theorem 2 is that, while Theorem 4 gives a very strong and clear characterisation of families with ﬁxed diversity, the size of the family is not monotone w.r.t. diversity (the size of the largest family with a given diversity does not necessarily decrease when diversity increases, although it is true in most cases), and an extra eﬀort is needed to ﬁnd the right point of view.

We will give two versions of the main theorem of this section. First, we give a “numerical” version with explicit sharp bounds on the size of an intersecting family. It may be more practical to apply in some cases, but it is diﬃcult to grasp, what is hidden behind the binomial coeﬃcients in the formulation. Thus, later in the section (and as an

intermediate step of the proof), we will give a “conceptual” version of our main theorem. We note that the proof that we present is completely computation-free. In the later parts of this section we present strengthenings and generalisations of our main result. We will settle the equality case in Theorems 6, 7, as well as consider the weighted case and a generalization to the case of general cross-intersecting families.

We note that the main results of the section are meaningful for any k ≥ 3. The following representation of natural numbers is important for the (classic form of)

the Kruskal-Katona theorem. Given positive integers γ and k, one can always write down γ uniquely in the k-cascade form:

![image 9](<2017-kupavskii-structure-properties-large-intersecting_images/imageFile9.png>)

γ =

ak k

+

ak−1 k − 1

+ . . . +

as s

, ak > ak−1 > . . . > as ≥ 1.

For the sake of comparison, let us state the classical version of the Kruskal-Katona theorem (equivalent to Theorem 4).

- Theorem 5 ([21],[19]). Let F ⊂ [nk] and put


∂(F) := F′ ∈

[n] k − 1

: F′ ⊂ F for some F ∈ F .

k + . . . + a

If |F| = a

s , then

s

k

|∂(F)| ≥

ak k − 1

+

ak−1 k − 1

+ . . . +

as s − 1

.

To state our theorem, we need to represent the diversity of an intersecting family in

- a cascade form. Given a number γ, let us write it in the (n − k − 1)-cascade form in the following particular way:


γ =

n − b1 n − k − 1

+

n − b2 n − k − 2

+ . . . +

n − bs

b

n − s − 1

,

- where 1 ≤ b1 < b2 < . . . < bs

b

. Deﬁne Tγ := {b1, . . ., bs

b

} and put Sγ := {bs

b

}∪([2, bs

b

]\Tγ). Note that Sγ ∪ Tγ = [2, bs

b

] and Sγ ∩ Tγ = {bs

b

}. We assume that Sγ = {a1, . . ., as

a

},

- where 2 ≤ a1 < . . . < as


= bs

. We call a number γ resistant, if the following holds:

a

b

![image 10](<2017-kupavskii-structure-properties-large-intersecting_images/imageFile10.png>)

- 1. sa = |Sγ| ≤ k, sb = |Tγ| ≤ k − 1;
- 2. bi > 2i + 2 for each i ∈ [sb];
- 3. For convenience, we assume that nk−−34 is a resistant number.


Thus, in particular, any integer γ > nk−−34 will have nk−−34 as one of the members in the (n − k − 1)-cascade form, so such γ is not resistant.

Let 1 = γ1 < γ2 < . . . < γm = nk−−34 be all the resistant numbers. Put γ0 = 0 for convenience.

- Theorem 6. Let n > 2k ≥ 6. Consider an intersecting family F ⊂ [nk] . Suppose that γl−1 < γ(F) ≤ γl for l ∈ [m] and that the representation of γl in the (n − k − 1)-cascade form is


n − bs

n − b2 n − k − 2

n − b1 n − k − 1

b

, then

+ . . . +

+

γl =

n − s − 1

n − as

n − a2 n − k − 1

n − a1 n − k

a

|F| ≤

+ γl, (2) where {b1, . . ., bs

+ . . . +

+

n − sa

} = Sγ. The expression in the right hand side of (2) strictly decreases as l increases. Moreover, the presented bound is sharp: for each l = 1, . . ., m there exists an inter-

} = Tγ and {a1, . . ., as

a

b

secting family with diversity γl which achieves the bound in (2).

Let us ﬁrst try to familiarize the reader with the statement of the theorem. We have γi = i for i = 1, . . ., k −3. Indeed, for 1 ≤ γ < n−k −1 we have γ = nn−−kk−−11 + nn−−kk−−22 + . . . + nn−−kk−−γγ . Thus, for any such γ we have Tγ = [k + 1, k + γ] and Sγ = [2, k] ∪ {γ}. Thus, the ﬁrst condition of the deﬁnition of a resistant number is satisﬁed if γ ≤ k − 1. However, the second condition is only satisﬁed when k + γ > 2γ + 2, which is equivalent to γ ≤ k − 3 (or when k = 3, γ = 1). From the discussion above we also get that for

- k > 3 γk−2 = n− n−k−k1 = n − k.


- Proposition 1. The bound in Theorem 6 is always at least as strong as the bound in Theorem 2 for intersecting F ⊂ [nk] with diversity γ(F) ≤ nk−−34 . Proof. Let us ﬁrst compare the statement of Theorem 6 with the statement of Theorem 2


for γl := nn−−uk−−11 with integer u. Such γl is resistant for any u ∈ [3, k] (note that nk−−34 is resistant due to the exceptional condition 3 in the deﬁnition). Moreover, it is not diﬃcult

to see that, if we substitute such γl in (2), then we will get the bound

|F| ≤

n − 2 n − k

+ . . . +

n − u − 1 n − k − u + 1

+ γl =

n − 1 n − k

−

n − u − 1 n − k − u

+

n − u − 1 n − k − 1

,

which is exactly the bound (1). However, we are getting it here in more relaxed assumptions: while we know that this bound is sharp for γ(F) = γl, Theorem 6 also tells us that for γ(F) > γl the bound would be strictly worse (and provides us with a possibility to extract, how much worse). Moreover, even if γl−1 < γ(F) ≤ γl, we are still getting the same upper bound.

Moving to the proof of the proposition, the function in the right hand side of (1) monotone decreasing as γ(F) increases (and thus u decreases). Therefore, to show that the bound (2) is stronger than (1), it is suﬃcient to show it for values γl, l = 0, . . ., m. But for each of these values the bound (2) is sharp, so (1) can be only weaker than (2) for these values.

Thus, clearly, Theorem 6 is a strengthening of Theorem 2. As a matter of fact, we can replace the bound in (1) with any monotone decreasing

![image 11](<2017-kupavskii-structure-properties-large-intersecting_images/imageFile11.png>)

![image 12](<2017-kupavskii-structure-properties-large-intersecting_images/imageFile12.png>)

![image 13](<2017-kupavskii-structure-properties-large-intersecting_images/imageFile13.png>)

![image 14](<2017-kupavskii-structure-properties-large-intersecting_images/imageFile14.png>)

function of γ(F), provided that the bound holds for each γl.

Finally, let us mention that we state Theorem 6 only for γ(F) ≤ nk−−34 , since Theorem 2 already gives us the bound |F| ≤ nk−−22 + 2 nk−−23 if γ(F) ≥ nk−−34 , and we cannot

get any better bound in this range. However, we are going to analyze the cases when the equality in the inequality for |F| above can be attained. It is worth mentioning that the intersecting family {F ∈ [nk] : |F ∩ [3]| ≥ 2} attains the bound above on the cardinality, and has diversity nk−−23 . We also note that in a recent work [23] the author managed to prove that for n > ck with some constant independent of k there are no intersecting families F ⊂ [nk] with diversity bigger than nk−−23 .

Our next goal is to state the “conceptual” version of Theorem 6. We will need certain preparations. We will use the framework and some of the ideas from [9], as well as from [24]. First of all, we pass to the cross-intersecting setting in a standard way: given an intersecting family F, we consider two families

F(1) :={F \ {1} : 1 ∈ F ∈ F} and F(¯1) :={F : 1 ∈/ F ∈ F},

and, applying Theorem 4, from now on and until the end of the section assume that F(1) = L(|F(1)|, k − 1), F(¯1) = L(|F(¯1)|, k). Note that F(1), F(¯1) ⊂ 2[2,n]. For shorthand we denote A := F(1), B := F(¯1). In the remaining part dedicated to Theorem 6 we will be mostly working with the set [2, n], in order not to confuse the reader and to keep clear the relationship between the diversity of intersecting families and the sizes of pairs of cross-intersecting families.

Both A and B are determined by their lexicographically last set. In this section we use lexicographical order on 2[2,n], which is deﬁned as follows: A < B iﬀ A ⊃ B or the minimal element of A\B is smaller than the minimal element of B\A. Let us recall some notions and results from [9] related to the Kruskal-Katona theorem and cross-intersecting families. For a set S ⊂ [n], 1 ∈ S and |S ∩ [2, n]| ≤ a, we deﬁne

L(S, a) := A ∈

[2, n] a

: A < S ∩ [2, n] .

For example, the family {G ∈ [210,n] : 2 ∈ G, G ∩ {3, 4} = ∅} is the same as the family L(S, 10) for S = {2, 4}. If G = L(S, a) for a certain set S, then we say that S is the

characteristic set of G. Note that, for convenience, we assume that 1 ∈ S (motivated by the fact that S is the characteristic set for the subfamily of all sets containing 1 in the original family), while T ⊂ [2, n].

We say that two sets S ⊂ [n] and T ⊂ [2, n] form a resistant pair, if the following holds. Assuming that the largest element of T is j, we have

![image 15](<2017-kupavskii-structure-properties-large-intersecting_images/imageFile15.png>)

- 1. S ∩ T = {j}, S ∪ T = [j], |S| ≤ k, |T| ≤ k;
- 2. for each 4 ≤ i ≤ j we have |[i]∩S| < |[i]\S| (this condition, roughly speaking, says that in each [i] there are more elements in T than in S);
- 3. For convenience, we include the pair T = {2, 3, 4}, S = {1, 4} in the list of resistant pairs.


Note that 2 implies that T ⊃ {2, 3, 4} for each resistant pair. There is a close relationship between this notion and the notion of a resistant number, which we discuss a bit later. Let us ﬁrst give the “conceptual” characteristic set version of Theorem 6. For convenience, we put T0 = [2, n] to correspond to the empty family.

- Theorem 7. Let n > 2k ≥ 6. Consider all resistant pairs Sl ⊂ [n], Tl ⊂ [2, n], where


- l ∈ [m]. Assume that T0 < T1 < T2 < . . . < Tm. Then |L(Sl−1, k − 1)| + |L(Tl−1, k)| > |L(Sl, k − 1)| + |L(Tl, k)| for each l ∈ [m], (3)


and any cross-intersecting pair of families A ⊂ [2k−,n1] , B ⊂ [2k,n] with |L(Tl−1, k)| < |B| ≤ |L(Tl, k)| satisﬁes

|A| + |B| ≤ |L(Sl, k − 1)| + |L(Tl, k)|. (4) In terms of intersecting families, if F ⊂ [nk] is intersecting and |L(Tl−1, k)| < γ(F) ≤

|L(Tl, k)|, then |F| ≤ |L(Sl, k − 1)| + |L(Tl, k)|.

First of all, we remark that the intersecting part is clearly equivalent to the second statement of the cross-intersecting part. Second, Proposition 2 below shows that the families L(Sl, k − 1) and L(Tl, k) are cross-intersecting and thus (4) is sharp. Now let us deduce Theorem 6 from Theorem 7.

Reduction of Theorem 6 to Theorem 7. For any set T ∈ [2, n] with the largest element sb we can compute the size of the family |L(T, k − 1) as follows. Find the ﬁrst element

- b1 ∈ [2, n], which is missing from T, and consider the family with characteristic set


T1 := (T ∩ [b1]) ∪ {b1}. The size of this family is n−b

k−b1+1 = n−b

n−k−1 , since actually T1 = [2, b1]. Since T1 < T, this family is a subfamily of L(T, k − 1). At each new step we ﬁnd the next (not found yet) element bi, which is missing from T, the set Ti := (T∩[bi])∪bi, and count the sets which belong to L(Ti, k−1)\L(Ti−1, k−1) = F ∈ [2k,n] : F∩[bi] = Ti . Their number is precisely n−b

1

1

k−|Ti| = n−b

n−k−|[bi]\Ti| . But since we are stopping at every element that is not included in T, we get that |[bi] \ Ti| = |[bi−1 \ Ti−1| + 1 = . . . = i. Therefore, the last binomial coeﬃcient is n−b

i

i

n−k−i . At some point Ti = T, and we stop the procedure, including the sets F ∈ [2k−,n1] that satisfy F ∩ [sb] = T. We get that

i

|L(T, k − 1)| =

n − b1 n − k − 1

+

n − b2 n − k − 2

+ . . . +

n − bs

b

n − sb − 1

,

the (n − k − 1)-cascade form! Moreover, we know that the set {b1, . . ., bs

} is exactly the set Tγ from before the deﬁnition of a resistant number, and we have Tγ = ([2, sb]\T)∪{sb} and thus T = Sγ.

b

Therefore, if S, T is a resistant pair, then, representing γ := |L(T, k − 1)| in an (n − k−1)-cascade form, we get that T = Sγ and S ∩[2, n] = Tγ. This immediately shows that Tγ and Sγ satisfy condition 1 of the deﬁnition of a resistant number. The implication in the other direction follows in the same way. Condition 2 of the deﬁnition of a resistant pair is equivalent to the statement that for each i 1 + |Tγ ∩ [i]| < |[2, i] \ Tγ|, which is, in turn, the same as saying bi > 2i + 2. Finally, it is clear that γ = nk−−34 correspond to the characteristic set {2, 3, 4}.

We conclude that Tl, Sl form a resistant pair if and only if |L(Tl, k − 1)| is a resistant number. Doing calculations as above, one can conclude that

|L(Sl, k)| =

n − a1 n − k

+

n − a2 n − k − 1

+ . . . +

n − as

a

n − sa

.

Given that, it is clear that the inequality (3) is equivalent to the statement saying that the right hand side of (2) is strictly monotone, and that the (2) is equivalent to (4).

Finally, the sharpness claimed in Theorem 6 follows right away from the fact that the inequality (4) in Theorem 7 is expressed in terms of families. That is, the pair L(Sl, k−1) and L(Tl, k) provides us with such an example.

![image 16](<2017-kupavskii-structure-properties-large-intersecting_images/imageFile16.png>)

![image 17](<2017-kupavskii-structure-properties-large-intersecting_images/imageFile17.png>)

![image 18](<2017-kupavskii-structure-properties-large-intersecting_images/imageFile18.png>)

![image 19](<2017-kupavskii-structure-properties-large-intersecting_images/imageFile19.png>)

Before proving Theorem 7, let us ﬁrst shed some light on pairs of cross-intersecting lexicographic families. We say that two sets S and T in [2, n] strongly intersect, if there exists a positive integer j, such that S ∩T ∩[2, j] = {j} and S ∪T ⊃ [2, j]. The following easy proposition was proven in [9]:

![image 20](<2017-kupavskii-structure-properties-large-intersecting_images/imageFile20.png>)

- Proposition 2 ([9]). Let A and B be subsets of [2, n], |A| ≤ a, |B| ≤ b, and |[2, n]| = n − 1 ≥ a + b. Then L(A, a) and L(B, b) are cross-intersecting iﬀ A and B strongly intersect.

We say that A ⊂ [2a,n] and B ⊂ [2b,n] form a maximal cross-intersecting pair, if

![image 21](<2017-kupavskii-structure-properties-large-intersecting_images/imageFile21.png>)

whenever A′ ⊂ [2a,n] and B′ ⊂ [2b,n] are cross-intersecting with A′ ⊃ A and B′ ⊃ B, then necessarily A = A′ and B = B′ holds.

The following proposition from [9] is another important step in our analysis.

- Proposition 3 ([9]). Let a and b be positive integers, a + b ≤ n − 1. Let P and Q be non-empty subsets of [2, n] with |P| ≤ a, |Q| ≤ b. Suppose that P and Q intersect strongly in their last element. That is, there exists j, such that P ∩ Q = {j} and P ∪ Q = [2, j]. Then L(P, a) and L(Q, b) form a maximal pair of cross-intersecting families.


Inversely, if L(m, a) and L(r, b) form a maximal pair of cross-intersecting families, then it is possible to ﬁnd sets P and Q such that L(m, a) = L(P, a), L(r, b) = L(Q, b) and P, Q satisfy the above condition.

We note that it may be helpful to interpret the strong intersection property, as well as the lexicographical order etc. in terms of {0, 1}-vectors: 1 on the i-th position if i is contained in the corresponding set, and 0 otherwise.

Now we pass on to the proof of the cross-intersecting version of Theorem 7. Fix a cross-intersecting pair of families A, B as in the theorem. There are three important reduction steps, which restrict the class of cross-intersecting families which we need to consider. First, as we have already mentioned, we assume that A = L(S, k − 1) and

- B = (T, k) for some characteristic sets S, T. Second, in view of Proposition 3, we may assume that A = L(S, k − 1), B = L(T, k) for some sets S, T that strongly intersect in their last element. Note also that |[2, n]| = n − 1 ≥ k + (k − 1), so we do not have to worry about this condition in the propositions above.


Recall that we aim to maximize |A| + |B| given a lower bound on |B|. The third reduction step is the following lemma.

- Lemma 1. Consider a pair of cross-intersecting families A ⊂ [2k−,n1] , B ⊂ [2k,n] . Suppose


- that A = L(S, k−1), B = L(T, k) for some sets S ⊂ [n], T ⊂ [2, n] that strongly intersect in their last element j.


Assume that S and T do not form a resistant pair, that is, there exists 4 ≤ i ≤ j, such that [i] \ S ≤ S ∩ [i] . Put T′ := [i] \ S and choose S′ so that it strongly intersects with T′ in its largest element. Then the families A′ ⊂ [2k−,n1] , B ⊂ [2k,n] with characteristic sets S′, T′ are cross-intersecting and satisfy |A′| + |B′| ≥ |A| + |B| and |B′| > |B|.

Moreover, if [i] \ S < S ∩ [i] , then we may conclude that |A′| + |B′| > |A| + |B|.

Proof of Lemma 1. First, recall that 1 ∈ S. Since S′ and T′ are strongly intersecting, the families A′, B′ are cross-intersecting. Next, clearly, T′ T and thus B′ B. Therefore, we only have to prove |A| + |B| ≤ |A′| + |B′|.

Consider the following families:

- Pa := P ∈

[2, n] k − 1

: P ∩ [i] = [2, i] ∩ S ,

- Pb := P ∈


[2, n] k

: P ∩ [i] = [i] \ S .

Most importantly, we have A\ Pa = A′, B ∪Pb = B′. Let us show, e.g., the ﬁrst equality. We have S′ < S < S ∩ [i], therefore A′ ⊂ A ⊂ L(S ∩ [i], k − 1). On the other hand, we claim that S′ and S ∩[i] are two consecutive sets in the lexicographic order on [i]. Indeed, assume that the largest element of T′ is j′. If j′ = i, then S′ ⊃ S ∩ [i], (S′ \ S)∩ [i] = {i}, which proves it in this case. If j′ < i, then [j′ + 1, i] ⊂ S ∩ [i], j′ ∈/ S ∩ [i]. It is easy to see that the set that precedes S ∩ [i] in the lexicographic order on [i] “replaces” [j′ + 1, i] with {j′}, that is, it is S′. Therefore,

A \ A′ ⊂ L(S ∩ [i], k − 1) \ A′ = L(S ∩ [i], k − 1) \ L(S′, k − 1) = Pa,

which, together with the fact that Pa and A′ are disjoint, is equivalent to the equality we aimed to prove.

Next, consider a bipartite graph G with parts Pa, Pb and edges connecting disjoint sets. Then, due to the fact that A and B are cross-intersecting, (A ∩ Pa) ∪ (B ∩ Pb) is an independent set in G.

The graph G is biregular, and therefore the largest independent set in G is one of its parts. We have |Pa| = ns−i

, |Pb| = ns−i

, where sa = k−|[i]∩S|, sb = k−|[i]\S|. By the condition from the lemma, we have sb ≥ sa, and, since n−i ≥ sa+sb, we have |Pb| ≥ |Pa|. We conclude that |Pb| is the largest independent set in G, so |Pb| ≥ (A ∩ Pa) ∪ (B ∩ Pb), and therefore

a

b

|A′| + |B′| − (|A| + |B|) = |Pb| − |A ∩ Pa| − |B ∩ Pb| ≥ 0.

If [i] \ S < S ∩ [i] , then |Pb| > |Pa| and Pb is the unique independent set of maximal size in G. Thus, we have strict inequality in the displayed formula above.

![image 22](<2017-kupavskii-structure-properties-large-intersecting_images/imageFile22.png>)

![image 23](<2017-kupavskii-structure-properties-large-intersecting_images/imageFile23.png>)

![image 24](<2017-kupavskii-structure-properties-large-intersecting_images/imageFile24.png>)

![image 25](<2017-kupavskii-structure-properties-large-intersecting_images/imageFile25.png>)

Our next goal is to understand how do the resistant pairs behave. More speciﬁcally, we aim to show that (3) holds: that sizes of resistant cross-intersecting families are increasing as the size of the second family decreases.

- Lemma 2. Consider a resistant pair of cross-intersecting families A ⊂ [2k−,n1] , B ⊂


[2,n] [2,n] k−1 , B′ ⊂ [2k,n] with characteristic sets S′, T′. Assume also that T = T′.

- k , with characteristic sets S, T, respectively, and another such resistant pair A′ ⊂


If T′ < T, then |B′| < |B| and |A| + |B| < |A′| + |B′|. Roughly speaking, while for general lexicographic pairs of families the size is not

monotone w.r.t. the lexicographic order, it is monotone for resistant pairs, which are maximal with respect to the properties that interest us.

Remark that, since T′ < T, then T′ = {2, 3, 4} and thus S′, T′ must satisfy the second condition from the deﬁnition of a resistant pair. We also note that we do not use the property that S, T form a resistant pair. The proof also works for T′ = T0(= [2, n]).

The proof of this lemma is based on biregular bipartite graphs and is very similar to the proof of Lemma 1, although is a bit trickier.

Proof. First of all, it is clear that in the conditions of the lemma we have |B′| < |B|. The rest of the proof is concerned with the inequality on the sums of sizes. We will consider two cases depending on how do the sets T and T′ relate.

Case 1. TTT′ TT T. Find the smallest i, such that one of the sets contain i, while the other does not. Since T′ < T, we clearly have i ∈ T′, i ∈/ T. Consider the set T′′ = T′ ∩ [i]. Then we clearly have T′ < T′′ < T and T′′ ⊂ T′. Accordingly, put S′′ to be {i} ∪ ([i] \ T′′), and consider the cross-intersecting families A′′ ⊂ [2k−,n1] , B′′ ⊂ [2k,n] , which have characteristic vectors S′′ and T′′, respectively. First, note that A′′ and B′′ is a resistant pair: it follows from the deﬁnition of T′′. We claim that |A′′| + |B′′| > |A| + |B|.

We prove the inequality above as in Lemma 1, but the roles of S and T are now switched. Consider a bipartite graph G with parts

- Pa := P ∈

[2, n] k

: P ∩ [i] = [2, i] \ T ,

- Pb := P ∈


[2, n] k

: P ∩ [i] = [i] ∩ T ,

and edges connecting disjoint sets. Similarly, we have A∪ Pa = A′′, B \ Pb = B′′. Indeed, let us verify, e.g., the second equality. All sets P such that P ∩ [i] < T′′ are in B and in

- B \ Pb, as well as in B′′, since T′′ T ∩ [i]. On the other hand, if we restrict to [i], the sets T ∩ [i] and T′′ are consecutive in the lexicographic order, and so any set B from B such that B > T′′ must satisfy B ∩ [i] = T ∩ [i]. Therefore, B \ B′′ ⊂ Pb and B \ Pb = B′′.


Since A and B are cross-intersecting, the set (A ∩ Pa) ∪ (B ∩ Pb) is independent in G. On the other hand, the largest independent set in G has size max{|Pa|, |Pb|}. Since the pair A, B is resistant (and that i is not the last element of T), we have that

|[i] ∩ T| = |[i] \ S| > |[i] ∩ S| = |[i] \ T|, which implies |Pa| = |[2 n,i−]\iT| > |[ ni]−∩Ti | = |Pb|, and thus Pa is the (unique) maximal independent set in G. We have

|A′′| + |B′′| − (|A| + |B|) = |Pa| − |A ∩ Pa| − |B ∩ Pb| > 0,

and the desired inequality is proven. Therefore, when comparing T′ and T, we may replace T with T′′, or rather assume that T ⊂ T′. We have reduced Case 1 to the following case.

Case 2. TTT′ ⊇ TTT. Arguing inductively, we may assume that |T′ \ T| = 1, and that T′ \ T = {i} for some i ∈ [2, n]. Note that in that case i is the last element of T′, S′, and that T′ ∩ S′ = {i}. Consider a bipartite graph G with parts

- Pa := P ∈

[2, n] k − 1

: P ∩ [i] = S′ ∩ [2, i] ,

- Pb := P ∈


[2, n] k

: P ∩ [i] = [i] \ S′ ,

and edges connecting disjoint sets. As before, we have A ∪ Pa = A′, B \ Pb = B′. Using the fact that |[i] \ S′| > |[i] ∩ S′|, we again conclude that |A′| + |B′| > |A| + |B|.

![image 26](<2017-kupavskii-structure-properties-large-intersecting_images/imageFile26.png>)

![image 27](<2017-kupavskii-structure-properties-large-intersecting_images/imageFile27.png>)

![image 28](<2017-kupavskii-structure-properties-large-intersecting_images/imageFile28.png>)

![image 29](<2017-kupavskii-structure-properties-large-intersecting_images/imageFile29.png>)

Now let us put the things together.

Proof of Theorem 7. First of all, (3) follows from Lemma 2. Next, given a pair of crossintersecting families A, B, we may assume using Proposition 3 that their characteristic sets S, T strongly intersect in their last coordinate. Using Lemma 1, we may further replace them with a resistant pair A′, B′ with characteristic vectors S′, T′, such that T < T′. Therefore, if Tl−1 < T and Tl−1 = T, then Tl < T′, and therefore the pair L(Sl, k −1), L(Tl, k) has at least as big sum of cardinalities as A′ and B′. This completes the proof of the theorem.

We only have to add that, although Tm = {2, 3, 4}, Sm = {1, 4} do not satisfy the second requirement of the deﬁnition of a resistant pair, it does not pose any problems. We still may apply Lemma 2 to this pair. Moreover, if initially the characteristic set T of the family A satisﬁes Tm−1 < T < Tm, then, using Lemma 1 it would be eventually reduced to Tm, and thus we may apply it as in other cases.

![image 30](<2017-kupavskii-structure-properties-large-intersecting_images/imageFile30.png>)

![image 31](<2017-kupavskii-structure-properties-large-intersecting_images/imageFile31.png>)

![image 32](<2017-kupavskii-structure-properties-large-intersecting_images/imageFile32.png>)

![image 33](<2017-kupavskii-structure-properties-large-intersecting_images/imageFile33.png>)

Let us discuss some possible strengthenings and generalizations of Theorems 6 and 7. First of all, let us determine, for which T, Tl−1 < T < Tl, it is possible to have equality in (4), given that A, B are determined by a strongly intersecting pair of sets S, T, |S|, |T| ≤

- k, which intersect in their last element. We say that a pair of strongly intersecting sets S, T as above is Tl-neutral, if T is obtained in the following recursive way:

![image 34](<2017-kupavskii-structure-properties-large-intersecting_images/imageFile34.png>)

- 1. Tl is Tl-neutral;
- 2. If T′ is Tl-neutral, then the set T := T′ ∪ {x} is Tl-neutral, where x = 2|T′|.


In practice, this means that, starting from a set Tl, we add the element 2|Tl|, and then continue adding every other element.

We remark that it is not diﬃcult to see that any Tl-neutral pair S, T actually satisﬁes Tl−1 < T ≤ Tl. Let us also note that T = T′: indeed, from the deﬁnition of a resistant pair, the largest element in Tl is at most 2|Tl| (actually, it is at most 2|Tl|−3 for all l < m and equal to 2|Tl| − 2 in the case l = m), and every newly added element (via part 2 of the recursive deﬁnition) is bigger by 2 than the previously added element.

Theorem 8. Let n > 2k ≥ 6. Consider a pair A ⊂ [2k−,n1] , B ⊂ [2k,n] deﬁned by strongly intersecting sets S, T that intersect in their largest element. If Tl−1 < T ≤ Tl for some

- l = 0, . . ., m, then equality in (4) holds if and only if the pair S, T is Tl-neutral.


Proof. First, let us show that any Tl-neutral pair would have equality in (4). We do it inductively. It is clear for a pair involving Tl itself. Assuming it holds for T′, let us prove that it holds for T := T′ ∪ {2|T′|}.

Consider the pairs of cross-intersecting families A, B, A′, B′, corresponding to the Tlneutral pairs of sets S, T and S′, T′, respectively. Looking in the proof of Lemma 1, given that |Pa| ≤ |Pb|, the equality in |A|+|B| ≤ |A′|+|B′| occur if and only if, ﬁrst |Pa| = |Pb|, and, second, A \ A′ = Pa, B \ B′ = Pb. Indeed, in a connected biregular bipartite graph there are only two possible independent sets of maximal size: its parts.

Consider the set T = T′ ∪ {x} and the corresponding set S. By the deﬁnition of a neutral set, we have

|[x] ∩ S| = |[x] \ S|. Therefore, applying the argument of Lemma 1 with

- Pa := P ∈

[2, n] k − 1

: P ∩ [x] = [2, x] ∩ S ,

- Pb := P ∈


[2, n] k

: P ∩ [x] = [x] \ S ,

We get that k − 1 − |[2, x] ∩ S| = k − |[x] \ S|, which implies |Pa| = |Pb|. Moreover,

- A \ A′ = Pa, B \ B′ = Pb, since the sets S′ and S are consecutive in the lexicographical order on [x], and the same for T, T′. Therefore, |A′| + |B′| = |A| + |B|.


In the other direction, take a set T, Tl−1 < T ≤ Tl, and its pair S. Consider the corresponding pair of cross-intersecting families A, B. Then it is easy to see that T ⊃ Tl. (Otherwise, either T > Tl, or T must contain and thus precede some other resistant set, which precedes Tl, and this would contradict the position of T in the ordering.) Assuming that x is the last element in T, we must have

|[i] ∩ S| < |[i] \ S| for 4 ≤ i ≤ x − 1.

Indeed, otherwise, considering the bipartite graph G with parts Pa, Pb as displayed above for that i, we would get that |Pa| ≤ |Pb| and both Pa ∩ A and Pb ∩ B are non-empty. In this case |Pa ∩ A| + |Pb ∩ B| < |Pa|, which means that the pair A′, B′ deﬁned by the characteristic sets T′ := T ∩ [i] and its pair S′ would satisfy |A′| + |B′| > |A| + |B|. Moreover, T′ ⊃ Tl, so T < T′ ≤ Tl and |A′|+|B′| ≤ |L(Sl, k −1)|+|L(Tl, k)|. This would contradict the equality in (4).

Therefore, since S, T are not resistant, we have |[x] ∩ S| = |[x] \ S|.

(We cannot have “>”, since otherwise we would have “≥” for i = x − 1.) Removing x, we get a set T′, and conclude that x = 2|T′|. By induction on the size of the set T, we may assume that T′ is Tl-neutral. But then T is Tl-neutral as well.

![image 35](<2017-kupavskii-structure-properties-large-intersecting_images/imageFile35.png>)

![image 36](<2017-kupavskii-structure-properties-large-intersecting_images/imageFile36.png>)

![image 37](<2017-kupavskii-structure-properties-large-intersecting_images/imageFile37.png>)

![image 38](<2017-kupavskii-structure-properties-large-intersecting_images/imageFile38.png>)

A slight modiﬁcation of this argument (with an extension of the deﬁnition of a neutral pair to the ones that start with Tm+1 := {2, 3}) gives the following:

- Proposition 4. Let n > 2k ≥ 6. For any intersecting F ⊂ [nk] with nk−−34 < γ(F) <


n−3

k−2 we have |F| < nk−−22 + 2 nk−−23 .

Recall that there are intersecting families F ⊂ [nk] for both γ(F) = nk−−34 and nk−−23 that have size nk−−22 + 2 nk−−23 .

Next, our techniques allow us to give a weighted version of Theorems 6 and 7. Assume that, instead of maximising the expression |F| = ∆(F) + γ(F) with a given lower bound on γ(F), we are maximising the expression ∆(F) + cγ(F) with some c > 1. (In terms of cross-intersecting families, we are maximising the expression |A| + c|B|.) Then the following is true.

- Theorem 9. Let n > 2k ≥ 6. Consider all resistant pairs Sl ⊂ [n], Tl ⊂ [2, n], where


- l = 0, . . ., m. Assume that T0 < T1 < T2 < . . . < Tm. Put C := n−k−k−33 > 1. Then |L(Sl−1, k − 1)| + C|L(Tl−1, k)| ≥ |L(Sl, k − 1)| + C|L(Tl, k)| for each l ∈ [m], (5)


![image 39](<2017-kupavskii-structure-properties-large-intersecting_images/imageFile39.png>)

and any cross-intersecting pair of families A ⊂ [2k−,n1] , B ⊂ [2k,n] with |L(Tl−1, k)| < |B| ≤ |L(Tl, k)| satisﬁes |A| + C|B| ≤ |L(Sl, k − 1)| + C|L(Tl, k)|.

In terms of intersecting families, if F ⊂ [nk] is intersecting and |L(Tl−1, k)| < γ(F) ≤ |L(Tl, k)|, then ∆(F) + Cγ(F) ≤ |L(Sl, k − 1)| + C|L(Tl, k)|.

Proof. The proof of this theorem follows the same steps as the proof of Theorem 7. We sketch the proof of the cross-intersecting version of the theorem. Using Lemma 1, we may assume that A and B form a resistant pair (indeed, otherwise, replacing A, B with

- A′|, |B′ which satisfy |A′| + |B′| ≥ |A| + |B|, |B′| > |B| deﬁnitely increases the value of |A| + C|B|). Then, looking at the proof of Lemma 2, we see that in each of the cases the


, ns−i

bipartite graph G had parts of sizes ns−i

, where sa + sb = 2k − i and sa > sb. We also know that sb ≤ k − 3. Therefore, even if we put weight ns−i

a

b

/ ns−i

on each vertex of the part Pb and weight 1 on each vertex of the part Pa, we can still conclude that the independent set of the largest weight in G is Pa, and the rest of the argument works out as before. We have

a

b

n−i

- sa

![image 40](<2017-kupavskii-structure-properties-large-intersecting_images/imageFile40.png>)

n−i

- sb


(n − i − sb) sa

≥

![image 41](<2017-kupavskii-structure-properties-large-intersecting_images/imageFile41.png>)

(n − 2k + sa) sa

=

![image 42](<2017-kupavskii-structure-properties-large-intersecting_images/imageFile42.png>)

(n − k − 3) k − 3

≥

. (6)

![image 43](<2017-kupavskii-structure-properties-large-intersecting_images/imageFile43.png>)

Therefore, substituting n−k−k−33 as the weight in the Pb part will work.

![image 44](<2017-kupavskii-structure-properties-large-intersecting_images/imageFile44.png>)

![image 45](<2017-kupavskii-structure-properties-large-intersecting_images/imageFile45.png>)

![image 46](<2017-kupavskii-structure-properties-large-intersecting_images/imageFile46.png>)

![image 47](<2017-kupavskii-structure-properties-large-intersecting_images/imageFile47.png>)

![image 48](<2017-kupavskii-structure-properties-large-intersecting_images/imageFile48.png>)

- Corollary 1. Let n > 2k ≤ 6. For any intersecting family F ⊂ [nk] , γ(F) ≤ nk−−34 , we have |∆(F)| + n−k−k−33γ(F) ≤ nk−−11 .


![image 49](<2017-kupavskii-structure-properties-large-intersecting_images/imageFile49.png>)

If, additionally, F is non-trivial, then |∆(F)|+ n−k−k−33γ(F) ≤ nk−−11 − n−k−k−11 + n−k−k−33. Is not diﬃcult extend the considerations of this section to the case of cross-intersecting

![image 50](<2017-kupavskii-structure-properties-large-intersecting_images/imageFile50.png>)

![image 51](<2017-kupavskii-structure-properties-large-intersecting_images/imageFile51.png>)

families A ⊂ [na] , B ⊂ [nb] , a < b. The wording of Theorem 7 would stay practically the same. One just need to adjust the deﬁnition of a resistant pair. Note that, unlike before

in this section, here we will work with cross-intersecting families on [n] (and not [2, n]).

We say that two sets S, T ⊂ [n] form an (a, b)-resistant pair, if the following holds. Assuming that the largest element of T is j, we have

![image 52](<2017-kupavskii-structure-properties-large-intersecting_images/imageFile52.png>)

- 1. S ∩ T = {j}, S ∪ T = [j], |S| ≤ a, |T| ≤ b;
- 2. for each b − a + 2 ≤ i ≤ j we have |[i] ∩ S| − a < |[i] \ S| − b;
- 3. The pair T = {1, . . ., b − a + 2}, S = {1, b − a + 2} is resistant.


Again, for convenience, we put T0 = [2, n] to correspond to the empty family and Tm+1 = {1, b − a + 1} to be an analogue of the set {2, 3} in this case, where m is the number of resistant pairs. Here is the theorem, which is an analogue of Theorems 7, 8, 9 and Proposition 4 in the case of general cross-intersecting families. Its proof is a straightforward generalization of the proofs of the respective theorems, thus we omit it.

- Theorem 10. Let a, b > 0, n > a + b. Consider all (a, b)-resistant pairs Sl ⊂ [n], Tl ⊂ [2, n], where l ∈ [m]. Assume that T0 < T1 < T2 < . . . < Tm < Tm+1.


1. Then |L(Sl−1, a)| + |L(Tl−1, b)| > |L(Sl, a)| + |L(Tl, b)| for each l ∈ [m], (7)

and any cross-intersecting pair of families A ⊂ [na] , B ⊂ [nb] with |L(Tl−1, b)| < |B| ≤ |L(Tl, b)| satisﬁes

|A| + |B| ≤ |L(Sl, a)| + |L(Tl, b)|. (8) With an obvious generalization of the notion of a neutral pair, if the families L(|A|, a), L(|B|, b) have characteristic sets S, T, then we have equality in (8) if and only if S, T is a Tl-neutral pair.

- 2. The same conclusion could be made with |B|, |L(Tl−1, b)| |L(Tl, b)| replaced with

C|B|, C|L(Tl−1, b)| C|L(Tl, b)|, where C is a constant, C < n−a−b−22.

![image 53](<2017-kupavskii-structure-properties-large-intersecting_images/imageFile53.png>)

- 3. Denote t := a − b − 1. For n+a−t−21 < |B| < a n−+1t we have

|A| + |B| <

n a

−

n + t a

+

n + t a − 1

=

n a

−

n + t − 1 a

+

n + t − 1 a − 2

.

For both Tm+1 = [b + 1 − a], Tm = [b + 2 − a] and the corresponding Sm+1, Sm we have equality in the inequality above for L(Si, a), L(Ti, b), i = m, m + 1 (note that the second family has cardinality a n−+1t and na+−t−21 , respectively).

This theorem generalizes and strengthens many results on cross-intersecting families, in particular, the theorem for cross-intersecting families proven in [24] and the following theorem due to Frankl and Tokushige [12]

Theorem 11 (Frankl, Tokushige, [12]). Let n > a + b, a ≤ b, and suppose that families F ⊂ [na] , G ⊂ [nb] are cross-intersecting. Suppose that for some real number α ≥ 1 we have nn−−αa ≤ |F| ≤ n n−−a1 . Then

|F| + |G| ≤

n b

+

n − α n − a

−

n − α b

. (9) The deduction is similar to the one we made for Theorems 2 from Theorem 6. One easy corollary of ((7) and part 3 of) Theorem 10, which also appeared in [24] and

other places, is as follows: Corollary 2 ([24]). Let a, b > 0, n > a + b. Let A ⊂ [na] , B ⊂ [nb] be a pair of cross-intersecting families. Then, if |B| ≤ n+aa−−1b−1 , then

|A| + |B| ≤

n a

. (10)

Moreover, the displayed inequality is strict unless |B| = 0. If nb−−jj ≤ |B| ≤ n+aa−−1b−1 for j ∈ [b − a + 1, b], then

|A| + |B| ≤

n a

−

n − j a

+

n − j b − j

. (11)

Moreover, if the left inequality on B is strict, then the inequality in the displayed formula above is also strict.

Note that the values |B| = nb−−jj correspond to resistant pairs in Theorem 10.

- 4 Beyond Hilton-Milner theorem


Several authors aimed to determine precisely, what are the largest intersecting families in

[n]

k with certain restrictions. One of such questions was studied by Han and Kohayakawa, who determined precisely, what is the largest family of intersecting families that is neither contained in the Erd˝os-Ko-Rado family, nor in the Hilton-Milner family. In our terms, the question is simply as follows: what is the largest intersecting family with γ(F) ≥ 2?

The proof of Han and Kohayakawa is quite technical and long. Kruskal-Katona-type arguments allow for a very short and simple proof in the case k ≥ 5. For i ∈ [k] let us put

Ji := [2, k+1]∪[i+1, k+i]∪ F ∈

[n] k

: 1 ∈ F, F ∩[2, k+1] = ∅, F ∩[i+1, k+i] = ∅ .

We note that Ji ⊂ [nk] and that Ji are intersecting. Moreover, γ(Ji) = 2 for i > 1 and

- J1 is the Hilton-Milner family.


- Theorem 12 ([14]). Let n > 2k, k ≥ 4. Then any intersecting family F with γ(F) ≥ 2 satisﬁes


n − k − 2 k − 2

n − k − 1 k − 1

n − 1 k − 1

−

−

|F| ≤

+ 2, (12) moreover, for k ≥ 5 the equality is attained only on the families isomorphic to J2.

We note that Han and Kohayakawa proved their theorem for k = 3, and also resolved the uniqueness case for k = 4. Unfortunately, this cannot be done in a simple way using our methods. A slightly weaker version of the theorem above (without uniqueness) is a consequence of one of the results obtained by Hilton and Milner [16] (see [14]).

It is not so diﬃcult to deduce Theorem 12 from Theorem 4 directly, but using Theorems 6, 7 makes it even easier. Proof. In terms of Theorem 6, we know that γi = i for i ∈ [k − 3], and γk−2 = n − k. Substituting l = 2 for k ≥ 5 in (2), we get

|F| ≤

n − 2 n − k

+

n − 3 n − k − 1

+ . . . +

n − k n − 2k + 2

+

n − k − 2 n − 2k + 1

+ 2 =

n − 1 n − k

−

n − k n − 2k + 1

+

n − k − 2 n − 2k + 1

+2 =

n − 1 n − k

−

n − k − 1 n − 2k

−

n − k − 2 n − 2k

+2,

which is exactly the right hand side of (12). We know that this is sharp, due to an example isomorphic to J2 (it is also isomorphic to the corresponding example from Theorem 6).

Since the right hand side of (2) strictly decreases as l increases, we may conclude that for k ≥ 5 any family F with γ(F) > γ2 = 2 will have strict inequality in (2) with l = 2, and thus a strict inequality in (12). Moreover, for k = 4 the lexicographic family with diversity γ2 = n − 4 has the same cardinality as J2, displayed above (due to Theorem 8, or via direct calculation), and no family with γ > γ1 can have larger cardinality.

Therefore, the bound (12) is proven, and to complete the proof, we should only show

that for k ≥ 5 among the intersecting families F ⊂ [nk] with γ(F) = 2 all families achieving equality in (12) are isomorphic to J2. This could be done by a simple computation.

Any (maximal) intersecting family F ⊂ [nk] with γ(F) = 2 is uniquely determined by the intersection of the two sets A, B, which are not containing the most popular element, and thus is isomorphic to one of the Ji, i ∈ [k].

Using exclusion-inclusion formula for Ji, we conclude that (the number of k-sets that contain 1 and do not intersect either A or B) = (the number of sets that contain 1 and miss A) + (the number of sets that contain 1 and miss B) − (the number of sets that contain 1 and miss both A and B) = 2 n−k−k−11 − n−2k+k|−A1∩B|−1 , and this function clearly strictly increases as the intersection size of A and B decreases, and so we “loose” more and more sets containing 1 as i become smaller. Therefore, the unique (up to isomorphism) maximal intersecting family F with γ(F) = 2 is J2. Theorem is proven.

![image 54](<2017-kupavskii-structure-properties-large-intersecting_images/imageFile54.png>)

![image 55](<2017-kupavskii-structure-properties-large-intersecting_images/imageFile55.png>)

![image 56](<2017-kupavskii-structure-properties-large-intersecting_images/imageFile56.png>)

![image 57](<2017-kupavskii-structure-properties-large-intersecting_images/imageFile57.png>)

Let us denote Fl the maximal intersecting family with Fl(¯1) = L(l, k). Note that

- J2 is isomorphic to F2. It is not diﬃcult to see that, in terms of Theorem 7, for l = 0, . . ., k − 3 we have Fl(¯1) = L(Tl, k) and, therefore, Fl(1) = L(Sl, k) (see the analysis after Theorem 7). We also have Fn−k = L(Tk−2, k). Moreover, it is not diﬃcult to see that for k − 1 < l < n − k we have Fl ⊂ Fn−k (indeed, we have Fl(1) = Fn−k(1) for this range). Also, using Theorems 7 and 8 (or by direct calculation), we can conclude that


|Fk−1| < |Fk−2| = |Fn−k|. The next theorem is another application of our method.

- Theorem 13. Assume that k ≥ 5 and n > 2k. Consider an intersecting family F ⊂ [nk] , such that ∆(F) = δ(1). Assume that | ∩F∈F(¯1) F| ≤ k − 2. Then

|F| ≤ |J3|, (13) with the equality only possible if F is isomorphic to J3.

Note that J3 is in a sense the family with the smallest J3(¯1) among the ones that satisfy the condition of the theorem. Before we prove it, let us put it into context. The following theorem is one of the main results in [20]:

- Theorem 14 ([20]). Let k ≥ 5 and n = n(k) be suﬃciently large. If F ⊂ [nk] is intersecting, and |F| > |J3|, then F ⊂ Fl for l ∈ {0, . . .k − 1, n − k}.

Many results in extremal set theory are much easier to get once one assumes that n is suﬃciently large in comparison to k. In this paper we prove the theorem above without the restriction on n. It follows immediately from Theorem 13.

- Theorem 15. Let k ≥ 5 and n > 2k. If F ⊂ [nk] is intersecting, and |F| ≥ |J3|, then either F is isomorphic to J3, or to a subset of Fl for l ∈ {0, . . .k − 1, n − k}.

We note that |J3| < |Fn−k| for n = ck: e.g., taking n > 4k is suﬃcient.

The following theorem is one of the main results of this paper. It generalizes Theorem 13 and gives a reasonable classiﬁcation of all large intersecting families (actually, all families with not too large diversity). We prove it using yet another variation of our methods. Let us call a family G ⊂ [2k,n] typical minimal, if, ﬁrst, for any Gl ∈ G we have |∩G∈G\{G

![image 58](<2017-kupavskii-structure-properties-large-intersecting_images/imageFile58.png>)

l}G| > |∩G∈G G|, and, second, either |G| = 2 or the number of elements contained in at least 2 sets from G is strictly bigger than |G|. (Note that the ﬁrst condition implies that there are at least |G| elements contained in exactly |G| − 1 sets from G. Therefore, the second condition is, in particular, satisﬁed when | ∩G∈G G| > 0.)

- Theorem 16. Assume that n > 2k ≥ 8. Consider an intersecting family F ⊂ [nk] , such that ∆(F) = δ(1). Assume that | ∩F∈F(¯1) F| = r, where r ∈ [0, k − 1]. Choose any k − 1 ≥ t ≥ r and any typical minimal subfamily G ⊂ F(¯1), such that | ∩F∈G F| = t. Take the (unique) maximal intersecting family F′, such that F′(¯1) = G. Then, if t ≥ 4


or γ(F) ≤ nk−−45 , we have

|F| ≤ |F′|, (14)

and equality is possible if and only if t = r and F is isomorphic to F′. In particular, in conditions above, if there are two sets in A, B ∈ F(¯1), such that |A ∩ B| = k − s + 1 for some s = 2, . . ., k, then

|F| ≤ |Js| (15) with the equality only possible if F is isomorphic to Js.

We note that r ≥ 3 implies both t ≥ 3 and γ(F) > nk−−45 , which, in turn, implies

|F| ≤ nk−−11 − nk−−15 + nk−−45 due to Theorem 2. Therefore, in particular, all families of size bigger than that are covered by the theorem.

### 4.1 Proof of Theorem 13

We are not going to use Theorem 7, but rather give a self-contained proof in the spirit of the proofs in [24]. The proof is rather simple and consists of two important steps. The ﬁrst is, via shifting and rearranging the elements, to reduce the family in question to a family that has certain structure (that is, sets of particular form). The second step is to use the method in the spirit of Lemmas 1, 2.

Let us ﬁrst give the deﬁnitions related to shifting. For a given pair of indices 1 ≤ i < j ≤ n and a set A ⊂ [n] deﬁne its (i, j)-shift

![image 59](<2017-kupavskii-structure-properties-large-intersecting_images/imageFile59.png>)

Si,j(A) as follows. If i ∈ A or j ∈/ A, then Si,j(A) = A. If j ∈ A, i ∈/ A, then Si,j(A) := (A − {j}) ∪ {i}. That is, Si,j(A) is obtained from A by replacing j with i.

The (i, j)-shift Si,j(F) of a family F is as follows:

Si,j(F) := {Si,j(A) : A ∈ F} ∪ {A : A, Si,j(A) ∈ F}. We call a family F shifted, if Si,j(F) = F for all 1 ≤ i < j ≤ n. We note that shifts do not destroy the cross-intersecting property, therefore, any pair

![image 60](<2017-kupavskii-structure-properties-large-intersecting_images/imageFile60.png>)

of cross-intersecting families may be transformed into a pair of shifted cross-intersecting families.

Take the family F satisfying the requirements of the statement. If γ(F) = 2, then F is isomorphic to one of the Ji, i = 3, . . ., k + 1, and we know that J3 is the largest out of

- them. Therefore, we may assume that γ(F) ≥ 3. Consider the families A := F(1), B := F(¯1). They are cross-intersecting. There are


two cases to consider.

Case 1. Assume that we have two sets A, B ∈ F(¯1), such that |A ∩ B| ≤ k − 2. First of all, by doing shifts, we may assume that there are two sets B1, B2 ∈ B, such

that |B1 ∩B2| = k −2. W.l.o.g., we may assume that B1 = [2, k −1] ∪{k + 1, k + 2}, and

- that B2 = [2, k] ∪ {k + 3}. We have at least one more set B3 in B. Doing (i, j)-shifts, where i ∈ [2, k − 1] and


- j ∈ [k, n], we can assume that B3 ⊃ [2, k − 1]. Apart from these elements, there are two more elements in B3, say, j1 and j2, j1 < j2. Either j1 = k, or j2 ≥ k + 3, and we can do a (k, j2)-shift (or a (k, j1)-shift, if j1 = k + 3), thus assuring that [2, k] ∈ B3. Denote by j the only remaining element of B3. Clearly, j = k + 3, since otherwise B3 = B2, and therefore we can safely do a (k + 1, j)-shift, thus transforming B3 into [2, k + 1] and not changing B1, B2. Moreover, if γ(F) ≥ 4, then there is yet another set B4, which, in a similar way, we can transform into [2, k] ∪ {k + 2}. In what follows, we assume that


- B3 = [2, k + 1] and B4 = [2, k] ∪ {k + 2}.


Assume ﬁrst that γ(F) = |B| = 3 and B = {B1, B2, B3} as above. Then we can use the following simple argument. Remove the set B3 from B, thus decreasing the sum of

cardinalities of A and B by 1, and then add to A all the (k − 1)-sets from the family

A1 := A ∈

[2, n] k − 1

: A ∩ [k + 1] = ∅, {k + 2, k + 3} ∈ A . (16)

Clearly, each set from A1 will intersect both B1 and B2, and thus the pair A, B will remain cross-intersecting. However, none of the sets from A1 was present in A before, since each set from A1 is disjoint with B3. Therefore, we increase the sum of cardinalities of A and B by |A1| = n−k−k−33 , which is more than 1 for n > 2k, k ≥ 4. Therefore, the resulting cross-intersecting pair, which corresponds to the family J3, is bigger than the initial one.

If γ(F) = |B| ≥ 4, then, due to the discussion two paragraphs above, we may assume that Bi ∈ B, i ∈ [4], and that A, B are shifted. Let T be the lexicographically last element in B. since the family B is itself intersecting, for each set B ∈ B there must be an i such that

|[2, i] ∩ B| > |[2, i] \ B|, (17)

because otherwise one of the sets in [2, n] that may be obtained from B by shifts will be disjoint from B, but at the same time it will lie in B.

Let us ﬁnd the biggest such i for T and consider a bipartite graph G with parts

- Pa := P ∈

[2, n] k − 1

: P ∩ [i] = [2, i] \ B ,

- Pb := P ∈


[2, n] k

: P ∩ [i] = [2, i] ∩ B

and edges connecting disjoint sets. Then we see that, due to (17) and n − 1 > 2k − 1, |Pa| ≥ |Pb|. At the same time, (A ∩ Pa) ∪ (B ∩ Pb) is an independent set in G and thus has size at most |Pa|. Therefore, replacing A, B with A′ := A ∪ Pa, B′ := B \ Pb, we do not decrease the sum of sizes. Moreover, it is easy to see that B′ is intersecting (since

- B′ ⊂ B) and that A′, B′ are cross-intersecting. Indeed, any set in B′ must intersect [2, i] in a set which lexicographically precedes [2, i] ∩ B, and thus which intersects [2, i] \ B. Moreover, the family B′ is shifted.


We repeat this with the lexicographically last element in B′, etc., until the lexicographically last set of the second family is B1. We note that we will arrive at such a moment. Indeed, the only obstacle is that we somehow remove B1 from the second family due to the fact that B1 ∈ Pb, where Pb was deﬁned by some other set B′ in the second family. Let us show that this is impossible. Recall that we chose i as the largest index, for which the inequality (17) is satisﬁed. We must have B′ ∩ [2, i] = B1 ∩ [2, i]. On the other hand, by the maximality of i, we have 1 = |B′ ∩ [2, i]| − |B′ \ [2, i]| = |B ∩ [2, i]| − |B \ [2, i]|. But |B ∩ [2, i]| − |B \ [2, i]| ≥ 2 for any i ≤ k + 2.

Therefore, we may assume that B1 is the lexicographically last element in B. Thus, each B ∈ B, B = B1, satisﬁes [2, k] ⊂ B. The number of such sets is n − k, and this, in particular, implies that |B| ≤ n − k + 1. At the same time, Bi ∈ B, i = [4], since they all precede B1 lexicographically (and thus could not have been removed before B1).

Removing all the sets from B apart from B1, B2 will decrease |A| + |B| by at most n − k − 1. At the same time, we may add to A the family A1 as well as the following family:

A2 := A ∈

[2, n] k − 1

: A ∩ ([k] ∪ {k + 2}) = ∅, {k + 1, k + 3} ∈ A . (18)

We have |A1| = |A2| = n−k−k−33 ≥ n−k−3, and both A1 and A2 are disjoint with A, since B3, B4 ∈ B. Thus we are getting 2(n − k − 3) new sets, and 2(n − k − 3) − (n − k − 1) = n − k − 5 > 0 for n > 2k, k ≥ 5. Therefore, we conclude that in this case as well, the size of the family F is smaller than the size of J2.

Case 2. Assume that any two sets in F(¯1) intersect in at least k−1 elements. Then,

knowing that |∩F∈F(¯1) F| ≤ k −2, we may assume that F(¯1) ⊂ [2,kk+2] (indeed, it is easy to check that all sets in F(¯1) must be contained in a certain k + 1-set). We may w.l.o.g.

assume that the sets C1 = [2, k + 1], C2 = [2, k] ∪ {k + 2}, C3 = [2, k − 1] ∪ {k + 1, k + 2} are contained in F(¯1). Let us look at the sets that Ci forbid in F(1), as compared to the sets that are forbidden by B1, B2. In both cases F(1) contain all sets intersecting [k − 1],

- as well sets containing {k} and one of {k +1, k+2}. Apart from the one listed above, the


sets Ci allow only for sets that intersect [k +2] in {k +1, k +2} (their number is n−k−k−32 ), while the sets Bi allow for the sets that contain {k + 3}, disjoint with [k], and intersect

- [k + 1, k + 2] in at least one element (their number is n−k−k−32 + n−k−k−33 ). Therefore, we can have n−k−k−33 sets more with B1, B2 than with C1, C2, C3. On the other hand, in this


case |F(¯1)| − 2 ≤ k − 1 < n−k−k−33 for any n > 2k ≥ 10. So we conclude that the families in this case are also smaller than J2.

### 4.2 Proof of Theorem 16

Choose F, t, G, and F′ satisfying the requirements of the theorem. We aim to prove that any family F satisfying the requirements of the theorem has size strictly smaller than F′, unless it is isomorphic to F′. As a condition, in some of the cases we have γ(F) ≤ nk−−45 . If it does not hold, but we have t ≥ 4 instead, then we still may assume that γ(F) ≤ nk−−45 . Indeed, the largest family with diversity > nk−−45 is at most as large

- as H5 := {A ∈ [nk] : [2, 5] ⊂ A} ∪ {A ∈ [nk] : 1 ∈ A, [2, 5] ∩ A = ∅}, and the latter family satisﬁes the requirements of the theorem (it contains a copy of any G as in the statement). Therefore, if we show that F′ is bigger than H5, it implies that F′ is bigger than any family with diversity > nk−−45 .


Therefore, from now on we assume that γ(F) ≤ nk−−45 . Assume that ∩F∈GF = [2, t+1] (note that it may be empty). For each i ∈ [2, t+1] consider the following bipartite graph. The parts are

- Pa := P \ {i} : P ∈ F(1), i ∈ P},
- Pb := P ∈ F(¯1) : i ∈/ P ,


and edges connect disjoint sets. Note that Pa ⊂ k X−2 , Pb ⊂ Xk , where X = [2, n] \ {i}, |X| = n − 2 > k + k − 2. Due to the condition on γ(F), we have |Pb ∩ F(¯1)| ≤ nk−−45 <

|X|−3

(k−2)−1 . Thus, we can apply (10) to

- A :=F(1) ∩ Pa and
- B :=F(¯1) ∩ Pb,


and conclude that |A|+|B| ≤ k |X−2| . Therefore, removing F(¯1)∩Pb from F(¯1) and adding sets from Pa to F(1), we get a pair of families with larger sum of cardinalities. Moreover, the new pair is cross-intersecting: all sets in F(¯1) \ Pb contain i, as well as the sets from

Pa. Therefore, we may assume that all sets in F(¯1) contain [2, t + 1]. Put G = {G1, . . ., Gz}. Due to minimality of G, for each Gl ∈ G, l ∈ [z], there is il ∈

G \

G .

G∈G

G∈G\{Gl}

We assume that il = t + l + 1, l ∈ [z]. In particular, {i1, . . ., iz} = [t + 2, t + z + 1]. Next, for each set i ∈ [t + 2, t + z + 1] consider the same bipartite graph as before.

We can apply (11) with j := k. Indeed, we know that |B| ≥ k |X−k| = 1 since Gi−t−1 ∈ Pb (note that Gl ∈/ Pb for l = i − t − 1, since all of them contain il due to the deﬁnition of

il). Therefore, |A| + |B| ≤ nk−−22 − n−k−k−22 + 1, and we may replace A, B with B′ := {B} and A′ := {A ∈ k X−2 : A ∩ B = ∅}. The resulting family is cross-intersecting. Repeating this procedure, we may conclude that any set in F(¯1) not from G must contain the set [2, t + z + 1]. If there are any other elements contained in all but 1 set from G, we repeat the same procedure with them. Assume that they together with [2, t + z + 1] form a segment [2, t′]. Note that for each l ∈ [z] the set Gl ∩ [2, t′] has the same size and must be non-empty. Otherwise, we have already proved the inequality (14), since the current F(¯1) is equal to G.

Recall that G is typical minimal, that is, the number of elements contained in at least 2 sets from G is at least z +1. If |[2, t′]| ≥ z +1 (which is the case, e.g., when t ≥ 1), then we proceed in the following way.

For each S ⊂ [z] of size z − 1 select one element il ∈ Gl ∩ [t′ + 1, n] for each l ∈ S. Note that il may coincide. Put IS := {il : l ∈ S}. Consider a bipartite graph with parts

- Pa := P\ : P ∈ F(1), IS ⊂ P, [2, t′] ∩ P = ∅},
- Pb := P \ [2, t′] : P ∈ F(¯1), IS ∩ P = ∅, [2, t′] ⊂ P ,


and edges connecting disjoint sets. Note that Pa ⊂ k− Yz

, z′ ≤ z, and Pb ⊂ k− Yz

,

′

′′

z′′ ≥ z+1, where Y = [t′+1, n]\IS, |Y | = n−z′′−z′. In particular, |Y | > k−z′+k−z′′. We have |G ∩ Pb| ∈ {0, 1}. Indeed, only the set Gl, {l} = [z] \ S may be left. Denote

A :=F(1) ∩ Pa and B :=F(¯1) ∩ Pb.

We have k − z′ > k − z′′, and, therefore, we may apply either (10) or (11) with a :=

- k −z′, b := k −z′′, j := k −z′′ (the upper bound on |B| becomes trivial in that case) and


′′

conclude that either |A|+|B| ≤ k |−Yz|

or |A|+|B| ≤ k |−Yz|

− |Y|−k+z

k−z′ +1. In both cases we may replace B with Pb ∩ G and A with all sets from Pa that intersect the set from Pb∩G (if it is non-empty). As before, the size does not decrease and the cross-intersecting property is preserved.

′

′

Repeating this for all possible choices of S and IS, we arrive at a point when any set from F(¯1) \ G must intersect any set IS. Tt is clear that it only holds for a set F if F ⊃ Gl ∩ [t′ + 1, n]. But then F = Gl, so F(¯1) = G, and the proof of (14) is complete in this case.

Assume now that |[2, t′]| = z + 1. By the typical minimality of G, we have an element i ∈, which is contained in at least 2 sets, say, G1 and G2. We do something very similar

to the previous case, but we have to be a bit more careful. We select a z − 1-set S ⊂ [z], which includes 1 and 2, a set IS := {i} ∪ {il : l ∈ [3, z] ∩ S}. It is clear that |IS| ≤ z − 2. Next, we consider the same bipartite graph as before. The sets in part Pa now have size

- at least k − z + 1, while the sets in Pb have size at most k − z. Therefore, we can apply


(10), (11) in the same way, and arrive at a family F(¯1), such that any set in F(¯1) \ G intersects any set IS of the form described above. In practice, this means that any set in F(¯1) \ G contains i! Thus, we may now add i to the set [2, t′] and proceed as in the ﬁrst case: we now have at least z + 1 common elements for all F ∈ F(¯1) \ G. The inequality (14) is proven.

Finally, the uniqueness follows from the fact that the inequalities (10), (11) are strict unless the family B has size 0 and 1, respectively. Therefore, if F(¯1) = G, then at some point we would have had a strict inequality in the application of (10), (11).

## 5 Degree versions

Recently, Huang and Zhao [17] gave an elegant proof of the following theorem using a linear-algebraic approach:

- Theorem 17 ([17]). Let n > 2k > 0. Then any intersecting family has minimum degree

- at most nk−−22 .


The bound in the theorem is tight because of the trivial intersecting family, and the condition n > 2k is necessary: in [17] the authors provide an example of a family for n = 2k which has larger minimal degree. In fact, for most values of k there are regular intersecting families in [2kk] of maximal possible size: 2kk−1 (see [18]). In the follow-up paper, Frankl, Han, Huang, and Zhao [8] proved

- Theorem 18 ([8]). Let k ≥ 4 and n ≥ ck2, where c = 30 for k = 4, 5, and c = 4 for k ≥ 6. Then any non-trivial intersecting family has minimum degree at most nk−−22 − n−k−k−22 .


Several questions and problems arose in this context, that were asked in [17], [8], as well as in personal communication with Hao Huang and his presentation on the Recent Advances in Extremal Combinatorics Workshop at TSIMF, Sanya. Some of them are as follows:

- 1. Can one ﬁnd a combinatorial proof of Theorem 17? This question was partially answered by Frankl and Tokushige [13], who proved it under the additional assumption n ≥ 3k. Huang claims that their proof can be made to work for n ≥ 2k+3, provided that one applies their approach more carefully. However, the cases n = 2k + 2 and n = 2k + 1 remained open.
- 2. Extend Theorem 18 to the case n ≥ ck for large k. Ultimately, prove Theorem 18 for all values n ≥ 2k + 1 for which it is valid.
- 3. Extend Theorems 17 and 18 to degrees of t-tuples of vertices. The degree of a subset


![image 61](<2017-kupavskii-structure-properties-large-intersecting_images/imageFile61.png>)

S ⊂ [n] is the number of sets from the family containing S. We denote by δt(F) the minimal degree of an t-element subset S ⊂ [n].

In this section we address these questions, partially answering all three of them. In the ﬁrst theorem, we prove a t-degree version of Theorem 17. Its proof is combinatorial and works, in particular, for s = 1 and n ≥ 2k + 2.

- Theorem 19. If n ≥ 2k+2 > 2, then for any intersecting family F of k-subsets of [n] we have δ1(F) ≤ nk−−22 . More generally, if n ≥ 2k+1−3tt

![image 62](<2017-kupavskii-structure-properties-large-intersecting_images/imageFile62.png>)

![image 63](<2017-kupavskii-structure-properties-large-intersecting_images/imageFile63.png>)

k

and 1 ≤ t < k, then δt(F) ≤ nk−−tt−−11 . In the second theorem we give a t-degree version of Theorem 18 with much weaker

restrictions on n for large k.

- Theorem 20. If t = 1, n ≥ 2k+5, and k ≥ 35, or 1 < t ≤ k4−2, n ≥ 2k+14t, then for any non-trivial intersecting family F of k-subsets of [n] we have δt(F) ≤ nk−−tt−−11 − n−k−t−t−k−11 .


![image 64](<2017-kupavskii-structure-properties-large-intersecting_images/imageFile64.png>)

After writing a preliminary version of the paper, we read the paper [13], where Theorem 19 is proven for s = 1 and n ≥ 3k. It turned out that the approach the authors took is very similar to the approach we use to prove Theorem 19. However, it seems that their proof, unlike ours, does not work for n = 2k + 2, which is probably due to the fact that they use the original Frankl’s degree theorem (see Section 2).

### 5.1 Calculations

In this section we do some of the calculations used in the proofs of Theorems 19 and 20. Note that, substituting u = 3 in (1), we get that

|F| ≤

n − 1 k − 1

+

n − 4 k − 3

−

n − 4 k − 1

=

n − 2 k − 2

+

n − 3 k − 2

+

n − 4 k − 2

+

n − 4 k − 3

=

k − 1 n − 1

n − 3 k − 2

n − 2 k − 2

n − 1 k − 1

2(k − 1)(n − k) (n − 2)(n − 1)

=

+ 2

= (k − 1)(3n − 2k − 2) (n − 1)(n − 2)

+

![image 65](<2017-kupavskii-structure-properties-large-intersecting_images/imageFile65.png>)

![image 66](<2017-kupavskii-structure-properties-large-intersecting_images/imageFile66.png>)

k(k − 1)(3n − 2k − 2) n(n − 1)(n − 2)

n − 1 k − 1

n k

. (19) We also have

=

![image 67](<2017-kupavskii-structure-properties-large-intersecting_images/imageFile67.png>)

![image 68](<2017-kupavskii-structure-properties-large-intersecting_images/imageFile68.png>)

n−u−1 n−k−1 n−u−1 k−1

=

![image 69](<2017-kupavskii-structure-properties-large-intersecting_images/imageFile69.png>)

n−k−1 i=1

n−u−i i

![image 70](<2017-kupavskii-structure-properties-large-intersecting_images/imageFile70.png>)

=

![image 71](<2017-kupavskii-structure-properties-large-intersecting_images/imageFile71.png>)

k−1 i=1

n−u−i i

![image 72](<2017-kupavskii-structure-properties-large-intersecting_images/imageFile72.png>)

n−k−1

n − u − i i

![image 73](<2017-kupavskii-structure-properties-large-intersecting_images/imageFile73.png>)

i=k

n−k−1

n − u − i n − 1 − i

=

.

![image 74](<2017-kupavskii-structure-properties-large-intersecting_images/imageFile74.png>)

i=k

Clearly, for 3 ≤ u ≤ k the last expression is maximized for u ≥ 3, and we get the following bound, provided n ≥ 2k + 2:

n−u−1 n−k−1 n−u−1 k−1

![image 75](<2017-kupavskii-structure-properties-large-intersecting_images/imageFile75.png>)

n−k−1

n − 3 − i n − 1 − i

≥

![image 76](<2017-kupavskii-structure-properties-large-intersecting_images/imageFile76.png>)

i=k

(k − 1)(k − 2) (n − k − 1)(n − k − 2)

=

![image 77](<2017-kupavskii-structure-properties-large-intersecting_images/imageFile77.png>)

If n = 2k + 1, then we get that the ratio is at least kk−−13. We will also use the following formula:

![image 78](<2017-kupavskii-structure-properties-large-intersecting_images/imageFile78.png>)

for 3 ≤ u ≤ k. (20)

n−t−k−1 k−t−1 n−t−1 k−t−1

=

![image 79](<2017-kupavskii-structure-properties-large-intersecting_images/imageFile79.png>)

k

n − k + 1 − i n − t − i

. (21)

![image 80](<2017-kupavskii-structure-properties-large-intersecting_images/imageFile80.png>)

i=1

### 5.2 Proof of Theorem 19

Take an intersecting family F with maximum degree ∆ and diversity γ. Then, by deﬁnition, |F| = ∆ + γ. W.l.o.g., we suppose that the element 1 has the largest degree.

Proposition 5. Fix some n, t, k. If for an intersecting family of k-sets F ⊂ 2[n] with maximum degree ∆ and diversity γ we have

k k − t

γ ≤

∆ +

![image 81](<2017-kupavskii-structure-properties-large-intersecting_images/imageFile81.png>)

n − 1 k − 1

, (22)

- then δt(F) ≤ nk−−tt−−11 .


Proof. The sum of t-degrees of all t-subsets of [2, n] is γ kt + ∆ k−t1 . Therefore, there is a t-tuple T of elements in [2, n], such that

γ kt + ∆ k−t1

δt(T) ≤

![image 82](<2017-kupavskii-structure-properties-large-intersecting_images/imageFile82.png>)

n−1 t

The ratio of two fractions is

t i=1

k−i+1 n−i

![image 83](<2017-kupavskii-structure-properties-large-intersecting_images/imageFile83.png>)

=

![image 84](<2017-kupavskii-structure-properties-large-intersecting_images/imageFile84.png>)

t i=1

k−i n−i

![image 85](<2017-kupavskii-structure-properties-large-intersecting_images/imageFile85.png>)

Therefore, if (22) holds, then

δt(F) ≤

t

k − i n − i

k k − t

γ) ≤

(∆ +

![image 86](<2017-kupavskii-structure-properties-large-intersecting_images/imageFile86.png>)

![image 87](<2017-kupavskii-structure-properties-large-intersecting_images/imageFile87.png>)

i=1

t

k − i + 1 n − i

+ ∆

= γ

![image 88](<2017-kupavskii-structure-properties-large-intersecting_images/imageFile88.png>)

i=1

t

k − i + 1 k − i

![image 89](<2017-kupavskii-structure-properties-large-intersecting_images/imageFile89.png>)

i=1

k k − t

=

![image 90](<2017-kupavskii-structure-properties-large-intersecting_images/imageFile90.png>)

t

k − i n − i

![image 91](<2017-kupavskii-structure-properties-large-intersecting_images/imageFile91.png>)

i=1

n − 1 k − 1

t

k − i n − i

. (23)

![image 92](<2017-kupavskii-structure-properties-large-intersecting_images/imageFile92.png>)

i=1

.

=

n − t − 1 k − t − 1

. (24)

![image 93](<2017-kupavskii-structure-properties-large-intersecting_images/imageFile93.png>)

![image 94](<2017-kupavskii-structure-properties-large-intersecting_images/imageFile94.png>)

![image 95](<2017-kupavskii-structure-properties-large-intersecting_images/imageFile95.png>)

![image 96](<2017-kupavskii-structure-properties-large-intersecting_images/imageFile96.png>)

To prove Theorem 19, we are only left to verify (22) for all intersecting families. It is vacuously true for trivial intersecting families, so we may assume that γ ≥ 1. Fix F as in the theorem. We have two cases to distinguish.

Case 1. γ ≤ nk−−34 . We only need to show that (1) holds. We may apply Corollary 1 (otherwise, it is not diﬃcult to obtain via direct calculations). We only have to check that

n − k − 3 k − 3

k k − t

≤

. (25)

![image 97](<2017-kupavskii-structure-properties-large-intersecting_images/imageFile97.png>)

![image 98](<2017-kupavskii-structure-properties-large-intersecting_images/imageFile98.png>)

Putting n = 2k + s, where s ≥ 1, we see that, if t = 1, then (25) holds for any s ≥ 1. If t > 1, then we must have

k2 − 3k − (k − 3)t + s(k − t) ≥ k2 − 3k, which is satisﬁed when

k − 3 k − t

t 1 − kt

s ≥

t ⇐ s ≥

.

![image 99](<2017-kupavskii-structure-properties-large-intersecting_images/imageFile99.png>)

![image 100](<2017-kupavskii-structure-properties-large-intersecting_images/imageFile100.png>)

![image 101](<2017-kupavskii-structure-properties-large-intersecting_images/imageFile101.png>)

Case 2. γ ≥ nk−−34 . By the calculations in Section 5.1, We know that |F| ≤

n−2

k−2 + 2 nk−−23 , and we use the following easy bound on δt(F) :

δt(F) ≤

k t n t

|F|. (26)

![image 102](<2017-kupavskii-structure-properties-large-intersecting_images/imageFile102.png>)

Thus, it is suﬃcient for us to check that the following inequality holds:

k t n t

n − 3 k − 2

n − t − 1 k − t − 1

n − 2 k − 2

≥

+ 2

![image 103](<2017-kupavskii-structure-properties-large-intersecting_images/imageFile103.png>)

We have n−t−1

n t

(n − t − 1)!n!(k − t)! (k − t − 1)!(n − k)!(n − t)!k!

k−t−1

=

=

![image 104](<2017-kupavskii-structure-properties-large-intersecting_images/imageFile104.png>)

![image 105](<2017-kupavskii-structure-properties-large-intersecting_images/imageFile105.png>)

k t

and, by the calculation in Section 5.1,

. (27)

k − t n − t

![image 106](<2017-kupavskii-structure-properties-large-intersecting_images/imageFile106.png>)

n k

(28)

n − 2 k − 2

+ 2

n − 3 k − 2

k(k − 1)(3n − 2k − 2) n(n − 1)(n − 2)

=

![image 107](<2017-kupavskii-structure-properties-large-intersecting_images/imageFile107.png>)

n k

.

Therefore, (27) is equivalent to

k − t n − t

![image 108](<2017-kupavskii-structure-properties-large-intersecting_images/imageFile108.png>)

k(k − 1)(3n − 2k − 2) n(n − 1)(n − 2)

≥

.

![image 109](<2017-kupavskii-structure-properties-large-intersecting_images/imageFile109.png>)

If t = 1, then it simpliﬁes to k(3nn(−n−2k2)−2) ≤ 1, which holds for any n ≥ 2k + 2. If t > 1, then it simpliﬁes to a quadratic inequality in n, which holds for

![image 110](<2017-kupavskii-structure-properties-large-intersecting_images/imageFile110.png>)

![image 111](<2017-kupavskii-structure-properties-large-intersecting_images/imageFile111.png>)

2k2 + (k − 3)t + (2k2 + (k − 3)t)2 − 8(k − t)t(k2 − 1) 2(k − t)

n ≥

.

![image 112](<2017-kupavskii-structure-properties-large-intersecting_images/imageFile112.png>)

The right hand side is at most

![image 113](<2017-kupavskii-structure-properties-large-intersecting_images/imageFile113.png>)

2k2 + (k − 3)t + (2k2 + (k − 3)t)2 2(k − t)

=

![image 114](<2017-kupavskii-structure-properties-large-intersecting_images/imageFile114.png>)

2k2 + (k − 3)t (k − t)

![image 115](<2017-kupavskii-structure-properties-large-intersecting_images/imageFile115.png>)

3(k − 1)t k − t

3t 1 − kt

= 2k +

< 2k +

.

![image 116](<2017-kupavskii-structure-properties-large-intersecting_images/imageFile116.png>)

![image 117](<2017-kupavskii-structure-properties-large-intersecting_images/imageFile117.png>)

![image 118](<2017-kupavskii-structure-properties-large-intersecting_images/imageFile118.png>)

### 5.3 Proof of Theorem 20

The strategy of the proof is very similar to that of Theorem 19. Fix a non-trivial intersecting family F with γ ≥ 2 (otherwise, it is a subfamily of some Hilton-Milner family). W.l.o.g., suppose that the element of the family F with maximal degree is 1, and that F contains the set [2, k +1]. Then any other set containing 1 must intersect U. We compare F with the Hilton-Milner family HM := {F : 1 ∈ F, F ∩ [2, k + 1] = ∅} ∪ [2, k + 1]. We consider cases depending on γ. The case analysis, however, will be more complicated, as compared to the previous case. Notably, we get a new non-trivial Case 1.

Case 1. 1 < γ < n−tk+2+t+1 . We have γ ≥ 2, and we may apply Theorem 4 to the families F(1) := {F \ {1} : 1 ∈ F ∈ F} and F(¯1) := {F : 1 ∈/ F ∈ F}. We get that the cardinality of F(1) is at most the cardinality of all (k − 1)-subsets of [2, n] that intersect the sets [2, k + 1] and [2, k] ∪ {k + 2}. In other words, the degree of 1 is at most

k−1 − n−k−k−11 − n−k−k−22 . That is, some n−k−k−22 sets from HM containing 1 are missing from F.

n−1

Denote G := {G ∈ [nk] \ F : 1 ∈ G, G ∩ [2, k + 1] = ∅}. By the paragraph above, we have |G| ≥ n−k−k−22 . Consider a subfamily G′ ⊂ G, such that each G′ ∈ G′ intersects

- [k + 2, n] in at least t elements.


Then, denoting by H the Hilton-Milner family, it is easy to see that the following rough estimate holds.

|G′|

− γ. (29)

δt(H) − δt(F) ≥

![image 119](<2017-kupavskii-structure-properties-large-intersecting_images/imageFile119.png>)

n−k−1 t

Indeed, the ﬁrst summand is the average loss in the t-degree of t-sets in [k + 2, n], and each set contributing to γ can contribute at most 1 to minimum t-degree. In the rest of this case our goal is to show that the RHS in (29) is always positive.

Let us ﬁrst estimate the size of G′. To do so, we have to exclude all the sets that intersect [1, k + 1] in more than k − t elements. Since 1 is always in the set, the number of sets we have to exclude is

k−1

i=k−t

k i

n − k − 1 k − i − 1

.

We have n−t−kj−1 > 2 nt−−jk−−11 for any j ≥ 0, since n ≥ 2k ≥ 8t. Therefore, the sum above is at most

n − k − 1 t

n − k − 1 t

k t

k k − t

, and we have

=

n − k − 1 t

n − k − 2 k − 2

k t

|G′| ≥

−

. (30)

To show that the RHS in (29) is always positive and thus to conclude the proof in Case 1, it is suﬃcient to show the ﬁrst in the following chain of inequalities:

n − k − 2 k − 2

≥

n − k − 1 t

n − k + t + 2 t + 2

>

n − k − 1 t

>

n − k + t + 1 t + 2

+

k t

n − k − 1 t

. (31)

Note that the second inequality is just a corollary of Newton’s binom and the fact that

k

t < n−tk+1+t+1 . We also use the fact that γ ≤ n−tk+2+t+1 .

If t = 1, n ≥ 2k + 5, then in the worst case for (31) is n = 2k + 5, and the ﬁrst inequality in (31) transforms into

which holds for k ≥ 35.

k + 3 5

≥ (k + 4)

k + 8 3

,

If 1 < t ≤ k4 − 2, n ≥ 2k + 14t, then we have n − k − 1 t

![image 120](<2017-kupavskii-structure-properties-large-intersecting_images/imageFile120.png>)

(n − k + t + 2)! t!(t + 2)!(n − k − t)!

n − k + t + 2 t + 2

≤

=

![image 121](<2017-kupavskii-structure-properties-large-intersecting_images/imageFile121.png>)

n − k + t + 2 2t + 2

n − k + t + 2 2t + 2

22t,

2t + 2 t

≤

where the last inequality holds for any t ≥ 2. On the other hand, using the above conditions on n, k, t, we have

n − k + t + 2 2t + 2

<

n − k − 2 n − k − 2t − 4

![image 122](<2017-kupavskii-structure-properties-large-intersecting_images/imageFile122.png>)

t+4 n − k − 2 2t + 2

≤

2t + 2 k + 10t − 4

1 +

![image 123](<2017-kupavskii-structure-properties-large-intersecting_images/imageFile123.png>)

t+4 n − k − 2 2t + 2

≤

19 16

![image 124](<2017-kupavskii-structure-properties-large-intersecting_images/imageFile124.png>)

t+4 n − k − 2 2t + 2

<

5 4

![image 125](<2017-kupavskii-structure-properties-large-intersecting_images/imageFile125.png>)

t+4 4t + 4 n − k − 4t − 6

![image 126](<2017-kupavskii-structure-properties-large-intersecting_images/imageFile126.png>)

2t+2 n − k − 2 4t + 4

≤

5 4

![image 127](<2017-kupavskii-structure-properties-large-intersecting_images/imageFile127.png>)

t+4 4t + 4 14t + 2

![image 128](<2017-kupavskii-structure-properties-large-intersecting_images/imageFile128.png>)

2t+2 n − k − 2 4t + 4

≤

5 4

![image 129](<2017-kupavskii-structure-properties-large-intersecting_images/imageFile129.png>)

t+4 2 5

![image 130](<2017-kupavskii-structure-properties-large-intersecting_images/imageFile130.png>)

2t+2 n − k − 2 4t + 4

≤

- 1

![image 131](<2017-kupavskii-structure-properties-large-intersecting_images/imageFile131.png>)

- 2


2t+2 n − k − 2 k − 2

.

Comparing this chain of inequalities with the one above, we conclude that for our choice of parameters

n−k−2 k−2 n−k−1 t

≥

![image 132](<2017-kupavskii-structure-properties-large-intersecting_images/imageFile132.png>)

n−k+t+2 t+2

22t+2 22t

> 1.

![image 133](<2017-kupavskii-structure-properties-large-intersecting_images/imageFile133.png>)

Case 2. n−tk+2+t+1 ≤ γ ≤ nk−−34 . Using the ﬁrst inequality in (24), we get the following analogue of Statement 5. Statement 1. Fix some n, t, k. If for an intersecting family of k-sets F ⊂ 2[n] with maximum degree ∆ and diversity γ we have

k

∆ + ctγ ≤ 1 −

i=1

n − k + 1 − i n − t − i

![image 134](<2017-kupavskii-structure-properties-large-intersecting_images/imageFile134.png>)

then δt(F) ≤ nk−−tt−−11 − n−k−t−t−k−11 . Proof. Indeed, if (32) holds, then, using (24), we get

n − 1 k − 1

, (32)

t

k − i n − i

δt(F) ≤

![image 135](<2017-kupavskii-structure-properties-large-intersecting_images/imageFile135.png>)

i=1

k

n − k + 1 − i n − t − i

1 −

![image 136](<2017-kupavskii-structure-properties-large-intersecting_images/imageFile136.png>)

i=1

n − 1 k − 1

=

n − t − 1 k − t − 1

k

n − k + 1 − i n − t − i

1 −

![image 137](<2017-kupavskii-structure-properties-large-intersecting_images/imageFile137.png>)

i=1

(21)=

n − t − 1 k − t − 1

−

n − t − k − 1 k − t − 1

.

![image 138](<2017-kupavskii-structure-properties-large-intersecting_images/imageFile138.png>)

![image 139](<2017-kupavskii-structure-properties-large-intersecting_images/imageFile139.png>)

![image 140](<2017-kupavskii-structure-properties-large-intersecting_images/imageFile140.png>)

![image 141](<2017-kupavskii-structure-properties-large-intersecting_images/imageFile141.png>)

We apply (1). Our situation corresponds to the case u ≤ k − t − 2. To verify (32), one has to check that

n − u − 1 k − 1

− ct

n − u − 1 n − k − 1

k

n − k + 1 − i n − t − i

−

![image 142](<2017-kupavskii-structure-properties-large-intersecting_images/imageFile142.png>)

i=1

n − 1 k − 1

≥ 0. (33)

We have

n − u − 1 k − 1

− ct

n − u − 1 n − k − 1

n−k−1

n − u − i n − 1 − i

k k − t

= 1 −

![image 143](<2017-kupavskii-structure-properties-large-intersecting_images/imageFile143.png>)

![image 144](<2017-kupavskii-structure-properties-large-intersecting_images/imageFile144.png>)

i=k

n − u − 1 k − 1

(20)

≥

k(k − 1)(k − 2) (k − t)(n − k − 1)(n − k − 2)

1 −

![image 145](<2017-kupavskii-structure-properties-large-intersecting_images/imageFile145.png>)

k−1

n − u − i n − i

![image 146](<2017-kupavskii-structure-properties-large-intersecting_images/imageFile146.png>)

i=1

n − 1 k − 1

.

The last expression is minimized when u = k − t− 2. Comparing the product above with the product in (33), we get

k i=1

n−k+1−i n−t−i

![image 147](<2017-kupavskii-structure-properties-large-intersecting_images/imageFile147.png>)

≤

![image 148](<2017-kupavskii-structure-properties-large-intersecting_images/imageFile148.png>)

k−1 i=1

n−u−i n−i

![image 149](<2017-kupavskii-structure-properties-large-intersecting_images/imageFile149.png>)

k i=1

n−k+1−i n−t−i

![image 150](<2017-kupavskii-structure-properties-large-intersecting_images/imageFile150.png>)

=

![image 151](<2017-kupavskii-structure-properties-large-intersecting_images/imageFile151.png>)

k−1 i=1

n−k+t+2−i n−i

![image 152](<2017-kupavskii-structure-properties-large-intersecting_images/imageFile152.png>)

- k−t−1 i=1

n−k−t−i n−t−i

![image 153](<2017-kupavskii-structure-properties-large-intersecting_images/imageFile153.png>)

![image 154](<2017-kupavskii-structure-properties-large-intersecting_images/imageFile154.png>)

- k−t−2 i=1


n−k−i n−i

![image 155](<2017-kupavskii-structure-properties-large-intersecting_images/imageFile155.png>)

≤

- k−t−1 i=1

n−k−t−i n−t−i

![image 156](<2017-kupavskii-structure-properties-large-intersecting_images/imageFile156.png>)

![image 157](<2017-kupavskii-structure-properties-large-intersecting_images/imageFile157.png>)

- k−t−2 i=1


n−k−t−i n−t−i

![image 158](<2017-kupavskii-structure-properties-large-intersecting_images/imageFile158.png>)

k n − k + 1

= 1 −

.

![image 159](<2017-kupavskii-structure-properties-large-intersecting_images/imageFile159.png>)

Therefore, to prove (33), it is suﬃcient for us to show that

k(k − 1)(k − 2) (k − t)(n − k − 1)(n − k − 2)

1 −

![image 160](<2017-kupavskii-structure-properties-large-intersecting_images/imageFile160.png>)

k n − k + 1

≥ 1 −

. (34)

![image 161](<2017-kupavskii-structure-properties-large-intersecting_images/imageFile161.png>)

For the fraction in the left hand side, we use the following property: if we add 1 to one of the multiples in the numerator and 1 to one of the multiples in the denominator, then the fraction will only increase, and the expression in the left hand side will decrease. If

- t = 1, then the LHS of (34) is


k(k − 2) (n − k − 1)(n − k − 2)

1 −

![image 162](<2017-kupavskii-structure-properties-large-intersecting_images/imageFile162.png>)

k2 (n − k + 1)(n − k − 2)

k n − k + 1

≥ 1 −

> 1 −

,

![image 163](<2017-kupavskii-structure-properties-large-intersecting_images/imageFile163.png>)

![image 164](<2017-kupavskii-structure-properties-large-intersecting_images/imageFile164.png>)

and therefore (33) is satisﬁed for any k and n ≥ 2k + 2.

If 1 < t ≤ k4 and n ≥ 2k + 4t, then (k − t)(n − k − 1) ≥ (k − t)(k + 4t − 1) = k2 + 3kt − 4t2 − k + t > k2, and, therefore, the LHS of (34) is at least

![image 165](<2017-kupavskii-structure-properties-large-intersecting_images/imageFile165.png>)

k3 (k − t)(n − k − 1)(n − k + 1)

k n − k + 1

> 1 −

1 −

,

![image 166](<2017-kupavskii-structure-properties-large-intersecting_images/imageFile166.png>)

![image 167](<2017-kupavskii-structure-properties-large-intersecting_images/imageFile167.png>)

and (33) is satisﬁed again.

Case 3. γ ≥ nk−−34 . As in Case 2 of the proof of Theorem 19, we know that (26) holds. We have to verify that

k t n t

n − t − k − 1 k − t − 1

n − t − 1 k − t − 1

n − 3 k − 2

n − 2 k − 2

≥

−

(35) holds.

+ 2

![image 168](<2017-kupavskii-structure-properties-large-intersecting_images/imageFile168.png>)

Using (19), (21) and (28), the inequality (35) is equivalent to

k − t n − t

![image 169](<2017-kupavskii-structure-properties-large-intersecting_images/imageFile169.png>)

k

n − k + 1 − i n − t − i

1 −

![image 170](<2017-kupavskii-structure-properties-large-intersecting_images/imageFile170.png>)

i=1

If t = 1, then it simpliﬁes to

k

n − k + 1 − i n − 1 − i

1−

![image 171](<2017-kupavskii-structure-properties-large-intersecting_images/imageFile171.png>)

i=1

k(3n − 2k − 2) n(n − 2)

≥

![image 172](<2017-kupavskii-structure-properties-large-intersecting_images/imageFile172.png>)

⇔

k(k − 1)(3n − 2k − 2) n(n − 1)(n − 2)

≥

. (36)

![image 173](<2017-kupavskii-structure-properties-large-intersecting_images/imageFile173.png>)

(n − k)(n − 2k − 2) n(n − 2)

≥

![image 174](<2017-kupavskii-structure-properties-large-intersecting_images/imageFile174.png>)

k

n − k + 1 − i n − 1 − i

.

![image 175](<2017-kupavskii-structure-properties-large-intersecting_images/imageFile175.png>)

i=1

This is equivalent to

(n − 2k − 2) n

≥

![image 176](<2017-kupavskii-structure-properties-large-intersecting_images/imageFile176.png>)

The right hand side is at most

(n − 2k + 1)(n − 2k + 2) (n − 3)(n − 4)

≤

![image 177](<2017-kupavskii-structure-properties-large-intersecting_images/imageFile177.png>)

k

n − k + 1 − i n − 1 − i

. (37)

![image 178](<2017-kupavskii-structure-properties-large-intersecting_images/imageFile178.png>)

i=2

(n − 2k + 4)(n − 2k + 2) n(n − 4)

.

![image 179](<2017-kupavskii-structure-properties-large-intersecting_images/imageFile179.png>)

Therefore (37) follows from n − 2k − 2 n

(n − 2k + 4)(n − 2k + 2) n(n − 4)

≥

![image 180](<2017-kupavskii-structure-properties-large-intersecting_images/imageFile180.png>)

![image 181](<2017-kupavskii-structure-properties-large-intersecting_images/imageFile181.png>)

⇔ (n−2k−2)(n−4) ≥ (n−2k+4)(n−2k+2),

which holds for any n ≥ 2k + 4 and k ≥ 12. If 1 < t ≤ k4 − 2, then

![image 182](<2017-kupavskii-structure-properties-large-intersecting_images/imageFile182.png>)

n − t k − t

k(k − 1)(3n − 2k − 2) n(n − 1)(n − 2)

k(k − 1)(3n − 2k − 2) (k − t)n(n − 1)

1 −

·

≥ 1 −

= (k − t)n2 − (3k2 − 3k − k + t)n + 2(k3 − k) (k − t)n(n − 1)

![image 183](<2017-kupavskii-structure-properties-large-intersecting_images/imageFile183.png>)

![image 184](<2017-kupavskii-structure-properties-large-intersecting_images/imageFile184.png>)

![image 185](<2017-kupavskii-structure-properties-large-intersecting_images/imageFile185.png>)

(k − t)n2 − 3k2n + 2k3 (k − t)n(n − 1)

(∗)

≥

≥

![image 186](<2017-kupavskii-structure-properties-large-intersecting_images/imageFile186.png>)

![image 187](<2017-kupavskii-structure-properties-large-intersecting_images/imageFile187.png>)

(n − k)(n − 2kk2+−ktt ) n(n − 1)

![image 188](<2017-kupavskii-structure-properties-large-intersecting_images/imageFile188.png>)

![image 189](<2017-kupavskii-structure-properties-large-intersecting_images/imageFile189.png>)

(n − k)(n − 2k − k2−ktt) n2

![image 190](<2017-kupavskii-structure-properties-large-intersecting_images/imageFile190.png>)

≥

≥

![image 191](<2017-kupavskii-structure-properties-large-intersecting_images/imageFile191.png>)

(n − k)(n − 2k − 3t) n2

,

![image 192](<2017-kupavskii-structure-properties-large-intersecting_images/imageFile192.png>)

where in the inequality (*) we used the fact that the diﬀerence between the ﬁrst numerator and the second numerator multiplied by by (k − t) is ktn − 2k2t, which is positive for n > 2k; in the last inequality we used that t ≤ k/3. On the other hand,

k

n − k + 1 − i n − t − i

![image 193](<2017-kupavskii-structure-properties-large-intersecting_images/imageFile193.png>)

i=1

k−t−1

n − t − k − i n − t − i

≤

=

![image 194](<2017-kupavskii-structure-properties-large-intersecting_images/imageFile194.png>)

i=1

n − k n

![image 195](<2017-kupavskii-structure-properties-large-intersecting_images/imageFile195.png>)

k−t−1

≤

n − k n

![image 196](<2017-kupavskii-structure-properties-large-intersecting_images/imageFile196.png>)

3k

4 +1

![image 197](<2017-kupavskii-structure-properties-large-intersecting_images/imageFile197.png>)

.

Therefore, combining these calculations, the inequality (36) would follow from the inequality

k n

2k + 3t n

3k/4

≥ 1 −

1 −

. (38)

![image 198](<2017-kupavskii-structure-properties-large-intersecting_images/imageFile198.png>)

![image 199](<2017-kupavskii-structure-properties-large-intersecting_images/imageFile199.png>)

If 2k + 14t ≤ n ≤ 7k, then the right hand side of the inequality above is at most e−

- 3k2

![image 200](<2017-kupavskii-structure-properties-large-intersecting_images/imageFile200.png>)

- 4n < e−


k

10, while the left hand side is at least 2k11+14t t > 2k22+28. It is easy to see that, say, for k ≥ 10, 2k22+28 > e−

![image 201](<2017-kupavskii-structure-properties-large-intersecting_images/imageFile201.png>)

![image 202](<2017-kupavskii-structure-properties-large-intersecting_images/imageFile202.png>)

![image 203](<2017-kupavskii-structure-properties-large-intersecting_images/imageFile203.png>)

k

10. If n > 7k and k ≥ 10, then

![image 204](<2017-kupavskii-structure-properties-large-intersecting_images/imageFile204.png>)

![image 205](<2017-kupavskii-structure-properties-large-intersecting_images/imageFile205.png>)

k n

1 −

![image 206](<2017-kupavskii-structure-properties-large-intersecting_images/imageFile206.png>)

k n

3k/4

< 1 −

![image 207](<2017-kupavskii-structure-properties-large-intersecting_images/imageFile207.png>)

7k n

7

< 1 −

![image 208](<2017-kupavskii-structure-properties-large-intersecting_images/imageFile208.png>)

21k2 n2

4k n

≤ 1 −

+

.

![image 209](<2017-kupavskii-structure-properties-large-intersecting_images/imageFile209.png>)

![image 210](<2017-kupavskii-structure-properties-large-intersecting_images/imageFile210.png>)

On the other hand, 1− 2kn+3t ≥ 1− 3nk, therefore, the inequality (38) is veriﬁed in this case.

![image 211](<2017-kupavskii-structure-properties-large-intersecting_images/imageFile211.png>)

![image 212](<2017-kupavskii-structure-properties-large-intersecting_images/imageFile212.png>)

To conclude, we remark that the only conditions on k that we used for t ≥ 2 were k ≥ 4t + 8 and k ≥ 10. The later one is implied by the former one.

## 6 Degree version of the Erdo˝s Matching Conjecture

The matching number ν(F) of a family F is the maximum number of pairwise disjoint sets from F. That is, intersecting families are exactly the families with matching number one. It is a natural question to ask, what is the largest family with matching number (at most) s. Speaking of uniform families, let us denote ek(n, s) the size of the largest family

![image 213](<2017-kupavskii-structure-properties-large-intersecting_images/imageFile213.png>)

- F ⊂ [nk] with ν(F) ≤ s. Note that this question is only interesting when n ≥ k(s + 1). The following two families are the natural candidates:

A0(n, k, s) := {A ⊂ [n] : A ∩ [s] = ∅},

Ak(k, s) :=

[k(s + 1) − 1] k

.

Erd˝os conjectured [2] that ek(n, s) = max |A0(n, k, s)|, |Ak(k, s)| . This conjecture is known as the Er˝os Matching conjecture. It was studied quite extensively over the last 50 years, but it remains unsolved in general. It is known to be true for k ≤ 3 [7] and for n ≥ (2s + 1)(k − 1) [6]. We note that A0(n, k, s) is bigger than Ak(k, s) already for relatively small n: the condition n > (k + 1)(s + 1) should suﬃce.

A degree version of Erd˝os Matching Conjecture and related problems attracted a lot of attention recently (see, e.g., [15], [22]). The following theorem was proved in [17].

- Theorem 21 ([17]). Given n, k, s with n ≥ 3k2(s + 1), if for a family F ⊂ [nk] with ν(F) ≤ s we have δ1(F) ≤ nk−−11 − n−k−s−11 = δ1(A0(n, k, s)).

This improved the result of Bollob´s, Daykin, and Erd˝os [1], who arrived at the same conclusion for n ≥ 2k3s. The authors conjectured that the same should hold for any n > k(s+1). Note that in the degree version we do not include the family Ak(k, s), since its minimum t-degree is 0 for n ≥ k(s + 1) and t ≥ 1. Note that, for general t we have δt(A0(n, k, s)) = nk−−tt − n−k−s−t t .

In this paper we improve and generalize Theorem 21 above result for k large in comparison to s.

- Theorem 22. Fix n, s, k and t ≥ 1, such that n ≥ 2k2, and k ≥ 5st (k ≥ 3s for t = 1).

For any family F ⊂ [nk] with ν(F) ≤ s we have δt(F) ≤ δ(A0(n, k, s)), with equality only in the case F = A0(n, k, s).

We note that the constants in the proof are not optimal, and chosen in this way to simplify the calculations. In the proof we make use of the stability theorem, proved by the author together with P. Frankl [10, 11]. Recall that τ(F) is the minimal size of a set S ⊂ [n], such that S ∩ F = ∅ for any F ∈ F. For ﬁxed n, s, k, saying that F ⊂ [nk]

satisﬁes ν(F) ≤ s and τ(F) > s is equivalent to saying that F is not isomorphic to a subfamily of A0(n, k, s).

- Theorem 23 ([10]). Let n = (u + s − 1)(k − 1) + s + k, u ≥ s + 1. Then for any family


- G ⊂ [nk] with ν(G) = s and τ(G) ≥ s + 1 we have


|G| ≤

n k

−

n − s k

u − s − 1 u

−

![image 214](<2017-kupavskii-structure-properties-large-intersecting_images/imageFile214.png>)

n − s − k k − 1

. (39)

Proof of Theorem 22. We prove the theorem by contradiction. Fix t ≥ 1 and take a family F with δt(F) > ns−−tt − n−s−s−t t . It cannot be a subfamily of A0(n, k, s) since δt(F) > δt(A0(n, k, s)). Therefore, τ(F) ≥ s + 1 and, assuming that ν(F) ≤ s, we conclude that |F| satisﬁes (39). By simple double counting, we have

δt(F) ≤

) (

(

k t

Note that n−k−s−t t =

![image 215](<2017-kupavskii-structure-properties-large-intersecting_images/imageFile215.png>)

)

n−s t

k t n t

![image 216](<2017-kupavskii-structure-properties-large-intersecting_images/imageFile216.png>)

n k

−

n − s k

) (

(

k t

n−s

k and nk−−tt =

![image 217](<2017-kupavskii-structure-properties-large-intersecting_images/imageFile217.png>)

n t

u − s − 1 u

−

![image 218](<2017-kupavskii-structure-properties-large-intersecting_images/imageFile218.png>)

n − s − k k − 1

)

n

k . We have

.

k

t (u − s − 1)

δt(A0(n, k, s)) − δt(F) ≥

![image 219](<2017-kupavskii-structure-properties-large-intersecting_images/imageFile219.png>)

n

t u

n − s − k k − 1

−

k t n−s t

k t n t

−

![image 220](<2017-kupavskii-structure-properties-large-intersecting_images/imageFile220.png>)

![image 221](<2017-kupavskii-structure-properties-large-intersecting_images/imageFile221.png>)

n − s k

=

k t n t

![image 222](<2017-kupavskii-structure-properties-large-intersecting_images/imageFile222.png>)

u − s − 1 u

![image 223](<2017-kupavskii-structure-properties-large-intersecting_images/imageFile223.png>)

n − s − k k − 1

−

t−1

n − i n − s − i

− 1

![image 224](<2017-kupavskii-structure-properties-large-intersecting_images/imageFile224.png>)

i=0

n − s k

= (∗).

We have ti=0−1 n−n−s−i i −1 ≤ (1+ n−ss−t)t −1. It is not diﬃcult to verify that for θ < 21m one has (1 + θ)m ≤ 1 + 2mθ. Therefore, assuming that

![image 225](<2017-kupavskii-structure-properties-large-intersecting_images/imageFile225.png>)

![image 226](<2017-kupavskii-structure-properties-large-intersecting_images/imageFile226.png>)

![image 227](<2017-kupavskii-structure-properties-large-intersecting_images/imageFile227.png>)

n ≥ s + t + 2st, (40) we have

t−1

n − i n − s − i

2ts n − s − t

− 1 ≤

. (41)

![image 228](<2017-kupavskii-structure-properties-large-intersecting_images/imageFile228.png>)

![image 229](<2017-kupavskii-structure-properties-large-intersecting_images/imageFile229.png>)

i=0

On the other hand, we have (1 − θ)m ≥ 1 − mθ and t ≤ k − 1, and

n−s−k k−1 n−s k

=

![image 230](<2017-kupavskii-structure-properties-large-intersecting_images/imageFile230.png>)

k n − s − k + 1

![image 231](<2017-kupavskii-structure-properties-large-intersecting_images/imageFile231.png>)

i=0

k−1

n − s − k − i + 1 n − s − i

![image 232](<2017-kupavskii-structure-properties-large-intersecting_images/imageFile232.png>)

k n − s − t

>

![image 233](<2017-kupavskii-structure-properties-large-intersecting_images/imageFile233.png>)

k − 1 n − s − k

1 −

![image 234](<2017-kupavskii-structure-properties-large-intersecting_images/imageFile234.png>)

k

>

(k − 1)k n − s − k

k 2(n − s − t)

k n − s − t

1 −

>

, provided

![image 235](<2017-kupavskii-structure-properties-large-intersecting_images/imageFile235.png>)

![image 236](<2017-kupavskii-structure-properties-large-intersecting_images/imageFile236.png>)

![image 237](<2017-kupavskii-structure-properties-large-intersecting_images/imageFile237.png>)

n ≥ s + k + 2k(k − 1). (42) We conclude that, provided that (40) and (42) hold, we get

k t n t

(∗) >

![image 238](<2017-kupavskii-structure-properties-large-intersecting_images/imageFile238.png>)

u − s − 1 u

k 2(n − s − t)

![image 239](<2017-kupavskii-structure-properties-large-intersecting_images/imageFile239.png>)

![image 240](<2017-kupavskii-structure-properties-large-intersecting_images/imageFile240.png>)

2ts n − s − t

−

![image 241](<2017-kupavskii-structure-properties-large-intersecting_images/imageFile241.png>)

n − s k

,

which is nonnegative provided k ≥ 4tsu−us−1. This inequality holds for k ≥ 5ts and

![image 242](<2017-kupavskii-structure-properties-large-intersecting_images/imageFile242.png>)

- u ≥ 9s. The last inequality is satisﬁed for n ≥ 2k2, since then n ≥ 2k2 ≥ (9s + s)k ≥ (9s + s − 1)(k − 1) + s + k. We note that with this choice of n and k both (40) and (42) hold.


For t = 1 one may improve (41) to n−ns − 1 ≤ n−ss and the condition on k may be relaxed to k ≥ 3s. The equality part of the statement follows easily from the fact that strict inequality is obtained in the case when τ(F) ≥ s + 1.

![image 243](<2017-kupavskii-structure-properties-large-intersecting_images/imageFile243.png>)

![image 244](<2017-kupavskii-structure-properties-large-intersecting_images/imageFile244.png>)

![image 245](<2017-kupavskii-structure-properties-large-intersecting_images/imageFile245.png>)

![image 246](<2017-kupavskii-structure-properties-large-intersecting_images/imageFile246.png>)

![image 247](<2017-kupavskii-structure-properties-large-intersecting_images/imageFile247.png>)

![image 248](<2017-kupavskii-structure-properties-large-intersecting_images/imageFile248.png>)

## 7 Conclusion

In this paper we explored several question concerning intersecting families. Some of these questions remain only partially resolved, and it would be highly desirable to settle them.

First of all, it would be desirable to understand the structure of families with diversity

larger than nk−−23 . As shown in [23], no such family exist for n > Ck with some absolute constant C. It is believed to be true for n > 3k − 2. For 2k < n < 3k, however, we do

have such families, and both the proof of the conjecture above and the understanding of their structure is interesting on its own and would be helpful in diﬀerent questions (for more information, see [23]).

In this paper we have applied the machinery of Section 3, based on papers [9], [24], to the setting of general families (see Theorem 16). This gave a reasonable classiﬁcation of all large intersecting families. However, it is by no means complete.

- Problem 1. To what extent one could relax the condition on diversity and/or on t in Theorem 16?
- Problem 2. In terms of Theorem 16, is there a reasonable way to compare the sizes of intersecting families generated by typical minimal families? In particular, we believe that, if F(¯1) contains a typical minimal subfamily G, such that | ∩F∈G F| = t ≥ 5, then

|F| ≤ |Jk−t+1| (43) with equality only possible if F is isomorphic to Js.

We believe that Theorem 16 is an important step towards classiﬁcation of families with large covering numbers τ(F) (the size of the smallest subset that intersects any set from F). An important result in this direction we obtained by Frankl [4], who resolved this problem for τ(F) = 3 and, again, for large enough n = n(k).

- Problem 3. Extend Theorem 16 to families with τ(F) ≥ k. The next question concerns the degree version of the Hilton-Minler theorem.
- Problem 4. Is there an example for n = 2k + 1 (n = 2k + ct, c is a small constant), such that there exists a non-trivial intersecting family F with minimal 1-degree (t-degree) higher than that of the Hilton-Milner family?

One reason to believe that the answer to this question is positive is that the degrees of elements in the Hilton-Milner family are irregular, even if we exclude the element of the highest degree out of consideration.

Finally, the following question concerning cross-intersecting families seem interesting for us.

- Problem 5. Consider two cross-intersecting families A, B ⊂ [nk] that are disjoint. Is it true that


n − 1 k − 1

- 1

![image 249](<2017-kupavskii-structure-properties-large-intersecting_images/imageFile249.png>)

- 2


min{|A|, |B|} ≤

?

## References

- [1] B. Bollob´s, D.E. Daykin, P. Erd˝os, Sets of independent edges of a hypergraph, Quart. J. Math. Oxford Ser. 27 (1976), N2, 25–32.
- [2] P. Erd˝os, A problem on independent r-tuples, Ann. Univ. Sci. Budapest. 8 (1965) 93–95.
- [3] P. Erd˝os, C. Ko, R. Rado, Intersection theorems for systems of ﬁnite sets, The Quarterly Journal of Mathematics, 12 (1961) N1, 313–320.
- [4] P. Frankl, On intersecting families of ﬁnite sets, Bull. Austral. Math. Soc. 21 (1980), 363– 372.
- [5] P. Frankl, Erdos-Ko-Rado theorem with conditions on the maximal degree, Journal of Combinatorial Theory, Series A 46 (1987), N2, 252–263.
- [6] P. Frankl, Improved bounds for Erd˝s’ Matching Conjecture, Journ. of Comb. Theory Ser. A 120 (2013), 1068–1072.
- [7] P. Frankl, On the maximum number of edges in a hypergraph with given matching number, Discrete Applied Mathematics 216 (2017), 562–581.
- [8] P. Frankl, J. Han, H. Huang, Y. Zhao A degree version of Hilton-Milner theorem, arXiv:1703.03896v2
- [9] P. Frankl, A. Kupavskii, Erd˝s-Ko-Rado theorem for {0, ±1}-vectors, arXiv:1510.03912
- [10] P. Frankl, A. Kupavskii, Families with no s pairwise disjoint sets, Journal of London Mathematical Society (2017), arXiv:1607.06122
- [11] P. Frankl, A. Kupavskii, Two problems of P. Erd˝s on matchings in set families, submitted, arXiv:1607.06126
- [12] P. Frankl, N. Tokushige, Some best possible inequalities concerning cross-intersecting families, Journal of Combinatorial Theory, Series A 61 (1992), N1, 87–97.
- [13] P. Frankl, N. Tokushige, A note on Huang–Zhao theorem on intersecting families with large minimum degree, Discrete Mathematics 340 (2016), N5, 1098–1103.
- [14] J. Han, Y. Kohayakawa, The maximum size of a non-trivial intersecting uniform family that is not a subfamily of the Hilton–Milner family, Proc. Amer. Math. Soc. 145 (2017) N1, 73–87.
- [15] H. H´an, Y. Person, M. Schacht, On perfect matchings in uniform hypergraphs with large minimum vertex degree, SIAM Journal on Discrete Mathematics 23 (2009), N2, 732–748.
- [16] A.J.W. Hilton, E.C. Milner, Some intersection theorems for systems of ﬁnite sets, Quart. J. Math. Oxford 18 (1967), 369–384.
- [17] H. Huang and Y. Zhao, Degree versions of the Erd˝s-Ko-Rado theorem and Erd˝s hypergraph matching conjecture, J. Combin. Theory Ser. A, to appear


- [18] F. Ihringer, A. Kupavskii, Regular intersecting families, preprint.
- [19] G. Katona, A theorem of ﬁnite sets, “Theory of Graphs, Proc. Coll. Tihany, 1966”, Akad, Kiado, Budapest, 1968; Classic Papers in Combinatorics (1987), 381-401.
- [20] A. Kostochka, Dhruv Mubayi, The structure of large intersecting families Proc. Amer. Math. Soc. 145 (2017), N6, 2311–2321.
- [21] J.B. Kruskal, The Number of Simplices in a Complex, Mathematical optimization techniques 251 (1963), 251-278.
- [22] D. K¨uhn, D. Osthus, Embedding large subgraphs into dense graphs, Surveys in combinatorics (2009). Papers from the 22nd British combinatorial conference, St. Andrews, UK, July 5–10, 2009, pages 137–167.
- [23] A. Kupavskii, Diversity of intersecting families, submitted
- [24] A. Kupavskii, D. Zakharov, Regular bipartite graphs and intersecting families, arXiv:1611.03129


