# Graphs

A graph is composed of 2 ingredients:
- Vertices aka Nodes - The terms can be used interchangeably.
- Edges - Pairs of nodes.

Furthermore, edges can be either directed or undirected. If the graph is
directed, then the edges are ordered. The edges of a directed graph are often
called arcs. For example if an arc (x, y) is directed from x to y:
- y is called the head and x is called the tail 
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

If you consider an undirected graph with *n* vertices, no parallel edges, and
is connected, the following is true:
- The min number of possible edges is *n* - 1
- The max number of possible edges is *n*(*n* - 1)/2

In most cases, you'll encounter connected graphs with no parallel edges. When
that's the case, the size of *m* is Ω(*n*) and *O*(*n*<sup>2</sup>).

The exact definition varies, but if *m* is closer to the lower bound, it's a
**sparse** graph. If *m* is closer to the upper bound, it's a **dense** graph.

There's 2 common graph representations:
- Adjacency matrices
- Adjacency lists

### Adjacency Matrices

For an adjacency matrix, picture an *n* x *n* matrix A where A<sub>ij</sub> is 1
if i-j has an edge and 0 if there i-j does not have an edge. This representation
can be easily modified to support parallel edges (each increment of 1 indicates
an edge), weights (values between 0 and 1), and more. Think about the space
requirements for an adjacency matrix. The matrix must be *n*<sup>2</sup>
regardless of *m*. For that reason, adjacency matrices are ideal for dense
graphs.

### Adjacency Lists

There are various ways to represent an adjacency list. You can use a two-dimensional array in which 
each index position represents a vertex and the array stored at that index holds a pointer to adjacent vertices. Guido Van Rossum has proposed a [dict representation](https://www.python.org/doc/essays/graphs/) when working in Python. 

Tim Roughgarden proposes a representation with the following ingredients:
- An array of vertices
- An array of edges
- Each edge entry stores a pointer to its endpoints (2 vertices)
- Each vertex entry stores a pointer to its edges 

Think about the space requirements for adjacency lists. It's equal to Θ(*n* +
*m*). For this reason, adjacency matrices are better suited to sparse graphs.


## Graph Search

Applications of graph search:
- Examining connectivity - Physical networks like phone networks and highway
  networks are intuitively well suited to graphs. Non-physical networks like
  social networks, are equally applicable.
- Formulating a plan for accomplishing a goal - In a more abstract sense,
  formulating a plan can be represented as a graph where each node is a decision
  point that leads to another decision point. As a result, graphs are ubiquitous
  in AI (e.g. A robot formulating a plan on how to pickup a package).
- Computing the "pieces" (or "components") of a graph. This is useful for
  clustering or determining the structure of a graph.

Goal:
- Given a starting vertex, traverse every findable vertex in the graph.
- Don't visit any vertex more than once.
- Do it in *O*(*m* + *n*) time

Here's a generic formulation of the graph search solution. Imagine there's a
graph and you divide it into two sets, the vertices that have already been
explored, and the vertices that haven't been visited. While there are vertices
that have one endpoint in the explored territory and one endpoint in the
unexplored territory, the algorithm will choose one of such edges and follow it
to the endpoint in the unexplored territory. Once there are no such edges, it
terminates.

From this generic formulation, different graph search algorithms emerge based on
how the next edge to explore is chosen.

Note that for graph search algorithms, it typically doesn't matter whether the
graph is directed or not. Computing connectivity is an exception to that rule. 

## Connected Components

The goal of graph connectivity is to compute all of the "connected components"
of a graph *G*. The following graph has 3 components:

![undirected-graph-conn](https://www.dropbox.com/s/f397saccydcnfd6/undirected-graph-conn.jpg?raw=1)

For undirected graphs, this is an easy problem to solve. It can be done with BFS or DFS.