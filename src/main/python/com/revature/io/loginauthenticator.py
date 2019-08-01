import re
import json
from main.resources import *

def loginlookup(username, password):
    with open("useraccounts.json", "r") as file:
        lookup = username + " " + password
        for acc in file:
            if re.search(lookup, acc):
                return 1
        return 0