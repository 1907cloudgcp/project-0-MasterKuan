from service.createaccount import *
from service.loginservice import *


# Run until exit or logged in
def run_front_menu():
    while True:
        action = front_menu()
        if action == 0:
            return 0
        elif action == 1:
            create_new_account()
        elif action == 2:
            session = login_service()
            if session:
                return session


# Get user input until valid input
def front_menu():
    while True:
        print("Main Actions:\n"
              "    Register\n"
              "    Login\n"
              "    Exit")

        user_input = input("Input: ").lower()
        action = parse(user_input)
        if not action == 3:
            return action


def parse(action):
    if action == "exit":
        print("\nExiting")
        return 0
    elif action == "register" :
        print("\nRegistering")
        return 1
    elif action == "login":
        print("\nLogging in")
        return 2
    else:
        print("\nInput was not recognized.")
        return 3