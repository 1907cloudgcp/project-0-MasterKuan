import pickle

server = None


def balance_connect_server(sock):
    global server
    server = sock


def balance_service(session):
    bal = send_info(session)
    try:
        balance = float(bal)

        if balance < 0:
            print("Error in getting balance")
        else:
            print("Your current balance is ${0:.2f}".format(balance))
    except ValueError:
        print("Error in converting balance")


def send_info(info):
    balance_info = pickle.dumps(("balance", info))
    server.sendall(balance_info)
    success = server.recv(1024)
    return success.decode('utf8')
