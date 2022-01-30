import unittest
import pathlib
from algorithms_mixtape.graphs.kargers_min_cut import min_cut


def read_adjacency_list():
    path = (
        pathlib.Path(__file__).resolve().parents[0]
        / "fixtures/graph_adjacency_list.txt"
    )
    with open(path, "r") as file:
        adjacency_list = [line.strip().split("\t") for line in file]
    return adjacency_list


class TestKargersMinCut(unittest.TestCase):
    def test_min_cut(self):
        adjacency_list = read_adjacency_list()
        graph = {v[0]: v[1:] for v in adjacency_list}
        observed_min = min_cut(graph)
        self.assertEqual(17, observed_min)


if __name__ == "__main__":
    unittest.main()
