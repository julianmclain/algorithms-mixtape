# Depth First Search

Intuitively, you can think of depth-first search as the aggressive way to search
a graph. DFS explores the graph by traversing edges directed away from the
starting point, only backtracking when necessary.

![graph-dfs](https://www.dropbox.com/s/kc8xzwqupxw5gxt/graph-dfs.jpg?dl=0)

## Implementation

### Input

A graph representation *G* and a starting vertex *s*.

### Output

In this abstract form of the algorithm, there is no output. As a side-affect,
all vertices of the graph will have been visited.

### Description

Imperative approach:
- For an imperative implementation, you can use the same approach as BFS,
  swapping the queue out for a stack (LIFO).

Recursive approach:
- Mark the vertex *s* as explored
- For every edge (*s*, *v*), call *DFS* again with *v* if *v* is unexplored.

## Asymptotic Runtime

> *O*(*n* + *m*)