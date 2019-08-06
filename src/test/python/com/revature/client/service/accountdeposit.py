from .connection import send_info


def deposit_service(session):
    deposit_amount = get_amount()

    if deposit_amount > 0:
        reply = send_info("deposit", "{} {}".format(session, deposit_amount))
        flag = reply[0]
        answer = reply[1]

        print(answer)
        if flag == 0:
            return 0
        return 1
    return 0


def get_amount():
    amount = input("Deposit amount: ")
    try:
        val = float(amount)
        if val <= 0:
            print("Cannot deposit ${0:.2f}".format(val))
            return 0
        return val
    except ValueError:
        print("Incorrect amount format")
        return 0
