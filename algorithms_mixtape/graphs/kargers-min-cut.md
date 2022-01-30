# Karger's algorithm

Karger's algorithm is a randomized algorithm for computing the minimum cut of a
connected graph. A minimum cut ("min cut") is a partition of a graph into two
non-empty sets *A* and *B* such that the partition between the two sets crosses
the fewest edges possible. A crossing edge is an edge with one endpoint
on either side of the cut.

![graph cuts](https://www.dropbox.com/s/536o3vmkhup6ia2/graphs.jpg?raw=1)
*Exhibit 1: cut diagram*

The min cut is a useful heuristic for identify clusters graph. Real-world
applications include:
- **Identifying bottlenecks or weakest points in a network** - Roughgarden gives the
  example of declassified Cold War documents that detail the US and USSR's
  efforts to identify the most effective way to disrupt transportation networks.
- **Identifying communities within a relationship network** - the minimum cut can
  identify pockets of a graph that are highly connected to each other but weakly
  connected to other parts of the graph.
- **Identifying objects in an image** - images can be represented as grid graphs
  where each pixel is a vertex and edges are adjacent pixels. You can attempt to
  identify objects in an image if you weight the edges by how similar the pixel
  is to it's neighbor and take the min cut.

## Implementation

### Input

An adjacency list representing an undirected graph.

### Output

The number of crossing edges in the minimum cut.

### Description
`min_cut(graph)` subroutine
1. If there are 2 vertices, return the number of edges connecting the two.
2. While there are more than 2 vertices:
    - Select an edge from the graph uniformly at random and
      "merge" the two endpoints into a single "super" vertex.
    - Eliminate any self-referential edges created by the merge.
3. Return the "cut" represented by the final 2 vertices.

![example cuts](https://www.dropbox.com/s/hp74sdzuvuf1c9g/min-cut.png?raw=1)
*Exhibit 2: the contraction process*

## Analysis

The probability that a single execution of this algorithm successfully computes
the correct min cut is actually low. Referring to *Exhibit 1* above, the
algorithm contracts an edge with 1 endpoint in *A* and 1 endpoint in *B* at any
point in the execution, it will return the wrong solution.

> With a single run, the probability of success is 1/*n*<sup>2</sup>.

While this is a low probability of success, it's still non-trivial. Through
repeated trials, we can successfully compute the min cut with almost complete
certainty. 

> The probably of success is almost 1 with *n*<sup>2</sup> ln *n* trials.

Due to it's randomized nature, Karger's algorithm can never gaurantee a correct solution. Such algorithms are
called [Monte Carlo
algorithms](https://en.wikipedia.org/wiki/Monte_Carlo_algorithm#:~:text=In%20computing%2C%20a%20Monte%20Carlo,for%20minimum%20Feedback%20arc%20set.).
They tend to have better runtimes than their deterministic counterparts, but do
not gaurantee correctness.

### Asymptotic runtime

Karger's Algorithm beautifully demonstrates that blind randomization and
repeated trials can solve certain problems with a high-degree of confidence. The
runtime, on the other hand, isn't that impresive. It's at least better than
deterministic brute-force search which would run in *O*(2<sup>n</sup>).

We can pretty easily come up with a rough lower-bound on the runtime. For an
almost certain correct solution, it needs to run *n*<sup>2</sup> ln *n* trials.
Each trial has to contract *m* - 2 edges, so there's a factor of *m*. Dropping
the non-dominant ln *n* term, we end up with:

> Ω(*n*<sup>2</sup> *m*)

David Karger later improved this basic form of the algorithm to achieve an order
of magnitude better performance.