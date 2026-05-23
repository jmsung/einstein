arXiv:1511.07082v3[math.CO]9Jan2018

Constructions in Ramsey theory

Dhruv Mubayi∗ Andrew Suk†

Abstract

We provide several constructions for problems in Ramsey theory. First, we prove a superexponential lower bound for the classical 4-uniform Ramsey number r4(5,n), and the same for the iterated (k − 4)-fold logarithm of the k-uniform version rk(k + 1,n). This is the ﬁrst improvement of the original exponential lower bound for r4(5,n) implicit in work of Erdo˝s and Hajnal from 1972 and also improves the current best known bounds for larger k due to the authors. Second, we prove an upper bound for the hypergraph Erdo˝s-Rogers function fkk+1,k+2(N) that is an iterated (k − 13)-fold logarithm in N. This improves the previous upper bounds that were only logarithmic and addresses a question of Dudek and the ﬁrst author that was reiterated by Conlon, Fox and Sudakov. Third, we generalize the results of Erdo˝s and Hajnal about the 3-uniform Ramsey number of K4 minus an edge versus a clique to k-uniform hypergraphs.

# 1 Introduction

- A k-uniform hypergraph H (k-graph for short) with vertex set V is a collection of k-element subsets


of V . We write Knk for the complete k-uniform hypergraph on an n-element vertex set. Given kgraphs F, G, the Ramsey number r(F,G) is the minimum N such that every red/blue coloring of

the edges of KNk results in a monochromatic red copy of F or a monochromatic blue copy of G.

In this paper, we study several problems in hypergraph Ramsey theory. We describe each problem in detail in its relevant section. Here we provide a brief summary. In Section 2, we give new lower bounds on the classical Ramsey number r(Kkk+1,Knk), improving the previous best known bounds obtained by the authors [18]. In particular, we give the ﬁrst superexponential lower bound for r(K54,Kn4) since the problem was ﬁrst explicitly stated by Erd˝os and Hajnal [12] in 1972. In Section 3, we establish a new upper bound for the hypergraph Erd˝os-Rogers function fkk+1,k+2(N) that is an iterated logarithm function in N. More precisely, we construct k-graphs on N vertices, with no copy of Kkk+2, yet every set of n vertices contains a copy of Kkk+1 where n is the (k−13)-fold iterated logarithm of N. This addresses questions posed by Dudek and the ﬁrst author [8] as well

- as by Conlon, Fox, and Sudakov [7] and signiﬁcantly improves the previous best known bound in [8] of n = O((log N)1/(k−1)). In Section 4 we study the Ramsey numbers for k-half-graphs versus


![image 1](<2015-mubayi-constructions-ramsey-theory_images/imageFile1.png>)

∗Department of Mathematics, Statistics, and Computer Science, University of Illinois, Chicago, IL, 60607 USA. Research partially supported by NSF grant DMS-1300138. Email: mubayi@uic.edu

†Department of Mathematics, University of California at San Diego, La Jolla, CA, 92093 USA. Supported by NSF grant DMS-1500153, an NSF CAREER award, and an Alfred Sloan Fellowship. Email: asuk@ucsd.edu MSC (2010): 05C15, 05C55, 05C65, 05D10, 05D40

cliques, generalizing the results of Erd˝os and Hajnal [12] about the 3-uniform Ramsey number of K4 minus an edge versus a clique. The upper bound is a straightforward extension of the method in [12], while the constructions are new.

All logarithms are base 2 unless otherwise stated. For the sake of clarity of presentation, we systematically omit ﬂoor and ceiling signs whenever they are not crucial.

# 2 A new lower bound for rk(k + 1, n)

In order to avoid the excessive use of superscripts, we use the simpler notation r(Ksk,Knk) = rk(s,n). Estimating the Ramsey number rk(s,n) is a classical problem in extremal combinatorics and has been extensively studied [13, 14, 16]. Here we study the oﬀ-diagonal Ramsey number, that is, rk(s,n) with k,s ﬁxed and n tending to inﬁnity. It is known that for ﬁxed s ≥ k +1, r2(s,n) grows polynomially in n [1, 2, 3] and r3(s,n) grows exponentially in a power of n [6]. In 1972, Erd˝os and Hajnal [12] raised the question of determining the correct tower growth rate for rk(s,n). We deﬁne the tower function twrk(x) by

twr1(x) = x and twri+1 = 2twri(x).

By applying the Erd˝os-Hajnal stepping up lemma in the oﬀ-diagonal setting (see [17]), it follows that rk(s,n) ≥ twrk−1(Ω(n)), for k ≥ 4 and for all s ≥ 2k−1 − k + 3. However they conjectured the following.

Conjecture 2.1. (Erdo˝s-Hajnal [12]) For s ≥ k + 1 ≥ 5 ﬁxed, rk(s,n) ≥ twrk−1(Ω(n)).

In [5], Conlon, Fox, and Sudakov modiﬁed the Erd˝os-Hajnal stepping-up lemma to show that Conjecture 2.1 holds for all s ≥ ⌈5k/2⌉ − 3. Recently the authors nearly proved the conjecture by establishing the following.

- Theorem 2.2 ([18]). There is a positive constant c > 0 such that the following holds. For k ≥ 4 and n > 3k, we have

- 1. rk(k + 3,n) ≥ twrk−1(cn),
- 2. rk(k + 2,n) ≥ twrk−1(clog2 n),
- 3. rk(k + 1,n) ≥ twrk−2(cn2).


