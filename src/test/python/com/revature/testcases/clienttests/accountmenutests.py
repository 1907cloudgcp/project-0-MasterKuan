def run_account_menu_tests():
    assert (parse_account_menu("l"), 0), "Should return 0"
    assert (parse_account_menu("deposit"), 1), "Should return 1"
    assert (parse_account_menu("withdraw"), 2), "Should return 2"
    assert (parse_account_menu("WItHDRAW"), 2), "Should return 2"
    assert (parse_account_menu("balance"), 3), "Should return 3"
    assert (parse_account_menu("4"), 4), "Should return 4"
    assert (parse_account_menu("5"), 5), "Should return 5"
    assert (parse_account_menu("login"), 999), "Should return 999"
    assert (parse_account_menu(53215), 0), "Should return 999"
    assert (parse_account_menu("loGOuT"), 0), "Should return 0"
    assert (parse_account_menu("2"), 2), "Should return 2"


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
