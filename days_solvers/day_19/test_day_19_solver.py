import unittest
from .day_19_solver import Day19Solver


class Day19SolverTestCase(unittest.TestCase):
    def setUp(self):
        self.solver = Day19Solver()
        mock_input_data = [
            {
                "ore": {"ore": 4},
                "clay": {"ore": 2},
                "obsidian": {"ore": 3, "clay": 14},
                "geode": {"ore": 2, "obsidian": 7},
            },
            {
                "ore": {"ore": 2},
                "clay": {"ore": 3},
                "obsidian": {"ore": 3, "clay": 8},
                "geode": {"ore": 3, "obsidian": 12},
            },
        ]
        self.solver.load_input = lambda: mock_input_data

    def tearDown(self):
        self.solver = None

    def test_solve_part_1(self):
        assert self.solver.solve(part=1)["val"] == 33

    def test_solve_part_2(self):
        assert self.solver.solve(part=2)["val"] == 3472
