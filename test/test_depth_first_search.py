import unittest
from algorithms_mixtape.graphs.depth_first_search import (
    dfs,
)


class DepthFirstSearchTest(unittest.TestCase):
    def setUp(self):
        self.graph = {'A': ['D', 'C', 'B'],
                            'B': ['E'],
                            'C': ['A', 'H'],
                            'D': ["A"],
                            'E': ["B", "F"],
                            "F": ["E", "G"],
                            "G": ["F"],
                            "H": ["C"],
                      }

    def test_dfs(self):
        self.assertEqual(['A', 'B', 'E', 'F', 'G', 'C', 'H', 'D'], dfs(self.graph, "A"))

