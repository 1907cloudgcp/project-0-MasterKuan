from bankdatalookup import *

resources = "../../../../resources/"


def view_transactions(info):
    user_data = info.split()
    account_number = int(user_data[0])
    session_token = user_data[1]

    if session_token == "":
        print("Attempted to access non session active account")
        return (0, "Session error, please contact support")

    login_file = read_file(resources+"loginaccounts.json")
    if not login_file:
        print("loginaccounts.json file not found")
        return (0, "Server error, please contact support")

    account_file = read_file(resources+"bankaccounts.json")
    if not account_file:
        print("account_file.json file not found")
        return (0, "Server error, please contact support")

    if find_login_session(login_file, account_number, session_token):
        account = find_bank_account(account_file, account_number, session_token)
        if account:
            print("Account transactions shown")
            return (1, account["transactions"])
        else:
            print("Account not found")
            return (0, "Account not found, please contact support")

    print("Login session error")
    return (0, "Session error, please contact support")
