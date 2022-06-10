import pathlib
import unittest
from typing import List, Set


def mwis(path: List[int]) -> Set[int]:
    """Compute the maximum weight independent set of a path

    :param path: list in which each index is a vertex label and value is the weight
    :return: Set of 1-based vertex labels comprising the MWIS
    """
    weights = mwis_weights(path)
    mwis = set()

    i = len(weights) - 1
    while i >= 2:
        if weights[i-1] >= weights[i-2] + path[i-1]:
            i -= 1
        else:
            mwis.add(i)
            i -= 2

    if i == 1:
        mwis.add(1)

    return mwis


def mwis_sum(path: List[int]) -> int:
    """Compute the value of a maximum weight independent set of a path

    :param path: list in which each index is a vertex label and value is the weight
    :return: the sum of the MWIS
    """
    weights = mwis_weights(path)
    return weights[-1]


def mwis_weights(path: List[int]) -> List[int]:
    n = len(path)
    weights = [0] * (n+1)  # base case 1 solution = 0
    weights[1] = path[0]   # base case 2
    for i in range(2, n+1):
        weights[i] = max(weights[i-1], weights[i-2] + path[i-1])
        print(weights)
    return weights


def mwis_sum_recursive(path: List[int]) -> int:
    """Recursively compute the sum of the maximum weight independent set of a path

    :param path: list in which each index is a vertex label and value is the weight
    :return: the sum of the MWIS
    """
    def helper(sub_path: List[int], n: int) -> int:
        if len(sub_path) == 0:
            return 0
        elif len(sub_path) == 1:
            return sub_path[0]
        else:
            s1 = helper(sub_path[:-1], n - 1)
            s2 = helper(sub_path[:-2], n - 2) + sub_path[n]
            return max(s1, s2)

    return helper(path, len(path)-1)


def read_fixture(filename: str) -> List[int]:
    file_path = pathlib.Path(__file__).resolve().parents[0] / filename
    with open(file_path, 'r') as f:
        f.readline()  # first line is a header
        return [int(line.strip()) for line in f]


class TestMaximumWeightIndependentSet(unittest.TestCase):
    def test_maximum_weight_independent_set_small(self):
        path = read_fixture("maximum-weight-independent-set-path-small.txt")
        result = mwis(path)
        self.assertTrue(len(result) == 4)
        self.assertTrue(2 in result)
        self.assertTrue(4 in result)
        self.assertTrue(7 in result)
        self.assertTrue(10 in result)

    def test_maximum_weight_independent_set(self):
        path = read_fixture("maximum-weight-independent-set-path.txt")
        result = mwis(path)
        self.assertTrue(1 in result)
        self.assertTrue(2 not in result)
        self.assertTrue(3 in result)
        self.assertTrue(4 not in result)
        self.assertTrue(17 not in result)
        self.assertTrue(117 in result)
        self.assertTrue(517 in result)
        self.assertTrue(997 not in result)

    def test_maximum_weight_independent_set_sum_recursive(self):
        path = read_fixture("maximum-weight-independent-set-path-small.txt")
        result = mwis_sum_recursive(path)
        self.assertEqual(2617, result)

    def test_maximum_weight_independent_set_sum_small(self):
        path = read_fixture("maximum-weight-independent-set-path-small.txt")
        result = mwis_sum(path)
        self.assertEqual(2617, result)

    def test_maximum_weight_independent_set_sum_large(self):
        path = read_fixture("maximum-weight-independent-set-path.txt")
        result = mwis_sum(path)
        self.assertEqual(2955353732, result)
