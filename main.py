from authentication import register_user, login_user
from encryption import encrypt_file, decrypt_file
from firewall import block_ip, allow_ip, check_ip
from integrity import file_hash
from logger import log_event

while True:

    print("\n===== Advanced Cloud Security System =====")
    print("1 Register User")
    print("2 Login")
    print("3 Encrypt File")
    print("4 Decrypt File")
    print("5 Check File Integrity")
    print("6 Block IP")
    print("7 Allow IP")
    print("8 Check IP Access")
    print("9 Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        u = input("Username: ")
        p = input("Password: ")
        print(register_user(u, p))
        log_event("User registered")

    elif choice == "2":
        u = input("Username: ")
        p = input("Password: ")
        print(login_user(u, p))
        log_event("User login attempt")

    elif choice == "3":
        file = input("File name: ")
        print(encrypt_file(file))
        log_event("File encrypted")

    elif choice == "4":
        file = input("Encrypted file: ")
        print(decrypt_file(file))
        log_event("File decrypted")

    elif choice == "5":
        file = input("File name: ")
        print("SHA256:", file_hash(file))

    elif choice == "6":
        ip = input("IP to block: ")
        print(block_ip(ip))

    elif choice == "7":
        ip = input("IP to allow: ")
        print(allow_ip(ip))

    elif choice == "8":
        ip = input("Enter IP: ")
        print(check_ip(ip))

    elif choice == "9":
        break