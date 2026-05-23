# Evaluating parametric holonomic sequences using rectangular splitting

arXiv:1310.3741v1[cs.SC]14Oct2013

Fredrik Johansson∗

RISC Johannes Kepler University 4040 Linz, Austria

fredrik.johansson@risc.jku.at ABSTRACT

where a0, . . . , ar are polynomials. The class of holonomic sequences enjoys many useful closure properties: for example, holonomic sequences form a ring, and if c(i) is holonomic then so is the sequence of partial sums s(n) = ni=0 c(i). A sequence is called hypergeometric if it is holonomic of order r = 1. The sequence of partial sums of a hypergeometric sequence is holonomic of order (at most) r = 2.

We adapt the rectangular splitting technique of Paterson and Stockmeyer to the problem of evaluating terms in holonomic sequences that depend on a parameter. This approach allows computing the n-th term in a recurrent sequence of suitable type using O(n1/2) “expensive” operations at the cost of an increased number of “cheap” operations.

Many integer and polynomial sequences of interest in number theory and combinatorics are holonomic, and the power series expansions of many well-known special functions (such as the error function and Bessel functions) are holonomic.

Rectangular splitting has little overhead and can perform better than either naive evaluation or asymptotically faster algorithms for ranges of n encountered in applications. As an example, fast numerical evaluation of the gamma function is investigated. Our work generalizes two previous algorithms of Smith.

We are interested in eﬃcient algorithms for evaluating an isolated term c(n) in a holonomic sequence when n is large. Section 2 recalls the well-known techniques of rewriting (1) in matrix form and applying binary splitting, which gives a near-optimal asymptotic speedup for certain types of coefﬁcients, or fast multipoint evaluation which in the general case is the asymptotically fastest known algorithm.

## Categories and Subject Descriptors

I.1.2 [Computing Methodologies]: Symbolic and Algebraic Manipulation—Algorithms; F.2.1 [Theory of Computation]: Analysis of Algorithms and Problem Complexity—Numerical Algorithms and Problems

In section 3, we give an algorithm (Algorithm 3) which becomes eﬃcient when the recurrence equation involves an “expensive” parameter (in a sense which is made precise), based on the baby-step giant-step technique of Paterson and Stockmeyer [11] (called rectangular splitting in [5]).

## General Terms

Algorithms

Our algorithm can be viewed as a generalization of the method given by Smith in [13] for computing rising factorials. Conceptually, it also generalizes an algorithm given by Smith in [12] for evaluation of hypergeometric series. Our contribution is to recognize that rectangular splitting can be applied systematically to a very general class of sequences, and in an eﬃcient way (we provide a detailed cost analysis, noting that some care is required in the construction of the algorithm to get optimal performance).

## Keywords

Linearly recurrent sequences, Numerical evaluation, Fast arithmetic, Hypergeometric functions, Gamma function

## 1. INTRODUCTION

A sequence (c(i))∞i=0 is called holonomic (or P-ﬁnite) of order r if it satisﬁes a linear recurrence equation

The main intended application of rectangular splitting is high-precision numerical evaluation of special functions, where the parameter is a real or complex number (represented by a ﬂoating-point approximation), as discussed further in section 4. Although rectangular splitting is asymptotically slower than fast multipoint evaluation, it is competitive in practice. In section 5, we present implementation results comparing several diﬀerent algorithms for numerical evaluation of the gamma function to very high precision.

ar(i)c(i + r) + ar−1(i)c(i + r − 1) + . . . + a0(i)c(i) = 0 (1)

![image 1](<2013-johansson-evaluating-parametric-holonomic-sequences_images/imageFile1.png>)

∗Supported by the Austrian Science Fund (FWF) grant Y464-N18.

Permission to make digital or hard copies of all or part of this work for personal or classroom use is granted without fee provided that copies are not made or distributed for proﬁt or commercial advantage and that copies bear this notice and the full citation on the ﬁrst page. To copy otherwise, to republish, to post on servers or to redistribute to lists, requires prior speciﬁc permission and/or a fee. Copyright 20XX ACM X-XXXXX-XX-X/XX/XX ...$10.00.

## 2. MATRIX ALGORITHMS

Let R be a commutative ring with unity and of suﬃciently large characteristic where necessary. Consider a sequence of rank-r vectors (c(i) = (c1(i), . . . , cr(i))T)∞i=0 satisfying a

recurrence equation of the form   

c1(i + 1) . cr(i + 1)

c1(i) . cr(i)

   = M(i)

  

   (2)

where M ∈ R[k]r×r (or Quot(R)(k)r×r) and where M(i) denotes entrywise evaluation. Given an initial vector c(0), we wish to evaluate the single vector c(n) for some n > 0, where we assume that no denominator in M vanishes for 0 ≤ i < n. A scalar recurrence of the form (1) can be rewritten as (2) by taking the vector to be c˜(i) = (c(i), . . . , c(i+r −1))T and setting M to the companion matrix





ar

...

1 ar

M =

. (3)

![image 2](<2013-johansson-evaluating-parametric-holonomic-sequences_images/imageFile2.png>)

 

 

ar −a0 −a1 . . . −ar−1

In either case, we call the sequence holonomic (of order r).

Through repeated application of the recurrence equation, c(n) can be evaluated using O(r2n) arithmetic operations (or O(rn) if M is companion) and temporary storage of O(r) values. We call this strategy the naive algorithm.

The naive algorithm is not generally optimal for large n. The idea behind faster algorithms is to ﬁrst compute the matrix product

P(0, n) =

n−1

M(i). (4)

i=0

and then multiply it by the vector of initial values (matrix multiplication is of course noncommutative, and throughout this paper the notation in (4) is understood to mean M(n − 1) . . . M(2)M(1)M(0)). This increases the cost to

- O(rωn) arithmetic operations where ω is the exponent of matrix multiplication, but we can save time for large n by exploiting the structure of the matrix product. The improvement is most dramatic when all matrix entries are constant, allowing binary exponentiation (with O(log n) complexity) or diagonalization to be used, although this is a rather special case. We assume in the remainder of this work that r is ﬁxed, and omit O(rω) factors from any complexity estimates.