Implicit in work of Erd˝os and Hajnal [12] is the bound r4(5,n) > 2cn for some absolute positive constant c. While the authors [18] recently improved this to 2cn2 above, there has been no superexponential lower bound given for this basic problem. Here we provide such a lower bound.

- Theorem 2.3. There is an absolute constant c > 0 such that r4(5,n) > 2ncloglogn,


and more generally for k > 4,

rk(k + 1,n) > twrk−2(nclog logn).

One of the building blocks we will use in our construction is the following lower bound of Conlon, Fox, and Sudakov [6]: there is an absolute positive constant c > 0 such that

r3(4,t) > 2c tlogt. (1) Our lower bound for r4(5,n) is proved via the following theorem.

- Theorem 2.4. For n suﬃciently large, we have r4(5,n) > 2r3(4,⌊(logn)/2⌋)−1.


Proof. The idea is to apply a variant of the Erd˝os-Hajnal stepping up lemma (see [17]). Set t = ⌊log2n⌋. Let φ be a red/blue coloring of the edges of the complete 3-uniform hypergraph on the vertex set {0,1,... ,r3 (4,t) − 2} without a red K43 and without a blue Kt3. We use φ to deﬁne a red/blue coloring χ of the edges of the complete 4-uniform hypergraph KN4 on the vertex set V = {0,1,... ,N − 1} with N = 2r3(4,t)−1, as follows.

![image 2](<2015-mubayi-constructions-ramsey-theory_images/imageFile2.png>)

For any a ∈ V , write a = ri=03(4,t)−2 a(i)2i with a(i) ∈ {0,1} for each i. For a = b, let δ(a,b) denote the largest i for which a(i) = b(i). Notice that we have the following stepping-up properties (again

see [17])

- Property A: For every triple a < b < c, δ(a,b) = δ(b,c) .
- Property B: For a1 < ··· < ar, δ(a1,ar) = max1≤j≤r−1 δ(aj,aj+1).

Given any 4-tuple a1 < ··· < a4 of V , consider the integers δi = δ(ai,ai+1),1 ≤ i ≤ 3. Say that δ1,δ2,δ3 forms a monotone sequence if δ1 < δ2 < δ3 or δ1 > δ2 > δ3. Now, deﬁne χ as follows:

χ(a1,a2,a3,a4) =

φ(δ1,δ2,δ3) if δ1,δ2,δ3 is monotone blue if δ1,δ2,δ3 is not monotone

Hence we have the following property which can be easily veriﬁed using Properties A and B (see [17]).

- Property C: For a1 < ··· < ar, set δj = δ(aj,aj+1) and suppose that δ1,... ,δr−1 form a monotone sequence. If χ colors every 4-tuple in {a1,... ,ar} red (blue), then φ colors every triple in {δ1,... ,δr−1} red (blue).


For sake of contradiction, suppose that the coloring χ produces a red K54 on vertices a1 < ··· < a5, and let δi = δ(ai,ai+1), 1 ≤ i ≤ 4. Then δ1,... ,δ4 form a monotone sequence and, by Property C, φ colors every triple in {δ1,... ,δ4} red which is a contradiction. Therefore, there is no red K54 in coloring χ.

Next we show that there is no blue Kn4 in coloring χ. Our argument is reminiscent of the standard argument for the bound r2(n,n) < 4n, though it must be adapted to this setting. For sake of

contradiction, suppose we have vertices a1,... ,an ∈ V such that a1 < ··· < an and χ colors every 4-tuple in the set {a1,... ,an} blue. Let δi = δ(ai,ai+1) for 1 ≤ i ≤ n − 1. We greedily construct a set Dh = {δi1,... ,δih} ⊂ {δ1,... ,δn−1} and a set Sh ⊂ {a1,... ,an} such that the following holds.

- 1. We have δi1 > ··· > δih.
- 2. For each δij = δ(aij,aij+1) ∈ Dh = {δi1,... ,δih}, consider the set of vertices A = {aij+1,aij+1+1,... ,aih,aih+1} ∪ Sh.

Then either every element in A is greater than aij or every element in A is less than aij+1. In the former case we will label δij white, in the latter case we label it black.

- 3. The indices of the vertices in Sh are consecutive, that is, Sh = {ar,ar+1,... ,as−1,as} for 1 ≤ r < s ≤ n.


We start with the D0 = ∅ and S0 = {a1,... ,an}. Having obtained Dh = {δi1,... ,δih} and Sh = {ar,... ,as}, 1 ≤ r < s ≤ n, we construct Dh+1 and Sh+1 as follows. Let δih+1 = δ(aℓ,aℓ+1) be the unique largest element in {δr,δr+1,... ,δs−1}, and set Dh+1 = Dh ∪ δih+1. The uniqueness of δih+1 follows from Properties A and B. If |{ar,ar+1,... ,aℓ}| ≥ |Sh|/2, then we set Sh+1 = {ar,ar+1,... ,aℓ}. Otherwise by the pigeonhole principle, we have |{aℓ+1,aℓ+2,... ,as}| ≥ |Sh|/2 and we set Sh+1 = {aℓ+1,aℓ+2,... ,as}.

Since |S0| = n, t = ⌊log2n⌋ and |Sh+1| ≥ |Sh|/2 for h ≥ 0, we can construct D2t = {δi1,... ,δi2t} with the desired properties. By the pigeonhole principle, at least t elements in D2t have the same label, say white. The other case will follow by a symmetric argument. We remove all black

![image 3](<2015-mubayi-constructions-ramsey-theory_images/imageFile3.png>)

labeled elements in D2t, and let {δj1,... ,δjt} be the resulting set. Now consider the vertices

