import random
from hashlib import sha256
from .bankdatalookup import *

ALPHANUMERIC = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"


def change_password(info):
    data = info.split()
    account_number = int(data[0])
    session_token = data[1]
    old_password = data[2]
    new_password = data[3]
    logger = logging.getLogger("Server")

    if session_token == "":
        logger.warning("User sent empty session token")
        return (0, "Session error, please contact support")

    login_file = read_file(get_file_directory() + "loginaccounts.json")
    if not login_file:
        logger.critical("loginaccounts.json file not found")
        return (0, "Server error, please contact support")

    login_account = find_login_session(login_file, account_number, session_token)
    if login_account:
        if sha256((old_password + login_account["salt"]).encode('ascii')).hexdigest() == login_account["password"]:
            if old_password == new_password:
                return (0, "Old password and new passwords are the same")
            try:
                with open(get_file_directory() + "loginaccounts.json", 'w') as accounts_write:
                    salt = ''.join(random.choice(ALPHANUMERIC) for i in range(16))
                    salt_n_hashed = sha256((new_password + salt).encode('ascii')).hexdigest()
                    login_account["salt"] = salt
                    login_account["password"] = salt_n_hashed
                    json.dump(login_file, accounts_write, indent=4)
                logger.info("Changed password: Account: {}".format(login_account["account"]))
                return (1, "Password changed")
            except FileNotFoundError:
                logger.critical("File loginaccounts.json is not found")
                return (0, "Server error, please contact support")
        else:
            logger.info("Mismatched change password: Account: {}".format(login_account["account"]))
            return (0, "Password did not match")

    logger.error("Login session error. Account: #{}, Session Token: {}".format(account_number, session_token))
    return (0, "Session error, please contact support")
