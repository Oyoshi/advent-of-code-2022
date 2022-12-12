from days_solvers import DaySolver


class Day12Solver(DaySolver):
    def __init__(self):
        self.day = "12"

    def load_input_impl(self, file):
        matrix = [list(line.rstrip()) for line in file]
        start = [
            (ix, iy)
            for ix, row in enumerate(matrix)
            for iy, i in enumerate(row)
            if i == "S"
        ][0]
        end = [
            (ix, iy)
            for ix, row in enumerate(matrix)
            for iy, i in enumerate(row)
            if i == "E"
        ][0]
        matrix[start[0]][start[1]] = "a"
        matrix[end[0]][end[1]] = "z"
        return [matrix, start, end]

    def solve_part_1(self):
        matrix, start, end = self.input_data
        distance = [[-1] * len(matrix[0]) for _ in range(len(matrix))]
        sx, sy = start
        Q = [start]
        distance[sx][sy] = 0
        while len(Q) != 0:
            pos = Q.pop()
            x, y = pos
            neighbours = self.compute_neighbours(
                x, y, len(matrix) - 1, len(matrix[0]) - 1
            )
            for n in neighbours:
                nx, ny = n
                if ord(matrix[nx][ny]) - ord(matrix[x][y]) <= 1:
                    if (nx, ny) == end:
                        return distance[x][y] + 1
                    if distance[nx][ny] == -1:
                        distance[nx][ny] = distance[x][y] + 1
                        Q.insert(0, (nx, ny))

    def compute_neighbours(self, x, y, x_max, y_max):
        return [
            (x + n[0], y + n[1])
            for n in [(-1, 0), (1, 0), (0, -1), (0, 1)]
            if (0 <= x + n[0] <= x_max) and (0 <= y + n[1] <= y_max)
        ]

    def solve_part_2(self):
        pass
