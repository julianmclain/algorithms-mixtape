import unittest
from algorithms_mixtape.arrays.array_operations import remove_element, duplicate_element, remove_duplicates


class TestArrayOperations(unittest.TestCase):

    def test_remove_element(self):
        nums = [0, 1, 2, 2, 3, 0, 4, 2]
        val = 2
        expected = [0, 1, 3, 0, 4]
        n = remove_element(nums, val)
        self.assertEqual(expected, nums[:n])

    def test_duplicate_element(self):
        nums = [1, 0, 2, 3, 0, 4, 5, 0]
        val = 0
        expected = [1, 0, 0, 2, 3, 0, 0, 4]
        duplicate_element(nums, 0)
        self.assertEqual(expected, nums)

    def test_duplicate_element_not_present(self):
        nums = [1, 2, 3]
        val = 0
        expected = [1, 2, 3]
        duplicate_element(nums, 0)
        self.assertEqual(expected, nums)

    def test_remove_duplicates(self):
        nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
        expected = [0, 1, 2, 3, 4]
        n = remove_duplicates(nums)
        self.assertEqual(5, n)
        self.assertEqual(expected, nums[:5])
