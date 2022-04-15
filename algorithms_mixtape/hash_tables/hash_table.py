from typing import Hashable, TypeVar, Generic


class HashSet:
    """
    A sample implementation of a HashSet. For this first pass I used an array
    for each 'bucket'. In the future I could get fancier and write another
    implementation using a linked list or a BST.
    """

    def __init__(self):
        self.max_buckets = (
            769  # choosing a prime number reduces the likelihood of collisions
        )
        self.buckets = [[] for i in range(self.max_buckets)]

    def hash_key(self, key: int) -> int:
        return key % self.max_buckets

    def add(self, key: int) -> None:
        if key is None:
            return

        bucket_index = self.hash_key(key)
        bucket = self.buckets[bucket_index]
        if key not in bucket:
            bucket.append(key)

    def remove(self, key: int) -> None:
        if key is None:
            return

        bucket_index = self.hash_key(key)
        bucket = self.buckets[bucket_index]
        if key in bucket:
            bucket.remove(key)

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        if key is None:
            return

        bucket_index = self.hash_key(key)
        return key in self.buckets[bucket_index]


K = TypeVar("K", bound=Hashable)
V = TypeVar("V")


class HashTable(Generic[K, V]):
    """
    Simple implementation of a hash table

    // TODO hash function only works with ints for now
    // TODO implement resize
    """
    class Node(Generic[K, V]):
        def __init__(self, key: K, value: V, next_node: "Node[K, V]" = None):
            self.key = key
            self.value = value
            self.next_node = next_node

    DEFAULT_NUM_BUCKETS = 769  # using a prime number reduces the likelihood of collisions

    def __init__(self):
        self.num_buckets = self.DEFAULT_NUM_BUCKETS
        self.arr = [None] * self.num_buckets
        self._size = 0

    @property
    def size(self):
        return self._size

    def put(self, key: K, value: V) -> None:
        if key is None:
            return

        self._size += 1
        i = self._hash(key)
        node = self.arr[i]

        if node is None:
            self.arr[i] = self.Node(key, value)
        else:
            while node.next_node is not None:
                node = node.next_node
            node.next_node = self.Node(key, value)

    def _hash(self, key: K) -> int:
        return key % self.num_buckets

    def get(self, key: K) -> V:
        if key is None:
            return

        i = self._hash(key)
        node = self.arr[i]

        while node is not None:
            if node.key == key:
                return node.value
            node = node.next_node

        raise KeyError(key)

    def delete(self, key: K) -> None:
        # TODO
        pass
