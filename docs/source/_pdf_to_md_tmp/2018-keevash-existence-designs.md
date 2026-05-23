arXiv:1802.05900v1[math.CO]16Feb2018

The existence of designs II

Peter Keevash∗ February 19, 2018

Abstract

We generalise the existence of combinatorial designs to the setting of subset sums in lattices with coordinates indexed by labelled faces of simplicial complexes. This general framework includes the problem of decomposing hypergraphs with extra edge data, such as colours and orders, and so incorporates a wide range of variations on the basic design problem, notably Baranyaitype generalisations, such as resolvable hypergraph designs, large sets of hypergraph designs and decompositions of designs by designs. Our method also gives approximate counting results, which is new for many structures whose existence was previously known, such as high dimensional permutations or Sudoku squares.

# 1 Introduction

The existence of combinatorial designs was proved in [15], to which we refer the reader for an introduction to and some history of the problem. There we obtained a more general result on clique decompositions of hypergraphs, that can be roughly understood as saying that under certain extendability conditions, the obstructions to decomposition can already be seen in two natural relaxations of the problem: the fractional relaxation (where we see geometric obstructions) and the integer relaxation (where we see arithmetic obstructions). The main theorem of this paper is an analogous result in a more general setting of lattices with coordinates indexed by labelled faces of simplicial complexes. There are many prerequisites for the statement of this result, so in this introduction we will ﬁrst discuss several applications to longstanding open problems in Design Theory, which illustrate various aspects of the general picture, and give some indication of why it is more complicated than one might have expected given the results of [15].

- 1.1 Resolvable designs In 1850, Kirkman formulated his famous ‘schoolgirls problem’:


Fifteen young ladies in a school walk out three abreast for seven days in succession: it is required to arrange them daily, so that no two shall walk twice abreast.

The general problem is to determine when one can ﬁnd designs that are ‘resolvable’: the set of blocks can be partitioned into perfect matchings. Recall from [15] that a set S of q-subsets of an n-set X is a design with parameters (n,q,r,λ) if every r-subset of X belongs to exactly λ elements

![image 1](<2018-keevash-existence-designs_images/imageFile1.png>)

∗Mathematical Institute, University of Oxford, Oxford, UK. Email: keevash@maths.ox.ac.uk. Research supported in part by ERC Consolidator Grant 647678.

of S, and that such S exists for any n > n0(q,r,λ) satisfying the necessary divisibility conditions that r q−−ii divides λ nr−−ii for 0 ≤ i ≤ r − 1. For a resolvable design, a further necessary condition is that q | n, otherwise there is no perfect matching on X, let alone a partition of S into perfect matchings! We will show that these necessary conditions suﬃce for large n; the case r = 2 of this result was proved in 1973 by Ray-Chaudhuri and Wilson [26, 27].

- Theorem 1.1. Suppose q ≥ r ≥ 1 and λ are ﬁxed and n > n0(q,r,λ) is large with q | n and


- q−i
- r−i | λ nr−−ii for 0 ≤ i ≤ r − 1. Then there is a resolvable (n,q,r,λ) design.


It is convenient to generalise the problem and then translate the generalisation into an equivalent hypergraph decomposition problem. Suppose G ∈ NXr is a r-multigraph supported in an n-set X, where q | n, satisfying the necessary divisibility conditions for a Kqr-decomposition, i.e. r q−−ii divides

{Ge : f ⊆ e} for any i-set f with 0 ≤ i ≤ r (we say G is Kqr-divisible). We also suppose that G is ‘vertex-regular’ in that |G(x)| is the same for all x ∈ X (this is clearly necessary for a resolvable decomposition). Under certain conditions (extendability and regularity) to be deﬁned later, we will show that G has a Kqr-decomposition that is resolvable, i.e. its q-sets can be partitioned into perfect matchings, each of which can be viewed as a Kqr-tiling, i.e. n/q vertex-disjoint Kqr’s.

Now we set up an equivalent hypergraph decomposition problem. Let Y be a set of m vertices disjoint from X, where m is the least integer with1 r m−1 ≥ q|G|/Qn, with Q = qr . Let J be an (r − 1)-graph on Y with |J| = q|G|/Qn = r q−−11 −1|G(x)| for all x ∈ X. Let G′ be the r-multigraph obtained from G by adding as edges (with multiplicity one) all r-sets of the form f ∪ {x} where f ∈ J and x ∈ X. Let H be the r-graph whose vertex set is the disjoint union of a q-set A and an (r − 1)-set B, and whose edges consist of all r-sets in A ∪ B that are contained in A or have exactly one vertex in A.

We claim that a resolvable Kqr-decomposition of G is equivalent to an H-decomposition of G′. To see this, suppose that an H-decomposition H of G′ is given. Let A be the set of the restrictions to A of the copies of H in H. Then A is a Kqr-decomposition of G. Furthermore, for each f ∈ J and x ∈ X there is a unique copy of H in H containing f ∪ {x}, so the elements of A corresponding to copies of H containing f form a perfect matching of X, and every element of A is thus obtained from a unique such f, so A is resolvable. Conversely, any resolvable Kqr-decomposition of G can be converted into an H-decomposition of G′ by assigning an edge of J to each perfect matching in the resolution and forming copies of H in the obvious way.

For general r-graphs H, Glock, Ku¨hn, Lo and Osthus [9] solved the H-decomposition problem for certain structures that they call ‘supercomplexes’, which in particular solves the problem for r-graphs

- G that are ‘typical’ or have large minimum degree: they show that in this setting there is an Hdecomposition if G is H-divisible, i.e. every i-set degree is divisible by the greatest common divisor of the i-set degrees in H. However, the bipartite form of the problem considered here is not covered by their framework; indeed, we will see later in more generality that there are additional complications in partite settings. Our general result on H-decompositions will be of the form discussed above, i.e. that under certain extendability conditions, the obstructions to decomposition appear in the fractional or integer relaxation. However, one should note that there can be additional obstructions in the integer relaxation besides the divisibility conditions mentioned above.


![image 2](<2018-keevash-existence-designs_images/imageFile2.png>)

1 We identify G with its edge set, so |G| denotes the number of edges in G.

## 1.2 Baranyai-type designs

Next we develop the theme suggested by the construction in the previous section, namely that of obtaining variations on the basic design problem that are equivalent to certain partite hypergraph decomposition problems. We will call these Baranyai-type designs, after the classical result of Baranyai [1] that any complete r-graph Knr with r | n can be partitioned into perfect matchings.

One natural question of this type is whether Knq can be decomposed into (n,q,r,λ)-designs; such a decomposition is known as a ‘large set’ of designs. Besides the necessary divisibility conditions discussed above for the existence of one such design, another obvious necessary condition is that the size λ qr −1 nr of each design in the decomposition should divide the size nq of Knq; equivalently, we need λ | nq−−rr . It is natural to conjecture that these necessary divisibility conditions should be suﬃcient, apart from a ﬁnite number of exceptions. Even in the very special case of Steiner Triple Systems, this was a longstanding open problem, settled in 1991 by Teirlinck [29]. Lovett, Rao and Vardy [22] extended the method of [18] to show that if q > 9r, ℓ ∈ N and n > n0(q,r,ℓ) satisﬁes the divisibility conditions then there is a large set of (n,q,r,λ)-designs, where nq = ℓλ qr −1 nr . This settles the existence conjecture when the edge multiplicity λ is within a constant factor of the maximum possible multiplicity, but leaves it open otherwise (for example, it does not include the case of large sets of Steiner systems). We will prove the general form of the existence conjecture for large sets of designs.

- Theorem 1.2. Suppose q ≥ r ≥ 1 are ﬁxed, n > n0(q,r) is large and λ | nq−−rr with all r q−−ii | λ nr−−ii . Then there is a large set of (n,q,r,λ) designs.

As for resolvable designs, we can consider the more general problem of decomposing any qmultigraph G on an n-set X into (n,q,r,λ)-designs. This clariﬁes the general form of the divisibility conditions, as there are several conditions that collapse into one in the case that G = Knq. Indeed, for each 0 ≤ i ≤ r and i-set I ⊆ [n] we need the degree |G(I)| of I to be divisible by the number

Zi := λ r q−−ii −1 nr−−ii of q-sets containing I in any (n,q,r,λ)-design. Furthermore, we clearly need G to be an ‘r-multidesign’, meaning that all |G(e)| with e ∈ [n]r are equal.

Again we formulate an equivalent hypergraph decomposition problem. Let Y be a set of m vertices disjoint from X, where m is the least integer with q m−r ≥ |G|/Z0. Let J be an (q −r)-graph on Y with |J| = |G|/Z0. Let G′ be the q-multigraph obtained from G by adding as edges with multiplicity λ all q-sets of the form e ∪ f with e ⊆ X and f ∈ J. Let H be the q-graph whose vertex set is the disjoint union of a q-set A and a (q − r)-set B, and whose edges consist of A and all q-sets in A∪B that contain B. Then a decomposition of G into (n,q,r,λ)-designs is equivalent to an H-decomposition of G. Indeed, given an H-decomposition H of G, each edge of G appears as exactly one copy of A in H, and for each f ∈ J the copies of A within the copies of H that contain f form an (n,q,r,λ)-design. Conversely, any decomposition of G into (n,q,r,λ)-designs can be converted into an H-decomposition of G by assigning an edge of J to each design in the decomposition.

Another natural example of a Baranyai-type design is what we will call a ‘complete resolution’ of Knq: we partition Knq into Steiner (n,q,q − 1) systems, each of which is partitioned into Steiner (n,q,q − 2) systems, and so on, down to Steiner (n,q,1) systems (which are perfect matchings). Again we show that this exists for n > n0(q) under the necessary divisibility conditions, which take the simple form q − j | n − j for 0 ≤ j < q, i.e. n = q mod lcm([q]).

- Theorem 1.3. Suppose q is ﬁxed and n > n0(q) is large with n = q mod lcm([q]). Then there is a complete resolution of Knq.


To formulate an equivalent hypergraph decomposition problem, we consider disjoint sets of vertices X and Y where |X| = n and Y is partitioned into Yj, 0 ≤ j < q with |Yj| = nq−−jj. We let G′ be the q-graph whose edges are all q-sets e ⊆ X ∪ Y such that |e ∩ Yj| ≤ 1 for all 0 ≤ j < q, and if e ∩ Yj = ∅ then e ∩ Yi = ∅ for all i > j. Let H be the q-graph whose vertex set is the disjoint union of two q-sets A and B = {b0,... ,bq−1}, whose edges are all q-sets e ⊆ A ∪ B such that if bj ∈ e then bi ∈ e for all i > j.

![image 3](<2018-keevash-existence-designs_images/imageFile3.png>)

Then a complete resolution of Knq is equivalent to an H-decomposition of G′. Indeed, given an H-decomposition H of G′, we note that for any yi ∈ Yi for j ≤ i ≤ q the set of copies of A in the copies of H in H that contain {yj,... ,yq} form a Steiner (n,q,j − 1) system, and as yj ranges over Yj we obtain a partition of the Steiner (n,q,j) system corresponding to the copies of H in

- H that contain {yj+1,... ,yq}. Conversely, a complete resolution of Knq can be converted into an H-decomposition of G′ by iteratively assigning vertices of Yj to the Steiner (n,q,j −1) systems that decompose each Steiner (n,q,j) system.


## 1.3 Partite decompositions

The above applications demonstrate the need for hypergraph decomposition in various partite settings. We defer our general statement and just give here some easily stated particular cases. First we consider the nonpartite setting and the typicality condition from [15].

- Deﬁnition 1.4. Suppose G is an r-graph on [n]. The density of G is d(G) = |G| nr −1. We say that G is (c,s)-typical if for any set A of (r − 1)-subsets of V (G) with |A| ≤ s we have |∩f∈AG(f)| = (1 ± |A|c)d(G)|A|n.


We show that any typical r-graph has an H-decomposition provided that it satisﬁes the necessary divisibility condition discussed above (this result was also proved in [9]).

Theorem 1.5. Let H be an r-graph on [q] and G be an H-divisible (c,hq)-typical r-graph on [n], where n = |V (G)| > n0(q) is large, h = 250q3, δ = 2−103q5, d(G) > 2n−δ/hq, c < c0d(G)h30q where c0 = c0(q) is small. Then G has an H-decomposition.

Next we consider the other extreme in terms of partite settings.

- Deﬁnition 1.6. Let H be an r-graph. We call an r-graph G an H-blowup if V (G) is partitioned as (Vx : x ∈ V (H)) and each e ∈ G is f-partite for some f ∈ H, i.e. f = {x : e ∩ Vx = ∅}.


We write Gf for the set of f-partite e ∈ G. For f ∈ H let df(G) = |Gf| x∈f |Vx|−1. We call G a (c,s)-typical H-blowup if for any s′ ≤ s and distinct e1,... ,es′ where each ej is fj-partite for some fj ∈ V (H)r−1, and any x ∈ ∩sj′=1H(fj) we have

Vx ∩

s′

G(ej) = (1 ± s′c)|Vx|

j=1

s′

dfj+x(G).

j=1

We say G has a partite H-decomposition if it has an H-decomposition using copies of H with one vertex in each part Vx.

We say G is H-balanced if for every f ⊆ V (H) and f-partite e ⊆ V (G) there is some ne such that |Gf′(e)| = ne for all f ⊆ f′ ∈ H.

Note that if G has a partite H-decomposition then G is H-balanced; we establish the converse for typical H-blowups.

- Theorem 1.7. Let H be an r-graph on [q] and G be an H-balanced (c,hq)-typical H-blowup on (Vx : x ∈ V (H)), where each n/h ≤ |Vx| ≤ n for some large n > n0(q) and h = 250q3, δ = 2−103q5, df(G) > d > 2n−δ/hq for all f ∈ H and c < c0dh30q, where c0 = c0(q) is small. Then G has a partite H-decomposition.

For example, if H = Krr+1 and G = Krr+1(n) is the complete (r+1)-partite r-graph with n vertices in each part then Theorem 1.7 shows the existence of an object known variously as an r-dimensional permutation or latin hypercube. (It can be viewed as an assignment of 0 or 1 to the elements of [n]r+1 so that every line has a unique 1, or as an assignment of [n] to the elements of [n]r so that each line contains every element of [n] exactly once.) The result for general G implies a lower bound on the number of r-dimensional permutations: we can estimate the number of choices for an almost H-decomposition by analysing a random greedy algorithm, and show that almost all of these can be completed to an (actual) H-decomposition (we omit the details of the proof, which are similar to those in [16]). In combination with the upper bound of Linial and Luria [21] we obtain the following answer to an open problem from [21].

- Theorem 1.8. The number of r-dimensional permutations of order n is (n/er + o(n))nr.

More generally, many applications of our main theorem can be similarly converted to an approximate counting result, where the upper bound comes from a general bound by Luria [23] on the number of perfect matchings in a uniform hypergraph with small codegrees (for example, we could give such estimates for the number of resolvable designs or large sets of designs). Another example2 is the following estimate for the number of (generalised) Sudoku squares (the theorem says nothing about the squares of the popular puzzle, in which n = 3).

- Theorem 1.9. The number of Sudoku squares with n2 boxes of order n is (n2/e3 + o(n2))n4.


## 1.4 Colours and labels

There are many questions in design theory that are naturally expressed as a decomposition problem for hypergraphs with extra data associated to edges, such as colours or vertex labels. A decomposition theorem for coloured multidigraphs with several such applications was given by Lamken and Wilson [20]. Here we illustrate one such application and an example of a hypergraph generalisation. (There are many other such applications, but for the sake of brevity we leave a detailed study for future research.)

The Whist Tournament Problem (posed in 1896 by Moore [24]) is to ﬁnd a schedule of games for 4n players, where in each game two players oppose two others, such that (1) the games are arranged into rounds, where each player plays in exactly one game in each of the rounds, (2) each player partners every other player exactly once and opposes every other player exactly twice. (There is also a similar problem for 4n + 1 players in which one player sits out in each round.) Whist Tournaments exist for all n (see [5, Chapter VI.64]). If we remove condition (1) we obtain the Whist Table Problem. As observed in [20], we obtain an equivalent form of the latter by considering a red/blue coloured multigraph on the set of players, where between each pair of players there is one

![image 4](<2018-keevash-existence-designs_images/imageFile4.png>)

2 Alexey Pokrovskiy drew this to my attention. Our theorem does not apply to the construction given by Luria [23], but it is not hard to give a suitable alternative construction. For example, let H be the 4-graph with V (H) = {x1, x2, y1, y2, z1, z2} and E(H) = {x1x2y1y2, x1x2z1z2, y1y2z1z2, x1y1z1z2}. Then an H-decomposition of the complete n-blowup of H can be viewed as a Sudoku square, where we represent rows by pairs (a1, a2), columns by (b1, b2), symbols by (c1, c2) and boxes by (a1, b1); a copy of H with vertices {a1, a2, b1, b2, c1, c2} represents a cell in row (a1, a2) and column (b1, b2) with symbol (c1, c2).

red edge (‘partner’) and two blue edges (‘oppose’), and we seek a decomposition into copies of K4 coloured as a blue C4 with two red diagonals. The Whist Tournament Problem is equivalent to a partite decomposition problem that ﬁts into our framework, but not that of [20] (which only covers the case of 4n + 1 players).

There are many ways to formulate similar problems with more complexities, such as larger teams and particular roles for players within teams. Here we describe a ﬁctional illustration of this idea, which we may call a ‘tryst tournament’ (sports aﬁcionados will no doubt be able to provide real examples). A tryst team consists of three players, one of whom is designated the captain. A tryst game is played by nine players divided into three tryst teams. The Tryst Table Problem is to ﬁnd a schedule of tryst games for n players, such that (1) for every triple T of players and every x ∈ T there is exactly one game in which T is a team and x is the captain, (2) for every triple T of players there is exactly one game in which T is the set of captains of the three teams in that game.3

- Theorem 1.10. The Tryst Table Problem has a solution for all suﬃciently large n. We reformulate the Tryst Table Problem (somewhat vaguely at ﬁrst) as follows. Form a ‘structure’


- G on the set V of players by including a red triple (‘captains’) for each triple and a blue ‘pointed’ triple (‘teams’) for each triple T and x ∈ T. We want to decompose G by copies of a ‘structure’ H on 9 vertices, with 3 vertex-disjoint blue pointed triples, and a red triple consisting of the points of the blue triples.

To make sense of the undeﬁned terms just used we now switch to a setting in which all edges come with labels on their vertices, so our fundamental object becomes a set of functions (instead of a hypergraph, which is a set of sets). For the Tryst Table Problem, we let G∗ contain a red copy and a blue copy of each injection from [3] to V . We deﬁne a set H∗ of red and blue injections from [3] to [9] as follows, in which we imagine that three teams are labelled 123, 456 and 789 with captains

- 1, 4 and 7. The red functions of H∗ consist of all bijections from [3] to 147. The blue functions of


- H∗ consist of all bijections from [3] to one of the teams 123, 456 or 789, such that 1 is mapped to the captain. A copy of H∗ in G∗ is deﬁned by ﬁxing any injection φ : [9] → V and composing all functions in H∗ with φ; the interpretation of this copy is a tryst game between teams φ(123), φ(456) and φ(789) with captains φ(1), φ(4) and φ(7). It is clear that the Tryst Table Problem is equivalent to ﬁnding an H∗-decomposition of G∗.


Our main theorem is a decomposition result for vectors where coordinates are indexed by functions and take values in some lattice ZD. The ‘subcoordinates’ in ZD may be interpreted as colours, so e.g. we may think of Jψ = (2,3) ∈ Z2 as saying that J has 2 red copies and 3 blue copies of some function ψ. This general framework includes all of the problems discussed above and many other variations thereupon (see subsection 2.4 for more examples).

One consequence of our main theorem is a generalisation of the hypergraph decomposition result alluded to above to decompositions of coloured multihypergraphs by coloured hypergraphs. It seems hard to describe the divisibility conditions in general, so here we will specialise to the setting of rainbow clique decompositions, for which the divisibility conditions are quite simple. We write [ qr ]Knr for the r-multigraph on [n] in which there are qr copies of each r-set coloured by [ qr ] = {1,... , qr }. We ask when [ qr ]Knr can be decomposed into rainbow copies of Kqr, i.e. copies of Kqr in

![image 5](<2018-keevash-existence-designs_images/imageFile5.png>)

3 We choose these simple rules for simplicity of exposition, and there is no doubt a direct proof of Theorem 1.10 not using our main theorem. The point is that one can use the same method to analyse variations with more rules, such as a Tryst Tournament Problem (arranging the games into rounds) and/or constraining more triples, e.g. we could also ask for every triple T of players and every x ∈ T to have exactly two games in which x captains a team and T \ {x} is the set of non-captains in a diﬀerent team.

[ qr ]Knr in which the colours of edges are all distinct. A stricter version of the question is to ﬁx some rainbow colouring of Kqr and only allow the decomposition to use copies of Kqr that are isomorphic to the ﬁxed rainbow colouring. We will answer both versions of the question.

First we consider the question in which we allow any rainbow Kqr. Ignoring colours, we have the same necessary divisibility condition as before for the multigraph qr Knr to have a Kqr-decomposition, namely r q−−ii | qr nr−−ii for 0 ≤ i ≤ r −1. We will show that under the same conditions we even have a rainbow Kqr-decomposition.

- Theorem 1.11. Suppose n > n0(q) is large and r q−−ii | qr nr−−ii for 0 ≤ i ≤ r − 1. Then [ qr ]Knr has a rainbow Kqr-decomposition.

Now suppose that we only allow copies of some ﬁxed rainbow colouring. For convenient notation we identify the set of colours with [q]r := {B ⊆ [q] : |B| = r} and suppose that in the ﬁxed colouring of [q]r we colour each set by itself. We write [q]rKnr for the corresponding relabelling of [ qr ]Knr. Any injection φ : [q] → [n] deﬁnes a copy of [q]r where for each B ∈ [q]r we use the colour B copy of φ(B). We say [q]rKnr has a [q]r-decomposition if it can be decomposed into such copies.

- Theorem 1.12. Suppose n > n0(q) is large and ri | nr−−ii for 0 ≤ i ≤ r − 1. Then [q]rKnr has a [q]r-decomposition.


The divisibility conditions in Theorem 1.12 are necessary for r ≤ q/2 but not in general.4 To see necessity, suppose D is a [q]r-decomposition of [q]rKnr. Identify each copy φ([q]r) with a vector vφ ∈ (Z[q]r)Knr where each vφφ(B) = eB (the standard basis vector for B ∈ [q]r). For any f ∈ [n]i we have {veφ : f ⊆ e ∈ Knr,φ ∈ D} = nr−−ii 1 ∈ Z[q]r equal to nr−−ii in each coordinate. On the other hand, the contribution of any given φ([q]r) to this sum is {eB : φ−1(f) ⊆ B}, which is a row of the inclusion matrix Mir(q): this has rows indexed by [q]i, columns by [q]r and each Mir(q)fe = 1f⊆e. As Mir(q) has full row rank (by Gottlieb’s Theorem [10], using r ≤ q/2), each row must appear the same number of times, say m, and then any B ∈ [q]r contributes m ri times, so ri | nr−−ii .

![image 6](<2018-keevash-existence-designs_images/imageFile6.png>)

## 1.5 Decomposition lattices

Here we will give some indication of what new ideas are needed in the general setting besides those in [15]. We start by recalling the proof strategy in [15] for clique decompositions of hypergraphs that are extendable and have no obstruction (fractional or integer) to decomposition. The ﬁrst step is a Randomised Algebraic Construction, which results in a partial decomposition (the ‘template’) that covers a constant fraction of the edge set, and carries a rich structure of possible local modiﬁcations. By the nibble and other random greedy algorithms, we can choose another partial decomposition that covers all edges not in the template, which also spills over slightly into the template, so that every edge is covered once or twice, and very few edges (the ‘spill’) are covered twice.

Next we ﬁnd an ‘integral decomposition’ of the spill, and apply a ‘clique exchange algorithm’ that replaces the integral decomposition by a ‘signed decomposition’, i.e. two partial decompositions, called ‘positive’ and ‘negative’, such that the underlying hypergraph of the negative decomposition is contained in that of the positive decomposition, and the diﬀerence forms a ‘hole’ that is precisely equal to the spill. We also ensure that for each positive clique Q+ there is a modiﬁcation (a ‘cascade’) to the clique decomposition of the template so that it contains Q+. Then deleting the positive cliques

![image 7](<2018-keevash-existence-designs_images/imageFile7.png>)

4 The precise divisibility conditions can be extracted from our characterisation of the divisibility lattice, but we omit this for the sake of a simple illustration.

and replacing them by the negative cliques eliminates one of the two uses of each edge in the spill, and we end up with a perfect decomposition.

In broad terms, the strategy of the proof in this paper is similar. Furthermore, much of the proof for designs can be adapted to the general setting (we give the details of this in section 3). However, the ‘integral decomposition’ step becomes much more diﬃcult (and it is necessary to overcome these diﬃculties, as this is a relaxation of the problem we are trying to solve). There are in fact two aspects of this step, which both become much more diﬃcult: (i) characterising the decomposition lattice (i.e. the set of Z-linear combinations of the vectors that we allow in our decomposition), (ii) ﬁnding bounded integral decompositions. Regarding (ii), there is a ‘local decoding’ trick for designs that greatly simpliﬁes the proof of [15, Lemma 5.12] (version 2), but in the general setting we do not have local decodability, so we revert to the original randomised rounding method of [15] (version 1).

As for (i), we give a cautionary example here to show that the decomposition lattice is in general not what one might guess given its simple structure for designs. Let us ﬁrst recall the characterisation by Graver and Jurkat [12] and Wilson [34] of the set of J ∈ ZKnr with an integral Kqr-decomposition, i.e. the Z-linear combinations of (characteristic vectors of) copies of Kqr. Clearly, any such J is Kqr-divisible (as deﬁned above), and the converse is also true for n ≥ q + r. For partite problems there may be additional ‘balance’ constraints (as in Theorem 1.7) but there may be further more subtle constraints.

Let us consider the decomposition lattice of the triangles of a rainbow K4, deﬁned as follows. Fix any bijection b : E(K4) → [6] and colouring c : E(Kn) → [6]. Let B be the set of all bcoloured copies of K43, i.e. for each injection φ : [4] → [n] such that all c(φ(i)φ(j)) = b(ij) we include {φ([4]\{i}) : i ∈ [4]}. We wish to characterise the lattice  B  generated by B. Certainly any J ∈  B  must be K43-divisible and supported on the set T of triangles that appear in B. One might guess by analogy with the lattice of K43’s in a random 3-graph (see [15]) that if c is random then whp there would be no further condition.

However, we will now describe a K43-divisible vector (a ‘twisted octahedron’) that is not in  B . Suppose that b(12) = 3, b(13) = 2, b(23) = 1, b(14) = 4, b(24) = 5, b(34) = 6. Consider any octahedron, i.e. complete tripartite graph, with parts {x0,x1}, {y0,y1}, {z0,z1} coloured so that all c(yizj) = 1, c(x0y0) = c(x0y1) = c(x1z0) = c(x1z1) = 2, c(x1y0) = c(x1y1) = c(x0z0) = c(x0z1) = 3. Then every triangle xiyjzk is rainbow. Let J ∈ ZT be ±1 on these triangles and 0 otherwise, with Jxiyjzk = (−1)i+j+k. Then J is null ( {Je : f ⊆ e ∈ T } = 0 whenever |f| ≤ 2) so is K43-divisible.

To see J ∈/  B  we use the colouring to deﬁne an algebraic invariant. For each triangle T = xy0z0 ∈ T containing y0z0 we let f(T) be one of the standard basis vectors of Z4 according to the colouring of T: we let f(T) be e1, e2, e3 or e4 according to whether (c(xy0),c(xz0)) is (2,3), (3,2), (5,6) or (6,5). We extend f to a Z-linear map from ZT to Z6, where f(T′) = 0 if T′ does not contain y0z0. If J′ ∈  B  then f(J′) lies in the lattice generated by (1,0,1,0) and (0,1,0,1). However, we have f(J) = (1,−1,0,0), so J ∈/  B . This example hints at the importance of vertex labels (even when not explicitly presented in a problem) when characterising decomposition lattices.

## 1.6 Organisation

The organisation of this paper is as follows. In the next section we set up our general framework of labelled complexes and vector-valued decompositions, and develop some basic theory of these deﬁnitions that will be used throughout the paper. In section 3 we state our main theorem and present those parts of the proof that are somewhat similar to those in [15]. We deﬁne and analyse the Clique Exchange Algorithm in section 4. We complete the proof of our main theorem by solving

the problems of integral decomposition (section 5) and bounded integral decomposition (section 6). Section 7 gives several applications of our main theorem.

## 1.7 Notation

Most of the following notation is as in [15]. Let [n] = {1,... ,n}. Let Sr denote the set of r-subsets of S. We write Q = [rq] and also Q = qr (the use will be clear from the context). We identify Q = [rq] with the edge set of Kqr (the complete r-graph on [q]). We write Kqr(S) for the complete q-partite r-graph with parts of size |S| where each part is identiﬁed with S. If S = [s] we write Kqr(S) = Kqr(s).

We use ‘concatenation notation’ for sets (xyz may denote {x,y,z}) and for function composition

(fg may denote f ◦ g). We say E holds with high probability (whp) if P(E) = 1 − e−Ω(nc) for some c > 0 as n → ∞. We write Y X for the set of vectors with entries in Y and coordinates indexed by X, which we also

identify with the set of functions f : X → Y . For example, we may consider v ∈ Fqp as an element of a vector space over Fp or as a function from [q] to Fp.

We identify v ∈ {0,1}X with the set {x ∈ X : vx = 1}, and v ∈ NX with the multiset in X in which x has multiplicity vx (for our purposes 0 ∈ N). We often consider algorithms with input v ∈ ZX, where each x ∈ X is considered |vx| times, with a sign attached to it (the same as that of vx); then we refer to x as a ‘signed element’ of v.

If G is a hypergraph, v ∈ ZG and e ∈ G we deﬁne v(e) ∈ ZG(e) by v(e)f = ve∪f for f ∈ G(e). We denote the standard basis vectors in Rd by e1,... ,ed. Given I ⊆ [d], we let eI denote the I

by [d] matrix in which the row indexed by i ∈ I is ei.

We write M ∈ Fpq×r to mean that M is a matrix with q rows and r columns having entries in Fp. For I ∈ Q = [qr] we let MI be the square submatrix with rows indexed by I. Note that MI = eIM.

We will regard Fpa as a vector space over Fp. For e ⊆ Fpa we write dim(e) for the dimension of

the subspace spanned by the elements of e. For e ∈ Fdpa we write dim(e) for the dimension of the set of coordinates of e.

When we use ‘big-O’ notation, the implicit constant will depend only on q. We write a = b ± c to mean b − c ≤ a ≤ b + c. Throughout the paper we omit ﬂoor and ceiling symbols where they do not aﬀect the argument. We also use the following notation (not from [15]). Let Bij(B,B′) denote the set of bijections from B to B′. Let Inj(B,V ) denote the set of injections from B to V . We extend our concatenation notation to sets of functions, e.g. φΥ = {φ ◦ ψ : ψ ∈ Υ}. We let ∅ denote the empty set and also the unique function with empty domain. For any set X write Xj = Xj (convenient notation for use in exponents). We write [q](S) for the set of partite maps f : [q] → [q] × S. We write Im(φ) and Dom(φ) for the image and domain of a function φ. We write ψ ⊆ φ for functions ψ and φ if ψ is a restriction of φ. Then φ\ψ denotes the restriction

of φ to Dom(φ) \ Dom(ψ). Given functions φj on Aj for j = 1,2 that agree on A1 ∩ A2 we write φ1 ∪ φ2 for the function on A1 ∪ A2 that restricts to φj on Aj for j = 1,2.

Given Γ ⊆ R, the Γ-span of S ⊆ Rd is S Γ = { x∈S Φxx : Φ ∈ ΓS}. We write S = S Z. If u ∈ (ZD)X we write |u| = x∈X d∈[D] |(ux)d|.

# 2 Basic structures

In this section we deﬁne the basic objects needed for the statement of our main theorem and record some simple properties of them that will be used throughout the paper. We start in the ﬁrst subsection with the labelled complex structure that is the functional analogue of a simplicial complex. The second subsection concerns embeddings and extensions of labelled complexes, and deﬁnes the extendability property mentioned in the introduction. In the third subsection we consider adapted complexes, in which we add the structure of a permutation group that acts on labellings: the orbits of this action play the role of edges in the example of hypergraph decomposition. Then in the fourth subsection we formalise our general decomposition problem with respect to a superimposed system of vector values on functions; here we also show how to realise several concrete examples within this general framework. We describe some basic properties of vector-valued decompositions in the ﬁfth subsection and introduce some terminology (atoms and types) for them; we also deﬁne the regularity property that formalises the ‘no fractional obstacle’ assumption discussed above.

- 2.1 Complexes We start by deﬁning a structure that we call a labelled complex.5


- Deﬁnition 2.1. (labelled complexes) We call Φ = (ΦB : B ⊆ R) an R-system on V if φ : B → V is injective for each φ ∈ ΦB. We call an R-system Φ an R-complex on V if whenever φ ∈ ΦB and B′ ⊆ B


we have φ |B′∈ ΦB′. Let Φ◦B = {φ(B) : φ ∈ ΦB}, Φ◦j = {Φ◦B : B ∈ Rj } and Φ◦ = {Φ◦B : B ⊆ R}. We write V (Φ) = Φ◦1.

Note that if A ⊆ A′ ∈ Φ◦B′ then A ∈ Φ◦B for some B ⊆ B′ (not necessarily unique); thus Φ◦ is a (simplicial) complex. We will now deﬁne some basic operations (forming restrictions and neighbourhoods) for working with labelled complexes.

- Deﬁnition 2.2. (restriction) Let Φ be an R-complex and Φ′ an R-system. We let Φ[Φ′] be the


R-system where Φ[Φ′]B is the set of φ ∈ ΦB such that φ |B′∈ Φ′B′ for all B′ ⊆ B such that Φ′B′ is deﬁned (we allow some Φ′B′ to be undeﬁned). If Φ′x = U ⊆ V (Φ) for all x ∈ R and Φ′B is undeﬁned otherwise then we also write Φ[Φ′] = Φ[U] = {φ ∈ Φ : Im(φ) ⊆ U}.

Lemma 2.3. Φ[Φ′] is an R-complex.

Proof. Consider φ ∈ Φ[Φ′]B and B∗ ⊆ B such that Φ′B∗ is deﬁned. We need to show φ |B∗∈ Φ[Φ′]B∗. To see this, note that φ |B∗∈ ΦB∗, and if B′ ⊆ B∗ is such that Φ′B′ is deﬁned then (φ |B∗) |B′= φ |B′∈ Φ′B′ as φ ∈ Φ[Φ′].

- Deﬁnition 2.4. Let Φ be an R-complex and φ∗ ∈ Φ. We write Φ |φ∗= {φ ∈ Φ : φ∗ ⊆ φ}.
- Deﬁnition 2.5. (neighbourhoods) Let Φ be an R-complex and φ∗ ∈ ΦB∗. For φ ∈ (Φ |φ∗)B∪B∗ with B ⊆ R \ B∗ let φ/φ∗ = φ |B. We deﬁne an (R \ B∗)-system Φ/φ∗ where each (Φ/φ∗)B consists of


all φ/φ∗ with φ ∈ (Φ |φ∗)B∪B∗. For J ∈ ΓΦ we deﬁne J/φ∗ ∈ ΓΦ/φ∗ by (J/φ∗)φ/φ∗ = Jφ whenever φ∗ ⊆ φ.

Lemma 2.6. Φ/φ∗ is an R \ B∗-complex. Proof. Consider B′ ⊆ B ⊆ R \ B∗ and φ/φ∗ ∈ (Φ/φ∗)B. We need to show (φ/φ∗) |B′∈ (Φ/φ∗)B′. This holds as φ′ := φ |B∗∪B′∈ ΦB∗∪B′ with φ′ |B∗= φ∗.

![image 8](<2018-keevash-existence-designs_images/imageFile8.png>)

5 We suppress the term ‘labelled’ in our terminology, as the labels are indicated by the labelling set R.

## 2.2 Embeddings and extensions

Here we formulate our extendability property and show that it is maintained under taking neighbourhoods. We start by deﬁning embeddings of labelled complexes.

- Deﬁnition 2.7. Let H and Φ be R-complexes. Suppose φ : V (H) → V (Φ) is injective. We call φ a Φ-embedding of H if φ ◦ ψ ∈ Φ for all ψ ∈ H.

We will deﬁne extendability using the following labelled complex of partite maps.

- Deﬁnition 2.8. Let R(S) be the R-complex of all partite maps from R to R × S, i.e. whenever i ∈ B ⊆ R and ψ ∈ R(S)B we have ψ(i) = (i,x) for some x ∈ S. If S = [s] we write R(S) = R(s).

The following extendability property can be viewed as a labelled analogue of that in [15].6

