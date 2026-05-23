|Noname manuscript No. (will be inserted by the editor)|
|---|


### Lower bounds on matrix factorization ranks via noncommutative polynomial optimization

#### Sander Gribling · David de Laat · Monique Laurent

# arXiv:1708.01573v3[math.OC]5Nov2018

Received: date / Accepted: date

Abstract We use techniques from (tracial noncommutative) polynomial optimization to formulate hierarchies of semideﬁnite programming lower bounds on matrix factorization ranks. In particular, we consider the nonnegative rank, the positive semideﬁnite rank, and their symmetric analogues: the completely positive rank and the completely positive semideﬁnite rank. We study convergence properties of our hierarchies, compare them extensively to known lower bounds, and provide some (numerical) examples.

Keywords Matrix factorization ranks · Nonnegative rank · Positive semideﬁnite rank · Completely positive rank · Completely positive semideﬁnite rank · Noncommutative polynomial optimization

#### Mathematics Subject Classiﬁcation (2010) 15A48 · 15A23 · 90C22

1 Introduction 1.1 Matrix factorization ranks

A factorization of a matrix A ∈ Rm×n over a sequence {Kd}d∈N of cones that are each equipped with an inner product  ·,·  is a decomposition of the form A = ( Xi,Yj ) with Xi,Yj ∈ Kd for all (i, j) ∈ [m]×[n], for some integer d ∈ N. Following [35], the

The ﬁrst and second authors are supported by the Netherlands Organization for Scientiﬁc Research, grant number 617.001.351, and the second author by the ERC Consolidator Grant QPROGRESS 615307.

S. Gribling CWI, Amsterdam

D. de Laat CWI, Amsterdam

M. Laurent CWI, Amsterdam, and Tilburg University

smallest integer d for which such a factorization exists is called the cone factorization rank of A over {Kd}.

The cones Kd we use in this paper are the nonnegative orthant Rd+ with the usual inner product and the cone Sd+ (resp., Hd+) of d ×d real symmetric (resp., Hermitian) positive semideﬁnite matrices with the trace inner product X,Y = Tr(XTY) (resp.,

X,Y = Tr(X∗Y)). We obtain the nonnegative rank, denoted rank+(A), which uses the cones Kd = Rd+, and the positive semideﬁnite rank, denoted psd-rankK(A), which uses the cones Kd = Sd+ for K = R and Kd = Hd+ for K = C. Both the nonnegative rank and the positive semideﬁnite rank are deﬁned whenever A is entrywise nonnegative.

The study of the nonnegative rank is largely motivated by the groundbreaking work of Yannakakis [78], who showed that the linear extension complexity of a polytope P is given by the nonnegative rank of its slack matrix. The linear extension complexity of P is the smallest integer d for which P can be obtained as the linear image of an afﬁne section of the nonnegative orthant Rd+. The slack matrix of P is given by the matrix (bi −aTi v)v∈V,i∈I, where P = conv(V) and P = {x : aTi x ≤ bi (i ∈ I)} are the point and hyperplane representations of P. Analogously, the semideﬁnite extension complexity of P is the smallest d such that P is the linear image of an afﬁne section of the cone Sd+ and it is given by the (real) positive semideﬁnite rank of its slack matrix [35].

The motivation to study the linear and semideﬁnite extension complexities is that polytopes with small extension complexity admit efﬁcient algorithms for linear optimization. Well-known examples include spanning tree polytopes [55] and permutahedra [33], which have polynomial linear extension complexity, and the stable set polytope of perfect graphs, which has polynomial semideﬁnite extension complexity [53] (see, e.g., the surveys [19,26]). The above connection to the nonnegative rank and to the positive semideﬁnite rank of the slack matrix can be used to show that a polytope does not admit a small extended formulation. Recently this connection was used to show that the linear extension complexities of the traveling salesman, cut, and stable set polytopes are exponential in the number of nodes [30], and this result was extended to their semideﬁnite extension complexities in [51]. Surprisingly, the linear extension complexity of the matching polytope is also exponential [66], even though linear optimization over this set is polynomial time solvable [24]. It is an open question whether the semideﬁnite extension complexity of the matching polytope is exponential.

Besides this link to extension complexity, the nonnegative rank also ﬁnds applications in probability theory and in communication complexity, and the positive semideﬁnite rank has applications in quantum information theory and in quantum communication complexity (see, e.g., [56,25,42,30]).

For square symmetric matrices (m = n) we are also interested in symmetric analogues of the above matrix factorization ranks, where we require the same factors for the rows and columns (i.e., Xi = Yi for all i ∈ [n]). The symmetric analog of the nonnegative rank is the completely positive rank, denoted cp-rank(A), which uses the cones Kd = Rd+, and the symmetric analog of the positive semideﬁnite rank is the completely positive semideﬁnite rank, denoted cpsd-rankK(A), which uses the cones Kd = Sd+ if K = R and Kd = Hd+ if K = C. These symmetric factorization ranks

are not always well deﬁned since not every symmetric nonnegative matrix admits a symmetric factorization by nonnegative vectors or postive semideﬁnite matrices. The symmetric matrices for which these parameters are well deﬁned form convex cones known as the completely positive cone, denoted CPn, and the completely positive semideﬁnite cone, denoted CSn+. We have the inclusions CPn ⊆ CSn+ ⊆ Sn+, which are known to be strict for n ≥ 5. For details on these cones see [7,18,50] and references therein.

Motivation for the cones CPn and CSn+ comes in particular from their use to model classical and quantum information optimization problems. For instance, graph parameters such as the stability number and the chromatic number can be written as linear optimization problems over the completely positive cone [45], and the same holds, more generally, for quadratic problems with mixed binary variables [14]. The cp-rank is widely studied in the linear algebra community; see, e.g., [7,69,68,11].

The completely positive semideﬁnite cone was ﬁrst studied in [50] to describe quantum analogues of the stability number and of the chromatic number of a graph. This was later extended to general graph homomorphisms in [72] and to graph isomorphism in [3]. In addition, as shown in [54,72], there is a close connection between the completely positive semideﬁnite cone and the set of quantum correlations. This also gives a relation between the completely positive semideﬁnite rank and the minimal entanglement dimension necessary to realize a quantum correlation. This connection has been used in [62,39,63] to construct matrices whose completely positive semideﬁnite rank is exponentially large in the matrix size. For the special case of synchronous quantum correlations the minimum entanglement dimension is directly given by the completely positive semideﬁnite rank of a certain matrix (see [38]).

The following inequalities hold for the nonnegative rank and the positive semideﬁnite rank: We have

psd-rankC(A) ≤ psd-rankR(A) ≤ rank+(A) ≤ min{m,n}

for any m×n nonnegative matrix A and cp-rank(A) ≤ n+21 for any n×n completely positive matrix A. However, the situation for the cpsd-rank is very different. Ex-

ploiting the connection between the completely positive semideﬁnite cone and quantum correlations it follows from results in [73] that the cone CSn+ is not closed for n ≥ 1942. The results in [23] show that this already holds for n ≥ 10. As a consequence there does not exist an upper bound on the cpsd-rank as a function of the matrix size. For small matrix sizes very little is known. It is an open problem whether CS5+ is closed, and we do not even know how to construct a 5 × 5 matrix whose cpsd-rank exceeds 5.

The rank+, cp-rank, and psd-rank are known to be computable; this follows using results from [65] since upper bounds exist on these factorization ranks that depend only on the matrix size, see [6] for a proof for the case of the cp-rank. But computing the nonnegative rank is NP-hard [76]. In fact, determining the rank+ and psd-rank of a matrix are both equivalent to the existential theory of the reals [70,71]. For the cp-rank and the cpsd-rank no such results are known, but there is no reason to assume they are any easier. In fact it is not even clear whether the cpsd-rank is computable in general.

To obtain upper bounds on the factorization rank of a given matrix one can employ heuristics that try to construct small factorizations. Many such heuristics exist for the nonnegative rank (see the overview [31] and references therein), factorization algorithms exist for completely positive matrices (see the recent paper [40], also [21] for structured completely positive matrices), and algorithms to compute positive semideﬁnite factorizations are presented in the recent work [75]. In this paper we want to compute lower bounds on matrix factorization ranks, which we achieve by employing a relaxation approach based on (noncommutative) polynomial optimization.

- 1.2 Contributions and connections to existing bounds


In this work we provide a uniﬁed approach to obtain lower bounds on the four matrix factorization ranks mentioned above, based on tools from (noncommutative) polynomial optimization.

We sketch the main ideas of our approach in Section 1.4 below, after having introduced some necessary notation and preliminaries about (noncommutative) polynomials in Section 1.3. We then indicate in Section 1.5 how our approach relates to the more classical use of polynomial optimization dealing with the minimization of polynomials over basic closed semialgebraic sets. The main body of the paper consists of four sections each dealing with one of the four matrix factorization ranks. We start with presenting our approach for the completely positive semideﬁnite rank and then explain how to adapt this to the other ranks.

For our results we need several technical tools about linear forms on spaces of polynomials, both in the commutative and noncommutative setting. To ease the readability of the paper we group these technical tools in Appendix A. Moreover, we provide full proofs, so that our paper is self-contained. In addition, some of the proofs might differ from the customary ones in the literature since our treatment in this paper is consistently on the ‘moment’ side rather than using real algebraic results about sums of squares.

In Section 2 we introduce our approach for the completely positive semideﬁnite rank. We start by deﬁning a hierarchy of lower bounds

ξ1cpsd(A) ≤ ξ2cpsd(A) ≤ ... ≤ ξtcpsd(A) ≤ ... ≤ cpsd-rankC(A),

where ξtcpsd(A), for t ∈ N, is given as the optimal value of a semideﬁnite program whose size increases with t. Not much is known about lower bounds for the cpsd-

rank in the literature. The inequality rank(A) ≤ cpsd-rankC(A) is known, which follows by viewing a Hermitian d ×d matrix as a d2-dimensional real vector, and an

analytic lower bound is given in [62]. We show that the new parameter ξ1cpsd(A) is at least as good as this analytic lower bound and we give a small example where a

strengthening of ξ2cpsd(A) is strictly better then both above mentioned generic lower bounds. Currently we lack evidence that the lower bounds ξtcpsd(A) can be larger than, for example, the matrix size, but this could be because small matrices with large cpsdrank are hard to construct or might even not exist. We also introduce several ideas leading to strengthenings of the basic bounds ξtcpsd(A).

We then adapt these ideas to the other three matrix factorization ranks discussed above, where for each of them we obtain analogous hierarchies of bounds.

For the nonnegative rank and the completely positive rank much more is known about lower bounds. The best known generic lower bounds are due to Fawzi and Parrilo [27,28]. In [28] the parameters τ+(A) and τcp(A) are deﬁned, which, respectively, lower bound the nonnegative rank and the cp-rank, along with their computable semideﬁnite programming relaxations τ+sos(A) and τcpsos(A). In [28] it is also shown that τ+(A) is at least as good as certain norm-based lower bounds. In particular, τ+(·) is at least as good as the ∞ norm-based lower bound, which was used by Rothvoß [66] to show that the matching polytope has exponential linear extension complexity. In [27] it is shown that for the Frobenius norm, the square of the norm-based bound is still a lower bound on the nonnegative rank, but it is not known how this lower bound compares to τ+(·).

Fawzi and Parrilo [28] use the atomicity of the nonnegative and completely positive ranks to derive the parameters τ+(A) and τcp(A); i.e., they use the fact that the nonnegative rank (cp-rank) of A is equal to the smallest d for which A can be written as the sum of d nonnegative (positive semideﬁnite) rank one matrices. As the psd-rank and cpsd-rank are not known to admit atomic formulations, the techniques from [28] do not extend directly to these factorization ranks. However, our approach via polynomial optimization captures these factorization ranks as well.

In Sections 3 and 4 we construct semideﬁnite programming hierarchies of lower bounds ξtcp(A) and ξt+(A) on cp-rank(A) and rank+(A). We show that the bounds ξt+(A) converge to τ+(A) as t → ∞. The basic hierarchy {ξtcp(A)} for the cp-rank does not converge to τcp(A) in general, but we provide two types of additional constraints that can be added to the program deﬁning ξtcp(A) to ensure convergence to τcp(A). First, we show how a generalization of the tensor constraints that are used in the deﬁnition of the parameter τcpsos(A) can be used for this, and we also give a more efﬁcient (using smaller matrix blocks) description of these constraints. This strengthening of ξ2cp(A) is then at least as strong as τcpsos(A), but requires matrix variables of roughly half the size. Alternatively, we show that for every ε > 0 there is a ﬁnite number of additional linear constraints that can be added to the basic hierarchy {ξtcp(A)} so that the limit of the sequence of these new lower bounds ξt+(A) is at least τcp(A)−ε. We give numerical results on small matrices studied in the literature, which show that ξ3+(A) can improve over τ+sos(A).

Finally, in Section 5 we derive a hierarchy {ξtpsd(A)} of lower bounds on the psd-rank. We compare the new bounds ξtpsd(A) to a bound from [52] and we provide some numerical examples illustrating their performance.

We provide two implementations of all the lower bounds introduced in this paper, at the arXiv submission of this paper. One implementation uses Matlab and the CVX package [37], and the other one uses Julia [9]. The implementations support various semideﬁnite programming solvers, for our numerical examples we used Mosek [2].

- 1.3 Preliminaries


In order to explain our basic approach in the next section, we ﬁrst need to introduce some notation. We denote the set of all words in the symbols x1,...,xn by

x = x1,...,xn , where the empty word is denoted by 1. This is a semigroup with involution, where the binary operation is concatenation, and the involution of a word w ∈ x is the word w∗ obtained by reversing the order of the symbols in w. The ∗-algebra of all real linear combinations of these words is denoted by R x , and its elements are called noncommutative polynomials. The involution extends to R x by linearity. A polynomial p ∈ R x is called symmetric if p∗ = p and SymR x denotes the set of symmetric polynomials. The degree of a word w ∈ x is the number of symbols composing it, denoted as |w| or deg(w), and the degree of a polynomial p = ∑w pww ∈ R x is the maximum degree of a word w with pw = 0. Given t ∈ N∪{∞}, we let x t be the set of words w of degree |w| ≤t, so that x ∞ = x , and R x t is the real vector space of noncommutative polynomials p of degree deg(p) ≤t. Given t ∈ N, we let x =t be the set of words of degree exactly equal to t.

For a set S ⊆ SymR x and t ∈ N∪{∞}, the truncated quadratic module at degree 2t associated to S is deﬁned as the cone generated by all polynomials p∗gp ∈ R x 2t with g ∈ S∪{1}:

M2t(S) = cone p∗gp : p ∈ R x , g ∈ S∪{1}, deg(p∗gp) ≤ 2t . (1)

Likewise, for a set T ⊆ R x , we can deﬁne the truncated ideal at degree 2t, denoted by I2t(T), as the vector space spanned by all polynomials ph ∈ R x 2t with h ∈ T:

I2t(T) = span ph : p ∈ R x , h ∈ T, deg(ph) ≤ 2t . (2) We say that M(S)+I (T) is Archimedean when there exists a scalar R > 0 such that

n

## ∑

xi2 ∈ M(S)+I (T). (3)

R−

i=1

Throughout we are interested in the space R x t ∗ of real-valued linear functionals on R x t. We list some basic deﬁnitions: A linear functional L ∈ R x t ∗ is symmetric if L(w) = L(w∗) for all w ∈ x t and tracial if L(ww ) = L(w w) for all w,w ∈ x t. A linear functional L ∈ R x ∗2t is said to be positive if L(p∗p) ≥ 0 for all p ∈ R x t. Many properties of a linear functional L ∈ R x ∗2t can be expressed as properties of its associated moment matrix (also known as its Hankel matrix). For L ∈ R x ∗2t we deﬁne its associated moment matrix, which has rows and columns indexed by words in x t, by

Mt(L)w,w = L(w∗w ) for w,w ∈ x t,

and as usual we set M(L) = M∞(L). It then follows that L is symmetric if and only if Mt(L) is symmetric, and L is positive if and only if Mt(L) is positive semideﬁnite. In fact, one can even express nonnegativity of a linear form L ∈ R x ∗2t on M2t(S) in terms of certain associated positive semideﬁnite moment matrices. For this, given a

polynomial g ∈ R x , deﬁne the linear form gL ∈ R x ∗

2t−deg(g) by (gL)(p) = L(gp). Then we have

L(p∗gp) ≥ 0 for all p ∈ R x t−dg ⇐⇒ Mt−dg(gL) 0, (dg = deg(g)/2 ),

and thus L ≥ 0 on M2t(S) if and only if Mt−dg(gL) 0 for all g ∈ S∪{1}. Also, the condition L = 0 on I2t(T) corresponds to linear equalities on the entries of Mt(L).

The moment matrix also allows us to deﬁne a property called ﬂatness. For t ∈ N,

a linear functional L ∈ R x ∗2t is called δ-ﬂat if the rank of Mt(L) is equal to that of its principal submatrix indexed by the words in x t−δ, that is,

rank(Mt(L)) = rank(Mt−δ(L)). (4)

We call L ﬂat if it is δ-ﬂat for some δ ≥ 1. When t = ∞, L is said to be ﬂat when rank(M(L)) < ∞, which is equivalent to rank(M(L)) = rank(Ms(L)) for some s ∈ N.

A key example of a ﬂat symmetric tracial positive linear functional on R x is given by the trace evaluation at a given matrix tuple X = (X1,...,Xn) ∈ (Hd)n:

##### p  → Tr(p(X)).

Here p(X) denotes the matrix obtained by substituting xi by Xi in p, and throughout Tr(·) denotes the usual matrix trace, which satisﬁes Tr(I) = d where I is the identity matrix in Hd. We mention in passing that we use tr(·) to denote the normalized matrix trace, which satisﬁes tr(I) = 1 for I ∈ Hd. Throughout, we use LX to denote the real part of the above functional, that is, LX denotes the linear form on R x deﬁned by

LX(p) = Re(Tr(p(X1,...,Xn))) for p ∈ R x . (5)

Observe that LX too is a symmetric tracial positive linear functional on R x . Moreover, LX is nonnegative on M(S) if the matrix tuple X is taken from the matrix positivity domain D(S) associated to the ﬁnite set S ⊆ SymR x , deﬁned as

X = (X1,...,Xn) ∈ (Hd)n : g(X) 0 for g ∈ S . (6)

##### D(S) =

d≥1

Similarly, the linear functional LX is zero on I (T) if the matrix tuple X is taken from the matrix variety V (T) associated to the ﬁnite set T ⊆ SymR x , deﬁned as

X ∈ (Hd)n : h(X) = 0 for all h ∈ T ,

##### V (T) =

d≥1

To discuss convergence properties of our lower bounds for matrix factorization ranks we will need to consider inﬁnite dimensional analogs of matrix algebras, namely C∗-algebras admitting a tracial state. Let us introduce some basic notions we need about C∗-algebras; see, e.g., [10] for details. For our purposes we deﬁne a C∗-algebra to be a norm closed ∗-subalgebra of the complex algebra B(H ) of bounded operators on a complex Hilbert space H . In particular, we have a∗a = a 2 for all elements a in the algebra. Such an algebra A is said to be unital if it contains the identity operator (denoted 1). For instance, any full complex matrix algebra Cd×d is a unital C∗-algebra. Moreover, by a fundamental result of Artin-Wedderburn, any

ﬁnite dimensional C∗-algebra (as a vector space) is ∗-isomorphic to a direct sum M m=1Cdm×dm of full complex matrix algebras [4,77]. In particular, any ﬁnite dimen-

sional C∗-algebra is unital.

An element b in a C∗-algebra A is called positive, denoted b 0, if it is of the form b = a∗a for some a ∈ A . For ﬁnite sets S ⊆ SymR x and T ⊆ R x , the C∗algebraic analogs of the matrix positivity domain and matrix variety are the sets

DA (S) = X = (X1,...,Xn) ∈ A n : Xi∗ = Xi for i ∈ [n], g(X) 0 for g ∈ S , VA (T) = X = (X1,...,Xn) ∈ A n : Xi∗ = Xi for i ∈ [n], h(X) = 0 for h ∈ T . A state τ on a unital C∗-algebra A is a linear form on A that is positive, i.e.,

