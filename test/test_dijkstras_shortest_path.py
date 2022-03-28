import pathlib
import unittest
from algorithms_mixtape.graphs.dijkstras_shortest_path import shortest_path_naive, shortest_path
from algorithms_mixtape.graphs.graph import WeightedEdge, WeightedGraph


def read_fixture(path) -> WeightedGraph:
    """
    The graph fixtures contain an adjacency list representation of undirected graphs with vertices
    labeled 1 to n. Each row indicates the edges incident to the given vertex along with their
    (nonnegative) lengths. For example, the sixth row has a "6" as its first entry indicating that
    this row corresponds to vertex 6. The next entry of this row "141,8200" indicates that there is
    an undirected edge between vertex 6 and vertex 141 that has length 8200. The rest of the pairs
    in this row indicate the other vertices adjacent to vertex 6 and the lengths of the corresponding edges.

    For example:
    1	2,1	8,2
    """
    graph = WeightedGraph()
    with open(path, "r") as f:
        for line in f:
            stripped_line = line.strip()
            parts = stripped_line.split("\t")

            if len(parts) >= 2:  # using 2 because we need at least a label and 1 edge
                vertex_label = int(parts[0])

                for edge_string in parts[1:]:
                    edge_parts = edge_string.split(",")
                    head = int(edge_parts[0])
                    weight = int(edge_parts[1])
                    weighted_edge = WeightedEdge(vertex_label, head, weight)
                    graph.add_edge(weighted_edge)

    return graph


class DijkstrasShortestPathTest(unittest.TestCase):
    def setUp(self):
        fixture_dir_path = pathlib.Path(__file__).resolve().parents[0] / "fixtures"
        small_undirected_graph_path = (
            fixture_dir_path / "shortest_path_small_undirected_graph.txt"
        )
        small_undirected_graph = read_fixture(small_undirected_graph_path)
        assert len(small_undirected_graph.vertices) == 8
        self.small_undirected_graph = small_undirected_graph

    def test_shortest_path_naive_small_undirected_graph(self):
        shortest_paths = shortest_path_naive(self.small_undirected_graph, 1)
        distances = [shortest_paths[i] for i in range(1, len(shortest_paths) + 1)]
        expected = [0, 1, 2, 3, 4, 4, 3, 2]  # shortest path for vertices 1 - 8 in order
        self.assertEqual(distances, expected)

    def test_shortest_path_small_undirected_graph(self):
        shortest_paths = shortest_path(self.small_undirected_graph, 1)
        distances = [shortest_paths[i] for i in range(1, len(shortest_paths) + 1)]
        expected = [0, 1, 2, 3, 4, 4, 3, 2]  # shortest path for vertices 1 - 8 in order
        self.assertEqual(distances, expected)

    def test_shortest_path_my_heap_small_undirected_graph(self):
        shortest_paths = shortest_path(self.small_undirected_graph, 1, use_my_heap=True)
        distances = [shortest_paths[i] for i in range(1, len(shortest_paths) + 1)]
        expected = [0, 1, 2, 3, 4, 4, 3, 2]  # shortest path for vertices 1 - 8 in order
        self.assertEqual(distances, expected)
