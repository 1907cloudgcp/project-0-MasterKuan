#!/usr/bin/env python3
from controller.run import run_app
from service.connection import connect


def main():
    sock = connect()
    if sock:
        run_app()
        sock.close()


if __name__ == '__main__':
    main()
