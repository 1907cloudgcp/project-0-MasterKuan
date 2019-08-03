from hashlib import sha256
from service.client import send_info


def create_new_account():
    while True:
        username = input("Username: ")
        password = input("Password: ")

        hashed_password = sha256(password.encode('ascii')).hexdigest()
        reply = send_info("create", username + " " + hashed_password)
        flag = reply[0]
        answer = reply[1]

        print(answer)
        if flag == 0:
            return 0
        elif flag == -1:
            print("Username is already in use")
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
