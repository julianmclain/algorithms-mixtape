import unittest
from pathlib import Path
from src.kargers_min_cut.kargers_min_cut import min_cut


PATH_TO_ADJACENCY_LIST = Path(__file__).resolve().parents[0] / 'fixtures/graph_adjacency_list.txt'


def read_adjacency_list(path):
    with open(path, mode='r') as file:
        adjacency_list = [line.strip().split('\t') for line in file]
    return adjacency_list


class TestKargersMinCut(unittest.TestCase):

    def test_min_cut(self):
        adjacency_list = read_adjacency_list(PATH_TO_ADJACENCY_LIST)
        graph = {v[0]: v[1:] for v in adjacency_list}
        observed_min = min_cut(graph)
        self.assertEqual(17, observed_min)


if __name__ == '__main__':
    unittest.main()
