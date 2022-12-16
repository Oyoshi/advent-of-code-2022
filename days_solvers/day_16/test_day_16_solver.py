import unittest
from .day_16_solver import Day16Solver


class Day16SolverTestCase(unittest.TestCase):
    def setUp(self):
        self.solver = Day16Solver()
        mock_input_data = {
            "AA": {"flow": 0, "tunnels": ["DD", "II", "BB"]},
            "BB": {"flow": 13, "tunnels": ["CC", "AA"]},
            "CC": {"flow": 2, "tunnels": ["DD", "BB"]},
            "DD": {"flow": 20, "tunnels": ["CC", "AA", "EE"]},
            "EE": {"flow": 3, "tunnels": ["FF", "DD"]},
            "FF": {"flow": 0, "tunnels": ["EE", "GG"]},
            "GG": {"flow": 0, "tunnels": ["FF", "HH"]},
            "HH": {"flow": 22, "tunnels": ["GG"]},
            "II": {"flow": 0, "tunnels": ["AA", "JJ"]},
            "JJ": {"flow": 21, "tunnels": ["II"]},
        }
        self.solver.load_input = lambda: mock_input_data

    def tearDown(self):
        self.solver = None

    def test_solve_part_1(self):
        assert self.solver.solve(part=1)["val"] == 1651

    def test_solve_part_2(self):
        assert self.solver.solve(part=2)["val"] == 1707
