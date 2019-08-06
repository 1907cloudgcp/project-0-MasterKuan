from error.customerrors import LargeDeposit
from .bankdatalookup import *


def deposit_to_account(info):
    user_data = info.split()
    account_number = int(user_data[0])
    session_token = user_data[1]
    deposit_amount = float(user_data[2])
    logger = logging.getLogger(__name__)

    if session_token == "":
        logger.warning("User sent empty session token")
        return (0, "Session error, please contact support")

    login_file = read_file(RESOURCES + "loginaccounts.json")
    if not login_file:
        logger.critical("loginaccounts.json file not found")
        return (0, "Server error, please contact support")

    account_file = read_file(RESOURCES + "bankaccounts.json")
    if not account_file:
        logger.critical("account_file.json file not found")
        return (0, "Server error, please contact support")

    if find_login_session(login_file, account_number, session_token):
        account = find_bank_account(account_file, account_number, session_token)
        if account:
            balance = float(account["balance"])

            # SUSPICIOUS AMOUNT DEPOSITED
            try:
                if deposit_amount >= 1000:
                    raise (LargeDeposit(account_number, deposit_amount, "Large deposit requested"))
                balance += deposit_amount
                account["balance"] = "{0:.2f}".format(balance)
                account["transactions"].append(["Deposit", "{0:.2f}".format(deposit_amount)])
                logger.info("Deposited successfully: Account #{0}, Amount ${1:.2f}".format(account_number,
                                                                                           deposit_amount))
                message = (1, "Deposited successfully.\nNew balance is ${}".format(balance))
            except LargeDeposit as error:
                logger.info(error.formatted_message())
                account["transactions"].append(["Pending Deposit", "{0:.2f}".format(deposit_amount)])
                message = (1, "Deposit request of ${0:.2f} is too large.\nPending for approval".format(deposit_amount))
            finally:
                try:
                    with open(RESOURCES + "bankaccounts.json", 'w') as account_write:
                        json.dump(account_file, account_write, indent=4)
                    return message
                except FileNotFoundError:
                    logger.critical("File bankaccounts.json is not found")
                    return (0, "Server error, please contact support")

    logger.error("Login session error. Account: #{}, Session Token: {}".format(account_number, session_token))
    return (0, "Session error, please contact support")
