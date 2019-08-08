from service.connection import send_info


def transfer_service(session):
    transfer_amount = get_amount()
    account_number = get_account()

    if transfer_amount > 0 and account_number > 0:
        reply = send_info("transfer", "{} {} {}".format(session, account_number, transfer_amount))
        flag = reply[0]
        answer = reply[1]

        print(answer)
        if flag == 0:
            return 0
        return 1
    return 0


def get_amount():
    amount = input("Transfer amount: ")
    try:
        val = float(amount)
        if val <= 0:
            print("Cannot transfer ${0:.2f}".format(val))
            return 0
        return val
    except ValueError:
        print("Incorrect amount format")
        return 0


def get_account():
    account = input("Account number of destination: ")
    try:
        val = int(account)
        if val <= 0:
            print("Account number incorrect")
            return 0
        return val
    except ValueError:
        print("Incorrect account number format")
        return 0
