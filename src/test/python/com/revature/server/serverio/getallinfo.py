from .bankdatalookup import *


def get_all_info(info):
    data = info.split()
    account_number = int(data[0])
    session_token = data[1]
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
            account_info = json.dumps({"Account": account["account"], "First Name": account["firstname"],
                                       "Last Name": account["lastname"], "Balance": account["balance"],
                                       "Transactions": account["transactions"]})
            logger.info("Full account info requested. Account: #{}".format(account["account"]))
            return (1, account_info)
        else:
            logger.warning("Account not found. Account: #{}".format(account_number))
            return (0, "Account not found, please contact support")

    logger.error("Login session error. Account: #{}, Session Token: {}".format(account_number, session_token))
    return (0, "Session error, please contact support")
