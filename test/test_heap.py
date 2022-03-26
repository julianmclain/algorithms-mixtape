import unittest
from algorithms_mixtape.heaps.heap import StandardLibHeap


class TestStandardLibHeap(unittest.TestCase):
    def test_insert(self):
        h = StandardLibHeap()
        h.insert(5, "five")
        self.assertFalse(h.is_empty())

    def test_insert_updates_existing_item(self):
        h = StandardLibHeap()
        h.insert(2, "not_five")
        h.insert(3, "not_five")
        h.insert(1, "not_five")

        key, item = h.extract_min()
        self.assertTrue(key == 1)
        self.assertTrue(item == "not_five")
        self.assertTrue(h.is_empty())

    def test_insert_unhashable_item_raises(self):
        h = StandardLibHeap()

        with self.assertRaises(TypeError):
            h.insert(2, ["not_five"])

    def test_extract_min(self):
        h = StandardLibHeap()
        h.insert(5, "five")
        h.insert(1, "one")
        h.insert(2, "two")

        key, item = h.extract_min()
        self.assertTrue(key == 1)
        self.assertTrue(item == "one")

        key, item = h.extract_min()
        self.assertTrue(key == 2)
        self.assertTrue(item == "two")

        key, item = h.extract_min()
        self.assertTrue(key == 5)
        self.assertTrue(item == "five")

    def test_extract_min_with_empty_heap_raises(self):
        h = StandardLibHeap()
        with self.assertRaises(IndexError):
            h.extract_min()

    def test_extract_min_with_duplicate_keys(self):
        h = StandardLibHeap()
        h.insert(5, "fiveA")
        h.insert(5, "fiveB")
        h.insert(5, "fiveC")
        h.insert(1, "oneA")
        h.insert(1, "oneB")
        h.insert(2, "two")

        key, item = h.extract_min()
        self.assertTrue(key == 1)
        self.assertTrue(item == "oneA" or item == "oneB")

        key, item = h.extract_min()
        self.assertTrue(key == 1)
        self.assertTrue(item == "oneA" or item == "oneB")

        key, item = h.extract_min()
        self.assertTrue(key == 2)
        self.assertTrue(item == "two")

    def test_delete(self):
        h = StandardLibHeap()
        h.insert(5, "five")
        h.insert(1, "one")
        h.insert(2, "two")

        h.delete("one")

        key, item = h.extract_min()
        self.assertTrue(key == 2)
        self.assertTrue(item == "two")

    def test_delete_with_duplicate_keys(self):
        h = StandardLibHeap()
        h.insert(5, "five")
        h.insert(1, "oneA")
        h.insert(1, "oneB")
        h.insert(2, "two")

        h.delete("oneA")

        key, item = h.extract_min()
        self.assertTrue(key == 1)
        self.assertTrue(item == "oneB")

    def test_delete_nonexistent_item_raises(self):
        h = StandardLibHeap()
        h.insert(1, "one")

        with self.assertRaises(KeyError):
            h.delete("two")

    def test_is_empty(self):
        h = StandardLibHeap()
        self.assertTrue(h.is_empty())

        h.insert(5, "five")
        self.assertFalse(h.is_empty())

        h.extract_min()
        self.assertTrue(h.is_empty())
