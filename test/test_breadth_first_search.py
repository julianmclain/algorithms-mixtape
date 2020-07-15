import unittest
from algorithms_mixtape.graphs.breadth_first_search import (
    bfs,
    shortest_path,
    shortest_path_remix,
    connected_components,
    connected_components_remix,
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

    def test_shortest_path(self):
        self.assertEqual(3, shortest_path(self.graph, "A", "G"))

    def test_shortest_path_remix(self):
        self.assertEqual(
            ["A", "B", "E", "G"], shortest_path_remix(self.graph, "A", "G")
        )

    def test_connected_components(self):
        graph = {
            "A": set(["B", "C"]),
            "B": set(["C", "A"]),
            "C": set(["A", "B"]),
            "D": set(),
            "E": set(["F"]),
            "F": set(["E"]),
        }
        self.assertEqual(3, connected_components(graph))

    def test_connected_components_remix(self):
        graph = {
            "A": set(["B", "C"]),
            "B": set(["C", "A"]),
            "C": set(["A", "B"]),
            "D": set(),
            "E": set(["F"]),
            "F": set(["E"]),
        }
        expected = [["A", "C", "B"], ["D"], ["E", "F"]]
        components = connected_components_remix(graph)
        for e, c in zip(expected, components):
            for v in e:
                self.assertIn(v, c)
