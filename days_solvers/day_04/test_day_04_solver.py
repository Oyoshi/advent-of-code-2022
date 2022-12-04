import unittest
from .day_04_solver import Day04Solver


class Day04SolverTestCase(unittest.TestCase):
    def setUp(self):
        self.solver = Day04Solver()
        self.mock_input_data = [
            [(2, 4), (6, 8)],
            [(2, 3), (4, 5)],
            [(5, 7), (7, 9)],
            [(2, 8), (3, 7)],
            [(6, 6), (4, 6)],
            [(2, 6), (4, 8)],
        ]
        self.solver.load_input = lambda: self.mock_input_data

    def tearDown(self):
        self.solver = None

    def test_solve_part_1(self):
        assert self.solver.solve(part=1)["val"] == 2

    def test_solve_part_2(self):
        assert self.solver.solve(part=2)["val"] == 4
