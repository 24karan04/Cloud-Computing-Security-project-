import json
import hashlib

USER_FILE = "data/users.json"

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def register_user(username, password):
    try:
        with open(USER_FILE, "r") as f:
            users = json.load(f)
    except:
        users = {}

    if username in users:
        return "User already exists"

    users[username] = hash_password(password)

    with open(USER_FILE, "w") as f:
        json.dump(users, f)

    return "User registered successfully"

def login_user(username, password):
    try:
        with open(USER_FILE, "r") as f:
            users = json.load(f)
    except:
        return "No users registered"

    if username not in users:
        return "User not found"

    if users[username] == hash_password(password):
        return "Login successful"
    else:
        return "Invalid password"