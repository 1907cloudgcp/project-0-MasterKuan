import pickle
import socket

HOST = "localhost"
PORT = 6969
sock = None


def connect():
    global sock
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        server_address = (HOST, PORT)
        print("Connecting to {} port {}".format(*server_address))
        sock.connect(server_address)
        return sock
    except:
        print("Cannot connect to server")
        return 0


def send_info(tag, info):
    new_account_info = pickle.dumps((tag, info))
    sock.sendall(new_account_info)
    reply = sock.recv(1024)
    return pickle.loads(reply)
