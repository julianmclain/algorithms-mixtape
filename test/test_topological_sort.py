import unittest
from typing import Dict, List
from algorithms_mixtape.graphs.topological_sort import topo_sort, dfs_topo_sort


def is_valid_topo_sort(graph: Dict[int, int], topo_sort: List[int]) -> bool:
    """Check if topological sort is valid

    A topological sort is valid if for each edge *u* -> *v*, *u* comes before *v* in the ordering
    """
    if not graph or not topo_sort:
      return False

    seen = set()

    for u, v in get_edge_list(graph):
        if topo_sort.index(u) > topo_sort.index(v):
            return False

    return True


def get_edge_list(graph: Dict[int, int]) -> List[List[int]]:
    edges = []

    for u, neighbors in graph.items():
      for v in neighbors:
        edges.append([u, v]) 

    return edges


class TopologicalSortTest(unittest.TestCase):
    def setUp(self):
        # [Graph image](https://www.dropbox.com/s/aprbzlhnlp1h0yb/topo-sort.png?raw=1)
        self.graph = {
          2: [],
          3: [8, 10],
          5: [11],
          7: [8, 11],
          8: [9],
          9: [],
          10: [],
          11: [2, 9, 10]
        }

        self.graph_with_loop = {
          0: [1],
          1: [2],
          2: [0],
          3: [0, 4],
          4: []
        }
    
    def test_is_valid_solution_helper(self):
        # The graph has many valid topological orderings
        self.SOLUTION_1 = [5, 7, 3, 11, 8, 2, 9, 10]  # (visual top-to-bottom, left-to-right)
        self.SOLUTION_2 = [3, 5, 7, 8, 11, 2, 9, 10]  # (smallest-numbered available vertex first)
        self.SOLUTION_3 = [5, 7, 3, 8, 11, 10, 9, 2]  # (fewest edges first)
        # switched the first and last of prev solution
        self.BAD_SOLUTION = [2, 7, 3, 8, 11, 10, 9, 5]

        self.assertTrue(is_valid_topo_sort(self.graph, self.SOLUTION_1))
        self.assertTrue(is_valid_topo_sort(self.graph, self.SOLUTION_2))
        self.assertTrue(is_valid_topo_sort(self.graph, self.SOLUTION_3))
        self.assertFalse(is_valid_topo_sort(self.graph, self.BAD_SOLUTION))
    
    def test_topological_sort(self):
        self.assertTrue(is_valid_topo_sort(self.graph, topo_sort(self.graph)))
        with self.assertRaises(ValueError):
            topo_sort(self.graph_with_loop)

    def test_dfs_topological_sort(self):
        self.assertTrue(is_valid_topo_sort(self.graph, dfs_topo_sort(self.graph)))
        self.assertFalse(is_valid_topo_sort(self.graph_with_loop, dfs_topo_sort(self.graph_with_loop)))
    
if __name__ == "__main__":
    unittest.main()