- Deﬁnition 2.9. Suppose H ⊆ R(S) is an R-complex and F ⊆ V (H). Deﬁne H[F] ⊆ R(S) by H[F] = {ψ ∈ H : Im(ψ) ⊆ F}. Suppose φ is a Φ-embedding of H[F]. We call E = (H,F,φ) a Φ-extension of rank s = |S|. We say E is simple if |V (H) \ F| = 1.

We write XE(Φ) for the set or number of Φ-embeddings of H that restrict to φ on F. We say E is ω-dense (in Φ) if XE(Φ) ≥ ω|V (Φ)|vE, where vE := |V (H) \ F|. We say Φ is (ω,s)-extendable if all Φ-extensions of rank s are ω-dense.

We will also require the following extension of the previous deﬁnition that allows for a system of extra restrictions.

- Deﬁnition 2.10. Let Φ be an R-complex and Φ′ = (Φt : t ∈ T) with each Φt ⊆ Φ. Let E = (H,F,φ) be a Φ-extension and H′ = (Ht : t ∈ T) for some mutually disjoint Ht ⊆ H \ H[F]; we call (E,H′) a (Φ,Φ′)-extension.

We write XE,H′(Φ,Φ′) for the set or number of φ∗ ∈ XE(Φ) with φ∗ ◦ ψ ∈ ΦtB whenever ψ ∈ HBt

and ΦtB is deﬁned. We say (E,H′) is ω-dense in (Φ,Φ′) if XE,H′(Φ,Φ′) ≥ ω|V (Φ)|vE. We say (Φ,Φ′) is (ω,s)-extendable if all (Φ,Φ′)-extensions of rank s are ω-dense in (Φ,Φ′).

When |T| = 1 we identify Φ′ ⊆ Φ with (Φ′). We also write XE(Φ,Φ′) = XE,H\H[F](Φ,Φ′). For L ⊆ Φ◦ we write XE(Φ,L) = XE(Φ,Φ′) where Φ′ = {φ ∈ Φ : Im(φ) ∈ L}; we also write Φ[L] = Φ[Φ′], and say that (Φ,L) is (ω,s)-extendable if (Φ,Φ′) is (ω,s)-extendable.

If L ⊆ V (Φ) we also say that (Φ,L) is (ω,s)-extendable wrt L if XE,H′(Φ,Φ′) ≥ ω|L|vE for all (Φ,Φ′)-extensions (E,H′) of rank s.

Note that if Φ′ ⊆ Φ and (Φ,Φ′) is (ω,s)-extendable then Φ[Φ′] is (ω,s)-extendable. In the next deﬁnition we combine the operations of taking neighbourhoods and restriction to an (unordered) hypergraph; the accompanying lemma shows that under the generalised extendability condition of the previous condition the resulting labelled complex is extendable. We note that if L = Φ◦r the restriction has no eﬀect, so Φ/φ∗L = Φ/φ∗, and in this case Lemma 2.12 states that if Φ is (ω,s)extendable then Φ/φ∗ is (ω,s)-extendable. A less trivial example is when L ⊆ V (Φ) = Φ◦1; then Φ/φ∗L = (Φ/φ∗)[L] is obtained by restricting Φ/φ∗ to L.

- Deﬁnition 2.11. Suppose Φ is an R-complex, L ⊆ Φ◦r and φ∗ ∈ ΦB∗. Let Φ/φ∗L be the set of all φ/φ∗ ∈ Φ/φ∗ such that e ∈ L for all e ∈ Im(φ)r with e \ Im(φ∗) = ∅.


- Lemma 2.12. If (Φ,L) is (ω,s)-extendable (wrt L) then Φ/φ∗L is (ω,s)-extendable. 6 The unlabelled analogue of our assumption here is weaker than that in [15], as we only consider partite extensions.


![image 9](<2018-keevash-existence-designs_images/imageFile9.png>)

Proof. Consider any Φ/φ∗L-extension E = (H,F,φ) where H ⊆ (R\B∗)(s). We need to show that E is ω-dense in Φ/φ∗L. To see this, we consider H+ ⊆ R(s) where for each B ⊆ R \ B∗, B′ ⊆ B∗, ψ ∈ HB we include ψ ∪B′ in HB+∪B′ deﬁned by (ψ ∪B′) |B= ψ and (ψ ∪B′)(i) = i = (i,1) for i ∈ B′. Consider the Φ-extension E+ = (H+,F+,φ ∪ φ∗) with F+ = F ∪ B∗.

As (Φ,L) is (ω,s)-extendable, we have XE+(Φ,L) > ω|V (Φ)|vE+, or XE+(Φ,L) > ω|L|vE+ if (Φ,L) is (ω,s)-extendable wrt L. It remains to show that if φ+ ∈ XE+(Φ,L) then φ+ |V (H)∈ XE(Φ/φ∗L). For any B ⊆ R \ B∗, ψ ∈ HB as φ+ ∈ XE+(Φ) we have φ′ := φ+ ◦ (ψ ∪ B∗) ∈ ΦB∪B∗, and as φ′ |B∗= φ∗ we have φ+ |V (H) ◦ψ = φ′ |B= φ′/φ∗ ∈ (Φ/φ∗)B. Furthermore, as φ+ ∈ XE+(Φ,L) we have e ∈ L for any e ∈ Im(φ+)r with e \ Im(φ∗) = ∅. Therefore φ+ |V (H)∈ XE(Φ/φ∗L).

## 2.3 Adapted complexes

Next we introduce the setting of adapted complexes, where we have a permutation group acting on the functions in a labelled complex. We start with some notation for permutation groups; in particular, given a permutation group Σ on R we deﬁne an R-complex Σ≤ that consists of all restrictions of elements of Σ.

- Deﬁnition 2.13. Suppose Σ is a permutation group on R. For B,B′ ⊆ R we write ΣBB′ = {σ |B: σ ∈ Σ,σ(B) = B′}, ΣB = ∪B′ΣBB′, ΣB′ = ∪BΣBB′, Σ[B] = ∪B′⊆BΣB′, Σ≤ = ∪B,B′ΣBB′.

We let PΣ be the equivalence classes of the relation B ∼ B′ ↔ ΣBB′ = ∅. Note that B ∼ B′ implies |B| = |B′|. We write PjΣ = {C ∈ PΣ : B ∈ C ⇒ |B| = j}.

We will restrict attention to labelled complexes in which any function can be relabelled under the group action, as follows.

- Deﬁnition 2.14. (adapted) Suppose Φ is an R-complex and Σ is a permutation group on R. For σ ∈ Σ and φ ∈ Φσ(B) let φσ = φ ◦ σ |B. We say Φ is Σ-adapted if φσ ∈ Φ for any φ ∈ Φ, σ ∈ Σ.

Next we introduce some notation for the orbits of the action implicit in the previous deﬁnition; these will play the role of edges in hypergraph decompositions.

- Deﬁnition 2.15. (orbits)

For ψ ∈ ΦB with B ⊆ R we deﬁne the orbit of ψ by ψΣ := ψΣB = {ψσ : σ ∈ ΣB}. We denote the set of orbits by Φ/Σ. We write ΦC = ∪B∈CΦB for C ∈ PΣ. We write Im(O) = Im(ψ) for ψ ∈ O ∈ Φ/Σ. For O,O′ ∈ Φ/Σ we write O ⊆ O′ if there are ψ ∈ O, ψ′ ∈ O′ with ψ ⊆ ψ′.

Note that the orbits partition Φ and ΦC = {ψΣ : ψ ∈ ΦB} for any B ∈ C. When we later consider functions on Φ we will decompose them by orbits as follows.

- Deﬁnition 2.16. (orbit decomposition) Let Γ be an abelian group. For J ∈ ΓΦr and O ∈ Φr/Σ we


r/Σ JO. Now we will illustrate the role of orbits with the two most obvious examples (see also subsection

deﬁne JO by JψO = Jψ1ψ∈O. The orbit decomposition of J is J = O∈Φ

### 2.4 for more examples). Examples.

- i. If Σ = {idR} is the trivial group then each equivalence class and orbit has size 1, and we can identify Φ with Φ/Σ. This choice of Σ is suitable for ‘fully partite’ hypergraph decompositions, in which every edge is uniquely labelled by the set of parts that it meets. We also denote Σ≤ by −→R, or by −→q when R = [q]. Then −→q B = {idB} for all B ⊆ [q].


- ii. If Σ is the symmetric group SR on R then the equivalence classes of PΣ are Rr for 0 ≤ r ≤ |R|.


We also denote Σ≤ by R≤. Then each RB≤ = Inj(B,R) consists of all injections from B to R. We can identify Φ◦ with Φ/Σ, where e ∈ Φ◦ is identiﬁed with {ψ ∈ Φ : Im(ψ) = e}. This

choice of Σ is suitable for nonpartite hypergraph decompositions, in which the labels play no essential role.

Next we show that adapted complexes have neighbourhoods that are also adapted complexes.

- Deﬁnition 2.17. Let Σ be a permutation group on R. For B∗ ⊆ R and σ ∈ Σ with σ |B∗= idB∗ we write σ/B∗ = σ |R\B∗. We let Σ/B∗ be the set of all such σ/B∗.


Note that Σ/B∗ is a permutation group on R \ B∗.

- Lemma 2.18. Let Φ be a Σ-adapted R-complex and φ∗ ∈ ΦB∗. Then Φ/φ∗ is a Σ/B∗-adapted (R \ B∗)-complex.


Proof. Suppose B ⊆ R \ B∗, σ = σ′/B∗ ∈ Σ/B∗ and ψ = ψ′/φ∗ ∈ (Φ/φ∗)B. As Φ is Σ-adapted, ψ′σ′ ∈ Φ, so ψσ = ψ′σ′/φ∗ ∈ Φ/φ∗.

Next we introduce the labelled complex structure deﬁned by embeddings of one labelled complex in another.

- Deﬁnition 2.19. Given R-complexes Φ and A we let A(Φ) denote the set of Φ-embeddings of A.


We let A(Φ)≤ denote the V (A)-complex where each A(Φ)≤F for F ⊆ V (A) is the set of Φ-embeddings of A[F].

In the next subsection we will apply Deﬁnition 2.19 with A = Σ≤; we conclude this subsection by showing that if Φ is Σ-adapted then we can identify the resulting complex of embeddings with Φ itself.

- Lemma 2.20. If Φ is Σ-adapted and B ⊆ [q] then Σ[B](Φ) = ΦB.


Proof. Consider any φ ∈ ΦB. As Φ is Σ-adapted, for any σ ∈ ΣB we have φσ ∈ Φ. As Φ is a [q]-complex we deduce φσ ∈ Φ for any σ ∈ Σ[B], so φ ∈ Σ[B](Φ). Conversely, if φ ∈ Σ[B](Φ) then φ = φ idB ∈ ΦB.

## 2.4 Vector-valued decompositions

Now we introduce our general framework for decomposing vectors with coordinates indexed by the functions of a labelled complex and entries in some abelian group. We follow the deﬁnition with several examples to show how it captures hypergraph decompositions and other related problems.

- Deﬁnition 2.21. Let A be a set of R-complexes; we call A an R-complex family. If each A ∈ A is


a copy of Σ≤ we call A a Σ≤-family. For r ∈ N we write Ar = {AB : B ∈ Rr } and Ar = ∪A∈AAr. We let A(Φ)≤ denote the V (A)-complex family (A(Φ)≤ : A ∈ A).

Let γ ∈ ΓAr for some abelian group Γ; we call γ a Γ-system for Ar. Let Φ be an R-complex. For φ ∈ A(Φ)≤ with A ∈ A we deﬁne γ(φ) ∈ ΓΦr by γ(φ)φ◦θ = γθ for

θ ∈ Ar (zero otherwise). We call γ(φ) a γ-molecule and let γ(Φ) be the set of γ-molecules.

Given Ψ ∈ ZA(Φ) we deﬁne ∂Ψ = ∂γΨ = φ Ψφγ(φ) ∈ ΓΦr. We also call Ψ an integral γ(Φ)decomposition of G = ∂Ψ and call γ(Φ) the decomposition lattice. If furthermore Ψ ∈ {0,1}A(Φ) (i.e. Ψ ⊆ A(Φ)) we call Ψ a γ(Φ)-decomposition of G.

Examples.

- i. Suppose H and G are r-graphs with V (H) = [q]. Let Φ be the complete [q]-complex on V (G), i.e. all ΦB = Inj(B,V (G)). Let G∗ = {ψ ∈ Φr : Im(ψ) ∈ G}. Let Σ = S[q], A = {A} with A = Σ≤, and γ ∈ {0,1}Ar with each γθ = 1Im(θ)∈H. Note that Φ is Σ-adapted. For any

φ ∈ A(Φ) = Φq and θ ∈ Ar we have γ(φ)φθ = γθ = 1Im(θ)∈H, so an (integral) H-decomposition of G is equivalent to a (an integral) γ(Φ)-decomposition of G∗. Similarly, if H is a family of r-graphs, by introducing isolated vertices we may assume they all have vertex set [q]. Then an H-decomposition of G is equivalent to a γ(Φ)-decomposition of G∗, where now A contains AH deﬁned as above for each H ∈ H, and γθ is as deﬁned above whenever θ ∈ AHr .

- ii. We generalise the previous example (for simplicity we revert to one r-graph H). Now suppose H and G have coloured edges. Let the set of colours be [D], let Hd and Gd be the edges in H and G of colour d. Let e1,... ,eD be the standard basis of ZD. Let Φ, Σ, A be as above. Deﬁne G∗ ∈ (ND)Φr by G∗ψ = ed for all ψ with Im(ψ) ∈ Gd and G∗ψ = 0 otherwise. Deﬁne γ ∈ (ND)Ar by γθ = ed for all θ ∈ Ar with Im(ψ) ∈ Hd and γθ = 0 otherwise. Then an H-decomposition of G that respects colours is equivalent to a γ(Φ)-decomposition of G∗.
- iii. Now suppose that G is q-partite, say with parts V1,... ,Vq. The previous examples will not be useful for ﬁnding an H-decomposition of G, as our main theorem requires (Φ,G) to be extendable, but if we allow Φ to disrespect the partition then we cannot extend all partial embeddings within G. Instead, we deﬁne ΦB for B ⊆ [q] to consist of all partite ψ ∈ Inj(B,V (G)), i.e. ψ(i) ∈ Vi for all i ∈ B. We let Σ = {id} be trivial, A = {A} with A = Σ≤, i.e. all AB = {idB}. Deﬁning G∗ and γ as in the ﬁrst example, we again see that an H-decomposition of G is equivalent to a γ(Φ)-decomposition of G∗.
- iv. Next we consider the H-decomposition problem for G when we are given bipartitions (X,Y ) of V (G) and (A,B) of V (H) = [q], and we only allow copies of H in which A maps into X and B into Y (recall that the problems of resolvable designs and large sets of designs are equivalent to such bipartite decomposition problems). We let ΦF for F ⊆ [q] consist of all ψ ∈ Inj(F,V (G)) such that ψ(F ∩ A) ⊆ X and ψ(F ∩ B) ⊆ Y . As usual, we let G∗ = {ψ ∈ Φr : Im(ψ) ∈ G}. We let Σ be the group of all σ ∈ Sq such that σ(A) = A and σ(B) = B. Then Φ is Σ-adapted.

As usual, we let A = {A′} with A′ = Σ≤ and γ ∈ {0,1}A′

r with each γθ = 1Im(θ)∈H. Then an H-decomposition of G is equivalent to a γ(Φ)-decomposition of G∗.

- v. In the above examples we were decomposing hypergraphs (sets of sets) and treating the labellings (sets of functions) as a convenient device, but many applications explicitly require labellings. An example that may have some topological motivation is that of decomposing the set of top-dimensional cells of an oriented simplicial complex. The standard deﬁnition of orientations ﬁts very well with our framework: for r-graphs H and G, an orientation is deﬁned by a bijective labelling of each edge by [r], where two labellings are considered equivalent if


they diﬀer by an even permutation in Sr. Then we wish to decompose G by copies of H, where we only allow copies φ(H) such that for each edge e of H composing the labelling of e with φ gives a labelling of φ(e) equivalent to that in G. To realise this problem in our framework (consider for simplicity the nonpartite setting where Φ is the complete [q]-complex on V (G) and Σ = Sq), for each B ∈ Q = [q]r we let πB ∈ Bij([r],B) be order preserving and let G∗B consist of all ψ ∈ ΦB such that ψ′ = ψ ◦ πB with Im(ψ′) ∈ G is correctly oriented. Similarly, we let A = {A} with A = Σ≤ and γ ∈ {0,1}Ar where for θ ∈ AB we let γθ be 1 if θ′ = θ ◦ πB with Im(θ′) ∈ H is correctly oriented, otherwise γθ = 0. Then an oriented H-decomposition of G is equivalent to a γ(Φ)-decomposition of G∗.

## 2.5 Atoms and types

In this subsection we introduce some structures and terminology for working with vector-valued decompositions, and make some preliminary observations regarding the decomposition lattice γ(Φ) . We also deﬁne the regularity property referred to above. Throughout we let Σ ≤ Sq be a permutation group, Φ be a Σ-adapted [q]-complex, A be a Σ≤-family and γ ∈ ΓAr.

- Deﬁnition 2.22. (atoms) For any φ ∈ A(Φ) and O ∈ Φr/Σ such that γ(φ)O = 0 we call γ(φ)O a γ-atom at O. We write γ[O] for the set of γ-atoms at O. We say γ is elementary if all γ-atoms are

linearly independent. We deﬁne a partial order ≤γ on ΓΦr where H ≤γ G iﬀ G−H can be expressed as the sum of a multiset of γ-atoms.

Note that if J ∈ γ(Φ) then each JO can be expressed as a Z-linear combination of γ-atoms at O. Furthermore, if γ is elementary then this expression is unique, so if J is the sum of a multiset Z of γ-atoms then a γ(Φ)-decomposition of J may be thought of as a partition of Z, where each part is the set of γ-atoms contained in some molecule γ(φ). This is a combinatorially natural condition, as it avoids arithmetic issues that arise e.g. for decompositions of integers (the Frobenius coin problem). In our main theorem we will assume that γ is elementary, but the proof also uses other vector systems derived from γ that are not necessarily elementary.

The following deﬁnition and accompanying lemma give various equivalent ways to represent atoms. The notation γ(φ) matches the notation for molecules in Deﬁnition 2.21 when φ ∈ A(Φ).

- Deﬁnition 2.23. For ψ ∈ ΦB and θ ∈ AB we deﬁne γ[ψ]θ ∈ ΓψΣ by γ[ψ]θψσ = γθσ. For φ ∈ A(Φ)≤ = Φ we deﬁne γ(φ) ∈ ΓΦr by γ(φ)φθ = γθ whenever θ ∈ Ar with Im(θ) ⊆ Dom(φ).


- Lemma 2.24. Suppose φ ∈ A(Φ) and ψ ∈ A(Φ)≤B = ΦB.


- i. If ψ = φθ with θ ∈ Ar then γ(φ)ψΣ = γ[ψ]θ. Furthermore, if θ ∈ AB and σ ∈ ΣB then γ[ψ]θ = γ[ψσ]θσ.
- ii. If ψ ⊆ φ then γ(φ)ψΣ = γ[ψ]idB = γ(ψ).


Proof. For (i), by Deﬁnitions 2.21 and 2.23, for any σ ∈ ΣB we have γ(φ)ψσ = γ(φ)φθσ = γθσ = γ[ψ]θψσ, i.e. γ(φ)ψΣ = γ[ψ]θ. Furthermore, if θ ∈ AB, σ ∈ ΣBB′, σ′ ∈ ΣB′ then γ[ψ]θψσσ′ = γθσσ′ = γ[ψσ]θσψσσ′. For (ii), we have ψ = φ idB, so γ(φ)ψΣ = γ[ψ]idB by (i). Also, for any σ ∈ ΣB we have γ(ψ)ψσ = γσ = γ[ψ]idψσB, so γ[ψ]idB = γ(ψ).

The following deﬁnition will be used for the extendability assumption on (Φ,γ[G]) in our main theorem, which gives a lower bound on extensions such that all atoms belong to G.

- Deﬁnition 2.25. For G ∈ ΓΦr we let γ[G] = (γ[G]A : A ∈ A) where each γ[G]A is the set of ψ ∈ A(Φ)≤r = Φr such that γ(ψ) ≤γ G.

When using the notation γ[ψ]θ for an atom, there may be several choices of θ that give rise to the same atom; this deﬁnes an equivalence relation that we will call a type. To illustrate the following deﬁnition, we recall example i (nonpartite H-decomposition) from subsection 2.4. In this case, there are two types for each r-set B of labels: for any θ ∈ AB, if Im(θ) ∈ H then γθ is the all-1 vector (we think of this type as an edge), whereas Im(θ) ∈/ H then γθ is the all-0 vector (the zero type, which we think of as a ‘non-edge’).

- Deﬁnition 2.26. (types) For θ ∈ AB with B ∈ Q we deﬁne γθ ∈ ΓΣB by γσθ = γθσ.


A type t = [θ] in γ is an equivalence class of the relation ∼ on any AB with B ∈ Q where θ ∼ θ′

iﬀ γθ = γθ′. We write TB for the set of types in AB. For θ ∈ t ∈ TB and ψ ∈ ΦB we write γt = γθ and γ[ψ]t = γ[ψ]θ. If γt = 0 call t a zero type and write t = 0. If φ ∈ A(Φ) with γ(φ)ψΣ = γ[ψ]t we write tφ(ψ) = t.

The next lemma shows that γ[ψ]t is well-deﬁned.

- Deﬁnition 2.27. For B ∈ C ∈ PrΣ and J ∈ ΓΦC we deﬁne fB(J) ∈ (ΓΣB)ΦB by (fB(J)ψ)σ = Jψσ.


- Lemma 2.28. If J = γ[ψ]t for some ψ ∈ ΦB, t ∈ TB then fB(J)ψ = γt.


Proof. For any σ ∈ ΣB and θ ∈ t we have (fB(J)ψ)σ = Jψσ = γ[ψ]θψσ = γθσ = γσθ = γσt .

We also see from Lemma 2.28 that γ is elementary iﬀ for any B ∈ Q the set of nonzero γt with t ∈ TB is linearly independent. Next we introduce certain group actions that will be important in section 5; the following lemma records their eﬀect on types.

- Deﬁnition 2.29. For any set X we deﬁne a right ΣBB action on XΣB by (vτ)σ = vτσ whenever v ∈ XΣB, τ ∈ ΣBB, σ ∈ ΣB.


Note that Deﬁnition 2.29 is indeed a right action, as for τ1,τ2 ∈ ΣBB we have ((vτ1)τ2)σ = (vτ1)τ2σ = vτ1τ2σ = (v(τ1τ2))σ. For future reference we also note the linearity (v + v′)τ = vτ + v′τ; indeed, for σ ∈ ΣB we have ((v + v′)τ)σ = (v + v′)τσ = vτσ + vτσ′ = (vτ)σ + (v′τ)σ.

- Lemma 2.30. If θ ∈ AB and τ ∈ ΣBB then γθτ = γθτ.


Proof. For any σ ∈ ΣB we have (γθτ)σ = γτσθ = γθτσ = γσθτ.

The next deﬁnition and accompanying lemma restate and provide notation for the earlier observation that any vector in the decomposition lattice can be expressed as a Z-linear combination of atoms (we omit the trivial proof).

- Deﬁnition 2.31. Let L−γ (Φ) be the set of J ∈ ΓΦr such that JO ∈ γ[O] for all O ∈ Φr/Σ.


- Lemma 2.32. γ(Φ) ⊆ L−γ (Φ). Next we deﬁne two notions of symmetry, one for vectors and the other for subsets.


- Deﬁnition 2.33. We call v ∈ (ΓΣB)ΦB symmetric if vψτ = vψτ whenever ψ ∈ ΦB, τ ∈ ΣBB. We call H ⊆ ΓΣB symmetric if gτ ∈ H whenever g ∈ H, τ ∈ ΣBB.


Note that

GB := {γt : t ∈ TB} and γB := GB ≤ ΓΣB

are symmetric by Lemma 2.30. Now we use types to give an alternative description of the lattice from Deﬁnition 2.31.

- Lemma 2.34. Let B ∈ C ∈ PrΣ and J ∈ ΓΦC ∩ L−γ (Φ). Then fB(J) ∈ (γB)ΦB is symmetric.


Proof. By linearity, we can assume J is a γ-atom, say J = γ[ψ]θ with ψ ∈ ΦB, θ ∈ AB. For any τ ∈ ΣBB we have J = γ[ψτ]θτ by Lemma 2.24.i and fB(J)ψτ = γθτ = γθτ = fB(J)ψτ by Lemmas

- 2.28, 2.30 and 2.28 again.


For future reference (in section 4) we also note the following lemma which will allow us to split any linear dependence of γ-atoms into constant sized pieces. If γ is elementary then ZB(γ) = {0} so there is nothing to prove; in this case we let C0 = 1. We call C0 the lattice constant.

- Lemma 2.35. There is C0 = C0(γ) such that for any n ∈ ZB(γ) := {n ∈ ZAr : θ nθγθ = 0}, there are ni ∈ ZB(γ) for i ∈ [t] for some t ≤ C0|n| with each |ni| ≤ C0 and n = i∈[t] ni.


Proof. Let X be an integral basis for ZB(γ). Let Z be the matrix with columns X. We will ﬁnd an integral solution v of n = Zv and then for each X ∈ X take |vX| of the ni equal to ±X (with the sign of vX). The following explicit construction implies the required bound for |v| in terms of |n|. We can put Z in ‘diagonal form’ via elementary row and column operations: there are unimodular (integral and having integral inverses) matrices P and Q such that D = PZQ has Dij = 0 ⇔ i = j. To solve n = Zv we need to solve Pn = DQ−1v. Let R be the set of nonzero rows of D and let (Pn)R and DR denote the corresponding restrictions of Pn and D. Then DR−1(Pn)R is integral (as n ∈  X ) so v = QDR−1(Pn)R is an integral solution of n = Zv.

Next we introduce some notation for the coeﬃcients that arise from decomposing a vector into atoms.

- Deﬁnition 2.36. (atom decomposition)

Suppose γ is elementary and J ∈ L−γ (Φ). For ψ ∈ ΦB with |B| = r we deﬁne integers Jψt for all nonzero t ∈ TB by JψΣ = 0 =t∈T

B

Jψt γ[ψ]t. Any choice of orbit representatives ψO ∈ ΦBO for each orbit O ∈ Φr/Σ deﬁnes an atom decomposition J = O∈Φ

r/Σ 0 =t∈TBO JψtOγ[ψO]t.

We need one ﬁnal deﬁnition before stating our main theorem in the next section; note that the coeﬃcients Gtψ are as in the previous deﬁnition.

- Deﬁnition 2.37. (regularity) Suppose γ ∈ (ZD)Ar and G ∈ (ZD)Φr. Let A(Φ,G) = {φ ∈ A(Φ) : γ(φ) ≤γ G}.


We say G is (γ,c,ω)-regular (in Φ) if there is y ∈ [ωnr−q,ω−1nr−q]A(Φ,G) such that for all B ∈ [q]r, ψ ∈ ΦB, 0 = t ∈ TB we have

∂tyψ :=

yφ = (1 ± c)Gtψ.

φ:tφ(ψ)=t

Note that if G and y are as in the previous deﬁnition and ψ ∈ O ∈ Φr/Σ then (∂γy)O =

yφγ(φ)O =

yφγ[ψ]t =

(1 ± c)Gtψγ[ψ]t = (1 ± c)GO.

0 =t∈TB φ:tφ(ψ)=t

0 =t∈TB

φ

We note for future reference that this implies an upper bound on the use (see Deﬁnition 3.13 below) of any orbit O ∈ Φr/Σ, namely U(G)O < 2|A|ω−1 (if c < 1/2). Also, summing over O we obtain ∂γy = (1 ± c)G, i.e. φ yφγ(φ)ψ,d = (1 ± c)Gψ,d for all ψ ∈ Φr, d ∈ [D].

# 3 Main theorem

Now we can state our main theorem. We will give the proof in this section, assuming Lemmas 3.27 and 3.18, which will be proved in sections 4 and 6. The parts of the proof given in this section are those that are somewhat similar to the proof in [15], so we will be quite concise in places where they are similar, and give more details at points of signiﬁcant diﬀerence. To apply Theorem 3.1 we also need a concrete description of the decomposition lattice γ(Φ) ; this will be given in section 5.

Theorem 3.1. For any q ≥ r and D there are ω0 and n0 such that the following holds for n > n0,

- h = 250q3, δ = 2−103q5, n−δ < ω < ω0 and c ≤ ωh20. Let A be a Σ≤-family with Σ ≤ Sq. Suppose γ ∈ (ZD)Ar is elementary. Let Φ be a Σ-adapted [q]-complex on [n]. Let G ∈ γ(Φ) be (γ,c,ω)-regular in Φ such that (Φ,γ[G]A) is (ω,h)-extendable for each A ∈ A. Then G has a γ(Φ)-decomposition.


Throughout this section we let Σ, A, γ, Φ and G be as in the statement of Theorem 3.1. We note that the assumption that γ is elementary bounds |A| as a function of q and D, say |A| < (Dq)qq. For convenient reference, we list here several parameters used throughout the paper.

Q = qr , z = h = 250q3, δ = 2−103q5, n−δ < ω < ω0(q,D), ωq := ω(9q)q+5,

p is a prime with 28q < p < 29q, a ∈ N with pa−2 < n ≤ pa−1, γ = np−a, ρ = ωz−Q|A|−1(q)−r Qγq−r, where (q)r = q!/(q − r)!, c = ωh20, c1 = (2Qc)1/2Q, ci+1 = ω−h3ci for i ∈ [4].

- 3.1 Probabilistic methods We brieﬂy recall two concentration inequalities (see [15, Lemmas 2.4 and 2.11]).


- Deﬁnition 3.2. Suppose Y is a random variable and F = (F0,... ,Fn) is a ﬁltration. We say that Y is (C,µ)-dominated (wrt F) if we can write Y = ni=1 Yi, where Yi is Fi-measurable, |Yi| ≤ C and E[|Yi| | Fi−1] < µi for i ∈ [n], where ni=1 µi < µ.

Lemma 3.3. If Y is (C,µ)-dominated then P(|Y | > (1 + c)µ) < 2e−µc2/2(1+2c)C.

- Deﬁnition 3.4. Let a = (a1,... ,an) and a′ = (a′1,... ,a′n), where ai ∈ N and a′i ∈ [ai] for i ∈ [n], and Π(a,a′) be the set of π = (π1,... ,πn) where πi : [a′i] → [ai] is injective. Suppose f : Π(a,a′) → R and b = (b1,... ,bn) with bi ≥ 0 for i ∈ [n]. We say that f is b-Lipschitz if for any i ∈ [n] and π,π′ ∈ Π(a,a′) such that πj = πj′ for j = i and πi = τ ◦ πi′ for some transposition τ ∈ Sai we have |f(s) − f(s′)| ≤ bi. We also say that f is B-varying where B = ni=1 a′ib2i .


- Lemma 3.5. Suppose f : Π(a,a′) → R is B-varying and X = f(π), where π = (πi) ∈ Π(a,a′) is


random with {πi : i ∈ [n]} independent and πi uniform whenever a′i > 1. Then P(|X − EX| > t) ≤ 2e−t2/2B.

The following lemma will be used to pass from fractional matchings to almost perfect matchings. The statement and proof are similar7 to those given by Kahn [14], so we omit the details. Call a hypergraph H a k≤-graph if all edges have size at most k.

![image 10](<2018-keevash-existence-designs_images/imageFile10.png>)

7 The constraint set P acts on the edges of H in [14], whereas here it is more convenient to use vertices. It is assumed to be of constant size in [14], which allows for a simple second moment argument, but we need to allow P to grow polynomially in α−1, which can be achieved by proving exponential tails on the failure probabilities (which follows

- Lemma 3.6. Suppose H is a k≤-graph and w is a fractional matching in H with {x,y}⊆e∈H we < α < α0(k) suﬃciently small for all {x,y} ⊆ V (H). Let P ⊆ RV(H) with |P| < α−k and maxv pv < (log α)−2 v pv for all p ∈ P. Then there is a matching M of H such that


pv = (1 ± α1/2k)

e∈H

v∈ M

pv for all p ∈ P.

we

v∈e

We will apply Lemma 3.6 to a hypergraph whose vertices can be identiﬁed with γ-atoms, we have α = O(n−1), and elements of P indicate atoms that ‘use’ a given ordered (r −1)-tuple from [n]; the conclusion will be that there is a matching with ‘bounded leave’ (see Deﬁnition 3.13 and Lemma

- 3.15 below).


## 3.2 Template

Recalling the proof strategy discussed in the introduction, we start by describing the template. This will be determined by some M∗ ⊆ A(Φ) such that G∗ := φ∈M∗ φ(Q) ⊆ Φ◦r, i.e. G∗ is an r-graph (with no multiple edges) contained in Φ◦r and {φ(Q) : φ ∈ M∗} is a Kqr-decomposition of G∗. Thus for each e ∈ Φ◦r there is at most one orbit O ∈ Φr/Σ with Im(O) = e and O ⊆ φΣ for some φ ∈ M∗, and given such O with representative ψO ∈ ΦB the use of O by φ has a unique type tφ(ψO) = t ∈ TB (which may be the zero type).

As in [15], we ﬁx M ∈ Fpq×r as a q × r matrix over Fp that is generic, in that every square submatrix of M is nonsingular.

As G is (γ,c,ω)-regular, there is y ∈ [ωnr−q,ω−1nr−q]A(Φ,G) with ∂tyψ = (1 ± c)Gtψ for all

- B ∈ [q]r, ψ ∈ ΦB, 0 = t ∈ TB. We activate each φ ∈ A(Φ) independently with probability yφωnq−r. Let f = (fj : j ∈ [z]), with z = h = 250q3, where we choose independent uniformly random


injections fj : [n] → Fpa. Given f, for each e ∈ Φ◦r we let Te = {j ∈ [z] : dim(fj(e)) = r}.

We abort if any |Te| ≤ z − 2r, which occurs with probability O(n−r). We assume without further comment that the template does not abort.

We choose Te ∈ [z] for all e ∈ Φ◦r independently and uniformly at random. We say φ ∈ A(Φ) is compatible with j if Te = j ∈ Te for all e ∈ φ(Q) and for some y ∈ Frpa we have fj(φ(i)) = (My)i for all i ∈ [q].

Let π = (πe : e ∈ Φ◦r) where we choose independent uniformly random injections πe : e → [q]. We say φ ∈ Φ is compatible with π if πeφ(i) = i whenever φ(i) ∈ e ∈ φ(Q) (for brevity we write this as πeφ = id).

We choose independent uniformly random Aφ ∈ A for each injection φ : [q] → [n].

- Deﬁnition 3.7. Let Mj∗ be the set of all activated φ ∈ Aφ(Φ) compatible with j and π such that γ(φ) ≤γ G. The template is M∗ = ∪j∈[z]Mj∗.


The underlying r-graph of the template is G∗ = ∪j∈[z]G∗j, where each G∗j = ∪φ∈M∗

φ(Q).

j

![image 11](<2018-keevash-existence-designs_images/imageFile11.png>)

from the same proof by applying standard concentration inequalities). Also, the error term in the conclusion is not explicitly given in [14], whereas we state a polynomial dependence on α (the proof gives α1/2k), which is needed if one desires counting versions of our results, as in [16]. A ﬁnal comment is that it is not essential to consider edge weights,

- as we anyway reduce to the case that all we are equal, but it is convenient to leave the weights in the statement, and this also facilitates comparison with the statement in [14].


Note that G∗ is the edge-disjoint union of the G∗j, and each {φ(Q) : φ ∈ Mj∗} is a Kqrdecomposition of G∗j (see [15, Lemma 3.3]).

We introduce the following further notation that will be used in the analysis of the template.

- Deﬁnition 3.8. For e ∈ G∗ let φe ∈ M∗ be such that e ∈ φe(Q). We write M∗(e) = φe(Q).


For J ⊆ G∗ let M∗(J) = e∈J M∗(e) ∈ NG∗. For e ∈ G∗ we write γ(e) = γ(φe)Oe where Oe = πe−1Σ. We call γ(e) an M∗-atom.

Note that γ(e) may be zero in Deﬁnition 3.8. If γ(e) = 0 then γ(e) is also a γ-atom. Furthermore, for any γ-atom γ(ψ) ≤γ ∂γM∗ we have γ(ψ) = γ(e) where Im(ψ) = e.

If 0 ≤γ J ≤γ ∂γM∗ with J = Z for some set Z of γ-atoms we write J◦ = {e ∈ G∗ : γ(e) ∈ Z}. For example, G∗ = (∂γM∗)◦.

## 3.3 Extensions

Next we give estimates on the probability that certain γ-atoms appear in the template and deduce that the template is whp extendable. Our estimates are conditional on the following local events (deﬁned similarly to [15]).

- Deﬁnition 3.9. (local events) Suppose e ∈ Φ◦r. We reveal Te = j and fj |e= α. If dim(α) < r then Ee is the event that Te = j and fj |e= α, which witnesses e ∈/ G∗.


Now suppose dim(α) = r, reveal πe, and let y ∈ Frpa with fj(x) = (My)i for all x ∈ e, πe(x) = i. We reveal fj−1((My)i) for all i ∈ [q] \ πe(e), and let φ : [q] → [n] be such that fjφ = My, and reveal Aφ. If we do not have γ(φ) ≤γ G with φ ∈ Aφ(Φ) then Ee is the event that Te = j and fjφ = My, which witnesses e ∈/ G∗.

Finally, if γ(φ) ≤γ G we reveal whether φ is activated, and reveal (Te′,πe′) for all e′ ∈ φ(Q)\{e}. Then Ee is deﬁned by all the above information, which determines whether e ∈ G∗: given Te = j, fjφ = My, φ ∈ Aφ(Φ), γ(φ) ≤γ G we have e ∈ G∗ iﬀ φ is activated and Te′ = j and πe′φ = id for all e′ ∈ φ(Q).

We say that a vertex x is touched by Ee if fj(x) is revealed by Ee. We say that an edge e′ is touched by Ee if Te′ is revealed by Ee.

The following lemma is analogous to [15, Lemma 3.6]. Let ρ := ωz−Q|A|−1(q)−r Qγq−r.

- Lemma 3.10. Let S ⊆ Φ◦r with |S| < h = z and E = ∩f∈SEf. Let ψ ∈ ΦB and t ∈ TB with t = 0 and γ[ψ]t ≤γ G (i.e. Gtψ > 0). Suppose e := Im(ψ) is not touched by E and j ∈ [z] \ {Tf : f ∈ S}. Then P(γ[ψ]t ≤γ ∂γMj∗ | E) = (1 ± 1.1c)ρGtψ.


Proof. We ﬁx any φ ∈ A(Φ) with γ(φ) ≤γ G and tφ(ψ) = t, and estimate the probability that φ ∈ Mj∗. We have P(Aφ = A) = |A|−1. We activate φ with probability yφωnq−r. We can assume every e′ ∈ φ(Q) is not touched by E, as this excludes O(nq−r−1) choices. Then all Te′ = j with probability z−Q. With probability (q)−r Q all πe′φ = id. We condition on fj |e such that dim(fj(e)) = r; this occurs with probability 1−O(n−1). There is a unique y ∈ Frpa such that (My)i = fj(x) for all x ∈ e,

- i = πe(x). With probability (1 + O(n−1))(p−a)q−r we have fj(φ(i)) = (My)i for all i ∈ [q] \ πe(e). Therefore P(φ ∈ Mj∗ | E) = (1 + O(n−1))|A|−1yφωnq−rz−Q(q)−r Q(p−a)q−r. The lemma follows by summing over φ, using ∂tyψ = (1 ± c)Gtψ.


Remark 3.11. The same proof shows

- i. P(γ[ψ]t ≤γ ∂γMj∗ | E ∩ {Te = j}) = (1 ± 1.1c)zρGtψ for any j ∈ [z] \ {Tf : f ∈ S},
- ii. P({γ[ψ]t ≤γ ∂γMj∗} ∩ {πe = π} ∩ {Aφe = A} | E) > ω2ρGtψ, for any A ∈ A and injection π : e → [q] such that ψ′ = π−1 ∈ A(Φ)≤ satisﬁes γ[ψ]t = γ(ψ′).


Note that (ii) is weaker than the corresponding bound in [15] as we cannot permute φ (this may change γ(φ)). Instead, we use extendability to see that there are at least ωnq−r choices of φ with γ(φ) ≤γ G containing ψ′, and each has yφ > ωnr−q.

The following lemma is analogous to [15, Lemma 3.8].

- Lemma 3.12. Suppose E = (φ,F,H) is a Φ-extension with |H| ≤ h/3. Let A ∈ A and H′ ⊆ Hr \ H[F]. Then whp XE,H′(Φ,γ[∂γM∗]A) > ωnvE(zρ/2)|H′|.


Proof. As (Φ,γ[G]A) is (ω,h)-extendable, there are at least ωnvE choices of φ+ ∈ XE,H′(Φ,γ[G]A), i.e. φ+ ∈ XE(Φ) with φ+ψ′ ∈ γ[G]AB for all ψ′ ∈ HB′ . We ﬁx any such φ+ and estimate P(φ+ ∈ XE,H′(Φ,γ[∂γM∗]A)) by repeated application of Lemma 3.10. For any ψ = φ+ψ′ with ψ′ ∈ HB′ , we condition on the intersection E of all previously considered local events, and estimate pjψ = P(γ[ψ]t ≤γ ∂γMj∗ | E), where t ∈ TB contains idB ∈ A and we can assume Im(ψ) is not touched by E. If t = 0 then pjψ = 1; otherwise, there are at least 2z/3 choices of j ∈ [z] not used by any previous edge such that Lemma 3.10 applies to give pjψ = (1 ± 1.1c)ρGtψ. Multiplying all conditional probabilities and summing over φ+ gives EXE,H′(Φ,γ[∂γM∗]A) > ωnvE(0.6zρ)|H′|. The proof of concentration is similar to that in [15, Lemma 3.8], noting that the eﬀect of changing any Aφ has a similar eﬀect to that of changing whether φ is activated.

## 3.4 Approximate decomposition

Similarly to [15, section 4] we will now complete the template to an approximate decomposition, namely M′ ⊆ A(Φ) such that ∂γM′ is almost equal to G, except that some (suitably bounded) set of M∗-atoms are each covered one time too many. First we introduce some notation and terminology that will be used throughout the rest of the paper.

- Deﬁnition 3.13. For J ∈ (ZD)Φr and ψ ∈ Φr, we deﬁne the use U(J)ψ of ψ by J as the minimum

possible value of w∈W |xw| where W is the set of γ-atoms at O = ψΣ and x ∈ ZW with JO =

xww. If there is no such x then U(J)ψ is undeﬁned. For ψ′ ∈ Φ we let U(J)ψ′ = {U(J)ψ : ψ′ ⊆ ψ ∈ Φr}. We note that use is a property of orbits, so U(J)ψΣ = U(J)ψ is well-deﬁned. We say J is θ-bounded if U(J)ψ < θ|V (Φ)| whenever ψ ∈ Φr−1.

Note that as γ is elementary the use of ‘minimum’ in Deﬁnition 3.13 is redundant, as JO has a unique atom decomposition; however, we will also need this deﬁnition for other γ that are not necessarily elementary. We will also sometimes use the following deﬁnition that ignores the edge labellings and atom structure (so is analogous to that used in [15]).

- Deﬁnition 3.14. Suppose J ∈ (ZD)Φ◦r. We let U(J)e = d∈[D] |(Je)d| for e ∈ Φ◦r and U(J)f = {U(J)e : f ⊆ e ∈ Φ◦r} for f ∈ Φ◦. We say J is θ-bounded if U(J)f < θ|V (Φ)| for all f ∈ Φ◦r−1.


Now we ﬁnd a γ(Φ)-decomposition of almost all of G − ∂γM∗, such that the leave is bounded in the sense of Deﬁnition 3.13. The following lemma is analogous to [15, Lemma 4.1].

- Lemma 3.15. There is Mn ⊆ A(Φ) with c1-bounded leave L := G − ∂γM∗ − ∂γMn ≥γ 0.


Proof. We deﬁne Φ′ ⊆ A(Φ) randomly as follows. Consider any φ ∈ A(Φ) such that γ(φ) ≤γ G and reveal the local events Ee for each e ∈ Q′ := φ(Q). If φ is not activated or Te = Te′ for any e = e′ in Q′ then we do not include φ in Φ′. For each e ∈ Q′ we ﬁx ψe with image e such that γ(ψe) ≤γ γ(φ), and let te = tφ(ψe), so γ(ψe) = γ[ψe]te. For v ∈ {0,1}Q′ let Evφ be the event that all ve = 1γ(ψe)≤γ∂γM∗. If φ is activated, all Te for e ∈ Q′ are distinct and Evφ holds then we include φ in Φ′ independently with probability pvφ = e∈Q′(1 − veqe), where qe = 1/Gtψe

if te = 0 or qe = zρ if te = 0.

e

Now we ﬁx any ψ and t = 0 with Gtψ > 0 and estimate the number X of φ ∈ Φ′ with tφ(ψ) = t. We consider any activated φ with tφ(ψ) = t, let e′ = Im(ψ), Q′ = φ(Q) and condition on the local event Ee′ and any event C = ∩e∈Q′{Te = je} such that all je are distinct (the latter occurs with probability (z)Qz−Q).

For any v ∈ {0,1}Q′ with ve′ = (∂γM∗)tψ, by repeated application of Remark 3.11.i we have P(Evφ | Ee′ ∩ C) = (1 ± Qc) e∈Q′\{e′} pvee, where if te = 0 we let p1e = 1 and p0e = 0, and otherwise p1e = zρGtψe

and p0e = 1 − zρGtψe

. Then p0e + p1e(1 − qe) = 1 − zρ, so as in the proof of [15, Lemma

e

e

- 4.1], P[φ ∈ Φ′ | Ee′ ∩ C] = (1 ± Qc)(1 − (∂γM∗)tψ/Gtψ)(1 − zρ)Q−1. We activate each φ with probability yφωnq−r, so as ∂tyψ = (1±c)Gtψ we deduce EX = (z)Qz−Q ·


(1 ± Qc)(1 − (∂γM∗)tψ/Gtψ)(1 − zρ)Q−1 · (1 ± c)ωnq−rGtψ = (1 ± 1.1Qc)d′nq−r(G − ∂γM∗)tψ, where

- d′ = (z)Qz−Qω(1 − zρ)Q−1. As in the proof of [15, Lemma 4.1], by Lemma 3.5 whp X = (1 ± 1.2Qc)d′nq−r(G − ∂γM∗)tψ.


Finally, we consider the following hypergraph H, where V (H) is the disjoint union of sets Vψt of size (G − ∂γM∗)tψ corresponding to the γ-atoms of G − ∂γM∗ counted with multiplicity. For each φ ∈ Φ′ we let Vφ be the set of all Vψt with γ[ψ]t ≤γ γ(φ), and include as an edge a uniformly random set eφ with one vertex in each V ∈ Vφ. Then whp every v ∈ V (H) has degree (1 ± 2Qc)d′nq−r. Also any {u,v} ⊆ V (H) is contained in O(nq−r−1) edges. Let P ⊆ RV(H) where for each ψ′ ∈ Φr−1 and we include pψ′ where pψ

′

′

v is 1 if v is in some Vψt with ψ′Σ ⊆ ψΣ, otherwise 0. Then v pψ

v counts the number of γ-atoms of G − ∂γM∗ on orbits containing ψ′Σ.

By Lemma 3.6, applied with uniform weights we = ((1 + 2Qc)d′nq−r)−1, there is a matching Mn

in H with v∈ Mn pv = (1 ± (1.1Qc)1/2Q) e∈H we v∈e pv = (1 ± (1.2Qc)1/2Q) v∈V (H) pv for all p ∈ P. We can also view Mn as a subset of A(Φ). Then L := G − ∂γM∗ − ∂γMn contains at most

(1.2Qc)1/2Q proportion of the γ-atoms of G − ∂γM∗ on orbits containing ψ′Σ, for any ψ′ ∈ Φr−1. Recalling that U(G)O < 2|A|ω−1 and |A| < Dq2q we see that L is c1-bounded.

To complete the approximate decomposition, we choose a partial γ(Φ)-decomposition that exactly

matches the leave on Φ◦r \G∗, but has some ‘spill’ S in G∗ that we will need to correct for later. The following lemma is analogous to [15, Lemma 4.2].

- Lemma 3.16. Suppose 0 ≤γ L ≤γ G − ∂γM∗ is c1-bounded. Then there is Mc ⊆ A(Φ) such that γ(φ) ≤γ L + ∂γM∗ for all φ ∈ Mc and ∂γMψc = Lψ for all ψ ∈ Φr with Im(ψ) ∈/ G∗, with spill S := G∗ ∩ φ∈Mc φ(Q), such that M∗(S) is a set and c2-bounded.


Proof. We order the γ-atoms of L as (γ(ψi) : i ∈ [nL]), where each ψi ∈ Ai(Φ)≤Bi = ΦBi. For each i we consider the Φ-extension Ei = (−→q ,Bi,ψi) and let H′ = −→q r \ {Bi}. We apply a random

(Φ,γ[∂γM∗]Ai), where we write Si = G∗ ∩ ∪i′<iφi′(Q) and choose φi uniformly at random such that M∗(φi(Q)) is a set disjoint from M∗(Si). For each i we add φi ∈ Ai(Φ) to Mc. The remainder of the proof is very similar to that of [15, Lemma 4.2]. We show that whp Mc has the stated properties. At any step i before M∗(S) fails to be c2-bounded at

greedy algorithm to select φi ∈ XEi,H′

i

(Φ,γ[∂γM∗]Ai) > ω(zρ/2)Qnq−r by Lemma L] P′(e ∈ M∗(φi(Q))) < 2(2q)2qω−1(zρ/2)−Qc1, so

