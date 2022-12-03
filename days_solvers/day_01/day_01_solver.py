from ..day_solver import DaySolver
from utils import sum_iterable


class Day01Solver(DaySolver):
    def __init__(self):
        self.day = "01"

    def load_input_impl(self, file):
        input_data = []
        calories = []
        for val in file:
            if val.rstrip().isdigit():
                calories.append(int(val))
            else:
                input_data.append(calories)
                calories = []
        return input_data

    def solve_part_1(self):
        return sum_nth_max(self.input_data, 1)

    def solve_part_2(self):
        return sum_nth_max(self.input_data, 3)


def sum_nth_max(iterable_input, nth):
    return sum_iterable(
        sorted([sum_iterable(list_item) for list_item in iterable_input])[-nth:],
    )
