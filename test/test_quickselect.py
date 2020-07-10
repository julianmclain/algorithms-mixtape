import unittest
from pathlib import Path
from algorithms_mixtape.quickselect.quickselect import quickselect


class TestQuickSelect(unittest.TestCase):

    def test_small(self):
        test_data = [5, 10, 4, 1, 8, 7, 2, 6, 3, 9]
        k = 7
        result = quickselect(test_data, k)
        self.assertEqual(k, result)

    def test_large(self):
        path = Path(__file__).resolve(
        ).parents[0] / 'fixtures/1_to_10000_distinct_unordered.txt'
        with open(path, mode='r') as file:
            test_data = [int(line) for line in file]
        k = 2222
        result = quickselect(test_data, k)
        self.assertEqual(k, result)


if __name__ == '__main__':
    unittest.main()
