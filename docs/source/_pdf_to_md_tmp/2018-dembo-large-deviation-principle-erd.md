# arXiv:1804.11327v1[math.PR]30Apr2018

## A LARGE DEVIATION PRINCIPLE FOR THE ERDOS–R˝ ENYI´ UNIFORM RANDOM GRAPH

AMIR DEMBO AND EYAL LUBETZKY

Abstract. Starting with the large deviation principle (ldp) for the Erdo˝s–R´enyi binomial random graph G(n, p) (edge indicators are i.i.d.), due to Chatterjee and Varadhan (2011), we derive the ldp for the uniform random graph G(n, m) (the uniform distribution over graphs with n vertices and m edges), at suitable m = mn. Applying the latter ldp we ﬁnd that tail decays for subgraph counts in G(n, mn) are controlled by variational problems, which up to a constant shift, coincide with those studied by Kenyon et al. and Radin et al. in the context of constrained random graphs, e.g., the edge/triangle model.

1. Introduction

The Erd˝s–R´enyi binomial random graph model G(n,p) is the graph on n vertices where each edge is present independently with probability p; the uniform random graph G(n,m) is the uniform distribution over graphs with n vertices and exactly m edges.

Let W be the space of all bounded measurable functions f : [0,1]2 → R that are symmetric (f(x,y) = f(y,x) for all x,y ∈ [0,1]). Let W0 ⊂ W denote all graphons, that is, symmetric measurable functions [0,1]2 → [0,1] (these generalize ﬁnite graphs; see (1.2)). The cut-norm of W ∈ W is given by

W := sup

W(x,y) dxdy = sup

W(x,y)u(x)v(y) dxdy ,

u,v: [0,1]→[0,1] [0,1]2

S,T⊂[0,1] S×T

(by linearity of the integral it suﬃces to consider {0,1}-valued u,v, hence the equality). For any measure-preserving map σ: [0,1] → [0,1] and W ∈ W, let Wσ ∈ W denote the graphon Wσ(x,y) = W(σ(x),σ(y)). The cut-distance on W is then deﬁned as

W1 − W2σ ,

δ (W1,W2) := inf

σ

with the inﬁmum taken over all measure-preserving bijections σ on [0,1]. It yields the pseudo-metric space (W0,δ ), which is elevated into a genuine metric space ( W0,δ ) upon taking the quotient w.r.t. the equivalence relation W1 ∼ W2 iﬀ δ (W1,W2) = 0. In what may be viewed as a topological version of Szemer´edi’s regularity lemma, Lov´sz and Szegedy [11] showed that the metric space ( W0,δ ) is compact. For a ﬁnite simple graph H = (V (H),E(H)) with V (H) = {1,...,k}, its subgraph density in W ∈ W0 is

W(xi,xj) dx1 ···dxk ,

tH(W) :=

[0,1]k (i,j)∈E(H)

with the map W  → tH(W) being Lipschitz-continuous in ( W0,δ ) (see [2, Thm 3.7]). Deﬁne Ip: [0,1] → R by

- 1 − x

- 2


1 − x 1 − p

x p

x 2

for p ∈ (0,1) and x ∈ [0,1], (1.1)

Ip(x) :=

log

+

log

2010 Mathematics Subject Classiﬁcation. 05C80, 60F10. Key words and phrases. Large deviations, Erdo˝s–Re´nyi graphs, constrained random graphs.

1

and extend Ip to W0 via Ip(W) := [0,1]2 Ip(W(x,y)) dxdy for W ∈ W0. As Ip is convex on [0,1], it is lower-semicontinuous on W0 w.r.t. the cut-metric topology ([4, Lem. 2.1]).

In the context of the space of graphons W0, a simple graph G with vertices {1,...,n} can be represented by

WG(x,y) =

1 if ( nx , ny ) is an edge of G, 0 otherwise.

(1.2)

For two graphs G and H let hom(H,G) count the number of homomorphisms from H to G (i.e., maps V (H) → V (G) that carry edges to edges). Let

tH(G) := |V (G)|−|V (H)||hom(H,G)| = tH(WG).

A sequence of graphs {Gn}n≥1 is said to converge if the sequence of subgraph densities tH(Gn) converges for every ﬁxed ﬁnite simple graph H. It was shown in [11] that for any such convergent graph sequence there is a limit object W ∈ W0 such that tH(Gn) → tH(W) for every ﬁxed H. Conversely, any W ∈ W0 arises as a limit of a convergent graph sequence. It was shown in [2] that a sequence of graphs {Gn}n≥1 converges if and only if the sequence of graphons WGn ∈ W0 converges in W0 w.r.t. δ

