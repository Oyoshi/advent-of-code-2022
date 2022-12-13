import unittest
from .day_13_solver import Day13Solver


class Day13SolverTestCase(unittest.TestCase):
    def setUp(self):
        self.solver = Day13Solver()
        mock_input_data = [
            [1, 1, 3, 1, 1],
            [1, 1, 5, 1, 1],
            [[1], [2, 3, 4]],
            [[1], 4],
            [9],
            [[8, 7, 6]],
            [[4, 4], 4, 4],
            [[4, 4], 4, 4, 4],
            [7, 7, 7, 7],
            [7, 7, 7],
            [],
            [3],
            [[[]]],
            [[]],
            [1, [2, [3, [4, [5, 6, 7]]]], 8, 9],
            [1, [2, [3, [4, [5, 6, 0]]]], 8, 9],
        ]
        self.solver.load_input = lambda: mock_input_data

    def tearDown(self):
        self.solver = None

    def test_solve_part_1(self):
        assert self.solver.solve(part=1)["val"] == 13

    def test_solve_part_2(self):
        assert self.solver.solve(part=2)["val"] == 140
