
from hashlib import sha1
import hmac
import time
import sys
from cryptography.fernet import Fernet
import os



def HOTP(K, C):
	C_bytes = int(C).to_bytes(8, 'big') 
	hashed = hmac.new(K, C_bytes, sha1).digest()
	offset = hashed[-1] & 0x0F
	converted_integer = (hashed[offset] & 0x7F) << 24 | \
						(hashed[offset + 1] & 0xFF) << 16 | \
						(hashed[offset + 2] & 0xFF) << 8  | \
						(hashed[offset + 3] & 0xFF)
	otp = converted_integer % 10 ** 6
	return f"{otp:06d}"  

def save_key_to_otp_file(key_file, encryption_key):
	key = ""
	hexadecimal_chars = "0123456789abcdefABCDEF"
	with open(key_file, "r") as f:
		key = f.read()
	if len(key) < 64:
		raise NameError("Please provide at least 64 hexadecimal key")
	if key[0:2] == "0x" or key[0:2] == "0X":
		key = key[2:]
	fernet = Fernet(encryption_key.encode('utf-8'))
	encrypted_key = fernet.encrypt(key.encode())
	with open("ft_otp.key", "wb") as f:
		f.write(encrypted_key)
	
def get_key():
	with open("ft_otp.key", "rb") as f:
		encryption_key = f.read()
	decryption_key = os.getenv("ENCRYPTION_KEY")
	fernet = Fernet(decryption_key)
	decrypted_data = fernet.decrypt(encryption_key)
	return decrypted_data
	
	  
error_message = """Wrong usage of program! the program works as follows:
./ftp_otp	-g [file_with_key]: The program receives as argument a hexadecimal key of at least 64 characters. The program stores this key safely in a file called ft_otp.key, which is encrypted.
./ftp_otp	-k ft_otp.key	 : The program generates a new temporary password based on the key given as argument and prints it on the standard output"""

options = ["-g", "-k"]
if len(sys.argv) != 3 or sys.argv[1] not in options:
	print(error_message)
	sys.exit(1)


def start_program():
	if sys.argv[1] == "-g":
		try:
			encryption_key =  os.getenv("ENCRYPTION_KEY")
			if encryption_key is None:
				raise NameError("Please remember to correctly export ENCRYPTION_KEY ")
			save_key_to_otp_file(sys.argv[2], encryption_key)
		except Exception as e:
			print(e)
	elif sys.argv[1] == "-k":
		K = get_key()
		C = int(time.time() // 30) 
		print(HOTP(K, C)) 
	   

try:
	  start_program()
except Exception as e:
	print(e)