A random graph Gn ∼ G(n,p) corresponds to a random point WGn ∈ W0—inducing a probability distribution P(Gn ∈ ·) on W0 supported on a ﬁnite set of points (n-vertex graphs)—and Gn → W for the constant graphon W ≡ p a.s. for every ﬁxed 0 < p < 1. Chatterjee and Varadhan [4] showed that, for 0 < p < 1 ﬁxed, the random graph G(n,p) obeys a large deviation principle (ldp) in ( W0,δ ) with the rate function Ip(·). Further denote W 1 = |W(x,y)|dxdy, and considering the restricted spaces

W0(p) := W ∈ W0 : W 1 = p and W0(p) = W ∈ W0 : W 1 = p , here we deduce the analogous statement for the random graph G(n,m), the uniform distribution over all graphs with n vertices and exactly m edges, with a rate function Jp(·) restricted to W0(p). As we later conclude, the variational formulas of this ldp for G(n,m), addressing such random graph structure conditioned on a large deviation, coincide with those studied earlier by Kenyon et al. and Radin et al. (cf., [7–9]).

Theorem 1.1. Fix 0 < p < 1 and let mn ∈ N be such that mn/ n2 → p as n → ∞. Let Gn ∼ G(n,mn). Then the sequence P(Gn ∈ ·) obeys the ldp in the space ( W0,δ ) with the good rate function Jp, where Jp(W) = Ip(W) if W ∈ W0(p) and is ∞ otherwise. That is, for any closed set F ⊆ W0,

n−2 log P(Gn ∈ F) ≤ − inf

limsup

Jp(W),

W∈F

n→∞

and for any open U ⊆ W0, liminf

n−2 log P(Gn ∈ U) ≥ − inf

Jp(W).

n→∞

W∈U

Deﬁne

φH(p,r) := inf Ip(W): W ∈ W0 , tH(W) ≥ r (1.3) and further let

ψH(p,r) := inf Ip(W): W ∈ W0(p) , tH(W) ≥ r (1.4)

(with Ip having compact level sets in ( W0,δ ) and tH(·) continuous on ( W0,δ ), the inﬁmums in (1.3),(1.4) are attained whenever the relevant set of graphons is nonempty). For any r ≥ tH(p) we relate the equivalent form of (1.4) (see Corollary 1.2), given by

ψH(p,r) = inf Ip(W): W ∈ W0(p) , tH(W) = r , (1.5) to the following variational problem that has been extensively studied (e.g., [7–9,14]) in constrained random graphs such as the edge/triangle model (where H is a triangle):

FH(p,r) := sup he(W): W ∈ W0(p) , tH(W) = r , (1.6)

where he(x) = −21(xlog x + (1 − x)log(1 − x)) is the (natural base) entropy function. As Ip(x) = −he(x) − x2 log p − 1−2x log(1 − p) and W 1 = p throughout W0(p), we see that both variational problems for FH and −ψH have the same set of optimizers, and FH(p,r) = −ψH(p,r) + he(p).

As a main application of their ldp, Chatterjee and Varadhan [4] showed that the large deviation rate function for subgraph counts in G(n,p) for any ﬁxed 0 < p < 1 and graph H reduces to the variational problem (1.3). Namely, if Gn ∼ G(n,p) then

n−2 log P(tH(Gn) ≥ r) = −φH(p,r) for every ﬁxed p,r ∈ (0,1) and H ,

lim

n→∞

and, on the event {tH(Gn) ≥ r}, the graph Gn is typically close to a minimizer of (1.3). Theorem 1.1 implies the analogous statement for the random graph G(n,mn) w.r.t. the variational problem (1.4) (similar statements hold for lower tails of subgraph counts both in case of G(n,p) and that of G(n,mn)).

Corollary 1.2. Fixing a subgraph H and 0 < p < 1, let rH ∈ (tH(p),1] denote the largest r for which the collection of graphons in (1.4) is nonempty.

