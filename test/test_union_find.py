import unittest
from algorithms_mixtape.union_finds.union_find import IntUnionFind, Entry


class TestIntUnionFind(unittest.TestCase):
    def test_find(self):
        uf = IntUnionFind([1, 2, 3, 4, 5, 6])
        uf.arr[1] = Entry(4, 0)
        uf.arr[2] = Entry(1, 0)
        uf.arr[3] = Entry(1, 0)
        uf.arr[4] = Entry(4, 0)
        uf.arr[5] = Entry(6, 0)
        uf.arr[6] = Entry(6, 0)

        self.assertEqual(4, uf.find(1))
        self.assertEqual(4, uf.find(2))
        self.assertEqual(4, uf.find(3))
        self.assertEqual(4, uf.find(4))
        self.assertEqual(6, uf.find(5))
        self.assertEqual(6, uf.find(6))

    def test_union(self):
        uf = IntUnionFind([1, 2, 3, 4, 5, 6])
        uf.arr[1] = Entry(4, 4)
        uf.arr[2] = Entry(1, 4)
        uf.arr[3] = Entry(1, 4)
        uf.arr[4] = Entry(4, 4)
        uf.arr[5] = Entry(6, 2)
        uf.arr[6] = Entry(6, 2)

        uf.union(1, 5)
        self.assertEqual(4, uf.find(1))
        self.assertEqual(4, uf.find(2))
        self.assertEqual(4, uf.find(3))
        self.assertEqual(4, uf.find(4))
        self.assertEqual(4, uf.find(5))
        self.assertEqual(4, uf.find(6))


class TestGeneralPurposeUnionFind(unittest.TestCase):
    def test_find(self):
        pass

    def test_union(self):
        pass
