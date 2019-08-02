import pickle

server = None


def withdraw_connect_server(sock):
    global server
    server = sock


def withdraw_service(session):
    withdraw_amount = get_amount()
    if withdraw_amount > 0:
        success = send_info("{} {}".format(session, withdraw_amount))
        if success:
            print("Successfully withdrew ${0:.2f}".format(withdraw_amount))
            return 1
        else:
            print("Insufficient balance to withdraw")
            return 0
    else:
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


def send_info(info):
    deposit_info = pickle.dumps(("withdraw", info))
    server.sendall(deposit_info)
    success = server.recv(1024)
    return int(success.decode('utf8'))
