import random
from hashlib import sha256
from .bankdatalookup import *

ALPHANUMERIC = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"


def create_account_attempt(info):
    data = info.split()
    first_name = data[0]
    last_name = data[1]
    username = data[2]
    password = data[3]
    logger = logging.getLogger("Server")

    login_file = read_file(get_file_directory() + "loginaccounts.json")

    if login_file or login_file == []:
        for acc in login_file:
            if acc["username"] == username:
                logger.info("Username is unavailable. Username: {}".format(username))
                return (-1, "Username is unavailable")

        logger.info("{} username available".format(username))
        try:
            with open(get_file_directory() + "loginaccounts.json", 'w') as accounts_write:
                if login_file == []:
                    account_num = 1
                else:
                    account_num = login_file[-1]["account"] + 1
                salt = ''.join(random.choice(ALPHANUMERIC) for i in range(16))
                salt_n_hashed = sha256((password + salt).encode('ascii')).hexdigest()
                login_file.append({"account": account_num,
                                   "firstname": first_name,
                                   "lastname": last_name,
                                   "username": username,
                                   "salt": salt,
                                   "password": salt_n_hashed,
                                   "attempts": 0,
                                   "session": ""})
                json.dump(login_file, accounts_write, indent=4)
        except FileNotFoundError:
            logger.critical("File loginaccounts.json is not found")
            return (0, "Server error, please contact support")

        account_file = read_file(get_file_directory() + "bankaccounts.json")
        if account_file or account_file == []:
            account_file.append({"account": account_num, "firstname": first_name, "lastname": last_name,
                                 "balance": "0.00", "transactions": [], "session": ""})
        else:
            logger.critical("File bankaccounts.json is not found")
            return (0, "Server error, please contact support")

        try:
            with open(get_file_directory() + "bankaccounts.json", 'w') as bank_write:
                json.dump(account_file, bank_write, indent=4)
            logger.info("New account created: Account: #{}, Username: {}".format(account_num, username))
            return (1, "New account made, login to continue")
        except FileNotFoundError:
            logger.critical("File bankaccounts.json is not found")
            return (0, "Server error, please contact support")
    else:
        logger.critical("File loginaccounts.json is missing.")
        return (0, "Server error, please contact support")
