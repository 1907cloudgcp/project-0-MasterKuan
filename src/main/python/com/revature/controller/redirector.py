from service.loginservice import *

server = None


def redirector_connect_server(sock):
    global server
    server = sock


def run():
    run_main_menu()


def run_main_menu():
    while True:
        action = main_menu()
        if action == 0:
            break
        elif action == 1:
            print(server.sendall("Register account!"))
        elif action == 2:
            login_connect_server(server)
            if login_service():
                account_menu()


def run_account_menu():
    while True:
        action = account_menu()


def main_menu():
    while True:
        print("Main Actions:\n"
              "    Register\n"
              "    Login\n"
              "    Exit")

        user_input = input("Input: ").lower()
        action = parse_main_menu(user_input)

        if action == 0:
            return 0
        elif action == 1:
            print("Register new account:")
            return 1
        elif action == 2:
            return 2


def account_menu():
    while True:
        print("Account Actions:\n"
              "    Deposit\n"
              "    Withdraw\n"
              "    History\n"
              "    Logout")
        user_input = input("Input: ").lower()
        if not parse_account_menu(user_input):
            break


def parse_main_menu(action):
    if action == "exit":
        print("\nExiting")
        return 0
    elif action == "register" :
        print("\nRegistering")
        return 1
    elif action == "login":
        print("\nLogging in")
        return 2
    else:
        print("\nInput was not recognized.")
        return 3


def parse_account_menu(action):
    if action == "logout":
        print("\nLogging out")
        return 0
    elif action == "deposit":
        print("\nDepositing")
        return 1
    elif action == "withdraw":
        print("\nWithdrawing")
        return 2
    elif action == "history":
        print("\nViewing transactions history")
        return 3
    else:
        print("\nInput was not recognized.")
        return 4
