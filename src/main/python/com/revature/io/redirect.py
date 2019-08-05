import pickle
from loginauthenticator import login_attempt
from accountcreator import create_account_attempt
from deposit import deposit_to_account
from withdraw import withdraw_from_account
from balance import view_balance
from transactions import view_transactions
from logout import logout_attempt
from getallinfo import get_all_info


def process_data(data):
    flag = data[0]
    if flag == "login":
        output = login_attempt(data[1])
    elif flag == "create":
        output = create_account_attempt(data[1])
    elif flag == "deposit":
        output = deposit_to_account(data[1])
    elif flag == "withdraw":
        output = withdraw_from_account(data[1])
    elif flag == "balance":
        output = view_balance(data[1])
    elif flag == "transactions":
        output = view_transactions(data[1])
    elif flag == "logout":
        output = logout_attempt(data[1])
    elif flag == "getall":
        output = get_all_info(data[1])
    else:
        print("Unhandled flag")
        output = (0, "Server error, please contact support")

    return pickle.dumps(output)