From this point, we may view the problem as that of evaluating (4) for some M ∈ R[k]r×r. It is not a restriction to demand that the entries of M are polynomials: if M = M/q˜ , we can write P(0, n) = P˜(0, n)/Q(0, n) where

- P˜(0, n) = ni=0−1 q(i)M˜ (i) and Q(0, n) = ni=0−1 q(i). This reduces the problem to evaluating two denominator-free products, where the second product has order 1.


- 2.1 Binary splitting In the binary splitting algorithm, we recursively compute


a product of square matrices P(a, b) = bi=−a1 M(i) (where the entries of M need not necessarily be polynomials of i),

as P(m,b)P(a,m) where m = ⌊(a + b)/2⌋. If the entries of partial products grow in size, this scheme balances the sizes of the subproducts in a way that allows us to take advantage of fast multiplication.

For example, take M(i) ∈ R[x]r×r where all M(i) have bounded degree. Then P(a,b) has entries in R[x] of degree

- O(b − a), and binary splitting can be shown to compute
- P(0, n) using O(M(n) log n) operations in R where M(n)


is the complexity of polynomial multiplication, using O(n) extra storage. Over a general ring R, we have M(n) = O(n log1+o(1) n) by the result of [6], making the binary splitting softly optimal. This is a signiﬁcant improvement over the naive algorithm, which in general uses O(n2) coeﬃcient operations to generate the n-th entry in a holonomic sequence of polynomials.

Analogously, binary splitting reduces the bit complexity for evaluating holonomic sequences over Z or Q (or more generally the algebraic numbers) from O(n2+o(1)) to O(n1+o(1)). For further references and several applications of the binary splitting technique, we refer to Bernstein [2].

## 2.2 Fast multipoint evaluation

The fast multipoint evaluation method is useful when all arithmetic operations are assumed to have uniform cost. Fast multipoint evaluation allows evaluating a polynomial of degree d simultaneously at d points using O(M(d)log d) operations and O(d log d) space. Applied to a polynomial matrix product, we obtain Algorithm 1, which is due to Chudnovsky and Chudnovsky [7].

![image 3](<2013-johansson-evaluating-parametric-holonomic-sequences_images/imageFile3.png>)

Algorithm 1 Polynomial matrix product using fast multipoint evaluation

![image 4](<2013-johansson-evaluating-parametric-holonomic-sequences_images/imageFile4.png>)

Input: M ∈ R[k]r×r, n = m × w Output: ni=0−1 M(i)

- 1: [T0, . . . , Tm−1] ← [M(k), . . . , M(k + m − 1)] ⊲ Compute entrywise Taylor shifts of the matrix
- 2: U ← mi=0−1 Ti ⊲ Binary splitting in R[k]r×r
- 3: [V0, . . . , Vw−1] ← [U(0), . . . , U((w − 1)m)] ⊲ Fast multipoint evaluation
- 4: return i w=0−1 Vi ⊲ Repeated multiplication in Rr×r


![image 5](<2013-johansson-evaluating-parametric-holonomic-sequences_images/imageFile5.png>)

We assume for simplicity of presentation that n is a multiple of the parameter m (in general, we can take w = ⌊n/m⌋ and multiply by the remaining factors naively). Taking m ∼ n1/2, Algorithm 1 requires O(M(n1/2)log n) arithmetic operations in the ring R, using O(n1/2 log n) temporary storage during the fast multipoint evaluation step. Bostan, Gaudry and Schost [4] improve the algorithm to obtain an O(M(n1/2)) operation bound, which is the best available result for evaluating the n-th term of a holonomic sequence over a general ring. Algorithm 1 and some of its applications are studied further by Ziegler [18].

## 3. RECTANGULAR SPLITTING FOR PARAMETRIC SEQUENCES

We now consider holonomic sequences whose recurrence equation involves coeﬃcients from a commutative ring C with unity as well as an additional, distinguished parameter x. The setting is as in the previous section, but with R = C[x]. In other words, we are considering holonomic sequences of polynomials (or, by clearing denominators, rational functions) of the parameter. We make the following deﬁnition.

Definition 1. A holonomic sequence (c(n) ≡ c(x, n))∞n=0 is parametric over C (with parameter x) if it satisﬁes a linear recurrence equation of the form (2) with M ∈ R[k] where R = C[x].

Let H be a commutative C-algebra, and let c(x, k) be a parametric holonomic sequence deﬁned by a recurrence matrix M ∈ C[x][k]r×r and an initial vector c(z, 0) ∈ Hr. Given some z ∈ H and n ∈ N, we wish to compute the single vector c(z, n) ∈ Hr eﬃciently subject to the assumption that operations in H are expensive compared to operations in C. Accordingly, we distinguish between:

- • Coeﬃcient operations in C
- • Scalar operations in H (additions in H and multiplications C × H → H)
- • Nonscalar multiplications H × H → H


For example, the sequence of rising factorials c(x, n) = xn = x(x + 1) · · · (x + n − 1)

![image 6](<2013-johansson-evaluating-parametric-holonomic-sequences_images/imageFile6.png>)

is ﬁrst-order holonomic (hypergeometric) with the deﬁning recurrence equation c(x, n + 1) = (n + x)c(x,n), and parametric over C = Z. In some applications, we wish to evaluate c(z, n) for z ∈ H where H = R or H = C.

The Paterson-Stockmeyer algorithm [11] solves the prob-

lem of evaluating a polynomial P(x) = ni=0−1 pixi with pi ∈ C at x = z ∈ H using a reduced number of nonscalar multiplications. The idea is to write the polynomial

- as a rectangular array P(x) = (p0 + . . . + pm−1xm−1)


+ (pm + . . . + p2m−1xm−1)xm

(5)

+ (p2m + . . . + p3m−1xm−1)x2m

+ . . .

After computing a table containing x2, x3, . . . , xm−1, the inner (rowwise) evaluations can be done using only scalar multiplications, and the outer (columnwise) evaluation with respect to xm can be done using about n/m nonscalar multiplications. With m ∼ n1/2, this algorithm requires O(n1/2) nonscalar multiplications and O(n) scalar operations.

A straightforward application of the Paterson-Stockmeyer

