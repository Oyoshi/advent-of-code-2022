from copy import deepcopy
from days_solvers import DaySolver


class Day23Solver(DaySolver):
    def __init__(self):
        self.day = "23"

    def load_input_impl(self, file):
        matrix = [list(line.rstrip()) for line in file]
        coords = set()
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == "#":
                    coords.add((j, len(matrix) - 1 - i))
        instructions = [
            [(-1, 1), (0, 1), (1, 1)],
            [(-1, -1), (0, -1), (1, -1)],
            [(-1, 1), (-1, 0), (-1, -1)],
            [(1, 1), (1, 0), (1, -1)],
        ]
        return coords, instructions

    def solve_part_1(self):
        coords, instructions = deepcopy(self.input_data)
        for _ in range(10):
            moves = self.generate_move_proposals(coords, instructions)
            updated_coords = self.execute_moves(coords, moves)
            coords = updated_coords
            first = instructions.pop(0)
            instructions.append(first)
        return self.compute_not_occupied_tiles(coords)

    def solve_part_2(self):
        coords, instructions = deepcopy(self.input_data)
        rounds = 0
        while True:
            rounds += 1
            moves = self.generate_move_proposals(coords, instructions)
            if len(moves) == 0:
                break
            updated_coords = self.execute_moves(coords, moves)
            coords = updated_coords
            first = instructions.pop(0)
            instructions.append(first)
        return rounds

    def generate_move_proposals(self, coords, instructions):
        all_neighbour_coords = [
            (-1, -1),
            (-1, 0),
            (-1, 1),
            (0, -1),
            (0, 1),
            (1, -1),
            (1, 0),
            (1, 1),
        ]
        all_potential_moves = {
            c: self.compute_neighbourhood(c, all_neighbour_coords) for c in coords
        }
        can_move = {
            c: d
            for c, d in all_potential_moves.items()
            if len(d.intersection(coords)) != 0
        }
        can_move = set(can_move.keys())
        will_move = {}
        for coord in can_move:
            i = 0
            valid_instr = False
            while i < len(instructions) and not valid_instr:
                moves = self.compute_neighbourhood(coord, instructions[i])
                if len(moves.intersection(coords)) == 0:
                    valid_instr = True
                else:
                    i += 1
            if valid_instr:
                will_move[coord] = self.compute_neighbourhood(
                    coord, [instructions[i][1]]
                ).pop()
        return will_move

    def compute_neighbourhood(self, coord, neighbour_coords):
        x, y = coord
        return set([(x + n[0], y + n[1]) for n in neighbour_coords])

    def execute_moves(self, coords, moves):
        unique_moves = {
            s: d for s, d in moves.items() if list(moves.values()).count(d) == 1
        }
        kupa = coords.difference(set(unique_moves.keys())).union(
            set(unique_moves.values())
        )
        return kupa

    def compute_not_occupied_tiles(self, coords):
        width = (
            max(coords, key=lambda c: c[0])[0] - min(coords, key=lambda c: c[0])[0] + 1
        )
        height = (
            max(coords, key=lambda c: c[1])[1] - min(coords, key=lambda c: c[1])[1] + 1
        )
        return width * height - len(coords)
