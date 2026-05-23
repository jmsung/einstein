# arXiv:1804.07673v2[math.CO]22Dec2018

## TURÁN’S THEOREM FOR THE FANO PLANE

LOUIS BELLMANN AND CHRISTIAN REIHER

Abstract. Conﬁrming a conjecture of Vera T. Sós in a very strong sense, we give a complete solution to Turán’s hypergraph problem for the Fano plane. That is we prove for n ě 8 that among all 3-uniform hypergraphs on n vertices not containing the Fano plane there is indeed exactly one whose number of edges is maximal, namely the balanced, complete, bipartite hypergraph. Moreover, for n “ 7 there is exactly one other extremal conﬁguration with the same number of edges: the hypergraph arising from a clique of order 7 by removing all ﬁve edges containing a ﬁxed pair of vertices.

For suﬃciently large values n this was proved earlier by Füredi and Simonovits, and by Keevash and Sudakov, who utilised the stability method.

§1. Introduction

With his seminal work [22], Turán initiated extremal graph theory as a separate subarea of combinatorics. After proving his well known extremal result concerning graphs not containing a clique of ﬁxed order, he proposed to study similar problems for graphs arising from platonic solids and for hypergraphs. For instance, given a 3-uniform hypergraph F and a natural number n, there arises the question to determine the largest number expn,Fq of edges that a 3-uniform hypergraph H can have without containing F as a subhypergraph.

Here a 3-uniform hypergraph H “ pV,Eq consists of a set V of vertices and a collection E Ď V p3q “ te Ď V : |e| “ 3u of 3-element subsets of V , that are called the edges of H. Since all hypergraphs occurring in this article are 3-uniform, we will henceforth abbreviate the terminology and just say “hypergraph” when we mean “3-uniform hypergraph.”

Despite tremendous eﬀorts over the last 70 years, our knowledge about these Turán functions n ÞÝÑ expn,Fq is very limited, even for very innocent looking hypergraphs F such as the tetrahedron F “ K4p3q. It is thus customary to focus on the Turán densities

expn,Fq `n

πpFq “ nlimÑ8

˘ ,

3

the existence of which follows from the fact that the sequences n ÞÝÑ expn,FqL`n

˘

are, by a result of Katona, Nemetz, and Simonovits [9], monotonically decreasing. These Turán densities are not understood very well either and all one knows in this regard about the

3

2010 Mathematics Subject Classiﬁcation. 05C65, 05D05. Key words and phrases. Turán’s hypergraph problem, Fano plane. The second author was supported by the European Research Council (ERC grant PEPCo 724903).

1

tetrahedron are the estimates

