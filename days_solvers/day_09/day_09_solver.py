from days_solvers import DaySolver


class Day09Solver(DaySolver):
    def __init__(self):
        self.day = "09"

    def load_input_impl(self, file):
        return list(
            map(lambda e: (e[0], int(e[1])), [line.rstrip().split() for line in file])
        )

    def solve_part_1(self):
        return self.simulate_rope(2)

    def solve_part_2(self):
        return self.simulate_rope(10)

    def simulate_rope(self, knots):
        rope = self.create_rope(knots)
        visited_by_tail = set()
        visited_by_tail.add(rope[knots - 1])
        for cmd in self.input_data:
            dir, val = cmd[0], cmd[1]
            while val > 0:
                if dir == "R":
                    rope[0] = (rope[0][0] + 1, rope[0][1])
                elif dir == "L":
                    rope[0] = (rope[0][0] - 1, rope[0][1])
                elif dir == "U":
                    rope[0] = (rope[0][0], rope[0][1] + 1)
                elif dir == "D":
                    rope[0] = (rope[0][0], rope[0][1] - 1)
                for i in range(1, knots):
                    rope[i] = self.align(rope[i - 1], rope[i])
                visited_by_tail.add(rope[knots - 1])
                val -= 1
        return len(visited_by_tail)

    def create_rope(self, knots):
        return [(0, 0)] * knots

    def align(self, h, t):
        dx = h[0] - t[0]
        dy = h[1] - t[1]
        if abs(dx) > 1 and abs(dy) > 1:
            return (t[0] + (dx // 2), t[1] + (dy // 2))
        elif dx > 1:
            return (t[0] + 1, h[1])
        elif dx < -1:
            return (t[0] - 1, h[1])
        elif dy > 1:
            return (h[0], t[1] + 1)
        elif dy < -1:
            return (h[0], t[1] - 1)
        else:
            return t
