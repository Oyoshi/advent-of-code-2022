from days_solvers import DaySolver
from utils import sum_iterable


class Day04Solver(DaySolver):
    def __init__(self):
        self.day = "04"

    def load_input_impl(self, file):
        return [
            [tuple(map(int, coords.split("-"))) for coords in line.rstrip().split(",")]
            for line in file
        ]

    def solve_part_1(self):
        return sum_iterable(
            map(lambda r: self.is_range_fully_overlap(r[0], r[1]), self.input_data)
        )

    def is_range_fully_overlap(self, range1, range2):
        s1, e1, s2, e2 = range1[0], range1[1], range2[0], range2[1]
        return int((s1 >= s2 and e1 <= e2) or (s2 >= s1 and e2 <= e1))

    def solve_part_2(self):
        pass
