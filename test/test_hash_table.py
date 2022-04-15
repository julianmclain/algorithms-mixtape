import unittest
from algorithms_mixtape.hash_tables.hash_table import HashTable


class TestHashTable(unittest.TestCase):
    def test_size_0_when_empty(self):
        h = HashTable()
        self.assertEqual(h.size, 0)

    def test_size_after_put(self):
        h = HashTable()
        h.put(1, "test")
        h.put(2, "test")
        self.assertEqual(h.size, 2)

    def test_get(self):
        h = HashTable()
        h.put(1, "test")
        self.assertEqual(h.get(1), "test")

    def test_get_when_load_factor_greater_than_1(self):
        h = HashTable()
        for i in range(1000):
            h.put(i, "test")
        for i in range(1000):
            self.assertEqual(h.get(i), "test")
