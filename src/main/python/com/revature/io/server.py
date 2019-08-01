import socket

def start_server():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_address = ('localhost', 10000)
    sock.bind(server_address)

    sock.listen(1)

    while True:
        connection, client_address = sock.accept()
        try:
            print('Connection from', client_address)

            # Receive the data in small chunks and retransmit it
            while True:
                data = connection.recv(1024).decode()
                if data == "exit":
                    print("Exiting")
                    break
                elif data:
                    print("Recieved: " + data)
                    connection.send(("Recieved: " + data).encode())
                else:
                    print('No data from', client_address)
                    break

        finally:
            print("Disconnected")
            connection.close()

start_server()