from bankdatalookup import *

resources = "../../../../resources/"


def get_all_info(info):
    data = info.split()
    account_number = int(data[0])
    session_token = data[1]


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
            account_info = json.dumps({"Account": account["account"], "First Name": account["firstname"],
                                       "Last Name": account["lastname"], "Balance": account["balance"],
                                       "Transactions": account["transactions"]})
            print("Full account info for account #{} requested".format(account["account"]))
            return (1, account_info)
        else:
            print("Account not found")
            return (0, "Account not found, please contact support")

    print("Login session error")
    return (0, "Session error, please contact support")
