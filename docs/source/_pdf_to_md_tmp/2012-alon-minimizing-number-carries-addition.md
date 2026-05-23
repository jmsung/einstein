arXiv:1209.1131v1[math.CO]5Sep2012

Minimizing the number of carries in addition

Noga Alon ∗

Abstract When numbers are added in base b in the usual way, carries occur. If two random, independent

1-digit numbers are added, then the probability of a carry is b2−b1. Other choices of digits lead to less carries. In particular, if for odd b we use the digits {−(b − 1)/2,−(b − 3)/2,...,...(b − 1)/2}

![image 1](<2012-alon-minimizing-number-carries-addition_images/imageFile1.png>)

2−1 4b2 . Diaconis, Shao and Soundararajan conjectured that this

then the probability of carry is only b

![image 2](<2012-alon-minimizing-number-carries-addition_images/imageFile2.png>)

is the best choice of digits, and proved that this is asymptotically the case when b = p is a large prime. In this note we prove this conjecture for all odd primes p.

AMS Subject Classiﬁcation: 11P99 Keywords: carry, modular addition

# 1 The problem and result

When numbers are added in base b in the usual way, carries occur. If two added one-digit numbers are random and independent, then the probability of a carry is b2−b1. Other choices of digits lead to less carries. In particular, if for odd b we use balanced digits, that is, the digits

![image 3](<2012-alon-minimizing-number-carries-addition_images/imageFile3.png>)

{−(b − 1)/2,−(b − 3)/2,... ,0,1,2,... (b − 1)/2}

then the probability of carry is only b42b−21. Diaconis, Shao and Soundararajan [4] conjectured that this is the best choice of digits, and proved that this conjecture is asymptotically correct when b = p is a

![image 4](<2012-alon-minimizing-number-carries-addition_images/imageFile4.png>)

large prime. More precisely, they proved the following.

- Theorem 1.1 ([4]) For every ǫ > 0 there exists a number p0 = p0(ǫ) so that for any prime p > p0 the probability of carry when adding two random independent one-digit numbers using any ﬁxed set of digits in base p is at least 41 − ǫ.

![image 5](<2012-alon-minimizing-number-carries-addition_images/imageFile5.png>)

The estimate given in [4] to p0 = p0(ǫ) is a tower function of 1/ǫ. Here we establish a tight result for any prime p, proving the conjecture for any prime.

- Theorem 1.2 For any odd prime p, the probability of carry when adding two random independent one-digit numbers using any ﬁxed set of digits in base p is at least p42p−21.


![image 6](<2012-alon-minimizing-number-carries-addition_images/imageFile6.png>)

![image 7](<2012-alon-minimizing-number-carries-addition_images/imageFile7.png>)

∗Sackler School of Mathematics and Blavatnik School of Computer Science, Tel Aviv University, Tel Aviv 69978, Israel. Email: nogaa@tau.ac.il. Research supported in part by an ERC Advanced grant, by a USA-Israeli BSF grant and by the Israeli I-Core program.

The proof is very short, and is in fact mostly an observation that the above result follows from a theorem of J. M. Pollard proved in the 70s. The conjecture for non-prime values of p remains open.

The proof can be extended to show that balanced digits minimize the probability of carry while adding k numbers, for any k ≥ 2.

The rest of this short note is organized as follows. The next section contains a brief description of the digit systems considered. In Section 3 we present the short derivation of Theorem 1.2 from Pollard’s Theorem, and in Section 4 we describe the proof of the extension to the addition of more than two summands.

# 2 Addition and choices of digits

A simple example illustrating the advantage of using digits that minimize the probability of carry is that of adding numbers in the ﬁnite cyclic group Zb2. Here the basis used is b. Since Zb2 is a ﬁnite group, one can choose random members of it g1,g2,... ,gn uniformly and independently and consider their sum in Zb2. Following the discussion in Section 6 of [1], consider the normal subgroup Zb ⊳ Zb2, where Zb is the subgroup of Zb2 consisting of the elements {0,b,2b,... ,(b − 1)b}.

Let A ⊂ Zb2 be a set of representatives of the cosets of Zb in Zb2. Therefore |A| = b and no two elements of A are equal modulo b. These are the digits we use. Any element g ∈ Zb2 now has a unique representation of the form g = x + y, where x ∈ A and y ∈ Zb. Indeed, x is the member of A representing the coset of Zb that contains g, and y ∈ Zb is determined by the equality g = x + y.

