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
        return self.simulate_move(self.move_on_plain)

    def solve_part_2(self):
        pass
        # return self.simulate_move(self.move_on_cube)

    def simulate_move(self, move_rules_callback):
        board, instructions = self.input_data
        pos = (0, board[0].index("."))
        direction = Direction.RIGHT
        for instr in instructions:
            if instr.isdigit():
                pos = move_rules_callback(board, direction, pos, int(instr))
            else:
                direction = self.rotate(direction, instr)
        return 1000 * (pos[0] + 1) + 4 * (pos[1] + 1) + direction.value

    def move_on_plain(self, board, direction, pos, steps):
        match direction:
            case Direction.RIGHT:
                y, x = pos
                for _ in range(steps):
                    if x == len(board[y]) - 1 or board[y][x + 1] == " ":
                        new_x = board[y].index(".")
                        if new_x > 0 and board[y][new_x - 1] == "#":
                            return (y, x)
                        x = new_x
                    elif board[y][x + 1] == "#":
                        return (y, x)
                    else:
                        x += 1
                return (y, x)
            case Direction.LEFT:
                y, x = pos
                for _ in range(steps):
                    if x == 0 or board[y][x - 1] == " ":
                        new_x = len(board[y]) - 1 - board[y][::-1].index(".")
                        if new_x + 1 < len(board[y]) and board[y][new_x + 1] == "#":
                            return (y, x)
                        x = new_x
                    elif board[y][x - 1] == "#":
                        return (y, x)
                    else:
                        x -= 1
                return (y, x)
            case Direction.DOWN:
                y, x = pos
                for _ in range(steps):
                    if y == len(board) - 1 or board[y + 1][x] == " ":
                        i = 0
                        while i < y:
                            if board[i][x] == ".":
                                if i > 0 and board[i - 1][x] == "#":
                                    return (y, x)
                                y = i
                                break
                            i += 1
                    elif board[y + 1][x] == "#":
                        return (y, x)
                    else:
                        y += 1
                return (y, x)
            case Direction.UP:
                y, x = pos
                for _ in range(steps):
                    if y == 0 or board[y - 1][x] == " ":
                        i = len(board) - 1
                        while i >= 0:
                            if board[i][x] == ".":
                                if i < len(board) - 1 and board[i + 1][x] == "#":
                                    return (y, x)
                                y = i
                                break
                            i -= 1
                    elif board[y - 1][x] == "#":
                        return (y, x)
                    else:
                        y -= 1
                return (y, x)

    def move_on_cube(self, board, direction, pos, steps):
        match direction:
            case Direction.RIGHT:
                y, x = pos
                for _ in range(steps):
                    if x == len(board[y]) - 1 or board[y][x + 1] == " ":
                        new_x = board[y].index(".")
                        if new_x > 0 and board[y][new_x - 1] == "#":
                            return (y, x)
                        x = new_x
                    elif board[y][x + 1] == "#":
                        return (y, x)
                    else:
                        x += 1
                return (y, x)
            case Direction.LEFT:
                y, x = pos
                for _ in range(steps):
                    if x == 0 or board[y][x - 1] == " ":
                        new_x = len(board[y]) - 1 - board[y][::-1].index(".")
                        if new_x + 1 < len(board[y]) and board[y][new_x + 1] == "#":
                            return (y, x)
                        x = new_x
                    elif board[y][x - 1] == "#":
                        return (y, x)
                    else:
                        x -= 1
                return (y, x)
            case Direction.DOWN:
                y, x = pos
                for _ in range(steps):
                    if y == len(board) - 1 or board[y + 1][x] == " ":
                        i = 0
                        while i < y:
                            if board[i][x] == ".":
                                if i > 0 and board[i - 1][x] == "#":
                                    return (y, x)
                                y = i
                                break
                            i += 1
                    elif board[y + 1][x] == "#":
                        return (y, x)
                    else:
                        y += 1
                return (y, x)
            case Direction.UP:
                y, x = pos
                for _ in range(steps):
                    if y == 0 or board[y - 1][x] == " ":
                        i = len(board) - 1
                        while i >= 0:
                            if board[i][x] == ".":
                                if i < len(board) - 1 and board[i + 1][x] == "#":
                                    return (y, x)
                                y = i
                                break
                            i -= 1
                    elif board[y - 1][x] == "#":
                        return (y, x)
                    else:
                        y -= 1
                return (y, x)

    def determine_cube_faces(self, board):
        rows, cols = len(board), len(board[0])
        if rows > cols:
            pass

    def rotate(self, direction, instr):
        return (
            Direction((direction.value + 1) % 4)
            if instr == "R"
            else Direction((direction.value - 1) % 4)
        )
