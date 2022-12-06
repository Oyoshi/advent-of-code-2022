import unittest
from .day_06_solver import Day06Solver


class Day06SolverTestCase(unittest.TestCase):
    def setUp(self):
        self.solver = Day06Solver()
        mock_input_data = "mjqjpqmgbljsphdztnvjfqwrcgsmlb"
        self.solver.load_input = lambda: mock_input_data

    def tearDown(self):
        self.solver = None

    def test_solve_part_1(self):
        assert self.solver.solve(part=1)["val"] == 7

    def test_solve_part_2(self):
        assert self.solver.solve(part=2)["val"] == 19
