import unittest
from typing import List, Tuple


def sequence_alignment(x: str, y: str, gap_penalty: int, mismatch_penalty: int) -> int:
    lookup_table = get_lookup_table(x, y, gap_penalty, mismatch_penalty)
    return lookup_table[-1][-1]


def get_lookup_table(x: str, y: str, gap_penalty: int, mismatch_penalty: int) -> List[List[int]]:
    table_width = len(x) + 1
    table_height = len(y) + 1
    table = [[0] * table_height for _ in range(table_width)]

    for i in range(table_width):
        table[i][0] = gap_penalty * i

    for i in range(table_height):
        table[0][i] = gap_penalty * i

    for i in range(1, table_width):
        for j in range(1, table_height):
            no_gap = table[i-1][j-1] + (0 if x[i-1] == y[j-1] else mismatch_penalty)
            x_gap = table[i][j-1] + gap_penalty
            y_gap = table[i-1][j] + gap_penalty
            table[i][j] = min(no_gap, x_gap, y_gap)

    return table


def reconstruction(x: str, y: str, gap_penalty: int, mismatch_penalty: int, lookup_table: List[List[int]]) -> Tuple[str, str]:
    i = len(lookup_table) - 1
    j = len(lookup_table[0]) - 1
    x_chars = []
    y_chars = []
    while i > 0 and j > 0:
        curr = lookup_table[i][j]
        if curr == lookup_table[i-1][j-1] + (0 if x[i-1] == y[j-1] else mismatch_penalty):
            x_chars.append(x[i-1])
            y_chars.append(y[j-1])
            i -= 1
            j -= 1
        elif curr == lookup_table[i][j-1] + gap_penalty:
            x_chars.append("-")
            y_chars.append(y[j-1])
            j -= 1
        else:
            x_chars.append(y[j-1])
            y_chars.append("-")
            i -= 1

    if i > 0:
        x_chars.extend(reversed(x[:i]))
        y_chars.extend(["-"] * i)
    if j > 0:
        y_chars.extend(reversed(y[:j]))
        x_chars.extend(["-"] * j)

    return "".join(reversed(x_chars)), "".join(reversed(y_chars))


def get_penalty(x: str, y: str, gap_penalty: int, mismatch_penalty: int) -> int:
    penalty = 0
    for x_char, y_char in zip(x, y):
        if x_char == "-" or y_char == "-":
            penalty += gap_penalty
        elif x_char != y_char:
            penalty += mismatch_penalty

    return penalty


class TestSequenceAlignment(unittest.TestCase):
    def test_sequence_alignment_small(self):
        x = "CG"
        y = "CA"
        gap_penalty = 3
        mismatch_penalty = 5
        min_penalty = 5

        # check solution
        solution_penalty = sequence_alignment(x, y, gap_penalty, mismatch_penalty)
        self.assertEqual(min_penalty, solution_penalty)

        # check reconstruction
        lookup_table = get_lookup_table(x, y, gap_penalty, mismatch_penalty)
        optimal_x, optimal_y = reconstruction(x, y, gap_penalty, mismatch_penalty, lookup_table)
        self.assertEqual(min_penalty, get_penalty(optimal_x, optimal_y, gap_penalty, mismatch_penalty))


    def test_sequence_alignment_small_2(self):
        x = "CG"
        y = "CA"
        gap_penalty = 3
        mismatch_penalty = 7

        min_penalty = 6
        min_x = "CG-"
        min_y = "C-A"

        # check solution
        solution_penalty = sequence_alignment(x, y, gap_penalty, mismatch_penalty)
        self.assertEqual(min_penalty, solution_penalty)

        # check reconstruction
        lookup_table = get_lookup_table(x, y, gap_penalty, mismatch_penalty)
        optimal_x, optimal_y = reconstruction(x, y, gap_penalty, mismatch_penalty, lookup_table)
        self.assertEqual(min_penalty, get_penalty(optimal_x, optimal_y, gap_penalty, mismatch_penalty))

    def test_sequence_alignment_med(self):
        x = "AGGGCT"
        y = "AGGCA"
        gap_penalty = 3
        mismatch_penalty = 2
        min_penalty = 5

        # check solution
        solution_penalty = sequence_alignment(x, y, gap_penalty, mismatch_penalty)
        self.assertEqual(min_penalty, solution_penalty)

        # check reconstruction
        lookup_table = get_lookup_table(x, y, gap_penalty, mismatch_penalty)
        optimal_x, optimal_y = reconstruction(x, y, gap_penalty, mismatch_penalty, lookup_table)
        self.assertEqual(min_penalty, get_penalty(optimal_x, optimal_y, gap_penalty, mismatch_penalty))


    def test_sequence_alignment_med_2(self):
        x = "AACAGTTACC"
        y = "TAAGGTCA"
        gap_penalty = 2
        mismatch_penalty = 1
        min_penalty = 7

        # check solution
        solution_penalty = sequence_alignment(x, y, gap_penalty, mismatch_penalty)
        self.assertEqual(min_penalty, solution_penalty)

        # check reconstruction
        lookup_table = get_lookup_table(x, y, gap_penalty, mismatch_penalty)
        optimal_x, optimal_y = reconstruction(x, y, gap_penalty, mismatch_penalty, lookup_table)
        self.assertEqual(min_penalty, get_penalty(optimal_x, optimal_y, gap_penalty, mismatch_penalty))

    def test_sequence_alignment_med_3(self):
        x = "AGTACG"
        y = "ACATAG"
        gap_penalty = 1
        mismatch_penalty = 2
        min_penalty = 4

        # check solution
        solution_penalty = sequence_alignment(x, y, gap_penalty, mismatch_penalty)
        self.assertEqual(min_penalty, solution_penalty)

        # check reconstruction
        lookup_table = get_lookup_table(x, y, gap_penalty, mismatch_penalty)
        optimal_x, optimal_y = reconstruction(x, y, gap_penalty, mismatch_penalty, lookup_table)
        self.assertEqual(min_penalty, get_penalty(optimal_x, optimal_y, gap_penalty, mismatch_penalty))
