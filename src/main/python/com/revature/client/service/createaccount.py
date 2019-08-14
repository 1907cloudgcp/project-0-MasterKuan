from hashlib import sha256
from getpass import getpass
from controller.settingsmenu import get_hide
from service.client import send_info


def create_new_account():
    first_name = get_non_blank("First name", False)
    last_name = get_non_blank("Last name", False)

    while True:
        username = get_non_blank("Username", False)
        password = get_non_blank("Password", get_hide())

        hashed_password = sha256(password.encode('ascii')).hexdigest()
        reply = send_info("create", "{} {} {} {}".format(first_name, last_name, username, hashed_password))
        flag = reply[0]
        answer = reply[1]

        print(answer)
        if flag == 0:
            return 0
        elif flag == -1:
            while True:
                answer = input("Try again? (y/n): ").lower()
                if answer == "n":
                    return 0
                elif not answer == "y":
                    print("Not an answer")
                else:
                    break
        else:
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
