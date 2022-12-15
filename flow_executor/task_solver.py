import importlib
import logging
import statistics
from .args_parser import AOC_DAYS


class TaskSolver:
    def solve(self, config):
        if config.benchmark:
            self.solve_benchmark(config.benchmark)
        else:
            self.solve_day(config)

    def solve_benchmark(self, trials):
        solvers = [
            self.get_solver(day)
            for day in [self.parse_day(day) for day in range(1, AOC_DAYS + 1)]
        ]
        results = [
            {
                "part1": [solver.solve(part=1, benchmark=True) for _ in range(trials)],
                "part2": [solver.solve(part=2, benchmark=True) for _ in range(trials)],
            }
            for solver in solvers
        ]
        print(self.generate_markdown_table(results))

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

    def generate_markdown_table(self, results):
        statistics_part_1 = self.calcute_statistics(results, "part1")
        statistics_part_2 = self.calcute_statistics(results, "part2")
        table_header = "|        | Part 1  &mu; [ms] | Part 1  &sigma; [ms] | Part 2  &mu; [ms] | Part 2  &sigma; [ms] |\n| ------ | ------  | ------ |  ------ |  ------ | \n"
        table_body = "".join(
            [
                f"| Day {self.parse_day(idx + 1)} | {stat[0][1]:.2f} | {stat[0][1]:.2f} |  {stat[1][0]:.2f} | {stat[1][1]:.2f} |\n"
                for idx, stat in enumerate(zip(statistics_part_1, statistics_part_2))
            ]
        )
        return table_header + table_body

    def calcute_statistics(self, results, part):
        return map(
            lambda t: (statistics.mean(t), statistics.stdev(t)),
            map(lambda e: list(map(lambda ee: ee["time"], e[part])), results),
        )
