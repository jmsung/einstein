arXiv:1102.2853v2[math.CO]12Mar2011

An extension of the Moser-Tardos algorithmic local lemma

Wesley Pegden∗ March 12, 2011

Abstract

A recent theorem of Bissacot, et al. proved using results about the cluster expansion in statistical mechanics extends the Lova´sz Local Lemma by weakening the conditions under which its conclusions holds. In this note, we prove an algorithmic analog of this result, extending Moser and Tardos’s recent algorithmic Local Lemma, and providing an alternative proof of the theorem of Bissacot, et al. applicable in the Moser-Tardos algorithmic framework.

# 1 Introduction

If events A1,A2,...,An are independent, then we have P( A ¯i)) > 0 so long

- as P(Ai) < 1 for each i. A central tool in probabilistic combinatorics is the Lov´asz Local Lemma proved by Erdo˝s and Lov´asz [5], which can be seen as generalizing this simple fact to situations where some dependencies among the


Ai are allowed, in exchange for better bounds on the probabilities P(Ai).

The Local Lemma is commonly presented through the framework of a dependency graph on the events Ai, where if C is any family of non-neighbors of some Ai, then we have that Ai is independent of the family C of events. The Lov´asz Local Lemma is then as follows:

- Theorem 1.1 (Lov´asz Local Lemma). Let G be any dependency graph for a


ﬁnite family A of events, and suppose that there are real numbers 0 < xA < 1 (A ∈ A) such that for all A ∈ A we have

P(A) ≤ xA

(1 − xB). (1)

B∼A

Then

A¯ >

P

(1 − xA),

A∈A

A∈A

![image 1](<2011-pegden-extension-moser-tardos-algorithmic-local_images/imageFile1.png>)

∗Courant Institute of Mathematical Sciences, New York University, 251 Mercer St, Rm 921, New York, NY 10012 Email: pegden@math.nyu.edu. Partially supported by NSF MSPRF grant 1004696.

and so in particular, we have

P

A¯ > 0. (2)

A∈A

The ﬁrst breakthrough in ﬁnding an algorithmic version of the Local Lemma was made by Beck, who demonstrated his method on the classical Local Lemma application to 2-colorable hypergraphs. Beck’s method was subsequently reﬁned and given a more general framework [1,4,9,14], but required stronger bounds on the probabilities of the events than were required by the nonalgorithmic version.

In Moser and Tardos’ recent breakthrough paper [10], they give an algorithmic proof of the Lov´asz Local Lemma in a setting which is general enough for nearly all applications of the Lemma in combinatorics, with bounds identical to those required by the nonalgorithmic version. In the framework Moser and Tardos consider, the events in A depend on some underlying set V of independent random variables, and they denote by vbl(A) (A ∈ A) the minimal set of random variables from V on which each A depends; A is said to be ‘violated’ with respect to a particular evalation of the variables in vbl(A) if the event occurs for that evaluation. A Moser-Tardos dependency graph is one which implies that if events A and B are nonadjacent, then vbl(A) is disjoint from vbl(B). (Note that this notion of a dependency graph is more restrictive than the Lov´asz version based on probabilistic independence, as is demonstrated by an example of Kolipaka and Szegedy [8].) Moser and Tardos’s theorem is then the following:

- Theorem 1.2 (Moser and Tardos). Let V be a ﬁnite set of mutually independent variables in a probability space, and let A be a ﬁnite family of events determined by these variables. If there are real numbers 0 < xA < 1 (A ∈ A) such that


P(A) ≤ xA

(1 − xB) (3)

B∼A

then there exists an assignment to the variables V which corresponds to no occurrence of any event from A. Moreover, the randomized algorithm described below resamples an event A at most an expected x

1−xA times before ﬁnding the evaluation, thus the total number of resampling steps is A∈A x

A

![image 2](<2011-pegden-extension-moser-tardos-algorithmic-local_images/imageFile2.png>)

1−xA in expectation.

A

![image 3](<2011-pegden-extension-moser-tardos-algorithmic-local_images/imageFile3.png>)

