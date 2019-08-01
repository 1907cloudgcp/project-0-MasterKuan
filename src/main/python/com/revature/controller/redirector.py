from service.loginservice import *


def run(sock):
    connect_server(sock)

    while True:
        action = main_menu()
        if action == 0:
            break
        elif action == 1:
            print(sock.sendall("Register account!"))
        elif action == 2:
            username = input("Username: ")
            password = input("Password: ")
            login(username, password)


def main_menu():
    while True:
        print("Actions:\n"
              "    Register\n"
              "    Login")

        user_input = input("Input: ").lower()
        action = parse(0, user_input)

        if action == 0:
            return 0
        elif action == 1:
            print("Register new account:")
            return 1
        elif action == 2:
            print("Login:")
            return 2


def account_menu():
    while True:
        print("Actions:\n"
              "    Deposit\n"
              "    Withdraw\n"
              "    History\n"
              "    Logout")
        user_input = input("Input: ").lower()
        if not parse(1, user_input):
            break


def parse(menu, action):
    if (action == "exit"):
        print("Exiting")
        return 0
    elif (action == "register" and menu == 0):
        print("Registering")
        return 1
    elif (action == "login" and menu == 0):
        print("Logging in")
        return 2
    elif (action == "logout" and menu == 1):
        print("Logging out")
        return 0
    elif (action == "deposit" and menu == 1):
        print("Depositing")
        return 1
    elif (action == "withdraw" and menu == 1):
        print("Withdrawing")
        return 2
    elif (action == "history" and menu == 1):
        print("Viewing transactions history")
        return 3
    else:
        print("Input was not recognized.")
        return 4
