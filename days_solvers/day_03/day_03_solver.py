from itertools import chain
from ..day_solver import DaySolver
from utils import sum_iterable


class Day03Solver(DaySolver):
    def __init__(self):
        self.day = "03"

    def load_input_impl(self, file):
        return [line.rstrip() for line in file]

    def solve_part_1(self):
        rucksacks = map(list, self.input_data)
        unique_items = [
            next(
                iter(
                    set(rucksack[: len(rucksack) // 2])
                    & set(rucksack[len(rucksack) // 2 :])
                )
            )
            for rucksack in rucksacks
        ]
        return sum_iterable(map(self.map_item_to_priority, unique_items))

    def solve_part_2(self):
        it = iter(map(list, self.input_data))
        grouped_rucksacks = [
            [set(lhs), set(mid), set(rhs)] for lhs, mid, rhs in zip(it, it, it)
        ]
        unique_items = [next(iter(set.intersection(*gr))) for gr in grouped_rucksacks]
        return sum_iterable(map(self.map_item_to_priority, unique_items))

    def map_item_to_priority(self, char):
        return ord(char) - 96 if char.islower() else ord(char) - 38
