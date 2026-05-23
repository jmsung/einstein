arXiv:1511.00563v1[math.CO]2Nov2015

Hedgehogs are not colour blind

David Conlon∗ Jacob Fox† Vojtˇech Ro¨dl‡

Abstract

We exhibit a family of 3-uniform hypergraphs with the property that their 2-colour Ramsey numbers grow polynomially in the number of vertices, while their 4-colour Ramsey numbers grow exponentially. This is the ﬁrst example of a class of hypergraphs whose Ramsey numbers show a strong dependence on the number of colours.

# 1 Introduction

The Ramsey number rk(H) of a k-uniform hypergraph H is the smallest n such that any 2-colouring of the edges of the complete k-uniform hypergraph Kn(k) contains a monochromatic copy of H. Similarly, for any q ≥ 2, we may deﬁne a q-colour Ramsey number rk(H;q).

One of the main outstanding problems in Ramsey theory is to decide whether the Ramsey number for complete 3-uniform hypergraphs is double exponential. The best known bounds, due to Erd˝os, Hajnal and Rado [5, 6], state that there are positive constants c and c′ such that

′t.

2ct2 ≤ r3(Kt(3)) ≤ 22c

Paul Erd˝os has oﬀered $500 for a proof that the upper bound is correct, that is, that there exists a positive constant c such that r3(Kt(3)) ≥ 22ct. Some evidence that this may be true was given by Erd˝os and Hajnal (see, for example, [9]), who showed that the analogous bound holds for 4 colours, that is,

- that there exists a positive constant c such that r3(Kt(3);4) ≥ 22ct. In this paper, we show that this evidence may not be so compelling by ﬁnding a natural class of hypergraphs, which we call hedgehogs, whose Ramsey numbers show a strong dependence on the number of colours.


The hedgehog Ht is the 3-uniform hypergraph with vertex set [t + 2 t ] such that for every pair (i,j) with 1 ≤ i < j ≤ t there is a unique vertex k > t such that ijk is an edge. We will sometimes refer

to the set {1,2,... ,t} as the body of the hedgehog. Our main result is that the 2-colour Ramsey number r3(Ht) grows as a polynomial in t, while the 4-colour Ramsey number r3(Ht;4) grows as an exponential in t.

- Theorem 1 If Ht is the 3-uniform hedgehog with body of order t, then


(i) r3(Ht) ≤ 4t3,

![image 1](<2015-conlon-hedgehogs-not-colour-blind_images/imageFile1.png>)

∗Mathematical Institute, Oxford OX2 6GG, United Kingdom. Email: david.conlon@maths.ox.ac.uk. Research supported by a Royal Society University Research Fellowship.

†Department of Mathematics, Stanford University, Stanford, CA 94305, USA. Email: fox@math.mit.edu. Research supported by a Packard Fellowship, by NSF Career Award DMS-1352121 and by an Alfred P. Sloan Fellowship.

‡Department of Mathematics and Computer Science, Emory University, Atlanta, GA 30322, USA. Email: rodl@mathcs.emory.edu. Research partially supported by NSF grants DMS-1102086 and DMS-1301698.

(ii) there exists a positive constant c such that r3(Ht;4) ≥ 2ct.

For the intermediate 3-colour case, we show that the answer is intimately connected with a special case of the multicolour Erd˝os–Hajnal conjecture [4]. This conjecture states that for any complete graph K with a ﬁxed q-colouring of its edges, there exists a positive constant c(K) such that any q-colouring (with the same q colours) of the edges of the complete graph on n vertices with no copy of K contains a clique of order nc(K) which receives only q − 1 colours. Though this conjecture is known to hold in a number of special cases (see, for example, Section 3.3 of [3]), the best known general result, due to Erd˝os and Hajnal themselves, says that there exists a positive constant c(K) such that any q-colouring of the edges of the complete graph on n vertices with no copy of K contains a clique of order ec(K)

√log n

![image 2](<2015-conlon-hedgehogs-not-colour-blind_images/imageFile2.png>)

which receives only q − 1 colours. We will be concerned with the particular case where q = 4 and the banned conﬁguration K is a rainbow triangle with one edge in each of the ﬁrst three colours.

Deﬁnition. Let F(t) be the smallest n such that every 4-colouring of the edges of Kn, in red, blue, green and yellow, contains either a rainbow triangle K, with one edge in each of red, blue and green, or a clique of order t with at most 3 colours.

