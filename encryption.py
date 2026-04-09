from cryptography.fernet import Fernet

key = Fernet.generate_key()
cipher = Fernet(key)

def encrypt_file(filename):
    with open(filename, "rb") as f:
        data = f.read()

    encrypted = cipher.encrypt(data)

    with open(filename + ".enc", "wb") as f:
        f.write(encrypted)

    return "File encrypted"

def decrypt_file(filename):
    with open(filename, "rb") as f:
        data = f.read()

    decrypted = cipher.decrypt(data)

    with open("decrypted_" + filename, "wb") as f:
        f.write(decrypted)

    return "File decrypted"