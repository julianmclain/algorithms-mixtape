from typing import List, Dict
from collections import defaultdict


class WeightedEdge:
    def __init__(self, tail: int, head: int, weight: int):
        self.tail = tail
        self.head = head
        self.weight = weight


class WeightedGraph:
    def __init__(self):
        self.graph: Dict[int, List[WeightedEdge]] = defaultdict(list)

    @property
    def vertices(self) -> List[int]:
        return list(self.graph.keys())

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
