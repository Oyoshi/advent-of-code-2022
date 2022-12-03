import functools as ft
from ..day_solver import DaySolver


class Day03Solver(DaySolver):
    def __init__(self):
        self.day = "03"

    def load_input_impl(self, file):
        return [line.rstrip() for line in file]

    def solve_part_1(self):
        rucksacks = [list(items) for items in self.input_data]
        unique_items = [
            next(
                iter(
                    set(rucksack[: len(rucksack) // 2])
                    & set(rucksack[len(rucksack) // 2 :])
                )
            )
            for rucksack in rucksacks
        ]
        priorities = [convert_char_to_priority(char) for char in unique_items]
        return ft.reduce(lambda a, b: a + b, priorities)

    def solve_part_2(self):
        pass


def convert_char_to_priority(char):
    return ord(char) - 96 if char.islower() else ord(char) - 38
