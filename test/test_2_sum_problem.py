import unittest
import bisect
from helpers import FIXTURE_DIRECTORY_PATH


def read_input():
    p = FIXTURE_DIRECTORY_PATH / "1_million_random_ints.txt"
    nums = []
    with open(p, 'r') as f:
        for line in f:
            nums.append(int(line.strip()))
    return nums


class Test2SumProblem(unittest.TestCase):
    def test_2_sum_problem(self):
        nums = read_input()
        nums.sort()
        targets = set()
        for x in nums:
            low = bisect.bisect_left(nums, -10_000 - x)
            high = bisect.bisect_right(nums, 10_000 - x)
            for y in nums[low:high]:
                if x != y:
                    t = x+y
                    targets.add(t)
                    # print(f"found match, x={x}, y={y}, t={x+y}")
        self.assertEqual(427, len(targets))