most half of the choices of φi are forbidden, as XEi,H′

i

- 3.12. Then for all e ∈ G∗ we estimate re := i∈[n


by Lemma 3.3 whp M∗(S) is c2-bounded.

## 3.5 Proof modulo lemmas

In this subsection we give the proof of Theorem 3.1, assuming two lemmas that will be proved later. First we need to deﬁne use and boundedness for vectors indexed by A(Φ).

- Deﬁnition 3.17. For Ψ ∈ ZA(Φ) and ψ ∈ Φ the use of ψ by Ψ is U(Ψ)ψ = {|Ψφ| : ψΣ ⊆ φΣ}. We also write U(Ψ)ψΣ = U(Ψ)ψ. We say Ψ is θ-bounded if {U(Ψ)ψ : ψ′ ⊆ ψ ∈ Φr} < θ|V (Φ)| whenever ψ′ ∈ Φr−1.


The following is a bounded integral decomposition lemma, analogous to [15, Lemma 5.1], which will be proved in section 6. Recall ωq := ω(9q)q+5.

- Lemma 3.18. Let A be a Σ≤-family with Σ ≤ Sq and |A| ≤ K and suppose γ ∈ (ZD)Ar. Let Φ be an (ω,h)-extendable Σ-adapted [q]-complex on [n], where n−h−3q < ω < ω0(q,D,K) and n > n0(q,D,K). Suppose J ∈ γ(Φ) is θ-bounded, with n−(5hq)−r < θ < 1. Then there is some ωq−2hθbounded Ψ ∈ ZA(Φ) with ∂γΨ = J.

The following lemma takes as input a bounded integral decomposition as produced by Lemma 3.18 and produces a signed decomposition analogous to that in [15, Lemma 8.1]. In the next subsection we will reduce Lemma 3.19 to Lemma 3.27, which will be proved in section 4. Let c′2 = ω−h2c2.

- Lemma 3.19. Suppose Ψ ∈ ZA(Φ) is c′2-bounded with 0 ≤γ ∂γΨ ≤γ ∂γM∗. Let S = (∂γΨ)◦ and suppose M∗(S) is a set. Then there is Mo ⊆ M∗ and Mi ⊆ A(Φ) such that ∂γMo = ∂γMi + ∂γΨ.


The proof of Theorem 3.1 is now quite short given these lemmas.

Proof of Theorem 3.1. Fix a template M∗ as in Deﬁnition 3.7 that satisﬁes all of the whp statements in the paper. Let Mn be obtained from Lemma 3.15 and Mc and S from Lemma 3.16. Let J = ∂γ(M∗ + Mn + Mc) − G and note that J ∈ γ(Φ) , 0 ≤γ J ≤γ ∂γM∗ and J◦ = S. Then J is c2-bounded, so by Lemma 3.18 there is some c′2-bounded Ψ ∈ ZA(Φ) with ∂γΨ = J. Then we can apply Lemma 3.19 to obtain Mo ⊆ M∗ and Mi ⊆ A(Φ) such that ∂γMo = ∂γMi + J. Now M = Mn ∪ Mc ∪ (M∗ \ Mo) ∪ Mi is a γ(Φ)-decomposition of G.

## 3.6 Absorption In this subsection, we establish the algebraic absorbing properties of the template, and so reduce

- Lemma 3.19 to Lemma 3.27. Following [15, section 6], with appropriate modiﬁcations for the more general setting here, we will deﬁne absorbers, cascades and cascading cliques, then estimate the number of cascades for any cascading cliques. We will always be concerned with absorbing maps that are compatible with the template (possibly with one ‘bad edge’), as in the following deﬁnition.


- Deﬁnition 3.20. Let φ ∈ A(Φ) for some A ∈ A. We say that φ is M∗-compatible if φ is π-compatible and φe ∈ A(Φ) for all e ∈ φ(Q) ∩ G∗. Also, for e′ ∈ φ(Q) and Q∗ = φ(Q) ∩ G∗ \ {e′}, we say that φ is M∗-compatible bar e′ if πeφ = id and φe ∈ A(Φ) for all e ∈ Q∗.


Note that if φ is M∗-compatible and φ(Q) ⊆ G∗ then γ(e) = γ(ψ) whenever e = Im(ψ) ∈ G∗ with ψ ⊆ φ. To deﬁne absorbers we require some notation: let Ker := {a ∈ Fqp : aM = 0} and

vaw = MM[−r]1(e[r] + a)w, v′wa = w + Maw for a ∈ Kerr and w ∈ Fqpa.

- Deﬁnition 3.21. (absorbers) Let φ ∈ A(Φ) be M∗-compatible with φ(Q) ⊆ G∗j and dim(w) = q, where w := fjφ ∈ Fqpa. Suppose φw : [q] × Ker → [n] such that


- i. fjφw((i,a)) = wi + a · w for each i ∈ [q], a ∈ Ker,
- ii. if φ′ ∈ [q](Ker) with fjφwφ′ = vaw for some a ∈ Kerr then Aφwφ′ = A and φwφ′ ∈ Mj∗. We say that φ is absorbable and call φw the absorber for φ. We also refer to the subgraph8


Θφ(Q) = Θw = φw(Kqr(Ker)) of G∗ as the absorber for φ(Q).

We denote the edges of Θw by ewa where fj(ewa ) = (eI +a)w for some a ∈ KerI, I ∈ Q. As in [15, Lemma 6.3], each edge has full dimension under the relevant embedding: we have dim(fj(ewa )) = r. As in [15], we also view [q](Ker) as a subset of Fpq×q, and then we can write Deﬁnition 3.21.i as fjφwφ′ = w + φ′w. We deﬁne

φa := MM[−r]1(e[r] + a) − I, and φ′a = Ma, so that fjφwφa = w + φaw = vaw and fjφwφ′a = w + φ′aw = v′wa . We write Ψ(φw) = {φwφa : a ∈ Kerr} and Ψ′(φw) = {φwφ′a : a ∈ Kerr},

noting that Ψ(φw) ⊆ Mj∗ and φ ∈ Ψ′(φw). By [15, Lemma 6.4], Ψ(φw) and Ψ′(φw) both give Kqr-decompositions of Θφ(Q). Furthermore, ∂γΨ(φw) = ∂γΨ′(φw) ≤γ ∂γM∗.

Next we recall [15, Lemma 6.5].

- Lemma 3.22. There are Kqr-decompositions Υ and Υ′ of Ω = Kqr(p) such that


- i. |V (f) ∩ V (f′)| ≤ r for all f ∈ Υ and f′ ∈ Υ′,
- ii. if f ∈ Υ and {f′,f′′} ⊆ Υ′ with |V (f) ∩ V (f′)| = |V (f) ∩ V (f′′)| = r then (V (f′) \ V (f)) ∩ (V (f′′) \ V (f)) = ∅.


We identify Υ and Υ′ with subsets of [q](p), i.e. the set of partite maps from [q] to [q] × [p]. We identify [q] with {(i,1) : i ∈ [q]} ⊆ V (Ω) and with the corresponding map id[q]; by relabelling we can assume [q] ∈ Υ. For U′ ⊆ U ⊆ [n] we say that U is j-generic for U′ if dim(fj(U)) = dim(fj(U′)) + |U| − |U′|. Now we can deﬁne cascades.

- Deﬁnition 3.23. (cascades) Let φ ∈ A(Φ) be M∗-compatible. Suppose φc is an embedding of Kqr(p) in G∗j where φc id[q] = φ and Im(φc) is j-generic for Im(φ), such that each φcφ′ with φ′ ∈ Υ′ has


Aφcφ′ = A and is absorbable, with absorber Θφcφ′(Q) = φwφ′(Kqr(Ker)), and Cφc = {Θφcφ′(Q) : φ′ ∈ Υ′} is a set (without multiple elements). We call Cφc a cascade for φ.

To ﬂip a cascade Cφc we replace

Ψ(Cφc) := {Ψ(wφ′) : φ′ ∈ Υ′} by Ψ′(Cφc) := {φcφ′ : φ′ ∈ Υ} ∪ {Ψ′(wφ′) \ {φcφ′} : φ′ ∈ Υ′}.

This modiﬁes M∗ so as to include φ. Next we deﬁne the class of cliques for which we will show that there are many cascades.

![image 12](<2018-keevash-existence-designs_images/imageFile12.png>)

8 Here we use ‘Θ’ rather than the natural ‘A’ used in [15] to avoid clashes with other uses of ‘A’ in the paper.

- Deﬁnition 3.24. (cascading cliques) Let Q∗ = ∪j∈[z]Qj, where each Qj is the set of all M∗compatible φ ∈ A(Φ) with dim(fjφ) = q and φ(Q) ⊆ G∗j (we call φ cascading).


The following is [15, Lemma 6.10].

- Lemma 3.25. Suppose φ ∈ Q∗, Q′ = φ(Q) and e ∈ G∗ with |e \ V (M∗(Q′))| = r′. Let φ′ ∈ Υ′,

- I ∈ Q, a ∈ KerI. Then there are at most p2qnq(p−1)−r′ cascades Cφc for φ such that the absorber Θφcφ′(Q) = φwφ′(Kqr(Ker)) for φcφ′ satisﬁes eawφ′ = e.


The following is analogous to [15, Lemma 6.11].

- Lemma 3.26. whp for any cascading φ ∈ Q∗ there are at least ωpq

2

nq(p−1) cascades for φ.

Proof. We follow the proof in [15], indicating the necessary modiﬁcations. Suppose φ ∈ A(Φ), let Q′ = φ(Q), and condition on local events E = ∩e∈Q′Ee such that φ ∈ Qj. Let U be the set of vertices touched by E. As φ is M∗-compatible, each e ∈ φ(Q) has φe ∈ A(Φ) ∩ M∗ with e ∈ φe(Q) and πeφe = πeφ = id.

Next we specify the combinatorial structure of a potential cascade for φ. For the base of the cascade, we ﬁx a Φ-embedding φc of [q](p) with φc id[q] = φ and Im(φc) \ Im(φ) disjoint from U, such that for all φcψ ∈ A(Φ)≤r where ψ ∈ [q](p)r we have γ(φcψ) ≤γ G. For the absorbers in the cascade, for each φ′ ∈ Υ′ we ﬁx any Φ-embedding φφ′ of [q](Ker) with φφ′φ′0 = φcφ′, such that for all φφ′ψ ∈ A(Φ)≤r where ψ ∈ [q](Ker)r we have γ(φφ′ψ) ≤γ G. If φ′ is some φ′e with φ(Im(φ′e) ∩ [q]) = e ∈ φ(Q) we have the additional constraint φφ′eφae = φe, where ae ∈ Kerr is such that Im(πe) ⊆ Im(φae). We choose absorbers as disjointly as possible, i.e. with ‘private vertices’ Iφ′ that are pairwise disjoint and disjoint from U ∪ Im(φc), where Iφ′ = Im(φφ′) \ Im(φcφ′) if φ′ is not some φ′e or Iφ′

e = Im(φφ′e) \ (Im(φcφ′e) ∪ Im(φe)).

As (Φ,γ[G]A) is (ω,h)-extendable, the number of such choices for φc and φφ′ given φ and E is at least 0.9ωnq(p−1)+v+, where v+ = φ′ |Iφ′| = prq(pq−r − 1) − Q(q − r).

Now we consider the algebraic constraints that must be satisﬁed for the cascade described above to appear in the template. We condition on fjφc such that Im(φc) is j-generic for Im(φ) and deﬁne wφ′ = fjφcφ′ for φ′ ∈ Υ′. Then each dim(wφ′) = q. Now φc will deﬁne a cascade Cφc = {Θφcφ′(Q) : φ′ ∈ Υ′} with each Θφcφ′(Q) = φwφ′(Kqr(Ker)) = φφ′(Kqr(Ker)) as in Deﬁnitions 3.21 and 3.23 if

i. fjφφ′((i,a)) = (wφ′)i + a · wφ′ for each φ′ ∈ Υ′, i ∈ [q], a ∈ Ker, and ii. φφ′φa is activated, Aφφ′φa = A, and Te = j and πeφφ′φa = id for all φ′ ∈ Υ′, a ∈ Kerr, e ∈ φφ′φa(Q).

We have the same bound on the probability of these events as in [15], as the estimates there were suﬃciently crude to absorb the extra factor of |A|pr(q−r+1) here for the events Aφφ′φa = A. The proof of concentration of the number of cascades is also the same (the eﬀect of changing Aφ is analysed in the same way as the eﬀect of changing whether φ is activated).

The proof of [15, Lemma 8.1] (the cascade random greedy algorithm) now applies to show that

- Lemma 3.19 follows from the following lemma.


- Lemma 3.27. Suppose Ψ0 ∈ ZA(Φ) is c′2-bounded with 0 ≤γ ∂γΨ0 ≤γ ∂γM∗. Let S = (∂γΨ0)◦ and suppose M∗(S) is a set. Then there are M± ⊆ A(Φ) such that every φ ∈ M+ is cascading, M∗( φ∈M+ φ(Q)) is a set and 3c4-bounded, and ∂γM+ = ∂γM− + ∂γΨ0.


We will prove Lemma 3.27 in section 4.

# 4 Clique Exchange Algorithm

In this section we deﬁne our Clique Exchange Algorithm, which has three applications in this paper, namely to the proofs of Lemmas 4.1 and 3.27 (in this section) and Lemma 6.8 (in section 6). The following lemma will allow us to modify an integer decomposition so as to avoid unforced uses of bad sets. For the statement we recall the lattice constant C0 = C0(γ) from Lemma 2.35, and that

- C0 = 1 if γ is elementary.


- Lemma 4.1. Let A be a Σ≤-family with Σ ≤ Sq and |A| ≤ K and suppose γ ∈ (ZD)Ar. Let Φ be an (ω,h)-extendable Σ-adapted [q]-complex on [n], where ω < ω0(q,D,K) and n > n0(q,D,K). Suppose Ψ0 ∈ ZA(Φ) is θ-bounded with n−1/2 < θ < ω4. Let Bk ⊆ Φ◦k be η-bounded for r ≤ k ≤ q,


where η = (9q)−2qω. Then there is some M2θ-bounded Ψ ∈ ZA(Φ), where M2 = q(2q)2qC02ω−2, with ∂γΨ = J := ∂γΨ0 such that

- i. if k > r then U(Ψ)ψ ≤ 1 for all ψ ∈ Φk, and U(Ψ)ψ = 0 if Im(ψ) ∈ Bk,
- ii. U(Ψ)ψ ≤ U(J)ψ + C0 + 1 for all ψ ∈ Φr, and U(Ψ)ψ = U(J)ψ if Im(ψ) ∈ Br.


Lemma 4.1 and Lemma 3.18 immediately imply the following lemma, which will be used (with smaller q) in the inductive proof of Lemma 3.18 in section 6.

- Lemma 4.2. Let A be a Σ≤-family with Σ ≤ Sq and |A| ≤ K and suppose γ ∈ (ZD)Ar. Let Φ be an (ω,h)-extendable Σ-adapted [q]-complex on [n], where n−h−3q < ω < ω0(q,D,K) and n > n0(q,D,K). Suppose J ∈ γ(Φ) is θ-bounded with n−(5hq)−r < θ < ω4. Suppose Bk ⊆ Φ◦k is ηbounded for r ≤ k ≤ q, where η = (9q)−2qω. Then there is some ωq−3hθ-bounded Ψ ∈ ZA(Φ) with ∂Ψ = J such that


i. if k > r then U(Ψ)ψ ≤ 1 for all ψ ∈ Φk, and U(Ψ)ψ = 0 if Im(ψ) ∈ Bk, ii. U(Ψ)ψ ≤ U(J)ψ + C0 + 1 for all ψ ∈ Φr, and U(Ψ)ψ = U(J)ψ if Im(ψ) ∈ Br.

## 4.1 Splitting Phase

Now we start the proof of Lemma 4.1. Suppose Ψ0 ∈ ZA(Φ) is θ-bounded. We will obtain the desired Ψ by an algorithm similar to that in [15] (but with several signiﬁcant diﬀerences).

To deﬁne the ﬁrst phase of the algorithm, we recall the Kqr-decompositions Υ and Υ′ of Ω = Kqr(p) given by Lemma 3.22, and write Ω′ = Kqr(p) \ Q.

Algorithm 4.3. (Splitting Phase) Let (φi : i ∈ |Ψ0|) be any ordering of the signed elements of Ψ0, i.e. Ψ0 = i si{φi} with each si ∈ ±1 and φi ∈ Ai(Φ) for some Ai ∈ A. We apply a random greedy algorithm to choose φ∗i ∈ XEi(Φ) for each i, where Ei = ([q](p),[q],φi). We say φ∗i uses e ∈ Φ◦ if

- e ⊆ Im(φ∗i φ) for some φ ∈ Υ′ ∪ Υ and e \ Im(φi) = ∅. Let Fi be the set of used e ∈ Φ◦r. We choose φ∗i ∈ XEi(Φ) uniformly at random subject to not using Fi or B = ∪kBk.


- Lemma 4.4. whp Splitting Phase does not abort and F|Ψ0| is M1θ-bounded, where M1 = 2r+3(pq)qω−1.


Proof. For i ∈ [|Ψ0|] we let Bi be the bad event that Fi is not M1θ-bounded. Let τ be the smallest i for which Bi holds or the algorithm aborts, or ∞ if there is no such i. It suﬃces to show whp τ = ∞. We ﬁx i0 ∈ [|Ψ0|] and bound P(τ = i0) as follows.

We claim that for any i < i0 the restrictions on φ∗i forbid at most half of the possible choices of φ∗i ∈ XEi(Φ). To see this, ﬁrst note that XEi(Φ) > ωnpq−q as Φ is (ω,s)-extendable. As Fi is M1θ-bounded and each Bk is η-bounded, at most (pq)q(qη +M1θ)npq−q choices use Fi ∪B; the claim follows.

P′(e ∈ φ∗i(Ω′)), where P′ denotes conditional probability given the choices made before step i.

Now for each e ∈ Φ◦r let re = i<i

0

For any i < i0, writing r′ = |e \ Im(φi)|, there are at most (pq)qnpq−q−r′ choices of φ∗i such that

- e ∈ φ∗i (Ω′), so by the claim P′(e ∈ φ∗i (Ω′)) < 2(pq)qω−1n−r′. Also, given r′ ∈ [r], as Ψ0 is θ-bounded there are at most 2 r r′ θnr′ choices of i such that |e \ Im(φi)| = r′. Therefore re < 2r+2(pq)qω−1θ.

Now ﬁx any f ∈ Φ◦r−1 and write U(Fi)f = i<i

0

Xi, where Xi is the number of e ∈ Φ◦r with

- f ⊆ e ∈ φ∗i (Ω′). Then each |Xi| < |Ω′| and i<i


E′Xi = {re : f ⊆ e} < 2r+2(pq)qω−1θn, so by

0

- Lemma 3.3 whp U(Fi)f < M1θn, so Fi is M1θ-bounded, so τ > i0. Taking a union bound over i0, whp τ = ∞, as required.


We let9 Ψ1 = Ψ0 + i∈[|Ψ0|] si(Ai(Φ[φ∗i Υ′]) − Ai(Φ[φ∗i Υ])). Then ∂γΨ1 = ∂γΨ0 = J, and all signed elements of Ψ0 are cancelled, so Ψ1 is supported on maps added during Splitting Phase.

We classify maps added during Splitting Phase as near or far, where the near maps are those of the form φ∗i φ for φ ∈ Υ′ with |Im(φ) ∩ [q]| = r. Also, for each pair (O,φ′) where φ′ is added during Splitting Phase, O ∈ Φr/Σ and O ⊆ φ′Σ, we call (O,φ′) near if φ′ = φ∗iφ is near and Im(O) = φ∗i(Im(φ) ∩[q]), otherwise we call (O,φ′) far. We ﬁx orbit representatives ψO ∈ O and say that (O,φ′) has type θ where γ(φ′)O = γ[ψO]θ = γ(ψOθ−1) (we ﬁx any such θ for each γ-atom at O). We also classify maps and near pairs as positive or negative according to their sign in Ψ1.

Note that for each orbit O such that there is some far pair on O there are exactly two such far pairs (O,φ±) and γ(φ−)O = −γ(φ+)O. For each O ∈ Φr/Σ we let ΨO be the sum of all ±{φ} where ±(O,φ) is a signed near pair in Ψ1. Then (∂γΨO)O = (∂γΨ1)O = JO.

## 4.2 Grouping Phase

Now we will organise the near pairs on each O into some cancelling groups and U(J)O ungrouped near pairs. To do so we will introduce some additional near pairs in which we add and subtract some given element of A(Φ) (which has no net eﬀect on Ψ1).

Consider any orbit O with ψO ∈ ΦB, B ∈ Q. As J = ∂γΨ0 ∈ γ(Φ) = Lγ(Φ) ⊆ L−γ (Φ), we have fB(J)ψO ∈ γB = γθ : θ ∈ AB . By deﬁnition of U(J)O we can express JO as a sum of U(J)O signed γ-atoms, i.e. fB(J)ψO = θ nOθ γθ, so JO = θ nOθ γ(ψOθ−1), where nO ∈ ZAB with |nO| = U(J)O. Let mOθ ± be the number of near pairs on O of type θ of each sign. As JO = (∂γΨO)O we have fB(J)ψO = θ(mOθ + − mOθ −)γθ, so nO − mO+ + mO− ∈ ZB(γ). By Lemma 2.35 we have nOj ∈ ZB(γ) for j ∈ [tO] for some tO ≤ C0(|nO| + |mO+| + |mO−|) with each |nOj| ≤ C0 and nO − mO+ + mO− = j∈[tO] nOj.

We will assign the near pairs to cancelling groups and ungrouped near pairs so that for each such O and θ, there are |nOθ | (correctly signed) ungrouped near pairs on O of type θ, and the jth group has |nOjθ | such near pairs.

Let dOθ = ( j |nOjθ |) − mOθ + = ((|nOθ | + j |nOjθ |) − (mOθ + + mOθ −))/2. If dOθ > 0 then we need to introduce dOθ new near pairs of type θ on O in the Grouping Phase below. If dOθ ≤ 0 then we do not need to introduce any new near pairs of type θ on O. If dOθ < 0 then we have 2|dOθ | unassigned near pairs of type θ on O, with which we form |dOθ | additional cancelling groups each containing one positive and one negative near pair.

Algorithm 4.5. (Grouping Phase) Let SJ = {(Oi,θi) : i ∈ [|SJ|]} be such that each (O,θ) with dOθ > 0 appears dOθ times. We apply a random greedy algorithm to choose φi ∈ XEi(Φ) with

![image 13](<2018-keevash-existence-designs_images/imageFile13.png>)

9 Note that (e.g.) Ai(Φ[φ∗i Υ]) = {φ∗i ψ ∈ Ai(Φ) : ψ ∈ Υ}.

Ei = (−→q ,Im(θi),ψOi(θi)−1). We say φi uses e ∈ Φ◦r if Im(Oi) = e ⊆ Im(φi). Let Fi′ be the set of used e ∈ Φ◦r. We choose φi uniformly at random subject to not using Fi′ ∪ F|Ψ0| ∪ B.

Similarly to Lemma 4.4, whp Grouping Phase does not abort and F|′SJ| is M1θ-bounded. We create new near pairs by adding and subtracting each φi, and then organise the near pairs into cancelling groups and ungrouped near pairs as described above.

## 4.3 Elimination Phase

In the Elimination Phase we replace Ψ1 by Ψ2 so as to remove all cancelling groups while preserving ∂Ψ2 = ∂Ψ1 = J. We start by recalling [15, Deﬁnition 6.15].

- Deﬁnition 4.6. Let Ω1 and Ω2 be two copies of Ω. Fix f ∈ Υ and f′ ∈ Υ′ with |V (f) ∩ V (f′)| = r. For j = 1,2 we denote the copies of Υ, Υ′, f, f′ in Ωj by Υj, Υ′j, fj, fj′. Let Ω∗ be obtained by identifying Ω1 and Ω2 so that f1′ = f2′. Let Υ+ = Υ1 ∪ (Υ′2 \ {f2′}) and Υ− = Υ2 ∪ (Υ′1 \ {f1′}). Then Υ+ is a Kqr-decomposition of Ω∗ containing f1 and Υ− is a Kqr-decomposition of Ω∗ containing f2.


Next we introduce some notation for octahedra and their associated signed characteristic vectors.

- Deﬁnition 4.7. (octahedra) Let Φ be an R-complex and B ⊆ R. The B-octahedron is OB = B(2).


For x ∈ [2]B we deﬁne the sign of x by s(x) = (−1) i(xi−1). For ψ ∈ OBB such that ψ(i) = (i,xi) for all i ∈ B we also write s(ψ) = s(x). Let OB(Φ) be the set of Φ-embeddings of OB. For φ ∈ OB(Φ)

we let χ(φ) denote the ‘signed characteristic vector’ in ZΦB, where χ(φ)φ◦ψ = s(ψ) for ψ ∈ OBB, and all other entries of χ(φ) are zero.

The following deﬁnition and lemma implement octahedra as signed combinations of cliques.

- Deﬁnition 4.8. For x = (xi) ∈ [s]q we identify x with the partite map x : [q] → [q] × [s] where each x(i) = (i,xi), and also with the image of this map. We write 1 for the map with all 1(i) = 1 and identify [q] with 1([q]).


For e ∈ [q](s)r let Xe = {x : e ⊆ x}. Suppose w ∈ {−1,0,1}[s]q. We say e ∈ [q](s)r is bad for w if |{x ∈ Xe : wx = 1}| > 1 or |{x ∈ Xe : wx = −1}| > 1. We say w is simple if no e is bad for w. We deﬁne ∂w ∈ Z[q](s)r by ∂we = x∈X

wx.

e

- Lemma 4.9. Let s = (2q)r. Then for any B ∈ Q there is a simple wB ∈ {−1,0,1}[s]q with ∂wB = χ(OB). Let wrB denote the set of e ∈ [q](s)r such that wxB = 0 for some x ∈ Xe. We can choose wB with w1B = 1 so that wrB[V (OB) ∪ [q]] = OBB ∪ Q.


Proof. We start by setting wxB = (−1) ri=1(xi−1) if xi ∈ [2] for i ∈ B and xi = 1 for i ∈ [q] \ B, otherwise wxB = 0. Then ∂weB = χ(OB). We will repeatedly apply transformations to wB that preserve ∂wB = χ(OB) until wB becomes simple. Suppose wB is not simple. Fix e bad for wB and x,x′ ∈ Xe with wxB = 1 and wxB′ = −1. Fix a [q](s)-embedding φ of Ω∗ as in Deﬁnition 4.6, where φ(f1) = x, φ(f2) = x′ and if a ∈ φ(V (Ω∗)) \ (x ∪ x′) then wyB = 0 whenever a ∈ y. We modify wB by adding −1 to each φ(g) where g ∈ Ψ+ and 1 to each φ(g′) where g′ ∈ Ψ−. This preserves ∂weB = χ(OB) and reduces the sum of |wxB| over x ∈ Xe with e bad for wB. The process terminates with wB that is simple, and we can relabel so that the other properties hold.

Let wB = [q](s)[wrB] be the [q]-complex obtained by restricting [q](s) to wrB.

Algorithm 4.10. (Elimination Phase) Let (Ci : i ∈ [P]) be any ordering of the cancelling groups, where each Ci = {(Oi,φij) : j ∈ [|Ci|]} for some orbit Oi with representative ψOi ∈ ΦBi and each φij ∈ Aij(Φ). Our random greedy algorithm will make several choices at step i. First we choose ψi∗ ∈ XEi(Φ) where Ei = (Bi(2),Bi,ψOi); we say that this choice has type 1. Then for each

(Φ) where Eji = (wBji,Fji,φ′ij), Fji = [q] ∪ (Bji × [2]), Bji = θji(Bi), ψOi = φijθji, φ′ij |[q]= φij, φ′ij(θji(x),y) = ψi∗(x,y) for x ∈ Bi, y ∈ [2].

- j ∈ [|Ci|] we make type 2 choices φ∗ji ∈ XEi


j

- i
- j


We let Ω′i = Bi(2)r \ {idBi} and Ωij = wB

r \ (Bji(2) ∪ −→q r). We say that ψi∗ uses e ∈ Φ◦r with type 1 if e = Im(ψi∗ψ) for some ψ ∈ Ω′i (we also write e ∈ ψi∗(Ω′i)). We say that φ∗ji uses e ∈ Φ◦r with type 2 if e = Im(φ∗jiψ) for some ψ ∈ Ωij or if |e| > r and e ⊆ Im(φ∗jix) for some x ∈ [s]q \ {1} with wB

- i
- j


x = 0.

For α = 1,2 let Fiα be the set of e ∈ Φ◦r used with type α. We make each choice at step i uniformly at random subject to not using Fi1 ∪ Fi2 ∪ F|Ψ0| ∪ F|′SJ| ∪ B.

- i
- j


We will obtain Ψ from Ψ1 by adding x wB

x Aij(Φ[φ∗jix]) for each i ∈ [P] and j ∈ [|Ci|] with the opposite sign to that of the near pair (Oi,φij). This cancels all cancelling groups and preserves ∂γΨ = ∂γΨ1 = J by the following lemma, which shows that the construction for each cancelling group has no total eﬀect on ∂γΨ, using j∈[|Ci|] γθji = 0.

- Lemma 4.11. With notation as in Algorithm 4.10, we have


∂γ

x

- i
- j


wB

x Aij(Φ[φ∗jix]) = {χ(ψi∗)eγ(φ∗jie(θji)−1) : e ∈ ψi∗OBBii}.

- i
- j


Proof. By Lemma 4.9, we have (∂γ x wB

x Aij(Φ[φ∗jix]))ψ equal to zero unless ψΣ = eΣ with e ∈ ψi∗OBBii, in which case, writing e′ = e ◦ (θji)−1, it equals (∂wB

- i
- j


e′ )γ(φ∗jie′) = χ(ψi∗)eγ(φ∗jie′). Recall M1 = 2r+3(pq)qω−1, M2 = q(2q)2qC02ω−2 and note that M2θ < ω1.5 for ω < ω0(q,D,K).

- Lemma 4.12. whp Elimination Phase does not abort and FP1 ∪ FP2 is M2θ/2-bounded.


Proof. For i ∈ [P] we let Bi be the bad event that Fi1 is not 2C0M1θ-bounded or Fi2 is not M2θ/4bounded. Let τ be the smallest i for which Bi holds or the algorithm aborts, or ∞ if there is no such i. It suﬃces to show whp τ = ∞. We ﬁx i0 ∈ [P] and bound P(τ = i0) as follows.

Consider any i < i0. Then Fi1 is 2C0M1θ-bounded and Fi2 is M2θ/4-bounded. As Φ is (ω,h)extendable, each XEi(Φ) > ωnvEi and XEi

vEi

j. As F|Ψ0| and F|′SJ| are M1θ-bounded, and each Bk is η-bounded, at most half of the choices for ψi∗ or φ∗ji are forbidden due to using Fi1 ∪ Fi2 ∪ F|Ψ0| ∪ F|′SJ| ∪ B.

(Φ) > ωn

j

Next we ﬁx e ∈ Φ◦r and estimate the probability of using e at step i with each type. For uses of type 1 there are at most 2rnvEi−|e\Im(Oi)| choices of ψi∗ with e ∈ ψi∗(Ω′i), so P′(e ∈ ψi∗(Ω′i)) ≤ 2r+1ω−1n−|e\Im(Oi)|. Similarly, for uses of type 2 we have P′(e ∈ φ∗ji(Ωij)) < 2|Ωij|ω−1n−rji(e), where rji(e) is the minimum |e \ Im(ψ′)| with ψ′ ⊆ φij or ψ′ = ψi∗ψ with ψ ∈ Bji(2).

For any r′ ∈ [r], as Φ0 is θ-bounded, by construction of the cancelling groups in Grouping Phase, there are at most r r′ C0θnr′ choices of i with |Im(Oi) \ e| = r′, so re1 := i<i

P′(e ∈ ψi∗(Ω′i)) < 22rω−1C0θ. Similarly, as F|Ψ0| and F|′SJ| are M1θ-bounded and Fi1 is 2C0M1θ-bounded, there are

0

- at most 4C0M1 r r′ θnr′ choices of i with rji(e) = r′, so re2 := i<i


0 j∈[|Ci|] P′(e ∈ φ∗ji(Ωij)) < C0|Ωij|2r+3C0M1θ. By Lemma 3.3 we deduce whp Fi1 is 2C0M1θ-bounded and Fi2 is M2θ/4-bounded, so τ > i0. Taking a union bound over i0, whp τ = ∞, as required.

For any ψ ∈ Φr−1 we have U(Ψ)ψ ≤ U(Ψ0)ψ + |(F|Ψ0| + F|′SJ| + FP1 + FP2) |ψ | < M2θn, so Ψ is M2θ-bounded. For k > r we avoided using any ψ ∈ Φk more than once or Bk at all, so U(Ψ)ψ ≤ 1 for all ψ ∈ Φk, and U(Ψ)ψ = 0 if Im(ψ) ∈ Bk. For any ψ ∈ Φr we have a contribution of U(J)ψ from ungrouped near pairs to U(Ψ)ψ. If ψ ∈ Br there are no other uses, so U(Ψ)ψ = U(J)ψ, and otherwise there are at most10 C0 + 1 other uses by a cancelling group, so U(Ψ)ψ ≤ U(J)ψ + C0 + 1. This completes the proof of Lemma 4.1.

## 4.4 Proof of Lemma 3.27

The proof of Lemma 3.27 is very similar to that of Lemma 4.1, so we will just show the necessary modiﬁcations. We consider Ψ0 ∈ ZA(Φ) that is c′2-bounded, where c′2 = ω−h2c2. There are no bad sets B. We also suppose 0 ≤γ ∂γΨ0 ≤γ ∂γM∗ and M∗(S) is a set, where S = (∂γΨ0)◦. We require the following deﬁnitions for Splitting Phase.

- Deﬁnition 4.13. Consider any extension E(φ) = ([q](p),[q],φ) where φ ∈ A(Φ) with γ(φ) ≤γ G. Let


H(φ) = [q](p)r\−→q r. We let XE∗(φ),H(φ) be the set or number of extensions φ+ ∈ XE(φ),H(φ)(Φ,γ[∂γM∗]A) such that

- i. φ+ is rainbow: j = j′ whenever {ψ,ψ′} ⊆ [q](p)r \ −→q r, Im(φ+ψ) ∈ G∗j, Im(φ+ψ′) ∈ G∗j′, and
- ii. each φ+φ′ with φ′ ∈ Υ′ is M∗-compatible if |Im(φ′) ∩ [q]| < r or M∗-compatible bar φ+(e) if Im(φ′) ∩ [q] = e ∈ Q.


We claim whp

XE∗(φ),H(φ) > ωnpq−q(ω2zρ/2)Qpr. (1) Indeed, the proof of Lemma 3.12 already gives rainbow extensions φ+, and by Remark 3.11.ii we can also require πeφ+ψ = id and Aφe = A for all ψ ∈ [q](p)r \ −→q , e = Im(φ+ψ), which gives φ+ ∈ XE∗(φ),H(φ).

For the modiﬁed Splitting Phase, recalling that Fi is the set of used e ∈ Φ◦r, we let Di = ∪e∈FiM∗(e), and choose φ∗i ∈ XE∗(φ

i),H(φi) uniformly at random subject to φ∗i (Ω′)∩(M∗(S)∪Di) = ∅. Note that each φ∗i (Ω′) ⊆ G∗ is rainbow, so M∗(φ∗i (Ω′)) is a set.

The modiﬁed form of Lemma 4.4 is to show whp D|Ψ0| is c3-bounded. Accordingly, the bad event Bi is that Di is not c3-bounded. To see that at most half of the choices of φ∗i ∈ XE∗(φ

i),H(φi) are forbidden we use (1), which gives XE∗(φ

i),H(φi) > ωnpq−q(ω2zρ/2)Qpr > 4(pq)qc3npq−q. For e ∈ G∗ we deﬁne re = i<i

0 e′∈M∗(e) P′(e′ ∈ φ∗i (Ω′)). As Ψ0 is c′2-bounded, there are at most c′2 r r′ nr′ choices of i with |e′ \ Im(φi)| = r′, each P′(e′ ∈ φ∗i (Ω′)) <

P′(e ∈ M∗(φ∗i (Ω′))) = i<i

0

- 2r!|Ω′|ω−1(ω2zρ/2)−Qprn−r′, so re < (pq)qω−1(ω2zρ/2)−Qpr2r+1c′2. We conclude that whp no Bi occurs, so whp D|Ψ0| is c3-bounded.


Deﬁning Ψ1 as before, we have ∂γΨ1 = ∂γΨ0 = J and Ψ1 is supported on maps added during Splitting Phase, which are now rainbow in G∗ and M∗-compatible bar at most one edge.

As before, we classify maps φ′ and pairs (O,φ′) added in Splitting Phase as near/far and positive/negative, and assign types to pairs. As γ is now elementary, the next part of the algorithm

![image 14](<2018-keevash-existence-designs_images/imageFile14.png>)

10 The ‘+1’ is only needed to account for cancelling pairs in the case C0 = 1.

becomes simpler. Indeed, for each O ∈ Φr/Σ we can group the near pairs on O into cancelling groups of size one (near pairs of type zero) or size two (of the same type and opposite sign), and at most one additional positive near pair (O,φO), which we call ‘solo’, where if Im(O) = e ∈ S with γ(e) = 0 then φO(Q) ⊆ G∗, φO is M∗-compatible bar e, and γ(e) = γ(ψ) with ψ ⊆ φO.

In Grouping Phase we only need to consider the solo near pairs, which we denote by {(Oi,φOi) :

i ∈ [s′]}. We let ei = Im(Oi) ∈ G∗, Ai = Aφei, and θi ∈ AiBi be such that ψi′ := ψOi(θi)−1 = πe−i1 ∈ Ai, so γ(ψi′) = γ(ei). Writing Di′ = ∪i′<iM∗(φi(Q))), we choose φi ∈ XEi(Φ) with Ei = (−→q ,Im(θi),ψOi(θi)−1) uniformly at random subject to (φ∗i (Q) \ {ei}) ∩ (M∗(S) ∪ D|Ψ0| ∪ Di′) = ∅ and φi ∈ Q∗ being cascading. Similarly to Lemma 4.15 (see below), there are at least 0.9(ω/z)q−r choices for each φi, and similarly to Lemma 4.4 whp Ds′′ is c3-bounded.

