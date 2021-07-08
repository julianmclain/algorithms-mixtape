import unittest
from typing import List


"""Self-referential data

When information in the problem domain is of an arbitrary
size, you need a self-referential (or mutually referential)
data definition.

For example:
- A List[str] is either [] or [str] + List[str] 

Template for functions operating on self-referential data:
```
def fn_for_data(data):
    if not data:                                      # base case
        return ???
    else:                                             # recursive case
        return data[0] ??? fn_for_data(data[1:])
```
"""


"""Operating on lists of numbers"""


def sum(nums: list) -> int:
    if not nums:
        return 0

    return nums[0] + sum(nums[1:])


def tail_rec_sum(nums: list) -> int:
    def loop(nums: list, rsf: int) -> int:
        if not nums:
            return rsf

        return loop(nums[1:], nums[0] + rsf)

    return loop(nums, 0)


def max(nums: list) -> int:
    if not nums:
        return None

    first = nums[0]
    rest = max(nums[1:])
    return first if not rest or first > rest else rest


def find_homes_in_distance(homes: List[dict], dist) -> List[dict]:
    def find(homes, dist, rsf):
        if not homes:
            return rsf

        if homes[0]["dist"] <= dist:
            return find(homes[1:], dist, rsf + [homes[0]])
        else:
            return find(homes[1:], dist, rsf)

    return find(homes, dist, [])


"""Operating on strings"""


def reverse_string(s: str) -> str:
    if not s:
        return ""

    return reverse_string(s[1:]) + s[0]


def replace(s: str, char: str, replacement: str) -> str:
    if not s:
        return ""

    if s[0] == char:
        return replacement + replace(s[1:], char, replacement)
    else:
        return s[0] + replace(s[1:], char, replacement)


class TestSelfReference(unittest.TestCase):
    def test_list_operations(self):
        test_nums = [[], [1], [999, 1], [1, 2, 3]]
        print("sums", list(map(sum, test_nums)))
        print("tail rec sums", list(map(tail_rec_sum, test_nums)))
        print("maxes", list(map(max, test_nums)))

        test_homes = [
            {"name": "sea side mansion", "dist": 1,},
            {"name": "mountain cabin", "dist": 99},
            {"name": "abandoned shack", "dist": 10},
        ]
        print("homes in dist", find_homes_in_distance(test_homes, 10))

    def test_string_operations(self):
        test_strings = ["", "h", "hi", "hiccup", "hi my name is hiccup"]
        print("reversed", list(map(reverse_string, test_strings)))
        print("replaced", replace(test_strings[-1], " ", "-"))


if __name__ == "__main__":
    unittest.main()
