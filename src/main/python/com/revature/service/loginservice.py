from hashlib import sha256

def login(username, password):
    hashed_password = sha256(password.encode('ascii')).hexdigest()
    print("User: " + username)
    print("Hashed password: " + hashed_password)