- aj1,aj2,... ,ajt ∈ V . By construction and by Property B, we have aj1 < aj2 < ··· < ajt and


δ(aj1,aj2) = δij

,δ(aj2,aj3) = δij

,... ,δ(ajt,ajt+1) = δij

. Therefore we have a monotone sequence

t

1

2

δ(aj1,aj2) > δ(aj2,aj3) > ··· > δ(ajt,ajt+1).

By Property C, φ colors every triple from this set blue which is a contradiction. Therefore there is no red K54 and no blue Kn4 in coloring χ. Applying the lower bound in (1), we obtain that

![image 4](<2015-mubayi-constructions-ramsey-theory_images/imageFile4.png>)

![image 5](<2015-mubayi-constructions-ramsey-theory_images/imageFile5.png>)

![image 6](<2015-mubayi-constructions-ramsey-theory_images/imageFile6.png>)

![image 7](<2015-mubayi-constructions-ramsey-theory_images/imageFile7.png>)

r4(5,n) ≥ 2r3(4,⌊logn/2⌋)−1 > 22clognloglogn = 2ncloglogn for some absolute positive constant c and this establishes the ﬁrst part of Theorem 2.3.

We next prove Theorem 2.3 for k ≥ 5. Independently, Conlon, Fox and Sudakov [4] gave a diﬀerent proof of Theorem 2.2 part 1. Their approach was to begin with a known 4-uniform construction that yields r4(7,n) > 22cn and then use a variant of the stepping up lemma to give tower-type lower bounds for larger k. Unfortunately, this variant of the stepping up lemma does not work if one begins instead with a lower bound for r4(5,n) which is our case. However, a further variant of the approach does work, and this is what we do below.

- Lemma 2.5. For k ≥ 5 and n suﬃciently large, we have


rk(k + 1,n) ≥ 2rk−1(k,⌊n/6⌋)−1.

Proof. Again we apply a variant of the stepping-up lemma. Let φ be a red/blue coloring of the edges of the complete (k − 1)-uniform hypergraph on the vertex set {0,1,... ,rk−1(k,⌊n/6⌋) − 2} without a red Kkk−1 and without a blue K⌊kn/−16⌋. We use φ to deﬁne a red/blue coloring χ of the edges of the complete k-uniform hypergraph KNk on the vertex set V = {0,1,... ,N − 1} with N = 2rk−1(k,⌊n/6⌋)−1, as follows.

Just as above, for any a ∈ V , write a = ri=0k−1(k,⌊n/6⌋)−2 a(i)2i with a(i) ∈ {0,1} for each i. For a = b, let δ(a,b) denote the largest i for which a(i) = b(i). Hence Properties A and B hold.

Given any k-tuple a1 < a2 < ... < ak of V , consider the integers δi = δ(ai,ai+1),1 ≤ i ≤ k − 1. We say that δi is a local minimum if δi−1 > δi < δi+1, a local maximum if δi−1 < δi > δi+1, and a local extremum if it is either a local minimum or a local maximum. We say that δi is locally monotone if δi−1 < δi < δi+1 or δi−1 > δi > δi+1. Since δi−1 = δi for every i, every nonmonotone sequence δ1,... ,δk−1 has a local extremum. If δ1,... ,δk−1 form a monotone sequence, then let χ(a1,a2,... ,ak) = φ(δ1,δ2,... ,δk−1). Otherwise if δ1,... ,δk−1 is not monotone, then let χ(a1,a2,... ,ak) be red if and only if δ2 is a local maximum and δ3 is a local minimum. Hence the following generalization of Property C holds.

- Property D: For a1 < ··· < ar, set δj = δ(aj,aj+1) and suppose that δ1,... ,δr−1 form a monotone sequence. If χ colors every k-tuple in {a1,... ,ar} red (blue), then φ colors every (k−1)tuple in {δ1,... ,δr−1} red (blue).


For sake of contradiction, suppose that the coloring χ produces a red Kkk+1 on vertices a1 < ··· <

- ak+1, and let δi = δ(ai,ai+1), 1 ≤ i ≤ k. We have two cases.


- Case 1. Suppose δ1,... ,δk−1 is monotone. Then if δ2,... ,δk is also a monotone sequence, φ colors every (k − 1)-tuple in {δ1,... ,δk} red by Property D, which is a contradiction. Otherwise, δk−1 is the only local extremum and χ(a2,... ,ak+1) is blue, which is again a contradiction.
- Case 2. Suppose δ1,... ,δk−1 is not monotone. Then we know that δ2 is a local maximum and δ3 is a local minimum. However this implies that χ(a2,... ,ak+1) is blue, which is a contradiction. Hence there is no red Kkk+1 in coloring χ.


Next we show that there is no blue Knk in coloring χ. For sake of contradiction, suppose we have vertices a1,... ,an ∈ V such that a1 < ··· < an and χ colors every k-tuple blue, and let δi = δ(ai,ai+1) for 1 ≤ i ≤ n−1. By Property D, there is no integer r such that δr,δr+1,... ,δr+⌊n/6⌋ is monotone, since this implies that φ colors every (k−1)-tuple in the set {δr,δr+1,... ,δr+⌊n/6⌋} blue which is a contradiction. Therefore the sequence δ1,... ,δn−1 contains at least four local extrema. Let δj1 be the ﬁrst local maximum, and let δj2 be the next local extremum, which must be a local minimum. Recall that δj1 = δ(aj1,aj1+1) and δj2 = δ(aj2,aj2+1). Consider the k vertices

aj1−1,aj1,aj2,aj2+1,aj2+2,... ,aj2+k−3

