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
        return sum_iterable(sum_iterable(visibility_matrix))

    def solve_part_2(self):
        rows, cols = len(self.input_data), len(self.input_data[0])
        scenic_score = 0
        for i in range(1, rows - 1):
            for j in range(1, cols - 1):
                tree_height = self.input_data[i][j]
                l, r = j - 1, j + 1
                t, b = i - 1, i + 1
                l_scoring, r_scoring = 0, 0
                t_scoring, b_scoring = 0, 0
                while l >= 0:
                    l_scoring += 1
                    if self.input_data[i][l] >= tree_height:
                        l = 0
                    l -= 1
                while r < cols:
                    r_scoring += 1
                    if self.input_data[i][r] >= tree_height:
                        r = cols
                    r += 1
                while b < rows:
                    b_scoring += 1
                    if self.input_data[b][j] >= tree_height:
                        b = rows
                    b += 1
                while t >= 0:
                    t_scoring += 1
                    if self.input_data[t][j] >= tree_height:
                        t = 0
                    t -= 1
                scoring = l_scoring * r_scoring * t_scoring * b_scoring
                scenic_score = max(scenic_score, scoring)
        return scenic_score
