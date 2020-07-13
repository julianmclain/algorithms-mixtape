# Breadth-First Search (BFS)

Intuitively, you can think of BFS as the most cautious way to explore a graph.
BFS explores the graph in "layers." If the starting point *S*
is layer 0, then the neighbors of *S* constitute layer 1, the neighbors of
vertices in layer 1 constitute layer 2, and so forth. BFS is an ideal solution
for computing the shortest path to a vertex. The algorithm will never have to
explore vertices beyond the layer where the target vertex lies. BFS can also
be used to compute the connected compononents of an undirected graph. Depth-first
search should be used for computing the connected components of directed graphs.

![graph-bfs](https://www.dropbox.com/s/kscbqr6ygq9ywrp/graph-bfs.jpg?raw=1)

## Implementation

### Input

A graph representation *G* and a starting vertex *s*.

### Output

In this abstract form of the algorithm, there is no output. As a side-affect,
all vertices of the graph will have been visited.

### Description
- Mark the starting vertex *s* as explored
- Let *Q* = a queue data structure (FIFO), initialized with *s*
- While *Q* is non-empty:
  - Remove the first vertex from *Q*, call it *v*
  - For each edge (*v*, *w*):
    - If *w* is unexplored, mark it explored and add it to the queue

## Asymptotic Runtime 

The While loop has to traverse *n* vertices, so the runtime is at least
*O*(*n*). For each vertex, it has to inspect it's edges. That means that the
algorithm will read all *m* edges. That means BFS must do *O*(*m*) work as well.
All the queue operations can be done in constant time, so we end up with:

> *O*(*n* + *m*)
