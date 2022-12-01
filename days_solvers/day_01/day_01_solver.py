import functools as ft
import os
from ..day_solver import DaySolver


class Day01Solver(DaySolver):
    def __init__(self):
        self.day = "01"

    # override default implementation
    def load_input(self):
        file_path = os.path.join("inputs", self.get_input_filename())
        input_data = []
        with open(file_path) as f:
            calories = []
            for val in f:
                if val.rstrip().isdigit():
                    calories.append(int(val))
                else:
                    input_data.append(calories)
                    calories = []
        return [ft.reduce(lambda a, b: a + b, list_item) for list_item in input_data]

    def solve_part_1(self):
        return sum_nth_max(self.input_data, 1)

    def solve_part_2(self):
        return sum_nth_max(self.input_data, 3)


def sum_nth_max(iterable_input, nth):
    return ft.reduce(lambda a, b: a + b, sorted(iterable_input)[-nth:])
