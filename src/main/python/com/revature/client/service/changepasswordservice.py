from getpass import getpass
from hashlib import sha256
from service.client import send_info
from controller.settingsmenu import get_hide


def password_service(session):
    hide = get_hide()
    old_password = get_non_blank("Current Password", hide)
    new_password = get_non_blank("New Password", hide)

    hashed_old = sha256(old_password.encode('ascii')).hexdigest()
    hashed_new = sha256(new_password.encode('ascii')).hexdigest()
    reply = send_info("changepass", "{} {} {}".format(session, hashed_old, hashed_new))

    flag = reply[0]
    answer = reply[1]

    print(answer)
    if flag == 0:
        return 0
    return 1


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
