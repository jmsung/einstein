# arXiv:1605.02994v3[math.PR]15Feb2018

## UPPER TAIL LARGE DEVIATIONS FOR ARITHMETIC PROGRESSIONS IN A RANDOM SET

BHASWAR B. BHATTACHARYA, SHIRSHENDU GANGULY, XUANCHENG SHAO, AND YUFEI ZHAO

Abstract. Let Xk denote the number of k-term arithmetic progressions in a random subset of Z/NZ or {1,...,N} where every element is included independently with probability p. We determine the asymptotics of log P(Xk ≥ (1 + δ)EXk) (also known as the large deviation rate) where p → 0 with p ≥ N−c

k for some constant ck > 0, which answers a question of Chatterjee and Dembo. The proofs rely on the recent nonlinear large deviation principle of Eldan, which improved on earlier results of Chatterjee and Dembo. Our results complement those of Warnke, who used completely diﬀerent methods to estimate, for the full range of p, the large deviation rate up to a constant factor.

Contents

- 1. Introduction 1
- 2. Statements of results 3
- 3. Gaussian width and non-linear large deviations 7
- 4. Bounds on Gaussian width 11
- 5. Variational problem at the macroscopic scale 16
- 6. Variational problem at the microscopic scale 21
- 7. Replica symmetry 25
- 8. Maximizing the number of k-APs 27 Appendix A. Proofs of further bounds on Gaussian widths 31 References 32


1. Introduction

Let Xk denote the number of k-term arithmetic progressions (k-AP) in the random set Ωp, where Ω is taken to be either Z/NZ or [N] := {1,...,N} throughout this paper, and Ωp denotes the random subset of Ω where every element is included independently with probability p. The upper tail problem asks to estimate the probability that Xk signiﬁcantly exceeds its expectation. This problem has received some interest over the years [8, 25, 31]. More generally, the problem of computing tail probabilities of a sum of weakly dependent random variables has a long and interesting history [2, 6, 8, 9, 10, 13, 14, 22, 23, 24, 25, 26, 28, 27, 30, 31]. There has been many exciting recent developments, particularly in the setting of random graphs [6, 8, 14], where one is interested in the concentration of the number of triangles in

SG was supported by a Miller Research Fellowship. XS was supported by a Glasstone Research Fellowship. YZ was supported by an Esmée Fairbairn Junior Research Fellowship at New College, Oxford and NSF

Award DMS-1362326.

1

an Erdős–Rényi random graph G(N,p). See Chatterjee’s recent survey [7] and the references therein for an introduction to recent developments on large deviations in random graphs.

The recent work of Warnke [31] settles the question of the asymptotic order of P(Xk ≥ (1 + δ)EXk) when Ω = [N]. Warnke [31] shows that for ﬁxed δ > 0 and k ≥ 3, there exists constants c,C > 0 (depending only on k) such that

√

√

δNpk/2 ≤ P(Xk ≥ (1 + δ)EXk) ≤ pc

δNpk/2, (1.1)

pC

as long as p = pN ≥ (log N/N)1/(k−1) and p is bounded away from 1. Prior to Warnke’s work, the best upper bound [25] was P(Xk ≥ (1 + δ)EXk) ≤ e−c

δpk/2N, for some constant cδ > 0 depending on k and δ. However, the natural question of precise asymptotics still remained open.

The main result of this paper shows for every k ≥ 3, ﬁxed δ > 0, and Ω = [N], if p = pN ≥ N−

1

6k(k−1) log N and p → 0, then, as N → ∞, P(Xk ≥ (1 + δ)EXk) = p(1+o(1))

√

δNpk/2. (1.2)

The lower bound to the probability can be seen by forcing an interval of length (1 + o(1))

√

δpk/2N to be present in Ω, so that it generates the extra δEXk many k-APs as desired. For the special case of k = 3, which was also treated in [8], methods in [15] combined with Fourier analysis allow us to take p ≥ N−1/18 log N, improving on the p ≥ N−1/162(log N)34/162 hypothesis in [8]. For k ≥ 4, (1.2) is the ﬁrst large deviation result for k-AP counts allowing p to decay as N−c, thereby answering a question posed by Chatterjee and Dembo [8, Section 1.8] and improving on Warnke’s result in the appropriate regime.1

The proofs rely on the powerful nonlinear large deviation principle (LDP) developed by Chatterjee and Dembo [8], which was recently improved by Eldan [15] using diﬀerent methods, namely stochastic control theory. These LDPs reduce the determination of the large deviation rate (i.e., asymptotics of log-probability) in many combinatorial problems to a natural variational problem involving entropies. For the problem of upper tails of subgraph counts in a sparse random graph, the corresponding variational problem was recently solved [2, 28]. For arithmetic progressions, Chatterjee and Dembo were able to verify the hypotheses of their LDP for 3-term arithmetic progressions but not longer ones [8, Section 1.5]. More recently, Eldan [15] provided a diﬀerent, but related, set of hypotheses for his LDP, involving the supremum of an associated Gaussian process (see Theorem 3.1). We prove the necessary bounds to apply Eldan’s LDP for arithmetic progressions of arbitrary ﬁxed length. We remark that similar arguments can also be used to verify Chatterjee and Dembo’s LDP hypotheses for arithmetic progressions of any ﬁxed length. Some interesting open problems in additive combinatorics arise in the analysis of this Gaussian process (see Section 4).

After establishing the LDP, we solve the corresponding variational problem. Here, there are two regimes, below, depending on how δ decays to zero compared to p.

(1) In the macroscopic (large δ) regime, where δ−3pk−2(log(1/p))2 → 0, the solution of the variational problem reduces to the extremal problem of maximizing the number of k-APs in a set of given size, which was solved by Green and Sisask [18] for 3-APs, and extended to k-APs in Theorem 2.4. The solution to this extremal problem is

1In a previous arXiv version of this paper, we proved the result with p decaying extremely slowly, as our previous proof depended on the heavy-powered inverse theorem for Gowers uniformity norms due to Green, Tao, and Ziegler [20].

attained by an interval. The case of ﬁxed δ > 0, namely the asymptotic (1.2), belongs to this regime.

(2) In the microscopic (small δ) regime, where δ−3pk−2(log(1/p))2 → ∞, the variational problem exhibits a rather diﬀerent qualitative behavior compared to the previous case. We show that

2Np, for some explicit constant c > 0 depending on k and Ω.

P(Xk ≥ (1 + δ)EXk) = e−(c+o(1))δ

Note that in both these regimes above we require p = pN → 0. If both p and δ are ﬁxed, the situation is quite diﬀerent, and we report some partial results for this setting in Section 7.

It is worth comparing these results for arithmetic progressions to the corresponding results for triangles in a random graph. Let XK

denote the number of copies of K3 in G(N,p). It was shown in [28] (again relying on [8], which was recently improved in [15]) that for p = pN → 0 with p ≥ N−1/18 log N and ﬁxed δ > 0, one has

3

