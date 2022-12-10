from days_solvers import DaySolver
from utils import sum_iterable


class Day10Solver(DaySolver):
    def __init__(self):
        self.day = "10"

    def load_input_impl(self, file):
        return [line.rstrip() for line in file]

    def solve_part_1(self):
        cycles = [20, 60, 100, 140, 180, 220]
        cycle_ctr = 1
        added_values = []
        signals = []
        for i in range(len(self.input_data)):
            if cycle_ctr in cycles:
                signals.append(1 + sum(added_values))
            instr = self.input_data[i].split()
            if instr[0] == "addx":
                cycle_ctr += 1
                if cycle_ctr in cycles:
                    signals.append(1 + sum(added_values))
                cycle_ctr += 1
                added_values.append(int(instr[1]))
            else:
                cycle_ctr += 1
        return sum_iterable(map(lambda e: e[0] * e[1], zip(cycles, signals)))

    def solve_part_2(self):
        width, height = 40, 6
        CRT = [[""] * width for _ in range(height)]
        X = 1
        cycle_ctr = 0
        for i in range(len(self.input_data)):
            instr = self.input_data[i].split()
            if instr[0] == "addx":
                if cycle_ctr % 40 >= X - 1 and cycle_ctr % 40 <= X + 1:
                    CRT[cycle_ctr // 40][cycle_ctr % 40] = "#"
                else:
                    CRT[cycle_ctr // 40][cycle_ctr % 40] = "."
                cycle_ctr += 1
                if cycle_ctr % 40 >= X - 1 and cycle_ctr % 40 <= X + 1:
                    CRT[cycle_ctr // 40][cycle_ctr % 40] = "#"
                else:
                    CRT[cycle_ctr // 40][cycle_ctr % 40] = "."
                cycle_ctr += 1
                X += int(instr[1])
            else:
                if cycle_ctr % 40 >= X - 1 and cycle_ctr % 40 <= X + 1:
                    CRT[cycle_ctr // 40][cycle_ctr % 40] = "#"
                else:
                    CRT[cycle_ctr // 40][cycle_ctr % 40] = "."
                cycle_ctr += 1
        for i in range(height):
            CRT[i] = "".join(CRT[i])
        return CRT

    def compute_pixel_pos(self, cycle_ctr):
        return cycle_ctr % 40