algorithm to evaluate each entry of ni=0−1 M(x,i) ∈ C[x]r×r yields Algorithm 2 and the corresponding complexity esti-

mate of Theorem 2.

![image 7](<2013-johansson-evaluating-parametric-holonomic-sequences_images/imageFile7.png>)

- Algorithm 2 Polynomial matrix product and evaluation using rectangular splitting Input: M ∈ C[x][k]r×r, z ∈ H, n = m × w Output: ni=0−1 M(z, i) ∈ Hr×r


![image 8](<2013-johansson-evaluating-parametric-holonomic-sequences_images/imageFile8.png>)

- 1: [T0, . . . , Tn−1] ← [M(x, 0), . . . , M(x,n − 1)] ⊲ Evaluate matrix w.r.t. k, giving Ti ∈ C[x]r×r
- 2: U ← ni=0−1 Ti ⊲ Binary splitting in C[x]r×r
- 3: V ← U(z) ⊲ Evaluate U entrywise using Paterson-Stockmeyer

with step length m

- 4: return V


![image 9](<2013-johansson-evaluating-parametric-holonomic-sequences_images/imageFile9.png>)

Theorem 2. The n-th entry in a parametric holonomic sequence can be evaluated using O(n1/2) nonscalar multiplications, O(n) scalar operations, and O(M(n) log n) coeﬃcient operations.

Proof. We call Algorithm 2 with m ∼ n1/2. Letting d =

- max degk M and e = max degx M, computing T0, . . . , Tn−1


takes O(nde) = O(n) coeﬃcient operations. Since degx Ti ≤ e, generating U using binary splitting costs O(M(n) log n) coeﬃcient operations. Each entry in U has degree at most ne = O(n), and can thus be evaluated using O(n1/2) nonscalar multiplications and O(n) scalar operations with the Paterson-Stockmeyer algorithm.

![image 10](<2013-johansson-evaluating-parametric-holonomic-sequences_images/imageFile10.png>)

![image 11](<2013-johansson-evaluating-parametric-holonomic-sequences_images/imageFile11.png>)

![image 12](<2013-johansson-evaluating-parametric-holonomic-sequences_images/imageFile12.png>)

![image 13](<2013-johansson-evaluating-parametric-holonomic-sequences_images/imageFile13.png>)

If we only count nonscalar multiplications, Theorem 2 is an asymptotic improvement over fast multipoint evaluation which uses O(n1/2 log2+o(1) n) nonscalar multiplications (O(n1/2 log1+o(1) n) with the improvement of Bostan, Gaudry and Schost).

- Algorithm 2 is not ideal in practice since the polynomials

in U grow to degree O(n). Their coeﬃcients also grow to O(n log n) bits when C = Z (for example, in the case of rising factorials, the coeﬃcients are the Stirling numbers of the ﬁrst kind S(n, k) which grow to a magnitude between (n−1)! and n!). This problem can be mitigated by repeatedly ap-

plying Algorithm 2 to successive subproducts ai=+˜an M(z, i) where n˜ ≪ n, but the nonscalar complexity is then no longer

the best possible. A better strategy is to apply rectangular splitting to the matrix product itself, leading to Algorithm 3. We can then reach the same operation complexity while only working with polynomials of degree O(n1/2), and over C = Z, having coeﬃcients of bit size O(n1/2 log n).

Theorem 3. For any choice of m, Algorithm 3 requires O(m + n/m) nonscalar multiplications, O(n) scalar operations, and O((n/m)M(m) log m) coeﬃcient operations. In particular, the complexity bounds stated in Theorem 2 also hold for Algorithm 3 with m ∼ n1/2. Moreover, Algorithm 3 only requires storage of O(m) elements of C and H, and if C = Z, the coeﬃcients have bit size O(m log m).

Proof. This follows by applying a similar argument as used in the proof of Theorem 2 to the operations in the inner loop of Algorithm 3, noting that U has entries of degree mdegx M = O(m) and that the matrix multiplication S × V requires O(1) nonscalar multiplications and scalar operations (recalling that we consider r ﬁxed).

![image 14](<2013-johansson-evaluating-parametric-holonomic-sequences_images/imageFile14.png>)

![image 15](<2013-johansson-evaluating-parametric-holonomic-sequences_images/imageFile15.png>)

![image 16](<2013-johansson-evaluating-parametric-holonomic-sequences_images/imageFile16.png>)

![image 17](<2013-johansson-evaluating-parametric-holonomic-sequences_images/imageFile17.png>)

![image 18](<2013-johansson-evaluating-parametric-holonomic-sequences_images/imageFile18.png>)

- Algorithm 3 Improved polynomial matrix product and evaluation using rectangular splitting Input: M ∈ C[x][k]r×r, z ∈ H, n = m × w Output: ni=0−1 M(z, i) ∈ Hr×r


![image 19](<2013-johansson-evaluating-parametric-holonomic-sequences_images/imageFile19.png>)

- 1: Compute power table [zj, 0 ≤ j ≤ m degx M]
- 2: V ← 1Hr×r ⊲ Start with the identity matrix
- 3: for i ← 0 to w − 1 do
- 4: [T0, . . . , Tm−1] ← [M(x, im + j)]mj=0−1 ⊲ Evaluate matrix w.r.t. k, giving Tj ∈ C[x]r×r
- 5: U ← mj=0−1 Tj ⊲ Binary splitting in C[x]r×r
- 6: S ← U(z) ⊲ Evaluate w.r.t. x using power table
- 7: V ← S × V ⊲ Multiplication in Hr×r
- 8: return V


![image 20](<2013-johansson-evaluating-parametric-holonomic-sequences_images/imageFile20.png>)

## 3.1 Variations

Many variations of Algorithm 3 are possible. Instead of using binary splitting directly to compute U, we can generate the bivariate matrix

m−1

M(x, k + i) ∈ C[x][k]r×r (6)

Wm =

i=0

- at the start of the algorithm, and then obtain U by evalu-


ating Wm at k = im. We may also work with diﬀerences of two successive U (for small m, this can introduce cancellation resulting in slightly smaller polynomials or coeﬃcients). Combining both variations, we end up with Algorithm 4 in which we expand and evaluate the bivariate polynomial matrices

