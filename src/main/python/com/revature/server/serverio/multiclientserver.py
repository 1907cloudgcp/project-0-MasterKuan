import logging.handlers
import multiprocessing
from multiprocessing.connection import Listener
from serverio.redirect import *


HOST = "localhost"
PORT = 6969


def client_configurer(queue):
    handler = logging.handlers.QueueHandler(queue)
    logger = logging.getLogger("Server")
    logger.addHandler(handler)
    logger.setLevel(logging.DEBUG)


def client_handler(sock, listener, queue, configurer):
    configurer(queue)
    logger = logging.getLogger("Server")

    try:
        logger.log(logging.INFO, "Connection from {}".format(listener.address))
        while True:
            packet = sock.recv()
            if packet:
                data = process_data(packet)
                sock.send(data)
            else:
                logger.info("No data from {}".format(listener.address))
                break
    finally:
        logger.info("Client disconnected")
        sock.close()


def run_server(queue):
    handler = logging.handlers.QueueHandler(queue)
    logger = logging.getLogger("Server")
    logger.addHandler(handler)
    logger.setLevel(logging.DEBUG)
    logger.info("Server started up")

    server_address = (HOST, PORT)
    listener = Listener(server_address)

    while True:
        sock = listener.accept()
        process = multiprocessing.Process(target=client_handler, args=(sock, listener, queue, client_configurer))
        process.daemon = True
        process.start()
