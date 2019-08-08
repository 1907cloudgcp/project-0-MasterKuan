from .bankdatalookup import *


def view_transactions(info):
    user_data = info.split()
    account_number = int(user_data[0])
    session_token = user_data[1]
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
        account = find_bank_account(account_file, account_number, session_token)
        if account:
            logger.info("Account transactions shown. Account: #{}".format(account_number))
            return (1, account["transactions"])
        else:
            logger.error("Account not found. Account: #{}".format(account_number))
            return (0, "Account not found, please contact support")

    logger.error("Login session error. Account: #{}, Session Token: {}".format(account_number, session_token))
    return (0, "Session error, please contact support")