- (a) The lsc function r  → ψH(p,r) is zero on [0,tH(p)] and ﬁnite, strictly increasing on [tH(p),rH]. The nonempty set F of minimizers of (1.4) is a single point W ≡ p for r ≤ tH(p) and F coincides for any r ∈ [tH(p),rH] with the minimizers of (1.5).
- (b) For any mn ∈ N such that mn/ n2 → p as n → ∞ and any right-continuity point r ∈ [0,rH) of t  → ψH(p,t), the random graph Gn ∼ G(n,mn) satisﬁes

lim

n→∞

n−2 log P(tH(Gn) ≥ r) = −ψH(p,r). (1.7)

- (c) For any (p,r) as in part (b), and every ε > 0 there is C = C(H,ε,p,r) > 0 so that for all n large enough


P δ (Gn,F ) ≥ ε tH(Gn) ≥ r ≤ e−Cn2 . (1.8)

- Remark 1.3. Since the function r  → ψH(p,r) is monotone, it is continuous a.e.; however, the identity (1.7) may fail when ψH(p,·) is discontinuous at r. For example, at r = rH the lhs of (1.7) equals −∞ whenever mn/ n2 ↑ p slowly enough.
- Remark 1.4. The analog of (1.7) in the sparse regime (with edge density pn = o(1)) has been established in [3] in terms of a discrete variational problem in lieu of (1.3),


valid when n−cH pn 1 for some cH > 0 (see also [6], improving the range of pn, and [1,12,13,15] for analyses of these variational problems in the sparse/dense regimes). In contrast with the delicate regime pn = n−c, such results in the range pn (log n)−c of G(n,p) are a straightforward consequence of the weak regularity lemma (cf. [13, §5]), and further extend to G(n,mn), where the discrete variational problem features an extra constraint on the number of edges (see Proposition 3.2).

Consider (p,r) in the setting of Corollary 1.2. The studies of the variational problem for FH given in (1.6) were motivated by the question of estimating the number of graphs with prescribed edge and H-densities, via the following relation:

|E(Gn)|/ n2 − p ≤ δ , |tH(Gn) − r| ≤ δ

1 n2

log |Hn,p,rδ | where Hn,p,rδ = Gn :

FH(p,r) = lim δ↓0

lim

.

n→∞

(This follows by general principles from the ldp of [4] for G(n,p); see Proposition 2.1(a), or [14, Thm 3.1] for the derivation in the special case of the edge/triangle model). Corollary 1.2 allows us, roughly speaking, to interchange the order of these two limits; for instance, for any right-continuity point r ≥ tH(p) of t  → ψH(p,t) (which holds a.e.), the same variational problem in (1.6) also satisﬁes

|E(Gn)| = m, tH(Gn) ≥ r

1 n2

log |Hn,mn,r| where Hn,m,r = Gn :

FH(p,r) = lim

. (1.9)

n→∞

(Indeed, −ψH(p,r) = limn→∞ n−2 log P(tH(G(n,mn)) ≥ r), and this log-probability is then translated to log |Hn,mn,r| by adding n−2 log (n2)

mn → he(p) = FH(p,r)+ψH(p,r).) For the various results (as well as numerical simulations for the many problems related

- to (1.6) that remain open), the reader is referred to [7–9] and the references therein.


Recall that the law of G(n,mn) can be represented as that of a random graph Gn from the model G(n,p), conditional on |E(Gn)| = mn. While our choice of mn in Theorem 1.1 is rather typical for G(n,p) when n 1, any ldp and in particular the ldp of [4], deals only with open and closed sets. The challenge in deriving Theorem 1.1 is thus in handling the point conditioning. To this end, we provide in Section 2 a general result (Proposition 2.1) for deriving a conditional ldp, which we then combine in §3.1 with a combinatorial coupling, and thereby prove Theorem 1.1. Building on the latter, §3.2 provides the proof of Corollary 1.2, whereas §3.3 is devoted to the analog of (1.7) for G(n,mn) in the range mn n2(log n)−cH (see Proposition 3.2).

2. Conditional LDP

The ldp for G(n,m) is obtained by the next result, whose proof mimics that of [5, Theorem 4.2.16] about exponential approximations (see [5, Deﬁnition 4.2.14]).

- Proposition 2.1. Suppose Borel probability measures {µn} on a metric space (X,d) satisfy the ldp with rate an → 0 and good rate function I(·). Fix a metric space (S,ρ), a continuous map f : (X,d) → (S,ρ) and s ∈ S. For every η > 0, let Znη denote radnom variables of the law


νnη := µn · | Bf,s,ηo , (2.1) where

