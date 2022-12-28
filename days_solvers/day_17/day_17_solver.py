from math import floor
from days_solvers import DaySolver


class Day17Solver(DaySolver):
    def __init__(self):
        self.day = "17"

    def load_input_impl(self, file):
        return list(map(lambda s: -1 if s == "<" else +1, file.readlines()[0]))

    def solve_part_1(self):
        return self.simulate_falling_rocks(2022)

    def solve_part_2(self):
        return self.simulate_falling_rocks(1000000000000)

    def simulate_falling_rocks(self, until):
        jet = 0
        next_rock = 0
        tower_height = 0
        rocks_ctr = 0
        cycle_found = False
        seen_states = {}
        rocks_in_state = 30
        solid_squares = set([(x, 0) for x in range(7)])
        placed_rocks = []

        while rocks_ctr < until:
            if not cycle_found:
                last_n_rocks = list(
                    map(
                        lambda rock: frozenset(
                            [(x, y - tower_height) for x, y in rock]
                        ),
                        placed_rocks[-rocks_in_state:],
                    )
                )
            start_state = frozenset([jet, next_rock, frozenset(last_n_rocks)])
            if start_state in seen_states:
                cycle_found = True
                r0, height0 = seen_states[start_state]
                cycle_length = rocks_ctr - r0
                height_per_cycle = tower_height - height0
                remaining_rocks = until - r0
                num_cyles = floor(remaining_rocks / cycle_length)
                rocks_ctr = r0 + (cycle_length * num_cyles)
                tower_height = height0 + (height_per_cycle * num_cyles)
                for rock in last_n_rocks:
                    for x, y in rock:
                        solid_squares.add((x, y + tower_height))
            else:
                seen_states[start_state] = (rocks_ctr, tower_height)
            rock = self.spawn_rock(tower_height, next_rock)
            while True:
                jet_direction = self.input_data[jet]
                jet = (jet + 1) % len(self.input_data)
                if self.should_push(rock, jet_direction, solid_squares):
                    rock = self.push(rock, jet_direction)
                if self.should_fall(rock, solid_squares):
                    rock = self.fall(rock)
                else:
                    break
            max_y, rock = self.come_to_rest(rock, solid_squares, placed_rocks)
            tower_height = max(tower_height, max_y)
            next_rock = (next_rock + 1) % 5
            rocks_ctr += 1
        return tower_height

    def spawn_rock(self, tower_height, pattern):
        x, y = (2, tower_height + 4)

        match pattern:
            case 0:
                return set([(x, y), (x + 1, y), (x + 2, y), (x + 3, y)])
            case 1:
                return set(
                    [
                        (x + 1, y),
                        (x, y + 1),
                        (x + 1, y + 1),
                        (x + 2, y + 1),
                        (x + 1, y + 2),
                    ]
                )
            case 2:
                return set(
                    [(x, y), (x + 1, y), (x + 2, y), (x + 2, y + 1), (x + 2, y + 2)]
                )
            case 3:
                return set([(x, y), (x, y + 1), (x, y + 2), (x, y + 3)])
            case 4:
                return set([(x, y), (x + 1, y), (x, y + 1), (x + 1, y + 1)])

    def fall(self, rock):
        return set([(x, y - 1) for x, y in rock])

    def push(self, rock, direction):
        return set([(x + direction, y) for x, y in rock])

    def should_fall(self, rock, solid_squares):
        for square in rock:
            x, y = square
            if (x, y - 1) in solid_squares:
                return False
        return True

    def should_push(self, rock, direction, solid_squares):
        for square in rock:
            x, y = square

            if direction == -1 and x - 1 < 0:
                return False

            if direction == 1 and x + 1 > 6:
                return False

            if (x + direction, y) in solid_squares:
                return False

        return True

    def come_to_rest(self, rock, solid_squares, placed_rocks):
        max_y = 0

        for square in rock:
            _, y = square
            solid_squares.add(square)
            max_y = max(max_y, y)

        placed_rocks.append(rock)
        return (max_y, rock)
