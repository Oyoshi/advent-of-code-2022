from days_solvers import DaySolver


class Day17Solver(DaySolver):
    def __init__(self):
        self.day = "17"

    def load_input_impl(self, file):
        jets_pattern = list(map(lambda s: -1 if s == "<" else +1, file.readlines()[0]))
        rocks = [
            [[1, 1, 1, 1]],
            [[0, 1, 0], [1, 1, 1], [0, 1, 0]],
            [[0, 0, 1], [0, 0, 1], [1, 1, 1]],
            [[1], [1], [1], [1]],
            [[1, 1], [1, 1]],
        ]
        return jets_pattern, rocks

    def solve_part_1(self):
        jets_pattern, rocks = self.input_data
        return self.simulate_falling_rocks(jets_pattern, rocks, 0, 0, 2022)

    def solve_part_2(self):
        jets_pattern, rocks = self.input_data
        r1, r2 = self.find_cycle(jets_pattern, rocks)
        initial_height = r1[2]
        height_in_cycle = r2[2] - r1[2]
        cycle_length = r2[0] - r1[0]
        cycles_num = (1000000000000 - r1[0]) // cycle_length
        print(cycle_length, height_in_cycle, cycles_num * height_in_cycle)
        acc_height = cycles_num * height_in_cycle
        print(1514285714288 - cycles_num * height_in_cycle)
        total = (
            initial_height + acc_height
        )  # + self.simulate_falling_rocks(jets_pattern, rocks, 49, 78, 1000000000000 - cycles_num * cycle_length)
        print(1514285714288 - total)
        # print(1000000000000 - cycles_num * cycle_length - r1[0])

    def find_cycle(self, jets_pattern, rocks):
        rocks_ctr = 0
        step = 0
        height = 0
        occupied = set([(x, 0) for x in range(-1, 8)])  # ground
        register = []
        while True:
            can_fall = True
            rock = rocks[rocks_ctr % len(rocks)]
            rock_width, rock_height = len(rock[0]), len(rock)
            x_l, x_r = 2, 2 + rock_width - 1
            bottom_rock_height = height + 4
            occupied |= set([(-1, height + y) for y in range(1, 5)])  # left edge
            occupied |= set([(7, height + y) for y in range(1, 5)])  # right edge
            while can_fall:
                jet = jets_pattern[step % len(jets_pattern)]
                occupied_by_rock = self.map_rock_to_coordinates(
                    rock, x_l + jet, bottom_rock_height + rock_height - 1
                )
                if len(occupied.intersection(occupied_by_rock)) == 0:
                    x_r += jet
                    x_l += jet
                occupied_by_rock = self.map_rock_to_coordinates(
                    rock, x_l, bottom_rock_height + rock_height - 2
                )
                if len(occupied.intersection(occupied_by_rock)) == 0:
                    bottom_rock_height -= 1
                else:
                    can_fall = False
                    occupied_by_rock = self.map_rock_to_coordinates(
                        rock, x_l, bottom_rock_height + rock_height - 1
                    )
                    height = max(height, max(occupied_by_rock, key=lambda e: e[1])[1])
                    occupied |= occupied_by_rock
                register.append((rocks_ctr, step, height))
                i, j = self.check_for_cycle(register, len(rocks), len(jets_pattern))
                if i != -1 and j != -1:
                    return register[i], register[j - 1]
                step += 1
            rocks_ctr += 1

    def check_for_cycle(self, register, rocks_len, jets_pattern_len):
        cyclotron = list(
            map(lambda r: (r[0] % rocks_len, r[1] % jets_pattern_len), register)
        )
        for i in range(len(cyclotron)):
            for j in range(i + 1, len(cyclotron)):
                if cyclotron[i] == cyclotron[j]:
                    if (
                        2 * j - i < len(cyclotron)
                        and cyclotron[i:j] == cyclotron[j : 2 * j - i]
                    ):
                        return i, j
        return -1, -1

    def simulate_falling_rocks(self, jets_pattern, rocks, rocks_ctr, step, until):
        jets_pattern, rocks = self.input_data
        height = 0
        occupied = set([(x, 0) for x in range(-1, 8)])  # ground
        ctr = 0
        while ctr < until:
            can_fall = True
            rock = rocks[rocks_ctr % len(rocks)]
            rock_width, rock_height = len(rock[0]), len(rock)
            x_l, x_r = 2, 2 + rock_width - 1
            bottom_rock_height = height + 4
            occupied |= set([(-1, height + y) for y in range(1, 5)])  # left edge
            occupied |= set([(7, height + y) for y in range(1, 5)])  # right edge
            while can_fall:
                jet = jets_pattern[step % len(jets_pattern)]
                occupied_by_rock = self.map_rock_to_coordinates(
                    rock, x_l + jet, bottom_rock_height + rock_height - 1
                )
                if len(occupied.intersection(occupied_by_rock)) == 0:
                    x_r += jet
                    x_l += jet
                occupied_by_rock = self.map_rock_to_coordinates(
                    rock, x_l, bottom_rock_height + rock_height - 2
                )
                if len(occupied.intersection(occupied_by_rock)) == 0:
                    bottom_rock_height -= 1
                else:
                    can_fall = False
                    occupied_by_rock = self.map_rock_to_coordinates(
                        rock, x_l, bottom_rock_height + rock_height - 1
                    )
                    height = max(height, max(occupied_by_rock, key=lambda e: e[1])[1])
                    occupied |= occupied_by_rock
                step += 1
            rocks_ctr += 1
            ctr += 1
        return height

    def map_rock_to_coordinates(self, rock, x_l, y_t):
        coords = set()
        for i in range(len(rock)):
            for j in range(len(rock[i])):
                if rock[i][j] == 1:
                    coords.add((x_l + j, y_t - i))
        return coords