The next deﬁnition and accompanying lemma set up the notation for the Elimination Phase and show that there are whp many choices for each step.

- Deﬁnition 4.14. Given A ∈ A, B ∈ Q, ψ ∈ A(Φ)≤B = ΦB we let E(ψ) = (B(2),B,ψ) and H(ψ) = B(2)B \ {idB}.


Suppose ψ ⊆ φ ∈ A(Φ) with φ(Q) \ Im(ψ) rainbow in G∗ and φ is M∗-compatible bar Im(ψ). Let XEφ(ψ),H(ψ) be the set or number of ψ∗ ∈ XE(ψ),H(ψ)(Φ,γ[∂γM∗]A) such that

- i. Im(ψ∗) ∩ Im(φ) = Im(ψ),
- ii. Q∗ := (φ(Q) ∪ {Im(ψ∗ψ′) : ψ′ ∈ B(2)B}) \ {Im(ψ)} is rainbow in G∗, and
- iii. for all e = Im(ψ∗ψ′) with ψ′ ∈ B(2)B \ {idB} we have Aφe = A and πeψ∗ψ′ = id. For ψ∗ ∈ XEφ(ψ),H(ψ) we let Eψφ∗ = (wB,F,ψ∗ ∪ φ), where F = [q] ∪ (B × [2]).


We let Hψφ∗ = wB \ wB[F] and vc := vEφ

. Let Xc(Eψφ∗)± be the set or number of φ+ ∈ XEφ

ψ∗

ψ∗,Hψφ∗(Φ,γ[∂γM∗]A) that are ‘rainbow Υ± cascading’, i.e. φ+x ∈ Q∗ is cascading for all x ∈ Υ± := {x ∈ [s]q \ {1} : wxB = ±1}, and j = j′ whenever {x,x′} ⊆ Υ± with φ+x ∈ Qj, φ+x′ ∈ Qj′.

- Lemma 4.15. For ψ, φ, ψ∗ as in Deﬁnition 4.14 whp Xc(Eψφ∗)± > (ω/z)3Q2srnvc. The proof of Lemma 4.15 requires the following analogue of Lemma 3.10.
- Lemma 4.16. Let S ⊆ Φ◦r with |S| < h = z and E = ∩f∈SEf. Suppose φ ∈ A(Φ) with γ(φ) ≤γ G such that |φ(Q) ∩ S| ≤ 1 and each e′ ∈ φ(Q) \ S is not touched by E. Let j ∈ [z] be such that Te′ = j for all e′ ∈ S \ φ(Q). If φ(Q) ∩ S = {e} suppose also that πeφ = id, e ∈ G∗j, φe ∈ A(Φ). Then P(φ ∈ Qj | E) > (ω/z)3Q2.


Proof. Let 1e be 1 if φ(Q) ∩S = {e} or 0 otherwise. For e′ ∈ φ(Q) \ S let πe0′ : e′ → [q] be such that πe0′φ = id. For each e′ ∈ φ(Q) \ S we ﬁx φe0′ ∈ A(Φ) with πe0′φe0′ = id and estimate the probability that all such e′ ∈ G∗j with φe′ = φe0′. Let U be the set of vertices touched by E. As (Φ,γ[G]A) is (ω,h)-extendable, there are at least (1 − O(n−1))ωn(Q−1e)(q−r) choices for all φe0′ such that the sets Im(φe0′)\e′ are pairwise disjoint and disjoint from Im(φ)∪U, and for each e′ ∈ φ(Q)\S and ψ ⊆ φe0′ with Im(ψ) ∈ φe0′(Q) \ {e′} we have γ(ψ) ≤γ G. The probability that φe0′ is activated, Aφe′

= A, Tf = j and πfφe0′ = id for all such e′ and f ∈ φe0′ is at least ((z(q)r)−Q|A|−1ω2)Q−1e.

0

We condition on fj |Im(φ) such that dim(fjφ) = q; this occurs with probability 1 − O(n−1). For each e′ ∈ φ(Q) \ S there is a unique ye′ ∈ Frpa such that (Mye′)i = fjπe−′1(i) for all i ∈ Im(πe′). With probability (1 + O(n−1))(p−a)(q−r)(1e−Q) we have fj(φe′(i)) = (Mye′)i for all such e′ and

i ∈ [q] \ Im(πe′). Therefore P(∩e′{φe′ = φe0′} | E) > (1 + O(n−1))[(z(q)r|A|−1ω−2)Qpa(q−r)]1e−Q. Summing over all choices for φe0′ gives P(φ ∈ Qj | E) > (ω/z)3Q2.

- Proof of Lemma 4.15. As (Φ,γ[G]A) is (ω,h)-extendable, there are at least ωnvc choices of φ+ ∈


ψ∗,Hψφ∗(Φ,γ[G]A). We ﬁx any such φ+ and estimate P(φ+ ∈ Xc(Eψφ∗)+) by repeated application

XEφ

of Lemma 4.16. (The same estimates will apply to Xc(Eψφ∗)−.) We consider sequentially each φ′ ∈ Υ+, and ﬁx j ∈ [z] distinct from all previous choices such that (recall Q∗ from Deﬁnition 4.14)

if Im(φ′) ∩ Q∗ = e then e ∈ G∗j.

We let E be the intersection of all local events Ee where e ∈ Q∗ or e ⊆ Im(φ+φ′′) for some previously considered φ′′ ∈ Υ+. We discard O(nvc−1) choices of φ+ such that any e′ ∈ φ+φ′(Q) is touched by E. Then P(φ+φ′ ∈ Qj | E) > (ω/z)3Q2 by Lemma 4.16. Multiplying all conditional probabilities and summing over φ+ gives EXc(Eψφ∗)+ > (1−O(n−1))((ω/z)3Q2)sr−1nvc; concentration follows from Lemma 3.5.

In the modiﬁed Elimination Phase, we recall that the cancelling groups have size one (zero near pairs) or two (cancelling pairs), say Ci = {(Oi,φi)} or Ci = {(Oi,φi+),(Oi,φi−)}. We adopt the notation of Deﬁnition 4.14 and ﬁx representatives ψOi ∈ Oi as in Algorithm 4.10.

If Ci = {(Oi,φi)} we write11 φi+ = φi, ψOi = φi+θ+i and ψ+i = ψOi(θ+i )−1 ⊆ φi+ ∈ Ai(Φ), where γ(ψ+i ) = 0, we choose ψi+ ∈ Xφ

i

i

E(ψ+i ),H(ψ+i ) and then φ+i ∈ Xc(Eφ

ψi+)+.

+

+

If Ci = {(Oi,φi+),(Oi,φi−)}, we write ψOi = φi±θ±i and ψ±i = ψOi(θ±i )−1 ⊆ φi± ∈ Ai±(Φ), where γ(ψ+i ) = γ(ψ−i ). We note that γ(φi±) − γ(ψ±i ) ≤γ ∂γM∗, let B±i = θ±i (Bi) and choose ψi+ ∈ Xφ

i

+

E(ψ+i ),H(ψ+i ) such that Q±i = (φi±(Q) ∪ {Im(ψi+ψ′) : ψ′ ∈ B±i (2)r}) \ Im(Oi)

is rainbow in G∗ (this holds by deﬁnition for Q+i but is an extra requirement for Q−i ). We deﬁne ψi− ∈ Xφ

i ±

i −

E(ψ−i ),H(ψ−i ) by ψi−(θ−i (x),y) = ψi+(θ+i (x),y) and choose φ±i ∈ Xc(Eφ

ψi±)±. We deﬁne type 1 and 2 uses similarly to before and let Diα = ∪ψ∈Fα

M∗(Im(ψ)). We make the above choices uniformly at random such that M∗(Q±i ) both avoid M∗(S) ∪ D|Ψ0| ∪ D|′SJ| ∪ Di1 ∪ Di2.

i

To modify Lemma 4.12, we let Bi be the event that Di1 ∪ Di2 is not c4-bounded. To see that at most half of the choices for any ψi+ or φ±i are forbidden, we use Xφ

i

E(ψ+i ),H(ψ+i ) > ωnq−r(ω2zρ/2)Q > qqc4nq−r (this bound is similar to that in (1)) and Xc(Eφ

+

i ±

ψi±)± > (ω/z)3Q2srnvc > (qs)qc4nvc (by

- Lemma 4.15). Then for e ∈ G∗ we have


P′(e′ ∈ ψi+(Ω′i)) < 2r22rω−1(ω2zρ/2)−Qc3,

P′(e ∈ M∗(ψi+(Ω′i))) =

re1 :=

i<i0 e′∈M∗(e)

i<i0

recalling Ω′i = Bi(2)r \ {idBi}, and re2 :=

P′(Im(ψ) ∈ M∗(e)) < (qs)q(ω/z)−3Q2src3,

i<i0 ψ∈Γi

![image 15](<2018-keevash-existence-designs_images/imageFile15.png>)

11 The sign of a zero pair is irrelevant; we ﬁx + for convenient notation.

i

r ± \ (B±i (2) ∪ −→q r), we let Γi = φ+i Ωi+ if |Ci| = 1 or Γi = φ+i Ωi+ ∪ φi−Ωi− if |Ci| = 2. As before, we deduce whp no Bi occurs, so DP1 ∪ DP2 is c4-bounded.

where, writing Ωi± = wB

i

To conclude, we obtain Ψ from Ψ1 where for each i ∈ [P] we add x wB

x+Ai(Φ[φ+i x]) with the opposite sign to (Oi,φi) if |Ci| = 1, or x wB

i

i

x+Ai+(Φ[φ+i x]) − x wB

x−Ai−(Φ[φ−+x]) if |C2| = 1; this cancels all cancelling pairs and preserves ∂γΨ = ∂γΨ0. Also, for all positive maps φ added in Grouping Phase and not cancelled, or added during Elimination Phase, φ is cascading, M∗(φ(Q)) is a set, all such M∗(φ(Q)) are disjoint, their union is contained in DP1 ∪ DP2 , which is c4-bounded and disjoint from M∗(S). This completes the proof of Lemma 3.27.

# 5 Integral decomposition

In this section we give a characterisation of the decomposition lattice γ(Φ) , which generalises the degree-type conditions for Kqr-divisibility to the labelled setting. The characterisation is given in the second subsection, using a characterisation of the simpler auxiliary problem of octahedral decomposition, which is given in the ﬁrst subsection.

## 5.1 Octahedral decomposition

- A key ingredient in the results of Graver and Jurkat [12] and Wilson [34] (generalised in [15]) is the decomposition of null vectors by octahedra. In this subsection we establish an analogous result for adapted complexes. We start by deﬁning null vectors. Throughout, Φ is a Σ-adapted R-complex and Γ is a ﬁnite abelian group.


- Deﬁnition 5.1. (null) For J ∈ ΓΦ and ψ ∈ Φ we write ∂Jψ = J |ψ= {Jφ : ψ ⊆ φ ∈ Φ}. We deﬁne ∂iJ ∈ ΓΦi by (∂iJ)ψ = ∂Jψ for ψ ∈ Φi. We say J is i-null if ∂iJ = 0. For J ∈ ΓΦj we write ∂J = ∂j−1J; we say J is null if ∂J = 0, i.e. J is (j − 1)-null.


Next we introduce the symmetric analogues of octahedra and their associated signed characteristic vectors (recall Deﬁnitions 2.33 and 4.7).

- Deﬁnition 5.2. Given ψ∗ ∈ OB(Φ) and v ∈ ΓΣB let χ(v,ψ∗) denote the ‘symmetric characteristic vector’ in (ΓΣB)ΦB where χ(v,ψ∗)ψ∗ψτ = s(ψ)vτ whenever ψ ∈ OBB, τ ∈ ΣBB, and all other entries of χ(v,ψ∗) are zero. For Ψ ∈ (ΓΣB)OB(Φ) we write ∂Ψ = ψ∗ χ(Ψψ∗,ψ∗).


We note the linearity χ(v+v′,ψ∗) = χ(v,ψ∗)+χ(v′,ψ∗), which follows from (v+v′)τ = vτ +v′τ.

- Lemma 5.3. If ψ∗ ∈ OB(Φ) and v ∈ ΓΣB then χ(v,ψ∗) is symmetric and null.


Proof. For ψ ∈ OBB and τ,τ′ ∈ ΣBB we have χ(v,ψ∗)ψ∗ψτ′τ = s(ψ)vτ′τ = χ(v,ψ∗)ψ∗ψτ′τ, so χ(v,ψ∗) is symmetric. Also, for any ψ± ∈ OBB that agree on ψ′ ∈ OBB′′ with |B′| = |B| − 1 we have ∂χ(v,ψ∗)ψ∗ψ′τ = χ(v,ψ∗)ψ∗ψ+τ + χ(v,ψ∗)ψ∗ψ−τ = s(ψ+)vτ + s(ψ−)vτ = 0, so χ(v,ψ∗) is null.

The following main lemma of this subsection shows that groups of symmetric null vectors are generated by symmetric characteristic vectors of octahedra when Φ is extendable.

- Lemma 5.4. Let Φ be an (ω,s)-extendable Σ-adapted R-complex and B ⊆ R with |B| = r, where


s = 3r2, n = |V (Φ)| > n0(r,Γ) is large and ω > n−1/2. Suppose H is a symmetric subgroup of ΓΣB and J ∈ HΦB is symmetric and null. Then J = ∂Ψ for some Ψ ∈ HOB(Φ).

It is convenient to ﬁrst reduce the proof of Lemma 5.4 to the case B = R.

- Lemma 5.5. It suﬃces to prove Lemma 5.4 when B = R.

Proof. We reduce the general case of Lemma 5.4 to the case B = R as follows. Let Φ′ be the B-complex with Φ′B′ = ΦB′ for all B′ ⊆ B. Then Φ′ is ΣBB-adapted and (ω′,s)-extendable, with ω′ = ωn/n′ > n1/2/n′ > n′−1/2, where n′ = |V (Φ′)|.

Suppose B ∈ C ∈ PΣ. Let X = {xB′ : B′ ∈ C} where for each B′ ∈ C we ﬁx any representative xB′ ∈ ΣBB′. Note that any σ ∈ ΣB has a unique expression σ = τx with τ ∈ ΣBB, x ∈ X.

We deﬁne π : (ΓX)ΣBB → ΓΣB by π(v)τx = (vτ)x. For any set Y we deﬁne π : ((ΓX)ΣBB)Y → (ΓΣB)Y by π(w)y = π(wy) for all y ∈ Y . Note that for any v ∈ (ΓX)ΣBB and τ′ ∈ ΣBB we have π(vτ′) = π(v)τ′; indeed, for any τ ∈ ΣBB and x ∈ X we have π(vτ′)τx = ((vτ′)τ)x = (vτ′τ)x = π(v)τ′τx = (π(v)τ′)τx. We let H′ = {h′ : π(h′) ∈ H} and note that H′ is a symmetric subgroup of (ΓX)ΣBB.

Suppose J ∈ HΦB is symmetric and null. Deﬁne J′ ∈ (H′)Φ′B by ((Jψ′ )τ)x = (Jψ)τx. Note that π(J′) = J.

We claim that J′ is symmetric and null. To see this, note that for any τ,τ′ ∈ ΣBB and x ∈ X we have ((Jψ′ τ′)τ)x = ((Jψ′ )τ′τ)x = (Jψ)τ′τx = (Jψτ′)τx = (Jψτ′)τx = ((Jψτ′ ′)τ)x, i.e. Jψ′ τ′ = Jψτ′ ′, i.e.

- J′ is symmetric. Also, for any ψ′ ∈ Φ′B′ with B′ ⊆ B, |B′| = r − 1 and τ ∈ ΣBB, x ∈ X we have ((∂Jψ′ ′)τ)x = {((Jψ′ )τ)x : ψ′ ⊆ ψ} = {(Jψ)τx : ψ′ ⊆ ψ} = (∂Jψ)τx = 0, so J′ is null, as claimed.


Now by the case B = R of Lemma 5.4 we have J′ = ∂Ψ′ for some Ψ′ ∈ (H′)OB(Φ). Let Ψ = π(Ψ′) ∈ HOB(Φ). It remains to show that ∂Ψ = J, i.e. for any ψ ∈ ΦB that ∂Ψψ = π(∂Ψ′ψ). It suﬃces to show for any ψ∗ ∈ OB(Φ) that χ(Ψψ∗,ψ∗)ψ = πχ(Ψ′ψ∗,ψ∗)ψ. Let τ0 ∈ ΣBB be such that ψτ0−1 ∈ ψ∗OBB. Then χ(Ψ′ψ∗,ψ∗)ψ = Ψ′ψ∗τ0 and χ(π(Ψ′ψ∗),ψ∗)ψ = π(Ψ′ψ∗)τ0 = π(Ψ′ψ∗τ0), as required.

We will prove Lemma 5.4 (with B = R) by induction on r; the proof of the following lemma uses the induction hypothesis.

- Lemma 5.6. Let Φ be an (ω,s′)-extendable Σ-adapted B-complex and B′ ⊆ B, with |B| = r, |B′| = r′, s′ = 3(r − r′)2 and n = |V (Φ)| > n0(r,Γ) large and ω > n−1/2. Suppose B′ ∈ C′ ∈ PΣ and Φ′ ⊆ ΦC′ is such that (Φ,Φ′) is (ω,2)-extendable and Φ[Φ′] is Σ-adapted. Suppose H is a symmetric subgroup of ΓΣ and J ∈ HΦB is null and symmetric. Then there is Ψ ∈ HOB(Φ) with J − ∂Ψ ∈ HΦ[Φ′]B.


Proof. We can assume B′ = ∅, otherwise the lemma holds trivially with Ψ = 0. Let B∗ = B \ B′, Σ′ = {σ ∈ Σ : σ |B′= idB′} and Σ∗ = Σ/B′ = {σ |B∗: σ ∈ Σ′}. Let X = {xC : C ∈ Σ′ \Σ} be a set of representatives of the right cosets of Σ′ in Σ. Then any σ ∈ Σ has a unique representation σ = σ′x with σ′ ∈ Σ′, x ∈ X.

We deﬁne π : (ΓX)Σ∗ → ΓΣ by π(v)σ′x = (vσ∗)x whenever x ∈ X, σ′ ∈ Σ′, σ∗ = σ′ |B∗. Note that for any v ∈ (ΓX)Σ∗, τ′ ∈ Σ′, τ∗ = τ′ |B∗ we have π(vτ∗) = π(v)τ′; indeed, π(vτ∗)σ′x = ((vτ∗)σ∗)x = (vτ∗σ∗)x = π(v)τ′σ′x = (π(v)τ′)σ′x. We let H∗ = {h∗ : π(h∗) ∈ H} and note that H∗ is a symmetric subgroup of (ΓX)Σ∗.

Consider any ψ∗ ∈ ΦB′ \ Φ′. Recall (Lemma 2.18) that Φ∗ = Φ/ψ∗ is Σ∗-adapted. Deﬁne J∗ ∈ (H∗)Φ∗B∗ by ((Jψ/ψ∗ ∗)σ∗)x = (Jψ)σ′x whenever ψ∗ ⊆ ψ ∈ ΦB, x ∈ X and σ∗ = σ′ |B∗ with σ′ ∈ Σ′. Note that π(Jψ/ψ∗ ∗) = Jψ.

We claim that J∗ is symmetric and null. To see this, consider any ψ∗ ⊆ ψ ∈ ΦB, x ∈ X and σ∗ = σ′ |B∗, τ∗ = τ′ |B∗ with σ′,τ′ ∈ Σ′. Then ((Jψ/ψ∗ ∗τ∗)σ∗)x = ((Jψ/ψ∗ ∗)τ∗σ∗)x = (Jψ)τ′σ′x = (Jψτ′)σ′x = (Jψτ′)σ′x = ((Jψτ∗ ′/ψ∗)σ∗)x = ((J(∗ψ/ψ∗)τ∗)σ∗)x, so J∗ is symmetric. Also, for any ψ′/ψ∗ ∈ Φ∗r−r′−1 we have ((∂Jψ∗′/ψ∗)σ∗)x = {((Jψ/ψ∗ ∗)σ∗)x : ψ/ψ∗ ∈ Φ∗B∗ |ψ′/ψ∗} = {(Jψ)σ′x : ψ ∈ Φ |ψ′} = 0, so J∗ is null, as claimed.

∗(Φ∗). For each φ∗ ∈ OB∗(Φ∗) we consider the Φ-extension Eψ

By the inductive hypothesis of Lemma 5.4 we have J∗ = ∂Ψψ∗ for some Ψψ∗ ∈ (H∗)OB

∗

φ∗ = (OB,F,ψ∗ ∪ φ∗), where F = B ∪ V (OB∗). We construct Ψ ∈ HOB(Φ) by letting ψ∗ range over a set of orbit representatives for (ΦB′ \ Φ′)/Σ, letting φ∗ range over OB∗(Φ∗), and adding π(Ψψφ∗∗){φ} to Ψ for some φ ∈ XEψ∗

(Φ,Φ′).

φ∗

