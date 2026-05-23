# arXiv:1301.0096v2[math.CO]7Sep2013

## The Structure of Critical Product Sets

Matt DeVos∗ mdevos@sfu.ca

November 3, 2021

Abstract

Let G be a multiplicative group, let A,B ⊆ G be ﬁnite and nonempty, and deﬁne the product set AB = {ab | a ∈ A and b ∈ B}. Two fundamental problems in combinatorial number theory are to ﬁnd lower bounds on |AB|, and then to determine structural properties of A and B under the assumption that |AB| is small. We focus on the extreme case when |AB| < |A| + |B|, and call any such pair (A,B) critical.

In the case when |G| is prime, the Cauchy-Davenport Theorem asserts that |AB| ≥ min{|G|,|A|+|B|−1}, and Vosper reﬁned this result by classifying all critical pairs in these groups. For abelian groups, Kneser proved a natural generalization of CauchyDavenport by showing that there exists H ≤ G so that |AB| ≥ |A| + |B| − |H| and ABH = AB. Kemperman then proved a result which characterizes the structure of all critical pairs in abelian groups.

Our main result gives a classiﬁcation of all critical pairs in an arbitrary group G. As a consequence of this we derive the following generalization of Kneser’s Theorem to arbitrary groups: There exists H ≤ G so that |AB| ≥ |A| + |B| − |H| and so that for every y ∈ AB there exists x ∈ G so that y(x−1Hx) ⊆ AB.

#### Outline

Our proof involves an early departure from the problem of classifying critical product sets in a group G to an alternate problem of classifying certain specially structured incidence geometries on which G has a natural action. So, we will ﬁrst derive a structure theorem for these incidence geometries, and then deduce our structure theorem for product sets from this. To help illuminate the structure of this paper, we begin with a diagram showing dependencies among our sections and a table oﬀering a brief description of the content of

∗Supported in part by an NSERC Discovery Grant (Canada) and a Sloan Fellowship.

###### each section. This is followed by a ﬁgure showing the relationships among some of our lemmas, theorems, and corollaries.

###### Product Sets Incidence Geometry

|14. Corollaries|
|---|


|13. The Structure of Critical Subset Trios|
|---|


|6. The Main Theorem|
|---|


|12. Maximality of Songs|
|---|


|10. Near Graphs and Doubling Blocks|
|---|


|Sequences<br><br>9. Sequences and Near|
|---|


|11. Clips and Near Clips|
|---|


|7. Graphs|
|---|


|8. Octahedral Choruses|
|---|


|Duets and Trios<br><br>5. Basic Properties of|
|---|


|4. The Structure of Critical Trios|
|---|


|2. Dihedral Groups and The Classiﬁcation|
|---|


|3. Incidence Trios|
|---|


|1. Introduction|
|---|


|Section<br><br>|Content|
|---|---|
|1<br>2<br>3<br>4<br>5<br>6<br>7-11<br><br><br>12<br>13<br>14<br>|A discussion of lower bounds on sizes of product sets, structure theorems for critical product sets, and a rough sketch of our proof.<br><br>Statement of our classiﬁcation theorem for critical product sets.<br><br>An introduction to the incidence geometries we classify, and an example to motivate this approach.<br><br>Statement of our main classiﬁcation theorem (incidence geometry).<br><br>Numerous basic properties of our incidence geometries are established.<br><br>Proof of the main theorem (hard direction) assuming numerous lemmas.<br><br>Proofs of the lemmas required for the main theorem.<br><br>The easy direction of the main theorem is proved.<br><br>A derivation of our classiﬁcation theorem for critical product sets from our classiﬁcation theorem on incidence geometries<br><br>Some corollaries of the main result are established.|


|Corollaries 1.3, 1.4 generalized Kneser|
|---|


|Corollary 1.5 Stability/Structure|
|---|


|Corollary 1.10 |A2| < 2|A||
|---|


|Theorem 2.3 Subset Classiﬁcation|
|---|


|Corollary 14.1 Weak Structure|
|---|


|Corollary 14.4 |AB| < 2min{|A|,|B|}|
|---|


Product Sets Incidence Geometry

|Theorem 4.7 Main Classiﬁcation|
|---|


|Lemma 5.12 Disconnected Trios|
|---|


|Lemmas 6.2, 6.6, 6.7 (stability)|
|---|


|Lemma 6.8 Light Sides|
|---|


|Maximality Lemmas 12.1 Impure Beat<br><br>12.3 Dihedral Chord<br>12.4 Video<br>|
|---|


|Stability Lemmas 7.10 Graph<br><br>9.13 Near Sequence<br>10.10 Near Graph<br>11.5 Clip 11.10 Near Clip<br>|
|---|


|Light Side Lemmas<br><br>7.13 Video 9.10 Chord|
|---|


#### 1 Introduction

Except where noted, all groups will be written multiplicatively, and let us now ﬁx such a group G. For a set A ⊆ G we let A = G \ A and we deﬁne A−1 = {g−1 | g ∈ A}. If B ⊆ G then we deﬁne the product set of A and B to be AB = {ab | a ∈ A and b ∈ B}. For an element g ∈ G we let gA = {g}A and let Ag = A{g}, and we call a set of either form a shift of A.

One of the central goals in combinatorial number theory is to understand the structure of ﬁnite sets A,B ⊆ G for which the product set AB is small. This program began in earnest with the pioneering work of Freiman [14], and has been further developed through the contributions of Ruzsa [41] and numerous others. Quite recently, a breakthrough by Breuillard, Green, and Tao [3] has established a powerful rough structure theorem for arbitrary groups.

Our interest here is in the exceptional case when a pair (A,B) of ﬁnite subsets of G satisfy |AB| < |A| + |B|, and in this case we deﬁne (A,B) to be critical. Although there are numerous constructions of critical pairs, this is a suitably restrictive notion to hope for

- a precise structure theorem. Vosper [51] [52] proved such a characterization for groups of prime order, Kemperman [29] extended this to abelian groups, and the goal of this paper is to prove a characterization which holds for an arbitrary group. We will also apply this structure theorem to derive some new lower bounds on the sizes of product sets.


The remainder of this section is organized as follows. In the ﬁrst subsection we discuss old and new lower bounds on sizes of product sets, and in the second we give a brief overview of some existing structure theorems concerning critical product sets in nonabelian groups. In the third and fourth subsections, we will transform the problem of classifying critical product sets into a new problem concerning the classiﬁcation of certain triples of subsets we call maximal critical subset trios. The ﬁfth subsection contains a description of Vosper’s Theorem and Kemperman’s Theorem, and in the sixth and last subsection we give a rough sketch of our proof. (The statement of our structure theorem for critical product sets is postponed to the following section.)

##### 1.1 Lower Bounds

The starting point for the study of small product sets is the following famous result, which was ﬁrst proved by Cauchy and then rediscovered by Davenport. For every positive integer n we let Cn denote a cyclic group of order n

- Theorem 1.1 (Cauchy [5] - Davenport [7]) If p is prime and A,B ⊆ Cp are nonempty, then

|AB| ≥ min{p,|A| + |B| − 1}. Kneser generalized this result to abelian groups as follows.

- Theorem 1.2 (Kneser [31]) If G is abelian and A,B ⊆ G are ﬁnite and nonempty, then there exists H ≤ G so that


- 1. |AB| ≥ |A| + |B| − |H|
- 2. ABH = AB.


The above theorem does not hold for general nonabelian groups even if we replace property 2 above with the weaker statement that H must satisfy one of the conditions: ABH = AB or AHB = AB or HAB = AB. This was demonstrated by Olson in [39] and will be discussed later in this section. The following corollary of our main theorem generalizes Kneser’s Theorem by weakening the second property in a diﬀerent manner.

- Corollary 1.3 If A,B ⊆ G are ﬁnite and nonempty, there exists H ≤ G so that


- 1. |AB| ≥ |A| + |B| − |H|
- 2. For every y ∈ AB there exists x ∈ G so that y(x−1Hx) ⊆ AB.


There is an equivalent form of Kneser’s Theorem where the ﬁrst condition is replaced by the following stronger inequality:

|AB| ≥ |AH| + |BH| − |H|.

A similar statement also holds for general groups. For a set A ⊆ G and a subgroup H ≤ G, we say that A is left (right) H-stable if HA = A (AH = A), and we say that A is H-stable if it is both left and right H-stable. We say that A is H-conj-stable if for every y ∈ A there exists x ∈ G so that y(x−1Hx) ⊆ A (note that x−1Hxy = y((xy)−1Hxy) so there is no distinction here between y multiplied on the left or right by a conjugate of H).

- Corollary 1.4 If A,B ⊆ G are ﬁnite and nonempty, there exists H ≤ G and A∗,B∗ ⊆ G with A ⊆ A∗ and B ⊆ B∗ so that

- 1. A∗B∗ = AB
- 2. |AB| ≥ |A∗| + |B∗| − |H|
- 3. A∗, B∗, AB, and (AB)−1 are H-conj-stable.


Next we shall introduce an important parameter. Deﬁne the deﬁciency of a pair of ﬁnite subsets (A,B) of G to be δ(A,B) = |A| + |B| − |AB|. So, a pair has positive deﬁciency if and only if it is critical. Also, note that all of the aforementioned theorems may be viewed as upper bounds on the deﬁciency of a pair (A,B).

Although it is not possible to replace the condition of conjugate stability in the previous two corollaries with the more desirable notions of left or right stability, by looking “one step” into our structure theorem, we may obtain the following result which either gives some stronger stability properties, or gives us some structural information about the sets A and B. Let us note that this result has a stronger form, Corollary 14.1 (a weak version of the full structure theorem) which appears in the ﬁnal section of the paper.

- Corollary 1.5 (Structure/Stability) If A,B ⊆ G are ﬁnite, then one of the following holds.


- 1. One of A, B, or AB is contained in a coset of a proper subgroup.

- 2. There exists a ﬁnite subgroup H G satisfying δ(A,B) ≤ 21|H| and one of:


- (a) G/H is cyclic, |G/H| ≥ 4, and max{|AH \ A|,|BH \ B|} + δ(A,B) ≤ |H|.


- (b) G/H is dihedral, |G/H| ≥ 8, and max{|AH \ A|,|BH \ B|} + δ(A,B) ≤ 2|H|.


- 3. There exist H1,H2,H3 ≤ G so that H1AH2BH3 = AB and δ(A,B) ≤ min1≤i≤3 |Hi|.


There is already a wide body of existing results which provide upper bounds on the deﬁciency of a pair of sets in a nonabelian group under various assumptions. Although we will not give an extensive overview of these, we will highlight a couple signiﬁcant results of this type which relate closely with this article. Below is a theorem due to Kemperman which has a very similar structure to our Corollary 1.3.

- Theorem 1.6 (Kemperman [28]) If A,B ⊆ G are ﬁnite and nonempty and a ∈ A and

b ∈ B, there exists H ≤ G so that

- 1. δ(A,B) ≤ |H|
- 2. aHb ⊆ AB.


The preceding theorem is also consequence of Corollary 1.3. To see this, let a ∈ A and b ∈ B and then apply this corollary to choose H ≤ G and x ∈ G so that |AB| ≥

- |A| + |B| − |H| and (ab)(x−1Hx) ⊆ AB. Now setting K = bx−1Hxb−1 we have that |AB| ≥ |A| + |B| − |K| and aKb = a(bx−1Hxb−1)b = ab(x−1Hx) ⊆ AB. Indeed, we may view Corollary 1.3 as a uniform version of this theorem of Kemperman.


We close this subsection with an important deﬁciency bound which will play a key early role in our proof. In Subsection 1.3 we will call upon this result to reduce the overall classiﬁcation problem.

- Theorem 1.7 (Kemperman, Scherk1 [28]) If A,B ⊆ G are ﬁnite and nonempty, then


δ(A,B) ≤ min

|{(a,b) ∈ A × B | ab = z}|.

z∈AB

##### 1.2 Structure

In this subsection we will brieﬂy discuss some existing partial results on the structure of critical product sets in arbitrary groups, and we will mention one more corollary of our structure theorem. Our focus here will be on nonabelian groups, since Kemperman’s structure theorem (which gives a complete description in the abelian case) will be treated in detail later in this section. Again, we have made no eﬀort to give a comprehensive survey, and will present only a handful of results which connect closely with this work.

1We have followed Lev [32] in attributing this result.

Fix a ﬁnite nonempty set B ⊂ G and note that for every ﬁnite nonempty set A ⊆ G we must have δ(A,B) = |A| + |B| − |AB| ≤ |B|. In light of this we may deﬁne

δ(B) = max{δ(A,B) | A ⊆ G is ﬁnite and A,AB = ∅}.

Below we state a theorem of Hamidoune concerning δ(B) which extends some related results of Mann [36] and Z´emor [54]. A variant of this result will play an important role in our proof.

- Theorem 1.8 (Hamidoune [19]) If B ⊂ G is ﬁnite and nonempty, there exists a ﬁnite set

- A ⊆ G so that A,AB = ∅, and δ(A,B) = δ(B), and either A or AB is a ﬁnite subgroup.


This theorem was one of many which Hamidoune proved using the isoperimetric method (see also [21], [18], [23], [22]), and in fact he proved a generalization of this result which holds in the setting of vertex transitive digraphs, and is quite closely related to the precise result we will utilize. Indeed, our incidence geometries are close relatives of Hamidoune’s vertex transitive graphs, and our basic technique is a variant of the isoperimetric method. As such, this work may be viewed as a continuation of Hamidoune’s central program.

In one of his last papers, Hamidoune [24] investigated sets B for which δ(B) = 1 and there exists A ⊆ G with |A|,|AB| ≥ 2 for which δ(A,B) = 1, and this work was then sharpened by Serra and Z´emor [46]. These authors obtain a structure theorem for such sets which is a special case of our main result. Namely, they prove that either there exists a set A as in the statement of Hamidoune’s Theorem for which either A or AB is a nontrivial subgroup of G, or the set B is a geometric progresion, or there exists a set A and a ﬁnite subgroup H ≤ G so that δ(A ,B) = 1 and both A and A B are unions of two right H-cosets.

Next we shall introduce another recent theorem giving some structural information about critical product sets. The essential ingredients for the proof of this theorem were provided by Hamidoune [25] in response to a question of Tao [48], but the result was proved in this form by Tao [47], so we have credited both with the theorem. This gives a generalization to nonabelian groups of a consequence of Kneser’s Theorem.

- Theorem 1.9 (Hamidoune [25], Tao [47]) Let A,B ⊆ G be ﬁnite and nonempty and assume |A| ≥ |B| and |AB| ≤ (2 − )|B| for some > 0. Then one of the following holds.


- 1. B is contained in a coset of a ﬁnite subgroup H with |H| ≤ 2 |B|.

- 2. B can be covered by at most 2 − 1 right H cosets for some H ≤ G with |H| ≤ |B|.


The above result may also be deduced (in somewhat stronger form) from Corollary 14.4 of our structure theorem.

A case of particular interest in small product set problems, is ﬁnite subsets A ⊆ G for which the set A2 = AA has small size. In the very extreme case when |A2| < 1.5|A|, Freiman proved that the following property holds (see [12])

- (1) There exists H ≤ G and x ∈ G so that A ⊆ xH = Hx and A2 = x2H.

Freiman [15] also proved a structure theorem for sets A with |A2| < 1.6|A|, and a modern translation of this appears in Husbands’ Masters Thesis [27]. Here it is proved that such sets must either satisfy (1) above or the following property.

- (2) There exists K ≤ G so that the set B = KAK satisﬁes |B| = 2|K| and |B2| = 3|K|.


In fact, whenever (2) holds, there exist subgroups L ≤ K ≤ H ≤ G and x ∈ G so that B ⊆ xH = Hx and [K : L] ≤ 2, and furthermore L is a normal subgroup of H with the property that H/L is either cyclic or dihedral. So, in eﬀect, this critical phenomena can be found either in a cyclic or a dihedral group (more precisely, setting C = x−1B and D = Bx−1, we have that the images of C and D under the canonical homomorphism from H to H/L form a critical pair). A proof of the existence of these subgroups L,H appears in the appendix. It relies only upon material appearing in Section 3.

Our main theorem specializes to sets A with |A2| < 2|A| to give the following result. This corollary also has a stronger form, Corollary 14.4, which gives added structural information in the second and third outcomes (and also applies more generally to pairs (A,B) for which |AB| < min{|A|,|B|}).

Corollary 1.10 Let A ⊆ G be ﬁnite with |A| ≥ 2 and |A2| < 2|A|. If x ∈ A and H is the unique minimal subgroup for which A ⊆ xH, then xH = Hx and there exists K < H satisfying one of the following.

- 1. There exists y ∈ H so that x2H \ x2yK ⊆ A2.
- 2. K H, and H/K is cyclic with order at least 4, and δ(A,A) + |AK \ A| ≤ |K|.
- 3. K H, and H/K is dihedral with order at least 8, and δ(A,A) + |AK \ A| ≤ 2|K|.


##### 1.3 Tight Critical Pairs

In this subsection we will simplify the task of classifying all critical pairs by ﬁrst identifying some trivial constructions, and then reducing the general problem to that of classifying certain special critical pairs we call tight.

Let (A,B) be a critical pair in G. If exactly one of A, B is empty then (A,B) will be critical (as AB = ∅) and we call such a pair trivial. Another case of little interest is when

- G is ﬁnite and |A| + |B| > |G|. Here, it follows immediately that (A,B) will be critical.


However, in this case we must also have AB = G (to check this, note that for every g ∈ G we have B ∩ A−1g = ∅ so there will exist x ∈ A for which x−1g ∈ B). Therefore, the critical pairs (A,B) with AB = G are precisely those A,B for which |A| + |B| > |G| and accordingly, we shall also call these trivial. Having deﬁned these, we now turn our attention to nontrivial critical pairs.

We deﬁne (A,B) to be tight if the only sets A∗ ⊇ A and B∗ ⊇ B for which A∗B∗ = AB are given by A∗ = A and B∗ = B. Fortunately, the problem of classifying all critical pairs reduces to the problem of classifying tight critical pairs, as shown by the following result.

- Theorem 1.11 The pair (A,B) is critical if and only if there exists a tight critical pair (A∗,B∗) for which A ⊆ A∗ and B ⊆ B∗ and the following equation holds:


|A∗ \ A| + |B∗ \ B| < δ(A∗,B∗).

Proof: First suppose that (A,B) is a critical pair and choose A∗ ⊇ A and B∗ ⊇ B maximal so that A∗B∗ = AB (it follows immediately from the fact that AB is ﬁnite that such maximal sets exist). This gives us

δ(A∗,B∗) = |A∗ \ A| + |B∗ \ B| + δ(A,B) > |A∗ \ A| + |B∗ \ B|.

Next let (A∗,B∗) be a tight critical pair and let A ⊆ A∗ and B ⊆ B∗ satisfy |A∗ \

- A| + |B∗ \ B| < δ(A∗,B∗). Theorem 1.7 implies that every element in A∗B∗ has at least δ(A∗,B∗) representations as a product of an element in A∗ times an element in B∗. It follows from this and |A∗ \A|+|B∗ \B| < δ(A∗,B∗) that AB = A∗B∗. Therefore, the pair (A,B) satisﬁes δ(A,B) = |A| + |B| − |AB| > |A∗| + |B∗| − δ(A∗,B∗) − |A∗B∗| = 0 so it is critical.


##### 1.4 Subset Trios

In the study of critical pairs (A,B), there is a third set of signiﬁcant interest which deserves to considered together with A and B, namely C = (AB)−1. For simplicity, ﬁrst suppose that G is ﬁnite, and that (A,B) is a nontrivial critical pair, and observe the following two properties:

- • |A| + |B| + |C| > |G|,
- • 1  ∈ ABC.


Given the above, it follows that the pair (B,C) is also critical (to see this, note that BC must be disjoint from A−1, so it will have size at most |G|−|A| < |B|+|C|). Similarly, we have 1  ∈ CAB, so (C,A) is also a critical pair. In light of this, we shall now extend our deﬁnitions to triples. To allow for the possibility that G is inﬁnite, we will permit sets in our triples to be inﬁnite if they are coﬁnite.

Deﬁnition: If A,B,C ⊆ G are all ﬁnite or coﬁnite and 1  ∈ ABC then we deﬁne (A,B,C) to be a subset trio (in G).

Next we extend some of our earlier terminology from pairs to subset trios. We call the subset trio (A,B,C) trivial if one of A, B, or C is empty. Note that for a nontrivial subset trio, at most one of the three sets may be inﬁnite. Set n to be the size of the complement of a largest set in (A,B,C) and let  ,m be the sizes of the other two sets in (A,B,C). Then we deﬁne the deﬁciency of (A,B,C) to be δG(A,B,C) = + m − n (we permit δG(A,B,C) = ∞ if two of A,B,C are inﬁnite and δG(A,B,C) = −∞ if A,B,C are ﬁnite but G is inﬁnite), and we say that (A,B,C) is critical if δ(A,B,C) > 0. As usual, we drop the subscript when the group is clear from context. A subset trio (A,B,C) is maximal if the only subset trio (A∗,B∗,C∗) with A ⊆ A∗ and B ⊆ B∗ and C ⊆ C∗ is given by

- A = A∗ and B = B∗ and C = C∗. Equivalently, (A,B,C) is maximal if C = (AB)−1 and A = (BC)−1 and B = (CA)−1. The natural motivation for these deﬁnitions is the following.


If A,B are ﬁnite subsets of G and C = (AB)−1 then:

- • (A,B) is trivial if and only if (A,B,C) is trivial,
- • (A,B) is critical if and only if (A,B,C) is critical,
- • δ(A,B) = δ(A,B,C),
- • (A,B) is tight if and only if (A,B,C) is maximal.


It is immediate that whenever (A,B,C) is a subset trio, the triples (B,C,A), (C,A,B), (C−1,B−1,A−1), (B−1,A−1,C−1), and (A−1,C−1,B−1) will also be subset trios. Similarly, for every g ∈ G the triples (Ag,g−1B,C), (A,Bg,g−1C), and (g−1A,B,Cg) will be subset trios. All of these transformations preserve the properties of interest to us (nontrivial, critical, maximal, deﬁciency). Accordingly, we will say that any subset trio obtained from (A,B,C) by a sequence of these transformations is similar to (A,B,C).

At this point, we have transformed the original problem of classifying critical pairs to the new problem of classifying nontrivial maximal critical subset trios.

##### 1.5 Classical Critical Subset Trios

In this subsection we will describe some classical constructions of critical subset trios, and state the theorems of Vosper and Kemperman. Although Vosper’s Theorem has a fairly simple form, Kemperman’s Theorem is somewhat complicated to state. Indeed, the diﬃculty of his theorem and his paper lead at one point to some confusion about the precise nature of his results. Fortunately, this situation has been remedied by recent work of Grynkiewicz [16] [17], Hamidoune [26] [23], and Lev [33]. Notably, Lev [33] gives a top-down version of Kemperman’s Theorem which is considerably easier to work with. We shall adopt this framework throughout.

We begin with two easy constructions for critical pairs. The ﬁrst construction is to take one of the sets to be a singleton. For instance, if A = {a} then |AB| = |B| and so (A,B) will be critical. For our second construction, we require some additional notation. We deﬁne any set of the form A = {gi | 0 ≤ i ≤ } for g ∈ G to be a basic geometric progression with ratio g. We say that this progression is nontrivial if it has size at least two and proper if g +1  ∈ A. More generally, we deﬁne a geometric progression2 with ratio g to be any set of the form hA where h ∈ G and A is a basic geometric progression with ratio g, and we say that this geometric progression is nontrivial (proper) if A has this property. Now suppose that A and B are proper basic geometric progressions with ratio g, say A = {gi | 0 ≤ i ≤ } and B = {gi | 0 ≤ i ≤ m}. In this case |A| = + 1 and

- |B| = m + 1 and AB = {gi | 0 ≤ i ≤ + m} satisﬁes |AB| ≤ + m + 1, so (A,B) is critical. We may extend this pair to a critical subset trio by deﬁning C = (AB)−1. Up to our equivalence relation, this gives all of the possibilities for nontrivial critical trios in groups of prime order.


- Theorem 1.12 (Vosper [51], [52]) If (A,B,C) is a nontrivial critical subset trio in Cp for p prime, then one of the following holds.


- 1. min{|A|,|B|,|C|} = 1
- 2. A,B,C are geometric progressions with a common ratio.


For groups with nontrivial subgroups, there are natural generalizations of these critical subset trios which we shall now deﬁne. For a set A ⊆ G, the left stabilizer of A is stabL(A) = {g ∈ G | gA = A} and the right stabilizer of A is stabR(A) = {g ∈ G | Ag = A}. Note that stabL(A) and stabR(A) are both subgroups of G and that A is left (right) H-stable if and only if H ≤ stabL(A) (H ≤ stabR(A)).

2Since we will only consider geometric progressions in abelian groups, we have not concerned ourselves with right vs. left multiplication here.

Deﬁnition: Let H < G be ﬁnite. A subset trio is a pure beat relative to H if it is similar to a subset trio (A,B,C) satisfying:

- 1. A = H
- 2. stabL(B) = H
- 3. C = (AB)−1.


Observe that every pure beat relative to H is a maximal nontrivial critical trio (with deﬁciency |H|).

If H G, we let ϕG/H : G → G/H denote the canonical homomorphism.

Deﬁnition: Let H G be ﬁnite with G/H is cyclic and |G/H| ≥ 5. A subset trio is a pure cyclic chord relative to H if there exists a similar subset trio (A,B,C) and S ∈ G/H which generates G/H satisfying:

- 1. A,B,C are H-stable.
- 2. ϕG/H(A) and ϕG/H(B) are nontrivial basic geometric progressions with ratio S.
- 3. C = (AB)−1 is not contained in a single H-coset.


Note that every pure cyclic chord relative to H is a maximal critical subset trio with deﬁciency |H|.

Next we shall introduce two structures which are similar to pure beats and pure chords, but allow for recursive constructions of critical pairs and critical subset trios.

| |
|---|
| |
| |
| |
| |
| |
| |


| |
|---|
| |
| |
| |
| |
| |
| |


| |
|---|
| |
| |
| |
| |
| |
| |


Hx3 Hx3

- Hx1
- Hx2


- Hx1
- Hx2


H

H H

A B AB

| |
|---|


Figure 1: An impure beat

Deﬁnition: Let H < G. A subset trio Φ is an impure beat relative to H if there exists an similar subset trio (A,B,C) which satisﬁes the following properties.

- 1. A ⊆ H
- 2. H ≤ stabL(B \ H)
- 3. C \ H = (AB)−1 \ H

- 4. B ∩ H and C ∩ H are nonempty.


In this case we deﬁne the (nontrivial) subset trio Φ = (A,B ∩ H,C ∩ H) in the group H, to be a continuation of Φ. Observe that δH(Φ ) = δG(Φ) and that Φ is maximal whenever Φ is maximal.

In our deﬁnition of pure beats, we insisted that the subgroup H be ﬁnite, however this restriction was not included in the deﬁnition of impure beat. This restriction is actually implied for pure beats, as otherwise the deﬁnitions would force all of A, B, and C to be inﬁnite. For impure beats, if H is inﬁnite, then either B or C is contained in a single H-coset. This is a natural possibility which is straightforward to construct. To do so, let

- H be an inﬁnite subgroup of G, let (A,B) be a nontrivial critical pair from H, and set


- C = (AB)−1.


Let us pause here to make another comment concerning the above construction. One might have hoped to generalize Kneser’s Theorem to nonabelian groups by showing that for every pair A,B of ﬁnite nonempty subsets of a group there exist subgroups H1,H2,H3 ≤ G for which H1AH2BH3 = AB and |AB| ≥ |A| + |B| − max{|H1|,|H2|,|H3|}. However, this statement is false. In [39], Olson constructs sets A,B for which |AB| < |A|+|B|−1 and the only possible subgroups H1,H2,H3 with H1AH2BH3 = AB are given by H1 = H2 = H3 = {1}. In our language, his construction uses impure beats, and it is not diﬃcult to indicate the key principle involved in this construction. First note that in the language of trios, we wish to construct a maximal subset trio (A,B,C) for which δ(A,B,C) ≥ 2 and each of A,

- B, and C has trivial right and left stabilizers. Suppose now that (A,B,C) is an impure beat


relative to H where A ⊆ H and H ≤ stabL(B \ H) and that (A ,B ,C ) is a continuation as given in the deﬁnition of impure beat. In this case, it is quite possible that there exists a nontrivial subgroup H3 < H so that B H3 = B and H3C = C but BH3 = B and H3C = C. So, in other words, the outer structure of the impure beat (A,B,C) may spoil the stabilizer behaviour found in the continuation. Olson’s construction uses a nesting of impure beats to spoil all of the stabilizers.

Deﬁnition: Let H G be ﬁnite with G/H is cyclic and |G/H| ≥ 4. A subset trio Φ is an impure cyclic chord relative to H if there exists a similar trio (A,B,C) and S ∈ G/H which generates G/H satisfying

- 1. A ∪ H and B ∪ H are H-stable.


| |
|---|
| |
| |
| |
| |
| |
| |


| |
|---|
| |
| |
| |
| |
| |
| |


| |
|---|
| |
| |
| |
| |
| |
| |


R4

- R2 R

R2

- R3 R3


R

R

H H H

A B AB

| |
|---|


Figure 2: An impure cyclic chord

- 2. ϕG/H(A) and ϕG/H(B) are nontrivial basic geometric progressions with ratio S.
- 3. C \ H = (AB)−1 \ H = ∅ and C ∩ H = ∅.


We call the (nontrivial) subset trio Φ = (A ∩ H,B ∩ H,C ∩ H) a continuation of Φ. Observe that δH(Φ ) = δG(Φ), and that Φ is maximal whenever Φ is maximal. With this terminology in place, we are ready to state Kemperman’s Theorem.

- Theorem 1.13 (Kemperman [29]) If Φ is a nontrivial maximal critical subset trio in the abelian group G, there exists a sequence of subgroups G = G1 > G2 ... > Gm and a sequence of subset trios Φ = Φ1,Φ2,...,Φm so that the following hold


- 1. Φi is a subset trio in the group Gi for 1 ≤ i ≤ m.
- 2. Φi is an impure beat or impure cyclic chord with continuation Φi+1 for 1 ≤ i < m.
- 3. Φm is either a pure beat or a pure cyclic chord.


Our methods do specialize to give an alternative proof of Kemperman’s Theorem. However, there is little need to pass to the setting of incidence geometry when working with abelian groups, and certain aspects of our argument can be simpliﬁed signiﬁcantly in this setting. In a paper together with Boothby and Montejano [2], we have carried through these simpliﬁcations to obtain a new proof of Kemperman’s Theorem.

##### 1.6 Proof Sketch

In order to prove our result, we will move from the world of product sets and subsets of groups to the world of incidence geometries equipped with group actions. Following the next section (where our characterization theorem for critical subset trios is stated), we will

turn our attention to these incidence geometries, and this is the setting in which all of the heavy lifting of the proof will be done. Although this departure is well precedented, it has the side eﬀect that the partial results we prove have a rather diﬀerent appearance from those found in earlier works. Despite this, all of the essential ingredients in our proof are very standard combinatorial intersection-union and induction arguments which have been well established by numerous authors. To help account for some of these important contributions we will give a brief overview of these ideas next.

The practice of exchanging a pair of sets A,B from a common ground set by A∩B,A∪B we will casually refer to as uncrossing, and it has a surprisingly rich history in the world of combinatorics. From additive number theory, there are numerous transforms which are based on uncrossing together with shifting sets. These transforms are key ingredients in the proofs of the Cauchy-Davenport Theorem and Kneser’s Theorem (see [37]), the results from the ﬁrst section due to Kemperman and Scherk, and numerous other theorems. In the world of graph theory, Mader [35] [34] and Watkins [53] exploited uncrossing arguments to achieve a number of important theorems concerning connectivity properties of vertex transitive graphs, and these tools have been further developed by many other authors. In fact, connectivity of vertex transitive graphs is intimately linked with the study of small product sets. Hamidoune was among the ﬁrst to recognize the importance of this connection, and his work helped to establish a rich bridge between these worlds. Our program of working in incidence geometries is a natural extension of Hamidoune’s methodology.

Although our work will be done in a diﬀerent setting, it is possible to describe the analogue of our procedure in the framework of product sets, so we shall give a rough sketch of this here. The basic property upon which all of our results are based is the following uncrossing property: If (A,B,C) and (A ,B ,C) are subset trios, then (A ∩ A ,B ∪ B ,C) and (A ∪ A ,B ∩ B ,C) are also subset trios and

δ(A ∩ A ,B ∪ B ,C) + δ(A ∪ A ,B ∩ B ,C) = δ(A,B,C) + δ(A ,B ,C). (1)

We will take advantage of this in numerous ways, but let us highlight one here. Suppose that (A,B,C) is critical, let g ∈ G, and set A = Ag and B = g−1B. Then (A ,B ,C) is another subset trio, and it follows from equation 1 that either one of (A ∩ A,B ∪ B,C) or (A ∪ A,B ∩ B,C) has greater deﬁciency than (A,B,C) or they both have the same deﬁciency as (A,B,C). The ﬁrst usage of this precise transformation we know of appears in a paper of Kemperman [28] but it is closely related to other transformations used earlier by Sherck, and Davenport and others. The traditional method of application is to set up an inductive framework in which one of these two new subset trios has improved with regard to the inductive parameter, and then to obtain the result by applying induction to this trio. Of course, if one of these two new subset trios is trivial, then it has rather little structure, so in general, when using these transformations one restricts attention to only those which produce nontrivial subset trios.

For our purposes, we will need to maintain a stronger condition than nontriviality.

- A cursory glance at the structures found in Kemperman’s Theorem reveals the following essential property: For both pure and impure beats, one of the three sets is contained in a coset of a proper subgroup, but the other two have relatively little individual structure; in contrast to this, for both pure and impure chords, all three sets in the subset trio have strong structure individually. Roughly speaking, our plan will be to begin with a critical trio (A,B,C) for which none of the three sets is contained in a coset of a proper subgroup (the other case is dealt with separately), and then try to apply an uncrossing argument to obtain two new trios with the same property. Assuming we have improved a suitable inductive parameter, we will be able to apply the theorem inductively to one of these new subset trios, say (A∗,B∗,C). Since (A∗,B∗,C) will not be a pure or impure beat (and cannot be contained in one), we may apply our result to gain useful structural information about the set C. With this in hand, we will then return to try to understand the structure of (A,B,C).


There are a number of complications in following this plan. First oﬀ, we will need to use critical trios of the form (A∗,B∗,C) not constructed in the aforementioned manner of Kemperman. For this purpose, we will develop a technique called puriﬁcation based on Hamidoune’s Theorem 1.8 which will allow for more subtle modiﬁcations. Another complication is that we are only proving a structure theorem for maximal subset trios. So, after our uncrossing operation we will need to pass from the new trio we have found to a maximal one. As a consequence of this, the structural description of C we obtain will be somewhat rough. To remedy this situation, we will need to prove a number of stability results which show that whenever a maximal critical subset trio (A,B,C) has one set which is suitably close to one found in our structures, then (A,B,C) is one of our familiar types. These stability lemmas will constitute the lion share of the technical work.

#### 2 Dihedral Groups and the Classiﬁcation

The main goal of this section is to state our structure theorem for critical subset trios. However, before doing so, we will need to introduce some additional types of critical behaviour.

##### 2.1 Pure Dihedral Chords

In this subsection we will introduce a simple type of critical trio which occurs in dihedral groups. This critical behaviour has been observed previously. For instance, it appears (implicitly) in a paper of Eliahou and Kervaire [11] which investigates small product sets in dihedral groups.

For every positive integer n we let Dn denote a dihedral group of order 2n, and we let

- D∞ denote a countably inﬁnite dihedral group. Let us now ﬁx a dihedral group Dn (here we permit n = ∞) with n ≥ 3. Then Dn has a unique cyclic subgroup of index two, which we call the rotation subgroup. We call the elements of this subgroup rotations and all other elements ﬂips. Let r be a rotation, let f be a ﬂip and let k be a nonnegative integer. We deﬁne any set of the following form to be a basic dihedral progression with ratio r.


A = {1,r,r2,...,rk}{1,f}. (2)

We deﬁne a dihedral progression with ratio r to be any set of the form sA where s ∈ Dn, but we will keep our focus on basic progressions. We say that the basic dihedral progression A is nontrivial if k ≥ 1 and proper if rk+1  ∈ A. Assuming A is proper, it follows immediately that |A| = 2(k + 1). Since the conjugate of a rotation by a ﬂip yields the inverse rotation we may also express A as follows.

A = {1,fr−k}{1,r,r2,...,rk}.

If A is proper, there does not exist a nontrivial rotation in stabL(A) ∪ stabR(A) (such an element would have to stabilize {1,r,...,rk} which is not possible). It then follows that stabL(A) = {1,fr−k} and stabR(A) = {1,f}. Next suppose that is a positive integer and let B be a basic dihedral progression with ratio r given as follows.

B = {1,f}{1,r,r2,...,r } = {1,r,...,r }{1,fr }. (3) This gives us

AB = {1,r,...,rk}{1,f}{1,r,...,r }

= {1,fr−k}{1,r,...,rk}{1,r,...,r }

= {1,fr−k}{1,r,...,rk+ } = {1,r,...,rk+ }{1,fr }.

So, AB will be another basic dihedral progression with ratio r. If AB is proper, then |AB| = 2(k + + 1) = |A| + |B| − 2 so (A,B) is a nontrivial critical pair. Note that in this case stabL(A) = stabL(AB) = {1,fr−k} and stabR(AB) = stabR(B) = {1,fr }. We now deﬁne a type of subset trio which captures this behaviour.

Deﬁnition: Let H G be ﬁnite with G/H dihedral and |G/H| ≥ 10. A subset trio is a pure dihedral chord relative to H if there is a similar subset trio (A,B,C) and S ∈ G/H generating the rotation subgroup so that

- 1. A,B,C are H-stable.
- 2. ϕG/H(A) and ϕG/H(B) are nontrivial basic dihedral progressions with ratio S and stabR(A) = stabL(B).
- 3. C = (AB)−1 satisﬁes |C| > 2|H|.


Observe that every pure dihedral chord is a maximal nontrivial critical trio, and setting H1 = stabL(A) = stabR(C) and H2 = stabR(A) = stabL(B) and H3 = stabR(B) = stabL(C) we have that δ(A,B,C) = |H1| = |H2| = |H3|.

##### 2.2 Dihedral Prechords

As was the case with cyclic chords, there is also an impure version of dihedral chords. Analogously, the group G will have a normal subgroup H so that the three sets A and

- B and C are close to H-stable sets with quotient a dihedral progression, but with some impurity at the ends. However, before deﬁning these we will ﬁrst need to introduce a type of triple of subsets (in a dihedral group) which is not a subset trio, but has only a small number of diﬀerent combinations which multiply to give the identity. This is the purpose of this subsection. For a basic dihedral progression A as given by equation 2 we deﬁne the ends of A to be (1,f,rk,fr−k).


- Deﬁnition: Let G be a dihedral group of order at least 8 with rotation subgroup generated by r, let A,B be basic nontrivial dihedral progressions with ratio r and assume that stabR(A) = stabL(B) and that X = AB = G. Then X is another basic dihedral progression


with ratio r, we let (x1,x2,x3,x4) denote its ends, and put C = X−1∪{x−1 1,x−2 1,x−3 1,x−4 1}. We deﬁne the triple (A,B,C) to be a dihedral prechord.

One key property of a dihedral prechord (A,B,C) which is an immediate consequence of our deﬁnition is the following

|A| + |B| − |C| = 6. (4)

Consider a dihedral prechord as in the above deﬁnition where A and B are given by equations 2 and 3. Label the ends of A and B and X as follows.

- A has ends (a1,a2,a3,a4) = (1,f,rk,fr−k),
- B has ends (b1,b2,b3,b4) = (1,fr ,r ,f), X has ends (x1,x2,x3,x4) = (1,fr ,rk+ ,fr−k).


Now let us consider the diﬀerent ways that the ends of the progression X can be produced as a product of an element in A and an element in B. For this purpose, deﬁne the

representation function RepA,B(g) = {(a,b) ∈ A × B | ab = g}. It follows immediately from the assumption stabR(A) = stabL(B) = {1,f} that every element x ∈ X will have |RepA,B(x)| ≥ 2. For the ends of X, this bound will be met with equality as indicated below.

RepA,B(x1) = RepA,B(1) = {(1,1),(f,f)} = {(a1,b1),(a2,b4)}, RepA,B(x2) = RepA,B(fr ) = {(1,fr ),(f,r )} = {(a1,b2),(a2,b3)}, RepA,B(x3) = RepA,B(rk+ ) = {(rk,r ),(fr−k,fr )} = {(a3,b3),(a4,b2)}, RepA,B(x4) = RepA,B(fr−k) = {(rk,f),(fr−k,1)} = {(a3,b4),(a4,b1)}.

Next we deﬁne the following group elements (note the intentional ﬂip in indexing yielding

- c2 = x4−1 and c4 = x−2 1)3. (c1,c2,c3,c4) = (x−1 1,x−4 1,x−3 1,x−2 1) = (1,fr−k,r−k− ,fr ,).


c3

a4

b2

v

w

u

- a1
- a2


b1

c4 c2

w

u

c1

b3

a3

b4

v

Figure 3: A labelled octahedron

The key point is that the three sets A,B,C have the property that there are exactly 8 elements (a,b,c) in A × B × C for which abc = 1 and these 8 products are precisely those labelling the edges around each face of the octahedron pictured in Figure 3. We call this ﬁgure a labelled octahedron associated with (A,B,C), and it will prove helpful since it conveniently encodes all trivial triple products from our sets. Next we shall explore the structure of this labelling a little further.

Assign the vertex labels from Figure 3 as follows u = v = w = 1,

- u = c2,
- v = a2,
- w = b2.


3The cause of this slightly strange ﬂip is that the object of interest is not X, but C = X−1 ∪ {x−1 1, x−2 1, x−3 1, x−4 1}. If C is ﬁnite, then it is a basic dihedral progression with ends (c1, c2, c3, c4).

Now consider an edge e in our octahedron which goes from a vertex with label x to one with label y. A check of our assignments reveals that the label on the edge e is given by x−1y. In fact, this is a special case of a more general phenomena. For an arbitrary directed graph Γ, a map ψ : E(Γ) → G is called a tension if for every closed walk in the underlying graph with edge sequence e1,...,en we have ni=1(ψ(ei))ηi = 1 where ηi = 1 if ei is traversed in the forward direction and ηi = −1 if ei is traversed backward. A basic property of every tension ψ is that there exists a map τ : V (Γ) → G called a potential function so that every edge e = (x,y) satisﬁes ψ(e) = τ(x)−1τ(y). In our case, the product of the edge labels on each of the closed walks bounding a face of our octahedron is trivial, and it then follows by an easy inductive argument that these labels form a tension. The vertex labelling given above is a potential function associated with this tension.

##### 2.3 Impure Dihedral Chords

In this subsection we will use the notion of a dihedral prechord to introduce a type of critical behaviour which occurs in groups which have dihedral quotients.

- Deﬁnition: Let H G be ﬁnite, with G/H is dihedral and |G/H| ≥ 8. A subset trio is an impure dihedral chord (relative to H) if there exists a similar subset trio (A,B,C)


and A1,...,A4, B1,...,B4, C1,...,C4 ∈ G/H so that A+ = A ∪ (∪4i=1Ai) and B+ =

- B ∪ (∪4i=1Bi) and C+ = C ∪ (∪4i=1Ci) satisfy


- 1. A+ and B+ and C+ are H-stable.
- 2. (ϕG/H(A+),ϕG/H(B+),ϕG/H(C+)) is a dihedral prechord with labelled octahedron indicated on the left in Figure 4.
- 3. 0 < |A+ \ A| < 4|H| and 0 < |B+ \ B| < 4|H| and 0 < |C+ \ C| < 4|H|.


C3∗

C3

B2∗

- A∗4

A∗3

- B1∗


B2

A4

v

u

w

- A∗1
- A∗2


- A1
- A2


B1

C4∗ C2∗

C4 C2

w

u

B3∗ C1∗

B3 C1

A3

B4∗

B4

v

| |
|---|


Figure 4: labelled octahedra

Let us pause to make a technical comment concerning the bound |G/H| ≥ 8 in the above deﬁnition. Although it would be possible to extend the notion of an impure dihedral chord to the case when G/H is a dihedral group of order 6, it follows from the analysis in Section 9 that a maximal critical subset trio of this form would also be either a pure or impure beat.

Our next task will be to investigate the possible behaviour of the sets A∩(∪4i=1Ai) and

- B ∩ (∪4i=1Bi) and C ∩ (∪4i=1Ci) (which is intentionally obscured in the above deﬁnition). To do so, we shall follow the same procedure as before to choose u,u ,v,v ,w,w ∈ G so that in Figure 4 the label on the edge (x,y) is given by x−1Hy. Now, for 1 ≤ i ≤ 4 we


deﬁne a new set A∗i for as follows: If the initial vertex of the Ai edge is labelled with x and the terminal vertex labelled with y then we set A∗i = x(Ai ∩ A)y−1. We deﬁne the sets Bi∗ and Ci∗ for 1 ≤ i ≤ 4 similarly.

It follows from our deﬁnitions that A∗1 ...A∗4,B1∗,...,B4∗,C1∗ ...C4∗ ⊆ H. Furthermore, in the octahedron on the right in Figure 4 we have the property that the product of the three sets (in order) labelling the edges of any oriented triangle does not contain the identity. To see this last claim, suppose (for a contradiction) that 1 ∈ A∗3B3∗C3∗ and observe that

1 ∈ u(A ∩ A3)v−1v(B ∩ B3)w−1w(C ∩ C3)u−1 = u(A ∩ A3)(B ∩ B3)(C ∩ C3)u−1 which contradicts the assumption that (A,B,C) is a subset trio. It follows from equation

- 4 that the deﬁciency of (A,B,C) is given by the following formula


4

δ(A,B,C) =

i=1

|A∗i| + |Bi∗| + |Ci∗| − 6|H|.

This prompts a new deﬁnition.

Deﬁnition: For a ﬁnite group H, an octahedral conﬁguration (in H) consists of an oriented octahedron in which each edge is labelled with a subset of H as in Figure 4, with the property that the product of the labels (in order) on any three edges forming a directed triangle does not contain 1.

An octahedral conﬁguration maximal if it is not possible to replace any of the sets with a proper superset while maintaining an octahedral conﬁguration. We deﬁne the deﬁciency of an octahedral conﬁguration in H as given on the right in Figure 4 to be

4 i=1 |A∗i| + |Bi∗| + |Ci∗| − 6|H| and we say that such a conﬁguration is critical if it has

positive deﬁciency.

We say that an octahedral conﬁguration derived as above from an impure dihedral chord (A,B,C) is associated with (A,B,C). Our deﬁnitions of maximal and deﬁciency imply that the deﬁciency of an associated octahedral conﬁguration is equal to the deﬁciency

of (A,B,C), and this associated octahedral conﬁguration is maximal whenever (A,B,C) is maximal.

To complete our classiﬁcation we shall determine all maximal critical octahedral conﬁgurations in a ﬁnite group H. In our next subsection we turn our attention to this problem.

##### 2.4 Critical Octahedral Conﬁgurations

In a maximal critical octahedral conﬁguration in the group H, many of the sets involved will be either ∅ or the entire group H. Next we will introduce some notation to help work with this situation. In the following ﬁgures, we have depicted octahedra with three types of edges: a dotted line indicates that the label on the associated edge is empty, a solid dark line indicates it is the full group H, and a grey line indicates that its label is a proper nonempty subset of H.

Deﬁnition: We say that an octahedral conﬁguration has type −1, 0, 1, or 2 if its associated graph appears in Figure 5 with the corresponding label.4.

type −1 type 0

type 1 type 2

| |
|---|


Figure 5: Octahedral conﬁgurations

In Section 13 we will prove the following theorem which classiﬁes maximal critical octahedral conﬁgurations.

- Theorem 2.1 Every maximal critical octahedral conﬁguration has type −1, 0, 1, or 2.


If (A,B,C) is an impure dihedral chord with an associated octahedral conﬁguration of type n, then we say that (A,B,C) has type n. We shall prove that an impure dihedral chord

4To help explain this numbering, let us comment that conﬁgurations of type −1 will be inessential, and conﬁgurations of type 0, 1, and 2 have the corresponding number of triangles of grey edges.

of type −1 cannot be a maximal subset trio, so this type of impure dihedral chord will not appear in our structure theorem. An impure dihedral chord of type 0 is a fully described maximal critical trio which will appear as a possible outcome in our structure theorem. Next consider an impure dihedral chord (A,B,C) of type 1, and assume that it has an associated octahedral conﬁguration in H for which the labels on the unique directed triangle of grey edges are A , B , C (in this order). Then (A ,B ,C ) is a nontrivial subset trio in H which we call a continuation of (A,B,C). As with our other structures, δ(A,B,C) = δ(A ,B ,C ) and (A ,B ,C ) is maximal whenever (A,B,C) is maximal. Maximal critical impure dihedral chords of type 2 have some additional structure, and we shall now introduce some deﬁnitions to handle this.

Deﬁnition: Consider an octahedral conﬁguration in H of type 2 in which the labels on the two directed triangles of grey edges are A ,B ,C and A ,B ,C , and let x ∈ A and K ,K < H.

- (2A) We say this conﬁguration has type 2A if A ⊆ xK ⊆ xK and (A ,B ,C ) is an impure beat relative to K and (xK ,B ,C ) is a pure beat relative to K . In this case we deﬁne a continuation of this conﬁguration to be a continuation of (A ,B ,C ).
- (2B) We say this conﬁguration has type 2B if A = xK ∩xK and both (xK ,B ,C ) and (xK ,B ,C ) are pure beats (relative to K , K ).


Extending our notation in the obvious manner, we will say that a dihedral chord has type

- 2A or 2B if it has an associated octahedral conﬁguration of this type. A dihedral conﬁguration of type 2B is a fully described maximal critical trio, so these will appear as a possible outcome in our structure theorem. For a dihedral chord (A,B,C) of type 2A, we deﬁne a continuation of (A,B,C) to be a continuation of its associated octahedral conﬁguration. As in the other cases, if (A ,B ,C ) is such a continuation, then δ(A ,B ,C ) = δ(A,B,C) and (A ,B ,C ) will be maximal whenever (A,B,C) is maximal. In Section 13 we shall prove the following result.


- Theorem 2.2 Every type 2 maximal critical octahedral conﬁguration has type 2A or 2B.


In summary, every maximal critical subset trio which is an impure dihedral chord will have type 0, 1, 2A, or 2B. Those of types 0 or 2B are fully described maximal critical trios, while those of types 1 and 2A have continuations which are maximal critical subset trios in a proper (ﬁnite) subgroup.

##### 2.5 The Classiﬁcation Theorem

There is another simple and ﬂexible construction of a critical pair (or subset trio) which is well known, and appears for instance as the exceptional case in Serra and Zemor’s paper [46] discussed earlier. Namely, choose a ﬁnite subgroup H ≤ G and x ∈ G \ H and set A = H∪xH and B = H∪Hx. In this case |A| = |B| = 2|H| but AB = H∪xH∪Hx∪xHx will have size less than 4|H| (since xH ∩ Hx = ∅), so (A,B) will be critical. Of course, in the special case when G is abelian, this is nothing new since in this case A = B is a geometric progression in the quotient group G/H. However, for general groups this does yield new critical pairs.

There are additional constructions of critical pairs (A,B), where A is a union of a small number of left H-cosets and B is a union of a small number of right H-cosets. More precisely, there are two inﬁnite families for which AH = A and HB = B and

|A| |H|, ||HB|| = {2,3}, and there are a small number of exceptional examples which are based on the Platonic solids and the regular maps on the projective plane. We shall postpone discussion of these since they are easier to understand within the framework developed in the following section. We now state our main classiﬁcation theorem for critical subset trios.

For every positive integer n we let Sn and An denote the symmetric and alternating groups of permutations of {1,2,...,n}.

- Theorem 2.3 If Φ is a nontrival maximal critical subset trio in G, then there exists a se-


quence of subgroups G = G1 > G2 ...Gm and a sequence of subset trios Φ = Φ1,Φ2,...,Φm so that the following hold:

- 1. Φi is a subset trio in the group Gi for 1 ≤ i ≤ m.
- 2. Φi is either an impure beat, an impure cyclic chord, or an impure dihedral chord of type 1 or 2A with continuation Φi+1 for 1 ≤ i < m.
- 3. Φm is either a pure beat, a pure cyclic chord, a pure dihedral chord, an impure dihedral chord of type 0 or 2B, or there exists a subset trio (A,B,C) similar to Φm and a (possibly trivial) subgroup H Gm together with subgroups H H1,H2,H3 ≤ Gm so that H1 = stabL(A) = stabR(C), H2 = stabR(A) = stabL(B), H3 = stabR(B) = stabL(C) and one of the following holds:


- (a) |A| = 2|H2| = |B| and δ(A,B,C) = |H1| = |H3| < |H2|.
- (b) 9|H1| = |A| = 3|H2| and 2|H2| = |B| = 3|H3| and δ(A,B,C) = |H1|. Further, if Gm is ﬁnite, then [H1 : H] divides 16.
- (c) 4|H1| = |A| = 2|H2| and 3|H2| = |B| = 2|H3| and δ(A,B,C) = |H1|. Further, if Gm is ﬁnite, then [H1 : H] divides 16.


- (d) Gm/H and A,B,C and H1,H2,H3 satisfy one of the following.


|Gm/H<br><br>||Gm| |H1|<br><br>||Gm| |H2|<br><br>||Gm| |H3|<br><br>||Gm| |A|<br><br>||Gm| |B|<br><br>||Gm| |C|<br><br>|
|---|---|---|---|---|---|---|
|C2 × S4, C2 × A4, or S4 C2 × A5 or A5 C2 × A5 or A5 C2 × A5 or A5 S5 A5 S6, or A6, or S5<br><br>|8 12 20 20 12 6 20|12 20 30 12 15 15 15<br><br>|6 30 12 30 10 10 6<br><br>|4 4 10<br><br>4 3 3<br>5<br>|3 10 6 6 5 5 3<br><br>|2<br>3/2<br>4/3<br>5/3 2 2 2<br>|


This paper gives an almost entirely self-contained proof of this theorem. Indeed, the only signiﬁcant result we rely on which is not proved here is a theorem of Tutte concerning arc-transitive cubic graphs which we use to get the bounds on [H1 : H] in (b) and (c) of the third part of the outcome. This theorem as stated is not a proper characterization since we have not supplied a converse. However, in Section 13 we will remedy this by establishing a variant of the above result for which we do have a converse.

#### 3 Incidence Trios

As indicated earlier, our approach to classifying critical subset trios in the group G will involve an incidence geometry on which G has a natural action. This step brings us from groups to group actions, and has the advantage that it permits us to ﬁrst classify the extremal structures, and then to determine which groups act on them. The purpose of this section is to introduce the incidence geometries we will work with, and to motivate this approach with a natural example. This example will also give us opportunity to introduce some of the exceptional critical phenomena.

##### 3.1 Incidence Geometry

In this subsection we will introduce the basic terminology we will use for working with incidence geometries.

Deﬁnition: An incidence geometry Λ = (X1,...,Xn;∼) consists of a ﬁnite sequence of pairwise disjoint sets (X1,...,Xn) together with a symmetric binary relation ∼ on ∪ni=1Xi, called the incidence relation, which satisﬁes the following rule: For every 1 ≤ i ≤ n, if x,y ∈ Xi then x  ∼ y. We deﬁne ∪ni=1Xi to be the ground set of Λ and deﬁne the rank of Λ to be n. If x,y ∈ Xi for some 1 ≤ i ≤ n we say that x and y have the same type, and otherwise they have diﬀerent type.

For every point x ∈ Xi, the neighbours of x are NΛ(x) = {y ∈ ∪ni=1Xi | y ∼ x} and for a subset of points A we let NΛ(A) = ∪x∈ANΛ(x). When the incidence geometry is clear from context, we will drop these subscripts.

For brevity, we will frequently write Λ = (X1,...,Xn) to specify an incidence geometry, and treat the incidence relation ∼ as implied. Also for convenience, when X1,...,Xn are disjoint sets and ∼ is a relation deﬁned on a superset of ∪ni=1Xi satisfying x  ∼ y whenever x,y ∈ Xi, we will let (X1,...,Xn;∼) denote the incidence geometry given by (X1,...,Xn;∼ ) where ∼ is the restriction of ∼ to ∪ni=1Xi.

Next we introduce a few ways to construct a new incidence geometry from an existing one. If σ ∈ Sn then Λ = (Xσ(1),...,Xσ(n);∼) is also an incidence geometry, and we say that Λ and Λ are equivalent and write Λ ≡ Λ . If i1,i2,...,i ∈ {1,2,...,n} are distinct, and for every 1 ≤ j ≤ we have a set X i

,...,X j ;∼) is an incidence geometry which we say is contained in Λ, and we write Λ ⊆ Λ. In this case we will also call Λ a subgeometry of Λ. Finally, if 1 ≤ i,j ≤ n and i = j, then (Xi,Xj;∼) is a subgeometry of Λ which we call a side of Λ.

###### ⊆ Xij, then Λ = (X j

1

j

For incidence geometries deﬁned on the same sequence of sets, there is a natural partial order which will be of interest to us. If Λ∗ = (X1,...,Xn,∼∗) is another incidence geometry we write Λ ≤ Λ∗ if for every x,y ∈ ∪ni=1Xi we have x ∼ y only if x ∼∗ y. If Λ ≤ Λ∗ and Λ = Λ∗ we write Λ < Λ∗.

Isomorphisms will play an important role for us, so let us introduce this concept here. If Π = (Y1,...,Yn; ) is another incidence geometry, an isomorphism from Λ to Π is a map φ : ∪ni=1Xi → ∪ni=1Yi so that φ maps Xi bijectively to Yi for every 1 ≤ i ≤ n, and so that for all x,x ∈ ∪ni=1Xi we have x ∼ x if and only if φ(x) φ(x ). If such a map exists we say that Λ and Π are isomorphic and write Λ ∼= Π. An isomorphism from Λ to itself is called an automorphism and we let Aut(Λ) denote the group of automorphisms (under composition).

Next we introduce a concept which plays an important role in our proof. We say that an incidence geometry ∆ of rank 2 is disconnected if there exists a partition of the ground set of ∆ into {U,W} so that no element in U is incident with an element in W. We say that ∆ is connected if it is not disconnected, and we deﬁne a connected component of ∆ to be a maximal connected subgeometry. For an incidence geometry Λ of rank greater than 2, we deﬁne Λ to be connected5 if every side of Λ is connected.

Finally, let us close this subsection by introducing a particularly important family of rank 2 incidence geometries. We deﬁne a graph to be a rank 2 incidence geometry (V,E) with the property that |N(e)| = 2 for every e ∈ E. This is the standard deﬁnition of a graph where multiple edges are permitted, but loops are forbidden. We say that a graph is simple

5Although this will prove to be the meaningful type of connectivity for us, it should be noted that this is not the standard use of the term in incidence geometry.

if it has no parallel edges (i.e. there do not exist distinct e,e ∈ E with N(e) = N(e )), and for convenience, we will say that an incidence geometry is graphic if it is a graph.

##### 3.2 Choruses

Our main focus will be on incidence geometries which are equipped with a natural group action. Throughout this paper our groups will always act on the left. So, if G acts on the set X and x ∈ X and g ∈ G we let gx denote the image of x under the permutation associated with g. For a subset S ⊆ X we let gS = {gs | s ∈ S} and deﬁne GS = {g ∈ G | gS = S} and G(S) = {g ∈ G | gs = s for every s ∈ S}. We will shortcut this notation for singletons and write Gx = G{x}. The action is transitive if for every x,y ∈ X there exists g ∈ G for which gx = y and it is regular if there is a unique such g. A block of imprimitivity (sometimes abbreviated block) is a set S ⊆ X so that for every g ∈ G either gS = S or gS ∩ S = ∅. If S is a block, and the action of G is transitive, then {gS | g ∈ G} is a partition of X which we call a system of imprimitivity generated by S.

Deﬁnition: For a group G, a G-chorus consists of an incidence geometry Λ = (X1,...,Xn) equipped with an action of G on Λ (i.e. a homomorphism G → Aut(Λ)) so that G acts transitively on Xi for every 1 ≤ i ≤ n.

Next we deﬁne a natural family of choruses.

Deﬁnition: Let G be a group and let M be an n × n matrix of subsets of G with the property that Mij = Mji−1 and Mii = ∅ for every 1 ≤ i,j ≤ n. We deﬁne the Cayley Chorus, denoted CayleyC(G;M), to be the incidence geometry (G × {1},G × {2},...,G × {n}) where (x,i) and (y,j) are incident if and only if y ∈ xMij.

Cayley choruses of rank 2 and 3 will be of frequent interest for us, so we add some shortcuts to the above notation. For sets A,B,C ⊆ G we let

 

 

∅ A C−1 A−1 ∅ B

M = ∅ A A−1 ∅

M =

C B−1 ∅

and deﬁne

CayleyC(G;A) = CayleyC(G;M), CayleyC(G;A,B,C) = CayleyC(G;M ).

Note that in the above deﬁnition of a Cayley chorus, we have deﬁned incidence in terms of right multiplication. It follows from this that the group G has a natural left action

on the structure (sending each (x,i) to (gx,i)) which shows that Cayley choruses are indeed choruses. The following observation follows immediately from our deﬁnitions, and determines when a Cayley chorus is connected.

- Observation 3.1 If A ⊆ G then CayleyC(G;A) is connected if and only if A is not contained in a coset of a proper subgroup.

The central goal of the remainder of this subsection is to make the connection between general choruses and Cayley choruses explicit, but to do so will require a couple of concepts. Let Λ = (X1,...,Xn) be an incidence geometry and let P be a partition of Xj. We deﬁne Λ = (X1,...,Xj−1,P,Xj+1,...,Xn) to be the incidence geometry with incidence relation given by the rule that x ∈ Xi and y ∈ Xk are incident in Λ if they are incident in Λ, and

- x ∈ Xi and P ∈ P are incident in Λ if there exists y ∈ P so that x and y are incident in Λ. We call any geometry formed from Λ by a sequence of these operations a quotient of

Λ. Note that if Λ is a G-chorus and P is a system of imprimitivity on Xj, then Λ is also a G-chorus.

Next we introduce an important relation. We deﬁne two points x,y in the ground set of an incidence geometry Λ to be clones if they are of the same type and N(x) = N(y). We say that Λ is clone free if it does not contain distinct points which are clones. It follows immediately that the clone relation is an equivalence relation. For every 1 ≤ i ≤ n let Pi be the partition of Xi given by the clone relation. We say that Pi is the clone partition of

- Xi and we deﬁne Λ• = (P1,...,Pn). Again we note that if Λ is a G-chorus, then Λ• is also a G-chorus. More generally, if Qj is a system of imprimitivity on Xj for some 1 ≤ j ≤ n so that any two points in the same block of Qj are clones, we call Qj a system of clones. If Qi is a system of clones for every 1 ≤ i ≤ n then we say that (Q1,...,Qn) is obtained from Λ by identifying clones.


Next we state an observation which follows immediately from our deﬁnitions. If H is a subgroup of the group G then we let G/H denote the set of all left H-cosets in G.

- Observation 3.2 Let A ⊆ G and assume that H1 = stabL(A) and H2 = stabR(A). Then in the chorus CayleyC(G;A), the clone partition of G × {i} is G/Hi × {i}.


If Λ = (X1,...,Xn) and Π = (Y1,...,Yn) are two G-choruses, we say that a function φ : ∪ni=1Xi → ∪ni=1Yi is a strong isomorphism if it is an isomorphism, and furthermore, for every g ∈ G and x ∈ ∪ni=1Xi we have that φ(gx) = gφ(x). If such a map exists, we say that Λ and Π are strongly isomorphic.

The next theorem shows that every chorus is strongly isomorphic to one obtained from a Cayley chorus by identifying clones. We give a particularly detailed statement of this result since this will be required in the ﬁnal section. This relationship given by this result

mirrors the connection between Cayley graphs and general vertex transitive graphs, so we have attributed it to Sabidussi who proved the corresponding statement in that setting.

- Theorem 3.3 (Sabidussi [42]) Let Λ = (X1,...,Xn) be a G-chorus and let xi ∈ Xi for every 1 ≤ i ≤ n. For every 1 ≤ i ≤ n associate each x ∈ Xi with Sx = {g ∈ G | gxi = x}, and for every 1 ≤ i,j ≤ n deﬁne Aij = ∪y∈Xj∩N(xi)Sy. Then we have:


- 1. Sx is a left Gxi coset for every x ∈ Xi.
- 2. if x,y ∈ Xi and g ∈ G, then gx = y if and only if gSx = Sy.
- 3. GxiAijGxj = Aij for every 1 ≤ i,j ≤ n.
- 4. if y ∈ Xi and z ∈ Xj, then y ∼ z if and only if (Sy)−1Sz ⊆ Aij.
- 5. if M is the n × n matrix with ij entry Aij, then CayleyC(G;M) has the property that G/Gxi × {i} is a system of clones for 1 ≤ i ≤ n, and associating each x ∈ Xi with Sx × {i} is a strong isomorphism from Λ to (G/Gx1 × {1},...,G/Gxn × {n}).


Proof: Associating every x ∈ Xi with Sx yields the standard representation of the action of G on Xi by left Gxi cosets with “base point” xi. The ﬁrst two parts of the result are basic features of this representation, and follow immediately from the deﬁnitions. For the third part, observe that we must have AijGxj = Aij since Aij is a union of left Gxj cosets. To see that GxiAij = Aij, note that N(xi)∩Xj is setwise stabilized by Gxi. For the fourth part, choose g ∈ G so that gxi = y and observe that y ∼ z if and only if xi = g−1y ∼ g−1z which, by part 2, holds if and only if g−1Sz ⊆ Aij. However, in light of 3, this last condition is equivalent to (Sy)−1Sz = (gGxi)−1Sz ⊆ Aij. For the last part, observe that from our construction we have Aii = ∅ and from 4 we have Aij = A−ji1 for every 1 ≤ i,j ≤ n. So, we may deﬁne the Cayley chorus CayleyC(G;M). It follows from 3 that G/Gxi × {i} is a system of clones for every 1 ≤ i ≤ n, and it follows from parts 2 and 4 that associating each x ∈ Xi to Sx × {i} gives a strong isomorphism.

We close this subsection by introducing some important incidence geometries. Though we have worked only with multiplicative groups so far, for indexing purposes and for deﬁning Cayley incidence geometries, it will be helpful for us to occasionally use the additive groups Z/nZ and Z. For J = Z or J = Z/nZ we call an incidence geometry by the name below if it is isomorphic to an incidence geometry in the corresponding description.

|Name|Description|
|---|---|
|polygon sequence|CayleyC(J;{0,1}) with |J| ≥ 2<br><br>CayleyC(J;{0,1,...,  − 1}) with |J| ≥ 4 and 2 ≤ ≤ |J| − 2<br><br>|


We deﬁne a triangle to be a polygon (X,Y ) with |X| = |Y | = 3. Note that every polygon (X,Y ) with |X| = |Y | ≥ 4 is also a sequence.

##### 3.3 Trios

In this subsection we will restrict our attention to ﬁnite groups and ﬁnite incidence geometries since these are somewhat simpler to work with, and this is suﬃcient to motivate our approach. The purpose of this subsection will be to introduce the type of chorus which will be our principle object of study (for the ﬁnite case). In Subsection 3.5 we will extend this to the general case.

We say that an incidence geometry Λ is collision free if there do not exist distinct points x,y,z in the ground set of Λ with x ∼ y and y ∼ z and z ∼ x. If (X1,X2) is an incidence geometry with X1 and X2 ﬁnite, we deﬁne the density of (X1,X2) to be

q(X1,X2) = |{(x,y) ∈ X1 × X2 | x ∼ y}| |X1| · |X2|

.

Note that if there exists an integer d so that every point in X1 has exactly d neighbours in X2, then q(Λ) = |Xd

2|. Next we have a key observation concerning the Cayley chorus depicted in Figure 6.

G × {2}

·A ·B

G × {3}

G × {1}

·C

Figure 6: A Cayley chorus based on a subset trio

- Observation 3.4 Let (A,B,C) be a critical subset trio in the ﬁnite group G. Then Θ = CayleyC(G;A,B,C) satisﬁes the following properties:


- • Θ is a G-chorus,
- • Θ is collision free,
- • 1≤i<j≤3 q(G × {i},G × {j}) = ||GA|| + ||BG|| + ||CG|| > 1. This prompts the following deﬁnition, which we make here only for ﬁnite groups.


Deﬁnition: If G is a ﬁnite group, a G-(incidence) trio (X,Y,Z) is a collision free G-chorus of rank 3. We say that (X,Y,Z) is critical if q(X,Y ) + q(Y,Z) + q(Z,X) > 1.

A key property to note here is that our notion of critical depends only on the underlying structure of the geometry and not on the particular group acting on it. This feature permits us to ﬁrst classify critical incidence trios and then to determine which groups act on them.

We have already deﬁned a number of important properties of subset trios, and now we shall introduce analogous properties for (incidence) trios. We say that a trio Θ = (X,Y,Z) is trivial if it has a side which does not contain a pair of incident points, and we say that Θ is maximal if there does not exist a G-trio Θ with Θ < Θ . Note that if Θ is a maximal

- G-trio and x,y are points of distinct type in the ground set with x  ∼ y then there must exist a point z with x ∼ z and y ∼ z (otherwise we could increase the incidence relation by adding all incidences between pairs of points of the form (gx,gy) for g ∈ G to obtain a new trio contradicting the maximality of Θ). If (A,B,C) is a subset trio in G, we call Θ = CayleyC(G;A,B,C) a Cayley (incidence) trio. Note that in this case we have the following equivalences:


 

 

 

 

critical maximal trivial

critical maximal trivial

.

if and only if (A,B,C) is

Θ is









Next let us consider the notion of similarity for subset trios. Let (A,B,C) be a subset trio in G and deﬁne Θ = CayleyC(G;A,B,C). Now let x,y,z ∈ G and apply Theorem 3.3 to Θ for the points (x,1), (y,2), and (z,3) to produce a new trio Θ . A quick check reveals that Θ = CayleyC(G;A ,B ,C ) where A = xAy−1, B = yBz−1, and C = zCx−1. So, we see that our notion of similarity for subset trios corresponds to switching “base points” and equivalence of incidence trios.

##### 3.4 An Example

In this subsection, we oﬀer an example of a natural (incidence) trio as motivation for the introduction of incidence geometry. This will also permit us to introduce some of the exceptional structures which appear in our classiﬁcation.

Tetrahedron Cube Octahedron Dodecahedron Icosahedron

| |
|---|


Figure 7: The Platonic Solids

Consider a map Ξ on a surface with vertex set V , edge set E, and face set F and assume that Ξ is vertex, edge, and face transitive and that V,E,F are all ﬁnite.

Now, deﬁne an incidence geometry Λ on (V,E,F) by the rule that an edge e ∈ E is incident with an element in V ∪ F in Λ if they are incident in Ξ, and v ∈ V and f ∈ F are incident in Λ if they are not incident in Ξ. It follows that Λ is a G-chorus where G is the automorphism group of Ξ. Further, it is collision free by construction, so Λ is a G-trio. To determine if this trio is critical, we need to determine the densities of the sides. First note that the density of (V,E) is |V2| and the density of (E,F) is |F2|. For the side (V,F), observe that the number of vertex-face incidences in Ξ is exactly 2|E| since for every v ∈ V and f ∈ F which are incident, there are exactly two edges which are incident with both v and f, and each edge contributes to four such incident pairs. It follows from this that the sum of the densities of (F,E), (V,F), and (V,E) is given by

|F| + 1 − |V2||·|EF| | + |V2| = 1 + |V |·|2F| (|V | − |E| + |F|). So, we see that this construction gives a critical trio if and only if the Euler characteristic is positive, which holds only when the surface is either a sphere or projective plane. Applying this construction to any of the dual pairs Cube/Octahedron, Dodecahedron/Icosahedron, Petersen/K6 results in an exceptional critical trio (for smaller maps the resulting trio is degenerate and falls into another class).

2

K6 & Petersen

Figure 8: Two dual maps on the projective plane

To see how these structures will appear in the context of subset trios, let us now assume that (A,B,C) is a critical subset trio in G and assume that the (incidence) trio Θ = CayleyC(G;A,B,C) has the property that Θ• is isomorphic to the exceptional structure just described for the cube. Now our group G must have a homomorphism to the automorphism group of the cube, so we have

G → Aut(Θ•) ∼= C2 × S4. The kernel of this map is a normal subgroup H G and the image of G is a subgroup of Aut(Θ•) which acts transitively on the vertices, edges, and faces of the cube. The only proper subgroups which have this property are isomorphic to C2 × A4 and S4, so G must have a normal subgroup H with G/H isomorphic to one of C2 × S4, C2 × A4, or S4. Furthermore, A,B,C must all be H-stable, and with some further analysis, we can determine the precise structure of these sets.

##### 3.5 Weights and General Trios

So far we have only deﬁned (incidence) trios in the special case when the group is ﬁnite. In this subsection we will extend this notion to allow for inﬁnite groups. To do this, we will introduce weights, and insist that the geometries of interest to us all have either ﬁnite or coﬁnite weight. In fact, these weights are nothing more than the sizes of sets involved were we to model our incidence geometry as a Cayley chorus using Theorem 3.3.

Let G act transitively on the set X. Then |Gx| = |Gy| for every x,y ∈ X, and we call this number (or ∞) the point weight of X and denote it by wG◦ (X). Note that this group action is regular if and only if wG◦ (X) = 1. For A ⊆ X we deﬁne the weight of A to be wG(A) = wG◦ (X)|A| and the coweight of A to be wG(A) = wG◦ (X)|X \A|. When the group is clear from context, we shall drop these subscripts.

Let (X,Y ) be a G-chorus. Then |N(x)| is independent of the choice of x ∈ X and we call this number (or ∞) the degree of (X,Y ) and denote it by d(X,Y ). Note that for a graphic duet, this aligns with the standard deﬁnition of degree. Similarly, |Y \ N(x)| is independent of the choice of x and we denote this quantity by d(X,Y ). We deﬁne wG(X,Y ) = wG(N(x)) = d(X,Y )wG◦ (Y ) and wG(X,Y ) = wG(N(x)) = d(X,Y )wG◦ (Y ), and call these quantities the weight and coweight of (X,Y ). As usual, when the group is clear from context, we drop the subscript.

Deﬁnition: A G-duet is a G-chorus ∆ = (X,Y ) for which w◦(X) and w◦(Y ) are ﬁnite and either w(X,Y ) or w(X,Y ) is ﬁnite.

Next we establish an easy but essential property of duets.

- Proposition 3.5 For every G-duet (X,Y ) we have


wG(X,Y ) = wG(Y,X), wG(X,Y ) = wG(Y,X).

Proof: Apply Theorem 3.3 to choose a Cayley chorus CayleyC(G;A) with incidence relation ∼ and subgroups H1,H2 ≤ G so that G/H1 × {1} and G/H2 × {2} are systems of clones, and (X,Y ) is strongly isomorphic to (G/H1 × {1},G/H2 × {2};∼). Now we have

- w(X,Y ) = |A| = |A−1| = w(Y,X) and w(X,Y ) = A = A−1 = w(Y,X).


Next we generalize our earlier notion of ﬁnite (incidence) trios, to allow for inﬁnite groups. This will be our principle object of study.

Deﬁnition: A G-trio is a collision-free G-chorus for which each side is a duet.

Extending our deﬁnitions from the ﬁnite case, we will say that a G-trio is trivial if it has a side which is empty and maximal if there does not exist a G-trio Θ with Θ < Θ . Next we establish the notion of deﬁciency for (incidence) trios.

Deﬁnition: Let Θ = (X,Y,Z) be a G-chorus and assume (without loss) w(X,Y ) ≤

- w(Y,Z) ≤ w(X,Z). We deﬁne the deﬁciency of Θ to be δG(Θ) = w(X,Y ) + w(Y,Z) − w(X,Z), and we say that Θ is critical if δG(Θ) > 0. As usual, we drop the subscript when the group is clear from context.


Note that for A,B,C ⊆ G we have that (A,B,C) is a subset trio if and only if Θ = CayleyC(G;A,B,C) is an (incidence) trio, and δ(A,B,C) = δ(Θ). As was the case with ﬁnite trios, the next observation shows that our notion of critical for a general trio depends only on the structure of the underlying incidence geometry and not on the particular group acting on it.

- Observation 3.6 If (X,Y,Z) is a G-trio with d(X,Z) < ∞ and d(X,Y ) > 0, then (X,Y,Z) is critical if and only if


d(Z,X) d(Y,X) −

d(Z,Y ) d(X,Y )

1 >

.

Proof: This follows from the equation

d(Z,Y ) d(X,Y ) −

d(Z,X) d(Y,X)

1 +

1 w(X,Y )

(w(X,Y ) + w(Z,Y ) − w(Z,X)).

=

#### 4 The Structure of Critical Trios

The main goal of this section is to state our structure theorem for critical (incidence) trios. Although we have already stated our theorem for subset trios, the setting of incidence geometry provides us with a diﬀerent, and sometimes more beneﬁcial, perspective on these structures.

##### 4.1 Videos

Consider a maximal subset trio (A,B,C) for which H = stabR(A) = stabL(B) satisﬁes |AH| = 2|H| and deﬁne Θ = CayleyC(G;A,B,C). It follows from our assumptions that whenever x,y ∈ G lie in the same left H-coset, the points (x,2) and (y,2) will be clones. It then follows that in the trio Θ•, the side corresponding to (G × {1},G × {2}) will be

a graph. So, to get a handle on subset trios of this form, we will investigate (incidence) trios which have a graphic side. Conveniently, the next lemma shows that a natural graph parameter determines when such a trio is critical. For a set of vertices A in a graph Γ, we let ∂(A) denote the set of all edges with exactly one end in A, and we call any set of this form an edge cut. We deﬁne c(A) = |∂(A)|.

- Observation 4.1 Let Θ = (V,E,Z) be a nontrivial maximal trio for which (V,E) is a graph of degree d. If z ∈ Z and A = N(z) ∩ V , then Θ is critical if and only if c(A) < 2d.


Proof: Set S = N(z) ∩ E. First suppose that w(Z,V ) is ﬁnite, and observe that by maximality, S is precisely the set of edges with both endpoints in V \ A. Now summing the degrees of the vertices in V \ A counts every edge in S twice and every edge in ∂(A) once. This gives us d|V \ A| = 2|S| + c(A). So Θ is critical if and only if

1 > dd((E,VZ,V )) − dd((Z,EV,E)) = |V2\A| − |Sd| = c(2Ad) which is precisely the desired condition.

Next consider the case when w(Z,E) is ﬁnite and set R = E \ (S ∪ ∂(A)). It follows from maximality that R is precisely the set of edges with both ends in A. Summing the degrees of the vertices in A counts every edge in R twice and every edge in ∂(A) once, so d|A| = 2|R| + c(A). Now, Θ will be critical if and only if

1 > dd((Z,EV,E)) − dd((E,VZ,V )) = |R|+dc(A) − |A2| = c(2Ad)

which is again the desired condition. Since one of w(Z,V ) or w(Z,E) must be ﬁnite, this completes the proof.

So, to understand critical trios which have a graphic side, we will need to classify edgecuts of size at most 2d in vertex and edge-transitive graphs of degree d. This will be a major focus of Section 7. For now we will introduce some notation to help us describe the trios which result from this construction.

Let Γ be a graph, let m be a positive integer, and deﬁne Cm(Γ) (Pm(Γ)) to be the set of all cycles (paths) of Γ with exactly m vertices. Note that if Γ is a G-duet, then G has a natural action on both Cm(Γ) and Pm(Γ). If Γ is a subgraph of Γ, v ∈ V (Γ), and e ∈ E(Γ) then we deﬁne v ∼ Γ if v ∈ V (Γ ) and e ∼ Γ if e ∈ E(Γ ). Now, for any graph Γ and positive integer m, we have operators V , E, Pm, and Cm which take Γ and return a set. Using these operators together with the various relations ∼ deﬁned here permits the construction of numerous incidence geometries based on Γ. If A,B,C are three such operators and we have deﬁne a relation ∼ between A and B and between B and C then we let Γ : A ∼ B ∼ C denote the incidence geometry (A(Γ),B(Γ),C(Γ)) with incidence

relation given by the rule that y ∈ B(Γ) is incident with another point w of diﬀerent type if w ∼ y, and two points x ∈ A(Γ) and z ∈ C(Γ) are incident if and only if there does not exist y ∈ B(Γ) with x ∼ y ∼ z. It follows from this that Γ : A ∼ B ∼ C is always collision free. We shall permit A and C to be the same operator and in this case for the incidence geometry we just use two diﬀerent copies of the set A(Γ) = C(Γ). With this, we can introduce three families of critical incidence trios.

Deﬁnition: A trio Θ ≡ (X,Y,Z) is a standard video if there exists a graphic duet Γ of degree d so that (X,Y,Z)• is isomorphic to one of the following.

- 1. Γ : E ∼ V ∼ E where d ≥ 3, and |V (Γ)| ≥ 5
- 2. Γ : P3 ∼ V ∼ E where d = 3, and |V (Γ)| ≥ 6
- 3. Γ : P3 ∼ E ∼ V where d = 3, and |V (Γ)| ≥ 6.


As indicated earlier, the six graphs Cube, Octahedron, Dodecahedron, Icosahedron, Petersen, and K6 will play a special role in our theorem. These graphs give rise to exceptional critical trios because they possess exceptional small edge cuts. The ﬁrst four of these graphs embed in the sphere and the last two embed naturally in the projective plane (as can be seen in Figures 7 and 8). For any one of these graphs G, we deﬁne F(G), to be the faces of G in this embedding and we use ∼ to denote the incidence relation between vertices and faces and between edges and faces. We treat the operator F as V,E,Pm,Cm above. With this, we can introduce the exceptional videos.

Deﬁnition: A trio Θ ≡ (X,Y,Z) is an exceptional video if (X,Y,Z)• is isomorphic to one of the following.

- 1. Cube/Octahedron : V ∼ E ∼ F
- 2. Dodecahedron : F ∼ V ∼ E
- 3. Dodecahedron/Icosahedron : V ∼ E ∼ F
- 4. Icosahedron : F ∼ V ∼ E
- 5. Petersen : C5 ∼ E ∼ V
- 6. Petersen/K6 : F ∼ E ∼ V
- 7. K6 : C3 ∼ E ∼ V .


Deﬁnition: A trio is a video if it is either a standard video or an exceptional video.

##### 4.2 Beats and Chords

In this subsection we will introduce the remaining types of critical (incidence) trios. We have already encountered these structures in the context of subset trios, and our names for

- them will be similar to those we used in that setting.


We say that an incidence geometry (X,Y ) is a matching if |X| ≥ 2 and there is a bijection f : X → Y so that for every x ∈ X and y ∈ Y we have x ∼ y if and only if f(x) = y.

Deﬁnition: We deﬁne a trio Θ ≡ (X,Y,Z) to be a pure beat relative to (X,Y ) if (X,Y )• is a matching, and Θ is maximal and nontrivial.

Consider a pure beat as in the above deﬁnition for which ∆ = (X,Y ) and Θ ≡ (X,Y,Z), and let x ∈ X and y ∈ Y satisfy x ∼ y. It then follows from the structure of ∆ and the maximality of Θ that every point z ∈ Z will satisfy either z ∼ x or z ∼ y. It follows from this that Θ is critical and δ(Θ) = w(X,Y ).

Deﬁnition: A trio Θ ≡ (X,Y,Z) is a pure chord if there exist  ,m ≥ 1 and a group J = Z or J = Z/nZ with |J| ≥ + m + 3 so that (X,Y,Z)• is isomorphic to

Cayley(J;{0,..., },{0,...,m},J \ {− − m,...,0}).

It is straightforward to verify that pure chords are maximal and critical. Furthermore, by the bounds on the parameters, pure chords will also be connected.

We say that an incidence geometry Λ is empty if no two points in Λ are incident, and we say that Λ is full if x ∼ y whenever x and y are points of diﬀerent type. Finally, we call Λ partial if it is neither empty nor full.

If ∆ = (X,Y ) is a G-duet which is nonempty and disconnected, then there exist systems

- of imprimitivity P = {Pi | i ∈ I} of X and Q = {Qi | i ∈ I} of Y so that {(Pi,Qi) | i ∈ I} is the set of connected components of ∆, and we call (P,Q) the component quotient of (X,Y ). Note that (P,Q) is a matching which is a G-chorus, but (P,Q) will be a G-duet if and only if w◦(P) = w◦(Q) < ∞.


Deﬁnition: We deﬁne a trio Θ ≡ (X,Y,Z) to be an impure beat relative to (X,Y ) if (X,Y ) is disconnected with component quotient (P,Q), and for every z ∈ Z we have

- 1. there is exactly one Pz ∈ P with (z,Pz) partial, exactly one Qz ∈ Q with (z,Qz) partial, and these blocks satisfy Pz ∼ Qz.


| |
|---|
| |
| |
| |
| |
| |
| |
| |


Figure 9: An impure beat

- 2. for every P ∈ P \ {Pz} and Q ∈ Q \ {Qz} with P ∼ Q, one of (z,P), (z,Q) is full and the other is empty.


Let P ∈ P and Q ∈ Q satisfy P ∼ Q and deﬁne R = {z ∈ Z | ({z},P) is partial}. It follows immediately that R is a block of imprimitivity, and we say that the P,Q, and the system of imprimitivity generated by R are associated with this impure beat. We call (P,Q,R) a continuation of Θ, and note that any two such continuations are isomorphic. Setting H = GP = GQ = GR we have that (P,Q,R) is an H-trio and δH(P,Q,R) = δG(Θ).

Figure 10: A cyclic chord

Deﬁnition: We say that Θ ≡ (X,Y,Z) is an (impure) cyclic chord if there exist  ,m ≥ 1, a group J = Z or J = Z/nZ with |J| ≥ + m + 2 and systems of imprimitivity P = {Pj :

j ∈ J}, Q = {Qj : j ∈ J}, R = {Rj : j ∈ J} of X,Y,Z so that the following hold

 

partial if j = i full if i + 1 ≤ j ≤ i + empty otherwise

(Pi,Qj) is



 

partial if j = i full if i + 1 ≤ j ≤ i + m empty otherwise

(Qi,Rj) is



 

partial if j = i empty if i + 1 ≤ j ≤ i + + m full otherwise

(Pi,Rj) is



In this case we will say that Θ is a cyclic chord relative to P,Q,R. It follows immediately that the subgroup H = G(P) = G(Q) = G(R) has G/H cyclic, and furthermore H is the stabilizer of each block in P ∪Q∪R. Let P ∈ P, Q ∈ Q, and R ∈ R satisfy (P,Q), (Q,R), and (R,P) partial. Then (P,Q,R) is an H-trio, and we call (P,Q,R) a continuation of Θ. It follows easily that any two continuations are isomorphic, and as usual, we have δH(P,Q,R) = δG(Θ).

We need one added bit of notation before introducing our next structure. If a group G acts on a set X, we say the action is dihedral if G is dihedral, and the rotation subgroup of G acts regularly on X. So, the standard action of the dihedral group Dn on the vertices of a regular n-gon is dihedral.

Figure 11: A dihedral chord

Deﬁnition: We deﬁne a connected trio Θ ≡ (X,Y,Z) to be an (impure) dihedral chord if there exist  ,m ≥ 1, a group J = Z or J = Z/nZ with |J| ≥ + m + 2, and systems of

imprimitivity P = {Pj : j ∈ J}, Q = {Qj : j ∈ J}, R = {Rj : j ∈ J} of X,Y,Z so that

 

partial if j = i or j = i + full if i + 1 ≤ j ≤ i + − 1 empty otherwise

(Pi,Qj) is



 

partial if j = i or j = i + m full if i + 1 ≤ j ≤ i + m − 1 empty otherwise

(Qi,Rj) is



 

partial if j = i or j = i + + m empty if i + 1 ≤ j ≤ i + + m − 1 full otherwise

(Pi,Rj) is



and in addition, for the normal subgroup H = G(P) = G(Q) = G(R), the action of G/H on each of P, Q, R is dihedral. We will also say that Θ is a dihedral chord relative to P,Q,R.

In the next two subsections we will develop the notion of a continuation of a dihedral chord. However, we are now able to state a signiﬁcant corollary of our structure theorem, so we end the present subsection with this.

- Corollary 4.2 Every nontrivial maximal critical trio is one of the following: a pure beat, a pure chord, a video, an impure beat, a cyclic chord, or a dihedral chord.


##### 4.3 Square and Octahedral Choruses

In this subsection we will develop a framework to investigate the structure of (impure) dihedral chords. We begin by deﬁning a type of duet which appears as a side of a dihedral chord of ﬁnite weight.

Figure 12: A fringed sequence

Deﬁnition: For a positive integer , we say that a duet (X,Y ) is a fringed sequence of length +1 if there exists a group J = Z or J = Z/nZ with n ≥ min{4, +2}, and systems

- of imprimitivity P = {Pj | j ∈ J} of X and Q = {Qj | j ∈ J} of Y so that


 

partial if j = i or j = i + full if i + 1 ≤ j ≤ i + − 1 empty otherwise

(Pi,Qj) is



and in addition H = G(P) = G(Q) has the property that the action of G/H on each of P and Q is dihedral. In this case we will also say that (X,Y ) is a fringed sequence relative to (P,Q).

Let us pause to note a couple of consequences of the dihedral action of G/H on P and Q (these will be discussed in detail in Section 9). First, it follows from this that whenever P,P ∈ P and Q,Q ∈ Q satisfy (P,Q) and (P ,Q ) partial, there exists g ∈ G for which gP = P and gQ = Q . It also follows from this dihedral action that the stabilizers of P and Q satisfy [GP : H] = 2 and [GQ : H] = 2. So, P (Q) will consist of either one or two orbits under the action of H. Next we will introduce a type of chorus equipped with some additional structure to work with this situation.

Deﬁnition: For a ﬁnite group H, an H-square chorus is an H-chorus Λ = (X1,...,Xn) equipped with a partition {Λ1,Λ2} of {X1,...,Xn} so that |Λi| = 1,2 for i = 1,2 and so that (X,Y ) is empty whenever X,Y ∈ Λi are distinct.

Continuing with P,Q from above, let P ∈ P and Q ∈ Q satisfy (P,Q) partial and deﬁne Λ1 = {X1,...,Xm} to be the set of H-orbits in P (so m = 1 or m = 2) and Λ2 = {Xm+1,...Xn} to be the set of H-orbits in Q. Now Λ = (X1,...,Xn) is an H-chorus and together with {Λ1,Λ2} it forms an H-square chorus. We will say that Λ is associated with (X,Y ).

We will need to relate the weight of (X,Y ) to the weights of the sides of Λ. To do so, put mi = 3 − |Λi| for i = 1,2 and deﬁne the adjusted weight of Λ to be

wˆH(Λ) =

m1m2wH(S,T)

S∈Λ1,T∈Λ2

- Proposition 4.3 Let (X,Y ) be a fringed sequence of length +1 and let Λ be an associated


- H-square chorus. Then w(X,Y ) = 2( − 1)|H| + wˆH(Λ).


Proof: Let P and Q and P,Q and Λ1,Λ2 be as in the above discussion and let Q ∈ Q\{Q} satisfy (P,Q ) partial. Choose x ∈ P and if |Λ1| = 2 choose x ∈ P so that x and x are in distinct H-orbits. Now w◦(P) = 2|H| = w◦(Q) so we have

w(X,Y ) = w(N(x)) = 2( − 1)|H| + w(N(x) ∩ (Q ∪ Q )).

The following properties (all of which follow immediately) permit us to express w(N(x) ∩ (Q ∪ Q )) in terms of weights of sides of Λ.

- • If |Λ1| = 1 then wG(N(x) ∩ (Q ∪ Q )) = 2wG(N(x) ∩ Q).


- • If |Λ1| = 2 then wG(N(x) ∩ (Q ∪ Q )) = wG(N(x) ∩ Q) + wG(N(x ) ∩ Q).
- • If Λ2 = {Q} then for every D ⊆ Q we have wG(D) = 2wH(D).
- • If Λ2 = {Q1,Q2} then for i = 1,2 and every D ⊆ Qi we have wG(D) = wH(D).


For instance, if Λ1 = {P1,P2} and Λ2 = {Q} then wG(N(x) ∩ (Q ∪ Q )) = wG(N(x) ∩ Q) + wG(N(x ) ∩ Q)

= 2wH(N(x) ∩ Q) + 2wH(N(x ) ∩ Q)

= 2wH(P1,Q) + 2wH(P2,Q)

= wˆH(Λ).

A similar analysis in the remaining cases reveals that wG(N(x) ∩ (Q ∪ Q )) = wˆ(Λ) holds in general, and this completes the proof.

All of our analysis extends naturally from fringed sequences to dihedral chords, but for this, we need to step up from square choruses to the following.

Deﬁnition: For a ﬁnite group H, an H-octahedral chorus is a collision free H-chorus Λ = (X1,...,Xn) equipped with a partition {Λ1,Λ2,Λ3} of {X1,...,Xn} so that |Λi| = 1,2 for i = 1,2,3 and so (X,Y ) is empty whenever X,Y ∈ Λi are distinct. We set mi = 3−|Λi| for i = 1,2,3 and deﬁne the adjusted weight of Λ to be

wˆH(Λ) =

mimjwH(S,T).

1≤i<j≤3 S∈Λi,T∈Λj

If Λ = (X1,...,Xn) together with the partition {Λ1,Λ2,Λ3} is an octahedral chorus,

- then we may obtain a square chorus from Λ by choosing 1 ≤ i ≤ 3 and removing all


members of Λi from the sequence of sets, and using the partition {Λ1,Λ2,Λ3}\Λi. We say that such a square chorus is contained in Λ.

Now let us return to the dihedral chord Θ deﬁned in the previous subsection, and choose

- P ∈ P and Q ∈ Q and R ∈ R so that (P,Q) and (Q,R) and (P,R) are partial. Then deﬁne Λ1,Λ2,Λ3 to be the respective partitions of P,Q,R into H-orbits. These orbits together with the partition {Λ1,Λ2,Λ3} form an octahedral chorus, Λ which we say is associated with Θ. Let Λ12, Λ23, and Λ13 be the three square choruses contained in Λ. Using our earlier analysis for fringed sequences (and noting w◦(P) = w◦(Q) = w◦(R) = 2|H|) we have


δ(Θ) = wG(X,Y ) + wG(Y,Z) − wG(X,Z)

= ( − 1)2|H| + wˆH(Λ12) + (m − 1)2|H| + wˆH(Λ23) − ( + m + 1)2|H| + wˆH(Λ13)

= wˆH(Λ) − 6|H|.

Accordingly, we now deﬁne the deﬁciency of an octahedral chorus Λ to be δ(Λ) = wˆH(Λ)− 6|H| and call Λ critical if it has positive deﬁciency. The following observation records the obvious purpose for this deﬁnition.

- Observation 4.4 If Θ is a dihedral chord and Λ is an associated octahedral chorus δ(Θ) = δ(Λ).


##### 4.4 Critical Octahedral Choruses

It follows from the developments of the previous subsection that every maximal critical trio which is a dihedral chord has an associated octahedral chorus which will be maximal and critical. The goal of this subsection is to introduce terminology to describe all such octahedral choruses.

As we did with octahedral conﬁgurations in Section 2, we shall associate each octahedral chorus Λ = (X1,...,Xn) with a graph Γ with three types of edges. The vertex set of Γ is {X1,...,Xn}, and if Xi,Xj are in distinct members of the distinguished partition, there is an edge between them in Γ. This edge will be dotted if (Xi,Xj) is empty, grey if (Xi,Xj) is partial, and solid black if (Xi,Xj) is full.

type −1

type 2

Figure 13: Octahedral choruses of low rank

Deﬁnition: We deﬁne an octahedral chorus to be of type −1, 0, 1, or 2 if its associated graph appears in either Figure 5 or in Figure 13 with the corresponding label.

In Section 8 we will prove the following theorem, which classiﬁes maximal critical octahedral choruses.

- Theorem 4.5 (Classiﬁcation of critical octahedral choruses) Every maximal critical octahedral chorus has type −1, 0, 1, or 2.


We will say that a dihedral chord has type n if it has an associated octahedral chorus of type n. We will prove that dihedral chords of type −1 cannot be maximal trios, so they will not appear in our structure theorem. We will prove that a dihedral chord of type 0 is also a pure chord (with a special type of group action), and hence these structures will appear elsewhere in our structure theorem. Next consider a G-trio Θ which is a dihedral chord

- of type 1, let Λ be an associated H-octahedral chorus, and assume that (X,Y ), (Y,Z), and (X,Z) are distinct sides of Λ which are partial. Then (X,Y,Z) is an H-trio for which


δH(X,Y,Z) = δH(Λ) = δG(Θ) and we call (X,Y,Z) a continuation of Θ. Maximal critical trios which are type 2 have additional structure, and we now introduce some deﬁnitions

- to capture this. For a symmetric relation ∼ on X and Y ⊆ X we let ∼ |Y denote the restriction of ∼ to Y .


Deﬁnition: Let Λ be an H-octahedral chorus of type 2 with incidence relation ∼ and ﬁrst assume that (X,Y ), (Y,Z1), (X,Z1), (X,Z2), (Y,Z2) are distinct sides of Λ which are partial (so the associated graph is one from Figure 5). For i = 1,2 let Υi = (X,Y,Zi;∼i) be an H-trio, and assume that ∼ |X∪Zi = ∼i |X∪Zi and ∼ |Y ∪Zi = ∼i |Y ∪Zi for i = 1,2.

- (2A) We say that Λ has type 2A if ∼ |X∪Y = ∼1 |X∪Y ⊆ ∼2 |X∪Y and Υ1 is an impure beat relative to (X,Y ) and Υ2 is a pure beat relative to (X,Y ). In this case we deﬁne a continuation of Λ to be a continuation of Υ1.
- (2B) We say that Λ has type 2B if ∼ |X∪Y = ∼1 |X∪Y ∩ ∼2 |X∪Y and both Υ1 and Υ2 are pure beats relative to (X,Y ).

Next assume that Λ is an H-octahedral chorus with incidence relation ∼ and assume that (X,Y ), (Y,Z), (X,Z) are sides of Λ which are partial and that {Z} is a member of the distinguished partition (so the associated graph is one from Figure 13).

- (2C) We say that Λ has type 2C if (X,Y,Z) is a pure beat relative to (X,Y ).


As before, we will say that a dihedral chord has type 2A, 2B, or 2C if it has an associated octahedral chorus of this type. Note that a dihedral chord of type 2B or 2C is a fully described critical trio. For a dihedral chord Θ of type 2A, we deﬁne a continuation of Θ to be a continuation of its associated octahedral chorus. If Θ is such a continuation, then δ(Θ ) = δ(Θ) and Θ will be maximal whenever Θ is maximal. Our next result gives us a classiﬁcation of the type 2 choruses of interest.

- Theorem 4.6 (Classiﬁcation of type 2 octahedral choruses) Every maximal critical octahedral chorus of type 2 has type 2A, 2B, or 2C.

In summary, every maximal critical trio which is a dihedral chord has type 0, 1, 2A, 2B, or 2C. Those of type 0 appear elsewhere in our classiﬁcation theorem. Dihedral chords of type 2B, or 2C are fully described critical trios. Finally, dihedral chords of types 1 and 2A have continuations which are maximal critical trios in a proper (ﬁnite) subgroup.

4.5 The Classiﬁcation Theorem

In this subsection, we will state our structure theorem for critical trios. We begin by naming the trios of interest.

Deﬁnition: A trio Θ is a song6 if there exists a sequence of trios Θ = Θ1,...,Θm so that the following hold.

- 1. For 1 ≤ i < m the trio Θi is an impure beat, a cyclic chord, or a dihedral chord of type 1 or 2A, and has continuation Θi+1.
- 2. Θm is a video, a pure beat, a pure chord, or a dihedral chord of type 2B or 2C. We are now ready to state our main theorem.


- Theorem 4.7 A nontrivial trio is maximal and critical if and only if it is a song.


We will give an elementary proof of this theorem which is entirely contained in this article. In the next section we will develop some basic bounds and tools for working with critical trios, and in Section 6 we will give a proof of the “only if” direction of this theorem under the assumption of a number of lemmas. These lemmas will then be proved in Sections 7-11. The “if” direction of the proof is given in Section 12.

#### 5 Basic Properties of Duets and Trios

In this section we will develop some basic tools for working with critical trios, and establish some simple bounds on deﬁciency. Most if not all of these results are straightforward generalizations of existing theorems concerning product sets.

6To help explain our choice of terminology, observe that a song is recursively composed of beats and chords, possibly ending with a video

##### 5.1 Uncrossing

The goal of this subsection is to develop a basic uncrossing procedure which can be used to move from one trio to another one. We will use this to prove a variant of a theorem of Hamidoune which will play a key role in the proof of our main theorem.

Deﬁnition: Let (X,Y ) be a duet, let A ⊆ X and B ⊆ Y , and assume that each of A,B is either ﬁnite or coﬁnite. We say that (A,B) is a cross (of (X,Y )) if x  ∼ y for every x ∈ A and y ∈ B.

Next we introduce two deﬁnitions which identify a key correspondence between G-trios and crosses in G-duets.

Deﬁnition: Let (X,Y,Z) be a trio and let z ∈ Z. Then (N(z) ∩ X,N(z) ∩ Y ) is a cross of (X,Y ) which we call the cross associated with z.

Deﬁnition: Let (X,Y ) be a G-duet and let (A,B) be a cross of (X,Y ). Deﬁne Z = {(gA,gB) | g ∈ G} and extend the incidence relation ∼ from X ∪ Y to X ∪ Y ∪ Z by the rule that (A ,B ) ∈ Z is incident with A ∪ B . It follows that (X,Y,Z) is a G-trio and we call it the trio associated with the cross (A,B).

Consider a G-trio (X,Y,Z), choose z ∈ Z and let (A,B) be the cross associated with z. Then starting from the G-duet (X,Y ) let (X,Y,Z ) be the trio associated with the cross (A,B). It follows that (X,Y,Z ) is strongly isomorphic to the trio obtained from (X,Y,Z) by identifying clones in Z (i.e. the trio (X,Y,R) where R is the clone partition of Z).

So (up to clones), we see that trios correspond to duets with distinguished crosses. Next we will introduce some natural terminology for crosses which correspond with already established deﬁnitions for trios. Let (A,B) be a cross of the G-duet (X,Y ) and let (X,Y,Z) be the trio associated with (A,B). We say that (A,B) is trivial if A = ∅ or B = ∅. We deﬁne δ(A,B) = δ(X,Y,Z) and we say that (A,B) is critical if δ(A,B) > 0. Naturally, we will say that (A,B) is maximal if the only cross (A∗,B∗) with A∗ ⊇ A and B∗ ⊇ B is given by A∗ = A and B∗ = B.

The natural motivation for these deﬁnitions are the following equivalences which hold whenever Θ = (X,Y,Z) is the trio associated with the cross (A,B) of the duet (X,Y ), and also whenever (A,B) is the cross of (X,Y ) associated with a point z ∈ Z of the trio Θ = (X,Y,Z).

- • (X,Y,Z) is nontrivial if and only if (X,Y ) is nonempty and (A,B) is nontrivial;


- • (X,Y,Z) is critical if and only if (A,B) is critical;
- • w(A) = w(Z,X), w(A) = w(Z,X), w(B) = w(Z,Y ), and w(B) = w(Z,Y );

- • If B is coﬁnite, δ(A,B) = w(A) + w(X,Y ) − w(B);

- • If d(X,Y ) is ﬁnite, δ(A,B) = w(A) + w(B) − w(X,Y );

- • (A,B) is maximal if and only if every trio Θ = (X,Y,Z;∼ ) for which Θ ≤ Θ satisﬁes ∼ |X∪Z =∼ |X∪Z and ∼ |Y ∪Z =∼ |Y ∪Z.


With this, we are ready for the following observation which is our basic uncrossing argument. The ﬁrst part of this observation follows immediately from the deﬁnition of cross, while the second follows from the above deﬁnitions (here we need to split into cases depending on which of w(X,Y ) and w(A) and w(B) is ﬁnite).

- Observation 5.1 (Uncrossing) If (A,B) and (A ,B ) are crosses of a duet, then


- 1. (A ∩ A ,B ∪ B ) and (A ∪ A ,B ∩ B ) are crosses.
- 2. δ(A,B) + δ(A ,B ) = δ(A ∩ A ,B ∪ B ) + δ(A ∪ A ,B ∩ B ).


Since connectivity will play an important role in our arguments, we will be interested in when the trio (X,Y,Z) which is associated with the cross (A,B) of (X,Y ) is connected. For this purpose, let us introduce a little further notation. If G acts transitively on the set

- X and A ⊆ X, the closure of A, denoted [A], is the minimal block of imprimitivity which contains A (since blocks of imprimitivity are closed under intersection, there is always a unique such minimal block).


- Observation 5.2 Let (A,B) be a cross of the duet (X,Y ) and let (X,Y,Z) be the associated trio. Then (X,Z) is connected if and only if [A] = X.


Proof: First suppose that (Z,X) is disconnected and let {(Zi,Xi)}i∈I be its connected components. Then each Xi is a block of imprimitivity, and one must contain A, so [A] = X. Next suppose that [A] = X and let P be the associated system of imprimitivity. Then every z ∈ Z has N(z) ⊆ P for some P ∈ P, so (Z,X) is disconnected.

Our next goal will be to deﬁne a notion of deﬁciency for a duet so that the deﬁciency of a duet is equal to the maximum deﬁciency of a nontrivial cross. However, we will require the following easy lemma to ensure that our upcoming deﬁnition makes sense.

- Lemma 5.3 For every nontrivial G-trio (X,Y,Z) we have


- 1. δ(X,Y,Z) ≤ w(X,Y ) ≤ w(Y,Z)

- 2. if G is ﬁnite, then δ(X,Y,Z) ≤ 12|G|.


Proof: For the second inequality in part 1, choose x ∈ X and z ∈ Z with x ∼ z and observe w(X,Y ) = w(N(x) ∩ Y ) ≤ w(Y \ N(z)) = w(Y,Z).

To prove the other inequality in part 1, we may assume that w(Y,Z) < ∞. By an argument similar to the above we ﬁnd that w(X,Z) ≤ w(Y,Z) and then we have

δ(X,Y,Z) = w(X,Y ) + w(X,Z) − w(Y,Z) ≤ w(X,Y ).

For part 2, assume G is ﬁnite and suppose (without loss) that w(X,Y ) ≤ w(Y,Z). Then part 1 implies w(X,Y ) ≤ w(Y,Z) so w(X,Y ) ≤ 12|G|. Using part 1 again we have δ(X,Y,Z) ≤ w(X,Y ) ≤ 12|G| as desired.

Let ∆ be a nonempty duet and let (A,B) be a nontrivial cross of ∆. Then by applying the previous lemma to the trio associated with the cross (A,B) we deduce that δ(A,B) ≤ min{w(∆),w(∆)}. So, in particular, there do not exist nontrivial crosses of ∆ with arbitrarily large deﬁciency. This permits the following deﬁnition.

Deﬁnition: For a partial duet (X,Y ), the deﬁciency of (X,Y ) is

δ(X,Y ) = max{δ(A,B) | (A,B) is a nontrivial cross of (X,Y ) }.

If (X,Y ) is a duet and A ⊆ X is ﬁnite or coﬁnite, then (A,Y \ N(A)) is a cross. Similarly, if B ⊆ Y is ﬁnite or coﬁnite, then (X \N(B),B) is a cross. It will be convenient for us to further extend our notion of deﬁciency to subsets of X and Y in accordance with this observation.

Deﬁnition: If (X,Y ) is a duet and A ⊆ X and B ⊆ Y are ﬁnite or coﬁnite, we deﬁne the deﬁciency of A and B as follows:

- δ(A) = δ(A,Y \ N(A)),
- δ(B) = δ(X \ N(B),B).


As usual, we say that a set is critical if it has positive deﬁciency. We say that a nonempty subset A ⊆ X (or B ⊆ Y ) is nontrivially critical if δ(A) > 0 (δ(B) > 0) and N(A) = Y (N(B) = X). Since it will be frequently used, let us highlight the following observation.

- Observation 5.4 If (X,Y ) is a duet with w(X,Y ) < ∞ and A ⊆ X is ﬁnite then


- 1. δ(A) = w(A) + w(X,Y ) − w(N(A))
- 2. if (X,Y ) is nonempty, w(N(A)) ≥ w(A).


Proof: Part 1 is a restatement of our deﬁnitions. For part 2 we let (X,Y,Z) be the trio associated with the cross (A,Y \N(A)). If A = ∅ or N(A) = Y the result holds immediately. Otherwise, Lemma 5.3 gives

w(N(A)) = w(Y,Z) ≥ w(Z,X) = w(A).

Our next result reveals an important property of duets. We have credited Hamidoune with this theorem since he proved the analogue for digraphs. To see this connection between duets and digraphs, note that if Γ = (V,E) is a digraph and G ≤ Aut(Γ) acts transitively on V with ﬁnite vertex stabilizers, then we may form a G-duet on (V,V ) where V is a copy of V , by the rule that x ∈ V and y ∈ V satisfy x ∼ y if (x,y) ∈ E.

Theorem 5.5 (Hamidoune) If ∆ = (X,Y ) is a partial G-duet, there exists a ﬁnite nontrivially critical block of imprimitivity T ⊆ X or T ⊆ Y so that δ(T) = δ(∆). Proof: Choose a nontrivial cross (A,B) subject to the constraints

α) δ(A,B) is maximum. β) min{w(A),w(B)} is minimum (subject to α).

Assume (without loss) that w(A) ≤ w(B), and note that this implies that A is ﬁnite. Now suppose (for a contradiction) that A is not a block of imprimitivity. Then we may choose g ∈ G so that ∅ = A ∩ gA = A. Set (A ,B ) = (A ∩ gA,B ∪ gB) and (A ,B ) = (A∪gA,B∩gB) and note that these are both crosses. If (A ,B ) is trivial then B∩gB = ∅, so B is ﬁnite, but then

δ(A ,B ) = w(A ) + w(B ) − w(∆) > 2w(B) − w(∆) ≥ w(A) + w(B) − w(∆)

= δ(A,B)

so (A ,B ) contradicts our choice of (A,B) for α. It follows that both (A ,B ) and (A ,B ) are nontrivial. However, then by Observation 5.1 (applied to (A,B) and (gA,gB)), either one of (A ,B ) or (A ,B ) has greater deﬁciency than (A,B) which again contradicts the choice of (A,B) for α, or δ(A ,B ) = δ(A,B) and then (A ,B ) contradicts the choice of (A,B) for β.

##### 5.2 Puriﬁcation

In this subsection we will use Theorem 5.5 from the previous subsection to develop a process called puriﬁcation which we will later use to simplify critical crosses. The results in this subsection have been proved only for duets of ﬁnite weight since this is all that we require, but they can easily be extended to duets of inﬁnite (but coﬁnite) weight.

Proposition 5.6 Let ∆ = (X,Y ) be a duet with w(∆) < ∞, let P be a system of imprimitivity on X with ﬁnite blocks, and let T ∈ P. Setting ∆ = (P,Y ) we have

- 1. w(N∆(T)) = w(T)d(Y,P).
- 2. If T = X and w(N(T)) = w(T), then ∆ is disconnected.
- 3. If T is critical, then w(N(T)) = w(T) ww(∆)(T) .


Proof: Part 1 follows from the equation w(N∆(T)) = w(N∆ (T)) = w(P,Y ) = w(T)d(Y,P).

For part 2, note that if w(N(T)) = w(T) then by part 1 we have d(Y,P) = 1. Since T = X we ﬁnd that ∆ is disconnected, but then ∆ is also disconnected. For part 3, choose x ∈ T and note that w(N(T)) ≥ w(N(x)) = w(∆). Since T is critical we also have w(T) + w(∆) > w(N(T)). However, Part 1 implies that w(N(T)) is a multiple of w(T), and this yields the desired result.

As already noted, the ﬁrst part of the above proposition implies that w(N(T)) will always be a multiple of w(T). Our next lemma uses this to establish a nice property of subsets of critical blocks of imprimitivity.

- Lemma 5.7 Let ∆ = (X,Y ) be a duet with w(∆) < ∞ and let T ⊆ X be a ﬁnite critical block of imprimitivity. If S ⊆ T, then δ(S) ≤ δ(T). Proof: Choose S ⊆ T subject to


α) δ(S) maximum. β) |S| minimum (subject to α).

As in the proof of Theorem 5.5, it follows from our choice that S must be a block of imprimitivity (otherwise we may choose g ∈ G with ∅ = S ∩ gS = S and either one of

gS∩S or gS∪S has greater deﬁciency than S, or both have the same deﬁciency, and either case contradicts our choice of S).

Therefore k = ww((TS)) is an integer. Now, choose a point x ∈ S and observe the following (the last inequality follows from the assumption T is critical).

w(N(T) \ N(S)) ≤ w(N(T) \ N(x)) = w(N(T)) − w(∆) < w(T) = kw(S)

It follows from the previous proposition that w(N(T)) − w(N(S)) is a multiple of w(S) so we conclude that this quantity is at most (k − 1)w(S). But then we have

δ(T) − δ(S) = w(T) − w(N(T)) − w(S) + w(N(S))

= (k − 1)w(S) − w(N(T)) − w(N(S)) ≥ 0. It follows that every S ⊆ T satisﬁes δ(S) ≤ δ(T) as desired.

Throughout much of this paper, we will be considering a group acting transitively on a set X with a distinguished system of imprimitivity P. For a set A ⊆ X and a block P ∈ P we say that

 

 

 

 

P ⊆ A P ∩ A = ∅ otherwise.

inner outer boundary

.

(with respect to A) if

P is









We say that a set A is pure with respect to P if there are no boundary blocks, and impure otherwise. Similarly, if (X,Y ) is a duet and P,Q are systems of imprimitivity of X,Y then we say that a cross (A,B) of (X,Y ) is pure with respect to (P,Q) if A is pure with respect

- to P and B is pure with respect to Q.


Deﬁnition: If (A,B) is a cross of (X,Y ) and P ⊆ X is a ﬁnite critical boundary block, we deﬁne the cross (A∪P,B\N(P)) to be the weak puriﬁcation of (A,B) at P. We deﬁne weak puriﬁcation similarly for blocks of Y .

A disadvantage of weak puriﬁcation is that purifying a maximal cross may result in a cross which is no longer maximal. Next we introduce a stronger process which does not have this defect.

Deﬁnition: If (A,B) is a cross of (X,Y ) and P ⊆ X is a ﬁnite critical boundary block, we set B = B \ N(P) and A = X \ N(B ) and deﬁne (A ,B ) to be the puriﬁcation of (A,B) at P. We deﬁne puriﬁcation similarly for blocks of Y .

We close this subsection with a theorem which encapsulates the essential properties of puriﬁcation.

- Theorem 5.8 (Puriﬁcation) Let (X,Y ) be a duet with w(X,Y ) < ∞, let (A,B) be a nontrivial critical cross, and let P ⊆ X be a ﬁnite critical boundary block. If (A ,B ) and (A ,B ) are the weak puriﬁcation and the puriﬁcation of (A,B) at P then

- 1. δ(A ,B ) ≥ δ(A ,B ) ≥ δ(A,B)
- 2. If (A,B) is maximal, then (A ,B ) is maximal.
- 3. w(B \ B ) = w(B \ B ) < w(P).


Proof: Part 1 follows from δ(A ,B ) ≥ δ(A ,B ) and the following equation (which calls on Lemma 5.7).

δ(A ,B ) − δ(A,B) = w(P \ A) − w(B ∩ N(P)) ≥ w(P \ A) − w(N(P)) − w(N(P ∩ A))

= δ(P) − δ(P ∩ A) ≥ 0.

Part 2 is an immediate consequence of our deﬁnitions, and part 3 follows from B = B and the inequality

0 ≤ δ(A ,B ) − δ(A,B) = w(A \ A) − w(B \ B ) < w(P) − w(B \ B ).

5.3 Connectivity

In this subsection we will prove a couple of results concerning connectivity. The ﬁrst is a variant of a theorem of Olson [38] which asserts that whenever A,B are ﬁnite subsets of the group G and B is a generating set containing 1, either AB = G or |AB| ≥ |A| +

- 1

- 2|B|. Equivalently, whenever B ⊂ G is a generating set containing 1, the duet ∆ = CayleyC(G;B) satisﬁes δ(∆) ≤ 12|B|.


- Theorem 5.9 (Olson) If ∆ = (X,Y ) is a connected partial G-duet, δ(∆) ≤ min 2 1w(∆), 13|G| .


Proof: First we establish an easy inequality for integers. Let d,t be nonnegative integers and choose integers a,k so that d = at + k where 1 ≤ k ≤ t. Then we have

d + t − t dt = (at + k) + t − t(a + 1) = k ≤ (at + k)/(a + 1) = d/ dt

If w(X,Y ) = ∞ then we have nothing to prove, so we may assume w(X,Y ) < ∞. Now, apply Theorem 5.5 to choose a block of imprimitivity T so that T is nontrivally critical

and δ(T) = δ(∆). We assume (without loss) that T ⊆ X. Then by Proposition 5.6 (and the above inequality) we have

δ(∆) = w(∆) + w(T) − w(N(T))

= w(∆) + w(T) − w(T) ww(∆)(T) ≤ w(∆) ww(∆)(T) .

If w(∆) ≤ w(T) then Proposition 5.6 implies w(N(T)) = w(T) and that ∆ is disconnected which is contradictory. Thus w(∆) > w(T) and this implies δ(∆) ≤ 12w(∆). Next observe that if G is ﬁnite then w(N(T)) and |G| are both multiples of w(T) and w(T) < w(N(T)) < |G|. Thus |G| ≥ 3w(T) and this gives δ(∆) ≤ w(T) ≤ 13|G|.

- Corollary 5.10 If (X,Y ) is a nonempty G-duet and A ⊆ X satisﬁes [A] = X and N(A) =


- Y , then δ(A) ≤ min 12w(A), 31|G| .


Proof: Let (X,Y,Z) be the trio associated with the cross (A,Y \ N(A)). Then, by Observation 5.2 we have that (X,Z) is connected. So, by the previous theorem gives

δ(A) = δ(X,Y,Z) ≤ δ(X,Z) ≤ min{12w(X,Z), 13|G|} = min{12w(A), 13|G|} as desired.

Next we prove a key lemma concerning critical crosses in disconnected duets.

- Lemma 5.11 Let (X,Y ) be a disconnected duet with component quotient (P, Q). If (A,B) is a maximal critical cross of (X,Y ) then either (A,B) is pure with respect to (P,Q), or there is exactly one P ∈ P (Q ∈ Q) which is a boundary block and further


δ(A,B) ≤ min{12w(X,Y ), 13w◦(P)}.

Proof: Assume that ∆ = (X,Y ) is a G-duet, and note that w(X,Y ) < ∞. Let P = {Pi | i ∈ I} and Q = {Qi | i ∈ I} and assume Pi ∼ Qi for every i ∈ I. We may assume that w(A) < ∞, and then for every i ∈ I set Ai = A ∩ Pi. This gives us

0 < δG(A)

= wG(∆) − wG(N(A)) + wG(A)

= wG(∆) −

wG(N(Ai)) − wG(Ai) . (5)

i∈I

If N(Ai) = Qi then wG(Ai) ≤ wG(Pi) = wG(Qi) = wG(N(Ai)). Next suppose that i ∈ I satisﬁes Ai = ∅ and N(Ai) = Qi. Then (Ai,Qi \ N(Ai)) is a nontrivial cross of the connected duet ∆i = (Pi,Qi). If we set H = GPi = GQi then wG◦ (X) = wH◦ (Pi) and wG◦ (Y ) = wH◦ (Qi) (since every point x ∈ Pi satisﬁes Gx = Hx and similarly every y ∈ Qi satisﬁes Gy = Hy). It follows that wG(∆) = wH(∆i). Since ∆i is connected, Theorem 5.9 gives us

- 1

- 2wG(∆) = 12wH(∆i) ≥ δH(∆i) ≥ wH(∆i) − wH(N(Ai)) + wH(Ai)


= wG(∆) − wG(N(Ai)) + wG(Ai)

so wG(N(Ai)) − wG(Ai) ≥ 12wG(∆). It follows from this, maximality, and equation 5 that there is at most one i ∈ I so that Pi is a boundary block with respect to A (and similarly for

Q). If there does exist such a boundary block Pi, then δ(A,B) ≤ 21w(∆), and by applying Theorem 5.9 to the H-duet ∆i = (Pi,Qi) we ﬁnd δ∆(A,B) = δ∆i(Ai) ≤ 13|H| = 13w◦(P) which completes the proof.

##### 5.4 Disconnected Trios and Closure

In this section we prove a lemma which reveals the structure of maximal critical disconnected trios, and a theorem concerning the closure of a critical set in a duet.

- Lemma 5.12 (Disconnected Trios) Let Θ = (X,Y,Z) be a maximal nontrivial critical trio in G with (X,Y ) disconnected. Then Θ is either a pure or impure beat relative to (X,Y ). In the latter case, if Θ = (X ,Y ,Z ) is an H-trio which is a continuation of Θ, one of the following holds:


- 1. H is ﬁnite and |H| < |G|.
- 2. H is inﬁnite, so there are sides ∆ of Θ and ∆ of Θ with wG(∆) = ∞ = wH(∆ ), and these sides satisfy w¯G(∆) = w¯H(∆ ). Furthermore, Θ has a side of ﬁnite weight which is connected, but all sides of Θ of ﬁnite weight are disconnected.


Proof: Let Θ = (X,Y,Z) be a nontrivial maximal critical G-trio with (X,Y ) disconnected, and let (P,Q) be the component quotient of (X,Y ). Choose z ∈ Z, let (A,B) be the cross of (X,Y ) associated with z and assume (without loss) that A is ﬁnite. If (A,B) is pure with respect to (P,Q), then A contains a block of P so we have w◦(P) = w◦(Q) < ∞. It then follows from the maximality of Θ that any two points in the same block of P (Q) are clones, so Θ is a pure beat relative to (X,Y ), and we are ﬁnished. Otherwise, it follows

from the previous lemma that there is exactly one P ∈ P and one Q ∈ Q for which P and

- Q are boundary blocks. It then follows from the maximality of Θ that Θ is an impure beat relative to (X,Y ).


Using these blocks P ∈ P and Q ∈ Q we may now choose R ⊆ Z so that Θ = (P,Q,R) is a continuation of Θ and assume Θ is an H-trio. If H is ﬁnite, then |H| < |G| and there is nothing left to prove. Otherwise, the blocks in P and Q are inﬁnite, and it follows that A is contained in a single block of P (since A is ﬁnite). In this case, w(Y,Z) = ∞ = w(Q,R) and w¯(Y,Z) = w¯(Q,R). Furthermore, the sides (X,Y ) and (X,Z) of Θ have ﬁnite weight and are disconnected, but the side (P,Q) of Θ has ﬁnite weight and is connected.

Our next result reveals an important property of the closure of a critical set. Note that in this theorem, the block of imprimitivity T may be trivially critical.

Theorem 5.13 (Critical Closure) Let ∆ = (X,Y ) be a connected G-duet with w(∆) < ∞, let A ⊆ X be ﬁnite and critical and assume that T = [A] = X. Then T is ﬁnite and critical. Further, if N(A) = N(T) then δ∆(A) ≤ 13w(T).

Proof: Let (X,Y,Z;∼) be the trio associated with (X,Y ) and the cross (A,Y \ N∆(A)). The duet Υ = (X,Z;∼) is disconnected, so it has a nontrivial component quotient (P,Q), and our assumptions imply that T ∈ P. Now, let (B,C) be a cross of (X,Z) associated with some point in Y . It follows from the construction of (X,Y,Z;∼) that NΥ(B) = Z \C, so we may choose B ⊆ B∗ ⊆ X so that (B∗,C) is a maximal cross of Υ. Now by Lemma

- 5.11, the set B∗ is either pure with respect to P, or it has exactly one boundary block. It follows from the connectivity of (X,Y ) that [B] = X so B∗ is not contained in a block of P. Thus, B∗ contains a block of P, and since B∗ is ﬁnite, we have that T is ﬁnite.


Now deﬁne Υ∗ = (X,Z,∼∗) by the rule that x ∈ X and z ∈ Z satisfy x ∼∗ z if the blocks P ∈ P, Q ∈ Q with x ∈ P and z ∈ Q satisfy P ∼ Q. Suppose ﬁrst that C is pure relative to Q and note that this implies NΥ(B) is pure with respect to Q. In this case, for every y ∈ Y and z ∈ Z we have that there exists x ∈ X with y ∼ x ∼∗ z if and only if there exists x ∈ X with y ∼ x ∼ z. It follows from this that N∆(A) = N∆(T), which implies that T is critical (and completes the proof of this case). So, we may now assume that C is not pure relative to Q, which implies N∆(A) = N∆(T). Lemma 5.11 implies

δ∆(A) = δ(X,Y,Z;∼) = δΥ(B,C) ≤ δΥ(B∗,C) ≤ 31w◦(P) = w(T).

Furthermore, since NΥ(B) has a single boundary block, we have w(NΥ∗(B))−w(NΥ(B)) ≤ w(Υ∗) − w(Υ). This gives δ∆(T) = δΥ∗(B) ≥ δΥ(B) = δ∆(A) > 0 as desired.

Next we record a simple corollary of this for future use.

Corollary 5.14 Let ∆ = (X,Y ) be a connected G-duet with w(X,Y ) < ∞, let T ⊂ X be a ﬁnite block of imprimitivity and let A ⊆ T satisfy N(A) = N(T). Then one of the following holds.

- 1. w(N(A)) ≥ w(∆) + w(A) − 13w(T)

- 2. There is a block A ⊆ S ⊆ T so that N(A) = N(S) and w(S) = 12w(T).


In particular, w(N(A)) ≥ w(∆) + w(A) − 12w(T) is always satisﬁed.

Proof: We may assume that A is critical, as otherwise the ﬁrst outcome holds trivially. Let S = [A]. If N(A) = N(S), then the previous lemma (and the observation that

- w(S) ≤ w(T)) implies that 1 holds. Thus we may assume N(A) = N(S). If w(S) ≤ 13w(T) then w(N(A)) ≥ w(∆) ≥ w(S) + w(∆) − 13w(T) and 1 holds. Otherwise w(S) = 12w(T) so w(N(A)) ≥ w(∆) ≥ w(∆) + w(A) − 12w(T) and 2 holds.


#### 6 The Main Theorem

The goal of this section is to give a proof of the main theorem assuming the validity of several lemmas which will be stated in this section but proved later in the paper.

##### 6.1 Sidon Duets

We say that a rank 2 incidence geometry (X,Y ) is Sidon7 if there do not exist distinct points x1,x2 ∈ X and y1,y2 ∈ Y with xi ∼ yj for every i,j ∈ {1,2}. Note that that CayleyC(G;A) is Sidon if and only if A is a Sidon set. Our goal in this subsection will be to prove the following lemma.

- Lemma 6.1 (Sidon stability) Every connected critical trio with a Sidon side is either a video or a pure chord.


Our proof of this lemma will rely upon a stability lemma stated below. The proof of the ﬁrst part of this lemma is established by Lemma 7.10 and the second part follows from Lemma 11.5.

If Γ is a graph and A and B are operators given by V , E, Ck, or Pk as in Subsection

- 4.1 for which we have deﬁned an incidence relation between A(Γ) and B(Γ), then we let Γ(A,B) denote the incidence geometry (A(Γ),B(Γ)) given by this relation.


7Rank 2 incidence geometries with this property are sometimes called linear spaces, but the word “linear” is rather heavily used in mathematical writing, so we have adopted the term Sidon instead.

- Lemma 6.2 Let Θ be a connected critical trio and assume one of the following


- 1. Θ has a side which is a simple graph.
- 2. Θ has a side isomorphic to K5(E,C3)8 or K6(E,C3). Then Θ is either a video or a pure chord.


It is worth noting that in both of the lemmas just stated, we have not assumed that the trio is maximal. In sharp contrast to most of the other theorems in this paper, we do not need to assume maximality here, since the property Sidon has extremely strong forcing. Simple graphs are Sidon by deﬁnition, and they will play an important role for us as the primary instances of Sidon duets appearing in critical trios (the only others are K5(E,C3) and K6(E,C3)). The next lemma gives an indication of how they will emerge.

- Lemma 6.3 Let Θ = (X,Y,Z) be a connected critical trio. If both (Z,X) and (Z,Y ) are Sidon, then one of (X,Z), (Z,X), (Z,Y ), or (Y,Z) is a simple graph.


Proof: Since (Z,X) and (Z,Y ) are Sidon, both d(Z,X) and d(Z,Y ) are ﬁnite. Choose z ∈ Z and let (A,B) be the cross of (X,Y ) corresponding to z. We assume (without loss) that w(A) ≤ w(B). Since Θ is connected, we may choose z ∈ Z \ {z} so that the cross (A ,B ) of (X,Y ) which corresponds to z satisﬁes A ∩ A = ∅. It follows from this (and the assumption that (X,Z) is Sidon) that A ∩ A = {x} for some x ∈ X.

Suppose (for a contradiction) that B ∩ B = ∅. In this case x is not incident with any point in B ∪B so we have that we have w(X,Y ) = w(Y \N(x)) ≥ 2w(B) ≥ w(A)+w(B), but this contradicts the assumption that Θ is critical. Therefore B ∩ B is nonempty and since (Y,Z) is Sidon it follows that B ∩ B = {y} for some y ∈ Y . Furthermore, we must have B ∪ B = Y \ N(x) as otherwise we would again have w(Y \ N(x)) ≥ 2w(B) giving us the same contradiction.

If the only points in Z incident with x are z and z , then (Z,X) is a graph and we are done. Otherwise we may choose z ∈ Z \ {z,z } which is incident with x. Let (A ,B ) be the cross associated with z . By our assumptions, we must have B ⊆ B∪B , |B ∩B | ≤ 1, and |B ∩ B| ≤ 1. It follows that |B | = 2, so (Y,Z) is a simple graph.

Next we require an observation concerning some basic properties of videos. Here the two small videos shown in Figure 14 will play a special role. As indicated by this ﬁgure, the side of K5 : E ∼ V ∼ E on the pair of copies of E(K5) is isomorphic to the duet K5(E,C3), and the side of K3,3 : E ∼ V ∼ P3 on the pair (E(K3,3),P3(K3,3)) is isomorphic to the line graph of K3,3.

8This is more commonly known as Desargues conﬁguration.

K5(E,C3) E E

V

K5 : E ∼ V ∼ E

E P3 L(K3,3)

V

K3,3 : E ∼ V ∼ P3

Figure 14: Two small videos

- Observation 6.4 If ∆ is a Sidon side of a video, or a pure chord, then either ∆ or its reverse is a simple connected graph, or is isomorphic to one of K5(E,C3) or K6(E,C3).


Proof: This is immediate for pure chords, and can be veriﬁed for the exceptional videos by a straightforward check. Consider a standard video given by (E1,V,E2) = Γ : E ∼ V ∼ E. The sides (V,E1) and (V,E2) are both graphs. If |V | = 5 then Γ ∼= K5 and then (E1,E2) ∼= K5(E,C3). Otherwise |V | ≥ 6, so there are two vertex disjoint subgraphs in P3(Γ) and the four edges contained in these two paths show that (E1,E2) is not Sidon.

Next consider a standard video given by (P3,V,E) = Γ : P3 ∼ V ∼ E. The side (V,E) is graphic and the side (P3,V ) is not Sidon. If Γ ∼= K3,3, then (E,P3) is a graph. Otherwise, |V | ≥ 8 and we may choose a vertex v and edges e,e so that neither v nor any vertex adjacent to v is incident with either e or e . Considering e,e and the three two edge paths with middle vertex v we see that (P3,E) is not Sidon.

Finally, consider a standard video (P3,E,V ) = Γ : P3 ∼ E ∼ V . In this case both (V,E) and (E,P3) are graphs. Choose a vertex v and vertices w,w not adjacent with v. By considering the vertices w,w and the three two edge paths with middle vertex v we ﬁnd that (P3,V ) is not Sidon.

Proof of Lemma 6.1: Let Θ = (X,Y,Z) be a connected critical trio and assume that (X,Y ) is Sidon. We begin by proving a key claim (note that this claim applies even to trivially critical blocks of imprimitivity).

Claim: There does not exist a ﬁnite proper nontrivial block of imprimitivity of X or Y which is critical in (X,Y ).

Suppose (for a contradiction) that T ⊂ X is a ﬁnite proper critical block of imprimitivity with |T| ≥ 2 (the case when T ⊂ Y is similar). Choose distinct points x1,x2 ∈ T. Then w(N(T)) ≥ 2w(T) (by Proposition 5.6) and w(N(T)) \ N(xi)) = w(N(T)) − w(X,Y ) <

- w(T) (since T is critical) so for i = 1,2 we have that xi is incident with more than half of the points in N(T). Since (X,Y ) is Sidon it follows that |N(x1) ∩ N(x2)| = 1 and


N(T) = N(x1) ∪ N(x2). If there exists x3 ∈ T \ {x1,x2}, then N(x3) is subset of N(T) of size d = d(X,Y ) which meets N(x1) and N(x2) in at most one point. In this case, we must have d = 2 so (Y,X) is a simple graph. However, then Lemma 6.2 implies that Θ is either a video or a pure chord, and we are ﬁnished. Thus we may assume T = {x1,x2}. Now w(N(T)) is a multiple of 2w◦(X) and w(N(x1)) + w(N(x2)) is a multiple of 2w◦(X), and it follows from this that w◦(Y ) is a multiple of 2w◦(X). However, now we have w(N(T)) ≥ w(N(x1)) + w◦(Y ) ≥ w(X,Y ) + w(T) and this contradicts the assumption that T is critical.

Now, let (A,B) be a critical cross of (X,Y ) with |A|,|B| ≥ 2 (note that one exists by

our assumptions) chosen so that α) δ(A,B) is maximum. β) min{w(B) + w◦(X),w(A) + w◦(Y )} is minimum (subject to α).

Assume (without loss) that w(A)+w◦(Y ) ≤ w(B)+w◦(X), and note that this implies A is ﬁnite. Now suppose (for a contradiction) that there exists g ∈ G with 2 ≤ |gA ∩ A| < |A|. If |gB ∩ B| ≤ 1 then B is also ﬁnite and we ﬁnd

w(gA ∩ A) + w(gB ∪ B) ≥ 2w◦(X) + 2w(B) − w◦(Y ) ≥ w◦(X) + w(A) + w(B).

However, then δ(gA∩A,gB ∪B) > δ(A,B) which contradicts our choice of (A,B). Therefore, we must have |gB∩B| ≥ 2. But then, either one of (gA∩A,gB∪B) or (gA∪A,gB∩B) has deﬁciency greater than (A,B), which contradicts α, or both are equally critical and then (gA∩A,gB ∪B) contradicts the choice of (A,B) for β. It follows from this that every g ∈ G with |gA ∩ A| < |A| satisﬁes |gA ∩ A| ≤ 1.

Our claim together with Theorem 5.13 imply that [A] = X and [B] = Y , and it follows from this that the trio Θ = (X,Y,Z ) associated with the cross (A,B) is connected. Furthermore, by the above property of A we must have that (X,Z ) is Sidon. Therefore Θ has two Sidon sides, so by Lemma 6.3 we must have that one of (X,Y ), (Y,X), (X,Z), or (Z,X) is a simple connected graph. It now follows from Lemma 6.2 that Θ is either a video or a pure chord. But then, Observation 6.4 implies that one of (X,Y ) or (Y,X) is either a simple connected graph or is isomorphic to one of K5(E,C3) or K6(E,C3). Now by applying Lemma 6.2 to Θ and either (X,Y ) or (Y,X) we deduce that Θ is either a video or pure chord as desired.

##### 6.2 Nearness and Constituent Lemmas

In this subsection we will introduce the important concept of near, and then state some lemmas concerning this property which will be used to prove our main theorem. The proofs of these lemmas is postponed to later in the article.

Deﬁnition: Let ∆ = (X,Y ) and Λ be duets and let P, Q be systems of imprimitivity on X, Y with ﬁnite blocks. We say that ∆ is near Λ relative to (P, Q) if (P,Q) ∼= Λ and the following equation is satisﬁed

w(P,Q) − w(∆) < min{w◦(P),w◦(Q)}.

Next we record a useful observation about the notion of near for future use. We deﬁne a system of imprimitivity to be critical if its blocks are critical.

- Observation 6.5 If ∆ = (X,Y ) is near Λ relative to (P,Q) and w(∆) < ∞ then


- 1. P and Q are critical.
- 2. For every P ∈ P (Q ∈ Q) the set N(P) (N(Q)) is pure with respect to Q (P).


Proof: Let ∆ = (P,Q). For part 2, let P ∈ P and observe that w(∆ ) − w◦(P) < w(∆) ≤ w(N∆(P)) ≤ w(N∆ (P)) = w(∆ ).

It follows from Proposition 5.6 that w(N∆(P)) and w(∆ ) = w(N∆ (P)) must be a multiples of w◦(P). But then we must have w(N∆(P)) = w(N∆ (P)), so N(P) is pure with respect

- to Q. A similar argument shows that N(Q) is pure with respect to P for every Q ∈ Q. For part 1 we have


δ∆(P) = w(P) + w(∆) − w(N∆(P)) = w(P) + w(∆) − w(∆ ) > 0 so P is critical, and by a similar argument Q is critical.

Before introducing our next stability lemma, we need to deﬁne a particular set of duets which will play an essential role in our proof. A graph is cubic if every vertex is incident with 3 edges.

Deﬁnition: A duet ∆ is a clip if it is isomorphic to one of the following

- 1. Γ(V,P3) for a cubic graph Γ with |V (Γ)| ≥ 6
- 2. K5(E,C3)
- 3. K6(E,C3)
- 4. Petersen(E,C5)
- 5. Dodecahedron(V,F).


We call a graph (V,E) true if it is simple, connected, and all vertices have degree at least 3. We will say that a duet ∆ is a near true graph, near sequence, or near clip if it is near a duet of this type. The next lemma summarizes three stability lemmas, the ﬁrst of which follows from Lemma 10.10, the second from Lemma 11.10, and the third from Lemma 9.13.

- Lemma 6.6 (Near True Graph, Near Clip and Near Sequence Stability) Let ∆ be a side of the maximal connected critical trio Θ.

- 1. If ∆ is a near true graph, then Θ is a video.
- 2. If ∆ is a near clip, then Θ is a video.
- 3. If ∆ is a near sequence, then Θ is either a pure chord, a cyclic chord, or a dihedral chord of type 1, 2A, 2B, or 2C.


For a somewhat technical purpose in the proof, we require one additional stability result. In a duet (X,Y ) we say that a block of imprimitivity T ⊆ X or T ⊆ Y is doubling if T is critical and w(N(T)) = 2w(T). Doubling blocks naturally give rise to graphs, and the following lemma follows from Lemma 10.10.

- Lemma 6.7 (Doubling Block Stability) Let ∆ be a side of the maximal connected critical trio Θ. If ∆ has a doubling block, then either Θ is a video or ∆ is a near polygon.

In addition to these stability lemmas, we will require some lemmas which give some control over the sides of a critical trio Θ with the property that Θ ≤ Θ∗ for a song Θ∗. The following lemma ﬁts this need. It will be proved by Lemmas 7.13 and Lemma 9.10. We say that a side (X,Y ) of a trio Θ is light if there is a side of Θ other than (X,Y ) and (Y,X) which has weight at least w(X,Y ).

- Lemma 6.8 (Light Sides) Let Θ be a connected critical trio and assume that Θ ≤ Θ∗ for a song Θ∗. If (X,Y ) is a light side of Θ, then either (X,Y ) or (Y,X) is a near true graph, a near clip, or a near sequence.


##### 6.3 The Proof

In this subsection we prove our main theorem. We will say that a cross (A,B) of a duet (X,Y ) is connected if [A] = X and [B] = Y . Note that whenever (X,Y ) is connected, and (A,B) is connected, the trio associated with this cross will also be connected.

Proof of the “only if” direction of Theorem 4.7: Let Θ = (X,Y,Z) be a nontrivial maximal critical G-trio, let ∆1 = (X,Y ), ∆2 = (Z,X), and ∆3 = (Z,Y ) and assume that w(∆1) ≤

- w(∆2) ≤ w(∆3). We shall assume that Θ is a counterexample to Theorem 4.7 which is chosen according to the following criteria.

- 1. if there is a ﬁnite counterexample, then |G| is minimum.
- 2. w(∆3) is minimum (subject to 1).

- 3. |{i ∈ {1,2,3} | ∆i is connected}| is maximum (subject to 1 and 2).


By passing from Θ to Θ• we may assume that Θ is clone free. Our ﬁrst task will be to establish a sequence of claims.

- (i) Θ is connected.

Suppose (for a contradiction) that Θ is disconnected, and apply Lemma 5.12. If Θ is a pure beat, then we have an immediate contradiction. Otherwise, Θ is an impure beat, and we let Θ be an H-trio which is a continuation of Θ. If H is ﬁnite, then Θ contradicts the choice of Θ for the ﬁrst criteria. Otherwise, Θ and Θ will be the same with regard to the ﬁrst two criteria, but Θ contradicts the choice of Θ for the third.

- (ii) ∆1 is not a near true graph, a near clip, or a near sequence.

If ∆1 is a near true graph or a near clip, then it follows from Lemma 6.6 that Θ is a video which is a contradiction. If ∆1 is a near sequence, then by the same lemma, Θ is either a pure chord, cyclic chord, or dihedral chord of type 1, 2A, 2B, or 2C. For the pure chord and dihedral chords of type 2B, and 2C we have an immediate contradiction. In the remaining cases, a continuation of Θ must be a smaller counterexample to our theorem, which again contradicts our choice of Θ.

- (iii) ∆1 is not a near polygon.


Suppose (for a contradiction) that (X,Y ) is a near polygon relative to (P,Q). It follows from (ii) that |P| ≤ 3 (all other polygons are also sequences). If |P| = 2 then we have

- w(∆3) ≥ w(∆2) ≥ w(∆1) > 12|G| which contradicts part 2 of Lemma 5.3. Thus, we may assume that P = {P1,P2,P3} and Q = {Q1,Q2,Q3} where Pi  ∼ Qi for i = 1,2,3 (so then Pi ∼ Qj whenever 1 ≤ i,j ≤ 3 satisfy i = j). Next, choose z ∈ Z and let (A,B) be the cross of ∆1 associated with z. Since [A] = X and [B] = Y the set A cannot be contained in a block of P and B cannot be contained in a block of Q. It follows that there must exist 1 ≤ i ≤ 3 so that A = A ∩ Pi = ∅ and B = B ∩ Qi = ∅. Set A = A \ A and B = B \ B and observe that N(A ) and B are disjoint subsets of Y \ Qi. So, setting


k = w◦(P) = w◦(Q) we have w(N(A )) ≤ 2k − w(B ). The next inequality uses this together with Lemma 5.7.

0 ≤ δ(Pi) − δ(A )

= w(Pi) − w(N(Pi)) − w(A ) + w(N(A )) ≤ −k − w(A ) + (2k − w(B ))

= k − w(A ) − w(B ).

So w(A )+w(B ) ≤ k and similarly w(B )+w(A ) ≤ k. However, then w(∆2)+w(∆3) = w(A) + w(B) ≤ 2k < 2w(∆1) and this is a contradiction.

- (iv) If a block of imprimitivity T ⊂ X or T ⊂ Y is critical in ∆1, then w(T) < 21w(∆1).

It follows from Proposition 5.6 and the assumption that ∆1 is connected that every proper critical block of imprimitivity T of X or Y must satisfy w(T) < w(∆1). If there exists such a block with w(T) ≥ 21w(∆1) then T is a doubling block in ∆1. Then by Lemma 6.7, we ﬁnd that either Θ is a video, which is a contradiction, or Θ is a near polygon, which

- contradicts (iii).

(v) If (A,B) is a critical cross of ∆1 and min{w(A),w(B)} ≥ 21w(∆1) then (A,B) is connected.

If we suppose (for a contradiction) that A is ﬁnite and [A] = X, then Theorem 5.13 implies that [A] is critical in (X,Y ) and then we have w([A]) ≥ w(A) ≥ 21w(∆1) which

- contradicts (iv).




With these claims in hand, we are ready for the heart of the argument. Let P and Q be maximal proper systems of imprimitivity on X and Y for which the blocks are ﬁnite and critical (they are permitted to be trivially critical) in ∆1. (such systems of imprimitivity exist since the discrete partition is one, and there is a maximal one by (iv)).

Let z ∈ Z, let (A,B) be the cross of ∆1 associated with z and suppose (for a contradiction) that there is a boundary block Q ∈ Q with respect to B. Let (A ,B ) be the new cross obtained from purifying (A,B) at Q. It follows from Theorem 5.8 that

- w(A ) > w(A) − w◦(Q) ≥ 21w(∆1) and trivially, w(B ) ≥ w(B) ≥ w(∆1). Therefore, by (v) we have that the trio Θ which is associated with (A ,B ) is also connected. Let Θ be a maximal trio with Θ ≤ Θ . Now, it follows from our choice of Θ that Θ is not a counterexample, so it is a connected song. It now follows from applying Lemma 6.8 to Θ


that ∆1 is either a near true graph, a near clip, or a near sequence, but this contradicts (ii). It follows that there is no boundary block of Q with respect to B. However, then by the maximality of Θ we must have that Q is a system of clones. Since, by assumption, Θ is clone free, we conclude that Q is the discrete partition.

Ignoring our earlier assignment, let us now choose (A,B) to be a connected cross of ∆1

so that α) δ(A,B) is maximum. β) the number of boundary blocks in P w.r.t. A is minimum (subject to α). γ) min{w(B) + w◦(P),w(A) + w◦(Y )} is minimum (subject to α and β).

Note that by using a cross associated with some point z ∈ Z we must have δ(A,B) ≥ δ(Θ). Furthermore, it follows immediately from α that (A,B) is maximal.

Suppose (for a contradiction) that w(A) < w(∆1). Then we have w(B) = w(∆1) + w(A) − δ(A,B) < w(∆1) + w(∆2) − δ(Θ) = w(∆3).

Now, let Θ be the trio associated with (A,B) and let Θ be a maximal trio with Θ ≤ Θ . It follows from the above equation and our choice of Θ that Θ is a song. But then applying

- Lemma 6.8 to Θ shows that ∆1 is either a near true graph, a near clip, or a near sequence, and this contradicts (ii). We obtain a similar contradiction under the assumption that


- w(B) < w(∆1), so we conclude that w(A),w(B) ≥ w(∆1).


Next, suppose (for a contradiction) that there is a boundary block P ∈ P with respect to A. Let (A ,B ) denote the cross obtained from (A,B) by purifying at P. It follows from Theorem 5.8, the above argument and (iv) that w(B ) ≥ w(B)−w◦(P) ≥ w(∆1)− 21w(∆1). It now follows from (v) that [B ] = Y . Since A ⊇ A we also have [A ] = X and now (A ,B ) contradicts the choice of (A,B). It follows that A is pure with respect to P. We now prove two properties which will be used to handle the two possibilities for which term in optimization criterion γ is minimum. Since these arguments are quite similar, we only sketch the second.

- ( ) If w(A) + w◦(Y ) ≤ w(B) + w◦(P) then w(gA ∩ A) ≤ w◦(P) for every g ∈ G with


- gA = A.


Note that it follows from the above inequality that A is ﬁnite. Suppose (for a contradiction) that there exists g ∈ G so that 2w◦(P) ≤ w(gA ∩ A) < w(A). Let (A ,B ) = (gA ∩ A,gB ∪ B) and (A ,B ) = (gA ∪ A,gB ∩ B). If |B | ≤ 1 then B is also ﬁnite and we have

w(A ) + w(B ) ≥ 2w◦(P) + 2w(B) − w◦(Y ) ≥ w◦(P) + w(A) + w(B).

This implies that δ(A ,B ) > δ(A,B). It now follows from the maximality of P and Theorem 5.13 that [A ] = X. However, then (A ,B ) is connected and contradicts our

choice. It follows that we must have |B | ≥ 2. Now, since Y has no nontrivial critical blocks of imprimitivity, Theorem 5.13 implies that [B ] = Y so (A ,B ) will also be a connected cross. However, then one of (A ,B ) or (A ,B ) contradicts our choice of (A,B).

- ( ) If w(B) + w◦(P) ≤ w(A) + w◦(Y ) then w(gB ∩ B) ≤ w◦(Y ) for every g ∈ G with


- gB = B.


Note that it follows form the above inequality that B is ﬁnite. Arguing as in the previous case, we suppose (for a contradiction) that there exists g ∈ G with 2w◦(Y ) ≤ w(gB ∩ B) < w(B). Let (A ,B ) = (gA ∪ A,gB ∩ B) and (A ,B ) = (gA ∩ A,gB ∪ B). If w(A ) ≤ w◦(P) then A is also ﬁnite and

w(A ) + w(B ) ≥ 2w◦(Y ) + 2w(A) − w◦(P) ≥ w◦(Y ) + w(A) + w(B).

so as before we have δ(A ,B ) > δ(A,B). By Theorem 5.13 we ﬁnd that (A ,B ) is connected and this contradicts our choice. So, it must be that w(A ) ≥ 2w◦(P). But then both (A ,B ) and (A ,B ) are connected and one contradicts our choice of (A,B). It follows that every g ∈ G for which gB = B must satisfy w(gB ∩ B) ≤ w◦(Y ).

Now, in either case we let Θ = (X,Y,Z ;∼ ) be the trio associated with (A,B) and let Θ = (X,Y,Z ;∼ ) be a maximal trio with Θ ≤ Θ . It follows from the maximality of (A,B) that ∼ |X∪Z =∼ |X∪Z and ∼ |Y ∪Z =∼ |Y ∪Z . If x,x ∈ P for some P ∈ P then NΘ (x) ∩ Z = NΘ (x ) ∩ Z by construction, so this also holds in the trio Θ , but it follows from this that x and x will be clones in Θ . Therefore, P is a system of clones in Θ . Let Θ∗ be the trio obtained from Θ by taking the quotient (P,Y,Z ) and note that by property ( ) or ( ), the trio Θ∗ has a side which is Sidon. It now follows from Lemma

- 6.1 that Θ∗ is either a video or a pure chord, and thus Θ is either a video or a pure chord.


However, then applying Lemma 6.8 to Θ reveals that either ∆1 or its reverse is a near true graph, a near clip, or a near sequence, and this contradicts (ii). This completes the proof.

#### 7 Graphs

In this section we prove a stability lemma for trios with a graphic side, and a light side lemma for videos. The proof of this stability lemma has two principal parts. The ﬁrst part is a classiﬁcation of certain small edge cuts in vertex and edge transitive graphs, and this is the content of the ﬁrst subsection. The second part requires an analysis of the trios which can arise from these, and this is done in the second subsection.

##### 7.1 Small Edge Cuts

In this subsection we will prove a theorem which characterizes all edge cuts of size less than 2d (with at least one side ﬁnite) in a vertex and edge transitive graph of degree d. Our techniques are the same as those used by Mader, Watkins, Hamidoune and others to achieve similar connectivity results in vertex transitive graphs. We begin with a proposition which sharpens Observation 4.1 and motivates this characterization. Recall that for a subset of vertices A we let c(A) denote the number of edges with exactly one endpoint in A.

- Lemma 7.1 Let Γ = (V,E) be a graphic duet of degree d, and let A ⊆ V be ﬁnite or coﬁnite. Then


w◦(E) 2

2d − c(A) .

δ(A) =

Proof: First note that w(Γ) = dw◦(E) = 2w◦(V ). Let S denote the set of edges with both ends in V \A. If A is coﬁnite, then summing degrees in V \A gives us d|V \A| = 2|S|+c(A) which implies

◦(E)

δ(A) = w(S) + w(Γ) − w(V \ A) = w◦(E) |S| + d − d2|V \ A| = w

2 2d − c(A) .

Otherwise, A is ﬁnite, and setting R to be the set of edges with both ends in A we have d|A| = 2|R| + c(A) (by counting degree sums in A). This gives us

◦(E)

δ(A) = w(A) + w(Γ) − w(R ∪ ∂(A)) = w◦(E) d2|A| + d − |R| − c(A) = w

2 2d − c(A) as desired.

Next we introduce some graph theoretic terminology. The girth of a graph Γ is the length of the shortest cycle, or ∞ if it has no cycle. The line graph of Γ, denoted L(Γ), is a simple graph with vertex set E with the property that e,f ∈ E are adjacent (in L(Γ)) if these edges are incident with a common vertex (in Γ). We deﬁne LC to be the class of all graphs which are isomorphic to L(Γ) for some cubic graph Γ with girth at least four. If Γ is a regular graph with girth g and there exists an integer s so that every edge of Γ is contained in exactly s cycles with length g, then we call Γ an equitable graph. Note that every vertex and edge transitive graph is equitable. Next we oﬀer a basic proposition concerning equitable graphs. The proof follows from a simple case analysis, so we have only provided a sketch.

Proposition 7.2 The following chart is a complete list (up to isomorphism) of all connected equitable graphs with the indicated degree and girth parameters.

|Degree<br><br>|Girth|Equitable graphs|
|---|---|---|
|3<br><br>|3|Tetrahedron|
|3<br><br>|4|Cube, K3,3|
|4<br><br>|3|Octahedron, K5, members of LC|
|3|5<br><br>|Dodecahedron, Petersen|
|5|3|Icosahedron, K6|


Sketch of Proof: Let Γ be an equitable graph with degree d, girth g, and with exactly s cycles of length g containing each edge. Since every cycle which contains a vertex u must contain exactly two edges incident with u, it follows that s must be even whenever d is odd. Let us note a couple of easy facts which are helpful in the forthcoming analysis. First, observe that if g = 3 then s ≤ d−1 and if s = d−1 we must have Γ ∼= Kd+1. Next suppose that s = 2 and either d = 3, or g = 3 and the set of vertices adjacent to a given vertex induce a cycle. In either of these cases, we can form a polygonal surface from our graph by identifying each cycle of length g with a regular g-gon. In these cases, it may be helpful to argue in terms of this surface.

If d = 3 and g = 3, then s = 2 and Γ ∼= Tetrahedron. If d = 3 and g = 4, then either s = 2 and Γ ∼= Cube or s ≥ 4. In the latter case, it follows easily from considering the subgraph induced by two adjacent vertices and any vertex adjancent to one of them that Γ ∼= K3,3. If d = 3 and g = 5, then either s = 2 and G ∼= Dodecahedron, or s ≥ 4. In the latter case, it follows easily from considering the graph induced by all vertices of distance at most two from a ﬁxed vertex that s = 4 and G ∼= Petersen. If d = 4, g = 3, and s = 1, then deﬁne a new graph Υ with a vertex for each triangle of Γ and with two vertices adjacent if and only if the corresponding triangles share a vertex. Then Υ is cubic with girth at least four, and Γ ∼= L(Υ), so Γ is in LC. If d = 4, g = 3, and s = 2 then G ∼= Octahedron, and if d = 4, g = 3 and s = 3, then G ∼= K5. Finally, if d = 5 and g = 3, then either s = 2 and G ∼= Icosahedron or s = 4 and G ∼= K6.

Now we are ready for the main theorem of this subsection which classiﬁes small edge cuts in vertex and edge transitive graphs. The key property utilized by our argument is the following submodularity inequality which holds for every graph Γ and A,B ⊆ V (Γ) with c(A),c(B) < ∞.

c(A ∩ B) + c(A ∪ B) ≤ c(A) + c(B). (6)

Theorem 7.3 Let Γ = (V,E) be a simple connected vertex and edge-transitive graph of degree d and let A ⊆ V be ﬁnite and nonempty. If c(A) < 2d and |A| ≤ 12|V |, then setting Γ to be the subgraph induced by A one of the following holds.

- 1. Γ is a single vertex.
- 2. Γ is a one edge path.


- 3. Γ is a cycle and Γ is a path.
- 4. Γ is cubic and Γ is a 2-edge path.
- 5. Γ is in LC and Γ is a triangle.
- 6. Γ is isomorphic to Cube, Octahedron, Dodecahedron, Icosahedron, Petersen, or K6, and Γ is a shortest cycle of Γ.


Proof: Let G ≤ Aut(Γ) act transitively on V and E. Now suppose (for a contradiction) that the theorem is fails for Γ, and choose a counterexample A subject to the following conditions.

α) c(A) is minimum. β) |A| is minimum (subject to α).

Note that the minimality of our counterexample implies that the graph Γ is connected. We proceed with a sequence of claims.

- (i) d ≥ 3, |A| ≥ 4, and Γ is not isomorphic to Cube, Octahedron, Dodecahedron, Icosahedron, Petersen, or K6. In particular, if d = 3 then Γ has girth at least 6.

We leave the reader to verify the cases when d ≤ 2 or |A| ≤ 3 or Γ is one of the graphs in the above list. In light of Proposition 7.2 we may then assume that the girth of Γ is at least 6 in the case when d = 3.

- (ii) degΓ (x) > 21degΓ(x) for every x ∈ A.

If (ii) is false for x, then the theorem holds for A \ {x} and we must have outcome 4 or

5. Either case yields a contradiction.

- (iii) If 3 ≤ |gA ∩ A| < |A| for g ∈ G, then |gA ∩ A| = 3 and either d = 3 or Γ ∈ LC.

Let k = |gA∩A| ≥ 3 and note that |V \(gA∪A)| ≥ |gA∩A| = k. If c(gA∪A) < c(A) then by our choice of counterexample, the theorem holds for either gA ∪ A or its complement. Only outcomes 4 and 5 are possible, and in either case it follows that k = 3 so (iii) holds. Otherwise c(gA ∪ A) ≥ c(A) and then by equation 6 we conclude that c(gA ∩ A) ≤ c(A). So, the theorem holds for gA ∩ A and the desired conclusion follows immediately.

- (iv) Γ is not cubic.


- Suppose (for a contradiction) that Γ is cubic. Observe that by (ii) we must have |{v ∈ V | degΓ (v) = 2}| = c(A) < 6. If the graph Γ has at most two vertices with degree 3, then Γ has girth at most 5 and Proposition 7.2 gives us a contradiction to (i). Otherwise, we may choose a pair of adjacent vertices u,u ∈ A and a pair of adjacent vertices v,v ∈ A so that degΓ (u) = degΓ (u ) = degΓ (v) = 3 and degΓ (v ) = 2. Since G acts transitively on E we may choose g ∈ G so that g{u,u } = {v,v }. Then we have 4 ≤ |gA ∩ A| < |A| which contradicts (iii).
- (v) Γ is not in LC.

Suppose (for a contradiction) that Γ ∼= L(Υ) for a cubic graph Υ with girth at least four. Observe that the vertex set of Υ corresponds to C3(Γ) and the edge set of Υ corresponds to V . It follows that Υ is both vertex and edge transitive.

| |
|---|


Figure 15: Prism

If there exists u ∈ A with degΓ (u) = 4, then (by (ii)) we may choose v ∈ A with degΓ (v) = 3 and g ∈ G with gu = v. However then we have 4 ≤ |gA ∩ A| < |A| which contradicts (iii). It follows that degΓ (u) = 3 for every u ∈ A. Now we have |A| = c(A) < 8, so Γ is a cubic graph on fewer than 8 vertices, and it must then be isomorphic to one of K4, K3,3, or Prism (depicted in Figure 15). Observe that Γ has a 4-cycle, so Υ must have girth 4. However, then Proposition 7.2 implies that Υ is isomorphic to either Cube or K3,3. Thus Γ ∼= L(Cube) or Γ ∼= L(K3,3) and either possibility contradicts the structure of Γ .

- (vi) Let u,v ∈ A and g ∈ G satisfy gu = v and gA = A. Then d is odd and further degΓ (u) = degΓ (v) = d+12 .


If u,v and g satisfy the conditions above, then by (iii),(iv),(v) it follows that |A∩gA| ≤ 2 so both g{w ∈ A | w ∼ u} and {w ∈ A : w ∼ v} are subsets of {w ∈ V : w ∼ v} with size greater than d2 and intersection of size at most 1. The above conclusion follows immediately from this.

If there exist u,v ∈ A with degΓ (u) = degΓ (v), then choosing g ∈ G so that gu = v gives us a contradiction to (vi). Therefore Γ is regular. Now, A cannot be a block of imprimitivity of V since there are edges with both ends in A and edges with one end in A (and G acts transitively on E). It follows that we may choose g ∈ G so that ∅ = gA∩A = A. From here, (vi) implies that d is odd and Γ is d+12 regular. Now by (iv) we have d ≥ 5

so |A| = c(A)d−21 < 4d−d1 ≤ 5. The only possibility here is d = 5 and Γ ∼= K4, but then Proposition 7.2 implies that Γ ∼= K6 which contradicts (i).

A quick check of the statement of the previous theorem reveals that c(A) ≥ 2d − 2 in all cases except for the ﬁrst outcome. The next corollary follows immediately from Lemma

- 7.1 and this observation.


Corollary 7.4 Let Γ = (V,E) be a graphic duet of degree d. If A ⊆ V is ﬁnite or coﬁnite then either min{|A|,|V \ A|} ≤ 1 or δ(A) ≤ w◦(E).

##### 7.2 Stability

The main theorem from the previous subsection will be used to characterize all maximal critical crosses (A,B) of graphic duets (V,E). Here we shall determine which trios arise from such crosses by studying their behaviour under the group action. We begin with an easy lemma concerning the transitivity of duets. We say that a G-duet ∆ = (X,Y ) is incidence transitive if G acts transitively on the set {(x,y) ∈ X × Y | x ∼ y}.

- Lemma 7.5 If ∆ = (X,Y ) is a G-duet and d∆(X,Y ), d∆(Y,X) are ﬁnite and relatively prime, then ∆ is incidence transitive.


Proof: Let S ⊆ {(x,y) ∈ X×Y | x ∼ y} be a G-orbit and deﬁne a new symmetric incidence relation ∼ on X ∪ Y by the rule that x ∼ y whenever (x,y) ∈ S. It follows immediately that ∆ = (X,Y ) equipped with the incidence relation ∼ is a G-duet. Next observe

- w◦(X)

- w◦(Y )


- d∆(X,Y )

- d∆(Y,X)


- d∆ (X,Y )

- d∆ (Y,X)


=

=

.

Now d∆(X,Y ) and d∆(Y,X) are relatively prime, d∆ (X,Y ) ≤ d∆(X,Y ), and d∆ (Y,X) ≤ d∆(Y,X). It follows that d∆ (X,Y ) = d∆(X,Y ) and d∆ (Y,X) = d∆(Y,X), so ∆ = ∆ and we conclude that ∆ is incidence transitive.

For a graph Γ = (V,E) an ordered pair of adjacent vertices is called an arc, and we say that Γ is arc transitive if Aut(Γ) acts transitively on the set of arcs.

- Lemma 7.6 Let Γ = (V,E) be a graphic G-duet with degree 3. Then G acts transitively on P3(Γ).


Proof: It follows from the previous lemma that Γ is G-incidence transitive, so G acts transitively on the arcs of Γ. Next we establish a correspondence between P3(Γ) and the

set of arcs of Γ as follows. We associate the path with vertex sequence x,y,z to the arc (y,y ) where y is unique vertex adjacent to y other than x,z. Since the action of G on Γ preserves this correspondence, it follows that G acts transitively on P3(Γ) as desired.

If Γ is a graph which is isomorphic to Petersen (K6), we say that a face set for Γ is a subset F of C5(Γ) (C3(Γ)) with the property that every edge is contained in exactly two members of F. This set of faces then yields an embedding of Γ in the projective plane as shown in Figure 8.

Proposition 7.7 Let Γ = (V,E) be a graphic G-duet with girth g. Then we have

- 1. If Γ is isomorphic to Cube, Icosahedron, or Dodecahedron, then G acts transitively on Cg(Γ).
- 2. If Γ ∼= Octahedron, then either G acts transitively on C3(Γ) or C3 consists of two G-orbits with every edge incident with exactly one cycle from each orbit .
- 3. If Γ is isomorphic to either Petersen or K6, then either G acts transitively on Cg(Γ) or Cg(Γ) contains two G-orbits, each of which is a face set for Γ.


Proof: Let S ⊆ Cg(Γ) be a G-orbit. Since G acts transitively on E, it follows that every e ∈ E is incident with the same number, say t, of cycles in S. If the degree of Γ is odd, then t must be even, since every such cycle incident with a vertex v contains two edges from ∂(v). This easily implies the result.

- Lemma 7.8 Let Γ = (V,E) be a graph which is either a cycle or a two-way inﬁnite path. If G ≤ Aut(Γ) acts transitively on V and E, then G acts transitively on Pk(Γ) for every k.


Proof: For i = 1,2 let Γi be a path of length k in Γ given by the vertex-edge sequence v1i,ei1,v2i,...,eik−1,vki (so each eij is an edge incident with the vertices vji and vji+1). It is suﬃcient to prove that there exists g ∈ G with gΓ1 = Γ2. If k is odd, say k = 2j + 1, then since G acts vertex transitively there exists g ∈ G with gvj1+1 = gvj2+1 (so g maps the middle vertex of Γ1 to the middle vertex of Γ2) and then gΓ1 = Γ2. If k is even, say k = 2j then we may choose g ∈ G with ge1j−1 = e2j−1 (so g maps the middle edge of Γ1 to the middle edge of Γ2) and then gΓ1 = Γ2.

We have now collected the required information concerning the actions of G on various structures in graphic G-duets for our stability lemma. However we need to take care of one more detail before we are ready for this proof. In the previous subsection we saw small edge cuts arising from triangles in graphs from LC. However, this class of graphs does not

appear in our deﬁnition of videos. This disappearance is due to the following observation showing that these trios are isomorphic to other videos.

- Observation 7.9 Let Υ be a cubic graph with girth at least 4 and let Γ = L(Υ). Then Γ : C3 ∼ V ∼ E ∼= Υ : V ∼ E ∼ P3.


Proof: There are natural correspondences between V (Γ) and E(Υ) and between C3(Γ) and V (Υ). In addition, we may associate each path of Υ with vertex sequence x,y,z to the edge of Γ which is contained in the triangle associated with y and has one endpoint in the triangle associated with x and one in the triangle associated with z. This yields the desired isomorphism.

We are now ready to prove the main result from this section.

- Lemma 7.10 (Graph Stability) Every connected critical trio with a side which is a simple graph is either a video or a pure chord.


Proof: Let (V,E,Z) be a connected critical trio and assume that Γ = (V,E) is a simple graph of degree d. The clone relation must be trivial when restricted to V ∪ E, and by identifying clones in Z we may assume it is also trivial on Z. Let (A,B) be a cross of (V,E) associated with some point in Z. We will determine the original structure of (V,E,Z) by classifying (A,B) and then determining its image under the action of G. To classify (A,B), note that Lemma 7.1 gives c(A) < 2d so either A or A = V \ A must satisfy one of the six outcomes of Theorem 7.3. We now step through these possibilities, studying the possible orbits of (A,B) for each one.

The ﬁrst outcome contradicts the assumption that (V,E,Z) is connected, since in this case either d(Z,V ) = 1 or d(Z,E) = 0. In all the remaining cases Corollary 7.4 implies that δ(A) ≤ w◦(E) so we must have B = E \ N(A).

For the second outcome, it is not possible for A to be the vertex set of a one edge path, since then d(Z,E) = 1 contradicting our connectivity assumption. If A is the vertex set of a one edge path, then since G acts transitively on E we have (Z,V,E) ∼= Γ : E ∼ V ∼ E. It follows from the connectivity of (V,E,Z) that |V | ≥ 5, so (Z,E,V ) is a standard video.

In case we have the third outcome, Γ is either a cycle or a two-way inﬁnite path and either A is the vertex set of a path or B is the edge set of a path (both if Γ is ﬁnite). It then follows from Lemma 7.8 that either (Z,V,E) ∼= Γ : Pk ∼ V ∼ E or (V,E,Z) ∼= Γ : V ∼ E ∼ Pk for some k, and in either case we have that (V,E,Z) is a pure chord.

For the fourth outcome, Γ is cubic and either A is the vertex set of a 2 edge path or B is the edge set of a 2 edge path. It then follows from Lemma 7.6 that either (V,E,Z) ∼=

Γ : V ∼ E ∼ P3 or (Z,V,E) ∼= Γ : P3 ∼ V ∼ E. Again by the connectivity of (V,E,Z) we must have |V | ≥ 6, so (V,E,Z) is a standard video.

If we get the ﬁfth outcome, Γ is in LC and either A is the vertex set of a triangle, or B is the edge-set of a triangle. The latter possibility cannot occur, since this would imply d(E,Z) = 1 contradicting our connectivity assumption. To handle the former case, let us choose a cubic graph Υ so that Γ ∼= L(Υ). Now G acts transitively on the vertices and edges of Υ so Υ is also a G-duet. Furthermore G acts transitively on the triangles of Γ so

- Observation 7.9 implies (Z,V,E) ∼= Γ : C3 ∼ V ∼ E ∼= Υ : V ∼ E ∼ P3.


Finally, let us consider the sixth outcome. In this case, Proposition 7.7 implies that (V,E,Z) is an exceptional video except in the special case when Γ ∼= Octahedron and the action of G on the triangles is not transitive. However, in this case we have d(E,Z) = 1 which contradicts our connectivity assumption.

##### 7.3 Light Sides of Videos

In this subsection we will prove a simple lemma which bounds the deﬁciency of a video, and we will prove our light side lemma for videos.

- Lemma 7.11 (Video criticality) Let Θ = (X,Y,Z) be a video. Then δ(Θ) ≤ min{w◦(X),w◦(Y ),w◦(Z)}.

Proof: By possibly passing to a quotient, we may assume that Θ is clone free. We will use

- Lemma 7.1 to relate δ(Θ) to w◦(E). For a trio Θ = Γ : E ∼ V ∼ E based on a graph of degree d ≥ 3 we have δ(Θ) = w◦(E) ≤ w◦(V ). For a trio Θ = Γ : E ∼ V ∼ P3 or Γ : V ∼


E ∼ P3 based on a cubic graph Γ we have δ(Θ) = 12w◦(E) = w◦(P3) ≤ w◦(E) ≤ w◦(V ). The exceptional trios are straightforward to check.

For the purposes of determining the light sides of videos, it will be convenient to record the densities of the sides of (ﬁnite) videos. This information appears in Figure 16 where the variables d, e, and v denote the degree of Γ, |E(Γ)|, and |V (Γ)|.

- Lemma 7.12 Let Θ be a clone free video and let (X,Y ) be a light side of Θ. Then either (X,Y ) or (Y,X) is a true graph or a clip.


Proof: We shall repeatedly call upon the information in Figure 16, and shall use d,e,v as in this ﬁgure. The proof of the lemma is a straightforward check for the exceptional

###### 1 − 7e

1 − v3

1 − 2de+1

P3

P3

V

E

E

E

3 v

2 v

2 e

3 e

- d

- e


- d

- e


V

V

E

Γ : E ∼ V ∼ E Γ : P3 ∼ V ∼ E Γ : P3 ∼ E ∼ V

- 2

- 3


3 5

- 1

- 2


- 3

- 4


V F

F

F E

V F

E

1 4

1 6

1 10

1 10

1 4

1 3

1 4

1 6

V

V

E

E

Cube : V ∼ E ∼ F Dodec. : F ∼ V ∼ E Dodec. : V ∼ E ∼ F Icos. : F ∼ V ∼ E

- 1

- 2


- 1

- 2


- 1

- 2


C5 V

C3

F

V

V

1 3

1 5

1 3

1 5

1 5

1 3

E

E

E

Petersen : C5 ∼ E ∼ V Petersen : F ∼ E ∼ V K6 : C3 ∼ E ∼ V

| |
|---|


###### Figure 16: Densities of video sides

###### videos. Consider a standard video given by (E1,V,E2) = Γ : E ∼ V ∼ E. Obviously, the duets (V,E1) and (V,E2) are graphs. If the duet (E1,E2) is a light side, then 1− 2de+1 ≤ de and since e = dv2 this implies 2 ≤ d(6 − v) so we must have v ≤ 5. However, then Γ ∼= K5 and (E1,E2) is isomorphic to the clip K5(E,C3). Next consider a video given by (P3,V,E) = Γ : P3 ∼ V ∼ E (where Γ is cubic). The side (V,E) is a graph and (P3,V ) is a video. If the side (P3,E) is light, then 1 − 7e ≤ v3. Now using e = 23v we ﬁnd v ≤ 233 < 8. However, then Γ ∼= K3,3, and (as seen in Figure 14) we have that (E,P3) is a graph. Finally, we consider a standard video of the form (P3,E,V ) = Γ : P3 ∼ E ∼ V . Both of the sides (E,P3) and (V,E) are graphs. If (P3,V ) is a light side then 1 − v3 ≤ 3e. However, then using e = 23v we have v ≤ 5 which contradicts the deﬁnition.

###### Lemma 7.13 (Light Sides Video) Let Θ ≤ Θ∗ be trios and assume that Θ is critical and that Θ∗ is a video. If ∆ is a light side of Θ, then either ∆ or its reverse is either a near true graph or a near clip. Proof: Assume that Θ = (X,Y,Z;∼) and Θ∗ = (X,Y,Z;∼∗) and that ∆ = (X,Y ). Since

- (X,Y ;∼) is a light side of Θ we may assume (without loss) that w(X,Y ;∼) ≤ w(Y,Z;∼). Since Θ is critical we must have


w(X,Y ;∼∗) − w(X,Y ;∼) < δ(Θ∗). (7)

Suppose (for a contradiction) that w(X,Y ;∼∗) > w(Y,Z;∼∗). Let P,Q denote the clone partitions of X,Y in the trio Θ∗ and note that w(X,Y ;∼∗) and w(Y,Z;∼∗) are both multiples of w◦(Q). Thus Lemma 7.11 implies

w(X,Y ;∼) > w(X,Y ;∼∗) − δ(Θ∗) ≥ w(X,Y ;∼∗) − w◦(Q) ≥ w(Y,Z;∼∗) ≥ w(Y,Z;∼)

which is contradictory. So, Lemma 7.12 implies that either (X,Y ;∼∗) or (Y,X;∼∗) is either a true graph or a clip. Equation 7 then gives us

w(X,Y ;∼) > w(X,Y ;∼∗) − δ(Θ∗) ≥ w(X,Y ;∼∗) − min{w◦(P),w◦(Q)} so ∆ = (X,Y ;∼) is near (X,Y ;∼∗)• relative to (P,Q) as desired.

#### 8 Octahedral Choruses

The goal of this section will be to classify maximal critical octahedral choruses.

##### 8.1 Octahedral Classiﬁcation

Let Λ = (X1,...,Xn) be an octahedral chorus with distinguished partition {Λ1,Λ2,Λ3}. In Section 4 we associated Λ with a graph Γ which has vertex set {X1,...,Xn} and an edge between Xi and Xj if Xi and Xj are not contained in the same member of the distinguished partition. Furthermore, we split the edges of Γ into three types: empty, partial, and full. Here we shall reﬁne this division by introducing a weight function on the edges of Γ given by the rule that the weight of an edge e between Xi and Xj is given by q(e) = q(Xi,Xj) (recall that q(Xi,Xj) is the density of the duet (Xi,Xj)). So, an edge e is empty if q(e) = 0, full if q(e) = 1 and partial if 0 < q(e) < 1. We will also use the function m given by m(Xi) = 1 if the member of the distinguished partition containing Xi has size two, and m(Xi) = 2 otherwise. We say that the graph Γ equipped with the functions q and m is associated with Λ. The following easy observation relates the deﬁciency of Λ to this graph. Here we use xy to denote the edge between vertices x and y.

- Observation 8.1 An octahedral chorus Λ is critical if and only if its associated graph Γ satisﬁes


m(x)m(y)q(xy) > 6

xy∈E(Γ)

Proof: This follows immediately from the deﬁnition of critical and the observation that for a ﬁnite group H an H-duet (X,Y ) satisﬁes

wH(X,Y ) = d(X,Y )w◦(Y ) = d(X,Y )|H| |Y |

= |H|q(X,Y ).

Our next proposition records some simple properties we will use frequently.

- Lemma 8.2 Let Λ be an octahedral chorus and let Γ be the associated graph. Let e,e ,e ∈ E(Γ) be the edge set of a triangle.


- 1. If e is a full edge, one of e ,e is empty.
- 2. If q(e) > 0 then q(e ) + q(e ) ≤ 1.
- 3. If e,e ,e are nonempty then q(e) + q(e ) + q(e ) ≤ 32.

- 4. q(e) + q(e ) + q(e ) ≤ 2.


Proof: Part 1 is immediate, parts 2 and 3 follow from Lemma 5.3, and part 4 follows from part 3.

With this, we are ready to prove our classiﬁcation theorem for octahedral choruses.

- Proof of Theorem 4.5: Let Λ be a maximal critical octahedral chorus and let Γ be the associated weighted graph. Note that the maximality of Λ implies that every partial edge


of Γ must be contained in a triangle of partial edges. Let ζ = uv∈E(Γ) q(uv)m(u)m(v), so ζ > 6 by assumption. We split into cases depending on |V (Γ)|.

- Case 1: |V (Γ)| ≤ 4.


If |V (Γ)| = 3 then Γ must have an empty edge as otherwise part 3 of Lemma 8.2 gives

ζ = 4 e∈E(Γ) q(e) ≤ 6 which is contradictory. However, then by maximality Γ must have two full edges and one empty edge (a graph which appears in Figure 13). Next suppose

that |V (Γ)| = 4 and let y,z ∈ V (Γ) be the two vertices with m(y) = m(z) = 2 and let x,x be the two vertices with m(x) = m(x ) = 1. If every edge is partial then using part 3 of

- Lemma 8.2 gives us


ζ = 2 q(yx) + q(zx) + q(yz) + 2 q(yx ) + q(zx ) + q(yz) ≤ 2(23 + 32) = 6

which is a contradiction. If yx, zx and yz are partial then one of yx and yz is empty so using part 2 of Lemma 8.2 we ﬁnd

ζ ≤ 4q(yz) + 2q(xy) + 2q(xz) + 2 = 2(q(yz) + q(xy)) + 2(q(yz) + q(xz)) + 2 ≤ 6

which is another contradiction. Thus Γ must have no partial edges and an easy check reveals that it must be one of the graphs in Figure 13.

- Case 2: |V (Γ)| = 5. Let x be the vertex with m(x) = 2, let y,z,y ,z be the other vertices and assume that

- y and y are nonadjacent. First, observe that if all edges are partial, then summing the bound from part 3 of Lemma 8.2 over all triangles gives us ζ ≤ 6 which is a contradiction. It follows that there must be at least one empty edge. Next suppose that yz is empty and that all other edges except possibly y z are nonempty. Then using bounds 2 and 4 from


Lemma 8.2 we ﬁnd ζ = q(xy) + q(yz ) + q(xy) + q(xz ) + q(xz) + q(xy ) + q(xz) + q(zy )

+ q(xy ) + q(xz ) + q(y z ) ≤ 6

and this is a contradiction. It follows from this that either Γ has an empty edge incident with x or Γ has two empty edges incident with some other vertex. In either case, we may assume without loss that there is a vertex not incident with any partial edge. We may assume (without loss) that z is such a vertex. If all edges not incident with z are partial then using bound 2 from the above proposition gives us

q(xy) + q(yz) + q(xy) + q(xz) + q(xy ) + q(y z) + q(xy ) + q(xz) ≤ 4

but then again ζ ≤ 6 which gives us a contradiction. It follows that there is at most one triangle of partial edges in Γ. If there is no triangle of partial edges then Γ must be one of the graphs in Figure 13 of type −1. Otherwise, applying the bound in part 3 of the above proposition to the unique triangle of partial edges reveals that the total sum of q(uv)m(u)m(v) over all non partial edges must be greater than 3, and then Γ must be one of the graphs from Figure 13 of type 2.

- Case 3: |V (Γ)| = 6.


Call two triangles T,T of Γ opposite if every they are vertex disjoint. We begin by proving that for every pair of opposite triangles T,T , there is an empty edge in E(T) ∪ E(T ). To show this, let us suppose (for a contradiction) that it fails, and let E(T) = {e1,e2,e3}. For i = 1,2,3 let Ti be the triangle distinct from T which contains ei and let the edges of Ti be ei,e i,e i . Now using part 2 of Lemma 8.2 gives w(e i) + w(e i ) ≤ 1 and part 3 of this proposition gives w(E(T)),w(E(T )) ≤ 32 and this contradicts ζ > 6.

Our next goal will be to prove that there is a vertex x of Γ which is incident with at least two empty edges but no partial edge. To do so, let us now choose S to be a minimal set of empty edges so that every pair of opposite triangles contains at least one. If |S| = 2

then S consists of two edges incident with a common vertex x but not contained in a triangle, and in this case the vertex x meets our goal. Otherwise |S| = 3 and there exist opposite triangles T,T so that S ⊆ E(T) ∪ E(T ). If S = E(T), then we may partition the edges not in T into three triangles, and then bound 5 from Lemma 8.2 brings us to a contradiction. In the remaining case, there is a vertex x incident with two edges in S, and every triangle containing x contains an edge in S, so by maximality, x is not incident with any partial edge.

Let V (Γ) = {x,x ,y,y ,z,z } (with x as in the previous paragraph) and assume that x,x are nonadjacent and y,y are nonadjacent. Suppose (for a contradiction that x is not incident with an empty edge. Then using bound 2 from Lemma 8.2 gives us

q(x z) + q(zy ) + q(x y) + q(yz) + q(x z ) + q(z y) + q(x y ) + q(y z ) ≤ 4

and since x is incident with at least two empty edges, this is contradictory. So, we may assume without loss that x y is empty. It now follows that y is not contained in any triangle of partial edges.

Based on our analysis, we now have that Γ contains at most two triangles of partial edges, and if there are two, they share an edge. If there are no partial edges, then ζ > 6 implies that Γ is one of the graphs in Figure 5 of type −1 or type 0. If there is one triangle of partial edges, then bound 3 from Lemma 8.2 implies that there must be at least 5 full

- edges, and it follows that Γ is one of the graphs in Figure 5 of type 1. Finally, if there are two triangles of partial edges sharing an edge, then bound 3 in Lemma 8.2 implies that the sum of the weights of these partial edges is at most 3, so there must be at least 4 full
- edges, and it follows that Γ is one of the graphs in Figure 5 of type 2.


##### 8.2 Type 2 Classiﬁcation

In this subsection we will further analyze type 2 octahedral choruses, showing that those of interest to us must have type 2A, 2B, or 2C. We also record a simple lemma concerning the deﬁciency of an octahedral chorus.

- Lemma 8.3 Let (X,Y,Z) be a nontrivial maximal critical trio and assume δ(X,Y,Z) = w(X,Y ). Then (X,Y,Z) is a pure beat relative to (X,Y ).


Proof: It follows from Theorem 5.9 that (X,Y ) is disconnected, so we may let (P,Q) denote its component quotient. Choose z ∈ Z and let (A,B) be the cross associated with

- z. Then δ(Θ) = δ(A,B), so Lemma 5.11 implies that (A,B) is pure with respect to (P,Q). It then follows from maximality that (X,Y,Z) is a pure beat relative to (X,Y ), as desired.


We are now ready to prove our classiﬁcation theorem for octahedral choruses of type 2.

- Proof of Theorem 4.6: Let Λ be a maximal critical H-octahedral chorus of type 2 with incidence relation ∼ and choose X,Y,Z1,Z2 so that for i = 1,2 we have that (X,Y ),


- (Y,Zi), and (X,Zi) are sides of Λ each of which is partial. We may assume that either Λ has rank 6 and Z1 = Z2 or Λ has rank 5 and Z1 = Z2 has the property that {Zi} is a member of the distinguished partition. For i = 1,2 let Θi = (X,Y,Zi;∼) and note that Θi is a nontrivial H-trio. Our deﬁnitions now imply the following (for both the rank 5 and rank 6 cases)


0 < δ(Λ) = w(X,Y ) + w(X,Z1) + w(Y,Z1) + w(X,Z2) + w(Y,Z2) − 2|H|

= δ(Θ1) + δ(Θ2) − w(X,Y )

Observe ﬁrst that the above equation together with the easy bound δ(Θi) ≤ w(X,Y ) (from Lemma 5.3) imply that both Θ1 and Θ2 are critical. If (X,Y ) is connected, then Theorem

- 5.9 implies δ(Θi) ≤ 21w(X,Y ) for i = 1,2 which again contradicts our equation. Thus, (X,Y ) is disconnected, and we will let (P,Q) be its component quotient. Now for i = 1,2 choose zi ∈ Zi and let (Ai,Bi) be the cross of (X,Y ) associated with zi in the trio Θi, and note that the maximality of Λ implies that (Ai,Bi) is maximal for i = 1,2. It follows from Lemma 5.11 that at least one of (A1,B1) and (A2,B2) is pure with respect to (P,Q). If Λ has rank 5, then Θ1 = Θ2 and (A1,B1) = (A2,B2) is pure. Now by maximality, Θ1 is a pure beat relative to (X,Y ), and Λ has type 2C. So, we may now assume that Λ has rank 6. For


i = 1,2 if (Ai,Bi) is pure, choose a maximal trio Θi = (X,Y,Z,∼i) with Θi ≤ Θ∗i and note that the maximality of (Ai,Bi) implies that ∼ |X∪Zi =∼i |X∪Zi and ∼ |Y ∪Zi =∼i |Y ∪Zi, so

- Lemma 8.3 implies that Θ∗i is a pure chord relative to (X,Y ). If both (A1,B1) and (A2,B2) are pure, then the maximality of Λ implies ∼ |X∪Y = ∼1 |X∪Y ∩ ∼2 |X∪Y and we conclude that Λ has type 2B. Otherwise, we may assume (without loss) that (A1,B1) is impure. In this case Lemma 5.11 implies that (X,Y,Z1;∼) is an impure beat relative to (X,Y ). Further, Θ2 = (X,Y,Z;∼2) is a pure beat relative to (X,Y ) and by construction ∼ |X∪Y ⊆∼2 |X∪Y so Λ is type 2A.


- Lemma 8.4 Let Λ = (X1,...,Xn) be a maximal critical octahedral chorus of type 0, 1, or 2 and let (Xi,Xj) be a nonempty side of Λ. Then δ(Λ) ≤ w(Xi,Xj).


Proof If (Xi,Xj) is full, then the result is immediate. Otherwise there exists 1 ≤ k ≤ n so that (Xi,Xj,Xk) is a nontrivial trio for which δ(Λ) ≤ δ(Xi,Xj,Xk). Now the result follows from Lemma 5.3.

#### 9 Sequences and Near Sequences

The purpose of this section is to prove a stability lemma for near sequences and a light side lemma for chords.

##### 9.1 Sequence Stability

In this subsection we establish some basic terminology, and then prove a stability lemma for sequences.

Let ∆ = (X,Y ) be a sequence. We deﬁne the length of ∆ to be = d(X,Y ). We say that two points x,x ∈ X (or x,x ∈ Y ) are consecutive if |N(x)∩N(x )| = −1. It follows from our deﬁnitions (which require 2 ≤ ≤ |X| − 2) that every point in X is consecutive with exactly two other points, so the graph on X obtained by adding an edge between each pair of consecutive points is either a two-way inﬁnite path or a (ﬁnite) cycle. We say that a set I ⊆ X (or I ⊆ Y ) is an interval if we can write I = {x1,x2,...,xk} where all these points are distinct, and xi and xi+1 are consecutive for every 1 ≤ i ≤ k − 1. In this case we call x1 and xk the endpoints, and we say the sequence is nontrivial whenever x1 = xk. Our ﬁrst lemma shows that critical crosses of sequences come from intervals.

- Lemma 9.1 Let ∆ = (X,Y ) be a sequence. If (A,B) is a nontrivial critical cross of ∆ with A ﬁnite, then (A,B) is maximal and A, Y \ B are intervals.


Proof: Let (A,B) be a nontrivial critical cross, and choose a maximal cross (A∗,B∗) with A∗ ⊇ A and B∗ ⊇ B. Since N(A∗) is ﬁnite, we may express it as a disjoint union of intervals I1 ∪ I2 ∪ ... ∪ Im. For each x ∈ A∗ we have that N(x) is an interval, so there must exist 1 ≤ i ≤ m with N(x) ⊆ Ii. If m > 1 we may partition A∗ into {A∗1,A∗2} so that N(A∗1) ∩ N(A∗2) = ∅. Then Theorem 5.9 implies

w(N(A∗)) = w(N(A∗1)) + w(N(A∗2)) ≥ w(A∗1) + 21w(∆) + w(A∗2) + 21w(∆)

= w(A∗) + w(∆)

which contradicts the criticality of A∗. Thus N(A∗) = Y \B∗ is a single interval, and then by maximality, A∗ must also be an interval. Furthermore, if we set k = w◦(X) = w◦(Y ) then δ(A∗,B∗) = kd(X,Y ) + k|A∗| − k|N(A∗)| = k. It follows from this last equation that (A,B) = (A∗,B∗) which completes the proof.

Let G be a group acting on a set X. We previously deﬁned this action to be dihedral if G is dihedral and the rotation subgroup of G acts regularly on X. We now deﬁne this

action to be cyclic if G is cyclic and G acts regularly on X, and we deﬁne it to be split if G is dihedral and G acts regularly on X.

Let ∆ = (X,Y ) be a G-duet which is a sequence. The automorphism group of ∆ must preserve the relation consecutive, and it follows easily that Aut(∆) is the dihedral group Dn where n = |X| ≥ 4 (here we permit n = ∞ if X is inﬁnite). Since ∆ is a G-duet, this gives us a homomorphism

φ : G → Aut(∆) ∼= Dn.

Note that the kernel of φ is given by H = G(X) = G(Y ). It follows easily that the action of G/H on X and Y must be either dihedral, cyclic, or split, and we say that ∆ has dihedral, cyclic, or split action accordingly. We record this observation below.

- Observation 9.2 If (X,Y ) is a G-duet which is a sequence, it has either cyclic, dihedral, or split action.


We deﬁne a coset S ∈ G/H to be a consecutive shift if for some (and thus every) g ∈ S we have that gx and x are consecutive for every x ∈ X. Note that sequences with dihedral or cyclic action have consecutive shifts, but sequences with split action do not. Indeed, for a sequence (X,Y ) with split action, we may colour the points in X with {black,white} so that consecutive points are distinct colour, and then φ(G) contains all rotations which map each colour class to itself, and all ﬂips which interchange the colour classes. Sequences with split action must also satisfy an additional parity constraint as indicated by the following observation.

Observation 9.3 Let ∆ = (X,Y ) be a G-duet which is a sequence with split action.

- 1. The collection of all intervals of Y of length m form a single orbit under the action of G if m is odd, and form two orbits if m is even.
- 2. The length of ∆ is odd.


Proof Sketch: To see part 1, ﬁrst suppose that m is odd, and note that for any two intervals, I,I ⊆ Y with |I| = |I | = m there must exist g ∈ G which maps the “middle point” of I to the “middle point” of I and then gI = I. On the other hand, if m is even and I is an interval with |I| = m then there exists g ∈ G which acts nontrivially on X but has gI = I. For part 2, note that in order to be a G-duet, G must act transitively on {N(x) | x ∈ X}, so d(X,Y ) = d(Y,X) must be odd.

Let Θ = (X,Y,Z) be a G-trio which is a pure chord. We say that Θ has dihedral, cyclic, or split action if setting H = G(X) = G(Y ) = G(Z) we have that the action of G/H on each

of X, Y , and Z has the corresponding type. It follows easily that every pure chord has either dihedral, cyclic, or split action.

We are now ready for our stability lemma for sequences.

- Lemma 9.4 (Sequence Stability) Let Θ be a maximal critical connected G-trio. If Θ has a side ∆ which is a sequence, then Θ is a pure chord.


Proof: By identifying clones, we may assume that Θ = (X,Y,Z) is a clone free G-trio and that (X,Y ) is a sequence. Then choose z ∈ Z, let (A,B) be the cross of (X,Y ) associated with z, and assume A is ﬁnite. If {gA | g ∈ G} is the set of all intervals of X of size |A|, then (X,Y,Z) is a pure chord as desired. This completes the proof except in the case when (X,Y ) has split action and |A| is even. However, it then follows from Observation

- 9.3 that there exist distinct points x,x ∈ X for which x ∈ gA if and only if x ∈ gA for all g ∈ G. But then N(x) ∩ Z = N(x ) ∩ Z but N(x) ∩ Y = N(x ) ∩ Y and this contradicts the maximality of Θ.


##### 9.2 Adjusting Fringed Sequences

In this section we will prove a key lemma which allows us to adjust a fringed sequence with a special behaviour. As a consequence of this we will derive lemmas to deal with dihedral chords of type −1 and type 0. We begin with some deﬁnitions and a signiﬁcant technical point.

Consider a G-duet ∆ = (X,Y ) which is a length fringed sequence relative to (P,Q) where J = Z or Z/nZ for some n ≥ min{4,  + 1} and P = {Pj | j ∈ J} and Q = {Qj | j ∈ J} satisfy

 

partial if j = i or j = i + − 1 full if i + 1 ≤ j ≤ i + − 2 empty otherwise

(Pi,Qj) is

(8)



Let H = G(P) = G(Q) and recall that by our deﬁnition G/H is dihedral, and further, the action of G/H on P and Q is dihedral.

We now deﬁne ∆ to be short if = 2 and long if = |J| − 1. Observe that the duet (P,Q) will be a sequence if and only if ∆ is not long. We will have to be mindful of this technicality since we will be interested in passing between fringed sequences and near sequences. Also, this slight diﬀerence will force us to deﬁne a couple of terms for fringed sequence which we have already established for sequences.

For i,j ∈ J we say that Pi and Pj (Qi and Qj) are consecutive if i = j ± 1. It is straightforward to check that every automorphism of ∆ must preserve this relation. As before, we say that S ∈ G/H is a consecutive shift if some (and thus every) g ∈ S we have

that gP and P (gQ and Q) are consecutive for every P ∈ P (Q ∈ Q). It follows that there are exactly two consecutive shifts, S and S−1, one of which maps each block in P,Q to the next higher index, and one mapping each such block to the next lower index.

Deﬁnition: Let Λ be a square chorus. We say that Λ is small (big) if there exists P ∈ Λ so that (P,Q) is empty (full) for every Q ∈ Λ which is not in the same member of the distinguished partition as P.

- P30
- P31


- P20
- P21


- P10
- P11


- P00
- P01


| |
|---|
| |
| |
| |
| |
| |
| |
| |


| |
|---|
| |
| |
| |


| |
|---|
| |
| |
| |


| |
|---|
| |
| |
| |
| |
| |
| |
| |


- P30
- P31


- P20
- P21


- Q1
- Q2

Q4

- Q3


- P10
- P11


- P00
- P01


- Q1
- Q2

Q4

- Q3


Figure 17: Adjusting a Fringed Sequence

- Lemma 9.5 (Adjusting Fringed Sequences) Let (X,Y ) be a fringed sequence of length relative to the systems of imprimitivity P,Q of X,Y and assume it has a small associated


square chorus, that H = G(P) = G(Q), and that S ∈ G/H is a consecutive shift. If = 2 then (X,Y ) is disconnected. Otherwise, there exist systems of imprimitivity P of X and Q of Y so that

- • G(P ) = G(Q ) = H.
- • w◦(P ) = w◦(Q ) = w◦(P) = w◦(Q).
- • (P ,Q ) is a sequence of length − 1 with dihedral action and consecutive shift S.
- • (X,Y ) is a near sequence relative to (P ,Q )


Proof: Assume that (X,Y ) and P,Q, H, and are as given in equation 8, let Λ be an associated square chorus, and note that Λ is nonempty by assumption. Consider (P1,Q1) and observe that by the assumption Λ is small, there must either exist x ∈ P1 so that N(x)∩ Q1 = ∅ or there must exist y ∈ Q1 so that N(y) ∩ P1 = ∅ and we shall assume the former case without loss. It now follows from our assumptions that every Pj is the disjoint union of two H-orbits which we shall denote Pj0 and Pj1. We may assume further that (Pj1,Qj) and (Pj0,Qj+ −1) are empty for every j ∈ J. Now, P = {...,P01 ∪ P10,P11 ∪ P20,P21 ∪ P30,...} is

a system of imprimitivity. It follows from our construction that (P11 ∪P20,Qj) is nonempty only for 2 ≤ j ≤ . If = 2 then N(P11∪P20) is contained in Q2 and (X,Y ) is disconnected. Otherwise, (P ,Q) is a sequence of length − 1 and

w(X,Y ) = 2( − 2)|H| + wˆH(Λ) > ( − 2)w◦(P) = w(P ,Q) − w◦(P )

so (X,Y ) is a near sequence relative to (P ,Q). The remaining properties are straightforward to verify.

Next we establish a result which will be used to handle dihedral chords of type −1.

- Lemma 9.6 There does not exist a maximal dihedral chord of type −1.


Proof: Suppose (for a contradiction) that Θ is a maximal dihedral chord of type −1, let Λ be an associated octahedral chorus and note that our deﬁnitions imply that Θ is critical. It follows from the deﬁnition of dihedral chord that none of the square choruses contained in Λ can be full or empty. This eliminates all possibilities for Λ except those in Figure 18.

Figure 18: Two type −1 octahedral choruses

Both of the octahedral choruses in this ﬁgure have the property that they contain two square choruses which are simultaneously big and small. Therefore, we may choose a side ∆ of Θ so that ∆ is a fringed sequence of length relative to (P,Q) and its associated H square chorus Λ is both big and small (recall that by deﬁnition w◦(P) = w◦(Q) = 2|H|). Next apply Lemma 9.5 to choose a quotient (P ,Q ) of ∆. Now we have

w(∆) = 2( − 2)|H| + wˆH(Λ ) = 2( − 1)|H| = w(P ,Q )

so P and Q are systems of clones in ∆, and ∆• is a sequence. However, w◦(P ) = w◦(Q ) = 2|H|, but in both of the octahedral choruses in Figure 18, one of the three associated square choruses is a rank 4 chorus which has (up to reversing) three full sides and one empty side. It follows from this that there is a side ∆ of Θ for which either w(∆ ) or w(∆ ) is an odd multiple of |H|, and this contradicts the maximality of Θ.

Our next lemma uses similar logic to handle dihedral chords of type 0.

- Lemma 9.7 A trio is a dihedral chord of type 0 if and only if it is a a pure chord with split action.


Proof: First, we let Θ = (X,Y,Z) be a dihedral chord of type 0 and show that Θ is a pure chord with split action. A quick check of Figure 5 reveals that in the graph associated with an octahedral chorus of type 0, among the three squares which are associated with a square chorus, two have three full edges and one empty edge, while the other has one full edge and three empty edges. It follows that we may choose a side (X,Y ) of Θ which is a fringed sequence (i.e. w(X,Y ) < ∞) relative to (P,Q) and has associated square chorus with 3 full and one empty edge. We shall assume that ∆ = (X,Y ) and P, Q, H, and

are as given in equation 8. By assumption, each Pj (Qj) is the union of two H-orbits which we denote Pj0 and Pj1 (Q0j and Q1j). We may further assume that for every j ∈ J we have (Pji,Qkj) is empty if and only if i = 1 and k = 0 and (Pji,Qkj+ −1) is empty if and only if i = 0 and k = 1 as shown in Figure 19. Deﬁne P = {...,P00,P01,P10,P11,...} and Q = {...,Q00,Q10,Q01,Q11,...}, and observe that P and Q are systems of clones, and further (P ,Q ) is a sequence with split action. Let (A,B) be a cross of (X,Y ) associated with some point in Z, and assume (without loss) that A is ﬁnite. Now (A,B) is pure with respect to (P ,Q ) so by Lemma 9.1 there must be an interval I ⊆ P of (P ,Q ) so that A is the union of the blocks in I. Furthermore, it follows from the assumption that Θ has type 0 that |I| is odd. It then follows from Observation 9.3 that Θ is a pure chord with split action, as desired.

| |
|---|
| |


- Q0
- Q1


| |
|---|
| |


P11 P10

| |
|---|
| |


Q11

Q01

Figure 19: Adjusting a type 0 dihedral chord

Next suppose that Θ = (X,Y,Z) is a pure chord with split action and with clone partitions P,Q,R of X,Y,Z. Assume that w(X,Y ),w(Y,Z) < ∞ and suppose that Q = {Qj | j ∈ J} for J = Z or Z/nZ and that Qj and Qj+1 are consecutive for every j ∈ J. Note that d(P,Q) and d(Q,R) are odd, and d(P,R) is either odd or ∞ so we must have |J| ≥ 8. Now deﬁne Q = {Q1 ∪ Q2,Q3 ∪ Q4,...}, and note that Q is a system of imprimitivity. Furthermore, in the duet (P,Q) every P ∈ P is joined to an interval of odd length from Q. It follows that for every P ∈ P there is exactly one P ∈ P \ {P} so that P and P have the same neighbours in (P,Q ). Thus P ∪ P is a block of imprimitivity and we

- let P denote the corresponding system of imprimititivity. Deﬁne R on Z using blocks from R analogously. Note that Θ is maximal since it is a pure chord. Therefore, Θ is a maximal critical dihedral chord relative to P ,Q ,R and the square choruses associated to the fringed sequences on (X,Y ) and (Y,Z) both have the property that their associated square choruses have rank 4, no partial sides, and (up to reversing) just one empty side. It follows from this and a check of Figure 5 that Θ is a dihedral chord of type 0 relative to P ,Q ,R , as desired.


##### 9.3 Light Sides

The goal of this subsection is to prove our light side lemma for chords. In fact, we will prove a somewhat stronger result which applies not only to light sides, but more generally to sides of ﬁnite weight. We begin with an observation which follows from a check of Figures 5 and 13.

- Observation 9.8 For every octahedral chorus of type 0, 1, or 2, two of the square choruses it contains are big and the other is small.

Observation 9.8 is especially convenient since it forces the square choruses we use to be one of two extreme types. The next observation follows quite quickly from this.

- Observation 9.9 Let Θ be a dihedral chord and let ∆ be a side of Θ which is a fringed sequence with associated square chorus Λ.


- 1. If ∆ is short, then Λ is big.
- 2. If ∆ is long, then Λ is small.


Proof: For part 1, observe that if ∆ is short and Λ is small, then Lemma 9.5 would imply that ∆ is not connected, which contradicts the deﬁnition of dihedral chord. For part 2, note that if ∆ is long, then every side of Θ other than ∆ or its reverse will be a short fringed sequence, which by part 1 must have an associated square chorus which is big. Observation 9.8 then implies that Λ must be small.

The previous two observations also reveal why in the deﬁnition of dihedral chord, we could insist on the bound |J| ≥ 4 without loss. Were we to permit |J| = 3 for such a trio, it would have every side short, but then Observation 9.8 and Lemma 9.5 would force the trio to be disconnected.

- Lemma 9.10 Let Θ = (X,Y,Z;∼) be a critical G-trio and assume that Θ ≤ Θ∗ for a song Θ∗. Let ∆ be a side of Θ with w(∆) < ∞.


- 1. If Θ∗ is a pure chord, then ∆ is a near sequence.
- 2. If Θ∗ is a cyclic chord relative to P,Q,R on X,Y,Z then ∆ is a near sequence relative to (P,Q), and furthermore, w(P,Q) − w(∆) ≤ w◦(P) − δ(Θ).
- 3. Assume Θ∗ be a dihedral chord of type 1 or 2 relative to P,Q,R on X,Y,Z with consecutive shift S. Then there exist systems of imprimitivity P ,Q so that ∆ is a near sequence relative to (P ,Q ) with dihedral action and consecutive shift S, and furthermore, w(P ,Q ) − w(∆) ≤ w◦(P) − δ(Θ).


Proof: Let Θ∗ = (X,Y,Z;∼∗), assume that ∆ = (X,Y ;∼) and let ∆∗ = (X,Y ;∼∗). Then we have

w(∆∗) − w(∆) ≤ δ(Θ∗) − δ(Θ) (9) We now split into cases depending on Θ∗.

- Case 1: Θ∗ is a pure chord.

Let P, Q, R be the clone partitions of X, Y , Z in the trio Θ∗ and note that (P,Q;∼∗) is a sequence. Set k = w◦(P) = w◦(Q) = w◦(R) and note that k = δ(Θ∗). Now by equation

- 9 we have w(P,Q) = w(∆∗) < w(∆) + k, so ∆ is a near sequence relative to (P,Q).


- Case 2: Θ∗ is a cyclic chord.

Choose P ∈ P let {Q1,...,Q } = {Q ∈ Q | Q ∼∗ P}, and set k = w◦(P) = w◦(Q) = w◦(R). Since Θ∗ is a cyclic chord, we may assume (without loss) that (P,Q1;∼∗) is partial, and (P,Qi;∼∗) is full for 2 ≤ i ≤ . Now, (P,Q1;∼∗) is a side of a continuation of Θ∗ so we have δ(Θ∗) ≤ w(P,Q1;∼∗) (by Lemma 5.3). Combining this with Equation 9 then yields

w(P,Q;∼∗) − w(∆) = w(P,Q;∼∗) − w(∆∗) + w(∆∗) − w(∆) ≤ k − w(P1,Q1;∼∗) + δ(Θ∗) − δ(Θ) ≤ k − δ(Θ).

Since δ(Θ) > 0, it follows that ∆ is a near sequence relative to (P,Q), and since k = w◦(P) we also have w(P,Q) − w(∆) ≤ w◦(P) − δ(Θ).

- Case 3: Θ∗ is a dihedral chord.


Deﬁne H = G(P) = G(Q) = G(R) and note that S ∈ G/H. It follows from our assumptions that ∆∗ is a fringed sequence relative to (P,Q) with cyclic shift S and we let be its length and let Λ∗ be an associated H-square chorus. By assumption, Θ∗ must

have type 1 or 2 so we may choose a side Υ∗ of Λ∗ which is partial. Note that Lemma 8.4 implies δ(Θ∗) ≤ wH(Υ∗). If Λ∗ is big, then wˆ(Λ∗) ≥ 2|H| + wH(Υ∗) so we have

w(P,Q) − w(∆) = w(P,Q) − w(∆∗) + w(∆∗) − w(∆) ≤ w◦(P) − wH(Υ∗) + δ(Θ∗) − δ(Θ) ≤ w◦(P) − δ(Θ).

Since Observation 9.9 implies that ∆∗ is not long, and δ(Θ) > 0, the above equation implies that ∆ is a near sequence relative to (P,Q). Further, it inherits dihedral action and consecutive shift S from Θ∗. Otherwise Λ∗ is small, so wH(Υ∗) ≤ wˆ(Λ∗) < 2|H| and we may apply Lemma 9.5 to choose P ,Q . Now we have

w(P ,Q ) − w(∆) = w(P ,Q ) − w(∆∗) + w(∆∗) − w(∆) ≤ w◦(P ) − wH(Υ∗) + δ(Θ∗) − δ(Θ) ≤ w◦(P ) − δ(Θ).

Since ∆∗ is not short, ∆ is a near sequence relative to (P ,Q ). Furthermore, Lemma 9.5 implies that this near sequence has dihedral action and consecutive shift S.

##### 9.4 Crosses of Near Sequences

In this subsection we will establish a lemma which provides strong information about critical crosses in near sequences. We begin with an easy lemma.

- Lemma 9.11 Let (X,Y ) be a duet which is a near sequence relative to (P,Q), and let A ⊆ X be ﬁnite and critical. If A is pure with respect to P, then A and N(A) are unions of intervals of P and Q.

Proof: Observation 6.5 implies that N(A) is pure with respect to Q. Thus, A = {P ∈ P | P ⊆ A} is critical in (P,Q) and the result now follows from Lemma 9.1.

Let (X,Y ) be a duet, let P, Q be systems of imprimitivity on X and Y and assume that (P,Q) is a sequence. We say that a ﬁnite set A ⊆ X (B ⊆ Y ) is weakly fringed if the set of non-outer blocks of P (Q) forms a nontrivial interval, and every boundary block is an endpoint of this interval. An inﬁnite set is weakly fringed if its complement is weakly fringed. Finally, we say that a cross (A,B) is weakly fringed if both A and B are weakly fringed. We are now ready for the main lemma from this subsection.

- Lemma 9.12 Let ∆ = (X,Y ) be a G-duet which is a near sequence relative to (P,Q) and let (A,B) be a maximal critical cross of (X,Y ). If A is not contained in any block of P and B is not contained in any block of Q, then (A,B) is weakly fringed.


Proof: Deﬁne ∆ = (P,Q), set = d(P,Q), set k = w◦(P) = w◦(Q) and let H = G(P) = G(Q). Now suppose (for a contradiction) that the lemma fails for ∆, let (A,B) be a counterexample so that

α) δ(A,B) is maximum. β) The total number of boundary blocks in P and Q is minimum (subject to α). γ) min{w(A),w(B)} is minimum (subject to α, β).

Criteria α and β have a convenient behaviour in relation to puriﬁcation. Namely, if we modify (A,B) by purifying at any boundary block T ∈ P ∪ Q, the new cross will be superior to (A,B) with regard to α and β. To see this, let (A ,B ) and (A ,B ) be the weak puriﬁcation and the puriﬁcation of (A,B) at T. Now Theorem 5.8 implies δ(A ,B ) ≥ δ(A ,B ) ≥ δ(A,B). Since N(T) is pure (by Observation 6.5) it follows that (A ,B ) is superior to (A,B) with regard to α and β. Now either (A ,B ) = (A ,B ) or δ(A ,B ) >

- δ(A ,B ), and in either case (A ,B ) is superior to (A,B) with regard to α and β.


Note that by Lemma 9.11 there must be at least one boundary block, and then by maximality (and Observation 6.5) it follows that there must be a boundary block in both P and Q. Next we establish a couple of key claims.

- (i) Either there exists an interval I of P so that A ⊆ ∪P∈IP and |N∆ (I)| = |I| + − 1 or there exists an interval I of Q so that B ⊆ ∪Q∈I Q and |N∆ (I )| = |I| + − 1.


We shall assume (without loss) for the purposes of this claim that w(A) ≤ w(B). We may also assume w(B) < ∞ as otherwise the claim holds trivially. Choose a boundary block P0 ∈ P and let (A ,B ) be the cross obtained by purifying (A,B) at P0. Note that w(B) > 12w(∆) ≥ k so by Theorem 5.8 we must have B = ∅. If B is not contained in any block of Q, then we may apply the lemma inductively to (A ,B ), and we deduce that (A ,B ) is weakly fringed. But then there exists an interval I of P with A ⊆ ∪P∈IP and |N∆ (I)| = |I| + − 1, so the same holds for A, thus proving the claim. Thus, we may assume that B ⊆ Q0 for some Q0 ∈ Q. If Q0 is inner with respect to B, then I = P \ N∆ (Q0) satisﬁes the claim for A, so we may assume that Q0 is a boundary block of B. Next consider the cross (A ,B ) obtained from (A,B) by weakly purifying at P0 and then purifying at Q0. Since this cross is critical and B = Q0 it follows that every

- P ∈ P \ N∆ (Q0) must be non-outer in A . However, then there must exist at least two blocks of P which are non-outer with respect to A and are not incident with Q0. Now deﬁne (A ,B ) to be the cross obtained by purifying (A,B) at Q0. It follows from our assumptions that A is not contained in any block of P and B is not contained in any boundary block of Q. So, by induction (A ,B ) is weakly fringed, and since B ⊆ B it follows that there exists an interval I which satisﬁes the claim for B.


By claim (i) we may assume that there is an interval I of P so that A ⊆ ∪P∈IP and |N∆ (I)| = |I| + − 1. Furthermore, by possibly interchanging A,B we may assume that either w(A) ≤ w(B) or that P has no inner block (if w(B) < w(A) and P has an inner

block P, then I = Q \ N∆ (P) is an interval of ∆ and B ⊆ ∪Q∈I Q). By choosing I minimal, we may further assume that each endpoint of I is a non-outer block.

- (ii) Every block in I is either inner or boundary (with respect to A).


To see this, modify (A,B) to form (A ,B ) by weakly purifying at every boundary block in P. Then the set A is pure with respect to P and it is critical. If N(A ) = Y then Lemma 9.11 implies that A is the union of the blocks in I, and this gives the desired result. Otherwise w(∆) ≤  k and w(N(A)) = (|I|+ −1)k so again A must contain every block in I and we are ﬁnished.

Now it will be helpful to introduce coordinates. Assume that P = {Pj | j ∈ J} and

- Q = {Qj | j ∈ J} where J = Z or J = Z/nZ and Pi ∼ Qj if i ≤ j ≤ i+ −1. Assume that I = {P1,P2,...,Pm}, so the blocks Q1,Q2,...,Q +m−1 are distinct. Note that (ii) implies that A ∩ Pi = ∅ for 1 ≤ i ≤ m.


Next we consider the case that m ≥ 3. Since A ∩ P1 = ∅ the block Q1 must be either boundary or outer. First let us suppose that Q1 is boundary and let (A ,B ) be the cross obtained from (A,B) by purifying at Q1. Note that our assumptions imply A = A \ P1. Now, the lemma applies nontrivially to (A ,B ) and it follows that (A ,B ) is weakly fringed, so in particular ∪i=3 +m−2Qi ⊆ N(A ). It follows that blocks Q3,...Q +m−2 must be outer with respect to our original set B. Next we shall show that a similar conclusion holds under the assumption that Q1 is outer. In this case we let (A ,B ) be a maximal cross containing (A \ P1,B ∪ Q1). Note that by the maximality of (A,B) we must again have A = A \ P1. We claim that the cross (A ,B ) is superior to (A,B) with regard to our three optimization criteria. It is immediate that δ(A ,B ) ≥ δ(A,B) and this claim holds already if δ(A ,B ) > δ(A,B). Otherwise we must have that P1 is inner (which implies that

- w(A) ≤ w(B)) and B = B ∪ Q1 (which implies that (A ,B ) has the same total number of boundary blocks as (A,B)) so the cross (A ,B ) improves upon (A,B) with regard to our third optimization criteria. Therefore, the lemma applies nontrivially to (A ,B ) and


we conclude, as before, that ∪i=3 +m−2Qi ⊆ N(A ) so blocks Q3,...,Q +m−2 must be outer with respect to B. By a similar argument applied to the block Q +m−1 we conclude that blocks Q2,...,Q +m−3 must be outer with respect to B. But then B is weakly fringed, and by maximality A is weakly fringed.

Thus, we may now assume m = 2. The result holds trivially whenever one of P1 or P2 is inner, so we may assume P1 and P2 are boundary. Now we shall consider the case ≥ 3. Observe that if there exists g ∈ GP1 \ H then gQ1 = Q and gQ = Q1. Based on this we can “split” our duet according to the following procedure. Deﬁne the duet ∆1 = (X,Y ;∼1)

- by the rule that x ∈ X and y ∈ Y satisfy x ∼1 y if x ∼ y and the blocks Pi ∈ P with x ∈ Pi and Qj ∈ Q with y ∈ Qj satisfy i < j < i + − 1. We deﬁne the duet ∆2 = (X,Y ;∼2)
- by the rule that x ∈ X and y ∈ Y satisfy x ∼2 y if x ∼ y and x  ∼1 y. It follows from our earlier observation that ∆1 and ∆2 are G-duets and further w(∆) = w(∆1) + w(∆2). Since B is not weakly fringed, we may assume (by possibly interchanging P1 and P2 and reindexing) that there exists y ∈ B ∩ (∪i=2 −1Qi). Now set A1 = A ∩ P1 and observe that N(y) ∩ A1 = ∅ implies that w(∆1) = w(N∆1(y)) ≤ ( − 2)k − w(A1). Choose a point


- x ∈ A1 and note that w(∆2) = w(N∆2(x)) ≤ w(N(x) ∩ Q1) + k. Now let (A ,B ) be the cross obtained from (A,B) by weakly purifying at P2. Then A = A1 ∪ P2 is critical, but


w(N(A )) ≥  k + w(N(x) ∩ Q1) ≥ (k − 1) + w(∆2) ≥ k + w(A1) + w(∆1) + w(∆2)

= w(A ) + w(∆) which is a contradiction.

Finally, we are left with the case = m = 2. Here we may assume that P1, P2, and Q2 are boundary. Since the lemma we are establishing is unaﬀected by identifying clones, and splitting into clones, we may apply Proposition 3.3 to assume that G acts regularly on X and Y .

First consider the case that H = GP1. In this case ∆1 = (P1,Q1) and ∆2 = (P1,Q2) are H-duets and wG(∆) = wH(∆1)+wH(∆2). Set A1 = A∩P1 and choose x ∈ A1 and y ∈ B∩Q2. Since N(y)∩A1 = ∅ we have wH(∆2) = wH(N∆2(y)) ≤ k−wH(A1) = k−wG(A1). In addition wG(N∆(A1) ∩ Q1) ≥ wG(N∆(x) ∩ Q1) = wH(∆1). Now, let (A ,B ) be the cross obtained from (A,B) by purifying at P2. Then we have

wG(N(A )) = 2k + wG(N∆(A1) ∩ Q1) ≥ k + wG(A1) + wH(∆2) + wH(∆1)

= w(A ) + w(∆) and this contradicts the criticality of A .

Next consider the case that H = GP1. Since we are assuming that G acts regularly, it follows that every Pj (Qj) is the union of two H-orbits, which we denote by Pj0 and Pj1 (Q0j and Q1j). Furthermore, by indexing consistently, we may assume that for 0 ≤ i,j ≤ 1 there exist wij so that wH(Pmi ,Qjm) = wij. It then follows that wH(P10,Q12) = w10 and wH(P11,Q12) = w00 and wH(P20,Q12) = w01 and wH(P21,Q12) = w11 as shown in the ﬁgure.

Since B is not weakly fringed, we may assume without loss that B ∩ Q12 = ∅. Then by possibly reindexing, we may assume that w00+w10 ≥ w01+w11. Choose a point y ∈ B∩Q12, and for i = 1,2 let Ai1 = A ∩ P1i. Since Ai1 is disjoint from y we must have

w(A01) ≤ |H| − w10 and w(A11) ≤ |H| − w00 (10)

- P20
- P21


w11 w01

w00

w10

- P10
- P11


w11

w01

w10

w00

- Q01

- Q11

Q02

- Q12

Q03

- Q13




Furthermore, if Ai1 is nonempty then we have

w(N(Ai1) ∩ Qj1) ≥ wij. (11) Let (A ,B ) be the critical cross obtained from (A,B) by purifying at P2 (so w(A ) =

- 2|H| + w(A1)). First suppose that A01 = ∅ and A11 = ∅. In this case, averaging equation 11


gives us w(N(A1)∩Q1) ≥ 12(w00 +w01 +w10 +w11) ≥ w01 +w11. But then using equation

- 10 we ﬁnd


w(N(A )) ≥ 4|H| + w01 + w11 ≥ 2|H| + w(A1) + w00 + w10 + w01 + w11

= w(A) + w(∆)

which is a contradiction. Next suppose that A11 = ∅ (so A01 = ∅). In this case

w(N(A )) ≥ 4|H| + w00 + w01 ≥ 3|H| + w(A1) + w10 + w00 + w01 ≥ w(A ) + w(∆)

Finally, if A01 = ∅ (so A11 = ∅) we have

w(N(A )) ≥ 4|H| + w10 + w11 ≥ 3|H| + w(A1) + w00 + w10 + w11 ≥ w(A) + w(∆)

which is again a contradiction. This completes the proof.

- 9.5 Near Sequence Stability In this subsection we prove our stability lemma for near sequences.


- Lemma 9.13 (Near Sequence Stability) Let Θ be a maximal connected critical trio with a side which is a near sequence. Then Θ is a pure chord, a cyclic chord, or a dihedral chord of type 1, 2A, 2B, or 2C.


Proof: Let Θ = (X,Y,Z) and assume that ∆ = (X,Y ) is a near sequence relative to (P,Q). Assume further that P = {Pj | j ∈ J} and Q = {Qj | j ∈ J} for J = Z or Z/nZ where Pi ∼ Qj if i ≤ j ≤ i + − 1. Choose z ∈ Z and let (A,B) be the cross of (X,Y ) associated with z. It now follows from Lemma 9.12 that (A,B) is weakly fringed, so we may assume that the non-outer blocks of A form the interval {P1,...,Pm}. If (A,B) is pure with respect to (P,Q), then by maximality ∆• is a sequence. Since ∆• is a side of Θ• (by maximality), Lemma 9.4 completes the proof. It follows from this and the maximality of (A,B) that either P and Q each have exactly one boundary block, or they each have exactly two. Now, assume Θ is a G-trio and let H = G(P) = G(Q). We now split into cases depending on the action on (P,Q).

- Case 1: The sequence (P,Q) has cyclic action.

First suppose that A and B each have two boundary blocks. Then ∆1 = (P1,Q1) and ∆m = (Pm,Q +m−1) are both nontrivial H-duets and by maximality, we must have wG(∆) = w(∆1) + w(∆m) + ( − 2)|H|. Set A1 = A ∩ P1 and Am = A ∩ Pm and note that

- wG(A) = wG(A1) + wG(Am) + (m − 2)|H|. Then by Lemma 5.3, we have for i = 1 and i = m that wH(N∆i(Ai)) ≥ wH(∆i) + wH(Ai) − 21|H|. But then


wG(N(A)) = wH(N∆1(A1)) + wH(N∆2(A2)) + ( + m − 3)|H| ≥ wH(∆1) + wH(A1) + wH(∆m) + wH(Am) + ( + m − 4)|H|

= wG(A) + wG(∆)

which contradicts the criticality of A. It follows that A and B must each have one boundary block. Now it follows from maximality that Θ is a cyclic chord.

- Case 2: The sequence (P,Q) has dihedral action.


For every j ∈ J, let Rj be the set of all points in z for which the cross associated with z has nonempty intersection with all of the blocks Pj,Pj+1,...,Pj+m−1. By maximality, every z ∈ Rj will have ({z},Pj+1∪...∪Pj+m−2) full, and by the assumption that the action is dihedral (and the assumption (A,B) is impure), there must exist z ∈ Ri with ({z },Pj) not full and z ∈ Rj with ({z },Pj+m−1) not full. It follows from this and maximality that Θ is a dihedral chord relative to P, Q, and {Rj | j ∈ J}. By Theorems 4.5 and 4.6 we ﬁnd that the associated octahedral chorus must have type −1, 0, 1, 2A, 2B, or 2C, so Θ must have one of these types. Now by Lemmas 9.6 and 9.7, we deduce that either Θ is a pure chord, or a dihedral chord of type 1, 2A, 2B, or 2C.

- Case 3: The sequence (P,Q) has split action.


Any two consecutive blocks of P or Q form a block of imprimitivity, so it follows from the connectivity of Θ that neither A nor B can be contained in two consecutive blocks. Thus m ≥ 3 and since Q2 ∪ Q3 ... ∪ Q +m−2 ⊆ N(A) so we must have |J| ≥ + m ≥ + 3. Suppose (for a contradiction) that |J| = + 3. In this case m = 3 and we must have that

- P2 is inner, P1,P3 are boundary, and on the other side Q +3 is inner, and Q +2,Q +4 = Q1 boundary. Now deﬁne the H-duets ∆1 = (P1,Q1) and ∆2 = (P3,Q +2) and note that by this choice we must have wG(∆) ≤ wH(∆1)+wH(∆2)+( −2)|H|. Now setting A1 = A∩P1 and A3 = A ∩ P3 we have Q1  ⊆ N(A1) and Q +2  ⊆ N(A3) so Lemma 5.3 implies

wG(N(A)) = wH(N∆1(A1)) + wH(N∆2(A3)) + |H| ≥ wH(∆1) + wH(A1) + wH(∆2) + wH(A3) + ( − 1)|H| ≥ wG(A) + wG(∆).

which contradicts the criticality of A. Therefore, we must have |J| > + 3. Since |J| must be ∞ or even and is odd (by Lemma 9.3) we conclude |J| ≥ + 5 ≥ 8.

Note that N(P1 ∪ P2) = Q1 ∪ ... ∪ Q +1 and that (P1 ∪ P2,Q2i+1 ∪ Q2i+2) is full for

- 1 ≤ i < −21. Now we deﬁne the systems of imprimitivity P = {P1 ∪ P2,P3 ∪ P4,...} and


- Q = {Q1 ∪ Q2,Q3 ∪ Q4,...}. It follows from our assumptions that (X,Y ) is a fringed sequence relative to (P ,Q ). Now the argument from the previous case implies that Θ is either a pure chord or a dihedral chord of type 1, 2A, 2B, or 2C as desired.


#### 10 Near Graphs and Doubling Blocks

In this section we will prove a stability result for near true graphs and duets which have doubling blocks. As will be detailed shortly, these two classes of duets are very closely related.

##### 10.1 Preliminaries

Here we prove a sequence of three lemmas which will culminate with an important, albeit rather technical bound. To motivate the ﬁrst lemma in this sequence, recall that by Theorem 5.5 every partial duet ∆ = (X,Y ) has a nontrivially critical block of imprimitivity T which has the same deﬁciency as ∆. However, this lemma gives us no control over whether T is included in X or Y . Our ﬁrst lemma permits us to choose T ⊆ Y under certain additional assumptions.

- Lemma 10.1 Let ∆ = (X,Y ) be a ﬁnite partial duet of degree d. Assume that there is at most one integer m with d ≤ m < |Y | which is not relatively prime with |Y |, and if such a


number exists, it has the form m = (s − 1)t where st = |Y | and 3t ≤ 2(|Y | − d + 1). Then there exists a nontrivially critical block of imprimitivity Q ⊆ Y with δ(Q) = δ(∆).

Proof: By Theorem 5.5 we may choose a nontrivially critical block of imprimitivity P so that δ(P) = δ(∆) and we may assume P ⊆ X as otherwise we are done. Let P be the system of imprimitivity associated with P and set m = |N(P)|. Now w(N(P)) is given by

the equation w(N(P)) = mw◦(Y ) = m||YG||. However, by Proposition 5.6 we may choose ∈ Z so that w(N(P)) =  w(P) = ||P|G|. Since m ≥ d this gives us

d |Y |

m |Y |

w(N(P)) |G|

≤

=

=

< 1. (12)

|P|

If m and |Y | are relatively prime, then |P| ≥ |Y |, and choosing y ∈ Y we have δ({y}) = w(y) + w(∆) − w(N(y)) = w(y) ≥ w(P) ≥ w(P) + w(∆) − w(N(P)) = δ(P).

Thus, {y} is a block of imprimitivity which satisﬁes the lemma. Otherwise our assumptions imply m = (s − 1)t and |Y | = st. First suppose that |P| = s (so = s − 1). Since every

- P ∈ P satisﬁes w(N(P )) = |Gs| we have that Q = {Y \ N(P ) | P ∈ P} is a system of imprimitivity. Further, every Q ∈ Q has δ(Q) = δ(P) so it is a nontrivially critical block of maximum deﬁciency. Thus, we may now assume |P| = s. Equation 12 gives us


- |P| = |mY | = s−s1, which implies |P| ≥ 2s. Now by the assumption 3t ≤ 2(|Y | − d + 1) we ﬁnd


|G| 2s

δ(P) = w(P) + w(∆) − w(N(P)) ≤

+

d|G| st −

(s − 1)t|G| st ≤

|G| st

= w◦(Y ).

However, this again implies that a single point of Y is a nontrivially critical block of maximum deﬁciency.

- Lemma 10.2 Let ∆ = (X,Y ) be a duet with 4 ≤ |Y | ≤ 9 and |Y2| < d(X,Y ) < min{6,|Y |}. If S ⊆ Y satisﬁes |S| = 2 then one of the following holds


- 1. w(N(S)) ≥ w(∆) + w◦(Y )
- 2. |Y | = 6, S is a block of clones, and ∆• is a triangle.


Proof: Let d = d(X,Y ) and k = w◦(Y ) and observe that w(∆) = dk. We shall assume that the ﬁrst outcome does not hold, and prove that the second does. By the previous lemma, we may choose a nontrivially critical block of imprimitivity Q ⊆ Y so that δ(Q) = δ(∆) ≥ δ(S) = w(S) + w(∆) − w(N(S)) > k. Since each singleton from Y has deﬁciency k it follows that Q is a nontrivial block of imprimitivity. Furthermore, since w(N(Q)) is

a multiple of w(Q) strictly between w(Q) and w(Y ) = |G| (by Proposition 5.6) it must be that (|Y |,|Q|) is one of (6,2), (8,2), or (9,3). First suppose |Y | = 8 and |Q| = 2. In this case d = 5 so w(∆) = 5k and since w(N(Q)) is a multiple of 2k we must have w(N(Q)) = 6k. But then δ(Q) = k which is a contradiction. In the remaining cases,

- let Q be the system of imprimitivity associated with Q, and observe that (X,Q)• is a triangle. First suppose |Y | = 6 and |Q| = 2. In this case 4k = w(N(T)) ≥ w(∆) = dk so we must have d = 4. However, then w(N(Q)) = w(∆) so Q is a block of clones, and the second outcome is satisﬁed. In the remaining case, |Y | = 9 and |Q| = 3 and this implies d = 5. If S contains points in two distinct blocks of Q then each point has a neighbourhood of weight 5k and these neighbourhoods overlap in a set of weight at most


- 3k so w(S) ≥ 7k which contradicts our assumption. Otherwise, there exists Q ∈ Q with


- S ⊆ Q and we must have [S] = Q. Now either w(N(S)) = w(N(Q)) = 6k or by Theorem


- 5.13 w(N(S)) ≥ w(S)+w(∆)− 13w(Q) = 6k, and since 6k = w(∆)+w◦(Y ) this contradicts our assumption.


Now we will turn our attention to duets which have graphic quotients (the main subject of this section). We begin by introducing a useful bit of terminology.

Deﬁnition: Let ∆ = (X,Y ) be a G-duet and let V,E be systems of imprimitivity on X,Y

so that (V,E) is a graph. Let E ∈ E and assume E has ends V1,V2 ∈ V. We deﬁne the proﬁle of ∆ with respect to (V,E) to be {w(N∆(E) ∩ V1),w(N∆(E) ∩ V2)} (note that this is independent of the choice of E).

- Lemma 10.3 Let ∆ = (X,Y ) be a G-duet, and let V,E be systems of imprimitivity on X,Y . Assume that (V,E) is a graph of degree d ≥ 4 with proﬁle {w1,w2}, and assume


that V is critical. Let k = 21w◦(E). If w1 = w2 then 2k|wi for i = 1,2. Otherwise k|w1, and furthermore, whenever E1,E2 ∈ E are incident with V ∈ V and E1 = E2 one of the following holds

- 1. w(N∆(E1 ∪ E2) ∩ V ) ≥ min{dk,6k,w1 + k}
- 2. The incidence geometry (V,{E ∈ E | E ∼ V })• is a triangle and d = 6.


Proof: Our assumptions imply wG◦ (V) = dk and wG(V,E) = 2dk. Since every block of V is critical, we have

dk < wG(∆) ≤ wG(X,E) = w1 + w2 (13) First suppose that G acts arc-transitively on (V,E) (so w1 = w2), let V ∈ V, deﬁne

- Q = {E ∈ E | E ∼ V }, and let E1,E2 ∈ Q be distinct. Now (V,Q) is an H-duet for H = GV , and we have wH◦ (Q) = wH(E1) = 12wG(E1) = k. This gives us


w1 = wG(N(E1) ∩ V ) = wH(N(E1) ∩ V ) = wH(V,Q) = d(V,Q)wH◦ (Q) = d(V,Q)k

so w1 is a multiple of k. If w1 ≥ 6k then the ﬁrst outcome holds and we are ﬁnished. So, by equation 13 we may assume d ≤ 9. If d = 6 and (V,Q)• is a triangle, then the second outcome is satisﬁed. Otherwise the previous lemma gives

wG(N∆(E1 ∪ E2) ∩ V ) = wH(N(E1 ∪ E2) ∩ V ) ≥ wH(V,Q) + wH◦ (Q) = w1 + k and this completes the proof for this case.

In the remaining case G does not act arc-transitively on (V,E) which implies that d is even. Set H = GV as before, and observe that {E ∈ E | E ∼ V } consists of two H-orbits which we denote by Q1, Q2. For every E ∈ Qi we have wG(N∆(E) ∩ V ) =

- wH(N∆(E) ∩ V ) = wH(V,Qi) so we may asume (without loss) that wi = wH(V,Qi) for


i = 1,2. Furthermore, wH◦ (Qi) = wH(E) = wG(E) = 2k so wi = wH(V,Qi) = d(V,Qi)wH◦ is a multiple of 2k.

If w1 = w2 then we have nothing left to prove, so we may assume w1 = w2. Now let E1,E2 ∈ E be distinct with E1,E2 ∼ V , and suppose (without loss) that E1 ∈ Q1. Now we have wG(N∆(E1) ∩ V ) = wH(V,Q1) = w1 so we are ﬁnished unless w1 < 6k. It now follows from our assumptions and equation 13 that w1 = 4k, and d ∈ {4,6}. If d = 4 then wG(N∆(E1) ∩ V ) = dk and we are done. So, we may now assume d = 6, which implies

- |Q1| = |Q2| = 3. It then follows from w1 = w2 = 4k that both (V,Q1)• and (V,Q2)• are triangles. If E2 ∈ Q1 then V ⊆ N∆(E1 ∪ E2) so wG(N∆(E1 ∪ E2) ∩ V ) = dk and we are done. So, we may assume E2 ∈ Q2. Now for i = 1,2 let Pi be the partition of V into clones in the duet (V,Qi) (so |P1| = |P2| = 3), and for i = 1,2 choose Pi ∈ Pi to be the block of points not incident with Ei. Set T = P1 ∩ P2. If w(T) ≤ k then we have wG(N∆(E1 ∪ E2)) = 6k − w(T) ≥ 5k satisfying outcome 1. Otherwise, note that both P1 and P2 are systems of imprimitivity under the action of G, so T is also a block of imprimitivity. But then w(T) > k forces P1 = P2 = T. Thus, P1 = P2, and (V,{E ∈ E | E ∼ V })• is a triangle satisfying outcome 2.


##### 10.2 Star

The main goal of this subsection is to prove a lemma which will be used to handle crosses in duets with graphic quotients where all non-outer edges are incident with a common vertex (thus forming a star). However, we begin by introducing a new deﬁnition which will capture the duets we are interested in a form which is convenient to work with.

Deﬁnition: Let (X,Y ) be a duet and let V, E be systems of imprimitivity on X, Y . We say that (X,Y ) is a weak true graph (relative to (V,E)) if the following properties hold

- 1. (V,E) is a true graph.


- 2. V is critical.
- 3. If d(V,E) = 3 then the associated proﬁle is {w◦(V)}.


Our next lemma demonstrates that this deﬁnition captures the duets which will be of interest to us in this section.

- Lemma 10.4 If ∆ is a near true graph then it is a weak true graph. If ∆ is a connected duet with a doubling block, then either ∆ is a near polygon, or one of ∆ or its reverse is a weak true graph.

Proof: If ∆ = (X,Y ) is a near true graph relative to (V,E) then it follows from Observation 6.5 that ∆ is also a weak true graph relative to (V,E). Next suppose that ∆ is a connected duet with a doubling block, and let U be a doubling block with w(U) minimum. We may assume by possibly replacing (X,Y ) with its reverse that U ⊆ X and we let V denote the corresponding system of imprimitivity. Let ∆ = (V,Y ) and note that by our assumptions w(∆ ) = w(N∆ (U)) = w(N∆(U)) = 2w(U). Therefore every y ∈ Y has w(N∆ (y)) = 2w(U) so y must be incident with exactly two blocks of V. Let E be the partition of Y into clones from the duet ∆ . Then (V,E) is a simple connected graph, so it must either be a polygon (in which case we are ﬁnished) or a true graph. For the last part, suppose that (V,E) is a true graph with d(V,E) = 3 and let k = 21w◦(E) = 13w◦(V). Now let E ∈ E and observe that

3k < w(∆) ≤ w(N∆(E)) ≤ w(N∆ (E)) = 6k.

It follows from Proposition 5.6 that w(N∆(E)) must be a multiple of 2k. If w(N∆(E)) = 4k then E is a doubling block which contradicts our choice of V . Thus we must have w(N∆(E)) = 6k and this implies that property 3 holds, thus completing the proof.

- Lemma 10.5 Let ∆ = (X,Y ) be a weak true graph relative to (V,E), let d = d(V,E), and let (A,B) be a maximal critical cross of ∆ with at least two non-outer edges. If every non-outer edge is incident with the vertex V , then one of the following holds.


- 1. (A,B) is pure, E is critical, and d = 3.
- 2. [B] = Y , every y ∈ B satisﬁes w(N(y) ∩ V ) > 12w(N(y)), and there are no outer vertices in V \ {V }.


Proof: Let k = 12w◦(E) = d1w◦(V). Suppose (for a contradiction) that the lemma is false for ∆ and let (A,B) be a counterexample with w(B) maximum. Let E1,E2,...,Em be the non-outer edges and assume that Ei has ends V and Vi for 1 ≤ i ≤ m. Set Ai = A ∩ Vi and Bi = B ∩ Ei for 1 ≤ i ≤ m. We shall assume (without loss) that w(A1) ≤ w(Ai) for

every 1 ≤ i ≤ m. So in particular, if some Vi is outer, then V1 is outer. We proceed with a sequence of claims.

- (i) w(V1 \ A1) > 12dk. It follows from the assumption that V is critical that w(∆) > dk. So, it suﬃces to prove

that w(V1 \ A1) ≥ 12w(∆). Suppose (for a contradiction) that this fails. Then for every y ∈ Bi we have w(N(y) ∩ Vi) ≤ w(Vi \ Ai) ≤ w(V1 \ A1) < 12w(∆) = 21w(N(y)). But then setting T = {y ∈ Y | w(N(y) ∩ V ) > 21w(N(y))} we ﬁnd that T is a block of imprimitivity containing B, so [B] = Y and outcome 2 is satisﬁed.

- (ii) w(B1 ∪ Bi) > w(V1 \ A1) for every 2 ≤ i ≤ m.

Suppose that (ii) is violated and modify (A,B) to form (A ,B ) by purifying at every boundary Vh where h ∈ {2,...,m} \ {i}. Set B i = B ∩ Ei for 1 ≤ i ≤ m. By this modiﬁcation, every h ∈ {2,...,m} \ {i} satisﬁes either B h = ∅ or Vh ⊆ N(B h) so in either case w(N(B h) ∩ Vh) ≥ w(B h). By assumption we have w(N(B 1) ∩ V1) = w(V1 \ A1) ≥ w(B 1 ∪ B i), and obviously w(N(Bi)) ≥ w(∆). Combining these gives a contradiction to δ(B ) > 0.

- (iii) Every Vi is boundary. Also, if d = 3 then E is not critical.

Suppose (for a contradiction) that V1 is outer (so A1 = ∅). Then by (ii) we have 4k ≥ w(B1 ∪ B2) > w(V1 \ A1) = dk which implies d = 3. If m = 2 we must have N(B2) = N(E2) (as otherwise (A,B) is pure), but then w(B1∪B2) > 3k implies w(B2) > k, so [B2] = E2. Then Theorem 5.13 implies

w(N(B)) ≥ 3k + w(N(B2)) ≥ 2

1 3

k + w(B2) + w(∆) ≥ w(B) + w(∆)

which is a contradiction. If m = 3 and V2 is also outer then w(N(B)) ≥ 6k + w(N(B3)) ≥ w(B) + w(∆) which is a contradiction. Finally, if m = 3 and V2,V3 are boundary, then we may purify at V3 to obtain a critical cross where V1 is outer and V2 is boundary and this leads to a contradiction as before. It follows that every Vi is boundary. For the second part, note that if d = 3 and E is critical, then purifying at E1 gives a cross (A ,B ) which contradicts the choice of (A,B).

- (iv) Either d = 3 and there exists a critical system of imprimitivity E which is a reﬁnement of E with w◦(E ) = k, or 4 ≤ d ≤ 7 and setting E = E we have that E is critical.


It follows from (i) and (ii) that 4k ≥ w(B1 ∪ B2) > d2k so we must have d < 8. If d ≥ 4 then we may choose j ∈ {1,2} so that w(Bj) > k and if d = 3 we may choose j ∈ {1,2}

so that w(Bj) > 43k. Now, (iii) implies that every Vi is boundary, so by purifying at every Vi with i ∈ {1,2,...,m} \ {j} we ﬁnd that Bj is critical. Then by applying Theorem 5.13 we deduce that [Bj] is critical. So, for 4 ≤ d ≤ 7 we have E = E is critical and for d = 3 (applying (iii)) proves the existence of a critical system of imprimitivity E as claimed.

- (v) Bi ∈ E for every 1 ≤ i ≤ m.


Suppose (for a contradiction) that the above property fails for Bi. If 4 ≤ d ≤ 7 then Ei is a critical block of imprimitivity and purifying (A,B) at Ei results in a cross which contradicts our choice of (A,B). If d = 3 then property 3 in the deﬁnition of weak true graph together with (iii) imply that Bi = Ei. If Bi  ∈ E then there is a block T ∈ E which is boundary with respect to (A,B) and purifying (A,B) at T gives a cross which contradicts the choice of (A,B).

With this last claim in place, we are ready to complete the proof. Now, (V,E ) is a (not

necessarily simple) connected graph and d = d(V,E ) satisﬁes 4 ≤ d ≤ 7. Let k = 12w◦(E ), and note that B is pure with respect to E (by (v)) and note that d k = w◦(V) = dk. Now

let {w1,w2} be the proﬁle of (X,Y ) associated with (V,E ) and assume (without loss) that w1 = w(N(B1)) ∩ V1 = w(V1 \ A1). It follows from (i) that w1 > 21d k ≥ 2k and from (ii) that 4k = w(B1∪B2) > w1. It now follows from Lemma 10.3 that w1 = w2 = 3k and from w1 > 12d k that d ∈ {4,5}. Now applying Lemma 10.3 again gives us w(N(B)∩V ) ≥ 4k , but then we have

w(N(B)) ≥ 4k + 3k m ≥ 6k + 2k m = w(X,E ) + w(B) ≥ w(∆) + w(B) which contradicts the assumption that (A,B) is critical.

##### 10.3 Triangle

Our main interest in this subsection is crosses in weak graphs for which the only non-outer edges form a triangle. However, before treating these, we will to establish a couple lemmas.

- Lemma 10.6 Let ∆ = (X,Y ) be a weak true graph relative to (V,E) and assume that


d(V,E) = 3. If there exists a critical block S contained in a vertex V with w(S) = 21w(V ) and N(S) = N(V ), then w(N(S) ∩ E) = 21w(V ) for every E ∈ E incident with V . Proof: Let k = 12w◦(E) = 13w◦(V). Proposition 5.6 implies that w(N(S)) is a multiple of

- 3


- 2k and 3k < w(∆) ≤ w(N(S)) < w(N(V )) = 6k, so it must be that w(N(S)) = 92k. Let V


be the system of imprimitivity associated with S and observe that w(V ,Y ) = 92k so every y ∈ Y is incident with exactly three blocks of V . Now let E ∈ E, choose y ∈ E and deﬁne

- T = {y ∈ E | N(V ,Y )(y ) = N(V ,Y )(y)}. Since E is incident with exactly four blocks of V


and T is a block of imprimitivity contained in E we must have that 1 ≤ ww((ET)) ≤ 4 is an integer. However, by construction w(N(V ,Y )(T)) = 92k so by Proposition 5.6 w(T) must divide 92k and it follows that w(T) = 12k. Thus, the system of imprimitivity E associated with T has w◦(E ) = 12k and the result follows immediately from this.

- Lemma 10.7 Let ∆ = (X,Y ) be a weak true graph relative to (V,E) and let (A,B) be a maximal critical cross. If there are exactly two non-outer vertices, then (A,B) is pure.


Proof: Let d = d(V,E) and set k = 12w◦(E) = d1w◦(V). Suppose (for a contradiction) that the lemma is false for ∆, and let (A,B) be a counterexample for which w(A) is as large

- as possible. Let V1,V2 be the vertices which have nonempty intersection with A and set Ai = A ∩ Vi for i = 1,2. If V1,V2 are not incident with a common edge, then Theorem 5.9


gives us w(N∆(A)) = 2i=1 w(N(Ai)) ≥ 2i=1(w(Ai) + 12w(∆)) ≥ w(A) + w(∆) which is a contradiction. Thus V1,V2 are incident with a common edge E. If there exist non-outer edges E1 = E incident with V1 and E2 = E incident with V2, then purifying at V1 results in a cross which contradicts our choice of (A,B). Thus, we may assume (without loss) that every edge incident with V1 except possibly E is outer. It follows from this that

w(N(A)) ≥ w(N(A2)) + 2(d − 1)k. (14)

Note that V2 must not be inner since (A,B) is maximal and impure. If w(N(A2)) ≥ w(A2)+ w(∆)−13w(V ) then combining this with equation 14 we ﬁnd w(N(A)) ≥ 2(d−1)k+w(A2)+ w(∆) − 31dk ≥ w(A) + w(∆) giving us a contradiction. Thus it follows from Corollary 5.14 and the assumption that (A,B) is maximal that A2 is a critical block with w(A2) = d2k. If

- d ≥ 4 then equation 14 gives w(N(A)) ≥ 2(d−1)k+w(∆) ≥ 32dk+w(∆) ≥ w(A)+w(∆) and we have another contradiction. So, we may assume d = 3 and now by Lemma 10.6 we have


that w(N(A2)∩E ) = 32k for every E ∈ E with E ∼ V . Now V1 must be inner (otherwise purifying at V1 gives a better cross) so w(N(A)) = 9k = w(A)+w(N(A2)) ≥ w(A)+w(∆) which gives us a ﬁnal contradiction.

Consider a duet (X,Y ) which is a weak true graph relative to (V,E) and let (A,B) be a critical cross of (X,Y ) for which the non-outer edges form a triangle. It is certainly possible that (A,B) is pure with respect to (V,E) as we have already seen examples of critical crosses in graphs whose edges form a triangle. However, in addition to this, there are some examples of impure critical crosses for which the non-outer edges form a triangle, two of these are depicted in Figure 20. Both of these duets are weak true graphs, where the vertex partition V is indicated by the circles. In both of these cases each V ∈ V has the property that (V,N(V ))• is a triangle, and T is a critical block of imprimitivity for which N(T) is impure with respect to V. Fortunately, these are in a sense the only essentially new types of critical crosses of this form, as is proved in our main lemma from this subsection.

T

T

Figure 20: Critical blocks of imprimitivity in weak true graphs

- Lemma 10.8 Let ∆ = (X,Y ) be a weak true graph relative to (V,E), let d = d(V,E) and


k = 21w◦(E). If (A,B) is a maximal critical impure cross so that the non-outer edges form a triangle, then [B] = Y , there are no outer vertices, and one of the following holds.

- 1. d = 6 and E is critical and (V,{E ∈ E | E ∼ V })• is a triangle for every V ∈ V.
- 2. d = 3, there is a critical system of imprimitivity E which is a reﬁnement of E so that w◦(E ) = k, and (V,{E ∈ E | E ∼ V })• is a triangle for every V ∈ V.


We suppose (for a contradiction) that the lemma is false for ∆ and let (A,B) be a counterexample with w(B) as large as possible. Assume that the non-outer edges form a triangle with vertices V1,V2,V3 and edges E1,E2,E3 and assume that Ei is not incident with Vi for 1 ≤ i ≤ 3. Also, for 1 ≤ i ≤ 3, set Bi = B ∩ Ei and Ai = A ∩ Vi. We proceed with a sequence of claims.

- (i) w(Vi \ Ai) < w(B) for 1 ≤ i ≤ 3. To see this, choose u ∈ Bi and observe that

w(B) + w(∆) > w(N(B)) ≥ w(Vi \ Ai) + w(N(u)) = w(Vi \ Ai) + w(∆).

- (ii) At most one Vi with 1 ≤ i ≤ 3 is outer.


Suppose (for a contradiction) that A2 = A3 = ∅. Then since (A,B) is impure and maximal we must have E1 ⊆ B and V1 boundary. Now by weakly purifying at V1 we deduce that (X \ (V2 ∪ V3),E1) is critical which implies that w(∆) + w(E1) > w(V2 ∪ V3) so w(∆) > (2d − 2)k. Now choose x ∈ A1 and note that B2 ∪ B3 is disjoint from N(x) so w(B2 ∪ B3) < 2k. It follows that w(B) < 4k and then by (i) and the assumption A2 = ∅

we have dk < 4k, so d = 3. However, then (V,E) ∼= Tetrahedron (by Proposition 7.2) and there are exactly two non-outer vertices in (A,B) and this contradicts Lemma 10.7.

- (iii) If E is critical, then B = E1 ∪ E2 ∪ E3.

Suppose (for a contradiction) that (iii) fails. If Ei is boundary, then consider the cross (A ,B ) obtained by purifying (A,B) at Ei. It follows from our choice of counterexample that (A ,B ) is pure, and this implies that Vi is outer with respect to (A,B). So, by (ii) we may assume that V1 is outer, V2,V3 are boundary, E2,E3 are inner and E1 is boundary. If d = 3 then by the deﬁnition of weak true graph V3 ⊆ N(E2) and this is contradictory, so d ≥ 4. By purifying at E1 we have that (X \ (V1 ∪ V2 ∪ V3),E1 ∪ E2 ∪ E3) is critical. It follows that w(∆) + 6k > 3dk. Now choose a point x ∈ A2 and note that B3 must be disjoint from N(x) so 2k = w(B3) ≤ 2dk − w(∆) < (6 − d)k which is a contradiction.

- (iv) If E is not critical then Vi is boundary for 1 ≤ i ≤ 3.

By (ii) we may suppose (for a contradiction) that V1 is outer and V2,V3 are boundary. For i = 2,3 we may purify at Vi to obtain a critical cross, and it follows that Bi is critical. Then Theorem 5.13 implies that [Bi] is critical for i = 2,3. Since E is not critical, it must be that w(Bi) ≤ k for i = 2,3. If B1 is not critical then w(N(B)) ≥ w(V1) + w(N(B1)) ≥ w(B2 ∪ B3) + w(∆) + w(B1) which contradicts the criticality of B. Thus B1 is critical, and by Theorem 5.13 we have that [B1] is critical, and as before, this implies w(B1) ≤ k. However, then w(B) ≤ 3k and we have a contradiction to (i).

- (v) Either E is not critical and there exists a critical system of imprimitivity E reﬁning E with either w◦(E ) = 23k and d = 3 or with w◦(E ) = k and 3 ≤ d ≤ 5 or E = E is critical and 4 ≤ d ≤ 11.

Since w(∆) > dk, by considering a point y ∈ B1 we have that w(N(y)) > dk and this

implies max{w(V2 \ A2),w(V3 \ A3)} > 12dk and it then follows from (i) that w(B) > 12dk. Since w(B) ≤ 3w◦(E) = 6k it follows that d ≤ 11. If E is critical, then (iii) (and the

deﬁnition of weak true graph) imply that d ≥ 4 and there is nothing left to prove. So, we may assume E is not critical. By the above we may choose j ∈ {1,2,3} so that w(Bj) > 61dk. Now by (iv) Vj is boundary, so by purifying at Vj we deduce that Bj is critical. Then by Theorem 5.13 the block T = [Bj] is also critical. Since w(T) > 16dk and w(T) is a proper divisor of 2k, it must be that either 3 ≤ d ≤ 5 and w(T) = k or d = 3 and w(T) = 23k and then setting E to be the system of imprimitivity induced by T we have the desired conclusion.

- (vi) Bi ∈ E for 1 ≤ i ≤ 3.


If E = E then (iii) implies the result. Otherwise E is not critical, so by (iv) every Vi is boundary. If there is a block of E which is boundary, then purifying (A,B) at this block results in a cross which contradicts our choice of (A,B). So each Bi is a union of blocks of

- E . If Bi consists of more than one such block, then by purifying at Vi we deduce that Bi is critical, and then Theorem 5.13 implies that [Bi] is critical, but [Bi] = Ei and this is a contradiction.


With this last claim in place we are ready to complete the proof. Consider the graph

(V,E ), let d = d(V,E ) and set k = 12w◦(E ), and note that by our assumptions we must have 4 ≤ d ≤ 11. Let {w1,w2} be the proﬁle of (X,Y ) associated with (V,E ), and note that

w1 + w2 = w(X,E ) ≥ w(∆) > dk = d k . (15)

Next choose 1 ≤ i ≤ 3 so that Ei is not incident with an outer vertex and note that N(Bi) must intersect one end of Ei, say Vj, in a set of weight max{w1,w2}. Since Vj  ⊆ N(Bi) and (by (i)) w(N(Bi) ∩ Vj) < w(B) = 6k we have the following inequality.

max{w1,w2} < min{6k ,d k }. (16)

If w1 = w2, Lemma 10.3 implies that d is even, and w1,w2 are multiples of 2k . However, then equation 16 implies that {w1,w2} = {2k ,4k } and d ≥ 6, but this contradicts equation 15. So we must have w1 = w2, and then Lemma 10.3 implies that w1 is a multiple of k , so equations 15 and 16 force w1 ∈ {3k ,4k ,5k }. If w1 = 5k then we must have d ≥ 6, but then Lemma 10.3 implies that w(V1 \ A1) ≥ 6k ≥ w(B) which contradicts (i). Similarly, if w1 = 3k then we must have d ∈ {4,5}, and then Lemma 10.3 implies that w(V1\A1) = w(N(B2∪B3)∩V1) ≥ 4k and similarly for the other two vertices. However, then we have the contradiction w(N(B)) ≥ 12k ≥ 6k +6k = w(B)+w(X,E ) ≥ w(B)+w(∆). In the remaining case we have w1 = 4k and note that this implies d ≥ 5. If w(Vi\Ai) ≥ 5k for every 1 ≤ i ≤ 3 then w(N(B)) ≥ 15k > 6k +8k = w(B)+w(X,E ) ≥ w(B)+w(∆) which is contradictory. Therefore, by Lemma 10.3 we deduce that d = 6 and (V,{E ∈ E | E ∼ V })• is a triangle for every V ∈ V. It follows that whenever E,E ∈ E are incident with V ∈ V either V ⊆ N(E ∪ E ) or N(E) ∩ V = N(E ) ∩ V . Let us say that E and E are clones with respect to V if the latter condition is satisﬁed. Note that for every vertex V there are 6 incident edges in E and these are grouped into 3 doubletons of clones. If B1 and B2 are not clones with respect to V3, then V3 is outer and we have w(N(B)) ≥ w(V3) + 2 · 4k = 14k ≥ w(B) + w(∆) which is a contradiction. So, we ﬁnd that B1 and B2 are clones with respect to V3, and similarly B2,B3 and B1,B3 are clones with respect to their common endpoint. However, in this case B = B1 ∪B2 ∪B3 is a block of imprimitivity so conclusion 1 or 2 from the lemma holds.

##### 10.4 Stability

In this section we will prove our stability lemma for near graphs and duets with doubling blocks. This will follow easily once we have established the following.

- Lemma 10.9 Let ∆ = (X,Y ) be a weak true graph relative to (V,E) and let (A,B) be a maximal critical cross. If there are at least two non-outer vertices and at least two nonadjacent non-outer edges, then (A,B) is pure.


Proof: Let d = d(V,E), let k = 12w◦(E) = d1w◦(V), and note that dk < w(∆) since V is critical. We may assume w(∆) < 2dk as otherwise V is a block of clones, and the result is

immediate. Now suppose (for a contradiction) that the lemma is false for ∆ and choose a counterexample (A,B) subject to the following conditions.

α) δ(A,B) is maximum. β) The total number of boundary blocks in V is minimum (subject to α).

As was the case in the proof of Lemma 9.12, modifying (A,B) by purifying at a boundary vertex V results in a cross which is superior to (A,B) with regard to α, β. We now proceed with a sequence of claims.

- (i) There does not exist a boundary vertex V so that the cross obtained by purifying (A,B)


- at V is impure and has three non-outer edges which form a triangle.


Suppose (for a contradiction) that V is a vertex which violates (i), let E1,E2,E3 ∈ E be the edges in the resulting triangle, and note that the puriﬁcation of (A,B) at V must satisfy outcome 1 or 2 in Lemma 10.8.

First assume that outcome 1 is satisﬁed, and note that this implies w(∆) ≤ w(X,E) =

- 8k. In this case E is critical, and we now deﬁne (A ,B ) to be the critical cross obtained from (A,B) by weakly purifying at every boundary edge. If F1,...,F are the edges incident with V which are not outer with respect to (A,B) then B = E1 ∪ E2 ∪ E3 ∪ F1 ...,F so w(B ) = 2k(3 + ). Furthermore, the structure of (X,E) implies that for every V ∈ V with N(B ) ∩ V = ∅ we have w(N(B ) ∩ V ) ≥ 4k and further, w(N(B ) ∩ V ) = 6k if B contains at least three edges incident with V . However, this contradicts δ(B ) > 0.


Next suppose that outcome 2 in Lemma 10.8 holds and let E be the corresponding critical system of imprimitivity on Y . Now d = 3, so Proposition 7.2 implies that the graph (V,E) is isomorphic to Tetrahedron. It then follows from Lemma 10.8 and our assumptions that there are no outer vertices with respect to (A,B). Choose a vertex V ∈ V \ {V } so that the edge incident with V and V is not outer, and note that V must

then be incident with at least three non-outer blocks of E . Now consider modifying (A,B) by repeatedly purifying at blocks of E . It follows from our assumptions that at some point in this process the vertex V will become outer. However, if we stop this process as soon as the ﬁrst outer vertex is encountered, the resulting cross contradicts the choice of (A,B).

- (ii) There exists a critical cross (A ,B ) which is pure with respect to (V,E) and has at least two inner vertices and at least two outer vertices.

If (A,B) has at least two outer vertices, then let (A ,B ) be obtained by repeatedly weakly purifying (A,B) at every boundary vertex. It follows immediately that (A ,B ) has no boundary vertices, and from the maximality of (A,B) that (A ,B ) it has no boundary edges, so it satisﬁes (ii). So, we may now assume there is at most one outer vertex with respect to (A,B). Then, by our assumptions, we may choose non-outer non-adjacent edges E,E ∈ E so that if an outer vertex exists, it is an endpoint of E. If there exists a boundary vertex not incident with E or E then purifying at this vertex gives a cross which contradicts (A,B). So, letting V1,V2 be the ends of E and V 1,V 2 be the ends of E we have that every non-outer edge has both ends in {V1,V2,V 1,V 2}.

If E,E are the only non-outer edges, then by Corollary 5.10 we have w(N(B)) = w(N(B∩E))+w(N(B∩E )) ≥ w(B)+w(∆) which is contradictory. Thus, we may assume that there is a non-outer edge F with ends V1,V 1. Let (A ,B ) be the cross obtained from (A,B) by purifying at V 2. If (A ,B ) is pure, then (ii) is satisﬁed, so we may assume it is not. It then follows from (i) that the non-outer edges in (A ,B ) are precisely E and F. Now by applying Lemma 10.5 we ﬁnd that V2 is boundary, and every y ∈ F satisﬁes w(N(y) ∩ V 1) < w(N(y) ∩ V1). In this case we may purify the original cross (A,B) at the vertex V2 to obtain a new cross (A ,B ). It follows from a similar argument that either (A ,B ) is pure (so we are done) or every y ∈ F satisﬁes w(N(y) ∩ V1) < w(N(y) ∩ V 1). However, this last possibility is contradictory, and this completes the proof of (ii).

- (iii) ∆ is a near true graph relative to (V,E).

By (ii) we may choose a pure critical cross (A ,B ) with at least two inner and two outer vertices. If we let A∗ be the set of inner vertices with respect to (A ,B ) and B∗ be the set of inner edges with respect to (A ,B ), then (A∗,B∗) is a critical cross in (V,E). Now using Corollary 7.4 we have

w(V,E) − w(X,Y ) = δ(A∗,B∗) − δ(A ,B ) < δ(A∗) ≤ w◦(E) and this completes the proof.

- (iv) The graph (V,E) is not isomorphic to Tetrahedron.


Suppose (iv) fails and choose two nonadjacent non-outer edges E,E . It follows from

- Lemma 10.7 that there is at most one outer vertex, so E and E must both be boundary, and we may assume that if an outer vertex exists it is incident with E. However, then purifying at E yields a maximal impure cross with exactly two non-outer vertices, thus contradicting Lemma 10.7.


- (v) Every boundary edge is incident with every boundary vertex.

Suppose (for a contradiction) that V is a boundary vertex and E a boundary edge and V  ∼ E. Now consider the cross (A ,B ) obtained from (A,B) by purifying at E. By construction (A ,B ) is not pure, and by Observation 6.5 it has fewer boundary vertices than (A,B), so it must be that V is the only non-outer vertex of (A ,B ) (otherwise (A ,B ) contradicts the choice of (A,B)). It follows from (iv) that |V| ≥ 5 and thus there must exist an edge E not incident with V and not adjacent with E. But then the cross obtained from (A,B) by purifying at V is a counterexample which contradicts our choice of (A,B).

- (vi) There is exactly one boundary vertex V (so every boundary edge is incident with V ).

If (vi) fails, then by (v) there must exist a single boundary edge E so that the boundary vertices are precisely the two ends V1,V2 of E. Now every edge incident with V1 or V2 other than E must be outer (were E to be an inner edge incident with Vi for i = 1,2 Observation 6.5 would imply that Vi is outer). But then N(B∩E)∩N(B\E) = ∅ and by Corollary 5.10 we ﬁnd that w(N(B)) = w(N(B ∩ E)) + w(N(B \ E)) ≥ w(B) + w(∆) which contradicts the assumption that B is critical.

- (vii) There are at least three inner vertices.


It follows from (vi) and Lemma 10.7 that there are at least two inner vertices. Suppose (for a contradiction) that there are exactly two inner vertices. Let (A ,B ) be the cross obtained by weakly purifying at the unique boundary vertex V and let (A∗,B∗) denote the cross of (V,E) obtained by taking A∗ to be the set of inner vertices and B∗ to be the inner edges with respect to (A ,B ). Now, as before, we have that (A∗,B∗) is critical, so by (iv) and Theorem 7.3 it must be that either (V,E) has degree 3 and the three non-outer vertices form a path, or (V,E) has degree 4 or 5 and the three non-outer vertices induce a triangle. A quick check reveals that the following inequality holds in all of these cases.

w(N(A) \ N(V )) ≥ w(A \ V ) + 21dk However, we must have N(A ∩ V ) = N(V ) so Corollary 5.14 implies w(A ∩ V ) ≥ w(∆) +

- w(A ∩ V ) − 21dk and combining this with the above inequality yields a contradiction.


With this ﬁnal claim in place, we can complete the proof. There are at least three inner vertices by (vii), and since there are two nonadjacent non-outer edges, (vi) implies that

we must also have at least three outer vertices. Consider the cross (A1,B1) obtained by purifying at the unique boundary vertex and a cross (A2,B2) obtained by purifying at any boundary edge, and note that by (iii) and Observation 6.5, both of these crosses are pure. Now let A∗1 denote the set of inner vertices with respect to (A1,B1) and A∗2 denote the set of inner vertices with respect to A2. As in the previous cases, we have that A∗1 and A∗2 are critical in the duet (V,E). Furthermore, by construction A∗2 = A∗1 \ {V }. By applying Theorem 7.3 we deduce that (V,E) ∼= Cube and the set of non-outer vertices is the vertex set of a cycle of length four. Since A is critical the set A = A ∩ V satisﬁes

w(N(A )) + 10k ≤ w(N(A)) < w(A) + w(∆) = 9k + w(A ) + w(∆). Since N(A ) = N(V ) it then follows from Corollary 5.14 and the maximality of (A,B) that A is a critical block of imprimitivity with w(A ) = 23k. However, then w(A) = 212 k and

- Lemma 10.6 implies that w(N(A)) = 312 k and w(∆) ≤ w(N(A )) = 29k and this gives us a ﬁnal contradiction, thus completing the proof.


- Lemma 10.10 (Near Graph and Doubling Block Stability) Let Θ be a maximal connected critical trio, and let ∆ be a side of Θ.

- 1. If ∆ is a near true graph, then Θ is a video.
- 2. If ∆ has a critical doubling block, then either Θ is a video or ∆ is a near polygon.


Proof: Let Θ = (X,Y,Z) and suppose that ∆ = (X,Y ). In light of Lemma 10.4, to complete the proof it suﬃces to show that Θ is a video under the assumption that ∆ is a weak true graph. Choose systems of imprimitivity V, E so that ∆ is a weak true graph relative to (V,E). Let (A,B) be the cross of ∆ associated with some point in Z and note that by the connectivity of Θ this cross must have at least two non-outer vertices and at least two non-outer edges. If all non-outer edges are pairwise incident, then it follows from

- Lemma 10.5 or 10.8 (and the connectivity of Θ) that (A,B) is pure. Otherwise, Lemma


- 10.9 shows that (A,B) is pure. It now follows from the maximality of Θ that V and E are systems of clones and that ∆• is a true graph. Then Lemma 7.10 implies that Θ is a video,

- as desired.


11 Clips and Near Clips

In this section we establish stability lemmas for clips and near clips.

- 11.1 Crosses of Clips In this subsection we will classify critical crosses of clips.




- Lemma 11.1 Let Γ = (V,E) be an arc-transitive cubic graph and let {A,A} be a partition of V so that |A| ≥ 2 and |A| ≥ 3 and at least one of A,A is ﬁnite. Then one of the following holds.


- 1. There are at least 9 two edge paths with one end in A and with middle vertex in A.

- 2. A consists of two adjacent vertices.
- 3. A is the vertex set of a two edge path.

- 4. Γ ∼= Cube and A,A are vertex sets of cycles of length 4.


Proof: Suppose (for a contradiction) that the lemma is false and choose a counterexample {A,A} for which c(A) is minimum. The lemma is straightforward to verify when |A| = 2 or |A| = 3 so we may assume |A| ≥ 3 and |A| ≥ 4. We deﬁne a two edge path to be interesting if it has one end in A and middle vertex in A. Now, for 0 ≤ i ≤ 3 let Ai = {x ∈ A : |∂(x) ∩ ∂(A)| = i} and let Ai = {y ∈ A : |∂(y) ∩ ∂(A)| = i}.

First suppose that there exists a vertex v ∈ A3 ∪ A3, and modify {A,A} by moving this vertex to the other part of the partition. This operation does not create any new interesting paths, and reduces c(A), thus contradicting the choice of {A,A}. Next suppose there exists a vertex v ∈ A2 ∪ A2 and modify {A,A} by moving this vertex to the other side of the partition. This operation causes at least two paths to change from interesting to non-interesting, and at most two paths to change from non-interesting to interesting (here we use A3 = A3 = ∅), so again the resulting partition contradicts our choice. Thus, we may now assume A3 = A3 = A2 = A2 = ∅. If c(X) ≥ 5 then there are at least 10 interesting paths, so the ﬁrst outcome holds. Otherwise, it follows from Lemma 7.3 that outcome 4 is satisﬁed.

- Lemma 11.2 Let Γ be a graphic duet with degree 3 and let (A,B) be a critical cross of Γ(V,P3) with |A|,|B| ≥ 2. Then (A,B) is maximal and one of the following holds


- 1. A consists of two adjacent vertices.
- 2. Γ is isomorphic to Cube, and A consists of the four vertices of a face, so [B] = P3(Γ).


Proof: Let V = V (Γ) and P = P3(Γ), so (V,P) = Γ(V,P3), and let k = w◦(P) = 31w(V ).

Suppose ﬁrst that A is ﬁnite, let D ⊆ P be the set of all two edge paths with middle vertex in A, and let D = N(A) \ D. Now we have

w(D) + k|D | = w(D) + w(D ) = w(N(A)) < w(A) + w(∆) = w(D) + 9k.

Thus, Lemma 11.1 implies that either A consists of two adjacent vertices, or Γ is the cube and A is the vertex set of a cycle of length four. In either case the only way for (A,B) to be critical is for it to be maximal, and this completes the proof.

Next suppose that A is inﬁnite, let A = V \ A, and let B be the set of all two edge paths with middle vertex in A but at least one endpoint in A. Now B ∪ B is contained in the set of two edge-paths with middle vertex in A so we have

k|B | + w(B) = w(B ) + w(B) ≤ w(A) < w(B) + w(∆) = w(B) + 9k, but this contradicts the assumption A is inﬁnite and Lemma 11.1.

For reference purposes, let record some parameters of the exceptional clips. In the chart below, we have deﬁned k = w

◦(X)

◦(Y ) d(Y,X).

d(X,Y ) = w

|(X,Y )|w◦(X)<br><br>|w◦(Y )|w(X,Y )|
|---|---|---|---|
|K5(E,C3)|3k<br><br>|3k|21k|
|K6(E,C3)<br><br>|4k<br><br>|3k<br><br>|48k|
|Petersen(E,C5)|4k<br><br>|5k|40k|
|Dodecahedron(V,F)<br><br>|3k|5k|45k|


Table 1: Weights of some elements in exceptional videos

- Lemma 11.3 Let (A,B) be a critical cross of one of K5(E,C3), Petersen(E,C5), or K6(E,C3). If |A|,|B| ≥ 2 then (A,B) is maximal and A = ∂(v) for some vertex v.


Proof: Suppose (for a contradiction) that the lemma fails, let V , E be the vertex and edge sets of the graph, and let (A,B) be a counterexample for which |B| is minimum. The lemma is straightforward to verify whenever |B| = 2, and whenever A ⊆ ∂(v) for some vertex v so we may further assume that |B| ≥ 3 and that A contains two non-adjacent edges. We now split into cases depending upon the input graph.

- Case 1: K5(E,C3)

In this case a cross (A ,B ) is critical if and only if |A | + |B | > 7. If there is an edge e ∈ E\A which is incident with just one triangle q ∈ B, then (A∪{e},B\{q}) is a superior cross. So, we may assume no such edge e exists. Since A contains two non-adjacent edges, the graph (V,E \ A) must then be a subgraph of K2,2,1 (as depicted on the left in Figure 21) which contains at least two triangles through each edge. However no such graph exists.

- Case 2: ∆ = K6(E,C3)


K2,2,1 K2,2,2 K3,2,1 Petersen − 2

Figure 21: Subgraphs of K5, K6, and Petersen

In this case a cross (A ,B ) is critical if and only if 4|A | + 3|B | > 48. It follows from the minimality of |B| that there does not exist an edge e ∈ E \ A which is incident with just one triangle in B. The result is straightforward to verify when (V,E \ A) contains a K4 subgraph (so A is contained in ∂(u) ∪ ∂(v) for some u,v ∈ V ) so we may assume this is not the case. It follows from this that A must either contain a three edge matching, or two vertex disjoint subgraphs one consisting of a triangle, the other consisting of an edge. Therefore, (V,E \ A) must be a subgraph of one of the two graphs in the middle of Figure 21 which contains at least two triangles through every edge. There is only one such graph, Octahedron, and it does not give a critical cross.

- Case 3: Petersen(E,C5)


In this case a cross (A ,B ) is critical if and only if 4|A | + 5|B | > 40. It follows from the minimality of |B| that there must not exist a pair of edges e,e ∈ E \A incident with a pentagon q ∈ B with the property that no other pentagon in B is incident with either e or e . Since A contains two non-adjacent edges, the graph (V,E \ A) must be a subgraph of one of the graphs on the right in Figure 21 containing no pair of edges e,e as described. There is only one such graph (obtained from the rightmost graph in the ﬁgure by deleting the two vertices of degree two on the bottom), and it is straightforward to check that does not yield a critical cross.

- Lemma 11.4 If (A,B) is a critical cross of Dodecahedron(V,F) and |A|,|B| ≥ 2, then (A,B) is maximal and either A consists of two adjacent vertices, or B consists of two adjacent faces.


Proof: Let V,F be the vertex and face sets of Dodecahedron, and note that a cross (A ,B ) is critical if and only if 3|A | + 5|B | > 45. We suppose (for a contradiction) that the lemma is false, and choose a counterexample (A,B) with δ(A,B) maximum. The lemma is straightforward to verify when |A| ≤ 4 and when |B| ≤ 2 so we may further assume |A| ≥ 5 and |B| ≥ 3. Now consider a face f ∈ B and let f1,...,f5 be the faces adjacent to f so that fi and fi+1 are adjacent for every 1 ≤ i ≤ 5 (working modulo 5). If there are two vertices incident with f which are not incident with any other member of B, then

adding these to A and removing f from B results in a superior cross. Therefore, we may assume (without loss) that f1,f3 ∈ B. Now, there is a unique vertex v incident with f2 but not incident with either f1 or f3. If f2  ∈ B then we may obtain a superior cross by adding f2 to B and removing v from A. Thus f1,f2,f3 ∈ B. If f4,f5  ∈ B then we may obtain a superior cross by adding f4,f5 to B and removing any vertex of A incident with one of these. Thus, f1,...,f5 ∈ B, but repeating this argument results in an apparent contradiction.

##### 11.2 Clip Stability

In the previous subsection we determined all critical crosses of clips. To complete our stability lemma for clips, we will need to understand the images of these critical crosses under the group action. To help appreciate a subtlety here, consider a G-duet given by K6(E,C3). By assumption, G acts transitively on E(K6) and on C3(K6), and this action preserves incidence. However, it is not obvious, a priori, that G is acting on the graph K6 (i.e. acting on the vertex and edge sets preserving incidence). Our ﬁrst task will be to show that for each of our clips, the group G is indeed acting on the appropriate graph. Once we have this action in hand, it will be straightforward to determine the image of the crosses of interest under the action of G.

- Lemma 11.5 (Clip Stability) Let Θ be a connected critical trio. If Θ has a side which is a clip, then Θ is a video.


Proof: Assume Θ = (Z,X,Y ) is a G-trio, and let ∆ = (X,Y ) be a side of Θ which is a clip. Let z ∈ Z and let (A,B) be the cross of (X,Y ) associated with z. Now we split into cases depending on the possibilities for ∆.

- Case 1: ∆ ∼= Γ(V,P3) for a graphic duet Γ of degree 3.

Deﬁne two vertices of Γ to be adjacent if they are both incident with four members of Γ(P3). These adjacencies correspond to E(Γ), and it follows that G is acting on the graph Γ. It then follows from the assumption that G acts transitively on P3(Γ) that G is also transitive on E(Γ). Now by the connectivity of Θ and Lemma 11.2 we ﬁnd that A consists of two adjacent vertices and B = Y \ N(A). Since our action is edge-transitive, we deduce that Θ• ∼= Γ : E ∼ V ∼ P3.

- Case 2: ∆ is isomorphic to one of K5(E,C3), K6(E,C3), or Petersen(E,C5).


For K5 and K6 we deﬁne two edges to be adjacent if there is a triangle incident with both edges, and for Petersen we deﬁne two edges to be adjacent if there are four pentagons

incident with both edges. Maximum size sets of pairwise adjacent edges correspond to vertices, so G is indeed acting on our graph. Furthermore, it follows from the assumption that the action of G is edge-transitive and the fact that our graph is not bipartite, that this action is vertex transitive. It follows from the connectivity of Θ and Lemma 11.3 that A = ∂(v) for some vertex, and we must have B = Y \ N(A) in order to be critical. It now follows that Θ• is isomorphic to one of K5 : V ∼ E ∼ C3 or K6 : V ∼ E ∼ C3 or Petersen : V ∼ E ∼ C5 as desired.

- Case 3: ∆ ∼= Dodecahedron(V,F).


Deﬁne two vertices to be adjacent if there are two faces incident with both vertices. These adjacencies correspond precisely to E(Dodecahedron) so G is acting on Dodecahedron, as desired. Furthermore, G acts transitively on the edge set (and also their duals). Lemma 11.4 implies that (A,B) is maximal and either A consists of two adjacent vertices or B consists of two adjacent faces. It follows that Θ• must be isomorphic to a trio equivalent to Dodecahedron : E ∼ F ∼ V or Dodecahedron: F ∼ V ∼ E.

- 11.3 Near Clip Stability In this subsection we prove a stability lemma for near clips.


- Lemma 11.6 Let (X,Y ) be a duet which is near Γ(V,P3) for a graphic duet Γ of degree


- 3. If (A,B) is a maximal critical cross of (X,Y ) with at least two non-outer vertices and


- at least two non-outer paths, then (A,B) is pure.


Proof: Choose block partitions V of X and P of Y so that (X,Y ) is near Γ(V,P3) relative to (V,P) and let (A,B) be a counterexample to the lemma chosen so that

α) δ(A,B) is maximum. β) The total number of boundary blocks in V and P is minimum (subject to α).

As in the previous instances, purifying (A,B) at any boundary block results in a cross which will be superior to (A,B) with regard to the above criteria. Let k = w◦(P) = 13w◦(V) and note that 8k < w(X,Y ) ≤ 9k since P is critical. We proceed with a sequence of numbered claims.

- (i) There do not exist V1,V2 ∈ V with A ⊆ V1 ∪ V2.


Suppose (for a contradiction) that (i) is violated and let Ai = A ∩ Vi for i = 1,2. If there is a boundary path not incident with V1 and a boundary path not incident with V2

then by purifying at V1 or V2 yields a cross which contradicts our choice of (A,B). Thus we may assume without loss that every boundary path is incident with V1. Now by Corollary

- 5.14 we have


w(N(A)) ≥ 5k + w(N(A2)) ≥ 27k + w(∆) + w(A2) ≥ w(A) + w(∆) which contradicts the assumption that A is critical.

- (ii) We have w(B) < 4k.

Suppose w(B) ≥ 4k and let (A ,B ) be the cross obtained from (A,B) by purifying at a boundary vertex V . It follows from Theorem 5.8 that w(B ) > k so B is not contained in a single member of P. It then follows from our choice of (A,B) that (A ,B ) is pure, and then from (i) that Γ ∼= Cube and B corresponds to the set of paths contained in a face. Now let (A ,B ) be the weak puriﬁcation of (A,B) at the vertex V . Since k ≥ δ(A ,B ) ≥ δ(A ,B ) > 0 it must be that 12k = w(A ) ≤ w(A ) + k ≤ w(A) + 4k. However, now we may modify (A,B) by purifying at a boundary path to obtain a cross (A ,B ) for which

- w(A ) ≥ w(A) − k ≥ 7k. It follows from our choice of (A,B) that (A ,B ) is pure, but

- A is not contained in two vertices, and this gives us a contradiction.

(iii) We have w(A) ≥ 4k

Otherwise, w(A)+w(B)+w(∆) ≤ 17k ≤ 3k|V| = w(X) which contradicts the assumption (A,B) is critical.

Now consider the cross (A ,B ) obtained from (A,B) by purifying at a boundary path

- P. It follows from (iii) and our choice of (A,B) that (A ,B ) is pure. If A consists of two adjacent vertices, then by Theorem 5.8 it must be that w(A) ≤ 7k but then 3k|V| =


w(X) < w(A) + w(B) + w(∆) ≤ 20k so |V| ≤ 6 which implies that Γ ∼= K3,3 and B

corresponds to the set of four paths contained in a cycle of length four. If A does not consist of two adjacent vertices, then by Lemma 11.2 we ﬁnd that Γ ∼= Cube and again

- B corresponds to the set of four paths contained in a cycle of length four. So, B has the same structure in both cases, and we have w(B ) = 4k. Next choose x ∈ A \ A and choose V ∈ V with x ∈ V . Now w(N(V ) ∩ B ) = 3k so it follows from the assumption that w(P,Q) − w(X,Y ) < w◦(P) = k that w(N(x) ∩ B ) > 2k. But then we must have


- w(B \ B) ≥ 2k. However, Theorem 5.8 implies w(A \ A ) < k so we have k < w(B \ B) − w(A \ A ) = δ(A ,B ) − δ(A,B) ≤ k − δ(A,B)




which is a contradiction.

Next we prove a general stability lemma which will be used to handle duets which are near one of K5(E,C3), K6(E,C3) or Petersen(E,C5).

- Lemma 11.7 Let (X,Y ) be a duet which is near ∆ relative to (P,Q), and assume that every critical cross (A∗,B∗) of (P,Q) with |A∗|,|B∗| ≥ 2 satisﬁes w(A∗) = a and w(B∗) = b and δ(A∗,B∗) = t. If w(X,Y ) ≥ 2w◦(P)+2w◦(Q) and a ≥ w◦(P)+3t and b ≥ w◦(Q)+3t, then every maximal critical cross (A,B) of (X,Y ) satisﬁes one of:


- 1. A is contained in a block of P.
- 2. B is contained in a block of Q.
- 3. (A,B) is pure.


Proof: Suppose (for a contradiction) that the lemma is false for (X,Y ) and choose a counterexample (A,B) so that

α) δ(A,B) is maximum. β) The total number of boundary blocks in P and Q is minimum (subject to α).

First we claim that there do not exist boundary blocks P ∈ P and Q ∈ Q so that purifying at P yields a cross (A ,B ) for which B is contained in a block of Q and purifying at Q yields a cross (A ,B ) for which A is contained in a block of P. To verify this, suppose otherwise, and note that Theorem 5.8 implies w(A) < w(A ) + w◦(Q) ≤ w◦(P) + w◦(Q) and w(B) < w(B ) + w◦(P) ≤ w◦(P) + w◦(Q). However, then 0 < δ(A,B) = w(A) +

- w(B) − w(X,Y ) ≤ 2w◦(P) + 2w◦(Q) − w(X,Y ) contradicts our assumptions.


Next suppose there exist boundary blocks P ∈ P and Q ∈ Q for which P  ∼ Q. Let (A ,B ) ((A ,B )) be obtained from (A,B) by purifying at P (Q). Now (A ,B ) and (A ,B ) are impure, but are superior to (A,B) with regard to criteria α, β. Therefore B is contained in a block of Q and A is contained in a block of P, but this contradicts our above claim. Therefore, every boundary block in P is incident with every boundary block in Q, so purifying at any boundary block results in a pure cross.

By our earlier claim, we may now assume (without loss) that purifying at some block

- P ∈ P results in a pure cross (A ,B ) for which w(A ) = a and w(B ) = b. Since (A ,B ) is critical, our assumptions (concerning critical crosses (A∗,B∗) of (P,Q)) imply 0 < δ(A ,B ) = t − (w(P,Q) − w(X,Y )), so we have


w(P,Q) < w(X,Y ) + t. (17)

Next deﬁne m (n) to be the sum of the weights of the boundary blocks of P (Q). Choose a point y ∈ B so that y is in a boundary block of Q and note that since y is incident with

every boundary block of P, equation 17 implies that m < t, and by a similar argument we have n < t. Using w(B) = w(B ) + n we then ﬁnd

t > δ(A ,B ) − δ(A,B)

= w(A ) − w(A) + w(B ) − w(B) ≥ a − w(A) − t. (18)

Next consider a cross (A ,B ) obtained from (A,B) by purifying at a boundary block of Q. It follows from our assumptions that (A ,B ) is pure, and w(A ) < w(A ) = a, so it must be that either A = ∅ or A ∈ P. In either case Theorem 5.8 implies w(A) = w(A )+m ≤ w◦(P) + t. But then combining this with equation 18 gives us w◦(P) + t ≥ w(A) > a − 2t which contradicts our hypothesis.

- Lemma 11.8 Let (X,Y ) be near one of K5(E,C3), K6(E,C3), or Petersen(E,C5) relative to (E,C). If (A,B) is a maximal critical cross of (X,Y ), then either A is contained in a member of E or B is contained in a member of V or (A,B) is pure.

Proof: Let k = w

◦(E)

d(E,C) = w

◦(C)

d(C,E) and consider a critical cross (A∗,B∗) of (E,C) for which |A∗|,|B∗| ≥ 2. It follows from Lemma 11.3 that A∗ = ∂(v) for a vertex v so we must have one of the following cases.

|(E,C)<br><br>|w(A∗)|w(B∗)|δ(A∗,B∗)|
|---|---|---|---|
|K5(E,C3)|12k<br><br>|12k<br><br>|3k|
|K6(E,C3)<br><br>|20k|30k<br><br>|2k|
|Petersen(E,C5)|12k<br><br>|30k|2k|


From here the result follows easily from the observation w(X,Y ) ≥ w(E,V), Table 1, and

- Lemma 11.7.


- Lemma 11.9 Let (X,Y ) be near Dodecahedron(V,F) relative to (V,F). If (A,B) is a maximal critical cross of (X,Y ), then either A is contained in a member of V, or B is contained in a member of F, or (A,B) is pure.


◦(V)

Proof: Suppose (for a contradiction) that the lemma is false for (X,Y ), set k = w

d(V,F) =

w◦(F) d(F,V) (so w◦(V) = 3k and w◦(F) = 5k) and then choose a counterexample (A,B) so that

α) δ(A,B) is maximum. β) The total number of boundary blocks in V and F is minimum (subject to α).

Since (A,B) is critical we have w(A) + w(B) > w(X,Y ) ≥ w(V,F) = 45k and it follows that min{w(A),w(B)} > 20k.

First suppose w(B) > 20k and let (A ,B ) be the cross obtained by purifying (A,B) at a boundary vertex. It follows from α and β that the lemma holds for (A ,B ). Theorem 5.8 implies that w(B ) > 17k and since A cannot be contained in a single vertex it must be that A is the disjoint union of two adjacent vertices V1,V2. If there exist boundary faces F1,F2 so that Vi ∼ Fj if and only if i = j, then by purifying at V1 gives an impure cross which contradicts our choice of (A,B). So, we may assume (without loss) that every boundary face is incident with V1. Now by Corollary 5.14 we have w(N(A)) ≥ 5k + w(N(A ∩ V1)) ≥

- 5k + w(A ∩ V1) + w(∆) − 23k ≥ w(A) + w(∆) which is a contradiction. Next suppose w(A) > 20k and let (A ,B ) be the cross obtained by purifying (A,B)


at a boundary face. As before, our lemma holds for (A ,B ), so by Theorem 5.8 we have w(A ) > 15k and we deduce that B is the disjoint union of two adjacent faces F1,F2. If there exist boundary vertices V1,V2 so that Fi ∼ Vj if and only if i = j then purifying at

- F1 gives us a contradiction. So, we may assume (without loss) that every boundary vertex is incident with F1. Now by Corollary 5.14 we have w(N(B)) ≥ 9k + w(N(F1 ∩ B)) ≥


- 9k + w(F1 ∩ B) + w(∆) − 25k ≥ w(B) + w(∆) which is a contradiction.


- Lemma 11.10 (Near clip stability) Let Θ be a maximal connected critical trio. If a side of Θ is a near clip, then Θ is a video.


Proof: Assume that Θ = (X,Y,Z) and that (X,Y ) is a near clip relative to (P,Q). Let z ∈ Z and let (A,B) be the cross of (X,Y ) associated with z. It follows from the connectivity of Θ that A is not contained in a block of P and B is not contained in a block of Q. Therefore, by Lemmas 11.6, 11.8, and 11.9 it must be that (A,B) is pure. However, it then follows from the maximality of Θ that P,Q are systems of clones, so (X,Y )• is a clip. Now the result follows by applying Lemma 11.5 to Θ•.

#### 12 Maximality of Songs

In this section we will prove the easy direction of the main theorem, that every song is a maximal critical trio. This proof will call upon a handful of lemmas which demonstrate the maximality of various type of trios.

- 12.1 Impure Beats In this subsection we prove the following lemma concerning maximality of impure beats.


- Lemma 12.1 Every impure beat with a maximal continuation in maximal.


Proof: Let Θ = (X,Y,Z;∼) be a G-trio. Assume that Θ is an impure beat relative to (X,Y ) with associated systems of imprimitivity P,Q,R of X,Y,Z, and assume further that Θ has a maximal continuation. Now suppose (for a contradiction) that there exists a trio Θ∗ = (X,Y,Z;∼∗) for which Θ < Θ∗. It follows from the maximal continuation assumption that whenever (P,Q,R;∼) is a continuation of Θ we must have (P,Q,R;∼) = (P,Q,R;∼∗). It follows from this (and the structure of an impure beat) that ∼∗ |X∪Z =∼ |X∪Z and ∼∗ |Y ∪Z =∼ |Y ∪Z. Choose z ∈ Z, let (A,B) be the cross of (X,Y ) associated with z (this is the same in either Θ or Θ∗), and assume (without loss) that A is ﬁnite. Let P1 ∈ P and

- Q1 ∈ Q be the unique blocks for which ({z},P1) and ({z},Q1)) are partial.


Next consider the G-chorus (P,Q,∼∗). It follows from the assumption that Θ has a maximal continuation that (P,Q,∼∗) is not a matching. Let ∆ = (P ,Q ,∼∗) be the component of (P,Q,∼∗) which contains P1 and let A = {P ∈ P | P ⊆ A} and B = {Q ∈

- Q | Q ⊆ B}. Choose a point x ∈ A ∩ P1 and observe that NΘ∗(x) must contain a point in


- Q2 for some Q2 ∈ Q \ {Q1}. It follows from this that Q2 ∈ Q and Q2  ∈ B . Now choose P2 ∈ P to be the unique block for which P2 ∼ Q2 and note that P2 ∈ A , so in particular A = ∅. Since A is ﬁnite (by assumption) and P2 ⊆ A, the blocks of P and Q must be ﬁnite, so ∆ is a G-duet. A similar argument shows that B = ∅, so (A ,B ) is a nontrivial cross in the duet ∆. Now setting t = wG◦ (P) = wG◦ (Q) and applying Theorem 5.9 gives us


1 2w(∆) ≥ δ(∆) ≥ δ(A ,B ) = w(A ) + w(∆) − w(B ) = w(∆) − t.

This implies 2t ≥ w(∆) = d∆(P ,Q )t and since ∆ is connected, it follows that it is a polygon. However, then N∆(P1) = {Q1,Q2} is disjoint from B so (A ∪ {P1},B ) is a nontrivial cross of ∆ and we have

δ(∆) ≥ δ(A ∪ {P1},B ) = w(∆) which contradicts Theorem 5.9.

##### 12.2 Octahedral Choruses

An octahedral chorus Λ = (X1,...,Xn;∼) is maximal if there does note exist another octahedral chorus Lambda∗ = (X1,...,Xn;∼∗) with the same distinguished partition and Λ < Λ∗.

- Lemma 12.2 If Λ = (X1,...,Xn) is an octahedral chorus satisfying one of the following properties, it is maximal.


- 1. If Λ is type 2B, or 2C.


- 2. If Λ is type 1 or 2A with a maximal continuation.


Proof: Let x ∈ Xi and y ∈ Xj and assume that x  ∼ y and that Xi,Xj are in distinct members of the distinguished partition. It suﬃces to prove that that the following holds: ( ) There exists z in the ground set of Λ so that x ∼ z ∼ y.

If (Xi,Xj) is empty, then it follows from a check of our deﬁnitions that there must exist 1 ≤ k ≤ n so that one of (Xi,Xk), (Xj,Xk) is full and the other is nonempty, and this implies ( ). So, we may assume (Xi,Xj) is partial. If Λ is type 1, then x and y are in a continuation of Λ, and the result follows from the maximality of this continuation. If Λ is type 2C then there exists 1 ≤ k ≤ m so that (Xi,Xj,Xk) is a pure beat, and since pure beats are maximal, this again implies ( ). In the remaining cases, Λ is either type 2A or 2B, and we let Υ1 and Υ2 be the H-trios as given in the deﬁnition of these types. If for i = 1 or i = 2 we have that x,y lie in the ground set of Υi and Υi is an impure beat, then the result follows from Lemma 12.1. Next suppose that there is exactly one i ∈ {1,2} for which x,y lie in the ground set of Υi and that Υi is a pure beat. Setting Υi ≡ (Xi,Xj,Xk) we may then assume w(Xi,Xj) = w(Xj,Xk). However, it now follows from the fact that (Xi,Xj,Xk) is nontrivial and Lemma 5.3 that ( ) must hold (otherwise we could modify the incidence relation on (Xi,Xj,Xk) to obtain a counterexample to this lemma). In the remaining case, we may assume that x,y are contained in the ground set of both Υ1 and Υ2. Let ∼,∼1,∼2 denote the incidence relations of Λ, Υ1, and Υ2. Since x  ∼ y it follows that there exists 1 ≤ i ≤ 2 so that x  ∼i y. However, it then follows from the fact that Υi is maximal that ( ) holds, and this completes the proof.

- 12.3 Dihedral Chords In this subsection we prove a maximality lemma for dihedral chords.


- R1
- R2
- R3
- R4


|z|
|---|


- Q1
- Q2


P1

x

- R1
- R2
- R3


z

- Q1
- Q2


P1

x

Figure 22: Parts of dihedral chords

- Lemma 12.3 Every trio of one of the following types is maximal.


- 1. A dihedral chord of type 0, 2B, or 2C.


- 2. A dihedral chord of type 1 or 2A with a maximal continuation.


Proof: Let Θ = (X,Y,Z) be a dihedral chord relative to the systems of imprimitivity P,Q,R on X,Y,Z which satisﬁes one one of the input assumptions. Let H = G(P) = G(Q) = G(R). Let x ∈ X and z ∈ Z satisfy x  ∼ z and note that it suﬃces to prove:

( ) There exists y in the ground set of Λ so that x ∼ y ∼ z.

If there is an associated octahedral chorus containing x and z, then the result follows from Lemma 12.2. Otherwise, let Λ be an associated octahedral chorus, and let ΛXY (ΛY Z) be the square of Λ with ground set contained in X ∪Y (Y ∪Z). Choose P ∈ P with x ∈ P and R ∈ R with z ∈ R. First suppose that ΛXY is not small and that either w(Y,Z) = ∞ or that (Y,Z) is a fringed sequence which is not short. In this case (depicted on the left in Figure 22) we may choose Q ∈ Q so that (P,Q) is nonempty and (Q,R) is full. If (P,Q) is partial, then it follows from the assumption that ΛXY is not small that we may choose y ∈ Q so that x ∼ y, and if (P,Q) is full then we choose y ∈ Q arbitrarily. In either case we see that ( ) holds. A similar argument handles the case when ΛY Z is not small and either w(X,Y ) = ∞ or (X,Y ) is a fringed sequence which is not short. In light of Observation 9.8 this resolves all of the cases except when both (X,Y ) and (Y,Z) are fringed sequences which are short (and thus both ΛXY and ΛY Z are not small). In this last case (depicted on the right in Figure 22) there exist Q1,Q2 ∈ Q so that N(P) = Q1 ∪Q2 = N(R). Now it follows from Observation 9.8 that ΛXY and ΛY Z are big and w(N(x) ∩ (Q1 ∪ Q2)) > 2|H| and w(N(z) ∩ (Q1 ∪ Q2)) ≥ 2|H|. Since w(Q1 ∪ Q2) = 4|H| it follows that there exists y ∈ Q1 ∪ Q2 with x ∼ y ∼ z as desired.

##### 12.4 The Proof

In this subsection we prove a maximality lemma for videos, and then the easy direction of the main theorem.

- Lemma 12.4 Every video is maximal.


Proof: For the purpose it it suﬃcient to consider only clone-free videos. Let (X,Y,Z) be a clone-free video and assume (without loss) that w(X,Y ) ≤ w(Y,Z) ≤ w(Z,X). Note that by Lemma 7.12 one of (X,Y ) or (Y,X) (and similarly one of (Y,Z) or (Z,Y )) must either be a graph or a clip. To check that (X,Y,Z) is maximal, it suﬃces to prove that for a point z ∈ Z the cross of (X,Y ) associated with z is maximal, and for a point x ∈ X the cross of (Y,Z) associated with x is maximal. This is easy to verify for graphs, and the other cases follow from Lemmas 11.2, 11.3, and 11.4.

Proof of the “if” direction of Theorem 4.7: Let Θ be a song. It follows from Observation

- 4.1 and a routine check of our deﬁnitions that Θ is critical. The fact that Θ is maximal follows from a straightforward induction and the following claim. Claim: A trio is maximal if it is one of the following.


|Structure<br><br>|Proof|
|---|---|
|Video Pure beat Pure chord Impure beat with maximal continuation Cyclic chord with maximal continuation Dihedral chord of type 2B or 2C Dihedral chord of type 1,2A with maximal continuation<br><br>|Lemma 12.4 by deﬁnition straightforward Lemma 12.1 straightforward Lemma 12.3 Lemma 12.3|


#### 13 The Structure of Critical Subset Trios

The goal of this section will be to prove a slight strengthening of Theorem 2.3, which will give a necessary and suﬃcient condition for a nontrivial subset trio to be maximal and critical.

##### 13.1 Symmetries of Videos

Our ﬁrst step will be to record some properties of automorphism groups of videos. Fo standard videos which come from cubic graphs, the following fundamental theorem of Tutte will provide us with an additional bound.

Theorem 13.1 (Tutte [50]) Let Γ = (V,E) be a ﬁnite cubic arc-transitive graph and let

- G = Aut(Γ). Then wG◦ (V ) divides 48 and wG◦ (E) divides 32.


| | | |
|---|---|---|
| | | |


| | |
|---|---|
| | |


###### S5 A5 S5

| |
|---|


Figure 23: Automorphism groups of edge coloured graphs and maps

In addition, we will call on some standard (and easily veriﬁed) facts concerning the automorphism groups of some small graphs and coloured graphs. The most interesting of these involves the interesting action of S5 on 6 points as given by an outer-automorphism of S6. In Figure 23 we have depicted K6 and Petersen with a distinguished 5-edge colouring. We view this edge-colouring as an equivalence relation on the edges, where two edges are equivalent if they have the same colour. So, the automorphism group of this coloured graph is the subgroup of the automorphism group of the underlying graph which preserves this equivalence relation. In Figure 23, the automorphism group of both the edge-coloured K6 and the edge-coloured Petersen is S5, and each permutation of these 5 colours corresponds uniquely to an isomorphism of the coloured graph (for Petersen this is the full automorphism group). In both cases, S5 acts transitively on the shortest cycles of the graph, but when we restrict to the subgroup A5 these cycles break into two orbits, each of which yields an embedding in the projective plane.

The following lemma records the information we require concerning the automorphism groups of videos. For an incidence geometry Λ = (X1,...,Xn), we say that G ≤ Aut(Λ) is fully transitive if G acts transitively on Xi for every 1 ≤ i ≤ n.

Proposition 13.2 The following chart indicates the poset of fully transitive subgroups of the automorphism group of each of the exceptional videos.

|Video|Fully transitive groups|
|---|---|
|Cube/Octahedron : V ∼ E ∼ F|S4 × C2<br><br>S4 A4 × C2|
|Dodecahedron : F ∼ V ∼ E Dodecahedron/Icosahedron : V ∼ E ∼ F Icosahedron : F ∼ V ∼ E<br><br>|A5 × C2<br><br>A5|
|Petersen : C5 ∼ E ∼ V<br><br>|S5|
|Petersen/K6 : F ∼ E ∼ V|A5|
|K6 : C3 ∼ E ∼ V<br><br>|S6<br><br>S5 A6|


Proof: First note that the automorphism groups of the graphs Cube/Octahedron, Dodecahedron/Icosahedron, and Petersen are isomorphic to S4 × C2, A5 × C2, and S5. Every

subgroup which acts transitively on the vertices and edges of these graphs (except Octahedron) must act transitively on the arcs (so must have size a multiple of 2|E| where E is the set of edges), and it follows easily that the ﬁrst two rows in the table are valid. For Petersen, the only proper subgroup of the automorphism group which is both vertex and edge transitive is isomorphic to A5. The 5 cycles of Petersen form a single orbit under the full automorphism group, but split into two orbits of size 6 under this A5 subgroup, and this implies the validity of the third and fourth rows of the table.

To verify the ﬁnal row, let E = E(K6), V = V (K6), and T = C3(K6) and let G be a subgroup of Aut(K6 : C3 ∼ E ∼ V ) which acts transitively on E and V and T. It follows from Lemma 7.5 that G acts transitively on the arcs. Deﬁne a relation σ on E by the rule eσf if either e = f or if e, f are nonadjacent and there exists an element of G which transposes the ends of e, transposes the ends of f, and ﬁxes the other two vertices. Since there are 30 arcs and 20 triangles, the subgroup of G which stabilizes an arc must have even order so there must be an element in G which acts on V as either a transposition or as a permutation which consists of two disjoint transpositions. In the former case, it follows from edge transitivity that G ∼= S6 and we are done. Thus, we may assume that G contains a permutation consisting of two disjoint transpositions, so σ is is nontrivial.

Since there are 15 edges, every edge e must satisfy eσf and eσf for at least two distinct edges f,f . If there exist such edges f,f where f and f are adjacent, then by composing the two corresponding permutations we ﬁnd an element of G which acts as a 3-cycle on V . In this case it follows from the transitivity of G on T that G contains all 3-cycles on V , so G must be either the full automorphism group or the subgroup isomorphic to A6. In the only remaining case, σ is an equivalence relation where each equivalence class is a perfect matching. Following our earlier discussion, the subgroup of Aut(K6) which preserves the 5-edge colouring given by σ is S5 and G must be a subgroup of this. Since the stabilizer of an arc has order at least two, G must have order at least 60. However, we cannot have G ∼= A5 as this would contradict the assumption that G acts transitively on T. Therefore, G ∼= S5, and this completes the proof.

##### 13.2 Structure Theorem I

Our goal over the next two subsections will be to derive our main structure theorem for subset trios from our structure theorem for incidence trios. This is largely a rather straightforward exercise in specializing from group actions back to the setting of groups. However, due to the inherent complexity of our structures, it still requires some eﬀort. In this section we will introduce some helpful terminology, and then prove lemmas to handle beats, cyclic chords, and videos. In the next subsection we will prove lemmas to take care of dihedral chords and pure chords, and then establish the structure theorem.

Deﬁnition: Let Λ = (X1,...,Xn) be a Cayley G-chorus and assume that the action of G

on Xi is regular for 1 ≤ i ≤ n. Let xi ∈ Xi for every 1 ≤ i ≤ n and following Theorem 3.3 make the following associations.

- • Every x ∈ Xi is associated with the unique g ∈ G for which gxi = x.
- • For every 1 ≤ i,j ≤ n the side (Xi,Xj) is associated with the set of all group elements which are associated to a point in N(xi) ∩ Xj.


Now Theorem 3.3 gives us a representation of Λ as a Cayley chorus Λ = CayleyC(G;M) where M is the n × n matrix with ij entry equal to the subset associated with the side (Xi,Xj). We say that Λ is the realization of Λ using base points x1,...,xn.

The following observation follows immediately from our deﬁnitions.

Observation 13.3 Let (A,B,C) be a subset trio in G and let x,y,z ∈ G. The realization of CayleyC(G;A,B,C) using base points (x,1),(y,2),(z,3) is given by

CayleyC(G;xAy−1,yBz−1,zCx−1).

We will repeatedly apply the above observation to move from a subset trio (A,B,C) to a similar subset trio (A ,B ,C ) in the forthcoming lemmas.

- Lemma 13.4 Let (A,B,C) be a subset trio, and assume that Θ = CayleyC(G;A,B,C) is a pure beat relative to (G × {1},G × {2}). Then there exists a proper ﬁnite subgroup H so that A is a left H-coset and (A,B,C) is a pure beat relative to H. Proof: Let P, Q be the clone partitions of G × {1}, G × {2}. Choose x ∈ G so that


- (x,1) ∼ (1,2) and choose z ∈ G arbitrarily. Now let P ∈ P contain (x,1), let Q ∈ Q


contain (1,2), let H = GP = GQ, and note that H is a proper ﬁnite subgroup of G. Next we deﬁne Θ = CayleyC(G;A ,B ,C ) be the realization of Θ using the base points

- (x,1),(1,2),(z,3). Observe that by construction we have A = H. Furthermore, by the


maximality of Θ we have stabL(B ) = H and C = (A B )−1. Therefore (A ,B ,C ), and similarly (A,B,C) is a pure beat relative to H. Furthermore, by construction A is contained in a left H-coset.

- Lemma 13.5 Let (A,B,C) be a subset trio in G, and assume Θ = CayleyC(G;A,B,C)


is an impure beat relative to (G × {1}, G × {2}) with continuation Θ1, an H-trio. Then there exist A ,B ,C ⊆ H so that

- 1. CayleyC(H;A ,B ,C ) is a realization of Θ1.


- 2. (A,B,C) is an impure beat relative to H with continuation (A ,B ,C ).
- 3. The minimal subgroup H so that A is contained in a left H -coset is conjugate to H.


Proof: Let P, Q, and R be the systems of imprimitivity on G × {1}, G × {2} and G × {3} associated with this impure beat, and choose P ∈ P, and Q ∈ Q, and R ∈ R so that Θ1 = (P,Q,R) (so H = GP = GQ = GR). Choose x,y,z ∈ G so that (x,1) ∈ P and

- (y,2) ∈ Q and (z,3) ∈ R and let Θ = CayleyC(G;A ,B ,C ) be the realization of Θ using the base points (x,1), (y,2), and (z,3). As in the deﬁnition of realization, we associate each point (u,1) ∈ G × {1} with the group element g for which (gx,1) = (u,1) and we associate points in G×{2} and G×{3} with elements in G using (y,2) and (z,3) similarly. Note that for every block in P ∪Q∪R, the set of group elements associated with this block (i.e. associated with a point in this block) is a left H-coset.


Now H is precisely the set of elements associated with a point in Q, which gives us ∅ = A ⊂ H. Furthermore, since (P,Q) is connected, it follows that A is not contained in a left coset of a proper subgroup of H. Since A = xAy−1 it follows that H = y−1Hy is the unique minimal subgroup for which A is contained in a left H -coset. Now we deﬁne the following sets.

- B0 = {g ∈ G | g is associated with a point in NΘ(z,3) ∩ Q}
- B1 = {g ∈ G | g is associated with a point in NΘ(z,3) ∩ (G × {2} \ Q)} C0 = {g ∈ G | g is associated with a point in NΘ(z,3) ∩ P} C1 = {g ∈ G | g is associated with a point in NΘ(z,3) ∩ (G × {1} \ P)}.


It follows from our construction that (B )−1 = B0 ∪B1 and C = C0 ∪C1. Futhermore, we have ∅ = B0,C0 ⊆ H and H ≤ stabR(B1), stabR(C1). This implies H ≤ stabL(B \ H). Now, for every S ∈ G/H \ {H} there exist blocks P ∈ P and Q ∈ Q which are associated with this set of elements, and these blocks satisfy P ∼ Q . Furthermore, by construction, we must have either S ⊆ B1 or S ⊆ C1. It follows from this that (A B )−1 \ H = C \ H. We conclude that (A ,B ,C ) and similarly (A,B,C) is an impure beat relative to H. Furthermore, (A ,B0,C0) is a continuation of (A,B,C) and CayleyC(H;A ,B0,C0) is a realization of Θ1.

- Lemma 13.6 Let (A,B,C) be a subset trio in G and assume Θ = CayleyC(G;A,B,C) is a cyclic chord with continuation Θ1, an H-trio. Then there exists A ,B ,C ⊆ H so that


- 1. CayleyC(H;A ,B ,C ) is a realization of Θ1.
- 2. (A,B,C) is an impure cyclic chord with continuation (A ,B ,C ).


Proof: By possibly replacing (A,B,C) by a similar trio, we may assume that w(G×{1},G× {2}), w(G × {2},G × {3}) < ∞. We may choose a group J = Z or J = Z/nZ and systems of imprimitivity P = {Pj | j ∈ J} of G × {1} and Q = {Qj | j ∈ J} of G × {2} and

- R = {Rj | j ∈ J} of G × {3} together with integers  ,m in accordance with the deﬁnition of cyclic chord and assume (without loss of generality) that Θ1 = (P0,Q0,R0). Note that the subgroup H as given in the statement of this lemma also aligns with that given in this deﬁnition. Choose S ∈ G/H so that every g ∈ S satisﬁes gPj = Pj+1 and gQj = Qj+1 and gRj = Rj+1 for every j ∈ J.


Now choose x,y,z ∈ G so that (x,1) ∈ P0 and (y,2) ∈ Q0 and (z,3) ∈ R0 and let Θ = CayleyC(G;A ,B ,C ) be the realization of Θ using the base points (x,1),(y,2),(z,3). It follows that for every j ∈ J, the set of group elements associated with Pj (or Qj or Rj) is given by Sj. Therefore, A ∪ H and B ∪ H are H-stable, ϕG/H(A ), ϕG/H(B ) are basic geometric progressions with ratio S, and ∅ = (A B )−1 \ H = C \ H and C ∩ H = ∅. Thus (A ,B ,C ), and similarly (A,B,C), is an impure cyclic chord. Furthermore, setting

- A = A ∩H and B = B ∩H and C = C ∩H we have that (A ,B ,C ) is a continuation of (A,B,C) and CayleyC(H;A ,B ,C ) is a realization of Θ1, as desired.


- Lemma 13.7 Let (A,B,C) be a subset trio in G and let Θ = CayleyC(G;A,B,C). If Θ is a video, there exists a subset trio (A ,B ,C ) similar to (A,B,C) and subgroups H G and H H1,H2,H3 ≤ G with H1 = stabL(A ) = stabR(C ), H2 = stabR(A ) = stabL(B ), and H3 = stabR(B ) = stabL(C ) satisfying one of the following


- 1. |A | = 2|H2| = |B | and δ(A ,B ,C ) = |H1| = |H3| < |H2|.
- 2. 9|H1| = |A | = 3|H2| and 2|H2| = |B | = 3|H3| and δ(A ,B ,C ) = |H1|. Further, if G is ﬁnite, then [H1 : H] divides 16.
- 3. 4|H1| = |A | = 2|H2| and 3|H2| = |B | = 2|H3| and δ(A ,B ,C ) = |H1|. Further, if G is ﬁnite, then [H1 : H] divides 16.
- 4. One of the following is satisﬁed.


|G/H<br><br>||G|<br><br>|H1|<br>||G|<br><br>|H2|<br><br><br>||G|<br><br>|H3|<br>||G| |A |<br><br>||G| |B |<br><br>||G| |C |<br><br>|
|---|---|---|---|---|---|---|
|C2 × S4, C2 × A4, or S4 C2 × A5 or A5 C2 × A5 or A5 C2 × A5 or A5 S5 A5 S6, or A6, or S5|8 12 20 20 12 6 20<br><br>|12 20 30 12 15 15 15<br><br>|6 30 12 30 10 10 6|4 4 10<br><br>4<br><br>3 3<br><br>5<br><br><br>|3 10 6 6 5 5 3|2<br><br>3/2<br><br>4/3<br><br>5/3<br><br><br>2 2 2<br><br>|


Proof: By possibly replacing (A,B,C) by an similar trio, we may assume that Θ• is isomorphic to one of the trios listed in the deﬁnition of standard video or exceptional video. Now for 1 ≤ i ≤ 3 choose a subgroup Hi ≤ G so that the clone partition of G × {i} is given by G/Hi × {i} for 1 ≤ i ≤ 3. It follows that H1AH2 = A and H2BH3 = B and H3CH1 = C. Let H G be the kernel of the action of G on Θ• and note that H ≤ Hi for

- 1 ≤ i ≤ 3. We now split into cases depending on Θ•.


- Case 1: Θ• is isomorphic to Γ : E ∼ V ∼ E for a graphic duet Γ with degree d ≥ 3.

In this case, it follows from the degrees of the duets in Θ• that |A| = 2|H2| = |B| and then d|H1| = |A| = |B| = d|H3|. Lemma 7.1 gives us δ(A,B,C) = δ(Θ) = |H1| = |H3| < |H2| so the ﬁrst outcome holds.

- Case 2: Θ• is isomorphic to Γ : P3 ∼ V ∼ E for graphic duet Γ of degree 3 Here it follows from the degrees of the duets in Θ• that 9|H1| = |A| = 3|H2| and

- 2|H2| = |B| = 3|H3|. Lemma 7.1 gives us δ(A,B,C) = 12|H3| = |H1| and Theorem 13.1 implies that [H1 : H] divides 16 whenever G is ﬁnite. It follows that the second outcome holds.

Case 3: Θ• is isomorphic to Γ : P3 ∼ E ∼ V for a graphic duet Γ of degree 3. In this case it follows from the degrees of duets in Θ• that 4|H1| = |A| = 2|H2| and

- 3|H2| = |B| = 2|H3|. Lemma 7.1 gives us δ(A,B,C) = 12|H2| = |H1| and Theorem 13.1 implies that [H1 : H] divides 16 whenever G is ﬁnite. So, the third outcome is satisﬁed.


- Case 4: Θ• is isomorphic to an exceptional video.


In all of these cases, we will show that one of the outcomes from the table in part 4 of the statement of the lemma is satisﬁed. These outcomes correspond in order, to the videos Cube/Oct. : V ∼ E ∼ F, Dodec. : F ∼ V ∼ E, Dodec./Icos. : V ∼ E ∼ F, Icos. :

- F ∼ V ∼ E, Petersen: C5 ∼ E ∼ V , Petersen/K6 : F ∼ E ∼ V , and K6 : C3 ∼ E ∼ V . The structure of the group G/H is given by Proposition 13.2, and the remaining properties are straightforward to verify (much of this information is encapsulated in Figure 16).


##### 13.3 Structure Theorem II

In Section 2 we introduced the notion of an octahedral conﬁguration (recall that this is an oriented octahedron with edges labelled by subsets from a group H), and then in Section

- 3 we deﬁned a Cayley chorus. In fact, Cayley choruses provide a natural framework to


C3

A4

B2

A1

B1

C4 C2

C1

B3

A3

A2

B4

·C3

·B2

·A4

H × {6} H × {3} H × {2}

- ·A1
- ·A2


·B1

·C4 ·C2

H × {5}

H × {1}

·C1

·B3

·A3

·B4

H × {4}

Figure 24: An octahedral conﬁguration and a corresponding octahedral Cayley chorus

work with octahedral conﬁgurations. To treat these in the desired manner, we introduce a natural deﬁnition.

Deﬁnition: Let A1,...,A4,B1,...,B4,C1,...,C4 ⊆ H and let Ω be an octahedral conﬁguration given by these sets and the labelled graph on the left in Figure 24. We deﬁne the Cayley octahedral chorus

CayleyOct(H;A1,...,A4,B1,...,B4,C1,...,C4) = CayleyC(H;M) where the matrix M is given below





∅ ∅ A1 A2 C1−1 C4−1 ∅ ∅ A4 A3 C2−1 C3−1

- A−1 1 A−4 1 ∅ ∅ B1 B2
- A−2 1 A−3 1 ∅ ∅ B4 B3 C1 C2 B1−1 B4−1 ∅ ∅ C4 C3 B2−1 B3−1 ∅ ∅


M =

 

 

and we equip this chorus with the following partition. {H × {1},H × {2}}, {H × {3},H × {4}}, {H × {5},H × {6}} .

It follows from the deﬁnition of octahedral conﬁguration that this chorus is collision free, and therefore it is indeed an octahedral chorus. We say that this chorus corresponds with Ω, and we have depicted it on the right in Figure 24.

Of course, octahedral conﬁgurations and octahedral Cayley choruses, are in essence the same. However, we have deﬁnitions in place for type and continuation of an octahedral conﬁgurations which are based on subsets, and other deﬁnitions in place for type and continuation of an octahedral chorus which are based on properties of these incidence geometries. Our next lemma shows that these deﬁnitions align properly.

- Lemma 13.8 Let H be a ﬁnite group, let Ω be an octahedral conﬁguration in H and let Λ be the corresponding Octahedral Cayley chorus. Then we have


- 1. Λ is not type 2C.
- 2. If Λ has type −1, 0, 1, 2A, or 2B then Ω has the same type.
- 3. If Λ has type 1 or 2A with continuation Θ, a K-trio, there are A ,B ,C ⊆ K so that


- (a) CayleyC(K,A ,B ,C ) is a realization of Θ.
- (b) (A ,B ,C ) is a continuation of Ω.


Proof: Let Ω be given by the labelled graph on the left in Figure 24, so Λ is depicted on the right in this ﬁgure. Note that Λ has rank 6, so in particular Λ is not type 2C. If Λ has type −1 or 0, then it follows immediately that Ω has the same type. Next suppose that Λ has

- type 1 and assume for notational convenience that A1,B1,C1 are proper nonempty subsets of H, so Θ = (H × {1},H × {3},H × {5}) is the unique continuation of Λ. Then Ω is type

- 1, and CayleyC(H;A1,B1,C1) is a realization of Θ and (A1,B1,C1) is a continuation of Ω, as desired.


Next assume that Λ has type 2A or 2B and assume for notational convenience that A1,B1,C1,B2,C4 are proper nonempty subsets of H. Now let Υ1 = (H ×{1},H ×{3},H × {5};∼1) and Υ2 = (H ×{1},H ×{3},H ×{6};∼2) be the H-trios as given by the deﬁnition of types 2A and 2B. For i = 1,2 we may choose Ai1 ⊆ H so that (x,1) ∈ H × {1} and (y,3) ∈ H ×{3} satisfy (x,1) ∼i (y,3) if and only if y ∈ xAi1, and note that the deﬁnitions of types 2A and 2B (for incidence trios) imply that A1 = A11 ∩ A21. If Λ is type 2B then Υ1 and Υ2 are pure beats relative to (H × {1},H × {3}). Now applying Lemma 13.4 we have that there exist proper subgroups K1,K2 < H so that (A11,B1,C1) is a pure beat relative to K1 and A11 is a left K1-coset, and similarly (A21,B2,C4) is a pure beat relative to K2 and A21 is a left K2-coset. It follows that Ω has type 2B as desired. Next suppose that Λ has type 2A with continuation Θ a K1-trio, and assume (without loss) that Υ1 is an impure beat relative to (H × {1},H × {3}) and Υ2 is a pure beat relative to (H × {1},H × {3}) (so A1 = A11 ⊆ A21). In this case, applying Lemma 13.4 to Υ2 gives us a subgroup K2 < H so that (A21,B2,C4) is a pure beat relative to K2, and A21 is a left K2 coset. Now applying Lemma 13.5 to the impure beat (A1,B1,C1) and the continuation Θ gives us A ,B ,C ⊆ K1 so that CayleyC(K1,A ,B ,C ) is a realization of Θ and (A ,B ,C ) is a continuation of (A1,B1,C1) and the minimal subgroup K 1 so that A1 is contained in a K 1 coset is conjugate to K1. Since K1 and K 1 are conjugate, (A1,B1,C1) is also an impure beat relative to K 1, and since K 1 ≤ K2 it follows that Ω has

- type 2A with continuation (A ,B ,C ), thus completing the proof.


With this lemma in place, we can now prove two of the theorems stated in Section 2 concerning the classiﬁcation of critical octahedral conﬁgurations.

Proof of Theorems 2.1 and 2.2: Let Ω be maximal critical octahedral conﬁguration and let Λ be the associated octahedral Cayley chorus. It follows from our deﬁnitions that Λ is also maximal and critical, and by construction Λ must have rank 6. It then follows from Theorems 4.5 and 4.6 that Λ has type −1, 0, 1, 2A, or 2B. Lemma 13.8 now implies that Ω has type −1, 0, 1, 2A, or 2B which implies both Theorems 2.1 and 2.2.

- Lemma 13.9 Let (A,B,C) be a subset trio in G and assume that Θ = Cayley(G;A,B,C) is a dihedral chord. Then (A,B,C) is an impure dihedral chord, and further


- 1. Θ is not type 2C.
- 2. If Θ has type 0, 1, 2A, or 2B then (A,B,C) has the same type.
- 3. If Θ has type 1 or 2A with continuation Θ1, there exists a ﬁnite subgroup K < G and A ,B ,C ⊆ K so that CayleyC(K;A ,B ,C ) is a realization of Θ1 and (A ,B ,C ) is a continuation of (A,B,C).


Proof: By replacing (A,B,C) by a similar subset trio, we may choose J = Z or Z/nZ, systems of imprimitivity P = {Pj | j ∈ J}, Q = {Qj | j ∈ J}, R = {Rj | j ∈ J} on

- G × {1}, G × {2}, G × {3}, a subgroup H G, and integers  ,m as in the deﬁnition of dihedral chord. We may also assume (without loss) that if there is a continuation Θ1 as described in the statement of the lemma, then Θ1 has ground set a subset of P0 ∪Q0 ∪R0.


By assumption the action of G/H on each of P,Q,R is dihedral, so we may choose a rotation S ∈ G/H so that every g ∈ S satisﬁes gPj = Pj+1 and gQj = Qj+1 and gRj = Rj+1. Now choose (x,1) ∈ P0 and (y,2) ∈ Q0 and (z,3) ∈ R0 and let Θ = CayleyC(G;A ,B ,C ) be the realization of Θ using these base points. This associates each block in P ∪Q∪R with a set of group elements which consists of the union of two left H-cosets, one rotation and one ﬂip. Furthermore, since the action of G on Θ is regular, we may reﬁne our partitions P,Q,R by letting {Pj0,Pj1} be a partition of Pj so that the set Pj0 is associated with a rotation in G/H and Pj1 is associated with a ﬂip. Deﬁne Qij and Rji similarly for every j ∈ J and i = 0,1. It follows immediately that {Pji | j ∈ J and i = 0,1} and {Qij | j ∈ J and i = 0,1} and {Rji | j ∈ J and i = 0,1} are systems of imprimitivity. Furthermore, our deﬁnitions imply (x,1) ∈ P00 and (y,2) ∈ Q00 and (z,3) ∈ R00. Now we deﬁne a family of H-cosets as follows.

 

 

 

 

- Q00,Q10,Q0 ,Q1
- R01,R01,Rm0 ,Rm1


- A1,A2,A3,A4
- B1,B2,B3,B4
- C1,C2,C3,C4


are associated with









P00,P01,P0 +m,P1 +m

Note that this construction yields A1,B1,C1 = H. Next deﬁne A+ = A ∪ ∪4i=1 Ai and

- B+ = B ∪ ∪4i=1 Bi and C+ = C ∪ ∪4i=1 Ci . It follows immediately that A+, B+,


and C+ are H-stable. Furthermore, ϕG/H(A+) is a dihedral progression with ratio S given by {H,S,S2,...,S }{H,A2}. Similarly ϕG/H(B+) is a dihedral progression with ratio S and furthermore, (ϕG/H(A+),ϕG/H(B+),ϕG/H(C+)) is a dihedral prechord with labelled octahedron given by the sets A1,...,A4,B1,...,B4,C1,...,C4 and the graph on the left in Figure 4. It follows from this that (A ,B ,C ) is an impure dihedral chord.

Now we will follow the procedure described in Section 2 to construct an octahedral conﬁguration associated with A ,B ,C . To do this, we will use the variables u,u ,v,v ,w,w labelling the vertices of the graph on the left in Figure 4. Let u ,v ,w = 1 and choose

- u ∈ C2 and v ∈ A2 and w ∈ B2. Then for 1 ≤ i ≤ 4 if the Ai edge has initial vertex labelled by x and terminal vertex labelled by y then we set A∗i = x(A ∩Ai)y−1, and deﬁne


Bi∗ and Ci∗ similarly. This gives us an octahedral conﬁguration Ω as depicted on the right in Figure 4.

Returning to our incidence geometry, we deﬁne Λ to be the H-octahedral chorus given by Λ = (P00,P01,Q00,Q10,R00,R01) with distinguished partition {{P00,P01}, {Q00,Q10}, {R00,R01}}. So, by our assumptions, if Θ1 is a continuation of Θ, then Θ1 is a continuation of Λ. Now deﬁne Λ to be the realization of Λ using the base points (x,1), (ux,1), (y,2), (vy,2), (z,3), (wz,3), and assume that

Λ = CayleyOct(H;A 1,...,A 4,B 1,...,B 4,C 1,...,C 4). Now we have

- A 1 = {h ∈ H | (hy,2) ∼ (x,1)} = A ∩ A1 = A∗1
- A 2 = {h ∈ H | (hvy,2) ∼ (x,1)} = {h ∈ H | hv ∈ A ∩ A2} = (A ∩ A2)v−1 = A∗2
- A 3 = {h ∈ H | (hvy,2) ∼ (ux,1)} = {h ∈ H | u−1hv ∈ A ∩ A3} = u(A ∩ A3)v−1 = A∗3
- A 4 = {h ∈ H | (hy,2) ∼ (ux,1)} = {h ∈ H | u−1h ∈ A ∩ A4} = u(A ∩ A4) = A∗4


Similarly we ﬁnd B i = Bi∗ and C i = Ci∗ for 1 ≤ i ≤ 4. Therefore, Λ is a Cayley octahedral chorus corresponding to Ω, and Λ is a realization of Λ. The result now follows from Lemma

- 13.8.


- Lemma 13.10 Let (A,B,C) be a subset trio in G and assume Θ = CayleyC(G;A,B,C) is a pure chord.


- 1. If Θ has cyclic action, then (A,B,C) is a pure cyclic chord.
- 2. If Θ has dihedral action, then (A,B,C) is a pure dihedral chord.
- 3. If Θ has split action, then (A,B,C) is an impure dihedral chord of type 0.


Proof: By possibly replacing (A,B,C) with a similar trio we may assume that A and B are ﬁnite. Based on the deﬁnition of pure chord, we may choose a group J = Z or J = Z/nZ and positive integers  ,m so that the clone partitions of G × {1}, G × {2} and G × {3} in Θ are given by P = {Pj | j ∈ J}, Q = {Qj | j ∈ J}, and R = {Rj | j ∈ J} where N(Pj) ∩ G × {2} = Qj ∪ ...Qj+ and N(Qj) ∩ G × {3} = Rj ∪ ...,∪Rj+m. Deﬁne H to be the subgroup G(P) = G(Q) = G(R). Next, choose (x,1) ∈ P0 and (y,1) ∈ Q0 and

- (z,1) ∈ R0 and deﬁne Θ = CayleyC(G;A ,B ,C ) to be the realization of Θ using the base points (x,1), (y,2), and (z,3). We now split into cases depending on Θ.


- Case 1: Θ is a pure chord with cyclic action.

In this case G/H is cyclic and we may choose a consecutive shift S ∈ G/H so that every g ∈ S satisﬁes gPj = Pj+1 and gQj = Qj+1 and gRj = Rj+1 for every j ∈ J. It now follows that S generates the group G/H and further A = H ∪S∪...∪S and B = H ∪S∪...Sm. It follows from our deﬁnitions that C = (A B )−1 is not contained in a single H-coset, so

- (A ,B ,C ), and similarly (A,B,C) is a pure cyclic chord.

Case 2: Θ is a pure chord with split action.

It follows from Lemma 9.7 that Θ is a dihedral chord of type 0. So by Lemma 13.9 we have that (A,B,C) is an impure dihedral chord of type 0, as desired.

Case 3: Θ is a pure chord with dihedral action.

In this case G/H is dihedral and we may choose a consecutive shift S ∈ G/H so that every g ∈ S satisﬁes gPj = Pj+1 and gQj = Qj+1 and gRj = Rj+1 for every j ∈ J. It now follows that S generates the rotation subgroup of G/H. Choose a ﬂip F ∈ G/H so

that GQ0 = H ∪ F and then observe that A is precisely the set (H ∪ S ∪ ... ∪ S )(H ∪ F) so ϕG/H(A ) is a basic dihedral progression with ratio S. A similar argument shows that

- (B )−1 is given by (H ∪ F)(H ∪ S−1 ∪ ... ∪ S−m. So ϕG/H(B ) is also a basic dihedral progression with ratio S and stabL(A ) = H ∪ F = stabR(B ). It follows that (A ,B ,C ), and similarly (A,B,C) is a pure dihedral chord.




We are now ready to prove our classiﬁcation theorem for maximal critical subset trios.

- Theorem 13.11 If Φ is a nontrival subset trio in G, then Φ is maximal and critical if and only if there exist a sequence of subgroups G = G1 > G2 ... > Gm and a sequence of subset trios Φ = Φ1,Φ2,...,Φm so that the following hold.


- 1. Φi is a subset trio in the group Gi for 1 ≤ i ≤ m.


- 2. Φi is either an impure beat, an impure cyclic chord, or an impure dihedral chord of type 1 or 2A with continuation Φi+1 for 1 ≤ i < m.
- 3. Φm is either a pure beat, a pure cyclic chord, a pure dihedral chord, an impure dihedral chord of type 0 or 2B, or Φm = (A,B,C) where CayleyC(Gm;A,B,C) is a video.


Proof: For the “only if” direction, we let Φ = (A,B,C) be maximal and critical and deﬁne Θ = CayleyC(G;A,B,C). It follows from Theorem 4.7 that Θ is a song, and so the result follows from Lemmas 13.4, 13.5, 13.6, 13.9, and 13.10, together with a straightforward induction.

For the “if” direction, we also let Φ = (A,B,C) and deﬁne Θ = CayleyC(G;A,B,C). It follows from our deﬁnitions and a straightforward induction that Θ is a song, so Θ is maximal and critical. This implies that (A,B,C) is maximal and critical and desired.

Proof of Theorem 2.3: This follows from the previous theorem and Lemma 13.7.

#### 14 Corollaries

In this section we will prove the corollaries of the main theorem which were stated in the Introduction.

##### 14.1 Weak Structure

Our ﬁrst corollary will be a weak version of the structure theorem which applies to any critical pair, and has the convenience of unpacking some of our notation. We will then use this result to derive Corollary 1.5.

Corollary 14.1 (Weak Structure) If (A,B) is a critical pair in the group G, then setting

- C = (AB)−1, one of the following holds.


- 1. One of A, B, or C is contained in a coset of a proper subgroup.
- 2. There exists H  G so that G/H is a cyclic group with |G/H| ≥ 4 for which ϕG/H(A) and ϕG/H(B) are geometric progressions with a common ratio. Furthermore, one of the following holds.


- (a) δ(A,B) ≤ 12|H| and max{|AH \ A|,|BH \ B|} + δ(A,B) ≤ |H|.

- (b) ABH = AB and δ(A,B) + |AH \ A| + |BH \ B| = |H|.


- 3. There exists H G so that G/H is dihedral with |G/H| ≥ 8. In addition, there exist A+ ⊇ A and B+ ⊇ B so that A+H = A+ and B+H = B+ and ϕG/H(A+), ϕG/H(B+) are dihedral progressions with a common ratio. Furthermore, one of the following holds.

- (a) δ(A,B) ≤ 21|H| and max{|A+ \ A|,|B+ \ B|} + δ(A,B) ≤ 2|H|.

- (b) ABH = AB and |H| = |B+\BH| = |A+\AH| = δ(A,B)+|AH\A|+|BH\B|.
- (c) A+B+ = AB and δ(A,B) + |A+ \ A| + |B+ \ B| = 2|H|.


- 4. There exist A∗ ⊇ A and B∗ ⊇ B so that A∗B∗ = AB and there exists (S,T) ∈

{(A∗,B∗),(B∗,C),(C,A∗)} and H1,H2,H3 ≤ G so that H1SH2 = S and H2TH3 = T and one of the following holds.

- (a) |H|S|

2| = |H|T|

2| = 2 and δ(A,B) + |A∗ \ A| + |B∗ \ B| = |H1| = |H3| < |H2|.

- (b) |H |S|


2|, |H|T|

2| = {2,3} and δ(A,B)+|A∗\A|+|B∗\B| = min |H1|,|H3| < |H2|.

- 5. There exist H G and H ≤ H1,H2,H3 ≤ G so that A∗ = H1AH2 and B∗ = H2BH3 satisfy A∗B∗ = AB and δ(A,B)+|A∗\A|+|B∗\B| ≤ min{|H1|,|H2|,|H3|}. Furthermore, one of the following holds.


|G/H<br><br>||G|/|A∗|,|G|/|B∗|,|G|/|C||
|---|---|
|C2 × S4, C2 × A4, or S4 C2 × A5 or A5 S6, A6, S5, or A5<br><br>|{2,3,4}<br><br>{3/2,4,10}, {4/3,6,10}, or {5/3,4,6}<br><br>{2,3,5}<br>|


Proof: Let (A∗,B∗,C) be a maximal subset trio with A∗ ⊇ A and B∗ ⊇ B and deﬁne the Cayley choruses Θ = CayleyC(G;A,B,C) and Θ∗ = CayleyC(G;A∗,B∗,C). We will use ∼ to denote the incidence relation in Θ, and ∼∗ for the incidence relation in Θ∗. Note that δ(A,B) = δ(Θ) = δ(Θ∗) − |A∗ \ A| − |B∗ \ B|. If (A∗,B∗,C) is trivial, then the ﬁrst outcome holds. Otherwise, Theorem 4.7 implies that Θ∗ is a song. We now split into cases depending on Θ∗.

- Case 1: Θ∗ is a pure or impure beat. In this case it follows from Lemma 13.4 or 13.5 that the ﬁrst outcome holds.
- Case 2: Θ∗ is a video. Lemma 13.7 implies that either the fourth or ﬁfth outcome holds.
- Case 3: Θ∗ is a pure chord.


It follows from Lemma 13.10 that (A∗,B∗,C) is either a pure cyclic chord, a pure dihedral chord, or an impure dihedral chord of type 0. If (A∗,B∗,C) is a pure cyclic chord relative to H, then δ(A∗,B∗,C) = |H|, so A∗ = AH and B∗ = BH and outcome 2b holds. If (A∗,B∗,C) is a pure dihedral chord relative to H, then δ(A∗,B∗,C) = 2|H| and outcome 3c holds (with A+ = A∗ and B+ = B∗). In the remaining case we may assume that (A∗,B∗,C) is an impure dihedral chord of type 0 relative to H. We claim that in this case, outcome 3b is satisﬁed. First observe that ABH = AB and A∗H = A∗ and B∗H = B∗ and δ(A∗,B∗,C) = |H| which implies AH = A∗ and BH = B∗. So, to show that 3b holds, we need only ﬁnd suitable sets A+ containing AH and B+ containing BH. Now choose sets A+,B+,C+ in accordance with the deﬁnition of impure dihedral chord so that AH ⊆ A+ and BH ⊆ B+ and C ⊆ C+ and A+,B+ are dihedral progressions with a common ratio. It follows from the deﬁnition of a type 0 that the ends (A1,A2,A3,A4) of A+ satisfy one of the following

• |{1 ≤ i ≤ 4 | Ai ⊆ AH}| = 3 and |{1 ≤ i ≤ 4 | Ai ∩ AH = ∅}| = 1 • |{1 ≤ i ≤ 4 | Ai ⊆ AH}| = 1 and |{1 ≤ i ≤ 4 | Ai ∩ AH = ∅}| = 3

In the former case A+ contains AH as desired. In the latter we may shorten A+ by replacing it with either A+ \ (A1 ∪ A2) or A+ \ (A3 ∪ A4) to obtain a dihedral progression containing AH as desired. A similar argument for B+ shows that outcome 3b holds.

- Case 4: Θ∗ is a cyclic chord.

- In this case we will show that outcome 2a is satisﬁed. Suppose that Θ∗ is a cyclic

chord relative to the systems of imprimitivity P,Q,R on G × {1}, G × {2}, G × {3}, and let H = G(P) = G(Q) = G(R). It follows from the structure of a cyclic chord that G/H is cyclic, so we may choose a consecutive shift S ∈ G/H. Since Θ∗ has a continuation which is a nontrivial H-trio with the same deﬁciency as Θ∗, Lemma 5.3 gives us δ(A,B) ≤ δ(Θ∗) ≤ 21|H|. Now by Lemma 9.10 we ﬁnd that (G × {1},G × {2};∼) is a near sequence relative to (P,Q) and w(P,Q;∼) − w(G × {1},G × {2};∼) ≤ |H| − δ(Θ). It follows from this that we may choose integers < m so that the set A+ = S ∪ S +1 ... ∪ Sm satisﬁes A ⊆ A+ and |A+ \ A| ≤ |H| − δ(A,B). However, we must then have A+ = AH, which implies |AH \ A| ≤ |H| − δ(A,B). A similar argument for the set B shows that outcome 2a holds, as desired.

Case 5: Θ∗ is a dihedral chord of type 1 or 2.

- In this case we will show that outcome 3a is satisﬁed. Suppose that Θ∗ is a dihedral




chord relative to the systems of imprimitivity P,Q,R on G × {1}, G × {2}, G × {3}, and set H = G(P) = G(Q) = G(R). By assumption we have that G/H is dihedral, so we may

choose a consecutive shift S ∈ G/H. Observe that Θ∗ cannot be a dihedral chord of type

- 2c, and if it has type 2b then δ(Θ∗) = |K| for a proper subgroup K < H so δ(Θ∗) ≤ 21|H|. Otherwise, Θ∗ is either type 1 or type 2a, so it has a continuation which is a nontrivial K-trio for some K ≤ H with the same deﬁciency as Θ∗. It follows from this and Lemma

5.3 that δ(A,B) ≤ δ(Θ∗) ≤ 12|H|.

Now apply Lemma 9.10 to the side (G × {1},G × {2};∼) of Θ. This gives us systems of imprimitivity P ,Q of G × {1}, G × {2} so that (G × {1},G × {2};∼) is a near sequence relative to (P ,Q ) with dihedral action and consecutive shift S, and furthermore w(P ,Q ;∼) − w(G × {1},G × {2};∼) ≤ 2|H| − δ(Θ). It follows from this that we may choose integers < m and a ﬂip F ∈ G/H so that the set A+ = (S ∪S +1 ...∪Sm)(H ∪F) satisﬁes A ⊆ A+ and |A+ \ A| ≤ 2|H| − δ(A,B). A similar argument for the set B shows that outcome 3a holds, as desired.

Proof of Corollary 1.5: If (A,B) is not critical then 3 holds for H1 = H2 = H3 = {1}. Otherwise, we apply Corollary 14.1. If we get outcome 1 from this corollary, then 1 holds for (A,B). If we get outcomes 2a or 3a then 2 holds for (A,B). Outcomes 2b and 3b give us a subgroup H G so that setting H1 = H2 = H3 = H we have that 3 holds. If we get outcome

- 3c, then there exist A+,B+ ⊆ G with A ⊆ A+ and B ⊆ B+ so that (A+,B+,C) is a pure dihedral chord, so the subgroups H1 = stabL(A+), and H2 = stabR(A+) = stabL(B+) and


- H3 = stabR(B+) all satisfy [Hi : H] = 2 and it follows that 3 holds. Finally, outcomes 4 and 5 give us subgroups H1,H2,H3 which satisfy 3.


- 14.2 Deﬁciency vs. Disparity For a pair (A,B) of subsets of G, we deﬁne the disparity of (A,B) to be ν(A,B) =


- |A| − |B| . In this section we will consider pairs (A,B) for which δ(A,B) > ν(A,B), or


equivalently, |AB| < 2min{|A|,|B|} (note that any critical pair of the form (A,A) satisﬁes this inequality). Pairs which have deﬁciency greater than discrepancy can only form videos in a particular manner, as we will see in the next lemma, and this fact will allow us to simplify our weak structure theorem in this case.

- Lemma 14.2 Let (A,B,C) be a subset trio in G and assume Θ = CayleyC(G;A,B,C) is a video. If δ(Θ) > ν(A,B) then Θ ∼= Γ : E ∼ V ∼ E for a graphic duet Γ. Therefore, there exists H ≤ G so that H = stabR(A) = stabL(B) satisﬁes |A| = 2|H| = |B| and δ(A,B,C) = |stabL(A)| = |stabR(B)| < |H|.


Proof: Let (X,Y,Z) be an arbitrary video and assume |w(X,Y ) − w(Y,Z)| < δ(X,Y,Z). If w(X,Y ) = w(Y,Z), then follows from Lemma 7.11 that |w(X,Y )−w(Y,Z)| ≥ w◦(Y ) ≥ δ(Θ) which is a contradiction. So, it must be that w(X,Y ) = w(Y,Z). A straightforward

analysis using Figure 16 implies that this is only possible when (X,Y,Z) ∼= Γ : E ∼ V ∼ E for a graphic duet Γ.

Based on this analysis, we ﬁnd that Θ ∼= Γ : E ∼ V ∼ E for a graphic duet Γ with degree at least three. If the clone partition of G×{i} (in the trio Θ) is given by G/Hi×{i} for 1 ≤ i ≤ 3 then H1 = stabL(A) and stabR(A) = H2 = stabL(B) and H3 = stabR(B). Further, |A| = 2|H2| = |B| and δ(Θ) = δ(A,B,C) = |H1| = |H3| < |H2| as desired.

- Lemma 14.3 Let A,B ⊆ G be ﬁnite and assume B = x−1Ax for some x ∈ G and that (A,B) is critical. If C = (AB)−1 and (A∗,B∗,C) is a maximal critical trio with A ⊆ A∗ and B ⊆ B∗, then CayleyC(G;A∗,B∗,C) is not a video.


Proof: Suppose (for a contradiction) that Θ = CayleyC(G;A∗,B∗,C) is a video. Since δ(A,B) > 0 = ν(A,B) it follows that δ(Θ) = δ(A∗,B∗) > ν(A∗,B∗). So, by the previous lemma the subgroups H1 = stabL(A∗), H2 = stabR(A∗) = stabL(B∗), H3 = stabR(B∗) satisfy |A∗| = 2|H2| = |B∗| and δ(Θ) = |H1| = |H3| < |H2|.

Now, on one hand, we have 2|A∗ \ A| = |A∗ \ A| + |B∗ \ B| = δ(A∗,B∗,C) − δ(A,B,C) < |H1|

so A is very eﬃciently contained in A∗ which has left stabilizer H1. On the other hand, the set B∗ = H2B contains B = x−1Ax so 2|H2| = |H2x−1Ax| = |xH2x−1A|, which means that the subgroup K = xH2x−1 satisﬁes |KA| = 2|K| = 2|H2|. Thus, A is also eﬃciently contained in KA which is left stabilized by K.

Let d = |A∗|/|H1| (so d is the number of right H1-cosets contained in A∗) and note that d ≥ 3 by assumption. Since |A∗ \ A| < 21|H1| it follows that we may choose y ∈ A so that |H1y ∩ A| > (1 − 21d)|H1| ≥ 23|H1|. Since |KA| = 2|K| it follows that we may choose z ∈ A so that |Kz ∩ H1y ∩ A| > 13|H1|. However, then Kz ∩ H1y must be a right L-coset for a subgroup L ≤ H1 ∩ K with [H1 : L] ≤ 2.

Now consider the set A = LA. Since L ≤ H1 and H1 = stabL(A∗) it must be that A ⊆ A∗ and since |A∗ \ A| < |L| we must have A = A∗. Note that this implies |A | = 2|H2| = 2|K|. However, L ≤ K so A ⊆ KA and since |A | = 2|K| we must have

- A = KA. However, this contradicts stabL(A∗) = H1, thus completing the proof.


Corollary 14.4 (Deﬁciency vs. Disparity) Let A,B ⊆ G be ﬁnite and nonempty, and assume |AB| < 2min{|A|,|B|}. Let x ∈ A and y ∈ B and assume that H ≤ G is the unique minimal subgroup for which A ⊆ xH. Then B ⊆ Hy, and one of the following holds.

- 1. Either AB = xHy or there exists K < H and z ∈ H so that x(H \ zK)y ⊆ AB.


- 2. There exists K H so that H/K is a cyclic group with |H/K| ≥ 4 so that ϕH/K(x−1A) and ϕH/K(By−1) are geometric progressions with a common ratio. Furthermore, one of the following holds.

(a) δ(A,B) ≤ 21|K| and δ(A,B) + max{|AK \ A|,|KB \ B|} ≤ |K|. (b) AKB = AB and δ(A,B) + |AK \ A| + |KB \ B| = |K|.

- 3. There exists K H so that H/K is dihedral with |H/K| ≥ 8 and sets A+ ⊇ A and

B+ ⊇ B so that A+K = A+ and KB+ = B+ and ϕH/K(x−1A+), ϕH/K(B+y−1) are dihedral progressions with a common ratio. Furthermore, one of the following holds.

- (a) δ(A,B) ≤ 12|K| and δ(A,B) + max{|A+ \ A|,|B+ \ B|} ≤ 2|K|.

- (b) AKB = AB and |K| = |B+\KB| = |A+\AK| = δ(A,B)+|AK\A|+|KB\B|.
- (c) A+B+ = AB and δ(A,B) + |A+ \ A| + |B+ \ B| = 2|K|.


- 4. There exist K1,K2,K3 ≤ H so that K1AK2BK3 = AB and furthermore


- (a) |AK2| = 2|K2| = |K2B|
- (b) δ(A,B) + |AK2 \ A| + |K2B \ B| = |K1| = |K3| < |K2|.


Furthermore, if A = B, then xH = Hx and outcome 4 may be excluded.

Proof: First we prove that B is contained in a single right H-coset. Suppose (for a contradiction) that y,z ∈ B satisfy Hy∩Hz = ∅. Then we have |AB| ≥ |A{y,z}| = 2|A| which is contradictory. Thus we have A ⊆ xH and B ⊆ Hy. Furthermore, by a similar argument, H must be the minimal subgroup so that B ⊆ Hy. Now deﬁne the sets A = x−1A and

- B = By−1. It follows that (A ,B ) is a critical pair in H. Furthermore, neither A nor B is contained in a coset of a proper subgroup of H.


Next deﬁne C = H\(A B )−1 and note that we may assume C = ∅ as otherwise the ﬁrst outcome is satisﬁed. Let (A∗,B∗,C) be a maximal trio in H with A ⊆ A∗ and B ⊆ B∗ and deﬁne Θ = CayleyC(H;A∗,B∗,C). Now the remaining part of the argument follows the proof of Corollary 14.1 with a few exceptions which we now detail.

First, if Θ is a pure or impure beat, then C must be contained in a coset of a proper subgroup, giving us the ﬁrst outcome. Second, if Θ is a video, then the bound ν(A ,B ) < δ(A ,B ) implies ν(A∗,B∗) < δ(A∗,B∗) = δ(Θ), so Lemma 14.2 implies the existence of subgroups K1,K2,K3 as given in the ﬁnal outcome.

Finally, if A = B then we may take x = y, so A ⊆ xH and A ⊆ Hx. However, this implies A ⊆ xH ∩ Hx = x(H ∩ x−1Hx) and then by the choice of H we must have x−1Hx = H. Furthermore, the sets A = x−1A and B = Ax−1 now satisfy B = xA x−1 so Lemma 14.3 implies that Θ cannot be a video, which excludes the fourth outcome.

Proof of Corollary 1.10: Applying Corollary 14.4 to the pair (A,A) implies that xH = Hx and one of the ﬁrst three outcomes of this corollary holds. The second and third outcomes of this corollary immediately yield the second and third outcomes for Corollary 1.10. If we get the ﬁrst outcome of Corollary 14.4 and AA = xHx then since |A| ≥ 2 the subgroup K = {1} < H has the desired properties. Otherwise this ﬁrst outcome gives us a subgroup K and some conjugate of K has the desired properties.

##### 14.3 Generalizing Kneser’s Theorem

In this subsection we prove Corollaries 1.4 and 1.3 which generalize of Kneser’s addition theorem. We will deduce these as corollaries of Theorem 13.11 which allows us to work primarily in the context of subsets of groups (instead of incidence geometry), however this theorem still has a conclusion concerning videos which will require us to consider these particular incidence geometries.

The corollaries we are proving here concern the notion of conjugate stability (recall that for a subgroup H ≤ G, a set A ⊆ G is H-conj-stable if for every x ∈ A there exists y ∈ G so that x(y−1Hy) ⊆ A). For a subgroup H ≤ G we deﬁne a trio (A,B,C) to be H-controlled if A,B,C are all H-conj-stable and δ(A,B,C) ≤ |H|. We say that (A,B,C) is controlled if it is H-controlled for some H ≤ G. The main result of this subsection (from which we will derive Corollaries 1.4 and 1.3) is as follows.

- Theorem 14.5 Every maximal subset trio is controlled.


Although the notion of conjugate stability is much weaker than that of stability, it does have some convenient properties, as indicated by the following straightforward observation.

Observation 14.6 Let A,B ⊆ G and let g ∈ G.

- 1. If H ≤ stabL(A) or H ≤ stabR(A), then A is H-conj-stable.
- 2. If A is H-conj-stable, then AB, BA, gA, Ag, and A−1 are all H-conj-stable.
- 3. If (A,B,C) and (A ,B ,C ) are similar subset trios, and A,B,C are H-conj-stable, then A ,B ,C are H-conj-stable.


Our proof will call upon a lemma concerning videos which we give next.

Lemma 14.7 If (A,B,C) is a subset trio and Θ = CayleyC(G;A,B,C) is a video, then (A,B,C) is controlled.

Proof: By possibly replacing (A,B,C) by a similar trio, we may assume that Θ• is isomorphic to one of the trios given in the deﬁnition of standard and exceptional video. Choose subgroups Hi ≤ G for 1 ≤ i ≤ 3 so that G/Hi × {i} is the clone partition of G × {i} given by Θ. Now, Lemma 7.1 relates the deﬁciency of Θ with the number of edges in certain edge-cuts. Two of the edge-cuts appearing in our structures have size 2d−2 where d is the degree of the graph Γ, while all of the others have size 2d − 1. We ﬁrst handle these two special cases, and then give a general argument for the others.

- Case 1: Θ• ∼= Γ : E ∼ V ∼ E for a graphic duet Γ.

In this case H1 and H3 are subgroups stabilizing edges of Γ so H1 and H3 are conjugate. Since H1 ≤ stabL(A) and H3 ≤ stabR(B) and H1 ≤ stabR(C) we have that A,B,C are all H1-conj-stable. It follows from Lemma 7.1 that δ(A,B,C) = δ(Θ) = |H1|, so (A,B,C) is

- H1-controlled.


- Case 2: Θ• ∼= Cube/Octahedron : V ∼ E ∼ F.


We may assume (without loss) that Θ• ∼= Cube : V ∼ E ∼ F. In this case, it follows immediately that A and B are H2-conj-stable since H2 ≤ stabR(A) and H2 ≤ stabL(B). To see that C is also H2-conj-stable, we shall construct another incidence geometry. For this purpose, we deﬁne the relation x a y if x and y are antipodal faces in the cube.

### V ∼ E ∼ F a F

Figure 25: An incidence geometry based on Cube

Let V = V (Cube) and E = E(Cube) and F = F(Cube). Next deﬁne an incidence geometry Λ = (V,E,F ×{1},F ×{2}) with incidence given by the following rules for every

- v ∈ V and e ∈ E and (x,1) ∈ F × {1} and (y,2) ∈ F × {2}.


- • v and e are incident in Λ if they are incident in Cube.
- • e and (x,1) are incident in Λ if e,x are incident in Cube.
- • (x,1) and (y,2) are incident in Λ if x a y.

- • there are no incidences between V and F ×{1}∪F ×{2} or between E and F ×{2}.


We already have a realization of a part of Λ using the subgroups H1,H2,H3 and the sets A and B. By applying Theorem 3.3 we may extend this by choosing a set D ⊆ G with

H3DH3 = D so that the chorus CayleyC(G;M) given by the matrix

  

  

∅ A ∅ ∅

A−1 ∅ B ∅ ∅ B−1 ∅ D ∅ ∅ D−1 ∅

M =

has quotient (G/H1 × {1},G/H2 × {2},G/H3 × {3},G/H3 × {4}) strongly isomorphic to Λ. It follows from this construction that ABD = C. Since A is H2-conj-stable, C must also be H2-conj-stable, and since δ(A,B,C) = δ(Θ) = |H2| we have that (A,B,C) is

- H2-controlled.


- Case 3: Θ• is not isomorphic to one of the videos from Case 1 or Case 2.


In all of these cases, one of the subgroups, say Hi, corresponds to the stabilizer of an edge, and another, say Hj corresponds to the stabilizer of a vertex. Choose H ≤ G to be the stabilizer of an arc. Then, H is conjugate to a subgroup of Hi and to a subgroup of Hj. Since each of the three sets A,B,C is either right or left stabilized by one of the subgroups Hi or Hj, it follows that A,B,C are all H-conj-stable. Now, the stabilizer of an arc will either be equal to the stabilizer of the corresponding edge, or a subgroup of this group of index two, so we have |H| ≥ 12|Hi|. Then by Lemma 7.1 we have δ(A,B,C) = δ(Θ) = 12|Hi| ≥ |H| which shows that (A,B,C) is H-controlled.

We are now ready for the main result of this subsection.

Proof of Theorem 14.5: Let Φ be a maximal subset trio in G. If δ(Φ) ≤ 0 then Φ is {1}-controlled, so we may assume Φ is critical. If Φ is trivial, then it is similar to (G,G,∅) so it is G-controlled. Otherwise, Φ is a nontrivial maximal critical trio, so we may apply Theorem 13.11 to obtain sequence of subset trios Φ1,...,Φm. The desired result now follows from Lemma 14.7, the following claim, and a straightforward induction.

Claim: Let (A,B,C) be a subset trio in G.

- 1. If (A,B,C) is a pure beat, pure cyclic chord, or pure dihedral chord, then (A,B,C) is controlled.
- 2. If (A,B,C) is an impure beat or an impure cyclic chord with a continuation which is K-controlled, then (A,B,C) is K-controlled.
- 3. If (A,B,C) is an impure dihedral chord of type 0 or 2B, then it is controlled. If it has type 1 or 2A with a continuation which is K-controlled, then (A,B,C) is K-controlled.


So to complete the proof, we need only to establish the claim, which we do in parts.

- Proof of 1. If (A,B,C) is either a pure beat relative to H, or a pure cyclic chord relative to H, then it follows from Observation 14.6 and our deﬁnitions that (A,B,C) is H-controlled. If (A,B,C) is a pure dihedral chord relative to H, then there exist subgroups H1,H2,H3 where each Hi has the form Hi = H ∪ F for a ﬂip F ∈ G/H so that H1AH2 = A and H2BH3 = B and H3CH1 = C. Now, in the dihedral group Dn, the subgroups of the form {1,f} where f is a ﬂip will form a single conjugacy class if n is odd, and form two conjugacy classes if n is even. It follows that we may choose 1 ≤ i < j ≤ 3 so that Hi and Hj are conjugate. Now since each of our sets A,B,C is either left or right stabilized by Hi or Hj it follows that A,B,C are all Hi-conj-stable, and since δ(A,B,C) = 2|H|, we have that (A,B,C) is Hi-controlled, as desired.
- Proof of 2. Let (A,B,C) be an impure beat or impure cyclic chord relative to H with a K-controlled continuation (so K < H). By possibly replacing (A,B,C) with a similar trio, we may assume that (A ∩ H,B ∩ H,C ∩ H) is a continuation which is a K-controlled H-trio. Now A \ H and B \ H and C \ H are all unions of either left or right H-cosets, so it follows immediately from this and the assumption that (A ,B ,C ) is K-controlled that (A,B,C) is K-controlled.
- Proof of 3. Let (A,B,C) be an impure dihedral chord relative to H and assume it has type 0, 1, 2A, or 2B. If (A,B,C) is type 0, then A,B,C are all H-stable and δ(A,B,C) = |H| so (A,B,C) is H-controlled. Next suppose that (A,B,C) is type 1 and that (A ,B ,C ) is a continuation of (A,B,C) (so (A ,B ,C ) is an H-trio) which is K-controlled. In this case, there exist R,S,T ∈ G/H so that A\R,B \S,C \T are H-stable and (A∩R,B ∩S,C ∩T) is similar to (A ,B ,C ) when viewed as subset trios of G. It follows immediately that A,B,C are K-conj-stable, and thus (A,B,C) is K-controlled.


In the remaining cases, (A,B,C) is an impure dihedral chord of type 2A or 2B and we may assume that Ω is an associated octahedral conﬁguration and that the subsets A ,B ,C ,B ,C ⊆ H and subgroups K ,K < H are as given in the deﬁnitions of these types. It follows that for every S ∈ G/H the set A∩S (B ∩S, C ∩S) is either empty, equal to S, or conjugate to A (to one of B ,B , or to one of C ,C ). If (A,B,C) has type 2A, then (A ,B ,C ) is an impure beat relative to K with a continuation which is K-controlled, so we have that A ,B ,C are all K-conj-stable and δ(A ,B ,C ) = δ(A,B,C) ≤ |K|. Since K ≤ K and for x ∈ A we have that (xK ,B ,C ) is a pure beat relative to K it must be that B and C are also K-conj-stable, and it follows that (A,B,C) is K-controlled. If (A,B,C) has type 2B, then (xK ,B ,C ) is a pure beat relative to K so these sets are K -conj-stable, and (xK ,B ,B ) is a pure beat relative to K so these sets are K -conjstable, and then for the subgroup K = K ∩K we ﬁnd that A,B,C are all K-conj-stable, and δ(A,B,C) = |A | = |K| so (A,B,C) is K-controlled, as desired.

Proof of Corollay 1.4: Let A,B ⊆ G be ﬁnite and nonempty, let C = (AB)−1 and choose A ⊆ A∗ and B ⊆ B∗ so that (A∗,B∗,C) is a maximal subset trio. By the previous theorem there exists a subgroup H so that A∗,B∗,C are H-conj-stable and |A∗| + |B∗| − |AB| = δ(A∗,B∗,C) ≤ |H|. Since A∗ is H-conj-stable and AB = A∗B∗, the set AB is also H-conjstable, and this completes the proof.

Proof of Corollary 1.3: This follows immediately from Corollary 1.4.

#### Appendix

Here we prove a result mentioned in Section 1 which is of interest in conjunction with a theorem of Freiman.

Proposition Let B ⊆ G and K ≤ G be ﬁnite and assume KBK = B and |B| = 2|K| and

- |B2| < 2|B|. Then there exist L ≤ K ≤ H ≤ G and x ∈ G so that the following hold.


- 1. B ⊆ xH = Hx
- 2. [K : L] ≤ 2
- 3. L H and H/L is either cyclic or dihedral.


Proof: Let x ∈ B and let H be the minimal subgroup for which B ⊆ xH. Suppose (for a contradiction) that B  ⊆ Hx and choose y ∈ B \ Hx. Now xHx ∩ xHy = ∅ so Bx ∩ By = ∅, but then |B2| ≥ |B{x,y}| ≥ 2|B| gives us a contradiction. Thus B ⊆ Hx ∩ xH = x(x−1Hx ∩ H) from which it follows that x−1Hx = H and thus 1 is satisﬁed. If K = stabL(B) then B is a single left H-coset and setting L = K satisﬁes the proposition. So, we may assume K = stabL(B), and by a similar argument K = stabR(B).

Now deﬁne ∆ = CayleyC(G;B) and note that K = stabL(B) = stabR(B), so we have that G/K ×{1} and G/K ×{2} are the clone partitions of G×{1} and G×{2}. Consider the sets P = H × {1} and Q = Hx × {2} and note that our construction implies that (P,Q) is a connected H-duet. Furthermore, it follows from the stability properties of B that (P,Q)• is a polygon. Deﬁne L = {g ∈ H | g ﬁxes each point in (P,Q)•} and note that by construction L H. Now K × {1} is a single point in (P,Q)• with stabilizer K, and it follows from the structure of a polygon that [K : L] ≤ 2. The action of H on (P,Q)• gives us an isomorphism from H/L to a subgroup of the automorphism group of a polygon (which is dihedral), and this yields the ﬁnal part of the proposition.

#### References

- [1] E. Balandraud, Une variante de la methode isoperimetrique de Hamidoune, appliquee au theoreme de Kneser. Ann. Inst. Fourier (Grenoble) 58 (2008), no. 3, 915-943.
- [2] T. Boothby, M. DeVos, and A. Montejano, A new proof of Kemperman’s Theorem. preprint.
- [3] E. Breuillard, B. J. Green and T. C. Tao. A nilpotent Freiman dimension lemma, arXiv:1112.4174
- [4] L. V. Brailovsky, and G. A. Freiman, On a product of ﬁnite subsets in a torsion-free group. J. Algebra 130 (1990), no. 2, 462-476.
- [5] A. Cauchy, Recherches sur les nombres, J. Ecole polytechnique 9 (1813), 99-116.
- [6] S. Chowla, A theorem on the addition of residue classes: applications to the number Γ(k) in Waring’s problem, Proc. Indian Acad. Sc., 2 (1935), 242-243.
- [7] H. Davenport, On the addition of residue classes, J. London Math. Soc. 10(1935), 30-32.
- [8] H. Davenport, A historical note, Journal of the London Mathematical Society, 22

(1947) 100-101.

- [9] G. T. Diderrich, On Kneser’s addition theorem in groups, Proc. Amer. Math. Soc. 38

(1973), 443-451.

- [10] F. J. Dyson, A theorem on the densities of sets of integers. J. London Math. Soc. 20,

(1945). 8-14.

- [11] S. Eliahou and M. Kervaire, Sumsets in dihedral groups, European J. Combin., 27

(2006) 617-628.

- [12] G. A. Freiman, On ﬁnite subsets of nonabelian groups with small doubling. Proc. Amer. Math. Soc. 140 (2012), no. 9, 2997-3002
- [13] G. A. Freiman, Inverse problems of additive number theory, On the addition of sets of residues with respect to a prime modulus, Doklady Akad. Nauk SSSR, 141 (1961), 571–573.
- [14] G. A. Freiman, Foundations of a structural theory of set addition, translated from the Russian, Translations of Mathematical Monographs, Vol 37, American Mathematical Society, Providence, RI, 1973.


- [15] G. Freiman, Groups and the inverse problems of additive number theory. Numbertheoretic studies in the Markov spectrum and in the structural theory of set addition (Russian), pp. 175-183. Kalinin. Gos. Univ., Moscow, 1973.
- [16] D. J. Grynkiewicz, Quasi-periodic decompositions and the Kemperman structure theorem, European J. Combin., 26 (2005), no. 5, 559-575.
- [17] D. J. Grynkiewicz, A step beyond Kemperman’s structure theorem. Mathematika 55

(2009), no. 1-2, 67-114.

- [18] Y. O. Hamidoune, Quelques problemes de connexite´ dans les graphes orient´es. J. Combin. Theory Ser. B 30 (1981), no. 1, 1-10.
- [19] Y. O. Hamidoune, On the connectivity of Cayley digraphs. European J. Combin. 5

(1984), no. 4, 309-312.

- [20] Y. O. Hamidoune, An isoperimetric method in additive theory. J. Algebra 179 (1996), no. 2, 622-630.
- [21] Y. O. Hamidoune, On small subset product in a group. Structure Theory of setaddition. Astrisque no. 258 (1999), xiv-xv, 281-308.
- [22] Y. O. Hamidoune, Extensions of the Scherk-Kemperman theorem. J. Combin. Theory Ser. A 117 (2010), no. 7, 974-980.
- [23] Y. O. Hamidoune, A structure theory for small sum subsets. Acta Arith. 147 (2011), no. 4, 303-327.
- [24] Y. O. Hamidoune, On Minkowski product size: The Vospers property. arXiv:1004.3010
- [25] Y. O. Hamidoune, Two Inverse results, arXiv:1006.5074
- [26] Y. O. Hamidoune, Hyper-atoms and the Kemperman’s critical pair Theory. arXiv:0708.3581
- [27] L. Husbands, Approximate Groups in Additive Combinatorics: A Review of Methods and Literature, Masters dissertation, University of Bristol, September, 2009.
- [28] J.H.B. Kemperman, On complexes in a semigroup, Indag. Math. 18 (1956), 247-254.
- [29] J. H. B. Kemperman, On small sumsets in an abelian group, Acta Mathematica, 103

(1960), 63-88.

- [30] J. H. B. Kemperman and P. Scherk, On sums of sets of integers. Canadian J. Math. 6, (1954). 238-252.


- [31] M. Kneser, Absch¨atzungen der asymptotischen Dichte von Summenmengen, Math. Z 58 (1953), 459-484.
- [32] V. F. Lev, Restricted set addition in Abelian groups: results and conjectures, Journal de thorie des nombres de Bordeaux, 17 no. 1 (2005), p. 191-203.
- [33] V. Lev, Critical Pairs in abelian groups and Kemperman’s Structure Theorem, Int. J. Number Theory 2 (2006), no. 3, 379-396.
- [34] W. Mader, Uber den Zusammenhang symmetrischer Graphen. Arch. Math. (Basel) 21 (1970) 331-336.
- [35] W. Mader, Minimale n-fach kantenzusammenhngende Graphen. Math. Ann. 191

(1971), 21-28.

- [36] H. B. Mann, An addition theorem for sets of elements of an Abelian group, Proc. Amer. Math. Soc. 4 (1953), 423.
- [37] M. B. Nathanson, Additive Number Theory: Inverse Problems and the Geometry of Sumsets, Graduate Texts in Mathematics, 165, Springer-Verlag, New York, 1996.
- [38] J. E. Olson, On the sum of two sets in a group, J. Number Theory 18 (1984), 110-120.
- [39] J. E. Olson, On the symmetric diﬀerence of two sets in a group, Europ. J. Combinatorics, (1986), 43-54.
- [40] G. Petridis, New Proofs of Plu¨nnecke-type Estimates for Product Sets in Non-Abelian Groups, arXiv:1101.3507
- [41] I. Z. Ruzsa. Generalized arithmetical progressions and sumsets, Acta Math. Hungar. 65(4) (1994), 379-388.
- [42] G. Sabidussi, Vertex-transitive graphs. Monatsh. Math. 68 (1964) 426-438.
- [43] P. Scherk, Advanced Problems and Solutions: Solutions: 4466, Amer. Math. Monthly 62 (1955), no. 1, 46-47.
- [44] P. Scherk, and J. H. B. Kemperman, Complexes in abelian groups. Canadian J. Math. 6, (1954). 230-237.
- [45] O. Serra, An isoperimetric method for the small sumset problem, Surveys in combinatorics 2005, London Math. Soc. Lecture Note Ser., 327, Cambridge Univ. Press, Cambridge (2005), 119-152.
- [46] O. Serra, and G. Z´emor, A Structure Theorem for Small Sumsets in Nonabelian Groups arXiv:1203:0654


- [47] T. Tao, Noncommutative sets of small doubling, arXiv:1106.2267
- [48] T. Tao, http://terrytao.wordpress.com/2009/11/10/an-elementary-non-commutativefreiman-theorem/
- [49] T. Tao, V. Vu, Additive Combinatorics, Cambridge University Press, 2006.
- [50] W. T. Tutte, A family of cubical graphs. Proc. Cambridge Philos. Soc. 43, (1947). 459-474.
- [51] A. G. Vosper, The critical pairs of subsets of a group of prime order, J. London Math. Soc., 31 (1956), 200-205.
- [52] A. G. Vosper, Addendum to “The critical pairs of subsets of a group of prime order,” J. London Math. Soc., 31 (1956), 280-282.
- [53] M. E. Watkins, Connectivity of transitive graphs. J. Combinatorial Theory 8 1970 23-29.
- [54] G. Z´emor, A generalisation to noncommutative groups of a theorem of Mann, Discrete Math. 126 (1994), no. 1-3, 365-372.


