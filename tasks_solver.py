import importlib


class TasksSolver:
    def solve(self, config):
        day, part = config.day, config.part
        module = importlib.import_module("days_solvers")
        class_name = f"Day{day}Solver"
        DaySolver = getattr(module, class_name)
        day_solver = DaySolver()
        result = day_solver.solve(part)
        print(f"Day:{day}/part:{part}: {result}")
