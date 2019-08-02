import json
import random
from hashlib import sha256

resources = "../../../../resources/"
ALPHANUMERIC = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"


def login_attempt(info):
    login_info = info.split()
    try:
        with open(resources+"loginaccounts.json", 'r') as f:
            data = json.load(f)
            for acc in data:
                if acc["username"] == login_info[0]:
                    if sha256((login_info[1] + acc["salt"]).encode('ascii')).hexdigest() == acc["password"]:
                        print("Login success")
                        session_token = ''.join(random.choice(ALPHANUMERIC) for i in range(16))
                        set_session(acc["account"], session_token)
                        session = str(acc["account"]) + " " + session_token
                        return session
                    else:
                        print("Incorrect password")

                        return "0"
            print("Account doesn't exist")
        return "0"
    except FileNotFoundError:
        print("File loginaccounts.json is missing.")
        return "0"


def set_session(account_num, token):
    with open(resources+"bankaccounts.json", 'r') as bank_read:
        bank = json.load(bank_read)

    for acc in bank:
        if acc["account"] == account_num:
            acc["session"] = token

    with open(resources+"bankaccounts.json", 'w') as bank_write:
        json.dump(bank, bank_write, indent=4)
