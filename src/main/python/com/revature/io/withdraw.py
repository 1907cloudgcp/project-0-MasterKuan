import json

resources = "../../../../resources/"


def withdraw_from_account(info):
    data = info.split()
    account_number = int(data[0])
    session_token = data[1]
    withdraw_amount = float(data[2])

    if session_token == "":
        return 0

    with open(resources+"bankaccounts.json", 'r') as account_read:
        bank = json.load(account_read)

    for acc in bank:
        if acc["account"] == account_number and acc["session"] == session_token:
            balance = float(acc["balance"])
            if balance < withdraw_amount:
                return 0
            balance -= withdraw_amount
            acc["balance"] = "{0:.2f}".format(balance)
            acc["transactions"].append(["Withdraw", "{0:.2f}".format(withdraw_amount)])

            with open(resources + "bankaccounts.json", 'w') as account_write:
                json.dump(bank, account_write, indent=4)
            return 1
        else:
            return 0
