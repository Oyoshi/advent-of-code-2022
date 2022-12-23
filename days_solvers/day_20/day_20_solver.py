from days_solvers import DaySolver
from utils import sum_iterable


class Day20Solver(DaySolver):
    def __init__(self):
        self.day = "20"

    def load_input_impl(self, file):
        return [int(line.rstrip()) for line in file]

    def solve_part_1(self):
        decoded = [(i, n) for i, n in enumerate(self.input_data)]
        self.decode(self.input_data, decoded)
        decoded = list(map(lambda e: e[1], decoded))
        zero_index = decoded.index(0)
        indices = [(zero_index + i * 1000) % len(decoded) for i in range(1, 4)]
        vals = [decoded[i] for i in indices]
        return sum_iterable(vals)

    def decode(self, encrypted, decoded):
        for i, number in enumerate(encrypted):
            encrypted_number = (i, number)
            current_position = decoded.index(encrypted_number)
            if number == 0:
                continue
            del decoded[current_position]
            new_position = (current_position + number) % len(decoded)
            decoded.insert(new_position, encrypted_number)

    def solve_part_2(self):
        pass