The Moser-Tardos algorithm consists just of beginning with a random evaluation of all the variables in V, and then resampling vbl(A) for any violated events A until no violated events remain. Of course, the eﬃciency of the algorithm depends on the ability to resample variables eﬃciently and check whether individual events are violated; this is generally an easy implementation problem, however, making the analysis of the number of resampling steps the important issue.

Recently, Bissacot, Ferna´ndez, Procacci and Scoppola proved the following improvement of the Lov´asz Local Lemma:

- Theorem 1.3 (Bissacot, et al. [3]). Consider a ﬁnite family A of events in some probability space Ω, with some dependency graph G. If there are real numbers

- 0 < µA < ∞ such that


P(A) ≤

µA

![image 4](<2011-pegden-extension-moser-tardos-algorithmic-local_images/imageFile4.png>)

I⊂Γ(¯ A) I indep.

B∈I

µB

(4)

then P

A∈A

A¯ > 0.

It is not diﬃcult to check that condition (4) is weaker than condition (1) by considering the substitution µA = x

A

![image 5](<2011-pegden-extension-moser-tardos-algorithmic-local_images/imageFile5.png>)

1−xA. (Condition (1) would be equivalent to (4) without the condition in the sum that the sets I be independent.) In [3], they also give examples where this theorem improves some classical theorems proved with the Local Lemma. Theorem 1.3 has also since been applied to improve some theorems on graph colorings in [11].

Their proof of Theorem 1.3 is based on Shearer’s characterization of labeled dependency graphs to which the conclusion of the Local Lemma applies [13] and two of those authors’ recent results on the radius of convergence of logs of partition functions [7]. (The connection between the Local Lemma and the partition functions of statistical mechanics was ﬁrst made by Scott and Sokal [12].)

In this short note, we prove an algorithmic analog to the result of Bissacot, et. al. That is, we will show that in the setting of Moser and Tardos’s algorithmic Local Lemma, Moser and Tardos’s bounds on the running time of their algorithm hold even with their condition (3) replaced with condition (4):

- Theorem 1.4. Let V be a ﬁnite set of mutually independent variables in a probability space, and let A be a ﬁnite family of events determined by these variables. If there are real numbers 0 < µA < ∞ (A ∈ A) such that


µA

, (5)

P(A) ≤

![image 6](<2011-pegden-extension-moser-tardos-algorithmic-local_images/imageFile6.png>)

µB

I⊂Γ(¯ A) I indep.

B∈I

then there exists an assignment to the variables V which corresponds to no occurrence of any event from A. Moreover, the Moser-Tardos algorithm resamples an event A at most an expected µA times before ﬁnding the evaluation, thus the total number of resampling steps is

µA in expectation.

A∈A

(The running time bound here is equivalent to the Moser-Tardos bound under the substituation µA = x

1−xA.)

A

![image 7](<2011-pegden-extension-moser-tardos-algorithmic-local_images/imageFile7.png>)

The proof of Theorem 1.4 consists simply of re-doing one part of the proof of Moser and Tardos’s theorem, taking advantage of some constraints which were not necessary for Moser and Tardos’s original result.

Theorem 1.4 can be seen as doing two things: ﬁrst, it extends the result of Moser and Tardos by giving a weaker condition under which the identical

result holds—note that this has also been done in a more general sense by Kolipaka and Szegedy [8], who directly connect Shearer’s condition with the Moser/Tardos algorithmic framework. Secondly, it gives an alternative proof of the result of Bissacot, et al. (in the slightly more restrictive algorithmic setting) which is independent of Shearer’s theorem and the cluster expansion methods used in [7].

Bissacot, et al. note that their Theorem 1.3 can be extended to Lopsided dependency graphs, ﬁrst considered by Erdo˝s and Spencer in [6]. In their paper on their algorithmic Local Lemma, Moser and Tardos deﬁne an analog of lopsidependency in the algorithm/variable setting, and a reader familiar with Moser and Tardos’s paper can easily verify that our improvement to Moser and Tardos’s theorem applies to their theorem on algorithmic lopsided dependency graphs as well, as we only re-do their branching argument, which is applied to the lopsided case in the same way as in their main result.

