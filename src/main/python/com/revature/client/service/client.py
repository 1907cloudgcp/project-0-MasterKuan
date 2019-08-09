from multiprocessing.connection import Client

HOST = "localhost"
PORT = 6969
sock = None


def connect():
    global sock
    global HOST
    global PORT

    try:
        server_address = (HOST, PORT)
        sock = Client(server_address)
        print("Connecting to {} port {}".format(*server_address))
        # sock.connect(server_address)
        return sock
    except:
        print("Cannot connect to server")
        return 0


def send_info(tag, info):
    if tag == "":
        sock.send("")
    else:
        packet = (tag, info)
        sock.send(packet)
        reply = sock.recv()
        return reply
