import json
import random
from hashlib import sha256

# I hate this
resources = "../../../../resources/"

ALPHABET = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

def create_account_attempt(info):
    account_info = info.split()

    try:
        with open(resources+"loginaccounts.json", 'r') as f:
            data = json.load(f)

            for acc in data:
                if acc["username"] == account_info[0]:
                    print("Username is unavailable")
                    f.close()
                    return 0

        print("Username available")
        with open(resources+"loginaccounts.json", 'w') as f:
            salt = ''.join(random.choice(ALPHABET) for i in range(16))
            salt_n_hashed = sha256((account_info[1] + salt).encode('ascii')).hexdigest()
            data.append({"username": account_info[0], "salt": salt, "password": salt_n_hashed})
            json.dump(data, f, indent= 4)
            f.close()
            return 1

    except FileNotFoundError:
        print("File loginaccounts.json is missing.")
        return 0