∆m =

m−1

M(x, k + m + i) −

i=0

m−1

M(x, k + i) ∈ C[x][k]r×r.

i=0

This version of the rectangular splitting algorithm can be viewed as a generalization of an algorithm used by Smith [13] for computing rising factorials (we consider the case of rising factorials further in Section 5.1). In fact, the author of the present paper ﬁrst found Algorithm 4 by generalizing Smith’s algorithm, and only later discovered Algorithm 3 by “interpolation” between Algorithm 2 and Algorithm 4.

![image 21](<2013-johansson-evaluating-parametric-holonomic-sequences_images/imageFile21.png>)

Algorithm 4 Polynomial matrix product and evaluation using rectangular splitting (variation)

![image 22](<2013-johansson-evaluating-parametric-holonomic-sequences_images/imageFile22.png>)

Input: M ∈ C[x][k]r×r, z ∈ H, n = m × w Output: ni=0−1 M(z, i) ∈ Hr×r

- 1: Compute power table [zj, 0 ≤ j ≤ m degx M]
- 2: ∆ ← mi=0−1 M(x,k + m + i) − mi=0−1 M(x, k + i) ⊲ Binary splitting in C[x][k]r×r
- 3: V ← S ← mi=0−1 M(z, i) ⊲ Evaluate w.r.t. k, and w.r.t. x using power table
- 4: for i ← 0 to w − 2 do
- 5: S ← S + ∆(z,mi) ⊲ Evaluate w.r.t. k, and w.r.t. x using power table
- 6: V ← S × V
- 7: return V


![image 23](<2013-johansson-evaluating-parametric-holonomic-sequences_images/imageFile23.png>)

The eﬃciency of Algorithm 4 is theoretically somewhat worse than that of Algorithm 3. Since degx Wm = O(m) and degk Wm = O(m), Wm has O(m2) terms (likewise for ∆m), making the space complexity higher and increasing the number of coeﬃcient operations to O((n/m)m2) for the evaluations with respect to k. However, this added cost

- may be negligible in practice. Crucially, when C = Z, the coeﬃcients have similar bit sizes as in Algorithm 3.


Initially generating Wm or ∆m also adds some cost, but this is cheap compared to the evaluations when n is large enough: binary splitting over C[x][k] costs O(M(m2)log m) coeﬃcient operations by Lemma 8.2 and Corollary 8.28 in [17]. This is essentially the same as the total cost of binary splitting in Algorithm 3 when m ∼ n1/2.

We also note that a small improvement to Algorithm 3 is possible if M(x, k + m) = M(x + m, k): instead of computing U from scratch using binary splitting in each loop iteration, we can update it using a Taylor shift. At least in suﬃciently large characteristic, the Taylor shift can be computed using O(M(m)) coeﬃcient operations with the convolution algorithm of Aho, Steiglitz and Ullman [1], saving a factor O(log n) in the total number of coeﬃcient operations. In practice, basecase Taylor shift algorithms may also be beneﬁcial (see [16]).

In lucky cases, the polynomial coeﬃcients (in either Algorithm 3 or 4) might satisfy a recurrence relation, allowing them to be generated using O(n) coeﬃcient operations (and avoiding the dependency on polynomial arithmetic).

- 3.2 Several parameters The rectangular splitting technique can be generalized to

sequences c(x1, . . . , xv, k) depending on several parameters. In Algorithm 3, we simply replace the power table by a vdimensional array of the possible monomial combinations. Then we have the following result (ignoring coeﬃcient operations).

Theorem 4. The n-th entry in a holonomic sequence depending on v parameters can be evaluated with rectangular splitting using O(mv + n/m) nonscalar multiplications and O((n/m)mv) scalar multiplications. In particular, taking m = n1/(v+1), O(n1−1/v) nonscalar multiplications and O(n2v/(1+v)) scalar multiplications suﬃce.

Proof. If di = degx

i

M ≤ d, the entries of a product of m successive shifts of M are C-linear combinations of xe11,j · · · xehv,j, 0 ≤ ei,j ≤ mdi ≤ md, so there is a total of O(mv) powers.

![image 24](<2013-johansson-evaluating-parametric-holonomic-sequences_images/imageFile24.png>)

![image 25](<2013-johansson-evaluating-parametric-holonomic-sequences_images/imageFile25.png>)

![image 26](<2013-johansson-evaluating-parametric-holonomic-sequences_images/imageFile26.png>)

![image 27](<2013-johansson-evaluating-parametric-holonomic-sequences_images/imageFile27.png>)

Unfortunately, this gives rapidly diminishing returns for large v. When v > 1, the number of nonscalar multiplications according to Theorem 4 is asymptotically worse than with fast multipoint evaluation, and reducing the number of nonscalar multiplication requires us to perform more than O(n) scalar multiplications, as shown in Table 1. Nevertheless, rectangular splitting could perhaps still be useful in some settings where the cost of nonscalar multiplications is suﬃciently large.

v m Nonscalar Scalar

![image 28](<2013-johansson-evaluating-parametric-holonomic-sequences_images/imageFile28.png>)

- 1 n1/2 O(n0.5) O(n)
- 2 n1/3 O(n0.666...) O(n1.333...)
- 3 n1/4 O(n0.75) O(n1.5)
- 4 n1/5 O(n0.8) O(n1.6)


![image 29](<2013-johansson-evaluating-parametric-holonomic-sequences_images/imageFile29.png>)

Table 1: Step size m minimizing the number of nonscalar multiplications for rectangular splitting involving v parameters.

- 4. NUMERICAL EVALUATION


Assume that we want to evaluate c(x, n) where the underlying coeﬃcient ring is C = Z (or Q) and the parameter x is a real or complex number represented by a ﬂoating-point approximation with a precision of p bits.

![image 30](<2013-johansson-evaluating-parametric-holonomic-sequences_images/imageFile30.png>)

Let MZ(p) denote the bit complexity of some algorithm for multiplying two p-bit integers or ﬂoating-point numbers. Commonly used algorithms include classical multiplication with MZ(p) = O(p2), Karatsuba multiplication with MZ(p) = O(p1.585), and Fast Fourier Transform (FFT) based multiplication, such as the Sch¨onhage-Strassen algorithm, with MZ(p) = O˜(p). An unbalanced multiplication where the smaller operand has q bits can be done using O((p/q)MZ(q)) bit operations [5].

