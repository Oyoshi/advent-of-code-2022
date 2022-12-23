import unittest
from .day_05_solver import Day05Solver


class Day05SolverTestCase(unittest.TestCase):
    def setUp(self):
        self.solver = Day05Solver()
        mock_crates = [["Z", "N"], ["M", "C", "D"], ["P"]]
        mock_moves = [(1, 2, 1), (3, 1, 3), (2, 2, 1), (1, 1, 2)]
        mock_input_data = mock_crates, mock_moves
        self.solver.load_input = lambda: mock_input_data

    def tearDown(self):
        self.solver = None

    def test_solve_part_1(self):
        assert self.solver.solve(part=1)["val"] == "CMZ"

    def test_solve_part_2(self):
        assert self.solver.solve(part=2)["val"] == "MCD"
