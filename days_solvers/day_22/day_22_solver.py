import re
from enum import Enum
from days_solvers import DaySolver


class Direction(Enum):
    RIGHT = 0
    DOWN = 1
    LEFT = 2
    UP = 3


class Day22Solver(DaySolver):
    def __init__(self):
        self.day = "22"

    def load_input_impl(self, file):
        board = []
        instructions = []
        append_board = True
        for line in file:
            if line == "\n":
                append_board = False
                continue
            if append_board:
                board.append(list(line.rstrip()))
            else:
                instructions = [
                    instr for instr in re.split(r"(\d+)", line.rstrip()) if instr != ""
                ]
        max_len = max([len(b) for b in board])
        for i in range(len(board)):
            if len(board[i]) < max_len:
                board[i] += [" "] * (max_len - len(board[i]))
        return board, instructions

    def solve_part_1(self):
        return self.simulate_move(self.check_boundary_transition_part_1)

    def solve_part_2(self):
        return self.simulate_move(self.check_boundary_transition_part_2)

    def simulate_move(self, boundary_comp_cb):
        board, instructions = self.input_data
        pos = (0, board[0].index("."))
        direction = Direction.RIGHT
        for instr in instructions:
            if instr.isdigit():
                direction, pos = self.move(
                    board, direction, pos, int(instr), boundary_comp_cb
                )
            else:
                direction = self.rotate(direction, instr)
        return 1000 * (pos[0] + 1) + 4 * (pos[1] + 1) + direction.value

    def move(self, board, direction, pos, steps, boundary_comp_cb):
        while steps > 0:
            direction_, pos_ = boundary_comp_cb(direction, pos)
            if pos_ != pos:
                y_, x_ = pos_
                if board[y_][x_] == "#":
                    return direction, pos
                direction = direction_
                pos = pos_
            else:
                pos_ = self.step_on_face(direction, pos)
                y_, x_ = pos_
                if board[y_][x_] == "#":
                    return direction, pos
                pos = pos_
            steps -= 1
        return direction, pos

    def step_on_face(self, direction, pos):
        y, x = pos
        match direction:
            case Direction.RIGHT:
                return (y, x + 1)
            case Direction.LEFT:
                return (y, x - 1)
            case Direction.UP:
                return (y - 1, x)
            case Direction.DOWN:
                return (y + 1, x)

    def rotate(self, direction, instr):
        return (
            Direction((direction.value + 1) % 4)
            if instr == "R"
            else Direction((direction.value - 1) % 4)
        )

    # Below two implementations of boundary calculation strategy are based on
    # hardcoded shape (net) of my input which is:
    #
    #         @@@@@@@@
    #         @@@@@@@@
    #         @@@@@@@@
    #         @@@@@@@@
    #         @@@@
    #         @@@@
    #         @@@@
    #         @@@@
    #     @@@@@@@@
    #     @@@@@@@@
    #     @@@@@@@@
    #     @@@@@@@@
    #     @@@@
    #     @@@@
    #     @@@@
    #     @@@@

    def check_boundary_transition_part_1(self, direction, pos):
        y, x = pos
        pos_ = (y, x)
        if x == 0 and direction == Direction.LEFT:
            if 100 <= y and y < 150:
                pos_ = (y, 99)
            elif 150 <= y and y < 200:
                pos_ = (y, 49)
        elif x == 50 and direction == Direction.LEFT:
            if y < 50:
                pos_ = (y, 149)
            elif 50 <= y and y < 100:
                pos_ = (y, 99)
        elif x == 49 and 150 <= y and direction == Direction.RIGHT:
            pos_ = (y, 0)
        elif x == 99 and direction == Direction.RIGHT:
            if 50 <= y and y < 100:
                pos_ = (y, 50)
            elif 100 <= y and y < 150:
                pos_ = (y, 0)
        elif x == 149 and y < 50 and direction == Direction.RIGHT:
            pos_ = (y, 50)
        elif y == 0 and direction == Direction.UP:
            if 50 <= x and x < 100:
                pos_ = (149, x)
            elif 100 <= x and x < 150:
                pos_ = (49, x)
        elif y == 49 and 100 <= x and x < 150 and direction == Direction.DOWN:
            pos_ = (0, x)
        elif y == 100 and x < 50 and direction == Direction.UP:
            pos_ = (199, x)
        elif y == 149 and 50 <= x and x < 100 and direction == Direction.DOWN:
            pos_ = (0, x)
        elif y == 199 and x < 50 and direction == Direction.DOWN:
            pos_ = (100, x)
        return direction, pos_

    def check_boundary_transition_part_2(self, direction, pos):
        y, x = pos
        direction_ = direction
        pos_ = (y, x)
        if x == 0 and direction == Direction.LEFT:
            if 100 <= y and y < 150:
                pos_ = (50 - y % 50, 50)
                direction_ = Direction.RIGHT
            elif 150 <= y:
                pos_ = (0, 50 + y % 50)
                direction_ = Direction.DOWN
        elif x == 50 and direction == Direction.LEFT:
            if y < 50:
                pos_ = (100 + y % 50, 0)
                direction_ = Direction.RIGHT
            elif 50 <= y and y < 100:
                pos_ = (100, y % 50)
                direction_ = Direction.DOWN
        elif x == 49 and 150 <= y and direction == Direction.RIGHT:
            pos_ = (149, 50 + y % 50)
            direction_ = Direction.UP
        elif x == 99 and direction == Direction.RIGHT:
            if 50 <= y and y < 100:
                pos_ = (49, 100 + y % 50)
                direction_ = Direction.UP
            elif 100 <= y and y < 150:
                pos_ = (y % 50, 149)
                direction_ = Direction.LEFT
        elif x == 149 and y < 50 and direction == Direction.RIGHT:
            pos_ = (100 + y % 50, 99)
            direction_ = Direction.LEFT
        elif y == 0 and direction == Direction.UP:
            if 50 <= x and x < 100:
                pos_ = (150 + x % 50, 0)
                direction_ = Direction.RIGHT
            elif 100 <= x and x < 150:
                pos_ = (199, x % 50)
                direction_ = Direction.UP
        elif y == 49 and 100 <= x and x < 150 and direction == Direction.DOWN:
            pos_ = (50 + x % 50, 99)
            direction_ = Direction.LEFT
        elif y == 100 and x < 50 and direction == Direction.UP:
            pos_ = (50 + x % 50, 50)
            direction_ = Direction.RIGHT
        elif y == 149 and 50 <= x and x < 100 and direction == Direction.DOWN:
            pos_ = (150 + x % 50, 49)
            direction_ = Direction.LEFT
        elif y == 199 and x < 50 and direction == Direction.DOWN:
            pos_ = (0, 100 + x % 50)
            direction_ = Direction.DOWN
        return direction_, pos_
