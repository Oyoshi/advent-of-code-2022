import importlib
import logging


class TaskSolver:
    def solve(self, config):
        if config.benchmark:
            self.solve_benchmark()
        else:
            self.solve_day(config)

    def solve_benchmark(self):
        pass

    def solve_day(self, config):
        day, part = self.parse_day(config.day), config.part
        day_solver = self.get_solver(day)
        result = day_solver.solve(part)
        logging.info(f"Day:{day}/part:{part}: {result}")

    def parse_day(self, day):
        return f"0{day}" if day < 10 else str(day)

    def get_solver(self, day):
        module = importlib.import_module("days_solvers")
        class_name = f"Day{day}Solver"
        DaySolver = getattr(module, class_name)
        day_solver = DaySolver()
        return day_solver
