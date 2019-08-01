import socket

def connect():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        server_address = ("localhost", 10000)
        print("Connecting to {} port {}".format(*server_address))
        sock.connect(server_address)
        return sock
    except:
        print("Cannot connect to server")
        return 0