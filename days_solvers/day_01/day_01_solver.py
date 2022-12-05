from days_solvers import DaySolver
from utils import sum_iterable


class Day01Solver(DaySolver):
    def __init__(self):
        self.day = "01"

    def load_input_impl(self, file):
        input_data = []
        calories = []
        for line in file:
            if line.rstrip().isdigit():
                calories.append(int(line))
            else:
                input_data.append(calories)
                calories = []
        return input_data

    def solve_part_1(self):
        return self.sum_nth_max(self.input_data, 1)

    def solve_part_2(self):
        return self.sum_nth_max(self.input_data, 3)

    def sum_nth_max(self, iterable_input, nth):
        return sum_iterable(
            sorted(map(sum_iterable, iterable_input))[-nth:],
        )