and the sequence

δ(aj1−1,aj1),δ(aj1,aj2),δ(aj2,aj2+1),... ,δ(aj2+k−4,aj2+k−3).

By Property B we have δ(aj1,aj2) = δj1, and therefore δ(aj1,aj2) is a local maximum and δ(aj2,aj2+1) is a local minimum. Therefore χ(aj1−1,aj1,aj2,aj2+1,... ,aj2+k−3) is red and we have our contradiction. Hence there is no blue Knk in coloring χ.

![image 8](<2015-mubayi-constructions-ramsey-theory_images/imageFile8.png>)

![image 9](<2015-mubayi-constructions-ramsey-theory_images/imageFile9.png>)

![image 10](<2015-mubayi-constructions-ramsey-theory_images/imageFile10.png>)

![image 11](<2015-mubayi-constructions-ramsey-theory_images/imageFile11.png>)

By combining Theorem 2.4 with Lemma 2.5, we establish Theorem 2.3.

# 3 The Erd˝os-Rogers function for hypergraphs

An s-independent set in a k-graph H is a vertex subset that contains no copy of Ksk. So if s = k, then it is just an independent set. Let αs(H) denote the size of the largest s-independent set in H.

Deﬁnition 3.1. For k ≤ s < t < N, the Erd˝os-Rogers function fs,tk (N) is the minimum of αs(H) taken over all Ktk-free k-graphs H of order N.

To prove the lower bound fs,tk (N) ≥ n one must show that every Ktk-free k-graph of order N contains an s-independent set with n vertices. On the other hand, to prove the upper bound

fs,tk (N) < n, one must construct a Ktk-free k-graph H of order N with αs(H) < n. The problem of determining fs,tk (n) extends that of ﬁnding Ramsey numbers. Formally,

rk(s,n) = min{N : fk,sk (N) ≥ n}.

For k = 2 the above function was ﬁrst considered by Erd˝os and Rogers [15] only for t = s + 1, which might be viewed as the most restrictive case. Since then the function has been studied by several researchers culminating in the work of Wolfowitz [20] and Dudek, Retter and Ro¨dl [9] who proved the upper bound that follows (the lower bound is due to Dudek and the ﬁrst author [8]): for every s ≥ 3 there are positive constants c1 and c2(s) such that

c1

N log N log log N

![image 12](<2015-mubayi-constructions-ramsey-theory_images/imageFile12.png>)

1/2

< fs,s2 +1(N) < c2(log N)4s2N1/2.

The problem of estimating the Erd˝os-Rogers function for k > 2 appears to be much harder. Let us denote

g(k,N) = fkk+1,k+2(N) so that the above result (for s = 3) becomes g(2,N) = N1/2+o(1). Dudek and the ﬁrst author [8] proved that (log N)1/4+o(1) < g(3,N) < O(log N) and more generally that there are positive constants c1 and c2 with

c1(log(k−2) N)1/4 < g(k,N) < c2(log N)1/(k−2) (2)

where log(i) is the log function iterated i times. The exponent 1/4 was improved to 1/3 by Conlon, Fox, Sudakov [7]. Both sets of authors asked whether the upper bound could be improved (presumably to an iterated log function). Here we prove this where the number of iterations is k −O(1). It remains an open problem to determine the correct number of iterations (which may well be k − 2).

- Theorem 3.2. Fix k ≥ 14. Then g(k,N) < O(log(k−13) N).


Proof. We will proceed by induction on k. The base case of k = 14 follows from the upper bound in (2). For the inductive step, let k > 14 and assume that the result holds for k − 1. We will show that

g(k,2N) < k · g(k − 1,N), and this recurrence clearly implies the theorem. Indeed, it easily implies the upper bound

g(k,N) < 2kk!log(k−13) N by induction on k, as g(k + 1,N) is at most

g(k + 1,2⌈logN⌉) < (k + 1)g(k,⌈log N⌉)

< 2k(k + 1)!log(k−13)⌈log N⌉

≤ 2k+1(k + 1)!log(k−12) N.

Our strategy is to apply a variant of the stepping-up lemma. Let us begin with a Kkk+1−1-free (k−1)graph H′ on N vertices for which αk(H′) = g(k − 1,N). Note that this exists by deﬁnition of g(k − 1,N). We will use H′ to produce a Kkk+2-free k-graph H on 2N vertices with αk+1(H) < kαk(H′) = kg(k − 1,N).

Let V (H′) = {0,1,... ,N − 1} and V (H) = {0,1,... ,2N − 1}. For any a ∈ V (H), write a = N−1 i=0 a(i)2i with a(i) ∈ {0,1} for each i. For a = b, let δ(a,b) denote the largest i for which

a(i) = b(i). Therefore Properties A and B in the previous section hold.

Given any set of s vertices a1 < a2 < ... < as of V (H), consider the integers δi = δ(ai,ai+1),1 ≤ i ≤ s − 1. For e = (a1,... ,as), let m(e) denote the number of local extrema in the sequence δ1,... ,δs−1. In the case s = k, we deﬁne the edges of H as follows. If δ1,... ,δk−1 form a monotone sequence, then let (a1,a2,... ,ak) ∈ E(H) if and only if (δ1,δ2,... ,δk−1) ∈ E(H′). Otherwise if δ1,... ,δk−1 is not monotone, then (a1,a2,... ,ak) ∈ E(H) if and only if m(e) ∈ {k − 4,k − 3}. In other words, given that δ1,... ,δk−1 is not monotone, (a1,a2,... ,ak) ∈ E(H) if and only if δ1,... ,δk−1 has at most one locally monotone element. Note that we have the following variant of Property D.

