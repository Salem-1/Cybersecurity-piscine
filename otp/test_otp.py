import sys
import time
import os
from cryptography.fernet import Fernet
import pyotp
import base64

def save_key_to_otp_file(key_file, encryption_key):
    key = ""
    with open(key_file, "r") as f:
        key = f.read().strip()
    if len(key) < 64:
        raise ValueError("Please provide at least 64 hexadecimal characters.")
    if key.startswith("0x") or key.startswith("0X"):
        key = key[2:]
    fernet = Fernet(encryption_key.encode('utf-8'))
    encrypted_key = fernet.encrypt(key.encode())
    with open("ft_otp.key", "wb") as f:
        f.write(encrypted_key)

def get_key():
    with open("ft_otp.key", "rb") as f:
        encrypted_key = f.read()
    decryption_key = os.getenv("ENCRYPTION_KEY")
    fernet = Fernet(decryption_key.encode('utf-8'))
    decrypted_key = fernet.decrypt(encrypted_key)
    return base64.b32encode(decrypted_key).decode()  # Assuming key needs to be base32 encoded for TOTP

error_message = """Wrong usage of program! The program works as follows:
./ftp_otp -g [file_with_key]: The program receives as argument a hexadecimal key of at least 64 characters. The program stores this key safely in a file called ft_otp.key, which is encrypted.
./ftp_otp -k ft_otp.key     : The program generates a new temporary password based on the key given as argument and prints it on the standard output"""

options = ["-g", "-k"]
if len(sys.argv) != 3 or sys.argv[1] not in options:
    print(error_message)
    sys.exit(1)

def start_program():
    if sys.argv[1] == "-g":
        try:
            encryption_key = os.getenv("ENCRYPTION_KEY")
            if not encryption_key:
                raise ValueError("ENCRYPTION_KEY environment variable not set")
            save_key_to_otp_file(sys.argv[2], encryption_key)
        except Exception as e:
            print(e)
            print("Please make sure to add your key as hexadecimal chars with length 64 chars at least to your key file")
    elif sys.argv[1] == "-k":
        secret_key = get_key()
        totp = pyotp.TOTP(secret_key)
        print(totp.now())

try:
    start_program()
except Exception as e:
    print(e)
