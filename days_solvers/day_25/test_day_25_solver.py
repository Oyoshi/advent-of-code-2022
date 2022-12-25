import unittest
from .day_25_solver import Day25Solver


class Day25SolverTestCase(unittest.TestCase):
    def setUp(self):
        self.solver = Day25Solver()
        mock_input_data = [
            "1=-0-2",
            "12111",
            "2=0=",
            "21",
            "2=01",
            "111",
            "20012",
            "112",
            "1=-1=",
            "1-12",
            "12",
            "1=",
            "122",
        ]
        self.solver.load_input = lambda: mock_input_data

    def tearDown(self):
        self.solver = None

    def test_solve_part_1(self):
        assert self.solver.solve(part=1)["val"] == "2=-1=0"
