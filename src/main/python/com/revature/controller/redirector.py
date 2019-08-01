import re

def main_menu():
    while True:
        print("Actions:\n"
              "    Register\n"
              "    Login")
        user_input = input("Input: ").lower()
        action = parse(0, user_input)
        if action == 0:
            break
        elif action == 1:
            print("Register success")
        elif action == 2:
            print("Log in success")

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