# 2 Proof

The Moser-Tardos algorithm is as follows:

- 1: procedure Moser-Tardos(P)
- 2: for all P ∈ P do
- 3: vP ←(random evaluation of P)
- 4: end for
- 5: while ∃A s.t. A is violated when P = vP (∀P) do
- 6: for all P ∈ vbl(A) do
- 7: vP ←(new random evaluation of P)
- 8: end for
- 9: end while
- 10: end procedure (Note that when multiple events exist satisfying line 5, one of the satisfying events is chosen arbitrarily.)


Moser and Tardos’ proof that this algorithm terminates in polynomial time (under condition (3)) is based on the notion of a ‘witness tree’. As the algorithm runs and bad events are found and resampled, a witness tree is assigned to each step of the algorithm (where a step consists of a resampling of an event). A witness tree is a rooted tree with labels from A. The witness tree Wt for step t of the algorithm is constructed as follows: choose as its root a vertex labeled with whatever event A0 was resampled at step t. If the event A1 which was resampled at step t − 1 overlaps the label of the root, a vertex is added as a child of the root labeled with A1. (We may have A1 = A0.) In general, for each step i = t − 1,t − 2,...,1 of the algorithm, if the event Ai which was added

- at step i overlaps any of the events currently labels of vertices of our partially constructed Wt, we add a vertex labeled with Ai as the child of a vertex of maximum depth whose label overlaps Ai. In the result, Wt, children always overlap their parents, and children of a common parent always get distinct


labels (otherwise, whichever was added after the other would have been added as a child of the other). Any tree T with labels from A with these two properties is called a proper witness tree.

Moser and Tardos’s proof of their algorithm’s eﬃciency consists of two parts: ﬁrst, they show that any proper witness tree T has probability at most

P(Av) (6)

v∈T

of occurring as a witness tree at any point in the running of the algorithm, where here Av denotes the event labeling the vertex v.

Now, if an event A is resampled at step t, the number of occurrences of A as a label in the witness tree Wt is equal to the number of times A has been resampled on steps 1,...,t—in particular, all witness trees which will occur in a run of the algorithm will be distinct. Thus if we let TA denote the set of proper witness trees with root label A, the expected value of the number NA of resamplings of A which occur in a run of the algorithm is equal to

E(NA) =

P(T occurs in the log) ≤

P(Av). (7)

T∈TA

T∈TA v∈T

The second part of Moser and Tardos’s proof consists of bounding the sum of products in line (7). They do this by considering a random process for constructing trees: Suppose xA (A ∈ A) are real numbers between 0 and 1. Fix now any event A0. In the ﬁrst round of the process, a vertex labeled A0 is created. In each subsequent round, for each event vertex v with label Av created in the previous round, and for each event Au ∈ Γ(¯ Av) (in the dependency graph), a vertex u with label Au is added as a child of v with probability xA

. (All of these choices are are made independently.)

u

Moser and Tardos prove:

- Lemma 2.1 (Moser Tardos Branching Lemma). For any proper witness tree T


with root labeled A0, the probability pT that the process above produces exactly the tree T is

1 − xA

0

pT =

(1 − xB) . (8)

xA

![image 8](<2011-pegden-extension-moser-tardos-algorithmic-local_images/imageFile8.png>)

v

xA

0 v∈T

B∼Av

![image 9](<2011-pegden-extension-moser-tardos-algorithmic-local_images/imageFile9.png>)

![image 10](<2011-pegden-extension-moser-tardos-algorithmic-local_images/imageFile10.png>)

![image 11](<2011-pegden-extension-moser-tardos-algorithmic-local_images/imageFile11.png>)

![image 12](<2011-pegden-extension-moser-tardos-algorithmic-local_images/imageFile12.png>)

Thus, the Lemma gives us that

1 − xA xA T∈T

1 ≥

pT ≥

![image 13](<2011-pegden-extension-moser-tardos-algorithmic-local_images/imageFile13.png>)

A v∈T

T∈TA

(1 − xB) (9)

xA

v

B∼Av

