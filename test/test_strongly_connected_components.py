import unittest
import pathlib
from typing import Dict, Set, List, Tuple
from collections import defaultdict
from algorithms_mixtape.graphs.strongly_connected_components import scc


class StronglyConnectedComponentsTest(unittest.TestCase):
    def setUp(self):
        # str -> ([incoming], [outgoing])
        self.small_graph = {
            "0": (["1"], ["2", "3"]),
            "1": (["2"], ["0"]),
            "2": (["0"], ["1"]),
            "3": (["0"], ["4"]),
            "4": (["3"], []),
        }
        self.graph = self.create_graph_from_fixture("scc_graph_1.txt")

    def create_graph_from_fixture(
        self, file_name: str
    ) -> Dict[str, Tuple[List[str], List[str]]]:
        """ returns dict of str -> (incoming_neighbors, outgoing_neighbors)
        """
        path = pathlib.Path(__file__).resolve().parents[0] / f"fixtures/{file_name}"
        graph = defaultdict(lambda: tuple([[], []]))
        with open(path, "r") as f:
            for line in f:
                u, v = line.strip().split(" ")
                graph[v][0].append(u)
                graph[u][1].append(v)

        return graph

    def test_create_graph_from_fixture(self):
        first_20_edges = []
        path = pathlib.Path(__file__).resolve().parents[0] / "fixtures/scc_graph_1.txt"
        with open(path, "r") as f:
            for _ in range(20):
                u, v = f.readline().strip().split(" ")
                first_20_edges.append((u, v))
        for u, v in first_20_edges:
            self.assertTrue(v in self.graph[u][1])  # check outgoing
            self.assertTrue(u in self.graph[v][0])  # check incoming

    def test_scc_small_graph(self):
        result = scc(self.small_graph)
        scc_sizes = list(result.values())
        self.assertEqual([1, 1, 3], scc_sizes)

    # @unittest.skip("The graph is huge so this takes a long time")
    def test_scc_large_graph(self):
        result = scc(self.graph)
        scc_sizes = list(result.values())
        scc_sizes.sort(reverse=True)
        largest_5_sccs = scc_sizes[:5]
        self.assertEqual(largest_5_sccs, [434821, 968, 459, 313, 211])
