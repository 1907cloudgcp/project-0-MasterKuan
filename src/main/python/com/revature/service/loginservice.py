from hashlib import sha256
from main.python.com.revature.io.loginauthenticator import *

def login(username, password):
    success = loginlookup(username, sha256(password))
    if not success:
        print("Username and/or password do not match records.")
        return 0
    return success