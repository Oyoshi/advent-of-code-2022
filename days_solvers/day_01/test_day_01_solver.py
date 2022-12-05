import unittest
from .day_01_solver import Day01Solver


class Day01SolverTestCase(unittest.TestCase):
    def setUp(self):
        self.solver = Day01Solver()
        mock_input_data = [
            [1000, 2000, 3000],
            [4000],
            [5000, 6000],
            [7000, 8000, 9000],
            [10000],
        ]
        self.solver.load_input = lambda: mock_input_data

    def tearDown(self):
        self.solver = None

    def test_solve_part_1(self):
        assert self.solver.solve(part=1)["val"] == 24000

    def test_solve_part_2(self):
        assert self.solver.solve(part=2)["val"] == 45000
