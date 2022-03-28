import unittest
from algorithms_mixtape.heaps.heap import StandardLibHeap, MyHeap


class TestHeap(unittest.TestCase):
    """
    It would be good to figure out a better way to execute the exact same tests for 2 implementations.

    Pytest has good test parameterization support which would've worked well. Apparently the unittest
    equivalent is the `with self.subtTest():` context manager. I didn't like the way it reported test
    failures. They didn't show up on the main test run report line. E.g. these failures don't mark the
    test as a failure (F):
    ```
        ❯ python3 -m unittest discover
        ................................ss.....
        ======================================================================
        FAIL: test_insert (test.test_heap.TestHeap) (h=<algorithms_mixtape.heaps.heap.MyHeap object at 0x10fec6370>)
        ----------------------------------------------------------------------
        Traceback (most recent call last):
          File "/Users/julianmclain/code/algorithms-mixtape/test/test_heap.py", line 14, in test_insert
            self.assertTrue(h.is_empty())
        AssertionError: None is not true

        ======================================================================
        FAIL: test_insert_updates_existing_item (test.test_heap.TestHeap) (<subtest>)
        ----------------------------------------------------------------------
        Traceback (most recent call last):
          File "/Users/julianmclain/code/algorithms-mixtape/test/test_heap.py", line 27, in test_insert_updates_existing_item
            self.assertTrue(item == "not_five")
        AssertionError: False is not true

        ----------------------------------------------------------------------
        Ran 41 tests in 2.883s
    ```
    """

    def setUp(self) -> None:
        std_lib_heap = StandardLibHeap()
        my_heap = MyHeap()
        self.heap_implementations = [std_lib_heap, my_heap]

    def test_insert(self):
        for h in self.heap_implementations:
            self.assertTrue(h.is_empty(), h.__class__.__name__)
            h.insert(5, "five")
            self.assertFalse(h.is_empty(), h.__class__.__name__)

    def test_insert_updates_existing_item(self):
        for h in self.heap_implementations:
            h.insert(2, "not_five")
            h.insert(3, "not_five")
            h.insert(1, "not_five")

            key, item = h.extract_min()
            self.assertTrue(key == 1, h.__class__.__name__)
            self.assertTrue(item == "not_five", h.__class__.__name__)
            self.assertTrue(h.is_empty(), h.__class__.__name__)

    def test_insert_unhashable_item_raises(self):
        for h in self.heap_implementations:
            with self.assertRaises(TypeError):
                h.insert(2, ["not_five"])

    def test_extract_min(self):
        for h in self.heap_implementations:
            h.insert(5, "five")
            h.insert(1, "one")
            h.insert(2, "two")

            key, item = h.extract_min()
            self.assertTrue(key == 1, h.__class__.__name__)
            self.assertTrue(item == "one", h.__class__.__name__)

            key, item = h.extract_min()
            self.assertTrue(key == 2, h.__class__.__name__)
            self.assertTrue(item == "two", h.__class__.__name__)

            key, item = h.extract_min()
            self.assertTrue(key == 5, h.__class__.__name__)
            self.assertTrue(item == "five", h.__class__.__name__)

    def test_extract_min_with_empty_heap_raises(self):
        for h in self.heap_implementations:
            with self.assertRaises(IndexError):
                h.extract_min()

    def test_extract_min_with_duplicate_keys(self):
        for h in self.heap_implementations:
            h.insert(5, "fiveA")
            h.insert(5, "fiveB")
            h.insert(5, "fiveC")
            h.insert(1, "oneA")
            h.insert(1, "oneB")
            h.insert(2, "two")

            key, item = h.extract_min()
            self.assertTrue(key == 1, h.__class__.__name__)
            self.assertTrue(item == "oneA" or item == "oneB", h.__class__.__name__)

            key, item = h.extract_min()
            self.assertTrue(key == 1, h.__class__.__name__)
            self.assertTrue(item == "oneA" or item == "oneB", h.__class__.__name__)

            key, item = h.extract_min()
            self.assertTrue(key == 2, h.__class__.__name__)
            self.assertTrue(item == "two", h.__class__.__name__)

    def test_delete(self):
        for h in self.heap_implementations:
            h.insert(5, "five")
            h.insert(1, "one")
            h.insert(2, "two")

            h.delete("one")

            key, item = h.extract_min()
            self.assertTrue(key == 2, h.__class__.__name__)
            self.assertTrue(item == "two", h.__class__.__name__)

    def test_delete_with_duplicate_keys(self):
        for h in self.heap_implementations:
            h.insert(5, "five")
            h.insert(1, "oneA")
            h.insert(1, "oneB")
            h.insert(2, "two")

            h.delete("oneA")

            key, item = h.extract_min()
            self.assertTrue(key == 1, h.__class__.__name__)
            self.assertTrue(item == "oneB", h.__class__.__name__)

    def test_delete_nonexistent_item_raises(self):
        for h in self.heap_implementations:
            h.insert(1, "one")

            with self.assertRaises(KeyError):
                h.delete("two")

    def test_is_empty(self):
        for h in self.heap_implementations:
            self.assertTrue(h.is_empty(), h.__class__.__name__)

            h.insert(5, "five")
            self.assertFalse(h.is_empty(), h.__class__.__name__)

            h.extract_min()
            self.assertTrue(h.is_empty(), h.__class__.__name__)
