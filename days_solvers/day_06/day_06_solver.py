from days_solvers import DaySolver
from utils import sum_iterable


class Day06Solver(DaySolver):
    def __init__(self):
        self.day = "06"

    def load_input_impl(self, file):
        return list(file.readlines()[0])

    def solve_part_1(self):
        SEQ_SIZE = 4
        start_idx = 0
        end_idx = len(self.input_data) - 1
        marker = -1
        while start_idx < end_idx - SEQ_SIZE and marker == -1:
            seq = set(self.input_data[start_idx : start_idx + SEQ_SIZE])
            if len(seq) == SEQ_SIZE:
                marker = start_idx + SEQ_SIZE
            start_idx += 1
        return marker

    def solve_part_2(self):
        pass
