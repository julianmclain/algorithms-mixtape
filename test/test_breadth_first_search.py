import unittest
from algorithms_mixtape.graphs.breadth_first_search import (
    bfs,
    dist,
    shortest_path_remix,
    num_ucc,
    ucc,
)


class BreadthFirstSearchTest(unittest.TestCase):
    def setUp(self):
        self.graph = {
            "A": ["B", "C"],
            "B": ["A", "D", "E"],
            "C": ["A", "F"],
            "D": ["B"],
            "E": ["B", "F", "G"],
            "F": ["C", "E"],
            "G": [],
        }

    def test_bfs(self):
        self.assertEqual(["A", "B", "C", "D", "E", "F", "G"], bfs(self.graph, "A"))

    def test_dist(self):
        self.assertEqual(3, dist(self.graph, "A", "G"))

    def test_shortest_path_remix(self):
        self.assertEqual(
            ["A", "B", "E", "G"], shortest_path_remix(self.graph, "A", "G")
        )

    def test_num_ucc(self):
        graph = {
            "A": {"B", "C"},
            "B": {"C", "A"},
            "C": {"A", "B"},
            "D": set(),
            "E": {"F"},
            "F": {"E"},
        }
        self.assertEqual(3, num_ucc(graph))

    def test_ucc(self):
        graph = {
            "A": {"B", "C"},
            "B": {"C", "A"},
            "C": {"A", "B"},
            "D": set(),
            "E": {"F"},
            "F": {"E"},
        }
        expected = [["A", "C", "B"], ["D"], ["E", "F"]]
        components = ucc(graph)
        for e, c in zip(expected, components):
            for v in e:
                self.assertIn(v, c)
