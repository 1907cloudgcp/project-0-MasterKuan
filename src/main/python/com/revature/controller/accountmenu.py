from service.accountdeposit import deposit_service
from service.accountwithdraw import withdraw_service
from service.viewbalance import balance_service
from service.viewtransactions import transaction_service


# Run until logout
def run_account_menu(session):

    while True:
        action = account_menu()
        if action == 0:
            return 0
        elif action == 1:
            deposit_service(session)
        elif action == 2:
            withdraw_service(session)
        elif action == 3:
            balance_service(session)
        elif action == 4:
            transaction_service(session)


# Get user input until valid input
def account_menu():
    while True:
        print("Account Actions:\n"
              "    Deposit\n"
              "    Withdraw\n"
              "    Balance\n"
              "    Transactions\n"
              "    Logout")
        user_input = input("Input: ").lower()
        action = parse_account_menu(user_input)
        if not action == 5:
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
    elif action == "balance":
        print("\nViewing balance")
        return 3
    elif action == "transactions":
        print("\nViewing transactions history")
        return 4
    else:
        print("\nInput was not recognized.")
        return 5
