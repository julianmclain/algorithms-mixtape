import unittest
from algorithms_mixtape.trees.binary_tree import BinarySearchTree


class TestBinaryTree(unittest.TestCase):
    def setUp(self) -> None:
        self.small_tree = BinarySearchTree(3, "three")
        self.small_tree.insert(1, "one")
        self.small_tree.insert(2, "two")
        self.small_tree.insert(4, "four")
        self.small_tree.insert(5, "five")

        self.large_tree = BinarySearchTree(10, "ten")
        self.large_tree.insert(1, "one")
        self.large_tree.insert(2, "two")
        self.large_tree.insert(4, "four")
        self.large_tree.insert(5, "five")
        self.large_tree.insert(12, "twelve")
        self.large_tree.insert(14, "fourteen")
        self.large_tree.insert(17, "seventeen")
        self.large_tree.insert(20, "twenty")

    def test_get(self):
        self.assertEqual(self.small_tree.get(5).value, "five")
        self.assertEqual(self.small_tree.get(1).value, "one")
        self.assertEqual(self.small_tree.get(4).value, "four")

    def test_get_raises_when_key_not_found(self):
        with self.assertRaises(KeyError):
            self.small_tree.get(20)

    def test_min(self):
        self.assertEqual(self.small_tree.min.value, "one")

    def test_max(self):
        self.assertEqual(self.small_tree.max.value, "five")

    def test_predecessor(self):
        self.assertEqual(self.small_tree.predecessor.value, "two")
        self.assertEqual(self.small_tree.get(5).predecessor.value, "four")

    def test_predecessor_raises_when_tree_size_1(self):
        with self.assertRaises(ValueError):
            one_node_tree = BinarySearchTree(3, "three")
            one_node_tree.predecessor

    def test_predecessor_raises_when_min_node(self):
        with self.assertRaises(ValueError):
            min_node = self.small_tree.get(1)
            min_node.predecessor

    def test_sorted_value_list(self):
        self.assertEqual(self.small_tree.sorted_value_list, ["one", "two", "three", "four", "five"])

    def test_delete_leaf(self):
        root = self.small_tree.delete(2)
        with self.assertRaises(KeyError):
            root.get(2)
        self.assertEqual(root.sorted_value_list, ["one", "three", "four", "five"])

    def test_delete_node_with_one_child(self):
        root = self.small_tree.delete(5)
        with self.assertRaises(KeyError):
            root.get(5)
        self.assertEqual(root.sorted_value_list, ["one", "two", "three", "four"])

    def test_delete_root_with_two_children(self):
        root = self.small_tree.delete(3)
        with self.assertRaises(KeyError):
            root.get(3)
        self.assertEqual(root.sorted_value_list, ["one", "two", "four", "five"])

    def test_select(self):
        self.assertEqual(self.small_tree.select(3).key, 3)
        self.assertEqual(self.small_tree.select(2).key, 2)
        self.assertEqual(self.small_tree.select(1).key, 1)
        self.assertEqual(self.large_tree.select(5).key, 10)
        self.assertEqual(self.large_tree.select(9).key, 20)
        self.assertEqual(self.large_tree.select(7).key, 14)

    def test_select_after_delete(self):
        self.assertEqual(self.large_tree.select(9).key, 20)
        self.large_tree.delete(12)
        self.assertEqual(self.large_tree.select(8).key, 20)
        self.large_tree.delete(14)
        self.assertEqual(self.large_tree.select(7).key, 20)
        self.large_tree.delete(17)
        self.assertEqual(self.large_tree.select(6).key, 20)

    def test_rank(self):
        self.assertEqual(self.small_tree.get(3).rank, 3)
        self.assertEqual(self.small_tree.get(5).rank, 5)
        self.assertEqual(self.large_tree.get(5).rank, 4)
        self.assertEqual(self.large_tree.get(17).rank, 8)
