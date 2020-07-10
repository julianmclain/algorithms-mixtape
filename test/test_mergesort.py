import unittest
from algorithms_mixtape.mergesort.mergesort import mergesort


class TestMergeSort(unittest.TestCase):

    def test_small(self):
        test_data = [5, 10, 11, 4, 1, 8, 7, 2, 6, 3, 9]
        expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
        sorted = mergesort(test_data)
        self.assertEqual(expected, sorted)

    def test_duplicates(self):
        test_data = [5, 10, 4, 4, 1, 8, 7, 2, 6, 3, 7]
        expected = [1, 2, 3, 4, 4, 5, 6, 7, 7, 8, 10]
        sorted = mergesort(test_data)
        self.assertEqual(expected, sorted)


if __name__ == '__main__':
    unittest.main()
