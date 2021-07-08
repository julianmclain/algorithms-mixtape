class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def iterative_preorder_traversal(root) -> list:
    if not root:
        return []

    vals = []
    stack = [root]
    while stack:
        node = stack.pop()
        vals.append(node.val)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

    return vals


def recursive_preorder_traversal(root) -> list:
    def _traverse(root, acc):
        if not root:
            return []

        acc.append(root.val)
        _traverse(root.left, acc)
        _traverse(root.right, acc)
        return acc

    return _traverse(root, [])


def concise_preorder_traversal(root) -> list:
    if not root:
        return []

    return (
        [root.val]
        + concise_preorder_traversal(root.left)
        + concise_preorder_traversal(root.right)
    )


def recursive_inorder_traversal(root) -> list:
    def _traverse(root, acc):
        if not root:
            return []

        _traverse(root.left, acc)
        acc.append(root.val)
        _traverse(root.right, acc)
        return acc

    return _traverse(root, [])


def recursive_postorder_traversal(root) -> list:
    if not root:
        return []

    vals = []
    vals.extend(recursive_inorder_traversal(root.left))
    vals.extend(recursive_inorder_traversal(root.right))
    vals.append(root.val)

    return vals


def count_unival(root) -> int:
    def is_unival(root: TreeNode, par_val) -> bool:
        if not root:
            return True

        return all(
            [
                root.val == par_val,
                is_unival(root.left, par_val),
                is_unival(root.right, par_val),
            ]
        )

    if not root:
        return 0

    if is_unival(root.left, root.val) and is_unival(root.right, root.val):
        return 1 + count_unival(root.left) + count_unival(root.right)
    else:
        return count_unival(root.left) + count_unival(root.right)


root = TreeNode(
    5, TreeNode(1, TreeNode(5), TreeNode(5)), TreeNode(5, None, TreeNode(5))
)
print(count_unival(root))
