from .day_01_solver import Day01Solver


def load_input_mock():
    return [6000, 4000, 11000, 24000, 10000]


def test_solve_part_1():
    solver = Day01Solver()
    solver.load_input = load_input_mock
    assert solver.solve(part=1)["val"] == 24000


def test_solve_part_1():
    solver = Day01Solver()
    solver.load_input = load_input_mock
    assert solver.solve(part=2)["val"] == 45000