To complete the proof, it suﬃces to show that (∂Ψ)ψ = Jψ for any ψ ∈ ΦB with ψ∗Σ ⊆ ψΣ for some representative ψ∗ used in the construction. As ∂Ψ and J are both symmetric, it suﬃces to prove this when ψ∗ ⊆ ψ. As Jψ = π(Jψ/ψ∗ ∗) and Jψ/ψ∗ ∗ = ∂Ψ∗ψ/ψ∗ it suﬃces to show that π(χ(Ψψ

∗

∗

φ∗,φ∗)ψ/ψ∗) = χ(π(Ψψ

φ∗),φ)ψ for any φ∗ and φ as above. Both sides are zero unless ψ(τ′)−1 ∈ φOBB for some τ′ ∈ Σ. Then τ′ ∈ Σ′ as ψ∗ ⊆ ψ. Let τ∗ = τ′ |B∗. Then (ψ/ψ∗)(τ∗)−1 ∈ φ∗OBB∗∗. We have χ(Ψψ

∗

∗

∗

∗

∗

φ∗)τ′ = π(Ψψ

φ∗),φ)ψ = π(Ψψ

φ∗τ∗ and χ(π(Ψψ

φ∗,φ∗)ψ/ψ∗ = Ψψ

φ∗τ∗), as required.

- Proof of Lemma 5.4. We can assume B = R by Lemma 5.5. For the purposes of induction we prove a slightly stronger statement, in which we replace the assumption ω > n−1/2 by the weaker assumption ω > (2r)r5n−0.6. Fix any Φ-embedding ψ0 of OB. Let V0 = Im(ψ0) and τ : V (Φ)\V0 → B be uniformly random. For (i,xi) ∈ V (OB) let τ(ψ0(i,xi)) = i. Let Φτ be the set of φ ∈ Φ with τφ = id. Consider the Φ[Φτ]-extension E0 = (B(3),V (OB),ψ0). For j ∈ [r] we let


Lj = {ψ∗eΣ : ψ∗ ∈ XE0(Φ[Φτ]),e ∈ B(3)B′,B′ ∈ Bj }. The main part of the proof lies in showing that we can reduce the support of J to Φ[Lr]B.

Before doing so, we start by making the support disjoint from V0. We identify B with [r] and for each j ∈ B we let L′j = {ψΣ : ψ ∈ Φj,ψ(j) ∈/ V0}. We deﬁne Φ′j for 0 ≤ j ≤ r by Φ′0 = Φ and Φ′j = Φ′j−1[L′j] for j ∈ [r]. Then Φ′ := Φ′r = Φ[V (Φ) \ V0].

We claim that each (Φ′j−1,L′j) is (ω−O(n−1),s)-extendable. To see this, consider any (Φ′j−1,L′j)extension (E,H′) where E = (H,F,φ) is a Φ′j−1-extension and H′ ⊆ H \ H[F]. Note that if φ∗ ∈ XE(Φ′j−1) with Im(φ∗) ∩ V0 = Im(φ) ∩ V0 then φ∗ ∈ XE(Φ′j−1,L′j). Thus XE(Φ′j−1,L′j) > XE(Φ′j−1) − O(nvE−1). As Φ is (ω,s)-extendable, the claim follows. Now by Lemma 5.6 applied to each (Φ′j−1,Φ′j) successively, there is Ψ′ ∈ HOB(Φ) with J′ = J − ∂Ψ′ ∈ HΦ′B.

Next we will reduce the support of J′ to Φ[Lr]B. We deﬁne Φ0 = Φ′ and Φj = Φj−1[Lj] for j ∈ [r], and show that whp each (Φj−1,Lj) is ((2r)−jrsω,s − 3j)-extendable. We show by induction on j ∈ [r] that any Φj−1-extension E = (H′,F,φ) of rank s − 3j is (2r)−jrsω-dense in (Φj−1,Lj). Note that Φ0 = Φ′ is (ω − O(n−1),s)-extendable, and the induction statement for j implies that Φj is ((2r)−jrsω,s − 3j)-extendable. Thus for the induction step we can assume that Φj−1 is ((2r)−(j−1)rsω − O(n−1),s − 3j + 3)-extendable.

We can assume that H′ ⊆ B([s−3j+3]\[3]). For each e ∈ HB′ ′ with B′ ∈ Bj and e\F = ∅ we ﬁx a B(s−3j +3)-embedding ψe of B(3) such that ψe is the identity on OB, e = ψee′ where e′ ∈ B(3)B′ with e′(x) = (x,3) for all x ∈ B′, and ψe is otherwise disjoint from H′, i.e. ψe(V (B(3))) ∩ V (H′) = Im(e).

Let E+ = (H+,F+,φ+), where H+ = H′ ∪ {ψee′ : e ∈ HB′ ′,B′ ∈ Bj ,e′ ∈ B(3)}, F+ =

- F ∪ V (OB) and φ+ restricts to φ on F and ψ0 on V (OB). We claim that φ+ is a Φj−1-embedding


of H+[F+]. To see this, consider any f ∈ H+[F+] with |Im(f)| = i < j, and write f = f1 ∪ f2, where Im(f1) ⊆ F and f2 ∈ OB. As φ is a Φj−1-embedding of H′[F], we have φf1 = ψ1e1σ for some ψ1 ∈ XE0(Φ[Φτ]), σ ∈ Σ, e1 ∈ B(3). Then φ+f = ψ1(e1 ∪ f2σ−1)σ, so φ+f ∈ Li, which proves the claim. Thus E+ is a Φj−1-extension.

Let X be the number of φ∗ ∈ XE+(Φj−1) such that τ(φ∗(i,xi)) = i for all (i,xi) ∈ V (H+) \ F+. Then XE(Φj−1,Lj) ≥ XnvE−vE+ by construction of E+. As Φj−1 is ((2r)−(j−1)rsω − O(n−1),s − 3j + 3)-extendable, we have XE+(Φj−1) ≥ (2r)−(j−1)rsωnvE+ − O(nvE−1), so EXE(Φj−1,Lj) ≥ r−vE+(2r)−(j−1)rsωnvE − O(nvE−1). Changing any value of τ aﬀects XE(Φj−1,Lj) by O(nvE−1), so by Lemma 3.5 whp XE(Φj−1,Lj) ≥ (2r)−jrsωnvE. This completes the induction step, so each (Φj−1,Lj) is ((2r)−jrsω,s − 3j)-extendable.

Now by Lemma 5.6 repeatedly applied to each (Φj−1,Φj) successively, always with s′ ≥ s −3r ≥

- 3(r − 1)2 and extendability parameter ω′ > (2r)−3r4(2r)r5n−0.6 > (2(r − 1))(r−1)5n−0.6, there is Ψ0 ∈ HOB(Φ) with J0 = J′ − ∂Ψ0 ∈ HΦ[Lr]B. We will deﬁne null J1,... ,Jr ∈ HΦ[Lr]B such that Jψj = 0 whenever |Im(ψ) ∩ V0| < j, via the following construction of ‘reducing octahedra’.


Let L∗ be the set of e ∈ Lr with Im(e) \ V0 = ∅ such that e = ψ0ef0e for some ψ0e ∈ XE0(Φ[Φτ]) and f0e ∈ B(3)B (i.e. we can take σ = id in the deﬁnition of Lr). For each e ∈ L∗ we ﬁx some Φ-embedding ψe of OB of the form ψe = ψ0e |Fe πe, where f1e ∈ OB and πeOB is the copy of OB in B(3) spanned by Fe := Im(f0e) ∪ Im(f1e), identiﬁed so that f0e has sign 1. Note that for any e′ ∈ ψeOBB with e′ = e we have |Im(e′) ∩ V0| > |Im(e) ∩ V0| and e′ ∈ Lr. We deﬁne J1 = J0 − ∂Ψ1, where Ψ1 = e∈L∗ Je0{ψe}. As J0 and each χ(Je0,ψe) are symmetric, we have Jψ1 = 0 whenever Im(ψ) ∩ V0 = ∅.

Given Jj with 0 < j < r, we deﬁne Jj+1 as follows. Consider any f ∈ Φ◦r−j disjoint from V0, write B′ = τ(f) ⊆ B, and suppose f = Im(ψ∗), where ψ∗ ∈ ΦB′ with τψ∗ = id. For any ψ ∈ ΦB with Jψj = 0 and ψ∗Σ ⊆ ψΣ, by deﬁnition of Lr we can pick a representative ψ of ψΣ with ψ∗ ⊆ ψ and τψ = id. Furthermore, for any x ∈ B \ B′ and ψ′ ∈ ΦB−x with ψ∗ ⊆ ψ′ and τψ′ = id, if there is ψ′ ⊆ ψ with Jψj = 0 then there are exactly two such ψ, say ψ±, obtained from each other by interchanging ψ0((x,0)) and ψ0((x,1)), where as Jj is null we have Jψj− = −Jψj+. Thus there is af ∈ H such that Jψj = ±af whenever ψ∗ ⊆ ψ and τψ = id, where the sign is that of ψ0−1ψ |B\B′ in OB\B′. Fix e with ψ∗ ⊆ e, τe = id, Jej = af. By symmetry, we have Jψj = χ(af,ψe)ψ whenever Jψj = 0 with ψ∗Σ ⊆ ψΣ. We add af{ψe} to Ψj+1 for each such f, e and let Jj+1 = Jj − ∂Ψj+1.

We conclude with Jr such that Jer is zero unless e ∈ ψ0OBBΣ. As Jr is symmetric and null, we have Jr = χ(a,ψ0) for some a ∈ H. Then Ψ := Ψ′ + a{ψ0} + rj=0 Ψj has ∂Ψ = J.

Next we give two quantitative versions of Lemma 5.4. These will be used in the next subsection to prove two quantitative versions of the main lemma of this section, which will in turn both be used in the proof of Lemma 3.18 in the next section. We make the following deﬁnitions.

- Deﬁnition 5.7. (G-use) Suppose H is a symmetric subgroup of ΓΣ and G is a symmetric generating set of H. For v ∈ Γ we write |v|G for the minimum possible g∈G |cg| where v = g∈G cgg with all cg ∈ Z. For Ψ ∈ HOB(Φ) we write |Ψ|G = |Ψφ|G. If J ∈ HΦB is symmetric we write |J|G = ′ψ |Jψ|G, where the sum is over any choice of orbit representatives for ΦB/Σ.


The following lemma quantiﬁes the total ‘G-use’ of the octahedral decomposition Ψ in terms of that of J. We deﬁne C(i) = 2(9i+2)i+5.

- Lemma 5.8. Let Φ be an (ω,s)-extendable Σ-adapted B-complex with |B| = r, s = 3r2, n = |V (Φ)| > n0(r,Γ) large and ω > n−1/2. Suppose H is a symmetric subgroup of ΓΣ and G is a


symmetric generating set of H. Suppose J ∈ HΦB is symmetric and null. Then there is Ψ ∈ HOB(Φ) with ∂Ψ = J such that |Ψ|G ≤ C(r)|J|G.

Following the proof of Lemma 5.4, we quantify the total G-use in Lemma 5.6.

- Lemma 5.9. In Lemma 5.6, we can choose Ψ with |Ψ|G ≤ C(r − r′)|J|G and |J − ∂Ψ|G ≤ 2rC(r − r′)|J|G.


The proof of Lemma 5.9 is the same as that of Lemma 5.6, noting also that when we apply the inductive hypothesis each |Ψψ∗|G ≤ C(r − r′)|J∗|G, so |Ψ|G ≤ C(r − r′)|J|G, and this also gives |J − ∂Ψ|G ≤ 2rC(r − r′)|J|G.

Proof of Lemma 5.8. We will estimate the total G-use during the proof of Lemma 5.4. We write Ψ′ = rj=1 Ψ′j, J′0 = J and J′j = J′j−1 − ∂Ψ′j for j > 0, so J′r = J′. By Lemma 5.9 each |Ψ′j|G ≤ C(r − 1)|J′j−1|G and |J′j|G ≤ 2rC(r − 1)|J′j−1|G, so |J′|G ≤ 2r2C(r − 1)r|J|G.

Similarly, we write Ψ0 = rj=1 Ψ0,j, J00 = J′ and J0,j = J0,j−1 − ∂Ψ0,j for j > 0. Then J0r = J0, and each Φj = Φj−1[Lj] is obtained by repeated restriction to each LjB′ with B′ ∈ Bj , so writing rj = rj we have |Ψ0,j|G ≤ C(r − j)rj|J0,j−1|G, and |J0,j|G ≤ (2rC(r − j))rj|J0,j−1|G, so |J0|G ≤ 2r2r|J′|G i r=0−1 C(i)ri.

Next we have |Ψ1|G ≤ |J0|G and |J1|G ≤ 2r|J0|G. For j > 0 we have |Ψj+1|G ≤ |Jj|G and |Jj+1|G ≤ 2r|Jj|G, so |Ψr|G ≤ 2r2|J0|G ≤ 2r2r+2r2|J|GC(r − 1)2r i r=0−2 C(i)ri. Recalling C(i) = 2(9i+2)i+5, we see that Ψ := Ψ′ + a{ψ0} + rj=0 Ψj has |Ψ|G < C(r)|J|G.

In our second quantitative version, we suppose Γ = ZD is free, and consider rational decompositions, where we now bound G-uses on every function in Φr (as opposed to the total bound in the previous version).

- Deﬁnition 5.10. Suppose H is a symmetric subgroup of (ZD)Σ and G is a symmetric generating set of H. For v ∈ QH we write |v|G for the minimum possible g∈G |cg| where v = g∈G cgg with all cg ∈ Q. For Ψ ∈ (QH)OB(Φ) and ψ ∈ ΦB we write UG(Ψ)ψ = {|Ψφ|G : ψ = φψ′,ψ′ ∈ OBB}.


- Lemma 5.11. Let Φ be an (ω,s)-extendable Σ-adapted B-complex where n = |V (Φ)| > n0(r,Γ) is large, |B| = r, n−1/2 < ω < ω0(r) and s = 3r2. Suppose H is a symmetric subgroup of (ZD)Σ and

G is a symmetric generating set of H. Suppose J ∈ (QH)ΦB is symmetric and null with |Jψ|G ≤ θ for all ψ ∈ ΦB. Then there is Ψ ∈ (QH)OB(Φ) with ∂Ψ = J such that UG(Ψ)ψ ≤ C(r,ω)θ for all ψ ∈ ΦB, where C(i,ω) = 2C(i)ω−(9i)i+4.

Again we require the corresponding quantitative version of Lemma 5.6.

- Lemma 5.12. Let Φ be an (ω,s′)-extendable Σ-adapted B-complex and B′ ⊆ B, with |B| = r, |B′| = r′, s′ = 3(r′)2, n = |V (Φ)| > n0(r,Γ) large and n−1/2 < ω < ω0(r). Suppose B′ ∈ X ∈ PΣ and Φ′ ⊆ ΦX is such that (Φ,Φ′) is (ω,2)-extendable and Φ[Φ′] is Σ-adapted. Suppose H is a symmetric subgroup of (ZD)Σ and G is a symmetric generating set of H. Suppose J ∈ (QH)ΦB is


symmetric and null with all |Jψ|G ≤ θ. Then there is Ψ ∈ (QH)OB(Φ) with J −∂Ψ ∈ (QH)Φ[Φ′]B such that for all ψ ∈ ΦB both UG(Ψ)ψ and |(J − ∂Ψ)ψ|G are at most 2rω−1C′θ, where C′ = C(r − r′,ω).

Proof. We follow the proof of Lemma 5.6. For each ψ∗ ∈ ΦB′ \ Φ′, we deﬁne Φ∗, J∗, Ψψ∗ as before, where by the inductive hypothesis of Lemma 5.11 there is Ψψ∗ ∈ (QH∗)OB

∗(Φ∗) with ∂Ψψ∗ = J∗

and all UG∗(Ψψ∗)ψ/ψ∗ ≤ C′θ, where G∗ = {h∗ ∈ H∗ : π(h∗) ∈ G}. For each orbit representative ψ∗ and φ∗ ∈ OB∗(Φ∗) we add π(Ψψφ∗∗)E{φ} to Ψ, where φ is uniformly random in XEψ∗

(Φ,Φ′). Then J − ∂Ψ ∈ (QH)Φ[Φ′]B as in the proof of Lemma 5.6.

φ∗

For any ψ ∈ ΦB we have UG(Ψ)ψ ≤ ψ∗∈ΦB′\Φ′ φ∗∈OB∗(Φ∗) |Ψψφ∗∗|G∗ ψB∈OBB P(ψ = φψB), where φ is as above. Note that any given ψB can only contribute to UG(Ψ)ψ if ψ(x) = φ∗ψB(x) for all x ∈ B∗ and ψ(x) = ψ∗(x) for all x ∈ B′ \ D, where D = D(ψB) = {x ∈ B′ : ψB(x) = (x,2)}.

For each ψ′ ∈ SD := {ψ′ ∈ ΦB : ψ′ |B\D= ψ |B\D} and ψ∗ = ψ′ |B′ we have P(ψ = φψB) < ω−1n−|D|, as (Φ,Φ′) is (ω,2)-extendable. We have |SD| < n|D| and all |Ψψ

∗

φ∗|G∗ ≤ C′θ, so summing over ψB and ψ′ ∈ SD(ψB) gives UG(Ψ)ψ ≤ 2rω−1C′θ. The same bound applies to |(J − ∂Ψ)ψ|G.

- Proof of Lemma 5.11. We follow the proof of Lemma 5.4, estimating uses of any ﬁxed ψ ∈ ΦB, and then average over all choices of the initial Φ-embedding ψ0 of OB. We use the same notation as in the proofs of Lemmas 5.4 and 5.8.


Letting θ0′ = θ, and θj′ for j > 0 be such that all |J′jψ|G ≤ θj′, by Lemma 5.12, for each j > 0 both UG(Ψ′j)ψ and |J′jψ|G are at most 2r−1(ω − O(n−1))−1C(r − 1,ω − O(n−1))θj′−1, so we can deﬁne θj′ = 2rω−1C(r − 1,ω)θj′−1. Then both UG(Ψ′)ψ and |Jψ′ |G are at most 2θr′ .

Similarly, letting θ0 = 2θr′ and θj for j > 0 be such that all |Jψ0,j|G ≤ θj, by Lemma 5.12, for each j > 0 both UG(Ψ0,j)ψ and |Jψ0,j|G are at most 2θj−1[2r−j((2r)−jrsω)−1C(r − j,(2r)−jrsω)]rj, so we can deﬁne θj = θj−1[2r((2r)−jrsω)−1C(r −j,(2r)−jrsω)]rj. Then UG(Ψ0)ψ and |Jψ0|G are at most θ∗ := 2θr′ (2rω−1(2r)sr2)2r i r=0−1 C(i,(2r)−sr2ω)ri.

Now write B′ = {x : ψ(x) ∈/ V0} and ψ′ = ψ |B′. For 0 ≤ j < r − |B′| we have UG(Ψj+1)ψ′ ≤ 2r|(Jj |ψ′)|G, so r−|B

′|

j=1 UG(Ψj)ψ ≤ 2r2|(J0 |ψ′)|G ≤ 2r2θ∗nr−|B′|.

Letting Ψ be the average of Ψ (from the proof of Lemma 5.4) over all Φ-embeddings ψ0 of OB, as Φ is (ω,2)-extendable, UG(Ψ)ψ ≤ 2r2+1θ∗ B′⊆B n2r−(r−|B′|)(ωn2r)−1nr−|B′| < 2(r+1)2ω−1θ∗ < C(r,ω)θ, for ω < ω0(r), using s = 3r2, C(i,ω) = 2C(i)ω−(9i)i+4 and C(i) = 2(9i+2)i+5.

![image 16](<2018-keevash-existence-designs_images/imageFile16.png>)

![image 17](<2018-keevash-existence-designs_images/imageFile17.png>)

## 5.2 Lattices

In this subsection we use the octahedral decompositions from the previous subsection to characterise the decomposition lattice γ(Φ) . For the following lemma, we recall (Lemma 2.32) that γ(Φ) ⊆ L−γ (Φ). We will show that if Φ is extendable then this inclusion becomes an equality when we restrict to null vectors.

- Lemma 5.13. Let Σ ≤ Sq, A be a Σ≤-family and γ ∈ (ZD)Ar. Let Φ be a Σ-adapted (ω,s)-extendable [q]-complex with s = 3r2, n = |V (Φ)| > n0(q,D) large and ω > n−1/2. Suppose B ∈ C ∈ PrΣ and J ∈ L−γ (Φ) ∩ (ZD)ΦC is null. Then J ∈ γ(Φ) .


Proof. Recall (Lemma 2.34) that fB(J) ∈ (γB)ΦB is symmetric, and (Lemma 2.30) that γB is symmetric. We also note that fB(J) is null, as for any ψ′ ∈ ΦB′ with B′ ⊆ B, |B′| = r − 1 and σ ∈ ΣB we have (∂fB(J)ψ′)σ = {(fB(J)ψ)σ : ψ′ ⊆ ψ} = {Jψσ : ψ′ ⊆ ψ} = ∂Jψ′σ = 0. By

- Lemma 5.4 we have Ψ ∈ (γB)OB(Φ) with fB(J) = ∂Ψ = ψ∗ χ(Ψψ∗,ψ∗). By deﬁnition of γB we can


mθψ∗γθ.

ﬁx integers mθψ∗ so that each Ψψ∗ = θ∈A

B

We will show for any ψ∗ ∈ OB(Φ) and θ ∈ AB that there is Ψψ∗θ ∈ ZA(Φ) with fB(∂γΨψ∗θ) = χ(γθ,ψ∗). This will suﬃce to prove the lemma. Indeed, letting Ψ∗ = ψ∗,θ mθψ∗Ψψ∗θ, we will have

∂γΨ∗ = ψ∗,θ mθψ∗χ(γθ,ψ∗) = ψ∗ χ(Ψψ∗,ψ∗) = ∂Ψ = J.

Consider ψ∗ ∈ OB(Φ), A ∈ A, θ ∈ AB, let F = θ(B) × [2] and deﬁne ψ0 : F → V (Φ) by ψ0(θ(i),x) = ψ∗(i,x) for i ∈ B, x ∈ [2]. We claim that ψ0 ∈ Oθ(B)(Φ), and so E = ([q](2),F,ψ0) is a Φ-extension. To see this, note that for any υ ∈ Oθθ((BB)), deﬁning υ′ ∈ OBB such that υ′(i) = (i,x) when υ(θ(i)) = (θ(i),x), as ψ∗ ∈ OB(Φ) we have ψ0υθ = ψ∗υ′ ∈ ΦB. As Φ is Σ-adapted, we deduce ψ0υ ∈ Φθ(B), which proves the claim.

As Φ is (ω,s)-extendable, we can choose ψ+ ∈ XE(Φ). We let Ψψ∗θ be the sum of all ±{ψ+ ◦ φ} over all A(2)-embeddings φ of A such that φ(i) = (i,1) when i ∈/ θ(B), where the sign is that of φ |θ(B) in Oθ(B), i.e. that of ψ′ ∈ OB deﬁned by ψ′ = (ψ∗)−1ψ, where ψ = ψ0φθ with ψ0

- as above. Then all entries in ∂γΨψ∗θ cancel in ± pairs, except that for each ±{ψ+ ◦ φ} in Ψψ∗θ there is a non-cancelling term γ(ψ+φ)ψΣ = γ[ψ]θ (by Lemma 2.24.i) as ψ = ψ0φθ = ψ+φθ. Now fB(γ[ψ]θ)ψ = ±γθ = χ(γθ,ψ∗)ψ, where the sign is that of ψ′ = (ψ∗)−1ψ ∈ OB, so by symmetry fB(∂γΨψ∗θ) = χ(γθ,ψ∗), as required to prove the lemma.


To motivate the characterisation of decomposition lattices in general, it may be helpful to consider the decomposition lattice of triangles in a complete tripartite graph (a very special case of Theorem 1.7). Say T is a complete tripartite graph with parts (A,B,C). It is not hard to show that J ∈ ZT is in the decomposition lattice iﬀ J is ‘balanced’, in that each a ∈ A has b∈B Jab = c∈C Jac and similarly for each b ∈ B and c ∈ C. At ﬁrst sight this seems a rather diﬀerent condition to the tridivisibility condition that arises for nonpartite triangle decomposition (even degrees and 3 | J). However, we can unify the conditions by lifting J to a vector J+ ∈ (Z3)T in which we assign diﬀerent basis vectors to the three bipartite subgraphs, say (1,0,0) to (B,C), (0,1,0) to (A,C) and (0,0,1) to (A,B). We want to characterise when J+ is in the lattice generated by all vectors v(abc) ∈ (Z3)T, where for a ∈ A, b ∈ B, c ∈ C we let v(abc)bc = (1,0,0), v(abc)ac = (0,1,0), v(abc)ab = (0,0,1) and v(abc)xy = 0 otherwise. The lifted vertex degree condition is that for any a ∈ A we have

x∈V (T) Jax+ in the lattice generated by (0,1,0) and (0,0,1), and similarly for any b ∈ B and c ∈ C; this is equivalent to J being balanced. This example suggests the form of the degree conditions in the following deﬁnition.

- Deﬁnition 5.14. Let Φ be a [q]-complex, A be a [q]-complex family and γ ∈ (ZD)Ar. For J ∈ (ZD)Φr we deﬁne J♯ ∈ ((ZD)Q)Φ by (Jψ♯′)B = {Jψ : ψ′ ⊆ ψ ∈ ΦB} for B ∈ Q, ψ′ ∈ Φ. Similarly, we deﬁne

γ♯ ∈ ((ZD)Q)∪A by (γθ♯′)B = {γθ : θ′ ⊆ θ ∈ AB} for B ∈ Q, θ′ ∈ A ∈ A. We let Lγ(Φ) be the set of all J ∈ (ZD)Φr such that (J♯)O ∈ γ♯[O] for any O ∈ Φ/Σ.

Note that γ♯ = (γi♯ : 0 ≤ i ≤ r) where each γi♯ is a vector system for Ai. For convenient use in Lemma 5.19 we will reformulate Deﬁnition 5.14 in terms of iterated independent shadows, in the sense of the following deﬁnition.

- Deﬁnition 5.15. (independent shadows)


For each B ∈ [q]i and any set S we deﬁne πB : ZS → Z[q]i×S by πB(v) = eB ⊗ v, i.e. πB(v) is v in the block of S coordinates belonging to B and 0 otherwise.

Let Φ be a [q]-complex. We deﬁne πi : (ZS)Φi → (Z[q]i×S)Φi by πi(J)ψ = πB(Jψ) for ψ ∈ ΦB,

- B ∈ [q]i. We also write J+ = πi(J) for J ∈ (ZS)Φi. For i = r,... ,0 we deﬁne Di by Dr = [q]r × [D] and Di = [q]i × Di+1 for 0 ≤ i < r. For


J ∈ (ZDi+1)Φi+1 we deﬁne ∂∗J ∈ (ZDi)Φi by ∂∗J = πi(∂iJ) = (∂J)+. For J ∈ (ZD)Φr and 0 ≤ i ≤ r we deﬁne ∂i∗J = (∂∗)r−i(J+).

Similarly, given a [q]-complex family A and γ ∈ (ZD)Ar we deﬁne ∂i∗γ = (∂∗)r−i(πr(γ)), where for γ′ ∈ (ZDi+1)Ai+1 and θ′ ∈ A ∈ A we deﬁne (∂γ′)θ′ = {γθ′ : θ ∈ A |θ′} and (∂∗γ′)θ′ = πi((∂γ′)θ′).

We let Liγ(Φ) be the set of all J ∈ (ZD)Φr such that ∂i∗J ∈ L−∂i∗γ(Φ), i.e. (∂i∗J)O ∈ (∂i∗γ)[O] for any O ∈ Φi/Σ. Remark 5.16. Unravelling the iterative deﬁnitions in Deﬁnition 5.15, we see that each Di = [D] ×

r j=i[q]j, and for each Bi ∈ [q]i, ψi ∈ ΦBi, we have (∂i∗J)ψi supported on ‘full chains from Bi’, i.e.

if ((∂i∗J)ψi)C = 0 then C = (Bi,... ,Br) with each Bj ∈ [q]j and Bj ⊆ Bj+1 for i ≤ j < r.

We obtain ((∂i∗J)ψi)C ∈ ZD by summing Jψr over all choices of (ψi,... ,ψr) with each ψj ∈ ΦBj and ψj ⊆ ψj+1 for i ≤ j < r.

Similarly, for A ∈ A, θi ∈ ABi we obtain ((∂i∗γ)θi)C ∈ ZD by summing γθr over all choices of (θi,... ,θr) with each θj ∈ ABj and θj ⊆ θj+1 for i ≤ j < r.

Now we reformulate Deﬁnition 5.14 using Deﬁnition 5.15.

- Lemma 5.17. Lγ(Φ) = ∩ri=0Liγ(Φ).

Proof. Fix ψO ∈ O ∈ Φi/Σ, say with ψO ∈ ΦB′. We need to show (J♯)O ∈ γ♯[O] iﬀ (∂i∗J)O ∈ (∂i∗γ)[O] . We have (J♯)O ∈ γ♯[O] iﬀ there is n ∈ ZAB′ with (J♯)O = σ{nσγ♯(ψOσ−1)}, i.e. all Jψ♯Oσ′ =

σ{nσγσσ♯ ′}, i.e. for each A ∈ A, σ′ ∈ A[B′], B ∈ Q we have {Jψ : ψOσ′ ⊆ ψ ∈ ΦB} = σ,θ{nσγθ : σσ′ ⊆ θ ∈ AB}.

We have (∂i∗J)O ∈ (∂i∗γ)[O] iﬀ there is n′ ∈ ZAB′ such that for each A ∈ A, σ′ ∈ A[B′] and chain C = (Bi,... ,Br) from Bi = B′ to Br = B ∈ Q, we have ψi,...,ψr Jψr = σ,θi,...,θr n′σγθr, where we sum over (θi,... ,θr) and (ψi,... ,ψr) with θi = σσ′, ψi = ψOσ′, each θj ∈ ABj, ψj ∈ ΦBj, and each θj ⊆ θj+1, ψj ⊆ ψj+1.

Setting n′ = n we see that the two conditions are identical, as any such chain C and σ′,σ uniquely speciﬁes all ψj = ψr |Bj and θj = θr |Bj.

Our next lemma shows that the two deﬁnitions of ∂i∗ (for vectors and for vector systems) are compatible with each other.

- Lemma 5.18. If Ψ ∈ ZA(Φ) then ∂∂i∗γΨ = ∂i∗(∂γΨ).

Proof. By linearity we can assume Ψ = {φ} for some φ ∈ A(Φ). We prove the identity by induction on i = r,... ,0. In the base case i = r we have ∂∂r∗γΨ = (∂r∗γ)(φ) = (πrγ)(φ) = πr(γ(φ)) = ∂r∗(∂γΨ), where in the third equality we used (πrγ)(φ)φθ = (πrγ)θ = πr(γθ) = πr(γ(φ)φθ). For the induction step with i < r we have ∂∂i∗γΨ = (∂i∗γ)(φ) = (∂∗∂i∗+1γ)(φ) = ∂∗(∂i∗+1γ)(φ) = ∂∗∂∂i∗+1γΨ = ∂∗∂i∗+1(∂γΨ) = ∂i∗(∂γΨ), where in the third equality, writing γ′ = ∂i∗+1γ, for θ′ ∈ A ∈ A we used (∂∗γ′)(φ)φθ′ = (∂∗γ′)θ = πi {γθ′ : θ ∈ A |θ′} = πi {γθ′ : φθ ∈ Φ |φθ′} = ∂∗(γ′(φ)φθ′).

Now we come to the main lemma of this section, which characterises the decomposition lattice.

- Lemma 5.19. Let Σ ≤ Sq, A be a Σ≤-family and γ ∈ (ZD)Ar. Let Φ be a Σ-adapted (ω,s)-extendable [q]-complex with s = 3r2, n = |V (Φ)| > n0(q,D) large and ω > n−1/2. Then γ(Φ) = Lγ(Φ).


Proof. Note for any molecule γ(φ) ∈ γ(Φ) that (∂i∗γ)(φ) ∈ (∂i∗γ)(Φ) ⊆ L−∂i∗γ(Φ), so γ(Φ) ⊆ Liγ(Φ). We now show that the reverse inclusions hold. Suppose J ∈ Lγ(Φ). We will deﬁne Ψ0,... ,Ψr ∈ ZA(Φ)

so that, letting J0 = J − ∂γΨ0 and Ji = Ji−1 − ∂γΨi for i ∈ [r], each ∂i∗Ji = 0. We will then have Jr = 0, so J = ri=0 ∂γΨi ∈ γ(Φ) , as required.

We start by noting that12 ∂0∗J∅ ∈ (∂0∗γ)∅ as J ∈ L0(Φ), so we have integers kA with ∂0∗J∅ =

- A∈A kA(∂0∗γ)∅A. We can take Ψ0 = A∈A kA{φA} for any choices of φA ∈ A(Φ). Then J0 =


J − ∂γΨ0 has ∂0∗J0 = 0. It remains to deﬁne Ψi given Ji−1 for some i ∈ [r].

Note that Ji−1 ∈ Liγ(Φ) as J ∈ Liγ(Φ) and γ(Φ) ⊆ Liγ(Φ), so ∂i∗Ji−1 ∈ L−∂i∗γ(Φ). We write ∂i∗Ji−1 = C∈PΣ

JC, where each JC is uniquely deﬁned by JψC = ∂i∗Jψi−1 for ψ ∈ ΦC. We claim that each JC is null. Indeed, for any ψ ∈ Φi−1 we have 0 = ∂i∗−1Jψi−1 = (∂∂i∗Ji−1)+ψ = C(∂JC)+ψ, so by linear independence each (∂JC)ψ = 0, as claimed.

i

By Lemma 5.13 each JC ∈ (∂i∗γ)(Φ) , so we have Ψi ∈ ZA(Φ) with ∂∂i∗γΨi = ∂i∗Ji−1. Letting Ji = Ji−1 − ∂γΨi, by Lemma 5.18 we have ∂i∗Ji = 0, as required.

To illustrate the use of Lemma 5.19, we give the following characterisation of the decomposition lattice for nonpartite hypergraph decomposition, thus giving an independent proof of (a generalisation of) a result of Wilson [35] (a similar generalisation is implicit in [9]).

- Lemma 5.20. Let H be an r-graph on [q] and Φ be an (ω,s)-extendable Sq-adapted [q]-complex where n = |V (Φ)| > n0(q) is large, s = 3r2 and ω > n−1/2. Let H(Φ) = {φ(H) : φ ∈ Φq}. Suppose

- G ∈ NΦ◦r. Then G ∈ H(Φ) iﬀ G is H-divisible.


Proof. As in example i in subsection 2.4, we have G ∈ H(Φ) iﬀ G∗ ∈ γ(Φ) , with G∗ ∈ NΦr deﬁned by G∗ψ = GIm(ψ) for ψ ∈ Φr, and γ ∈ {0,1}Ar with A = Sq≤ and γθ = 1Im(θ)∈H. By Lemma 5.19 we have γ(Φ) = Lγ(Φ). By Deﬁnition 5.14 we need to show that G is H-divisible iﬀ ((G∗)♯)O ∈ γ♯[O] for any O ∈ Φ/Sq.

Fix any O ∈ Φ/Sq, write e = Im(O) ∈ Φ◦ and i = |e|. Then ((G∗)♯)O ∈ (ZQ)O = ZQ×O is a vector supported on the coordinates (B,ψ′) with B′ ⊆ B ∈ Q and ψ′ ∈ O ∩ ΦB′ in which every nonzero coordinate is equal: we have ((G∗)♯ψ′)B) = {G∗ψ : ψ′ ⊆ ψ ∈ ΦB} = (r−i)!|G(e)|. Similarly,

γ♯[O] is generated by vectors with the same support that are constant on the support, where the constant can be (r − i)!|H(f)| for any f ∈ [q]i, and so any multiple of (r − i)!gcdi(H). Therefore ((G∗)♯)O ∈ γ♯[O] iﬀ gcdi(H) divides |G(e)|, as required.

For the proof of Lemma 3.18 in the next section, we also require two quantitative versions of

- Lemma 5.19, analogous to those given above for Lemma 5.4. We recall the notation for G-use from


- Deﬁnition 5.7, and for B ∈ Q ﬁx the symmetric generating set G = GB = {γθ : θ ∈ AB} for γB. Then we have the following relationship between G-use and use in the sense of Deﬁnition 3.13.


- Lemma 5.21. Suppose B ∈ C ∈ PrΣ and J ∈ L−γ (Φ) ∩ (ZD)ΦC. Then U(JO) = |fB(JO)|G for each O ∈ Φr/Σ, so U(J)∅ = |fB(J)|G. Proof. We ﬁx an orbit representative ψ ∈ O and write U(JO) as the minimum possible value of


{|xθψ|} over all expressions of JO = {xθψγ[ψ]θ} as a Z-linear combination of γ-atoms at O. We can write any such expression using some ﬁxed representative ψ ∈ ΦB; then fB(JO)ψ = θ xθψγθ. As |fB(JO)|G is the minimum value of {|xθψ|} over all such expressions the lemma follows.

Our ﬁrst quantitative version of Lemma 5.19 will bound the total use U(Ψ) of atoms by Ψ in

terms of that by J, where U(Ψ) = φ |Ψφ|U(γ(φ)) ≤ q2r|Ψ|, where |Ψ| = φ |Ψφ|. We start by stating the analogous statement for Lemma 5.13.

![image 18](<2018-keevash-existence-designs_images/imageFile18.png>)

12 Recall that ∅ may denote the empty set or the function with empty domain. We write ∅A for the copy of ∅ in A.

- Lemma 5.22. Let Σ ≤ Sq, A be a Σ≤-family and γ ∈ (ZD)Ar. Let Φ be a Σ-adapted (ω,s)-extendable [q]-complex with s = 3r2, n = |V (Φ)| > n0(q,D) large and ω > n−1/2. Suppose B ∈ C ∈ PrΣ and J ∈ L−γ (Φ)∩(ZD)ΦC is null. Then there is Ψ∗ ∈ ZA(Φ) with ∂γΨ∗ = J and U(Ψ∗) ≤ 2rq2rC(r)U(J).

The proof of Lemma 5.22 is the same as that of Lemma 5.13. When we apply Lemma 5.8 to fB(J) ∈ (γB)ΦB we obtain Ψ ∈ (γB)OB(Φ) with fB(J) = ∂Ψ and |Ψ|G ≤ C(r)|fB(J)|G. We write each Ψψ∗ = θ∈A

