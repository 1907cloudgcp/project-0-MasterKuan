import socket
import logging
import logging.config
import yaml
from redirect import *

PORT = 10000


def main():
    run_server()


def run_server():
    global PORT
    logger = logging.getLogger(__name__)

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
                    logger.info("No data from {}".format(client_address))
                    break

        finally:
            logger.info("Client disconnected")
            connection.close()
            break

    logger.info("Server shutting down")
    sock.close()


if __name__ == '__main__':
    logger = logging.getLogger(__name__)
    logging.basicConfig(level=logging.DEBUG, filename="../../../../resources/serverlog.log",
                        format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

    main()