- Property E: For a1 < ··· < ar, set δj = δ(aj,aj+1) and suppose that δ1,... ,δr−1 form a monotone sequence. If every k-tuple in {a1,... ,ar} is in E(H) (in E(H)), then every (k − 1)-tuple in {δ1,... ,δr−1} is in E(H′) (in E(H′)).


![image 13](<2015-mubayi-constructions-ramsey-theory_images/imageFile13.png>)

![image 14](<2015-mubayi-constructions-ramsey-theory_images/imageFile14.png>)

We are to show that H contains no (k + 2)-clique and αk+1(H) < kαk(H′). First let us establish the following lemma.

- Lemma 3.3. Given e = (a1,... ,a7) with a1 < ··· < a7, let δi = δ(ai,ai+1) for 1 ≤ i ≤ 6. If m(e) = 4, then there is an ai such that 2 ≤ i ≤ 6 and m(e − ai) = 2.


Proof. Suppose ﬁrst that δ2 is a local minimum, so δ1 > δ2 < δ3 > ··· . Then we have m(e−a4) = 2. Indeed, since δ4 is a local minimum, Property B implies δ(a3,a5) = δ3. If δ5 > δ3, then we have δ2 < δ(a3,a5) < δ5 and therefore m(e − a4) = 2. If δ5 < δ3, then we have δ(a3,a5) > δ5 > δ6 which again implies that m(e − a4) = 2.

Now suppose that δ2 is a local maximum, so δ1 < δ2 > δ3 < ··· . Then we have m(e − a3) = 2. Indeed, by Property B we have δ(a2,a4) = δ2. If δ4 < δ2, then we have δ(a2,a4) > δ4 > δ5 which implies m(e − a3) = 2. If δ4 > δ2, then we have δ1 < δ(a2,a4) < δ4 which again implies m(e − a3) = 2.

![image 15](<2015-mubayi-constructions-ramsey-theory_images/imageFile15.png>)

![image 16](<2015-mubayi-constructions-ramsey-theory_images/imageFile16.png>)

![image 17](<2015-mubayi-constructions-ramsey-theory_images/imageFile17.png>)

![image 18](<2015-mubayi-constructions-ramsey-theory_images/imageFile18.png>)

For sake of contradiction, suppose there are k + 2 vertices a1 < ··· < ak+2 that induce a Kkk+2 in H. Deﬁne δi = δ(ai,ai+1) for all 1 ≤ i ≤ k + 1. Given the sequence δ1,δ2,... ,δk+1, let us consider the number of locally monotone elements in D = {δ2,... ,δk}.

- Case 1. Suppose every element in D is locally monotone. Then δ1,... ,δk+1 form a monotone sequence. By Property E, every (k − 1)-tuple in the set {δ1,... ,δk+1} is an edge in H′ which is a contradiction since H′ is Kkk+1−1-free.
- Case 2. Suppose there is at least one local extremum δℓ ∈ D and at least two elements δi,δj ∈ D that are locally monotone. Then any k-tuple e ⊂ {a1,... ,ak+2} that includes the vertices

ai−1,ai,ai+1,ai+2,aj−1,aj,aj+1,aj+2,aℓ−1,aℓ,aℓ+1,aℓ+2 satisﬁes 1 ≤ m(e) < k − 4. Therefore e is not an edge in H and we have a contradiction.

- Case 3. Suppose there is exactly one element δi ∈ D that is locally monotone (and therefore at least one local extremum). Since k ≥ 15, either |{a1,... ,ai−1}| ≥ 7 or |{ai+2,... ,ak+2}| ≥ 7. Let us only consider the former case, the latter being symmetric. By Lemma 3.3, there is an element aj ∈ {a2,... ,a6} ⊂ {a1,... ,ai−1} such that for e′ = (a1,... ,a7), m(e′ −aj) = 2. Then any k-tuple e ⊂ {a1,... ,ak+2} \ {aj} that includes vertices

{at : 1 ≤ t ≤ 7,t = j} ∪ {ai−1,ai,ai+1,ai+2} satisﬁes 1 ≤ m(e) < k − 4. Hence e is not an edge in H and we have a contradiction.

- Case 4. Suppose every element in D is a local extremum. We then apply Lemma 3.3 to the set A = {a1,... ,a7} and B = {a8,... ,a14} to obtain vertices ai ∈ A and aj ∈ B such that m({a1,... ,a7} \ {ai}) = 2 and m({a8,... ,a14} \ {aj}) = 2. In particular, this implies that for e = {a1,... ,ak+2} \ {ai,aj}, the corresponding sequence of δ’s has at least two locally monotone elements. Since clearly e has at least one local extremum, we obtain 1 ≤ m(e) < k − 4. Hence e  ∈ E(H) and we have a contradiction.


Therefore we have shown that H is Kkk+2-free.

Our ﬁnal task is to show that αk+1(H) < kαk(H′). Set n = kt where t = αk(H′). Let us assume for contradiction that there are vertices a1 < ··· < an that induce a (k + 1)-independent set in H. Let δi = δ(ai,ai+1) for 1 ≤ i ≤ n − 1. If the sequence δ1,... ,δn−1 contains fewer than k

local extrema, then there is a j such that δj,... ,δj+t is monotone. Since t = αk(H′), the t + 1 vertices {δj,... ,δj+t} contain a copy of Kkk−1 in H′. Say this copy is given by δj1,... ,δjk. Then by Property E, the vertices aj1 < ··· < ajk < ajk+1 induce a copy of Kkk+1 which contradicts our assumption that {a1,... ,an} is a (k + 1)-independent set in H.

