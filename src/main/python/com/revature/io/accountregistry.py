import re
import json

def register(username, password):
    if (check_existing(username + " " + password)):
        create_account()
        return 1
    else:
        return 0

def check_existing(new_acc):
    with open("useraccounts.json", "r+") as f:
        for acc in f:
            exists = bool (re.search(new_acc, acc))
            if exists:
                return 0
        f.write(new_acc)
        return 1

def create_account():
    print("TODO")