The naive algorithm clearly uses O(nMZ(p)) bit operations to evaluate c(x, n), or O˜(np) with FFT multiplication. In Algorithm 3, the nonscalar multiplications cost O((m + n/m)MZ(p)) bit operations. The coeﬃcient operations cost O˜(mn) bit operations (assuming the use of fast polynomial arithmetic), which becomes negligible if p grows faster than m. Finally, the scalar multiplications (which are

unbalanced) cost

MZ(mlog m) m log m

O n p

![image 31](<2013-johansson-evaluating-parametric-holonomic-sequences_images/imageFile31.png>)

bit operations. Taking m ∼ nα for 0 < α < 1, we get an asymptotic speedup with classical or Karatsuba multiplication (see Table 2) provided that p grows suﬃciently rapidly along with n. With FFT multiplication, the scalar multiplications become as expensive as the nonscalar multiplications, and rectangular therefore does not give an asymptotic improvement.

Mult. algorithm Scalar multiplications Naive Classical O˜(n1+αp) O˜(np2) Karatsuba O˜(n1+0.585αp) O˜(np1.585) FFT O˜(np) O˜(np)

![image 32](<2013-johansson-evaluating-parametric-holonomic-sequences_images/imageFile32.png>)

![image 33](<2013-johansson-evaluating-parametric-holonomic-sequences_images/imageFile33.png>)

![image 34](<2013-johansson-evaluating-parametric-holonomic-sequences_images/imageFile34.png>)

![image 35](<2013-johansson-evaluating-parametric-holonomic-sequences_images/imageFile35.png>)

- Table 2: Bit complexity of scalar multiplications in


- Algorithm 3 and total bit complexity of the naive algorithm


However, due to the overhead of FFT multiplication, rectangular splitting is still likely to save a constant factor over the naive algorithm. In practice, one does not necessarily get the best performance by choosing m ≈ n0.5 to minimize the number of nonscalar multiplications alone; the best m has to be determined empirically.

Algorithm 1 is asymptotically faster than the naive algorithm as well as rectangular splitting, with a bit complexity of O˜(n1/2p). It should be noted that this estimate does not reﬂect the complexity required to obtain a given accuracy. As observed by K¨ohler and Ziegler [9], fast multipoint evaluation can exhibit poor numerical stability, suggesting that p might have to grow at least as fast as n to get accuracy proportional to p.

When x and all coeﬃcients in M are positive, rectangular splitting introduces no subtractions that can cause catastrophic cancellation, and the reduction of nonscalar multiplications even improves stability compared to the naive algorithm, making O(log n) guard bits suﬃcient to reach p-bit accuracy. When sign changes are present, evaluating degree-m polynomials in expanded form can reduce accuracy, typically requiring use of O˜(m) guard bits. In this case Algorithm 3 is a marked improvement over Algorithm 2.

## 4.1 Summation of power series

A common situation is that we wish to evaluate a truncated power series

f(x) ≈ s(x,n) =

n

c(k)xk, n = O(p) (7)

k=0

where c(k) is a holonomic sequence taking rational (or algebraic) values and x is a real or complex number. In this case the Paterson-Stockmeyer algorithm is applicable, but might not give a speedup when applied directly as in Algorithm 2 due to the growth of the coeﬃcients. Since d(k) = c(k)xk and s(x, n) are holonomic sequences with x as parameter, Algorithm 3 is applicable.

Smith noted in [12] that when c(k) is hypergeometric (Smith considered the Taylor expansions of elementary functions in particular), the Paterson-Stockmeyer technique can be combined with scalar divisions to remove accumulated

factors from the coeﬃcients. This keeps all scalars at a size of O(log n) bits, giving a speedup over naive evaluation when non-FFT multiplication is used (and when scalar divisions are assumed to be roughly as cheap as scalar multiplications). This algorithm is studied in more detail by Brent and Zimmermann [5].

At least conceptually, Algorithm 3 can be viewed as a generalization of Smith’s hypergeometric summation algorithm to arbitrary holonomic sequences depending on a parameter (both algorithms can be viewed as means to eliminate repeated content from the associated matrix product). The speedup is not quite as good since we only reduce the coeﬃcients to O(n1/2 log n) bits versus Smith’s O(log n). However, even for hypergeometric series, Algorithm 3 can be slightly faster than Smith’s algorithm for small n (e.g. n 100) since divisions tend to be more expensive than scalar multiplications in implementations.

Algorithm 3 is also more general: for example, we can use it to evaluate the generalized hypergeometric function

pFq

- a1, . . . , ap
- b1, . . . , bq


![image 36](<2013-johansson-evaluating-parametric-holonomic-sequences_images/imageFile36.png>)

![image 37](<2013-johansson-evaluating-parametric-holonomic-sequences_images/imageFile37.png>)

ak1 · · · akp bk1 · · · bkq

∞

wk k!

![image 38](<2013-johansson-evaluating-parametric-holonomic-sequences_images/imageFile38.png>)

z =

![image 39](<2013-johansson-evaluating-parametric-holonomic-sequences_images/imageFile39.png>)

![image 40](<2013-johansson-evaluating-parametric-holonomic-sequences_images/imageFile40.png>)

![image 41](<2013-johansson-evaluating-parametric-holonomic-sequences_images/imageFile41.png>)

![image 42](<2013-johansson-evaluating-parametric-holonomic-sequences_images/imageFile42.png>)

k=0

(8)

where ai, bi, w (as opposed to w alone) are rational functions of the real or complex parameter x.

An interesting question, which we do not attempt to answer here, is whether there is a larger class of parametric sequences other than hypergeometric sequences and their sums for which we can reduce the number of nonscalar multiplications to O(n1/2) while working with coeﬃcients that are strictly smaller than O(n1/2 log n) bits.

## 4.2 Comparison with asymptotically faster algorithms

