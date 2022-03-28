import heapq
from abc import ABC, abstractmethod
from typing import Tuple, Hashable, TypeVar, Generic


REMOVED = "<removed-task>"  # placeholder for a removed task

K = TypeVar("K")
V = TypeVar("V", bound=Hashable)

class Heap(ABC, Generic[K, V]):
    """
    Simple heap interface. It doesn't allow duplicate items.

    At this interface level V shouldn't need to be Hashable. However, both implementations require it
    and I'm being lazy. To support item deletion, both implementations use items as dict keys. Thus
    unhashable types like lists and dicts can't be used. See: https://docs.python.org/3/glossary.html#term-hashable
    """

    @abstractmethod
    def insert(self, key: K, item: V) -> None:
        """
        Add a new item or update the key of an existing item
        """
        pass

    @abstractmethod
    def extract_min(self) -> Tuple[K, V]:
        """
        Remove the item with the smallest key. If there are multiple items with the smallest key, no
        guarantee is given about which item will be removed.

        :raises: IndexError if heap is empty
        :return: key, item
        """
        pass

    @abstractmethod
    def delete(self, item: V) -> None:
        """
        Remove an item

        :raises: KeyError if item not in heap
        """
        pass

    @abstractmethod
    def is_empty(self) -> bool:
        pass


class HeapEntry:
    def __init__(self, item: V):
        self.item = item

    def __lt__(self, other: V) -> bool:
        """
        Entries need to be comparable when using heapq for the heap algorithm. If there are duplicate keys,
        it compares the entries in order to determine sort order.
        """
        return True


class StandardLibHeap(Heap):
    """
    Heap implementation based on the heapq algorithm provided by the standard lib
    https://docs.python.org/3/library/heapq.html
    """

    def __init__(self):
        self.h = []
        self.entry_finder = {}

    def insert(self, key: K, item: V) -> None:
        """
        :raises TypeError if item unhashable
        """
        if item in self.entry_finder:
            self.delete(item)

        entry = HeapEntry(item)
        self.entry_finder[item] = entry
        heapq.heappush(self.h, (key, entry))

    def extract_min(self) -> Tuple[K, V]:
        key, entry = heapq.heappop(self.h)
        if entry.item == REMOVED:
            return self.extract_min()
        else:
            del self.entry_finder[entry.item]
            return key, entry.item

    def delete(self, item: V) -> None:
        entry = self.entry_finder[item]
        entry.item = REMOVED

    def is_empty(self) -> bool:
        for key, entry in self.h:
            if entry.item is not REMOVED:
                return False
        return True


class MyHeap(Heap):
    """
    My heap implementation
    """

    def __init__(self):
        self.h = []
        self.entry_finder = {}

    def insert(self, key: K, item: V) -> None:
        """
        :raises TypeError if item unhashable
        """
        if item in self.entry_finder:
            self.delete(item)

        entry = HeapEntry(item)
        self.entry_finder[item] = entry
        self.h.append((key, entry))
        self._bubble_up(len(self.h)-1)

    def extract_min(self) -> Tuple[K, V]:
        min_key, min_entry = self.h[0]
        last_entry = self.h.pop()

        if len(self.h) >= 1:
            self.h[0] = last_entry
            self._bubble_down(0, len(self.h)-1)

        if min_entry.item == REMOVED:
            return self.extract_min()
        else:
            del self.entry_finder[min_entry.item]
            return min_key, min_entry.item

    def delete(self, item: V) -> None:
        entry = self.entry_finder[item]
        entry.item = REMOVED

    def is_empty(self) -> bool:
        for key, entry in self.h:
            if entry.item is not REMOVED:
                return False
        return True

    def _bubble_up(self, index: int):
        """
        Ensure heap property by recursively swapping parent-child relationships in which the
        parent is larger than the child.
        """
        if index == 0:
            return

        parent_index = self.calculate_parent_index(index)
        parent_key, parent_entry = self.h[parent_index]
        child_key, child_entry = self.h[index]

        if parent_key > child_key:
            # swap parent with child and recurse
            self.h[parent_index] = (child_key, child_entry)
            self.h[index] = (parent_key, parent_entry)
            self._bubble_up(parent_index)

    @staticmethod
    def calculate_parent_index(index: int) -> int:
        if index <= 0:
            raise ValueError
        elif index % 2 == 0:
            return index // 2 - 1
        else:
            return index // 2

    def _bubble_down(self, curr_index, stop_index):
        """
        Ensure heap property by recursively swapping parent with smallest child if the parent is
        larger than the smallest child.
        """
        l_child_index = self.calculate_l_child_index(curr_index)
        r_child_index = self.calculate_r_child_index(curr_index)
        if l_child_index > stop_index or r_child_index > stop_index:
            return

        l_child_key, l_child_entry = self.h[l_child_index]
        r_child_key, r_child_entry = self.h[r_child_index]

        if l_child_key < r_child_key:
            smallest_child_key = l_child_key
            smallest_child_index = l_child_index
            smallest_child_entry = l_child_entry
        else:
            smallest_child_key = r_child_key
            smallest_child_index = r_child_index
            smallest_child_entry = r_child_entry

        curr_key, curr_entry = self.h[curr_index]
        if curr_key > smallest_child_key:
            # swap parent with smallest child and recurse
            self.h[smallest_child_index] = (curr_key, curr_entry)
            self.h[curr_index] = (smallest_child_key, smallest_child_entry)
            self._bubble_down(smallest_child_index, stop_index)

    @staticmethod
    def calculate_l_child_index(index: int) -> int:
        return 2 * index + 1

    @staticmethod
    def calculate_r_child_index(index: int) -> int:
        return 2 * index + 2
