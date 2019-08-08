from controller.accountmenu import *
from controller.frontmenu import *


# If login is successful from front menu, run account menu
def run_app():
    while True:
        session = run_front_menu()
        if session:
            run_account_menu(session)
        else:
            break