If all coeﬃcients in (7) including the parameter x are rational or algebraic numbers and the series converges, f(x) can be evaluated to p-bit precision using O˜(p) bit operations using binary splitting. An O˜(p) bit complexity can also be achieved for arbitrary real or complex x by combining binary splitting with translation of the diﬀerential equation for f(x). The general version of this algorithm, sometimes called the bit-burst algorithm, was developed by Chudnovsky and Chudnovsky and independently with improvements by van der Hoeven [14]. It is used in some form for evaluating elementary functions in several libraries, and a general version has been implemented by Mezzarobba [10].

For high-precision evaluation of elementary functions, binary splitting typically only becomes worthwhile at a precision of several thousand digits, while implementations typically use Smith’s algorithm for summation of hypergeometric series at lower precision. We expect that Algorithm 3 can be used in a similar fashion for a wider class of special functions.

When c(k) in (7) involves real or complex numbers, binary splitting no longer gives a speedup. In this case, we can use fast multipoint to evaluate (7) using O˜(p1.5) bit operations (Borwein [3] discusses the application to numerical evaluation of hypergeometric functions). This method does not appear to be widely used in practice, presumably owing to its high overhead and relative implementation diﬃculty. Although rectangular splitting is not as fast asymptotically, its ease of implementation and low overhead makes it an attractive alternative.

## 5. HIGH-PRECISION COMPUTATION OF THE GAMMA FUNCTION

polynomials can be written down explicitly as

m−v−1

m−1

ki Cm(v,i)

xv

∆m = (x + k + m)m − (x + k)m =

![image 43](<2013-johansson-evaluating-parametric-holonomic-sequences_images/imageFile43.png>)

![image 44](<2013-johansson-evaluating-parametric-holonomic-sequences_images/imageFile44.png>)

In this section, we consider two holonomic sequences depending on a numerical parameter: rising factorials, and the partial sums of a certain hypergeometric series deﬁning the incomplete gamma function. In both cases, our goal is to accelerate numerical evaluation of the gamma function at very high precision.

i=0

v=0

(9) where

m−v

j i

v + j v

mj−iS(m,v + j)

(10)

Cm(v, i) =

We have implemented the algorithms in the present section using ﬂoating-point ball arithmetic (with rigorous error bounding) as part of the Arb library1. All arithmetic in Z[x] is done via FLINT [8], using a Sch¨onhage-Strassen FFT implemented by W. Hart.

j=i+1

and where S(m, v + j) denotes an unsigned Stirling number of the ﬁrst kind. This formula can be used to generate ∆m eﬃciently in practice without requiring bivariate polynomial arithmetic. In fact, the coeﬃcients can be generated even cheaper by taking advantage of the recurrence (found by M. Kauers)

Fast numerically stable multiplication in R[x] is done by breaking polynomials into segments with similarly-sized coeﬃcients and computing the subproducts exactly in Z[x] (a simpliﬁed version of van der Hoeven’s block multiplication algorithm [15]), and asymptotically fast polynomial division is implemented using Newton iteration.

(v + 1)Cm(v + 1, i) = (i + 1)Cm(v, i + 1). (11)

We have implemented several algorithm for evaluating the rising factorial of a real or complex number. For tuning parameters, we empirically determined simple formulas that give nearly optimal performance for diﬀerent combinations of n, p < 105 (typically within 20% of the speed with the best tuning value found by a brute force search):

All benchmark results were obtained on a 2.0 GHz Intel Xeon E5-2650 CPU.

## 5.1 Rising factorials

Rising factorials of a real or complex argument appear when evaluating the gamma function via the asymptotic Stirling series

- • In Algorithm 1, m = n0.5.
- • Algorithm 2 is applied to subproducts of length n˜ = min(2n0.5, 10p0.25), with m = n˜0.5.
- • In Algorithms 3 and 4, m = min(0.2p0.4, n0.5).


- 1

![image 45](<2013-johansson-evaluating-parametric-holonomic-sequences_images/imageFile45.png>)

- 2


log 2π 2

log Γ(x) = x −

log x − x +

![image 46](<2013-johansson-evaluating-parametric-holonomic-sequences_images/imageFile46.png>)

N−1

Our implementation of Algorithm 4 uses (10) instead of binary splitting, and Algorithm 3 exploits the symmetry of x and k to update the matrix U using Taylor shifts instead of repeated binary splitting.

B2k 2k(2k − 1)x2k−1

+ RN(x).

+

![image 47](<2013-johansson-evaluating-parametric-holonomic-sequences_images/imageFile47.png>)

k=1

To compute Γ(x) with p-bit accuracy, we choose a positive integer n such that there is an N for which |RN(x + n)| < 2−p, and then evaluate Γ(x) = Γ(x + n)/xn. It is suﬃcient to choose n such that the real part of x + n is of order βp where β = (2π)−1 log 2 ≈ 0.11.

Figure 5.1 compares the running times where x is a real number with a precision of p = 4n bits. This input corresponds to that used in our Stirling series implementation of the gamma function.

![image 48](<2013-johansson-evaluating-parametric-holonomic-sequences_images/imageFile48.png>)

The eﬃciency of the Stirling series can be improved by choosing n slightly larger than the absolute minimum in order to reduce N. For example, Re(x + n) ≈ 2βp is a good choice. A faster rising factorial is doubly advantageous: it speeds up the argument reduction, and making larger n cheap allows us to get away with fewer Bernoulli numbers.

![image 49](<2013-johansson-evaluating-parametric-holonomic-sequences_images/imageFile49.png>)

![image 50](<2013-johansson-evaluating-parametric-holonomic-sequences_images/imageFile50.png>)

![image 51](<2013-johansson-evaluating-parametric-holonomic-sequences_images/imageFile51.png>)

Smith [13] uses the diﬀerence of four consecutive terms

![image 52](<2013-johansson-evaluating-parametric-holonomic-sequences_images/imageFile52.png>)

![image 53](<2013-johansson-evaluating-parametric-holonomic-sequences_images/imageFile53.png>)

(x + k + 4)4 − (x + k)4 = (840 + 632k + 168k2 + 16k3)

+ (632 + 336k + 48k2)x

![image 54](<2013-johansson-evaluating-parametric-holonomic-sequences_images/imageFile54.png>)

+ (168 + 48k)x2

+ 16x3

