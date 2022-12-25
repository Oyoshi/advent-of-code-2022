import unittest
from .day_23_solver import Day23Solver


class Day23SolverTestCase(unittest.TestCase):
    def setUp(self):
        self.solver = Day23Solver()
        mock_input_data = (
            {
                (3, 4),
                (4, 3),
                (3, 7),
                (4, 6),
                (9, 8),
                (8, 6),
                (7, 7),
                (6, 5),
                (6, 8),
                (9, 7),
                (9, 4),
                (6, 4),
                (7, 3),
                (7, 9),
                (3, 5),
                (4, 4),
                (5, 5),
                (8, 4),
                (5, 8),
                (9, 6),
                (7, 5),
                (7, 8),
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

    def test_solve_part_2(self):
        assert self.solver.solve(part=2)["val"] == 20