Bf,s,η := {x ∈ X : ρ(s,f(x)) ≤ η} , Bf,s,ηo := {x ∈ X : ρ(s,f(x)) < η} .

- (a) If

lim

n→∞

an log µn(Bf,s,ηo ) = 0 for every η > 0 ﬁxed, (2.2) then for the good rate function

J0(x) :=

I(x), f(x) = s ∞, otherwise

and any open U ⊂ X and closed F ⊂ X, liminf

η→0

liminf

n→∞

an log νnη(U) ≥ − inf x∈U

J0(x), (2.3) limsup η→0

limsup

n→∞

an log νnη(F) ≤ − inf x∈F

J0(x). (2.4)

- (b) Suppose (2.2) holds and that {Znη} form an exponentially good approximation of variables Zn ∼ νn; i.e., for any δ > 0, there exist couplings Pn,η of (Zn,Znη) so that


an log Pn,η(d(Zn,Znη) > δ) = −∞. (2.5) Then {νn} satisfy the ldp with rate an → 0 and the good rate function J0(·).

lim

limsup

η↓0

n→∞

Proof. We ﬁrst deduce from (2.2) that for every η > 0, open U ⊂ X and closed F ⊂ X, liminf

Jηo(x), (2.6) limsup n→∞

an log νnη(U) ≥ − inf x∈U

n→∞

an log νnη(F) ≤ − inf x∈F

Jη(x), (2.7) where

I(x), x ∈ Bf,s,ηo ∞, otherwise.

I(x), x ∈ Bf,s,η ∞, otherwise

, Jηo(x) :=

Jη(x) :=

Indeed, for any Borel set A and η > 0,

µn(A ∩ Bf,s,η) µn(Bf,s,ηo )

µn(A ∩ Bf,s,ηo ) ≤ νnη(A) ≤

.

Hence, for any open set U, we deduce from the ldp for {µn} that liminf

Jηo(x). Similarly, for any closed set F it follows from (2.2) that

an log νnη(U) ≥ liminf

an log µn(U ∩ Bf,s,ηo ) ≥ − inf

I(x) = − inf

x∈U∩Bf,s,ηo

n→∞

n→∞

x∈U

an log νnη(F) ≤ limsup

I(x) = − inf

an log µn(F ∩ Bf,s,η) ≤ − inf

Jη(x).

limsup

x∈F

x∈F∩Bf,s,η

n→∞

n→∞

- (a). In the lower bound (2.6) one obviously can use J0(·) ≥ Jηo(·), yielding (2.3). Moreover, we get the bound (2.4) out of (2.7), upon showing that for any closed F ⊆ X,

inf

y∈F

{J0(y)} ≤ liminf

η↓0

inf

y∈F

{Jη(y)} := α. (2.8)

To this end, it suﬃces to consider only α < ∞, in which case Jη (y ) ≤ α+ −1 for some η ↓ 0 and y ∈ F. As {y } is contained in the compact level set {x : I(x) ≤ α + 1}, it has a limit point y ∈ F. Since Jη (y ) = I(y ) → α it follows from the lsc of x  → I(x) that I(y ) ≤ α. Passing to the convergent sub-sequence ρ(f(y ),f(y )) → 0. Further, recall that ρ(s,f(y )) ≤ η ↓ 0, hence by the triangle inequality ρ(s,f(y )) = 0. Consequently, J0(y ) = I(y ) ≤ α yielding (2.8) and completing the proof of part (a).

- (b). Clearly, Jη is a good rate function (namely, of compact level sets {x : Jη(x) ≤ α} = {x : I(x) ≤ α} ∩ Bf,s,η), and Jη ≤ Jηo ↑ J0. If Jηo ≡ Jη then (2.7)–(2.6) form the ldp for {νnη} with the good rate function Jη. While in general this may not be the case, assuming hereafter that (2.5) holds and proceeding as in [5, (4.2.20)], we get from


- (2.6) that {νn} satisﬁes the ldp lower bound with the rate function


{Jηo(z)},

J(y) := sup

liminf

inf

z∈By,δ

η↓0

δ>0

where By,δ = {z ∈ X : d(y,z) < δ} (see [5, (4.2.17)], noting that no ldp upper bound for νnη is needed here). Since y ∈ By,δ for any δ > 0, we have that

Jηo(y) ≥ J(y)

J0(y) = lim η↓0

