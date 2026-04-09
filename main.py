import sqlite3
from cryptography.fernet import Fernet
import os

# ================= DATABASE =================
conn = sqlite3.connect("users.db", check_same_thread=False)
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS users(
    username TEXT,
    password TEXT
)
""")
conn.commit()

# ================= ENCRYPTION =================
if not os.path.exists("key.key"):
    key = Fernet.generate_key()
    open("key.key", "wb").write(key)
else:
    key = open("key.key", "rb").read()

fernet = Fernet(key)

# ================= USERS =================
def register_user(u, p):
    cur.execute("INSERT INTO users VALUES (?, ?)", (u, p))
    conn.commit()
    return "Registered Successfully!"

def login_user(u, p):
    cur.execute("SELECT * FROM users WHERE username=? AND password=?", (u, p))
    if cur.fetchone():
        return True
    return False

# ================= FILE =================
def encrypt_file(filepath):
    with open(filepath, "rb") as f:
        data = f.read()

    encrypted = fernet.encrypt(data)

    with open(filepath + ".enc", "wb") as f:
        f.write(encrypted)

    return "File Encrypted!"

def decrypt_file(filepath):
    with open(filepath, "rb") as f:
        data = f.read()

    decrypted = fernet.decrypt(data)

    new_name = filepath.replace(".enc", "_decrypted.txt")

    with open(new_name, "wb") as f:
        f.write(decrypted)

    return "File Decrypted!"
