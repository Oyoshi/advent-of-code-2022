from days_solvers import DaySolver
from utils import sum_iterable


class Day08Solver(DaySolver):
    def __init__(self):
        self.day = "08"

    def load_input_impl(self, file):
        return [list(map(int, list(line.rstrip()))) for line in file]

    def solve_part_1(self):
        rows, cols = len(self.input_data), len(self.input_data[0])
        visibility_matrix = [[0] * cols for _ in range(rows)]
        for i in range(rows):
            max_val_from_left = self.input_data[i][0]
            max_val_from_right = self.input_data[i][cols - 1]
            for j in range(cols):
                if i == 0 or i == rows - 1:
                    visibility_matrix[i][j] = 1
                elif j == 0 or j == cols - 1:
                    visibility_matrix[i][j] = 1
                if max_val_from_left < self.input_data[i][j]:
                    visibility_matrix[i][j] = 1
                    max_val_from_left = self.input_data[i][j]
                if self.input_data[i][cols - 1 - j] > max_val_from_right:
                    visibility_matrix[i][cols - 1 - j] = 1
                    max_val_from_right = self.input_data[i][cols - 1 - j]
        for j in range(cols):
            max_val_from_top = self.input_data[0][j]
            max_val_from_bottom = self.input_data[rows - 1][j]
            for i in range(rows):
                if max_val_from_top < self.input_data[i][j]:
                    visibility_matrix[i][j] = 1
                    max_val_from_top = self.input_data[i][j]
                if self.input_data[rows - 1 - i][j] > max_val_from_bottom:
                    visibility_matrix[rows - 1 - i][j] = 1
                    max_val_from_bottom = self.input_data[rows - 1 - i][j]
        print(visibility_matrix)

        return sum_iterable(sum_iterable(visibility_matrix))

    def solve_part_2(self):
        pass
