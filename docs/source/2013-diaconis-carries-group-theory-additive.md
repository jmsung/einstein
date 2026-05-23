---
type: source
kind: paper
title: Carries, group theory, and additive combinatorics
authors: Persi Diaconis, Xuancheng Shao, Kannan Soundararajan
year: 2013
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/1309.0434v1
source_local: ../raw/2013-diaconis-carries-group-theory-additive.pdf
topic: general-knowledge
cites:
---

CARRIES, GROUP THEORY, AND ADDITIVE COMBINATORICS

arXiv:1309.0434v1[math.CO]2Sep2013

PERSI DIACONIS, XUANCHENG SHAO, KANNAN SOUNDARARAJAN

1. Introduction

When numbers are added in the usual way carries occur along the route. These carries cause a mess and it is natural to seek ways to minimize them. This paper proves that balanced arithmetic minimizes the proportion of carries. It also positions carries as cocycles in group theory and shows that if coset representatives for a ﬁnite-index normal subgroup H in a group G can be chosen so that the proportion of carries is less than 2/9, then there is a choice of coset representatives where no carries are needed (in other words, the extension splits). Finally, our paper makes the link between the problems above and the emerging ﬁeld of additive combinatorics. Indeed the tools and techniques of this ﬁeld are used in our proofs, and our examples provide an elementary introduction.

- 1.1. Carries.


- Example 1.1. Table 1 shows a carries matrix for base b = 10. Thus when 0 is added to one of the digits 0, 1, · · · , b− 1, no carries occur. When 1 is added, there is a carry of b at b−1. There is a carry of b in position i, j if and only if i + j ≥ b.


Table 1. Carries matrix for b = 10. There is a carry of b if and only if i + j ≥ b.

![image 1](<2013-diaconis-carries-group-theory-additive_images/imageFile1.png>)

![image 2](<2013-diaconis-carries-group-theory-additive_images/imageFile2.png>)

0 1 2 3 4 5 6 7 8 9

![image 3](<2013-diaconis-carries-group-theory-additive_images/imageFile3.png>)

- 0 0 0 0 0 0 0 0 0 0 0

![image 4](<2013-diaconis-carries-group-theory-additive_images/imageFile4.png>)

![image 5](<2013-diaconis-carries-group-theory-additive_images/imageFile5.png>)

- 1 0 0 0 0 0 0 0 0 0 b

![image 6](<2013-diaconis-carries-group-theory-additive_images/imageFile6.png>)

![image 7](<2013-diaconis-carries-group-theory-additive_images/imageFile7.png>)

- 2 0 0 0 0 0 0 0 0 b b

![image 8](<2013-diaconis-carries-group-theory-additive_images/imageFile8.png>)

![image 9](<2013-diaconis-carries-group-theory-additive_images/imageFile9.png>)

- 3 0 0 0 0 0 0 0 b b b

![image 10](<2013-diaconis-carries-group-theory-additive_images/imageFile10.png>)

![image 11](<2013-diaconis-carries-group-theory-additive_images/imageFile11.png>)

- 4 0 0 0 0 0 0 b b b b

![image 12](<2013-diaconis-carries-group-theory-additive_images/imageFile12.png>)

![image 13](<2013-diaconis-carries-group-theory-additive_images/imageFile13.png>)

- 5 0 0 0 0 0 b b b b b

![image 14](<2013-diaconis-carries-group-theory-additive_images/imageFile14.png>)

![image 15](<2013-diaconis-carries-group-theory-additive_images/imageFile15.png>)

- 6 0 0 0 0 b b b b b b

![image 16](<2013-diaconis-carries-group-theory-additive_images/imageFile16.png>)

![image 17](<2013-diaconis-carries-group-theory-additive_images/imageFile17.png>)

- 7 0 0 0 b b b b b b b

![image 18](<2013-diaconis-carries-group-theory-additive_images/imageFile18.png>)

![image 19](<2013-diaconis-carries-group-theory-additive_images/imageFile19.png>)

- 8 0 0 b b b b b b b b

![image 20](<2013-diaconis-carries-group-theory-additive_images/imageFile20.png>)

![image 21](<2013-diaconis-carries-group-theory-additive_images/imageFile21.png>)

- 9 0 b b b b b b b b b


![image 22](<2013-diaconis-carries-group-theory-additive_images/imageFile22.png>)

![image 23](<2013-diaconis-carries-group-theory-additive_images/imageFile23.png>)

![image 24](<2013-diaconis-carries-group-theory-additive_images/imageFile24.png>)

![image 25](<2013-diaconis-carries-group-theory-additive_images/imageFile25.png>)

The ﬁrst author is supported in part by NSF grant DMS 08-04324. The third author is supported in part by NSF grant DMS-1001068, and a Simons Investigator award from the Simons Foundation.

1

For an arbitrary base b > 1 with digits 0, 1, . . ., b − 1, the corresponding matrix has 2 b

carries. If the digits are chosen uniformly at random, the chance of a carry is 2 b /b2 = 12 − 21b. This is 45% when b = 10.

![image 26](<2013-diaconis-carries-group-theory-additive_images/imageFile26.png>)

![image 27](<2013-diaconis-carries-group-theory-additive_images/imageFile27.png>)

If bZ ⊂ Z is the subgroup {0, ±b, ±2b, · · ·} and coset representatives are chosen as {0, 1, 2, · · · , b − 1}, the carries are cocycles [21]: i + j = (i + j)b + f(i, j) with (i + j)b the sum modulo b and f(i, j) the ‘remainder’. Here f(i, j) = 0 when i+j < b and f(i, j) = b when i + j ≥ b. It is natural to ask if some other choice of coset representatives has fewer carries. The answer is classically known.

- Example 1.2. For simplicity, take b odd. The balanced representatives {0, ±1, · · · , ±b−21} lead to about half as many carries. For example, when b = 5, the carries table for 5Z ⊂ Z is shown in Table 2.


![image 28](<2013-diaconis-carries-group-theory-additive_images/imageFile28.png>)

Table 2. Carries matrix for b = 5 with signed coset representatives {0, ±1, ±2}. Here −i is coded as ¯i.

¯2 ¯1 0 1 2

![image 29](<2013-diaconis-carries-group-theory-additive_images/imageFile29.png>)

![image 30](<2013-diaconis-carries-group-theory-additive_images/imageFile30.png>)

![image 31](<2013-diaconis-carries-group-theory-additive_images/imageFile31.png>)

