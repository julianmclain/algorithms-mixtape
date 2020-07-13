import unittest
import pathlib
from algorithms_mixtape.count_inversions.count_inversions import count_inversions 


class TestCountInversions(unittest.TestCase):
    def test_count_inversions_small(self):
        test1 = [1, 2, 3, 4, 5, 6]
        test2 = [1, 3, 5, 2, 4, 6]
        test3 = [6, 5, 4, 3, 2, 1]
        count1 = count_inversions(test1)
        count2 = count_inversions(test2)
        count3 = count_inversions(test3)
        self.assertEqual(0, count1)
        self.assertEqual(3, count2)
        self.assertEqual(15, count3)

    def test_count_inversions_large(self):
        """
        The test input file contains all of the 100,000 integers between 1 and
        100,000 (inclusive) in some order, with no integer repeated.

        Your task is to compute the number of inversions in the file given,
        where the i^{th} row of the file indicates the i^{th} entry of an array.
        """
        path = pathlib.Path(__file__).resolve().parents[0] / "fixtures/1_to_100000_distinct_unordered.txt"
        with open(path, 'r') as test_file:
            test_input = [int(line) for line in test_file]
        count = count_inversions(test_input)
        self.assertEqual(2407905288, count)