τ(a∗a) ≥ 0 for all a ∈ A , and satisﬁes τ(1) = 1. Since A is a complex algebra, every state τ is Hermitian: τ(a) = τ(a∗) for all a ∈ A . We say that that a state is tracial if τ(ab) = τ(ba) for all a,b ∈ A and faithful if τ(a∗a) = 0 implies a = 0. A useful fact is that on a full matrix algebra Cd×d the normalized matrix trace is the unique tracial state (see, e.g., [16]). Now, given a tuple X = (X1,...,Xn) ∈ A n in a C∗-algebra A with tracial state τ, the second key example of a symmetric tracial positive linear functional on R x is given by the trace evaluation map, which we again denote by LX and is deﬁned by

LX(p) = τ(p(X1,...,Xn)) for all p ∈ R x .

- 1.4 Basic approach


To explain the basic idea of how we obtain lower bounds for matrix factorization ranks we consider the case of the completely positive semideﬁnite rank. Given a minimal factorization A = (Tr(Xi,Xj)), with d = cpsd-rankC(A) and X = (X1,...,Xn) in (Hd+)n, consider the linear form LX on R x as deﬁned in (5):

##### LX(p) = Re(Tr(p(X1,...,Xn))) for p ∈ R x .

Then we have A = (LX(xixj)) and cpsd-rankC(A) = d = LX(1). To obtain lower bounds on cpsd-rankC(A) we minimize L(1) over a set of linear functionals L that satisfy certain computationally tractable properties of LX. Note that this idea of minimizing L(1) has recently been used in the works [74,59] in the commutative setting to derive a hierarchy of lower bounds converging to the nuclear norm of a symmetric tensor.

The above linear functional LX is symmetric and tracial. Moreover it satisﬁes some positivity conditions, since we have LX(q) ≥ 0 whenever q(X) is positive semideﬁnite. It follows that LX(p∗p) ≥ 0 for all p ∈ R x and, as we explain later, LX satisﬁes the localizing conditions LX(p∗(√Aiixi −xi2)p) ≥ 0 for all p and i. Truncating the linear form yields the following hierarchy of lower bounds:

ξtcpsd(A) = min L(1) : L ∈ R x1,...,xn ∗2t tracial and symmetric, L(xixj) = Aij for i, j ∈ [n], L ≥ 0 on M2t { A11x1 −x12,..., Annxn −xn2} .

The bound ξtcpsd(A) is computationally tractable (for small t). Indeed, as was explained in Section 1.3, the localizing constraint “L ≥ 0 on M2t(S)” can be enforced by requiring certain matrices, whose entries are determined by L, to be positive semideﬁnite. This makes the problem deﬁning ξtcpsd(A) into a semideﬁnite program. The localizing conditions ensure the Archimedean property of the quadratic module, which permits to show certain convergence properties of the bounds ξtcpsd(A).

The above approach extends naturally to the other matrix factorization ranks, using the following two basic ideas. First, since the cp-rank and the nonnegative rank deal with factorizations by diagonal matrices, we use linear functionals acting on classical commutative polynomials. Second, the asymmetric factorization ranks (psdrank and nonnegative rank) can be seen as analogs of the symmetric ranks in the partial matrix setting, where we know only the values of L on the quadratic monomials corresponding to entries in the off-diagonal blocks (this will require scaling of the factors in order to be able to deﬁne localizing constraints ensuring the Archimedean property). A main advantage of our approach is that it applies to all four matrix factorization ranks, after easy suitable adaptations.

- 1.5 Connection to polynomial optimization


In classical polynomial optimization the problem is to ﬁnd the global minimum of a commutative polynomial f over a semialgebraic set of the form

##### D(S) = {x ∈ Rn : g(x) ≥ 0 for g ∈ S},

where S ⊆ R[x] = R[x1,...,xn] is a ﬁnite set of polynomials.1 Tracial polynomial optimization is a noncommutative analog, where the problem is to minimize the normalized trace tr(f(X)) of a symmetric polynomial f over a matrix positivity domain D(S) where S ⊆ SymR x is a ﬁnite set of symmetric polynomials.2 Notice that the distinguishing feature here is the dimension independence: the optimization is over all possible matrix sizes. Perhaps counterintuitively, in this paper we use techniques similar to those used for the tracial polynomial optimization problem to compute lower bounds on factorization dimensions.

For classical polynomial optimization Lasserre [46] and Parrilo [60] have proposed hierarchies of semideﬁnite programming relaxations based on the theory of moments and the dual theory of sums of squares polynomials. These can be used to compute successively better lower bounds converging to the global minimum (under the Archimedean condition). This approach has been used in a wide range of applications and there is an extensive literature (see, e.g., [1,47,49]). Most relevant to this work, it is used in [48] to design conic approximations of the completely positive cone and in [58] to check membership in the completely positive cone. This approach has also been extended to the noncommutative setting, ﬁrst to the eigenvalue optimization problem [61,57] (which will not play a role in this paper), and later to tracial optimization [15,43].

- 1 Here, and throughout the paper, we use [x] as the commutative analogue of x .
- 2 In fact, one could consider optimization over D(S)∩V (T) for some ﬁnite set T ⊆ R x , the results


below still hold in that setting, see Appendix A.

For our paper the moment formulation of the lower bounds is most relevant: For all t ∈ N∪{∞} we can deﬁne the bounds

ft = inf L(f) : L ∈ R[x]∗2t, L(1) = 1, L ≥ 0 on M2t(S) ,

fttr = inf L(f) : L ∈ R x ∗2t tracial and symmetric, L(1) = 1, L ≥ 0 on M2t(S) , where ft (resp., fttr) lower bounds the (tracial) polynomial optimization problem.

The connection between the parameters ξtcpsd(A) and fttr is now clear: in the former we do not have the normalization property “L(1) = 1” but we do have the additional afﬁne constraints “L(xixj) = Aij”. This close relation to (tracial) polynomial optimization allows us to use that theory to understand the convergence properties of our bounds. Since throughout the paper we use (proof) techniques from (tracial) polynomial optimization, we will state the main convergence results we need, with full proofs, in Appendix A. Moreover, we give all proofs from the “moment side”, which is most relevant to our treatment. Below we give a short summary of the convergence results for the hierarchies {ft} and {fttr} that are relevant to our paper. We refer to Appendix A.3 for details.

Under the condition that M(S) is Archimedean we have asymptotic convergence: ft → f∞ and fttr → f∞tr as t → ∞. In the commutative setting one can moreover show that f∞ is equal to the global minimum of f over the set D(S). However, in the noncommutative setting, the parameter f∞tr is in general not equal to the minimum of tr(f(X)) over X ∈ D(S). Instead we need to consider the C∗-algebraic version of the tracial polynomial optimization problem: one can show that

f∞tr = inf τ(f(X)) : X ∈ DA (S), A is a unital C∗-algebra with tracial state τ . An important additional convergence result holds under ﬂatness. If the program deﬁning the bound ft (resp., fttr) admits a sufﬁciently ﬂat optimal solution, then equality holds: ft = f∞ (resp., fttr = f∞tr). Moreover, in this case, the parameter fttr is equal to the minimum value of tr(f(X)) over the matrix positivity domain D(S).

#### 2 Lower bounds on the completely positive semideﬁnite rank

Let A be a completely positive semideﬁnite n×n matrix. For t ∈ N∪{∞} we consider the following semideﬁnite program, which, as we see below, lower bounds the complex completely positive semideﬁnite rank of A:

ξtcpsd(A) = min L(1) : L ∈ R x1,...,xn ∗2t tracial and symmetric, L(xixj) = Aij for i, j ∈ [n], L ≥ 0 on M2t(SAcpsd) ,

where we set

SAcpsd = A11x1 −x12,..., Annxn −xn2 . (7)

Additionally, deﬁne the parameter ξ∗cpsd(A), obtained by adding the rank constraint rank(M(L)) < ∞ to the program deﬁning ξ∞cpsd(A), where we consider the inﬁmum instead of the minimum since we do not know whether the inﬁmum is always attained.

(In Proposition 1 we show the inﬁmum is attained in ξtcpsd(A) for t ∈ N∪{∞}). This gives a hierarchy of monotone nondecreasing lower bounds on the completely positive semideﬁnite rank:

ξ1cpsd(A) ≤ ... ≤ ξtcpsd(A) ≤ ... ≤ ξ∞cpsd(A) ≤ ξ∗cpsd(A) ≤ cpsd-rankC(A).

The inequality ξ∞cpsd(A) ≤ ξ∗cpsd(A) is clear and monotonicity as well: If L is feasible for ξkcpsd(A) with t ≤ k ≤ ∞, then its restriction to R x 2t is feasible for ξtcpsd(A).

The following notion of localizing polynomials will be useful. A set S ⊆ R x is said to be localizing at a matrix tuple X if X ∈ D(S) (i.e., g(X) 0 for all g ∈ S) and we say that S is localizing for A if S is localizing at some factorization X ∈ (Hd+)n of A with d = cpsd-rankC(A). The set SAcpsd as deﬁned in (7) is localizing for A, and, in fact, it is localizing at any factorization X of A by Hermitian positive semideﬁnite matrices. Indeed, since

Aii = Tr(Xi2) ≥ λmax(Xi2) = λmax(Xi)2 we have √AiiXi −Xi2 0 for all i ∈ [n].

We can now use this to show the inequality ξ∗cpsd(A) ≤ cpsd-rankC(A). For this set d = cpsd-rankC(A), let X ∈ (Hd+)n be a Gram factorization of A, and consider the linear form LX ∈ R x ∗ deﬁned by

LX(p) = Re(Tr(p(X))) for all p ∈ R x .

By construction LX is symmetric and tracial, and we have A = (L(xixj)). Moreover, since the set of polynomials SAcpsd is localizing for A, the linear form LX is nonnegative on M(SAcpsd). Finally, we have rank(M(LX)) < ∞, since the algebra generated by X1,...,Xn is ﬁnite dimensional. Hence, LX is feasible for ξ∗cpsd(A) with LX(1) = d, which shows ξ∗cpsd(A) ≤ cpsd-rankC(A).

The inclusions in (8) below show the quadratic module M(SAcpsd) is Archimedean (recall the deﬁnition in (3)). Moreover, although there are other possible choices for the localizing polynomials to use in SAcpsd, these inclusions also show that the choice made in (7) leads to the largest truncated quadratic module and thus to the best bound. For any scalar c > 0, we have the inclusions

M2t(x,c−x) ⊆ M2t(x,c2 −x2) ⊆ M2t(cx−x2) ⊆ M2t+2(x,c−x), (8) which hold in light of the following identities:

c−x = (c−x)2 +c2 −x2 /(2c), (9) c2 −x2 = (c−x)2 +2(cx−x2), (10) cx−x2 = (c−x)x(c−x)+x(c−x)x /c, (11)

x = (cx−x2)+x2 /c. (12)

In the rest of this section we investigate properties of the hierarchy {ξtcpsd(A)} as well as some variations on it. We discuss convergence properties, asymptotically and under ﬂatness, and we give another formulation for the parameter ξ∗cpsd(A). Moreover, as the inequality ξ∗cpsd(A) ≤ cpsd-rankC(A) is typically strict, we present an

approach to strengthen the bounds in order to go beyond ξ∗cpsd(A). Then we propose some techniques to simplify the computation of the bounds, and we illustrate the behaviour of the bounds on some examples.

- 2.1 The parameters ξ∞cpsd(A) and ξ∗cpsd(A)


In this section we consider convergence properties of the hierarchy ξtcpsd(·), both asymptotically and under ﬂatness. We also give equivalent reformulations of the lim-

iting parameters ξ∞cpsd(A) and ξ∗cpsd(A) in terms of C∗-algebras with a tracial state, which we will use in Sections 2.3-2.4 to show properties of these parameters.

- Proposition 1 Let A ∈ CSn+. For t ∈ N∪{∞} the optimum in ξtcpsd(A) is attained, and

lim

t→∞

ξtcpsd(A) = ξ∞cpsd(A).

Moreover, ξ∞cpsd(A) is equal to the smallest scalar α ≥ 0 for which there exists a unital C∗-algebra A with tracial state τ and (X1,...,Xn) ∈ DA (SAcpsd) such that A = α ·(τ(XiXj)).

Proof The sequence (ξtcpsd(A))t is monotonically nondecreasing and upper bounded by ξ∞cpsd(A) < ∞, which implies its limit exists and is at most ξ∞cpsd(A).

As ξtcpsd(A) ≤ ξ∞cpsd(A), we may add the redundant constraint L(1) ≤ ξ∞cpsd(A) to the problem ξtcpsd(A) for every t ∈ N. By (10) we have Tr(A)−∑ixi2 ∈ M2(SAcpsd). Hence, using the result of Lemma 13, the feasible region of ξtcpsd(A) is compact, and thus it has an optimal solution Lt. Again by Lemma 13, the sequence (Lt) has a pointwise converging subsequence with limit L ∈ R x ∗. This pointwise limit L is

symmetric, tracial, satisﬁes (L(xixj)) = A, and is nonnegative on M(SAcpsd). Hence L is feasible for ξ∞cpsd(A). This implies that L is optimal for ξ∞cpsd(A) and we have

limt→∞ξtcpsd(A) = ξ∞cpsd(A).

The reformulation of ξ∞cpsd(A) in terms of C∗-algebras with a tracial state follows directly using Theorem 1.

Next we give some equivalent reformulations for the parameter ξ∗cpsd(A), which follow as a direct application of Theorem 2. In general we do not know whether the inﬁmum in ξ∗cpsd(A) is attained. However, as a direct application of Corollary 1, we see that this inﬁmum is attained if there is an integer t ∈ N for which ξtcpsd(A) admits a ﬂat optimal solution.

- Proposition 2 Let A ∈ CSn+. The parameter ξ∗cpsd(A) is given by the inﬁmum of L(1) taken over all conic combinations L of trace evaluations at elements in DA (SAcpsd) for which A = (L(xixj)). The parameter ξ∗cpsd(A) is also equal to the inﬁmum over all α ≥ 0 for which there exist a ﬁnite dimensional C∗-algebra A with tracial state τ and (X1,...,Xn) ∈ DA (SAcpsd) such that A = α ·(τ(XiXj)).


In addition, if ξtcpsd(A) admits a ﬂat optimal solution, then ξtcpsd(A) = ξ∗cpsd(A).

Next we show a formulation for ξ∗cpsd(A) in terms of factorization by blockdiagonal matrices, which helps explain why the inequality ξ∗cpsd(A) ≤ cpsd-rankC(A) is typically strict. Here  ·  is the operator norm, so that X = λmax(X) for X 0.

- Proposition 3 For A ∈ CSn+ we have


M

Xim 2 Aii

## ∑

ξ∗cpsd(A) = inf

dm ·max i∈[n]

: M ∈ N, d1,...,dM ∈ N, (13) Xim ∈ Hd+m for i ∈ [n],m ∈ [M], A = Gram ⊕Mm=1 X1m,...,⊕Mm=1Xnm .

m=1

Note that using matrices from Sd+m instead of Hd+m does not change the optimal value. Proof The proof uses the formulation of ξ∗cpsd(A) in terms of conic combinations of trace evaluations at matrix tuples in D(SAcpsd) as given in Proposition 2. We ﬁrst show the inequality β ≤ ξ∗cpsd(A), where β denotes the optimal value of the program in (13).

For this, assume L ∈ R x ∗ is a conic combination of trace evaluations at elements

of D(SAcpsd) such that A = (L(xixj)). We will construct a feasible solution for (13) with objective value L(1). The linear functional L can be written as

M

## ∑

λmLYm, where λm > 0 and Ym = (Y1m,...,Ynm) ∈ D(SAcpsd) for m ∈ [M].

L =

m=1

Let dm denote the size of the matrices Y1m,...,Ynm, so that L(1) = ∑mλmdm. Since Ym ∈ D(SAcpsd), we have Yim 0 and AiiI − (Yim)2 0 by identities (10) and (12). This implies Yim 2 ≤ Aii for all i ∈ [n] and m ∈ [M]. Deﬁne Xm = √λmYm. Then, L(xixj) = ∑mTr(XimXjm), so that the matrices ⊕mX1m,...,⊕mXnm form a Gram decomposition of A. This gives a feasible solution to (13) with value

M

M

Xim 2 Aii

Yim 2 Aii ≤

## ∑

## ∑

dmλmmax i∈[n]

dm ·max i∈[n]

=

m=1

m=1

which shows β ≤ L(1), and hence β ≤ ξ∗cpsd(A). For the other direction we assume

M

## ∑

dmλm = L(1),

m=1

A = Gram ⊕Mm=1 X1m,...,⊕Mm=1Xnm , X1m,...,Xnm ∈ Sd+m for m ∈ [M]. Set λm = maxi∈[n] Xim 2/Aii, and deﬁne the linear form L by

M

## ∑

λmLYm, where Ym = Xm/ λm for all m ∈ [M].

L =

m=1

We have L(1) = ∑mλmdm and A = (L(xixj)), and thus it sufﬁces to show that each matrix tuple Ym belongs to D(SAcpsd). For this we observe that λmAii ≥  Xim 2. Therefore λmAiiI (Xim)2, and thus AiiI (Yim)2, which implies √AiiYim−(Yim)2 0. This shows ξ∗cpsd(A) ≤ L(1) = ∑mλmdm, and thus ξ∗cpsd(A) ≤ β.

We can say a bit more when the matrix A lies on an extreme ray of the cone CSn+. In the formulation from Proposition 3 it sufﬁces to restrict the minimization over factorizations of A involving only one block. However, we know very little about the extreme rays of CSn+, also in view of the recent result that the cone is not closed for large n [73,23].

- Proposition 4 If A lies on an extreme ray of the cone CSn+, then


Xi 2 Aii

ξ∗cpsd(A) = inf d ·max i∈[n]

: d ∈ N,X1,...,Xn ∈ Hd+, A = Gram X1,...,Xn .

Moreover, if ⊕Mm=1X1m,...,⊕Mm=1Xnm is a Gram decomposition of A providing an optimal solution to (13) and some block Xim has rank 1, then ξ∗cpsd(A) = cpsd-rankC(A).

Proof Let β be the inﬁmum in Proposition 4. The inequality ξ∗cpsd(A) ≤ β follows from the reformulation of ξ∗cpsd(A) in Proposition 3. To show the reverse inequality we consider a solution ⊕Mm=1X1m,...,⊕Mm=1Xnm to (13), and set λm = maxi Xim 2/Aii. We will show β ≤ ∑mdmλm. For this deﬁne the matrices Am = Gram(X1m,··· ,Xnm), so that A = ∑mAm. As A lies on an extreme ray of CSn+, we must have Am = αmA for some αm > 0 with ∑mαm = 1. Hence, since

A = Am/αm = Gram(X1m/√αm,··· ,Xnm/√αm),

we have β ≤ dmλm/αm for all m ∈ [M]. It sufﬁces now to use ∑mαm = 1 to see that minmdmλm/αm ≤ ∑mdmλm. So we have shown β ≤ minmdmλm/αm ≤ ∑mdmλm. This implies β ≤ ξ∗cpsd(A), and thus equality holds.

Assume now that ⊕Mm=1X1m,...,⊕Mm=1Xnm is optimal to (13) and that there is a block Xim of rank 1. By Proposition 3 we have ∑mdmλm = ξ∗cpsd(A). From the argument just made above it follows that

ξ∗cpsd(A)=minmdmλm/αm =∑

dmλm.

m

As ∑mαm = 1 this implies dmλm/αm = minmdmλm/αm for all m; that is, all terms dmλm/αm take the same value ξ∗cpsd(A). By assumption there exist some m ∈ [M] and i ∈ [n] for which Xim has rank 1. Then Xim 2 = Xim,Xim , which gives λm = αm, and thus ξ∗cpsd(A) = dm. On the other hand, cpsd-rankC(A) ≤ dm since (Xim/√αm)i forms a Gram decomposition of A, so equality ξ∗cpsd(A) = dm = cpsd-rankC(A) holds.

- 2.2 Additional localizing constraints to improve on ξ∗cpsd(A)


In order to strengthen the bounds we may require nonnegativity over a (truncated) quadratic module generated by a larger set of localizing polynomials for A. The following lemma gives one such approach.

- Lemma 1 Let A ∈ CSn+. For v ∈ Rn and gv = vTAv − ∑ni=1vixi 2, the set {gv} is localizing for every Gram factorization by Hermitian positive semideﬁnite matrices of A (in particular, {gv} is localizing for A).


