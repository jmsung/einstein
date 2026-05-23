# arXiv:1308.4893v3[math.MG]6Jul2016

## COMPUTING UPPER BOUNDS FOR THE PACKING DENSITY OF CONGRUENT COPIES OF A CONVEX BODY

FERNANDO MARIO´ DE OLIVEIRA FILHO AND FRANK VALLENTIN

Abstract. In this paper we prove a theorem that provides an upper bound for the density of packings of congruent copies of a given convex body in Rn; this theorem is a generalization of the linear programming bound for sphere packings. We illustrate its use by computing an upper bound for the maximum density of packings of regular pentagons in the plane. Our computational approach is numerical and uses a combination of semideﬁnite programming, sums of squares, and the harmonic analysis of the Euclidean motion group. We show how, with some extra work, the bounds so obtained can be made rigorous.

1. Introduction

How much of Euclidean space can be ﬁlled with pairwise nonoverlapping congruent (i.e., rotated and translated) copies of a given convex body K?

A union of congruent copies of K with pairwise disjoint interiors is a packing of congruent copies of K, or just a packing of K for short; below, packings are always packings of congruent copies of the body. The density of a packing is the fraction of Euclidean space it covers. Rewritten, the question of the previous paragraph is: What is the maximum density of a packing of congruent copies of K? We call this the body packing problem.

Theorem 1.1, the main theorem of this paper, provides a way to compute upper bounds to the density of any packing of a given convex body K. We then illustrate the use of this theorem by applying computational methods to obtain bounds for packings of regular pentagons in the Euclidean plane — the case when K ⊆ R2 is a regular pentagon.

Before presenting our main theorem and its application, let us ﬁrst survey some of the most interesting cases of the body packing problem. We refer to the following books and survey for more information: Conway and Sloane [21], Brass, Moser and Pach [10], Bezdek and Kuperberg [8], Fejes T´th and Kuperberg [27].

Perhaps the most well-known case occurs when K is a unit ball. We then have the classical sphere packing problem. It is easy to ﬁnd out which sphere packings are optimal (i.e., attain the maximum packing density) in dimensions 1 and 2. In dimension 3, it was conjectured by the German mathematician and astronomer Johannes

Date: July 6, 2016. 1991 Mathematics Subject Classiﬁcation. 52C17, 90C22. Key words and phrases. Tetrahedra packings, pentagon packings, sphere packings, Lov´asz

theta number, Delsarte’s method, Euclidean motion group, polynomial optimization, semideﬁnite programming.

The ﬁrst author was support by Rubicon grant 680-50-1014 from the Netherlands Organization for Scientiﬁc Research (NWO). The second author was supported by Vidi grant 639.032.917 from the Netherlands Organization for Scientiﬁc Research (NWO).

1

Kepler (–) [35] that a certain packing covering π/(3√2) = 0.74048... of space is optimal. The Kepler conjecture has been proven by Hales [30], who makes massive use of computers in his proof. On August 10, 2014, the ﬂyspeck project was completed which had the purpose to produce a formal proof of the Kepler conjecture, see [31].

In all other dimensions the best known upper bounds come from the linear programming bound of Cohn and Elkies [15]. For a long time this upper bound was conjectured to provide tight bounds in dimensions 8 and 24 and there was very strong numerical evidence to support this conjecture, see Cohn and Kumar [16] or Cohn and Miller [18]; the only thing missing was a rigorous proof. Very recently, on March 14, 2016 Viazovska [48] announced a proof for dimension 8 and a few days later, on March 21, 2016, building on Viazovska’s breakthrough result, Cohn, Kumar, Miller, Radchenko, and Viazovska [17] announced a proof for dimension 24. In dimensions 4, 5, 6, 7, and 9 the linear programming bound of Cohn and Elkies was improved by de Laat, Oliveira, and Vallentin [38], who also provided upper bounds for binary sphere packings, that is, for packings of spheres of two diﬀerent sizes.

Another case of the body packing problem that has attracted attention happens when K is a regular tetrahedron in R3. We called the sphere packing problem “classical”, but this adjective most properly applies to the problem of packing tetrahedra, as it was considered by Aristotle ( BC– BC).

In his treatise De Caelo (On the Heavens), Aristotle attacks the Platonic theory of assigning geometrical ﬁgures, namely the Platonic solids, to the elements, stating (cf. De Caelo, Book III, Chapter VIII, in translation by Guthrie [4]):

This attempt to assign geometrical ﬁgures to the simple bodies is on all counts irrational. In the ﬁrst place, the whole of space will not be ﬁlled up. Among surfaces it is agreed that there are three ﬁgures which ﬁll the place that contains them — the triangle, the square, and the hexagon: among solids only two, the pyramid and the cube. But they need more than these, since they hold that the elements are more.

Here, the “pyramid” is the regular tetrahedron. Aristotle then thought it to be possible to tile the space with regular tetrahedra. Only much latter, Johannes Mu¨ller von K¨nigsberg (–), commonly known as Regiomontanus, a pioneer of trigonometry, would prove that it is actually not possible to do so — it is amusing to observe that this in fact makes Aristotle’s argument stronger.

Regiomontanus’ manuscript, titled De quinque corporibus aequilateris quae vulgo regularis nuncupantur: quae videlicet eorum locum impleant corporalem et quae non, contra commentatorem Aristotelis Averroem1, is lost. The Italian mathematician and astronomer Francesco Maurolico (–) mentions Regiomontanus’ work on a manuscript of very similar title [42]. Considering Regiomontanus’ manuscript as lost, he sets out to obtain the same results. He observes (cf. §2, ibid.) that the angles between the faces of a solid are of importance in determining whether the solid tiles space or not. Nowadays one may easily check that the angle between two faces of a regular tetrahedron is arccos 13 ≈ 70.52877◦, thus a little less

1On the ﬁve equilateral bodies, that are usually called regular, and which of them ﬁll their natural space, and which do not, in contradiction to the commentator of Aristotle, Averro¨es.

than 360◦/5 = 72◦, and one sees that it is therefore impossible to tile R3 with regular tetrahedra. Maurolico himself did a similar computation (cf. §73, ibid.):

(...) Nunc exponam hosce angulos cum suis chordis hic inferius: Pyramidis angulus – gradus 70. minutiæ 31. secundæ 4312. chorda 1154701.2

More on the history of the tetrahedra packing problem can be found in the paper by Lagarias and Zong [39].

In 2006, Conway and Torquato [22] found surprisingly dense packings of tetrahedra. This sparked renewed interest in the problem and a race for the best construction (cf. Lagarias and Zong [39] and Ziegler [50]). The current record is held by Chen, Engel, and Glotzer [13], who found a packing with density ≈ 0.8563, a much larger fraction of space than that which can be covered by spheres. This prompted the quest for upper bounds: We know tetrahedra do not tile space, so the maximum packing density is strictly less than 1. The current record rests with Gravel, Elser, and Kallus [29], who proved an upper bound of 1 − 2.6... · 10−25. They are themselves convinced that the bound can be greatly improved:

In fact, we conjecture that the optimal packing density corresponds to a value of δ [the fraction of empty space] many orders of magnitude larger than the one presented here. We propose as a challenge the task of ﬁnding an upper bound with a signiﬁcantly larger value of δ (e.g., δ > 0.01) and the development of practical computational methods for establishing informative upper bounds.

In 1964, in his famous little book on packing and covering Rogers noted [44, p. 12]: “Little precise is known about the packing density δ(K) in three or more dimensions.” Since then the general situation did not improve much. In dimension three, the only cases where the optimal packing density is known are the cases when K is a space ﬁlling polytope, or when K is the unit ball, or when K is a slight truncation of the rhombic dodecahedron, see [8]. In particular ﬁnding good upper bounds for the body packing problem is very diﬃcult. Recently, progress was made by Fejes T´th, Fodor, and Vı´gh [26] in the case when K is the n-dimensional cross polytope.

Our paper can be seen as a step in the search for good upper bounds for the maximum density of body packings in general and tetrahedra packings in particular. Its main theorem is a generalization of the linear programming bound of Cohn and Elkies [15] for the sphere packing density, which provides the best known upper bounds in small and high dimensions (cf. Cohn and Zhao [19]). To specify a sphere packing it suﬃces to give the centers of the spheres in the packing; this is the reason why the Cohn-Elkies bound is a linear programming bound. In our case, to specify a packing of congruent copies of a body, we need also to consider diﬀerent rotations of the body, and so linear programming is replaced by semideﬁnite programming.

We apply the theorem to packings of pentagons in the plane because the speciﬁc structure of the Euclidean plane simpliﬁes computations and because such packings are interesting in themselves (see e.g. Kuperberg and Kuperberg [37], Casselman [12], and Atkinson, Jiao, and Torquato [3]), obtaining an upper bound

2Below I show these angles with their chords: Angle of the pyramid – 70 degrees. 31 minutes. 4312 seconds. chord 1154701.

of 0.98103 for the density of any such packing. The best known construction is a packing consisting of pentagons placed in two opposite orientations achieving a density of (5 −

√5)/3 = 0.9213... (cf. Kuperberg and Kuperberg, ibid.). Kallus and Kusner [33] showed that the pentagon packing of Kuperberg and Kuperberg cannot be improved by small perturbations.

Using more reﬁned computational tools, for example using a numerically stable complex semideﬁnite programming solver, it is conceivable that our upper bound could be improved. Our main goal however was to show how the theorem can be applied and that it gives bounds well-below the trivial bound of 1. Our long-term goal is to apply the theorem to obtain upper bounds for packings in R3, in particular tetrahedra packings.

In fact, after the ﬁrst draft of our paper was ﬁnished and submitted, Hales and Kusner [32] improved our upper bound for pentagon packings to 0.9611. For this they used an entirely diﬀerent method, based on area estimates of Voronoi cells.

- 1.1. The main theorem. We deﬁned the density of a packing informally, as the fraction of space it covers. There are diﬀerent ways to formalize this deﬁnition, and questions arise as to whether every packing has a density and so on. We postpone such discussion to §2, when we shall prove the main theorem.


Let SO(n) be the group of rotations of Rn, that is, SO(n) = {A ∈ Rn×n : ATA = I and detA = 1}.

The set M(n) = Rn × SO(n) is a group with identity element (0,I), multiplication deﬁned as

(x,A)(y,B) = (x + Ay,AB), and inversion given by

(x,A)−1 = (−A−1x,A−1).

