from .bankdatalookup import *


def transfer_funds(info):
    data = info.split()
    account_number = int(data[0])
    session_token = data[1]
    deposit_account_number = int(data[2])
    transfer_amount = float(data[3])

    logger = logging.getLogger(__name__)

    if session_token == "":
        logger.warning("User sent empty session token")
        return (0, "Session error, please contact support")

    login_file = read_file(get_file_directory()+"loginaccounts.json")
    if not login_file:
        logger.critical("loginaccounts.json file not found")
        return (0, "Server error, please contact support")

    account_file = read_file(get_file_directory()+"bankaccounts.json")
    if not account_file:
        logger.critical("account_file.json file not found")
        return (0, "Server error, please contact support")

    if find_login_session(login_file, account_number, session_token):
        user_account = find_bank_account(account_file, account_number, session_token)
        if user_account:
            found = False
            deposit_account = None
            for deposit_account in account_file:
                if deposit_account["account"] == deposit_account_number:
                    found = True
                    break
            if not found:
                logger.error("Bank account not found. Account: #{}".format(deposit_account_number))
                return (0, "Transfer bank account not found.")

            try:
                user_balance = float(user_account["balance"])
            except ValueError:
                logger.error("Could not convert account balance. Account: #{}, Balance: {}".format(
                    deposit_account_number, deposit_account["balance"]))
                return (0, "Server error, please contact support")

            try:
                deposit_balance = float(deposit_account["balance"])
            except ValueError:
                logger.error("Could not convert balance to float: Balance: {}".format(user_account["balance"]))
                return (0, "Server error, please contact support")

            if transfer_amount > user_balance:
                logger.info("Insufficient funds. Account: #{}, Balance: {}, Amount: ${}".format(account_number,
                                                                                                user_balance,
                                                                                                transfer_amount))
                return (0, "Insufficient funds to transfer")

            user_balance -= transfer_amount
            user_account["balance"] = "{0:.2f}".format(user_balance)
            user_account["transactions"].append(["Transferred out", "{0:.2f}".format(transfer_amount)])

            deposit_balance += transfer_amount
            deposit_account["balance"] = "{0:.2f}".format(deposit_balance)
            deposit_account["transactions"].append(["Transferred in", "{0:.2f}".format(transfer_amount)])

            try:
                with open(get_file_directory() + "bankaccounts.json", 'w') as account_write:
                    json.dump(account_file, account_write, indent=4)
                return (1, "Transfer completed.")
            except FileNotFoundError:
                logger.critical("File bankaccounts.json is not found")
                return (0, "Server error, please contact support")

        else:
            logger.error("User account not found. Account: #{}".format(account_number))
            return (0, "User account not found, please contact support")

    logger.error("Login session error. Account: #{}, Session Token: {}".format(account_number, session_token))
    return (0, "Session error, please contact support")
