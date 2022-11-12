import itertools as it
from .day_solver import DaySolver


class Day01Solver(DaySolver):
    def __init__(self):
        self.day = "01"

    def solve_part_1(self):
        return count_increasing_elements(self.input_data)

    def solve_part_2(self):
        return count_increasing_elements(self.input_data)


def count_increasing_elements(iterable_input):
    pairs = [y - x for (x, y) in it.pairwise(iterable_input)]
    return len(list(filter(lambda elem: elem > 0, pairs)))
