import unittest
from algorithms_mixtape.linked_lists.singly_linked_list import Node


def reverse_list(node: object) -> object:
    prev = None
    curr = node

    while curr:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp

    return prev


def recursive_reverse_inplace(node: object) -> object:
    def loop(node, prev):
        if not node:
            return prev

        temp_next = node.next
        node.next = prev
        return loop(temp_next, node)

    return loop(node, None)


def recursive_reverse(node: object) -> object:
    def loop(node, prev):
        if not node:
            return prev

        return loop(node.next, Node(node.val, next=prev))

    return loop(node, None)


def has_cycle(node: object) -> bool:
    """Detect if the list has a cycle.

    Floyd's Tortoise and Hare algorithm: https://en.wikipedia.org/wiki/Cycle_detection#Floyd's_Tortoise_and_Hare

    Time complexity:  0(n)
    Space complexity: 0(1)
    """
    if node is None:
        return False
    slow = node
    fast = node

    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            return True

    return False


def remove_nth_from_end(self, head: object, n: int) -> object:
    """Remove the nth element from the end of the list.

    Assume n is a valid 1-based integer. Using a sentinel node eliminates
    edge cases when `head` is None or the element to be removed is the first
    element.
    """
    sentinel = Node(0)
    sentinel.next = head
    slow = sentinel
    fast = sentinel

    for _ in range(n):
        fast = fast.next

    while fast.next:
        slow = slow.next
        fast = fast.next

    slow.next = slow.next.next
    return sentinel.next


class TestLinkedListOperations(unittest.TestCase):
    def test_recursive_reverse_inplace(self):
        ll = Node(1, Node(2, Node(3, Node(4))))
        reversed_ll = recursive_reverse_inplace(ll)

        counter = 4
        while reversed_ll:
            assert reversed_ll.val == counter
            reversed_ll = reversed_ll.next
            counter -= 1

    def test_recursive_reverse(self):
        ll = Node(1, Node(2, Node(3, Node(4))))
        reversed_ll = recursive_reverse(ll)

        counter = 4
        while reversed_ll:
            assert reversed_ll.val == counter
            reversed_ll = reversed_ll.next
            counter -= 1


if __name__ == "__main__":
    unittest.main()
