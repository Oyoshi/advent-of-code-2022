from .day_02_solver import Day02Solver


def load_input_mock():
    return [["A", "Y"], ["B", "X"], ["C", "Z"]]


def test_solve_part_1():
    solver = Day02Solver()
    solver.load_input = load_input_mock
    assert solver.solve(part=1)["val"] == 15


def test_solve_part_2():
    solver = Day02Solver()
    solver.load_input = load_input_mock
    assert solver.solve(part=2)["val"] == 12
