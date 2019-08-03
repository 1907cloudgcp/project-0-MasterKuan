import json
import random
from hashlib import sha256
from bankdatalookup import read_file

resources = "../../../../resources/"
ALPHANUMERIC = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"


def login_attempt(info):
    user_data = info.split()
    username = user_data[0]
    password = user_data[1]

    login_file = read_file(resources+"loginaccounts.json")

    if login_file:
        for login_account in login_file:
            if login_account["username"] == username:
                # Account locked
                if login_account["attempts"] > 5:
                    print("Account is locked")
                    return (0, "Account is locked due to exceeding the number of incorrect attempts")

                # Check password match
                if sha256((password + login_account["salt"]).encode('ascii')).hexdigest() == login_account[
                    "password"]:
                    # Logged in already
                    if not login_account["session"] == "":
                        print("Account already logged in")
                        return (0, "Account is already logged in")

                    # Success
                    session_token = ''.join(random.choice(ALPHANUMERIC) for i in range(16))

                    # Write to login accounts the session token and reset attempts
                    login_account["session"] = session_token
                    login_account["attempts"] = 0
                    try:
                        with open(resources+"loginaccounts.json", 'w') as login_write:
                            json.dump(login_file, login_write, indent=4)
                    except FileNotFoundError:
                        print("File loginaccounts.json is missing")
                        return (0, "Server error, please contact support")

                    # Write to bank accounts the session token
                    bank_accounts = read_file(resources+"bankaccounts.json")
                    if bank_accounts:
                        for account in bank_accounts:
                            if account["account"] == login_account["account"]:
                                account["session"] = session_token
                    try:
                        with open(resources+"bankaccounts.json", 'w') as json_file:
                            json.dump(bank_accounts, json_file, indent=4)
                    except FileNotFoundError:
                        print("File bankaccounts.json is missing")
                        return (0, "Server error, please contact support")

                    # Return account number and session token
                    session = "{} {}".format(str(login_account["account"]), session_token)
                    print("Login successful")
                    return (1, session)
                else:
                    print("Incorrect password")
                    login_account["attempts"] += 1
                    try:
                        with open(resources+"loginaccounts.json", 'w') as login_write:
                            json.dump(login_file, login_write, indent=4)
                    except FileNotFoundError:
                        print("File loginaccounts.json is missing")
                        return (0, "Server error, please contact support")
                    return (0, "Incorrect password")
        print("Account doesn't exist")
        return (0, "Account doesn't exist")
    else:
        print("HELP")
        return (0, "Server error, please contact support")
