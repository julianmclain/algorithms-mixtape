import unittest
from typing import Dict, List, Tuple
from collections import defaultdict

from .helpers import FIXTURE_DIRECTORY_PATH
from algorithms_mixtape.graphs.clustering import kclustering


def read_graph(filename: str) -> Dict[int, List[Tuple[int, int]]]:
    graph = defaultdict(list)
    with open(FIXTURE_DIRECTORY_PATH / filename, "r") as f:
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


class TestClustering(unittest.TestCase):
    def test_kclustering(self):
        graph = read_graph("clustering_graph.txt")
        self.assertEqual(106, kclustering(graph, k=4))
