import re
from enum import Enum
from days_solvers import DaySolver

from copy import deepcopy


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
        board, instructions = self.input_data
        copied_board = deepcopy(board)
        pos = (0, board[0].index("."))
        direction = Direction.RIGHT
        for instr in instructions:
            if instr.isdigit():
                pos = self.move(board, direction, pos, int(instr), copied_board)
            else:
                direction = self.rotate(direction, instr)
                self.mark_on_board(copied_board, direction, pos)
        return 1000 * (pos[0] + 1) + 4 * (pos[1] + 1) + direction.value

    def mark_on_board(self, board, direction, pos):
        y, x = pos
        match direction:
            case Direction.RIGHT:
                board[y][x] = ">"
            case Direction.DOWN:
                board[y][x] = "v"
            case Direction.LEFT:
                board[y][x] = "<"
            case Direction.UP:
                board[y][x] = "^"

    def move(self, board, direction, pos, steps, cp_board):
        match direction:
            case Direction.RIGHT:
                y, x = pos
                for _ in range(steps):
                    self.mark_on_board(cp_board, direction, (y, x))
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
                    self.mark_on_board(cp_board, direction, (y, x))
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
                    self.mark_on_board(cp_board, direction, (y, x))
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
                    self.mark_on_board(cp_board, direction, (y, x))
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

    def rotate(self, direction, instr):
        return (
            Direction((direction.value + 1) % 4)
            if instr == "R"
            else Direction((direction.value - 1) % 4)
        )

    def solve_part_2(self):
        pass
