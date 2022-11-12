from .args_parser import parse_args
from .task_solver import TaskSolver


def execute_flow():
    config = parse_args()
    tasks_solver = TaskSolver()
    tasks_solver.solve(config)
