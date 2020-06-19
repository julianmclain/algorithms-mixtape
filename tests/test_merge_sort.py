import unittest
from src.merge_sort.merge_sort import merge_sort


class TestMergeSort(unittest.TestCase):

    def test_small(self):
        """
        Test merge_sort on a small input array
        """
        input = [5, 10, 11, 4, 1, 8, 7, 2, 6, 3, 9]
        expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
        sorted = merge_sort(input)
        self.assertEqual(expected, sorted)


if __name__ == '__main__':
    unittest.main()
