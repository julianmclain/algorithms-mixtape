# Karger's algorithm

conditional probability 
independence

compute the cut. So, a cut is a partition of the graph vertices into two groups,
A and B. The number of edges crossing the cut is simply those that have one
endpoint on each side. And amongst all the exponentially possible cuts, we want
to identify one that has The fewest number of crossing edges, or a "min cut".

Karger's algorithm, also referred to as the randomized contraction algorithm for
computing the minimum cut of a graph, is a solution to the minimum cut problem.
A cut of a graph is a partition of the vertices into two non-empty sets *A* and
*B*. In the minimum cut problem, the goal is to identify a "min cut" that has
the least number of crossing edges. A crossing edge is an edge with one endpoint
on each side of the cut.

![graph cuts](https://www.dropbox.com/s/536o3vmkhup6ia2/graphs.jpg?raw=1)

The minimum cut problem is a specific variant of the more general graph
partition problem (how to divide a graph). There are many applications of graph
partition problems, for example:
- Identifying bottlenecks or weakest points in a network - Roughgarden gives the
  example of declassified Cold War documents that detail the US and USSRs
  efforts to identify the most effective way to disrupt transportation networks.
- Identifying communities within a relationship network - the minimum cut can
  identify pockets of a graph that are highly connected to each other but weakly
  connected to other parts of the graph.
- Identifying objects in an image - images can be represented as grid graphs
  where each pixel is a vertex and edges are adjacent pixels. You can attempt to
  identify objects in an image if you weight the edges by how similar the pixel
  is to it's neighbor and take the min cut.

![example cuts](https://www.dropbox.com/s/hp74sdzuvuf1c9g/min-cut.png?raw=1)