B

mθψ∗γθ with θ∈A

B

|mθψ∗| = |Ψψ∗|G. Deﬁning Ψ∗ as in the proof of Lemma 5.13, we have |Ψ∗| ≤ 2r|Ψ|G ≤ 2rC(r)|fB(J)|G, so U(Ψ∗) ≤ 2rq2rC(r)U(J) by Lemma 5.21.

- Lemma 5.23. Let Σ ≤ Sq, A be a Σ≤-family with γ ∈ (ZD)Ar. Let Φ be a Σ-adapted (ω,s)extendable [q]-complex with s = 3r2, n = |V (Φ)| > n0(q,D) large and ω > n−1/2. Suppose J ∈ Lγ(Φ). Then there is Ψ ∈ ZA(Φ) with ∂γΨ = J and U(Ψ) ≤ 2(9q)q+2U(J).

Proof. We follow the proof of Lemma 5.19. We can choose the kA so that U(Ψ0) = |kA| ≤ U(J) and U(J0) ≤ q2rU(J). For each i ∈ [r], by Lemma 5.22 we can take U(Ψi) ≤ 2iq2iC(i)U(∂i∗Ji−1) ≤ (2rq2)iC(i)U(Ji−1), and so U(Ji) ≤ q2r(2r)iC(i)U(Ji−1), where U(∂i∗Ji−1) is deﬁned with respect to (∂i∗γ)-atoms. Then U(Ψ) ≤ 2U(J0) i q2r2r+iC(i) ≤ 2(9q)q+2U(J), as C(i) = 2(9i+2)i+5.

Our second quantitative version of Lemma 5.19 is analogous to Lemma 5.11: we seek a rational decomposition Ψ for which we bound the usage of every orbit in terms of that in J. We start with the analogous statement for Lemma 5.13.

- Lemma 5.24. Let Σ ≤ Sq, A be a Σ≤-family and γ ∈ (ZD)Ar. Let Φ be a Σ-adapted (ω,s)extendable [q]-complex with s = 3r2, n = |V (Φ)| > n0(q,D) large and ω > n−1/2. Suppose C ∈ PrΣ and J ∈ QL−γ (Φ) ∩ (QD)ΦC is null with U(J)ψ ≤ ε for all ψ ∈ ΦB. Then there is Ψ∗ ∈ QA(Φ) with ∂γΨ∗ = J and U(Ψ∗)O ≤ q2rC(r,ω)ω−1ε for each orbit O ∈ Φr/Σ.

Proof. We follow the proof of Lemma 5.13. Applying Lemma 5.11 to fB(J) ∈ (QγB)ΦB gives Ψ ∈ (QγB)OB(Φ) with fB(J) = ∂Ψ and UG(Ψ)ψ ≤ C(r,ω)ε for all ψ ∈ ΦB. We write each Ψψ∗ =

θ∈AB mθψ∗γθ with θ∈A

B

|mθψ∗| = |Ψψ∗|G.

We let Ψ∗ = ψ∗,θ mθψ∗Ψψ∗θ, where we modify the deﬁnition of each Ψψ∗θ by averaging over the choice of ψ+ ∈ XE(Φ). To estimate U(Ψ∗)O for some O ∈ Φr/Σ we ﬁx any representative ψ′ ∈ O, say with ψ′ ∈ ΦB′. For each A ∈ A, θ ∈ AB, writing r′ = |θ(B) \ B′|, there are at most nr′ choices of ψ ∈ ΦB such that ψθ−1 agrees with ψ′ on θ(B) ∩ B′ and each has UG(Ψ)ψ ≤ C(r,ω)ε. For each ψ∗ ∈ OB(Φ) with ψ = ψ∗υ for some υ ∈ OBB, letting φ be the A(2)-embedding of A such that φ(i) = (i,1) for i ∈/ θ(B) and φ(i) = (i,x) when i = θ(j) with j ∈ B and υ(j) = (j,x), for uniformly random ψ+ ∈ XE(Φ) we have P(ψ′ ⊆ ψ+φ) < ω−1n−r′, as Φ is (ω,s)-extendable. Summing over ψ′ and θ gives U(Ψ∗)O ≤ q2rC(r,ω)ω−1ε.

We conclude this section by proving the second quantitative version of Lemma 5.19, which can be viewed as a rational version of Lemma 3.18, and will form the basis of the ‘randomised rounding’ aspect of the proof referred to in the introduction.

- Lemma 5.25. Let Σ ≤ Sq, A be a Σ≤-family with γ ∈ (ZD)Ar. Let Φ be a Σ-adapted (ω,s)extendable [q]-complex with s = 3r2, n = |V (Φ)| > n0(q,D) large and n−1/2 < ω < ω0(r). Suppose J ∈ QLγ(Φ) with U(J)O ≤ ε for all O ∈ Φr/Σ. Then there is Ψ ∈ QA(Φ) with ∂γΨ = J and all U(Ψ)O ≤ C(q,ω)ε.


Proof. We follow the proof of Lemma 5.19. We can choose the kA so that A |kA| ≤ U(J) < εnr. We deﬁne Ψ0 by averaging over each choice of φA ∈ A(Φ). Then for any orbit O we have P(O ⊆

φAΣ) < qrω−1n−r, as Φ is (ω,s)-extendable, so U(Ψ0)O < A |kA|qrn−r < qrω−1ε and similarly U(J0)O ≤ q2rω−1ε.

By Lemma 5.24 we can construct Ψi and Ji = Ji−1 − ∂γΨi as in the proof of Lemma 5.19 so that all U(Ψi)O ≤ εi and U(Ji)O ≤ qrεi, where ε0 = qrω−1ε and εi = qr+2iC(i,ω)ω−1εi−1. Then all U(Ψ)O ≤ 2q2rω−1ε i∈[r](qr+2iC(i,ω)ω−1) < C(q,ω)ε, recalling that C(i,ω) = 2C(i)ω−(9i)i+4 and C(i) = 2(9i+2)i+5.

# 6 Bounded integral decomposition

To complete the proof of Theorem 3.1, it remains to prove Lemma 3.18. The high-level strategy is similar to the randomised rounding and focussing argument from [15] (version 1), although there are some additional complications in the general setting. The proof is by induction on q. In the inductive step we can assume Lemma 4.2 for smaller values of q (this will be used in the proof of

- Lemma 6.2). Note that we do not assume that γ is elementary, as this property is not preserved by the inductive step.


## 6.1 Proof modulo lemmas

We start by stating two key lemmas and using them to deduce Lemma 3.18; the remainder of the section will then be devoted to proving the key lemmas. The ﬁrst lemma is an approximate version of Lemma 3.18; the second will allow us to focus the support in a smaller set of vertices. The proof of Lemma 3.18 is then to alternate applications of these lemmas until the support is suﬃciently small that it suﬃces to use the total use quantitative version of the decomposition lattice lemma. In the statements of the lemmas we denote the labelled complex by Φ, but note that they will be applied to restrictions of Φ as in the statement of Lemma 3.18, so we allow for weaker lower bounds on the extendability and number of vertices. Throughout we ﬁx a Σ≤-family A with Σ ≤ Sq and |A| ≤ K, suppose γ ∈ (ZD)Ar and let ω0 := ω0(q,D,K), n0 := n0(q,D,K) be as in Lemma 3.18.

Lemma 6.1. Let Φ be an (ω′,h)-extendable Σ-adapted [q]-complex on [n], where n−h−2q < ω′ < ω0 and n > n01/2r. Suppose J ∈ γ(Φ) is θ-bounded, with n−(4hq)−r < θ < 1. Then there is some (ω′)3qqhθ-bounded J′ ∈ (ZD)Φr and (ω′)−q 1θ-bounded Ψ ∈ ZA(Φ) with ∂γΨ = J − J′.

- Lemma 6.2. Let Φ be an (ω′,h)-extendable Σ-adapted [q]-complex on [n], where n−h−2q < ω′ < ω0


and n > n01/2r. Let V ′ ⊆ V (Φ) with |V ′| = n/2 be such that (Φ,V ′) is (ω′,h)-extendable wrt V ′. Suppose J ∈ γ(Φ) is θ-bounded, with n−(3hq)−r < θ < (ω′)3qqh. Then there is some (ω′)−q 2qhθbounded J′ ∈ (ZD)Φ[V′]r and (ω′)q−2qhθ-bounded Ψ ∈ ZA(Φ) with ∂γΨ = J − J′.

Proof of Lemma 3.18. Let A be a Σ≤-family with Σ ≤ Sq and |A| ≤ K and suppose γ ∈ (ZD)Ar. Let Φ be an (ω,h)-extendable Σ-adapted [q]-complex on [n], where n−h−3q < ω < ω0 and n > n0. Suppose J ∈ γ(Φ) is θ-bounded, with n−(5hq)−r < θ < 1. We need to show that there is some ωq−2hθ-bounded Ψ ∈ ZA(Φ) with ∂γΨ = J.

Let t be such that n1/2r/2 < 2−tn ≤ n1/2r. Choose Vt ⊆ ... ⊆ V1 ⊆ V0 = V (Φ) with |Vi| = 2−in uniformly at random. By Lemma 6.5 (a simple concentration argument given in the next subsection) whp all (Φ[Vi],Vi+1) are (ω′,h)-extendable wrt Vi+1, where ω′ = (ω/2)h > n−h−2q. We deﬁne θbounded Ji ∈ γ(Φ[Vi]) as follows.

Let J0 = J. Given Ji with 0 ≤ i < t, we apply Lemma 6.1 to obtain some (ω′)3qqhθ-bounded Ji′ ∈ (ZD)Φ[Vi]r and (ω′)−q 1θ-bounded Ψi ∈ ZA(Φ[Vi]) with ∂γΨi = Ji − Ji′. Note that Ji′ ∈ γ(Φ[Vi]) .

Next we apply Lemma 6.2 to Ji′ (with (ω′)3qqhθ in place of θ) to obtain some θ-bounded Ji+1 ∈ (ZD)Φ[Vi+1]r and θ-bounded Ψ′i ∈ ZA(Φ[Vi]) with ∂γΨ′i = Ji′ − Ji+1.

To continue the process, we need to show Ji+1 ∈ γ(Φ[Vi+1]) . To see this, ﬁrst note Ji+1 ∈ γ(Φ) = Lγ(Φ) by Lemma 5.19. Now for any O ∈ Φ[Vi+1]/Σ, by deﬁnition of Lγ(Φ) we have

(Ji♯+1)O ∈ γ♯[O] , so Ji+1 ∈ Lγ(Φ[Vi+1]) = γ(Φ[Vi+1]) , again by Lemma 5.19.

We conclude with some θ-bounded Jt ∈ γ(Φ[Vt]) , where |Vt| ≤ n1/2r. By Lemma 5.23 there is Ψt ∈ ZA(Φ[Vt]) such that ∂γΨt = Jt and U(Ψt) ≤ 2(9q)q+2U(Jt). Let Ψ = Ψt + ti=0−1(Ψi + Ψ′i). Then ∂γΨ = Jt + ti=0−1(Ji − Ji′ + Ji′ − Ji+1) = J.

Also, for any ψ ∈ Φr−1 we have U(Ψ)ψ ≤ U(Ψt)ψ + ti=0−1(U(Ψi)ψ +U(Ψ′i)ψ) < 2(9q)q+2θ(n1/2r)r+ t−1 i=0((ω′)−q 1θ2−in + θ2−in) < 2(ω′)−q 1θn, so Ψ is (say) ωq−2hθ-bounded.

## 6.2 Random subgraphs

In the next subsection we will extend the rational decomposition lemma (Lemma 5.25) to a version relative to a sparse random subgraph L. We establish some preliminary properties of L in this subsection. First we show that whp L is ‘typical’ in Φ, in that specifying that certain edges of an extension should belong to L scales the number of extensions in the expected way.

- Deﬁnition 6.3. Let Φ be an [q]-complex and L ⊆ Φ◦r. Let dΦ(L) = |L||Φ◦r|−1. We say L is (c,s)-typical in Φ if for any Φ-extension E = (H,F,φ) of rank s and H′ ⊆ Hr◦ \ Hr◦[F] we have XE,H′(Φ,L) = (1 ± c)dΦ(L)|H′|XE(Φ).


- Lemma 6.4. Let Φ be an (ω,s)-extendable [q]-complex. Suppose L is ν-random in Φ◦r, where ν > n−(3sq)−r, n = |V (Φ)|. Then whp L is (n−1/3,s)-typical in Φ. In particular, Φ[L] is (ω′,s)-extendable, where ω′ = 0.9νQsrω.


Proof. First note by the Chernoﬀ bound that whp dΦ(L) = (1 ± n−0.4)ν. Let E = (H,F,φ) be any Φ-extension of rank s, H′ ⊆ Hr◦ \ Hr◦[F] and X = XE,H′(Φ,L). Note that EX = ν|H′|XE(Φ), where XE(Φ) > ωnvE. Also, for any k ∈ [r] there are O(nk) choices of f ∈ Φ◦r with f \ φ(F)| = k, and for each such f, changing whether f ∈ L aﬀects X by O(nvE−k). Thus X is O(n2vE−1)-varying, so by Lemma 3.5 whp X = (1 ± n−1/3)ν|H′|XE(Φ). In particular, X > ω′nvE.

Similarly, we obtain the following variant form of the previous lemma that was used in the previous subsection.

- Lemma 6.5. Let Φ be an (ω,s)-extendable [q]-complex on [n]. Suppose S is uniformly random in [n] m , where m > ω−1 log n and n is large. Then (Φ,S) is ((ω/2)h,s)-extendable wrt S with probability


- at least 1 − e−(ωm)2/20.


Proof. It suﬃces to estimate the probability that any simple Φ-extension of rank s is ω/2-dense in (Φ,S). Let E = (H,F,φ) be any Φ-extension of rank s with F = V (H)\{x} for some x ∈ V (H). Note

that XE(Φ,S) = φ+∈XE(Φ) 1φ+(x)∈S and XE(Φ) > ωn as Φ is (ω,s)-extendable. Then XE(Φ,S) is hypergeometric with EXE(Φ,S) > ωm, so P(XE(Φ,S) < ωm/2) < e−(ωm)2/12. The lemma follows by taking a union bound over at most qsnqs < e(ωm)2/48 choices of E.

We also require the following reﬁned notion of boundedness that operates with respect to all small extensions in L. The following lemma is analogous to [15, Lemma 2.21].

- Deﬁnition 6.6. Let Φ be an [q]-complex, L ⊆ Φ◦r, and J ∈ (ZD)Φr. Let E = (H,F,φ) with


- H ⊆ [q](s) be a Φ-extension, G ⊆ Hr◦ \ Hr◦[F], ψ ∈ [q](s)r and e = Im(ψ). We write XE,Ge,J (Φ,L) =


φ∗∈XE,G(Φ,L) U(J)φ∗ψ. We say that J is (θ,s)-bounded wrt (Φ,L) if XE,Ge,J (Φ,L) < θdΦ(L)|G||V (Φ)|vE for any such E, G and e with e ∈/ G and e \ F = ∅.

- Lemma 6.7. Let Φ be an [q]-complex with |V (Φ)| = n. Suppose J ∈ (ZD)Φr is θ-bounded, with

θ > n−0.01, and all U(J)ψ < n0.1. Let L be ν-random in Φ◦r, where ν > n−(3sq)−r. Then whp J is (1.1θ,s)-bounded wrt (Φ,L).

Proof. Let E = (H,F,φ) with H ⊆ [q](s) be a Φ-extension, G ⊆ Hr◦ \ Hr◦[F] and ψ ∈ [q](s)r with e := Im(ψ) ∈/ G and e \ F = ∅. Write X = XE,Ge,J (Φ,L) = φ∗∈XE(Φ) 1φ∗∈XE,G(Φ,L)U(J)φ∗ψ. As J is θ-bounded we have φ∗∈XE(Φ) U(J)φ∗ψ < θnvE. For each φ∗ ∈ XE(Φ) we have P(φ∗ ∈ XE,G(Φ,L)) = ν|G|, so EX < θν|G|nvE. For any k ∈ [r] there are O(nk) choices of f ∈ Φ◦r with |f \ φ(F)| = k, and for each such f, changing whether f ∈ L aﬀects X by O(nvE−k+0.1). Thus X is O(n2vE−0.8)-varying, so by Lemma 3.5 whp X < 1.1θdΦ(L)|G|nvE.

- 6.3 Rational decompositions


In this subsection we prove the following result, which is a version of Lemma 5.25 relative to a sparse random subgraph L; note the key point that we incur a loss in boundedness that depends only on q, not on the density of L. Throughout, as in the hypotheses of Lemma 6.1, we let A be a Σ≤-family with Σ ≤ Sq and |A| ≤ K, suppose γ ∈ (ZD)Ar, and let Φ be an (ω,h)-extendable Σ-adapted [q]-complex on [n], where n−h−2q < ω < ω0 and n > n−0 1/2. (For convenient notation we rename ω′

- as ω.)


- Lemma 6.8. Suppose L ⊆ Φ◦r is (c,h)-typical in Φ with dΦ(L) = ν ≥ n−(3hq)−r. Let J ∈ γ(Φ) Q ∩ QΦ[L]r. Suppose J is θ-bounded with all |Jψ| < n0.1 and (θ,h)-bounded wrt (Φ,L). Then there is some ωq−0.9θ-bounded Ψ ∈ QA(Φ[L]) with ∂γΨ = J.

The proof of Lemma 6.8 uses the following result, which reduces to the case when we bound the use of every orbit.

- Lemma 6.9. For any θ-bounded J ∈ (QD)Φr there is some J′ ∈ (QD)Φr and Ψ ∈ QA(Φ) such that ∂Ψ = J − J′, and for any O ∈ Φr/Σ both U(Ψ)O − U(J)O and U(J′)O are at most qqω−1θ.


Proof. For each O ∈ Φr/Σ we ﬁx a representative ψO ∈ ΦBO and nO ∈ QABO with |nO| = U(J)O and fBO(J)ψO = θ nOθ γθ, so JO = θ nOθ γ(ψOθ−1). For each such (O,θ) we let EθO = (−→q ,Im(θ),ψOθ−1). We let Ψ = O,θ nOθ |XEO

(Φ)|−1XEO

(Φ), where if θ ∈ A ∈ A we choose the copy of φ ∈ A(Φ) for each φ ∈ XEO

θ

θ

(Φ). Then J is exactly cancelled by the γ-atoms of ∂γΨ corresponding to γ(φ)O for φ ∈ A(Φ). To estimate the remaining contributions of ∂γΨ, note that for any O ∈ Φr/Σ and r′ ∈ [r] we have {|nOθ ′| : |Im(O′) \ Im(O)| = r′} ≤ r r′ θnr′. For each such (O′,θ), there are at least ωnq−r choices of φ, of which at most (q − r)!nq−r−r′ contain Im(O), so for random φ ∈ XEO′

θ

(Φ) we have P(O ⊆ φΣ) ≤ (q − r)!ω−1n−r′. Summing over r′ gives the stated bounds on U(Ψ)O − U(J)O and U(J′)O.

θ

- Proof of Lemma 6.8. We start by deﬁning Ψ0 ∈ QA(Φ) such that ∂γΨ0 = J and U(Ψ0)O < U(J)O + (C∗ − 1)θ for all O ∈ Φr/Σ, where C∗ = 2C(q,ω)qqω−1 (so Ψ0 is C∗θ-bounded). Then we will modify Ψ0 to obtain Ψ using a version of the Clique Exchange Algorithm.


First we apply Lemma 6.9 to obtain Ψ′ ∈ QA(Φ) and J′ = J − ∂γΨ so that all U(Ψ)O − U(J)O and U(J′)O are at most qqω−1θ. Then by Lemma 5.25 there is Ψ′′ ∈ QA(Φ) such that ∂γΨ′′ = J′ and all U(Ψ′′)O < C(q,ω)qqω−1θ. We take Ψ0 = Ψ′ + Ψ′′.

We apply two Splitting Phases, the ﬁrst in Φ and the second in Φ[L]. For the ﬁrst, we ﬁx N0 ∈ N such that N0Ψ0 ∈ ZA(Φ), and list the signed elements of N0Ψ0 as (siφi : i ∈ [|N0Ψ0|]), where each si ∈ ±1. For each i, say with φi ∈ Ai(Φ), we consider the Φ-extension Ei = ([q](p),[q],φi), and deﬁne Ψ1 ∈ QA(Φ) by Ψ1 = Ψ0 + N0−1 i∈[|N

i∈XEi(Φ)(Ai(Φ[φ∗i Υ′]) − Ai(Φ[φ∗i Υ])). Then ∂γΨ1 = ∂γΨ0 = J, and all signed elements in Ψ0 are cancelled.

0Ψ0|] siEφ∗

We claim for any O ∈ Φr/Σ that ΓO := U(Ψ1)O − U(Ψ0)O ≤ r!ω−1(2pq)rC∗θ. To see this, we estimate ΓO ≤ Ei∈[|N0Ψ0|]P(Im(O) ∈ φ∗i(Ω′)) (recall Ω′ = Kqr(p) \ Q). For any r′ ∈ [r], as Ψ0 is C∗θ-bounded there are at most N0 r r′ C∗θnr′ choices of i such that |Im(O) \ Im(φi))| = r′. For each such i, as Φ is (ω,h)-extendable there are at least ωnpq−q choices of φ∗i ∈ XEi(Φ), of which

- at most r!|Ω′|nvEi−r′ have Im(O) ∈ φ∗i (Ω′), so P(Im(O) ∈ φ∗i(Ω′)) < r!ω−1|Ω′|n−r′. Therefore ΓO ≤ N0−1 r′∈[r] N0 r r′ C∗θnr′ · r!ω−1|Ω′|n−r′ < r!ω−1(2pq)rC∗θ, as claimed.


Also, for any φ ∈ A(Φ) we claim that |Ψ1φ| < ω−1pqnr−q O⊆φΣ(qC∗θ + U(J)O). To see this, we consider separately the contributions from φi according to r′ = |Im(φ) ∩ Im(φi)|.

First we consider 0 ≤ r′ < r. As Ψ0 is C∗θ-bounded there are at most N0QC∗θnr−r′ such choices of φi. For each such i, there are at least ωnpq−q choices of φ∗i ∈ XEi(Φ), of which at most pqnpq−q−(q−r′)) have φ = φ∗iφ′ for some φ′ ∈ [q](p), so the total such contribution to |Ψ1φ| is at most

- N0−1 r′ N0QC∗θnr−r′ · ω−1pqnr′−q = rpqQC∗ω−1θnr−q. It remains to consider r′ = r. For each O ⊆ φΣ there are at most N0(U(J)O +(C∗ −1)θ) choices

of φi containing Im(O). For each of these with |Im(φi) ∩ Im(φ)| = r we have φ = φ∗i φ′ for some φ′ ∈ [q](p) with probability at most ω−1pqnr−q, so the total such contribution to |Ψ1φ| is at most (U(J)O + (C∗ − 1)θ)ω−1pqnr−q. The claim follows.

In the second Splitting Phase, we ﬁx N1 ∈ N such that N1Ψ1 ∈ ZA(Φ), and list the signed elements of N1Ψ1 as (siφi : i ∈ [|N1Ψ1|]), where each si ∈ ±1. For each i, say with φi ∈ Ai(Φ), we consider the Φ-extension Ei = ([q](p),[q],φi), and deﬁne Ψ2 ∈ QA(Φ) by Ψ2 = Ψ1 +

- N1−1 i∈[|N


i∈XEi,L(Φ)(Ai(Φ[φ∗i Υ′]) − Ai(Φ[φ∗iΥ])). Then ∂Ψ2 = ∂Ψ1 = J, and all signed elements in Φ1 are cancelled, so Ψ2 is supported on maps φ such that there is at most one e ∈ Q with φ(e) ∈/ L. (This was the same as the ﬁrst Splitting Phase except that we changed XEi(Φ) to XEi(Φ,L).)

1Ψ1|] siEφ∗

We claim for any O ∈ Φr/Σ that Γ′O := U(Ψ2)O−U(Ψ1)O ≤ (pq)2qω−2C∗θν−1, where ν := dΦ(L). To see this, we estimate Γ′O ≤ Ei∈[|N1Ψ1|]P(Im(O) ∈ φ∗i (Ω′)). We ﬁx f′ ∈ Ω′ and consider the contribution from i with O = φ∗if′Σ. Consider any φ′ ∈ Φ with O = φ′f′Σ and the Φ-extension Ef′ = (H,f′,φ′), where H = [q](p)[[q]∪f′] is the restriction of [q](p) to [q]∪f′. Let H′ = Hr◦ \([q]r ∪{f′}).

The number of i with φi = φ∗ |[q] for some φ∗ ∈ XE

f′,H′(Φ,L) is at most N1

(qC∗θ + U(J)ψ)

N1ω−1pqnr−q

|Ψ1φ∗|[q]| <

ψ⊆φ∗|[q]

φ∗∈XE

φ∗∈XE

f′,H′(Φ,L)

f′,H′(Φ,L)

 qQC∗θXE

 

′,J

Xe

= N1ω−1pqnr−q

f′,H′(Φ,L) +

Ef′,H′(Φ,L)

e′∈Q

< 2N1ω−1pqnr−qqQC∗θν|H′|nq−|f′∩[q]|, as L is (c,h)-typical and J is (θ,h)-bounded wrt L.

For each such i, there are at least 0.9ωnpq−qν|Ω′| choices of φ∗i ∈ XEi(Φ,L), of which the number containing φ′ is at most 1.1ν|Ω′|−|H′∪{f′}|npq−q−r+|f′∩[q]|, so P(φ′ ⊆ φ∗i) < 1.3ω−1ν−|H′|−1n|f′∩[q]−r. Thus

2N1ω−1pqnr−qqQC∗θν|H′|nq−|f′∩[q]| · 1.3ω−1ν−|H′|−1n|f′∩[q]|−r

Γ′O < qrN1−1

f′∈Ω′

< (pq)2qω−2C∗θν−1, using p > 28q, as claimed.

We ﬁx N2 ∈ N such that N2Ψ2 ∈ ZA(Φ), and classify signed elements of N2Ψ2 as before: recall that a pair (O,φ′) is near or far, has the same sign as that of φ′ in N2Ψ2, and has a type θ determined by an orbit representative ψO ∈ O. For φ ∈ A(Φ) let Bφ be the number of pairs (O,φ) in N2Ψ2 such that Im(O) ∈/ L; note that all such pairs are near and Im(O) is uniquely determined by φ.

We claim that each Bφ < 3N2ω−2pqν−Q+1nr−q ψ⊆φ(qQC∗θ + U(J)ψ), To see this, we ﬁx ψ′ ∈ Υ′∪Υ\{[q]} and consider the contributions from i with φ∗i ψ′ = φ. We consider the Φ-extension Eψ′ = (H,F′,φ′), where F′ = Im(ψ′) (so |F′ ∩ [q]| = r), H = [q](p)[[q] ∪ F′] and φ = φ′ψ′. Let

- H′ = Hr◦ \ ([q]r ∪ Fr′).


The number of i with φi = φ∗ |[q] for some φ∗ ∈ XE

ψ′,H′(Φ,L) is at most N1

(qC∗θ + U(J)ψ)

N1ω−1pqnr−q

|Ψ1φ∗|[q]| ≤

ψ⊆φ∗|[q]

φ∗∈XE

φ∗∈XE

ψ′,H′(Φ,L)

ψ′,H′(Φ,L)

 qQC∗θXE

 

′,J

Xe

= N1ω−1pqnr−q

ψ′,H′(Φ,L) +

Eψ′,H′(Φ,L)

e′∈Q

< 2N1ω−1pqnr−qν|H′|nq−|F′∩[q]|(qQC∗θ + U(J)O)

= 2N1ω−1pqν|H′|(qQC∗θ + U(J)O), where for e′ = F′ ∩ [q] we let O ⊆ φΣ be such that Im(O) = φ(e′) and use Xe

′,J

Eψ′,H′(Φ,L) ≤ XE

ψ′,H′(Φ,L)U(J)O. For each such i, there are at least 0.9ωnpq−qν|Ω′| choices of φ∗i ∈ XEi(Φ,L), of which the number

containing ψ′ is at most 1.1ν|Ω′|−|H′|−(Q−1)npq−q−q+|F′∩[q]| (as |Fr′ \ [q]r| = Q − 1), so P(ψ′ ⊆ φ∗i ) < 1.3ω−1ν−|H′|−Q+1nr−q. Then

2N1ω−1pqν|H′|(qQC∗θ + U(J)O) · 1.3ω−1ν−|H′|−Q+1nr−q

Bφ < N2N1−1

ψ′:|F′∩[q]|=r

< 3N2ω−2pqν−Q+1nr−q

(qQC∗θ + U(J)ψ), as claimed.

ψ⊆φ

In Elimination Phase, we consider each orbit O ∈ Φr/Σ with Im(O) ∈/ L, say with representative ψO ∈ ΦB, and let EO = (B(2),B,ψO). For each ψO∗ ∈ XEO(Φ,L) and each signed near pair ±(O,φ) in N2Ψ2, say of type θ, i.e. φθ = ψO, we let Eφ(ψO∗ ) = (wBOφ ,F,φ0), where BOφ = θ(B),

- F = [q] ∪ (BOφ × [2]), φ0 |[q]= φ and φ0(θ(x),y) = ψO∗ (x,y) for x ∈ B, y ∈ [2].


φ

)(Φ,L) x∈[q](s) wB

We let Ψ = Ψ2 + N2−1 (O,φ) ±Eψ∗

xOψ∗x, where the sign

O∈XEO(Φ,L)Eψ+∈XEφ(ψ∗

O

is that of (O,φ), and each ψ∗x ∈ Aφ(Φ) where φ ∈ Aφ(Φ). Then ∂γΨ = J, similarly to the previous version of the algorithm, treating all near pairs on O as a single cancelling group, which is valid as JO = 0 when Im(O) ∈/ L. All pairs (O,φ) with Im(O) ∈/ L are cancelled, so Ψ ∈ QA(Φ[L]).

We claim for any O′ ∈ Φr/Σ that Γ′′O′ := U(Ψ)O′ −U(Ψ2)O′ ≤ ω−3(pq)2qC∗θν−1. To see this, we estimate

Γ′′O′ ≤ N2−1

(O,φ)

O∈XEO(Φ,L)P(Im(O′) ∈ ψ+(Ω′)) = N2−1

Eψ∗

P(Im(O′) ∈ ψOφ(Ω′)),

(O,φ)

(Φ,L) where EOφ = ([q](s),[q],φ).

with each ψOφ uniformly random in XEφ

O

We ﬁx f′ ∈ [q](s)r \ −→q r and consider the contribution from near pairs (O,φ) with O′ = ψOφf′Σ. Consider any φ′ ∈ Φr with O′ = φ′f′Σ and the Φ-extension Ef′ = (H,f′,φ′), where H = [q](p)[[q] ∪ f′]. For B ∈ [q]r let HB = Hr◦ \ {B,f′}.

The number of signed near pairs ±(O,φ) in N2Ψ2 with φ = φ∗ |[q], Im(O) ∈/ L, O = φ∗ |B Σ for some B ∈ [q]r and φ∗ ∈ XE

f′,HB(Φ,L) is at most

φ∗∈XE

f′,HB(Φ,L)

3N2ω−2pqν−Q+1nr−q

(qQC∗θ + U(J)ψ)

Bφ∗|[q] <

φ∗∈XE

ψ⊆φ

f′,HB(Φ,L)

f′,HB(Φ,L) + XEe∗,J

[qQC∗θXE

= 3N2ω−2pqν−Q+1nr−q

f′,HB(Φ,L)] < 3N2ω−2pqν−Q+1nr−q2QqQC∗θν|HB|nq−|f′∩[q]|,

e∗∈Q

as L is (c,h)-typical and J is (θ,h)-bounded wrt L. For each such (O,φ), there are at least 0.9ωnqs−qνQ(sr−1) choices for ψOφ ∈ XEφ

(Φ,L), of

O

which the number with O′ = ψOφf′Σ is at most 1.1nqs−q−r+|f′∩[q]|νQsr−|H|, so P(O′ = ψOφf′Σ) < 1.3ω−1ν−|HB|+Q−2n−r+|f′∩[q]|, as Qsr − |H| = Q(sr − 1) − |HB| + Q − 2. Thus

3N2ω−2pqν−Q+1nr−q2QqQC∗θν|HB|nq−|f′∩[q]|

Γ′′O′ < N2−1

f′∈[q](s)r\−→q r

· 1.3ω−1ν−|HB|+Q−2n−r+|f′∩[q]| < ω−3(pq)2qC∗θν−1, as claimed.

Finally, for any f ∈ Φr−1 we have

U(Ψ)f ≤ U(Ψ0)f + {ΓO : fΣ ⊆ O} + {Γ′O + Γ′′O : fΣ ⊆ O,Im(O) ∈ L} < C∗θn + r!ω−1(2pq)rC∗θn + 1.1qrνn((pq)2qω−2C∗θν−1 + ω−3(pq)2qC∗θν−1) < 2ω−3qr(pq)2qC∗θn.

Recalling that C∗ = 2C(q,ω)qqω−1, C(i,ω) = 2C(i)ω−(9i)i+4, C(i) = 2(9i+2)i+5, ωq := ω(9q)q+5, and ω < ω0 we see that Ψ is ωq−0.9θ-bounded.

## 6.4 Approximation

In this subsection we prove Lemma 6.1 (approximate bounded integral decomposition) by randomly rounding Lemma 6.8 (rational decomposition with respect to a sparse random subgraph). Throughout, as in the hypotheses of Lemma 6.1, we let A be a Σ≤-family with Σ ≤ Sq and |A| ≤ K, suppose γ ∈ (ZD)Ar, and let Φ be an (ω,h)-extendable Σ-adapted [q]-complex on [n], where n−h−2q < ω < ω0 and n > n0. We start with some preliminary lemmas for ﬂattening and focussing a vector.

### Lemma 6.10. If J ∈ (ZD)Φr is θ-bounded with θ > n−1/2 then there is some J′ ∈ (ZD)Φr and Ψ ∈ ZA(Φ) such that ∂Ψ = J − J′, J′ and Ψ are qqω−1θ-bounded, and U(J′)O < n0.1 for all O ∈ Φr/Σ.

Proof. Similarly to the proof of Lemma 6.9, for each O ∈ Φr/Σ with representative ψO ∈ ΦBO, we have nO ∈ ZABO with |nO| = U(J)O and fBO(J)ψO = θ nOθ γθ, so JO = θ nOθ γ(ψOθ−1). Let S be the intset where each (O,θ) appears |nOθ | times with the sign of nOθ . For each (O,θ) in S we add to Ψ with the same sign as (O,θ) a uniformly random φ ∈ XE(Φ) with E = (−→q ,Im(θ),ψOθ−1); then each γ(ψOθ−1) is cancelled by the corresponding γ(φ)O, where θ ∈ A, φ ∈ A(Φ).

For any ψ ∈ Φr−1 and k ∈ [r] there are at most k r−−11 θnk signed elements (O,θ) of S with |Im(O) \ Im(ψ)| = k. For each such (O,θ), there are at least ωnq−r choices of φ, of which at most (q − r)!nq−r−(k−1) contain φ, so P(ψ ⊆ φ) ≤ (q − r)!ω−1n−k+1. Then U(Ψ)ψ is a sum of bounded independent variables with mean at most 0.9qqω−1θn, so whp J′ and Φ are qqω−1θ-bounded. Similarly, whp U(J′)O < n0.1 for all O ∈ Φr/Σ.

### Lemma 6.11. Suppose J ∈ (ZD)Φr is θ-bounded with θ > n−1/2. Let L ⊆ Φ◦r be (c,h)-typical in Φ with dΦ(L) > n−(3hq)−r. Suppose J is (θ,h)-bounded wrt (Φ,L). Then there is some J′ ∈ (ZD)Φ[L]r and Ψ ∈ ZA(Φ) such that ∂Ψ = J − J′, J′ and Ψ are 22rω−1θ-bounded, and J′ is (q!22rω−1θ,h)bounded wrt (Φ,L).

Proof. We apply the same procedure as in the proof of Lemma 6.10, replacing XE(Φ) by XE(Φ,L). To spell this out, for each orbit O with representative ψO ∈ ΦBO, we have nO ∈ ZABO with |nO| = U(J)O and fBO(J)ψO = θ nOθ γθ, so JO = θ nOθ γ(ψOθ−1). Let S be the intset where each (O,θ) appears |nOθ | times with the sign of nOθ . For each (O,θ) in S we add to Ψ with the same sign as (O,θ) a uniformly random φOθ ∈ XE(Φ,L) with E = (−→q ,Im(θ),ψOθ−1); then each γ(ψOθ−1) is cancelled by γ(φOθ )O, where θ ∈ A, φOθ ∈ A(Φ).

We claim for any e′ ∈ L that Ee′ := (O,θ) B′∈[q]r\{Im(θ)} P(φOθ (B′) = e′) < 1.3q!2rω−1θd(L)−1. To see this, ﬁrst note that for any k ∈ [r], as J is (θ,h)-bounded wrt (Φ,L) there are at most

k+r

r −2θnk signed elements (O,θ) of S with |Im(O)\Im(e′)| = k. As Φ is (ω,h)-extendable and L is (c,h)-typical in Φ, for each such (O,θ), there are at least 0.9d(L)Q−1ωnq−r choices of φOθ , of which at most 1.1q!d(L)Q−

r k d(L)

k+r

r nq−r−k have φOθ (B′) = e′ for some B′ = Im(θ), so P(φOθ (B′) = e′) < 1.3q!ω−1d(L)1−

k+r

r n−k. The claim follows. Now for any f ∈ Φr−1, by typicality |L(Im(f))| < 1.1d(L)n, so by the claim U(Ψ)f is a sum of bounded independent variables with mean at most 1.5q!2rω−1θn, so whp J′ and Ψ are q!2r+1ω−1θ-bounded.

Finally, consider any Φ-extension E = (H,F,φ) with H ⊆ [q](h), any G ⊆ Hr◦ \ Hr◦[F] and H+ = H ∪ ψ≤ and G+ = G ∪ {e}. Note that Xe,J

- e ∈ [q](h)◦r \ G with e \ F = ∅. Write e = Im(ψ) with ψ ∈ [q](h), E+ = (H+,F,φ) with


′

E,G(Φ,L) = φ+∈XE+,G+(Φ,L) U(J′)φ+(e). As L is (c,h)-typical in Φ we have XE+,G+(Φ,L) < 1.1d(L)|G|+1nvE, so by the claim EXE,Ge,J′(Φ,L) < 0.9q!22rω−1θd(L)|G|nvE. Any choice of φOθ aﬀects XE,Ge,J′(Φ,L) by O(nvE−1), so by Lemma 3.3 whp Xe,J

′

E,G(Φ,L) < q!22rω−1θd(L)|G|nvE. Thus J′ is (q!22rω−1θ,h)-bounded wrt (Φ,L).

We also need the following estimate for the expected deviation from the mean of a random variable that is a sum of independent indicator variables.

### Lemma 6.12. There is C > 0 such that for any sum of independent indicator variables X with mean µ we have E|X − µ| ≤ C√µ.

![image 19](<2018-keevash-existence-designs_images/imageFile19.png>)

Proof. We can assume µ > 1, otherwise we use the bound E|X −µ| ≤ 2µ ≤ 2√µ. Write E|X −µ| =

![image 20](<2018-keevash-existence-designs_images/imageFile20.png>)

t≥0 |t − µ|P(X = t) = E0 + E1, where Ei is the sum of |t − µ|P(X = t) over |t − µ| > 12C√µ for i = 0 or |t − µ| ≤ 21C√µ for i = 1. Clearly, E1 ≤ 21C√µ, and by Chernoﬀ bounds, for C large,

![image 21](<2018-keevash-existence-designs_images/imageFile21.png>)

![image 22](<2018-keevash-existence-designs_images/imageFile22.png>)

![image 23](<2018-keevash-existence-designs_images/imageFile23.png>)

![image 24](<2018-keevash-existence-designs_images/imageFile24.png>)

![image 25](<2018-keevash-existence-designs_images/imageFile25.png>)

![image 26](<2018-keevash-existence-designs_images/imageFile26.png>)

a(e−a2/2µ + e−a2/2(µ+a/3)) ≤ 21C√µ.

E0 ≤

![image 27](<2018-keevash-existence-designs_images/imageFile27.png>)

![image 28](<2018-keevash-existence-designs_images/imageFile28.png>)

- 1

![image 29](<2018-keevash-existence-designs_images/imageFile29.png>)

- 2C√µ


a>

![image 30](<2018-keevash-existence-designs_images/imageFile30.png>)

Now we give the proof of our ﬁrst key lemma, on approximate integral decompositions.

Proof of Lemma 6.1. Suppose J ∈ (ZD)Φr is θ-bounded. By Lemma 6.10 there is some J0 ∈ (ZD)Φr and Ψ0 ∈ ZA(Φ) such that ∂Ψ0 = J −J0, J0 and Ψ0 are qqω−1θ-bounded, and U(J0)O < n0.1 for all O ∈ Φr/Σ.

Let L be ν-random in Φ◦r, where ν = n−(3hq)−r. By Lemma 6.4 whp L is (n−1/3,h)-typical in Φ. and by Lemma 6.7 whp J0 is (2qqω−1θ,h)-bounded wrt (Φ,L).

By Lemma 6.11 there is some J1 ∈ (ZD)Φ[L]r and Ψ1 ∈ ZA(Φ) such that ∂Ψ1 = J0 − J1, J1 and

Ψ1 are (2q)2qω−2θ-bounded, and J1 is ((2q)2qω−2θ,h)-bounded wrt (Φ,L). By Lemma 6.8 there is some ωq−1θ/2-bounded Ψ∗ ∈ QA(Φ[L]) with ∂Ψ∗ = J1. We obtain Ψ2 ∈ ZA(Φ[L]) from Ψ∗ by randomised rounding as follows. For each φ with Ψ∗φ = 0, let sφ ∈ ±1 be the sign of Ψ∗φ, let mφ = sφΨ∗φ , let Xφ be independent Bernoulli random variables such that Ψ∗φ = sφ(mφ + EXφ), and let Ψ2φ = sφ(mφ + Xφ). Note that each EΨ2φ = Ψ∗φ, so E∂Ψ2 = ∂Ψ∗ = J1.

Let J′ = J1−∂Ψ2. For any O ∈ Φ[L]r/Σ we have (J′)O = φ γ(φ)Osφ(EXφ−Xφ). Separating the positive and negative contributions for each γ-atom a at O we can write U(J′)O ≤ a∈±γ[O] |Ya−µa|, where each Ya is a sum of independent indicator variables with mean µa ≤ U(Ψ∗)O. By Lemma

- 6.12 we have EU(J′)O < C U(Ψ∗)O, where C depends only on q, D and K. For any f ∈ Φr−1,


![image 31](<2018-keevash-existence-designs_images/imageFile31.png>)

whp |L(Im(f))| < 1.1νn, so writing ′O for the sum over O ∈ Φr/Σ with f ⊆ Im(O) ∈ L, by Cauchy-Schwartz

′

′

EU(J′)f < C

U(Ψ∗)O)1/2