![image 32](<2013-diaconis-carries-group-theory-additive_images/imageFile32.png>)

![image 33](<2013-diaconis-carries-group-theory-additive_images/imageFile33.png>)

¯2 ¯b ¯b 0 0 0 ¯1 ¯b 0 0 0 0

![image 34](<2013-diaconis-carries-group-theory-additive_images/imageFile34.png>)

![image 35](<2013-diaconis-carries-group-theory-additive_images/imageFile35.png>)

- 0 0 0 0 0 0

![image 36](<2013-diaconis-carries-group-theory-additive_images/imageFile36.png>)

![image 37](<2013-diaconis-carries-group-theory-additive_images/imageFile37.png>)

- 1 0 0 0 0 b

![image 38](<2013-diaconis-carries-group-theory-additive_images/imageFile38.png>)

![image 39](<2013-diaconis-carries-group-theory-additive_images/imageFile39.png>)

- 2 0 0 0 b b


![image 40](<2013-diaconis-carries-group-theory-additive_images/imageFile40.png>)

![image 41](<2013-diaconis-carries-group-theory-additive_images/imageFile41.png>)

![image 42](<2013-diaconis-carries-group-theory-additive_images/imageFile42.png>)

For example (−2) + (−2) = −5 + 1 and 2 + 2 = 5 − 1. The balanced representatives lead

to 6 carries while the usual choice leads to 52 = 10. Signed digit representations have a long history going back to Colson [9] and Cauchy [8]. A careful history is in Cajori [7] with

Knuth [23] giving further details. The study of carries has links to probability [10,20] and various parts of algebra [6].

Can one do better? Why do there have to be any carries? What is the best that can be done? These are problems in additive combinatorics. If X is a choice of coset representatives for bZ in Z, we are asking for connections between X and its sumset X + X.

- 1.2. Group theory. These questions make sense for any group. For example, the matrix in Table 1 and Table 2 also give the carries for the cyclic group Z/bZ ⊂ Z/b2Z with coset representatives {0, 1, 2, · · · , b − 1} or {0, ±1, · · · , ±(b − 1)/2} and everything interpreted modulo b2. The proofs for Z do not carry over to Z/b2Z since i + j might collapse to a coset representative modulo b2.


Let us now formulate the carries problem precisely when G is a group, and H a ﬁnite index normal subgroup. Let X ⊂ G be coset representatives for H in G. Given two elements x1 and x2 in X, there is a unique third element x12 ∈ X such that x−121x1x2 lies in the subgroup H. Note that if we multiply x1h1 and x2h2 the answer is x1x2(x−2 1h1x2h2) =

x12(x−121x1x2)(x−2 1h1x2h2). In analogy with the usual addition, we view x−121x1x2 as the carry in performing this multiplication. Thus carries are elements of the subgroup H, and a (non-trivial) carry occurs for x, y ∈ X exactly when x · y is not in X.

If X is a subgroup (so that necessarily XH = HX = G and H ∩ X = {1}), there are no carries and the extension H ⊂ G is said to split. For Z/bZ ⊂ Z/b2Z, any choice of coset representatives has b elements and Z/bZ is the unique subgroup of Z/b2Z of order b, so the extension fails to split. Our main theorem shows that if the extension H ⊂ G is not split, then there must be many carries. To quantify this notion, let us deﬁne

C(X) = |{x, y ∈ X : xy ∈ X}| |X|2

.

![image 43](<2013-diaconis-carries-group-theory-additive_images/imageFile43.png>)

Theorem 1.3. Let X be coset representatives for a normal, ﬁnite index subgroup H in a group G. If

C(X) > 7/9 then there is a subgroup K with HK = G, H ∩ K = {1}.

From Theorem 12 on page 182 of [11] for example, one sees that the structure of G above may be described as the semi-direct product of the normal subgroup H and the group K. Further, the constant 7/9 is sharp as seen by taking 3Z ⊂ Z with balanced coset representatives.

- 1.3. Additive combinatorics. The problems discussed above may be seen as part of additive combinatorics. A basic question in this area asks how the size |X · X| depends on the structure of X. If X is a subgroup, then |X · X| = |X|. For a random set, one may expect X·X to have about |X|2 elements. What happens X·X contains unusually few elements; for example what if |X · X| ≤ 2|X|? The structure of such sets is studied in additive combinatorics, which is a burgeoning area of mathematics with applications in computer science [35], harmonic analysis [25], number theory [28], combinatorics and elsewhere. It has spanned a host of new techniques (e.g. Szemer´edi’s regularity lemma [24, 33], higher Fourier analysis [13,14,34]). It gives connections between formerly disparate areas of mathematics (e.g. combinatorics, number theory and ergodic theory). There are striking results, such as the Green-Tao theorem that the primes contain arbitrarily long arithmetic progression [18,19].


Our theorems oﬀer a gentle introduction to this ﬁeld in a natural problem. The proof of the main theorem uses results on approximate homomorphisms ﬁrst studied by computer scientists for property testing (the study of large systems from properties of small samples). A second related result is given in Section 5; here the situation is more general than in Theorem 1.3 but the conclusion is weaker. This uses an argument of Fournier, familiar in additive combinatorics, to show that any ﬁnite subset X of a group G is almost a subgroup if C(X) is large.

Our route to the discovery and proof of Theorem 1.3 has some lessons. Our ﬁrst results were limited to pZ/p2Z in Z/p2Z, and they were asymptotic: if X is a set of coset representatives then C(X) ≤ 3/4 + ǫ provided p is a suﬃciently large prime (depending on ǫ). Here the dependence on ǫ is exponential. The argument uses rectiﬁcation [4,17], which roughly

speaking converts additively structured subsets of Z/pZ to subsets of Z. Later we found out that we could get rid of the asymptotics, proving that C(X) ≤ (3p2 + 1)/(4p2) for any odd prime p using a theorem of Lev [26]. This was done independently by Alon [1]. All of these arguments rely on the primality of the base p.

Section 2 gives a very easy proof of the optimality of balanced coset representatives for bZ ⊂ Z. Theorem 1.3 is proved in Section 4. A diﬀerent proof (with C(X) ≥ 59/60 implying splitting) appears in Section 5. In Table 2 above there are three types of carries: 0, +b, −b, while only 0 and +b appear with the usual choice of digits. This is shown to characterize the usual digits in Section 6. The ﬁnal section presents some problems and conjectures. We do not know the answer to some simple related questions: how well can one do for (bZ)2 ⊂ Z2?

