import unittest
from .day_11_solver import Day11Solver, Monkey


class Day11SolverTestCase(unittest.TestCase):
    def setUp(self):
        self.solver = Day11Solver()
        mock_input_data = [
            Monkey([79, 98], {"lhs": "old", "op": "*", "rhs": 19}, 23, 2, 3),
            Monkey([54, 65, 75, 74], {"lhs": "old", "op": "+", "rhs": 6}, 19, 2, 0),
            Monkey([79, 60, 97], {"lhs": "old", "op": "*", "rhs": "old"}, 13, 1, 3),
            Monkey([74], {"lhs": "old", "op": "+", "rhs": 3}, 17, 0, 1),
        ]
        self.solver.load_input = lambda: mock_input_data

    def tearDown(self):
        self.solver = None

    def test_solve_part_1(self):
        assert self.solver.solve(part=1)["val"] == 10605
