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
        min_val, max_val = self.compute_min_max_space_values()
        initial_cube = (min_val, min_val, min_val)
        cubes = [initial_cube]
        visited = {cubes[0]}
        surfaces = 0
        while len(cubes) > 0:
            cube = cubes.pop()
            neighbours = self.generate_neighbours(cube, min_val, max_val)
            for n in neighbours:
                if n in visited:
                    continue
                if n in self.input_data:
                    surfaces += 1
                else:
                    visited.add(n)
                    cubes.append(n)
        return surfaces

    def compute_min_max_space_values(self):
        x_min, x_max = self.compute_axis_boundaries(0)
        y_min, y_max = self.compute_axis_boundaries(1)
        z_min, z_max = self.compute_axis_boundaries(2)
        min_val = min(x_min, y_min, z_min) - 1
        max_val = max(x_max, y_max, z_max) + 1
        return min_val, max_val

    def compute_axis_boundaries(self, axis):
        sorted_points = sorted(self.input_data, key=lambda e: e[axis])
        return sorted_points[0][axis], sorted_points[len(sorted_points) - 1][axis]

    def generate_neighbours(self, cube, min_val, max_val):
        x, y, z = cube
        neighbours = [
            (x + 1, y, z),
            (x - 1, y, z),
            (x, y - 1, z),
            (x, y + 1, z),
            (x, y, z - 1),
            (x, y, z + 1),
        ]
        return filter(
            lambda n: all([min_val <= coord and coord <= max_val for coord in n]),
            neighbours,
        )
