users = {}
blocked_ips = []


def register_user(username, password):
    users[username] = password
    return f"User {username} registered successfully!"


def login_user(username, password):
    if users.get(username) == password:
        return f"Welcome {username}!"
    return "Invalid login"


def encrypt_file(file):
    return f"{file} encrypted successfully (demo)"


def decrypt_file(file):
    return f"{file} decrypted successfully (demo)"


def check_integrity(file):
    return f"{file} integrity OK (demo)"


def block_ip(ip):
    blocked_ips.append(ip)
    return f"{ip} blocked"


def allow_ip(ip):
    if ip in blocked_ips:
        blocked_ips.remove(ip)
    return f"{ip} allowed"


def check_ip(ip):
    if ip in blocked_ips:
        return f"{ip} is BLOCKED"
    return f"{ip} is SAFE"