We may therefore assume that the sequence δ1,... ,δn−1 contains at least k local extrema. Now we make the following claim.

Claim 3.4. There is a set of k+1 vertices a∗1,... ,a∗k+1 ∈ {a1,... ,an} such that for δi∗ = δ(a∗i ,a∗i+1), the sequence δ1∗,... ,δk∗ has k − 2 local extrema.

Proof. Let δi1,... ,δik be the ﬁrst k extrema in the sequence δ1,... ,δn−1.

- Case 1. Suppose δi1 is a local minimum. If k is odd, then consider the k + 1 distinct vertices

e = ai1,ai1+1,ai3,ai3+1,ai5,ai5+1,... ,aik,aik+1.

Note that the pairs (ai1,ai1+1),(ai3,ai3+1),(ai5,ai5+1),... correspond to local minima. By Property B, δ(ai1+1,ai3) = δi2, δ(ai3+1,ai5) = δi4,.... Since δi2,δi4,δi6,... were local maxima in the sequence δ1,... ,δn−1, we have

δ(ai1,ai1+1) < δ(ai1+1,ai3) > δ(ai3,ai3+1) < δ(ai3+1,ai5) > ··· . Hence the vertices in e satisfy the claim. If k is even, then by the same argument as above, the k + 1 vertices

a1,ai1,ai1+1,ai3,ai3+1,ai5,ai5+1,... ,aik−1,aik−1+1 satisfy the claim.

- Case 2. Suppose δi1 is a local maximum. If k is odd, then the arguments above imply that the set of k + 1 vertices


a1,a2,ai2,ai2+1,ai4,ai4+1,... ,aik−1,aik−1+1 satisﬁes the claim. Likewise, if k is even, the set of k + 1 vertices

a1,ai2,ai2+1,ai4,ai4+1,... ,aik,aik+1 satisﬁes the claim.

![image 19](<2015-mubayi-constructions-ramsey-theory_images/imageFile19.png>)

![image 20](<2015-mubayi-constructions-ramsey-theory_images/imageFile20.png>)

![image 21](<2015-mubayi-constructions-ramsey-theory_images/imageFile21.png>)

![image 22](<2015-mubayi-constructions-ramsey-theory_images/imageFile22.png>)

By Claim 3.4, we obtain k + 1 vertices h = (a∗1,... ,a∗k+1) along with δ1∗,... ,δk∗ with the desired properties. Consider the k-tuple e = h−a∗i . If i = 1 or k+1, then it is easy to see that m(e) = k−3, which implies e ∈ E(H). For i = 2, δ3∗ is the only possible locally monotone element in the sequence δ(a∗1,a∗3),δ3∗,... ,δk∗. Therefore m(e − ai) ≥ k − 4 and e ∈ E(H). A symmetric argument for the

case i = k implies that e ∈ E(H). Therefore we can assume 3 ≤ i ≤ k −1. By Property B, we have δ(a∗i−1,a∗i+1) = max{δi∗−1,δi∗}. Let us consider the two cases.

- Case 1. Suppose δ(a∗i−1,a∗i+1) = δi∗−1. If δi∗+1 > δi∗−1, then δi∗−1 is the only element in the sequence

- δ1∗,... ,δi∗−1,δi∗+1,... ,δk∗ that is locally monotone. Hence m(e) = k − 4 and e ∈ E(H). If δi∗+1 <

δi∗−1, then δi∗+1 is the only possible element in the sequence δ1∗,... ,δi∗−1,δi∗+1,... ,δk∗ that is locally monotone. More precisely, if i = k − 1 then m(e) = k − 3, and if 3 ≤ i < k − 1 then m(e) = k − 4.

Hence m(e) ≥ k − 4 and therefore e ∈ E(H). Case 2. Suppose δ(a∗i−1,a∗i+1) = δi∗. If δi∗−2 > δi∗, then δi∗ is the only element in the sequence

- δ1∗,... ,δi∗−2,δi∗,... ,δk∗ that is locally monotone. Hence m(e) = k − 4 and e ∈ E(H). If δi∗−2 < δi∗,




then δi∗−2 is the only possible element in the sequence δ1∗,... ,δi∗−2,δi∗,... ,δk∗ that is locally monotone. More precisely, if i = 3 then m(e) = k−3, and if 3 < i ≤ k−1 then m(e) = k−4. Hence m(e) ≥ k−4

and e ∈ E(H). Therefore every k-tuple e = h − ai is an edge in H, and the k + 1 vertices h induces a Kkk+1 in H. This is a contradiction and we have completed the proof.

![image 23](<2015-mubayi-constructions-ramsey-theory_images/imageFile23.png>)

![image 24](<2015-mubayi-constructions-ramsey-theory_images/imageFile24.png>)

![image 25](<2015-mubayi-constructions-ramsey-theory_images/imageFile25.png>)

![image 26](<2015-mubayi-constructions-ramsey-theory_images/imageFile26.png>)

# 4 Ramsey numbers for k-half-graphs versus cliques

Let K43 \ e denote the 3-uniform hypergraph on four vertices, obtained by removing one edge from K43. A simple argument of Erd˝os and Hajnal [12] implies r(K43 \e,Kn3) < (n!)2. On the other hand, they also gave a construction that shows r(K43 \ e,Kn3) > 2cn for some constant c > 0. Improving either of these bounds is a very interesting open problem, as K43 \ e is, in some sense, the smallest 3-uniform hypergraph whose Ramsey number with a clique is at least exponential.

