import json

resources = "../../../../resources/"


def deposit_to_account(info):
    data = info.split()
    account_number = int(data[0])
    session_token = data[1]
    deposit_amount = float(data[2])

    if session_token == "":
        return 0

    with open(resources+"bankaccounts.json", 'r') as account_read:
        bank = json.load(account_read)

    for acc in bank:
        if acc["account"] == account_number and acc["session"] == session_token:
            balance = float(acc["balance"])
            balance += deposit_amount
            acc["balance"] = "{0:.2f}".format(balance)
            acc["transactions"].append(["Deposit", "{0:.2f}".format(deposit_amount)])

            with open(resources + "bankaccounts.json", 'w') as account_write:
                json.dump(bank, account_write, indent=4)
            return 1

    return 0
