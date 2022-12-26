import unittest
from .day_21_solver import Day21Solver


class Day21SolverTestCase(unittest.TestCase):
    def setUp(self):
        self.solver = Day21Solver()
        mock_input_data = {
            "root": "pppw + sjmn",
            "dbpl": "5",
            "cczh": "sllz + lgvd",
            "zczc": "2",
            "ptdq": "humn - dvpt",
            "dvpt": "3",
            "lfqf": "4",
            "humn": "5",
            "ljgn": "2",
            "sjmn": "drzm * dbpl",
            "sllz": "4",
            "pppw": "cczh / lfqf",
            "lgvd": "ljgn * ptdq",
            "drzm": "hmdt - zczc",
            "hmdt": "32",
        }
        self.solver.load_input = lambda: mock_input_data

    def tearDown(self):
        self.solver = None

    def test_solve_part_1(self):
        assert self.solver.solve(part=1)["val"] == 152

    def test_solve_part_2(self):
        assert self.solver.solve(part=2)["val"] == 301
