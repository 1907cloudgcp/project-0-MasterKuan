import logging
from bankdatalookup import *

resources = "../../../../resources/"


def withdraw_from_account(info):
    user_data = info.split()
    account_number = int(user_data[0])
    session_token = user_data[1]
    withdraw_amount = float(user_data[2])
    logger = logging.getLogger(__name__)

    if session_token == "":
        logger.warning("User sent empty session token")
        return (0, "Session error, please contact support")

    login_file = read_file(resources + "loginaccounts.json")
    if not login_file:
        logger.critical("loginaccounts.json file not found")
        return (0, "Server error, please contact support")

    account_file = read_file(resources + "bankaccounts.json")
    if not account_file:
        logger.critical("account_file.json file not found")
        return (0, "Server error, please contact support")

    if find_login_session(login_file, account_number, session_token):
        account = find_bank_account(account_file, account_number, session_token)
        if account:
            balance = float(account["balance"])
            if balance < withdraw_amount or balance == 0:
                logger.info("Insufficient funds to withdraw from. Balance: ${0:.2f}, Requested: ${1}".format(
                    balance, withdraw_amount))
                return (0, "Insufficient funds to withdraw from")
            balance -= withdraw_amount
            account["balance"] = "{0:.2f}".format(balance)
            account["transactions"].append(["Withdraw", "{0:.2f}".format(withdraw_amount)])

            try:
                with open(resources+"bankaccounts.json", 'w') as account_write:
                    json.dump(account_file, account_write, indent=4)
            except FileNotFoundError:
                logger.critical("File bankaccounts.json is not found")
                return (0, "Server error, please contact support")

            # SUSPICIOUS AMOUNT WITHDREW
            if withdraw_amount >= 1000:
                logger.info("Suspicious amount withdrew\n"
                             "Account: {0}\n"
                             "Amount: ${1:.2f}".format(account_number, balance))
            logger.info("Withdrew successfully. Account: #{0}, Amount: ${1:.2f}".format(account_number,
                                                                                         withdraw_amount))
            return (1, "Withdrew successfully.\nNew balance is ${}".format(balance))

    logger.error("Login session error. Account: #{}, Session Token: {}".format(account_number, session_token))
    return (0, "Session error, please contact support")
