import importlib
import logging
from .args_parser import AOC_DAYS


class TaskSolver:
    def solve(self, config):
        if config.benchmark:
            self.solve_benchmark()
        else:
            self.solve_day(config)

    def solve_benchmark(self):
        solvers = [
            self.get_solver(day)
            for day in [self.parse_day(day) for day in range(1, AOC_DAYS + 1)]
        ]
        results = [
            {
                "part1": solver.solve(part=1, benchmark=True),
                "part2": solver.solve(part=2, benchmark=True),
            }
            for solver in solvers
        ]
        for idx, res in enumerate(results):
            logging.info(
                f"Day:{self.parse_day(idx + 1)}/Part:1:{res['part1']['time']}/Part:2:{res['part2']['time']}"
            )

    def solve_day(self, config):
        day, part = self.parse_day(config.day), config.part
        day_solver = self.get_solver(day)
        result = day_solver.solve(part)
        logging.info(f"Day:{day}/Part:{part}: {result['val']}")

    def parse_day(self, day):
        return f"0{day}" if day < 10 else str(day)

    def get_solver(self, day):
        module = importlib.import_module("days_solvers")
        class_name = f"Day{day}Solver"
        DaySolver = getattr(module, class_name)
        day_solver = DaySolver()
        return day_solver