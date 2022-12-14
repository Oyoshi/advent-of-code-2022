import unittest
from .day_14_solver import Day14Solver


class Day14SolverTestCase(unittest.TestCase):
    def setUp(self):
        self.solver = Day14Solver()
        mock_input_data = {
            (6, 497),
            (7, 502),
            (4, 503),
            (5, 498),
            (9, 496),
            (9, 502),
            (9, 499),
            (6, 496),
            (6, 502),
            (4, 502),
            (9, 495),
            (9, 498),
            (8, 502),
            (9, 501),
            (6, 498),
            (4, 498),
            (9, 497),
            (5, 502),
            (9, 494),
            (9, 500),
        }
        self.solver.load_input = lambda: mock_input_data

    def tearDown(self):
        self.solver = None

    def test_solve_part_1(self):
        assert self.solver.solve(part=1)["val"] == 24

    def test_solve_part_2(self):
        assert self.solver.solve(part=2)["val"] == 93