Proof If X1,...,Xn is a Gram decomposition of A by Hermitian positive semideﬁnite matrices, then

n

n

2

2

## ∑

## ∑

≥ λmax

vTAv = Tr

viXi

viXi

##### ,

i=1

i=1

hence vTAvI −(∑ni=1viXi)2 0. Given a set V ⊆ Rn, we consider the larger set

SAcpsd,V = SAcpsd ∪{gv : v ∈ V}

of localizing polynomials for A. For t ∈ N∪{∞,∗}, denote by ξtcpsd,V (A) the parameter obtained by replacing in ξtcpsd(A) the nonnegativity constraint on M2t(SAcpsd) by nonnegativity on the larger set M2t(SAcpsd,V ). We have ξtcpsd,0/ (A) = ξtcpsd(A) and

ξtcpsd(A) ≤ ξtcpsd,V (A) ≤ cpsd-rankC(A) for all V ⊆ Rn.

By scaling invariance, we can add the above constraints for all v ∈ Rn by setting V to be the unit sphere Sn−1. Since Sn−1 is a compact metric space, there exists a sequence V1 ⊆ V2 ⊆ ... ⊆ Sn−1 of ﬁnite subsets such that k≥1Vk is dense in Sn−1. Each of the parameters ξtcpsd,Vk (A) involves ﬁnitely many localizing constraints, and, as we now show, they converge to the parameter ξtcpsd,Sn−1(A).

- Proposition 5 Consider a matrix A ∈ CSn+. For t ∈ {∞,∗}, we have


ξtcpsd,Vk (A) = ξtcpsd,Sn−1(A).

lim

k→∞

Proof Let ε > 0. Since kVk is dense in Sn−1, there is an integer k ≥ 1 so that for every u ∈ Sn−1 there exists a vector v ∈ Vk satisfying

ελmin(A) 4√nmaxiAii

ελmin(A) 4Tr(A2)1/2

u−v 1 ≤

and u−v 2 ≤

. (14)

The above Propositions 1 and 2 have natural analogues for the programs ξtcpsd,V (A). These show that for t = ∞ (t = ∗) the parameter ξtcpsd,Vk (A) is the inﬁmum over all α ≥ 0 for which there exist a (ﬁnite dimensional) unital C∗-algebra A with tracial state τ and X ∈ DA (SAcpsd,V

) such that A = α ·(τ(XiXj)).

k

Below we will show that X = √1−εX ∈ DA (SAcpsd,Sn−1). This implies that the

linear form L ∈ R x ∗ deﬁned by L(p) = α/(1−ε)τ(p(X )) is feasible for ξtcpsd,Sn−1(A) with objective value L(1) = α/(1−ε). This shows

1 1−ε

1 1−ε

ξtcpsd,Vk (A). Since ε > 0 was arbitrary, letting ε tend to 0 completes the proof.

ξtcpsd,Sn−1(A) ≤

ξtcpsd,Vk (A) ≤

lim

k→∞

We now show X = √1−εX ∈ DA (SAcpsd,Sn−1). For this consider the map

n

2

## ∑

fX: Sn−1 → R, v  →

viXi

##### ,

i=1

where  ·  denotes the C∗-algebra norm of A . For α ∈ R and a ∈ A with a∗ = a, we have α ≥ a if and only if α −a 0 in A , or, equivalently, α2 −a2 0 in A .

Since X ∈ DA (SAcpsd,V

) we have vTAv− fX(v) ≥ 0 for all v ∈ Vk, and hence

k

fX(v) vTAv ≥ vTAv 1−(1−ε) = εvTAv ≥ ελmin(A).

vTAv− fX (v) = vTAv 1−(1−ε)

Let u ∈ Sn−1 and let v ∈ Vk be such that (14) holds. Using Cauchy-Schwarz we have

|uTAu−vTAv| = |(u−v)TA(u+v)| = | A,(u−v)(u+v)T | ≤ Tr(A2) Tr((u+v)(u−v)T(u−v)(u+v)T) ≤ Tr(A2) u−v 2 u+v 2 ≤ 2 Tr(A2) u−v 2 ≤ 2 Tr(A2)

ελmin(A) 2

ελmin(A) 4 Tr(A2)

##### .

=

Since √AiiXi −Xi2 is positive in A , we have that √Aii −Xi is positive in A by (9) and (10), which implies Xi  ≤

√Aii. By the reverse triangle inequality we then have

n

n

n

n

## ∑

## ∑

## ∑

## ∑

viX i

uiX i +

viX i

uiX i −

|fX (u)− fX (v)| =

i=1

i=1

i=1

i=1

n

(vi −ui)X i 2√nmaxi Aii

## ∑

≤

i=1

n

|vi −ui| X i 2√nmaxi Aii

## ∑

≤

i=1

ελmin(A) 4√nmaxiAii

ελmin(A) 2

≤ u−v 12√nmaxiAii ≤

2√nmaxiAii =

##### .

Combining the above inequalities we obtain that uTAu− fX (u) ≥ 0 for all Sn−1, and hence uTAu− ∑ni=1uiX i 2 is positive in A . Thus we have X ∈ DA (SAcpsd,Sn−1).

We now discuss two examples where the bounds ξ∗cpsd,V (A) go beyond ξ∗cpsd(A).

- Example 1 Consider the matrix


A =

1 1/2 1/2 1

= Gram

1 0 0 0

,

1/2 1/2 1/2 1/2

, (15)

with cpsd-rankC(A) = 2. We can also write A = Gram(Y1,Y2), where

#####  

#####  , Y2 =

#####  

 .

1 0 0 0 1 0 0 0 0

1 0 0

1 √2

1 √2

- 0 0 0
- 0 0 1


Y1 =

With Xi = √2 Yi we have I −Xi2 0 for i = 1,2. Hence the linear form L = LX/2 is feasible for ξ∗cpsd(A), which shows that ξ∗cpsd(A) ≤ L(1) = 3/2. In fact, this form

L gives an optimal ﬂat solution to ξ2cpsd(A), as we can check using a semideﬁnite programming solver, so ξ∗cpsd(A) = 3/2. In passing, we observe that ξ1cpsd(A) = 4/3, which coincides with the analytic lower bound (18) (see also Lemma 6 below).

For e = (1,1) ∈ R2 and V = {e}, this form L is not feasible for ξ∗cpsd,V (A), because for the polynomial p = 1−3x1−3x2 we have L(p∗gep) = −9/2 < 0. This means that the localizing constraint L(p∗gep) ≥ 0 is not redundant: For t ≥ 2 it cuts off part of the feasibility region of ξtcpsd(A). Indeed, using a semideﬁnite programming solver we ﬁnd an optimal ﬂat solution of ξ3cpsd,V (A) with objective value (5−

√3)/2 ≈ 1.633, hence

##### √3)/2 > 3/2 = ξ∗cpsd(A).

ξ∗cpsd,V (A) = (5−

- Example 2 Consider the symmetric circulant matrices






1 α 0 0 α α 1 α 0 0 0 α 1 α 0 0 0 α 1 α α 0 0 α 1

for α ∈ R.

M(α) =

 

 

For 0 ≤ α ≤ 1/2 we have M(α) ∈ CS5+ with cpsd-rankC(M(α)) ≤ 5. To see this we set β = (1+

√1−4α2)/2 and observe that the matrices

Xi = Diag( β ei + 1−β ei+1) ∈ S5+, i ∈ [5], (with e6 := e1),

form a factorization of M(α). As M(α) is supported by a cycle, we have M(α) ∈ CS5+ if and only if M(α) ∈ CP5 [50]. Thus M(α) ∈ CS5+ if and only if 0 ≤ α ≤ 1/2.

By using its formulation in Proposition 3, we can use the above factorization to

derive the inequality ξ∗cpsd(M(1/2)) ≤ 5/2. However, using a semideﬁnite programming solver we see that

ξ2cpsd,V (M(1/2)) = 5,

where V is the set containing the vector (1,−1,1,−1,1) and its cyclic shifts. Hence the bound ξ2cpsd,V (M(1/2)) is tight: It certiﬁes cpsd-rankC(M(1/2)) = 5, while the other known bounds, the rank bound rank(A) and the analytic bound (18), only give cpsd-rankC(A) ≥ 3.

We now observe that there exist 0 < ε,δ < 1/2 such that cpsd-rankC(M(α)) = 5 for all α ∈ [0,ε]∪[δ,1/2]. Indeed, this follows from the fact that ξ1cpsd(M(0)) = 5 (by Lemma 6), the above result that ξ2cpsd,V (M(1/2)) = 5, and the lower semicontinuity of α  → ξ2cpsd,V (M(α)), which is shown in Lemma 7 below.

As the matrices M(α) are nonsingular, the above factorization shows that their cp-rank is equal to 5 for all α ∈ [0,1/2]; whether they all have cpsd-rank equal to 5 is not known.

- 2.3 Boosting the bounds


In this section we propose some additional constraints that can be added to strengthen the bounds ξtcpsd,V (A) for ﬁnite t. These constraints may shrink the feasibility region of ξtcpsd,V (A) for t ∈ N, but they are redundant for t ∈ {∞,∗}. The latter is shown using the reformulation of the parameters ξ∞cpsd,V (A) and ξ∗cpsd,V (A) in terms of C∗-algebras.

We ﬁrst mention how to construct localizing constraints of “bilinear type”, inspired by the work of Berta, Fawzi and Scholz [8]. Note that as for localizing constraints, these bilinear constraints can be modeled as semideﬁnite constraints.

- Lemma 2 Let A ∈ CSn+, t ∈ N∪{∞,∗}, and let {g,g } be localizing for A. If we add the constraints

L(p∗gpg ) ≥ 0 for p ∈ R x with deg(p∗gpg ) ≤ 2t (16)

to ξtcpsd,V (A), then we still get a lower bound on cpsd-rankC(A). However, the constraints (16) are redundant for ξ∞cpsd,V (A) and ξ∗cpsd,V (A) when g,g ∈ M(SAcpsd,V ).

Proof Let X ∈ (Hd+)n be a Gram decomposition of A, and let L = LX be the real part of the trace evaluation at X. Then, p(X)∗g(X)p(X) 0 and g (X) 0, and thus

L(p∗gpg ) = Re(Tr(p(X)∗g(X)p(X)g (X))) ≥ 0. So by adding the constraints (16) we still get a lower bound on cpsd-rankC(A).

To show that the constraints (16) are redundant for ξtcpsd,V (A) and ξ∗cpsd,V (A) when g,g ∈ M(SAcpsd,V ), we let t ∈ {∞,∗} and assume L is feasible for ξtcpsd,V (A). By Theorem 1 there exist a unital C∗-algebra A with tracial state τ and X ∈ D(SAcpsd,V ) such that L(p) = L(1)τ(p(X)) for all p ∈ R x . Since g,g ∈ M(SAcpsd,V ) we know that g(X),g (X) are positive elements in A , so g(X) = a∗a and g (X) = b∗b for some a,b ∈ A . Then we have

L(p∗gpg) = L(1)τ(p∗(X)g(X) p(X)g (X))

= L(1)τ(p∗(X)a∗a p(X)b∗b)

= L(1)τ((a p(X)b∗)∗a p(X)b∗) ≥ 0, where we use that τ is a positive tracial state on A .

Second, we show how to use zero entries in A and vectors in the kernel of A to enforce new constraints on ξtcpsd,V (A).

- Lemma 3 Let A ∈ CSn+ and t ∈ N∪{∞,∗}. If we add the constraint


n

## ∑

vixi : v ∈ kerA ∪ xixj : Aij = 0 (17)

L = 0 on I2t

i=1

to ξtcpsd,V (A), then we still get a lower bound on cpsd-rankC(A). Moreover, these constraints are redundant for ξ∞cpsd,V (A) and ξ∗cpsd,V (A).

Proof Let X ∈ (Hd+)n be a Gram factorization of A and let LX be as in (5). If Av = 0, then 0 = vTAv = Tr((∑ni=1viXi)2) and thus ∑ni=1viXi = 0. Hence LX((∑nI=1vixi)p) = Re(Tr((∑ni=1viXi)p(X))) = 0. If Aij = 0, then Tr(XiXj) = 0, which implies XiXj = 0, since Xi and Xj are positive semideﬁnite. Hence LX(xixip) = Re(Tr(XiXjp(X))) = 0. Therefore, adding the constraints (17) still lower bounds cpsd-rankC(A).

As in the proof of the previous lemma, if t ∈ {∞,∗} and L is feasible for ξtcpsd,V (A) then, by Theorem 1, there exist a unital C∗-algebra A with tracial state τ and X in D(SAcpsd,V ) such that L(p) = L(1)τ(p(X)) for all p ∈ R x . Moreover, by Lemma 12 we may assume τ to be faithful. For a vector v in the kernel of A we have 0 = vTAv = L((∑ivixi)2) = L(1)τ((∑iviXi)2), and hence, since τ is faithful, ∑iviXi = 0 in A . It follows that L(p(∑ivixi)) = L(1)τ(p(X)0) = 0 for all p ∈ R x . Analogously, if Aij = 0, then L(xixj) = 0 implies τ(XiXj) = 0 and thus XiXj = 0, since Xi,Xj are positive in A and τ is faithful. This implies L(pxixj) = 0 for all p ∈ R x . This shows that the constraints (17) are redundant.

Note that the constraints L(p(∑ni=1vixi))=0 for p∈R x t, which are implied by (17), are in fact redundant: if v ∈ ker(A), then the vector obtained by extending v with ze-

ros belongs to ker(Mt(L)), since Mt(L) 0. Also, for an implementation of ξtcpsd(A) with the additional constraints (17), it is more efﬁcient to index the moment matrices

with a basis for R x t modulo the ideal It {∑ivixi : v ∈ ker(A)}∪{xixj : Aij = 0} .

- 2.4 Additional properties of the bounds


Here we list some additional properties of the parameters ξtcpsd(A) for t ∈ N∪{∞,∗}. First we state some properties for which the proofs are immediate and thus omitted.

- Lemma 4 Suppose A ∈ CSn+ and t ∈ N∪{∞,∗}.

- (1) If P is a permutation matrix, then ξtcpsd(A) = ξtcpsd(PTAP).
- (2) If B is a principal submatrix of A, then ξtcpsd(B) ≤ ξtcpsd(A).
- (3) If D is a positive deﬁnite diagonal matrix, then ξtcpsd(A) = ξtcpsd(DAD).


We also have the following direct sum property, where the equality follows using the C∗-algebra reformulations as given in Proposition 1 and Proposition 2.

- Lemma 5 If A ∈ CSn+ and B ∈ CSm+, then ξtcpsd(A⊕B) ≤ ξtcpsd(A)+ξtcpsd(B), where equality holds for t ∈ {∞,∗}.


Proof To prove the inequality we take LA and LB feasible for ξtcpsd(A) and ξtcpsd(B), and construct a feasible L for ξtcpsd(A⊕B) by L(p(x,y)) = LA(p(x,0))+LB(p(0,y)).

Now we show equality for t = ∞ (t = ∗). By Proposition 1 (Proposition 2), ξtcpsd(A⊕B) is equal to the inﬁmum over all α ≥ 0 for which there exists a (ﬁnite dimensional) unitalC∗-algebra A with tracial state τ and (X,Y) ∈ DA (SAcpsd⊕B) such that A = α ·(τ(XiXj)), B = α ·(τ(YiYj)) and (τ(XiYj)) = 0. This implies X ∈ DA (SAcpsd) and Y ∈ DA (SBcpsd). Let PA be the projection onto the space ∑iIm(Xi) and deﬁne the

linear form LA ∈ R x ∗ by LA(p) = α ·τ(p(X)PA). It follows that LA is is nonnegative on M(SAcpsd), and

LA(xixj) = α τ(xixjPA) = α τ(xixj) = Aij,

so LA is feasible for ξ∞cpsd(A) with LA(1) = ατ(PA). In the same way we consider the projection PB onto the space ∑j Im(Yj) and deﬁne a feasible solution LB for ξtcpsd(B) with LB(1)=ατ(PB). By Lemma 12 we may assume τ to be faithful, so that positivity of Xi and Yj together with τ(XiYj) = 0 implies XiYj = 0 for all i and j, and thus ∑iIm(Xi) ⊥ ∑j Im(Yj). This implies I PA +PB and thus τ(PA +PB) ≤ τ(1) = 1. We have

LA(1)+LB(1) = α τ(PA)+ατ(PB) ≤ α τ(1) = α, so ξtcpsd(A)+ξtcpsd(B) ≤ LA(1)+LB(1) ≤ α, completing the proof.

Note that the cpsd-rank of a matrix satisﬁes the same properties as those mentioned in the above two lemmas, where the inequality in Lemma 5 is always an equality: cpsd-rankC(A ⊕ B) = cpsd-rankC(A)+cpsd-rankC(B) [62,39].

The following lemma shows that the ﬁrst level of our hierarchy is at least as good as the analytic lower bound (18) on the cpsd-rank derived in [62, Theorem 10].

- Lemma 6 For any non-zero matrix A ∈ CSn+ we have


∑ni=1√Aii 2 ∑ni,j=1Aij

ξ1cpsd(A) ≥

. (18)

- Proof Let L be feasible for ξ1cpsd(A). Since L is nonnegative on M2(SAcpsd), it follows


√Aii. Moreover, the matrix M1(L) is positive semideﬁnite. By taking the Schur complement with respect to its upper left corner (indexed by 1) it follows that the matrix L(1)·A−(L(xi)L(xj)) is positive semideﬁnite. Hence the sum of its entries is nonnegative, which gives L(1)(∑i,j Aij) ≥ (∑iL(xi))2 ≥ (∑i√Aii)2 and shows the desired inequality.

that L(√Aiixi − xi2) ≥ 0, implying √AiiL(xi) ≥ L(xi2) = Aii and thus L(xi) ≥

As an application of Lemma 6, the ﬁrst bound ξ1cpsd is exact for the k × k identity matrix: ξ1cpsd(Ik) = cpsd-rankC(Ik) = k. Moreover, by combining this with Lemma 4, it follows that ξ1cpsd(A) ≥ k if A contains a diagonal positive deﬁnite k×k principal submatrix. A slightly more involved example is given by the 5×5 circulant matrix A whose entries are given by Aij = cos((i− j)4π/5)2 (i, j ∈ [5]); this matrix was used in [26] to show a separation between the completely positive semideﬁnite cone and the completely positive cone, and it was shown that cpsd-rankC(A) = 2. The analytic lower bound of [62] also evaluates to 2, hence Lemma 6 shows that our bound is tight on this example.

We now examine further analytic properties of the parameters ξtcpsd(·). For each r ∈ N, the set of matrices A ∈ CSn+ with cpsd-rankC(A) ≤ r is closed, which shows that the function A  → cpsd-rankC(A) is lower semicontinuous. We now show that the functions A  → ξtcpsd(A) have the same property. The other bounds deﬁned in this paper are also lower semicontinuous, with a similar proof.

- Lemma 7 For every t ∈ N∪{∞} and V ⊆ Rn, the function

Sn → R∪{∞}, A  → ξtcpsd,V (A) is lower semicontinuous.

Proof It sufﬁces to show the result for t ∈ N, because ξ∞cpsd,V (A) = supt ξtcpsd,V (A), and the pointwise supremum of lower semicontinuous functions is lower semicontinuous.

We show that the level sets {A ∈ Sn : ξtcpsd,V (A) ≤ r} are closed. For this we consider a sequence (Ak)k∈N in Sn converging to A ∈ Sn such that ξtcpsd,V (Ak) ≤ r for all k. We show that ξtcpsd,V (A) ≤ r. Let Lk ∈ R x ∗2t be an optimal solution to ξtcpsd,V (Ak). As Lk(1) ≤ r for all k, it follows from Lemma 13 that there is a pointwise converging subsequence of (Lk)k, still denoted (Lk)k for simplicity, that has a limit L ∈ R x ∗2t with L(1) ≤ r. To complete the proof we show that L is feasible for ξtcpsd,V (A). By the pointwise convergence of Lk to L, for every ε > 0, p ∈ R x , and i ∈ [n], there exists a K ∈ N such that for all k ≥ K we have

|L(p∗xip)−Lk(p∗xip)| < min{1,

ε

√Aii }, |L(p∗xi2p)−Lk(p∗xi2p)| < ε, | Aii − (Ak)ii| <

ε L(p∗xip)+1

. Hence we have

L(p∗( Aiixi −xi2)p) = Aii L(p∗xip)−Lk(p∗xip)+Lk(p∗xip)

− L(p∗xi2p)−Lk(p∗xi2p)+Lk(p∗xi2p)

- ≥ −2ε + AiiLk(p∗xip)−Lk(p∗xi2p)

- ≥ −3ε + (Ak)iiLk(p∗xip)−Lk(p∗xi2p)


= −3ε +Lk(p∗( (Ak)iixi −xi2)p) ≥ −3ε,

where in the second inequality we use that 0 ≤ Lk(p∗xip) ≤ L(p∗xip) + 1. Letting ε → 0 gives L(p∗(√Aiixi −xi2)p) ≥ 0.

Similarly one can show L(p∗(vTAv−(∑ivixi)2)p) ≥ 0 for v ∈ V, p ∈ R x .

If we restrict to completely positive semideﬁnite matrices with an all-ones diagonal, that is, to CSn+ ∩En, we can show an even stronger property. Here En is the elliptope, which is the set of n×n positive semideﬁnite matrices with an all-ones diagonal.

- Lemma 8 For every t ∈ N∪{∞}, the function


CSn+ ∩En → R, A  → ξtcpsd(A) is convex, and hence continuous on the interior of its domain.

Proof Let A,B ∈ CSn+ ∩ En and 0 < λ < 1. Let LA and LB be optimal solutions for ξtcpsd(A) and ξtcpsd(B). Since the diagonals of A and B are the same, we have SAcpsd = SBcpsd. So L = λLA +(1−λ)LB is feasible for ξtcpsd(λA+(1−λ)B), hence ξtcpsd(λA+(1−λ)B) ≤ λLA(1)+(1−λ)LB(1) = λξtcpsd(A)+(1−λ)ξtcpsd(B).

- Example 3 In this example we show that for t ≥ 1, the function

CSn+ → R, A  → ξtcpsd(A) is not continuous. For this we consider the matrices

Ak =

1/k 0 0 1 ∈ CS2+,

with cpsd-rankC(Ak) = 2 for all k ≥ 1. As Ak is diagonal positive deﬁnite we have ξtcpsd(Ak) = 2 for all t,k ≥ 1, while ξtcpsd(limk→∞Ak) = 1. This argument extends to CSn+ with n > 2. This example also shows that the ﬁrst level of the hierarchy ξ1cpsd(·) can be strictly better than the analytic lower bound (18) of [62].

- Example 4 In this example we determine ξtcpsd(A) for all t ≥ 1 and A ∈ CS2+. In view of Lemma 4(3) we only need to ﬁnd ξtcpsd(A(α)) for 0 ≤ α ≤ 1, where A(α) = α 1 α1 .


The ﬁrst bound ξ1cpsd(A(α)) is equal to the analytic bound 2/(α +1) from (18), where the equality follows from the fact that L given by L(xixj) = A(α)ij, L(x1) = L(x2) = 1 and L(1) = 2/(α +1) is feasible for ξ1cpsd(A(α)).

For t ≥ 2 we show ξtcpsd(A(α)) = 2−α. By the above this is true for α = 0 and α = 1, and in Example 1 we show ξtcpsd(A(1/2)) = 3/2 for t ≥ 2. The claim then follows since the function α  → ξtcpsd(A(α)) is convex by Lemma 8.

#### 3 Lower bounds on the completely positive rank

The best current approach for lower bounding the completely positive rank of a matrix is due to Fawzi and Parrilo [28]. Their approach relies on the atomicity of the completely positive rank, that is, the fact that cp-rank(A) = r if and only if A has an atomic decomposition A = ∑rk=1vkvTk for nonnegative vectors vk. In other words, if cp-rank(A) = r, then A/r can be written as a convex combination of r rank one positive semideﬁnite matrices vkvTk that satisfy 0 ≤ vkvTk ≤ A and vkvTk A. Based on this observation Fawzi and Parrilo deﬁne the parameter

τcp(A) = min α : α ≥ 0, A ∈ α ·conv R ∈ Sn : 0 ≤ R ≤ A, R A, rank(R) ≤ 1 ,

as lower bound for cp-rank(A). They also deﬁne the semideﬁnite programming parameter

τcpsos(A) = min α : α ∈ R, X ∈ Sn2,

α vec(A)T vec(A) X

0,

X(i,j),(i,j) ≤ A2ij for 1 ≤ i, j ≤ n, X(i,j),(k,l) = X(i,l),(k,j) for 1 ≤ i < k ≤ n, 1 ≤ j < l ≤ n, X A⊗A ,

as an efﬁciently computable relaxation of τcp(A), and they show rank(A) ≤ τcpsos(A). Therefore we have

rank(A) ≤ τcpsos(A) ≤ τcp(A) ≤ cp-rank(A).

Instead of the atomic point of view, here we take the matrix factorization perspective, which allows us to obtain bounds by adapting the techniques from Section 2 to the commutative setting. Indeed, we may view a factorization A = (aTi aj) by nonnegative vectors as a factorization by diagonal (and thus pairwise commuting) positive semideﬁnite matrices.

Before presenting the details of our hierarchy of lower bounds, we mention some of our results in order to make the link to the parameters τcpsos(A) and τcp(A). The direct analogue of {ξtcpsd(A)} in the commutative setting leads to a hierarchy that does not converge to τcp(A), but we provide two approaches to strengthen it that do converge to τcp(A). The ﬁrst approach is based on a generalization of the tensor constraints in τcpsos(A). We also provide a computationally more efﬁcient version of these tensor constraints, leading to a hierarchy whose second level is at least as good as τcpsos(A) while being deﬁned by a smaller semideﬁnite program. The second approach relies on adding localizing constraints for vectors in the unit sphere as in Section 2.2.

The following hierarchy is a commutative analogue of the hierarchy from Section 2, where we may now add the localizing polynomials Aij − xixj for the pairs 1 ≤ i < j ≤ n, which was not possible in the noncommutative setting of the completely positive semideﬁnite rank. For each t ∈ N∪{∞} we consider the semideﬁnite program

where we set

ξtcp(A) = min L(1) : L ∈ R[x1,...,xn]∗2t, L(xixj) = Aij for i, j ∈ [n], L ≥ 0 on M2t(SAcp) ,

SAcp = Aiixi −xi2 : i ∈ [n] ∪ Aij −xixj : 1 ≤ i < j ≤ n .

We additionally deﬁne ξ∗cp(A) by adding the constraint rank(M(L)) < ∞ to ξ∞cp(A). We also consider the strengthening ξtcp,†(A), where we add to ξtcp(A) the positivity constraints

L(gu) ≥ 0 for g ∈ {1}∪SAcp and u ∈ [x]2t−deg(g) (19) and the tensor constraints

(L((ww )c))w,w ∈ x =l A⊗l for all integers 2 ≤ l ≤ t, (20)

which generalize the case l = 2 used in the relaxation τcpsos(A). Here, for a word w ∈ x , we denote by wc the corresponding (commutative) monomial in [x]. The tensor constraints (20) involve matrices indexed by the noncommutative words of length exactly l. In Section 3.4 we show a more economical way to rewrite these con-

straints as (L(mm ))m,m ∈[x]=l QlA⊗lQTl , thus involving smaller matrices indexed by commutative words of degree l.

Note that, as before, we can strengthen the bounds by adding other localizing

polynomials to the set SAcp. In particular, we can follow the approach of Section 2.2. Another possibility is to add localizing constraints speciﬁc to the commutative set-

ting: we can add each monomial u ∈ [x] to SAcp (see Section 3.5.2 for an example).

The bounds ξtcp(A) and ξtcp,†(A) are monotonically nondecreasing in t and they are invariant under simultaneously permuting the rows and columns of A and under scaling a row and column of A by a positive number. In Propositions 6 and 7 we show

τcpsos(A) ≤ ξtcp,†(A) ≤ τcp(A) for t ≥ 2, and in Proposition 10 we show the equality ξ∗cp,†(A) = τcp(A).

- 3.1 Comparison to τcpsos(A)


We ﬁrst show that the semideﬁnite programs deﬁning ξtcp,†(A) are valid relaxations for the completely positive rank. More precisely, we show that they lower bound τcp(A).

- Proposition 6 For A ∈ CPn and t ∈ N∪{∞,∗} we have ξtcp,†(A) ≤ τcp(A).


Proof It sufﬁces to show the inequality for t = ∗. For this consider a decomposition A = α ∑rk=1λkRk, where α ≥ 1, λk > 0, ∑rk=1λk = 1, 0 ≤ Rk ≤ A, Rk A, and rankRk = 1. There are nonnegative vectors vk such that Rk = vkvTk . Deﬁne the linear map L ∈ R[x]∗ by L = α ∑rk=1λkLvk, where Lvk is the evaluation at vk mapping any polynomial p ∈ R[x] to p(vk).

The equality (L(xixj)) = A follows from the identity A = α ∑rk=1λkRk. The constraints L((√Aiixi −xi2)p2) ≥ 0 follow because

Lvk( Aiixi −xi2)p2) = ( Aii(vk)i −(vk)2i )p(vk)2 ≥ 0,

