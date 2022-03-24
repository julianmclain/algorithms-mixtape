from typing import Dict, Set, List
from collections import defaultdict
from functools import reduce

from algorithms_mixtape.graphs.graph import WeightedGraph, WeightedEdge


def shortest_path(graph: WeightedGraph, start) -> Dict[int, int]:
    """
    Note that if a vertex can't be reached from start, it's distance is recorded as -1

    :param graph:
    :param start:
    :return: dictionary of vertex label to shortest distance to start
    """
    seen = {start}
    dists = defaultdict(lambda:-1)
    dists[start] = 0

    frontier_crossing_edges = _find_frontier_crossing_edges(graph, seen)
    while len(frontier_crossing_edges) > 0:
        shortest_edge = _find_shortest_edge(frontier_crossing_edges, dists)
        dists[shortest_edge.head] = dists[shortest_edge.tail] + shortest_edge.weight
        seen.add(shortest_edge.head)
        frontier_crossing_edges = _find_frontier_crossing_edges(graph, seen)

    return dists


def _find_frontier_crossing_edges(graph: WeightedGraph, seen: Set[int]) -> List[WeightedEdge]:
    """
    A frontier crossing edge is one with tail in seen and head not in seen
    """
    edges = []
    for tail in seen:
        for incident_edge in graph.incident_edges(tail):
            if incident_edge.head not in seen:
                edges.append(incident_edge)

    return edges


def _find_shortest_edge(edges: List[WeightedEdge], distances: Dict[int, int]) -> WeightedEdge:
    """
    Compute Dijkstra's greedy criterion

    The `distances` dict is guaranteed to have a distance for the tail of every edge because this
    method is called with frontier-crossing edges. In prod code you'd want to enforce that logical
    dependency somehow.
    """
    shortest_edge = reduce(lambda e1, e2: e1 if distances[e1.tail] + e1.weight <= distances[e2.tail] + e2.weight else e2, edges)
    return shortest_edge