Acknowledgments. We are grateful to Ben Green, Bob Guralnick and Marty Isaacs for many valuable discussions.

2. The easiest case: Minimality of balanced digits for Z

For b a positive integer, consider bZ ⊂ Z. Choose coset representatives X = {0, x1, x2, · · · , xb−1} in Z. There is a carry at i, j if xi + xj ∈/ X. The following proposition shows that any choice for X results in at least ⌊b2/4⌋ carries. Balanced coset representatives give this and so are best (in this sense). In fact, the argument works for any set of b real numbers.

- Proposition 2.1. Let X = {0, x1, · · · , xb−1} be distinct real numbers. Then X induces at least ⌊b2/4⌋ carries.


Proof. Let there be c positive and (b − 1 − c) negative elements in X. Say 0 < y1 < y2 < · · · < yc are the positives. Then, adding yc results in at least c carries. Adding yc−1 results in at least c − 1 carries. Continuing in this fashion, adding y1 results in at least 1 carry. This forces at least c(c + 1)/2 carries. Similarly, the negative elements in X force at least (b − 1 − c)(b − c)/2 carries, thus obtaining altogether

b2 − 1 4

b − 1 2

2

- 1

![image 44](<2013-diaconis-carries-group-theory-additive_images/imageFile44.png>)

- 2[c(c + 1) + (b − 1 − c)(b − c)] =


+ c −

![image 45](<2013-diaconis-carries-group-theory-additive_images/imageFile45.png>)

![image 46](<2013-diaconis-carries-group-theory-additive_images/imageFile46.png>)

carries. This proves the Proposition.

By examining the above proof, we may check that ⌊b2/4⌋ carries are attained only if X is of the form {xn : −⌊b/2⌋ < n ≤ ⌊b/2⌋} for some x = 0. Thus, for bZ ⊂ Z balanced coset representatives and their dilates by any number a relatively prime to b are the only examples with ⌊b2/4⌋ carries.

In the other direction, it is easy to (foolishly) choose coset representatives X for bZ in Z such that every sum results in a carry. For example choose {b, b + 1, · · · , 2b − 1}.

3. The next case: Minimality of balanced digits for cyclic groups

This section studies the following problem: consider p(Z/p2Z) as a subgroup of Z/p2Z for an odd prime p. The usual coset representatives are {0, 1, 2, . . ., p − 1}. Balanced coset

representatives are {0, ±1, . . ., ±(p−1)/2}. The carries matrices are the same as for pZ ⊂ Z. The following proposition implies that balanced coset representatives again give the minimum number of carries.

- Proposition 3.1. Let p be an odd prime. Let X ⊂ Z/p2Z be coset representatives for the subgroup p(Z/p2Z) in Z/p2Z. Then X induces at least (p2 − 1)/4 carries.


- Proposition 3.1 is a consequence of the following result, proved below.
- Proposition 3.2. Let p be an odd prime. Let A1, A2, A3 ⊂ Z/p2Z be three sets of coset representatives for p(Z/p2Z) ⊂ Z/p2Z. Then the number of solutions to a1 + a2 = a3 with a1 ∈ A1, a2 ∈ A2, and a3 ∈ A3 is at most (3p2 + 1)/4.


The problem of counting the number of solutions to linear equations in ﬁnite ﬁelds has been studied in [26]. The strategy there is to use Pollard’s theorem [29]. Our situation is slightly diﬀerent in that we are working in Z/p2Z, which is not a ﬁnite ﬁeld. However, we can still follow the argument in [26], making use of a version of Pollard’s theorem for composite modulus [29].

- Theorem 3.3 (Pollard). Let m be a positive integer. Let A1, A2, . . ., Ak be subsets of Z/mZ and let A′1, A′2, . . ., A′k be another k subsets of Z/mZ such that each A′i consists of consecutive elements and has |A′i| = |Ai|. Write


S(A1, A2, . . ., Ak, r) =

min(r, n(x, A1, A2, . . ., Ak)),

x∈Z/mZ

where n(x, A1, A2, . . ., Ak) is the number of representations of x as x = a1 + a2 + · · · + ak (ai ∈ Ai). Deﬁne S(A′1A′2, . . ., A′k, r) similarly. Suppose that at least k − 1 of the sets Ai have the property that

(x − y, m) = 1 for x, y ∈ Ai and x = y. Then

S(A1, A2, . . ., Ak, r) ≥ S(A′1, A′2, . . ., A′k, r). To gain an appreciation of Pollard’s theorem, consider the special case m = p a prime, k =

- 2 and r = 1. When m is prime, the hypothesis in Pollard’s theorem is automatically satisﬁed. Now S(A1, A2, 1) counts the number of elements in the sumset A1+A2, and Pollard’s theorem gives that this cardinality is smallest when A1 and A2 are intervals. It thus follows that |A1 + A2| ≥ min(p, |A1| + |A2| − 1), which is a fundamental result on set addition known


- as the Cauchy-Davenport theorem (a result proved by Cauchy in 1813, and rediscovered by Davenport in 1935). Thus Pollard’s theorem may be viewed as a generalization of the Cauchy-Davenport result. There has also been extensive work on extending the CauchyDavenport theorem, leading up to Kemperman’s very general theorem [22]; see Serra [31] for a recent survey.


For the general case of Pollard’s theorem, consider for each natural number ℓ the set Sℓ of those elements in Z/mZ which can be expressed as a1 + . . . + ak in at least ℓ ways. Then S(A1, A2, . . ., Ak, r) equals the sum of the cardinalities of Sℓ for all 1 ≤ ℓ ≤ r.

Corollary 3.4. With notation as in Pollard’s theorem max

n(x, A′1, . . ., A′k).

n(x, A1, . . ., Ak) ≤ max

x

x

Proof. Suppose the corollary does not hold, and take r = maxx n(x, A′1, . . ., A′k) in Pollard’s theorem. Note that

S(A′1, . . ., A′k, r) =

n(x, A′1, . . ., A′k) = |A′1| · · ·|A′k|. On the other hand, since by assumption r < n(x, A1, . . ., Ak) for some x,

x

S(A1, . . ., Ak, r) =

max(r, n(x, A1, . . ., Ak)) <

n(x, A1, . . ., Ak) = |A1| · · ·|Ak|. But this contradicts Pollard’s theorem, proving the Corollary.

x

x

Proof of Proposition 3.2. Since A1, A2 and A3 consist of coset representatives for p(Z/p2Z) in Z/p2Z, the hypothesis in Pollard’s theorem is satisﬁed. Now take A′1 = A′2 = A′3 = I where I is the interval of length p centered around the origin. A simple calculation gives that

