import json
import random
import logging
from hashlib import sha256
from .bankdatalookup import *

ALPHANUMERIC = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"


def login_attempt(info):
    user_data = info.split()
    username = user_data[0]
    password = user_data[1]
    logger = logging.getLogger(__name__)

    login_file = read_file(resources+"loginaccounts.json")

    if login_file:
        for login_account in login_file:
            if login_account["username"] == username:
                # Account locked
                if login_account["attempts"] > 5:
                    logger.warning("Account is locked. Account: #{}".format(login_account["account"]))
                    return (0, "Account is locked due to exceeding the number of incorrect attempts")

                # Check password match
                if sha256((password + login_account["salt"]).encode('ascii')).hexdigest() == login_account["password"]:
                    # Logged in already
                    if not login_account["session"] == "":
                        logger.warning("Account already logged in. Account: #{}".format(login_account["account"]))
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
                        logger.critial("File loginaccounts.json is missing")
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
                        logger.critical("File bankaccounts.json is missing")
                        return (0, "Server error, please contact support")

                    # Return account number and session token
                    session = "{} {}".format(str(login_account["account"]), session_token)
                    logger.info("Login successful. Account: #{}, Session: {}".format(login_account["account"],
                                                                                      session_token))
                    return (1, session)
                else:
                    logger.info("Incorrect password. Account: #{}".format(login_account["account"]))
                    login_account["attempts"] += 1
                    try:
                        with open(resources+"loginaccounts.json", 'w') as login_write:
                            json.dump(login_file, login_write, indent=4)
                    except FileNotFoundError:
                        logger.critical("File loginaccounts.json is missing")
                        return (0, "Server error, please contact support")
                    return (0, "Incorrect password")
        logger.warning("Account doesn't exist. Username: {}".format(username))
        return (0, "Account doesn't exist")
    else:
        logger.critical("Login file not found")
        return (0, "Server error, please contact support")