We will show that r3(Ht;3) is bounded above and below by polynomials in F(t) (strictly speaking, the upper bound is a polynomial in F(t3), but, provided F(t) does not jump pathologically, this will be at most polynomial in F(t)). Since the result of Erd˝os and Hajnal mentioned in the previous paragraph implies that F(t) ≤ tclogt for some constant c, this in turn shows that r3(Ht;3) ≤ tclogt for some constant c. Moreover, the Erd˝os–Hajnal conjecture holds in this case if and only if there is a polynomial upper bound for r3(Ht;3).

- Theorem 2 If Ht is the 3-uniform hedgehog with body of order t, then


- (i) r3(Ht;3) = O(t4F(t3)2),
- (ii) r3(Ht;3) ≥ F(t).


In particular, there exists a constant c such that r3(Ht;3) ≤ tclogt.

We will prove Theorem 1 in the next section and Theorem 2 in Section 3. We conclude by discussing a number of interesting questions that arose from our work.

# 2 The basic dichotomy

In this section, we prove Theorem 1. We begin by proving that the 2-colour Ramsey number of Ht is at most 4t3.

- Proof of Theorem 1(i): Let n = 4t3. We will show that every red/blue-colouring of the complete


3-uniform hypergraph on n vertices contains a monochromatic copy of Ht. To begin, we deﬁne a partial colouring of the edges of the complete graph on the same vertex set. We will colour an edge uv

red if there are fewer than 2 t + t red triples containing u and v. Similarly, we colour uv blue if there are fewer than 2 t + t blue triples containing u and v. To ﬁnd a monochromatic Ht, it will clearly

suﬃce to ﬁnd a subset of order t containing no red edge or no blue edge, since we can consider this set as the body of the hedgehog and embed the spines greedily.

We claim that no vertex is contained in 2t2 red edges and 2t2 blue edges. Suppose, on the contrary, that u is such a vertex and let VR and VB be the vertices which are connected to u in red and blue, respectively. Since it is easy to see that no edge can be coloured both red and blue, VR and VB are disjoint. Moreover, for each vertex v in VR, since uv is contained in fewer than 2 t + t red triples, there are at least

t 2

|VB| 2

|VB| −

− t >

![image 3](<2015-conlon-hedgehogs-not-colour-blind_images/imageFile3.png>)

vertices w in VB such that uvw is blue. This implies that more than half of the triples uvw with v ∈ VR and w ∈ VB are blue. However, by ﬁrst considering vertices w in VB, the same argument also shows that more than half of these triples are red, a contradiction.

We now assign a colour to each vertex in the graph, colouring it red if it is contained in fewer than 2t2 red edges and blue otherwise. In the latter case, the claim of the last paragraph shows that it will be contained in fewer than 2t2 blue edges. By the pigeonhole principle, at least half the vertices in the graph have the same colour, say red. That is, we have a subset of order at least n/2 such that every vertex is contained in fewer than 2t2 red edges. By Brooks’ theorem, we conclude that this set contains a subset of order n/4t2 containing no red edge. Since n/4t2 ≥ t, this is the required set. ✷

We will now show that the 4-colour Ramsey number of Ht is at least 2ct for some positive constant c. This is clearly sharp up to the constant in the exponent.

- Proof of Theorem 1(ii): A standard application of the ﬁrst moment method gives a positive constant c such that, for every integer t ≥ 4, there is a 4-colouring χ of the edges of the complete graph on 2ct vertices with the property that every clique of order t contains all 4 colours. We now 4-colour the edges of the complete 3-uniform hypergraph on the same vertex set by colouring the triple uvw with any colour which is not contained within the set {χ(u,v),χ(v,w),χ(w,u)}. Suppose now that there is a monochromatic copy of Ht with colour 1, say, and let u1,u2,... ,ut be the body of this copy. Then, in the original graph colouring χ, none of the edges uiuj with 1 ≤ i < j ≤ t received the colour 1. However, this contradicts the property that every set of order t contains all 4 colours. ✷


# 3 Three colours and the Erd˝os–Hajnal conjecture

To prove Theorem 2(i), we require two lemmas. The ﬁrst is a result of Spencer [13] which says that any 3-uniform hypergraph with few edges contains a large independent set.

- Lemma 1 If H is a 3-uniform hypergraph with n vertices and e edges, then α(H) = Ω(n3/2/e1/2).

The second lemma we require is a result of Fox, Grinshpun and Pach [7] saying that the multicolour Erd˝os–Hajnal conjecture holds for 3-colourings of Kn with no rainbow triangle. The result we use is somewhat weaker than the main result in [7], but will be more than suﬃcient for our purposes.

