from .args_parser import parse_args
from .tasks_solver import TasksSolver


class FlowBuilder:
    def __init__(self):
        self.config = None

    def execute_flow(self):
        self.parse_args_flow().solve_task_flow()

    def parse_args_flow(self):
        self.config = parse_args()
        return self

    def solve_task_flow(self):
        tasks_solver = TasksSolver()
        tasks_solver.solve(self.config)
        return self
