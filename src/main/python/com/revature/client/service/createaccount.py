from hashlib import sha256
from service.connection import send_info


def create_new_account():
    first_name = get_non_blank("First name")
    last_name = get_non_blank("Last name")

    while True:
        username = get_non_blank("Username")
        password = get_non_blank("Password")

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


def get_non_blank(field):
    while True:
        answer = input("{}: ".format(field))
        if answer == "":
            print("No input recieved for {}".format(field))
        else:
            return answer
