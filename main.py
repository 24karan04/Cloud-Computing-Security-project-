# ---------------- USERS ----------------
users = {}

def register_user(username, password):
    users[username] = password
    return f"User {username} registered!"

def login_user(username, password):
    if users.get(username) == password:
        return f"Welcome {username}!"
    return "Invalid login"

# ---------------- ENCRYPT / DECRYPT ----------------
def encrypt_file(file):
    return f"{file} encrypted successfully (demo)"

def decrypt_file(file):
    return f"{file} decrypted successfully (demo)"

# ---------------- FIREWALL ----------------
blocked_ips = set()

def block_ip(ip):
    blocked_ips.add(ip)
    return f"{ip} blocked!"

def check_ip(ip):
    if ip in blocked_ips:
        return f"{ip} is BLOCKED"
    return f"{ip} is ALLOWED"
