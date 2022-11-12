#!/usr/bin/python3
import logging
from flow_builder import FlowBuilder

logging.basicConfig(format="%(levelname)s:%(message)s", level=logging.DEBUG)


def main():
    flow_builder = FlowBuilder()
    flow_builder.execute_flow()


if __name__ == "__main__":
    main()
