from copy import deepcopy
from math import lcm
from days_solvers import DaySolver
from utils import mul_iterable


class Monkey:
    def __init__(self, items, mod, div, dest_if_true, dest_if_false):
        self.items = items
        self.mod = mod
        self.div = div
        self.throw_dest = {True: dest_if_true, False: dest_if_false}


class Day11Solver(DaySolver):
    def __init__(self):
        self.day = "11"

    def load_input_impl(self, _):
        return [
            Monkey(
                [54, 82, 90, 88, 86, 54], {"lhs": "old", "op": "*", "rhs": 7}, 11, 2, 6
            ),
            Monkey([91, 65], {"lhs": "old", "op": "*", "rhs": 13}, 5, 7, 4),
            Monkey(
                [62, 54, 57, 92, 83, 63, 63],
                {"lhs": "old", "op": "+", "rhs": 1},
                7,
                1,
                7,
            ),
            Monkey([67, 72, 68], {"lhs": "old", "op": "*", "rhs": "old"}, 2, 0, 6),
            Monkey(
                [68, 89, 90, 86, 84, 57, 72, 84],
                {"lhs": "old", "op": "+", "rhs": 7},
                17,
                3,
                5,
            ),
            Monkey([79, 83, 64, 58], {"lhs": "old", "op": "+", "rhs": 6}, 13, 3, 0),
            Monkey([96, 72, 89, 70, 88], {"lhs": "old", "op": "+", "rhs": 4}, 3, 1, 2),
            Monkey([79], {"lhs": "old", "op": "+", "rhs": 8}, 19, 4, 5),
        ]

    def solve_part_1(self):
        return self.simulate_monkey_in_the_middle(20, 3)

    def solve_part_2(self):
        return self.simulate_monkey_in_the_middle(10000, 1)

    def simulate_monkey_in_the_middle(self, rounds, worry_div):
        monkeys = deepcopy(self.input_data)
        monkeys_activity = [0] * len(monkeys)
        modulo = lcm(*map(lambda m: m.div, monkeys))
        for _ in range(rounds):
            for mi in range(len(monkeys)):
                monkey = monkeys[mi]
                mod = monkey.mod
                l, op, r = mod["lhs"], mod["op"], mod["rhs"]
                while len(monkey.items) != 0:
                    monkeys_activity[mi] = monkeys_activity[mi] + 1
                    item = monkey.items.pop()
                    lhs = item if l == "old" else int(l)
                    rhs = item if r == "old" else int(r)
                    worry_lvl = self.evaluate(lhs, op, rhs) // worry_div
                    dest = monkey.throw_dest[worry_lvl % monkey.div == 0]
                    monkeys[dest].items.append(
                        worry_lvl if worry_div != 1 else worry_lvl % modulo
                    )
        return mul_iterable((sorted(monkeys_activity)[-2:]))

    def evaluate(self, lhs, op, rhs):
        if op == "+":
            return lhs + rhs
        elif op == "-":
            return lhs - rhs
        elif op == "*":
            return lhs * rhs
        else:
            return lhs // rhs