2/3/2, δ/3}N2p2.

) = p(1+o(1)) min{δ

P(XK

3 ≥ (1 + δ)EXK

3

This result was extended in [2], which determined the upper tail large deviation rate of XH for every graph H. The extra complexity in the above expression, as compared to (1.2), arises from the dichotomy of methods of generating many extra triangles: we can either force a clique to be present, or force a small subset of vertices to be connected to all other vertices.

2. Statements of results

- 2.1. Notation. We recall some standard asymptotic notations. For two nonnegative sequences (fn)n≥1 and (gn)n≥1, fn gn means fn = O(gn); fn ∼ gn means fn = (1 + o(1))gn; and fn gn means fn = Θ(gn), i.e., fn gn fn. Subscripts in the above notation, for example, O (·), , denote that the hidden constants may depend on the subscripted parameters. We always treat k (as in k-AP) as a constant, and the dependence of the hidden constants on k is always implicitly assumed and may be suppressed in the asymptotic notation.


For any set A in some ambient abelian group (in this paper the ambient group will always be either Z or Z/NZ) and k ≥ 3, we write Tk(A) to denote the number of pairs (a,b) of elements in the ambient group such that a,a + b,a + 2b,...,a + (k − 1)b ∈ A. Note that every non-trivial k-AP is counted twice, and every trivial k-AP (i.e., b = 0) is counted once. It will be convenient to state our results in terms of Tk(A).

For p ∈ (0,1) and a subset Ω in the ambient group, denote by Ωp ⊂ Ω the random set obtained by independently including each element in Ω with probability p. Throughout the paper, we will consider two settings:

- (1) Ω = [N] = {1,...,N}, and
- (2) Ω = Z/NZ.


The ambient group is Z and Z/NZ in the two respective settings. Note that, as long as pk−1N → ∞, it is easy to see that ETk(Ωp) = pk(Tk(Ω)−|Ω|)+p|Ω| ∼ pkTk(Ω). In this paper we are interested in the upper tail probability, P(Tk(Ωp) ≥ (1+δ)ETk(Ωp)), when p = pN → 0, as N → ∞ (δ = δN may also depend on N).

The relative entropy function with respect to Bernoulli(p) is denoted Ip(x) := xlog

1 − x 1 − p

x p

+ (1 − x)log

.

Finally, denote the weighted k-AP count of a function f : Ω → R by Tk(f) :=

f(a)f(a + b)···f(a + (k − 1)b). (2.1)

a,b

Here a and b each range over all elements of the ambient group (either Z or Z/NZ) such that {a,a + b,...,a + (k − 1)b} ⊂ Ω. By convention, when Ω = [N], we set f(x) = 0 for all x ∈/ Ω. Note that Tk(A) = Tk(1A), where 1A is the indicator function of A.

## 2.2. Large deviation principle. Let us write

Ip(f(a)) : Tk(f) ≥ (1 + δ)pkTk(Ω) (2.2)

φ(pk,Ω)(δ) := inf

f : Ω→[0,1]

a∈Ω

for the natural large deviations variational problem for upper tails of k-AP counts. We will establish in Section 3.1 the following LDP for k-APs, via Eldan’s LDP [15].

- Theorem 2.1. Fix k ≥ 3. Let Ω = [N] or Z/NZ. Let p = pN be bounded away from 1, and δ = δN > 0 with δ = O(1) such that


1

min{δpk,δ2p} ≥ N−

6(k−1) log N. (2.3) Then, as N → ∞,

− log P(Tk(Ωp) ≥ (1 + δ)ETk(Ωp)) = (1 + o(1))φ(pk,Ω)(δ + o(δ)). (2.4)

Furthermore, for k = 3, the right-hand side of (2.3) can be relaxed to N−1/6(log N)7/6; for k = 4, it can be relaxed to N−1/12(log N)13/12.

1

Remark. For ﬁxed δ > 0, the theorem requires p to decay slower than N−

6k(k−1). Very recently, Briët and Gopi [5] improved the exponent from 6k(k1−1) to 6k (k−11)/2 , which improves our result for all k ≥ 5. It remains an open problem to extend the range of validity of p. In comparison, Warnke’s asymptotics (1.1) on the order of log-probability holds for all p ≥ (log N/N)1/(k−1).

In the above theorem, δ is allowed to decay as a function of N, and there is a qualitative

change in the behavior of φ(pk,Ω)(δ) depending on how quickly δ decays compared to p. Drawing a parallel from statistical physics2, we refer to the two regimes by:

- • Macroscopic scale: when δ is “large”, namely when δ−3pk−2(log(1/p))2 → 0; and
- • Microscopic scale: when δ is “small”, namely when δ−3pk−2(log(1/p))2 → ∞.


### 2.3. Macroscopic scale. In the macroscopic scale, δ−3pk−2(log(1/p))2 → 0. Here, it might be helpful to think of δ as a constant or tending to zero “slowly” compared to p. We will establish, in Section 5, the following asymptotic solution to the variational problem (2.2) in this regime.

2The terms macroscopic/microscopic appear in many contexts in the statistical mechanics literature, and is generically used to described large/small scale behaviors, respectively. However, the exact deﬁnitions vary depending on the problem in question.

- Theorem 2.2. Fix k ≥ 3. Let Ω = [N] or Z/NZ, and in the latter case assume that N


is prime. Let p = pN → 0 and δ = δN > 0 be such that δ = O(1), δpkN2 → ∞, and δ−3pk−2(log(1/p))2 → 0. Then, as N → ∞,

φ(pk,Ω)(δ) = (1 + o(1)) (k − 1)δpkTk(Ω)log(1/p)

√

δpk/2N log(1/p) if Ω = [N], (1 + o(1)) (k − 1)δpk/2N log(1/p) if Ω = Z/NZ with prime N.

(1 + o(1))

=

Remark. In the case of constant δ, say, while the above solution to the variation problem needs only pkN2 → ∞, a stronger condition pk−1N → ∞ (implying ETk(Ωp) ∼ pkTk(Ω)) is necessary even just for the concentration of the random variable Tk(Ωp).

We prove Theorem 2.2 by ﬁrst reducing the variational problem to an extremal problem in additive combinatorics, namely that of determining the size of the smallest subset of Ω with a given number of k-APs, or equivalently, the maximum number of k-APs in a subset of Ω of a given size.

- Proposition 2.3. Under the same hypotheses as Theorem 2.2 (except that N is not required to be prime in the case Ω = Z/NZ), as N → ∞,


|S| : Tk(S) ≥ δpkTk(Ω) . (2.5)

φ(pk,Ω)(δ) = (1 + o(1))log(1/p) · min

S⊂Ω

The number of k-APs in a set of given (suﬃciently small) size is always maximized by an interval, as stated precisely below. The theorem below was proved for 3-APs by Green and Sisask [18] and extended to all k-APs in Section 8.

Theorem 2.4. Fix a positive integer k ≥ 3. There exists some constant ck > 0 such that the following statement holds. Let A ⊂ Z be a subset with |A| = n, or A ⊂ Z/NZ with N prime and |A| = n ≤ ckN. Then Tk(A) ≤ Tk([n]). After some algebra one easily obtains

n2 k − 1 −

r2 k − 1

+ r, where r ∈ {1,2,...,k − 1} is chosen such that n ≡ r (mod k − 1). In particular we have n2 k − 1 ≤ Tk([n]) ≤

Tk([n]) =

n2 k − 1

1 4

(k − 1). (2.6) From this formula we can easily deduce Theorem 2.2 from Proposition 2.3.

+

Combining with the large deviation principle Theorem 2.1, we obtain the following corollary on the large deviation rate for upper tails of k-AP counts.

Corollary 2.5. Fix k ≥ 3. Let Ω = [N] or Z/NZ, and in the latter case assume that N is prime. Let p = pN → 0 and δ = δN > 0 be such that δ = O(1), δ−3pk−2(log(1/p))2 → 0, and

1

δpk ≥ N−

6(k−1) log N (2.7) (for k = 3, the right-hand side can be relaxed to N−1/6(log N)7/6; for k = 4, it can be relaxed to N−1/12(log N)13/12). Then, as N → ∞, the random variable Xk = Tk(Ωp) satisﬁes

1 + o(1) if Ω = [N], √k − 1 + o(1) if Ω = Z/NZ with prime N.

−log P(Xk ≥ (1 + δ)EXk) √

=

δpk/2N log(1/p)

Remark. When Ω = Z/NZ, it is standard to assume N → ∞ along the primes to avoid torsion issues. Without the primality assumption, the leading constant in the large deviations rate function could depend on the subsequence along which N goes to inﬁnity (a similar issue was discussed in [12]). For example, when N = N1N2, the maximum number of k-APs in Z/NZ in a set of size N1 is given by A = N2Z/NZ, which has Tk(A) = N12, more than Tk([N1]) = N12/(k − 1) + O(1). Thus, as a consequence of Proposition 2.3, we could have a diﬀerent constant in Corollary 2.5 for Ω = Z/NZ if N → ∞ along some sequence other than the primes.

- 2.4. Microscopic scale. In the microscopic scale, δ−3pk−2(log(1/p))2 → ∞. Here δ = δN is thought as tending to zero relatively quickly compared to p = pN. We will establish, in Section 6, the following asymptotic solution to the variational problem (2.2) in this regime.


- Theorem 2.6. Fix k ≥ 3. Let Ω = Z/NZ or [N]. Let p = pN ∈ (0,1) and δ = δN > 0 be such that p → 0 and δ−3pk−2(log(1/p))2 → ∞. Then, as N → ∞,


 

- 1

- 2k2


+ o(1) δ2Np if Ω = Z/NZ,

φ(pk,Ω)(δ) =

- 1

- 2γk




+ o(1) δ2Np if Ω = [N], where

(k − 1)2 − i2 − (k − 1 − j)2 (k − 1 − i)j

4 3

. (2.8)

γk =

k +

0≤i<j<k

Remark. The ﬁrst few values of γk are γ3 = 28/3, γ4 = 17, and γ5 = 718/27. We are not aware of a closed-form expression for γk. However, one always has γk ≥ k2, and asymptotically limk→∞ γk/k2 = (30 − 2π2)/9 ≈ 1.14.

Combining with the large deviation principle Theorem 2.1, we obtain the following corollary.

Corollary 2.7. Fix k ≥ 3. Let Ω = [N] or Z/NZ, and in the latter case assume that N is prime. Let p = pN → 0 and δ = δN > 0 be such that δ = O(1), δ−3pk−2(log(1/p))2 → ∞, and

1

min{δpk,δ2p} ≥ N−

6(k−1) log N (for k = 3, the right-hand side can be relaxed to N−1/6(log N)7/6; for k = 4, it can be relaxed to N−1/12(log N)13/12). Then, as N → ∞, the random variable Xk = Tk(Ωp) satisﬁes

1/(2k2) + o(1) if Ω = Z/NZ, 1/(2γk) + o(1) if Ω = [N],

−log P(Xk ≥ (1 + δ)EXk) δ2Np

=

where γk is deﬁned in (2.8).

The upper bound on φ(pk,Ω) in Theorem 2.6 for Ω = Z/NZ is obtained by taking the constant function on Ω with value p(1 + δ)1/k, which turns out to be tight asymptotically to the ﬁrst order. This behavior, where the solution to the variational problem is obtained by a constant function, at least asymptotically, suggests that the reason for many k-APs in the microscopic scale is a uniform boost in the density of the set, and such phenomena are referred to in the literature as replica symmetry [10]. (Admittedly we are somewhat abusing terminology here, as replica symmetry in previous works [10, 27, 32] on random graphs refer to setting of constant p and δ). In Section 7 we record some partial results on

replica symmetry for constant p and δ for k-APs. On the contrary, in the macroscopic scale, many k-APs are created by a smaller set arranged in a special structure, for example, an interval, and this is referred as replica symmetry breaking.

When Ω = [N], in the microscopic scale, the asymptotically optimal solution to the variational problem turns out not to be a constant function, but rather, a function that assigns each a ∈ [N] to a number proportional to the number of k-APs in [N] containing a. This is due to the asymmetry of the elements in [N], as the elements in the middle bulk are contained in more k-APs than those in the fringe. Even though the constant function does not asymptotically minimize the variational problem in this setting, the solution nevertheless exhibits some features of replica symmetry (by analogy to the Z/NZ setting). We ﬁnd this new phenomenon interesting, as we are not aware of analogous results in the random graph setting.

3. Gaussian width and non-linear large deviations

In this section we apply Eldan’s non-linear large deviation principle [15] to k-AP upper tails, reducing the large deviation rate problem to a variational problem. The proof relies on bounding the Gaussian width of a set of gradients, which will be done in Section 4.

- 3.1. Eldan’s LDP. We start with a short discussion of Eldan’s [15] result (adapted to our setting). For any K ⊂ RN deﬁne the Gaussian width of K by


GW(K) := E sup

x,Z

x∈K

where the expectation is taken over Z ∼ Normal(0,IN), a standard Gaussian random vector in RN.

For any function F : {0,1}N → R, deﬁne its discrete derivatives by

DiscDervi F(y) = F(y1,...,yi−1,1,yi+1,...,yN) − F(y1,...,yi−1,0,yi+1,...,yN) for any i ∈ [N] and y = (y1,y2,...,yN) ∈ {0,1}N, and its discrete gradient by

DiscGradF(y) = (DiscDerv1 F(y),...,DiscDervN F(y)).

A key quantity is the Gaussian width of the set of all discrete gradients of F, which we denote by

DiscGW(F) := GW DiscGradF(y) : y ∈ {0,1}N ∪ {0} . (3.1) Deﬁne the discrete Lipschitz constant of F by

DLip(f) = max

DiscDervi f(y).

i∈[N],y∈{0,1}N

Improving an earlier result of Chatterjee and Dembo [8], Eldan [15] proved a large deviation principle for general non-linear functions F : {0,1}N → R satisfying certain hypotheses on its set of discrete gradients. The large deviation rate is given in terms of the natural variational problem:

N

Ip(yi) : EF(Y ) ≥ tN , (3.2)

ϕFp (t) := inf

y∈[0,1]N

i=1

where the expectation is taken with respect to a random vector Y = (Y1,Y2,...,YN) with Yi ∼ Bernoulli(yi) independently for every i ∈ [N].

- Theorem 3.1 (Eldan [15]). Let X = (X1,X2,...,XN) ∈ {0,1}N be a random vector with i.i.d. Xi ∼ Bernoulli(p). Given a function F : {0,1}N → R, for every t,ε ∈ R with 0 < ε < ϕFp (t − ε)/N, we have


6L(log N)1/6 N1/3 with

log P(F(X) ≥ tN) ≤ −ϕFp (t − ε) 1 −

2/3

1/3

1 ε

1 ε

1 ε

DLip(F)2

√

DLip(F) + |log(p(1 − p))|

DiscGW(F) +

.

L =

2DLip(F) +

N

(3.3) Moreover, whenever the assumption Nε2

DLip(F)2 ≤ 12 holds, the following lower bound holds: log P(F(X) ≥ (t − ε)N) ≥ −ϕFp (t) 1 +

2

2 Nε2

DLip(F)2 − log 10.

Denote the usual gradient and partial derivatives of F : RN → R by

∇F := (∂1F,...,∂NF). Deﬁne

GW(F) := GW ∇F(y): y ∈ {0,1}N ∪ {0} (3.4) for the continuous analog of DiscGW(F) from (3.1). These two quantities diﬀer only negligibly in our applications.

- Lemma 3.2. For any twice-diﬀerentiable F : RN → R, we have


N

|DiscGW(F) − GW(F)|

|∂iiF(x)|,

sup

x∈[0,1]N

i=1

where ∂ijF = ∂2F/∂xi∂xj denotes the (i,j)-th partial derivative of F and DiscGW(F) is deﬁned by considering the restriction of F to {0,1}N.

Proof. Applying the intermediate value theorem (twice), we have |DiscDervi F(y) − ∂iF(y)| ≤ sup

|∂iiF(x)|

x∈[0,1]N

for any y ∈ {0,1}N. Thus for any Z = (Z1,...,ZN) ∈ RN and any y ∈ {0,1}N, | DiscGradF(y),Z −  ∇F(y),Z | ≤

|∂iiF(x)||Zi|.

sup

x∈[0,1]N

i

The result follows by ﬁrst taking the supremum over y, and then taking an expectation over Z ∼ Normal(0,IN) and using E|Zi| = O(1).

- 3.2. LDP for k-AP. Now, we apply Theorem 3.1 to derive a large deviation principle for k-AP counts, conditioned on bounds for the Gaussian width of the gradients of the k-AP counting function.


By viewing points in RΩ as functions Ω → R, the previously deﬁned k-AP functional Tk can be viewed as a function on RΩ by

Tk(y) =

a,b

yaya+bya+2b ...ya+(k−1)b, y ∈ RΩ.

In the case Ω = [N], the indices a and b both range over Z, and we set ya = 0 if a ∈/ [N]. In the case Ω = Z/NZ, the indices a and b both range over Z/NZ and the indices of y are taken mod N. Recall the deﬁnition (2.2) of the variational problem for upper tails of k-AP counts, reproduced here:

Ip(ya) : Tk(y) ≥ (1 + δ)pkTk(Ω) . (3.5)

φ(pk,Ω)(δ) := inf

y∈[0,1]Ω

a∈Ω

We will apply Theorem 3.1 to the function F = Tk/N. The relevant Gaussian width is

GW(Tk/N) = GW N 1 ∇Tk(y): y ∈ {0,1}Ω . Note that we do not need to include the origin in the deﬁnition since ∇Tk(0) = 0. We have the “trivial” bounds: √

N GW(Tk/N) N. (3.6) The lower bound comes from considering the constant vector y = (1,...,1), and the upper bound comes from noting that N1 ∇Tk(y) is coordinatewise O(1) for all y ∈ {0,1}Ω.

The main result of this section is the following proposition, showing that any power-saving improvement to the trivial upper bound to GW(Tk/N) leads to a large deviation principle allowing the probability p to decay as N−c. Combining it with bounds on the Gaussian width (to be proved in the next section) gives Theorem 2.1.

- Proposition 3.3. Fix k ≥ 3. Suppose we have real constants σ,τ such that GW(Tk/N) = O(N1−σ(log N)τ). (3.7)


Let p = pN be bounded away from 1, and δ = δN > 0 be such that δ = O(1) and

N−σ/3(log N)τ/3+1 min{δpk,φ(pk,Ω)(δ/2)/N}. (3.8) Then

−log P(Tk(Ωp) ≥ (1 + δ)ETk(Ωp)) = (1 + o(1))φ(pk,Ω)(δ + o(δ)).

As long as one can prove an estimate (3.7) on Gaussian width with σ > 0, we can allow p to decay as N−c for some constant c > 0. In Theorem 4.1, we show that one can take σ = 1/(2(k − 1)) and τ = 0 (with better bounds for k = 3,4). From the asymptotic solutions to the variational problems (Theorem 2.2 and 2.6), and noting that φ(Ωp ,k)(δ) is monotonic in δ, we have, as long as δpkN2 → ∞,

√

φp(Ω,k)(δ/2)/N min{

δpk/2 log(1/p),δ2p}.

Combining these asymptotics, we see that hypothesis (3.8) translates into hypothesis (2.3) in Theorem 2.1, and hence Proposition 3.3 implies Theorem 2.1.

In the rest of this section, we prove Proposition 3.3. We ﬁrst prove some easy estimates on the various quantities that appear in Theorem 3.1. Recall the deﬁnitions of DiscGW(F) and GW(F) from (3.1) and (3.4).

- Lemma 3.4. For any k ≥ 3, we have DLip(Tk/N) = O(1)


and

DiscGW(Tk/N) = GW(Tk/N) + O(1).

Proof. The ﬁrst claim follows from noting that in Tk(y) = a,b yaya+b ···ya+(k−1)b, every variable ya appears in O(N) terms.

The second claim follows from Lemma 3.2, as ∂aaTk(y) is uniformly bounded for all y ∈ [0,1]Ω and all a ∈ Ω.

- Proof of Proposition 3.3. We apply Theorem 3.1 for F = Tk/N. Set ε = N−1/3(log N)11/12 GW(Tk/N)1/3 N−σ/3(log N)τ/3+11/12.


By (3.8),

ε = o(δpk) and ε = o(φ(pk,Ω)(δ/2)/N). (3.9) Note that σ ≤ 1/2 due to the lower bound GW(Tk/N)

√

N in (3.6). So in particular, Nε2 → ∞. Also, log(1/p) = O(log N) by (3.8).

Recall L from (3.3). Using Lemma 3.4 and earlier estimates, we have

L ε−1(log N)2/3 GW(Tk/N)1/3. Thus, as N → ∞,

LN−1/3(log N)1/6 ε−1N−1/3(log N)5/6 GW(Tk/N)1/3 = (log N)−1/12 → 0.

Let Y = (Y1,...,YN) be a random vector with Yi ∼ Bernoulli(yi) independently for all i ∈ [N]. Then

ETk(Y ) = Tk(y) + O(N) = Tk(y) + o(δpkN2).

The discrepancy O(N) comes from terms in Tk(y) where some yi may appear more than once. Setting

t = (1 + δ)pkTk(Ω)/N2, we see that

ETk(Y )/N ≥ (t + o(δpk))N is equivalent to Tk(y) ≥ (1 + δ + o(δ))pkTk(Ω).

Comparing the deﬁnition of ϕFp (t) from (3.2) for F = Tk/N and φ(pk,Ω)(δ) from (3.5) (and noting that ϕFp (t) is non-decreasing in t and φ(pk,Ω)(δ) is non-decreasing in δ), we obtain

p (t ± ε) = φ(pk,Ω)(δ + o(δ)). The hypothesis 0 < ε < N1 ϕT

ϕT

k/N

k/N

p (t − ε) in Theorem 3.1 is also satisﬁed due to (3.9). Applying Theorem 3.1, we obtain the upper bound to the log-probability

log P(Tk(Ωp) ≥ (1 + δ)pkTk(Ω)) ≤ −(1 − o(1))ϕT

p (t − ε) ∼ −φ(pk,Ω)(δ − o(δ)), as well as the lower bound (changing t to t + ε when applying Theorem 3.1),

k/N

log P(Tk(Ωp) ≥ (1 + δ)pkTk(Ω)) ≥ −(1 − o(1))ϕT

p (t + ε) − O(1) ∼ −φ(pk,Ω)(δ + o(δ)).

k/N

Combining the upper and lower bounds, and recalling that ETk(Ωp) ∼ pkTk(Ω), the result follows.

4. Bounds on Gaussian width

In this section, we establish bounds on the Gaussian width of the set of gradients of Tk. These bounds can be used in Proposition 3.3 from the previous section to deduce Theorem 2.1 on the LDP for APs.

Our main result of this section is stated below. Recall from Section 3.1 that GW(Tk/N) = GW({∇Tk(y)/N : y ∈ {0,1}Ω})

N ∇Tk(y),Z . (4.1)

= EZ∼Normal(0,I

1

N) sup

y∈{0,1}Ω

- Theorem 4.1. For any ﬁxed k ≥ 3,


- 1

- 2(k−1)). (4.2)


GW(Tk/N) = O(N1− Furthermore, for k = 3, the bound can be tightened to

- GW(T3/N) = Θ( N log N).

For k = 4, the bound can be improved to

- GW(T4/N) = O(N3/4(log N)1/4).


Remark. After a preprint of our paper had appeared, Briët and Gopi [5] improved the bound to GW(Tk/N) = O(N1−

1

2 (k−1)/2 (log N)1/2) for all k ≥ 5. We have an easy lower bound GW(Tk/N)

√

N deduced by taking the constant vector y = (1,...,1) in (4.1). We conjecture that it is essentially tight. Conjecture 4.2. For any ﬁxed k ≥ 4,

√

N(log N)O(1).

GW(Tk/N) =

For the proof of Theorem 4.1, we go back to viewing Tk as an operator on functions Ω → R (as opposed to a function on points in RΩ). We deﬁne a multilinear version of Tk by setting, for f0,...,fk−1: Ω → R,

f0(a)f1(a + b)···fk−1(a + (k − 1)b),

Tk(f0,...,fk−1) :=

a,b

so that for f : Ω → R,

Tk(f) = Tk(f,f,...,f

).

k times

We identify points in CΩ with functions Ω → C and maintain the notation , for inner products, so that for f,h: Ω → C,

f,h :=

f(a)h(a).

a∈Ω

The gradient ∇Tk of Tk maps a function f : Ω → R to the function ∇Tk(f): Ω → R deﬁned by

k−1

∇Tk(f)(a) =

f(a + (j − i)b), a ∈ Ω.

i=0 0≤j≤k−1 j =i

b

Since Tk is multi-linear, for any f,h: Ω → R,

k−1

). (4.3)

 ∇Tk(f),h =

Tk(f,f,...,f

### ,h,f,f,...,f

j=0

j times

k−1−j times

- 4.1. 3-APs and Fourier analysis. Here, we prove the claim in Proposition 4.7 for k = 3 using Fourier analysis. It will be easier to work in the setting Ω = Z/NZ. The corresponding bounds for Ω = [N] ⊂ Z can be easily derived by embedding [N] in Z/N Z for some larger N ∈ [2N,3N] so that 3-APs in [N] ⊂ Z/N Z do not wrap-around zero in the cyclic group.


Given f : Z/NZ → C, deﬁne its discrete Fourier transform by f(r) =

1 N

f(a)ω−ar, r ∈ Z/NZ,

a∈Z/NZ

where ω = e2πi/N. The inverse transform is given by f(a) =

f(r)ωar.

r∈Z/NZ

The following standard identity relates T3 with the Fourier transform.

- Lemma 4.3. For f,g,h: Z/NZ → R, 1


f(r) g(−2r) h(r).

T3(f,g,h) =

N2

r∈Z/NZ

Proof. Expanding the left-hand side using the inverse transform, we have T3(f,g,h) =

f(a)g(a + b)h(a + 2b)

a,b∈Z/NZ

f(r) g(s) h(t)ωar+(a+b)s+(a+2b)t

=

a,b∈Z/NZ r,s,t∈Z/NZ

### = N2

f(r) g(−2r) h(r),

r∈Z/NZ

where the ﬁnal step follows from noting that

ωar+(a+b)s+(a+2b)t =

a,b∈Z/NZ

N2 if r + s + t = 0 and s + 2t = 0, 0 otherwise.

The above identity leads to the following bound, showing that T3 is controled by the Fourier transform of its inputs.

- Lemma 4.4. Let f0,f1,f2: Z/NZ → [−1,1]. For each i = 0,1,2, 1


| fi(r)|. Remark. If N is odd, then the can be replaced by ≤.

N2|T3(f0,f1,f2)| fi ∞ =: max

r

Proof. Using Lemma 4.3 and the Cauchy–Schwarz inequality, we have 1 N2|T3(f0,f1,f2)| ≤ f0 ∞

| f1(−2r)|| f2(r)|

r∈Z/NZ

| f2(r)|2 1/2

| f1(−2r)|2 1/2

≤ f0 ∞

r

r

| f2(r)|2 1/2

| f1(r)|2 1/2

f0 ∞

r

r

≤ f0 ∞.

The ﬁnal step follows from Parseval’s identity: r | fj(r)|2 = N1 a |fj(a)|2 ≤ 1. The proofs for i = 1,2 are analogous.

Proof of Theorem 4.1 for k = 3. For any g: Z/NZ → R, we have

 ∇T3(f),g = T3(g,f,f) + T3(f,g,f) + T3(f,f,g), so by Lemma 4.4,

1 N | ∇T3(f),g | N max

| g(r)|.

r

Now let g be a random function taking i.i.d. standard normal values. Then each g(r) is a normally distributed complex number with E[| g(r)|2] = 1/N, since the Fourier transform is a unitary operator. Standard results about the supremum of Gaussian processes, e.g.,

- Lemma 4.5 below, then gives Esupr | g(r)| (log N)/N. Thus


1 N  ∇T3(f),g NEsup

GW(T3/N) = E sup

| g(r)| N log N.

f : Z/NZ→{0,1}

r

The matching lower bound is proved in Appendix A.

See Appendix A for proof of the bound GW(T4/N) = O(N3/4(log N)1/4) in Theorem 4.1, which extends the above Fourier analytic technique.

## 4.2. k-APs and the Chinese remainder theorem. Our strategy for proving Theorem 4.1

is to show that the set of gradients ∇Tk(f)/N over all f : Ω → {0,1} is contained in the convex hull of a small set of bounded functions. We start with a standard bound on Gaussian width of sets. The proof is included for completeness.

- Lemma 4.5 (Small sets have small Gaussian widths). If S ⊂ [−1,1]N, then GW(S) = O( N log |S|).


Proof. We may assume that |S| ≥ 2. We have the following standard tail bound for Z ∼ Normal(0,σ2): P(Z > t) ≤ e−t2/(2σ2). With Z ∼ Normal(0,IN) a standard Gaussian vector in RN, one has y,Z ∼ Normal(0,|y|2) for every y ∈ RN. Thus P( y,Z > t) ≤ e−t2/(2|y|2) ≤ e−t2/(2N) for every y ∈ [−1,1]N. So for any t > 0, we have by the union bound

2/(2N).

y,Z > t) ≤ |S|e−t

P(sup

y∈S

Set u = 10 N log |S|. Then GW(S) = EZ sup

y,Z ≤ u + ˆ ∞

P(sup

y,Z > t)dt

y∈S

y∈S

u

≤ u + ˆ ∞

2/(2N) dt = O( N log |S|).

|S|e−t

u

Corollary 4.6. If {∇Tk(f)/N : f : Ω → {0,1}} is contained in the convex hull of a set S of uniformly bounded functions3 on Ω, then GW(Tk/N) = O( N log |S|).

We will prove the following bounds on the size of S, which imply the bound GW(Tk/N) = O(N1−

- 1

- 2(k−1)) in Theorem 4.1.


Proposition 4.7. Fix k ≥ 3. The set {∇Tk(f)/N : f : Ω → {0,1}} is contained in the convex hull of a set S of uniformly bounded functions on Ω, where |S| = exp(O(N1−1/(k−1))).

We can conjecture that the bound on |S| can be improved to eNo(1), or perhaps even the following stronger bound, which would imply Conjecture 4.2. Conjecture 4.8. In Proposition 4.7, for every ﬁxed k ≥ 4, one can have |S| = e(logN)O(1). Remark. For k = 3, one can have |S| = O(N) by considering the Fourier basis and using

- Lemma 4.4. For the ﬁrst open case k = 4, intuition from the theory of higher-order Fourier analysis (e.g., [29]) suggests that perhaps it suﬃces to take the set of “quadratic characters”, i.e., functions of the form a  → e2πiq(a) where q(a) behaves quadratically (very loosely speaking). More generally, perhaps we can take a set of nilsequences [19]. However, this method is currently incapable of proving the conjecture due to poor quantitative dependencies in the theory of higher order Fourier analysis. See [16, Section 4.1] for the analogous problem in the language of ergodic averages.


For the proof of Proposition 4.7, it will be easier to work in the setting Ω = [N] ⊂ Z. The proof can be easily adapted to work for Ω = Z/NZ by chopping Z/NZ into a bounded number of intervals and analyzing their contributions separately.

The argument we present here is essentially the same as that appearing in [17, Section 4], which in turn is motivated by the random sampling idea in [11]. Roughly speaking, we can obtain a good estimate of ∇Tk(f) by knowing f only on A ⊂ [N], where A is a random subset of slightly more than N1−1/(k−1) elements. Thus any gradient ∇Tk(f) can be well approximated by one of 2|A| many possible functions.4 Actually one can achieve a similar eﬀect (more simply and with better bounds) deterministically by partitioning [N] modulo k − 1 distinct primes of sizes roughly N1/(k−1) each, which is how we shall proceed. In this approach, the Chinese remainder theorem play a role similar to independence for random variables.

- Proof of Proposition 4.7. We may assume that N is large. To analyze ∇Tk(f), we make the following deﬁnition. For c1,...,ck−1 ∈ Z, let Φ(c1,...,ck−1) be the set of all functions


- 3Here, and in the sequel, uniformly bounded functions refer to those functions f with |f(a)| = O(1) point-wise.
- 4This random sampling argument can also be used in conjunction with Chatterjee and Dembo’s results [8] to obtain a large deviation principle for k-APs, allowing the probability p to decay as N−c


k for some constant ck > 0, though with a smaller ck than what is shown here.

F : [N] → R of the form F(a) =

1 N b∈Z

f(a + c1b)f(a + c2b)...f(a + ck−1b), a ∈ [N] (4.4)

for some f : [N] → {0,1} (set f(a) = 0 if a ∈/ [N]). It suﬃces to show that Φ(c1,...,ck−1) is contained in the convex hull of exp(O(N1−1/(k−1))) many bounded functions, whenever {c1,...,ck−1} is any of

{1,2,...,k − 1},{−1,1,...,k − 2},...,{−(k − 1),...,−2,−1}. For clarity, we assume that (c1,...,ck) = (1,...,k − 1), as the other cases are similar. Pick k −1 distinct primes q1,...,qk−1 ∈ [(N/2)

1

1

k−1] (such a choice always exist when N is large due to bounds on large gaps between primes [1]). We have q1q2 ···qk−1 ∈ [N/2,N]. Write

k−1,N

i+qiZ (4.5) where

f =

fr

ri∈Z/qiZ

f(a) if a ≡ ri (mod qi), 0 if a  ≡ ri (mod qi),

fr

i+qiZ(a) =

is the restriction of f to the residue class ri (mod qi). By using (4.5) to partition the i-th factor f(a + ib) in each term in (4.4), we obtain

k−1

1 q1 ···qk r

1 N b∈Z

fr

i+qiZ(a + ib) =

F(a) =

vr

1,...,rk−1;f(a)

i=1 ri∈Z/qiZ

1,...,rk−1

where the sum is taken over r1 ∈ Z/q1Z,...,rk−1 ∈ Z/qk−1Z, and

k−1

q1q2 ···qk−1 N b∈Z

i+qiZ(a + ib). (4.6) We see that F lies in the convex hull of

vr

1,...,rk−1;f(a) :=

fr

i=1

1,...,rk−1;f : f is {0,1}-valued,r1 ∈ Z/q1Z,...,rk−1 ∈ Z/qk−1Z}. For ﬁxed i and ri, the number of possibilities for fr

V = {vr

i+1 as f ranges over {0,1}-valued functions. It follows that

i+qiZ is at most 2N/q

k−1

1−1/(k−1)),

2N/q

i+1 = 2O(N

|V | ≤ q1q2 ···qk−1

i=1

by our choice of qi. It remains to show that all functions in V are bounded. Indeed, for any ﬁxed a ∈ [N], the simultaneous congruence conditions a+ib ≡ ri (mod qi), for 1 ≤ i ≤ k −1, in the unknown b ∈ [−N,N] have O(N/(q1q2 ···qk−1)+1) solutions by the Chinese Remainder Theorem. Thus the number of nonzero summands in (4.6) is O(N/(q1q2 ···qk−1) + 1), and it follows that

q1q2 ···qk−1 N

|vr

1,...,rk−1;f(a)| 1 +

1, as desired. This completes the proof.

This completes the proof of Theorem 4.1, which bounds GW(Tk/N), other than the matching lower bound GW(T3/N) √N log N and the improvement GW(T4/N) N3/4(log N)1/4, whose proofs can be found in Appendix A.

5. Variational problem at the macroscopic scale

The goal of this section is to prove Proposition 2.3, which reduces the entropic variational problem in the macroscopic scale, i.e., δ−3pk−2(log(1/p))2 → 0, to a corresponding extremal problem in additive combinatorics:

|S| : Tk(S) ≥ δpkTk(Ω) (5.1)

φ(pk,Ω)(δ) = (1 + o(1))log(1/p) · min

S⊂Ω

(provided that δ = O(1) and δpkN2 → ∞). Let us provide an overview of the proof strategy. The upper bound on φ(pk,Ω)(δ) follows by considering a function which takes value 1 on an interval and p elsewhere (Section 5.1). For the lower bound, suppose Tk(f) ≥ (1 + δ)pkTk(Ω). Write f(a) = p + g(a). Let g denote a function obtained from g by changing each g(a) to 0 if g(a) is already suﬃciently close to zero (the exact threshold will be speciﬁed in the proof). It will be shown that Tk(f) ≈ pkTk(Ω) + Tk(g ), so that Tk(g ) ≥ (1 − o(1))δpkTk(Ω). For now, it is ﬁne to pretend that g is an indicator function of a set, so that we have a lower bound on the number of k-APs of the set. We will prove an extremal result on maximizing the number of k-APs of a set of given size. This will imply a lower bound on a∈Ω g (a), thereby giving the desired lower bound on a Ip(f(a)) ≈ a g (a)log(1/p).

- 5.1. Proof of upper bound in Proposition 2.3. We begin by noting that the right-hand side expression of (5.1) does not change if δ is replaced by some δ = δ + o(δ). This is equivalent to the fact that the maximum number of k-APs in a subset of Ω of size n does not change signiﬁcantly if n is changed to n + o(n). This is clear from the exact formula in Theorem 2.4 and (2.6) whenever the hypothesis of the theorem applies, or otherwise in general from the easy lemma below (applied with n → ∞, n ≤ N, and s = o(n), so that Mn n2 and Mn+o(n) ∼ Mn).


- Lemma 5.1. Let k ≥ 3 and Ω = Z/NZ or [N]. Let Mn = maxA⊂Ω:|A|≤n Tk(A). Then Mn ≤ Mn+s ≤ Mn + ks(n + s)


for all n,s ≥ 0.

Proof. It is easy to see that Tk(A ∪ {a}) ≤ Tk(A) + k|A| + 1 by counting the number of new k-APs that are formed with the addition of a new element a to A. Thus Mn+1 ≤ Mn +kn+1. The lemma follows by iterating this bound.

It is not too hard to prove that φ(pk,Ω)(δ) is at most the right-hand side quantity in (5.1).

Take any S ⊂ Ω with Tk(S) ≥ (1 − pk)−1δpkTk(Ω) (here we are implicitly changing the δ in the right-hand side of (5.1) to δ = (1 − pk)−1δ = δ + o(δ)), and let f in the variational problem (2.2) be the function

So that

f(a) =

1 if a ∈ S, p if a ∈/ S.

Tk(f) ≥ (1 − pk)Tk(S) + pkTk(Ω) ≥ (1 + δ)pkTk(Ω),

(5.2)

### and

Ip(f(a)) = |S|log(1/p). This proves the upper bound in Proposition 2.3.

a∈Ω

- 5.2. Proof of lower bound in Proposition 2.3. To begin with note that taking S ⊂ Ω to be an interval of size kδ Tk(Ω)pk/2 , where δ = (1 − pk)−1δ = δ + o(δ), ensures Tk(S) ≥ (1 − pk)−1δpkTk(Ω). Then taking f as in (5.2) gives Tk(f) ≥ (1 + δ)pkTk(Ω)


√

kδNpk/2 log(1/p), for N large enough. Therefore, to show that the left-hand side of (2.5) is greater than its right-hand side, it suﬃces to restrict our attention to functions f : Ω → [p,1] that satisfy

and a∈Ω Ip(f(a)) = kδ Tk(Ω)pk/2 log(1/p) ≤ 2

√

kδNpk/2 log(1/p) and Tk(f) ≥ (1 + δ)pkTk(Ω) (5.3)

Ip(f(a)) ≤ 2

a∈Ω

(note that we can restrict the range of f to [p,1] since Ip(·) is decreasing in [0,p]). We will show that for such f,

|S| : Tk(S) ≥ δpkTk(Ω) .

Ip(f(a)) ≥ (1 + o(1))log(1/p) · min

S⊂Ω

a∈Ω

We recall a useful asymptotic estimate of Ip(·) from [28, Lemma 3.3].

- Lemma 5.2. Let p → 0, and x = x(p) ∈ [0,1 − p]. If x = o(p), then Ip(p + x) ∼ x2/(2p). If x/p → ∞, then Ip(p + x) ∼ xlog(x/p).


Let f(a) = p + g(a), where g : Ω → [0,1 − p]. (When Ω = [N], we set both f and g to be zero outside [N].) Note the following bounds on g: by convexity of Ip(·), (5.3), and

- Lemma 5.2,


1 N a∈Ω

1 N a∈Ω

1 N a∈Ω

f(a) ≤

Ip p +

g(a) = Ip

Ip(f(a))

√

kδpk/2 log(1/p) ∼ Ip p + 2(kδ)1/4p(k+2)/4 log(1/p) ,

≤

since δ1/4p(k+2)/4 log(1/p) = o(p) whenever δ = O(1). Moreover, since Ip(p+x) is increasing for x ∈ [0,p − 1],

N

1 N

g(a) δ1/4p(k+2)/4 log(1/p). (5.4)

a∈Ω

The proof of the lower bound on a∈Ω Ip(f(a)) proceeds via two-step thresholding on the function g. At each step, we choose some threshold τ and decompose g into its small and large components:

g = g≤τ + g>τ. Here g≤τ(a) := g(a)1{g(a) ≤ τ}, and g>τ := g(a)1{g(a) > τ}.

- (1) (Thresholding) First, we perform the decomposition with τ = p3/4 and show that the contribution to Tk(f) from the small component g≤τ is negligible.
- (2) (Bootstrapping) Next, we bootstrap the argument in the ﬁrst step and take a higher threshold τ = po(1).


The following lemma will be useful later.

### Lemma 5.3. Let Ω = Z/NZ or [N]. Let x,y ∈ {0,1,...,k − 1} with x = y. For any f : Ω → [0,1], one has

2

f(a + xb)f(a + yb) ≤ (k − 1)

f(a)

,

a∈Ω

a,b

where the sum on the left-hand side is taken over all pairs of elements (a,b) in the ambient group such that {a + xb,a + yb} ⊂ Ω.

Proof. The lemma follows from observing that after expanding the right-hand side, for any c,d ∈ Ω, there are at most k − 1 pairs of elements a,b in the ambient group such that a + xb = c and a + yb = d. Indeed, subtracting the two equations gives (x − y)b = c − d. Since 0 < |x − y| ≤ k − 1, the number of solutions for b is at most 1 when Ω = [N] and at most (k − 1) when Ω = Z/NZ.

- 5.2.1. The thresholding step. In this section we formalize step (1) above. Recall that f is as in (5.3), and f = p + g, where g : Ω → [0,1] satisﬁes 0 ≤ g ≤ 1 − p. From (5.3) we know that


Tk(p + g≤τ + g>τ) = Tk(f) ≥ (1 + δ)pkTk(Ω). The expression Tk(p + g≤τ + g>τ), when written out as a sum, expands into a number of components. The following lemma shows that, with an appropriate choice of τ, the only non-negligible contributions are Tk(p) = pkTk(Ω) and Tk(g>τ).

- Lemma 5.4. Assume that δ−3pk−2 log2(1/p) → 0, and f = p + g: Ω → [p,1] satisﬁes (5.3). Let τ = p3/4. Then


Tk(g>τ) ≥ (1 − o(1))δpkTk(Ω) (5.5) and

√

δNpk/2. (5.6)

g>τ(a)

a∈Ω

Remark. In the above lemma, one may take τ = ps for any ﬁxed 2/3 < s < 1. Proof. From Lemma 5.2 we have Ip(p + g>τ(x)) g>τ(x)log(1/p). Thus

√

δNpk/2 log(1/p),

Ip(p + g>τ(a)) ≤

g>τ(a)log(1/p)

Ip(f(a))

a∈Ω

a∈Ω

a∈Ω

where the ﬁnal step uses (5.3). This gives us (5.6). By expanding, we have

TX,Y,Z(p,g≤τ,g>τ), (5.7)

Tk(p + g≤τ + g>τ) =

X,Y,Z

where the sum is over all ordered partitions (X,Y,Z) of the set {0,1,...,k − 1}, and TX,Y,Z(p,g≤τ,g>τ) :=

g>τ(a + zb). (5.8)

p|X|

g≤τ(a + yb)

y∈Y

z∈Z

a,b

Here the sum is taken over all pairs of elements (a,b) in the ambient group such that {a,a + b,...,a + (k − 1)b} ⊂ Ω. We say that TX,Y,Z(p,g≤τ,g>τ) contributes negligibly to the sum (2.1) (or negligible for short) if TX,Y,Z(p,g≤τ,g>τ) = o(δN2pk). We will show that all terms except for (X,Y,Z) = ({0,...,k − 1},∅,∅) and (∅,∅,{0,...,k − 1}) are negligible, i.e., the only non-negligible terms are pkTk(Ω) and Tk(g>τ). This would prove (5.5), due to the assumption Tk(f) ≥ (1 + δ)pkTk(Ω) from (5.3).

First, if |Z| ≥ 2, then by Lemma 5.3 and (5.6),

2

TX,Y,Z(p,g≤τ,g>τ) ≤ (k − 1)τ|X∪Y|

τ|X∪Y|δN2pk.

g>τ(a)

a∈Ω

Therefore, if |Z| ≥ 2, then the contribution from TX,Y,Z(p,g≤τ,g>τ) is negligible unless |X ∪ Y | = 0, i.e., (X,Y,Z) = (∅,∅,{0,...,k − 1}).

Next, if |X| = k − 1 and |Y ∪ Z| = 1, then by (5.4), TX,Y,Z(p,g≤τ,g>τ) ≤ kNpk−1

g(a) δ1/4N2p(5k−2)/4 log(1/p) = o(δN2pk),

a∈Ω

where in the ﬁnal step we use the macroscopic scale assumption δ−3pk−2(log(1/p))2 → 0. Therefore these terms are negligible.

Finally, if |Z| ≤ 1 and |Y ∪ Z| ≥ 2, then by (5.4) and Lemma 5.3,

2

TX,Y,Z(p,g≤τ,g>τ) ≤ (k − 1)τk−2

τk−2N2δ1/2p(k+2)/2 log(1/p) = o(δN2pk),

g(a)

a∈Ω

where the last step holds due to τ = o(p2/3(log(1/p))−2/(3k−6)) and the macroscopic scale assumption on δ.

It follows from the above analysis that the only non-negligible contributions to the sum (5.7) are (X,Y,Z) = ({0,...,k − 1},∅,∅) and (∅,∅,{0,...,k − 1}), so that

Tk(f) = pkTk(Ω) + Tk(g>τ) + o(δpkN2). By the assumption Tk(f) ≥ (1+δ)pkTk(Ω) from (5.3), we obtain Tk(g>τ) ≥ (1−o(1))δpkTk(Ω)

- as desired.


- 5.2.2. The bootstrapping step. Now, we strengthen Lemma 6.3 by replacing τ with any τ = o(1).


- Lemma 5.5. Assume that δ−3pk−2 log2(1/p) → 0, and f = p + g: Ω → [p,1] satisﬁes (5.3). For any τ = o(1), we have


Tk(g>τ) ≥ (1 − o(1))δpkTk(Ω). Proof. Observe that

2

τδpkN2 = o(δpkN2). (5.9)

Tk(g>p3/4) − Tk(g>τ) ≤ k2τ

g>p3/4(a)

a∈Ω

To prove the ﬁrst inequality, note that the left-hand side can be bounded above by a sum of k terms, where the j-th term (for 1 ≤ j ≤ k) is itself the following sum

g1(a)g2(a + b)···gk(a + (k − 1)b)

a,b∈Ω

where gj = g≤τ and all other gi’s are set to g>p3/4, and this sum can be bounded by τ(k − 1)( a∈Ω g>p3/4)2 using Lemma 5.3. The second part of (5.9) follows from (5.6). By (5.5) we have Tk(g>p3/4) ≥ (1 − o(1))δpkTk(Ω), and thus by (5.9) we have Tk(g>τ) ≥ (1 − o(1))δpkTk(Ω) as well.

- 5.2.3. Completing the proof of Proposition 2.3. Assume that f : Ω → [p,1] satisﬁes (5.3). Let


- f = p + g, and choose some threshold τ satisfying τ = po(1) → 0 (e.g., τ = 1/log(1/p) for concreteness). By Lemma 5.5, one has


Tk(g>τ) ≥ (1 − o(1))δpkTk(Ω). This implies, by Lemma 5.6 below (used in the contrapositive in conjunction with Lemma 5.1),

|S| : Tk(S) ≥ δpkTk(Ω) .

g>τ(a) ≥ (1 + o(1))min

S⊂Ω

a∈Ω

By Lemma 5.2, Ip(p + g>τ(a)) ∼ g>τ(x)log(1/p) since τ = po(1). Therefore,

Ip(f(a)) ≥

Ip(p + g>τ(a)) = (1 + o(1))log(1/p)

g>τ(a)

a∈Ω

a∈Ω

a∈Ω

|S| : Tk(S) ≥ δpkTk(Ω) ,

≥ (1 + o(1))log(1/p)min

S⊂Ω

thereby completing the proof of Proposition 2.3, modulo the following lemma, which says that the problem of maximizing the number of k-APs in a set remains roughly unchanged even if we allow the elements to be weighted.

- Lemma 5.6. Let f : Ω → [0,1] be such that a∈Ω f(a) = m. Then


Tk(A) (5.10) provided that m → ∞ as N → ∞.

Tk(f) ≤ (1 + o(1)) max

A⊂Ω:|A|≤m

Proof. Let Ms = maxA⊂Ω:|A|≤s Tk(A). Let Ωf be a random subset of Ω chosen by including element a ∈ Ω with probability f(a) independently for all a ∈ Ω. Note that E[|Ωf|] = m, and for a,b ∈ Ω,

f(a)f(a + b)···f(a + (k − 1)b) ≤ P(a,a + b,...a + (k − 1)b ∈ A). (it is always an equality when the elements of the k-AP are distinct). This implies Tk(f) ≤ ETk(Ωf) ≤

P(|Ωf| = s)Ms.

s≥1

For s ≤ m + m2/3, we bound Ms ≤ Mm+m2/3 = (1 + o(1))Mm. And for s > m + m2/3 we use the trivial bound Ms ≤ s2. Thus

Tk(f) ≤ (1 + o(1))Mm + 4m2P(m + m2/3 < |A| ≤ 2m) +

P(|A| = s)s2

s>2m

≤ (1 + o(1))Mm + 4m2P(|A| > m + m2/3) +

s>2m

1/3/3 +

≤ (1 + o(1))Mm + 4m2e−m

s2e−s/6

s>2m

= (1 + o(1))Mm,

P(|A| ≥ s)s2

where the penultimate step uses Chernoﬀ bound in the following form: if X is a sum of independent indicator random variables, and EX = µ, then for any δ > 0, P(X ≥ (1+δ)µ) ≤ e−min{δ2,δ}µ/3.

This completes the proof of Proposition 2.3. Combining it with Theorem 2.4, which will be proved in Section 8, yields Theorem 2.2, the asymptotic solution to the variational problem in the macroscopic scale.

6. Variational problem at the microscopic scale

In this section, we prove Theorem 2.6, which solves the variational problem in the microscopic scale, i.e., δ−3pk−2 log2(1/p) → ∞. The following theorem uniﬁes the settings Ω = [N] and Z/NZ.

Theorem 6.1. Fix k ≥ 3. Let Ω = [N] or Z/NZ . Then for p = pN → 0 and δ = δN > 0 such that δ−3pk−2(log(1/p))2 → ∞, we have

δ2Tk(Ω)2p 2 a∈Ω νa2

, (6.1)

φ(pk,Ω)(δ) = (1 + o(1))

where νa is the number of k-APs in Ω containing a ∈ Ω (the constant k-AP a,a,...,a is counted k times), i.e., νa is the number of triples (x,y,j) where x,y are elements in the ambient group, j ∈ {0,1,...,k − 1}, so that a = x + jy and {x,x + y,...,x + (k − 1)y} ⊂ Ω.

In Section 6.1, we prove Theorem 6.1, following similar thresholding strategy to the macroscopic setting. In Section 6.2, we then compute the rate formulae in Theorem 2.6.

- 6.1. Proof of Theorem 6.1. We begin by showing that φ(pk,Ω)(δ) is at most the right-hand side of (6.1). The claim follows from an explicit construction of a function f in the variational problem (2.2), as given by the following lemma.


- Lemma 6.2. Let Ω = [N] or Z/NZ, and let νa be deﬁned as in Theorem 6.1. Deﬁne


- g: Ω → [0,1] by


δTk(Ω)νa a∈Ω νa2

p. Then f = p + g satisﬁes

g(a) =

δ2Tk(Ω)2p 2 a∈Ω νa2

and Tk(f) ≥ (1 + δ)pkTk(Ω). (6.2)

Ip(f(a)) ∼

2Tk(Ω)2p

As a consequence, φ(pk,Ω)(δ) ≤ (1 + o(1))δ

2 a∈Ωνa2. Proof. We have νa N, a∈Ω νa2 N3, so g(a) δp = o(p), and thus by Lemma 5.2,

δ2Tk(Ω)2p 2 a∈Ω νa2

g(a)2 2p ∼

Ip(f(a)) ∼

.

a∈Ω

a∈Ω

Next, by expanding we have

Tk(f) = Tk(p + g) ≥ pkTk(Ω) + pk−1

x,y

k−1

g(x + jy)

j=0

= pkTk(Ω) + pk−1

g(a)νa = (1 + δ)pkTk(Ω),

a∈Ω

where (x,y) ranges over all pairs of elements in the ambient group such that {x,x+y,...,x+ (k − 1)y} ⊂ Ω. This proves (6.2) and the upper bound on φ(pk,Ω)(δ) in Theorem 6.1.

Now we prove the lower bound on φ(pk,Ω)(δ). To begin with, using a∈Ω νa = kTk(Ω) and the Cauchy–Schwarz inequality, we have

δ2Tk(Ω)2p 2 a∈Ω νa2 ≤ (1 + o(1))

δ2pN 2k2

. (6.3)

φ(pk,Ω)(δ) ≤ (1 + o(1))

Therefore, to prove the lower bound on φ(pk,Ω)(δ) in (6.1), we can restrict our attention to functions f = p + g: Ω → [p,1] satisfying

Ip(f(a)) ≤ δ2Np and Tk(f) ≥ (1 + δ)pkTk(Ω). (6.4)

a∈Ω

Then by convexity, (6.4), and Lemma 5.2,

√

1 N a∈Ω

1 N a∈Ω

Ip(p + g(a)) ≤ δ2p ∼ Ip(p +

g(a) ≤

Ip p +

2δp).

Since Ip(p + x) is increasing for x ∈ [0,1 − p], we have

g(a) δpN. (6.5)

a∈Ω

The following lemma gives a lower bound on the weighted average of any function g satisfying f = p + g: Ω → [p,1] with Tk(f) ≥ (1 + δ)pkTk(Ω), in the microscopic regime.

- Lemma 6.3. Assume that δ−3pk−2 log2(1/p) → ∞, and f = p + g: Ω → [p,1] with Tk(f) ≥ (1 + δ)pkTk(Ω). Then


g(a)νa ≥ (1 − o(1))δpTk(Ω). (6.6)

a∈Ω

Proof. Set threshold τ = p3/4. As in Section 5.2.1, write g = g≤τ + g>τ. As in Lemma 6.3, we have by Lemma 5.2 and (6.4),

Ip(p + g>τ(a)) ≤

g>τ(a)log(1/p)

a∈Ω

a∈Ω

a∈Ω

thereby gaining an extra log(1/p) factor compared to (6.5). By expanding, we have

Ip(f(a)) ≤ δ2Np, (6.7)

Tk(p + g≤τ + g>τ) =

TX,Y,Z(p,g≤τ,g>τ), (6.8)

X,Y,Z

where TX,Y,Z(p,g≤τ,g>τ) is the same as earlier (5.8). We say that TX,Y,Z(p,g≤τ,g>τ) contributes negligibly to the sum (6.8) if TX,Y,Z(p,g≤τ,g>τ) = o(δN2pk). We will show that unless |X| = k − 1 or k, the term contributes negligibly.

Indeed, as in Section 5.2.1, if |Z| ≥ 2, then by Lemma 5.3 and (6.7),

2

2

δ2Np log(1/p)

= o(δN2pk),

TX,Y,Z(p,g≤τ,g>τ) ≤ (k − 1)

g>τ(a)

a∈Ω

where the ﬁnal step uses the microscopic scale hypothesis δ−3pk−2 log2(1/p) → ∞.

If |Z| ≤ 1 and |Y ∪ Z| ≥ 2, then by Lemma 5.3 and (6.5),

2

TX,Y,Z(p,g≤τ,g>τ) ≤ (k − 1)τk−2

τk−2δ2p2N2 = o(δN2pk),

g(a)

a∈Ω

where the last step holds due to τ = o(p2/3(log(1/p))−2/(3k−6)) and the microscopic scale hypothesis on δ.

This shows that the non-neglible contributions are those terms with |X| = k − 1 or k. Hence

k−1

Tk(f) = pkTk(Ω) + pk−1

g(x + jy) + o(δpkN2)

x,y

j=0

= pkTk(Ω) + pk−1

g(a)νa + o(δpkN2),

a∈Ω

where the ﬁrst sum runs over all pairs (x,y) of elements in the ambient group such that {x,x + y,...,x + (k − 1)y} ⊂ Ω. Since Tk(f) ≥ (1 + δ)pkTk(Ω), we have a∈Ω g(a)νa ≥ (1 − o(1))δpTk(Ω), as required.

In the ﬁnal step of the proof of Theorem 6.1, we convert the lower bound on the weighted

sum of g from the above lemma to a lower bound on the entropy a Ip(p+g(a)). We consider the two cases Ω = Z/NZ and [N] separately.

Case 1: Ω = Z/NZ. In this case, we have νa = kN for all a ∈ Ω and Tk(Ω) = N2. By convexity of Ip(·), (6.6), and Lemma 5.2,

1 N a∈Ω

Ip(p + g(a)) ≥ NIp p +

g(a)

a∈Ω

δ2Np 2k2

δp k ∼

≥ NIp p + (1 − o(1))

. This combined with Lemma 6.2, proves Theorem 6.1, when Ω = Z/NZ.

Case 2: Ω = [N]. In this case, the quantities νa are unequal, and the solution requires an extra step. We use the estimate5

Ip(p + x) ≥ (1 + o(1))p0.3x uniformly for all x ∈ [p1.1,1 − p]. (6.9) It follows by (6.9) and (6.4) that

g>p1.1(a) ≤ (1 + o(1))p−0.3

Ip(p + g>p1.1(a))

a∈Ω

a∈Ω

≤ (1 + o(1))p−0.3

Ip(f(a)) ≤ (1 + o(1))δ2p0.7N = o(δpN)

a∈Ω

where the ﬁnal step, δ = o(p0.3), is due to the microscopic scale hypothesis. Since νa N for all a ∈ Ω, the above estimate along with (6.6) gives

g≤p1.1(a)νa ≥ (1 − o(1))δpTk(Ω).

a∈Ω

5Proof of estimate: by Lemma 5.2, for x ∈ [p1.1, 12p0.9] we have Ip(p + x) ≥ Ip(p + p1.1) ∼ 12p1.2 ≥ p0.3x, and for x ≥ 12p0.9 we have Ip(p + x) ∼ xlog(x/p) ≥ (1 + o(1))p0.3x.

### By the Cauchy–Schwarz inequality, we have

δ2p2Tk(Ω)2 a∈Ω νa2

g≤p1.1(a)2 ≥ (1 − o(1))

.

a∈Ω

It follows by Lemma 5.2 and the above estimate that

g≤p1.1(a)2 2p ≥ (1 + o(1))

δ2Tk(Ω)2 2 a∈Ω νa2

Ip(f(a)) ≥

Ip(p + g≤p1.1(a)) ∼

,

a∈Ω

a∈Ω

a∈Ω

which combined with Lemma 6.2 completes the proof of Theorem 6.1.

- 6.2. Microscopic rate function. In the case Ω = Z/NZ, by symmetry, νs = kN for all s ∈ Ω, and Tk(Ω) = N2. Thus Theorem 2.6 for Ω = Z/NZ follows from Theorem 6.1.


When Ω = [N] ⊂ Z, the derivation of the formula in Theorem 2.6 is routine though a bit more involved. For each s ∈ [N] and 0 ≤ j < k, let νs,j denote the number of pairs of a,b ∈ Z such that a,a + (k − 1)b ∈ [N] and a + jb = s, i.e., the number of k-APs (allowing zero or negative common diﬀerence) contained in [N] and whose (j + 1)-th term is s. It is easy to see that νs,j equals to the number of b ∈ Z satisfying 1 ≤ s + (k − 1 − j)b ≤ N and 1 ≤ s − jb ≤ N, so that

s − 1 j

N − s k − 1 − j

s − 1 k − 1 − j

N − s j

νs,j = min

+ 1. Thus, for each s ∈ [N],

,

+ min

,

k−1

k−1

s − 1 j

N − s k − 1 − j

,

.

νs =

νs,j = k + 2

min

j=0

j=0

By Riemann sum, we have

k−1

N

N−3

νs2 = 4

βi,j, where

lim

N→∞

s=1

i,j=0

βi,j = ˆ 1

1 − x k − 1 − i

x i

x

min

min

dx.

,

- j

,

1 − x

- k − 1 − j


0

Observing that min{x/i,(1 − x)(k − 1 − i)} is piecewise-linear with the kink at x = i/(k − 1), we can compute the above integral: for all 0 ≤ i ≤ j ≤ k − 1,

dx + ˆ j

βij = ˆ i

dx + ˆ 1

x2 ij

(1 − x)2 (k − 1 − i)(k − 1 − j)

(1 − x)x (k − 1 − i)j

k−1

k−1

dx

- j

- k−1


i k−1

0

(k − 1)2 − i2 − (k − 1 − j)2 6(k − 1)2(k − 1 − i)j

=

. In particular, for all 0 ≤ i ≤ k − 1,

1 3(k − 1)2

. Therefore,

βi,i =

k−1

k−1

N

γk (k − 1)2

N−3

νs2 = 4

βi,j = 4

βi,i + 8

βi,j =

lim

,

N→∞

s=1

i,j=0

i=0

0≤i<j<k

where

(k − 1)2 − i2 − (k − 1 − j)2 (k − 1 − i)j

4 3

γk =

k +

.

0≤i<j<k

Since Tk([N]) ∼ N2/(k − 1) for ﬁxed k as N → ∞, Theorem 2.6 for Ω = [N] follows from

- Theorem 6.1. As for the remark following Theorem 2.6, we always have γk ≥ k2 due to (6.3). The ﬁrst

few values of γk are

γ3 =

28 3

, γ4 = 17, γ5 =

718 27

.

The asymptotic dependence of γk on k can be computed via a Riemann integral6 (note that the integrand takes value in [0,2] in the given domain):

lim

k→0

γk k2

=

4 3

ˆ

0≤x≤y≤1

1 − x2 − (1 − y)2 (1 − x)y

dxdy =

40 − 2π2 9 ≈ 1.14.

7. Replica symmetry

In this section, we record a partial result on exact replica symmetry for constant values of p and δ in the case of Ω = Z/NZ, analogous to results about dense random graphs in [10, 27]. Unlike previous sections, where we solve the variational problem asymptotically as p → 0, the following theorem gives exact replica symmetry, i.e., we give suﬃcient conditions on constants p and δ so that the constant function uniquely minimizes the variational problem. Unlike the results in [27], we do not know if the following theorem gives the full replica symmetry phase (it probably does not). The proof is nearly identical to the one in [27], the only diﬀerence being the Hölder-like inequality (Lemma 7.2) for k-APs.

Using arguments very similar to [32], one can also prove regions of replica symmetry in the lower tail. Details are omitted.

- Theorem 7.1. Take any 0 < p ≤ q < 1, positive integer k ≥ 3 and prime N. Suppose that


(qk/2,Ip(q)) lies on the convex minorant of the function x  → Ip(x2/k). Then the constant function f ≡ q is the unique minimizer to the variational problem (2.2) with Ω = Z/NZ and

(1 + δ)pk = qk, so that φp(k,Z/NZ)(δ) = NIp(q).

Remark. The hypothesis that N is prime is mainly for convenience, and it is likely unnecessary here. For example, the proof shows that when k is even, there is no requirement on N, and when k is odd, gcd(k − 1,N) = 1 suﬃces.

Proof. In the variational problem (2.2), suppose that f : Z/NZ → [0,1] satisﬁes Tk(f) ≥ (1 + δ)pkN2 = qkN2. By Lemma 7.2 below, we have

f(a)k/2 ≥ qk/2N. (7.1)

a∈Z/NZ

Let J(x) = Ip(x2/k), and (x) = J (qk/2)(x − qk−2) + Ip(q). Then is the tangent line to J(x)

- at x = qk/2, and by the convex minorant condition, we have J(x) ≥ (x) for all x ∈ [0,1].


6The integral was computed using Mathematica.

### Since Ip(x) is increasing in x ∈ [p,1], we have J (qk/2) ≥ 0. It follows that

J(f(a)k/2)

Ip(f(a)) =

a∈Ω

a∈Ω

(f(a)k/2)

≥

a∈Ω

= J (qk/2)

f(a)k/2 − qk/2N + Ip(q) ≥ Ip(q)

a∈Ω

by (7.1). Equality occurs if and only if f(a) = q for all a ∈ Z/NZ.

- Lemma 7.2. Let k ≥ 3 and N a prime. For any f : Z/NZ → [0,∞), one has


2

f(a)k/2

Tk(f) ≤

.

a∈Z/NZ

Proof. Deﬁne

hi,j(a,b) = f(a + ib)f(a + jb). By Hölder’s inequality, one has

f(a)f(a + b)···f(a + (k − 1)b)

Tk(f) =

a,b∈Z/NZ

h0,1(a,b)h1,2(a,b)···hk−2,k−1(a,b)hk−1,0(a,b)

=

a,b∈Z/NZ

 

 

1/k

hi,j(a,b)k

≤

a,b∈Z/NZ

(i,j)∈{(0,1),(1,2),...,(k−2,k−1),(k−1,0)}

2

f(a)k/2

### =

,

a∈Z/NZ

where the last step is due to

hij(a,b)k =

f(a + ib)k/2f(a + jb)k/2

a,b∈Z/NZ

a,b∈Z/NZ

2

if gcd(i − j,N) = 1.

f(a)k/2

=

a∈Z/NZ

Note that when k is even, we can instead write

f(a)f(a + b)···f(a + (k − 1)b) = h0,1(a,b)2h2,3(a,b)2 ···hk−2,k−1(a,b)2 and remove the need for primality hypothesis on N.

8. Maximizing the number of k-APs In this section we prove Theorem 2.4, repeated below for convenience.

Theorem 2.4. Fix a positive integer k ≥ 3. There exists some constant ck > 0 such that the following statement holds. Let A ⊂ Z be a subset with |A| = n, or A ⊂ Z/NZ with N prime and |A| = n ≤ ckN. Then Tk(A) ≤ Tk([n]).

In Section 8.1, we will prove Theorem 2.4 when A ⊂ Z using a simple combinatorial argument. Unfortunately this proof does not extend to the case A ⊂ Z/NZ, due to the lack of a natural ordering in Z/NZ. Following the idea in [18], we will attempt to replace the original set A ⊂ Z/NZ by a Freiman model A ⊂ Z (so that in particular |A| = | A| and Tk(A) = Tk( A)). This technique, called rectiﬁcation, was ﬁrst investigated in [3]. The following lemma gives a simple example of rectiﬁcation:

- Lemma 8.1. Let N be a positive integer. Let A ⊂ Z ∩ (−N/4,N/4) be a subset, and let A ⊂ Z/NZ be the image of A under the natural projection Z → Z/NZ. Then Tk(A) = Tk( A).


Proof. Let π: A → A be the natural projection map. We need to show that both π and π−1 preserve k-APs. It suﬃces to show that π is a Freiman isomorphism, in the sense that for any a1,a2,a3,a4 ∈ A, a1 + a2 = a3 + a4 if and only if π(a1) + π(a2) = π(a3) + π(a4). The only if direction is clear. The if direction follows from the fact that

−N < a1 + a2 − a3 − a4 < N whenever a1,a2,a3,a4 ∈ A.

A more sophisticated rectiﬁcation lemma is given in [18, Theorem 4.1], which allows us to prove Theorem 2.4 when the set A has small doubling, in the sense that |A + A|/|A| is small (see Lemma 8.3 below). After stating some preparatory lemmas in Section 8.2, we will then prove the general case of Theorem 2.4 in Section 8.3 using a structural decomposition theorem [18, Proposition 3.2], which allows us to deduce that if Tk(A) is close to maximal then A must have small doubling.

- 8.1. Proof of Theorem 2.4 when A ⊂ Z. In this subsection we prove the case when


A ⊂ Z by induction on k.7 The statement is trivial when k = 2 since Tk(A) = n2 always. Now let k ≥ 3, and assume that the statement has been proved for smaller values of k. It is convenient to count the number of nontrivial increasing k-APs in A:

T k(A) = #{(a,b) : b > 0,a,a + b,...,a + (k − 1)b ∈ A}.

Clearly Tk(A) = 2T k(A) + n. Thus it suﬃces to show that T k(A) ≤ T k([n]). Arrange the elements in A in increasing order:

A = {a0 < a1 < ··· < an−1}. Choose m ∈ Z such that

k − 2 k − 1

k − 2 k − 1

(n − 1) ≤ m <

n + 1.

There are two types of k-APs counted in T k(A): those whose second largest element is at least am, and those whose second largest element is smaller than am. If the second largest

7We are grateful to Anton Bankevich for suggesting the proof in this subsection.

### element of a k-AP in A is ai for some m ≤ i < n, then there are at most n−1−i possibilities for its largest element. Thus the number of k-APs in A of the ﬁrst type is at most

(n − 1 − i).

m≤i<n

For k-APs in A of the second type, their ﬁrst k −1 terms form a (k −1)-AP in {a0,...,am−1}. Thus the number of k-APs in A of the second type is at most

T k−1({a0,...,am−1}) ≤ T k−1({0,1,...,m − 1}) by induction hypothesis. It follows that

(n − 1 − i) + T k−1({0,1,...,m − 1}).

T k(A) ≤

m≤i<n

To conclude the proof, we claim that the ﬁrst term on the right hand side above is equal to the number of k-APs in {0,1,...,n − 1} of the ﬁrst type:

(n − 1 − i) = #{(a,b) : b > 0,a ≥ 0,a + (k − 1)b < n,a + (k − 2)b ≥ m}, (8.1)

m≤i<n

and the second term is equal to the number of k-APs in {0,1,...,n − 1} of the second type:

T k−1({0,1,...,m − 1}) = #{(a,b) : b > 0,a ≥ 0,a + (k − 1)b < n,a + (k − 2)b < m}. (8.2) To prove (8.1), it suﬃces to show that for any m ≤ i < n we have

n − 1 − i = #{(a,b) : b > 0,a ≥ 0,a + (k − 1)b < n,a + (k − 2)b = i}.

This follows from the fact that any choice of the value of j = a+(k−1)b from {i+1,...,n−1} uniquely determines an admissible (a,b) since

i ≥ (k − 2)(j − i)

by our choice of m. To prove (8.2), note that any (a,b) with b > 0, a ≥ 0, and a+(k−2)b < m automatically satisﬁes a + (k − 1)b < n since

- k − 1

- k − 2


- k − 1

- k − 2


a k − 2 ≤

(m − 1) < n by our choice of m.

a + (k − 1)b =

[a + (k − 2)b] −

- 8.2. Proof of Theorem 2.4 when A ⊂ Z/NZ: preparations. In this subsection, we collect a few lemmas that will allow us to reduce the problem in Z/NZ to the simpler one in Z. From now on we ﬁx some large prime N and work in Z/NZ. To begin with, we show that k-AP counts are controlled by additive energy. For two subsets A,B ⊂ Z/NZ, the additive energy E(A,B) is deﬁned by


E(A,B) = #{(a,a ,b,b ) ∈ A × A × B × B : a + b = a + b }, and note the trivial bound

E(A,B) ≤ min(|A|2|B|,|A||B|2) ≤ |A|3/2|B|3/2. We will also consider additive energy of dilates · A for a positive integer , deﬁned by · A = { a : a ∈ A}. For subsets A1,...,Ak ⊂ Z/NZ, deﬁne the asymmetric k-AP count by Tk(A1,...,Ak) = #{(a,b) : a ∈ A1,a + b ∈ A2,...,a + (k − 1)b ∈ Ak}.

Clearly if A1 = ··· = Ak = A then Tk(A,...,A) = Tk(A).

- Lemma 8.2. Let A1,...,Ak ⊂ Z/NZ be subsets, and let n = max(|A1|,...,|Ak|). If

max

 ,  ∈{1,2}

E( · Ai,  · Ai+1) ≤ εn3

for some ε ∈ (0,1) and 1 ≤ i < k, then Tk(A1,...,Ak) ≤ ε1/6n2. Proof. Note that Tk(A1,...,Ak) is trivially bounded by either T3(Ai−1,Ai,Ai+1) or T3(Ai,Ai+1,Ai+2). The conclusion then follows immediately from [18, Lemma 4.2].

The following lemma shows that Theorem 2.4 holds if A has small doubling.

- Lemma 8.3. Let K ≥ 1. The following statement holds if c is suﬃciently small in terms of K. Let A ⊂ Z/NZ be a subset with |A| = n ≤ cN and |A + A| ≤ K|A|. Then Tk(A) ≤ Tk([n]).

Proof. By [18, Theorem 4.1], there exisits a dilate d · A of A (for some d ∈ (Z/NZ)∗) that is contained in an interval of length at most N/2k. After dilation and translation we may assume that A ⊂ [1,N/2k]. Now that any k-AP in A (as a subset of Z/NZ) is also a k-AP in Z, we may apply the A ⊂ Z case of Theorem 2.4 to conclude that Tk(A) ≤ Tk([n]), as desired.

8.3. Proof of Theorem 2.4 when A ⊂ Z/NZ. We continue to work in Z/NZ. In view of Lemma 8.3, we may assume that n is suﬃciently large in terms of k. We ﬁrst establish a rough structure theorem for sets with close to maximal number of k-APs.

- Lemma 8.4. Let c > 0 be suﬃciently small. Let A ⊂ Z/NZ be a subset with |A| = n ≤ cN, and suppose that n is suﬃciently large in terms of k. If


n2 k − 1

1 100k2

Tk(A) ≥

1 −

,

then there exists a dilate d · A of A for some d ∈ (Z/NZ)∗, such that all but at most n/10k2 elements in d · A lies in an interval of length at most N/100k.

Proof. Choose a suﬃciently small ε > 0, and then choose some ε > 0 suﬃciently small in terms of ε. Apply [18, Proposition 3.2] to obtain a structural decomposition A = A1 ∪···∪Am ∪A0 into disjoint subsets satisfying the following properties:

- (1) |Ai| ε |A| for each 1 ≤ i ≤ m, so that m ε 1;
- (2) |Ai + Ai| ε,ε |Ai| for each 1 ≤ i ≤ m;
- (3) E( · Ai,  · Aj) ≤ ε |Ai|3/2|Aj|3/2 whenever 1 ≤ i < j ≤ m and  ,  ∈ {1,2};
- (4) E( · A0,  · A) ≤ ε|A|3 whenever  ,  ∈ {1,2}.


) for some 1 ≤ i1,...,ik ≤ m, and the k terms Tk(A0,A,...,A),Tk(A,A0,...,A),...,Tk(A,A,...,A0). To estimate Tk(Ai

To estimate Tk(A), we write it as the sum of mk terms of the form Tk(Ai

### ,...,Ai

1

k

) when i1,...,ik are not all the same, we use Lemma 8.2 and property (3) to obtain

### ,...,Ai

1

k

) ≤ ε 1/6n2.

Tk(Ai

### ,...,Ai

1

k

Thus the total contributions from these terms are bounded by ε 1/6mkn2. Moreover, by Lemma 8.2 and property (4) we also have

Tk(A0,A,...,A) ≤ ε1/6n2,

and similarly for the other k − 1 terms involving A0. Thus we have shown that

m

k

n2 100k3

Tk(Ai) + ε 1/6mk + ε1/6k n2 ≤

Tk(A) ≤

Tk(Ai) +

,

i=1

i=1

if ε,ε are small enough (recall that m depends only on ε). If c is suﬃciently small in terms of ε,ε , then Lemma 8.3 can be applied to each Ai in view of property (2) to get

1 k − 1

Tk(A) ≤

m

|Ai|2 +

i=1

n2 100k3 ≤

1 4

n k − 1

(k − 1)m +

|Ai| +

max

1≤i≤m

n2 100k3

1 4

(k − 1)m +

.

Combined with the lower bound for Tk(A) in the hypothesis, this implies that |Ai| ≥ (1 − 1/10k2)n for some 1 ≤ i ≤ k. By [18, Theorem 4.1], after dilation we may assume that Ai is contained in an interval of length at most N/100k.

We are now ready to prove Theorem 2.4. In view of Lemma 8.4, after a suitable dilation and translation we may assume that the set A0 = A ∩ [−N/100k,N/100k] has size |A0| ≥ (1 − 1/10k2)|A|. Let

A1 = A ∩ ([−0.1N,0.1N] ∪ [0.4N,0.6N]).

Write n1 = |A1| and n2 = |A\A1| = n − n1. Note that for any k-AP in A, if at least two of its ﬁrst three terms lie in A0, then it is entirely contained in A1. Thus any k-AP in A that is not entirely contained in A1 must have at least one term outside A1 and at least two out of the ﬁrst three terms outside A0, and the number of these k-APs is then bounded by 3kn2|A\A0| ≤ nn2/2k. It follows that

nn2 2k

Tk(A) ≤ Tk(A1) +

.

Note that 2 · A1 ⊂ [−0.2N,0.2N]. Thus from Lemma 8.1 and the integer case of Theorem 2.4 proved in Section 8.1, we obtain

Tk(A1) = Tk(2 · A1) ≤ Tk([n1]). (8.3) Using (2.6) we arrive at

n21 k − 1

1 4

nn2 2k

(k − 1) +

Tk(A) ≤

. If n2 > 0, then

+

n2 − n21 k − 1

1 4

nn2 2k ≤

nn2 k ≤

(k − 1) +

, provided that n ≥ k(k − 1)/2 (which we may assume). Thus in this case we have Tk(A) ≤

n2 k − 1 ≤ Tk([n])

as desired. If n2 = 0, then A = A1 and the desired conclusion follows from (8.3).

Appendix A. Proofs of further bounds on Gaussian widths

- A.1. Matching lower bound for 3-APs. Here we prove the matching lower bound GW(T3/N) N log N

in Theorem 4.4. As in Section 4.1 we only work out the Ω = Z/NZ setting here. The Ω = [N] ⊂ Z setting can be deduced similarly by embedding [N] in a larger cyclic group to avoid APs from wrapping around zero.

First we show that if h: Z/NZ → R is a random function with h(a) ∼ Normal(0,1) i.i.d. for a ∈ Z/NZ, then, with probability at least 1/2, we can ﬁnd some f : Z/NZ → [0,1] such that

1

N ∇T3(f),h N log N. (A.1) Indeed, the real components of h(2s) for integers 0 ≤ s < N/4 are independent Gaussians with variance Θ(1/N) (since the Fourier transform is orthogonal), so with probability at least 0.9 there is some integer 0 < s < N/4 such that h(2s) (log N)/N and furthermore h(0) = O(1/

√

N). Then, setting f(a) = (1+cos(2πsa/N))/2 so that f(0) = 1/2, f(±s) = 1/4 and f(r) = 0 for all r ∈/ {0,s,−s}, we obtain, by Lemma 4.3,

1 N2

T3(f,h,f) = f(0)2 h(0) + f(s)2 h(−2s) + f(−s)2 h(2s) =

1 4

h(0) +

1 8

h(2s)

log N N

, and

1 N2

T3(h,f,f) =

1 N2

T3(f,f,h) = f(0)2 h(0) = O(N−1/2) Thus (A.1) holds since  ∇T3(f),h = T3(f,f,h) + T3(f,h,f) + T3(h,f,f).

Finally, one can convert f : Z/NZ → [0,1] to a {0,1}-valued function by changing the value of f at a ∈ Z/NZ to 1 with probability f(a) and 0 with probability 1−f(a). A routine probabilistic argument shows that (A.1) holds for some f : Z/NZ → {0,1}, thereby proving GW(T3/N) √N log N.

- A.2. Improved upper bound for 4-AP. Here we prove the ﬁnal claim in Theorem 4.1 that


GW(T4/N) N3/4(log N)1/4. (A.2) As earlier we only discuss the Ω = Z/NZ setting here. We have

 ∇T4(f),h = T4(h,f,f,f) + T4(f,h,f,f) + T4(f,f,h,f) + T4(f,f,f,h). (A.3) Deﬁne the following multiplicative analogue of the ﬁnite diﬀerence

∆sh(x) := f(x)h(x + s) (since we will be working with real-valued functions, one can ignore the conjugation). The Fourier transform of ∆sh controls T4, as shown by the following lemma, which plays a similar role to Lemma 4.4 for T3.

Lemma A.1. For any f : Z/NZ → [−1,1] and any h: Z/NZ → R,

1 N2|T4(h,f,f,f)|

1 N

1/2

∆sh ∞

.

s∈Z/NZ

The same holds with the left-hand side replaced by T(f,h,f,f), T(f,f,h,f), or T(f,f,f,h).

Proof. We prove the inequality for T(h,f,f,f) as the other cases are analogous. We have

2

|T4(h,f,f,f)|2 =

h(a − 3b)f(a − 2b)f(a − b) f(a)

a b

2

[Cauchy-Schwarz]

### ≤ N

h(a − 3b)f(a − 2b)f(a − b)

a b

h(a − 3b)h(a − 3b )f(a − 2b)f(a − 2b )f(a − b)f(a − b )

### = N

a,b,b

∆3sh(a − 3b)∆2sf(a − 2b)∆sf(a − b) [by setting s = b − b ]

### = N

a,b,s

### = N

s

T3(∆3sh,∆2sf,∆sf)

N3

s

∆3sh ∞ [by Lemma 4.4 on T3]

### N3

∆sh ∞. The lemma follows by rearranging.

s

Let h: Z/NZ → R be a random function with independent standard Gaussian values. Noting that

1 N

h(a)h(a + s)ω−ar

∆sh(r) =

a∈Z/NZ

is a quadratic form of Gaussians, and using tail bounds for such random variables [21] (also [4, Example 2.12]) we ﬁnd that for every s = 0,

log N N

with probability 1 − O(N−10). (A.4) We always have ∆sh ∞ ≤ 1 for all s. Thus

∆sh ∞ = O

GW(T4/N) = Eh sup

 ∇T4(f)/N,h

f : Z/NZ→{0,1}

√

1/2

Eh

[by (A.3) and Lem. A.1]

N

∆sh ∞

s∈Z/NZ

N3/4(log N)1/4. [by (A.4)]

Acknowledgments. We thank Ben Green and Freddie Manners for helpful discussions. We also thank the anonymous referee for helpful comments that improved the exposition of the paper.

References

- [1] R. C. Baker, G. Harman, and J. Pintz. The diﬀerence between consecutive primes. II. Proc. London Math. Soc. (3), 83(3):532–562, 2001. ↑15
- [2] B. B. Bhattacharya, S. Ganguly, E. Lubetzky, and Y. Zhao. Upper tails and independence polynomials in random graphs. Adv. Math., 319:313–347, 2017. ↑1, ↑2, ↑3


- [3] Y. F. Bilu, V. F. Lev, and I. Z. Ruzsa. Rectiﬁcation principles in additive number theory. Discrete Comput. Geom., 19(3, Special Issue):343–353, 1998. Dedicated to the memory of Paul Erdős. ↑27
- [4] S. Boucheron, G. Lugosi, and P. Massart. Concentration inequalities. Oxford University Press, Oxford,

2013. A nonasymptotic theory of independence, With a foreword by Michel Ledoux. ↑32

- [5] J. Briët and S. Gopi. Gaussian width bounds with applications to arithmetic progressions in random settings. arXiv:1711.05624. ↑4, ↑11
- [6] S. Chatterjee. The missing log in large deviations for triangle counts. Random Structures Algorithms, 40(4):437–451, 2012. ↑1
- [7] S. Chatterjee. An introduction to large deviations for random graphs. Bull. Amer. Math. Soc., to appear. ↑2
- [8] S. Chatterjee and A. Dembo. Nonlinear large deviations. Adv. Math., 299:396–450, 2016. ↑1, ↑2, ↑3, ↑7, ↑14
- [9] S. Chatterjee and P. S. Dey. Applications of Stein’s method for concentration inequalities. Ann. Probab., 38(6):2443–2485, 2010. ↑1
- [10] S. Chatterjee and S. R. S. Varadhan. The large deviation principle for the Erdős-Rényi random graph. European J. Combin., 32(7):1000–1017, 2011. ↑1, ↑6, ↑25
- [11] D. Conlon and W. T. Gowers. Combinatorial theorems in sparse random sets. Ann. of Math. (2), 184(2):367–454, 2016. ↑14
- [12] E. Croot. The minimal number of three-term arithmetic progressions modulo a prime converges to a limit. Canad. Math. Bull., 51:47–56, 2008. ↑6
- [13] B. Demarco and J. Kahn. Tight upper tail bounds for cliques. Random Structures Algorithms, 41(4):469– 487, 2012. ↑1
- [14] B. DeMarco and J. Kahn. Upper tails for triangles. Random Structures Algorithms, 40(4):452–459, 2012. ↑1
- [15] R. Eldan. Gaussian-width gradient complexity, reverse log-Sobolev inequalities and nonlinear large deviations. arXiv:1612.04346. ↑2, ↑3, ↑4, ↑7, ↑8
- [16] N. Frantzikinakis. Some open problems on multiple ergodic averages. arXiv preprint arXiv:1103.3808,

2016. ↑14

- [17] N. Frantzikinakis, E. Lesigne, and M. Wierdl. Random diﬀerences in Szemerédi’s theorem and related results. J. Anal. Math., 130:91–133, 2016. ↑14
- [18] B. Green and O. Sisask. On the maximal number of 3-term arithmetic progressions in subsets of Z/pZ. Bull. Lond. Math. Soc., 40(6):945–955, 2008. ↑2, ↑5, ↑27, ↑29, ↑30
- [19] B. Green and T. Tao. The quantitative behaviour of polynomial orbits on nilmanifolds. Ann. of Math.

(2), 175(2):465–540, 2012. ↑14

- [20] B. Green, T. Tao, and T. Ziegler. An inverse theorem for the Gowers Us+1[N]-norm. Ann. of Math. (2), 176(2):1231–1372, 2012. ↑2
- [21] D. L. Hanson and F. T. Wright. A bound on tail probabilities for quadratic forms in independent random variables. Ann. Math. Statist., 42:1079–1083, 1971. ↑32
- [22] S. Janson, K. Oleszkiewicz, and A. Ruciński. Upper tails for subgraph counts in random graphs. Israel J. Math., 142:61–92, 2004. ↑1
- [23] S. Janson and A. Ruciński. The infamous upper tail. Random Structures Algorithms, 20(3):317–342,

2002. ↑1

- [24] S. Janson and A. Ruciński. The deletion method for upper tail estimates. Combinatorica, 24(4):615–640,

2004. ↑1

- [25] S. Janson and A. Ruciński. Upper tails for counting objects in randomly induced subhypergraphs and rooted random graphs. Ark. Mat., 49(1):79–96, 2011. ↑1, ↑2
- [26] J. H. Kim and V. H. Vu. Divide and conquer martingales and the number of triangles in a random graph. Random Structures Algorithms, 24(2):166–174, 2004. ↑1
- [27] E. Lubetzky and Y. Zhao. On replica symmetry of large deviations in random graphs. Random Structures Algorithms, 47(1):109–146, 2015. ↑1, ↑6, ↑25
- [28] E. Lubetzky and Y. Zhao. On the variational problem for upper tails in sparse random graphs. Random Structures Algorithms, 50:420–436, 2017. ↑1, ↑2, ↑3, ↑17
- [29] T. Tao. Higher order Fourier analysis, volume 142 of Graduate Studies in Mathematics. American Mathematical Society, Providence, RI, 2012. ↑14


- [30] V. H. Vu. A large deviation result on the number of small subgraphs of a random graph. Combin. Probab. Comput., 10(1):79–94, 2001. ↑1
- [31] L. Warnke. Upper tails for arithmetic progressions in random subsets. Israel J. Math., 221:317–365, 2017. ↑1, ↑2
- [32] Y. Zhao. On the lower tail variational problem for random graphs. Combin. Probab. Comput., 26:301–320,


2017. ↑6, ↑25

Department of Statistics, University of Pennsylvania, Philadelphia, PA 19104, USA E-mail address: bhaswar@wharton.upenn.edu

Department of Statistics, UC Berkeley, California, CA 94720, USA E-mail address: sganguly@berkeley.edu

Department of Mathematics, University of Kentucky, Lexington, KY 40506, USA E-mail address: xuancheng.shao@uky.edu

Department of Mathematics, Massachusetts Institute of Technology, Cambridge, MA 02139, USA

E-mail address: yufeiz@mit.edu