The group M(n), the semidirect product Rn SO(n), is the Euclidean motion group of Rn; it is a noncompact (but locally compact), noncommutative group. When we integrate functions over M(n), we always use the measure d(x,A), which is the product of the Lebesgue measure dx for Rn with the Haar measure dA for SO(n), normalized so that SO(n) has total measure 1.

A bounded complex-valued function f ∈ L∞(M(n)) is said to be of positive type if

f(x,A) = f((x,A)−1) for all (x,A) ∈ M(n) and for all ρ ∈ L1(M(n)) we have

f((y,B)−1(x,A))ρ(x,A)ρ(y,B)d(y,B)d(x,A) ≥ 0.

M(n) M(n)

With this we have all we need for presenting the main theorem.

- Theorem 1.1. Let K ⊆ Rn be a convex body and let f ∈ L1(M(n)) be a bounded real-valued function such that:


- (i) f is continuous and of positive type;
- (ii) f(x,A) ≤ 0 whenever K◦ ∩ (x + AK◦) = ∅, where K◦ is the interior of K;
- (iii) λ = M(n) f(x,A)d(x,A) > 0.


Then the density of any packing of congruent copies of K is at most

f(0,I) λ

volK, where volK is the volume of K.

This theorem is a generalization of a theorem of Cohn and Elkies [15] that provides upper bounds for the maximum density of sphere packings, and more generally also for translational packings of convex bodies. The theorem of Cohn and Elkies generalizes Delsarte’s linear programming method. Delsarte (see for example the survey of Delsarte and Levenshtein [24]) gave a very general method to determine strong upper bounds for packing problems in compact spaces. The Cohn-Elkies bound deals with the noncompact, commutative group Rn and our bound deals with the noncompact, noncommutative group M(n).

Our theorem can also be seen as an extension of the Lov´sz theta number [41], a parameter originally deﬁned for ﬁnite graphs, to the inﬁnite packing graph for the body K. Our proof of Theorem 1.1 in §2 relies on this connection and will make it clear.

