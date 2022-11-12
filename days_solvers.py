import os
import itertools as it
from abc import ABC, abstractmethod


class DaySolver(ABC):
    def solve(self, part):
        self.load_input()
        solve_impl = getattr(self, f"solve_part_{part}")
        return solve_impl()

    def load_input(self):
        file_path = os.path.join("inputs", self.get_input_filename())
        with open(file_path) as f:
            input_data = [int(val) for val in f]
        self.input_data = input_data

    def get_input_filename(self):
        return f"day_0{self.day}.txt" if self.day < 10 else f"day_{self.day}.txt"

    @abstractmethod
    def solve_part_1(self):
        pass

    @abstractmethod
    def solve_part_2(self):
        pass


class Day1Solver(DaySolver):
    def __init__(self):
        self.day = 1

    def solve_part_1(self):
        return count_increasing_elements(self.input_data)

    def solve_part_2(self):
        return count_increasing_elements(self.input_data)


def count_increasing_elements(iterable_input):
    pairs = [y - x for (x, y) in it.pairwise(iterable_input)]
    return len(list(filter(lambda elem: elem > 0, pairs)))


class Day2Solver:
    def __init__(self):
        print("Day 2")
