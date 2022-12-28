from days_solvers import DaySolver

STATE_ELF = 16
STATE_UP = 8
STATE_RIGHT = 4
STATE_DOWN = 2
STATE_LEFT = 1

parse_map = {
    "^": STATE_UP,
    ">": STATE_RIGHT,
    "v": STATE_DOWN,
    "<": STATE_LEFT,
    ".": 0,
}
draw_map = {
    STATE_ELF: "E",
    STATE_UP: "^",
    STATE_RIGHT: ">",
    STATE_DOWN: "v",
    STATE_LEFT: "<",
    0: ".",
}
neighbors = {
    (0, -1): STATE_DOWN,
    (1, 0): STATE_LEFT,
    (0, 1): STATE_UP,
    (-1, 0): STATE_RIGHT,
}


def draw_scene(generation: dict, dimensions) -> None:
    width, height = dimensions
    for y in range(height):
        for x in range(width):
            state = generation.get((x, y))
            if not draw_map.get(state):
                bliz_num = 0
                for _ in range(4):
                    bliz_num += state & 1
                    state >>= 1
                print(bliz_num, end="")
                continue
            print(draw_map.get(state), end="")
        print()
    print()


def new_generation(generation: dict, dimensions, start, stop) -> dict:
    new_generation = {}
    for cell in generation:
        new_generation[cell] = 0
        for offset, state in neighbors.items():
            check_cell = (cell[0] + offset[0], cell[1] + offset[1])
            if cell != start and cell != stop:
                new_generation[cell] |= (
                    generation.get(
                        (check_cell[0] % dimensions[0], check_cell[1] % dimensions[1]),
                        0,
                    )
                    & state
                )
            new_generation[cell] |= generation.get(check_cell, 0) & STATE_ELF
        new_generation[cell] |= generation[cell] & STATE_ELF
        if new_generation[cell] - STATE_ELF > 0:
            new_generation[cell] ^= STATE_ELF

    return new_generation


class Day24Solver(DaySolver):
    def __init__(self):
        self.day = "24"

    def load_input_impl(self, file):
        return file.read().splitlines()  # [line.rstrip() for line in file]

    def solve_part_1(self):
        input_lines = self.input_data
        print(input_lines)
        generation = {
            (x, y): parse_map.get(char)
            for y, line in enumerate(input_lines, -1)
            for x, char in enumerate(line, -1)
            if not char == "#"
        }
        # print(generation)

        width = len(input_lines[0][1:-1])
        height = len(input_lines[1:-1])
        # print(width, height)
        start_pos = (0, -1)
        end_pos = (width - 1, height)

        generation[start_pos] = STATE_ELF
        generation[end_pos] = 0

        gen_count = 0
        while True:
            # print(gen_count)
            # draw_scene(generation, (width, height))
            if generation.get(end_pos) == STATE_ELF:
                break
            generation = new_generation(generation, (width, height), start_pos, end_pos)
            gen_count += 1
        return gen_count

    def solve_part_2(self):
        input_lines = self.input_data
        print(input_lines)
        generation = {
            (x, y): parse_map.get(char)
            for y, line in enumerate(input_lines, -1)
            for x, char in enumerate(line, -1)
            if not char == "#"
        }
        # print(generation)

        width = len(input_lines[0][1:-1])
        height = len(input_lines[1:-1])
        # print(width, height)
        start_pos = (0, -1)
        end_pos = (width - 1, height)

        generation[start_pos] = STATE_ELF
        generation[end_pos] = 0

        gen_count = 0
        while True:
            # print(gen_count)
            # draw_scene(generation, (width, height))
            if generation.get(end_pos) == STATE_ELF:
                break
            generation = new_generation(generation, (width, height), start_pos, end_pos)
            gen_count += 1
        generation[start_pos] = 0
        generation[end_pos] = STATE_ELF
        while True:
            # draw_scene(generation, (width, height))
            if generation.get(start_pos) == STATE_ELF:
                break
            generation = new_generation(generation, (width, height), end_pos, start_pos)
            gen_count += 1
        generation[start_pos] = STATE_ELF
        generation[end_pos] = 0
        while True:
            # print(gen_count)
            # draw_scene(generation, (width, height))
            if generation.get(end_pos) == STATE_ELF:
                break
            generation = new_generation(generation, (width, height), start_pos, end_pos)
            gen_count += 1
        return gen_count