Thus the bound P(A) ≤ (xA B∼A(1 − xB)) for all A implies, together with line (7), that

xA 1 − xA

. (10)

E(NA) ≤

![image 14](<2011-pegden-extension-moser-tardos-algorithmic-local_images/imageFile14.png>)

Our improvement comes just from a slightly more careful branching argument. Note that any witness tree which occurs in the log of the algorithm has the property that any children of a common vertex have labels which are nonadjacent in the dependency graph. This condition—let’s call it strongly proper—is stronger than requiring simply that children be distinct. Thus, we can strengthen line 7, as we have the bound

E(NA) =

P(T occurs in the log) ≤

P(Av). (11)

T∈TAS v∈T

T∈TAS

where TAS ⊂ TA is the set of strongly proper witness trees.

To bound the sum in (11), we consider a modiﬁed branching process which proceeds as follows.

Given real numbers 0 < µA < ∞, we deﬁne xA = µ

µA+1 (note that 0 < xA <

A

![image 15](<2011-pegden-extension-moser-tardos-algorithmic-local_images/imageFile15.png>)

- 1) and ﬁx any event A0. In the ﬁrst round of the process, a vertex labeled A0 is created. In each subsequent round, for each event vertex v with label Av in the previous round, we carry out a ‘subprocess’, where for each Au ∈ Γ(¯ v) (in the dependency graph), a vertex u with label Au is added as a child of v with


(the choices are independent). At the end of the subprocess, we check if the label-set of the resulting set of children for v is an independent set in the dependency graph. If it is not, we delete the children created and restart the subprocess. Note that xA < 1 (for all A) implies that the subprocess will eventually end (with probability 1) having produced an independent set.

probability xA

u

Note that the process described above is equivalent to one in which, in each round and for each vertex v from the previous round, we create a set of children

- u with labels from a set chosen from all independent sets Iv ⊂ Γ(¯ v), where the likelihood of the choice of each independent set Iv is weighted according the the product


 

)

w(Iv) =

(1 − xA

xA

 .

u

u

u∈Γ(¯ v)\Iv

u∈Iv

- Lemma 2.2 (Improved Branching Lemma). For any strongly proper witness


tree T with root labeled A0, the probability p′T that the modiﬁed branching process described above produces exactly the tree T is

p′T = µ−A1

0

v∈T

µA

u

. (12)

![image 16](<2011-pegden-extension-moser-tardos-algorithmic-local_images/imageFile16.png>)

µA

I⊂Γ(¯ Av) I indep.

A∈I

Proof. Letting Wv = Γ¯G(Av) \ ℓ(Γ+T (v)), where ℓ(v) is the label of vertex v, we have

(1 − xB)

xA

u

B∈Wv

u∈Γ+T (v)

p′T =

.

![image 17](<2011-pegden-extension-moser-tardos-algorithmic-local_images/imageFile17.png>)

(1 − xB)

xA

v∈T

I⊂Γ(¯ Av) I indep.

B∈Γ¯G(Av)\I

A∈I

This can be rewritten as

p′T =

xA

u

![image 18](<2011-pegden-extension-moser-tardos-algorithmic-local_images/imageFile18.png>)

1 − xA

u

u∈Γ+T (v)

xA 1 − xA

![image 19](<2011-pegden-extension-moser-tardos-algorithmic-local_images/imageFile19.png>)

v∈T

![image 20](<2011-pegden-extension-moser-tardos-algorithmic-local_images/imageFile20.png>)

I⊂Γ(¯ Av) I indep.

A∈I

G(Av)(1−xB). Since taking the double product v∈T u∈Γ+

by dividing the top and bottom by B∈Γ¯

0}, where

