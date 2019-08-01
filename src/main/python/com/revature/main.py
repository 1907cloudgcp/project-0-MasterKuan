#!/usr/bin/env python3
import socket
from controller.redirector import *
from service.client import connect


def main():
	sock = connect()
	if sock:
		redirector_connect_server(sock)
		run()
		sock.shutdown(socket.SHUT_RDWR)
		sock.close()


if __name__ == '__main__':
	main()