3p2 + 1 4

.

max

n(x, I, I, I) = n(0, I, I, I) =

![image 47](<2013-diaconis-carries-group-theory-additive_images/imageFile47.png>)

x

By Corollary 3.4 it follows that n(0, A1, A2, −A3) is at most (3p2 + 1)/4. Since n(0, A1, A2, −A3) precisely counts the number of solutions to a1 + a2 = a3, the Proposition follows.

4. Carries and Approximate Homomorphisms

This section proves Theorem 1.3 and gives an introduction to computer scientists’ use of approximate homomorphisms in cryptography and for verifying program correctness.

Deﬁnition 4.1 (Approximate homomorphisms). Let G1, G2 be arbitrary groups with G1 ﬁnite. Let ǫ > 0. A function f : G1 → G2 is an ǫ-homomorphism if, picking g, g′ independently and uniformly in G1,

Pg,g′∈G1{f(g)f(g′) = f(gg′)} ≥ ǫ.

Checking if a given program or black box is a homomorphism occurs in cryptography (e.g. checking a random number generator) and in program checking (e.g. does this matrix multiplication package really work). Here is a brief description.

Cryptography. Despite recent advances, many cryptography schemes in active use still proceed by taking a message, given as a string of letters in a ﬁnite ﬁeld x1x2 · · ·xN, adding noise ǫ1ǫ2 · · ·ǫN to each coordinate, and sending xi + ǫi = yi. A receiver in possession of the recipe for the noise ǫi decodes via yi − ǫi = xi. The noise is usually generated by a pseudorandom generator. For example, if the ﬁeld is Z/pZ, the generator might be ǫi+1 = aǫi + b (mod p). Another scheme has the ﬁeld Z/2Z, breaks the message into blocks: X1 = (x1 · · ·x256), X2 = (x257 · · ·x512), · · ·, and adds vectors of noise ǫ˜1, ˜ǫ2, · · ·. These ǫ˜i are often generated by a simple scheme such as ǫ˜i+1 = Aǫ˜i with A a ﬁxed 256 × 256 matrix.

Someone interested in checking this generator has to determine (a, b) (or A) and the initial seed. A ﬁrst task is to decide if such a linear scheme is in use. This entails testing if the output is a homomorphism! For background and a fascinating success story in online poker, see [2].

Program checking. A host of computer scientists have developed a sophisticated suite of programs for testing if programs designed to do standard numerical tasks are doing their job. A readable entry to this literature is [5] and their references. As an example, consider a program P to multiply two n × n matrices A, B with elements in a ﬁnite ﬁeld. Given A, B, the program outputs P(A, B). A complete test is out of the question. A test which proves correctness with high probability is suggested in [5]. Given A, B, form random uniform matrices A1, B1. Set A2 = A − A1, B2 = B − B1, and C = P(A1, B1) + P(A1, B2) + P(A2, B1)+P(A2, B2). If the program is working then C = P(A, B) by simple algebra. The tools of approximate homomorphisms are used to show this test (ampliﬁed by repetitions) gives an eﬃcient check which works with arbitrarily high probability. While the examples above involve homomorphisms between abelian groups (Z/pZ)n2, the theorists developed their tools for general groups. One of their theorems turns out to be just what we need to prove Theorem 1.3.

The following theorem, due to Ben-Or, Coppersmith, Luby, and Rubinfeld [3], says that for ǫ > 7/9, an ǫ-approximate homomorphism must coincide with a genuine homomorphism on a large subset of G1.

- Theorem 4.2 (Structure theorem for approximate homomorphisms). Let G1, G2 be arbitrary groups with G1 ﬁnite. Suppose that f : G1 → G2 is an ǫ-approximate homomorphism for


some ǫ > 7/9. Then there is a genuine homomorphism φ : G1 → G2 such that Pg∈G

(f(g) = φ(g)) ≤ τ, where τ = τ(ǫ) is the smaller root of the equation 3x − 6x2 = 1 − ǫ.

1

√24ǫ − 15)/12, and so τ(ǫ) < (3 − 11/3)/12 = 0.0904 . . . when ǫ > 7/9. Both the range ǫ > 7/9 and the parameter τ(ǫ) are sharp. The genuine homomorphism φ in the statement is constructed by taking φ(g) to be the most frequent value of f(gg′)f(g′)−1 over all g′ ∈ G1. Under the stated assumptions, it can be shown that this most frequent value is well-deﬁned, the resulting map φ is a genuine homomorphism, and it well approximates f.

![image 48](<2013-diaconis-carries-group-theory-additive_images/imageFile48.png>)

![image 49](<2013-diaconis-carries-group-theory-additive_images/imageFile49.png>)

