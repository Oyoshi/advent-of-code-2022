#!/usr/bin/python3
from args_parser import parse_args
from tasks_solver import TasksSolver


def main():
    config = parse_args()
    tasks_solver = TasksSolver()
    tasks_solver.solve(config)


if __name__ == "__main__":
    main()
