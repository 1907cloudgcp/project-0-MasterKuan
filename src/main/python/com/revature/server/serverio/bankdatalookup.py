import json
import logging

RESOURCES = "resources/"


def set_file_directory(fd):
    global RESOURCES
    RESOURCES = fd


def get_file_directory():
    global RESOURCES
    return RESOURCES


def read_file(file_name):
    logger = logging.getLogger(__name__)
    try:
        with open(file_name, 'r') as json_file:
            file = json.load(json_file)
        return file
    except FileNotFoundError:
        logger.critical("File {} is missing".format(file_name))
        return 0


def find_login_session(login_file, account_number, session_token):
    logger = logging.getLogger(__name__)
    for login in login_file:
        if login["account"] == account_number:
            if login["session"] == session_token:
                return login
            else:
                logger.error("Login session token error. Account: #{}, Session Token: {}".format(account_number,
                                                                                                  session_token))
                return 0
    logger.error("Login account not found. Account: #{}".format(account_number))
    return 0


def find_bank_account(account_file, account_number, session_token):
    logger = logging.getLogger(__name__)
    for account in account_file:
        if account["account"] == account_number:
            if account["session"] == session_token:
                return account
            else:
                logger.error("Account session token error. Account: #{}, Session Token: {}".format(account_number,
                                                                                                    session_token))
                return 0
    logger.error("Bank account not found. Account: #{}".format(account_number))
    return 0
