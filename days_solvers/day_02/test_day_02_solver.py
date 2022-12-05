import unittest
from .day_02_solver import Day02Solver


class Day02SolverTestCase(unittest.TestCase):
    def setUp(self):
        self.solver = Day02Solver()
        mock_input_data = [["A", "Y"], ["B", "X"], ["C", "Z"]]
        self.solver.load_input = lambda: mock_input_data

    def tearDown(self):
        self.solver = None

    def test_solve_part_1(self):
        assert self.solver.solve(part=1)["val"] == 15

    def test_solve_part_2(self):
        assert self.solver.solve(part=2)["val"] == 12
