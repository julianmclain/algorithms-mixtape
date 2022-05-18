import unittest
from collections import deque

from algorithms_mixtape.huffman_codes.huffman_codes import TreeNode, make_huffman_code_tree, make_huffman_code_tree_recursive
from .helpers import FIXTURE_DIRECTORY_PATH


def read_fixture(filename):
    with open(FIXTURE_DIRECTORY_PATH / filename, "r") as f:
        f.readline()  # first line is a header
        frequencies = {}
        for i, line in enumerate(f):
            frequencies[i] = int(line.strip())

        return frequencies


def get_codeword_min_length(hc_tree: TreeNode) -> int:
    q = deque([(0, hc_tree)])
    while q:
        length, node = q.pop()
        if node.value:
            return length
        else:
            if node.left:
                q.appendleft((length+1, node.left))
            if node.right:
                q.appendleft((length+1, node.right))


def get_codeword_max_length(hc_tree: TreeNode) -> int:
    max_length = 0
    q = deque([(0, hc_tree)])
    while q:
        length, node = q.pop()
        if node.value and length > max_length:
            max_length = length
        else:
            if node.left:
                q.appendleft((length+1, node.left))
            if node.right:
                q.appendleft((length+1, node.right))

    return max_length


class TestHuffmanCodes(unittest.TestCase):
    def test_make_huffman_code_tree_recursive(self):
        small_tree = make_huffman_code_tree_recursive(read_fixture("huffman-char-set-small.txt"))
        self.assertEqual(2, get_codeword_min_length(small_tree))
        self.assertEqual(5, get_codeword_max_length(small_tree))

        medium_tree = make_huffman_code_tree_recursive(read_fixture("huffman-char-set-medium.txt"))
        self.assertEqual(3, get_codeword_min_length(medium_tree))
        self.assertEqual(6, get_codeword_max_length(medium_tree))

    def test_make_huffman_code_tree(self):
        large_tree = make_huffman_code_tree(read_fixture("huffman-char-set-large.txt"))
        self.assertEqual(9, get_codeword_min_length(large_tree))
        self.assertEqual(19, get_codeword_max_length(large_tree))
