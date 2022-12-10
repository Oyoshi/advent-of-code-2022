from days_solvers import DaySolver


class Day09Solver(DaySolver):
    def __init__(self):
        self.day = "09"

    def load_input_impl(self, file):
        return list(
            map(lambda e: (e[0], int(e[1])), [line.rstrip().split() for line in file])
        )

    def solve_part_1(self):
        head_pos = (0, 0)
        tail_pos = (0, 0)
        visited_pos = set()
        visited_pos.add(tail_pos)
        for cmd in self.input_data:
            dir, val = cmd[0], cmd[1]
            while val > 0:
                if dir == "R":
                    head_pos = (head_pos[0] + 1, head_pos[1])
                    if head_pos[0] - tail_pos[0] > 1:
                        tail_pos = (tail_pos[0] + 1, head_pos[1])
                if dir == "L":
                    head_pos = (head_pos[0] - 1, head_pos[1])
                    if tail_pos[0] - head_pos[0] > 1:
                        tail_pos = (tail_pos[0] - 1, head_pos[1])
                if dir == "U":
                    head_pos = (head_pos[0], head_pos[1] + 1)
                    if head_pos[1] - tail_pos[1] > 1:
                        tail_pos = (head_pos[0], tail_pos[1] + 1)
                if dir == "D":
                    head_pos = (head_pos[0], head_pos[1] - 1)
                    if tail_pos[1] - head_pos[1] > 1:
                        tail_pos = (head_pos[0], tail_pos[1] - 1)
                visited_pos.add(tail_pos)
                val -= 1
        return len(visited_pos)

    def solve_part_2(self):
        pass
