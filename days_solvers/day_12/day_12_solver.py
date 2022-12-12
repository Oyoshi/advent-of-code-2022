from copy import deepcopy
from days_solvers import DaySolver
from utils import FifoQueue


class Day12Solver(DaySolver):
    def __init__(self):
        self.day = "12"

    def load_input_impl(self, file):
        return [list(line.rstrip()) for line in file]

    def solve_part_1(self):
        matrix = deepcopy(self.input_data)
        src = [
            (ix, iy)
            for ix, row in enumerate(matrix)
            for iy, i in enumerate(row)
            if i == "S"
        ][0]
        dest = [
            (ix, iy)
            for ix, row in enumerate(matrix)
            for iy, i in enumerate(row)
            if i == "E"
        ][0]
        sx, sy = src
        dx, dy = dest
        matrix[sx][sy] = "a"
        matrix[dx][dy] = "z"
        return self.compute_shortest_path_length(matrix, src, dest)

    def solve_part_2(self):
        matrix = deepcopy(self.input_data)
        s_coords = [
            (ix, iy)
            for ix, row in enumerate(matrix)
            for iy, i in enumerate(row)
            if i == "S"
        ][0]
        dest = [
            (ix, iy)
            for ix, row in enumerate(matrix)
            for iy, i in enumerate(row)
            if i == "E"
        ][0]
        matrix[s_coords[0]][s_coords[1]] = "a"
        matrix[dest[0]][dest[1]] = "z"
        sources = [
            (ix, iy)
            for ix, row in enumerate(matrix)
            for iy, i in enumerate(row)
            if i == "a"
        ]
        return min(
            filter(
                lambda e: e != -1,
                [
                    self.compute_shortest_path_length(matrix, src, dest)
                    for src in sources
                ],
            )
        )

    def compute_shortest_path_length(self, matrix, src, dest):
        distance = [[0] * len(matrix[0]) for _ in range(len(matrix))]
        Q = FifoQueue([src])
        sx, sy = src
        distance[sx][sy] = 0
        while not Q.is_empty():
            pos = Q.dequeue()
            x, y = pos
            neighbours = self.compute_neighbours(
                x, y, len(matrix) - 1, len(matrix[0]) - 1
            )
            for n in neighbours:
                nx, ny = n
                if ord(matrix[nx][ny]) - ord(matrix[x][y]) <= 1:
                    if (nx, ny) == dest:
                        return distance[x][y] + 1
                    if distance[nx][ny] == 0:
                        distance[nx][ny] = distance[x][y] + 1
                        Q.enqueue((nx, ny))
        return -1

    def compute_neighbours(self, x, y, x_max, y_max):
        return [
            (x + n[0], y + n[1])
            for n in [(-1, 0), (1, 0), (0, -1), (0, 1)]
            if (0 <= x + n[0] <= x_max) and (0 <= y + n[1] <= y_max)
        ]
