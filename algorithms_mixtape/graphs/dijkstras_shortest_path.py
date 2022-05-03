import math
from numbers import Number
from typing import Dict, List
from collections import defaultdict
from functools import reduce

from algorithms_mixtape.graphs.graph import WeightedGraph, WeightedEdge
from algorithms_mixtape.heaps.heap import StandardLibHeap, Heap, MyHeap


def shortest_path_naive(graph: WeightedGraph, start) -> Dict[int, int]:
    """
    Note that if a vertex can't be reached from start, its distance is recorded as -1

    :param graph:
    :param start:
    :return: dictionary of vertex label to shortest distance to start
    """
    seen = {start}
    dists = defaultdict(lambda: -1)
    dists[start] = 0

    frontier_crossing_edges = graph.find_frontier_crossing_edges(seen)
    while len(frontier_crossing_edges) > 0:
        shortest_edge = _find_shortest_edge(frontier_crossing_edges, dists)
        dists[shortest_edge.head] = dists[shortest_edge.tail] + shortest_edge.weight
        seen.add(shortest_edge.head)
        frontier_crossing_edges = graph.find_frontier_crossing_edges(seen)

    return dists


def _find_shortest_edge(
    edges: List[WeightedEdge], distances: Dict[int, int]
) -> WeightedEdge:
    """
    Compute Dijkstra's greedy criterion

    The `distances` dict is guaranteed to have a distance for the tail of every edge because this
    method is called with frontier-crossing edges. In prod code you'd want to enforce that logical
    dependency somehow.
    """
    shortest_edge = reduce(
        lambda e1, e2: e1
        if distances[e1.tail] + e1.weight <= distances[e2.tail] + e2.weight
        else e2,
        edges,
    )
    return shortest_edge


def shortest_path(graph: WeightedGraph, start, use_my_heap=False) -> Dict[int, Number]:
    """
    The distance to unreachable vertices is infinity

    :param graph:
    :param start:
    :return: dictionary of vertex label to shortest distance to start
    """
    dists = defaultdict(lambda: math.inf)
    dists[start] = 0
    for v in graph.vertices:
        if v is not start:
            dists[v] = math.inf

    heap = MyHeap() if use_my_heap else StandardLibHeap()
    for v in graph.vertices:
        heap.insert(key=dists[v], item=v)

    while not heap.is_empty():
        dist, w = heap.extract_min()
        dists[w] = dist
        ensure_min_dijkstra_scores(graph, w, heap, dists)

    return dists


def ensure_min_dijkstra_scores(
    graph: WeightedGraph, vertex: int, heap: Heap, dists: Dict[int, Number]
) -> None:
    """
    This function maintains the following invariant:

    The heap key of vertex `y` taken from unexplored territory in the graph is the minimum Dijkstra score of an edge
    with tail `w` taken from the explored and head `y`, or positive infinity if no such edge exists.
    """
    ys = [e.head for e in graph.get_outgoing_edges(vertex)]
    for edge in graph.get_outgoing_edges(vertex):
        dist_from_w = dists[vertex] + edge.weight
        y = edge.head
        # If dist from w is shorter, update distance to y and replace heap entry with one containing the shorter dist.
        # Some heaps support a `decrease_key` operation which eliminates the need to delete + insert.
        if dist_from_w < dists[y]:
            dists[y] = dist_from_w
            heap.delete(y)
            heap.insert(dist_from_w, y)
