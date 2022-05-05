class CircularArrayQueue:
    def __init__(self, k: int):
        self.head_index = 0
        self.count = 0
        self.capacity = k
        self.arr = [0] * k

    def enqueue(self, value: int) -> bool:
        if self.is_full():
            return False
        self.arr[(self.head_index + self.count) % self.capacity] = value
        self.count += 1
        return True

    def dequeue(self) -> bool:
        if self.is_empty():
            return False
        self.head_index = (self.head_index + 1) % self.capacity
        self.count -= 1
        return True

    def front(self) -> int:
        if self.is_empty():
            return -1
        return self.arr[self.head_index]

    def rear(self) -> int:
        if self.is_empty():
            return -1

        return self.arr[(self.head_index + self.count - 1) % self.capacity]

    def is_empty(self) -> bool:
        return self.count == 0

    def is_full(self) -> bool:
        return self.count == self.capacity


class CircularLinkedListQueue:
    class Node:
        def __init__(self, val, next=None):
            self.val = val
            self.next = next

    def __init__(self, k: int):
        self.head = None
        self.tail = None
        self.capacity = k
        self.count = 0

    def enqueue(self, value: int) -> bool:
        if self.is_full():
            return False

        if self.count == 0:
            self.head = self.Node(value)
            self.tail = self.head
        else:
            new_node = self.Node(value)
            self.tail.next = new_node
            self.tail = new_node
        self.count += 1
        return True

    def dequeue(self) -> bool:
        if self.is_empty():
            return False
        self.head = self.head.next
        self.count -= 1
        return True

    def front(self) -> int:
        if self.is_empty():
            return -1
        return self.head.val

    def rear(self) -> int:
        if self.is_empty():
            return -1

        return self.tail.val

    def is_empty(self) -> bool:
        return self.count == 0

    def is_full(self) -> bool:
        return self.count == self.capacity
