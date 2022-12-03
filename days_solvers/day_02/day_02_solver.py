from days_solvers import DaySolver
from utils import sum_iterable


class Day02Solver(DaySolver):
    def __init__(self):
        self.day = "02"

    def load_input_impl(self, file):
        return [line.split() for line in file]

    def solve_part_1(self):
        return sum_iterable(
            [self.score(list_item, 1) for list_item in self.input_data],
        )

    def solve_part_2(self):
        return sum_iterable(
            [self.score(list_item, 2) for list_item in self.input_data],
        )

    def score(self, item, part):
        lhs, rhs = item[0], item[1]
        return self.score_choose(rhs, part) + self.score_round(lhs, rhs, part)

    def score_round(self, lhs, rhs, part):
        if part == 1:
            if (
                (lhs == "A" and rhs == "X")
                or (lhs == "B" and rhs == "Y")
                or (lhs == "C" and rhs == "Z")
            ):
                return 3
            if (
                (lhs == "A" and rhs == "Y")
                or (lhs == "B" and rhs == "Z")
                or (lhs == "C" and rhs == "X")
            ):
                return 6
            return 0
        else:
            if (
                (lhs == "A" and rhs == "X")
                or (lhs == "B" and rhs == "Z")
                or (lhs == "C" and rhs == "Y")
            ):
                return 3
            if (
                (lhs == "A" and rhs == "Z")
                or (lhs == "B" and rhs == "Y")
                or (lhs == "C" and rhs == "X")
            ):
                return 2
            if (
                (lhs == "A" and rhs == "Y")
                or (lhs == "B" and rhs == "X")
                or (lhs == "C" and rhs == "Z")
            ):
                return 1

    def score_choose(self, choose, part):
        if part == 1:
            return 1 if choose == "X" else 2 if choose == "Y" else 3
        else:
            return 0 if choose == "X" else 3 if choose == "Y" else 6
