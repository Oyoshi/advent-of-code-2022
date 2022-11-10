class TasksSolver:
    def __init__(self):
        self.days_solver = {1: "xxx"}

    def solve(self, config):
        day, part = config.day, config.part
        day_solver = self.days_solvers[day]
        result = day_solver.solve(part)
        print(f"Day:{day}/part:{part}: {result}")
