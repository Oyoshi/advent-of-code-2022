from days_solvers import DaySolver
from utils import sum_iterable


class Day25Solver(DaySolver):
    def __init__(self):
        self.day = "25"

    def load_input_impl(self, file):
        return [line.rstrip() for line in file]

    def solve_part_1(self):
        return self.convert_from_decimal_to_snafu(
            sum_iterable(
                [self.convert_from_snafu_to_decimal(snafu) for snafu in self.input_data]
            )
        )

    def solve_part_2(self):
        pass

    def convert_from_snafu_to_decimal(self, num):
        decimal_num = 0
        for i, d in enumerate(reversed(list(num))):
            decimal_num += (5**i) * self.match_digit_snafu(d)
        return decimal_num

    def convert_from_decimal_to_snafu(self, num):
        snafu_num = []
        while num != 0:
            r = num % 5
            if r == 3 or r == 4:
                r = num - 5 * (num // 5 + 1)
                num = num // 5 + 1
            else:
                num //= 5
            snafu_num.insert(0, self.match_digit_dec(r))
        return "".join(snafu_num)

    def match_digit_snafu(self, digit):
        match digit:
            case "=":
                return -2
            case "-":
                return -1
            case "0":
                return 0
            case "1":
                return 1
            case "2":
                return 2

    def match_digit_dec(self, digit):
        match digit:
            case -2:
                return "="
            case -1:
                return "-"
            case 0:
                return "0"
            case 1:
                return "1"
            case 2:
                return "2"
