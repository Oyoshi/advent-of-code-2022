import unittest
from .day_12_solver import Day12Solver


class Day12SolverTestCase(unittest.TestCase):
    def setUp(self):
        self.solver = Day12Solver()
        mock_input_data = [
            ["S", "a", "b", "q", "p", "o", "n", "m"],
            ["a", "b", "c", "r", "y", "x", "x", "l"],
            ["a", "c", "c", "s", "z", "E", "x", "k"],
            ["a", "c", "c", "t", "u", "v", "w", "j"],
            ["a", "b", "d", "e", "f", "g", "h", "i"],
        ]
        self.solver.load_input = lambda: mock_input_data

    def tearDown(self):
        self.solver = None

    def test_solve_part_1(self):
        assert self.solver.solve(part=1)["val"] == 31

    def test_solve_part_2(self):
        assert self.solver.solve(part=2)["val"] == 29
