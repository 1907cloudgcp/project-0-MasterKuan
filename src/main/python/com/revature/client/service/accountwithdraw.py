from service.client import send_info


def withdraw_service(session):
    withdraw_amount = get_amount()
    if withdraw_amount > 0:
        reply = send_info("withdraw", "{} {}".format(session, withdraw_amount))
        flag = reply[0]
        answer = reply[1]

        print(answer)
        if flag == 0:
            return 0
        return 1
    return 0


def get_amount():
    amount = input("Withdraw amount: ")
    try:
        val = float(amount)
        if val <= 0:
            print("Cannot withdraw ${0:.2f}".format(val))
            return 0
        return val
    except ValueError:
        print("Incorrect amount format")
        return 0
