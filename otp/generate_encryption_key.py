from cryptography.fernet import Fernet

def generate_fernet_key():
    key = Fernet.generate_key()
    key_string = key.decode('utf-8')
    return key
print(generate_fernet_key())