where we use that (vk)i ≥ 0 and (vk)2i = (Rk)ii ≤ Aii implies (vk)2i ≤ (vk)i√Aii. The constraints L((Aij −xixj)p2) ≥ 0 and

L(gu) ≥ 0 for g ∈ {1}∪SAcp and u ∈ [x] follow in a similar way.

It remains to be shown that Xl A⊗l for all l, where we set Xl = (L(uv))u,v∈ x =l. Note that X1 = A. We adapt the argument used in [28] to show Xl A⊗l using induction on l ≥ 2. Suppose A⊗(l−1) Xl−1. Combining A−Rk 0 and Rk 0 gives

(A−Rk)⊗R⊗k (l−1) 0 and thus A⊗R⊗k (l−1) R⊗l

k for each k. Scale by factor αλk and sum over k to get

A⊗Xl−1 =∑

αλkA⊗R⊗k (l−1) ∑

αλkR⊗l

k = Xl.

k

k

Finally, combining with A⊗(l−1) −Xl−1 0 and A 0, we obtain A⊗l = A⊗(A⊗(l−1) −Xl−1)+A⊗Xl−1 A⊗Xl−1 Xl.

Now we show that the new parameter ξ2cp,†(A) is at least as good as τcpsos(A). Later in Section 3.5.1 we will give an example where the inequality is strict.

- Proposition 7 For A ∈ CPn we have τcpsos(A) ≤ ξ2cp,†(A).

- Proof Let L be feasible for ξ2cp,†(A). We will construct a feasible solution to the program deﬁning τcpsos(A) with objective value L(1), which implies τcpsos(A) ≤ L(1) and thus the desired inequality. For this set α = L(1) and deﬁne the symmetric n2 ×n2 matrix X by X(i,j),(k,l) = L(xixjxkxl) for i, j,k,l ∈ [n]. Then the matrix


M :=

α vec(A)T vec(A) X

is positive semideﬁnite. This follows because M is obtained from the principal submatrix of M2(L) indexed by the monomials 1 and xixj (1 ≤ i ≤ j ≤ n) where the rows/columns indexed by xjxi with 1 ≤ i < j ≤ n are duplicates of the rows/columns indexed by xixj.

We have L((Aij −xixj)xixj) ≥ 0 for all i, j: For i = j this follows using the con-

straint L((Aij −xixj)u) ≥ 0 with u = xixj (from (19)), and for i = j this follows from L((Aii −xi2)xi2) = L(( Aii −xi)2 +2( Aiixi −xi2)) ≥ 0,

which holds because of (10), the constraint L(p2) ≥ 0 for deg(p) ≤ 2, and the constraint L(√Aiixi − xi2) ≥ 0. Using L(xixj) = Aij, we get X(i,j),(i,j) = L(xi2x2j) ≤ A2ij. We also have X(i,j),(k,l) = L(xixjxkxl) = L(xixlxkxj) = X(i,l),(k,j), and the constraint (L(uv))u,v∈ x =2 A⊗2 implies X A⊗A.

- 3.2 Convergence of the basic hierarchy


We ﬁrst summarize convergence properties of the hierarchy ξtcp(A). Note that unlike in Section 2 where we can only claim the inequality ξ∞cpsd(A) ≤ ξ∗cpsd(A), here we can show the equality ξ∞cp(A) = ξ∗cp(A). This is because we can use Theorem 7, which permits to represent certain truncated linear functionals by ﬁnite atomic measures.

- Proposition 8 Let A ∈ CPn. For every t ∈ N∪{∞,∗} the optimum in ξtcp(A) is attained, and ξtcp(A) → ξ∞cp(A) = ξ∗cp(A) as t → ∞. If ξtcp(A) admits a ﬂat optimal solution, then ξtcp(A) = ξ∞cp(A). Moreover, ξ∞cp(A) = ξ∗cp(A) is the minimum value of


L(1) taken over all conic combinations L of evaluations at elements of D(SAcp) satisfying A = (L(xixj)).

Proof We may assume A = 0. Since √Aiixi −xi2 ∈ SAcp for all i, using (10) we obtain that Tr(A) − ∑ixi2 ∈ M2(SAcp). By adapting the proof of Proposition 1 to the commutative setting, we see that the optimum in ξtcp(A) is attained for t ∈ N∪{∞}, and ξtcp(A) → ξ∞cp(A) as t → ∞.

We now show the inequality ξ∗cp(A) ≤ ξ∞cp(A), which implies that equality holds. For this, let L be optimal for ξ∞cp(A). By Theorem 7, the restriction of L to R[x]2 extends to a conic combination of evaluations at points in D(SAcp). It follows that

this extension is feasible for ξ∗cp(A) with the same objective value. This shows that ξ∗cp(A) ≤ ξ∞cp(A), that the optimum in ξ∗cp(A) is attained, and that ξ∗cp(A) is the minimum of L(1) over all conic combinations L of evaluations at elements of D(SAcp) such that A = (L(xixj)). Finally, by Theorem 6 we have ξtcp(A) = ξ∞cp(A) if ξtcp(A) admits a ﬂat optimal solution.

Next, we give a reformulation for the parameter ξ∗cp(A), which is similar to the formulation of τcp(A), although it lacks the constraint R A which is present in τcp(A).

- Proposition 9 We have ξ∗cp(A) = min α : α ≥ 0, A ∈ α ·conv R ∈ Sn : 0 ≤ R ≤ A, rank(R) ≤ 1 .

Proof This follows directly from the reformulation of ξ∗cp(A) in Proposition 8 in terms of conic evaluations at points in D(SAcp) after observing that, for v ∈ Rn, we have v ∈ D(SAcp) if and only if the matrix R = vvT satisﬁes 0 ≤ R ≤ A.

- 3.3 Additional constraints and convergence to τcp(A)


The reformulation of the parameter ξ∗cp(A) in Proposition 9 differs from τcp(A) in that the constraint R A is missing. In order to have a hierarchy converging to τcp(A) we need to add constraints to enforce that L can be decomposed as a conic combination of evaluation maps at nonnegative vectors v satisfying vvT A. Here we present two ways to achieve this goal. First we show that the tensor constraints (20) sufﬁce in the sense that ξ∗cp,†(A) = τcp(A) (note that the constraints (19) are not needed for this result). However, because of the special form of the tensor constraints we do not know whether ξtcp,†(A) admitting a ﬂat optimal solution implies ξtcp,†(A) = ξ∗cp,†(A), and we do not know whether ξ∞cp,†(A) = ξ∗cp,†(A). Second, we adapt the approach of adding additional localizing constraints from Section 2.2 to the commutative setting, where we do show ξ∞cp,Sn−1(A) = ξ∗cp,Sn−1(A) = τcp(A). This yields a doubly indexed sequence of semideﬁnite programs whose optimal values converge to τcp(A).

- Proposition 10 Let A ∈ CPn. For every t ∈ N ∪ {∞} the optimum in ξtcp,†(A) is attained. We have ξtcp,†(A) → ξ∞cp,†(A) as t → ∞ and ξ∗cp,†(A) = τcp(A).


Proof The attainment of the optima in ξtcp,†(A) for t ∈ N∪{∞} and the convergence of ξtcp,†(A) to ξ∞cp,†(A) can be shown in the same way as the analogue statements for ξtcp(A) in Proposition 8.

We have seen the inequality ξ∗cp,†(A) ≤ τcp(A) in Proposition 6. Now we show the reverse inequality. Let L be feasible for ξ∗cp,†(A). We will show that L is feasible for τcp(A), which implies τcp(A) ≤ L(1) and thus τcp(A) ≤ ξ∗cp,†(A).

By Proposition 7 and the fact that rank(A) ≤ τcpsos(A) we have L(1) > 0 (where we assume A = 0). By Theorem 5, we may write

K

## ∑

λkLvk,

L = L(1)

k=1

where λk > 0, ∑k λk = 1, and Lvk is an evaluation map at a point vk ∈ D(SAcp). We deﬁne the matrices Rk = vkvTk , so that A = L(1)∑Kk=1Rk. The matrices Rk satisfy

- 0 ≤ Rk ≤ A since vk ∈ D(SAcp). Clearly also Rk 0. It remains to show that Rk A. For this we use the tensor constraints (20). Using that L is a conic combination of evaluation maps, we may rewrite these constraints as


K

## ∑

λkR⊗l

k A⊗l,

L(1)

k=1

from which it follows that L(1)λkR⊗l

k A⊗l for all k ∈ [K]. Therefore, for all k ∈ [K] and all vectors v with vTRkv > 0 we have

L(1)λk ≤

vTAv vTRkv

l

for all l ∈ N. (21)

Suppose there is a k such that Rk A. Then there exists a v such that vTRkv > vTAv. As (vTAv)/(vTRkv) < 1, letting l tend to ∞ we obtain L(1)λk = 0, reaching a contradiction. It follows that Rk A for all k ∈ [K].

The second approach for reaching τcp(A) is based on using the extra localizing constraints from Section 2.2. For a subset V ⊆ Sn−1, deﬁne ξtcp,V(A) by replacing the truncated quadratic module M2t(SAcp) in ξtcp(A) by M2t(SAcp,V), where

SAcp,V = SAcp ∪ vTAv−

n

## ∑

vixi

i=1

2

: v ∈ V .

Proposition 5 can be adapted to the completely positive setting, so that we have a sequence of ﬁnite subsets V1 ⊆V2 ⊆ ... ⊆ Sn−1 with ξ∗cp,Vk(A) → ξ∗cp,Sn−1(A) as k → ∞. Proposition 8 still holds when adding extra localizing constraints, so that for any k ≥ 1 we have

ξtcp,Vk(A) = ξ∗cp,Vk(A). Combined with Proposition 11 this shows that we have a doubly indexed sequence ξtcp,Vk(A) of semideﬁnite programs that converges to τcp(A) as t → ∞ and k → ∞.

lim

t→∞

- Proposition 11 For A ∈ CPn we have ξ∗cp,Sn−1(A) = τcp(A).


Proof The proof is the same as the proof of Proposition 9, with the following additional observation: Given a vector u ∈ Rn, we have u ∈ D(SAcp,Sn−1) only if uuT A. The latter follows from the additional localizing constraints: for each v ∈ Rn we have

0≤vTAv− ∑

viui

i

2

##### = vT(A−uuT)v.

- 3.4 More efﬁcient tensor constraints


Here we show that for any integer l ≥2 the constraint A⊗l −(L((ww )c))w,w ∈ x =l 0, used in the deﬁnition of ξtcp,+(A), can be reformulated in a more economical way using matrices indexed by commutative monomials in [x]=l instead of noncommutative words in x =l. For this we exploit the symmetry in the matrices A⊗l and (L((ww )c))w,w ∈ x =l for L ∈ R[x]∗2l. Recall that for a word w ∈ x , we let wc denote the corresponding (commutative) monomial in [x].

Deﬁne the matrix Ql ∈ R[x]=l× x =l by

1/dm if wc = m, 0 otherwise,

(22)

(Ql)m,w =

where, for m = x1α1 ···xnαn ∈ [x]=l, we deﬁne the multinomial coefﬁcient

l! α1!···αn!

dm = w ∈ x =l : wc = m =

. (23)

- Lemma 9 For L ∈ R[x]∗2l we have

Ql(L((ww )c))w,w ∈ x =lQTl = (L(mm ))m,m ∈[x]=l. Proof For m,m ∈ [x]l, the (m,m )-entry of the left hand side is equal to

