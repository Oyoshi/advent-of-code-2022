from .day_01_solver import Day01Solver


def load_input_mock():
    return [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]


def test_solve_part_1():
    solver = Day01Solver()
    solver.load_input = load_input_mock
    assert solver.solve(1) == 7
