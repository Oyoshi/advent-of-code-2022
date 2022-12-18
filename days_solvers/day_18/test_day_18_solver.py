import unittest
from .day_18_solver import Day18Solver


class Day18SolverTestCase(unittest.TestCase):
    def setUp(self):
        self.solver = Day18Solver()
        mock_input_data = [
            (2, 2, 2),
            (1, 2, 2),
            (3, 2, 2),
            (2, 1, 2),
            (2, 3, 2),
            (2, 2, 1),
            (2, 2, 3),
            (2, 2, 4),
            (2, 2, 6),
            (1, 2, 5),
            (3, 2, 5),
            (2, 1, 5),
            (2, 3, 5),
        ]
        self.solver.load_input = lambda: mock_input_data

    def tearDown(self):
        self.solver = None

    def test_solve_part_1(self):
        assert self.solver.solve(part=1)["val"] == 64

    def test_solve_part_2(self):
        assert self.solver.solve(part=2)["val"] == 58