∑

w,w ∈ x =l

QmwQm w L((ww )c)= ∑

w∈ x =l wc=m

∑

w ∈ x =l (w )c=m

L((ww )c) dmdm

= L(mm ).

The symmetric group Sl acts on x =l by (xi1 ···xil)σ = xiσ(1) ···xiσ(l) for σ ∈ Sl. Let

P =

1

l! ∑

σ∈Sl

Pσ, (24)

where, for any σ ∈ Sl, Pσ ∈ R x =l× x =l is the permutation matrix deﬁned by

(Pσ)w,w =

1 if wσ = w , 0 otherwise.

A matrix M ∈ R x =l× x =l is said to be Sl-invariant if PσM = MPσ for all σ ∈ Sl.

- Lemma 10 If M ∈ R x =l× x =l is symmetric and Sl-invariant, then M 0 ⇐⇒ QlMQTl 0.


Proof The implication M 0 =⇒ QlMQTl 0 is immediate. For the other implication we need a preliminary fact. Consider the diagonal matrix D ∈ R[x]=l×[x]=l with

Dmm = dm for m ∈ [x]=l. We claim that QTl DQl = P, the matrix in (24). Indeed, for any w,w ∈ x =l, we have

1/dm if wc = (w )c = m, 0 otherwise

(QTl DQl)ww = ∑

(Ql)mw(Ql)mw Dmm =

m∈[x]=l

##### = |{σ ∈ Sl : wσ = w }|

= Pww .

l!

Suppose QlMQTl 0, and let λ be an eigenvalue of M with eigenvector z. Since MP = PM, we may assume Pz = z, for otherwise we can replace z by Pz, which is

still an eigenvector of M with eigenvalue λ. We may also assume z to be a unit vector. Then λ ≥ 0 can be shown using the identity QTl DQl = P as follows:

λ = zTMz = zTPMPz = zT(QTl DQl)M(QTl DQl)z = (DQlz)T(QlMQTl )DQlz ≥ 0. We can now derive our symmetry reduction result:

- Proposition 12 For L ∈ R[x]∗2l we have A⊗l −(L((ww )c))w,w ∈ x =l 0 ⇐⇒ QlA⊗lQTl −(L(mm ))m,m ∈[x]=l 0.


Proof For any w,w ∈ x =l we have (PσA⊗lPσT)w,w = A⊗l

wσ,(w )σ = A⊗l

w,w and (Pσ(L((uu )c))u,u ∈ x =lPσ∗)w,w = L((wσ(w )σ)c) = L((ww )c).

This shows that the matrix A⊗l − (L((ww )c))w,w ∈ x =l is Sl-invariant. Hence the claimed result follows by using Lemma 9 and Lemma 10.

- 3.5 Computational examples


- 3.5.1 Bipartite matrices Consider the (p+q)×(p+q) matrices


(a+q)Ip Jp,q

P(a,b) =

Jq,p (b+ p)Iq

##### , a,b ∈ R+,

where Jp,q denotes the all-ones matrix of size p×q. We have P(a,b) = P(0,0)+D for some nonnegative diagonal matrix D. As can be easily veriﬁed, P(0,0) is completely positive with cp-rank(P(0,0)) = pq, so P(a,b) is completely positive with pq ≤ cp-rank(P(a,b)) ≤ pq+ p+q.

For p = 2 and q = 3 we have cp-rank(P(a,b)) = 6 for all a,b ≥ 0, which follows from the fact that 5 × 5 completely positive matrices with at least one zero entry have cp-rank at most 6; see [7, Theorem 3.12]. Fawzi and Parrilo [28] show that τcpsos(P(0,0)) = 6, and give a subregion of [0,1]2 where 5 < τcpsos(P(a,b)) < 6. The next lemma shows the bound ξ2cp,†(P(a,b)) is tight for all a,b ≥ 0 and therefore strictly improves on τcpsos in this region.

- Lemma 11 For a,b ≥ 0 we have ξ2cp,†(P(a,b)) ≥ pq. Proof Let L be feasible for ξ2cp,†(P(a,b)) and let


B =

α cT c X

be the principal submatrix of M2(L) where the rows and columns are indexed by

##### {1}∪{xixj : 1 ≤ i ≤ p, p+1 ≤ j ∈ p+q}.

It follows that c is the all ones vector c = 1. Moreover, if P(a,b)ij = 0 for some i = j, then the constraints L(xixju) ≥ 0 and L((P(a,b)ij −xixj)u) ≥ 0 imply L(xixju) = 0 for all u ∈ [x]2. Hence, Xxixj,xkxl = L(xixjxkxl) = 0 whenever xixj = xkxl. It follows that X is a diagonal matrix. We write

B =

α 1T 1 Diag(z1,...,zpq)

##### .

##### 1 −1T −1 J

Since

- 0 we have

0 ≤ Tr

α 1T

- 1 Diag(z1,...,zpq)


pq

1 −1T −1 J

## ∑

= α −2pq+

zk.

k=1

Finally, by the constraints L((P(a,b)ij − xixj)u) ≥ 0 (with i ∈ [p], j ∈ p + [q] and u = xixj) and L(xixj) = P(a,b)ij we obtain zk ≤ 1 for all k ∈ [pq]. Combined with the above inequality, it follows that

L(1) = α ≥ 2pq−

and hence ξ2cp,†(P(a,b)) ≥ pq.

pq

## ∑

zk ≥ pq,

k=1

- 3.5.2 Examples related to the DJL-conjecture


The Drew-Johnson-Loewy conjecture [22] states that the maximal cp-rank of an n × n completely positive matrix is equal to n2/4 . Recently this conjecture has been disproven for n = 7,8,9,10,11 in [11] and for all n ≥ 12 in [12] (interestingly, it remains open for n = 6). Here we study our bounds on the examples of [11]. Although our bounds are not tight for the cp-rank, they are non-trivial and as such may be of interest for future comparisons. For numerical stability reasons we have evaluated our bounds on scaled versions of the matrices from [11], so that the diagonal entries become equal to 1. The matrices M˜7, M˜8 and M˜9 correspond to the matrices M˜ in Examples 1,2,3 of [11], and M7, M11 correspond to the matrices M in Examples

- 1 and 4. The column ξ2cp,†(·)+xixj corresponds to the bound ξ2cp,†(·) where we replace SAcp by SAcp ∪{xixj : 1 ≤ i < j ≤ n}.


Table 1 Examples from [11] with various bounds on their cp-rank

Example cp-rank(·) n42 rank(·) ξ1cp(·) ξ2cp(·) ξ2cp,†(·) ξ2cp,†(·)+xixj ξ3cp,†(·)

M7 14 12 7 2.64 4.21 7.21 9.75 10.50 M7 14 12 7 2.58 4.66 8.43 9.53 10.50 M8 18 16 8 3.23 5.45 8.74 10.41 13.82 M9 26 20 9 3.39 5.71 11.60 13.74 17.74 M11 32 30 11 4.32 7.46 20.76 21.84 –

#### 4 Lower bounds on the nonnegative rank

In this section we adapt the techniques for the cp-rank from Section 3 to the asymmetric setting of the nonnegative rank. We now view a factorization A = (aTi bj)i∈[m],j∈[n] by nonnegative vectors as a factorization by positive semideﬁnite diagonal matrices, by writing Aij = Tr(XiXm+j), with Xi = Diag(ai) and Xm+j = Diag(bj). Note that we can view this as a “partial matrix” setting, where for the symmetric matrix (Tr(XiXk))i,k∈[m+n] of size m + n, only the off-diagonal entries at the positions (i,m+ j) for i ∈ [m], j ∈ [n] are speciﬁed.

This asymmetry requires rescaling the factors in order to get upper bounds on their maximal eigenvalues, which is needed to ensure the Archimedean property for the selected localizing polynomials. For this we use the well-known fact that for any A ∈ Rm+×n there exists a factorization A = (Tr(XiXm+j)) by diagonal nonnegative matrices of size rank+(A), such that

λmax(Xi),λmax(Xm+j) ≤ Amax for all i ∈ [m], j ∈ [n],

where Amax := maxi,jAij. To see this, observe that for any rank one matrix R = uvT with 0 ≤ R ≤ A, one may assume 0 ≤ ui,vj ≤

√Amax for all i, j. Hence, the set

SA+ = Amaxxi −xi2 : i ∈ [m+n] ∪ Aij −xixm+j : i ∈ [m], j ∈ [n]

is localizing for A; that is, there exists a minimal factorization X of A with X ∈ D(SA+). Given A ∈ Rm≥×0n, for each t ∈ N∪{∞} we consider the semideﬁnite program

ξt+(A) = min L(1) : L ∈ R[x1,...,xm+n]∗2t, L(xixm+j) = Aij for i ∈ [m], j ∈ [n], L ≥ 0 on M2t(SA+) .

Moreover, deﬁne ξ∗+(A) by adding the constraint rank(M(L)) < ∞ to the program deﬁning ξ∞+(A). It it easy to check that ξt+(A) ≤ ξ∞+(A) ≤ ξ∗+(A) ≤ rank+(A) for

- t ∈ N.


Denote by ξt+,†(A) the strengthening of ξt+(A) where we add the positivity constraints

L(gu) ≥ 0 for g ∈ {1}∪SA+ and u ∈ [x]2t−deg(g). (25) Note that these extra constraints can help for ﬁnite t, but are redundant for t ∈ {∞,∗}.

- 4.1 Comparison to other bounds


As in the previous section, we compare our bounds to the bounds by Fawzi and Parrilo [28]. They introduce the following parameter τ+(A) as analogue of the bound τcp(A) for the nonnegative rank:

τ+(A) = min α : α ≥ 0, A ∈ α ·conv R ∈ Rm×n : 0 ≤ R ≤ A, rank(R) ≤ 1 , and the analogue τ+sos(A) of the bound τcpsos(A) for the nonnegative rank:

τ+sos(A) = inf α : X ∈ Rmn×mn, α ∈ R,

α vec(A)T vec(A) X

0,

X(i,j),(i,j) ≤ A2ij for 1 ≤ i ≤ m,1 ≤ j ≤ n, X(i,j),(k,l) = X(i,l),(k,j) for 1 ≤ i < k ≤ m, 1 ≤ j < l ≤ n .

First we give the analogue of Proposition 8, whose proof we omit since it is very similar.

- Proposition 13 Let A ∈ Rm+×n. For every t ∈ N ∪ {∞,∗} the optimum in ξt+(A) is attained, and ξt+(A) → ξ∞+(A) = ξ∗+(A) as t → ∞. If ξt+(A) admits a ﬂat optimal solution, then ξt+(A) = ξ∗+(A). Moreover, ξ∞+(A) = ξ∗+(A) is the minimum of L(1)

over all conic combinations L of trace evaluations at elements of D(SA+) satisfying A = (L(xixm+j)).

Now we observe that the parameters ξ∞+(A) and ξ∗+(A) coincide with τ+(A), so that we have a sequence of semideﬁnite programs converging to τ+(A).

- Proposition 14 For any A ∈ Rm≥×0n, we have ξ∞+(A) = ξ∗+(A) = τ+(A).

Proof The discussion at the beginning of Section 4 shows that for any rank one matrix R satisfying 0 ≤ R ≤ A we may assume that R = uvT with (u,v) ∈ Rm+ × Rn+ and ui,vj ≤

√Amax for i ∈ [m], j ∈ [n]. Hence, τ+(A) can be written as min α : α ≥ 0, A ∈ α ·conv uvT: u ∈ 0, Amax

m

,v ∈ 0, Amax

n

, uvT ≤ A

= min α : α ≥ 0, A ∈ α ·conv uvT : (u,v) ∈ D(SA+) .

The equality ξ∞+(A) = ξ∗+(A) = τ+(A) now follows from the reformulation of ξ∗+(A) in Proposition 13 in terms of conic evaluations, after noting that for (u,v) in Rm ×Rn

we have (u,v) ∈ D(SA+) if and only if the matrix R = uvT satisﬁes 0 ≤ R ≤ A.

Analogously to the case of the completely positive rank we have the following proposition. The proof is similar to that of Proposition 4.2, considering now for M the principal submatrix of M2(L) indexed by the monomials 1 and xixm+j for i ∈ [m] and j ∈ [n].

- Proposition 15 If A is a nonnegative matrix, then ξ2+,†(A) ≥ τ+sos(A).


In the remainder of this section we recall how τ+(A) and τ+sos(A) compare to other bounds in the literature. These bounds can be divided into two categories: combinatorial lower bounds and norm-based lower bounds. The following diagram from [28] summarizes how τ+sos(A) and τ+(A) relate to the combinatorial lower bounds

τ+sos(A) ≤ τ+(A) ≤ rank+(A)

≤

≤

≤

fool(A) = ω(RG(A)) ≤ ϑ(RG(A)) ≤ χfrac(RG(A)) ≤ χ(RG(A)) = rankB(A).

Here RG(A) is the rectangular graph, with V = {(i, j) ∈ [m]×[n] : Aij > 0} as vertex set and E = {((i, j),(k,l)) : AilAkj = 0} as edge set. The coloring number of RG(A) coincides with the well known rectangle covering number (also denoted rankB(A)), which was used, e.g., in [30] to show that the extension complexity of the correlation polytope is exponential. The clique number of RG(A) is also known as the fooling set number (see, e.g., [29]). Observe that the above combinatorial lower bounds only depend on the sparsity pattern of the matrix A, and that they are all equal to one for a strictly positive matrix.

Fawzi and Parrilo [28] have furthermore shown that the bound τ+(A) is at least as good as norm-based lower bounds:

N ∗(A) N (A)

τ+(A) = sup

.

N monotone and positively homogeneous

Here, a function N : Rm+×n → R+ is positively homogeneous if N (λA) = λN (A) for all λ ≥ 0 and monotone if N (A) ≤ N (B) for A ≤ B, and N ∗(A) is deﬁned as

N ∗(A) = max{L(A) : L : Rm×n → R linear and L(X) ≤ 1 for all X ∈ Rm+×n with rank(X) ≤ 1 and N (X) ≤ 1}.

These bounds are called norm-based since norms often provide valid functions N . For example, when N is the ∞-norm, Rothvoß [66] used the corresponding lower bound to show that the matching polytope has exponential extension complexity.

When N is the Frobenius norm: N (A) = (∑i,j A2ij)1/2, the parameter N ∗(A) is known as the nonnegative nuclear norm. In [27] it is denoted by ν+(A), shown to satisfy rank+(A) ≥ (ν+(A)/||A||F)2, and reformulated as

ν+(A)=min ∑

λi :A=∑

λiuivTi , (λi,ui,vi) ∈ R1++m+n, ||ui||2 = ||vi||2 = 1 (26)

i

i

= max A,W : W ∈ Rm×n, −W I T −IW is copositive . (27) where the cone of copositive matrices is the dual of the cone of completely positive matrices. Fawzi and Parrilo [27] use the copositive formulation (27) to pro-

vide bounds ν+[k](A) (k ≥ 0), based on inner approximations of the copositive cone from [60], which converge to ν+(A) from below. We now observe that by Theorem 7 the atomic formulation of ν+(A) from (26) can be seen as a moment optimization problem:

ν+(A) = min

1dµ(x) s.t. Aij =

V(S)

xixm+j dµ(x) for i ∈ [m], j ∈ [n].

V(S)

Here, the optimization variable µ is required to be a Borel measure on the variety V(S), where

S = {∑mi=1xi2 −1, ∑nj=1xm2+j −1}. (The same observation is made in [74] for the real nuclear norm of a symmetric 3-tensor and in [59] for symmetric odd-dimensional tensors.) For t ∈ N ∪ {∞}, let µt(A) denote the parameter deﬁned analogously to ξt+(A), where we replace the condition L ≥ 0 on M2t(SA+) by L ≥ 0 on M2t({x1,...,xm+n}) and L = 0 on I2t(S), and let µ∗(A) be obtained by adding the constraint rank(M(L)) < ∞ to µ∞(A). We have µt(A) → µ∞(A) = µ∗(A) = ν+(A) by Theorem 7 and (a non-normalized analogue of) Theorem 8. One can show that µ1(A) with the additional constraints L(u) ≥ 0 for all

- u ∈ [x]2, is at least as good as ν+[0](A). It is not clear how the hierarchies µt(A) and ν+[k](A) compare in general.


- 4.2 Computational examples


We illustrate the performance of our approach by comparing our lower bounds ξ2+,† and ξ3+,† to the lower bounds τ+ and τ+sos on the two examples considered in [28].

- 4.2.1 All nonnegative 2×2 matrices

For A(α) = 11 α1 , Fawzi and Parrilo [28] show that

τ+(A(α)) = 2−α and τ+sos(A(α)) =

2 1+α

for all 0 ≤ α ≤ 1.

Since the parameters τ+(A) and τ+sos(A) are invariant under scaling and permuting rows and columns of A, one can use the identity

1 1 1 α =

1 0 0 α

1 1 1 1/α

- 0 1
- 1 0


to see this describes the parameters for all nonnegative 2 × 2 matrices. By using a semideﬁnite programming solver for α = k/100, k ∈ [100], we see that ξ2+(A(α)) coincides with τ+(A(α)).

- 4.2.2 The nested rectangles problem


In this section we consider the nested rectangles problem as described in [28, Section 2.7.2] (see also [56]), which asks for which a,b there exists a triangle T such that R(a,b) ⊆ T ⊆ P, where R(a,b) = [−a,a]×[−b,b] and P = [−1,1]2.

The nonnegative rank relates not only to the extension complexity of a polytope [78], but also to extended formulations of nested pairs [13,32]. An extended formulation of a pair of polytopes P1 ⊆ P2 ⊆ Rd is a (possibly) higher dimensional polytope K whose projection π(K) is nested between P1 and P2. Let us suppose π(K) = {x ∈ Rd : y ∈ Rk+, (x,y) ∈ K} and K = {(x,y) : Ex+Fy = g, y ∈ Rk+}, then k

is the size of the extended formulation, and the smallest such k is called the extension complexity of the pair (P1,P2). It is known (cf. [13, Theorem 1]) that the extension complexity of the pair (P1,P2), where

P1 = conv({v1,...,vn}) and P2 = {x : aTi x ≤ bi for i ∈ [m]},

is equal to the nonnegative rank of the generalized slack matrix SP1,P2 ∈ Rm×n, deﬁned by

(SP1,P2)ij = bj −aTj vi for i ∈ [m], j ∈ [n].

Any nonnegative matrix is the slack matrix of some nested pair of polytopes [35, Lemma 4.1] (see also [32]).

Applying this to the pair (R(a,b),P), one immediately sees that there exists a polytope K with at most three facets whose projection T = π(K) ⊆ R2 satisﬁes R(a,b) ⊆ T ⊆ P if and only if the pair (R(a,b),P) admits an extended formulation of size 3. For a,b > 0, the polytope T has to be 2 dimensional, therefore K has to be at least 2 dimensional as well; it follows that K and T have to be triangles. Hence there exists a triangle T such that R(a,b) ⊆ T ⊆ P if and only if the nonnegative rank of the slack matrix S(a,b) := SR(a,b),P is equal to 3. One can verify that

  

  .

1−a 1+a 1−b 1+b 1+a 1−a 1−b 1+b 1+a 1−a 1+b 1−b 1−a 1+a 1+b 1−b

S(a,b) =

Such a triangle exists if and only if (1+a)(1+b) ≤ 2 (see [28, Proposition 4] for a proof sketch). To test the quality of their bound, Fawzi and Parrilo [28] compute τ+sos(S(a,b)) for different values of a and b. In doing so they determine the region where τ+sos(S(a,b)) > 3. We do the same for the bounds ξ1+,†(S(a,b)),ξ2+,†(S(a,b)) and ξ3+,†(S(a,b)), see Figure 1. The results show that ξ2+,†(S(a,b)) strictly improves upon the bound τ+sos(S(a,b)), and that ξ3+,†(S(a,b)) is again a strict improvement over ξ2+,†(S(a,b)).

#### 5 Lower bounds on the positive semideﬁnite rank

The positive semideﬁnite rank can be seen as an asymmetric version of the completely positive semideﬁnite rank. Hence, as was the case in the previous section for the nonnegative rank, we need to select suitable factors in a minimal factorization in order to be able to bound their maximum eigenvalues and obtain a localizing set of polynomials leading to an Archimedean quadratic module.

