import re
from days_solvers import DaySolver
from utils import sum_iterable, mul_iterable


class Day19Solver(DaySolver):
    def __init__(self):
        self.day = "19"

    def load_input_impl(self, file):
        splitted_lines = [line.rstrip() for line in file]
        blueprints = []
        for line in splitted_lines:
            vals = tuple(map(int, re.findall(r"\d+", line)))
            blueprints.append(
                {
                    "ore": {"ore": vals[1]},
                    "clay": {"ore": vals[2]},
                    "obsidian": {"ore": vals[3], "clay": vals[4]},
                    "geode": {"ore": vals[5], "obsidian": vals[6]},
                }
            )
        return blueprints

    def solve_part_1(self):
        return sum_iterable(
            (idx + 1) * self.largest_geode_num(bp, 24)
            for idx, bp in enumerate(self.input_data)
        )

    def solve_part_2(self):
        return mul_iterable(
            self.largest_geode_num(bp, 32) for bp in self.input_data[:3]
        )

    def largest_geode_num(self, bp, time):
        init_robots = {r: 1 if r == "ore" else 0 for r in bp}
        stack = [(0, init_robots, {m: 0 for m in bp}, set())]
        best_at_time = {}
        max_robots = self.get_max_robots(bp)
        while stack:
            t, robots, resources, skipped_last_iteration = stack.pop(0)
            best_at_time[t] = max(
                best_at_time[t] if t in best_at_time else 0, resources["geode"]
            )
            if t <= time and best_at_time[t] == resources["geode"]:
                options = self.get_build_options(bp, resources)
                for to_build in options:
                    if not to_build:
                        resources_ = self.harvest(robots, resources.copy())
                        stack.append((t + 1, robots, resources_, options))
                    elif (
                        to_build in skipped_last_iteration
                        or robots[to_build] + 1 > max_robots[to_build]
                    ):
                        continue
                    else:
                        robots_, resources_ = self.build_robot(
                            bp, robots.copy(), resources.copy(), to_build
                        )
                        resources_ = self.harvest(robots, resources_.copy())
                        stack.insert(0, (t + 1, robots_, resources_, set()))
        return best_at_time[time]

    def get_max_robots(self, bp):
        max_robots = {r: 9999999 if r == "geode" else 0 for r in bp}
        for _, needs in bp.items():
            for robot, amount in needs.items():
                max_robots[robot] = max(max_robots[robot], amount)
        return max_robots

    def get_build_options(self, bp, resources):
        options = {None}
        for robot, needs in bp.items():
            if all(amount <= resources[need] for need, amount in needs.items()):
                options.add(robot)
        return {"geode"} if "geode" in options else options

    def build_robot(self, bp, robots, resources, to_build):
        robots[to_build] += 1
        resources = resources | {k: resources[k] - v for k, v in bp[to_build].items()}
        return robots, resources

    def harvest(self, robots, resources):
        return {k: resources[k] + v for k, v in robots.items()}
