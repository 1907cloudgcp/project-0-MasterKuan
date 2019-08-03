import socket
from redirect import *

PORT = 10000


def main():
    run_server()


def run_server():
    global PORT

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', PORT)
    sock.bind(server_address)
    sock.listen(1)

    while True:
        connection, client_address = sock.accept()
        try:
            print('Connection from', client_address)
            while True:
                data = pickle.loads(connection.recv(1024))
                if data:
                    answer = process_data(data)
                    connection.sendall(answer)
                else:
                    print('No data from', client_address)
                    break

        finally:
            print("Client disconnected")
            connection.close()
            break

    print("Server shutting down")
    sock.close()





if __name__ == '__main__':
    main()
