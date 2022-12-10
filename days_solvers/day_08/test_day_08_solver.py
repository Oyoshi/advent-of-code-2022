import unittest
from .day_08_solver import Day08Solver


class Day08SolverTestCase(unittest.TestCase):
    def setUp(self):
        self.solver = Day08Solver()
        mock_input_data = [
            [3, 0, 3, 7, 3],
            [2, 5, 5, 1, 2],
            [6, 5, 3, 3, 2],
            [3, 3, 5, 4, 9],
            [3, 5, 3, 9, 0],
        ]
        self.solver.load_input = lambda: mock_input_data

    def tearDown(self):
        self.solver = None

    def test_solve_part_1(self):
        assert self.solver.solve(part=1)["val"] == 21

    def test_solve_part_2(self):
        assert self.solver.solve(part=2)["val"] == 8
