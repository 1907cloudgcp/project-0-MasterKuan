from service.accountdeposit import *
from service.accountwithdraw import *
from service.viewtransactions import *


# Run until logout
def run_account_menu(session):
    data = session.split()
    account_number = int(data[0])
    session_token = data[1]

    while True:
        action = account_menu()
        if action == 0:
            return 0
        elif action == 1:
            break
        elif action == 2:
            break
        elif action == 3:
            break


# Get user input until valid input
def account_menu():
    while True:
        print("Account Actions:\n"
              "    Deposit\n"
              "    Withdraw\n"
              "    History\n"
              "    Logout")
        user_input = input("Input: ").lower()
        action = parse_account_menu(user_input)
        if not action == 4:
            return action


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