For this we can follow, e.g., the approach in [52, Lemma 5] to rescale a factorization and claim that, for any A ∈ Rm+×n with psd-rankC(A) = d, there exists a factorization A = ( Xi,Xm+j ) by matrices X1,...,Xm+n ∈ Hd+ such that ∑mi=1Xi = I and Tr(Xm+j) = ∑iAij for all j ∈ [n]. Indeed, starting from any factorization Xi,Xm+j in Hd+ of A, we may replace Xi by X−1/2XiX−1/2 and Xm+j by X1/2Xm+jX1/2, where

- 0.8
- 1


| | | | | | | |
|---|---|---|---|---|---|---|
| |![image 1](<2017-gribling-lower-bounds-matrix-factorization_images/imageFile1.png>)| | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |


0.6

b

0.4

0.2

0

0 0.2 0.4 0.6 0.8 1

a

- Fig. 1 The colored region corresponds to rank+(S(a,b)) = 4. The top right region (black) corresponds to ξ1+,†(S(a,b)) > 3, the two top right regions (black and red) together correspond to τ+sos(S(a,b)) > 3, the three top right regions (black, red and yellow) to ξ2+,†(S(a,b)) > 3, and the four top right regions (black, red, yellow, and green) to ξ3+,†(S(a,b)) > 3


X := ∑mi=1Xi is positive deﬁnite (by minimality of d). This argument shows that the set of polynomials

m

## ∑

SApsd = xi −xi2 : i ∈ [m] ∪

Aij xm+j −xm2+j : j ∈ [n]

i=1

is localizing for A; that is, there is at least one minimal factorization X of A such that g(X) 0 for all polynomials g ∈ SApsd. Moreover, for the same minimal factorization X of A we have p(X)(1−∑mi=1Xi) = 0 for all p ∈ R x .

Given A ∈ Rm+×n, for each t ∈ N∪{∞} we consider the semideﬁnite program

ξtpsd(A) = min L(1) : L ∈ R x1,...,xm+n ∗2t, L(xixm+j) = Aij for i ∈ [m], j ∈ [n], L ≥ 0 on M2t(SApsd), L = 0 on I2t(1−∑mi=1xi) .

We additionally deﬁne ξ∗psd(A) by adding the constraint rank(M(L)) < ∞ to the program deﬁning ξ∞psd(A) (and considering the inﬁmum instead of the minimum, since we do not know if the inﬁmum is attained in ξ∗psd(A)). By the above discussion it follows that the parameter ξ∗psd(A) is a lower bound on psd-rankC(A) and we have

ξ1psd(A) ≤ ... ≤ ξtpsd(A) ≤ ... ≤ ξ∞psd(A) ≤ ξ∗psd(A) ≤ psd-rankC(A).

Note that, in contrast to the previous bounds, the parameter ξtpsd(A) is not invariant under rescaling the rows of A or under taking the transpose of A (see Section 5.2.2).

It follows from the construction of SApsd and Equation (10) that the quadratic mod-

ule M(SApsd) is Archimedean, and hence the following analogue of Proposition 1 can be shown.

- Proposition 16 Let A ∈ Rm+×n. For each t ∈ N ∪ {∞}, the optimum in ξtpsd(A) is attained, and we have


ξtpsd(A) = ξ∞psd(A).

lim

t→∞

Moreover, ξ∞psd(A) is equal to the inﬁmum over all α ≥ 0 for which there exists a unital C∗-algebra A with tracial state τ and X ∈ DA (SApsd)∩VA (1−∑mi=1xi) such that A = α ·(τ(XiXm+j))i∈[m],j∈[n].

- 5.1 Comparison to other bounds In [52] the following bound on the complex positive semideﬁnite rank was derived:

psd-rankC(A) ≥

m

∑

i=1

maxj∈[n]

Aij ∑iAij

. (28)

- If a feasible linear form L to ξtpsd(A) satisﬁes the inequalities L(xi(∑iAij−xm+j)) ≥ 0 for all i ∈ [m], j ∈ [n], then L(1) is at least the above lower bound. Indeed, the inequalities give


L(xi) ≥ maxj∈[n]

L(xixm+j) ∑iAij

= maxj∈[n]

Aij ∑iAij

.

and hence

L(1) =

m

∑

i=1

L(xi) ≥

m

∑

i=1

maxj∈[n]

Aij ∑iAij

.

The inequalities L(xi(∑iAij −xm+j)) ≥ 0 are easily seen to be valid for trace evaluations at points of D(SApsd). More importantly, as in Lemma 2, these inequalities are satisﬁed by feasible linear forms to the programs ξ∞psd(A) and ξ∗psd(A). Hence, ξ∞psd(A) and ξ∗psd(A) are at least as good as the lower bound (28).

In [52] two other ﬁdelity based lower bounds on the psd-rank were deﬁned; we do not know how they compare to ξtpsd(A).

- 5.2 Computational examples


In this section we apply our bounds to some (small) examples taken from the literature, namely 3×3 circulant matrices and slack matrices of small polygons.

- 0

- 0.5
- 1

1.5

2

- 2.5
- 3


- 3.5
- 4


| | | | | | | | | | |
|---|---|---|---|---|---|---|---|---|---|
| |![image 2](<2017-gribling-lower-bounds-matrix-factorization_images/imageFile2.png>)| | | | | | | | |
| | | | | | | | | | |
| | | | | | | | | | |
| | | | | | | | | | |
| | | | | | | | | | |
| | | | | | | | | | |
| | | | | | | | | | |
| | | | | | | | | | |
| | | | | | | | | | |


c

0 0.5 1 1.5 2 2.5 3 3.5 4 b

- Fig. 2 The colored region corresponds to the values (b,c) for which psd-rankR(M(b,c)) = 3; the outer region (yellow) shows the values of (b,c) for which ξ2psd(M(b,c)) > 2.


5.2.1 Nonnegative circulant matrices of size 3

We consider the nonnegative circulant matrices of size 3 which are, up to scaling, of the form

 

  with b,c ≥ 0.

1 b c c 1 b b c 1

M(b,c) =

- If b = 1 = c, then rank(M(b,c)) = psd-rankR(M(b,c)) = psd-rankC(M(b,c)) = 1. Otherwise we have rank(M(b,c)) ≥ 2, which implies psd-rankK(M(b,c)) ≥ 2 for


- K ∈ {R,C}. In [26, Example 2.7] it is shown that


psd-rankR(M(b,c)) ≤ 2 ⇐⇒ 1+b2 +c2 ≤ 2(b+c+bc).

Hence, if b and c do not satisfy the above relation then psd-rankR(M(b,c)) = 3.

To see how good our lower bounds are for this example, we use a semideﬁnite programming solver to compute ξ2psd(M(b,c)) for (b,c) ∈ [0,4]2 (with stepsize 0.01). In Figure 2 we see that the bound ξ2psd(M(b,c)) certiﬁes that psd-rankR(M(b,c)) = psd-rankC(M(b,c)) = 3 for most values (b,c) where psd-rankR(M(b,c)) = 3.

5.2.2 Polygons

Here we consider the slack matrices of two polygons in the plane, where the bounds are sharp (after rounding) and illustrate the dependence on scaling the rows or taking the transpose. We consider the quadrilateral Q with vertices (0,0),(0,1),(1,0),(2,2),

and the regular hexagon H, whose slack matrices are given by





- 0 1 2 2 1 0

- 0 0 1 2 2 1
- 1 0 0 1 2 2
- 2 1 0 0 1 2 2 2 1 0 0 1


- 1 2 2 1 0 0


  

  , SH =

- 0 0 2 2
- 1 0 0 3 0 1 3 0
- 2 2 0 0


SQ =

.

 

 

Our lower bounds on the psd-rankC are not invariant under taking the transpose, indeed numerically we have ξ2psd(SQ) ≈ 2.266 and ξ2psd(SQT) ≈ 2.5. The slack matrix SQ has psd-rankR(SQ) = 3 (a corollary of [36, Theorem 4.3]) and therefore both bounds certify psd-rankC(SQ) = 3 = psd-rankR(SQ).

Secondly, our bounds are not invariant under rescaling the rows of a nonnegative matrix. Numerically we have ξ2psd(SH) ≈ 1.99 while ξ2psd(DSH) ≈ 2.12, where D = Diag(2,2,1,1,1,1). The bound ξ2psd(DSH) is in fact tight (after rounding) for the complex positive semideﬁnite rank of DSH and hence of SH: in [34] it is shown that psd-rankC(SH) = 3.

#### 6 Discussion and future work

In this work we provide a uniﬁed approach for the four matrix factorizations obtained by considering (a)symmetric factorizations by nonnegative vectors and positive semideﬁnite matrices. Our methods can be extended to the nonnegative tensor rank, which is deﬁned as the smallest integer d for which a k-tensor A ∈ Rn+1×···×nk can be written as A = ∑dl=1u1,l ⊗ ··· ⊗ uk,l for nonnegative vectors uj,l ∈ Rn+j. The approach from Section 4 for rank+ can be extended to obtain a hierarchy of lower bounds on the nonnegative tensor rank. For instance, if A is a 3-tensor, the analogous bound ξt+(A) is obtained by minimizing L(1) over L ∈ R[x1,...,xn1+n2+n3]∗ such that L(xi1xn1+i2xn1+n2+i3) = Ai1i2i3 (for i1 ∈ [n1],i2 ∈ [n2],i3 ∈ [n3]), using as localizing polynomials in SA+ the polynomials √3 Amaxxi −xi2 and Ai1i2i3 −xi1xn1+i2xn1+n2+i3. As in the matrix case one can compare to the bounds τ+(A) and τ+sos(A) from [28]. One can show ξ∗+(A) = τ+(A), and one can show ξ3+,†(A) ≥ τ+sos(A) after adding the conditions L(xi1xn1+i2xn1+n2+i3(Ai1i2i3 −xi1xn1+i2xn1+n2+i3)) ≥ 0 to ξ3+(A).

Testing membership in the completely positive cone and the completely positive semideﬁnite cone is another important problem, to which our hierarchies can also be applied. It follows from the proof of Proposition 8 that if A is not completely positive then, for some order t, the program ξtcp(A) is infeasible or its optimum value is larger than the Caratheodory bound on the cp-rank (which is similar to an earlier result in [58]). In the noncommutative setting the situation is more complicated: If ξ∗cpsd(A) is feasible, then A ∈ CS+, and if A  ∈ CSn+,vN, then ξ∞cpsd(A) is infeasible (Propositions 1 and 2). Here CSn+,vN is the cone deﬁned in [18] consisting of the matrices admitting a factorization in a von Neumann algebra with a trace. By Lemma 12, CSn+,vN can equivalently be characterized as the set of matrices of the form α (τ(aiaj)) for someC∗-algebra A with tracial state τ, positive elements a1,...,an ∈ A and α ∈ R+.

Our lower bounds are on the complex version of the (completely) positive semideﬁnite rank. As far as we are aware, the existing lower bounds (except for the dimension counting rank lower bound) are also on the complex (completely) positive semideﬁnite rank. It would be interesting to ﬁnd a lower bound on the real (completely) positive semideﬁnite rank that can go beyond the complex (completely) positive semideﬁnite rank.

We conclude with some open questions regarding applications of lower bounds on matrix factorization ranks. First, as was shown in [62,39,63], completely positive semideﬁnite matrices whose cpsd-rankC is larger than their size do exist, but currently we do not know how to construct small examples for which this holds. Hence, a concrete question: Does there exist a 5×5 completely positive semideﬁnite matrix whose cpsd-rankC is at least 6? Second, as we mentioned before, the asymmetric setting corresponds to (semideﬁnite) extension complexity of polytopes. Rothvoß’ result [66] (indirectly) shows that the parameter ξ∞+ is exponential (in the number of nodes of the graph) for the slack matrix of the matching polytope. Can this result also be shown directly using the dual formulation of ξ∞+, that is, by a sum-of-squares certiﬁcate? If so, could one extend the argument to the noncommutative setting (which would show a lower bound on the semideﬁnite extension complexity)?

Acknowledgements The authors would like to thank Sabine Burgdorf for helpful discussions and an anonymous referee for suggestions that helped improve the presentation.

#### A Commutative and tracial polynomial optimization

In this appendix we discuss known convergence and ﬂatness results for commutative and tracial polynomial optimization. We present these results in such a way that they can be directly used for our hierarchies of lower bounds on matrix factorization ranks. Although the commutative case was developed ﬁrst, here we treat the commutative and tracial cases together. For the reader’s convenience we provide all proofs by working on the “moment side”; that is, relying on properties of linear functionals rather than using real algebraic results on sums of squares. Tracial optimization is an adaptation of eigenvalue optimization as developed in [61], but here we only discuss the commutative and tracial cases, as these are most relevant to our work.

- A.1 Flat extensions and representations of linear forms


The optimization variables in the optimization problems considered in this paper are linear forms on spaces of (noncommutative) polynomials. To study the properties of the bounds obtained through these optimization problems we need to study properties and representations of (ﬂat) linear forms on polynomial spaces.

In Section 1.3 the key examples of symmetric tracial linear functionals on R x 2t are trace evaluations on a (ﬁnite dimensional) C∗-algebra. In this section we present some results that provide conditions under which, conversely, a symmetric tracial linear map on R x 2t (t ∈ N∪{∞}) that is nonnegative on M(S) and zero on I (T) arises from trace evaluations at elements in the intersection of the C∗-algebraic analogs of the matrix positivity domain of S and the matrix ideal of T. In Theorems 1 and 2 we consider the case t = ∞ and in Theorem 3 we consider the case t ∈ N. Results like these can for instance be used to link the linear forms arising in the limiting optimization problems of our hierarchies to matrix factorization ranks.

The proofs of Theorems 1 and 2 use a classical Gelfand–Naimark–Segal (GNS) construction. In these proofs it will also be convenient to work with the concept of the null space of a linear functional L ∈ R x ∗2t,

which is deﬁned as the vector space Nt(L) = p ∈ R x t : L(qp) = 0 for q ∈ R x t .

We use the notation N(L) = N∞(L) for the nontruncated null space. Recall that Mt(L) is the moment matrix associated to L, its rows and columns are indexed by words in x t, and its entries are given by Mt(L)w,w = L(w∗w ) for w,w ∈ x t. The null space of L can therefore be identiﬁed with the kernel of Mt(L): A polynomial p = ∑w cww belongs to Nt(L) if and only if its coefﬁcient vector (cw) belongs to the kernel of Mt(L).

In Section 1.3 we deﬁned a linear functional L ∈ R x ∗2t to be δ-ﬂat based on the rank stabilization property (4) of its moment matrix: rank(Mt(L)) = rank(Mt−δ(L)). This deﬁnition can be reformulated in terms of a decomposition of the corresponding polynomial space using the null space: the form L is δ-ﬂat if and only if

R x t = R x t−δ +Nt(L). Recall that L is said to be ﬂat if it is δ-ﬂat for some δ ≥ 1. Finally, in the nontruncated case (t = ∞) L was called ﬂat if rank(M(L)) < ∞. We can now see that rank(M(L)) < ∞ if and only if there exists an integer s ∈ N such that R x = R x s +N(L).

Theorem 1 below is implicit in several works (see, e.g., [57,17]). Here we assume that M(S)+I (T) is Archimedean, which we recall means that there exists a scalar R > 0 such that

n

∑

xi2 ∈ M(S)+I (T).

R−

i=1

- Theorem 1 Let S ⊆ SymR x and T ⊆ R x with M(S) + I (T) Archimedean. Given a linear form


- L ∈ R x ∗, the following are equivalent:


- (1) L is symmetric, tracial, nonnegative on M(S), zero on I (T), and L(1) = 1;
- (2) there is a unital C∗-algebra A with tracial state τ and X ∈ DA (S)∩VA (T) with L(p) = τ(p(X)) for all p ∈ R x . (29)


Proof We ﬁrst prove the easy direction (2) ⇒ (1): We have L(p∗) = τ(p∗(X)) = τ(p(X)∗) = τ(p(X)) = L(p) = L(p),

where we use that τ is Hermitian and Xi∗ = Xi for i ∈ [n]. Moreover, L is tracial since τ is tracial. In addition, for g ∈ S∪{1} and p ∈ R x we have

###### L(p∗gp) = τ(p∗(X)g(X)p(X)) = τ(p(X)∗g(X)p(X)) ≥ 0,

since g(X) is positive in A as X ∈ DA (S) and τ is positive. Similarly L(hq) = τ(h(X)q(X)) = 0 for all h ∈ T, since X ∈ VA (T).

We show (1) ⇒ (2) by applying a GNS construction. Consider the quotient vector space R x /N(L), and denote the class of p in R x /N(L) by p. We can equip this quotient with the inner product p,q = L(p∗q) for p,q ∈ R x , so that the completion H of R x /N(L) is a separable Hilbert space. As N(L) is a left ideal in R x , the operator

Xi : R x /N(L) → R x /N(L), p  → xip (30) is well deﬁned. We have

Xi p,q = L((xip)∗q) = L(p∗xiq) = p,Xiq for all p,q ∈ R x ,

so the Xi are self-adjoint. Since g ∈ S ∪ {1} is symmetric and p,g(X)p = p,gp = L(p∗gp) ≥ 0 for all p we have g(X) 0. By the Archimedean condition, there exists an R > 0 such that R − ∑ni=1 xi2 ∈ M(S)+I (T). Using R−xi2 = (R−∑nj=1 x2j)+∑j =i x2j ∈ M(S)+I (T) we get

Xip,Xip = L(p∗xi2p) ≤ R·L(p∗p) = R p, p for all p ∈ R x .

So each Xi extends to a bounded self-adjoint operator, also denoted Xi, on the Hilbert space H such that g(X) is positive for all g ∈ S∪{1}. Moreover, we have f,h(X)1 = L(f∗h) = 0 for all f ∈ R x ,h ∈ T.

The operators Xi ∈ B(H ) extend to self-adjoint operators in B(C⊗R H ), where C⊗R H is the complexiﬁcation of H . Let A be the unital C∗-algebra obtained by taking the operator norm closure of R X ⊆ B(C⊗R H ). It follows that X ∈ DA (S)∩VA (T).

Deﬁne the state τ on A by τ(a) = 1,a1 for a ∈ A . For all p,q ∈ R x we have τ(p(X)q(X)) = 1, p(X)q(X)1 = 1, pq = L(pq), (31)

so that the restriction of τ to R X is tracial. Since R X is dense in A in the operator norm, this implies τ is tracial.

To conclude the proof, observe that (29) follows from (31) by taking q = 1.

The next result can be seen as a ﬁnite dimensional analogue of the above result, where we do not need M(S)+I (T) to be Archimedean, but instead we assume the rank of M(L) to be ﬁnite (i.e., L to be ﬂat). In addition to the Gelfand–Naimark–Segal construction, the proof uses Artin–Wedderburn theory. For the unconstrained case the proof of this result can be found in [16], and in [17,43] this result is extended to the constrained case.

- Theorem 2 For S ⊆ SymR x , T ⊆ R x , and L ∈ R x ∗, the following are equivalent:

- (1) L is a symmetric, tracial, linear form with L(1) = 1 that is nonnegative on M(S), zero on I (T), and has rank(M(L)) < ∞;
- (2) there is a ﬁnite dimensional C∗-algebra A with a tracial state τ, and X ∈ DA (S)∩VA (T) satisfying equation (29);
- (3) L is a convex combination of normalized trace evaluations at points in D(S)∩V (T).


Proof ((1) ⇒ (2)) Here we can follow the proof of Theorem 1, with the extra observation that the condition rank(M(L)) < ∞ implies that the quotient space R x /N(L) is ﬁnite dimensional. Since R x /N(L) is ﬁnite dimensional the multiplication operators are bounded, and the constructed C∗-algebra A is ﬁnite dimensional.

((2) ⇒ (3)) By Artin-Wedderburn theory there exists a ∗-isomorphism

ϕ : A →

M

m=1

Cdm×dm for some M ∈ N, d1,...,dM ∈ N.

Deﬁne the ∗-homomorphisms ϕm : A → Cdm×dm for m ∈ [M] by ϕ = ⊕Mm=1ϕm. Then, for each m ∈ [M], the map Cdm×dm → C deﬁned by X  → τ(ϕm−1(X)) is a positive tracial linear form, and hence it is a nonnegative multiple λmtr(·) of the normalized matrix trace (since, for a full matrix algebra, the normalized trace is the unique tracial state). Then we have τ(a) = ∑m λm tr(ϕm(a)) for all a ∈ A . So τ(·) = ∑m λmtr(·) for nonnegative scalars λm with ∑m λm = L(1) = 1. By deﬁning the matrices Xim = ϕm(Xi) for m ∈ [M], we get

