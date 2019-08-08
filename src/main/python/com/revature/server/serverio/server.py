import socket
from serverio.redirect import *

PORT = 10000


def run_server():
    global PORT
    logger = logging.getLogger(__name__)
    logger.info("Server started up")

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ("localhost", PORT)
    sock.bind(server_address)
    sock.listen(1)

    while True:
        connection, client_address = sock.accept()
        try:
            logger.info("Connection from {}".format(client_address))
            while True:
                data = pickle.loads(connection.recv(1024))
                if data:
                    answer = process_data(data)
                    connection.sendall(answer)
                else:
                    logger.info("No data from {}".format(client_address))
                    break

        finally:
            logger.info("Client disconnected")
            connection.close()
            break

    logger.info("Server shutting down")
    sock.close()