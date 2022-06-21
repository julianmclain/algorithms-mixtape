import unittest
import pathlib
from typing import List


def optimal_bst(frequencies: List[int]) -> int:
    """Compute an optimal BST given a set of node frequencies

    search space:
        - every tree size 0 to n
        - every contiguous range of nodes from i to j where i <= j
        - every root r where i <= r <= j

    :param frequencies: list of node frequencies; list key used as node label
    :return: the minimum weighted search time of a lookup in the tree
    """
    solutions = get_lookup_table(frequencies)
    return solutions[0][-1]


def get_lookup_table(frequencies: List[int]) -> List[List[int]]:
    n = len(frequencies)
    table = [[0] * n for _ in range(n)]

    for s in range(0, n):
        for i in range(n - s):
            # initialize min_cost with root = i;
            min_cost = get_entry(table, i, i-1) + get_entry(table, i+1, i+s)
            for root in range(i+1, i+s+1):
                left_subtree = get_entry(table, i, root-1)
                right_subtree = get_entry(table, root+1, i+s)
                min_cost = min(min_cost, left_subtree + right_subtree)

            table[i][i + s] = min_cost + sum(frequencies[i:i+s+1])

    return table


def get_entry(table: List[List[int]], i: int, j: int, default: int = 0) -> int:
    if i < len(table) and j < len(table[i]):
        return table[i][j]
    else:
        return default


def read_bst_frequencies(filename: str) -> List[int]:
    """
    The input file describes frequencies of keys in a BST. The keys are index of
    each frequency

    [bst_size]
    [freq_1],[freq_2],[freq_3]...
    """
    file_path = pathlib.Path(__file__).resolve().parents[0] / filename
    with open(file_path, 'r') as f:
        f.readline()  # first line is a header
        return [int(x) for x in f.readline().split(",")]


class TestOptimalBinarySearchTree(unittest.TestCase):
    def test_small(self):
        frequencies = [34, 8, 50]
        optimal_cost = 142
        self.assertEqual(optimal_cost, optimal_bst(frequencies))

    def test_small_2(self):
        frequencies = [34, 50]
        optimal_cost = 118
        self.assertEqual(optimal_cost, optimal_bst(frequencies))

    def test_large(self):
        frequencies = read_bst_frequencies("optimal-bst.txt")
        optimal_cost = 2780
        self.assertEqual(optimal_cost, optimal_bst(frequencies))