and consequently {νn} trivially satisﬁes the ldp lower bound also with respect to the good rate function J0. Now, precisely as in the proof of [5, Theorem 4.2.16(b)], we get

- from (2.5) and (2.7) that the corresponding ldp upper bound holds for {νn}, thanks


- to (2.8) (see [5, (4.2.18)]), thereby completing the proof of part (b) of Prop. 2.1.

3. LDP for the uniform random graph

- 3.1. Proof of Theorem 1.1. Let µn be the law of G(n,p), which obeys the ldp with good rate function Ip(·) on ( W0,δ ) and speed n2, and let νn denote the law of G(n,mn). We shall apply Proposition 2.1(b) for S = R and s = p, with f denoting the L1-norm on graphons (edge density):


f(W) := W 1 = W(x,y) dxdy .

With these choices, the role of Zn will be assumed by Gn ∼ G(n,mn), whereas those of the random variables Znη will be assumed by the binomial random graph G(n,p) conditioned on having between 21(p − η)n2 and 12(p + η)n2 edges:

Gηn ∼ G(n,p) Bp,ηo , where Bp,ηo = G : 2|En(2G)| ∈ (p − η,p + η) (3.1)

Note that pn := 2mn/n2 ∈ (p − η,p + η) for all n ≥ n0(η). We couple (Gn,Gηn) so that for such n, detereministically,

|E(Gn) E(Gηn)| < ηn2 (3.2) (here S T denotes symmetric diﬀerence). This is achieved by the following procedure:

- (i) Draw Gn ∼ G(n,mn).
- (ii) Independently of Gn draw En ∼ Bin( n2 ,p) and Mn ∼ En | |2En/n2 − p| < η . Let Dn = Mn − mn and obtain Gηn from Gn as follows:


- • [shortage] if Dn ≥ 0: add a uniformly chosen subset of Dn edges missing from Gn.
- • [surplus] if Dn ≤ 0: delete a uniformly chosen subset of Dn edges from Gn.


Since |Dn| < ηn2 this guarantees (3.2) and has Gn ∼ νn; the additional fact that Gηn ∼ νnη is seen by noting that, if G ∼ G(n,p) then |E(G)| ∼ Bin( n2 ,p), and on the event that G has M edges, these are uniformly distributed (i.e., the conditional distribution is G(n,M)).

We proceed to show that such {Gηn} form an exponentially good approximation of Gn. Indeed, from the identity ti=1 ai− ti=1 bi = tj=1( i<j ai)(aj −bj)( i>j bi) and the deﬁnition of tH(·), we ﬁnd that for any H of t edges and graphs G,G on n vertices,

2t n2

tH(G) − tH(G ) ≤ t WG − WG 1 =

E(G) E(G ) (3.3) (see also [10, Lemma 10.22]).

Next, ﬁxing δ > 0, we set k(δ) ∈ N large enough so that δ > 22/ log2 k (for example, k = 2(25/δ)2 ), and recall the following result:

Theorem ([2, Thm. 2.7(b)]). If k ≥ 1 and the graphs G,G are such that for every simple graph H on k vertices |tH(G)−tH(G )| ≤ 3−k2, then δ (WG,WG ) ≤ 22/ log2 k.

To utilize this relation, set η0(δ) = k−23−k2 noting that if graphs G,G on n vertices

satisfy |E(G) E(G )| < ηn2 for some η ≤ η0, then |tH(G) − tH(G )| < 2 k2 η0 < 3−k2 for every graph H on k vertices, and so by the preceding δ (G,G ) < δ. In particular,

- from (3.2) we deduce that for every η ≤ η0 and all n ≥ n0(η), P(δ (Gn,Gηn) > δ) = 0


holds under the above coupling of (Gn,Gηn), thereby implying (2.5).

Finally, Noting that Bp,ηo of (3.1) is the event |2En/n2−p| < η (with En ∼ Bin( n2 ,p) under µn), we deduce from the lln that µn(Bp,ηo ) → 1. In particular, for any η > 0 one has that n−2 log µn(Bp,ηo ) → 0, thereby verifying (2.2) for the case at hand.

- 3.2. Proof of Corollary 1.2. (a). Recalling that Jp(W) = Ip(W) on W0(p) and otherwise Jp(W) = ∞, we express (1.4) as


{Jp(W)}, for the closed set of graphons

ψH(p,r) = inf

W∈Γ≥r