Suppose, now that gi = xi + yi with xi ∈ A and yi ∈ Zb is the representation of n elements gi of Zb2 that we wish to sum. We start by computing g1 + g2. To do so one ﬁrst adds x1 + x2 (in Zb2). If their sum, call it z2, is a member of A, then there is no carry in this stage. We can then compute the sum y1 + y2 in Zb, and get w2 (in this stage there is no carry, as the addition here is modulo b). Therefore, in this case the representation of g1 + g2 using our digits is g1 + g2 = z2 + w2 with z2 ∈ A and w2 ∈ Zp, and we can now proceed by induction and compute the sum of this element with g3 + g4 + ... + gn. If, on the other hand, x1 + x2  ∈ A then there is a carry. In this case we let z2 be the unique member of A so that x1 + x2 lies in the coset of Zb containing z2. This determines the element t2 ∈ Zb so that x1 + x2 = z2 + t2. The carry here is t2, and we can now proceed and compute the sum t2 +y1 +y2 in Zb getting an element w2. Therefore in this case too the unique representation of g1 + g2 using our digits is z2 + w2, but since the process of computing them involved the carry t2 the number of additions performed during the computation in the group Zb was 2 and not 1 as in the case that involved no carry.

As g1 and g2 are random independent elements chosen uniformly in Zb2, their sum is also uniform in this group, implying that the element z2 +w2 is also uniform. Therefore, when we now proceed and compute the sum of this element with g3 the probability of carry is again exactly as it has been before (though the conditional probability of a carry given that there has been one in the previous step may be diﬀerent). We conclude that the expected number of carries during the whole process of adding g1 + g2 + ··· + gn that consist of n − 1 additions is exactly (n − 1) times the probability of getting a

carry in one addition of two independent uniform random digits in the set A.

Therefore, the problem of minimizing the expected number of these carries is that of selecting the set of coset representatives A so that the probability that the addition of two random members of A in Zb2 does not lie in A is minimized.

This leads to the following equivalent formulation of Theorem 1.2.

- Theorem 2.1 Let p be an odd prime. For any subset A of the group Zp2 of integers modulo p2 so that |A| = p and the members of A are pairwise distinct modulo p, the number of ordered pairs (a,b) ∈ A×A so that a + b (mod p2)  ∈ A is at least p24−1.

![image 8](<2012-alon-minimizing-number-carries-addition_images/imageFile8.png>)

3 Adding two numbers

The result of Pollard needed here is the following.

- Theorem 3.1 (Pollard [7]) For an integer m and two sets A and B of residues modulo m, and for


any positive integer r, let Nr = Nr(A,B) denote the number of all residues modulo m that have a representation as a sum a + b with a ∈ A and b ∈ B in at least r ways. (The representations are counted as ordered pairs, that is, if a and b diﬀer and both belong to A ∩B, then a +b = b +a are two distinct representations of the sum). If (x − y,m) = 1 for any two distinct elements x,y ∈ B then for any 1 ≤ r ≤ min{|A|,|B|}:

N1 + N2 + ··· + Nr ≥ r · min{m,|A| + |B| − r}.

Note that the case r = 1 is the classical theorem of Cauchy and Davenport (see [2], [3]). The proof is short and clever, following the approach in the original papers of Cauchy and Davenport. It proceeds by induction on |B|, where in the induction step one ﬁrst replaces B by a shifted copy B′ = B − g so that I = A ∩ B′ satisﬁes 1 ≤ |I| < |B′| = |B|, and then applies the induction hypothesis to the pair (A ∪ B′,I) and to the pair (A − I,B′ − I). The details can be found in [7] (see also [6]).

Proof of Theorem 1.2: As mentioned above, the statement of Theorem 1.2 is equivalent to that of Theorem 2.1: for any subset A of the group Zp2 of integers modulo p2 so that |A| = p and the members of A are pairwise distinct modulo p, the number of ordered pairs (a,b) ∈ A × A so that a + b (mod p2)  ∈ A is at least p24−1.

![image 9](<2012-alon-minimizing-number-carries-addition_images/imageFile9.png>)

Given such a set A, note that (x−y,p2) = 1 for every two distinct elements x,y ∈ A. We can thus apply Pollard’s Theorem stated above with m = p2, A = B and r = (p − 1)/2 to conclude that

N1 + N2 + ··· + Nr ≥ r · min{p2,|A| + |B| − r} = r · (2p − r).

The sum N1+N2+···+Nr counts every element x ∈ Zp2 exactly min{r,n(x)} times, where n(x) is the number of representations of x as an ordered sum a+b with a,b ∈ A. The total contribution to this sum

arising from elements x ∈ A is at most r|A| = rp. Therefore, there are at least r(p−r) = b−21 b+12 = b24−1 ordered pairs (a,b) ∈ A × A so that a + b  ∈ A, completing the proof. ✷

![image 10](<2012-alon-minimizing-number-carries-addition_images/imageFile10.png>)

![image 11](<2012-alon-minimizing-number-carries-addition_images/imageFile11.png>)

![image 12](<2012-alon-minimizing-number-carries-addition_images/imageFile12.png>)

Remark: The above proof shows that even if we use one set of digits for one summand, a possibly diﬀerent set of digits for the second summand, and a third set of digits for the sum, then still the probability of carry must be at least b42b−21.

![image 13](<2012-alon-minimizing-number-carries-addition_images/imageFile13.png>)

# 4 Adding more numbers

