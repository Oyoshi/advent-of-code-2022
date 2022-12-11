from copy import deepcopy
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
        return self.simulate_monkey_in_the_middle(20, True)

    def solve_part_2(self):
        return self.simulate_monkey_in_the_middle(10000, False)

    def simulate_monkey_in_the_middle(self, rounds, divide):
        monkeys = deepcopy(self.input_data)
        monkeys_activity = [0] * len(monkeys)
        for _ in range(rounds):
            for mi in range(len(monkeys)):
                monkey = monkeys[mi]
                targets = []
                mod = monkey.mod
                l, op, r = mod["lhs"], mod["op"], mod["rhs"]
                for i in range(len(monkey.items)):
                    monkeys_activity[mi] = monkeys_activity[mi] + 1
                    item = monkey.items[i]
                    lhs = item if l == "old" else int(l)
                    rhs = item if r == "old" else int(r)
                    worry_lvl = 0
                    if op == "+":
                        worry_lvl = lhs + rhs
                    elif op == "-":
                        worry_lvl = lhs - rhs
                    elif op == "*":
                        worry_lvl = lhs * rhs
                    else:
                        worry_lvl = lhs // rhs
                    worry_lvl = worry_lvl // 3 if divide else worry_lvl
                    targets.append(monkey.throw_dest[worry_lvl % monkey.div == 0])
                    monkey.items[i] = worry_lvl
                while len(targets) != 0:
                    dest = targets.pop(0)
                    item = monkey.items.pop(0)
                    monkeys[dest].items.append(item)
        return mul_iterable((sorted(monkeys_activity)[-2:]))
