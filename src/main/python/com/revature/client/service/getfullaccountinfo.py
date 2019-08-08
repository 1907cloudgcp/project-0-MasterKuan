import json
from service.connection import send_info


def get_all_service(session):
    reply = send_info("getall", session)
    flag = reply[0]
    answer = reply[1]

    if flag == 0:
        print(answer)
        return 0

    account = json.loads(answer)
    for key in account:
        if key == "Balance":
            print("Balance: ${}".format(account[key]))
        elif key == "Transactions":
            if not account[key]:
                print("No transactions have been made yet")
            for t in account[key]:
                print("{}: ${}".format(t[0], t[1]))
        else:
            print("{}: {}".format(key, account[key]))
    return 1