The theorem of Pollard is more general than the statement above and deals with addition of k > 2 sets as well. This can be used in determining the minimum possible probability of carry in the addition of k random 1-digit numbers in a prime base p with the best choice of the p digits. In fact, for every k and every odd prime p, the minimum probability is obtained by using the balanced digits {−(p−1)/2,−(p−3/2,... ,(p−1)/2}. Therefore, the minimum possible probability of carry in adding k 1-digit numbers in a prime base p > 2 is exactly the probability that the sum of k independent random variables, each distributed uniformly on the set

{−(p − 1)/2,−(p − 3/2,... ,(p − 1)/2},

is of absolute value exceeding (p − 1)/2. Here are the details. We need the following.

- Theorem 4.1 (Pollard [7]) Let m be a positive integer and let A1,A2,... ,Ak be subsets of Zm. Assume, further, that for every 2 ≤ i ≤ k every two distinct elements x,y of Ai satisfy (x−y,m) = 1. Let A′1,A′2,... ,A′k be another collection of subsets of Zm, in which each A′i consists of consecutive elements and satisﬁes |A′i| = |Ai|. For an x ∈ Zm let n(x) denote the number of representations of x as an ordered sum of the form x = a1 + a2 + ... + ak with ai ∈ Ai, and let n′(x) denote the number of


representations of x as an ordered sum of the form x = a′1 +a′2 +··· +a′k with a′i ∈ A′i for all i. Then, for any integer r ≥ 1

min{r,n′(x)}.

min{r,n(x)} ≥

x∈Zm

x∈Zm

Corollary 4.2 Let p be an odd prime, and let A be a subset of cardinality p of Zp2. Assume, further, that the members of A are pairwise distinct modulo p. Put A′ = {−(p−1)/2,−(p−3)/2,... ,(p−1)/2}. Then, for any positive integer k, the number of ordered sums modulo p2 of k elements of A that do not belong to A is at least as large as the number of ordered sums modulo p2 of k elements of A′ that do not belong to A′.

Proof: Let r be the number of ordered sums modulo p2 of k elements of A′ whose value is precisely (p − 1)/2. It is not diﬃcult to check that for any other member g of A′ there are at least r ordered sums modulo p2 of k elements of A′ whose value is precisely g. Similarly, for any x  ∈ A′, the number of ordered sums of k elements of A′ whose value is precisely x is at most r. Indeed, the number of times an element is obtained as an ordered sum modulo p2 of k elements of A′ is a monotone non-increasing

function of its distance from 0. (This can be easily proved by induction on k). Therefore,

min{r,n′(x)} = rp +

n′(x).

x∈Zp2

x∈Zp2−A′

By Theorem 4.1 with m = p2, A1 = A2 = ... = Ak = A and the value of r above

min{r,n′(x)}.

min{r,n(x)} ≥

x∈Zp2

x∈Zp2

However, clearly,

min{r,n(x)},

rp +

n(x) ≥

x∈Zp2−A

x∈Zp2

and therefore

rp +

n(x) ≥

x∈Zp2−A

min{r,n′(x)} = rp +

n′(x).

x∈Zp2

x∈Zp2−A′

This implies that

n′(x),

n(x) ≥

x∈Zp2−A

x∈Zp2−A′

as needed. ✷

The corollary clearly implies that the minimum possible probability of carry in adding k 1-digit numbers in a prime base p > 2 is exactly the probability that the sum of k independent random variables, each distributed uniformly on the set

{−(p − 1)/2,−(p − 3/2,... ,(p − 1)/2}, is of absolute value exceeding (p − 1)/2. Remarks:

- • As in the case of two summands, the proof implies that the assertion of the last paragraph holds even if we are allowed to choose a diﬀerent set of digits for each summand and for the result.
- • After the completion of this note I learned from the authors of [4] that closely related results (for addition in Zp, not in Zp2) appear in the paper of Lev [5].


Acknowledgment Part of this work was carried out during a visit at the Georgia Institute of Technology. I would like to thank my hosts for their hospitality during this visit. I would also like to thank Persi Diaconis for an inspiring lecture in Georgia Tech in which he mentioned the problem considered here and Kannan Soundararajan for telling me about [5].

# References

- [1] A. Borodin, P. Diaconis and J. Fulman, On adding a list of numbers (and other one-dependent determinantal processes), Bull. Amer. Math. Soc. 47 (2010), 639–670.
- [2] A. L. Cauchy, Recherches sur les nombres, J. de l’Ecole´ Polytech. 9 (1813), 99-116.
- [3] H. Davenport, On the addition of residue classes, J. London Math. Soc. 10 (1935), 30–32, 1935. See also: A historical note, J. London Math. Soc. 22 (1947), 100–101.
- [4] P. Diaconis, F. Shao and K. Soundararajan, to appear.
- [5] V. Lev, Linear equations over Z/pZ and moments of exponential sums, Duke Mathematical Journal 107 (2001), 239–263.
- [6] J. M. Pollard, A generalisation of the theorem of Cauchy and Davenport, J. London Math. Soc. 8 (1974), 460–462.
- [7] J. M. Pollard, Addition properties of residue classes, J. London Math. Soc. 11 (1975), 147-152.


