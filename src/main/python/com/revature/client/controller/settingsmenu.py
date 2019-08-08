HIDE = 0


# Run until exit
def run_settings_menu():
    while True:
        print("Hide is " + str(HIDE))
        action = settings_menu()
        if action == 0:
            return 0
        elif action == 1:
            change_hide_password()


def get_hide():
    global HIDE
    return HIDE


# Get user input until valid input
def settings_menu():
    while True:
        print("Main Actions:\n"
              "    1) Hide password\n"
              "    0) Exit")

        user_input = input("Input: ").lower()
        action = parse_settings(user_input)
        if not action == 999:
            return action


def parse_settings(action):
    if action == "exit" or action == "0" or action == "e":
        print("\nExiting")
        return 0
    elif action == "hide" or action == "1" or action == "h":
        return 1
    else:
        print("\nInput was not recognized.")
        return 999


def answer(display):
    while True:
        action = input(display + " (y/n)?: ").lower()
        if action == "y" or action == "yes":
            return 1
        elif action == "n" or action == "no":
            return 0
        else:
            print("Invalid input")


def change_hide_password():
    global HIDE

    if HIDE:
        print("Currently, typing a password is being HIDDEN")
        if answer("Show password while typing "):
            HIDE = 0
    else:
        print("Currently, typing a password is being SHOWN")
        if answer("Hide password while typing "):
            HIDE = 1
