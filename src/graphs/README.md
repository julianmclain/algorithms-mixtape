# Graphs

A graph is composed of 2 ingredients:
- Vertices aka Nodes - They can be used interchangeably.
- Edges - Pairs of nodes.

Furthermore, edges can be either directed or undirected. If the graph is
directed, then the edges are ordered. The edges of a directed graph are often
called arcs. For example if an arc (x, y) is directed from x to y:
- y is called the head and x is called the tail of the arc
- y is said to be a direct successor of x
- x is said to be a direct predecessor of y
- y is said to be reachable from x
- The arc (y, x) is called the inverted arc of (x, y)

Examples of graphs:
- Road networks - the intersections correspond to vertices and the roads
  correspond to edges.
- The Internet - web pages correspond to vertices and hyperlinks correspond
  edges.
- Social networks - individuals correspond to vertices and relationships
  correspond to edges.

## Graph representations

Let *n* represent the number of vertices and *m* represent the number of edges.

If you consider an undirected grpah with *n* verticies, no parallel edges, and is connected, the following is true:
- The min number of possible edges is *n* - 1
- The max number of possible edges is *n*(*n* - 1)/2

In most cases, you'll work with a connected graph with no parallel edges. When
that's the case, m is Ω(*n*) and *O*(*n*<sup>2</sup>).

The exact definition varies, but if *m* is closer to the lower bound, it's a
**sparse** graph. If *m* is closer to the upper bound, it's a **dense** graph.

There's 2 common graph representations:
- Adjacency Matrices
- Adjacency Lists

For an adjacency matrix, picture an *n* x *n* matrix A where A<sub>ij</sub> is 1
if i-j has an edge and 0 if there i-j does not have an edge. This representation
can be easily modified to support parallel edges (each increment of 1 indicates
an edge), weights (values between 0 and 1), and more. Think about the space
requirements for an adjacency matrix. The matrix must be *n*<sup>2</sup>
regardless of *m*. For that reason, adjacency matrices are ideal for dense
graphs.

For adjacency lists, there are the following ingredients:
- An array of vertices
- An array of edges
- Each edge entry stores a pointer to its endpoints (2 vertices)
- Each vertex entry stores a pointer to its edges 

Think about the space requirements for adjacency lists. It's equal to Θ(*n* + *m*). For this reason, adjacency matrices are better suited to sparce graphs.