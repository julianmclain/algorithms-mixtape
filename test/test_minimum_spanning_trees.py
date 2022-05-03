import unittest
from collections import defaultdict
from typing import Dict, List, Tuple
from algorithms_mixtape.graphs.graph import WeightedGraph, WeightedEdge
from algorithms_mixtape.graphs.minimum_spanning_trees import prim_mst_naive, prim_mst
from algorithms_mixtape.heaps.heap import StandardLibHeap
from helpers import FIXTURE_DIRECTORY_PATH


""" graph
1 --------1-------- 2
|  \                |
|      \            |
4          3        2    
|             \     |
|                 \ |
3 --------5-------- 4
"""
small_graph = {
    1: [(2, 1), (4, 3), (3, 4)],
    2: [(1, 1), (4, 2)],
    3: [(1, 4), (4, 5)],
    4: [(1, 3), (2, 2), (3, 5)]
}


small_mst_cost = 7
""" mst
1 ----------------- 2
|                   |
|                   |
|                   |    
|                   |
|                   |
3                   4
"""


# def read_medium_graph() -> WeightedGraph:
#     graph = WeightedGraph()
#     with open(FIXTURE_DIRECTORY_PATH / "mst_graph.txt", "r") as f:
#         f.readline()  # first line is a header
#         for line in f:
#             stripped_line = line.strip()
#             parts = stripped_line.split(" ", 2)
#             tail = int(parts[0])
#             head = int(parts[1])
#             weight = int(parts[2])
#             graph.add_edge(WeightedEdge(tail, head, weight))
#             graph.add_edge(WeightedEdge(head, tail, weight))  # graph is undirected
#     return graph


def read_graph(graph_name: str) -> Dict[int, List[Tuple[int, int]]]:
    graph = defaultdict(list)
    edges = []
    with open(FIXTURE_DIRECTORY_PATH / graph_name, "r") as f:
        f.readline()  # first line is a header
        for line in f:
            stripped_line = line.strip()
            parts = stripped_line.split(" ", 2)
            tail = int(parts[0])
            head = int(parts[1])
            weight = int(parts[2])
            graph[tail].append((head, weight))
            graph[head].append((tail, weight))
    return graph


def read_medium_graph() -> Dict[int, List[Tuple[int, int]]]:
    graph = defaultdict(list)
    edges = []
    with open(FIXTURE_DIRECTORY_PATH / "mst_graph.txt", "r") as f:
        f.readline()  # first line is a header
        for line in f:
            stripped_line = line.strip()
            parts = stripped_line.split(" ", 2)
            tail = int(parts[0])
            head = int(parts[1])
            weight = int(parts[2])
            graph[tail].append((head, weight))
            graph[head].append((tail, weight))
    return graph


class TestMinimumSpanningTrees(unittest.TestCase):
    def test_prim_mst_naive(self):
        min_cost = prim_mst_naive(read_graph("mst_graph.txt"))
        self.assertEqual(14, min_cost)

    def test_prim_mst(self):
        heap = StandardLibHeap()
        self.assertEqual(small_mst_cost, prim_mst(small_graph, heap))
        self.assertEqual(14, prim_mst(read_graph("mst_graph.txt"), heap))