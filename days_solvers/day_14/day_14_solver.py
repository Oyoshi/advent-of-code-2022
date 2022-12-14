from days_solvers import DaySolver


class Day14Solver(DaySolver):
    def __init__(self):
        self.day = "14"

    def load_input_impl(self, file):
        input_data = [
            [(tuple(map(int, e.split(",")))) for e in line.rstrip().split(" -> ")]
            for line in file
        ]
        rocks_pos = set()
        for rocks in input_data:
            k = 1
            while k < len(rocks):
                prev_coord = rocks[k - 1]
                cur_coord = rocks[k]
                px, py = prev_coord
                cx, cy = cur_coord
                if px == cx:
                    if py < cy:
                        for idx in range(py, cy + 1):
                            rocks_pos.add((idx, cx))
                    else:
                        for idx in range(cy, py + 1):
                            rocks_pos.add((idx, cx))
                else:
                    if px < cx:
                        for idx in range(px, cx + 1):
                            rocks_pos.add((cy, idx))
                    else:
                        for idx in range(cx, px + 1):
                            rocks_pos.add((cy, idx))
                k += 1
        return rocks_pos

    def solve_part_1(self):
        rocks = self.input_data
        sands = set()
        max_y = max(rocks, key=lambda e: e[0])[0]
        can_produce = True
        sand_coord = None
        while True:
            if can_produce:
                sand_coord = (0, 500)
                can_produce = False
            y, x = sand_coord
            if y + 1 <= max_y and (y + 1, x) not in rocks and (y + 1, x) not in sands:
                sand_coord = (y + 1, x)
            else:
                if (
                    y + 1 <= max_y
                    and (y + 1, x - 1) not in rocks
                    and (y + 1, x - 1) not in sands
                ):
                    sand_coord = (y + 1, x - 1)
                elif (
                    y + 1 <= max_y
                    and (y + 1, x + 1) not in rocks
                    and (y + 1, x + 1) not in sands
                ):
                    sand_coord = (y + 1, x + 1)
                else:
                    if y == max_y:
                        return len(sands)
                    else:
                        sands.add((y, x))
                        can_produce = True

    def solve_part_2(self):
        rocks = self.input_data
        sands = set()
        max_y = max(rocks, key=lambda e: e[0])[0] + 2
        can_produce = True
        sand_coord = None
        while True:
            if can_produce:
                sand_coord = (0, 500)
                can_produce = False
            y, x = sand_coord
            rocks.add((max_y, x))
            rocks.add((max_y, x - 1))
            rocks.add((max_y, x + 1))
            if (y + 1, x) not in rocks and (y + 1, x) not in sands:
                sand_coord = (y + 1, x)
            else:
                if (y + 1, x - 1) not in rocks and (y + 1, x - 1) not in sands:
                    sand_coord = (y + 1, x - 1)
                elif (y + 1, x + 1) not in rocks and (y + 1, x + 1) not in sands:
                    sand_coord = (y + 1, x + 1)
                else:
                    sands.add((y, x))
                    can_produce = True
                    if y == 0:
                        return len(sands)
