import unittest
from algorithms_mixtape.graphs.depth_first_search import (
    dfs,
    recursive_dfs,
    topo_sort
)


class DepthFirstSearchTest(unittest.TestCase):
    def setUp(self):
        self.graph = {
            "A": ["B", "G"],
            "B": ["C"],
            "C": ["D", "F"],
            "D": ["E", "F"],
            "E": [],
            "F": [],
            "G": ["C"],
        }  # graph image: https://www.dropbox.com/s/xukwybssi59gza0/test-dag.png?raw=1

    def test_dfs(self):
        self.assertEqual(["A", "G", "C", "F", "D", "E", "B"], dfs(self.graph, "A"))

    def test_recursive_dfs(self):
        self.assertEqual(["A", "B", "C", "D", "E", "F", "G"], recursive_dfs(self.graph, "A"))

    def test_topo_sort(self):
        # TODO
        pass