T(v) is a equivalent to taking a product v∈T\{v

- v0 denotes the root vertex of T, this gives line (12), recalling that xA = µ


A

![image 21](<2011-pegden-extension-moser-tardos-algorithmic-local_images/imageFile21.png>)

µA+1 and so x

1−xA = µA. This is applied now in the same way as the branching lemma used by Moser

![image 22](<2011-pegden-extension-moser-tardos-algorithmic-local_images/imageFile22.png>)

![image 23](<2011-pegden-extension-moser-tardos-algorithmic-local_images/imageFile23.png>)

![image 24](<2011-pegden-extension-moser-tardos-algorithmic-local_images/imageFile24.png>)

A

![image 25](<2011-pegden-extension-moser-tardos-algorithmic-local_images/imageFile25.png>)

![image 26](<2011-pegden-extension-moser-tardos-algorithmic-local_images/imageFile26.png>)

and Tardos, but with regards to the family TAS of strongly proper witness trees rooted with A, instead of the family TA of proper witness trees rooted with A. We have

µA

p′T ≥ µ−A1

u

1 ≥

. (13)

![image 27](<2011-pegden-extension-moser-tardos-algorithmic-local_images/imageFile27.png>)

0

µA

T∈TAS v∈T

T∈TAS

I⊂Γ(¯ Av) I indep.

A∈I

Putting this together with line (11), we see then that the condition (5) of the theorem implies that

E(NA) ≤ µA, (14)

completing the proof the the Moser-Tardos algorithm still terminates in expected time

µA.

A∈A

![image 28](<2011-pegden-extension-moser-tardos-algorithmic-local_images/imageFile28.png>)

![image 29](<2011-pegden-extension-moser-tardos-algorithmic-local_images/imageFile29.png>)

![image 30](<2011-pegden-extension-moser-tardos-algorithmic-local_images/imageFile30.png>)

![image 31](<2011-pegden-extension-moser-tardos-algorithmic-local_images/imageFile31.png>)

Acknowledgement I’d like to thank Joel Spencer for some helpful discussions on this note.

# References

- [1] N. Alon. A parallel algorithmic version of the local lemma, Random Structures and Algorithms 2 (1991) 367378.
- [2] J´oszef Beck. An Algorithmic Approach to the Lov´asz Local Lemma, Random Structures and Algorithms 2 (1991) 343–365.
- [3] R. Bissacot, R. Ferna´ndez, A. Procacci, B. Scoppola. Title: An Improvement of the Lovsz Local Lemma via Cluster Expansion. http://arxiv.org/abs/0910.1824v2 (10 pages).


- [4] A. Czumaj and C. Scheideler. Coloring non-uniform hypergraphs: a new algorithmic approach to the general Lov´asz local lemma, Symposium on Discrete Algorithms (2000) 3039.
- [5] P. Erdo˝s and L. Lov´asz. Problems and results on 3-chromatic hypergraphs and some related questions, in Inﬁnite and Finite sets II, North-Holland, pp. 609627, A. Hajnal, R. Rado, and V. T. So´s (Eds.) (1975).
- [6] P. Erdo˝s, J. Spencer. Lopsided Lov´asz Local Lemma and Latin transversals, Discrete Applied Math. 30 (1991) 151–154.
- [7] R. Fernandez, A. Procacci. Cluster expansion for abstract polymer models: New bounds from an old approach. Communications in Mathematical Physics 274 (2007) 123–140 (2007).
- [8] K. Kolipaka, M. Szegedy. Moser and Tardos meet Lov´asz. Manuscript

(2010).

- [9] M. Molloy and B. Reed. Further Algorithmic Aspects of the Local Lemma, Proceedings of the 30th Annual ACM Symposium on the Theory of Computing (1998) 524529.
- [10] R. Moser and G. Tardos. A constructive proof of the general Lov´asz Local Lemma, J. ACM 57 (2010) Article 11, 15 pages.
- [11] S. Ndreca, A. Procacci, B. Scoppola. Improved bounds on coloring of graphs, http://arxiv.org/abs/1005.1875.
- [12] A. Scott and A. Sokal. The repulsive lattice gas, the independent-set polynomial, and the Lov´asz local lemma, J. Stat. Phys. 118 (2005) 11511261.
- [13] J. Shearer. On a problem of Spencer, Combinatorica 5 (1985), 241-245.
- [14] A. Srinivasan. Improved algorithmic versions of the Lov´asz Local Lemma, Proceedings of the nineteenth annual ACM-SIAM symposium on Discrete algorithms (SODA) (2008) 611620.