![image 55](<2013-johansson-evaluating-parametric-holonomic-sequences_images/imageFile55.png>)

![image 56](<2013-johansson-evaluating-parametric-holonomic-sequences_images/imageFile56.png>)

![image 57](<2013-johansson-evaluating-parametric-holonomic-sequences_images/imageFile57.png>)

![image 58](<2013-johansson-evaluating-parametric-holonomic-sequences_images/imageFile58.png>)

![image 59](<2013-johansson-evaluating-parametric-holonomic-sequences_images/imageFile59.png>)

![image 60](<2013-johansson-evaluating-parametric-holonomic-sequences_images/imageFile60.png>)

![image 61](<2013-johansson-evaluating-parametric-holonomic-sequences_images/imageFile61.png>)

to reduce the number of nonscalar multiplications to compute xn from n − 1 to about n/4. This is precisely Algorithm 4 specialized to the sequence of rising factorials and with a ﬁxed step length m = 4.

![image 62](<2013-johansson-evaluating-parametric-holonomic-sequences_images/imageFile62.png>)

Figure 1: Timings of rising factorial algorithms, normalized against the naive algorithm.

Consider Smith’s algorithm with a variable step length m. Using the binomial theorem and some rearrangements, the

![image 63](<2013-johansson-evaluating-parametric-holonomic-sequences_images/imageFile63.png>)

1http://fredrikj.net/arb

On this benchmark, Algorithms 3 and 4 are the best by far, gaining a 20-fold speedup over the naive algorithm for

large n (the speedup levels oﬀ around n = 105, which is expected since this is the approximate point where FFT integer multiplication kicks in). Algorithm 4 is slightly faster than Algorithm 3 for n < 103, even narrowly beating the naive algorithm for n as small as ≈ 102.

where M(k) =

1 + k + z 1 + k + z 0 N

, q(k) = 1 + k + z. (14)

The matrix product (13) may be computed using fast multipoint evaluation or rectangular splitting. We note that the denominators are identical to the top left entries of the numerator matrices, and therefore do not need to be computed separately.

Algorithm 1 (fast multipoint evaluation) has the most overhead of all algorithms and only overtakes the naive algorithm around n = 104 (at a precision of 40, 000 bits). Despite its theoretical advantage, it is slower than rectangular splitting up to n exceeding 106.

Figure 5.2 compares the performance of the Stirling series (with fast argument reduction using rectangular splitting) and three diﬀerent implementations of the 1F1 series (naive summation, fast multipoint evaluation, and rectangular splitting using Algorithm 3 with m = 0.2n0.4) for evaluating Γ(x) where x is a real argument close to unity.

Table 5.1 shows absolute timings for evaluating Γ(x) where x is a small real number in Pari/GP 2.5.4, and our implementation in Arb (we omit results for MPFR 3.1.1 and Mathematica 9.0, which both were slower than Pari). Both implementations use the Stirling series, caching the Bernoulli numbers to speed up multiple evaluations. The better speed of Arb for a repeated evaluation (where the Bernoulli numbers are already cached) is mainly due to the use of rectangular splitting to evaluate the rising factorial. The total speedup is smaller than it would be for computing the rising factorial alone since we still have to evaluate the Bernoulli number sum in the Stirling series. The gamma function implementations over C have similar characteristics.

![image 64](<2013-johansson-evaluating-parametric-holonomic-sequences_images/imageFile64.png>)

![image 65](<2013-johansson-evaluating-parametric-holonomic-sequences_images/imageFile65.png>)

![image 66](<2013-johansson-evaluating-parametric-holonomic-sequences_images/imageFile66.png>)

![image 67](<2013-johansson-evaluating-parametric-holonomic-sequences_images/imageFile67.png>)

![image 68](<2013-johansson-evaluating-parametric-holonomic-sequences_images/imageFile68.png>)

![image 69](<2013-johansson-evaluating-parametric-holonomic-sequences_images/imageFile69.png>)

![image 70](<2013-johansson-evaluating-parametric-holonomic-sequences_images/imageFile70.png>)

![image 71](<2013-johansson-evaluating-parametric-holonomic-sequences_images/imageFile71.png>)

![image 72](<2013-johansson-evaluating-parametric-holonomic-sequences_images/imageFile72.png>)

Decimals Pari/GP (ﬁrst) Arb (ﬁrst)

![image 73](<2013-johansson-evaluating-parametric-holonomic-sequences_images/imageFile73.png>)

100 0.000088 0.00010 300 0.00048 0.00036

![image 74](<2013-johansson-evaluating-parametric-holonomic-sequences_images/imageFile74.png>)

1000 0.0057 0.0025 3000 0.072 (9.2) 0.021 (0.090)

![image 75](<2013-johansson-evaluating-parametric-holonomic-sequences_images/imageFile75.png>)

10000 1.2 (324) 0.25 (1.4) 30000 15 (8697) 2.7 (22) 100000 39 (433) 300000 431 (7131)

![image 76](<2013-johansson-evaluating-parametric-holonomic-sequences_images/imageFile76.png>)

![image 77](<2013-johansson-evaluating-parametric-holonomic-sequences_images/imageFile77.png>)

![image 78](<2013-johansson-evaluating-parametric-holonomic-sequences_images/imageFile78.png>)

![image 79](<2013-johansson-evaluating-parametric-holonomic-sequences_images/imageFile79.png>)

![image 80](<2013-johansson-evaluating-parametric-holonomic-sequences_images/imageFile80.png>)

![image 81](<2013-johansson-evaluating-parametric-holonomic-sequences_images/imageFile81.png>)

- Table 3: Timings in seconds for evaluating Γ(x) where x is a small real number (timings for the ﬁrst evaluation, including Bernoulli number generation, is shown in parentheses).


Figure 2: Timings of gamma function algorithms, normalized against the Stirling series with Bernoulli numbers cached.

## 5.2 A one-parameter hypergeometric series

The gamma function can be approximated via the (lower) incomplete gamma function as

Γ(z) ≈ γ(z, N) = z−1Nze−N 1F1(1, 1 + z, N). (12)