- Lemma 2 Suppose that the edges of the complete graph Kn have been 3-coloured, in red, blue and green, so that there are no rainbow triangles with one edge in each of red, blue and green. Then there is a clique of order n1/3 containing at most two of the three colours.


We are now ready to prove Theorem 2(i), that r3(Ht;3) = O(t4F(t3)2).

- Proof of Theorem 2(i): Suppose that the edges of the complete 3-uniform hypergraph on n = ct4F(t3)2 vertices have been 3-coloured, in red, blue and green, where c is a suﬃciently large constant to be chosen later. We will 4-colour the edges of the graph on the same vertex set as follows: if u and

v are contained in fewer than 2 t + t triples of a given colour, then we give the edge uv that colour, noting that an edge may receive more than one colour (but at most two). On the other hand, if an

edge is not coloured with any of red, blue or green, we colour it yellow. We claim that this colouring has at most t2n2 triangles containing all three of the colours red, blue and green (where we include the possibility that two of these colours may appear on the same edge). To see this, note that there are at most ( 2 t +t) n2 red triples containing a red edge. In particular, since the triangles we wish to count always contain a red edge, there are at most ( 2 t +t) n2 of these triangles in the graph corresponding to a red triple. Since we may similarly bound the number of these triangles corresponding to blue or green triples, we see that, for t ≥ 3, there are at most 3( 2 t + t) n2 ≤ t2n2 triangles in the graph which contain all three of the colours red, blue and green, as required. If we let H be the 3-uniform hypergraph on n vertices whose edges correspond to triangles containg all three of the colours red, blue and green, Lemma 1 now yields a subset U of order Ω(n1/2/t) containing no such triangle. By taking c to be suﬃciently large, we may assume that U has order at least tF(t3). We now consider the graph G on vertex set U whose edge set consists of all those edges which received two colours in the 4-colouring deﬁned above. If we ﬁx a vertex u ∈ U, then each of the edges in G that contain u must have received the same two colours in the original colouring. Otherwise, we would have a triangle containing all three of the colours red, blue and green. Suppose, therefore, that every edge in G that contains u received the colours red and blue in the original colouring. Then, again using the property that every triangle contains at most two of the colours red, blue and green, we see that the neighbourhood of u in G contains no green edges. Therefore, if u had t neighbours in G, we could use this neighbourhood to ﬁnd a green copy of Ht. Since a similar argument holds if the edges containing u correspond to blue and green or to red and green, we may assume that every vertex u ∈ U is contained in fewer than t edges in the graph G.

By Brooks’ theorem, it follows that U contains a subset V of order at least |U|/t ≥ F(t3) containing no edges from G, that is, such that every edge received at most one colour in the original colouring. Since V is a 4-coloured graph of order at least F(t3) containing no rainbow triangle in red, blue and green, there is a subset of order at least t3 with at most three colours. If the missing colour is red, we may easily ﬁnd a red copy of Ht and similar conclusions hold if the missing colour is either blue or green. On the other hand, if the missing colour is yellow, we have a 3-colouring, in red, blue and green, of a set of order at least t3 containing no rainbow triangle, so Lemma 2 tells us that there is a subset of order at least t with at most two colours. If we again consider the missing colour, it is easy to ﬁnd a monochromatic copy of Ht in that colour. ✷

The lower bound, r3(Ht;3) ≥ F(t) follows from a simple adaptation of the proof of Theorem 1(ii).

- Proof of Theorem 2(ii): By the deﬁnition of F(t), there exists a 4-colouring χ, in red, blue, green and yellow, say, of the edges of the complete graph on F(t)−1 vertices containing no rainbow triangle with one edge in each of red, blue and green and such that every clique of order t contains all 4 colours. We now 3-colour the complete 3-uniform hypergraph on the same vertex set in red, blue and green, colouring the triple uvw with any colour which is not contained within the set {χ(u,v),χ(v,w),χ(w,u)}.


Since there are no rainbow triangles in red, blue and green, this colouring is well-deﬁned. Suppose now that there is a monochromatic copy of Ht in red, say, and let u1,u2,... ,ut be the body of this copy. Then, in the original graph colouring χ, none of the edges uiuj with 1 ≤ i < j ≤ t are red. However, this contradicts the property that every set of order t contains all 4 colours. ✷

# 4 Concluding remarks

The results of this paper raise a number of interesting questions, some of which we describe below.