Γ≥r := W ∈ W0 : tH(W) ≥ r , (3.4) denoting by Γ=r the closed subset of graphons with tH(W) = r. The unique global minimizer of Jp(·) over W0 is W ≡ p. With W ∈ Γ=tH(p), it follows that ψH(p,r) = 0 on [0,tH(p)]. Next, for any r ∈ (tH(p),rH], the good rate function Jp(·) is ﬁnite on the nonempty set Γ≥r ∩ W0(p), hence ψH(p,r) = α is ﬁnite and positive, with the inﬁmum in (1.4) attained at the nonempty compact set

F = Γ≥r ∩ {W ∈ W0 : Jp(W) ≤ α}. (3.5) Fixing such r and Wr ∈ F , consider the map Wr(λ) := λWr + (1 − λ)W from [0,1] to W0(p). Thanks to the continuity of λ  → tH(Wr(λ)) on [0,1], there exists for any r ∈ [tH(p),tH(Wr)) some λ = λ (r ) ∈ [0,1) such that tH(Wr(λ )) = r . Hence, due to the convexity of Jp(·),

ψH(p,r ) ≤ Jp(Wr(λ )) ≤ λ Jp(Wr)) = λ α < α := ψH(p,r).

We have shown that ψH(p,r ) < ψH(p,r) for all r ∈ [tH(p),tH(Wr)). Recalling that tH(Wr) ≥ r, it follows that ψH(p,·) is strictly increasing on [tH(p),rH] and further, that necessarily tH(Wr) = r for any Wr ∈ F . That is, the collection F of minimizers of (1.4) then consists of only the minimizers of (1.5).

Next, if ψH(p,r ) ≤ α < ∞ for all r < r then there exist a pre-compact collection {Wr ,r < r} in (δ , W0), with Jp(Wr ) ≤ α and tH(Wr ) ≥ r . By the continuity of tH(·) and the lsc of Jp(·), it follows that tH(Wr) ≥ r and Jp(Wr) ≤ α for any limit point Wr of Wr as r ↑ r. Consequently ψH(p,r) ≤ α as well, establishing the stated left-continuity of ψH(p,·) on [0,rH]. Finally, recall that an increasing function, ﬁnite on [0,rH] and inﬁnite otherwise, is lsc iﬀ it is left continuous on [0,rH].

- (b). Considering the ldp bounds of Theorem 1.1 for the closed set Γ≥r and its open subset Γ>r := Γ≥r \ Γ=r we deduce that

−lim

r ↓r

{ψH(p,r )} = − inf

W∈Γ>r

{Jp(W)} ≤ liminf

n→∞

n−2 log P(tH(Gn) > r) ≤ limsup

n→∞

n−2 log P(tH(Gn) ≥ r) ≤ −ψH(p,r).

By the assumed right-continuity of t  → ψH(p,t) at r ∈ [0,rH), the preceding inequalities must all hold with equality, resulting with (1.7).

- (c). Proceeding to prove (1.8), we ﬁx (p,r) as in part (b). Further ﬁxing ε > 0, let BW ,ε := W ∈ W0 : δ (W,W ) < ε


denote open cut-metric balls and consider the closed subset of Γ≥r, Γ≥r,ε := Γ≥r

(BW ,ε)c . (3.6)

W ∈F

In view of (1.7) and the fact that

{δ (Gn,F ) ≥ ε, tH(Gn) ≥ r} = {WGn ∈ Γ≥r,ε}, it suﬃces for (1.8) to show that

n−2 log P(WGn ∈ Γ≥r,ε) < −α. By the ldp upper-bound of Theorem 1.1, this in turn follows upon showing that inf

limsup

n→∞

{Jp(W)} ≤ α (3.7)

W∈Γ≥r,ε

contradicts the deﬁnition of F . Indeed, Jp(·) has compact level sets, so if (3.7) holds then Jp(Wr) ≤ α for some Wr ∈ Γ≥r,ε. Recall (3.5) that in particular Wr ∈ F , hence

- (3.6) implies that δ (Wr,Wr) ≥ ε > 0, yielding the desired contradiction.


- 3.3. Sparse uniform random graphs. In this section we show that, as was the case in G(n,p), the analog of (1.7), giving the asymptotic rate function for G(n,m)


in the sparse regime mn = n2/logc n for a suitably small c > 0, can be derived in a straightforward manner from the weak regularity lemma. Indeed, the proof below follows essentially the same short argument used for G(n,p) in [13, Prop. 5.1].

