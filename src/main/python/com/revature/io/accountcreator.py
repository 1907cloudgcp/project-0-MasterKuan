import json
import random
from hashlib import sha256

resources = "../../../../resources/"
ALPHANUMERIC = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"


def create_account_attempt(info):
    account_info = info.split()

    try:
        with open(resources+"loginaccounts.json", 'r') as accounts_read:
            login_data = json.load(accounts_read)
            for acc in login_data:
                if acc["username"] == account_info[0]:
                    print("Username is unavailable")
                    return 0

        print("Username available")
        with open(resources+"loginaccounts.json", 'w') as accounts_write:
            account_num = login_data[-1]["account"] + 1
            salt = ''.join(random.choice(ALPHANUMERIC) for i in range(16))
            salt_n_hashed = sha256((account_info[1] + salt).encode('ascii')).hexdigest()
            login_data.append({"username": account_info[0], "salt": salt, "password": salt_n_hashed, "account": account_num})
            json.dump(login_data, accounts_write, indent=4)

        with open(resources+"bankaccounts.json", 'r') as bank_read:
            account_data = json.load(bank_read)

        with open(resources+"bankaccounts.json", 'w') as bank_write:
            account_data.append({"account": account_num, "balance": "0.00", "transactions": [], "session": ""})
            json.dump(account_data, bank_write, indent=4)
        return 1

    except FileNotFoundError:
        print("File loginaccounts.json is missing.")
        return 0
