from bankdatalookup import *

resources = "../../../../resources/"


def deposit_to_account(info):
    user_data = info.split()
    account_number = int(user_data[0])
    session_token = user_data[1]
    deposit_amount = float(user_data[2])

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
            balance = float(account["balance"])
            balance += deposit_amount
            account["balance"] = "{0:.2f}".format(balance)
            account["transactions"].append(["Deposit", "{0:.2f}".format(deposit_amount)])

            try:
                with open(resources+"bankaccounts.json", 'w') as account_write:
                    json.dump(account_file, account_write, indent=4)
            except FileNotFoundError:
                print("File bankaccounts.json is not found")
                return (0, "Server error, please contact support")

            # SUSPICIOUS AMOUNT DEPOSITED
            if deposit_amount >= 1000:
                print("Suspicious amount deposited\n"
                      "Account: {0}\n"
                      "Amount: ${1:.2f}".format(account_number, balance))
            print("Deposited successfully")
            return (1, "Deposited successfully.\nNew balance is ${}".format(balance))

    print("Login session error")
    return (0, "Session error, please contact support")
