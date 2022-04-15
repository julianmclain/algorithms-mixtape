from typing import TypeVar, Generic, List, Optional

T = TypeVar("T")


class BinarySearchTree(Generic[T]):
    """
    Binary Search Tree implementation with no guarantees about balance. Duplicate
    keys are allowed.
    """
    def __init__(
        self,
        key: int,
        value: T,
        left: Optional["BinarySearchTree[T]"] = None,
        right: Optional["BinarySearchTree[T]"] = None,
        parent: Optional["BinarySearchTree[T]"] = None,
        size: int = 1
    ):
        self.key = key
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent
        self.size = size

    @property
    def height(self):
        """
        Get the 1-based height of the tree
        """
        return 1 # TODO

    @property
    def is_root(self) -> "BinarySearchTree[T]":
        """
        True if node is the root of the tree
        """
        return self.parent is None

    @property
    def root(self):
        """
        Get the root of the tree
        """
        if self.parent:
            return self.parent.root
        else:
            return self

    @property
    def is_root(self) -> bool:
        """
        True if node is the root
        """
        return not self.parent

    @property
    def is_left_child(self) -> bool:
        """
        True if node is left child of parent
        """
        return self.parent and self.parent.left is self

    @property
    def is_right_child(self) -> bool:
        """
        True if node is right child of parent
        """
        return self.parent and self.parent.right is self

    @property
    def min(self) -> "BinarySearchTree[T]":
        """
        Get the node with the smallest key
        """
        if self.left is not None:
            return self.left.min
        else:
            return self

    @property
    def max(self) -> "BinarySearchTree[T]":
        """
        Get the node with the largest key
        """
        if self.right is not None:
            return self.right.max

        return self

    @property
    def predecessor(self) -> "BinarySearchTree[T]":
        """
        Get the node with the next smallest key

        :raises: ValueError when tree size 1 or the node contains the minimum key
        """
        if self.left is None and self.right is None and self.parent is None:
            raise ValueError("Tree size is 1")

        if self.left is not None:
            return self.left.max

        def find_predecessor_in_ancestors(parent, child):
            if parent is None:
                raise ValueError("The node has no predecessor")
            elif parent.right is child:
                return parent
            else:
                return find_predecessor_in_ancestors(parent.parent, parent)

        return find_predecessor_in_ancestors(self.parent, self)

    @property
    def rank(self) -> int:
        """
        Get the rank of the key associated with this node (e.g. position in sorted list)
        """
        if self.is_root:
            left_size = self.left.size if self.left else 0
            return left_size + 1
        elif self.is_left_child:
            right_size = self.right.size if self.right else 0
            return self.parent.rank - right_size - 1
        else:
            left_size = self.left.size if self.left else 0
            return self.parent.rank + left_size + 1

    @property
    def sorted_value_list(self) -> List[T]:
        """
        Get the tree values as a list sorted by key
        """
        out = []
        if self.left is not None:
            out.extend(self.left.sorted_value_list)
        out.append(self.value)
        if self.right is not None:
            out.extend(self.right.sorted_value_list)
        return out

    def get(self, key: int) -> "BinarySearchTree[T]":
        """
        Return the node with a given key

        :raises: KeyError if key not in tree
        """
        if key == self.key:
            return self
        elif key < self.key and self.left is not None:
            return self.left.get(key)
        elif key > self.key and self.right is not None:
            return self.right.get(key)
        else:
            raise KeyError("key not in tree")

    def insert(self, key: int, value: T) -> None:
        """
        Add a node to the tree
        """
        self.size += 1
        if key == self.key:
            # Add duplicate key as root node in left tree
            left_child = self.left
            inserted = BinarySearchTree(key, value, left_child, None, self, self.size)
            left_child.parent = inserted
            self.left = inserted
        elif key < self.key:
            if self.left is None:
                self.left = BinarySearchTree(key, value, None, None, self)
            else:
                self.left.insert(key, value)
        else:
            if self.right is None:
                self.right = BinarySearchTree(key, value, None, None, self)
            else:
                self.right.insert(key, value)

    def delete(self, key: int) -> "BinarySearchTree[T]":
        """
        Delete a node with given key

        :returns: the root of the modified tree
        :raises: KeyError if key not in tree
        """
        to_delete = self.get(key)

        if to_delete.left and to_delete.right:
            predecessor = to_delete.predecessor

            to_delete_key = to_delete.key
            to_delete_value = to_delete.value
            to_delete._assign(predecessor.key, predecessor.value)
            predecessor._assign(to_delete_key, to_delete_value)
            predecessor._splice()
        else:
            to_delete._splice()

        return self.root

    def _assign(self, key, value) -> None:
        """
        Assign a key, value pair to a node. Note: usage doesn't ensure that the search tree property is maintained.
        """
        self.key = key
        self.value = value

    def _splice(self) -> None:
        """
        Remove a node by connecting its parent to its left or right child. Only valid for nodes with 1 or no children
        """
        if self.left and self.right:
            raise ValueError("Cannot splice node with 2 children (only one child can replace it)")

        child = self.left if self.left else self.right
        if child:
            child.parent = self.parent

        if self.is_left_child:
            self.parent.left = child
        elif self.is_right_child:
            self.parent.right = child

    def select(self, i) -> "BinarySearchTree[T]":
        """
        Return the tree node with the ith-smallest key

        :raises: ValueError if tree doesn't contain at least i items
        """
        j = self.left.size if self.left else 0
        if i == j + 1:
            return self
        elif i < j + 1:
            return self.left.select(i)
        else:
            return self.right.select(i-j-1)

    def __repr__(self):
        return f"BinarySearchTree(key={self.key}, value={self.value}, left={self.left.key if self.left else None}, " + \
               f"right={self.right.key if self.right else None} parent = {self.parent if self.parent else None})"


def iterative_preorder_traversal(root) -> list:
    if not root:
        return []

    vals = []
    stack = [root]
    while stack:
        node = stack.pop()
        vals.append(node.value)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

    return vals


def recursive_preorder_traversal(root) -> list:
    def _traverse(root, acc):
        if not root:
            return []

        acc.append(root.value)
        _traverse(root.left, acc)
        _traverse(root.right, acc)
        return acc

    return _traverse(root, [])


def concise_preorder_traversal(root) -> list:
    if not root:
        return []

    return (
        [root.value]
        + concise_preorder_traversal(root.left)
        + concise_preorder_traversal(root.right)
    )


def recursive_inorder_traversal(root) -> list:
    def _traverse(root, acc):
        if not root:
            return []

        _traverse(root.left, acc)
        acc.append(root.value)
        _traverse(root.right, acc)
        return acc

    return _traverse(root, [])


def recursive_postorder_traversal(root) -> list:
    if not root:
        return []

    vals = []
    vals.extend(recursive_inorder_traversal(root.left))
    vals.extend(recursive_inorder_traversal(root.right))
    vals.append(root.value)

    return vals


def count_unival(root) -> int:
    def is_unival(root: BinarySearchTree, par_val) -> bool:
        if not root:
            return True

        return all(
            [
                root.value == par_val,
                is_unival(root.left, par_val),
                is_unival(root.right, par_val),
            ]
        )

    if not root:
        return 0

    if is_unival(root.left, root.value) and is_unival(root.right, root.value):
        return 1 + count_unival(root.left) + count_unival(root.right)
    else:
        return count_unival(root.left) + count_unival(root.right)
