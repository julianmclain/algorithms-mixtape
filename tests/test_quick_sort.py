import unittest
import pathlib
from src.quick_sort.quick_sort import quick_sort


class TestMergeSort(unittest.TestCase):

    def test_small(self):
        """
        Test quick_sort on a small input array
        """
        test_data = [5, 10, 4, 1, 8, 7, 2, 6, 3, 9]
        expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        quick_sort(test_data)
        self.assertEqual(expected, test_data)

    def test_large(self):
        path = pathlib.Path.cwd() / 'tests/fixtures/1_to_10000_distinct_unordered.txt'
        expected = list(range(1, 10000 + 1))
        with open(path, mode='r') as file:
            test_data = [int(line) for line in file]
        quick_sort(test_data)
        self.assertEqual(expected, test_data)


if __name__ == '__main__':
    unittest.main()