- A k-half-graph, denote by Bk, is a k-uniform hypergraph on 2k − 2 vertices, whose vertex set is of the form S ∪ T, where |S| = |T| = k − 1, and whose edges are all k-subsets that contain S, and one k-subset that contains T. The hypergraph Bk can be viewed as a generalization of K43 \ e as
- B3 = K43 \ e.


The goal of this section is to obtain upper and lower bounds for r(Bk,Knk) that parallel the known state of aﬀairs for K43 \e. We begin by presenting a straightforward generalization of the argument of Erd˝os and Hajnal to establish an upper bound for Ramsey numbers for k-half-graphs versus cliques. Again for simplicity we write r(Bk,Knk) = rk(B,n).

- Theorem 4.1. For k ≥ 4, we have rk(B,n) ≤ (n!)k−1.


First, let us recall an old lemma due to Spencer.

- Lemma 4.2 ([19]). Let H = (V,E) be a k-uniform hypergraph on N vertices. If |E(H)| > N/k, then there exists a subset S ⊂ V (H) such that S is an independent set and


1 k

|S| ≥ 1 −

![image 27](<2015-mubayi-constructions-ramsey-theory_images/imageFile27.png>)

N

N k|E(H)|

![image 28](<2015-mubayi-constructions-ramsey-theory_images/imageFile28.png>)

1 k−1

![image 29](<2015-mubayi-constructions-ramsey-theory_images/imageFile29.png>)

.

Proof of Theorem 4.1. We proceed by induction on n. The base case n = k is trivial. Let n > k and assume the statement holds for n′ < n. Let k ≥ 4 and let χ be a red/blue coloring on the edges of KNk , where N = (n!)k−1. Let ER denote the set of red edges in KNk .

- Case 1: Suppose |ER| ≤ N/k. Then one can delete N/k vertices from H and obtain a blue clique of size (1 − 1/k)N ≥ n.
- Case 2: Suppose N/k < |ER| <

(1−k1)k−1Nk

![image 30](<2015-mubayi-constructions-ramsey-theory_images/imageFile30.png>)

![image 31](<2015-mubayi-constructions-ramsey-theory_images/imageFile31.png>)

knk−1 . Then by Lemma 4.2, KNk contains a blue clique of size n.

- Case 3: Suppose |ER| ≥


(1−k1)k−1Nk

![image 32](<2015-mubayi-constructions-ramsey-theory_images/imageFile32.png>)

knk−1 . Then by averaging, there is a (k − 1)-element subset S ⊂ V such that N(S) = {v ∈ V : S ∪ {v} ∈ ER} satisﬁes

![image 33](<2015-mubayi-constructions-ramsey-theory_images/imageFile33.png>)

1 − k1 k−1 Nk nk−1 k N−1

![image 34](<2015-mubayi-constructions-ramsey-theory_images/imageFile34.png>)

≥ ((n − 1)!)k−1 .

|N(S)| ≥

![image 35](<2015-mubayi-constructions-ramsey-theory_images/imageFile35.png>)

The last inequality follows from the fact that k ≥ 4. Fix a vertex u ∈ S. If {u} ∪ T ∈ ER for some T ⊂ N(S) such that |T| = k − 1, then S ∪ T forms a red Bk and we are done. Therefore we can assume otherwise. By the induction hypothesis, N(S) contains a red copy of Bk, or a blue copy of Knk−1. We are done in the former case, and in the latter case, we can form a blue Knk by adding the vertex u.

We now move to our main new contribution, which are constructions which show that rk(B,n) is

- at least exponential in n. Theorem 4.3. For ﬁxed k ≥ 3, we have rk(B,n) > 2Ω(n).


Proof. Surprisingly, we require diﬀerent arguments for k even and k odd.

The case when k is odd. Assume k is odd, and set N = 2cn where c = c(k) will be determined later. Then let T be a random tournament on the vertex set [N], that is, for i,j ∈ [N], independently,

either (i,j) ∈ E or (j,i) ∈ E, where each of the two choices is equally likely. Then let χ : [Nk] → {red,blue} be a red/blue coloring on the k-subsets of [N], where χ(v1,... ,vk) = red if v1,... ,vk induces a regular tournament, that is, the indegree of every vertex is (k − 1)/2 (and hence the outdegree of every vertex is (k − 1)/2). Otherwise we color it blue. We note that since k is odd, a regular tournament on k vertices is possible by the fact that Kk has an Eulerian circuit, and then by directing the edges according to the circuit we obtain a regular tournament.

Notice that the coloring χ does not contain a red Bk. Indeed, let S,T ⊂ [N] such that |S| = |T| = k −1, S ∩T = ∅, and every k-tuple of the form S ∪{v} is red, for all v ∈ T. Then for any u ∈ S, all edges in the set u × T must have the same direction, either all emanating out of u or all directed towards u. Therefore it is impossible for u ∪ T to have color red, for any choice u ∈ S.

Next we estimate the expected number of monochromatic blue copies of Knk in χ. For a given k-tuple v1,... ,vk ∈ [N], the probability that χ(v1,... ,vk) = blue is clearly at most 1 − 1/2(k2).

Let T = {v1,... ,vn} be a set of t vertices in [n], where v1 < ··· < vn. Let S be a partial Steiner (n,k,2)-system with vertex set T, that is, S is a k-uniform hypergraph such that each 2-element set of vertices is contained in at most one edge in S. Moreover, S satisﬁes |S| = c′n2 where c′ = c′(k). It is known that such a system exists. Then the probability that every k-tuple in T has color blue is at most the probability that every k-tuple in S is blue. Since the edges in S are independent, that is no two edges have more than one vertex in common, the probability that T is

