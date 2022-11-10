from argparse import ArgumentParser

AOC_DAYS = 25
AOC_DAY_PARTS = 2


def parse_args():
    args_parser = create_args_parser()
    config = args_parser.parse_args()
    return config


def create_args_parser():
    args_parser = ArgumentParser(
        description="Advent of Code 2022 solutions", allow_abbrev=False
    )
    args_parser.add_argument(
        "--day",
        type=int,
        choices=range(1, AOC_DAYS + 1),
        metavar=f"[1-{AOC_DAYS}]",
        help="day of AoC",
    )
    args_parser.add_argument(
        "--part",
        type=int,
        choices=range(1, AOC_DAY_PARTS + 1),
        metavar=f"[1-{AOC_DAY_PARTS}]",
        help="part of the AoC day",
    )
    return args_parser
