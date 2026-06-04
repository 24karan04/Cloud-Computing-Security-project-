from cryptography.fernet import Fernet
import os

# ============================================

# KEY FILE NAME

# ============================================

KEY_FILE = "secret.key"

# ============================================

# LOAD OR CREATE ENCRYPTION KEY

# ============================================

def load_key():

```
# Create key if not exists
if not os.path.exists(KEY_FILE):

    key = Fernet.generate_key()

    with open(KEY_FILE, "wb") as key_file:
        key_file.write(key)

    print("New encryption key created")

# Load existing key
with open(KEY_FILE, "rb") as key_file:
    return key_file.read()
```

# ============================================

# INITIALIZE CIPHER

# ============================================

key = load_key()
cipher = Fernet(key)

# ============================================

# ENCRYPT FILE FUNCTION

# ============================================

def encrypt_file(filename):

```
try:

    # Check if file exists
    if not os.path.exists(filename):
        return "Error: File does not exist"

    # Read original file
    with open(filename, "rb") as file:
        file_data = file.read()

    # Encrypt data
    encrypted_data = cipher.encrypt(file_data)

    # Save encrypted file
    encrypted_filename = filename + ".enc"

    with open(encrypted_filename, "wb") as file:
        file.write(encrypted_data)

    return f"File encrypted successfully: {encrypted_filename}"

except Exception as e:
    return f"Encryption Error: {str(e)}"
```

# ============================================

# DECRYPT FILE FUNCTION

# ============================================

def decrypt_file(filename):

```
try:

    # Check if file exists
    if not os.path.exists(filename):
        return "Error: File does not exist"

    # Read encrypted file
    with open(filename, "rb") as file:
        encrypted_data = file.read()

    # Decrypt data
    decrypted_data = cipher.decrypt(encrypted_data)

    # Remove .enc extension if exists
    if filename.endswith(".enc"):
        output_filename = filename[:-4]
    else:
        output_filename = "decrypted_" + filename

    # Save decrypted file
    decrypted_filename = "decrypted_" + output_filename

    with open(decrypted_filename, "wb") as file:
        file.write(decrypted_data)

    return f"File decrypted successfully: {decrypted_filename}"

except Exception as e:
    return f"Decryption Error: {str(e)}"
```

# ============================================

# TESTING MENU

# ============================================

if **name** == "**main**":

```
while True:

    print("\n========== FILE ENCRYPTION SYSTEM ==========")
    print("1. Encrypt File")
    print("2. Decrypt File")
    print("3. Exit")

    choice = input("Enter your choice: ")

    # Encrypt option
    if choice == "1":

        filename = input("Enter file name to encrypt: ")

        result = encrypt_file(filename)

        print(result)

    # Decrypt option
    elif choice == "2":

        filename = input("Enter encrypted file name: ")

        result = decrypt_file(filename)

        print(result)

    # Exit option
    elif choice == "3":

        print("Exiting program...")
        break

    else:
        print("Invalid choice")
```
