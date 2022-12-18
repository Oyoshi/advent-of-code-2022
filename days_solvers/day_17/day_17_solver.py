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
        rocks_ctr, step, height = self.find_cycle(jets_pattern, rocks)
        cycle_length = rocks_ctr
        cycles_num = 1000000000000 // (cycle_length + 1)
        acc_height = cycles_num * height
        print(rocks_ctr, cycles_num * (cycle_length + 1))
        rest_height = self.simulate_falling_rocks(
            jets_pattern, rocks, 0, step, 1000000000000 - cycles_num * cycle_length
        )
        return acc_height + rest_height

    def find_cycle(self, jets_pattern, rocks):
        rocks_ctr = 0
        step = 0
        height = 0
        occupied = set([(x, 0) for x in range(-1, 8)])  # ground
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
                step += 1
            rocks_ctr += 1
            if rocks_ctr >= 25:
                cycle_height = self.check_for_cycle(occupied, height)
                if cycle_height != -1:
                    return rocks_ctr - 1, step - 1, cycle_height

    def check_for_cycle(self, occupied, height):
        first_floor = sorted(
            list(set([(x, 1) for x in range(-1, 8)]).intersection(occupied)),
            key=lambda e: e[0],
        )
        matches = []
        for h in range(2, height + 1):
            floor = sorted(
                list(set([(x, h) for x in range(-1, 8)]).intersection(occupied)),
                key=lambda e: e[0],
            )
            if len(floor) != len(first_floor):
                continue
            diff = [(f2[0] - f1[0], f2[1]) for f1, f2 in zip(first_floor, floor)]
            if len(diff) == len(list(filter(lambda e: e[0] == 0, diff))):
                matches.append(h)
        differences = [j - i for i, j in zip(matches[:-1], matches[1:])]
        print(matches)
        print(sorted(occupied, key=lambda e: e[1]))
        return matches[0] - 1
        # idx = differences[1:].index(differences[0]) if len(differences) > 0 and differences[0] in differences[1:] else -1
        # if idx != -1:
        #    print(matches[idx+2])
        #    print(sorted(occupied, key=lambda e: e[1]))
        # return -1 if idx == -1 else matches[idx+2] - 1

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