![image 32](<2018-keevash-existence-designs_images/imageFile32.png>)

U(Ψ∗)O ≤ C(1.1νn

O

O

< C(νqrωq−1θ)1/2n < ωq3qhθn/2, as ν = n−(3hq)−r, θ > n−(4hq)−r, ωq = ω(9q)q+5, ω > n−h−2q.

Any rounding decision aﬀects U(J′)f by at most 1, so by Lemma 3.3 whp U(J′)f < ωq3qhθn for all f ∈ Φr−1. Similarly, whp U(Ψ2)f < 0.9ωq−1θn for all f ∈ Φr−1. Thus J′ is ωq3qhθ-bounded and Ψ = Ψ0 + Ψ1 + Ψ2 is ωq−1θ-bounded with ∂Ψ = J − J′.

## 6.5 Lifts and neighbourhood lattices

This subsection contains some preliminaries for the proof of our second key lemma in the following subsection. Throughout we suppose A is a Σ≤-family, γ ∈ (ZD)Ar and Φ is a Σ-adapted [q]-complex. The construction in the following deﬁnition is a technical device for working with neighbourhood lattices.

- Deﬁnition 6.13. (lifts)


Fix a representative ψO for each orbit O ∈ Φr/Σ. Given J ∈ ΓΦr we deﬁne J↑ ∈ (ΓΣ≤)Φr, where for each O ∈ Φr/Σ we let (Jψ↑O)σ = JψOσ where deﬁned, and set all other entries to zero. We call J↑ a lift of J. For J′ ∈ (ΓΣ≤)Φr we write π(J′) := {(Jψ′ )σ{ψσ} : ψ ∈ Φr,σ ∈ Σ≤}.

Note that J = π(J↑).

![image 33](<2018-keevash-existence-designs_images/imageFile33.png>)

- Deﬁnition 6.14. (lifted vector systems) Let A↑ be obtained from A by including a copy Aθ of A for each A ∈ A and θ = (θB : B ∈ Q) with each θB ∈ ΣB.


![image 34](<2018-keevash-existence-designs_images/imageFile34.png>)

Suppose γ ∈ ΓAr. Let γ↑ ∈ (ΓΣ≤)A↑r where for θ ∈ Aθ we have γθ↑ = 0 unless θ = θB for some

![image 35](<2018-keevash-existence-designs_images/imageFile35.png>)

- B ∈ Q, when (γθ↑B)σ is γθBσ if θB ∈ ΣB′, σ ∈ ΣB′ or 0 otherwise. Lemma 6.15.


- i. The set of γ↑-molecules is the set of lifts of γ-molecules.
- ii. The set of γ↑-atoms is the set of lifts of γ-atoms.
- iii. If J ∈ γ(Φ) then any lift J↑ of J is in γ↑(Φ) , with U(J↑)O = U(J)O for all O ∈ Φr/Σ.


![image 36](<2018-keevash-existence-designs_images/imageFile36.png>)

Proof. Clearly (ii) and (iii) follow from (i). For (i), consider any φ ∈ A(Φ) and φ↑ ∈ Aθ(Φ) with φ↑ = φ. We claim γ↑(φ↑) is a lift of γ(φ). Indeed, for any O ∈ Φr/Σ with O ⊆ φΣ and ψ ∈ O we have γ↑(φ↑)ψ = 0, except for ψ = φθB ∈ O where B = φ−1(Im(O)), when each (γ↑(φ↑)ψ)σ = (γ↑(φ↑)φ↑θB)σ = (γθ↑B)σ = γθBσ = γ(φ)ψσ. Conversely, any lift of γ(φ) with respect to orbit representatives ψO can be expressed as γ↑(φ↑) with φ↑ ∈ Aθ(Φ) where θB = φ−1ψO for each B ∈ Q, Im(O) = φ(B).

![image 37](<2018-keevash-existence-designs_images/imageFile37.png>)

We also require some notation and basic properties of neighbourhood lattices (recall the notation of Deﬁnitions 2.5 and 2.17).

- Deﬁnition 6.16. (quotients) Let Σ∗ = Σ/B∗ where B∗ ⊆ [q] with r∗ = r −|B∗| > 0. Suppose A∗ is a Σ∗-family that includes a copy Aθ∗ of (Σ∗)≤ for each A ∈ A and θ∗ ∈ AB∗. We call γ∗ ∈ (ZD)A∗r∗


a B∗-quotient of γ if for each θ∗ ∈ AB∗ there is σ∗ = σ∗(θ∗) ∈ Σ with σ∗θ∗ = idB∗ such that γθ∗′ = γθ whenever θ∗ ⊆ θ ∈ Ar, θ′ = (σ∗θ)/idB∗ ∈ Aθ∗.

Lemma 6.17. Let J ∈ (ZD)Φr, ψ∗ ∈ ΦB∗, Φ∗ = Φ/ψ∗ and J∗ = J/ψ∗. Suppose γ∗ ∈ (ZD)A∗r∗ is a B∗-quotient of γ ∈ (ZD)Ar. Then

- i. φ′ ∈ A∗(Φ∗) iﬀ φ′ = (φ ◦ (σ∗)−1)/ψ∗ for some φ ∈ A(Φ), θ∗ ∈ AB∗, σ∗ = σ∗(θ∗).
- ii. for such φ′, φ we have γ(φ)/ψ∗ = γ∗(φ′),
- iii. if J ∈ γ(Φ) then J∗ ∈ γ∗(Φ∗) .


Proof. For (i), ﬁrst consider any φ′ ∈ A∗(Φ∗), say φ′ ∈ Aθ∗(Φ∗), and deﬁne φ such that φ′ = (φ ◦ (σ∗)−1)/ψ∗. As φ′ ∈ Σ∗≤(Φ∗) = Φ∗q−|B∗| we have φ ◦ (σ∗)−1 ∈ Φ, so φ ∈ Φq = A(Φ). Conversely, consider any φ′ = (φ◦(σ∗)−1)/ψ∗ with φ ∈ A(Φ), θ∗ ∈ AB∗, σ∗ = σ∗(θ∗). For any θ′ = (σ∗θ)/idB∗ ∈ Aθ∗ where θ∗ ⊆ θ ∈ A we have φθ ∈ Φ as φ ∈ A(Φ), so φ′θ′ = (φθ)/ψ∗ ∈ Φ∗, so φ′ ∈ Aθ∗(Φ∗). This proves (i). Furthermore, if θ ∈ Ar then (γ(φ)/ψ∗)φ′θ′ = γ(φ)φθ = γθ = γθ∗′ = γ∗(φ′)φ′θ′, so (ii) holds, and (iii) is immediate from (ii).

## 6.6 Reducing support

In this section we prove Lemma 6.2, using the inductive hypothesis of Lemma 3.18 if r > 1. Our argument will also prove the case r = 1, which is the base of the induction. For convenient notation

we rename ω′ as ω. Let V ′ ⊆ V (Φ) with |V ′| = n/2 be such that (Φ,V ′) is (ω,h)-extendable wrt V ′. Suppose J ∈ γ(Φ) is θ-bounded, where θ < ωq3qh. We need to ﬁnd some ωq−2qhθ-bounded J′ ∈ (ZD)Φ[V′]r and ωq−2qhθ-bounded Ψ ∈ ZA(Φ) with ∂Ψ = J − J′.

We will deﬁne J = J0,... ,Jr ∈ γ(Φ) so that Jψj = 0 whenever |Im(ψ) ∩ V ′| < j and Jj is θj-bounded, where θ0 = θ, θ1 = 2qω−1θ and for 0 < j < r we let θj+1 = 2r2+2η−r+1MjIHθj, where η = (9q)−2qω and MjIH = ωq−−3rh+j = ω−3h(9(q−r+j))q−r+j+5. As θ < ωq3qh we see that n−(5h(q−r+j))−j < n−(5hq)−r < θj < ωq3−h(rq+−jr+j), i.e. θj satisﬁes the necessary bounds to apply Lemma 4.2 with (q−r+j,j) in place of (q,r), and also that θr < ωq < 2−rη.

We start with J0 = J. To deﬁne J1 = J − ∂γΨ0, for each orbit O ∈ Φr/Σ with Im(O) ∩ V ′ = ∅, we ﬁx a representative, say ψO ∈ ΦBO, recall fBO(J)ψO ∈ γBO by Lemma 2.34, and ﬁnd nO ∈ ZABO with |nO| = U(J)O and fBO(J)ψO = θ nOθ γθ. Then JO = θ nOθ γ[ψO]θ = θ nOθ γ(ψOθ−1).

Let S be the intset where each (O,θ) appears |nOθ | times with the sign of nOθ . For each (O,θ) in S we add to Ψ0 a uniformly random φ with ψOθ−1 ⊆ φ ∈ A(Φ) and Im(φ) \ Im(ψO) ⊆ V ′, with the same sign as that of (O,θ) in S. Then γ(ψOθ−1) is cancelled by γ(φ) in J1 = J − ∂γΨ0, and all other ψ with γ(φ)ψ = 0 have Im(ψ) ∩ V ′ = ∅. As (Φ,V ′) is (ω,h)-extendable wrt V ′ there are at least ω(n/2)q−r choices for each φ, so similarly to Lemma 6.10, whp J1 and Ψ0 are θ1-bounded. If r = 1 this completes the construction, so henceforth we suppose r > 1.

Given Jj with 0 < j < r we will let Jj+1 = Jj − ∂γΨj, where |Im(φ) ∩ V ′| = j whenever Ψjφ = 0. To deﬁne Ψj, we ﬁx any (see Deﬁnition 6.13) lift Jj↑ of Jj with orbit representatives ψO for O ∈ Φr/Σ, such that writing BO = {i : ψO(i) ∈ V \ V ′}, we have ψO′ |BO= ψO |BO for any orbit O′ that contains some ψ with ψ |BO= ψO |BO. Then for each ψ∗ ∈ Φr−j with Im(ψ∗)∩V ′ = ∅ such that ψ∗ is some ψO |BO we consider Φ∗ = Φ/ψ∗, J∗ = Jj↑/ψ∗, Σ∗ = Σ/BO and some BO-quotient (see

- Deﬁnition 6.16) γ∗ ∈ ((ZD)Σ≤)A∗r∗ of γ↑. Note that J∗ is supported in Φ∗[V ′]r∗, and Φ∗[V ′] is (ω,h)extendable by Lemma 2.12. Then J∗ ∈ γ∗(Φ∗) by Lemmas 6.15 and 6.17, so J∗ ∈ γ∗(Φ∗[V ′]) by Lemma 5.19 (as in the earlier proof of Lemma 3.18 modulo lemmas).


We will write J∗ = ∂γ∗Ψ∗ for some Ψ∗ = Ψψ∗ ∈ ZA∗(Φ∗[V′]) and deﬁne Ψj as the sum over all such ψ∗ and φ′ ∈ A∗(Φ∗[V ′]) of Ψψ

∗

![image 38](<2018-keevash-existence-designs_images/imageFile38.png>)

φ′ {φ}, where φ′ = (φ ◦ (σ∗)−1)/ψ∗ for some φ ∈ Aθ(Φ), θ∗ ∈ AθBO, σ∗ = σ∗(θ∗); recall from Lemma 6.17 that any φ′ ∈ A∗(Φ∗) can be thus expressed, and then γ↑(φ)/ψ∗ = γ∗(φ′). Then Jj+1 = Jj − ∂γΨj will be as required if ∂γΨjψ = Jψj for every ψ ∈ Φr with |Im(ψ) ∩ V ′| = j.

![image 39](<2018-keevash-existence-designs_images/imageFile39.png>)

To see this, consider any O ∈ Φr/Σ with |BO| = r − j and ψ = ψOσ ∈ O. Let ψ∗ = ψO |BO, and deﬁne J∗ and γ∗ for ψ∗ as above. For each ψ′ ∈ O with ψ′ |BO= ψ∗ let σ′ = σ′(ψ′) be such that ψ = ψ′σ′. Then

∂γΨjψ = π(∂γ↑Ψj)ψ =

(∂γ↑Ψjψ′)σ′ =

Ψjφ(γ↑(φ)ψ′)σ′

ψ′

ψ′ φ

Ψψφ′∗(γ∗(φ′)ψ′/ψ∗)σ′

Ψjφ((γ↑(φ)/ψ∗)ψ′/ψ∗)σ′ =

=

ψ′ φ

ψ′ φ′∈A∗(Φ∗)

∗

(∂γ∗Ψψ

(Jψ∗′/ψ∗)σ′ = (Jψ∗O/ψ∗)σ = (Jψj↑O)σ = Jψj , as required.

=

ψ′/ψ∗)σ′ =

ψ′

ψ′

We will construct Ψ∗ for each ψ∗ as above sequentially using Lemma 4.2 applied to J∗ ∈ γ∗(Φ∗[V ′]) which is valid by Lemma 4.1 and the inductive hypothesis of Lemma 3.18, as A∗ is a (Σ∗)≤-family, Φ∗[V ′] is Σ∗-adapted (by Lemma 2.18) and (ω,h)-extendable (by Lemma 2.12), and

J∗ is θj-bounded, as this is true of Jj and so Jj↑ by Lemma 6.15. Lemma 4.2 will give Ψ∗ that is MjIHθj-bounded, and also provides the option to avoid using any η-bounded sets Bp∗ ⊆ Φ∗[V ′]p for j ≤ p ≤ q − (r − j), which we will deﬁne below so as to maintain boundedness throughout the algorithm. During the construction of Ψj, we say that ψ ∈ Φ is full if

- i. |Im(ψ)| = r with U(Ψj)ψ > 0,
- ii. |Im(ψ)| = r − 1 with U(Ψj)ψ > θj+1n/4 − C0 − 1, or
- iii. |Im(ψ)| = i < r − 1 with more than 2−rηn − C0 − 1 full elements of Φi+1 |ψ. There will be no uses of full sets by Ψj apart from at most U(Jj)ψ ‘forced’ uses of ψ for each


ψ ∈ Φr, and at most C0 + 1 further unforced uses. This implies that for ψ with |Im(ψ)| = i < r, if ψ is not full then Φi+1 |ψ has at most 2−rηn full elements (if i = r − 1 we use θr < 2−rη here).

We claim that there is no full ψ′ ∈ Φ with |Im(ψ′) ∩ V ′| = j − 1. Indeed, suppose we have such ψ′. Let ψa = ψ′[V ′] and ψb = ψ′ \ ψa. Then

(θj+1n/4 − C0 − 1)(2−rηn − C0 − 1)r−1−|Im(ψ′)| < {U(Ψj)ψ : ψ′ ⊆ ψ ∈ Φr−1} = {U(Ψψ∗)ψa : ψb ⊆ ψ∗} < nr−j−|ψb| · MjIHθjn = MjIHθjnr−|Im(ψ′)|,

as all Ψψ∗ are MjIHθj-bounded. This contradicts the deﬁnition of θj+1 and so proves the claim.

When applying Lemma 4.2 to J∗ ∈ γ∗(Φ∗[V ′]) as above, for j ≤ p ≤ q − r + j we let Bp∗ be the set of Im(υ) with υ ∈ Φ∗p[V ′] such that υ ∪ ψ∗′ is full for some ψ∗′ ⊆ ψ∗, and υ′ ∪ ψ∗′ is not full for any υ′ υ, ψ∗′ ⊆ ψ∗. Then |Bp∗(Im(υ))| < ηn for all υ ∈ Φ∗p−1[V ′], by deﬁnition for p > j, and by the claim for p = j. Thus we can apply Lemma 4.2 to obtain some MjIHθj-bounded Ψ∗ = Ψψ∗ ∈ ZA∗(Φ∗[V ′]) with ∂γ∗Ψ∗ = J∗ such that

i. if p > j then U(Ψ∗)ψ ≤ 1 for all ψ ∈ Φp[V ′] and U(Ψ∗)ψ = 0 if Im(ψ) ∈ Bp∗, ii. U(Ψ∗)ψ ≤ U(J∗)ψ + C0 + 1 for all ψ ∈ Φj[V ′], and U(Ψ∗)ψ = U(J∗)ψ if Im(ψ) ∈ Bj∗.

As described above, Ψj is the sum over all such ψ∗ and φ′ ∈ A∗(Φ∗[V ′]) of Ψψφ′∗{φ}, where

![image 40](<2018-keevash-existence-designs_images/imageFile40.png>)

![image 41](<2018-keevash-existence-designs_images/imageFile41.png>)

φ′ = (φ ◦ (σ∗)−1)/ψ∗ for some φ ∈ Aθ(Φ), θ∗ ∈ AθBO, σ∗ = σ∗(θ∗). We claim that Ψj is θj+1/2bounded. To see this, we ﬁx ψ ∈ Φr−1, let ψa = ψ[V ′], ψb = ψ \ ψa and consider cases according to p = |Im(ψa)|.

- i. If p = j − 1 then U(Ψj)ψ = U(Ψψb)ψa < MjIHθjn < θj+1n/2, as Ψψb is MjIHθj-bounded,
- ii. If p > j then U(Ψj)ψ ≤ θj+1n/4 − C0 − 1 before ψ is full, after which U(Ψψ∗)ψa = 0 whenever ψb ⊆ ψ∗, except for at most one such ψ∗ with U(Ψψ∗)ψa ≤ C0 + 1, so U(Ψj)ψ < θj+1n/4 ≤ θj+1n/2.
- iii. If p = j then U(Ψj)ψ ≤ θj+1n/4 −C0 − 1 before ψ is full, after which U(Ψψ∗)ψa = U(Jj)ψa∪ψ∗ whenever ψb ⊆ ψ∗, except for at most one such ψ∗ with U(Ψψ∗)ψa ≤ U(Jj)ψa∪ψ∗ + C0 + 1, so U(Ψj)ψ ≤ θj+1n/4 + U(Jj)ψ ≤ θj+1n/2, as U(Jj)ψ ≤ θjn.


Thus U(Ψj)ψ ≤ θj+1n/2 in all cases, so the claim holds.

It follows that Jj+1 = Jj − ∂Ψj is θj+1-bounded, so the construction can proceed to the next step. We conclude with J′ := Jr ∈ (ZD)Φ[V′]r and Ψ = j Ψj ∈ ZA(Φ), such that J′ and Ψ are ωq−2qhθ-bounded with ∂Ψ = J − J′.

# 7 Applications

In this section we give several applications of our main theorem, including the theorems stated in the introduction of the paper. Most of the applications will follow from a decomposition theorem for hypergraphs in various partite settings. We also give some results on coloured hypergraph decomposition, and a simple illustration (the Tryst Table Problem) of other applications that are not equivalent to hypergraph decomposition, but for the sake of brevity we leave a detailed study of these applications for future research.

Our ﬁrst theorem in this section can be viewed as a simpliﬁed form of Theorem 3.1, in which various general deﬁnitions are specialised to the setting of hypergraph decompositions. To state it we require two deﬁnitions.

- Deﬁnition 7.1. Let Φ be a [q]-complex and H be an r-graph on [q]. We say G ∈ NΦ◦r is (H,c,ω)-


regular in Φ if there are yφ ∈ [ωnr−q,ω−1nr−q] for each φ ∈ Φq with φ(H) ⊆ G so that φ yφφ(H) = (1 ± c)G.

- Deﬁnition 7.2. We say that an R-complex Φ is exactly Σ-adapted if whenever φ ∈ ΦB and τ ∈


Bij(B′,B) we have φ ◦ τ ∈ ΦB′ iﬀ σ ∈ ΣBB′. We say Φ is exactly adapted if Φ is exactly Σ-adapted for some Σ.

- Theorem 7.3. Let H be an r-graph on [q] and Φ be an (ω,h)-extendable exactly adapted [q]-complex

where n = |V (Φ)| > n0(q) is large, h = 250q3, δ = 2−103q5, n−δ < ω < ω0(q) is small and c = ωh20. Suppose G ∈ H(Φ) is (H,c,ω)-regular in Φ and (Φ,G) is (ω,h)-extendable. Then G has an Hdecomposition in Φq.

Proof. Suppose Φ is exactly Σ-adapted, let A = {A} with A = Σ≤, and γ ∈ {0,1}Ar with each γθ = 1Im(θ)∈H. Let G∗ ∈ NΦr with G∗ψ = GIm(ψ) for ψ ∈ Φr. For any φ ∈ A(Φ) = Φq and θ ∈ Ar we have γ(φ)φθ = γθ = 1Im(θ)∈H. As Φ is exactly Σ-adapted, we deduce G ∈ H(Φ) iﬀ G∗ ∈ γ(Φ) , and that an H-decomposition of G is equivalent to a γ(Φ)-decomposition of G∗.

There are two types in γ for each B ∈ [q]r: the edge type {θ ∈ AB : Im(θ) ∈ H} and the nonedge type {θ ∈ AB : Im(θ) ∈/ H}. Each γθ is the all-1 vector for θ in an edge type or the all-0 vector for θ in a nonedge type, so γ is elementary. The atom decomposition of G∗ is G∗ = e∈Φ◦

r

Gee∗, where e∗ψ = 1 for all ψ ∈ Φr with Im(ψ) = e, i.e. e∗ contains all edge types at e.

As G is (H,c,ω)-regular in Φ, we have φ yφφ(H) = (1 ± c)G for some yφ ∈ [ωnr−q,ω−1nr−q] for each φ ∈ Φq with φ(H) ⊆ G. For any such φ we have γ(φ) ≤γ G, so φ ∈ A(Φ,G). Also, for any B ∈ [q]r and ψ ∈ ΦB, writing 1B ∈ TB for the edge type we have ∂1Byψ = φ:t

φ(ψ)=1B yφ = {yφ : Im(ψ) ∈ φ(H)} = (1 ± c)(G∗)1ψB, so G∗ is (γ,c,ω)-regular.

To apply Theorem 3.1, it remains to show that (Φ,γ[G]) is (ω,h)-extendable. We have γ[G] = (γ[G]B : B ∈ Q) where if B ∈/ H then γ[G]B = ΦB and if B ∈ H then γ[G]B = {ψ ∈ ΦB : GIm(ψ) > 0}. Let E = (J,F,φ) be any Φ-extension of rank s and J′ ⊆ Jr \J[F]. As (Φ,G) is (ω,h)-extendable we have XE,J′(Φ,G) > ωnvE. Consider any φ+ ∈ XE,J′(Φ,G). For any ψ ∈ J′ we have φ+ψ ∈ Φ and Im(φ+ψ) ∈ G, so φ+ψ ∈ γ[G]. Thus φ+ ∈ XE,J′(Φ,γ[G]), so (Φ,γ[G]) is (ω,h)-extendable. Now G∗ has a γ(Φ)-decomposition, so G has an H-decomposition.

The following theorem solves the H-decomposition problem in the nonpartite setting (so is similar in spirit to [9]); it is an immediate corollary of Theorem 7.3 with Σ = Sq and Theorem 5.20.

- Theorem 7.4. Let H be an r-graph on [q] and Φ be an (ω,h)-extendable Sq-adapted [q]-complex where n = |V (Φ)| > n0(q) is large, h = 250q3, δ = 2−103q5, n−δ < ω < ω0(q) is small and c = ωh20.


Suppose G is H-divisible and (H,c,ω)-regular in Φ and (Φ,G) is (ω,h)-extendable. Then G has an H-decomposition in Φq.

In the introduction we stated a simpliﬁed form of this result (using typicality rather than extendability and regularity); we now give the deduction. (It will also follow from a later more general result, but we include the proof for the sake of exposition.)

Proof of Theorem 1.5. Let H be an r-graph on [q] and G be an H-divisible (c,hq)-typical r-graph, where n = |V (Φ)| > n0(q), h = 250q3, δ = 2−103q5, d(G) > 2n−δ/hq and c < c0d(G)h30q. We need to show that G has an H-decomposition. Let Φ be the complete [q]-complex on V (G), i.e. each ΦB = Inj(B,V (G)). Then Φ is exactly Sq-adapted.

We claim that (Φ,G) is (ω,h)-extendable with ω = 12d(G)hq. To see this, consider any Φextension E = (J,F,φ) with J ⊆ [q](h) and any J′ ⊆ Jr◦ \ J◦[F]. Write V (J) \ F = {x1,... ,xvE} and suppose for i ∈ [vE] that there are mi edges of J′ that use xi but no xj with j > i. The number of choices for the embedding of each xi given any previous choices is (1 ± mic)d(G)min. Thus XE,J′(Φ,G) > 21d(G)eEnvE > ωnvE, as claimed.

![image 42](<2018-keevash-existence-designs_images/imageFile42.png>)

![image 43](<2018-keevash-existence-designs_images/imageFile43.png>)

Furthermore, if e ∈ G, f ∈ H, J = −→q , F = f, ψ ∈ Bij(f,e) we see that there are (1 ± |H|c)d(G)|H|−1nq−r extensions of ψ to φ ∈ Φq with e ∈ φ(H) ⊆ G. Deﬁning yφ = d(G)1−|H|nr−q for all φ ∈ Φq with φ(H) ⊆ G we see that G is (H,|H|c,ω)-regular in Φ. The theorem now follows from Theorem 7.4.

Our next deﬁnition sets up notation for hypergraph decompositions in a generalised partite setting that incorporates several earlier examples in the paper. It is followed by a theorem that solves the corresponding hypergraph decomposition problem.

Deﬁnition 7.5. Let H be an r-graph on [q] and P = (P1,... ,Pt) be a partition of [q]. Let Σ be the group of all σ ∈ Sq with all σ(Pi) = Pi. Let Φ be an exactly Σ-adapted [q]-complex with parts Q = (Q1,... ,Qt), where each Qi = {ψ(j) : j ∈ Pi,ψ ∈ Φj}. Let G ∈ NΦ◦r.

For S ⊆ [q] the P-index of S is iP(S) = (|S ∩P1|,... ,|S ∩Pt|); similarly, we deﬁne the Q-index of subsets of V (Φ), and also refer to both as the ‘index’. For i ∈ Nt we let Hi and Gi be the (multi)sets of edges in H and G of index i. Let I = {i : Hi = ∅}. We call G an (H,P)-blowup if Gi = ∅ ⇒ i ∈ I.

We say G has a P-partite H-decomposition if it has an H-decomposition using copies φ(H) of H with all φ(Pi) ⊆ Qi.

For e ⊆ V (Φ) we deﬁne the degree vector GI(e) ∈ NI by GI(e)i = |Gi(e)| for i ∈ I. Similarly, for

- f ⊆ [q] we deﬁne HI(f) by HI(f)i = |Hi(f)|. For i′ ∈ Nt let HiI′ be the subgroup of NI generated by {HI(f) : iP(f) = i′}. We say G is (H,P)-divisible if GI(e) ∈ HiI′ whenever iP(e) = i′.


Let G∗ ∈ NΦr with G∗ψ = Ge for ψ ∈ Φr, e = Im(ψ) with iQ(e) ∈ I, and G∗ψ is otherwise undeﬁned. Theorem 7.6. With notation as in Deﬁnition 7.5, suppose n/h ≤ |Qi| ≤ n with n > n0(q) large,

- G is an (H,P)-divisible (H,P)-blowup, G is (H,c,ω)-regular in Φ, and (Φ,G∗) is (ω,h)-extendable,


where h = 250q3, δ = 2−103q5, n−δ < ω < ω0(q) is small and c = ωh20. Then G has a P-partite H-decomposition.

Proof. Let A = Σ≤, H∗ = {θ ∈ Ar : Im(θ) ∈ H} and γθ = 1θ∈H∗ for θ ∈ Ar, Then an (integral) Ppartite H-decomposition of G is equivalent to an (integral) γ(Φ)-decomposition of G∗. By Theorem

- 7.3, it remains to show G ∈ H(Φ) , i.e. G∗ ∈ γ(Φ) = Lγ(Φ) (by Lemma 5.19).


Consider any i ∈ I = {i : Hi = ∅} and i′ ∈ Nt with all i′j ≤ ij. Let mii′ = j∈[t](ij − i′j)!. For any B′ ⊆ B ∈ Q with iP(B′) = i′ and iP(B) = i and ψ′ ∈ ΦB′ with Im(ψ′) = e we have

((G∗)♯ψ′)B) = {G∗ψ : ψ′ ⊆ ψ ∈ ΦB} = mii′|Gi(e)|. Writing O = ψ′Σ, for any ψ ∈ O we have ((G∗)♯ψ)B) = mii′|Gi(e)|. Thus we obtain (G∗)♯ψ from GI(e) by copying coordinates and multiplying all copies of each i-coordinate by mii′.

Similarly, for any θ′ ∈ AB′ with Im(θ′) = f we have (γθ♯′)B) = {γθ : θ′ ⊆ θ ∈ AB} = mii′|Hi(f)|, so γ♯[O] is generated by vectors vf ∈ (ZQ)O where f ⊆ [q] with iP(f) = i′ and for each ψ′ ∈ O, B ∈ Q we have (vψf′)B = mii′|Hi(f)| where i = iP(B). Thus all vectors in γ♯[O] are obtained from vectors in HiI′ by the same transformation that maps GI(e) to ((G∗)♯)O. As G is (H,P)-divisible we deduce ((G∗)♯)O ∈ γ♯[O] for any O ∈ Φ/Σ, as required.

Similarly to the nonpartite setting, which also give a simpliﬁed form of the previous theorem in which we replace extendability and regularity by typicality (which we will generalise here to multigraphs).

Deﬁnition 7.7. With notation as in Deﬁnition 7.5, suppose that Φ is the [q]-complex where each ΦB consists of all maps ψ : B → V (G) with ψ(B ∩Pi) ⊆ Qi for all i ∈ [t]; we call Φ the complete [q]complex wrt (P,Q), and note that Φ is exactly Σ-adapted. For f ∈ Q let |G∗∩Φf| = {G∗ψ : ψ ∈ Φf} and df(G∗) = |G∗ ∩ Φf|/|Φf|.

For any Φ-extension E = (J,F,φ) and J′ ⊆ Jr◦ \J◦[F] let XE,J′(Φ,G) = φ′∈XE(Φ) e∈J′ Gφ′(e). We call G a (c,s)-typical (H,P)-blowup if for every Φ-extension E = (J,F,φ) of rank s and

J′ ⊆ Jr◦ \ J◦[F] we have XE,J′(Φ,G) = (1 ± c)XE(Φ) e∈J′ de(G∗), where for e ∈ Jf◦ we write de(G∗) = df(G∗).

Now we give our theorem on decompositions of typical multigraphs in the generalised partite setting. We note that the case P = ([q]) implies Theorem 1.5 and the case P = ({1},... ,{q}) implies Theorem 1.7.

