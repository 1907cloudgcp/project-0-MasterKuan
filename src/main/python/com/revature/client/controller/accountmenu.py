from client.service.accountdeposit import deposit_service
from client.service.accountwithdraw import withdraw_service
from client.service.viewbalance import balance_service
from client.service.viewtransactions import transaction_service
from client.service.logoutservice import logout_service
from client.service.getfullaccountinfo import get_all_service


# Run until logout
def run_account_menu(session):
    while True:
        action = account_menu()
        if action == 0:
            logout_service(session)
            return 1
        elif action == 1:
            deposit_service(session)
        elif action == 2:
            withdraw_service(session)
        elif action == 3:
            balance_service(session)
        elif action == 4:
            transaction_service(session)
        elif action == 5:
            get_all_service(session)


# Get user input until valid input
def account_menu():
    while True:
        print("Account Actions:\n"
              "    1) Deposit\n"
              "    2) Withdraw\n"
              "    3) Balance\n"
              "    4) Transactions\n"
              "    5) Full account details\n"
              "    0) Logout")
        user_input = input("Input: ").lower()
        action = parse_account_menu(user_input)
        if not action == 999:
            return action


def parse_account_menu(action):
    if action == "logout" or action == "0" or action == "l":
        print("\nLogging out")
        return 0
    elif action == "deposit" or action == "1" or action == "d":
        print("\nDepositing")
        return 1
    elif action == "withdraw" or action == "2" or action == "w":
        print("\nWithdrawing")
        return 2
    elif action == "balance" or action == "3" or action == "b":
        print("\nViewing balance")
        return 3
    elif action == "transactions" or action == "4" or action == "t":
        print("\nViewing transactions history")
        return 4
    elif action == "full" or action == "5" or action == "f":
        print("\nViewing full account details")
        return 5
    else:
        print("\nInput was not recognized.")
        return 999