## 4.1 Higher uniformity hedgehogs

The k-uniform hedgehog Ht(k) is the hypergraph with vertex set [t+ k− t 1 ] such that for every (k −1)tuple (i1,... ,ik−1) with 1 ≤ i1 < ··· < ik−1 ≤ t there is a unique vertex ik > t such that i1 ... ik is an edge. A straightforward generalisation of the proof of Theorem 1(i) gives the following result.

- Theorem 3 For every integer k ≥ 4, there exists a constant ck such that if Ht(k) is the k-uniform hedgehog with body of order t, then


rk(Ht(k)) ≤ tk−2(ckt), where the tower function ti(x) is deﬁned by t1(x) = x and ti+1(x) = 2ti(x). A construction due to Kostochka and Ro¨dl [10] shows that this result is tight for k = 4, that is,

- that there exists a positive constant c such that r4(Ht(4)) ≥ 2ct. Since the construction is simple, we describe it in full. To begin, take a colouring of the edges of the complete graph on 2ct vertices such that every set of order t contains both a red triangle and a blue triangle. We then colour the edges of the 4-uniform hypergraph on the same vertex set by colouring a 4-tuple red if it contains a red triangle, blue if it contains a blue triangle and arbitrarily otherwise. It is easy to check that this 2-colouring


contains no monochromatic copy of Ht(4). Already for k = 5, we were unable to prove a matching lower bound, since it seems that one would ﬁrst need to know how to prove a double-exponential lower

bound for r3(Kt).

We were also unable to prove an analogue of Theorem 1(ii) for k = 4. Again, this is because of a basic gap in our understanding of hypergraph Ramsey problems. While we know that there are 4-colourings of the 3-uniform hypergraph on 22ct vertices such that every subset of order t receives at least two colours, we do not know if the following variant holds.

- Problem 1 Is there an integer q, a positive constant c and a q-colouring of the 3-uniform hypergraph on 22ct vertices such that every subset of order t receives at least three colours?


A positive answer to the analogous question where we ask that every subset of order t receives at least ﬁve colours would allow us to prove that there exists an integer q such that r4(Ht(4);q) ≥ 22ct. The proof of this statement is a variant of the proof of Theorem 1(ii). Indeed, suppose that we have a q-colouring χ of the edges of the 3-uniform hypergraph Kn(3) such that every subset of order t receives at least ﬁve colours. Then we deﬁne a colouring of the complete 4-uniform hypergraph Kn(4) with at most q+ 2 q +

- q 3 + 4 q colours by colouring the edge uvwx with the set {χ(uvw),χ(vwx),χ(wxu),χ(xuv)}. It is now


easy to check that if there is a monochromatic Ht(4) in this colouring, then, in the original colouring

χ, the body of the hedgehog is a subset of order t which receives at most 4 colours, contradicting our choice of χ.

Our motivation for investigating higher uniformity hedgehogs was the hope that they might allow us to show that there are families of hypergraphs for which there is an even wider separation between the 2-colour and q-colour Ramsey numbers. However, it seems likely that for hedgehogs the separation between the tower heights is at most one for any uniformity. This leaves the following problem open.

- Problem 2 For any integer h ≥ 3, do there exist integers k and q and a family of k-uniform hypergraphs for which the 2-colour Ramsey number grows as a polynomial in the number of vertices, while the q-colour Ramsey number grows as a tower of height h?

4.2 Burr–Erdo˝s in hypergraphs

The degeneracy of a graph H is the minimum d such that every induced subset contains a vertex of degree at most d. Building on work of Kostochka and Sudakov [11] and Fox and Sudakov [8], Lee [12] recently proved the famous Burr–Erdo˝s conjecture [1], that graphs of bounded degeneracy have linear Ramsey numbers. That is, he showed that for every positive integer d there exists a constant c(d) such that the Ramsey number of any graph H with n vertices and degeneracy d satisﬁes r(H) ≤ c(d)n.

If we deﬁne the degeneracy of a hypergraph H in a similar way, that is, as the minimum d such that every induced subset contains a vertex of degree at most d, we may ask whether the analogous statement holds in hypergraphs. Unfortunately, as ﬁrst observed by Kostochka and Ro¨dl [10], the 4-