L(p) = τ(p(X1,...,Xn)) =

M

∑

m=1

λm tr(p(X1m,...,Xnm)) for all p ∈ R x .

Since ϕm is a ∗-homomorphism we have g(X1m,...,Xnm) 0 for all g ∈ S∪{1} and also h(X1m,...,Xnm) = 0

- for all h ∈ T, which shows (X1m,...,Xnm) ∈ D(S)∩V (T). ((3) ⇒ (1)) If L is a conic combination of trace evaluations at elements from D(S)∩V (T), then L


is symmetric, tracial, nonnegative on M(S), zero on I (T), and satisﬁes rank(M(L)) < ∞ because the moment matrix of any trace evaluation has ﬁnite rank.

The previous two theorems were about linear functionals deﬁned on the full space of noncommutative polynomials. The following result claims that a ﬂat linear functional on a truncated polynomial space can be extended to a ﬂat linear functional on the full space of polynomials while preserving the same positivity properties. It is due to Curto and Fialkow [20] in the commutative case and extensions to the noncommutative case can be found in [61] (for eigenvalue optimization) and [16] (for trace optimization).

- Theorem 3 Let 1 ≤ δ ≤ t < ∞, S ⊆ SymR x 2δ, and T ⊆ R x 2δ. Suppose L ∈ R x ∗2t is symmetric, tracial, δ-ﬂat, nonnegative on M2t(S), and zero on I2t(T). Then L extends to a symmetric, tracial, linear form on R x that is nonnegative on M(S), zero on I (T), and whose moment matrix has ﬁnite rank.


Proof LetW ⊆  x t−δ index a maximum nonsingular submatrix of Mt−δ(L), and let span(W) be the linear space spanned by W. We have the vector space direct sum

R x t = span(W)⊕Nt(L). (32) That is, for each u ∈ x t there exists a unique ru ∈ span(W) such that u−ru ∈ Nt(L).

We ﬁrst construct the (unique) symmetric ﬂat extension Lˆ ∈ R x 2t+2 of L. For this we set Lˆ(p) = L(p) for deg(p) ≤ 2t, and we set

Lˆ(u∗xiv) = L(u∗xirv) and Lˆ((xiu)∗xjv) = L((xiru)∗xjrv)

- for all i, j ∈ [n] and u,v ∈  x with |u| = |v| =t. One can verify that Lˆ is symmetric and satisﬁes xi(u−ru) ∈ Nt+1(Lˆ) for all i ∈ [n] and u ∈ R x t, from which it follows that Lˆ is 2-ﬂat.


We also have (u−ru)xi ∈ Nt+1(Lˆ) for all i ∈ [n] and u ∈ R x t: Since Lˆ is 2-ﬂat, we have (u−ru)xi ∈ Nt+1(Lˆ) if and only if Lˆ(p(u − ru)xi) = 0 for all p ∈ R x t−1. By using deg(xip) ≤ t, L is tracial, and u−ru ∈ Nt(L), we get Lˆ(p(u−ru)xi) = L(p(u−ru)xi) = L(xip(u−ru)) = 0.

By consecutively using (v−rv)xj ∈ Nt+1(Lˆ), symmetry of Lˆ, xi(u−ru) ∈ Nt+1(Lˆ), and again symmetry of Lˆ, we see that

Lˆ((xiu)∗vxj) = Lˆ((xiu)∗rvxj) = Lˆ((rvxj)∗xiu) = Lˆ((rvxj)∗xiru) = Lˆ((xiru)∗rvxj), (33) and in an analogous way one can show

Lˆ((uxi)∗xjv) = Lˆ((ruxi)∗xjrv). (34)

We can now show that Lˆ is tracial. We do this by showing that Lˆ(wxj) = Lˆ(xjw) for all w with deg(w) ≤ 2t+1. Notice that when deg(w) ≤ 2t−1 the statement follows from the fact that Lˆ is an extension of L. Suppose w = u∗v with deg(u) = t +1 and deg(v) ≤ t. We write u = xiu , and we let ru ,rv ∈ R x t−1 be such that u −ru ,v−rv ∈ Nt(L). We then have

Lˆ(wxj) = Lˆ(u∗vxj) = Lˆ((xiu )∗vxj)

= Lˆ((xiru )∗rvxj) by (33) = L((xiru )∗rvxj) since deg(xiru rvxj) ≤ 2t = L((ru xj)∗xirv) since L is tracial = Lˆ((ru xj)∗xirv) since deg((ru xj)∗xirv) ≤ 2t = Lˆ((u xj)∗xiv) by (34) = Lˆ(xjw).

It follows Lˆ is a symmetric tracial ﬂat extension of L, and rank(M(Lˆ)) = rank(M(L)).

Next, we iterate the above procedure to extend L to a symmetric tracial linear functional Lˆ ∈ R x ∗. It remains to show that Lˆ is nonnegative on M(S) and zero on I (T). For this we make two observations:

- (i) I (Nt(L)) ⊆ N(Lˆ).
- (ii) R x = span(W)⊕I (Nt(L)).


For (i) we use the (easy to check) fact that Nt(L) = span({u−ru : u ∈ x t}). Then it sufﬁces to show that w(u−ru) ∈ N(Lˆ) for all w ∈ x , which can be done using induction on |w|. From (i) one easily deduces that span(W)∩N(Lˆ) = {0}, so we have the direct sum span(W)⊕I (Nt(L)). The claim (ii) follows using induction on the length of w ∈ x : The base case w ∈ x t follows from (32). Let w = xiv ∈ x and assume v ∈ span(W)⊕I (Nt(L)), that is, v = rv +qv where rv ∈ span(W) and qv ∈ I (Nt(L)). We have xiv = xirv +xiqv so it sufﬁces to show xirv,xiqv ∈ span(W)⊕I (Nt(L)). Clearly xiqv ∈ I (Nt(L)), since qv ∈ I (Nt(L)). Also, observe that xirv ∈ R x t and therefore xirv ∈ span(W)⊕I (Nt(L)) by (32).

We conclude the proof by showing that Lˆ is nonnegative on M(S) and zero on I (T). Let g ∈ M(S), h ∈ I (T), and p ∈ R x . For p ∈ R x we extend the deﬁnition of rp so that rp ∈ span(W) and p−rp ∈ I (Nt(L)), which is possible by (ii). Then,

Lˆ(p∗gp) (=i) Lˆ(p∗grp) = Lˆ(r∗pgp) (=i) Lˆ(r∗pgrp) = L(r∗pgrp) ≥ 0,

Lˆ(p∗h) = Lˆ(h∗p) (=i) Lˆ(h∗rp) = Lˆ(rph) = L(rph) = 0, where we use deg(r∗pgrp) ≤ 2(t −δ)+2δ = 2t and deg(rph) ≤ (t −δ)+2δ ≤ 2t.

Combining Theorems 2 and 3 gives the following result, which shows that a ﬂat linear form can be extended to a conic combination of trace evaluation maps. It was ﬁrst proven in [43, Proposition 6.1] (and in [16] for the unconstrained case).

Corollary 1 Let 1 ≤ δ ≤ t < ∞, S ⊆ SymR x 2δ, and T ∈ R x 2δ. If L ∈ R x ∗2t is symmetric, tracial, δ-ﬂat, nonnegative on M2t(S), and zero on I2t(T), then it extends to a conic combination of trace evaluations at elements of D(S)∩V (T).

- A.2 Specialization to the commutative setting


The material from Appendix A.1 can be adapted to the commutative setting. Throughout [x] denotes the set of monomials in x1,...,xn, i.e., the commutative analog of x .

The moment matrix Mt(L) of a linear form L ∈ R[x]∗2t is now indexed by the monomials in [x]t, where we set Mt(L)w,w = L(ww ) for w,w ∈ [x]t. Due to the commutativity of the variables, this matrix is smaller and more entries are now required to be equal. For instance, the (x2x1,x3x4)-entry of M2(L) is equal to its (x3x1,x2x4)-entry, which does not hold in general in the noncommutative case.

Given a ∈ Rn, the evaluation map at a is the linear map La ∈ R[x]∗ deﬁned by La(p) = p(a1,...,an) for all p ∈ R[x].

We can view La as a trace evaluation at scalar matrices. Moreover, we can view a trace evaluation map at a tuple of pairwise commuting matrices as a conic combination of evaluation maps at scalars by simultaneously diagonalizing the matrices.

The quadratic module M(S) and the ideal I (T) have immediate specializations to the commutative setting. We recall that in the commutative setting the (scalar) positivity domain and scalar variety of sets S,T ⊆ R[x] are given by

D(S) = a ∈ Rn : g(a) ≥ 0 for g ∈ S , V(T) = a ∈ Rn : h(a) = 0 for h ∈ T .3 (35)

We ﬁrst give the commutative analogue of Theorem 1, where we give an additional integral representation in point (3). The equivalence of points (1) and (3) is proved in [64] based on Putinar’s Positivstellensatz. Here we give a direct proof on the “moment side” using the Gelfand representation.

- Theorem 4 Let S,T ⊆ R[x] with M(S)+I (T) Archimedean. For L ∈ R[x]∗, the following are equivalent:


- (1) L is nonnegative on M(S), zero on I (T), and L(1) = 1;
- (2) there exists a unital commutative C∗-algebra A with a state τ and X ∈ DA (S)∩VA (T) such that L(p) = τ(p(X)) for all p ∈ R[x];
- (3) there exists a probability measure µ on D(S)∩V(T) such that


###### L(p) =

p(x)dµ(x) for all p ∈ R[x].

D(S)∩V(T)

Proof ((1) ⇒ (2)) This is the commutative analogue of the implication (1) ⇒ (2) in Theorem 1 (observing in addition that the operators Xi in (30) pairwise commute so that the constructed C∗-algebra A is commutative).

((2) ⇒ (3)) Let A denote the set of unital ∗-homomorphisms A → C, known as the spectrum of A . We equip A with the weak-∗ topology, so that it is compact as a result of A being unital (see, e.g., [10, II.2.1.4]). The Gelfand representation is the ∗-isomorphism

Γ : A → C( A ), Γ(a)(φ) = φ(a) for a ∈ A , φ ∈ A ,

3 Note that in the commutative setting we could avoid using the variety sinceV(T) = D(±T). However, in the noncommutative setting, the polynomials in T need not be symmetric in which case the quadratic module D(±T) would not be well deﬁned.

where C( A ) is the set of complex-valued continuous functions on A . Since Γ is an isomorphism, the state τ on A induces a state τ on C( A ) deﬁned by τ (Γ(a)) = τ(a) for a ∈ A . By the Riesz representation theorem (see, e.g., [67, Theorem 2.14]) there is a Radon measure ν on A such that

Γ(a)(φ)dν(φ) for all a ∈ A . We then have

###### τ (Γ(a)) =

A

###### L(p) = τ(p(X)) = τ (Γ(p(X))) =

###### Γ(p(X))(φ)dν(φ) =

φ(p(X))dν(φ)

A

A

###### p(φ(X1),...,φ(Xn))dν(φ) =

p(f(φ))dν(φ) =

p(x)dµ(x),

###### =

Rn

A

A

where f : A → Rn is deﬁned by φ  → (φ(X1),...,φ(Xn)), and where µ = f∗ν is the pushforward measure of ν by f; that is, µ(B) = ν(f−1(B)) for measurable B ⊆ Rn.

Since X ∈ DA (S), we have g(X) 0 for all g ∈ S, hence Γ(g(X)) is a positive element of C( A ), implying g(φ(X1),...,φ(Xn)) = φ(g(X)) = Γ(g(X))(φ) ≥ 0. Similarly we see h(φ(X1),...,φ(Xn)) = 0 for all h ∈ T. So, the range of f is contained in D(S)∩V(T), µ is a probability measure on D(S)∩V(T) since L(1) = 1, and we have L(p) = D(S)∩V(T) p(x)dµ(x) for all p ∈ R[x].

((3) ⇒ (1)) This is immediate.

Note that the more common proof for the implication (1) ⇒ (3) in Theorem 4 relies on Putinar’s Positivstellensatz [64]: if L satisﬁes (1) then L(p) ≥ 0 for all polynomials p nonnegative on D(S) ∩V(T) (since p+ε ∈ M(S)+I (T) for any ε > 0), and thus L has a representing measure µ as in (3) by the Riesz-Haviland theorem [41].

The following is the commutative analogue of Theorem 2.

- Theorem 5 For S ⊆ R[x], T ⊆ R[x], and L ∈ R[x]∗, the following are equivalent:

- (1) L is nonnegative on M(S), zero on I (T), has rank(M(L)) < ∞, and L(1) = 1;
- (2) there is a ﬁnite dimensional commutativeC∗-algebra A with a state τ, and X ∈ DA (S)∩VA (T) such that L(p) = τ(p(X)) for all p ∈ R[x];
- (3) L is a convex combination of evaluations at points in D(S)∩V(T).


Proof ((1) ⇒ (2)) We indicate how to derive this claim from its noncommutative analogue. For this denote the commutative version of p ∈ R x by pc ∈ R[x]. For any g ∈ S and h ∈ T, select symmetric polynomials

- g ,h ∈ R x with (g )c = g and (h )c = h, and set S = g : g ∈ S ⊆ R x and T = h : h ∈ T ∪ xixj −xjxi ∈ R x : i, j ∈ [n], i = j ⊆ R x .

Deﬁne the linear form L ∈ R x ∗ by L (p) = L(pc) for p ∈ R x . Then L is symmetric, tracial, nonnegative on M(S ), zero on I (T ), and satisﬁes rankM(L ) = rankM(L) < ∞. Following the proof of the implication (1) ⇒ (2) in Theorem 1, we see that the operators X1,...,Xn pairwise commute (since X ∈ VA (T ) and T contains all xixj −xjxi) and thus the constructed C∗-algebra A is ﬁnite dimensional and commutative.

- ((2) ⇒ (3)) Here we follow the proof of this implication in Theorem 2 and observe that since A is

ﬁnite dimensional and commutative, it is ∗-isomorphic to an algebra of diagonal matrices (dm = 1 for all m ∈ [M]), which gives directly the desired result.

- ((3) ⇒ (1)) is easy. The next result, due to Curto and Fialkow [20], is the commutative analogue of Corollary 1.


Theorem 6 Let 1 ≤ δ ≤ t < ∞ and S,T ⊆ R[x]2δ. If L ∈ R[x]∗2t is δ-ﬂat, nonnegative on M2t(S), and zero on I2t(T), then L extends to a conic combination of evaluation maps at points in D(S)∩V(T).

Proof Here too we derive the result from its noncommutative analogue in Corollary 1. As in the above proof for the implication (1) =⇒ (2) in Theorem 5, deﬁne the sets S ,T ⊆ R x and the linear form L ∈ R x ∗2t by L (p) = L(pc) for p ∈ R x 2t. Then L is symmetric, tracial, nonnegative on M2t(S ), zero on I2t(T ), and δ-ﬂat. By Corollary 1, L is a conic combination of trace evaluation maps at elements of D(S )∩V (T ). It sufﬁces now to observe that such a trace evaluation LX is a conic combination of (scalar) evaluations at elements of D(S)∩V(T). Indeed, as X ∈ V (T ), the matrices X1,...,Xn pairwise commute and thus can be assumed to be diagonal. Since X ∈ D(S ) ∩ V (T ), we have g(X) 0 for g ∈ S and

- h (X) = 0 for h ∈ T . This implies g((X1)j j,...,(Xn)j j) ≥ 0 and h((X1)j j,...,(Xn)j j) = 0 for all g ∈ S, h ∈ T, and j ∈ [d]. Thus LX = ∑j Lrj, where rj = ((X1)j j,...,(Xn)j j) ∈ D(S)∩V(T).




Unlike in the noncommutative setting, here we also have the following result, which permits to express any linear functional L nonnegative on an Archimedean quadratic module as a conic combination of evaluations at points, when restricting L to polynomials of bounded degree.

- Theorem 7 Let S,T ⊆R[x] such that M(S)+I (T) is Archimedean. If L ∈R[x]∗ is nonnegative on M(S)


and zero on I (T), then for any integer k ∈ N the restriction of L to R[x]k extends to a conic combination of evaluations at points in D(S)∩V(T).

Proof By Theorem 4 there exists a probability measure µ on D(S) such that

p(x)dµ(x) for all p ∈ R[x].

###### L(p) = L(1)

D(S)∩V(T)

A general version of Tchakaloff’s theorem, as explained in [5], shows that there exist r ∈ N, scalars λ1,...,λr > 0 and points x1,...,xr ∈ D(S) such that

r

∑

p(x)dµ(x) =

λip(xi) for all p ∈ R[x]k.

D(S)∩V(T)

i=1

Hence the restriction of L to R[x]k extends to a conic combination of evaluations at points in D(S).

- A.3 Commutative and tracial polynomial optimization


We brieﬂy discuss here the basic polynomial optimization problems in the commutative and tracial settings. We recall how to design hierarchies of semideﬁnite programming based bounds and we give their main convergence properties. The classical commutative polynomial optimization problem asks to minimize a polynomial f ∈ R[x] over a feasible region of the form D(S) as deﬁned in (35):

f∗ = infa∈D(S) f(a) = inf f(a) : a ∈ Rn, g(a) ≥ 0 for g ∈ S .

In tracial polynomial optimization, given f ∈ SymR x , this is modiﬁed to minimizing tr(f(X)) over a feasible region of the form D(S) as in (6):

###### f∗tr = infX∈D(S)tr(f(X)) = inf tr(f(X)) : d ∈ N, X ∈ (Hd)n, g(X) 0 for g ∈ S ,

where the inﬁmum does not change if we replace Hd by Sd. Commutative polynomial optimization is recovered by restricting to 1×1 matrices.

For the commutative case, Lasserre [46] and Parrilo [60] have proposed hierarchies of semideﬁnite programming relaxations based on sums of squares of polynomials and the dual theory of moments. This approach has been extended to eigenvalue optimization [61,57] and later to tracial optimization [15,43]. The starting point in deriving these relaxations is to reformulate the above problems as minimizing L(f) over all normalized trace evaluation maps L at points in D(S) or D(S), and then to express computationally tractable properties satisﬁed by such maps L.

For S∪{f} ⊆ R[x] and deg(f)/2 ≤ t ≤ ∞, recall the (truncated) quadratic module M2t(S) M2t(S) = cone gp2 : p ∈ R[x], g ∈ S∪{1}, deg(gp2) ≤ 2t , which we use to formulate the following semideﬁnite programming lower bound on f∗:

ft = inf L(f) : L ∈ R[x]∗2t, L(1) = 1, L ≥ 0 on M2t(S) . For t ∈ N we have ft ≤ f∞ ≤ f∗.

In the same way, for S∪{f} ⊆ SymR x and t such that deg(f)/2 ≤ t ≤ ∞, we have the following semideﬁnite programming lower bound on f∗tr:

fttr = inf L(f) : L ∈ R x ∗2t tracial and symmetric, L(1) = 1, L ≥ 0 on M2t(S) , where we now use deﬁnition (1) for M2t(S).

The next theorem from [46] gives fundamental convergence properties for the commutative case; see also, e.g., [47,49] for a detailed exposition.

- Theorem 8 Let 1 ≤ δ ≤ t < ∞ and S∪{f} ⊆ R[x]2δ with D(S) = 0/.

- (i) If M(S) is Archimedean, then ft → f∞ as t → ∞, the optimal values in f∞ and f∗ are attained, and f∞ = f∗.
- (ii) If ft admits an optimal solution L that is δ-ﬂat, then L is a convex combination of evaluation maps at global minimizers of f in D(S), and ft = f∞ = f∗.


Proof (i) By repeating the ﬁrst part of the proof of Theorem 9 in the commutative setting we see that ft → f∞ and that the optimum is attained in f∞. Let L be optimal for f∞ and let k be greater than deg(f) and deg(g) for g ∈ S. By Theorem 7, the restriction of L to R[x]k extends to a conic combination of evaluations at points in D(S). It follows that this extension if feasible for f∗ with the same objective value, which shows f∞ = f∗.

