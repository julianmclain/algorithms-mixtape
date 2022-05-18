from typing import Dict, Tuple, List

from algorithms_mixtape.heaps.heap import StandardLibHeap


class TreeNode:
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self):
        return str(self.value)


def make_huffman_code_tree_recursive(weights: Dict[int, int]) -> TreeNode:
    """ Construct a tree with minimum average leaf depth representing the prefix-free binary
    code with minimum encoding length """
    forest = [(weight, TreeNode(value=key)) for key, weight in weights.items()]
    _helper(forest)
    return forest[0][1]


def _helper(forest: List[Tuple[int, TreeNode]]) -> None:
    if len(forest) <= 1:
        return

    min_weight = _find_and_remove_min(forest)
    next_smallest = _find_and_remove_min(forest)
    forest.append((min_weight[0] + next_smallest[0], TreeNode(left=min_weight[1], right=next_smallest[1])))

    _helper(forest)


def _find_and_remove_min(forest: List[Tuple[int, TreeNode]]) -> Tuple[int, TreeNode]:
    if len(forest) < 1:
        raise ValueError("Cannot find min of empty list")

    min_index = 0
    for index, (weight, tree) in enumerate(forest):
        if weight < forest[min_index][0]:
            min_index = index

    return forest.pop(min_index)


def make_huffman_code_tree(weights: Dict[int, int]) -> TreeNode:
    """ Construct a tree with minimum average leaf depth representing the prefix-free binary
    code with minimum encoding length """
    heap = StandardLibHeap()
    for symbol, weight in weights.items():
        heap.insert(weight, TreeNode(value=symbol))

    while not heap.is_empty():
        a, min_tree = heap.extract_min()
        if heap.is_empty():
            return min_tree

        b, next_min_tree = heap.extract_min()
        heap.insert(a+b, TreeNode(left=min_tree, right=next_min_tree))



