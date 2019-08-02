from hashlib import sha256
import pickle

server = None


def create_account_connect_server(sock):
    global server
    server = sock


def create_new_account():
    while True:
        username = input("Username: ")
        password = input("Password: ")

        hashed_password = sha256(password.encode('ascii')).hexdigest()
        success = send_info(username + " " + hashed_password)

        if success:
            print("Successfully created new account")
            return 1
        else:
            print("Username is already in use")
            while True:
                answer = input("Try again? (y/n): ").lower()
                if answer == "n":
                    return 0
                elif not answer == "y":
                    print("Not an answer")
                else:
                    break


def send_info(info):
    new_account_info = pickle.dumps(("create", info))
    server.sendall(new_account_info)
    success = server.recv(1024)
    return int(success.decode('utf8'))