Deﬁnition 3.1 (Discrete variational problem for upper tails). Let H be a graph with κ edges, and let b > 1. Denote the set of weighted undirected graphs on n vertices by

Gn = {(aij)1≤i≤j≤n : 0 ≤ aij ≤ 1, aij = aji , aii = 0 for all i,j} ,

and extend the deﬁnition of the graphon W G in (1.2) to a weighted graph G ∈ Gn by replacing the weight 1 corresponding to an edge ( nx , ny ) by the weight a nx , ny . Taking mn ≤ n2 and pn = mn/ n2 , the variational problem for Gn ∼ G(n,mn) is

ψH(n,mn,b) := inf Ipn(W G) : G ∈ Gn , tH(W G) ≥ bpκn ,

aij = pn .

ij

Remark. When pn → p for some ﬁxed 0 < p < 1, and r ∈ [pκ,rH] is a right-continuity point of t  → ψH(p,t) (whence (1.7) holds), one has ψH(p,r) = limn→∞ ψH(n,mn,rp−κ) (e.g., rescale a sequence Gn of minimizers for ψH(n,mn,rp−κ + ε) by p/pn; conversely, for a minimizer W for ψH(p,r), one can take a sequence Gn with WGn → W).

- Proposition 3.2. Fix H be a graph with κ edges, ﬁx b > 1 and for mn ∈ N let


Gn ∼ G(n,m) and pn = mn/ n2 . For every ε > 0 there exists some K < ∞ such that, if pn(log n)1/(2κ) ≥ K and n is suﬃciently large then

1 n2

log P(tH(Gn) ≥ bpκn) ≤ − ψH(n,mn,b − ε) + ε.

− ψH(n,mn,b) − ε ≤

In particular, if mn ∈ N is such that pn(log n)1/(2κ) → ∞ and limn→∞ ψH(n,mn,t) exists and is continuous in some neighborhood of t = b, then

1 n2

log P(tH(Gn) ≥ bpκn) = − lim

lim

ψH(n,mn,b).

n→∞

n→∞

The following simple lemma, whose analog for upper tails in G(n,p) (addressing only the event E1 below) was phrased in [13, Lemma 5.2] for triangle counts in G(n,p), is an immediate consequence of the independence of distinct edges and Cram´er’s Theorem.

- Lemma 3.3. Fix ε > 0 and suppose n is suﬃciently large. Let V1,...,Vs be a partition of {1,...,n}, let G = (aij) ∈ Gs be such that aij = p = m/ n2 , and deﬁne

E1(G) =

i,j aij>p

{dG(Vi,Vj) ≥ aij} , E2(G) =

i,j aij<p

{dG(Vi,Vj) ≤ aij} ,

where dG(X,Y ) = # (x,y)∈X|X×||YY:|xy∈E(G) . Then Gn ∼ G(n,m) has

− Ip(W G) − ε ≤

1 n2

log P(E1(G) ∩ E2(G)) ≤ −Ip(W G) + ε. (3.8)

Proof. Let G n ∼ G(n,p), and recall that dG n(Vi,Vj)|Vi||Vj| ∼ Bin(|Vi||Vj|,p) and dG n(Vi,Vi) |V2i| ∼ Bin( |V2i| ,p), with these variables being mutually independent, thus

1 n2

log P E1(G n) ∩ E2(G n) ≤ −

1 n2 i<j |Vi||Vj|Ip(aij) −

1 n2 i

|Vi|

2 Ip(aii)

= −Ip(W G) + O(n−2). Next, since P(Gn ∈ ·) = P(G n ∈ · | |E(G n)| = m), it follows that log P(E1(Gn) ∩ E2(Gn)) − log P E1(G n) ∩ E2(G n) ≤ −log P(Bin( n2 ,p) = m).

For N = n2 , by deﬁnition p = m/N and so P(Bin(N,p) = m) ≥ 1/ 2πp(1 − p)N provided that N is large enough, and the result follows.

Combining the weak regularity lemma (see, e.g., [10, Lemma 9.3]) with the counting lemma for graphons (cf., e.g., [10, Lemma 10.23]) implies the following.

- Lemma 3.4. Let ε > 0 and set M = 41/ε2. For every graph G there is a partition V1,...,Vs of its vertices, for some s ≤ M, such that the weighted graph G ∈ Gs in which aij = dG(Vi,Vj) satisﬁes that, for every graph H with κ edges, tH(G) − tH( G) ≤ κε.


