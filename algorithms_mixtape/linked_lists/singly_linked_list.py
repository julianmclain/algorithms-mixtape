class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class LinkedList:
    def __init__(self):
        """
        self.head is a sentinel node. It will never be None,
        but its value will never be used. It's there to save
        us from dealing with head=None edge cases.
        """
        self.head = Node(0)
        self.size = 0

    def get(self, index: int) -> int:
        if index is None or index < 0:
            return -1

        i, curr = 0, self.head
        while curr and i < index + 1:
            curr = curr.next
            i += 1

        if curr:
            return curr.val

        return -1

    def add_at_head(self, val: int) -> None:
        self.add_at_index(0, val)

    def add_at_tail(self, val: int) -> None:
        self.add_at_index(self.size, val)

    def add_at_index(self, index: int, val: int) -> None:
        if index is None or index < 0 or index > self.size:
            return

        i, prev = 0, self.head
        while prev and i < index:
            prev = prev.next
            i += 1

        if not prev:
            return

        new_node = Node(val)
        new_node.next = prev.next
        prev.next = new_node
        self.size += 1

    def delete_at_index(self, index: int) -> None:
        if index >= self.size or index < 0:
            return

        i, prev = 0, self.head
        while prev and i < index:
            prev = prev.next
            i += 1

        prev.next = prev.next.next
        self.size -= 1
