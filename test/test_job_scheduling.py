import unittest
from typing import List, Tuple
from .helpers import FIXTURE_DIRECTORY_PATH
from algorithms_mixtape.scheduling.job_scheduling import greedy_diff, greedy_ratio


def read_jobs() -> List[Tuple[int, int]]:
    jobs = []
    with open(FIXTURE_DIRECTORY_PATH / "jobs.txt", "r") as f:
        f.readline()  # first line is a header
        for line in f:
            stripped_line = line.strip()
            parts = stripped_line.split(" ", 1)
            weight = int(parts[0])
            length = int(parts[1])
            jobs.append((weight, length))

    return jobs


class TestJobScheduling(unittest.TestCase):
    def test_greedy_diff(self):
        """
        Your task in this problem is to run the greedy algorithm that schedules jobs in decreasing order
        of the difference (weight - length).  Recall from lecture that this algorithm is not always optimal.
        IMPORTANT: if two jobs have equal difference (weight - length), you should schedule the job with
        higher weight first.
        """
        self.assertEqual(69119377652, greedy_diff(read_jobs()))

    def test_greedy_ratio(self):
        """
        Your task now is to run the greedy algorithm that schedules jobs (optimally) in decreasing order
        of the ratio (weight/length).  In this algorithm, it does not matter how you break ties.
        """
        self.assertEqual(67311454237, greedy_ratio(read_jobs()))
