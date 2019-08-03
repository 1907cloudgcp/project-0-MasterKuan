import json


def read_file(file_name):
    try:
        with open(file_name, 'r') as json_file:
            file = json.load(json_file)
        return file
    except FileNotFoundError:
        print("File {} is missing".format(file_name))
        return 0


def find_login_session(login_file, account_number, session_token):
    for login in login_file:
        if login["account"] == account_number:
            if login["session"] == session_token:
                return login
            else:
                print("Login session token error")
                return 0
    print("Login account not found")
    return 0


def find_bank_account(account_file, account_number, session_token):
    for account in account_file:
        if account["account"] == account_number:
            if account["session"] == session_token:
                return account
            else:
                print("Account session token error")
                return 0
    print("Account not found in bank")
    return 0
