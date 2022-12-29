from enum import Enum
from math import lcm
import heapq
from days_solvers import DaySolver


class Direction(Enum):
    UP = 1
    RIGHT = 2
    DOWN = 3
    LEFT = 4


class Tile(Enum):
    WALL = 1
    BLIZZARD = 2


class Day24Solver(DaySolver):
    def __init__(self):
        self.day = "24"

    def load_input_impl(self, file):
        valley_map = {}
        splitted_input = [list(line.rstrip()) for line in file]
        for r_idx, row in enumerate(splitted_input):
            for c_idx, col in enumerate(row):
                symbol = self.match_symbol(col)
                if symbol is not None:
                    coord = (r_idx, c_idx)
                    valley_map[coord] = symbol
        height = len(splitted_input)
        rows = len(splitted_input[0])
        return valley_map, height, rows

    def match_symbol(self, sym):
        match sym:
            case "#":
                return Tile.WALL
            case "^":
                return (Tile.BLIZZARD, Direction.UP)
            case ">":
                return (Tile.BLIZZARD, Direction.RIGHT)
            case "v":
                return (Tile.BLIZZARD, Direction.DOWN)
            case "<":
                return (Tile.BLIZZARD, Direction.LEFT)
            case _:
                return None

    def solve_part_1(self):
        _, height, width = self.input_data
        start_pos = (0, 1)
        end_pos = (height - 1, width - 2)
        positions = [(start_pos, end_pos)]
        return self.simulate_move(positions)

    def solve_part_2(self):
        _, height, width = self.input_data
        start_pos = (0, 1)
        end_pos = (height - 1, width - 2)
        positions = [(start_pos, end_pos), (end_pos, start_pos), (start_pos, end_pos)]
        return self.simulate_move(positions)

    def simulate_move(self, positions):
        valley_map, height, width = self.input_data
        walls = {c for c, t in valley_map.items() if t == Tile.WALL}
        inner_area_lcm = lcm(height - 2, width - 2)  # without walls
        blizzards_maps = self.generate_blizzards_maps(
            valley_map, inner_area_lcm, height, width
        )
        t = 0
        for start_pos, end_pos in positions:
            t = self.find_shortest_path(
                blizzards_maps,
                walls,
                height,
                width,
                inner_area_lcm,
                start_pos,
                end_pos,
                t,
            )
        return t

    # generates full map in each timestamp
    # crucial observation is that layouts are cyclic so there is no need to generate each map per time unit, just all maps per cycle
    def generate_blizzards_maps(self, valley_map, inner_area_lcm, height, width):
        cache = {}  # blizzard positions per time
        blizzards = [
            (c, t[1]) for c, t in valley_map.items() if t != Tile.WALL
        ]  # initial state
        init_blizzards_coords = set(map(lambda b: b[0], blizzards))
        cache[0] = init_blizzards_coords
        for t in range(1, inner_area_lcm + 1):
            upd_blizzards = []
            for coord, direction in blizzards:
                upd_coord = self.update_coord(coord, direction)
                match direction:
                    case Direction.UP:
                        if upd_coord[0] == 0:
                            upd_coord[0] = height - 2
                    case Direction.RIGHT:
                        if upd_coord[1] == width - 1:
                            upd_coord[1] = 1
                    case Direction.DOWN:
                        if upd_coord[0] == height - 1:
                            upd_coord[0] = 1
                    case Direction.LEFT:
                        if upd_coord[1] == 0:
                            upd_coord[1] = width - 2
                upd_blizzards.append((tuple(upd_coord), direction))
            blizzards = upd_blizzards
            cache[t] = set(map(lambda b: b[0], blizzards))
        return cache

    def update_coord(self, coord, direction):
        y, x = coord
        match direction:
            case Direction.UP:
                return [y - 1, x]
            case Direction.RIGHT:
                return [y, x + 1]
            case Direction.DOWN:
                return [y + 1, x]
            case Direction.LEFT:
                return [y, x - 1]

    def find_shortest_path(
        self,
        blizzards_maps,
        walls,
        height,
        width,
        inner_area_lcm,
        start_pos,
        end_pos,
        start_time,
    ):
        pq = [(start_time, start_pos)]
        heapq.heapify(pq)
        visited = set((start_time, start_pos))
        while pq:
            time, pos = heapq.heappop(pq)
            if pos == end_pos:
                return time
            upd_time = time + 1
            blizzards = blizzards_maps[upd_time % inner_area_lcm]
            possible_moves = [pos] + list(self.compute_neighbours(pos, height, width))
            not_occupied = list(
                filter(lambda c: c not in walls and c not in blizzards, possible_moves)
            )
            for n_pos in not_occupied:
                if (upd_time, n_pos) not in visited:
                    heapq.heappush(pq, (upd_time, n_pos))
                    visited.add((upd_time, n_pos))
        return -1

    def compute_neighbours(self, pos, height, width):
        y, x = pos
        return filter(
            lambda pos: 0 <= pos[0]
            and pos[0] < height
            and 0 <= pos[1]
            and pos[1] < width,
            [(y - 1, x), (y + 1, x), (y, x - 1), (y, x + 1)],
        )
