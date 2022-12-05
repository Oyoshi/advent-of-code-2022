from days_solvers import DaySolver


class Day05Solver(DaySolver):
    def __init__(self):
        self.day = "05"

    def load_input_impl(self, file):
        crates = [
            ["L", "N", "W", "T", "D"],
            ["C", "P", "H"],
            ["W", "P", "H", "N", "D", "G", "M", "J"],
            ["C", "W", "S", "N", "T", "Q", "L"],
            ["P", "H", "C", "N"],
            ["T", "H", "N", "D", "M", "W", "Q", "B"],
            ["M", "B", "R", "J", "G", "S", "L"],
            ["Z", "N", "W", "G", "V", "B", "R", "T"],
            ["W", "G", "D", "N", "P", "L"],
        ]
        moves = []
        for line in file:
            cmd = line.rstrip().split()
            amount, src, dest = cmd[1], cmd[3], cmd[5]
            moves.append(map(int, (amount, src, dest)))
        return [crates, moves]

    def solve_part_1(self):
        crates, moves = self.input_data[0], self.input_data[1]
        for move in moves:
            amount, src, dest = move
            while amount > 0:
                crates[dest - 1].append(crates[src - 1].pop())
                amount -= 1
        return "".join(crate.pop() for crate in crates)

    def solve_part_2(self):
        crates, moves = self.input_data[0], self.input_data[1]
        for move in moves:
            amount, src, dest = move
            tmp_queue = []
            while amount > 0:
                tmp_queue.append(crates[src - 1].pop())
                amount -= 1
            while len(tmp_queue) != 0:
                crates[dest - 1].append(tmp_queue.pop())
        return "".join(crate.pop() for crate in crates)