`

˘ ď 0.5616. (1.1)

K4p3q

5

9 ď π

The lower bound follows from an explicit construction due to Turán himself (see e.g. [4]), which is widely believed to be optimal. As observed by Brown [2] and Kostochka [12] there is for each ﬁxed n a large number of K4p3q-free hypergraphs with the same number of edges that is conjecturally extremal. It is often speculated that this non-uniqueness of the extremal conﬁguration is responsible for the enormous diﬃculty of the problem. The upper bound in (1.1) was established by Razborov [18] by means of his ﬂag algebraic approach introduced in [17].

Vera T. Sós proposed to study Turán’s hypergraph problem in the special case where

- F “ F is the Fano plane, i.e., the projective plane over the ﬁeld with two elements. More precisely, one takes F to be the hypergraph with 7 vertices, which are the points of the Fano plane, and whose 7 edges correspond to the lines of the Fano plane (see Fig. 1.1).


Figure 1.1. Fano plane

One veriﬁes easily that no matter how the vertices of the Fano plane get coloured with two colours, there will always be a monochromatic edge; this fact suggests that bipartite hypergraphs could be relevant to the problem under discussion. Given a natural number n, we denote the balanced, complete, bipartite hypergraph on n vertices by Bn. This hypergraph is deﬁned so as to have a partition V pBnq “ X ¨YY of its n-element vertex set with ˇ|X| ´ |Y |ˇ ď 1 such that a triple e Ď V pBnq forms an edge of Bn if and only if it intersects both X and Y . The above observation on vertex colourings implies F Ę Bn and, hence, that expn,Fq ě bpnq, where

bpnq “ ˆ

˙ ´ ˆ

˙ ´ ˆ

˙

tn{2u 3

tpn ` 1q{2u 3

n 3

denotes the number of edges of Bn. This number rewrites more conveniently as

$ &

n ´ 2 2 ¨ Z

^ “

1

8n2pn ´ 2q if n is even,

n2 4

(1.2)

bpnq “

1

8pn2 ´ 1qpn ´ 2q if n is odd.

%

Sós conjectured this construction to be optimal, i.e., that expn,Fq “ bpnq (1.3)

and that, moreover, Bn is the unique n-vertex hypergraph with bpnq edges not containing a Fano plane. According to Füredi [6], this conjecture of Sós was widely known since the 1970’s. In her problem and survey article [21], which often serves as a reference for this problem, she discusses several connections between design theory and extremal hypergraph theory, even though (1.3) does not seem to be mentioned there.

The ﬁrst result in this direction is due to de Caen and Füredi [3], who proved that

πpFq “ 43 holds for the Fano plane F. Their article introduced the so-called link multigraph method on which all further progress on Sós’s conjecture is based, and which has since

then found many further applications (see e.g. [10, 15]). A few years later it turned out that by combining the work in [3] with Simonovits’ stability method [20] one can prove (1.3) for all suﬃciently large n. This was done by Füredi and Simonovits in [8] and, independently, by Keevash and Sudakov in [11]. It is not straightforward to extract optimal quantitative information from either of those articles, but it seems safe to say that following [8] closely (1.3) would be hard to show for all n ě 10100 and easy for n ě 10300, while the arguments in [11] would probably require n to be larger than 10900.

The main result of the present work proves (1.3) for all n ě 7. Furthermore, we show that for n ě 8 the balanced, complete, bipartite hypergraph is indeed the only extremal conﬁguration. For n “ 7, however, there is a second extremal example, which is the hypergraph J7 remaining from the complete hypergraph K7p3q when one deletes all ﬁve edges involving a ﬁxed pair of vertices. Plainly J7 has

`7

˘´5 “ 30 “ bp7q edges and F Ę J7 follows from the fact that in the Fano plane every pair of points determines a line. Theorem 1.1. For every integer n ě 7 we have

3

^,

n ´ 2 2 ¨ Z

n2 4

expn,Fq “ bpnq “

where F denotes the Fano plane. Moreover, for n ě 8 the only extremal hypergraph is the balanced, complete, bipartite hypergraph Bn, while for n “ 7 there are exactly two extremal hypergraphs, namely B7 and J7.

We would like to point out that this result does not supersede the earlier works [8,11]. This is because they also prove the stability result that every large hypergraph with density 34 ´ op1q not containing a Fano plane has to look “almost” like Bn.

The proof of Theorem 1.1 proceeds by induction on n and uses the link multigraph method. Let us mention for completeness that for n ď 6 one trivially has expn,Fq “ `n

˘

, the unique extremal conﬁguration being the complete hypergraph Knp3q.

3

Organisation. We prove Theorem 1.1 in Section 4. Some auxiliary considerations dealing with small hypergraphs and inductive characterisations of balanced, complete, bipartite hypergraphs are gathered in Section 2. The results on multigraphs we shall require are developed in Section 3.

§2. Preliminaries

- 2.1. Tetrahedra. The n-vertex hypergraphs we need to deal with in the proof of our main result will have bpnq edges and, hence, an edge density of 34 ` op1q. In view of (1.1) such hypergraphs contain tetrahedra provided that n is suﬃciently large. Later on it will be important to know that this actually holds for small values of n as well, which can be seen by means of the following well-known, elementary argument.

Starting from the obvious fact ex

`

4,K4p3q

˘ “ 3 one uses the monotonicity of the sequence

n ÞÝÑ

ex

`

n,K4p3q

˘ `n

3

˘

in order to obtain

ex

`

n,K4p3q

˘ ď

- 3

- 4


ˆ

n 3

˙

for every n ě 4. Together with the estimate ˆ

- 3

- 4


n 3

˙ “

npn ´ 1qpn ´ 2q 8 ă

pn ` 1qpn ´ 1qpn ´ 2q 8

(1.2)

ď bpnq,

which holds for all n ě 3, this leads to the following statement. Fact 2.1. For n ě 4, every hypergraph on n vertices with bpnq edges contains a tetrahedron.

- 2.2. Finding Fano planes. This subsection discusses two ways of looking at the Fano plane F that turn out to be helpful for realising that a given hypergraph H contains a copy of F.


The ﬁrst of them goes back to the work of de Caen and Füredi [3] and reappeared in all subsequent articles addressing the Turán problem for the Fano plane. Given a vertex x of an arbitrary hypergraph H one may form its so-called link graph with vertex set V pHq in which two vertices u and v are declared to be adjacent if and only if the triple uvx is an edge of H. Now the simple yet important observation one frequently uses is that if xyz denotes an arbitrary edge of the Fano plane F, then the six further edges of F correspond to certain edges of the link graphs of x, y, and z. Moreover, these edges in the link graphs use four vertices only and they form a conﬁguration which has, for obvious reasons, been called “three crossing pairs” in [8] (see Fig. 2.1).

Another way of locating Fano planes in dense hypergraphs focuses on the link graph of a single vertex. Plainly, every vertex x of the Fano plane F belongs to three edges of F, which correspond to a perfect matching M in the link graph of x restricted to the six remaining vertices of F. There are four further edges in F forming a certain tripartite hypergraph P, whose partition classes are given by M. Owing to its connection with Pasch’s axiom in the axiomatic approach to planar Euclidean geometry (see [16, §2, Grundsatz IV]), P is often called the Pasch hypergraph (see Fig. 2.2).

z

y

x

(a) Fano plane

| |
|---|


(b) Crossing pairs

Figure 2.1. The edge xyz and the link graphs of x, y, and z.

This perspective on the Fano plane is especially useful when combined with the stability method, for the Pasch hypergraph is known to have vanishing Turán density—a fact exploited both in [8] and in [11]. In the present work, the Pasch hypergraph plays a much less prominent role and it will only be mentioned in the proof of Lemma 2.3 below.

x

Figure 2.2. The Pasch hypergraph contained in the Fano plane.

- 2.3. Small hypergraphs. In this subsection we gather several auxiliary statements addressing hypergraphs on 7 or 8 vertices. We begin with the case n “ 7 of Theorem 1.1, which will later constitute the start of an induction.


- Lemma 2.2. Every hypergraph with 7 vertices and 30 edges not containing a Fano plane is isomorphic to either B7 or J7.


Proof. Let H be such a hypergraph with vertex set r7s and write H for its complement, which has 5 edges.

For every permutation π in the symmetric group S7 we denote the number of triples among

πp1qπp2qπp3q, πp3qπp4qπp5q, πp1qπp5qπp6q, πp1qπp4qπp7q, πp3qπp6qπp7q, πp2qπp5qπp7q, and πp2qπp4qπp6q,

which are edges of H, by Apπq. As these seven triples form a Fano plane, the number Apπq cannot vanish for any π P S7, wherefore

ÿ

Apπq ě |S7| “ 7!.

πPS7

On the other hand, every edge of H appears in the above list for precisely 7¨3!¨4! “ 7!{5 permutations π and a double-counting argument yields

ÿ

Apπq “ 7!5 ¨ epHq “ 7!.

πPS7

For these reasons, we have Apπq “ 1 for every π P S7. If H would have two edges intersecting in a single vertex, then an appropriate permutation π P S7 would satisfy Apπq ě 2, which has just been proved to be false. Therefore, any two distinct edges of H are either disjoint or they intersect in a pair.

(a) B7 (b) J7

Figure 2.3. Possibilities for H.

A quick case analysis discloses that there are only two hypergraphs on 7 vertices with 5 edges having this property, namely the disjoint union of a tetrahedron and a single edge (see Fig. 2.3a), and the hypergraph whose edges are the ﬁve triples containing a ﬁxed pair of vertices (see Fig. 2.3b). In the former case H is isomorphic to B7 and in the latter case one has H – J7.

The next lemma analyses certain Fano-free hypergraphs on 7 vertices with possibly only 29 edges. It will allow us later to exclude several conﬁgurations on six vertices in a hypothetical minimal counterexample to Theorem 1.1. In its proof we exploit that every graph on six vertices with eleven edges contains a perfect matching. Moreover, the unique graph on six vertices with ten edges not containing a perfect matching consist of a K5 plus an isolated vertex. Both facts can either be proved by a direct case analysis based on Tutte’s 1-factor theorem [23] or by plugging n “ 6 and β “ 2 into [1, Corollary II.1.10]

- Lemma 2.3. Let H be a hypergraph on 7 vertices not containing a Fano plane. If some vertex v of H satisﬁes dpvq ě 11 and epH vq ě 18, then H v is isomorphic to B6.


Proof. Set K “ V pHq tvu and let L denote the link graph of v restricted to K. It has 6 vertices and at least 11 edges, and thus it contains a perfect matching M, say with edges x1x2, x3x4, x5x6.

Notice that the complement H‹ of H v has at most two edges. Assuming indirectly that H v is not isomorphic to B6 we know that this complement does not consist of two disjoint edges and thus there is a vertex, say x6, belonging to all edges of H‹. In other words, tx1,...,x5u is a clique of order 5 in H.

- x1
- x2 x4


x3 x5

K

| | |
|---|---|


v

M

x6

Figure 2.4. The matching M in the link of v and two Pasch hypergraphs (drawn red and blue).

Now both

- x1x3x5, x1x4x6, x2x3x6, x2x4x5 and
- x2x4x6, x2x3x5, x1x4x5, x1x3x6 are edge conﬁgurations forming Pasch hypergraphs that together with the matching M in the link of v would yield a Fano plane (see Figure 2.4). Thus both of the above disjoint rows contain a triple which fails to be an edge of H. On the other hand the complement H‹ has already been observed to possess have at most two edges.


So without loss of generality we may suppose that the edges of H‹ are x1x4x6 and x2x4x6. Now x1 and x2 are the only vertices of H‹ having degree 1. If there were a diﬀerent perfect matching M1 in L not pairing these two vertices with each other, we could repeat the entire argument with M1 in place of M and would thus ﬁnd a Fano plane in H.

This shows that all perfect matchings of L use the edge x1x2. Hence the graph L x1x2 with 6 vertices and at least 10 edges has no perfect matchings at all, which is only possible if this graph consists of a K5 and an isolated vertex. As the edge x1x2 cannot belong to this K5, the isolated vertex must be either x1 or x2. In both cases

x1x2, x3x5, x4x6 is a perfect matching in L. Together with the Pasch hypergraph

x1x3x4, x1x5x6, x2x3x6, x2x4x5 it leads to a Fano plane in H, which contradicts the hypothesis. Thus we have indeed pH vq – B6.

Finally, the last statement of this subsection will allow us later to eliminate a somewhat annoying case that arises in the induction step from 7 to 8 due to the non-uniqueness of the extremal hypergraph on 7 vertices.

Fact 2.4. Let H be a hypergraph on 8 vertices not containing a Fano plane. If K6p3q Ď H, then epHq ď 46 ă bp8q.

Proof. Write V pHq “ K Y tx,yu, where K induces a K6p3q in H. By Lemma 2.3 applied to H y there are at most 10 edges containing x but not y. Similarly, there are at most 10 edges containing y but not x. Finally, H can have at most |K| “ 6 edges containing both x and y. So altogether we have indeed

epHq ď 20 ` 10 ` 10 ` 6 “ 46 ă 48 “ bp8q.

- 2.4. Characterisations of Bn. In our inductive proof of Theorem 1.1 we will consider a hypergraph H on some number n ě 8 of vertices with bpnq edges and F Ę H. These assumptions will be shown to entail some strong structural properties of H and the purpose


of this subsection is to check that we can actually conclude H – Bn from those properties. This is much easier when the number of vertices is even.

- Lemma 2.5. Suppose that n ě 6 is even and that H is a hypergraph on n vertices. If for every vertex v of H the hypergraph H v is isomorphic to Bn´1, then H – Bn.

Proof. Let y P V pHq be arbitrary. Since H y is isomorphic to Bn´1, there exists a partition V pHq tyu “ X ¨Y Y with |X| “ n2 and |Y | “ n2 ´ 1 such that X and Y are independent sets in H. The same argument applies to every y1 P Y . Since Bn´1 has a unique independent set of size n2, the outcome must be the partition

V pHq ty1u “ X ¨Y `

Y Y tyu ty1u˘

for each y1 P Y . This proves that H is isomorphic to Bn with vertex classes X and Y Y tyu.

To handle the case where the number of vertices is odd we shall require the following lemma. Its initial assumption concerning the case n “ 8 will turn out to be harmless, as we will already know its truth when using the lemma for the ﬁrst time.

- Lemma 2.6. Assume that Theorem 1.1 holds for n “ 8. Now let n ě 9 be odd and let H be a hypergraph on n vertices with bpnq edges which does not contain a Fano plane. Suppose that whenever a four-element set K Ď V pHq induces a tetrahedron in H


- (i) we have pH Kq – Bn´4
- (ii) and every v P V pH Kq has degree exactly 5 in K.


Then H is isomorphic to Bn.

Proof. Recall that by Fact 2.1 there is a tetrahedron contained in H, say with vertex set K Ď V pHq. Owing to condition (i) there is a partition V K “ X ¨Y Y witnessing

that H K is indeed isomorphic to Bn´4. Notice that due to n ě 9 we may suppose that |X| ě 2 and |Y | ě 3.

Now consider any four distinct vertices x,x1 P X and y,y1 P Y . By clause (ii) applied to the tetrahedra K and K1 “ tx,x1,y,y1u we obtain

epK Y K1q “ epKq ` epK1q ` 5p|K| ` |K1|q “ 2 ¨ 4 ` 5 ¨ 8 “ 48 “ bp8q

and by the hypothesised validity of Theorem 1.1 for hypergraphs on 8 vertices it follows that K Y K1 induces a copy of B8 in H. As K induces a tetrahedron, there exists an enumeration K “ tv1,v2,v3,v4u such that the two independent 4-sets of this B8 are, possibly after relabelling y and y1,

- (a) either tv1,v2,x,x1u and tv3,v4,y,y1u
- (b) or tv1,v2,x,yu and tv3,v4,x1,y1u.


Y

y

X

v1 v2

x

K1

y1

K

x1

v3 v4

y2

Figure 2.5. The impossible case (b). Tetrahedra are drawn as yellow quadruples and independent sets as red lines.

Now assume for the sake of contradiction that the latter possibility occurs (see Fig. 2.5). Let y2 P Y be an arbitrary vertex distinct from y and y1. When applying the argument of the foregoing paragraph to tx,x1,y,y2u instead of K1 we still have the independent set tv1,v2,x,yu and, consequently, tv3,v4,x1,y2u is independent as well. But now, as the edges v3x1y1 and v3x1y2 are missing, the degree of v3 in the tetrahedron tx,x1,y1,y2u is at most 4, which violates condition (ii). This proves that alternative (b) is indeed impossible.

Summarising the discussion so far, we know that depending on any four distinct vertices x,x1 P X and y,y1 P Y there is an enumeration K “ tv1,v2,v3,v4u such that the two independent 4-sets of the copy of B8 induced by K Y tx,x1,y,y1u are as mentioned in (a).

Now if we keep y and y1 ﬁxed and let the pair x, x1 vary through X we will always get the same independent set tv3,v4,y,y1u and thus the entire set X Y tv1,v2u is independent in H. Similarly, Y Y tv3,v4u is independent as well. Consequently H is indeed isomorphic to Bn with partition classes X Y tv1,v2u and Y Y tv3,v4u.

§3. Multigraphs

This section builds upon [8, Section 2-4] and collects several extremal results on multigraphs that will be applied at a later occasion to certain link multigraphs arising in hypergraphs not containing Fano planes.

- Deﬁnition 3.1. For a positive integer p, a p-tuple

á

G “ pG1,...,Gpq of graphs on the same vertex set V p

á

Gq will be referred to as a p-multigraph.

Extending some pieces of graph theoretic notation to the context of multigraphs, we will write ep

á

Gq “ řp

i“1 epGiq for the total number of edges of a p-multigraph

á

G “ pG1,...,Gpq. Similarly, for every X Ď V p

á

Gq we put epXq “ řp

i“1 eG

ipXq and if the members of X are enumerated explicitly we will omit a pair of curly braces and write, e.g., epx,y,zq instead of the more baroque eptx,y,zuq. In the special case of two-element sets, the number epx,yq will be called the multiplicity of the pair xy.

With each p-multigraph one can associate a corresponding weighted graph pV,eq given by the set of vertices V “ V p

á

Gq and the multiplicity function px,yq ÞÝÑ epx,yq. There is a rich literature on extremal problems in weighted graphs and the topic is studied both for its own sake (see e.g. [7,19]) and due to its applicability to other parts of extremal combinatorics, such as Turán’s hypergraph problem and the Ramsey-Turán theory of graphs (see e.g. [5,13,14]).

The main diﬀerence between multigraphs and weighted graphs is that the former do also keep track of the sets Mpx,yq Ď rps containing for every pair xy of vertices those indices i P rps for which xy is an edge of Gi. Therefore, there is a richer variety of extremal questions that can be asked in the setting of multigraphs. The following such problem is closely tied to the Turán number of the Fano plane.

- Deﬁnition 3.2. For p ě 3 a p-multigraph


á

G “ pG1,...,Gpq is said to contain three crossing pairs (see Figure 3.1) if there are three distinct indices i,j,k P rps and four distinct vertices w,x,y,z P V p

á

Gq such that

- ‚ wx,yz P EpGiq;
- ‚ wy,xz P EpGjq; ‚ and wz,xy P EpGkq.


The maximum total number of edges that a p-multigraph on n vertices can have without containing three crossing pairs is denoted by fppnq.

The function f4p¨q was determined by Füredi and Simonovits in [8, Theorem 2.2]. Their result plays an important role in the proof of our main result and reads as follows. Theorem 3.3. For every n ě 4 one has

f4pnq “ 2ˆ

˙ ` 2Z

^.

n2 4

n 2

w

x

| |
|---|


y

z

Figure 3.1. Three crossing pairs in pGi,Gj,Gkq.

We would like to mention that Füredi and Simonovits also obtained a characterisation of the extremal conﬁgurations on n ě 8 vertices (see Figure 3.2). Namely, if

á

- G “ pG1,G2,G3,G4q denotes a 4-multigraph on at least 8 vertices with f4pnq edges that


á

does not contain three crossing pairs, then there are a partition V p

Gq “ X ¨Y Y and a permutation π in the symmetric group S4 such that

‚ |X| “ Xn

\

, |Y | “ Xn`1

\

, ‚ E

2

2

˘ “ Xp2q Y KpX,Y q, ‚ and E

`

˘ “ E

`

Gπp1q

Gπp2q

˘ “ Y p2q Y KpX,Y q, where KpX,Y q denotes the collection of all pairs xy with x P X and y P Y .

`

˘ “ E

`

Gπp4q

Gπp3q

- |X| “ Xn

2

\

- |Y | “ Xn`1


KpX,Y q “ EpG1q X EpG2q X EpG3q X EpG4q

\

2

Figure 3.2. An extremal 4-multigraph pG1,G2,G3,G4q with π “ id, G1 “ G2, and G3 “ G4.

It can be shown that this characterisation of the extremal conﬁgurations extends to the

- case n “ 7 as well, but for n P t4,5,6u further extremal multigraphs are mentioned in [8]. ˚ ˚ ˚


The remainder of this section deals with the function f5p¨q. Two instructive examples of 5-multigraphs without three crossing pairs are the following.

‚ Let G1 “ G2 “ G3 “ G4 “ G5 be a K4-free Turán graph on n vertices. Notice that this 5-multigraph has 5

Xn

\

- 2

- 3


edges. ‚ Let

á

G˚ “ pG1,G2,G3,G4q be an extremal 4-multigraph without three crossing pairs with vertex partition V p

á

G˚q “ X ¨Y Y as described earlier, take G5 to be the complete bipartite graph between X and Y and consider

á

G “ pG1,...,G5q. Clearly the 5-multigraph

á

G does not contain three crossing pairs either and its number of edges is 2

`n

˘ ` 3

Xn

\

2

.

2

4

These examples demonstrate f5pnq ě max ˆ5Z

^,2ˆ

˙ ` 3Z

^˙ (3.1)

n2 3

n2 4

n 2

and, as a matter of fact, we can show that equality holds for every n. Our proof of this statement is, however, quite laborious and relies on extensive case distinctions. For this reason we will state and prove below a weaker result on f5p¨q which still suﬃces for the application we have in mind.

Proposition 3.4. We have f5pnq ď 14p7n2 ´ nq for every natural number n ě 3.

Before we turn to the proof of this fact we take a closer look at the case n “ 4. Lemma 3.5. Let

á

G “ pG1,...,G5q be a 5-multigraph on four vertices not containing three crossing pairs and set e “ ep

á

Gq.

- (i) If e ě 23, then there exists an enumeration V p

á

Gq “ tw,x,y,zu such that epw,xq ` epy,zq ď 5.

- (ii) If e ě 22, then there exist two distinct vertices u and v with epu,vq “ 5.


á

Gq “ tw,x,y,zu and deﬁne a “ epw,xq ` epy,zq, b “ epw,yq ` epx,zq, as well as c “ epw,zq`epx,yq to be the sums of the multiplicities of the three pairs of disjoint edges. By symmetry we may suppose that the enumeration of V p

Proof. Write V p

á

Gq we started with has been chosen in such a way that a ď b ď c holds.

Now suppose for the sake of contradiction that a ě 6, b ě 7, and c ě 8. (‹)

Due to a ě 6 there is an index i P r5s such that wx and yz are edges of Gi. Similarly, b ě 7 implies that there are at least two indices j P r5s with the property that wy and xz are edges of Gj and, hence, at least one of them is distinct from i. Proceeding in the same way with c ě 8 one ﬁnds an index k ‰ i,j for which wz and xy are edges of Gk. We have thereby found three crossing pairs in pGi,Gj,Gkq and this contradiction proves that p‹q is indeed false.

Now part (i) of the lemma follows from the observation that a ` b ` c “ e ě 23 and 10 ě c ě b ě a entail c ě 8 and b ě 7. So the failure of p‹q yields a ď 5, as desired.

For the proof of part (ii) we notice that a`b`c “ e ě 22 and c ě b ě a still imply c ě 8. The falsity of p‹q shows that at least one of the estimates a ď 5 or b ď 6 holds. In both cases we obtain c ě 9, meaning that at least one of the two pairs wz or xy has multiplicity 5.

`3

˘ “ 15 shows that our claim holds

Proof of Proposition 3.4. The trivial bound f5p3q ď 5

2

for n “ 3. Next, an easy averaging argument yields f5pnq ď 54f4pnq for every natural number n. Due to Theorem 3.3 and (3.1) this gives the exact values

f5p4q “ 25 and f5p5q “ 40, (3.2)

which establish the desired estimate for n P t4,5u. Arguing indirectly we now let n ě 6 denote the least integer for which there exists a 5-multigraph

á

G “ pG1,...,G5q on n

vertices with more than 14p7n2 ´ nq edges that does not contain three crossing pairs. For every set X Ď V “ V p

á

á

Gq ´ epV Xq for the total number of edges having at least one endvertex in X. As long as 0 ă |X| ď n ´ 3 the minimality of n yields

Gq of vertices we shall write e`pXq “ ep

`

7pn ´ |X|q2 ´ pn ´ |X|q˘

epV Xq ď 14

, whence

e`pXq ą 14p14n|X| ´ 7|X|2 ´ |X|q. In particular, we obtain

$ ’&

- 1

- 2p7n ´ 3q if |X| “ 1, 7n ´ 7 if |X| “ 2,


(3.3)

e`pXq ě

’%

21

2 n ´ 16 if |X| “ 3.

`n

˘

á

á

Gq ą 72

G is greater than 72. Therefore,

Owing to ep

the average edge multiplicity in

2

there exist a set Q Ď V consisting of four vertices with epQq ą 6 ¨ 72 “ 21, and by Lemma 3.5(ii) it follows that there are two distinct vertices x and y with epx,yq “ 5.

According to (3.3) we have ÿ

`

epx,zq ` epy,zq˘ “ e`px,yq ´ 5 ě 7n ´ 12 ą 7pn ´ 2q.

zPV tx,yu

Consequently, there exists a vertex z distinct from x and y with epx,zq ` epy,zq ě 8.

Altogether we have thereby shown that there exist triples px˚,y˚,z˚q of distinct vertices with

epx˚,y˚q “ 5 and epx˚,z˚q ` epy˚,z˚q ě 8 and for the remainder of the proof we ﬁx one such triple with the additional property that epx˚,z˚q ` epy˚,z˚q ě 8 is maximal. Set α “ epx˚,z˚q as well as β “ epy˚,z˚q and observe that we may suppose α ě β for reasons of symmetry. Clearly pα,βq is one of the four ordered pairs p5,5q, p5,4q, p5,3q, or p4,4q.

Because of ÿ

`

epv,x˚q ` epv,y˚q ` epv,z˚q˘ “ e`px˚,y˚,z˚q ´ p5 ` α ` βq (3.4)

vPV tx˚,y˚,z˚u

˘ ´ 15 ą 10pn ´ 3q there exists a vertex v˚ ‰ x˚,y˚,z˚ satisfying

ě `21

(3.3)

2 n ´ 16

epv˚,x˚q ` epv˚,y˚q ` epv˚,z˚q ě 11. (3.5)

By applying the left part of (3.2) to the quadruple tv˚,x˚,y˚,z˚u we learn

α ` β ď 25 ´ 11 ´ 5 “ 9, meaning that the pair pα,βq cannot be p5,5q.

x˚

v˚

|4|
|---|


5

4

y˚

z˚

Figure 3.3. The case α “ β “ 4.

Assume next that α “ β “ 4 (see Figure 3.3), which yields epv˚,x˚,y˚,z˚q ě 13`11 “ 24. Due to Lemma 3.5(i) it follows that either epv˚,x˚q ď 1, epv˚,y˚q ď 1, or epv˚,z˚q “ 0. The last alternative would contradict (3.5), so by symmetry we may suppose that epv˚,y˚q ď 1. Invoking (3.5) once more we infer that epv˚,x˚q “ epv˚,z˚q “ 5. But now the edges of the triangle pv˚,x˚,z˚q have multiplicities 5, 5, and 4, contrary to the maximal choice of α ` β. We have thereby proved that pα,βq ‰ p4,4q.

For these reasons, it must be the case α “ 5 and β P t3,4u (see Figure 3.4). Adding ÿ

(3.3)

ě 27n ´ 232 to (3.4) we infer

epv,x˚q “ e`px˚q ´ 10

vPV tx˚,y˚,z˚u

ÿ

˘

`

2epv,x˚q ` epv,y˚q ` epv,z˚q˘ ě `21

˘ ` `7

2n ´ 232

2 n ´ 16 ´ 14

vPV tx˚,y˚,z˚u

ą 14pn ´ 3q, which shows that there exists a vertex w˚ ‰ x˚,y˚,z˚ such that

2epw˚,x˚q ` epw˚,y˚q ` epw˚,z˚q ě 15. (3.6) In particular, we have epw˚,x˚q ` epw˚,y˚q ` epw˚,z˚q ě 10 and, consequently,

epw˚,x˚,y˚,z˚q ě 13 ` 10 “ 23. Appealing to Lemma 3.5(i) again we deduce that at least one of the three cases

epw˚,x˚q ď 2, epw˚,y˚q “ 0, or epw˚,z˚q “ 0 occurs. The ﬁrst of them is incompatible with (3.6), so by symmetry we may suppose that epw˚,y˚q “ 0. In combination with (3.6) this yields epw˚,x˚q “ epw˚,z˚q “ 5. But now the triangle pw˚,x˚,z˚q contradicts the supposed maximality of α ` β.

Let us ﬁnally summarise the properties of f5 that shall be utilised in the next section.

x˚

w˚

|5|
|---|


5

β P t3,4u

y˚

z˚

Figure 3.4. The case α “ 5 and β ă 5.

Corollary 3.6. If n ě 9 is odd, then

(a) bpn ´ 5q ` f5pn ´ 5q ` 7pn ´ 5q ` 10 ă bpnq and (b)

`

bpn ´ 6q ` 12pn ´ 9q˘ ` f5pn ´ 6q ` `n´6

˘ ` 10pn ´ 6q ` 20 ă bpnq.

2

Proof. Due to the explicit formula (1.2) for bpnq and the estimate on f5pn ´ 5q provided by Proposition 3.4, part (a) is a consequence of 1 ă 18pn ´ 5q2, which is trivially valid. Similarly, part (b) reduces to 0 ă 14p3n ´ 23q, which is likewise obvious.

§4. Proof of the Main Theorem

This entire section is dedicated to the proof of Theorem 1.1, which proceeds by induction on n. Since the base case n “ 7 was already treated in Lemma 2.2, we may suppose that n ě 8 and that (1.1) as well as our statement addressing the extremal hypergraphs hold for every n1 P r7,nq in place of n. Now let H “ pV,Eq be a hypergraph on |V | “ n vertices with |E| “ bpnq edges that does not contain a Fano plane. We are to prove that H – Bn. Let us distinguish two cases according to the parity of n.

First Case: n ě 8 is even.

For every vertex v P V we have epH vq ď bpn ´ 1q, since otherwise the induction hypothesis would yield a Fano plane in H v. This shows that

dpvq ě bpnq ´ bpn ´ 1q “ 3ˆ

˙ “

n{2 2

3|E| n holds for every v P V . Due to

ř

vPV dpvq “ 3|E| this is only possible if every vertex has degree 3

`n{2

˘

. But now it follows that for every v P V the hypergraph H v has exactly bpn´1q edges. So if n ě 10 the induction hypothesis informs us that the assumption of Lemma 2.5 is satisﬁed, meaning that H is indeed isomorphic to Bn. In the remaining

2

- case n “ 8 the same conclusion can still be drawn unless there is a vertex v P V with


pH vq – J7. But this would entail K6p3q Ď J7 Ď H and Fact 2.4 would show |E| ă bp8q, which contradicts the choice of H.

Second Case: n ě 9 is odd.

For K Ď V and i P t0,1,2,3u let eipKq denote the number of edges of H with exactly i vertices in K. Clearly, we have

e0pKq ` e1pKq ` e2pKq ` e3pKq “ |E| “ bpnq (4.1) for every K Ď V .

We need to know later that H cannot contain a clique on ﬁve vertices and the claim that follows prepares the proof of this fact.

- Claim 4.1. If some six vertices of H span at least 18 edges, then they induce a copy of B6.


Proof. Let K “ tv1,...,v6u Ď V span at least 18 edges of H and suppose for the sake of contradiction that the subhypergraph of H induced by K is not isomorphic to B6. Arguing

- as in the second paragraph of the proof of Lemma 2.3 we may assume that tv1,...,v5u


induces a K5p3q in H. For n ě 13 we have n ´ 6 ě 7 and the induction hypothesis yields, in particular,

e0pKq ď bpn ´ 6q ` 21pn ´ 9q, (4.2)

where the additional term 12pn ´ 9q is actually not needed. The reason for including it here is that for n P t9,11u it makes the right side equal to the trivial upper bound

`n´6

˘

. Therefore (4.2) holds in all possible cases.

3

á

G “ pG1,...,G6q with vertex set V K, where for j P r6s the edges of Gj are inherited from the link graph of vj. Since tv1,...,v5u is a clique in H, three crossing pairs in pG1,...,G5q would give rise to a Fano plane in H. Hence epG1q ` ... ` epG5q ď f5pn ´ 6q and together with the trivial bound epG6q ď `n´6

Now consider the 6-multigraph

˘

we obtain

2

Gq ď f5pn ´ 6q ` ˆ

˙. (4.3)

n ´ 6 2

á

e1pKq “ ep

Moreover, Lemma 2.3 shows that every vertex v P V K can contribute at most 10 edges to e2pKq, wherefore

e2pKq ď 10pn ´ 6q. (4.4) By plugging (4.2), (4.3), (4.4), and the trivial upper bound e3pKq ď `6

˘ “ 20 into (4.1) we arrive at the estimate

3

bpn ´ 6q ` 21pn ´ 9q˘ ` f5pn ´ 6q ` ˆ

˙ ` 10pn ´ 6q ` 20,

n ´ 6 2

bpnq ď `

which contradicts Corollary 3.6(b). This proves Claim 4.1.

## Claim 4.2. K5p3q Ę H

Proof. Assume to the contrary that K “ tv1,...,v5u Ď V induces a K5p3q in H. We contend that e0pKq ď bpn ´ 5q. For n ě 13 this follows indeed from the induction hypothesis, for n “ 9 we just need to appeal to the trivial bound e0pKq ď `n´5

˘ “ 4 “ bpn ´ 5q and for n “ 11 the desired estimate holds in view of Claim 4.1.

3

A link multigraph argument similar to the one encountered in the foregoing proof of (4.3) shows that e1pKq ď f5pn ´ 5q. Owing to Claim 4.1 every vertex in V K belongs to

- at most 7 edges contributing to e2pKq, whence e2pKq ď 7pn ´ 5q. Combining all these estimates and e3pKq “ 10 with (4.1) we learn


bpnq ď bpn ´ 5q ` f5pn ´ 5q ` 7pn ´ 5q ` 10, which, however, contradicts Corollary 3.6(a). Thereby Claim 4.2 is proved.

In order to conclude the proof of our main result we will now show that H satisﬁes the assumptions of Lemma 2.6. Suppose to this end that K Ď V induces a tetrahedron in H. For n ě 11 the induction hypothesis gives e0pKq ď bpn ´ 4q and for n “ 9 this estimate could only fail if V K induces a K5p3q in H, which would contradict Claim 4.2. Thus we obtain

bpnq ď bpn ´ 4q ` f4pn ´ 4q ` 5pn ´ 4q ` 4 (4.5) in the usual manner, where the factor 5 in front of pn ´ 4q comes from the absence of 5-cliques in H. In view of (1.2) and Theorem 3.3 the right side equals

˘pn ´ 6q ` 2ˆ

˙ `

- 1

- 2`pn ´ 4q2 ´ 1


1 8`pn ´ 4q2 ´ 1

n ´ 4 2

˘ ` 5pn ´ 4q ` 4

1 8pn2 ´ 1qpn ´ 2q “ bpnq,

“

meaning that (4.5) actually holds with equality. In particular, this yields

e0pKq “ bpn ´ 4q (4.6) and

e2pKq “ 5pn ´ 4q.

The latter equation proves immediately that K obeys clause (ii) from Lemma 2.6. It remains to check that, similarly, (4.6) leads to (i), i.e., to pH Kq – Bn´4. For n ě 13 this is indeed true due to the induction hypotheses. For n “ 11 we need to point out additionally that H K cannot be isomorphic to J7, as this hypergraph contains a copy of K5p3q, whilst H does not. Finally, for n “ 9 the desired statement is a simple consequence of the fact that B5, the ﬁve-clique with one edge removed, is the only hypergraph on 5 vertices with bp5q “ 9 edges. This concludes the proof of our main result.

Acknowledgement

We would like to thank Miklós Simonovits for sending us a copy of [21], Zoltán Füredi [6] for further information regarding the history of the problem, and the referees for a careful reading of this article.

References

- [1] B. Bollobás, Extremal graph theory, Dover Publications, Inc., Mineola, NY, 2004. Reprint of the 1978 original. MR2078877 Ò2.3
- [2] W. G. Brown, On an open problem of Paul Turán concerning 3-graphs, Studies in pure mathematics, Birkhäuser, Basel, 1983, pp. 91–93. MR820213 Ò1
- [3] D. De Caen and Z. Füredi, The maximum size of 3-uniform hypergraphs not containing a Fano plane, J. Combin. Theory Ser. B 78 (2000), no. 2, 274–276, DOI10.1006/jctb.1999.1938. MR1750899 Ò1, 2.2
- [4] P. Erdős, Paul Turán, 1910–1976: his work in graph theory, J. Graph Theory 1 (1977), no. 2, 97–101. MR0441657 (56 #61) Ò1
- [5] P. Erdős, A. Hajnal, V. T. Sós, and E. Szemerédi, More results on Ramsey-Turán type problems, Combinatorica 3 (1983), no. 1, 69–81, DOI10.1007/BF02579342. MR716422 Ò3
- [6] Z. Füredi. Personal communication. Ò1, 4
- [7] Z. Füredi and A. Kündgen, Turán problems for integer-weighted graphs, J. Graph Theory 40 (2002), no. 4, 195–225, DOI10.1002/jgt.10012. MR1913847 Ò3
- [8] Z. Füredi and M. Simonovits, Triple systems not containing a Fano conﬁguration, Combin. Probab. Comput. 14 (2005), no. 4, 467–484, DOI10.1017/S0963548305006784. MR2160414 Ò1, 1, 2.2, 2.2, 3, 3, 3
- [9] G. Katona, T. Nemetz, and M. Simonovits, On a problem of Turán in the theory of graphs, Mat. Lapok 15 (1964), 228–238 (Hungarian, with Russian and English summaries). MR0172263 Ò1
- [10] P. Keevash and D. Mubayi, The Turán number of F3,3, Combin. Probab. Comput. 21 (2012), no. 3, 451–456, DOI10.1017/S0963548311000678. MR2912791 Ò1
- [11] P. Keevash and B. Sudakov, The Turán number of the Fano plane, Combinatorica 25 (2005), no. 5, 561–574, DOI10.1007/s00493-005-0034-2. MR2176425 Ò1, 1, 2.2
- [12] A. V. Kostochka, A class of constructions for Turán’s p3, 4q-problem, Combinatorica 2 (1982), no. 2, 187–192, DOI10.1007/BF02579317. MR685045 Ò1
- [13] C. M. Lüders and C. Reiher, The Ramsey-Turán problem for cliques, available at arXiv:1709.03352. Israel Journal of Mathematics. To Appear. Ò3
- [14] , Weighted variants of the Andrásfai-Erdős-Sós Theorem, available at arXiv:1710.09652. Submitted. Ò3

- [15] D. Mubayi and V. Rödl, On the Turán number of triple systems, J. Combin. Theory Ser. A 100

(2002), no. 1, 136–152, DOI10.1006/jcta.2002.3284. MR1932073 Ò1

- [16] M. Pasch, Vorlesungen über neuere Geometrie, Second edition, Teubner Studienbücher Mathematik. [Teubner Mathematical Textbooks], B. G. Teubner, Leipzig und Berlin, 1912 (German). With supplementary material by Paul Bernays. MR1109913 Ò2.2
- [17] A. A. Razborov, Flag algebras, J. Symbolic Logic 72 (2007), no. 4, 1239–1282, DOI10.2178/jsl/1203350785. MR2371204 (2008j:03040) Ò1
- [18] , On 3-hypergraphs with forbidden 4-vertex conﬁgurations, SIAM J. Discrete Math. 24 (2010), no. 3, 946–963, DOI10.1137/090747476. MR2680226 (2011k:05171) Ò1


- [19] V. Rödl and A. Sidorenko, On the jumping constant conjecture for multigraphs, J. Combin. Theory Ser. A 69 (1995), no. 2, 347–357, DOI10.1016/0097-3165(95)90057-8. MR1313901 Ò3
- [20] M. Simonovits, A method for solving extremal problems in graph theory, stability problems, Theory of Graphs (Proc. Colloq., Tihany, 1966), Academic Press, New York, 1968, pp. 279–319. MR0233735 Ò1
- [21] V. T. Sós, Remarks on the connection of graph theory, ﬁnite geometry and block designs, Colloquio Internazionale sulle Teorie Combinatorie (Roma, 1973), Accad. Naz. Lincei, Rome, 1976, pp. 223–233. Atti dei Convegni Lincei, No. 17 (English, with Italian summary). MR0543051 Ò1, 4
- [22] P. Turán, Eine Extremalaufgabe aus der Graphentheorie, Mat. Fiz. Lapok 48 (1941), 436–452 (Hungarian, with German summary). MR0018405 Ò1
- [23] W. T. Tutte, The factorization of linear graphs, J. London Math. Soc. 22 (1947), 107–111, DOI10.1112/jlms/s1-22.2.107. MR0023048 Ò2.3


Fachbereich Mathematik, Universität Hamburg, Hamburg, Germany E-mail address: Christian.Reiher@uni-hamburg.de E-mail address: louisnbell@aol.com

