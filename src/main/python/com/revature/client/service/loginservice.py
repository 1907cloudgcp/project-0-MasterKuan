from getpass import getpass
from hashlib import sha256
from service.client import send_info
from controller.settingsmenu import get_hide


def login_service():
    username = get_non_blank("Username", False)
    password = get_non_blank("Password", get_hide())

    hashed_password = sha256(password.encode('ascii')).hexdigest()
    reply = send_info("login", "{} {}".format(username, hashed_password))
    flag = reply[0]
    answer = reply[1]

    if flag == 0:
        print(answer)
        return 0
    return answer


def get_non_blank(field, hide):
    while True:
        if hide:
            answer = getpass("{}: ".format(field))
        else:
            answer = input("{}: ".format(field))

        if answer == "":
            print("No input recieved for {}".format(field))
        elif " " in answer:
            print("No spaces are allowed")
        else:
            return answer
