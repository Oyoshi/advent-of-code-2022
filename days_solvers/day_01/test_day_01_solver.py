from .day_01_solver import Day01Solver


def load_input_mock():
    return [[1000, 2000, 3000], [4000], [5000, 6000], [7000, 8000, 9000], [10000]]


def test_solve_part_1():
    solver = Day01Solver()
    solver.load_input = load_input_mock
    assert solver.solve(part=1)["val"] == 24000


def test_solve_part_2():
    solver = Day01Solver()
    solver.load_input = load_input_mock
    assert solver.solve(part=2)["val"] == 45000
