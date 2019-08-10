import logging.handlers
from multiprocessing.connection import Listener
from serverio.redirect import *

HOST = "localhost"
PORT = 4334


def client_configurer(queue):
    handler = logging.handlers.QueueHandler(queue)
    logger = logging.getLogger("Server")
    logger.addHandler(handler)
    logger.setLevel(logging.DEBUG)


def client_handler(sock, listener, queue, configurer):
    configurer(queue)
    logger = logging.getLogger("Server")
    try:
        logger.info("Connection from {}".format(listener.address))
        while True:
            packet = sock.recv()
            if packet:
                data = process_data(packet)
                sock.send(data)
            else:
                logger.info("No data from {}".format(listener.address))
                break
    finally:
        logger.info("Client {} disconnected".format(listener.address))
        sock.close()


def run_server(queue):
    logger = logging.getLogger("Server")
    logger.info("Server started up")

    server_address = (HOST, PORT)
    listener = Listener(server_address)

    sock = listener.accept()
    client_handler(sock, listener, queue, client_configurer)
    logger.info("Server shutting down")
    sock.close()
