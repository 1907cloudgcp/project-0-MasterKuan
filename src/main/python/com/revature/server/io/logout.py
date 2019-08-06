import logging
from .bankdatalookup import *


def logout_attempt(info):
    data = info.split()
    account_number = int(data[0])
    session_token = data[1]
    logger = logging.getLogger(__name__)

    login_file = read_file(resources+"loginaccounts.json")
    if login_file:
        login_account = find_login_session(login_file, account_number, session_token)
        if login_account:
            # Reset session token to none
            login_account["session"] = ""
            try:
                with open(resources+"loginaccounts.json", 'w') as f:
                    json.dump(login_file, f, indent=4)
                logger.info("Logout successful. Account: #{}".format(account_number))
                return (1, "Successfully logged out")
            except FileNotFoundError:
                logger.critical("File loginaccounts.json is not found")
                return (0, "Server error, please contact support")
        else:
            logger.error("Could not access login account. Account: #{}, Session: {}".format(account_number,
                                                                                             session_token))
            return (0, "Could not access account, contact support")
    else:
        logger.critical("File loginaccounts.json is missing.")
        return (0, "Server error, please contact support")