Proof of Proposition 3.2. By Lemma 3.4, if Gn has tH(Gn) ≥ bpκn and |E(Gn)| = m then there exists a partition V1,...,Vs of its vertices, for some s ≤ M, such that the corresponding weighted graph G satisﬁes tH(W G) ≥ bpκn − κε and W G = pn (note that the edge density is invariant under the partition). We may round each of the densities aij of G up to a multiple of ε (only increasing tH), with the eﬀect of potentially

increasing the edge density to at most pn + ε. By rescaling we then arrive at G such that WG 1 = pn and

bpκn − κε (1 + ε)κ ≥ bpκn − ε

tH(W G ) ≥

provided that ε/pκn is small enough, which will indeed be the case by our assumption on pn. Applying Lemma 3.3, along with a union bound on the partition (at most Mn possibilities) and the rounded aij’s (at most (1/ε)M2 possibilities, the dominant factor), gives the required result, as the hypothesis that pn(log n)1/2κ is large enough guarantees that this union bound amounts to a multiplicative factor of at most exp(ε n2).

Acknowledgment. A.D. was supported in part by NSF grant DMS-1613091 and E.L. was supported in part by NSF grant DMS-1513403.

References

- [1] B. B. Bhattacharya, S. Ganguly, E. Lubetzky, and Y. Zhao. Upper tails and independence polynomials in random graphs. Adv. Math., 319:313 – 347, 2017.
- [2] C. Borgs, J. T. Chayes, L. Lova´sz, V. T. So´s, and K. Vesztergombi. Convergent sequences of dense graphs. I. Subgraph frequencies, metric properties and testing. Adv. Math., 219(6):1801–1851, 2008.
- [3] S. Chatterjee and A. Dembo. Nonlinear large deviations. Adv. Math., 299:396 – 450, 2016.
- [4] S. Chatterjee and S. R. S. Varadhan. The large deviation principle for the Erdo˝s-Re´nyi random graph. European J. Combin., 32(7):1000–1017, 2011.
- [5] A. Dembo and O. Zeitouni. Large deviations techniques and applications, volume 38 of Stochastic Modelling and Applied Probability. Springer-Verlag, Berlin, 2010. Corrected reprint of the second

(1998) edition.

- [6] R. Eldan. Gaussian-width gradient complexity, reverse log-Sobolev inequalities and nonlinear large deviations. Preprint arXiv:1612.04346.
- [7] R. Kenyon, C. Radin, K. Ren, and L. Sadun. Multipodal structure and phase transitions in large constrained graphs. J. Stat. Phys., 168(2):233–258, 2017.
- [8] R. Kenyon, C. Radin, K. Ren, and L. Sadun. The phases of large networks with edge and triangle constraints. J. Phys. A, 50(43):435001, 22, 2017.
- [9] R. Kenyon, C. Radin, K. Ren, and L. Sadun. Bipodal structure in oversaturated random graphs. Int. Math. Res. Not. (IMRN), 2018(4):1009–1044, 2018.
- [10] L. Lova´sz. Large networks and graph limits, volume 60 of American Mathematical Society Colloquium Publications. American Mathematical Society, Providence, RI, 2012.
- [11] L. Lova´sz and B. Szegedy. Limits of dense graph sequences. J. Combin. Theory Ser. B, 96(6):933– 957, 2006.
- [12] E. Lubetzky and Y. Zhao. On replica symmetry of large deviations in random graphs. Random Structures Algorithms, 47(1):109–146, 2015.
- [13] E. Lubetzky and Y. Zhao. On the variational problem for upper tails in sparse random graphs. Random Structures Algorithms, 50(3):420–436, 2017.
- [14] C. Radin and L. Sadun. Phase transitions in a complex network. J. Phys. A, 46(30):305002, 12, 2013.
- [15] Y. Zhao. On the lower tail variational problem for random graphs. Combin. Probab. Comput., 26(2):301–320, 2017.


Amir Dembo

Department of Mathematics, Stanford University, Sloan Hall, Stanford, CA 94305, USA. E-mail address: amir@math.stanford.edu Eyal Lubetzky

Courant Institute, New York University, 251 Mercer Street, New York, NY 10012, USA. E-mail address: eyal@courant.nyu.edu

