import unittest
from algorithms_mixtape.insertion_sort.insertion_sort import insertion_sort


class TestInsertionSort(unittest.TestCase):

    def test_small(self):
        test_data = [5, 10, 11, 4, 1, 8, 7, 2, 6, 3, 9]
        expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
        insertion_sort(test_data)
        self.assertEqual(expected, test_data)
