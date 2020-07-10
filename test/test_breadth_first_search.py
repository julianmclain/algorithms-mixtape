import unittest
import pathlib
from . import read_adjacency_list

PATH_TO_ADJACENCY_LIST = pathlib.Path(__file__).resolve(
).parents[0] / 'fixtures/graph_adjacency_list.txt'


class TestBreadthFirstSearch(unittest.TestCase):

    def testUndirectedGraphBFS(self):
        graph = read_adjacency_list(PATH_TO_ADJACENCY_LIST)
