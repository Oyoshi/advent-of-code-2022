import unittest
from .day_03_solver import Day03Solver


class Day02SolverTestCase(unittest.TestCase):
    def setUp(self):
        self.solver = Day03Solver()
        self.mock_input_data = [
            "vJrwpWtwJgWrhcsFMMfFFhFp",
            "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
            "PmmdzqPrVvPwwTWBwg",
            "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
            "ttgJtRGJQctTZtZT",
            "CrZsJsPPZsGzwwsLwLmpwMDw",
        ]
        self.solver.load_input = lambda: self.mock_input_data

    def tearDown(self):
        self.solver = None

    def test_solve_part_1(self):
        assert self.solver.solve(part=1)["val"] == 157

    def test_solve_part_2(self):
        assert self.solver.solve(part=2)["val"] == 70
