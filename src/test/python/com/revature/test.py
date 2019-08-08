#!/usr/bin/env python3

def main():
    run_account_menu_tests()
    get_all_service_test()


def get_all_service_test():
    assert (get_all_service((0, "Fail")) == 0), "Should print Fail and return 0"
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
    })) == 1), "Should print account information and return 1"


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


def run_account_menu_tests():
    assert (parse_account_menu("l") == 0), "Should return 0"
    assert (parse_account_menu("deposit") == 1), "Should return 1"
    assert (parse_account_menu("withdraw") == 2), "Should return 2"
    assert (parse_account_menu("balance") == 3), "Should return 3"
    assert (parse_account_menu("4") == 4), "Should return 4"
    assert (parse_account_menu("5") == 5), "Should return 5"
    assert (parse_account_menu("login") == 999), "Should return 999"
    assert (parse_account_menu(53215) == 999), "Should return 999"
    assert (parse_account_menu("2") == 2), "Should return 2"


def parse_account_menu(action):
    if action == "logout" or action == "0" or action == "l":
        print("\nLogging out")
        return 0
    elif action == "deposit" or action == "1" or action == "d":
        print("\nDepositing")
        return 1
    elif action == "withdraw" or action == "2" or action == "w":
        print("\nWithdrawing")
        return 2
    elif action == "balance" or action == "3" or action == "b":
        print("\nViewing balance")
        return 3
    elif action == "transactions" or action == "4" or action == "t":
        print("\nViewing transactions history")
        return 4
    elif action == "full" or action == "5" or action == "f":
        print("\nViewing full account details")
        return 5
    else:
        print("\nInput was not recognized.")
        return 999


if __name__ == '__main__':
    main()
