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
    success = send_info(username + " " + hashed_password)

    if success:
        print("Login successful")
        return 1
    else:
        print("Login unsuccessful")
        return 0


def send_info(info):
    login_package = pickle.dumps(("login", info))
    server.sendall(login_package)
    success = server.recv(1024)
    return int(success.decode('utf8'))
