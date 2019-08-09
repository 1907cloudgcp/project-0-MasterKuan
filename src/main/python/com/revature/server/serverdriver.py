#!/usr/bin/env python3
import logging
import logging.config
import logging.handlers
import multiprocessing
import os
import sys
from serverio.bankdatalookup import set_file_directory
from serverio.multiclientserver import run_server as multi_client
from serverio.server import run_server as single_client


def listener_configurer():
    logging.basicConfig(level=logging.DEBUG, filename="resources/serverlog.log",
                        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", datefmt="%m/%d/%Y %I:%M:%S %p")


def logger_process(queue, configurer):
    configurer()
    while True:
        try:
            record = queue.get()
            if record is None:
                break
            logger = logging.getLogger(record.name)
            logger.handle(record)
        except KeyboardInterrupt:
            print("Keyboard interrupt")
            break


def run_server_driver(server_type):
    set_file_directory("resources/")
    queue = multiprocessing.Queue(-1)
    listener = multiprocessing.Process(target=logger_process, args=(queue, listener_configurer))
    listener.start()

    if server_type == "1":
        print("Starting single client server")
        single_client(queue)
    elif server_type == "2":
        print("Starting multi client server")
        multi_client(queue)
    else:
        print("Unavailable option")


if __name__ == '__main__':
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    if len(sys.argv) < 2:
        while True:
            print("Requires server type\n"
                  "1) Single client server\n"
                  "2) Multi client server")
            option = input("Server type: ")
            if not option == "1" and not option == "2":
                print("Enter a 1 or 2")
            else:
                run_server_driver(option)
    else:
        run_server_driver(sys.argv[1])