′n2

a monochromatic blue clique is at most 1 − 1/2(k2) |S| ≤ 1 − 1/2(k2) c

. Therefore the expected number of monochromatic blue copies of Knk in χ is at most

N n

′n2

1 − 1/2(k2) c

< 1,

for an appropriate choice for c = c(k). Hence, there is a coloring χ with no red Bk and no blue Knk. Therefore

rk(B,n) > 2cn.

The case when k is even. Assume k is even and set N = 2cn where c = c(k) will be determined later. Consider the coloring φ : [N2] → {1,... ,k − 1}, where each edge has probability 1/(k − 1) of being a particular color independent of all other edges (pairs). Using φ, we deﬁne the coloring χ : [Nk] → {red,blue}, where the k-tuple (v1,... ,vk) is red if φ is a proper edge-coloring on all pairs among {v1,... ,vk}, that is, each of the k −1 colors appears as a perfect matching. Otherwise we color it blue.

Notice that the coloring χ does not contain a red Bk. Indeed let S,T ⊂ [N] such that |S| = |T| = k − 1 and S ∩ T = ∅. If, for all v ∈ T, the k-tuples of the form S ∪ {v} are red, then the set of edges {u} × T is monochromatic with respect to φ for any u ∈ S. Hence, χ could not have colored {u} ∪ T red for any u ∈ S.

For a given k-tuple v1,... ,vk ∈ [N], the probability that χ(v1,... ,vk) = blue is at most 1−(1/(k− 1))(k2). By the same argument as above, the expected number of monochromatic blue copies of Knk with respect to χ is less than 1 for an appropriate choice of c = c(k). Hence, there is a coloring χ with no red Bk and no blue Knk. Therefore

rk(B,n) > 2cn and the proof is complete.

Acknowledgment. We thank the referee for helpful comments.

![image 36](<2015-mubayi-constructions-ramsey-theory_images/imageFile36.png>)

![image 37](<2015-mubayi-constructions-ramsey-theory_images/imageFile37.png>)

![image 38](<2015-mubayi-constructions-ramsey-theory_images/imageFile38.png>)

![image 39](<2015-mubayi-constructions-ramsey-theory_images/imageFile39.png>)

# References

- [1] M. Ajtai, J. Komlo´s, E. Szemere´di, A note on Ramsey numbers, J. Combin. Theory Ser. A 29


(1980), 354–360.

- [2] T. Bohman, The triangle-free process, Adv. Math. 221 (2009), 1653–1677.
- [3] T. Bohman, P. Keevash, The early evolution of the H-free process, Invent. Math. 181 (2010), 291–336.
- [4] D. Conlon, J. Fox, B. Sudakov, personal communication.
- [5] D. Conlon, J. Fox, and B. Sudakov, An improved bound for the stepping-up lemma, Discrete Applied Mathematics 161 (2013), 1191–1196.
- [6] D. Conlon, J. Fox, and B. Sudakov, Hypergraph Ramsey numbers, J. Amer. Math. Soc. 23

(2010), 247–266.

- [7] D. Conlon, J. Fox, and B. Sudakov, Short proofs of some extremal results, Combin. Probab. Comput. 23 (2014), 8–28.
- [8] A. Dudek, D. Mubayi, On generalized Ramsey numbers for 3-uniform hypergraphs, J. Graph Theory 76 (2014), 217–223.
- [9] A. Dudek, T. Retter, V. Ro¨dl, On generalized Ramsey numbers of Erd˝os and Rogers, J. Combin. Theory Ser. B 109 (2014), 213–227.
- [10] J. Fox, J. Pach, B. Sudakov, A. Suk, Erd˝os-Szekeres-type theorems for monotone paths and convex bodies, Proc. Lond. Math. Soc. 105 (2012), 953–982.
- [11] P. Erd˝os, Some remarks on the theory of graphs, Bull. Amer. Math. Soc. 53 (1947), 292–294.
- [12] P. Erd˝os, A. Hajnal, On Ramsey like theorems, problems and results, in Combinatorics (Proc. Conf. Combinatorial Math., Math. Inst., Oxford, 1972), pp. 123–140, Inst. Math. Appl., Southhend-on-Sea, 1972.
- [13] P. Erd˝os, A. Hajnal, R. Rado, Partition relations for cardinal numbers, Acta Math. Acad. Sci. Hungar. 16 (1965), 93–196.
- [14] P. Erd˝os, R. Rado, Combinatorial theorems on classiﬁcations of subsets of a given set, Proc. Lond. Math. Soc. 3 (1952), 417–439.
- [15] P. Erd˝os, C.A. Rogers, The construction of certain graphs, Canad. J. Math. 14 (1962), 702– 707.
- [16] P. Erd˝os, G. Szekeres, A combinatorial problem in geometry, Compos. Math. 2 (1935), 463–470.
- [17] R. L. Graham, B. L. Rothschild, J. H. Spencer: Ramsey Theory, 2nd ed., Wiley, New York, 1990.
- [18] D. Mubayi, A. Suk, Oﬀ-diagonal hypergraph Ramsey numbers, J. Combin. Theory Ser. B 125

(2017), 168–177.

- [19] J. Spencer, Tura´n theorem for k-graphs, Disc. Math. 2 (1972), 183–186.
- [20] G. Wolfowitz, K4-free graphs without large induced triangle-free subgraphs, Combinatorica 33 (2013), no. 5, 623–631.


