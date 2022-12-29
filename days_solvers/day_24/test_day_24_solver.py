import unittest
from .day_24_solver import Day24Solver, Tile, Direction


class Day24SolverTestCase(unittest.TestCase):
    def setUp(self):
        self.solver = Day24Solver()
        mock_input_data = (
            {
                (0, 0): Tile.WALL,
                (0, 2): Tile.WALL,
                (0, 3): Tile.WALL,
                (0, 4): Tile.WALL,
                (0, 5): Tile.WALL,
                (0, 6): Tile.WALL,
                (0, 7): Tile.WALL,
                (1, 0): Tile.WALL,
                (1, 1): (Tile.BLIZZARD, Direction.RIGHT),
                (1, 2): (Tile.BLIZZARD, Direction.RIGHT),
                (1, 4): (Tile.BLIZZARD, Direction.LEFT),
                (1, 5): (Tile.BLIZZARD, Direction.UP),
                (1, 6): (Tile.BLIZZARD, Direction.LEFT),
                (1, 7): Tile.WALL,
                (2, 0): Tile.WALL,
                (2, 2): (Tile.BLIZZARD, Direction.LEFT),
                (2, 5): (Tile.BLIZZARD, Direction.LEFT),
                (2, 6): (Tile.BLIZZARD, Direction.LEFT),
                (2, 7): Tile.WALL,
                (3, 0): Tile.WALL,
                (3, 1): (Tile.BLIZZARD, Direction.RIGHT),
                (3, 2): (Tile.BLIZZARD, Direction.DOWN),
                (3, 4): (Tile.BLIZZARD, Direction.RIGHT),
                (3, 5): (Tile.BLIZZARD, Direction.LEFT),
                (3, 6): (Tile.BLIZZARD, Direction.RIGHT),
                (3, 7): Tile.WALL,
                (4, 0): Tile.WALL,
                (4, 1): (Tile.BLIZZARD, Direction.LEFT),
                (4, 2): (Tile.BLIZZARD, Direction.UP),
                (4, 3): (Tile.BLIZZARD, Direction.DOWN),
                (4, 4): (Tile.BLIZZARD, Direction.UP),
                (4, 5): (Tile.BLIZZARD, Direction.UP),
                (4, 6): (Tile.BLIZZARD, Direction.RIGHT),
                (4, 7): Tile.WALL,
                (5, 0): Tile.WALL,
                (5, 1): Tile.WALL,
                (5, 2): Tile.WALL,
                (5, 3): Tile.WALL,
                (5, 4): Tile.WALL,
                (5, 5): Tile.WALL,
                (5, 7): Tile.WALL,
            },
            6,
            8,
        )
        self.solver.load_input = lambda: mock_input_data

    def tearDown(self):
        self.solver = None

    def test_solve_part_1(self):
        assert self.solver.solve(part=1)["val"] == 18

    def test_solve_part_2(self):
        assert self.solver.solve(part=2)["val"] == 54
