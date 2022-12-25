import unittest
from .day_23_solver import Day23Solver


class Day23SolverTestCase(unittest.TestCase):
    def setUp(self):
        self.solver = Day23Solver()
        mock_input_data = (
            {
                (4, 0),
                (3, 1),
                (5, 1),
                (0, 2),
                (2, 2),
                (1, 0),
                (1, 6),
                (2, 5),
                (1, 3),
                (6, 5),
                (4, 2),
                (4, 5),
                (5, 3),
                (0, 1),
                (0, 4),
                (6, 1),
                (6, 4),
                (3, 2),
                (3, 5),
                (4, 4),
                (1, 1),
                (6, 3),
            },
            [
                [(-1, 1), (0, 1), (1, 1)],
                [(-1, -1), (0, -1), (1, -1)],
                [(-1, 1), (-1, 0), (-1, -1)],
                [(1, 1), (1, 0), (1, -1)],
            ],
        )
        self.solver.load_input = lambda: mock_input_data

    def tearDown(self):
        self.solver = None

    def test_solve_part_1(self):
        assert self.solver.solve(part=1)["val"] == 110
