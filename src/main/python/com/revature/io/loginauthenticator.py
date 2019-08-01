import json
from hashlib import sha256

# I hate this
login_accounts = "../../../../resources/loginaccounts.json"


def login_attempt(info):
    login_info = info.split()

    try:
        with open(login_accounts, 'r') as f:
            data = json.load(f)
            for acc in data:
                if acc["username"] == login_info[0]:
                    if sha256((login_info[1] + acc["salt"]).encode('ascii')).hexdigest() == acc["password"]:
                        print("Login success")
                        f.close()
                        return 1
                    else:
                        print("Incorrect password")
                        f.close()
                        return 0
            print("Account doesn't exist")
        return 0
    except FileNotFoundError:
        print("File loginaccounts.json is missing.")
        return 0