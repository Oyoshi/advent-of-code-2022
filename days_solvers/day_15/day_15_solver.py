from days_solvers import DaySolver


class Day15Solver(DaySolver):
    def __init__(self):
        self.day = "15"

    def load_input_impl(self, file):
        return list(
            map(
                lambda e: (e[0], e[1], self.compute_distance(e[0], e[1])),
                [
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
                        tuple(
                            map(
                                int,
                                (e[8].split("=")[1].rstrip(","), e[9].split("=")[1]),
                            )
                        ),
                    ]
                    for e in [line.rstrip().split() for line in file]
                ],
            )
        )

    def solve_part_1(self):
        return self.find_no_beacons(2000000)

    def solve_part_2(self):
        max_range = 4000000
        y = 0
        while y <= max_range:
            segments = []
            for sensor, _, dist in self.input_data:
                delta_h = abs(y - sensor[1])
                if delta_h <= dist:
                    segments.append(
                        [
                            max(0, sensor[0] - (dist - delta_h)),
                            min(sensor[0] + (dist - delta_h), max_range + 1),
                        ]
                    )
            sorted_segments = sorted(segments)
            max_y = sorted_segments[0][1]
            i = 1
            while i < len(sorted_segments):
                max_y = max(max_y, sorted_segments[i - 1][1])
                if max_y + 1 < sorted_segments[i][0]:
                    return 4000000 * (sorted_segments[i - 1][1] + 1) + y
                i += 1
            y += 1
        return -1

    def find_no_beacons(self, target_y):
        beacons = set(map(lambda e: e[1], self.input_data))
        no_beacons = set()
        for sensor, _, dist in self.input_data:
            x_min, x_max = sensor[0] - dist, sensor[0] + dist
            y_min, y_max = sensor[1] - dist, sensor[1] + dist
            if y_min <= target_y and target_y <= y_max:
                x = x_min
                while x <= x_max:
                    potential_empty_pos = (x, target_y)
                    if (
                        potential_empty_pos not in beacons
                        and self.compute_distance(sensor, potential_empty_pos) <= dist
                    ):
                        no_beacons.add(potential_empty_pos)
                    x += 1
        return len(list(filter(lambda e: e[1] == target_y, no_beacons)))

    def compute_distance(self, lhs, rhs):
        return abs(lhs[0] - rhs[0]) + abs(lhs[1] - rhs[1])
