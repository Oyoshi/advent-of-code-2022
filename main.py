#!/usr/bin/python3
import logging
from flow_executor import execute_flow

logging.basicConfig(format="%(levelname)s:%(message)s", level=logging.DEBUG)


if __name__ == "__main__":
    execute_flow()
