def get_all_service_test():
    assert (get_all_service((0, "Fail")), 0), "Should print Fail and return 0"
    assert (get_all_service((1, {
        "account": 1,
        "firstname": "Ryan",
        "lastname": "Kuan",
        "balance": "580.00",
        "transactions": [
            [
                "Deposit",
                "580.00"
            ]
        ]
    })), 1), "Should print account information and return 1"


def get_all_service(set_reply):
    reply = set_reply
    flag = reply[0]
    answer = reply[1]

    if flag == 0:
        print(answer)
        return 0

    account = answer
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