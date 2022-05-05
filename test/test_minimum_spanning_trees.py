import unittest
from collections import defaultdict
from typing import Dict, List, Tuple
from algorithms_mixtape.graphs.minimum_spanning_trees import prim_mst_naive, prim_mst, kruskal_mst_naive, kruskal_mst
from algorithms_mixtape.heaps.heap import StandardLibHeap
from algorithms_mixtape.union_finds.union_find import IntUnionFind, GeneralPurposeUnionFind
from helpers import FIXTURE_DIRECTORY_PATH


"""
Graph
1 --------1-------- 2
|  \                |
|      \            |
4          3        2    
|             \     |
|                 \ |
3 --------5-------- 4

MST
1 ----------------- 2
|                   |
|                   |
|                   |
|                   |
|                   |
3                   4
"""
small_graph = {
    1: [(2, 1), (4, 3), (3, 4)],
    2: [(1, 1), (4, 2)],
    3: [(1, 4), (4, 5)],
    4: [(1, 3), (2, 2), (3, 5)]
}


def read_graph(graph_name: str) -> Dict[int, List[Tuple[int, int]]]:
    graph = defaultdict(list)
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


class TestMinimumSpanningTrees(unittest.TestCase):
    def test_prim_mst_naive(self):
        self.assertEqual(7, prim_mst_naive(small_graph))
        self.assertEqual(14, prim_mst_naive(read_graph("mst_graph.txt")))
        self.assertEqual(-3612829, prim_mst_naive(read_graph("large_mst_graph.txt")))

    def test_prim_mst(self):
        heap = StandardLibHeap()
        self.assertEqual(7, prim_mst(small_graph, heap))
        self.assertEqual(14, prim_mst(read_graph("mst_graph.txt"), heap))
        self.assertEqual(-3612829, prim_mst(read_graph("large_mst_graph.txt"), heap))

    def test_kruskal_mst_naive(self):
        self.assertEqual(7, kruskal_mst_naive(small_graph))
        self.assertEqual(14, kruskal_mst_naive(read_graph("mst_graph.txt")))
        self.assertEqual(-3612829, kruskal_mst_naive(read_graph("large_mst_graph.txt")))

    def test_kruskal_mst(self):
        small_graph_keys = sorted(list(small_graph.keys()))
        self.assertEqual(7, kruskal_mst(small_graph, IntUnionFind(small_graph_keys)))
        self.assertEqual(7, kruskal_mst(small_graph, GeneralPurposeUnionFind(small_graph_keys)))

        medium_graph = read_graph("mst_graph.txt")
        medium_graph_keys = sorted(list(medium_graph.keys()))
        self.assertEqual(14, kruskal_mst(medium_graph, IntUnionFind(medium_graph_keys)))
        self.assertEqual(14, kruskal_mst(medium_graph, GeneralPurposeUnionFind(medium_graph_keys)))

        large_graph = read_graph("large_mst_graph.txt")
        large_graph_keys = sorted(list(large_graph.keys()))
        self.assertEqual(-3612829, kruskal_mst(large_graph, IntUnionFind(large_graph_keys)))
        self.assertEqual(-3612829, kruskal_mst(large_graph, GeneralPurposeUnionFind(large_graph_keys)))
