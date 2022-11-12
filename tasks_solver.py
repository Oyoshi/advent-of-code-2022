import importlib
import logging


class TasksSolver:
    def solve(self, config):
        day, part = config.day, config.part
        day_solver = self.get_solver(day)
        result = day_solver.solve(part)
        logging.info(f"Day:{day}/part:{part}: {result}")

    def get_solver(self, day):
        module = importlib.import_module("days_solvers")
        class_name = f"Day{day}Solver"
        DaySolver = getattr(module, class_name)
        day_solver = DaySolver()
        return day_solver
