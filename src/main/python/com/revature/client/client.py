#!/usr/bin/env python3
from .service.client import connect
from .controller.run import run_app


def main():
    sock = connect()
    if sock:
        run_app()
        sock.close()


if __name__ == '__main__':
    main()
