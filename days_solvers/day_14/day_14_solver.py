from days_solvers import DaySolver


class Day14Solver(DaySolver):
    def __init__(self):
        self.day = "14"

    def load_input_impl(self, file):
        input_data = [
            [(tuple(map(int, e.split(",")))) for e in line.rstrip().split(" -> ")]
            for line in file
        ]
        flatten = [coord for row in input_data for coord in row]
        max_x, max_y = (
            max(flatten, key=lambda e: e[0])[0],
            max(flatten, key=lambda e: e[1])[1],
        )
        caves = [["."] * (max_x + 1) for _ in range(max_y + 1)]
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
                            caves[idx][cx] = "#"
                    else:
                        for idx in range(cy, py + 1):
                            caves[idx][cx] = "#"
                else:
                    if px < cx:
                        for idx in range(px, cx + 1):
                            caves[cy][idx] = "#"
                    else:
                        for idx in range(cx, px + 1):
                            caves[cy][idx] = "#"
                k += 1
        return caves

    def solve_part_1(self):
        caves = self.input_data
        max_y = len(caves)
        sand_ctr = 0
        can_produce = True
        sand_coord = None
        while True:
            if can_produce:
                sand_coord = (0, 500)
                can_produce = False
                sand_ctr += 1
            y, x = sand_coord
            if y + 1 == max_y:
                return sand_ctr - 1
            if caves[y + 1][x] == ".":
                sand_coord = (y + 1, x)
            else:
                if caves[y + 1][x - 1] == ".":
                    sand_coord = (y + 1, x - 1)
                elif caves[y + 1][x + 1] == ".":
                    sand_coord = (y + 1, x + 1)
                else:
                    caves[y][x] = "o"
                    can_produce = True

    def solve_part_2(self):
        pass
