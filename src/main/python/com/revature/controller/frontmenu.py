from service.createaccount import *
from service.loginservice import *
from controller.settingsmenu import run_settings_menu, get_hide


# Run until exit or logged in
def run_front_menu():
    while True:
        action = front_menu()
        if action == 0:
            return 0
        elif action == 1:
            create_new_account()
        elif action == 2:
            session = login_service(get_hide())
            if session:
                return session
        elif action == 3:
            run_settings_menu()


# Get user input until valid input
def front_menu():
    while True:
        print("Main Actions:\n"
              "    1) Register\n"
              "    2) Login\n"
              "    3) Settings\n"
              "    0) Exit")

        user_input = input("Input: ").lower()
        action = parse(user_input)
        if not action == 999:
            return action


def parse(action):
    if action == "exit" or action == "0" or action == "e":
        print("\nExiting")
        return 0
    elif action == "register" or action == "1" or action == "r":
        print("\nRegistering")
        return 1
    elif action == "login" or action == "2" or action == "l":
        print("\nLogging in")
        return 2
    elif action == "settings" or action == "3" or action == "s":
        print("\nView settings")
        return 3
    else:
        print("\nInput was not recognized.")
        return 999
