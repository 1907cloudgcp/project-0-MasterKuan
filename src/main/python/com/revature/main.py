#!/usr/bin/env python3
from service.client import connect
from controller.run import run_app
from service.createaccount import create_account_connect_server
from service.loginservice import login_connect_server
from service.accountdeposit import deposit_connect_server
from service.accountwithdraw import withdraw_connect_server
from service.viewbalance import balance_connect_server
from service.viewtransactions import transaction_connect_server


def main():
	sock = connect()
	if sock:
		login_connect_server(sock)
		create_account_connect_server(sock)
		deposit_connect_server(sock)
		withdraw_connect_server(sock)
		balance_connect_server(sock)
		transaction_connect_server(sock)
		run_app()
		sock.close()


if __name__ == '__main__':
	main()
