import unittest
from .day_09_solver import Day09Solver


class Day09SolverTestCase(unittest.TestCase):
    def setUp(self):
        self.solver = Day09Solver()
        mock_input_data = [
            ("R", 4),
            ("U", 4),
            ("L", 3),
            ("D", 1),
            ("R", 4),
            ("D", 1),
            ("L", 5),
            ("R", 2),
        ]
        self.solver.load_input = lambda: mock_input_data

    def tearDown(self):
        self.solver = None

    def test_solve_part_1(self):
        assert self.solver.solve(part=1)["val"] == 13