- Theorem 7.8. Let H be an r-graph on [q] and P = (P1,... ,Pt) be a partition of [q]. Suppose each n/h ≤ |Qi| ≤ n with n > n0(q) and h = 250q3, that δ = 2−103q5, d > 2n−δ/hq and c < c0dh30q, where c0 = c0(q) is small. Let G be an (H,P)-divisible (c,h)-typical (H,P)-blowup wrt Q = (Q1,... ,Qt), such that df(G) > d for all f ∈ H and Ge < d−1 for all e ∈ [n]r. Then G has a P-partite Hdecomposition.


Proof. With notation as in Deﬁnition 7.5, it follows (as in the proof of Theorem 1.5) from the deﬁnition of (c,h)-typical (H,P)-blowup that (Φ,G∗) is (ω,h)-extendable with ω = 12dhq > n−δ. By Theorem 7.6 it remains to show that G is (H,2c,ω)-regular in Φ.

![image 44](<2018-keevash-existence-designs_images/imageFile44.png>)

To see this, ﬁrst note that as G is (H,P)-divisible we have GI(∅) ∈ H0I = HI(∅) , so there is some integer Y such that |Gi| = Y |Hi| for all i ∈ I. For each φ ∈ Φq with φ(H) ⊆ G we let yφ = Y Z−1 f∈H Gφ(f), where Z = j∈[t] |Qj||Pj| f∈H df(G∗). Then yφ ∈ [ωnr−q,ω−1nr−q] for each such φ.

We need to show for any e ∈ Φ◦r that {yφ : e ∈ φ(H)} = (1 ± 2c)Ge. We can suppose Ge = 0, so i = i(e) ∈ I. Let mi = j∈[t] ij!. For any B ∈ Hi there are mi choices of ψ ∈ ΦB with ψ(B) = e. It suﬃces to show for any such B and ψ that {yφ : ψ ⊆ φ} = (1 ± 2c)Ge/(mi|Hi|).

Let E = (−→q ,B,ψ) and J′ = H\{B}. As G is a (c,h)-typical (H,P)-blowup we have XE,J′(Φ,G) = (1 ± c)XE(Φ) f∈J′ df(G∗) = (1 ± 2c)Z/(mi|Gi|), as XE(Φ) = (1 + O(n−1)) j∈[t] |Qj||Pj|−ij and mi|Gi| = |G∗ ∩ ΦB| = dB(G∗)|ΦB| = (1 + O(n−1))dB(G∗) j∈[t] |Qj|ij. Therefore

{yφ : ψ ⊆ φ} = Y Z−1

Gφ(f) = GeY Z−1XE,J′(Φ,G) = (1 ± 2c)Ge/(mi|Hi|).

φ∈XE(Φ) f∈H

Now we will prove several other theorems stated in the introduction for which we gave an equivalent reformulation in terms of hypergraph decompositions in partite settings as above. We start with the existence of resolvable designs, or more generally, resolvable hypergraph decompositions of multigraphs.13 We deduce Theorem 1.1 by applying Theorem 7.9 with H = Kqr and G = λKnr.

- Theorem 7.9. Let H be a vertex-regular r-graph on [q] and G be a vertex-regular H-divisible rmultigraph on [n] where n > n0(q) is large and q | n. Let Φ be a Sq-adapted [q]-complex on V (G). Suppose G is (H,c,ω)-regular in Φ and (Φ,G) is (ω,h)-extendable, where h = 250q3, δ = 2−103q5, n−δ/2h < ω < ω0, c = ωh22. Then G has a resolvable H-decomposition.


Proof. We start by recalling the equivalent partite hypergraph decomposition problem. Let Y be a set of m vertices disjoint from X, where m is the least integer with r m−1 ≥ q|G|/|H|n. Let J be a random (r − 1)-graph on Y with |J| = q|G|/|H|n. Let G′ be the r-multigraph obtained from G by adding as edges (with multiplicity one) all r-sets of the form f ∪ {x} where f ∈ J and x ∈ X. Let

- H′ be the r-graph whose vertex set is the disjoint union of a q-set A = [q] and an (r − 1)-set B, and whose edges consist of all r-sets in A∪B that are contained in H or have exactly one vertex in A. To adopt the notation of Deﬁnition 7.5 we let P = (P1,P2) with P1 = A, P2 = B and Q = (Q1,Q2) with Q1 = X, Q2 = Y . Then G′ is an (H′,P)-blowup and we wish to ﬁnd a P-partite H′-decomposition of G′.


First we check (H′,P)-divisibility. The set of edge indices is I = {(r,0),(1,r − 1)}. We identify NI with N2 by assigning (r,0) to the ﬁrst coordinate and (1,r − 1) to the second. Let i′ ∈ N2. Suppose i′2 > 0. Then H′Ii′ is {(0,0)} unless i′1 ≤ 1 and i′2 ≤ r − 1, in which case H′Ii′ is generated by (0,1) if i′1 = 1 or (0,q) if i′1 = 0. The resulting (H′,P)-divisibility conditions (GI(e) ∈ H′Ii′ whenever iP(e) = i′) are satisﬁed trivially when i′1 = 1 and as q | n when i′1 = 0. Now suppose i′2 = 0. Then H′Ii′ is generated by all (|H(f)|,0) with f ∈ [q]i′

if i′1 > 1 or by (|H(f)|,1) with f ∈ [q]i′

1

if i′1 ≤ 1. If i′1 > 1 then the (H′,P)-divisibility condition is equivalent to the H-divisibility condition that gcdi′

1

(H) divides |G(e)|. For i′1 = 0 we need (|G|,n|J|) to be an integer multiple of (|H|,q), so we require the H-divisibility condition |H| | |G| and also |J| = q|G|/|H|n. For i′1 = 1 we need (|G(x)|,|J|) to be an integer multiple of (rq−1|H|,1) for any x ∈ X (recall that H is vertex-

1

regular), so we require the Kqr-divisibility condition that rq−1|H| divides |G(x)| and also that G is vertex-regular. Therefore G′ is (H′,P)-divisible.

To apply Theorem 7.6, it remains to check extendability and regularity. We let Φ′ be the (A∪B)complex where each Φ′A′∪B′ for A′ ⊆ A, B′ ⊆ B consists of all φ ∈ Inj(A′ ∪ B′,X ∪ Y ) with φ |A′∈ Φ and φ(B′) ⊆ Y . Consider any Φ′-extension E = (J,F,φ) with J ⊆ (A ∪ B)(h) and any J′ ⊆ Jr \ J[F] with JB′ ′ = ∅ ⇒ iP(B′) ∈ I. Let E(A) and J′(A) be obtained by restricting to A(h), and deﬁne E(B) similarly. Then whp XE,J′(Φ′,G′) = (1 + o(1))XE(A),J′(A)(Φ,G)mvE(B), where XE(A),J′(A)(Φ,G) > ωnvE(A) as (Φ,G) is (ω,h)-extendable. As |G| > ωnr we have m ≥ (qω/Q)1/(r−1)n, so XE,J′(Φ′,G′) > ω2h(n + m)vE (say), i.e. (Φ′,G′) is (ω2h,h)-extendable.

For regularity, as G is (H,c,ω)-regular in Φ we can choose yφ ∈ [ωnr−q,ω−1nr−q] for each φ ∈ ΦA with φ(H) ⊆ G with {yφ : e ∈ φ(H)} = (1 ± c)Ge for any e ∈ Xr. We deﬁne yφ′ ′ = yφ′|A((r −1)!|J|)−1 for each φ′ ∈ Φ′A∪B with φ′(B) ∈ J. Then yφ′ ′ ∈ [ω2h(n+m)1−q,ω−2h(n+m)1−q] for all φ′ ∈ Φ′A∪B with φ′(H′) ⊆ G′. For any e ∈ Xr we have {yφ′ ′ : e ∈ φ′(H′)} = {yφ : e ∈ φ(H)} = (1 ± c)G′e.

![image 45](<2018-keevash-existence-designs_images/imageFile45.png>)

13 For the sake of brevity we just consider the case that H is vertex-regular, and leave the computation of the lattice for general H to the reader (if H is not vertex-regular than we need G the diﬀerence between any two vertex degrees in G to be divisible by the gcd of all diﬀerences of vertex degrees in H).

Also, for any e = f ∪ {x} with x ∈ X and f ∈ J, we have

{yφ′ ′ : e ∈ φ′(H′)} = |J|−1 {yφ : x ∈ Im(φ)}

= (|J|rq−1|H|)−1

{yφ : e′ ∈ φ(H)}

x∈e′∈Xr

= (|J|rq−1|H|)−1(1 ± c)|G(x)|.

As G is vertex-regular, |G(x)| = r|G|/n = r|H||J|/q, so {yφ′ ′ : e ∈ φ′(H′)} = 1 ± c = (1 ± c)G′e. Therefore G′ is (H′,c,ω2h)-regular in Φ′.

Next we show the existence of large sets of designs. Again, we ﬁrst consider the more general setting of decompositions of multidesigns into designs.

- Theorem 7.10. Let Φ be a Sq-adapted [q]-complex with V (Φ) = [n] where n > n0(q,λ) is large. Sup-


pose G ∈ NΦ◦q is an r-multidesign with all Ge < ω−1. For all 0 ≤ i ≤ r suppose Zi := λ r q−−ii −1 nr−−ii ∈ Z and Zi | |G(f)| for all f ∈ [n]i. Suppose also that (Φ,G) is (ω,h)-extendable, where h = 250q3, δ = 2−103q5, n−δ/2h < ω < ω0(q,λ). Then G has a decomposition into (n,q,r,λ)-designs.

Proof. We start by recalling the equivalent partite hypergraph decomposition problem. Let Y be a set of m vertices disjoint from X, where m is the least integer with q m−r ≥ |G|/Z0. Let J be a random (q − r)-graph on Y with |J| = |G|/Z0. Let G′ be the q-multigraph obtained from G by adding as edges with multiplicity λ all q-sets of the form e ∪ f with e ⊆ X and f ∈ J. Let H be the q-graph whose vertex set is the disjoint union of a q-set A and a (q − r)-set B, and whose edges consist of A and all q-sets in A ∪ B that contain B. To adopt the notation of Deﬁnition 7.5 we let P = (P1,P2) with P1 = A, P2 = B and Q = (Q1,Q2) with Q1 = X, Q2 = Y . Then G′ is an (H,P)-blowup and we wish to ﬁnd a P-partite H-decomposition of G′.

First we check (H,P)-divisibility. We identify NI with N2 by assigning (q,0) to the ﬁrst coordinate and (r,q − r) to the second. Let i′ ∈ N2. Suppose i′2 > 0. Then HiI′ is {(0,0)} unless i′1 ≤ r and i′2 ≤ q − r, in which case HiI′ is generated by (0, q−i

′ 1

r−i′1 ). The corresponding (H,P)-divisibility condition is Zi′

′ 1

∈ Z. Now suppose i′2 = 0. Then HiI′ is generated by (1,0) if i′1 > r or by (1, q−i

r−i′1 ) if i′1 ≤ r. The corresponding (H,P)-divisibility condition is trivial if i′1 > r. If i′1 ≤ r, for each f ∈ [n]i′

1

′ 1

′ 1

r−i′1 ) to be an integer multiple of (1, q−i

we need (|G(f)|,λ|J| n−i

r−i′1 ), i.e. |G(f)| = |J|Zi′

; this is equivalent to G being an r-multidesign. Therefore G′ is (H,P)-divisible.

1

1

To apply Theorem 7.6, it remains to check extendability and regularity. We let Φ′ be the (A∪B)complex where each Φ′A′∪B′ for A′ ⊆ A, B′ ⊆ B consists of all φ ∈ Inj(A′ ∪ B′,X ∪ Y ) with φ |A′∈ Φ and φ(B′) ⊆ Y . Then (Φ′,G′) is (ω2h,h)-extendable as in the proof of Theorem 7.9. For regularity, we deﬁne yφ = Gφ(A)(q!(q − r)!|J|)−1 for each φ ∈ Φ′A∪B with φ(B) ∈ J. Then yφ ∈ [ω2h(n + m)r−q,ω−2h(n + m)r−q] for all φ ∈ Φ′A∪B with φ(H) ⊆ G′. For any e ∈ Xq we have

{yφ : e ∈ φ(H)} = Ge = G′e. For any e = f ∪ f′ with f ∈ Xr and f′ ∈ J, as G is an r-multidesign

we have |G(f)| = Q nr −1|G| = λ|G|/Z0, so {yφ : e ∈ φ(H)} = (q!(q − r)!|J|)−1q!|G(f)|(q − r)! = |G(f)|Z0/|G| = λ = G′e.

Now we prove the existence conjecture for large sets of designs.

- Proof of Theorem 1.2. First we note that the case that λ is ﬁxed and n > n0(q,λ) is large follows from Theorem 7.10 applied to G = Knq. Now we can assume λ > λ′(q) is large. We let λ0 = ri=1 r q−−ii


and write λ = µλ0 + λ1 for some integers µ,λ1 with 0 ≤ λ1 < λ0. Write Zi := λ r q−−ii −1 nr−−ii and note that by assumption all Zi ∈ Z. Let ℓ = nq /Z0 = λ−1 nq−−rr . It suﬃces to decompose Knq into ℓµ designs with parameters (n,q,r,λ0) and ℓ with parameters (n,q,r,λ1). Indeed, these can then be combined into ℓ designs with parameters (n,q,r,λ).

We start by choosing the ℓ designs with parameters (n,q,r,λ1). We do this by a greedy process, where we start with Knq and repeatedly delete some (n,q,r,λ1)-design. Note that the divisibility conditions for the existence of an (n,q,r,λ1)-design are satisﬁed, namely all r q−−ii | λ1 nr−−ii . At each step of the process we have some q-graph G. We say that a q-set e is full if e ∈ Knq \ G, and for

- i < q that an i-set f is full if it is contained in at least c(q)n full (i + 1)-sets, where we choose 1/λ′(q) ≪ c(q) ≪ 1/h. Once a set is full we will avoid using it.

There can be no full r-set, as this would belong to at least (c(q)n)q−r/(q − r)! full q-sets, but we are only choosing ℓλ1 < λ0λ′(q)−1 nq−−rr such q-sets. Let Φ be the [q]-complex on V (G) where each ΦB consists of all φ ∈ Inj(B,V (G)) such that all subsets of Im(φ) are not full. Then Φ is (1/2,h)-extendable (say), so by Theorem 7.3 we can ﬁnd a Kqr-decomposition of λ1Knr in Φq, i.e. an (n,q,r,λ1)-design avoiding full sets. Thus the algorithm can be completed to choose ℓ designs with parameters (n,q,r,λ1).

Finally, letting Φ and G be as above after the ﬁnal step of the algorithm, (Φ,G) is (1/2,h)-

extendable, G is an r-multidesign, Zi0 := λ0 r q−−ii −1 nr−−ii ∈ Z and Zi0 | |G(f)| for all f ∈ [n]i. By Theorem 7.10 we can decompose G into ℓµ designs with parameters (n,q,r,λ0), as required.

Next we prove the existence of complete resolutions.

Proof of Theorem 1.3. Suppose q is ﬁxed and n > n0(q) is large with n = q mod lcm([q]). We start by recalling the reformulation of complete resolution as a partite hypergraph decomposition problem. We consider disjoint sets of vertices X and Y where |X| = n and Y is partitioned into Yj,

2 ≤ j ≤ q + 1 with |Yj| = nq−−jj+2+2. We let G′ be the q-graph whose edges are all q-sets e ⊆ X ∪ Y such that |e ∩ Yj| ≤ 1 for all 2 ≤ j ≤ q + 1, and if e ∩ Yj = ∅ then e ∩ Yi = ∅ for all i > j. Let H be the q-graph whose vertex set is the disjoint union of two q-sets A and B = {b2,... ,bq+1}, whose edges are all q-sets e ⊆ A ∪ B such that if bj ∈ e then bi ∈ e for all i > j. To adopt the notation of Deﬁnition 7.5 we let P = (P1,... ,Pq+1) and Q = (Q1,... ,Qq+1) with P1 = A, Q1 = X and Pj = {bj}, Qj = Yj for 2 ≤ j ≤ q + 1. Then G′ is an (H,P)-blowup and we wish to ﬁnd a P-partite H-decomposition of G′.

![image 46](<2018-keevash-existence-designs_images/imageFile46.png>)

To apply Theorem 7.6, we consider the complete (A ∪ B)-complex Φ wrt (P,Q). Then (Φ,G′)

is clearly (1/2,h)-extendable (say). Also, every edge of G′ is in exactly nq copies of H, so G′ is (H,c,ω)-regular in Φ for any c > 0 and ω < ω0. It remains to check (H,P)-divisibility.

The set of index vectors of edges is I = {ij : 1 ≤ j ∈ q + 1} ⊆ Nq+1 where ijj′ is 1 for

- j + 1 ≤ j′ ≤ q + 1, ij1 = j − 1 and ijj′ = 0 otherwise. We identify NI with Nq+1 by assigning ij to coordinate j. Consider i′ ∈ Nq+1. We can assume i′j′ ≤ 1 for j′ > 1. If there is any j′ > 1 with i′j′ = 0, we let j0 be the least such j′, otherwise we let j0 = q + 2. We can assume i′1 ≤ j0 − 2,


q−i′1

otherwise HiI′ = 0. Then HiI′ is generated by vi′ ∈ Nq where each vji′ = 1i′

j−1−i′1 . Let ui′ ∈ Nq where each uij′ is 1i′

1+1≤j≤j0−1

n−i′1 j−1−i′1

′

q+1 j∗=j+1 |Yj∗|1−i

j∗. Then the corresponding (H,P)-divisibility condition is that ui′ is an integer multiple of vi′. It suﬃces to consider the case that i′j = 1 for all j ≥ j0, and so each uij′ is 1i′

1+1≤j≤j0−1

n−i′1 j−1−i′1

j0−1 j∗=j+1 |Yj∗|. Then for i′1+1 ≤ j ≤ j0−1

1+1≤j≤j0−1

−1 n−i′1 j−1−i′1

′ 1

j0−1 j∗=j+1 |Yj∗| = j

0−1 j∗=i′1+2

n−j∗+2 q−j∗+2. This is an integer constant

we have uij′/vji′ = q−i

![image 47](<2018-keevash-existence-designs_images/imageFile47.png>)

j−1−i′1

independent of j, as required. Next we solve the Tryst Table Problem.

- Proof of Theorem 1.10. Let Φ be the complete [9]-complex on an n-set V where n is large. Let G∗ ∈ (Z2)Φ3 with all G∗φ = (1,1). Let A = {A} with A = S9≤. Let γ ∈ (Z2)A3 where


- • γθ = (1,0) if Im(θ) = {1,4,7},
- • γθ = (0,1) if Im(θ) = {3i − 2,3i − 1,3i} for some i ∈ [3] and θ(min(Dom(θ))) = 3i − 2,
- • γθ = (0,0) otherwise. The Tryst Table Problem is equivalent to ﬁnding a γ(Φ)-decomposition of G∗.


There are three types in γ for each B ∈ [9]3, where the type of θ is determined by γθ as above, so γ is elementary. The atom decomposition of G∗ is G∗ = e=abc∈[n]

(e1 + ea + eb + ec), where e1ψ is (1,0) for all ψ with Im(ψ) = e otherwise 0, and each exψ for x ∈ e is (0,1) for all ψ with Im(ψ) = e and ψ(min(Dom(ψ))) = x, otherwise 0. (The interpretation of e1 is that e is the set of captains, and of ex is that e is a team with captain x.) As all nonzero γ-atoms at e appear in G∗ we have γ[G] = (γ[G]B : B ∈ [9]3) with each γ[G]B = ΦB, so (Φ,γ[G]) is (ω,h)-extendable for any ω < 1 and n > n0(ω,h). To show regularity of G∗ we let yφ = 1/6(n − 3)6 for all φ ∈ A(Φ) = Φ9. Then for any B ∈ [9]3, ψ ∈ ΦB, t ∈ TB we have ∂tyφ = 6(n − 3)6|{φ : tφ(ψ) = t}| = 1, where the factor of 6 either represents all bijections from {1,4,7} to e = Im(ψ), or all bijections from {3i − 2,3i − 1,3i} to e mapping 3i−2 to some x ∈ e, where x is ﬁxed and i ranges over [3]. Therefore G∗ is (γ,c,1/7)-regular in Φ for any c > 0.

3

To apply Theorem 3.1, it remains to show that G∗ ∈ γ(Φ) = Lγ(Φ) (by Lemma 5.19). Fix any O ∈ Φ/S9, write e = Im(O) ∈ Φ◦ and i = |e|. Then ((G∗)♯)O ∈ (Z2)[9]3×O is a vector supported on the coordinates (B,ψ′) with B′ ⊆ B ∈ [9]3 and ψ′ ∈ O ∩ ΦB′ in which every nonzero coordinate is equal: we have ((G∗)♯ψ′)B) = {G∗ψ : ψ′ ⊆ ψ ∈ ΦB} = (n − i)3−i(1,1).

We need to show ((G∗)♯)O ∈ γ♯[O] . First consider the case i = 3. Then it is clear that ((G∗)♯)O is the sum of the γ♯-atoms at O, as these are obtained from the γ-atoms e1, ea, eb, ec described above by identifying each ψ with (B,ψ) where ψ ∈ ΦB.

Now suppose i = 2, say Im(O) = e = ab. There are four γ♯-atoms at O, which we label eab = γ♯(1 → a,4 → b) (a and b are captains), ea = γ♯(1 → a,2 → b) (a captains a team containing b), eb = γ♯(1 → b,2 → a) (b captains a team containing a), e0 = γ♯(2 → a,3 → b) (a and b are in the same team, neither is the captain).

To calculate eab, consider any θ′ ∈ A2 with θ′(x) = 1, θ′(y) = 4 and ψ′ ∈ Φ2 with ψ′(x) = a, ψ′(y) = b. Then eabψ′ = γθ♯′, so each (eabψ′)xyz = {γθ : θ′ ⊆ θ ∈ Axyz} = γx→1,y→4,z→7 = (1,0).

Next, if θ′ ∈ A2 with θ′(x) = 1, θ′(y) = 2 and ψ′ ∈ Φ2 with ψ′(x) = a, ψ′(y) = b then each (eaψ′)xyz = {γθ : θ′ ⊆ θ ∈ Axyz} = γx→1,y→2,z→3 is (0,1) if x = min{x,y,z} or (0,0) otherwise. Similarly, (ebψ′)xyz is (0,1) if y = min{x,y,z} or (0,0) otherwise.

Finally, if θ′ ∈ A2 with θ′(x) = 2, θ′(y) = 3 and ψ′ ∈ Φ2 with ψ′(x) = a, ψ′(y) = b then each (eaψ′)xyz = {γθ : θ′ ⊆ θ ∈ Axyz} = γz→1,x→2,y→3 is (0,1) if z = min{x,y,z} or (0,0) otherwise.

Therefore ((eab+ea+eb+e0)ψ′)xyz = (1,1) for every ψ′ ∈ O and xyz ∈ [9]3, so ((G∗)♯)O ∈ γ♯[O] . Now suppose i = 1, say Im(O) = a. There are two γ♯-atoms at O, which we label a1 = γ♯(1 → a)

(a is a captain), a0 = γ♯(2 → a) (a is not a captain).

Consider any θ′ ∈ A1 with θ′(x) = 1 and ψ′ ∈ Φ1 with ψ′(x) = a. Then each (a1ψ′)xyz = {γθ : θ′ ⊆ θ ∈ Axyz} is (2,2) if x = min{x,y,z} or (2,0) otherwise.

Next consider any θ′ ∈ A1 with θ′(x) = 2 and ψ′ ∈ Φ1 with ψ′(x) = a. Then each (a0ψ′)xyz = {γθ : θ′ ⊆ θ ∈ Axyz} is (0,0) if x = min{x,y,z} or (0,2) otherwise.

Therefore ((a1 + a0)ψ′)xyz = (2,2) for every ψ′ ∈ O and xyz ∈ [9]3. As each ((G∗)♯ψ′)xyz = (n(n − 1),n(n − 1)) we have ((G∗)♯)O ∈ γ♯[O] .

Finally, γ♯[∅] is generated by a vector v with all (v∅)B = (6,6). As ((G∗)♯∅)B = (n(n − 1)(n − 2),n(n − 1)(n − 2)) we have (G∗)♯∅ ∈ γ♯[∅].

Now we consider the more general setting of coloured hypergraph decompositions. We require some deﬁnitions. Deﬁnition 7.11. Suppose H is an r-graph on [q], edge-coloured as H = ∪d∈[D]Hd. We identify H with a vector H ∈ (ND)Q, where each (Hf)d = 1f∈Hd.

Let Φ be a [q]-complex. For φ ∈ Φq we deﬁne φ(H) ∈ (ND)Φ◦r by φ(H)φ(f) = Hf. Let H be an family of [D]-edge-coloured r-graphs on [q]. Let H(Φ) = {φ(H) : φ ∈ Φq,H ∈ H}.

We say G ∈ (ND)Φ◦r is (H,c,ω)-regular in Φ if there are yφH ∈ [ωnr−q,ω−1nr−q] for each H ∈ H, φ ∈ Φq with φ(H) ≤ G so that {yφHφ(H)} = (1 ± c)G.

We say that (Φ,G) is (ω,h)-extendable if (Φ,G′) is (ω,h)-extendable, where G′ = (G1,... ,GD) with each Gd = {e ∈ Φ◦r : (Ge)d > 0}.

The following generalises Theorem 7.3 by allowing colours and also families of hypergraphs.

Theorem 7.12. Let H be an family of [D]-edge-coloured r-graphs on [q]. Let Φ be an (ω,h)extendable exactly adapted [q]-complex where n = |V (Φ)| > n0(q,D) is large, h = 250q3, δ = 2−103q5, n−δ < ω < ω0(q,D) is small and c = ωh20. Suppose G ∈  H(Φ) is (H,c,ω)-regular in Φ and (Φ,G) is (ω,h)-extendable. Then G has an H-decomposition in Φq.

Proof. We follow the proof of Theorem 7.3, with appropriate modiﬁcations for the more general setting. Suppose Φ is exactly Σ-adapted and let A = {AH : H ∈ H} with each AH = Σ≤. Let γ ∈ (ZD)Ar with γθ = ed if θ ∈ AHr , H ∈ H, d ∈ [D] with Im(θ) ∈ Hd or γθ = 0 otherwise. Let G∗ ∈ (ND)Φr with G∗ψ = GIm(ψ) for ψ ∈ Φr. Then G ∈  H(Φ) iﬀ G∗ ∈ γ(Φ) , and an H-decomposition of G is equivalent to a γ(Φ)-decomposition of G∗.

There are D + 1 types in γ for each B ∈ [q]r: the colour d type {θ ∈ AHB : Im(θ) ∈ Hd,H ∈ H}

for each d ∈ [D], and the nonedge type {θ ∈ AHB : Im(θ) ∈/ H ∈ H}. Each γθ is ed in all coordinates for θ in a colour d type or 0 in all coordinates for θ in a nonedge type, so γ is elementary. The atom

decomposition of G∗ is G∗ = f∈Φ◦

r d∈[D](Gf)dfd, where fψd = ed for all ψ ∈ Φr with Im(ψ) = f, i.e. fd contains all colour d types at f.

As G is (H,c,ω)-regular in Φ we have {yφHφ(H)} = (1 ± c)G for some yφH ∈ [ωnr−q,ω−1nr−q] for each H ∈ H, φ ∈ Φq with φ(H) ≤ G. For any such φ ∈ H(Φ) we have γ(φ) ≤γ G, so φ ∈ A(Φ,G). We deﬁne yφ = yφH for φ ∈ AH(Φ). Then for any B ∈ [q]r, ψ ∈ ΦB and d ∈ [D], writing td ∈ TB for the colour d type we have ∂tdyψ = φ:t

φ(ψ)=td yφ = {yφH : Im(ψ) ∈ φ(Hd),H ∈ H} = (1±c)(G∗)tψd, so G∗ is (γ,c,ω)-regular.

To apply Theorem 3.1, it remains to show that each (Φ,γ[G]H) is (ω,h)-extendable. If B ∈/ H then γ[G]HB = ΦB and if B ∈ Hd for d ∈ [D] then γ[G]HB = {ψ ∈ ΦB : Im(ψ) ∈ Gd}. Let E = (J,F,φ) be any Φ-extension of rank s and J′ ⊆ Jr \ J[F]. Let J′′ = (Jd : d ∈ [D]) where each Jd = {JB′ : B ∈ Hd}. As (Φ,G) is (ω,h)-extendable we have XE,J′′(Φ,G) > ωnvE. Consider any φ+ ∈ XE,J′′(Φ,G). For any ψ ∈ Jd we have φ+ψ ∈ Φ and Im(φ+ψ) ∈ Gd, so φ+ψ ∈ γ[G]H. Thus

φ+ ∈ XE,J′(Φ,γ[G]H), so (Φ,γ[G]H) is (ω,h)-extendable. Now G∗ has a γ(Φ)-decomposition, so G has an H-decomposition.

We conclude by applying Theorem 7.12 to the two results on rainbow clique decompositions stated in the introduction.

- Proof of Theorem 1.11. We apply Theorem 7.12 with G = [ qr ]Knr and H equal to the set of

all rainbow [ qr ]-colourings of Kqr. We let Φ be the complete [q]-complex on [n] and note that G is (H,c,ω)-regular in Φ and (Φ,G) is (ω,h)-extendable for any c > 0 and some ω = ω(q).

It remains to check G ∈  H(Φ) . Let G∗ and γ be as in the proof of Theorem 7.12. We need to show G∗ ∈ γ(Φ) = Lγ(Φ) (by Lemma 5.19), i.e. ((G∗)♯)O ∈ γ♯[O] for any O ∈ Φ/Sq.

Fix any O ∈ Φ/Sq, write e = Im(O) ∈ Φ◦ and i = |e|. Then ((G∗)♯)O ∈ ((ZQ)Q)O = (ZQ)Q×O is a vector supported on the coordinates (B,ψ′) with B′ ⊆ B ∈ Q and ψ′ ∈ O ∩ ΦB′ with each ((G∗)♯ψ′)B) = {G∗ψ : ψ′ ⊆ ψ ∈ ΦB} ∈ ZQ equal to (r − i)! nr−−ii in each coordinate. Also, γ♯[O] is generated by γ♯-atoms γ♯(υ) at O, each of which is supported on the same coordinates (B,ψ′) as ((G∗)♯)O, with each (γ♯(υ)ψ′)B) equal to some (r − i)!v in each coordinate, where v ∈ {0,1}Q is any vector with B vB = r q−−ii .

To see that ((G∗)♯)O ∈ γ♯[O] we write ((G∗)♯)O as the sum of r q−−ii −1 qr nr−−ii atoms at O, where we choose the support of the vectors v cyclically: to be formal, identify Q with Z/QZ and assign the jth atom the vector in {0,1}Z/QZ with support {j qr−−ii + x : x ∈ [ r q−−ii ]}.

- Proof of Theorem 1.12. The proof is the same as that of Theorem 1.11, except for the veriﬁcation of ((G∗)♯)O ∈ γ♯[O] for any O ∈ Φ/Sq. The generators γ♯[O] are vectors of the same form as before


except that now v must be a row of the inclusion matrix Mir(q) (discussed after the statement of the theorem). To see that ((G∗)♯)O ∈ γ♯[O] , we note that the sum σO of all γ♯-atoms at O is supported

(as before) on the coordinates (B,ψ′) with B′ ⊆ B ∈ Q and ψ′ ∈ O ∩ ΦB′, with each coordinate equal to the vector in ZQ that is (r −i)! ri in each coordinate. Recalling that ((G∗)♯)O has the same description with ri replaced by nr−−ii , we have ((G∗)♯)O = ri −1 nr−−ii σO.

# References

- [1] Zs. Baranyai, On the factorization of the complete uniform hypergraph, in: Inﬁnite and ﬁnite sets, Colloq. Math. Soc. Ja´nos Bolyai, Vol. 10, North-Holland, Amsterdam, (1975), 91–108.
- [2] B. Barber, D. Ku¨hn, A. Lo and D. Osthus, Edge-decompositions of graphs with high minimum degree, Adv. Math. 288:337–385 (2016).
- [3] B. Barber, D. Ku¨hn, A. Lo, R. Montgomery and D. Osthus, Fractional clique decompositions of dense graphs and hypergraphs, J. Combin. Theory Ser. B 127:148–186 (2017).
- [4] P. Bennett and T. Bohman, A natural barrier in random greedy hypergraph matching, arXiv:1210.3581.
- [5] C.J. Colbourn and J.H. Dinitz, Handbook of Combinatorial Designs, 2nd ed. Chapman & Hall / CRC, Boca Raton (2006).
- [6] A. Ferber, R. Hod, M. Krivelevich and B. Sudakov, A construction of almost Steiner systems, J. Combin. Designs 22:488–494 (2014).


- [7] P. Frankl and V. Ro¨dl, Near perfect coverings in graphs and hypergraphs, Europ. J. Combin. 6:317–326 (1985).
- [8] S. Glock, D. Ku¨hn, A. Lo and D. Osthus, The existence of designs via iterative absorption, arXiv:1611.06827.
- [9] S. Glock, D. Ku¨hn, A. Lo and D. Osthus, Hypergraph F-designs for arbitrary F, arXiv:1706.01800.
- [10] D. H. Gottlieb, A certain class of incidence matrices, Proc. Amer. Math. Soc. 17:1233–1237

(1966).

- [11] D.A. Grable, More-than-nearly perfect packings and partial designs, Combinatorica 19:221–239

(1999).

- [12] J.E. Graver and W.B. Jurkat, The module structure of integral designs, J. Combin. Theory Ser. A 15:75–90 (1973).
- [13] T. Gustavsson, Decompositions of large graphs and digraphs with high minimum degree, Doctoral Dissertation, University of Stockholm, 1991.
- [14] J. Kahn, A linear programming perspective on the Frankl-Ro¨dl-Pippenger Theorem, Random Struct. Alg. 8:149–157 (1996).
- [15] P. Keevash, The existence of designs, arXiv:1401.3665.
- [16] P. Keevash, Counting designs, to appear in J. Eur. Math. Soc.
- [17] P. Keevash and R. Mycroft, A geometric theory for hypergraph matchings, Mem. Amer. Math. Soc. 233 (2014), monograph 1098.
- [18] G. Kuperberg, S. Lovett and R. Peled, Probabilistic existence of regular combinatorial objects, Geom. Funct. Anal. 27:919–972 (2017). Preliminary version in Proc. 44th ACM STOC (2012).
- [19] M. Kwan, Almost all Steiner triple systems have perfect matchings, arXiv:1611.02246.
- [20] E.R. Lamken and R.M. Wilson, Decompositions of Edge-Colored Complete Graphs, J. Combin. Theory Ser. A 89:149–200 (2000).
- [21] N. Linial and Z. Luria, An upper bound on the number of high-dimensional permutations, Combinatorica, 34:471–486 (2014).
- [22] S. Lovett, S. Rao and A. Vardy, Probabilistic Existence of Large Sets of Designs, arXiv:1704.07964.
- [23] Z. Luria, New bounds on the number of n-queens conﬁgurations, arXiv:1705.05225.
- [24] E.H. Moore, Tactical Memoranda I–III, Amer. J. Math. 18:264–303 (1896).
- [25] C.St.J.A. Nash-Williams, An unsolved problem concerning decomposition of graphs into triangles, Combinatorial Theory and its Applications III, North Holland (1970), 1179–1183.
- [26] D.K. Ray-Chaudhuri and R.M. Wilson, Solution of Kirkman’s schoolgirl problem, Proc. Sympos. Pure Math., American Mathematical Society, XIX:187–203 (1971).


- [27] D.K. Ray-Chaudhuri and R.M. Wilson, The existence of resolvable designs, in: A Survey of Combinatorial Theory, North-Holland, Amsterdam, 1973.
- [28] V. Ro¨dl, On a packing and covering problem, Europ. J. Combin. 6:69–78 (1985).
- [29] L. Teirlinck, A completion of Lu’s determination of the spectrum of large sets of disjoint Steiner triple systems, J. Combin. Theory Ser. A 57:302–305 (1991).
- [30] R. Wilson, The early history of block designs, Rend. del Sem. Mat. di Messina 9:267–276 (2003).
- [31] R.M. Wilson, An existence theory for pairwise balanced designs I. Composition theorems and morphisms, J. Combin. Theory Ser. A 13:220–245 (1972).
- [32] R.M. Wilson, An existence theory for pairwise balanced designs II. The structure of PBD-closed sets and the existence conjectures, J. Combin. Theory Ser. A 13:246–273 (1972).
- [33] R.M. Wilson, An existence theory for pairwise balanced designs III. Proof of the existence conjectures, J. Combin. Theory Ser. A 18:71–79 (1975).
- [34] R.M. Wilson, The necessary conditions for t-designs are suﬃcient for something, Utilitas Math. 4:207–215 (1973).
- [35] R.M. Wilson, Signed hypergraph designs and diagonal forms for some incidence matrices, Des. Codes Cryptogr. 17:289–297 (1999).
- [36] R.M. Wilson, Nonisomorphic Steiner Triple Systems, Math. Zeit. 135:303–313 (1974).


