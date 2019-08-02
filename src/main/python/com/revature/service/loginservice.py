from hashlib import sha256
import pickle

server = None


def login_connect_server(sock):
    global server
    server = sock


def login_service():
    username = input("Username: ")
    password = input("Password: ")

    hashed_password = sha256(password.encode('ascii')).hexdigest()
    session = send_info(username + " " + hashed_password)

    if session == "0":
        print("Login unsuccessful")
        return 0
    else:
        print("Login successful")
        return session


def send_info(info):
    login_package = pickle.dumps(("login", info))
    server.sendall(login_package)
    session = server.recv(1024)
    return session.decode()