Note that τ(ǫ) equals (3 −

Proof of Theorem 1.3. Since H is a normal subgroup, the quotient G/H forms a group. Consider now the map f : G/H → G that sends a coset gH to its unique coset representative in X. Given two cosets (along with their representatives in X), gH = xH and g′H = x′H note that f(gH)f(g′H) = f(gg′H) if and only if xx′ belongs to X. In other words, f is a C(X)-approximate homomorphism.

Since C(X) > 7/9 by hypothesis, Theorem 4.2 implies that there is a genuine homomor-

phism φ : G/H → G such that f(gH) = φ(gH) for all but at most τ|G/H| < 101 |G/H| cosets. Let K denote the image of the homomorphism φ. Thus K is a subgroup of G with

![image 50](<2013-diaconis-carries-group-theory-additive_images/imageFile50.png>)

|K∩X| ≥ (1−τ)|X| > 109 |X| = 109 |G/H|. By the ﬁrst isomorphism theorem K is isomorphic to (G/H)/ker(φ) and therefore the kernel of φ is trivial, and |K| = |G/H|. If K contains an

![image 51](<2013-diaconis-carries-group-theory-additive_images/imageFile51.png>)

![image 52](<2013-diaconis-carries-group-theory-additive_images/imageFile52.png>)

element 1 = ℓ ∈ H, then for each k ∈ K at most one of k or kℓ can be in X; this would mean that |K ∩ X| ≤ |K|/2 contradicting our lower bound for |K ∩ X|. Thus K ∩ H = {1}, and distinct elements of K belong to distinct cosets of H. Therefore K consists of a complete set of coset representatives for H in G, and we have G = HK, as desired.

5. An argument of Fournier

In this section we study a problem that is a little more general than the carries question. Let A be a ﬁnite set in a group G, and set (in analogy with our earlier deﬁnition)

C(A) = |{a1, a2 ∈ A : a1a2 ∈ A}| |A|2

.

![image 53](<2013-diaconis-carries-group-theory-additive_images/imageFile53.png>)

The following result, which is established following an argument of Fournier, shows that if C(A) is close to 1, then A is almost a subgroup.

- Theorem 5.1. For a ﬁnite set A in a group G, if C(A) ≥ 1 − δ for some δ ≤ 1/60, then there exists a subgroup K of G such that


|K| ≤ 10|A|/9, and |A ∩ K| ≥ (1 − 5δ)|A|. Let A be any subset of G, and let ǫ be a real number in [0, 1]. Deﬁne Sym1−ǫ(A) = {x ∈ G : |A ∩ Ax| ≥ (1 − ǫ)|A|}.

Since |A∩Ax| = |Ax−1 ∩A| the set Sym1−ǫ(A) is symmetric (that is, closed under inverses). The following monotonicity condition is clear:

Sym1−ǫ

(A) ⊂ Sym1−ǫ

(A) if ǫ1 ≤ ǫ2. Observe further that if x1 ∈ Sym1−ǫ

1

2

(A) and x2 ∈ Sym1−ǫ

(A) then x1x2 lies in Sym1−ǫ

1

2

1−ǫ2(A). To see this, note that #{a ∈ A : ax1x2 ∈/ A} ≤ #{a ∈ A : ax1 ∈/ A} + #{a ∈ A : ax1 ∈ A, ax1x2 ∈/ A}

≤ ǫ1|A| + #{b ∈ A : bx2 ∈/ A} ≤ (ǫ1 + ǫ2)|A|. The identity

1 =

|A ∩ Ax| =

x∈G a1,a2∈A a1=a2x

x∈G

1 = |A|2

a1,a2∈A x=a−2 1a1

shows that

(1) |Sym1−ǫ(A)| ≤ |A|/(1 − ǫ).

- Lemma 5.2. Let A be a subset of G with C(A) ≥ 1 − δ. Then for any ǫ > δ we have (1 − δ/ǫ)|A| ≤ |A ∩ Sym1−ǫ(A)|.


Proof. Note that

C(A)|A|2 = #{a1a2 = a3} =

|A ∩ Aa2|.

a2∈A

Now |A ∩ Aa2| ≤ |A| for all a2 ∈ A, and |A ∩ Aa2| ≤ (1 − ǫ)|A| for a2 lying in A but not in Sym1−ǫ(A). Thus

(1 − δ)|A|2 ≤ |A||A ∩ Sym1−ǫ(A)| + (1 − ǫ)|A|(|A| − |A ∩ Sym1−ǫ(A)|), and the lemma follows upon rearranging.

- Proof of Theorem 5.1. With η = 1/20 we shall show that Sym1−2η(A) equals Sym1−4η(A). Then Sym1−2η(A) × Sym1−2η(A) ⊂ Sym1−4η(A) = Sym1−2η(A), and it follows that


Sym1−2η(A) = Sym1−4η(A) is a group. This is the group K of the Theorem. By (1) it satisﬁes |K| ≤ 10|A|/9, and by Lemma 5.2 we have |A ∩ K| ≥ (1 − 5δ)|A|; thus K has the properties claimed in the Theorem.

Since Sym1−2η(A) ⊂ Sym1−4η(A), it remains only to show the reverse inclusion. Consider any x ∈ Sym1−4η(A). The sets Sym1−η(A) and xSym1−η(A) both have cardinality at least |A|(1 − δ/η) by Lemma 5.2, and both are contained in the set Sym1−5η(A) of cardinality at most |A|/(1− 5η) by (1). Since δ < 1/60, we deduce that Sym1−η(A) and xSym1−η(A) have a non-empty intersection, and therefore x may be written as the product of two elements from Sym1−η(A). Hence x must lie in Sym1−2η(A), completing the proof.

6. Characterizing the traditional choice of digits

This section returns to the original setting of the cyclic groups p(Z/p2Z) ⊂ Z/p2Z. The usual choice of coset representatives {0, 1, 2, · · · , p − 1} results in two types of carries {0, p} (Table 1). Balanced coset representatives (Table 2) need three types of carries {0, p, −p}. Random coset representatives almost surely need all p carries. The results below show that two types of carries characterize the usual choice of coset representatives. They use some basic tools of additive combinatorics due to Freiman and make for a nice introduction to these tools in a natural problem. At present the argument relies on p being prime, and it would be interesting to extend it to other groups.

- Theorem 6.1. Let p be a prime, and let A ⊂ Z/p2Z be a set of coset representatives for p(Z/p2Z) ⊂ Z/p2Z. Suppose that the carries matrix associated to A contains only two distinct entries. Then there exist c ∈ (Z/p2Z)× and d ∈ p(Z/p2Z) such that after dilating A by c and translating by d we have either cA+d = {0, 1, . . ., p−1} or cA+d = {1, 2, · · · , p}.


If the carries matrix for A contains only two distinct entries then the sumset A + A is contained in two translates of the set A and thus |A + A| ≤ 2|A|. Pollard’s theorem tells us that |A + A| ≥ 2|A| − 1 (this is essentially the Cauchy-Davenport theorem, as discussed in Section 3), and so our situation is very close to the minimal possible doubling of a set. Note that a typical random set A might be expected to have sumset A+A as large as |A|2 in size, and one would expect sets with small doubling to be very structured and far from random.

This is the content of a celebrated theorem of Freiman, and we give a sample such result in the case of subsets of the integers.

Theorem (Freiman’s 3k−3 theorem). Let A ⊂ Z with |A| = k ≥ 3. If |A+A| = 2k−1+b ≤

- 3k − 4 then A is a subset of an arithmetic progression of length k + b.


Freiman’s 3k − 3-theorem does not directly apply in our situation, since we are dealing with a subset of Z/p2Z rather than a subset of Z. The problem is that the congruence a + b ≡ c + d (mod p2) does not necessarily mean that a + b = c + d as an equation in the integers. Thus a sumset in Z/p2Z could look very diﬀerent from a sumset in Z. However, if we could choose representatives for the residue classes of A ⊂ Z/p2Z to lie always in the interval (−p2/4, p2/4] then the congruence a+b ≡ c+d (mod p2) is indeed equivalent to the equation a + b = c + d. If this can be done, then we may as well view A as a subset of the integers and results such as Freiman’s 3k − 3-theorem would become applicable. This is a case of a very useful notion of Freiman which identiﬁes when two subsets of diﬀerent groups behave additively in a similar way.

Deﬁnition 6.2 (Freiman isomorphism). Let A ⊂ G and B ⊂ H be two subsets of the abelian groups G and H. We say that A and B are Freiman isomorphic if there is a bijection φ : A → B such that the relation x + y = z + w holds with x, y, z, w in A if and only if the relation φ(x) + φ(y) = φ(z) + φ(w) holds in the group H.

Note that if A and B are Freiman isomorphic then |A + A| = |B + B|. Returning to our problem, we would like to show that our set A ⊂ Z/p2Z is Freiman isomorphic to a subset of the integers, and then apply Freiman’s 3k −3 theorem. This follows a strategy pioneered by Freiman himself, who showed that small subsets of Z/pZ with small doubling are isomorphic to subsets of the integers (also called rectiﬁable) leading to the following theorem (see Section 2.8 of Nathanson [28]).

Theorem (Freiman’s 2.4 theorem). Set c = 1/35 and α = 2.4. Let A ⊂ Z/pZ with |A| = k ≤ cp. If |A + A| = 2k − 1 + b ≤ αk − 3 then A is contained in an arithmetic progression in Z/pZ of length k + b.

More recently Bilu, Lev and Ruzsa [4] and Green and Ruzsa [17] have shown how any small subset of Z/pZ with small doubling may be rectiﬁed. By adapting these arguments to our setting of Z/p2Z we shall establish the following Proposition.

- Proposition 6.3. Let A ⊂ Z/p2Z be a set of coset representatives for p(Z/p2Z) ⊂ Z/p2Z and suppose that |A+A| ≤ 2|A|. Then there exists a dilation c ∈ (Z/p2Z)× and a translation d ∈ Z/p2Z such that cA+d lies in (−p2/4, p2/4]. Thus A is Freiman isomorphic to a subset of the integers.


Assuming this Proposition, let us now prove Theorem 6.1.

- Proof of Theorem 6.1 assuming Proposition 6.3. Let A ⊂ Z/p2Z be a set of coset representatives with only two distinct carries, so that |A + A| ≤ 2|A|. By Proposition 6.3 we may dilate A by some c ∈ (Z/p2Z)× and obtain a set contained in (d − p2/4, d + p2/4] for some


d ∈ Z/p2Z. This means that A is Freiman isomorphic to a subset of the integers, and applying Freiman’s 3k − 3-theorem we see that A must lie in an arithmetic progression of length

- at most |A + A| − |A| + 1 ≤ (p + 1). After a dilation if necessary, we may assume that A lies in an interval of length p + 1,


missing exactly one element from this interval. Since A consists of coset representatives, the missing element must be one of the endpoints of the interval, so that A consists of consecutive elements; say A = {u, u + 1, . . ., u + p − 1} for some u. It remains to show that u ≡ 0, 1 (mod p).

To see this, if u ≡ i (mod p) for some 2 ≤ i ≤ p − 1, then the following examples show that there must be three types of carries:

(u + p − 1) + (u + p − 1) − (u + i − 2) = 2p + u − i; u + u − (u + i) = u − i; and

(u + p − 1) + u − (u + i − 1) = p + u − i. This completes our proof.

Now we turn to the proof of Proposition 6.3, whose argument involves two parts. First we establish a combinatorial result which shows that if a substantial part of A can be translated and dilated into the interval (−p2/4, p2/4] then all of A can be. This result holds for all cyclic groups Z/mZ. Second we use some simple Fourier analysis to show that a large part of A can be translated and dilated into (−p2/4, p2/4] so that our ﬁrst argument may be used. This argument requires that we are working in Z/p2Z.

- 6.1. From a large subset to the entire set.


- Proposition 6.4. Let m be a positive integer, and let A be a subset of Z/mZ such that if x = y ∈ A then (x − y, m) = 1. Of all the sets cA + d (with c ∈ (Z/mZ)∗ and d ∈ Z/mZ let ℓ denote the maximum intersection of such a set with (−m/4, m/4]. Suppose that ℓ < |A|. Then either ℓ < (|2A| + 4)/3 or m ≤ 6(|2A| − ℓ).


Proof. Let us suppose that A has been already translated and dilated to have maximum intersection with (−m/4, m/4], and let A0 denote this intersection. Thus |A0| = ℓ < |A| by assumption, and A0 is Freiman isomorphic to a subset of the integers.

Now 2A0 ⊂ 2A, and write |2A| = 2ℓ − 1 + b. We may assume that b ≤ ℓ − 3, else the ﬁrst alternative in the Proposition holds. Since |2A0| ≤ 2ℓ−1+b, by Freiman’s (3k −3)-theorem we see that A0 is contained in an arithmetic progression of size ℓ + b. Since the elements of A (and hence A0) satisfy that (x − y, m) = 1, the common diﬀerence of this arithmetic progression must be coprime to m. Therefore by translating and dilating (using dilations coprime to m) we may assume that A0 is contained inside (−(ℓ + b)/2, (ℓ + b)/2].

Since ℓ < |A|, there must be an element a ∈ A such that when reduced (mod m), a lies either in (m/4, m/2] or (−m/2, −m/4]. Now the set A0 + A0 has at least 2ℓ − 1 elements, and all of these lie in (−ℓ − b, ℓ + b], and the set A0 + {a} has ℓ elements all lying in either (m/4 − (ℓ + b)/2, m/2 + (ℓ + b)/2] or (−m/2 − (ℓ + b)/2, −m/4 + (ℓ + b)/2]. If the second alternative of the proposition doesn’t hold, then the sets A0 + A0 and A0 + {a} have

at most one element in common, and thus give at least 3ℓ − 2 elements in 2A which is a contradiction.

- 6.2. Obtaining concentration near the origin. Now we carry out the second part of the argument showing that a large part of A can be put inside (−p2/4, p2/4].


- Proposition 6.5 (Concentration near the origin). Let A ⊂ Z/p2Z be as in the statement of Proposition 6.3. Then there exist c ∈ (Z/p2Z)× and d ∈ Z/p2Z such that after dilating A by c and translating by d, we have


- 1

![image 54](<2013-diaconis-carries-group-theory-additive_images/imageFile54.png>)

- 2 .


p 2

p − 2 2(p − 1)

|(cA + d) ∩ (−p2/4, p2/4]| ≥

1 +

![image 55](<2013-diaconis-carries-group-theory-additive_images/imageFile55.png>)

![image 56](<2013-diaconis-carries-group-theory-additive_images/imageFile56.png>)

This uses a little Fourier analysis: For A ⊂ Z/mZ the Fourier coeﬃcients are deﬁned by the formula

Aˆ(r) =

e2πira/m for r ∈ Z/mZ.

a∈A

- Lemma 6.6 (Obtaining a large Fourier coeﬃcient). Let m be a positive integer, and let A ⊂ Z/mZ be a subset. Write |A| = α1m and |A + A| = α2m. Then


- α1(1 − α2)

![image 57](<2013-diaconis-carries-group-theory-additive_images/imageFile57.png>)

- α2(1 − α1)


1/2

|Aˆ(r)| ≥ |A|

max

. Proof. Write S = A + A. Note that

r =0

α12m2 = |A|2 =

a1,a2∈A a1+a2∈S

Using Parseval’s identity this equals 1 m k

1 m k =0

Aˆ(k)2 S(−k) = α12α2m2 +

![image 58](<2013-diaconis-carries-group-theory-additive_images/imageFile58.png>)

![image 59](<2013-diaconis-carries-group-theory-additive_images/imageFile59.png>)

Thus

1 m k =0

Aˆ(k)2 S(−k) ≤ max

α12(1 − α2)m2 =

![image 60](<2013-diaconis-carries-group-theory-additive_images/imageFile60.png>)

k =0

1.

Aˆ(k)2 S(−k).

|Aˆ(k)|

1 m k =0 |Aˆ(k)|| S(−k)|.

![image 61](<2013-diaconis-carries-group-theory-additive_images/imageFile61.png>)

By Cauchy’s inequality and Parseval’s identity 1 m k =0 |Aˆ(k)|| S(−k)| ≤

1 m k =0 |Aˆ(k)|2

![image 62](<2013-diaconis-carries-group-theory-additive_images/imageFile62.png>)

![image 63](<2013-diaconis-carries-group-theory-additive_images/imageFile63.png>)

- 1

![image 64](<2013-diaconis-carries-group-theory-additive_images/imageFile64.png>)

- 2 1 m k =0 | S(−k)|2


![image 65](<2013-diaconis-carries-group-theory-additive_images/imageFile65.png>)

- 1

![image 66](<2013-diaconis-carries-group-theory-additive_images/imageFile66.png>)

- 2(α2(1 − α2))


- 1

![image 67](<2013-diaconis-carries-group-theory-additive_images/imageFile67.png>)

- 2m,


= (α1(1 − α1)) and the Lemma follows with a little rearranging.

- 1

![image 68](<2013-diaconis-carries-group-theory-additive_images/imageFile68.png>)

- 2


We also require the following combinatorial result of Lev [27] (see also Theorem 2.9 of Nathanson [28]).

- Lemma 6.7. Let z1, . . ., zm ∈ C be points on the unit circle. If |z1 + · · · + zm| > 2n − m + 2(m − n) cos(φ/2),


then there exists an arc on the unit circle of length φ containing more than n points. In particular some arc of length π contains at least 21(m + |z1 + . . . + zm|) points. Proof of Proposition 6.5. Apply Lemma 6.6 with m = p2, α1 = 1/p, and α2 ≤ 2/p, to get

![image 69](<2013-diaconis-carries-group-theory-additive_images/imageFile69.png>)

1/2

p − 2 2(p − 1)

|Aˆ(r)| ≥ p

max

.

![image 70](<2013-diaconis-carries-group-theory-additive_images/imageFile70.png>)

r =0

Since A consists of coset representatives for p(Z/p2Z) ⊂ Z/p2Z it follows that Aˆ(r) = 0 for those r that are multiples of p but not of p2. Thus the maximal non-zero Fourier coeﬃcient produced above is coprime to p. Thus after dilating the original A by r if needed, we may assume that the maximal Fourier coeﬃcient is attained at r = 1.

Now apply Lemma 6.7 with the p points e2πia/p2 for a ∈ A. We conclude that some arc of length π contains at least 21(p + |Aˆ(1)|) points e2πia/p2, which is the Proposition.

![image 71](<2013-diaconis-carries-group-theory-additive_images/imageFile71.png>)

Proof of Proposition 6.3. When p = 2 we may easily translate and dilate A to equal {0, 1}. When p = 3 or 5 Proposition 6.5 already shows that A may be translated and dilated to lie inside (−p2/4, p2/4]. For p at least 7, a small calculation shows that Propositions 6.4 and 6.5 may be combined to give the conclusion of Proposition 6.3.

7. Open Problems

For X coset representatives for a normal, ﬁnite index subgroup H in an arbitrary group G, we have shown that either G is a semi direct product of H and another subgroup K, or C(X) ≤ 7/9. For concrete examples of the pair (G, H), it is an interesting question to determine what the best upper bound for C(X) in this statement is. Denote this upper bound by C(G, H). We showed that C(Z, bZ) = 1 − ⌊b2/4⌋/b2; in particular C(Z, bZ) = 3/4 + o(1) as b → ∞. Consider the two-dimensional question of determining C(Z×Z, bZ×bZ). Clearly C(Z × Z, bZ × bZ) ≤ C(Z, bZ), and we conjecture that C(Z × Z, bZ × bZ) = C(Z, bZ)2 = (9/16 + o(1)); this bound may be attained by by taking X = {−(b − 1)/2, · · · , (b − 1)/2} × {−(b − 1)/2, · · · , (b − 1)/2}. We are unable to prove this conjecture; however, in [32], Shao makes partial progress obtaining C(Z × Z, bZ × bZ) ≤ 1 − 3√3/4π ≈ 0.59; note that 9/16 = 0.5625 so that Shao’s bound is not too far from our conjecture. As mentioned earlier, another open problem is to extend Theorem 6.1 to other groups.

![image 72](<2013-diaconis-carries-group-theory-additive_images/imageFile72.png>)

To end this paper, we make a ﬁnal remark on Theorem 4.2. It is natural to wonder what can be said about an ǫ-approximate homomorphism f for a small positive constant ǫ (say ǫ = 0.01). We have already seen that, in general, f need not resemble a genuine homomorphism. On the other hand, what one can conclude is that f resembles a genuine local homomorphism. In the special case when G and H are vector spaces over ﬁnite ﬁelds, it turns out that any ǫ-approximate homomorphism does resemble a genuine (global) homomorphism [30]. A quantitative version of this statement is equivalent to the polynomial Freiman-Ruzsa

(PFR) conjecture, a famous open problem in additive combinatorics. See [16] for the precise statement of this conjecture in the ﬁnite ﬁeld setting.

References

- [1] N. Alon. Minimizing the number of carries in addition. SIAM J. Discrete Math., 27(1):562–566, 2013.
- [2] B. Arkin, F. Hill, S. Marks, M. Schmid, T. J. Walls, and G. Mc-Graw. How we learned to cheat at online poker: A study in software security. The developer. com Journal, 1999.
- [3] M. Ben-Or, D. Coppersmith, M. Luby, and R. Rubinfeld. Non-abelian homomorphism testing, and distributions close to their self-convolutions. Random Structures Algorithms, 32(1):49–70, 2008.
- [4] Y. F. Bilu, V. F. Lev, and I. Z. Ruzsa. Rectiﬁcation principles in additive number theory. Discrete Comput. Geom., 19(3, Special Issue):343–353, 1998. Dedicated to the memory of Paul Erdo˝s.
- [5] M. Blum, M. Luby, and R. Rubinfeld. Self-testing/correcting with applications to numerical problems. In Proceedings of the 22nd Annual ACM Symposium on Theory of Computing (Baltimore, MD, 1990), volume 47, pages 549–595, 1993.
- [6] A. Borodin, P. Diaconis, and J. Fulman. On adding a list of numbers (and other one-dependent determinantal processes). Bull. Amer. Math. Soc. (N.S.), 47(4):639–670, 2010.
- [7] F. Cajori. A history of mathematical notations, volume 1. Dover Publications, 1993.
- [8] A. Cauchy. Sur les moyens d´eviter les erreurs dans les calculs num´eriques. Comptes Rendus de lAcade´mie des Sciences, Paris, 11:789–798, 1840.
- [9] J. Colson. A Short Account of Negativo-Aﬃrmative Arithmetick, by Mr. John Colson, FRS. Philosophical transactions, 34(392-398):161–173, 1726.
- [10] P. Diaconis and J. Fulman. Carries, shuﬄing, and an amazing matrix. Amer. Math. Monthly, 116(9):788– 803, 2009.
- [11] D. S. Dummit and R. M. Foote. Abstract algebra. John Wiley & Sons Inc., Hoboken, NJ, third edition, 2004.
- [12] J. Fournier. Sharpness in Young’s inequality for convolution. Paciﬁc J. Math., 72(2):383–397, 1977.
- [13] W. T. Gowers. A new proof of Szemer´edi’s theorem for arithmetic progressions of length four. Geom. Funct. Anal., 8(3):529–551, 1998.
- [14] W. T. Gowers. A new proof of Szemer´edi’s theorem. Geom. Funct. Anal., 11(3):465–588, 2001.
- [15] B. Green. Additive combinatorics. Lecture notes for the 22nd McGill invitational workshop on computational complexity.
- [16] B. Green. Finite ﬁeld models in additive combinatorics. In Surveys in combinatorics 2005, volume 327 of London Math. Soc. Lecture Note Ser., pages 1–27. Cambridge Univ. Press, Cambridge, 2005.
- [17] B. Green and I. Z. Ruzsa. Sets with small sumset and rectiﬁcation. Bull. London Math. Soc., 38(1):43–52, 2006.
- [18] B. Green and T. Tao. The primes contain arbitrarily long arithmetic progressions. Ann. of Math. (2), 167(2):481–547, 2008.
- [19] B. Green and T. Tao. Linear equations in primes. Ann. of Math. (2), 171(3):1753–1850, 2010.
- [20] J. M. Holte. Carries, combinatorics, and an amazing matrix. Amer. Math. Monthly, 104(2):138–149, 1997.
- [21] D. C. Isaksen. A cohomological viewpoint on elementary school arithmetic. Amer. Math. Monthly, 109(9):796–805, 2002.
- [22] J. H. B. Kemperman. On small sumsets in an abelian group. Acta Math., 103:63–88, 1960.
- [23] D. E. Knuth. The art of computer programming. Addison-Wesley, 2006.
- [24] J. Koml´os and M. Simonovits. Szemer´edi’s regularity lemma and its applications in graph theory. In Combinatorics, Paul Erdo˝s is eighty, Vol. 2 (Keszthely, 1993), volume 2 of Bolyai Soc. Math. Stud., pages 295–352. J´anos Bolyai Math. Soc., Budapest, 1996.


- [25] I.  Laba. From harmonic analysis to arithmetic combinatorics. Bull. Amer. Math. Soc. (N.S.), 45(1):77– 115, 2008.
- [26] V. F. Lev. Linear equations over Fp and moments of exponential sums. Duke Math. J., 107(2):239–263, 2001.
- [27] V. F. Lev. Distribution of points on arcs. Integers, 5(2):A11, 6, 2005.
- [28] M. B. Nathanson. Additive number theory: Inverse problems and the geometry of sumsets, volume 165 of Graduate Texts in Mathematics. Springer-Verlag, New York, 1996.
- [29] J. M. Pollard. Addition properties of residue classes. J. London Math. Soc. (2), 11(2):147–152, 1975.
- [30] A. Samorodnitsky. Low-degree tests at large distances. In STOC’07—Proceedings of the 39th Annual ACM Symposium on Theory of Computing, pages 506–515. ACM, New York, 2007.
- [31] O. Serra. An isoperimetric method for the small sumset problem. In Surveys in combinatorics 2005, volume 327 of London Math. Soc. Lecture Note Ser., pages 119–152. Cambridge Univ. Press, Cambridge, 2005.
- [32] X. Shao. Large values of the additive energy in Rd and Zd. Preprint.
- [33] E. Szemer´edi. Regular partitions of graphs. In Proble`mes combinatoires et the´orie des graphes (Colloq. Internat. CNRS, Univ. Orsay, Orsay, 1976), volume 260 of Colloq. Internat. CNRS, pages 399–401. CNRS, Paris, 1978.
- [34] T. Tao. Higher order Fourier analysis, volume 142 of Graduate Studies in Mathematics. American Mathematical Society, Providence, RI, 2012.
- [35] L. Trevisan. Guest column: additive combinatorics and theoretical computer science. ACM SIGACT News, 40(2):50–66, 2009.


Department of Mathematics, Stanford University, 450 Serra Mall, Bldg. 380, Stanford,

CA 94305-2125 E-mail address: fshao@stanford.edu E-mail address: ksound@math.stanford.edu

