from copy import deepcopy
from days_solvers import DaySolver
from utils import FifoQueue, mul_iterable


class Node:
    def __init__(self, time, ore, clay, obsidian, geode, robots):
        self.time = time
        self.resources = {
            "ore": ore,
            "clay": clay,
            "obsidian": obsidian,
            "geode": geode,
        }
        self.robots = robots

    def __str__(self):
        return (
            f"{self.time}: resources: {str(self.resources)}, robots: {str(self.robots)}"
        )


class Day19Solver(DaySolver):
    def __init__(self):
        self.day = "19"

    def load_input_impl(self, file):
        splitted_lines = [line.rstrip().split(". ") for line in file]
        blueprints = []
        robot_types = ["ore", "clay", "obsidian", "geode"]
        for sl in splitted_lines:
            blueprint = {}
            for i, r in enumerate(robot_types):
                blueprint |= self.parse_amount_and_unit(r, sl[i])
            blueprints.append(blueprint)
        return blueprints

    def parse_amount_and_unit(self, robot, cost_descr):
        splitted = cost_descr.split("costs ")[1].split(" ")
        costs = (
            [
                {"amount": int(splitted[0]), "unit": splitted[1]},
                {"amount": int(splitted[3]), "unit": splitted[4].rstrip(".")},
            ]
            if len(splitted) > 2
            else [{"amount": int(splitted[0]), "unit": splitted[1]}]
        )
        return {robot: costs}

    def solve_part_1(self):
        geo_per_blueprint = {}
        for b_idx, blueprint in enumerate(self.input_data):
            geodes = 0
            root = Node(
                25, 0, 0, 0, 0, {"ore": 1, "clay": 0, "obsidian": 0, "geode": 0}
            )
            Q = FifoQueue([root])
            while not Q.is_empty() and Q.top().time > 0:
                state = Q.dequeue()
                print(str(state), geodes)
                next_state_wait = self.create_next_state(
                    state, None, None
                )  # default wait
                next_state = None
                if self.can_build_robot(state, blueprint["geode"]):
                    next_state = self.create_next_state(state, blueprint, "geode")
                elif self.can_build_robot(state, blueprint["obsidian"]):
                    next_state = self.create_next_state(state, blueprint, "obsidian")
                elif self.can_build_robot(state, blueprint["clay"]):
                    next_state = self.create_next_state(state, blueprint, "clay")
                elif self.can_build_robot(state, blueprint["ore"]):
                    next_state = self.create_next_state(state, blueprint, "ore")
                if next_state:
                    Q.enqueue(next_state)
                Q.enqueue(next_state_wait)
                geodes = max(geodes, state.resources["geode"])
            geo_per_blueprint[b_idx] = geodes
        return mul_iterable(geo_per_blueprint.items())

    def can_build_robot(self, state, cost):
        return all(
            [
                state.resources[partial_cost["unit"]] >= partial_cost["amount"]
                for partial_cost in cost
            ]
        )

    def create_next_state(self, state, blueprint, robot):
        next_state = deepcopy(state)
        if robot:
            for partial_cost in blueprint[robot]:
                next_state.resources[partial_cost["unit"]] -= partial_cost["amount"]
        for rob, num in state.robots.items():
            next_state.resources[rob] += num
        if robot:
            next_state.robots[robot] += 1
        next_state.time -= 1
        return next_state

    def solve_part_2(self):
        pass
