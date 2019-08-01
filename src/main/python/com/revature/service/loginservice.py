from hashlib import sha256

connection = None


def connect_server(sock):
    global connection
    connection = sock


def login(username, password):
    hashed_password = sha256(password.encode('ascii')).hexdigest()
    print("User: " + username)
    print("Hashed password: " + hashed_password)
    send_info(username, hashed_password)


def send_info(username, password):
    connection.sendall(username.encode())

    #Confirm username recieved
    print(connection.recv(1024).decode())

    connection.sendall(password.encode())

    #Confirm password recieved
    print(connection.recv(1024).decode())