import unittest
from .day_20_solver import Day20Solver


class Day20SolverTestCase(unittest.TestCase):
    def setUp(self):
        self.solver = Day20Solver()
        mock_input_data = [1, 2, -3, 3, -2, 0, 4]
        self.solver.load_input = lambda: mock_input_data

    def tearDown(self):
        self.solver = None

    def test_solve_part_1(self):
        assert self.solver.solve(part=1)["val"] == 3
