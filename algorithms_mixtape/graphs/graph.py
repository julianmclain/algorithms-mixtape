import itertools
from typing import List, Dict, Set
from collections import defaultdict


class WeightedEdge:
    def __init__(self, tail: int, head: int, weight: int):
        self.tail = tail
        self.head = head
        self.weight = weight

    def __repr__(self):
        return f"(tail={self.tail} head={self.head} weight={self.weight})"


class WeightedGraph:
    def __init__(self):
        self.graph: Dict[int, List[WeightedEdge]] = defaultdict(list)

    @property
    def vertices(self) -> List[int]:
        return list(self.graph.keys())

    def edges(self) -> List[WeightedEdge]:
        return list(itertools.chain(*self.graph.values()))

    def get_outgoing_edges(self, vertex: int) -> List[WeightedEdge]:
        """
        Get a list of edges in the which provided vertex is the tail of the edge
        """
        return self.graph[vertex]

    def add_edge(self, edge: WeightedEdge) -> None:
        """
        Add an edge to the graph
        """
        self.graph[edge.tail].append(edge)

    def find_frontier_crossing_edges(self, explored: Set[int]) -> List[WeightedEdge]:
        """
        Given a set of vertices in an explored section of the graph, find edges with
        the tail in explored and head in unexplored
        """
        edges = []
        for tail in explored:
            for incident_edge in self.get_outgoing_edges(tail):
                if incident_edge.head not in explored:
                    edges.append(incident_edge)
        return edges
