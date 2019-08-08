#!/usr/bin/env python3
import logging.config
import os
from serverio.bankdatalookup import set_file_directory
from serverio.server import run_server


def run_server_driver():
    logging.basicConfig(level=logging.DEBUG, filename="resources/serverlog.log",
                        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", datefmt='%m/%d/%Y %I:%M:%S %p')
    set_file_directory("resources/")
    run_server()


if __name__ == '__main__':
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    run_server_driver()