uniform analogue of the Burr–Erdo˝s conjecture is false, since Ht(4) is 1-degenerate and r4(Ht(4)) ≥ 2ct. Since Ht is a 1-degenerate hypergraph, the results of this paper show that the Burr–Erdo˝s conjecture also fails for 3-uniform hypergraphs and 3 or more colours. For 4 colours, this follows immediately from Theorem 1(ii). For 3 colours, it follows from Theorem 2(ii) and the observation that F(t) = Ω(t3/log6 t). To show this, we amend a construction of Fox, Grinshpun and Pach [7], taking the lexicographic product of three 3-colourings of the complete graph on t/16log2 t vertices, one for each triple of colours from the set {red, blue, green, yellow} that contains yellow, each having the property that the union of any two colours contains no clique of order 4log t. This colouring will contain no rainbow triangle with one edge in each of red, blue and green and no clique of order t with at most 3 colours. For further details, we refer the reader to Theorem 3.1 of [7].

While it is also unlikely that an analogue of the Burr–Erdo˝s conjecture holds in the 2-colour case, it may still be the case that r3(Ht) is linear in the number of vertices, that is, that r3(Ht) = O(t2). It would already be interesting to prove an approximate version of this statement.

- Problem 3 Show that r3(Ht) = t2+o(1).


- 4.3 Multicolour Erdo˝s–Hajnal It is somewhat curious that our upper bound for r3(Ht;3) mirrors the best known lower bound for


- r3(Kt;3), due to Conlon, Fox and Sudakov [2], which says that there exists a positive constant c such that


r3(Kt;3) ≥ 2tclogt.

However, it seems likely that this is mere coincidence and that the function F(t) deﬁned in the introduction is polynomial in t. Phrasing the question in a more traditional fashion, we would very much like to know the answer to the following special case of the multicolour Erd˝os–Hajnal conjecture.

- Problem 4 Show that there exists a positive constant c such that if the edges of Kn are 4-coloured, in red, blue, green and yellow, so that there are no rainbow triangles with one edge in each of red, blue and green, then there is a clique of order nc containing at most three of the four colours.


That being said, if F(t) were superpolynomial, it would not only disprove the multicolour Erd˝os–Hajnal conjecture, it would also strengthen the curious correspondence between the bounds for r3(Ht;q) and r3(Kt;q). This would certainly be the more interesting outcome.

# References

- [1] S. A. Burr and P. Erd˝os, On the magnitude of generalized Ramsey numbers for graphs, in Inﬁnite and Finite Sets, Vol. 1 (Keszthely, 1973), 214–240, Colloq. Math. Soc. Ja´nos Bolyai, Vol. 10, NorthHolland, Amsterdam, 1975.
- [2] D. Conlon, J. Fox and B. Sudakov, Hypergraph Ramsey numbers, J. Amer. Math. Soc. 23 (2010), 247–266.
- [3] D. Conlon, J. Fox and B. Sudakov, Recent developments in graph Ramsey theory, in Surveys in Combinatorics 2015, London Math. Soc. Lecture Note Ser., Vol. 424, 49–118, Cambridge University Press, Cambridge, 2015.
- [4] P. Erd˝os and A. Hajnal, Ramsey-type theorems, Discrete Appl. Math. 25 (1989), 37–52.
- [5] P. Erd˝os, A. Hajnal and R. Rado, Partition relations for cardinal numbers, Acta Math. Acad. Sci. Hungar. 16 (1965), 93–196.
- [6] P. Erd˝os and R. Rado, Combinatorial theorems on classiﬁcations of subsets of a given set, Proc. London Math. Soc. 3 (1952), 417–439.
- [7] J. Fox, A. Grinshpun and J. Pach, The Erd˝os–Hajnal conjecture for rainbow triangles, J. Combin. Theory Ser. B 111 (2015), 75–125.
- [8] J. Fox and B. Sudakov, Two remarks on the Burr–Erdo˝s conjecture, European J. Combin. 30

(2009), 1630–1645.

- [9] R. L. Graham, B. L. Rothschild and J. H. Spencer, Ramsey theory, 2nd edition, John Wiley & Sons, 1990.
- [10] A. V. Kostochka and V. Ro¨dl, On Ramsey numbers of uniform hypergraphs with given maximum degree, J. Combin. Theory Ser. A 113 (2006), 1555–1564.
- [11] A. V. Kostochka and B. Sudakov, On Ramsey numbers of sparse graphs, Combin. Probab. Comput.
- 12 (2003), 627–641.


- [12] C. Lee, Ramsey numbers of degenerate graphs, arXiv:1505.04773 [math.CO].
- [13] J. Spencer, Tura´n’s theorem for k-graphs, Discrete Math. 2 (1972), 183–186.


