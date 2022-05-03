from typing import List, Tuple
from operator import itemgetter


def greedy_diff(jobs: List[Tuple[int, int]]):
    # Sort jobs descending by diff then weight. Takes advantage of Python sort stability
    # https://docs.python.org/3.9/howto/sorting.html#sort-stability-and-complex-sorts
    jobs.sort(key=itemgetter(0), reverse=True)
    jobs.sort(key=lambda job: job[0] - job[1], reverse=True)
    sum_weighted_times = _calculate_sum_weighted_completion_time(jobs)
    return sum_weighted_times


def _calculate_sum_weighted_completion_time(jobs: List[Tuple[int, int]]):
    time = 0
    sum_weighted_times = 0
    for weight, length in jobs:
        time += length
        sum_weighted_times += weight * time
    return sum_weighted_times


def greedy_ratio(jobs: List[Tuple[int, int]]):
    jobs.sort(key=lambda job: job[0] / job[1], reverse=True)
    sum_weighted_times = _calculate_sum_weighted_completion_time(jobs)
    return sum_weighted_times