Finally, applying Theorem 1.1 to ﬁnd upper bounds for the densities of packings of a given body K ⊆ Rn means ﬁnding a good function f satisfying the conditions required in the theorem. In §5, to ﬁnd such a function for the case of pentagon packings, we use a computational approach that relies on semideﬁnite programming (see §3) and the harmonic analysis of the Euclidean motion group of the plane (see §4. Here is a place where we see that it is simpler to deal with pentagon packings than with tetrahedra packings, since the formulas describing the harmonic analysis of M(2) are much simpler, specially from a computational perspective, than those describing the harmonic analysis of M(3).

2. Proving the main theorem

- 2.1. Packing density and periodic packings. To give a proof of Theorem 1.1 we need to present some technical considerations regarding the density of a packing. Here we follow Appendix A of Cohn and Elkies [15].


Let K ⊆ Rn be a convex body and P be a packing of congruent copies of K. We say that the density of P is ∆ if for all p ∈ Rn we have

vol(B(p,r) ∩ P) volB(p,r)

,

∆ = lim

r→∞

where B(p,r) is the ball of radius r centered at p. Not every packing has a density, but every packing has an upper density given by

vol(B(p,r) ∩ P) volB(p,r)

.

limsup

sup

p∈Rn

r→∞

We say that a packing P is periodic if there is a lattice3 L ⊆ Rn that leaves P invariant, i.e., which is such that P = x + P for all x ∈ L; here, L is the periodicity lattice of P. In other words, an invariant packing consists of some congruent copies of K arranged inside the fundamental cell of L, and this arrangement repeats itself at each copy of the fundamental cell translated by vectors of the lattice.

3A lattice is a discrete subgroup of (Rn, +).

Periodic packings have well-deﬁned densities. Moreover, it is not hard to prove that given any packing P, one may deﬁne a sequence of periodic packings whose fundamental cells have volumes approaching inﬁnity and whose densities converge to the upper density of P. So in computing bounds for the packing density of a given body, one may restrict oneself to periodic packings. This restriction is particularly interesting because it allows us to compactify the problem, as we will see later on.

- 2.2. A generalization of the Lova´sz theta number. Let G = (V,E) be an undirected graph without loops4, ﬁnite or inﬁnite. A set I ⊆ V is independent if no two vertices in I are adjacent. The independence number of G, denoted by α(G), is the maximum cardinality of an independent set of G.


Packings of a given body K ⊆ Rn correspond to the independent sets of the packing graph of K. This is the graph whose vertices are the elements of M(n). Here, vertex (x,A) ∈ M(n) corresponds to the congruent copy x + AK of K. Two vertices are adjacent when the corresponding copies of K cannot both be in the packing at the same time, i.e., when they intersect in their interiors. In other words, distinct vertices (x,A) and (y,B) are adjacent if

(x + AK◦) ∩ (y + BK◦) = ∅.

Clearly, an independent set of the packing graph corresponds to a packing and vice versa. The packing graph however has inﬁnite independent sets, and so its independence number is also inﬁnite.

If we consider periodic packings we may manage to work with graphs that, though inﬁnite, have a compact vertex set and also a ﬁnite independence number. Given a lattice L ⊆ Rn, write M(n)/L = (Rn/L) × SO(n). Note that this is a compact set. Here, we assume that the fundamental cell of L is big enough so that there exists a nonempty periodic packing with periodicity lattice L.

Consider the graph GL whose vertex set is M(n)/L and in which two distinct vertices (x,A) and (y,B) are adjacent if there is v ∈ L such that

(v + x + AK◦) ∩ (y + BK◦) = ∅.

In this setting, a vertex (x,A) ∈ M(n)/L now represents all bodies v+x+AK for v ∈ L, and we put an edge between two distinct vertices if any of the corresponding bodies overlap.

So, independent sets of GL correspond to periodic packings with periodicity lattice L and vice versa. Moreover, GL has ﬁnite independence number, and we actually have that the maximum density of a periodic packing with periodicity lattice L is equal to

α(GL) vol(Rn/L)

volK.

- (1)


In view of the fact that we may restrict ourselves to periodic packings, as seen in the previous section, if we manage to ﬁnd an upper bound for α(GL) for every L, then we obtain an upper bound for the maximum density of any packing of K.

Computing the independence number of a ﬁnite graph is an NP-hard problem, ﬁguring in the list of combinatorial problems proven to be NP-hard by Karp [34]. Lov´sz [41] introduced a graph parameter, the theta number, that provides an upper

4Like all the graphs considered in this paper.

bound for the independence number of a ﬁnite graph and that can be computed in polynomial time. In Theorem 2.1 we present a generalization of the theta number to graphs deﬁned over certain measure spaces, like the graph GL.

To present our theorem we need ﬁrst a few deﬁnitions and facts from functional analysis. For background we refer the reader to the book by Conway [20].

Let V be a separable and compact topological space and µ be a ﬁnite Borel measure on V which is such that every nonempty open subset of V has nonzero measure. There are many examples of such a space. For instance, any ﬁnite set V with the counting measure provides such an example, as does M(n)/L with its natural measure.

A Hilbert-Schmidt kernel, or simply a kernel, is a square-integrable function K : V × V → C. A kernel deﬁnes an operator TK : L2(V ) → L2(V ) as follows: for f ∈ L2(V ) and x ∈ V we have

K(x,y)f(y)dµ(y).

(TKf)(x) =

V

An eigenfunction of K is a nonzero function f ∈ L2(V ) such that TKf = λf for some λ ∈ C. We say that λ is the eigenvalue associated with f.

A kernel K is Hermitian if K(x,y) = K(y,x) for all x, y ∈ V ; a Hermitian kernel deﬁnes a self-adjoint operator TK. We say that K is positive if it is Hermitian and for all ρ ∈ L2(V ) we have

K(x,y)ρ(x)ρ(y)dµ(x)dµ(y) ≥ 0.

V V

This is equivalent to TKρ,ρ ≥ 0 for all ρ ∈ L2(V ), where f,g =

f(x)g(x)dµ(x)

V

is the standard inner product between f, g ∈ L2(V ). Further still, a Hermitian kernel is positive if and only if all its eigenvalues are nonnegative.

- Theorem 2.1. Let G = (V,E) be a graph, where V is a separable and compact topological space having a ﬁnite Borel measure µ such that every nonempty open set of V has nonzero measure. Suppose that kernel K : V × V → R satisﬁes the following conditions:


- (i) K is continuous;
- (ii) K(x,y) ≤ 0 whenever x = y are nonadjacent;
- (iii) K − J is positive, where J is the constant 1 kernel.


Then, for any number B such that B ≥ K(x,x) for all x ∈ V , we have α(G) ≤ B.

Notice that any kernel K satisfying the conditions of the theorem provides an upper bound for α(G). For a ﬁnite graph, the optimal bound given by the theorem is exactly the theta prime number of the graph G, a strengthening of the theta number introduced independently by McEliece, Rodemich, and Rumsey [43] and Schrijver [45].

Such generalizations of the theta number have been considered before by Bachoc, Nebe, Oliveira, and Vallentin [6], where it is proved that the linear programming bound of Delsarte, Goethals, and Seidel [23] for the sizes of spherical codes comes from such a generalization.

To prove the theorem we need the following alternative characterization of continuous and positive kernels: A continuous kernel K : V × V → C is positive if and only if for all m and any choice x1, ..., xm of points in V the matrix K(xi,xj) mi,j=1 is positive semideﬁnite (cf. Lemma 1 in Bochner [9]). In fact, here is where the hypothesis on V is used: To prove this, one needs to use the fact that V is compact, separable, and that the measure µ is ﬁnite and nonzero on nonempty open sets.

Proof of Theorem 2.1. Let I ⊆ V be a nonempty ﬁnite independent set. Since K−J is a continuous and positive kernel, we have that

J(x,y) = |I|2.

K(x,y) ≥

x,y∈I

x,y∈I

Since K satisﬁes condition (ii), if B is an upper bound on the diagonal entries of K we have that

K(x,y) ≥ |I|2,

|I|B ≥

K(x,x) ≥

x∈I

x,y∈I

and then B ≥ |I|, as we wanted.

- 2.3. A proof of the main theorem. The proof of Theorem 1.1 is similar to the proof of Theorem 3.1 in the paper by de Laat, Oliveira, and Vallentin [38]. We ﬁrst prove the theorem for functions of bounded support and then extend it to L1 functions.


Let f : M(n) → R be a function of bounded support satisfying conditions (i)–(iii) in Theorem 1.1. Given a lattice L ⊆ Rn whose fundamental cell is big enough so that there is a nonempty periodic packing with periodicity lattice L, we use f to deﬁne a kernel KL: (M(n)/L) × (M(n)/L) → R satisfying conditions (i)–(iii) of Theorem 2.1 for the graph GL, deﬁned in the previous section.

In fact, we let

f((y − v,B)−1(x,A))

KL((x,A),(y,B)) =

v∈L

- (2)


f(B−1(x − y + v),B−1A)

=

v∈L

for every (x,A), (y,B) ∈ M(n)/L.

Since f has bounded support and x, y ∈ Rn/L, the sum above is actually a ﬁnite sum. This shows not only that KL is well-deﬁned, but also that it is continuous.

We claim that KL has the following properties:

- K1. it is a positive kernel;
- K2. the constant 1 function is an eigenfunction of KL, with eigenvalue λ;
- K3. KL((x,A),(y,B)) ≤ 0 if (x,A) = (y,B) are nonadjacent in GL;
- K4. f(0,I) ≥ KL((x,A),(x,A)) for all (x,A) ∈ M(n)/L. Once we have established these properties, it becomes clear that the kernel


vol(Rn/L) λ

K˜L =

KL

satisﬁes conditions (i)–(iii) of Theorem 2.1 for the graph GL. In particular, the fact that K˜L − J is positive follows directly from K1 and K2 above, because the constant 1 function is an eigenfunction of both K˜L and J with associated eigenvalue vol(Rn/L) in both cases.

But then from K4 we may take B = f(0,I)vol(Rn/L)/λ in Theorem 2.1 and obtain the bound

vol(Rn/L) λ

α(GL) ≤ f(0,I)

.

So the maximum density of any periodic packing with periodicity lattice L is bounded from above by (cf. equation (1))

α(GL) vol(Rn/L)

f(0,I) λ

volK ≤

volK,

and since L is an arbitrary lattice, we would have a proof of Theorem 1.1.

So we set out to prove K1–K4. Property K1 is implied by the fact that f is of positive type. In fact, since f(x,A) = f((x,A)−1), kernel KL is Hermitian by construction. Now take a function ρ ∈ L2(M(n)/L). We also view ρ as the periodic function ρ: M(n) → C such that ρ(x + v,A) = ρ(x,A) for all v ∈ L. For T > 0, write MT(n) = [−T,T]n × SO(n). Then

KL((x,A),(y,B))ρ(x,A)ρ(y,B)d(y,B)d(x,A)

M(n)/L M(n)/L

f((y − v,B)−1(x,A))ρ(x,A)ρ(y,B)d(y,B)d(x,A).

=

M(n)/L M(n)/L v∈L

f((y,B)−1(x,A))ρ(y,B)d(y,B)ρ(x,A)d(x,A)

=

M(n)/L M(n)

vol(Rn/L) vol[−T,T]n M

f((y,B)−1(x,A))ρ(y,B)d(y,B)

= lim

T→∞

T (n) M(n)

· ρ(x,A)d(x,A)

vol(Rn/L) vol[−T,T]n M

f((y,B)−1(x,A))ρ(x,A)ρ(y,B)

= lim

T→∞

T (n) MT (n)

· d(y,B)d(x,A) ≥ 0.

Above, from the second to the third line we exchange the sum with the innermost integral and use the fact that, if h: Rn → C is an integrable function, then

- (3) v∈L Rn/L


h(x + v)dx =

h(x)dx.

Rn

To go from the third to the fourth line we notice that the function

(x,A)  →

f((y,B)−1(x,A))ρ(y,B)d(y,B)

M(n)

is periodic with respect to the lattice L. From the fourth to the ﬁfth line we use the fact that f is of bounded support. Finally, from the ﬁfth to the sixth line we apply directly the deﬁnition of a function of positive type.

### To see K2, we use (3) and notice that for a ﬁxed (x,A) ∈ M(n)/L we have

f((y − v,B)−1(x,A))d(y,B)

KL((x,A),(y,B))d(y,B) =

M(n)/L

M(n)/L v∈L

f((y,B)−1(x,A))d(y,B)

=

M(n)

= λ.

To prove K3, recall that (x,A), (y,B) ∈ M(n)/L are nonadjacent if for all v ∈ L we have (v + x + AK◦) ∩ (y + BK◦) = ∅, and this is the case if and only if

K◦ ∩ (B−1(x − y + v) + B−1AK◦) = ∅.

But then, since f satisﬁes (ii) in the statement of Theorem 1.1, every summand in (2) will be nonpositive, implying K3.

Property K4 may be similarly proven. In fact, since from start we assumed L has a large enough fundamental cell, for v ∈ L with v = 0 we have K◦∩(A−1v+K◦) = ∅. But then in expression (2) for KL((x,A),(x,A)), all summands but the one for v = 0 will be nonpositive, and the summand for v = 0 is exactly f(0,I), proving K4.

So we have K1–K4, and Theorem 1.1 follows for functions f of bounded support. To prove the theorem for a given L1 function, we approximate it by functions of bounded support as follows.

Let f ∈ L1(M(n)) be a real-valued function satisfying conditions (i)–(iii) in Theorem 1.1. For T > 0, consider the function gT : M(n) → R given by

vol(B(0,T) ∩ B(x,T)) volB(0,T)

f(x,A),

gT(x,A) =

where B(x,T) is the ball of radius T centered at x.

Clearly, gT is continuous and has bounded support. We claim that it is also a function of positive type.

To see this, we will use a characterization of continuous functions of positive type analogous to the characterization of continuous positive kernels given in §2.2, namely: A continuous function f ∈ L∞(M(n)) is of positive type if and only if the matrix

f((xj,Aj)−1(xi,Ai)) mi,j=1

is positive semideﬁnite for any m and any elements (x1,A1), ..., (xm,Am) ∈ M(n) (cf. Folland [28], Proposition 3.35).

Let (x1,A1), ..., (xm,Am) ∈ M(n) be any given elements. Let χi: Rn → {0,1} be the characteristic function of B(xi,T) and denote by f,g the standard inner product between functions f, g ∈ L2(Rn). Then

gT((xj,Aj)−1(xi,Ai)) = gT(A−j 1(xi − xj),A−j 1Ai)

vol(B(0,T) ∩ B(A−j 1(xi − xj),T)) volB(0,T)

f((xj,Aj)−1(xi,Ai))

=

vol(B(xi,T) ∩ B(xj,T)) volB(0,T)

f((xj,Aj)−1(xi,Ai))

=

χi,χj volB(0,T)

f((xj,Aj)−1(xi,Ai)).

=

This shows that the matrix

- (4) gT((xj,Aj)−1(xi,Ai)) mi,j=1 is the Hadamard (entrywise) product of the matrices

f((xj,Aj)−1(xi,Ai)) mi,j=1 and

1 volB(0,T)

χi,χj mi,j=1.

The ﬁrst matrix above is positive semideﬁnite since f is of positive type. The second matrix is positive semideﬁnite since it is a positive multiple of the Gram matrix of vectors χ1, ..., χm. So we have that (4) is positive semideﬁnite, and thus gT is of positive type.

By construction, whenever f(x,A) ≤ 0, also gT(x,A) ≤ 0. So gT is a continuous function of bounded support satisfying conditions (i) and (ii) from the statement of Theorem 1.1. This implies immediately that

- (5)


f(0,I) λT

gT(0,I) λT

volK is an upper bound for the density of any packing of congruent copies of K, where λT =

volK =

gT(x,A)d(x,A).

M(n)

To ﬁnish, notice that gT converges pointwise to f as T → ∞. Moreover, for all T we have |gT(x,A)| ≤ |f(x,A)|. So it follows from Lebesgue’s dominated convergence theorem that λT → λ as T → ∞. This together with (5) ﬁnishes the proof of Theorem 1.1.

- 2.4. Using the symmetry of the body. Let K ⊆ Rn be a convex body. Its symmetry group is the subgroup of SO(n) deﬁned as


S(K) = {A ∈ SO(n) : AK = K }.

The action by conjugation of an element B ∈ SO(n) on a function f ∈ L1(M(n)) is given by

(B · f)(x,A) = f((0,B)(x,A)(0,B)−1).

Suppose now G is a compact subgroup of S(K). Then in Theorem 1.1 we may restrict ourselves to G-invariant functions f ∈ L1(M(n)) without aﬀecting the bound obtained. Here we say that f is G-invariant if B · f = f for all B ∈ G.

This restriction to G-invariant functions may make it easier to apply Theorem 1.1. This is actually the case for our application to pentagon packings, as we will see in §5.

To see that the restriction to G-invariant functions does not aﬀect the bound that can be obtained from Theorem 1.1, notice that, if f ∈ L1(M(n)) is a bounded continuous function satisfying conditions (i)–(iii) of Theorem 1.1, then also B · f, for B ∈ G, satisﬁes these conditions.

In fact, to show that B ·f is of positive type, let (x1,A1), ..., (xm,Am) ∈ M(n). Then

(B · f)((xj,Aj)−1(xi,Ai)) mi,j=1

= f((0,B)(xj,Aj)−1(xi,Ai)(0,B)−1) mi,j=1

= f(((xj,Aj)(0,B)−1)−1((xi,Ai)(0,B)−1)) mi,j=1,

and since f is of positive type, B · f is also of positive type (cf. the alternative characterization of continuous functions of positive type in the previous section).

To see that B·f satisﬁes condition (ii) of Theorem 1.1, notice that, since B−1K = K, we have K◦ ∩ (x + AK◦) = ∅ if and only if K◦ ∩ (Bx + BAB−1K◦) = ∅.

Finally, we have

(B · f)(x,A)d(x,A) =

M(n)

f(x,A)d(x,A),

M(n)

and so we see that B · f satisﬁes the conditions of Theorem 1.1 and provides the same bound as f.

Now, since G is compact, it admits a Haar measure µ which we normalize so that µ(G) = 1. Then it is immediate that the function f ∈ L1(M(n)) such that

f(x,A) =

(B · f)(x,A)dµ(B)

G

satisﬁes (i)–(iii) of Theorem 1.1 and provides the same bound as f. Moreover, f is G-invariant. So it follows that a restriction to G-invariant functions does not aﬀect the bound of Theorem 1.1.

3. Semidefinite programming and sums of squares

We collect here the basic facts we need from semideﬁnite programming. For further background we refer to the book by Ben-Tal and Nemirovski [7].

A linear programming problem amounts to maximizing a linear function over a polyhedron, which is the intersection of the nonnegative orthant Rn≥0 with an aﬃne subspace. A semideﬁnite programming problem — a rich generalization of linear programming — amounts to maximizing a linear function over a spectrahedron, the intersection of the cone of positive semideﬁnite matrices Sn 0 with an aﬃne subspace. A semideﬁnite programming problem in primal standard form is

sup C,X : X ∈ Sn 0, Aj,X = bj, j = 1,...,m , where C, A1, ..., Am are given n × n matrices and where b1, ..., bm ∈ C. Here

A,B = tr(B∗A) denotes the trace inner product between matrices. Matrices C and Ai are usually required to be symmetric (or Hermitian). The seemingly more general setting used here can be easily reduced to this restricted version though.

Semideﬁnite programming problems are conic optimization problems. Sometimes it is convenient to assume that the variable matrix X has block-diagonal structure, which amounts to changing the cone Sn 0 to the direct product Sn

### 0×···×Sn

0. For solving semideﬁnite programming problems two types of algorithms are available: the ellipsoid method and interior point methods. The ellipsoid method focuses on the existence of polynomial-time algorithms but no practical implementation is available. In contrast to this there are many very good implementations of interior point methods; De Klerk and Vallentin showed in [36] that a variant of the interior point method for semideﬁnite programming can run in polynomial time on the Turing machine model.

k

1

Semideﬁnite programming is specially useful for certifying the nonnegativity of polynomials or of trigonometric polynomials via sums of squares. We quickly discuss the univariate case — the multivariate case is a simple extension.

A univariate polynomial p ∈ R[x] of degree 2d is a sum of squares, i.e., it can be written as

p = h21 + ··· + h2r for some r ∈ N and h1,...,hr ∈ R[x] of degree at most d if and only if there is a positive semideﬁnite matrix Q with

p = V,Q ,

where V is a matrix of polynomials such that Vkl = Pk(x)Pl(x) for some basis Pk of the space of polynomials of degree at most d.

Note p = V,Q is an identity between polynomials. One can check it by linear equalities — equating the coeﬃcients — once one writes both sides in terms of some basis.

If a polynomial can be written as a sum of squares, then it is clearly nonnegative. For univariate polynomials, the converse is also true. This is not the case in general, however; Laurent [40] presents a survey.

A similar approach can be applied to trigonometric polynomials. Such is an expression of the sort

n

ckeikθ,

p(θ) =

k=−n

where ck = c−k. One way to certify that this trigonometric polynomial is nonnegative for all θ is to write it as a sum of squares, that is, to write it as

p(θ) = |h1(eiθ)|2 + ··· + |hr(eiθ)|2

for some number r and some univariate polynomials h1, ..., hr. Now, being a sum of squares is equivalent to the existence of an (n+1)×(n+1) positive semideﬁnite matrix Q such that

p(θ) = V (eiθ),Q , where V is the matrix with Vkl(z) = zk−l.

4. Harmonic analysis on M(2)

Our approach to apply Theorem 1.1 in order to obtain upper bounds for the maximum density of pentagon packings is to specify the function f via its Fourier transform. So here we quickly present the facts from the theory of harmonic analysis on M(2) that we will use. We follow Sugiura [47] closely, though we deviate at some points, mainly concerning choices of normalization, as we will see.

For x, y ∈ R2, denote by x · y = x1y1 + x2y2 the Euclidean inner product. Let S1 be the unit circle and for ϕ, ψ ∈ L2(S1) denote by ϕ,ψ the standard inner product between ϕ and ψ, i.e.,

1 ω(S1) S1

ϕ,ψ =

ϕ(ξ)ψ(ξ)dω(ξ), where ω is the Lebesgue measure on the unit circle.

For a ≥ 0 and (x,A) ∈ M(2), consider the operator U(ax,A): L2(S1) → L2(S1) deﬁned as follows: For ϕ ∈ L2(S1) we have

[U(ax,A)ϕ](ξ) = e2πiax·ξϕ(A−1ξ)

for all ξ ∈ S1. (In the deﬁnition of U(ax,A) we diﬀer from Sugiura [47], who omits the factor 2π, which we include to obtain better formulas — from a computational

point of view — later on. Besides changing some normalization parameters, this does not aﬀect the theory as presented by Sugiura.)

Operator U(ax,A) is a bounded and unitary operator. Moreover, one can easily check that

U(ax,A)(y,B) = U(ax,A)U(ay,B)

for all (x,A), (y,B) ∈ M(2). So the strongly continuous map ρa(x,A) = U(ax,A) provides a representation of M(2) for every a ≥ 0. Representations ρa, for a > 0, are all irreducible and pairwise nonequivalent.

Given a function f ∈ L1(M(2)), its Fourier transform at a ≥ 0 is the bounded operator f(a): L2(S1) → L2(S1) deﬁned as

f(x,A)U(ax,A)−1 d(x,A).

f(a) =

M(2)

Having deﬁned the Fourier transform of f, we would like to have an inversion formula, that is, a way to compute f back from its Fourier transform. In our case the inversion formula takes the following shape:

∞

tr(U(ax,A) f(a))ada,

- (6) f(x,A) = 2π


0

where trF is the trace of a trace-class operator F. In the following, we only need positive trace-class operators. We deﬁne them now brieﬂy, and we refer e.g. to Conway [20] or Folland [28] for further information. A positive bounded operator F : L2(S1) → L2(S1) is called trace-class if there is a complete orthonormal system ϕk consisting of eigenfunctions of F with eigenvalues λk ≥ 0 and k λk < ∞. Then the trace of F is tr(F) = k λk = k Fϕk,ϕk .

In (6) we again deviate slightly from the exposition of Sugiura. The extra factor of 2π in the above formula as compared to Theorem 3.1 in his book [47] follows from the diﬀerent normalization he uses for the measure of M(2).

Of course, it is not always the case that the inversion formula holds or converges everywhere. In the book by Sugiura it is shown that the inversion formula holds for rapidly decreasing functions (see Deﬁnition 3 in Chapter IV, §3 in Sugiura [47]).

We will provide explicit formulas for the Fourier transform and hence obtain explicit formulas for f. In this way it will be clear in our application that f is continuous and L1. To ensure that f is of positive type, the following lemma will be useful. It shows that one can parametrize positive type functions by the positivity of the Fourier transform f. Here it shows that the computations needed for applying Theorem 1.1 are much more complicated than those for applying the Cohn-Elkies bound. For the Euclidean motion group M(n) the Fourier transform of a positive type function is positive trace-class-operator-valued, whereas for the translation group Rn its values are simply nonnegative real numbers.

Lemma 4.1. Suppose that for each a ≥ 0 we have that f(a) is a positive, traceclass operator. Then, if the function f deﬁned in (6) is bounded and continuous, it is of positive type.

Proof. Take (x1,A1), ..., (xm,Am) ∈ M(2). Recalling the alternative characterization of continuous functions of positive type given in §2.3, we show that the matrix

f((xj,Aj)−1(xi,Ai)) mi,j=1

is positive semideﬁnite.

By construction, this is a Hermitian matrix. From (6), to prove it is positive semideﬁnite it suﬃces to show that for all a ≥ 0 the matrix

j,Aj)−1(xi,Ai) f(a)) mi,j=1 is positive semideﬁnite.

