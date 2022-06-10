import unittest
import pathlib
from typing import List, Tuple, Set
from collections import namedtuple


KnapsackItem = namedtuple("KnapsackItem", "value weight")


def knapsack(items: List[Tuple[int, int]], knapsack_size: int) -> int:
    table = get_lookup_table(items, knapsack_size)
    return table[-1][-1]


def get_lookup_table(items: List[KnapsackItem], knapsack_size: int) -> List[List[int]]:
    table = [[]*knapsack_size for _ in range(len(items)+1)]

    for i in range(knapsack_size+1):
        table[0].append(0)

    for i, item in enumerate(items, 1):
        for j in range(knapsack_size+1):
            # Take previous solution or previous solution minus curr item weight plus curr item value
            knapsack_with_curr = table[i-1][j-item.weight] + item.value if j - item.weight >= 0 else 0
            knapsack_without_curr = table[i-1][j]
            table[i].append(max(knapsack_with_curr, knapsack_without_curr))

    return table


def knapsack_reconstruction(items: List[KnapsackItem], lookup_table: List[List[int]]) -> Set[int]:
    optimal_knapsack = set()
    i = len(lookup_table) - 1
    knapsack_capacity = len(lookup_table[0]) - 1
    while i >= 1 and knapsack_capacity > 0:
        curr_total = lookup_table[i][knapsack_capacity]
        if curr_total != lookup_table[i-1][knapsack_capacity]:
            optimal_knapsack.add(i)
            knapsack_capacity -= items[i-1].weight
        i -= 1

    return optimal_knapsack


def read_knapsack_items(filename: str) -> List[KnapsackItem]:
    """
    The input file describes a knapsack instance, and it has the following format:

    [knapsack_size][number_of_items]
    [value_1] [weight_1]
    [value_2] [weight_2]
    ...
    """
    file_path = pathlib.Path(__file__).resolve().parents[0] / filename
    out = []
    with open(file_path, 'r') as f:
        f.readline()  # first line is a header
        for line in f:
            value, weight = line.split(" ", 1)
            out.append(KnapsackItem(int(value), int(weight)))

    return out


def read_knapsack_size(filename: str) -> int:
    file_path = pathlib.Path(__file__).resolve().parents[0] / filename
    with open(file_path, 'r') as f:
        header = f.readline()
        header_parts = header.split(" ")
        return int(header_parts[0])


class TestKnapsack(unittest.TestCase):
    def test_knapsack_small(self):
        items = read_knapsack_items("knapsack-items-small.txt")
        size = read_knapsack_size("knapsack-items-small.txt")
        solution = knapsack(items, size)
        self.assertEqual(4, solution)

    def test_knapsack(self):
        items = read_knapsack_items("knapsack-items.txt")
        size = read_knapsack_size("knapsack-items.txt")
        solution = knapsack(items, size)
        self.assertEqual(2493893, solution)

    def test_knapsack_reconstruction(self):
        items = read_knapsack_items("knapsack-items-small.txt")
        size = read_knapsack_size("knapsack-items-small.txt")
        lookup_table = get_lookup_table(items, size)
        optimal_items = knapsack_reconstruction(items, lookup_table)
        self.assertEqual({2, 4}, optimal_items)
