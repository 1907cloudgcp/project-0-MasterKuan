#!/usr/bin/env python3
import os

from controller.run import run_app
from service.client import connect, send_info


def run_client_driver():
    sock = connect()
    if sock:
        run_app()
        send_info("", "")
        sock.close()


if __name__ == '__main__':
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    run_client_driver()
