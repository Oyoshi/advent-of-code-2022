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
        rocks_ctr = 0
        step = 0
        height = 0
        occupied = set([(x, 0) for x in range(-1, 8)])  # ground
        while rocks_ctr < 2022:
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
        return height

    def solve_part_2(self):
        jets_pattern, rocks = self.input_data
        rocks_ctr = 0
        step = 0
        height = 0
        occupied = set([(x, 0) for x in range(-1, 8)])  # ground
        while rocks_ctr < 2022:
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
        return height

    def map_rock_to_coordinates(self, rock, x_l, y_t):
        coords = set()
        for i in range(len(rock)):
            for j in range(len(rock[i])):
                if rock[i][j] == 1:
                    coords.add((x_l + j, y_t - i))
        return coords