Borwein [3] noted that applying fast multipoint evaluation to a suitable truncation of the hypergeometric series in (12) allows evaluating the gamma function of a ﬁxed real or complex argument to p-bit precision using O˜(p1.5) bit operations, which is the best known result for general z (if z is algebraic, binary splitting evaluation of the same series achieves a complexity of O˜(p)).

Let tk = Nk/(z(z + 1) · · · (z + k)) and sn = nk=0 tk, giving

lim

sn = 1F1(1, 1 + z, N)/z.

n→∞

For z ∈ [1, 2], choosing N ≈ plog 2 and n ≈ (elog 2)p gives an error of order 2−p (it is easy to compute strict bounds). The partial sums satisfy the order-2 recurrence

sk tk+1

M(k) q(k)

M(k − 1) q(k − 1)

=

· · ·

![image 82](<2013-johansson-evaluating-parametric-holonomic-sequences_images/imageFile82.png>)

![image 83](<2013-johansson-evaluating-parametric-holonomic-sequences_images/imageFile83.png>)

M(0) q(0)

![image 84](<2013-johansson-evaluating-parametric-holonomic-sequences_images/imageFile84.png>)

- 0
- 1/z


(13)

Both fast multipoint evaluation and rectangular splitting speed up the hypergeometric series compared to naive summation. Using either algorithm, the hypergeometric series is competitive with the Stirling series for a single evaluation at precisions above roughly 10,000 decimal digits.

Algorithm 1 performs better than on the rising factorial benchmark, and is faster than Algorithm 3 above 105 bits. A possible explanation for this diﬀerence is that the number of terms used in the hypergeometric series roughly is n ≈ 2p where p is the precision in bits, compared to n ≈ p/4 for the rising factorial, and rectangular splitting favors higher precision and fewer terms.

The speed of Algorithm 3 is remarkably close to that of Algorithm 1 even for p as large as 106. Despite being asymptotically slower, the simplicity of rectangular splitting combined with its lower memory consumption and better numerical stability (in our implementation, Algorithm 3 only loses a few signiﬁcant digits, while Algorithm 1 loses a few percent of the number of signiﬁcant digits) makes it an attractive option for extremely high-precision evaluation of the gamma function.

Once the Bernoulli numbers have been cached after the ﬁrst evaluation, the Stirling series still has a clear advantage up to precisions exceeding 106 bits. We may remark that

our implementation of the Stirling series has been optimized for multiple evaluations: by choosing larger rising factorials and generating the Bernoulli numbers dynamically without storing them, both the speed and memory consumption for a single evaluation could be improved.

## 6. DISCUSSION

We have shown that rectangular splitting can be profitably applied to evaluation of a general class of linearly recurrent sequences. When used for numerical evaluation of special functions, our benchmark results indicate that rectangular splitting can be faster than either naive evaluation or fast multipoint evaluation over a wide precision range (between approximately 103 and 106 bits).

Two natural questions are whether this approach can be generalized further (to more general classes of sequences), and whether it can be optimized further (perhaps for more speciﬁc classes of sequences).

## 7. ACKNOWLEDGEMENTS

The author thanks Manuel Kauers for providing useful feedback on draft versions of this paper.

## 8. REFERENCES

- [1] A. V. Aho, K. Steiglitz, and J. D. Ullman. Evaluating polynomials at ﬁxed sets of points. SIAM Journal on Computing, 4(4):533–539, 1975.
- [2] D. J. Bernstein. Fast multiplication and its applications. Algorithmic Number Theory, 44:325–384, 2008.
- [3] P. B. Borwein. Reduced complexity evaluation of hypergeometric functions. Journal of Approximation Theory, 50(3), July 1987.
- [4] A. Bostan, P. Gaudry, and E.´ Schost. Linear recurrences with polynomial coeﬃcients and application to integer factorization and Cartier-Manin operator. SIAM Journal on Computing, 36(6):1777–1806, 2007.
- [5] R. P. Brent and P. Zimmermann. Modern Computer Arithmetic. Cambridge University Press, 2011.
- [6] D. G. Cantor and E. Kaltofen. On fast multiplication of polynomials over arbitrary algebras. Acta Informatica, 28(7):693–701, 1991.
- [7] D. V. Chudnovsky and G. V. Chudnovsky. Approximations and complex multiplication according to Ramanujan. In Ramanujan Revisited, pages 375–472. Academic Press, 1988.
- [8] W. B. Hart. Fast Library for Number Theory: An Introduction. In Proceedings of the Third international congress conference on Mathematical software, ICMS’10, pages 88–91, Berlin, Heidelberg, 2010. Springer-Verlag. http://flintlib.org.
- [9] S. K¨ohler and M. Ziegler. On the stability of fast polynomial arithmetic. In Proceedings of the 8th Conference on Real Numbers and Computers, Santiago de Compostela, Spain, 2008.
- [10] M. Mezzarobba. NumGfun: a package for numerical and analytic computation with D-ﬁnite functions. In Proceedings of ISSAC’10, pages 139–146, 2010.
- [11] M. S. Paterson and L. J. Stockmeyer. On the number of nonscalar multiplications necessary to evaluate


- polynomials. SIAM Journal on Computing, 2(1), March 1973.
- [12] D. M. Smith. Eﬃcient multiple-precision evaluation of elementary functions. Mathematics of Computation, 52:131–134, 1989.
- [13] D. M. Smith. Algorithm: Fortran 90 software for ﬂoating-point multiple precision arithmetic, gamma and related functions. Transactions on Mathematical Software, 27:377–387, 2001.
- [14] J. van der Hoeven. Fast evaluation of holonomic functions. TCS, 210:199–215, 1999.
- [15] J. van der Hoeven. Making fast multiplication of polynomials numerically stable. Technical Report 2008-02, Universite´ Paris-Sud, Orsay, France, 2008.
- [16] J. von zur Gathen and J. Gerhard. Fast algorithms for Taylor shifts and certain diﬀerence equations. In Proceedings of ISSAC’97, pages 40–47, 1997.
- [17] J. von zur Gathen and J. Gerhard. Modern Computer Algebra. Cambridge University Press, 2nd edition, 2003.
- [18] M. Ziegler. Fast (multi-)evaluation of linearly recurrent sequences: Improvements and applications.


2005. http://arxiv.org/abs/cs/0511033.

