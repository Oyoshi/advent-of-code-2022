from days_solvers import DaySolver


class Day15Solver(DaySolver):
    def __init__(self):
        self.day = "15"

    def load_input_impl(self, file):
        return [
            [
                tuple(
                    map(
                        int,
                        (
                            e[2].split("=")[1].rstrip(","),
                            e[3].split("=")[1].rstrip(":"),
                        ),
                    )
                ),
                tuple(map(int, (e[8].split("=")[1].rstrip(","), e[9].split("=")[1]))),
            ]
            for e in [line.rstrip().split() for line in file]
        ]

    def solve_part_1(self):
        return self.find_no_beacons(2000000)

    def solve_part_2(self):
        # TODO - refactor it asnd add missing UT
        data = list(
            map(
                lambda e: (
                    e[0][0],
                    e[0][1],
                    self.compute_manhattan_distance(e[0], e[1]),
                ),
                self.input_data,
            )
        )
        a = (
            set(x - y + r + 1 for x, y, r in data)
            .intersection(x - y - r - 1 for x, y, r in data)
            .pop()
        )
        b = (
            set(x + y + r + 1 for x, y, r in data)
            .intersection(x + y - r - 1 for x, y, r in data)
            .pop()
        )
        return (a + b) * 4000000 // 2 + (b - a) // 2

    def find_no_beacons(self, target_y):
        beacons = set(map(lambda e: e[1], self.input_data))
        no_beacons = set()
        for pair_data in self.input_data:
            sensor, beacon = pair_data
            distance = self.compute_manhattan_distance(sensor, beacon)
            x_min, x_max = sensor[0] - distance, sensor[0] + distance
            y_min, y_max = sensor[1] - distance, sensor[1] + distance
            if y_min <= target_y and target_y <= y_max:
                x = x_min
                while x <= x_max:
                    potential_empty_pos = (x, target_y)
                    if (
                        potential_empty_pos not in beacons
                        and self.compute_manhattan_distance(sensor, potential_empty_pos)
                        <= distance
                    ):
                        no_beacons.add(potential_empty_pos)
                    x += 1
        return len(list(filter(lambda e: e[1] == target_y, no_beacons)))

    def compute_manhattan_distance(self, lhs, rhs):
        return abs(lhs[0] - rhs[0]) + abs(lhs[1] - rhs[1])
