import socket
import pickle
from loginauthenticator import login_attempt


def main():
    start_server()


def start_server():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_address = ('localhost', 10000)
    sock.bind(server_address)
    sock.listen(1)
    while True:
        connection, client_address = sock.accept()
        try:
            print('Connection from', client_address)
            while True:
                data = pickle.loads(connection.recv(1024))
                if data:
                    data_parse(connection, data)
                else:
                    print('No data from', client_address)
                    break

        finally:
            print("Disconnected")
            connection.close()
            break

    print("Shutting down")
    sock.close()


def data_parse(connection, data):
    flag = data[0]
    if flag == "login":
        success = login_attempt(data[1])
        connection.sendall(str(success).encode('utf8'))
    else:
        print("Unhandled flag")


if __name__ == '__main__':
    main()