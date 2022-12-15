import unittest
from .day_15_solver import Day15Solver


class Day15SolverTestCase(unittest.TestCase):
    def setUp(self):
        self.solver = Day15Solver()
        mock_input_data = [
            [(2, 18), (-2, 15)],
            [(9, 16), (10, 16)],
            [(13, 2), (15, 3)],
            [(12, 14), (10, 16)],
            [(10, 20), (10, 16)],
            [(14, 17), (10, 16)],
            [(8, 7), (2, 10)],
            [(2, 0), (2, 10)],
            [(0, 11), (2, 10)],
            [(20, 14), (25, 17)],
            [(17, 20), (21, 22)],
            [(16, 7), (15, 3)],
            [(14, 3), (15, 3)],
            [(20, 1), (15, 3)],
        ]
        self.solver.load_input = lambda: mock_input_data
        self.solver.solve_part_1 = lambda: self.solver.find_no_beacons(10)

    def tearDown(self):
        self.solver = None

    def test_solve_part_1(self):
        assert self.solver.solve(part=1)["val"] == 26
