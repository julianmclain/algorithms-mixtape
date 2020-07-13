# Undirected Connectivity

The goal of graph connectivity is to compute all of the "connected components"
of a graph *G*.

![undirected-graph-conn](https://www.dropbox.com/s/f397saccydcnfd6/undirected-graph-conn.jpg?dl=0)

For undirected graphs, this problem can be solved with BFS or DFS.

## Implementation

### Input

A graph representation *G*.

### Output

The number of connected components in the graph *G*.

### Description
- Let *k* = the number of connected components. Set it to 0.
- For all *n* nodes in the graph:
  - If *n* hasn't been explored:
    - Increment k
    - Run the BFS or DFS sub-routine

## Asymptotic Runtime

> *O*(*n* + *m*)