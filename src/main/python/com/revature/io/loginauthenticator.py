import json
from hashlib import sha256

# I hate this
resources = "../../../../resources/"


def login_attempt(info):
    login_info = info.split()

    try:
        data = json.loads(open(resources+"loginaccounts.json").read())

        try:
            account = data[login_info[0]]
            if sha256((login_info[1]+account["salt"]).encode('ascii')).hexdigest() == account["password"]:
                print("Login success")
                return 1
            else:
                print("Incorrect password")
                return 0
        except KeyError:
            print("Account doesn't exist")
            return 0
    except FileNotFoundError:
        print("File loginaccounts.json is missing.")
        return 0