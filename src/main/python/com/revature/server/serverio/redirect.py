import logging
from .accountcreator import create_account_attempt
from .balance import view_balance
from .deposit import deposit_to_account
from .getallinfo import get_all_info
from .loginauthenticator import login_attempt
from .logout import logout_attempt
from .transactions import view_transactions
from .transferfunds import transfer_funds
from .withdraw import withdraw_from_account
from .changepassword import change_password


def process_data(data):
    flag = data[0]
    logger = logging.getLogger("Server")
    output = (0, "Redirect error")

    if flag == "login":
        output = login_attempt(data[1])
    elif flag == "create":
        output = create_account_attempt(data[1])
    elif flag == "deposit":
        output = deposit_to_account(data[1])
    elif flag == "withdraw":
        output = withdraw_from_account(data[1])
    elif flag == "balance":
        output = view_balance(data[1])
    elif flag == "transactions":
        output = view_transactions(data[1])
    elif flag == "logout":
        output = logout_attempt(data[1])
    elif flag == "getall":
        output = get_all_info(data[1])
    elif flag == "transfer":
        output = transfer_funds(data[1])
    elif flag == "changepass":
        output = change_password(data[1])
    else:
        logger.warning("Unhandled flag. Flag: {}, Redirect Data: {}".format(flag, data[1]))
        output = (0, "Server error, please contact support")

    return output
