import pickle

server = None


def deposit_connect_server(sock):
    global server
    server = sock


def deposit_service(session):
    deposit_amount = get_amount()
    if deposit_amount > 0:
        success = send_info("{} {}".format(session, deposit_amount))
        if success:
            print("Successfully deposited ${0:.2f}".format(deposit_amount))
            return 1
        else:
            print("Error in depositing")
            return 0
    else:
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


def send_info(info):
    deposit_info = pickle.dumps(("deposit", info))
    server.sendall(deposit_info)
    success = server.recv(1024)
    return int(success.decode('utf8'))
