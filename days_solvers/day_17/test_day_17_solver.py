import unittest
from .day_17_solver import Day17Solver


class Day17SolverTestCase(unittest.TestCase):
    def setUp(self):
        self.solver = Day17Solver()
        mock_input_data = [
            1,
            1,
            1,
            -1,
            -1,
            1,
            -1,
            1,
            1,
            -1,
            -1,
            -1,
            1,
            1,
            -1,
            1,
            1,
            1,
            -1,
            -1,
            -1,
            1,
            1,
            1,
            -1,
            -1,
            -1,
            1,
            -1,
            -1,
            -1,
            1,
            1,
            -1,
            1,
            1,
            -1,
            -1,
            1,
            1,
        ]
        self.solver.load_input = lambda: mock_input_data

    def tearDown(self):
        self.solver = None

    def test_solve_part_1(self):
        assert self.solver.solve(part=1)["val"] == 3068

    def test_solve_part_2(self):
        assert self.solver.solve(part=2)["val"] == 1514285714288