- (7) tr(U(ax


Notice that since each f(a) is trace-class, and since U(ax,A) is a bounded operator,

then U(ax,A) f(a) is trace-class for all (x,A) ∈ M(2), and so each entry of (7) is welldeﬁned.

To see that (7) is positive semideﬁnite, let ϕ1, ϕ2, ... be a complete orthonormal system of L2(S1). For i, j = 1, ..., m we have

∞

tr(U(ax

j,Aj)−1(xi,Ai) f(a)) =

k=1

∞

=

k=1

∞

=

k=1

∞

=

k=1

∞

=

k=1

U(ax

j,Aj)−1(xi,Ai) f(a)ϕk,ϕk

U(ax

j,Aj)−1(xi,Ai) f(a)U(ax

j,Aj)−1ϕk,U(ax

j,Aj)−1ϕk

U(ax

i,Ai) f(a)U(ax

j,Aj)−1ϕk,ϕk

f(a)U(ax

j,Aj)−1ϕk,U(ax

i,Ai)−1ϕk

j,Aj)−1ϕk, f1/2(a)U(ax

f1/2(a)U(ax

i,Ai)−1ϕk .

Here, we go from the ﬁrst to the second line by noticing that, since U(ax

j,Aj)−1 is a unitary operator, U(ax

j,Aj)−1ϕ1, U(ax

j,Aj)−1ϕ2, ... is also a complete orthonormal system of L2(S1). Finally, from the fourth to the ﬁfth line, we observe that since f(a) is a positive trace-class operator, it has a square-root f1/2(a), a selfadjoint operator such that f(a) = f1/2(a) f1/2(a).

So we see that (7) is a sum of positive semideﬁnite matrices, the kth summand being the Gram matrix of m vectors, and we are done.

We ﬁnish this section by computing a more explicit formula for the inverse transform. We identify both SO(2) and S1 with the torus R/(2πZ), and by an abuse of language with the interval [0,2π]. We equip L2([0,2π]) with the inner product

2π

- 1

- 2π


ϕ(ξ)ψ(ξ)dξ

ϕ,ψ =

0

for ϕ, ψ ∈ L2([0,2π]). Then the functions χr ∈ L2([0,2π]), for r ∈ Z, deﬁned as χr(ξ) = eirξ provide a complete orthonormal system of L2([0,2π]).

We deﬁne the matrix coeﬃcients of the operator U(ax,A) on the basis χr as

uar,s(x,A) = U(ax,A)χs,χr with r, s ∈ Z. To compute this, we express x in polar coordinates as

x = ρ(cosθ,sinθ)

and we see A as the rotation matrix

- (8) A = A(α) =

cosα −sinα sinα cosα

,

which rotates vectors counter-clockwise by an angle of α. Then uar,s(ρ,θ,α) = U(ax,A)χs,χr

=

- 1

- 2π


2π

0

[U(ax,A)χs](ξ)χr(ξ)dξ

=

- 1

- 2π


2π

0

e2πiaρ(cosθ,sinθ)·(cosξ,sinξ)eis(ξ−α)e−irξ dξ

=

- 1

- 2π


e−isα

2π

0

e2πiaρcos(ξ−θ)ei(s−r)ξ dξ

=

- 1

- 2π


e−isα

2π

0

e2πiaρcosξei(s−r)(ξ+θ) dξ

=

- 1

- 2π


e−i(sα+(r−s)θ)

2π

0

ei(s−r)ξe2πiaρcosξ dξ

= is−re−i(sα+(r−s)θ)Js−r(2πaρ).

- (9)

Here, Jn(z) is the Bessel function of parameter n. To obtain the last line, we apply Bessel’s integral (cf. Watson [49], (1) in Chapter II, §2.2).

We may then rewrite (6) by expressing the operators f(a) on the basis χr, for r ∈ Z. This gives us

f(ρ,θ,α) =

∞

0 r,s∈Z

f(a)r,suar,s(ρ,θ,α)ada

=

∞

0 r,s∈Z

f(a)r,sis−re−i(sα+(r−s)θ)Js−r(2πaρ)ada.

- (10)


5. Computations for pentagon packings

In this section we present a semideﬁnite programming problem and show how from its solution a function f can be derived that satisﬁes conditions (i)–(iii) of Theorem 1.1 when K is a regular pentagon. We describe the semideﬁnite programming problem in detail, and then discuss how it can be solved with the computer and how a function f can be obtained from its solution that provides the bound of 0.98103 for the maximum density of packings of regular pentagons in R2.

Throughout this section, K will denote the regular pentagon on R2 whose vertices are the points

- 1

- 2


(cos(k2π/5),sin(k2π/5)) for k = 0, ..., 4. Note the circumscribed circle of K has radius 1/2.

The symmetry group of K is isomorphic to C5, the cyclic group of order 5. It consists of the rotation matrices A(k2π/5), for k = 0, ..., 4, where A(α) is given in (8).

- 5.1. Specifying the function. Our approach is to specify the function f required by Theorem 1.1 via its Fourier transform. In this section we discuss our choice for the Fourier transform of f, give explicit formulas for f in terms of its transform, and show which constraints must be imposed on the transform so that f is a realvalued, L1 and continuous function of positive type which is S(K)-invariant.


Let N > 0 be an integer and d ≥ 1 be an odd integer. Consider the matrix-valued function ϕ given by

- (11) ϕ(a) = ϕr,s(a) Nr,s=−N =

d

k=0

fr,s;ka2k

N

r,s=−N

.

Notice that each ϕ(a) is a (2N + 1) × (2N + 1) matrix whose entries are even univariate polynomials in the variable a.

We deﬁne f as the function whose Fourier transform is

- (12) f(a) = ϕ(a)e−πa

2

.

Note that we express the operator f(a) in the basis χr for r ∈ Z, as discussed in §4. Clearly, each f(a) is a trace-class operator. In fact, each f(a) has ﬁnite rank.

The reason for our choice for the Fourier transform is that it makes it easy to compute the function f. Let

Cr,s;k(ρ) =

Γ(k + 1 + |r − s|/2)(ρ√π)|r−s| 2πk+1Γ(|r − s| + 1)

.

Then using (4.11.24) in Andrews, Askey, and Roy [2], since Jn(z) = (−1)nJ−n(z), we have ∞

0

a2k+1e−πa

2

Js−r(2πaρ)da = (−1)s−r

∞

0

a2k+1e−πa

2

J|r−s|(2πaρ)da

= (−1)s−rCr,s;k(ρ)1F1 |r − s|/2 − k |r − s| + 1

;πρ2 e−πρ

2

,

where 1F1 is the hypergeometric series. Together with (10) and (11), this implies for f the formula

- (13) f(ρ,θ,α) =


N

d

(−1)s−ris−re−i(sα+(r−s)θ)fr,s;kCr,s;k(ρ)

r,s=−N

k=0

· 1F1 |r − s|/2 − k |r − s| + 1

2

;πρ2 e−πρ

, where (ρ,θ,α) parametrizes an element of M(2) as in §4.

It is immediately clear that, thanks to our choice of Fourier transform, f is an L1 and continuous function; actually, it is rapidly decreasing. So, by using Lemma 4.1, we see that if f(a) is a positive kernel for each a ≥ 0, then f is a function of positive type. From the deﬁnition of f(a), we see that f(a) is positive for every a ≥ 0 if and only if the matrices ϕ(a) are positive semideﬁnite for every a. Notice that requiring ϕ(a) to be positive semideﬁnite includes requiring ϕ(a) to be Hermitian. This on its turn we achieve by imposing the constraint

fr,s;k = fs,r;k for all r, s, and k.

We may further simplify (13) by imposing two extra conditions on the coeﬃcients fr,s;k. Namely, when r − s is even and |r − s|/2 − k ≤ 0, the hypergeometric

series in (13) becomes a Laguerre polynomial; see also the treatment about the eigenfunction decomposition of the Hankel transform in the book [1, Chapter 9] by Akhiezer. Indeed we have (cf. (6.2.2) in Andrews, Askey, and Roy [2])

1F1 |r − s|/2 − k |r − s| + 1

n! (|r − s| + 1)n

Ln|r−s|(πρ2), where n = k − |r − s|/2,

;πρ2 =

(a)n = a(a + 1)···(a + n − 1) for n > 0 with (a)0 = 1, and Lαn is the Laguerre polynomial of degree n and parameter α.

So we impose on the coeﬃcients fr,s;k the constraints

- (14) fr,s;k = 0 if r − s is odd or k < |r − s|/2. Then (13) becomes
- (15) f(ρ,θ,α) =

N

r,s=−N r−s even

d

k=|r−s|/2

(−1)|r−s|/2e−i(sα+(r−s)θ)fr,s;k

· Dr,s;k(ρ)L|nr−s|(πρ2)e−πρ

2

, where Dr,s;k(ρ) = Cr,s;k(ρ)n!/(|r − s| + 1)n.

To ensure that f is a real-valued function, we observe from (9) that when r − s is even, uar,s(ρ,θ,α) = ua−r,−s(ρ,θ,α). Then from (10) it is clear that if ϕr,s(a) = ϕ−r,−s(a) for all a ≥ 0 and r, s, function f is real-valued. So to ensure that f is real-valued it suﬃces to impose the constraint

- (16) fr,s;k = f−r,−s;k for all r, s, and k.

Finally, we would like to impose constraints on the coeﬃcients fr,s;k so as to make function f S(K)-invariant, that is, so as to have

f(ρ,θ + l2π/5,α) = f(ρ,θ,α) for l = 0, ..., 4. From (15), it is easy to see that one way of achieving this is to require that fr,s;k = 0 whenever r − s  ≡ 0 (mod 5). Since we already set fr,s;k = 0 when r − s is odd, we end up with the constraint

- (17) fr,s;k = 0 whenever r − s  ≡ 0 (mod 10). To ﬁnish, we summarize the constraints imposed on the coeﬃcients fr,s;k:


- (1) We consider only the pairs r, s such that r − s ≡ 0 (mod 10) and we

set fr,s;k = 0 if k < |r − s|/2. This has a double eﬀect: It simpliﬁes the hypergeometric series into a Laguerre polynomial and makes the function S(K)-invariant;

- (2) We set fr,s;k = fs,r;k for all r, s, and k. This makes the matrices ϕ(a) Hermitian. We then require these matrices to be positive semideﬁnite; this ensures that function f is of positive type;

- (3) We set fr,s;k = f−r,−s;k for all r, s, and k. This ensures that function f is real-valued.


With these constraints, we obtain the following formula for f:

N

d

(−1)|r−s|/2e−i(sα+(r−s)θ)fr,s;k

- (18) f(ρ,θ,α) =


r,s=−N r−s≡0 (mod 10)

k=|r−s|/2

2

· Dr,s;k(ρ)Ln|r−s|(πρ2)e−πρ

.

- 5.2. A semideﬁnite programming formulation: basic setup. Recall our goal is to describe a semideﬁnite programming problem whose solutions correspond to functions f ∈ L1(M(n)) satisfying the conditions of Theorem 1.1. In this section, we take a ﬁrst step by showing how to formulate the problem of ﬁnding a function ϕ like (11) as a semideﬁnite programming problem.


We start by making an extra assumption, namely that all coeﬃcients fr,s;k are real. This allows us to work exclusively with real matrices, making the semideﬁnite programming problem we obtain smaller. Then the optimization problem will be solvable by state-of-the-art semideﬁnite programming solvers which are numerically stable. In principle, however, everything we describe can be extended to the more general setting of complex coeﬃcients. It could be, though we do not know, that such a restriction to real numbers greatly worsens the bound that can be obtained via our approach.

So let ϕ be given as in (11) with

fs,r;k = fr,s;k = f−r,−s;k = f−s,−r;k for all r, s, and k as we require. Write y = (y−N,...,yN) and consider the polynomial

N

d

fr,s;ka2kyrys.

σ(a,y) =

r,s=−N r−s≡0 (mod 10)

k=|r−s|/2

Then ϕ(a) is positive semideﬁnite for all a if and only if σ is a sum of squares (see §3). (Here, it is easy to see that if σ is a sum of squares, then ϕ(a) is positive semideﬁnite for all a. The converse is also true; for a proof see Choi, Lam, and Reznick [14]. This fact is related to the Kalman-Yakubovich-Popov lemma in systems and control; see the discussion in Aylward, Itani, and Parrilo [5].)

The constraint that σ is a sum of squares can on its turn be formulated in terms of positive semideﬁnite matrices. Following the recipe given on §3, one would obtain a semideﬁnite programming formulation in terms of a single variable matrix of large size. In our case, however, since σ is an even polynomial in a and since the product yrys only appears when r −s ≡ 0 (mod 10), we may block-diagonalize the variable matrix, obtaining a formulation in terms of smaller matrices, as we show now.

To this end, let P0, P1, ... be a sequence of real, even, univariate polynomials such that Pk has degree 2k. For j = 0, ..., 9, let

Ij = {r ∈ Z : −N ≤ r ≤ N and r ≡ j (mod 10)}. For i = 0, 1 and j = 0, ..., 9, consider the matrix V ij with rows and columns indexed by {0,..., d/2 } × Ij such that

V(ijl,r)(l ,s) = a2iPl(a)Pl (a)yrys

for all l, l = 0, ..., d/2 and r, s ∈ Ij. Notice the entries of V ij are even polynomials in a.

Then σ is a sum of squares if and only if there are real, positive semideﬁnite matrices Qij, of appropriate dimensions, such that

1

9

Qij,V ij ,

σ =

i=0

j=0

where A,B = tr(B∗A) denotes the trace inner product between matrices A and B.

Here, it is also important to observe that the symmetry constraints fr,s;k = fs,r;k are implied by the fact that the matrices Qij are symmetric.

So ﬁnding real numbers fr,s;k such that fr,s;k = fs,r;k and such that ϕ(a) is positive semideﬁnite for all a amounts to ﬁnding real positive semideﬁnite matrices Qij. Also the other constraints that we imposed on the coeﬃcients fr,s;k can be represented as linear constraints on the entries of the Qij matrices, as we show now.

For r, s, k with r − s ≡ 0 (mod 10), let j ∈ {0,...,9} be such that r, s ∈

Ij. For i = 0, 1, consider the matrix Fr,si ;k with rows and columns indexed by {0,..., d/2 } × Ij such that

(Fr,si ;k)(l,r)(l ,s) = coeﬀ(a2k,a2iPl(a)Pl (a))

for all l, l = 0, ..., d/2 , where for a given polynomial p, coeﬀ(ak,p) is the coeﬃcient of monomial ak in p. Then we obtain the coeﬃcients fr,s;k from the matrices Qij by the formula

1

fr,s;k =

i=0

### So constraints (14) and (16) become

Fr,si ;k,Qij .

1

Fr,si ;k,Qij = 0 if k < |r − s|/2,

i=0

1

( Fr,si ;k,Qij − F−i r,−s;k,Qij ) = 0 for all r, s, and k,

i=0

where r, s ≡ j (mod 10) and −r,−s ≡ j (mod 10). Notice that constraint (17) is already implicit in our formulation, because we enforce by construction that only pairs r, s with r − s ≡ 0 (mod 10) occur.

Also the function f can be computed from matrices Qij. To see how, for r, s = −N, ..., N such that r − s ≡ 0 (mod 10) and for k ≥ |r − s|/2, set

- (19) [τr,s(a2k)](ρ,θ,α) = (−1)|r−s|/2e−i(sα+(r−s)θ)Dr,s;k(ρ)L|nr−s|(πρ2),


where n = k − |r − s|/2. When k < |r − s|/2, we set τr,s(a2k) = 0, and then we extend τr,s linearly to all even polynomials in the variable a.

For i = 0, 1 and j = 0, ..., 9, consider the matrix Fij with rows and columns indexed by {0,..., d/2 } × Ij such that

[Fij(ρ,θ,α)](l,r)(l ,s) = τr,s(a2iPl(a)Pl (a))

for all l, l = 0, ..., d/2 and r, s ∈ Ij. Then, in view of (18) and since fr,s;k = 0 whenever k < |r − s|/2, we have

- (20) f(ρ,θ,α) =

1

i=0

9

j=0

 Fij(ρ,θ,α),Qij e−πρ

2

.

- 5.3. Ensuring nonpositiveness. How can we ensure that function f, given by (20), satisﬁes constraint (ii) of Theorem 1.1? This we do also in terms of semideﬁnite programming constraints.


First, observe that we require f(x,A) ≤ 0 whenever K◦ ∩ (x + AK◦) = ∅. The latter happens if and only if x ∈/ (K − AK)◦, where K − AK is the Minkowski diﬀerence of K and AK:

K − AK = {y − z : y ∈ K, z ∈ AK }.

The Minkowski diﬀerence K−AK is a polygon for all A ∈ SO(2). Its vertices can be explicitly determined; Figure 1 shows the Minkowski diﬀerence when A = A(α) (as deﬁned in (8)) for α ∈ [−2π/10,2π/10]. By the symmetry of K, this gives a full characterization of the shape of the Minkowski diﬀerence for all α.

Our approach to ensure that f is nonpositive outside of (K − AK)◦ consists of two steps. First, we observe that all vertices of K −AK have norm at most 1. This implies that we must have f(x,A) ≤ 0 whenever x ≥ 1. This condition on f can be expressed in terms of sums of squares constraints.

Indeed, by writing z1 = eiθ and z2 = ei(α−θ), we may rewrite (19) as

[τr,s(a2k)](ρ,z1,z2) = (−1)|r−s|/2z1−rz2−sDr,s;k(ρ)L|nr−s|(πρ2). In view of (20), if we then have

1

i=0

9

j=0

 Fij(ρ,z1,z2),Qij ≤ 0 for all ρ ≥ 1,

we have f(ρ,θ,α) ≤ 0 whenever ρ ≥ 1, as we want. For j = 0, ..., 9, consider the set

Pj = {(r,s) : 0 ≤ r,s ≤ N and r − s ≡ j (mod 10)}. For i = 0, 1, j = 0, ..., 9, consider the matrix Wij with rows and columns indexed by {0,..., d/2 } × Pj such that

W(ijl,p)(l ,p )(ρ,z1,z2) = (ρiPl(ρ)z1−uz2−v)(ρiPl (ρ)z 1u z 2v ), where p = (u,v) and p = (u ,v ) with p, p ∈ Pj, and l, l = 0, ..., d/2 .

If there are real positive semideﬁnite matrices Rij for i = 0, 1 and j = 0, ..., 9, and Sj for j = 0, ..., 9, such that

- (21)


1

9

( Fij(ρ,z1,z2),Qij + Wij(ρ,z1,z2),Rij )

i=0

j=0

9

(ρ2 − 1)W0j(ρ,z1,z2),Sj = 0,

+

j=0

then f(ρ,θ,α) ≤ 0 for all ρ ≥ 1. Notice (21) is a polynomial identity on variables ρ, z1, z1−1, z2, and z2−1. In other words, the left-hand side deﬁnes a polynomial and the identity above states that this polynomial must be identically zero. To see

14

20

1

- 2 1

2

- 3


3

0

03

0

4 4

31

42

14 24

13

1

- 2
- 3 4


20

- 02
- 03


0

30

31

42

41

14 13 24

1 1

03

- 2

- 2
- 3


- 3 4


0

20

0

02

4

30

42

31

41

2π/10

π/10

α = 0

−π/10

−2π/10

Figure 1. From left to right, top to bottom. In the ﬁrst three pictures, we see the Minkowski diﬀerence K − A(α)K (the outer shape) for α = −2π/10, 0, and π/10. The dashed pentagon in the center corresponds to A(α)K. The vertices of the pentagons are numbered from 0 to 4. The vertices of the Minkowski diﬀerence are numbered ij, meaning that they correspond to x−y, where x is the ith vertex of K and y is the jth vertex of A(α)K. In the last picture we show the three-dimensional set {(x,α) : x ∈ K − A(α)K }. Here, α is on the vertical axis; every section perpendicular to the vertical axis corresponds to a Minkowski diﬀerence K − A(α)K.

that (21) implies that f(ρ,θ,α) ≤ 0 whenever ρ ≥ 1, one only has to notice that, for ρ ≥ 1 and θ,α ∈ [0,2π], the Hermitian matrices

Wij(ρ,eiθ,ei(α−θ)) and (ρ2 − 1)W0j(ρ,eiθ,ei(α−θ)) are positive semideﬁnite, and then all inner products in (21) become nonnegative.

Constraint (21) is not enough to ensure, however, that f is nonpositive outside of the Minkowski diﬀerence. To ensure nonpositiveness in the remaining region, we use a discretization heuristic: We pick a sample of triples (ρ,θ,α) with ρ ≤ 1 for which we have to ensure that f(ρ,θ,α) ≤ 0 and we do so explicitly for every point of the sample using (20). Afterwards, we have to analyze the solution obtained in order to check that it indeed satisﬁes condition (ii) of Theorem 1.1. We will give details on this approach in the next section.

One may model the constraint that f is nonpositive outside the Minkowski difference using only sums of squares, without using the discretization approach. The sizes of the matrices get very large, however, making this approach computationally infeasible.

5.4. The semideﬁnite programming problem and how to solve it. We now describe the semideﬁnite programming problem we solve to obtain upper bounds for the pentagon packing density.

Let N > 0 be an integer and d ≥ 1 be an odd integer. Let S be a ﬁnite set of triples (ρ,θ,α) with ρ ≤ 1 corresponding to elements (x,A) ∈ M(2) such that K◦ ∩ (x + AK◦) = ∅. We consider the following semideﬁnite programming problem:

Problem A. Find real, positive semideﬁnite matrices Qij, Rij for i = 0,1 and j = 0, ..., 9, and Sj for j = 0, ..., 9, that minimize

1

9

 Fij(0,0,0),Qij

i=0

j=0

subject to the constraints

1

### (22) Fr,si ;k,Qij = 0 if k < |r − s|/2, where r, s ≡ j (mod 10),

i=0

1

### (23) ( Fr,si ;k,Qij − F−i r,−s;k,Qij ) = 0 where r, s ≡ j (mod 10) and −r, −s ≡ j (mod 10),

i=0

1

9

### (24) ( Fij(ρ,z1,z2),Qij + Wij(ρ,z1,z2),Rij )

i=0

j=0

9

(ρ2 − 1)W0j(ρ,z1,z2),Sj = 0,

+

j=0

1

9

### (25)  Fij(ρ,θ,α),Qij ≤ 0 for all (ρ,θ,α) ∈ S,

i=0

j=0

1

### (26) F0i,0;0,Qi0 = 1.

i=0

Conditions (22)–(25) were already discussed in the previous sections. Notice this is indeed a semideﬁnite programming problem. In fact, the objective function and all constraints but (24) are clearly linear. As for the polynomial identity (24), one only has to observe that it can be turned into linear constraints by using the fact that a polynomial is identically zero if and only if each monomial has a zero coeﬃcient (cf. §3).

Of Problem A we have to explain our choice of objective function and also the meaning of constraint (26). To obtain the best possible bound from Theorem 1.1, we wish to minimize f(0,I)/λ, where

λ =

f(x,A)d(x,A).

M(2)

Constraint (26) is a normalization constraint, setting λ = 1. Indeed, one has λ = f0,0;0, since from the deﬁnition of f and the inversion formula (cf. §4) we have

f0,0;0 = ( f(0))0,0 = f(0)1,1

f(x,A)U(0x,A)−11d(x,A),1

=

M(2)

= λ 1,1

= λ,

where 1 ∈ L2(S1) is the constant one function, so that U(0x,A)−11 = 1. Now, the objective function evaluates f(0,I), that we wish to minimize.

To be able to solve Problem A on the computer, the choice of the sequence P0, P1, ... of polynomials which we use to deﬁne our matrices is essential. A bad choice here can lead to numerical instability that might prevent us from solving the problem.

In particular, we have observed that the monomial basis performs specially badly. A much better choice are normalized Laguerre polynomials, as had been observed in a similar setting by de Laat, Oliveira, and Vallentin [38]. Namely, we set

Pk(x) = µ−k 1L0k(2πx2),

where µk is the absolute value of the coeﬃcient of L0l (2πx2) with largest absolute value.

Also essential to the stability of Problem A is the choice of the basis used to express polynomial identity (24). Again, the monomial basis is a poor choice. Instead we use the basis

Pk(ρ2)z1−rz2−s for k = 0, ..., d and −N ≤ r,s ≤ N such that r − s ≡ 0 (mod 10).

This means that in order to express constraint (24), we expand the corresponding polynomial in the above basis, and then require each coeﬃcient of the expansion to be zero.

In preliminary tests with reasonably dense samples for constraint (25), we observed that most variables in Problem A did not seem to play a role, at least for the values of d and N that we considered. So we decided to discard all variable matrices except for

Q00, Q05, Q10, Q15, R00, R05, S0, and S5,

14 13 24

1 1

03

- 2

- 2
- 3


- 3 4


0

20

0

02

30

4

42

31

41

Figure 2. The points in gray are an example of a sample used in Problem A; here we show the points in the sample for α = π/10. Each facet F of the Minkowski diﬀerence deﬁnes a line lF, its supporting hyperplane, and for the sample we would then pick all points in the grid that are inside the circle of radius 1 and that lie, for some facet F of the Minkowski diﬀerence, on the side of lF that does not contain the origin. Since we work with S(K)-invariant functions, however, we need not choose all these points: It suﬃces to consider only two adjacent facets of the Minkowski diﬀerence, instead of all the facets.

and we observed that this did not have much eﬀect on the optimal value of the problem, while providing for simpler and more stable problems. From now on, when we refer to Problem A it should be understood that we only use the variables listed above.

We now have a complete description of the semideﬁnite programming problem to be solved, let us sketch how we obtained the bound of 0.98103 for the pentagon packing density.

We ﬁrst solve Problem A (with less variables, as explained above) for d = 11 and N = 5, using a sample with 537 points. This sample we pick as follows. We ﬁrst pick 5 uniformly spaced values for α in [−2π/10,0], starting with −2π/10 and ending with 0. For each such value of α, we pick in the square [−1,1]2 a uniformly spaced grid of 50×50 points, and add to the sample all triples (ρ,θ,α), where (ρ,θ) corresponds to a grid point outside of the Minkowski diﬀerence (K − A(α)K)◦ and such that ρ ≤ 1. Moreover, the symmetry of K allows us to restrict our sample considerably — Figure 2 has an example.

We observed, by evaluating the function f obtained via this approach, that this small sample is already enough to enforce condition (ii) of Theorem 1.1 on most of the required domain. To really obtain a function f satisfying the conditions of Theorem 1.1, however, we have to work a bit more.

Since we use a numerical solver for semideﬁnite programming, the solutions we obtain for Problem A are not really feasible, but almost feasible. So we cannot be a priori certain that the bound given by Problem A is really an upper bound.

To deal with this issue, we use the same approach outlined by de Laat, Oliveira, and Vallentin [38], which we brieﬂy explain here. First, we solve Problem A in order to get an estimate of its optimal value; say z∗ is the numerical optimal value obtained. Then, we solve a version of Problem A in which the objective function is removed but a constraint

1

9

 Fij(0,0,0),Qij ≤ z∗ + 10−5

i=0

j=0

is added.

This problem is a feasibility problem, and for this reason the solver will return a solution that is strictly feasible, i.e., a solution in which the solution matrices are positive deﬁnite, if one can be found.

In this way, we manage to obtain a solution of Problem A having objective value close to what the optimal value is supposed to be, in which each matrix has a minimum eigenvalue around 10−6, whereas the constraints are satisﬁed up to an absolute error of 10−9. By projecting the solution obtained onto the aﬃne subspace generated by constraints (22), (23), (24), and (26), using double-precision ﬂoating-point arithmetic, we manage to drop the absolute error to 10−22, while not changing much the minimum eigenvalues of the solution matrices. We give the matrices Q00,Q10,Q05,Q15 parametrizing function f in Figure 3.

So the approach detailed by de Laat, Oliveira, and Vallentin [38] applies. Namely, since the minimum eigenvalues of the solution matrices are big compared to the absolute errors, we may be sure that by changing the solution matrices slightly, we may ensure that the constraints are satisﬁed, thus obtaining a truly feasible solution, without signiﬁcantly changing the objective value. Notice that we do not need to carry out this change in practice, it suﬃces to know that it can be done.

Finally, we still have to show that the function f thus obtained satisﬁes condition (ii) of Theorem 1.1. We have said that f satisﬁes condition (ii) for most of the points on the required domain. For instance, since we have constraint (24), we know that f(ρ,θ,α) ≤ 0 for all ρ ≥ 1. There are, however, points (ρ,θ,α) with ρ ≤ 1 for which we have f(ρ,θ,α) positive, while (ii) would require this value to be nonpositive.

Though f does not satisfy condition (ii) of Theorem 1.1 for the pentagon K, it satisﬁes this condition once we enlarge K slightly. Indeed, f satisﬁes condition (ii) for the pentagon 1.02K. This we may verify by picking a ﬁne enough sample of points (ρ,θ,α) with ρ ≤ 1 for which f has to be nonpositive, and computing the minimum value of f on this sample using 256-bit-precision ﬂoating-point. By computing the derivatives of f, we may estimate how ﬁne the sample has to be and how large the absolute value of the minimum of f on the sample has to be, in order for us to be sure that f is nonpositive in the whole required region.

A side eﬀect of our restriction of the variables is that the function f we obtain is by construction such that

f(ρ,θ,α + l2π/5) = f(ρ,θ,α)

for all integer l (cf. (18)). This and the symmetry of K helps us restrict the sample to points (ρ,θ,α) with α ∈ [−2π/10,2π/10]. To obtain our bound, we had to

- 0

B

@

5.69975310.7181867.5005053.2820710.7248190.038715

10.71818628.67359323.88923211.7789992.8429420.168553

7.50050523.88923221.62381011.6021483.0118340.198710

3.28207111.77899911.6021486.9631341.9852460.150341

0.7248192.8429423.0118341.9852460.6208080.057626

0.0387150.1685530.1987100.1503410.0576260.008410

- 1


C

A

A 10Q=

- 0

B

@

    0.4716180.2604110.2361090.3771990.1809390.030009

0.2604117.59267910.2079927.7597192.8881780.397423

 0.23610910.20799216.82637715.3198076.5252111.046526

 0.3771997.75971915.31980715.8949027.4199041.313099

 0.1809392.8881786.5252117.4199043.8944050.800412

 0.0300090.3974231.0465261.3130990.8004120.192548

- 1


C

00Q=

- 0

B

@

    0.0312370.0000140.0738900.0000140.0667510.0000430.0422160.0000700.0151810.0000410.0019980.000008

    0.0000140.0312370.0000140.0738900.0000430.0667510.0000700.0422160.0000410.0151810.0000080.001998

     0.0738900.0000140.1870820.0000400.2062530.0002520.1570130.0003360.0633690.0002000.0088070.000043

     0.0000140.0738900.0000400.1870820.0002520.2062530.0003360.1570130.0002000.0633690.0000430.008807

      0.0667510.0000430.2062530.0002520.3327850.0006620.3149410.0007940.1404080.0004750.0203090.000106

      0.0000430.0667510.0002520.2062530.0006620.3327850.0007940.3149410.0004750.1404080.0001060.020309

      0.0422160.0000700.1570130.0003360.3149410.0007940.3226700.0009320.1481450.0005610.0216680.000129

      0.0000700.0422160.0003360.1570130.0007940.3149410.0009320.3226700.0005610.1481450.0001290.021668

      0.0151810.0000410.0633690.0002000.1404080.0004750.1481450.0005610.0687320.0003430.0101030.000082

      0.0000410.0151810.0002000.0633690.0004750.1404080.0005610.1481450.0003430.0687320.0000820.010103

      0.0019980.0000080.0088070.0000430.0203090.0001060.0216680.0001290.0101030.0000820.0014940.000022

      0.0000080.0019980.0000430.0088070.0001060.0203090.0001290.0216680.0000820.0101030.0000220.001494

- 1


05Q=

C

A

- 0

B

@

      0.1428740.0001330.3195210.0003470.2327970.0004150.1073810.0003230.0282400.0001160.0030130.000008

      0.0001330.1428740.0003470.3195210.0004150.2327970.0003230.1073810.0001160.0282400.0000080.003013

      0.3195210.0003470.7168700.0008920.5296690.0010280.2508300.0007830.0682800.0002790.0074940.000021

      0.0003470.3195210.0008920.7168700.0010280.5296690.0007830.2508300.0002790.0682800.0000210.007494

      0.2327970.0004150.5296690.0010280.4148940.0010770.2169900.0007670.0661660.0002680.0078840.000021

      0.0004150.2327970.0010280.5296690.0010770.4148940.0007670.2169900.0002680.0661660.0000210.007884

      0.1073810.0003230.2508300.0007830.2169900.0007670.1303490.0005180.0450320.0001790.0057800.000015

      0.0003230.1073810.0007830.2508300.0007670.2169900.0005180.1303490.0001790.0450320.0000150.005780

      0.0282400.0001160.0682800.0002790.0661660.0002680.0450320.0001790.0170030.0000650.0022840.000007

      0.0001160.0282400.0002790.0682800.0002680.0661660.0001790.0450320.0000650.0170030.0000070.002284

      0.0030130.0000080.0074940.0000210.0078840.0000210.0057800.0000150.0022840.0000070.0003140.000001

      0.0000080.0030130.0000210.0074940.0000210.0078840.0000150.0057800.0000070.0022840.0000010.000314

- 1


C

A

15Q=

1

### Figure 3. Matrices Q00,Q10,Q05,Q15 parametrizing the function f after the projection.

use a sample of about 6.5 million points to check that f satisﬁes condition (ii) of Theorem 1.1. Details of this procedure can be found in the paper [25] by Dostert, Guzm´n, Oliveira, and Vallentin.

Enlarging the body K worsens the bound given by Theorem 1.1, but since we consider a small enlargement of K, we still manage to obtain the bound of 0.98103.

Finally, we mention some of the computational tools used to generate the semideﬁnite programming problem and solve it. To generate the problem, we use a C++ program with a custom-made C++ library for generating semideﬁnite programming problems, in particular dealing with sums of squares constraints. As a solver we used CSDP [11], and to analyze the resulting solution and check that it is feasible we used a mix of SAGE [46] and C++.

Acknowledgements

We are thankful to Pier Daniele Napolitani and Claudia Addabbo from the Maurolico Project5, who provided us with a transcript of Maurolico’s manuscript. In particular, Claudia Addabbo provided us with a draft of her commented Italian translation of the manuscript.

References

- [1] N.I. Akhiezer, Lectures on Integral Transforms, Translations of Mathematical Monographs 70, American Mathematical Society, 1988.
- [2] G.E. Andrews, R. Askey, and R. Roy, Special Functions, Encyclopedia of Mathematics and its Applications 71, Cambridge University Press, Cambridge, 1999.
- [3] S. Atkinson, Y. Jiao, and S. Torquato, Maximally dense packings of two-dimensional convex and concave noncircular particles, Physical Review E 86 (2012) 031302.
- [4] Aristotle, On the Heavens, translation by W.K.C. Guthrie, Harvard University Press, Cambridge, 2006.
- [5] E. Aylward, S. Itani, and P.A. Parrilo, Explicit SOS decompositions of univariate polynomial matrices and the Kalman-Yakubovich-Popov Lemma, in: Proceedings of the 46th IEEE Conference on Decision and Control, 2007, pp. 5660–5665.
- [6] C. Bachoc, G. Nebe, F.M. de Oliveira Filho, and F. Vallentin, Lower bounds for measurable chromatic numbers, Geometric and Functional Analysis 19 (2009) 645–661.
- [7] A. Ben-Tal and A. Nemirovski, Lectures on Modern Convex Optimization: Analysis, Algorithms, and Engineering Applications, SIAM, Philadelphia, 2001.
- [8] A. Bezdek and W. Kuperberg, Dense packing of space with various convex solids, in: Geometry — Intuitive, Discrete, and Convex, A Tribute to L´aszlo´ Fejes To´th, (I. B´ara´ny, K. J. B¨oro¨czky, G. Fejes T´oth, J. Pach, eds.), Bolyai Society Mathematical Studies 24, Springer, 2013, pp. 66–90.
- [9] S. Bochner, Hilbert distances and positive deﬁnite functions, Annals of Mathematics 42 (1941) 647–656.
- [10] P. Brass, W. Moser, and J. Pach, Research Problems in Discrete Geometry, Springer, 2005.
- [11] B. Borchers, CSDP, A C Library for Semideﬁnite Programming, Optimization Methods and Software 11 (1999) 613–623.
- [12] B. Casselman, Can you do better?, Feature Column of the AMS, http://www.ams.org/ samplings/feature-column/fc-2012-11, 2012.
- [13] E.R. Chen, M. Engel, and S.C. Glotzer, Dense crystalline dimer packings of regular tetrahedra, Discrete & Computational Geometry 44 (2010) 253–280.
- [14] M.D. Choi, T.Y. Lam, and B. Reznick, Real zeros of positive semideﬁnite forms I, Mathematische Zeitschrift 171 (1980) 1–26.
- [15] H. Cohn and N.D. Elkies, New upper bounds on sphere packings I, Annals of Mathematics 157 (2003) 689–714.


5http://maurolico.free.fr

- [16] H. Cohn and A. Kumar, Optimality and uniqueness of the Leech lattice among lattices, Annals of Mathematics 170 (2009) 1003–1050.
- [17] H. Cohn, A. Kumar, S.D. Miller, D. Radchenko, and M.S. Viazovska, The sphere packing problem in dimension 24, arXiv:1603.06518 [math.NT], 2016, 12pp.
- [18] H. Cohn and S.D. Miller, Some properties of optimal functions for sphere packing in dimensions 8 and 24, arXiv:1603.04759 [math.MG], 2016, 23pp.
- [19] H. Cohn and Y. Zhao, Sphere packing bounds via spherical codes, Duke Mathematical Journal 163 (2014) 1965–2002.
- [20] J.B. Conway, A Course in Functional Analysis, Graduate Texts in Mathematics 96, SpringerVerlag, New York, 1985.
- [21] J.H. Conway and N.J.A. Sloane, Sphere packings, lattices and groups, Grundlehren der mathematischen Wissenschaften 290, 3rd ed., Springer-Verlag, New York, 1999
- [22] J.H. Conway and S. Torquato, Packing, tiling, and covering with tetrahedra, Proceedings of the National Academy of Sciences of the USA 103 (2006) 10612–10617.
- [23] P. Delsarte, J.M. Goethals, and J.J. Seidel, Spherical codes and designs, Geometriae Dedicata 6 (1977) 363–388.
- [24] P. Delsarte and V.I. Levensthein, Association schemes and coding theory, IEEE Transactions on Information Theory IT-44 (1988) 2477–2504.
- [25] M. Dostert, C. Guzm´an, F.M. de Oliveira Filho, and F. Vallentin, New upper bounds for the density of translative packings of three-dimensional convex bodies with tetrahedral symmetry, arXiv:1510.02331 [math.MG], 2015, 29pp.
- [26] G. Fejes T´oth, F. Fodor, and V. Vı´gh, The packing density of the n-dimensional crosspolytope, Discrete & Computational Geometry 54 (2015) 182–194.
- [27] G. Fejes T´oth and W. Kuperberg, Packing and covering with convex sets, in: Handbook of convex geometry. Vol. B (P.M. Gruber and J.M. Wills eds.), North-Holland, Amsterdam, 1993, pp. 799–860.
- [28] G.B. Folland, A Course in Abstract Harmonic Analysis, Studies in Advanced Mathematics, CRC Press, Boca Raton, 1995.
- [29] S. Gravel, V. Elser, and Y. Kallus, Upper bound on the packing density of regular tetrahedra and octahedra, Discrete & Computational Geometry 46 (2011) 799–818.
- [30] T.C. Hales, A proof of the Kepler conjecture, Annals of Mathematics 162 (2005) 1065–1185.
- [31] T.C. Hales, M. Adams, G. Bauer, D. Tat Dang, J. Harrison, T. Le Hoang, C. Kaliszyk, V. Magron, S. McLaughlin, T. Tat Nguyen, T. Quang Nguyen, T. Nipkow, S. Obua, J. Pleso, J. Rute, A. Solovyev, A. Hoai Thi Ta, T. Nam Tran, D. Thi Trieu, J. Urban, K. Khac Vu, and R. Zumkeller, A formal proof of the Kepler conjecture, arXiv:1501.02155 [math.MG], 2015, 21pp.
- [32] T.C. Hales and W. Kusner, Packings of regular Pentagons in the plane, arXiv:1602.07220 [math.MG], 2016, 26pp.
- [33] Y. Kallus and W. Kusner, The local optimality of the double lattice packing, arXiv:1509.02241 [math.MG], 2015, 23pp.
- [34] R.M. Karp, Reducibility among combinatorial problems, in: Complexity of Computer Computations (Proceedings of a symposium on the Complexity of Computer Computations, IBM Thomas J. Watson Research Center, Yorktown Heights, New York, 1972; R.E. Miller, J.W. Thatcher, eds.), Plenum Press, New York, 1972, pp. 85–103.
- [35] J. Kepler, Vom sechseckigen Schnee (Strena seu de Nive sexangula, published in 1611), translation with introduction and notes by Dorothea Goetz, Ostwalds Klassiker der exakten Wissenschaften 273, Akademische Verlagsgesellschaft Geest u. Portig K.-G., Leipzig, 1987.
- [36] E. de Klerk and F. Vallentin, On the Turing model complexity of interior point methods for semideﬁnite programming, arXiv:1507.03549 [math.OC], 2015, 16pp.
- [37] G. Kuperberg and W. Kuperberg, Double-lattice packings of convex bodies in the place, Discrete & Computational Geometry 5 (1990) 389–397.
- [38] D. de Laat, F.M. de Oliveira Filho, and F. Vallentin, Upper bounds for packings of spheres of several radii, Forum of Mathematics, Sigma 2 (2014), e23 (42 pages).
- [39] J.C. Lagarias and C. Zong, Mysteries in packing regular tetrahedra, Notices of the AMS 59 (2012) 1540–1549.
- [40] M. Laurent, Sums of squares, moment matrices and optimization, in: Emerging Applications of Algebraic Geometry, IMA Volumes in Mathematics and its Applications 149 (M. Putinar and S. Sullivant, eds.), Springer-Verlag, 2009, pp. 157–270.


- [41] L. Lov´asz, On the Shannon capacity of a graph, IEEE Transactions on Information Theory IT-25 (1979) 1–7.
- [42] F. Maurolico, De quinque solidis, quae vulgo regularia dicuntur, quae videlicet eorum locum impleant, et quae non, contra commentatorem Aristotelis, Averroem, 1529.
- [43] R.J. McEliece, E.R. Rodemich, and H.C. Rumsey, Jr., The Lov´asz bound and some generalizations, Journal of Combinatorics, Information & System Sciences 3 (1978) 134–152.
- [44] C.A. Rogers, Packing and Covering, Cambridge University Press, 1964.
- [45] A. Schrijver, A comparison of the Delsarte and Lova´sz bounds, IEEE Transactions on Information Theory IT-25 (1979) 425–429.
- [46] W.A. Stein et al., Sage Mathematics Software (Version 4.8), The Sage Development Team, 2012, http://www.sagemath.org.
- [47] M. Sugiura, Unitary Representations and Harmonic Analysis: An Introduction, Kodansha Scientiﬁc Books, Tokyo, 1990.
- [48] M.S. Viazovska, The sphere packing problem in dimension 8, arXiv:1603.04246 [math.NT], 2016, 22pp.
- [49] G.N. Watson, A Treatise on the Theory of Bessel Functions, Cambridge University Press, 1922.
- [50] G.M. Ziegler, Three Mathematics Competitions, in: An Invitation to Mathematics: From Competitions to Research (D. Schleicher and M. Lackmann, eds.), Springer-Verlag, Berlin, 2011, pp. 195–206.


F.M. de Oliveira Filho, Instituto de Matematica´ e Estat´ıstica, Universidade de Sao˜

Paulo, Rua do Matao,˜ 1010, 05508-090 Sao˜ Paulo, Brazil E-mail address: fmario@gmail.com F. Vallentin, Mathematisches Institut, Universitat¨ zu Koln,¨ Weyertal 86–90, 50931

Koln,¨ Germany E-mail address: frank.vallentin@uni-koeln.de

