import unittest
from .day_24_solver import Day24Solver


class Day24SolverTestCase(unittest.TestCase):
    def setUp(self):
        self.solver = Day24Solver()
        mock_input_data = [
            "#.######",
            "#>>.<^<#",
            "#.<..<<#",
            "#>v.><>#",
            "#<^v^^>#",
            "######.#",
        ]
        self.solver.load_input = lambda: mock_input_data

    def tearDown(self):
        self.solver = None

    def test_solve_part_1(self):
        assert self.solver.solve(part=1)["val"] == 18
