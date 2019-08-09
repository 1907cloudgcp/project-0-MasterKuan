from getpass import getpass
from hashlib import sha256

from service.client import send_info


def login_service(hide):
    username = input("Username: ")
    if hide:
        password = getpass("Password: ")
    else:
        password = input("Password: ")

    hashed_password = sha256(password.encode('ascii')).hexdigest()
    reply = send_info("login", username + " " + hashed_password)
    flag = reply[0]
    answer = reply[1]

    if flag == 0:
        print(answer)
        return 0
    return answer
