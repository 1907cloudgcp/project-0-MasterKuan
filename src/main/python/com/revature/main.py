#!/usr/bin/env python3
import socket
from service.client import connect
from controller.redirector import run


def main():
	sock = connect()
	if sock:
		run(sock)
		sock.shutdown(socket.SHUT_RDWR)
		sock.close()


if __name__ == '__main__':
	main()
