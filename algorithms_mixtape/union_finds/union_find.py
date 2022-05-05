from typing import List
from collections import namedtuple
from abc import ABC, abstractmethod


Entry = namedtuple('Entry', ['parent', 'size'])


class UnionFind(ABC):
    @abstractmethod
    def find(self, x: object) -> object:
        pass

    @abstractmethod
    def union(self, x: object, y: object):
        pass


class IntUnionFind(UnionFind):
    """
    UnionFind limited to int values - this is the implementation described in Algorithms
    Illuminated
    """
    def __init__(self, items: List[int]):
        """
        Note: assumes items is a 1-based range starting at 1
        """
        self.arr = [Entry(0, 0)] + [Entry(i, 1) for i in items]

    def find(self, x: int) -> int:
        parent = self.arr[x].parent
        while parent != self.arr[parent].parent:
            parent = self.arr[parent].parent

        return parent

    def union(self, x: int, y: int) -> None:
        """
        union-by-size: the root of the smaller tree is merged with the larger tree
        """
        x_root, y_root = self.find(x), self.find(y)
        smallest_root, largest_root = sorted([x_root, y_root], key=lambda root: self.arr[root].size)
        merged_size = self.arr[smallest_root].size + self.arr[largest_root].size
        self.arr[smallest_root] = Entry(largest_root, merged_size)
        self.arr[largest_root] = Entry(largest_root, merged_size)


class GeneralPurposeUnionFind(UnionFind):
    """
    UnionFind data structure for any object type
    """
    def __init__(self, objects: List[object]):
        self.leaders = {o: o for o in objects}
        self.subsets = {o: {o} for o in objects}

    def find(self, x: object) -> object:
        return self.leaders[x]

    def union(self, x: object, y: object) -> None:
        x_leader, y_leader = self.leaders[x], self.leaders[y]

        if x_leader == y_leader:
            return

        large_leader, small_leader = sorted([x_leader, y_leader], key=lambda leader: len(self.subsets[leader]))

        for o in self.subsets[small_leader]:
            self.leaders[o] = large_leader

        self.subsets[large_leader] = self.subsets[large_leader] | self.subsets[small_leader]
        del self.subsets[small_leader]
