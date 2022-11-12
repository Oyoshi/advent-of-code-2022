#!/usr/bin/python3
import logging
from args_parser import parse_args
from tasks_solver import TasksSolver

logging.basicConfig(format="%(levelname)s:%(message)s", level=logging.DEBUG)


def main():
    config = parse_args()
    tasks_solver = TasksSolver()
    tasks_solver.solve(config)


if __name__ == "__main__":
    main()
