import json

resources = "../../../../resources/"


def view_balance(info):
    data = info.split()
    account_number = int(data[0])
    session_token = data[1]

    if session_token == "":
        return -1

    with open(resources+"bankaccounts.json", 'r') as account_read:
        bank = json.load(account_read)

    for acc in bank:
        if acc["account"] == account_number and acc["session"] == session_token:
            return acc["balance"]

    print("Error viewing balance")
    return -1