(ii) This follows in the same way as the proof of Theorem 9(ii) below, where, instead of using Corollary 1, we now use its commutative analogue, Theorem 6.

To discuss convergence for the tracial case we need one more optimization problem: fIItr1 = inf τ(f(X)) : X ∈ DA (S), A is a unital C∗-algebra with tracial state τ .

This problem can be seen as an inﬁnite dimensional analogue of f∗tr: if we restrict to ﬁnite dimensional C∗algebras in the deﬁnition of fIItr1, then we recover the parameter f∗tr (use Theorem 2 to see this). Moreover, as we see in Theorem 9(ii) below, equality f∗tr = fIItr1 holds if some ﬂatness condition is satisﬁed. Whether fIItr1 = f∗tr is true in general is related to Connes’ embedding conjecture (see [44,43,17]).

Above we deﬁned the parameter fIItr1 using C∗-algebras. However, the following lemma shows that we get the same optimal value if we restrict to A being a von Neumann algebra of type II1 with separable predual, which is the more common way of deﬁning the parameter fIItr1 as is done in [43] (and justiﬁes the notation). We omit the proof of this lemma which relies on a GNS construction and algebraic manipulations, standard for algebraists.

Lemma 12 Let A be a C∗-algebra with tracial state τ and a1,...,an ∈ A . There exists a von Neumann algebra F of type II1 with separable predual, a faithful normal tracial state φ, and elements b1,...,bn ∈ F, so that for every p ∈ R x we have

τ(p(a1,...,an)) = φ(p(b1,...,bn)) and p(a1,...,an) is positive ⇐⇒ p(b1,...,bn) is positive. For all t ∈ N we have

fttr ≤ f∞tr ≤ fIItr1 ≤ f∗tr, where the last inequality follows by considering for A the full matrix algebra Cd×d. The next theorem from [43] summarizes convergence properties for these parameters, its proof uses Lemma 13 below.

- Theorem 9 Let 1 ≤ δ ≤ t < ∞ and S∪{f} ⊆ SymR x 2δ with D(S) = 0/.


- (i) If M(S) is Archimedean, then fttr → f∞tr as t → ∞, and the optimal values in f∞tr and fIItr1 are attained and equal.
- (ii) If fttr has an optimal solution L that is δ-ﬂat, then L is a convex combination of normalized trace evaluations at matrix tuples in D(S), and fttr = f∞tr = fIItr1 = f∗tr.


Proof We ﬁrst show (i). As M(S) is Archimedean, R−∑ni=1 xi2 ∈ M2d(S) for some R > 0 and d ∈ N. Since the bounds fttr are monotone nondecreasing in t and upper bounded by f∞tr, the limit limt→∞ fttr exists and it is at most f∞tr.

Fix ε > 0. For t ∈ N let Lt be a feasible solution to the program deﬁning fttr with value Lt(f) ≤ fttr+ε. As Lt(1) = 1 for all t we can apply Lemma 13 below and conclude that the sequence (Lt)t has a convergent subsequence. Let L ∈ R x ∗ be the pointwise limit. One can easily check that L is feasible for f∞tr. Hence we have f∞tr ≤ L(f) ≤ limt→∞ fttr +ε ≤ f∞tr +ε. Letting ε → 0 we obtain that f∞tr = limt→∞ fttr and L is optimal for f∞tr.

Next, since L is symmetric, tracial, and nonnegative on M(S), we can apply Theorem 1 to obtain a feasible solution (A ,τ,X) to fIItr1 satisfying (29) with objective value L(f). This shows f∞tr = fIItr1 and that the optima are attained in f∞tr and fIItr1.

Finally, part (ii) is derived as follows. If L is an optimal solution of fttr that is δ-ﬂat, then, by Corollary 1, it has an extension Lˆ ∈ R x ∗ that is a conic combination of trace evaluations at elements of D(S). This shows f∗tr ≤ Lˆ(f) = L(f), and thus the chain of equalities fttr = f∞tr = f∗tr = fΠtr1 holds.

We conclude with the following technical lemma, based on the Banach-Alaoglu theorem. It is a well known crucial tool for proving the asymptotic convergence result from Theorem 9(i) and it is used at other places in the paper.

Lemma 13 Let S ⊆ SymR x , T ⊆ R x , and assume R−(x12 +···+xn2) ∈ M2d(S)+I2d(T) for some d ∈ N and R > 0. For t ∈ N assume Lt ∈ R x ∗2t is tracial, nonnegative on M2t(S) and zero on I2t(T). Then we have |Lt(w)| ≤ R|w|/2Lt(1) for all w ∈ x 2t−2d+2. In addition, if supt Lt(1) < ∞, then {Lt}t has a pointwise converging subsequence in R x ∗.

Proof We ﬁrst use induction on |w| to show that Lt(w∗w) ≤ R|w|Lt(1) for all w ∈ x t−d+1. For this, assume Lt(w∗w) ≤ R|w|Lt(1) and |w| ≤ t −d. Then we have

Lt((xiw)∗xiw) = Lt(w∗(xi2 −R)w)+R·Lt(w∗w) ≤ R·R|w|Lt(1) = R|xiw|Lt(1).

For the inequality we use the fact that Lt(w∗(xi2 −R)w) ≤ 0 since w∗(R−xi2)w can be written as the sum of a polynomial in M2t(S)+I2t(T) and a sum of commutators of degree at most 2t, which follows using the following identity: w∗qhw = ww∗qh+[w∗qh,w]. Next we write any w ∈  x 2(t−d+1) as w = w∗1w2 with w1,w2 ∈ x t−d+1 and use the positive semideﬁniteness of the principal submatrix of Mt(Lt) indexed by {w1,w2} to get

Lt(w)2 = Lt(w∗1w2)2 ≤ Lt(w∗1w1)Lt(w∗2w2) ≤ R|w1|+|w2|Lt(1)2 = R|w|Lt(1)2. This shows the ﬁrst claim.

Suppose c := supt Lt(1) < ∞. For each t ∈ N, consider the linear functional Lˆt ∈ R x ∗ deﬁned by Lˆt(w) = Lt(w) if |w| ≤ 2t −2d +2 and Lˆt(w) = 0 otherwise. Then the vector (Lˆt(w)/(cR|w|/2))w∈ x lies in the supremum norm unit ball of R x , which is compact in the weak∗ topology by the Banach–Alaoglu

theorem. It follows that the sequence (Lˆt)t has a pointwise converging subsequence and thus the same holds for the sequence (Lt)t.

#### References

- 1. M.F. Anjos and J.B. Lasserre. Handbook on Semideﬁnite, Conic and Polynomial Optimization. International Series in Operations Research & Management Science Series, Springer, 2012.
- 2. MOSEK ApS. The MOSEK optimization toolbox for MATLAB manual. Version 8.0.0.81, 2017. URL http://docs.mosek.com/8.0/toolbox.pdf
- 3. A. Atserias, L. Manˇcinska, D. Roberson, R. S´ˇamal, S. Severini, and A. Varvitsiotis. Quantum and non-signalling graph isomorphisms. arXiv:1611.09837 (2016).
- 4. G.P. Barker, L.Q. Eiﬂer, and T.P. Kezlan. A non-commutative spectral theorem, Linear Algebra and its Applications 20(2) (1978), 95–100.
- 5. C. Bayer, J. Teichmann. The proof of Tchakaloff’s theorem. Proceedings of the American Mathematical Society 134 (2006), 3035–3040.
- 6. A. Berman, U.G. Rothblum. A note on the computation of the cp-rank. Linear Algebra and its Applications 419 (2006), 1–7.
- 7. A. Berman, N. Shaked-Monderer. Completely Positive Matrices. World Scientiﬁc, 2003.
- 8. M. Berta, O. Fawzi, V.B. Scholz. Quantum bilinear optimization. SIAM Journal on Optimization 26(3)

(2016), 1529–1564.

- 9. J. Bezanson, A. Edelman, S. Karpinski, V.B. Shah. Julia: A Fresh Approach to Numerical Computing. SIAM Review 59(1) (2017), 65–98.
- 10. B. Blackadar. Operator Algebras: Theory of C*-Algebras and Von Neumann Algebras. Encyclopaedia of Mathematical Sciences, Springer, 2006.
- 11. I.M. Bomze, W. Schachinger, R. Ullrich. From seven to eleven: Completely positive matrices with high cp-rank. Linear Algebra and its Applications 459 (2014), 208 – 221.
- 12. I.M. Bomze, W. Schachinger, R. Ullrich. New lower bounds and asymptotics for the cp-rank. SIAM Journal on Matrix Analysis and Applications 36 (2015), 20–37.
- 13. G. Braun, S. Fiorini, S. Pokutta, D. Steurer. Approximation limits of linear programs (beyond hierarchies). Mathematics of Operations Research 40(3) (2015), 756–772. Appeared earlier in FOCS’12.


- 14. S. Burer. On the copositive representation of binary and continuous nonconvex quadratic programs. Mathematical Programming 120(2) (2009), 479–495.
- 15. S. Burgdorf, K. Cafuta, I. Klep, J. Povh. The tracial moment problem and trace-optimization of polynomials. Mathematical Programming 137(1) (2013), 557–578.
- 16. S. Burgdorf, I. Klep. The truncated tracial moment problem. Journal of Operator Theory 68(1) (2012), 141–163.
- 17. S. Burgdorf, I. Klep, J. Povh. Optimization of Polynomials in Non-Commutative Variables. Springer Briefs in Mathematics, Springer, 2016.
- 18. S. Burgdorf, M. Laurent, T. Piovesan. On the closure of the completely positive semideﬁnite cone and linear approximations to quantum colorings. Electronic Journal of Linear Algebra 32 (2017), 15–40.
- 19. M. Conforti, G. Cornu´ejols, G. Zambelli. Extended formulations in combinatorial optimization. 4OR 8 (2010), 1–48.
- 20. R.E. Curto, L.A. Fialkow. Solution of the Truncated Complex Moment Problem for Flat Data. Memoirs of the American Mathematical Society, American Mathematical Society, 1996.
- 21. P. Dickinson, M. D¨ur. Linear-time complete positivity detection and decomposition of sparse matrices. SIAM Journal on Matrix Analysis and Applications 33(3) (2012), 701–720.
- 22. J.H. Drew, C.R. Johnson, R. Loewy. Completely positive matrices associated with M-matrices. Linear and Multilinear Algebra 37(4) (1994), 303–310.
- 23. K.J. Dykema, V.I. Paulsen, J. Prakash. Non-closure of the set of quantum correlations via graphs, arXiv:1709.05032 (2017).
- 24. J. Edmonds. Maximum matching and a polyhedron with 0,1 vertices. Journal of Research of the National Bureau of Standards 69 B (1965), 125–130.
- 25. Y. Faenza, S. Fiorini, R. Grappe, H. Tiwari. Extended formulations, non-negative factorizations and randomized communication protocols. Mathematical Programming 153(1) (2015), 75–94.
- 26. H. Fawzi, J. Gouveia, P.A. Parrilo, R.Z. Robinson, R.R. Thomas. Positive semideﬁnite rank. Mathematical Programming 153(1) (2015), 133–177.
- 27. H. Fawzi, P.A. Parrilo. Lower bounds on nonnegative rank via nonnegative nuclear norms. Mathematical Programming 153(1) (2015), 41–66.
- 28. H. Fawzi, P.A. Parrilo. Self-scaled bounds for atomic cone ranks: applications to nonnegative rank and cp-rank. Mathematical Programming 158(1) (2016), 417–465.
- 29. S. Fiorini, V. Kaibel, K. Pashkovich, D. Theis. Combinatorial bounds on nonnegative rank and extended formulations. Discrete Mathematics 313(1) (2013), 67–83.
- 30. S. Fiorini, S. Massar, S. Pokutta, H.R. Tiwary, R. de Wolf. Exponential lower bounds for polytopes in combinatorial optimization. Journal of the ACM 62(2) (2015), 17:1–17:23. Appeared earlier in STOC’12.
- 31. N. Gillis. Introduction to nonnegative matrix factorization. SIAG/OPT Views and News 25(1) (2017), 7–16.
- 32. N. Gillis, F. Glineur. On the geometric interpretation of the nonnegative rank. Linear Algebra and its Applications 437(11) (2012), 2685 – 2712.
- 33. M. Goemans. Smallest compact formulation for the permutahedron. Mathematical Programming 153(1) (2015), 5–11.
- 34. A.P. Goucha, J. Gouveia, P.M. Silva. On ranks of regular polygons. SIAM Journal on Discrete Mathematics 31(4) (2016), 2612–2625.
- 35. J. Gouveia, P.A. Parrilo, R.R. Thomas. Lifts of convex sets and cone factorizations. Mathematics of Operations Research 38(2) (2013), 248–264.
- 36. J. Gouveia, R.Z. Robinson, R.R. Thomas. Polytopes of minimum positive semideﬁnite rank. Discrete & Computational Geometry 50(3) (2013), 679–699.
- 37. M. Grant, S. Boyd. CVX: Matlab Software for Disciplined Convex Programming, version 2.1, 2014. http://cvxr.com/cvx
- 38. S. Gribling, D. de Laat, M. Laurent. Bounds on entanglement dimensions and quantum graph parameters via noncommutative polynomial optimization. Mathematical Programming Series B 171(1)

(2018), 5–42.

- 39. S. Gribling, D. de Laat, M. Laurent. Matrices with high completely positive semideﬁnite rank. Linear Algebra and its Applications 513 (2017), 122 – 148.
- 40. P. Groetzner, M. D¨ur. A factorization method for completely positive matrices. Preprint (2018), http: //www.optimization-online.org/DB_HTML/2018/03/6511.html.
- 41. E.K. Haviland. On the Momentum Problem for Distribution Functions in More Than One Dimension. II. American Journal of Mathematics 58(1) (1936), 164–168.


- 42. R. Jain, Y. Shi, Z. Wei, S. Zhang. Efﬁcient protocols for generating bipartite classical distributions and quantum states. IEEE Transactions on Information Theory 59(8) (2013), 5171–5178.
- 43. I. Klep, J. Povh. Constrained trace-optimization of polynomials in freely noncommuting variables. Journal of Global Optimization 64(2) (2016), 325–348.
- 44. I. Klep, M. Schweighofer. Connes’ embedding conjecture and sums of hermitian squares. Advances in Mathematics 217(4) (2008), 1816–1837.
- 45. E. de Klerk, D.V. Pasechnik. Approximation of the stability number of a graph via copositive programming. SIAM Journal on Optimization 12(4) (2002), 875–892.
- 46. J.B. Lasserre. Global optimization with polynomials and the problem of moments. SIAM Journal on Optimization 11(3) (2001), 796–817.
- 47. J.B. Lasserre. Moments, Positive Polynomials and Their Applications. Imperial College Press, 2009.
- 48. J.B. Lasserre. New approximations for the cone of copositive matrices and its dual. Mathematical Programming 144(1-2) (2014), 265–276.
- 49. M. Laurent. Sums of squares, moment matrices and optimization over polynomials. In Emerging Applications of Algebraic Geometry (M. Putinar, S. Sullivant eds.), Springer, 2009, pp. 157–270.
- 50. M. Laurent, T. Piovesan. Conic approach to quantum graph parameters using linear optimization over the completely positive semideﬁnite cone. SIAM Journal on Optimization 25(4) (2015), 2461–2493.
- 51. J.R. Lee, P. Raghavendra, D. Steurer. Lower bounds on the size of semideﬁnite programming relaxations. In Proceedings of the Forty-seventh Annual ACM Symposium on Theory of Computing, STOC’15, 2015, pp. 567–576.
- 52. T. Lee, Z. Wei, R. de Wolf. Some upper and lower bounds on psd-rank. Mathematical Programming 162(1) (2017), 495–521.
- 53. M. Gr¨otschel, L. Lov´asz., A. Schrijver. The ellipsoid method and its consequences in combinatorial optimization. Combinatorica 1(2) (1981), 169–197.
- 54. L. Manˇcinska, D. Roberson. Note on the correspondence between quantum correlations and the completely positive semideﬁnite cone. Available at quantuminfo.quantumlah.org/memberpages/ laura/corr.pdf (2014).
- 55. R.K. Martin. Using separation algorithms to generate mixed integer model reformulations. Operations Research Letters 10(3) (1991), 119–128.
- 56. D. Mond, J. Smith, D. van Straten. Stochastic factorizations, sandwiched simplices and the topology of the space of explanations. Proceedings of the Royal Society of London A: Mathematical, Physical and Engineering Sciences 459(2039) (2003), 2821–2845.
- 57. M. Navascu´es, S. Pironio, A. Ac´ın. SDP relaxations for non-commutative polynomial optimization. In Handbook on Semideﬁnite, Conic and Polynomial Optimization (M.F. Anjos, J.B. Lasserre eds.). Springer, 2012, pp. 601–634.
- 58. J. Nie. The A -truncated K-moment problem. Foundations of Computational Mathematics 14(6)

(2014), 1243–1276.

- 59. J. Nie. Symmetric tensor nuclear norms. SIAM Journal on Applied Algebra and Geometry 1(1) (2017), 599625.
- 60. P.A. Parrilo. Structured Semideﬁnite Programs and Semialgebraic Geometry Methods in Robustness and Optimization. PhD thesis, Caltech, 2000.
- 61. S. Pironio, M. Navascu´es, A. Ac´ın. Convergent relaxations of polynomial optimization problems with noncommuting variables. SIAM Journal on Optimization 20(5) (2010), 2157–2180.
- 62. A. Prakash, J. Sikora, A. Varvitsiotis, Z. Wei. Completely positive semideﬁnite rank. Mathematical Programming 171(12) (2017), 397–431.
- 63. A. Prakash, A. Varvitsiotis. Correlation matrices, Clifford algebras, and completely positive semideﬁnite rank. arXiv:1702.06305 (2017).
- 64. Putinar, M.: Positive polynomials on compact semi-algebraic sets. Indiana University Mathematics Journal 42, 969–984 (1993)
- 65. J. Renegar. On the computational complexity and geometry of the ﬁrst-order theory of the reals. Part I: Introduction. Preliminaries. The geometry of semi-algebraic sets. The decision problem for the existential theory of the reals. Journal of Symbolic Computation 13(3) (1992), 255 – 299.
- 66. T. Rothvoss. The matching polytope has exponential extension complexity. In Proceedings of the Forty-sixth Annual ACM Symposium on Theory of Computing, STOC’14, 2014, pp. 263–272.
- 67. W. Rudin. Real and complex analysis. Mathematics series. McGraw-Hill, 1987.
- 68. N. Shaked-Monderer, A. Berman, I.M. Bomze, F. Jarre, W. Schachinger. New results on the cp-rank and related properties of co(mpletely )positive matrices. Linear and Multilinear Algebra 63(2) (2015), 384–396.


- 69. N. Shaked-Monderer, I.M. Bomze, F. Jarre, W. Schachinger. On the cp-rank and minimal cp factorizations of a completely positive matrix. SIAM Journal on Matrix Analysis and Applications 34(2)

(2013), 355–368.

- 70. Y. Shitov. A universality theorem for nonnegative matrix factorizations. arXiv:1606.09068v2 (2016).
- 71. Y. Shitov. The complexity of positive semideﬁnite matrix factorization. SIAM Journal on Optimization 27(3) (2017), 1898–1909.
- 72. J. Sikora, A. Varvitsiotis. Linear conic formulations for two-party correlations and values of nonlocal games. Mathematical Programming 162(1) (2017), 431–463.
- 73. W. Slofstra. The set of quantum correlations is not closed. arXiv:1703.08618 (2017).
- 74. G. Tang, P. Shah. Guaranteed tensor decomposition: A moment approach. In Proceedings of the 32nd International Conference on International Conference on Machine Learning, ICML’15, 2015, pp. 1491–1500.
- 75. A. Vandaele, F. Glineur, N. Gillis. Algorithms for positive semideﬁnite factorization. arXiv:1707.07953v1 (2017).
- 76. S.A. Vavasis. On the complexity of nonnegative matrix factorization. SIAM Journal on Optimization 20(3) (2009), 1364–1377.
- 77. J.H.M. Wedderburn. Lectures on Matrices. Dover Publications Inc., 1964.
- 78. M. Yannakakis. Expressing combinatorial optimization problems by linear programs. Journal of Computer and System Sciences 43(3) (1991), 441 – 466.


