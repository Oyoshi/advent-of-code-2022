from days_solvers import DaySolver


class Day18Solver(DaySolver):
    def __init__(self):
        self.day = "18"

    def load_input_impl(self, file):
        return [tuple(map(int, line.rstrip().split(","))) for line in file]

    def solve_part_1(self):
        surfaces = {idx: 6 for idx in range(len(self.input_data))}
        for i in range(len(self.input_data)):
            for j in range(i + 1, len(self.input_data)):
                if self.are_connected(self.input_data[i], self.input_data[j]):
                    surfaces[i] -= 1
                    surfaces[j] -= 1
        return sum(surfaces.values())

    def are_connected(self, c1, c2):
        x1, x2 = c1[0], c2[0]
        y1, y2 = c1[1], c2[1]
        z1, z2 = c1[2], c2[2]
        return (
            (x1 == x2 and y1 == y2 and abs(z1 - z2) == 1)
            or (x1 == x2 and z1 == z2 and abs(y1 - y2) == 1)
            or (y1 == y2 and z1 == z2 and abs(x1 - x2) == 1)
        )

    def solve_part_2(self):
        pass
