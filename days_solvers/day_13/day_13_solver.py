from ast import literal_eval
from functools import cmp_to_key
from days_solvers import DaySolver
from utils import sum_iterable


class Day13Solver(DaySolver):
    def __init__(self):
        self.day = "13"

    def load_input_impl(self, file):
        return [literal_eval(line.rstrip()) for line in file if line.rstrip() != ""]

    def solve_part_1(self):
        pairs = list(zip(*(iter(self.input_data),) * 2))
        return sum_iterable(
            [
                i + 1
                for i, e in enumerate(
                    [self.compare(pair[0], pair[1]) for pair in pairs]
                )
                if e == -1
            ]
        )

    def solve_part_2(self):
        divider_packets = [[[2]], [[6]]]
        res = sorted(
            self.input_data + divider_packets,
            key=cmp_to_key(lambda x, y: self.compare(x, y)),
        )
        return (res.index(divider_packets[0]) + 1) * (res.index(divider_packets[1]) + 1)

    def compare(self, lhs, rhs):
        match lhs, rhs:
            case [], []:
                return 0
            case [x, *xs], []:
                return 1
            case [], [x, *xs]:
                return -1
            case [x, *xs], [y, *ys]:
                match x, y:
                    case int(a), int(b):
                        if a < b:
                            return -1
                        elif a > b:
                            return 1
                        else:
                            return self.compare(xs, ys)
                    case int(a), [*b]:
                        ret = self.compare([a], b)
                        return ret if ret != 0 else self.compare(xs, ys)
                    case [*a], int(b):
                        ret = self.compare(a, [b])
                        return ret if ret != 0 else self.compare(xs, ys)
                    case [*a], [*b]:
                        ret = self.compare(a, b)
                        return ret if ret != 0 else self.compare(xs, ys)
