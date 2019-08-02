import pickle

server = None


def transaction_connect_server(sock):
    global server
    server = sock


def transaction_service(session):
    transactions = send_info(session)

    if transactions == []:
        print("No transactions have been made yet")
    else:
        try:
            for t in transactions:
                print("{0}: ${1:.2f}".format(t[0], float(t[1])))
        except ValueError:
            print("Error in viewing transaction history")


def send_info(info):
    transactions_info = pickle.dumps(("transactions", info))
    server.sendall(transactions_info)
    transactions = server.recv(1024)
    return pickle.loads(transactions)
