import unittest
import pathlib
from algorithms_mixtape.kargers_min_cut.kargers_min_cut import min_cut
from test.helpers import read_adjacency_list


PATH_TO_ADJACENCY_LIST = (
    pathlib.Path(__file__).resolve().parents[0] / "fixtures/graph_adjacency_list.txt"
)


class TestKargersMinCut(unittest.TestCase):
    def test_min_cut(self):
        adjacency_list = read_adjacency_list(PATH_TO_ADJACENCY_LIST)
        graph = {v[0]: v[1:] for v in adjacency_list}
        observed_min = min_cut(graph)
        self.assertEqual(17, observed_min)


if __name__ == "__main__":
    unittest.main()
